from time import sleep

import json
import os
import shutil
import subprocess
import urllib
import yaml
import time
import requests
import codecs
import re
from xqueue_watcher.grader import Grader
from threading import Timer

html_header = '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /><br/>'

class SparkGrader(Grader):
    def __init__(self, grader_root='/home/ubuntu/app', fork_per_item=True, logger_name=__name__):
        """
        grader object
        :param grader_root: course directory
        """
        super(SparkGrader, self).__init__(grader_root=grader_root, fork_per_item=fork_per_item, logger_name=logger_name)
        self.grader_root = grader_root
        self.course_dir = os.path.join(grader_root, 'dummy-course')
        SparkGrader._create_dir(self.course_dir)
        with open("spark-grader.yml") as f:
            self.config = yaml.load(f.read())

    @staticmethod
    def _handle_result(success, **kwargs):
        if not success:
            print(json.dumps(kwargs))
        kwargs.update({'tests':'', 'errors':''})
        return kwargs

    @staticmethod
    def _create_dir(directory):
        if not os.path.exists(directory):
            os.makedirs(directory)

    def _download(self, submission_url, notebook_path):
        try:
            print("Downloading")
            response = requests.get(submission_url, stream=True)
            with open(notebook_path, 'wb') as f:
                #for l in urllib.urlopen(submission_url):
                for block in response.iter_content(1024):
                    f.write(block)
            print("Downloaded")
        except Exception as err:
            self._clean()
            return SparkGrader._handle_result(False, msg="<br/>".join(str(err).split("\n")), correct=False, score=0)
        return None

    def _convert(self, notebook_path, python_file_path):
        # IF students are submitting Jupyter notebooks
            # try:
            #     subprocess.run(["jupyter", "nbconvert", "--to", "python", notebook_path], check=True)
            # except subprocess.CalledProcessError as err:
            #     self._clean()
            #     return SparkGrader._handle_result(False, msg=str(err), correct=False, score=0)
        # ELSE IF students are submitting Python files
        content = []
        with open(notebook_path) as f_in:
            for line in f_in:
                if "SparkContext(" in line and not line.strip().startswith("#"):
                    if "SparkContext()" not in line:
                        self._clean()
                        err = "Do not change SparkContext object. You should use default initialization as provided in the notebook. \
                        i.e. sc = SparkContext()<br/><br/>"
                        return SparkGrader._handle_result(False, msg="<br/>".join(str(err).split("\n")), correct=False, score=0)
                content.append(line)
        content = ''.join(content)
        g = open(python_file_path,'w')
        g.write(content)
        g.close()
        return None

    def _compile(self, python_file_path):
        try:
            #subprocess.run(["python", "-m", "py_compile", python_file_path], check=True)
            compile_output = subprocess.check_output(["python3", "-m", "py_compile", python_file_path], stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as err:
            self._clean()
            #return SparkGrader._handle_result(False, msg="<br/>".join(str(err).split("\n"))+"<br/><br/>" , correct=False, score=0)
            return SparkGrader._handle_result(False, msg="<br/>Compilation Failed!<br/>" + "<br/>".join(str(err.output).split("\n"))+"<br/><br/>" , correct=False, score=0)
        return None
    
    def _submit(self, python_file_path, problem_name, student_id):
        def get_master_url():
            while True:
                for url in self.config["server"]:
                    api = "http://{}:8088/ws/v1/cluster/metrics".format(url)
                    if requests.get(api).json()['clusterMetrics']['appsRunning']:
                        continue
                    return url
                sleep(5)
        def _kill_func(container, flag):
            container.terminate()
                #kill yarn
            flag[0] = True
            q = subprocess.Popen(
                    ["ssh", "hadoop@" + master_url,
                     "/bin/bash", "kill_job.sh"])
            
        def _run(cmd, timeout_sec):
            proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, 
                                    stderr=subprocess.PIPE)
            
            timed_out = [False]
            
            timer = Timer(timeout_sec, _kill_func, [proc, timed_out])
            
            try:
                stdout, stderr = '', ''
                timer.start()
                stdout,stderr = proc.communicate()
            #    stdout = stdout.decode(encoding='utf-8')
            #except UnicodeEncodingError:
            #    stdout = 'Could not decode'
            #    print(e)
            #    print('--'*10+'\n\n\n')
            finally:
                timer.cancel()
            return stdout, stderr, timed_out[0]

        master_url = get_master_url()
        python_file_name = python_file_path.rsplit("/", 1)[1]
        timeout = self.config["timeout"][problem_name]

        try:
            #subprocess.run(
            subprocess.check_output(
                ["scp",
                 "submitted/hw2-files.txt",
                 python_file_path,
                 "hadoop@{}:~".format(master_url)],
                #check=True
            )
            print('Copied python file')
            #completed = subprocess.run(
            
            #p = subprocess.Popen(
            #    ["ssh", "hadoop@" + master_url,
            #     "spark-submit",
            #     "--master", "yarn",
            #     "--files", "./hw2-files.txt",
            #     "--name", "hacker",
            #     "./" + python_file_name],
            #    stderr=subprocess.PIPE,
            #    stdout=subprocess.PIPE,
                #stderr=subprocess.PIPE,
                #timeout=timeout,
                #check=True
            #)
            submit_cmd = ["ssh", "hadoop@" + master_url, "spark-submit",
                 "--master", "yarn",
                 "--files", "./hw2-files.txt",
                 "--name", "hacker",
                 "./" + python_file_name]
            start_time = time.time()
            proc_output, proc_error, timed_out = _run(submit_cmd, timeout)
            #while (time.time() - start <= timeout) and p.poll() is None:
                #sleep(1)
            #    continue
            #print(p.poll())
            #exit_code = p.returncode
            end_time = time.time()
            if timed_out:
            #    p.terminate()
                #kill yarn
            #    q = subprocess.Popen(
            #        ["ssh", "hadoop@" + master_url,
            #         "/bin/bash", "kill_job.sh"])
                return ("TIME_OUT. Time limit is " + str(timeout) + " seconds", "", "","")
            exit_code = 0
            if exit_code != 0:
                raise subprocess.CalledProcessError(exit_code, exit_code,p.stderr.read())
                
            #read output and errors from ssh process
            #proc_output, proc_error = proc.communicate()
        except subprocess.CalledProcessError as err:
            return ("ERROR: {}".format(err), "", "","")
        #except subprocess.TimeoutExpired:
        #    return ("TIME_OUT", "", "")
        #with open("/home/ubuntu/docker/CSE255_18_HW2/ClusterOutput/{}_out.html".format(student_id), 'w') as f:
        #    f.write("<br/>".join(proc_output.split("\n")))
        
        with open("/home/ubuntu/docker/CSE255_18_HW2/ClusterOutput/{}_{}_out.html".format(student_id, problem_name), 'wb') as f:
            f.write(html_header + "<br/>".join(proc_output.split("\n")))
        out_msg = "Link to output_file: <a href='http://54.160.232.161:8080/" + student_id  + "_"+ problem_name + "_out.html' target=_blank>Output</a><br/><br/>"
        with open("/home/ubuntu/docker/CSE255_18_HW2/ClusterOutput/{}_{}_err.html".format(student_id, problem_name), 'wb') as f:
            f.write(html_header + "<br/>".join(proc_error.split("\n")))
        error_msg = "Link to errors_file: <a href='http://54.160.232.161:8080/" + student_id + "_"+ problem_name + "_err.html' target=_blank>Error</a><br/><br/>"
        return ("OK", out_msg, error_msg, end_time-start_time)
        #return ("OK", output.decode(), "")



    def _clean(self):
        for dir_name in ['submitted']:
            dir_path = os.path.join(self.course_dir, dir_name)
            if os.path.isdir(dir_path):
                shutil.rmtree(dir_path)
        os.chdir("/home/ubuntu/edX-extensions/edX-nbgrader/xqueue-watcher")
    
    def _score(self, student_id, answer, time_taken, problem_name):
        def score_time(time_taken):
            timeout = self.config["timeout"][problem_name]
            best_time = self.config["besttime"][problem_name]
            max_score = self.config["score"][problem_name]
            time_range = timeout - best_time
            values = [x for x in xrange(best_time, timeout, int(time_range/6))]
            values.append(timeout)
            factor = max_score/10
            for x in values[1:]:
                if time_taken <= x:
                    return max_score
                else:
                    max_score -= 2*factor
            return 0
        def _grade(student_id, answer):
            f = codecs.open("/home/ubuntu/docker/CSE255_18_HW2/ClusterOutput/{}_{}_out.html".format(student_id, problem_name), 'r','utf-8')
            output = f.read()
            output = output.split(html_header)[1]
            output = [line.strip() for line in output.split('<br/>') if line.strip()]
            idx = 0
            for line in answer.split('\n'):
                line = line.strip()
                if not line:
                    continue
                if idx >= len(output):
                    return False, (line, "")
                if line != output[idx]:
                    return False, (line, output[idx])
                idx += 1
            return True, ('','')
        match, lines = _grade(student_id, answer)
        return score_time(time_taken) * match, lines
    
    #def grade(self, section_name, submission_url, problem_name, student_id):
    def grade(self, payload, files, _, student_id):
        section_name, problem_name = payload.split('/')
        files = json.loads(files)
        submission_url = files.values()[0]
        # if section_name != 'ps1':
        #     return SimpleGrader._handle_result(False, msg='Wrong section name.', correct=correct, score=score)
        
        with open(self.config["input-files"][problem_name]) as f:
            print("Some shit is happening")
            files_list = f.read()
        with codecs.open(self.config["solution"][problem_name],'r','utf-8') as f:
            answer = f.read()

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
        ret = self._convert(notebook_path, python_file_path)
        
        if ret is not None:
            return ret
        shutil.copy(python_file_path, "/home/ubuntu/docker/CSE255_18_HW2/UploadedHomework/{}_{}.py".format(student_id, problem_name))
        # compile the python file
        ret = self._compile(python_file_path)
        if ret is not None:
            return ret

        # submit
        res, stdout, stderr, time_taken = self._submit(python_file_path, problem_name, student_id)
        #stderr = "<br/>".join(stderr.split("\n"))
        if res != "OK":
            result = res
            score = 0
        else:
            score, error_lines = self._score(student_id, answer, time_taken, problem_name)
            if score:
            # grade
                result = "match" 
            else:
                result = "NOT match. Atleast one error was found in your output. At the point of the first error,<br/> We expected: <br/><b>" + error_lines[0] + "</b><br/><br/>You returned: <br/><b>"+ error_lines[1] + "</b><br/><br/>"
        #stdout = "<br/>".join(stdout.split("\n"))
        self._clean()
        ret = {
            'correct': score > 0,
            'score': score,
            'msg': "Your code executed in" + str(time_taken) +"seconds.<br/>Result: " + result + "<br/><br/>STDOUT:<br/>" + stdout + "<br/><br/>STDERR:<br/>" + stderr + "<br/><br/>",
            'tests': '',
            'errors': ''
        }
        print(json.dumps(ret))
        return ret


if __name__ == '__main__':
    test = SparkGrader('/home/arapat/Downloads')
    test.grade('ps1', 'http://localhost:8000/HW-2_sol.ipynb', 'twitter-10mb')
