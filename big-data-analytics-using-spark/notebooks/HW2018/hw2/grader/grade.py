import sys
from spark_grader import SparkGrader


grader = SparkGrader('/app')


if __name__ == "__main__":
    section_name, problem_name, submission_url = sys.argv[1], sys.argv[2], sys.argv[3]
    grader.grade(section_name, submission_url, problem_name)
