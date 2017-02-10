import BaseHTTPServer

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn
import threading
import urllib

import json
import os
import subprocess
import time
import random

import gc
from bs4 import BeautifulSoup as bs


# Random file name generator
def randgen():
    return str(random.random()).split('.')[-1]+'_'+str('%.6f' % time.time()).split('.')[-1]


class Handler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        pass

    def do_GET(self):
        pass

    def do_POST(self):
        body_len = int(self.headers.getheader('content-length', 0))
        body_content = self.rfile.read(body_len)
        problem, student_response = get_info(body_content)
        result = grade(problem, student_response)
	print result
        self.send_response(200)
        self.end_headers()
        self.wfile.write(result)


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """ This class allows to handle requests in separated threads.
        No further content needed, don't touch this. """


class HTTPHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_POST(self):
        body_len = int(self.headers.getheader('content-length', 0))
        body_content = self.rfile.read(body_len)
        problem_name, student_response = get_info(body_content)
        result = grade(problem_name, student_response)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(result)


def grade(problem, student_response):
    #TODO: error handling, problem specification, unique student name
    randfilename = randgen()
    grading_dir = 'submitted/hacker/ps1/'
    feedback_html = 'feedback/hacker/ps1/problem1.html'

    # Create python file to be tested from student's submitted program
    program_name = "problem1.ipynb"
    try:
        with open(grading_dir + program_name,'w') as f:
            for l in urllib.urlopen(student_response):
                f.write(l)
    except:
        return json.dumps({'msg':'invalid link', 'correct':None, 'score':None})
    p = subprocess.Popen(["nbgrader", "autograde", "ps1", "--student", "hacker"],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()

    print "Out is: >>>\n{0}\n<<<".format(out)
    print "Err is: >>>\n{0}\n<<<".format(err)
    # os.system('nbgrader autograde ps1 --student hacker')
    if 'AutogradeApp | ERROR' not in err:
        os.system('nbgrader feedback ps1 --student hacker')
    else:
        return json.dumps({'msg':'There is some problem during grading', 'correct':None, 'score':None})

    with open(feedback_html, 'r') as f:
        soup = bs(''.join(f.readlines()), 'html.parser')
    report = soup.body.div.div.div
    report = [line.strip() for line in report.prettify().split('\n') if line and not line.strip().startswith('<')]
    report = [l for l in report if not l.startswith('Comment')]  # We are not going to provide manual comment

    #remove student's program from disk
    os.remove(grading_dir + program_name)
    os.remove(feedback_html)
    
    score = float(report[0].split(' ')[-3])
    correct = score > 0
    msg = '\n'.join(report)
    #garbage collect
    gc.collect()
    return json.dumps({'correct': correct, 'score': score, 'msg': msg})
    
    
def process_result(result):
    #TODO: error handling
    pass


def get_info(body_content):
    # print body_content
    json_object = json.loads(body_content)
    json_object = json.loads(json_object["xqueue_body"])
    problem = json.loads(json_object["grader_payload"])
    student_response = json_object["student_response"]
    return problem, student_response


if __name__ == '__main__':
    server = ThreadedHTTPServer(('localhost', 1710), Handler)
    print 'Starting server on port 1710...'
    server.serve_forever()
