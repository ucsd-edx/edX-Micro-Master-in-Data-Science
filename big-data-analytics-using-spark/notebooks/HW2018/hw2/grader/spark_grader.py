from time import sleep

import json
import os
import shutil
import subprocess
import urllib
import yaml
import requests


class SparkGrader:
    def __init__(self, grader_root='/app'):
        """
        grader object
        :param grader_root: course directory
        """
        self.grader_root = grader_root
        self.course_dir = os.path.join(grader_root, 'dummy-course')
        SparkGrader._create_dir(self.course_dir)
        with open("spark-grader.yml") as f:
            self.config = yaml.load(f.read())

    @staticmethod
    def _handle_result(success, **kwargs):
        if not success:
            print(json.dumps(kwargs))
        return kwargs

    @staticmethod
    def _create_dir(directory):
        if not os.path.exists(directory):
            os.makedirs(directory)

    def _download(self, submission_url, notebook_path):
        try:
            with open(notebook_path, 'w') as f:
                for l in urllib.request.urlopen(submission_url):
                    f.write(l.decode("utf-8"))
        except Exception as err:
            self._clean()
            return SparkGrader._handle_result(False, msg=str(err), correct=False, score=0)
        return None

    def _convert(self, notebook_path):
        try:
            subprocess.run(["jupyter", "nbconvert", "--to", "python", notebook_path], check=True)
        except subprocess.CalledProcessError as err:
            self._clean()
            return SparkGrader._handle_result(False, msg=str(err), correct=False, score=0)
        return None

    def _compile(self, python_file_path):
        try:
            subprocess.run(["python", "-m", "py_compile", python_file_path], check=True)
        except subprocess.CalledProcessError as err:
            self._clean()
            return SparkGrader._handle_result(False, msg=str(err), correct=False, score=0)
        return None

    def _submit(self, python_file_path, problem_name):
        def get_master_url():
            while True:
                for url in self.config["server"]:
                    api = "http://{}:18080/api/v1/applications?status=running".format(url)
                    if requests.get(api).json():
                        continue
                    return "spark://{}:7077".format(url)
                sleep(5)

        spark_submit = os.path.join(self.config["spark"]["path"], "bin/spark-submit")
        master_url = get_master_url()
        timeout = self.config["timeout"][problem_name]

        try:
            completed = subprocess.run(
                [spark_submit, "--master", master_url,
                 "--files", "submitted/hw2-files.txt",
                 "--name", "hacker",
                 python_file_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=timeout,
                check=True
            )
        except subprocess.CalledProcessError as err:
            return ("ERROR: {}".format(err), "", "")
        except subprocess.TimeoutExpired:
            return ("TIME_OUT", "", "")
        return ("OK", completed.stdout, completed.stderr)

    def _grade(self, output, problem_name):
        output = [line.strip() for line in output.split('\n') if line.strip()]
        with open(self.config["solution"][problem_name]) as f:
            idx = 0
            for line in f:
                line = line.strip()
                if not line:
                    continue
                if line != output[idx]:
                    return False
                idx += 1
        return True

    def _clean(self):
        for dir_name in ['submitted']:
            dir_path = os.path.join(self.course_dir, dir_name)
            if os.path.isdir(dir_path):
                shutil.rmtree(dir_path)

    def grade(self, section_name, submission_url, problem_name):
        # if section_name != 'ps1':
        #     return SimpleGrader._handle_result(False, msg='Wrong section name.', correct=correct, score=score)

        with open(self.config["input-files"][problem_name]) as f:
            files_list = f.read()

        os.chdir(self.course_dir)

        # Create working dir
        grading_dir = 'submitted/hacker/{}/'.format(section_name)
        SparkGrader._create_dir(grading_dir)
        with open("submitted/hw2-files.txt", "w") as f:
            f.write(files_list)

        notebook_name = '{}.ipynb'.format(problem_name)
        notebook_path = os.path.join(grading_dir, notebook_name)
        python_file_name = '{}.py'.format(problem_name)
        python_file_path = os.path.join(grading_dir, python_file_name)

        # Download notebook
        ret = self._download(submission_url, notebook_path)
        if ret is not None:
            return ret

        # convert to python file
        ret = self._convert(notebook_path)
        if ret is not None:
            return ret

        # compile the python file
        ret = self._compile(python_file_path)
        if ret is not None:
            return ret

        # submit
        res, stdout, stderr = self._submit(python_file_path, problem_name)
        if res != "OK":
            result = res
            score = 0
        elif self._grade(stdout, problem_name): 
            # grade
            result = "match"
            score = 10
        else:
            result = "NOT match"
            score = 0

        self._clean()
        ret = {
            'correct': score > 0,
            'score': score,
            'msg': "Result: {}\nSTDOUT:\n{}\nSTDERR:\n{}\n".format(result, stdout, stderr)
        }
        print(json.dumps(ret))
        return ret


if __name__ == '__main__':
    test = SparkGrader('/home/arapat/Downloads')
    test.grade('ps1', 'http://localhost:8000/HW-2_sol.ipynb', 'twitter-10mb')
