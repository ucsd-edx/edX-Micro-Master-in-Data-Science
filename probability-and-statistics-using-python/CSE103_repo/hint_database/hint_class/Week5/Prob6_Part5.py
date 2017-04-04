# Make sure you name your file with className.py
from hint_class_helpers.find_matches import find_matches

class Prob6_Part5:
    """
    Author: Shen Ting Ang
    Date: 10/24/2016
    """
    def check_attempt(self, params):
        self.attempt = params['attempt'] #student's attempt
        self.answer = params['answer'] #solution
        self.att_tree = params['att_tree'] #attempt tree
        self.ans_tree = params['ans_tree'] #solution tree
        matches = find_matches(params)
        matching_node = [m[0] for m in matches]

        try:
            return "What is the sum of (X-u)^2?","10"

        except Exception:
            return '',''
    def get_problems(self):
        self.problem_list = ["ExpectationVariance/Notes3_5_2/part5"]
        return self.problem_list