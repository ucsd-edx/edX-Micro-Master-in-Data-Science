# Make sure you name your file with className.py
from hint_class_helpers.find_matches import find_matches

class Prob6_Part11:
    """
    Author: Shen Ting Ang
    Date: 11/7/2016
    """
    def check_attempt(self, params):
        self.attempt = params['attempt'] #student's attempt
        self.answer = params['answer'] #solution
        self.att_tree = params['att_tree'] #attempt tree
        self.ans_tree = params['ans_tree'] #solution tree
        matches = find_matches(params)
        matching_node = [m[0] for m in matches]

        try:
            hint = 'Recall the formula to find the expected value of E(XY) when X and Y are independent.'
            return hint + ' If the probability that X and Y happen is 1/2, X has the value 4, and Y has the value 6, what is the E(XY)?', '6'

        except Exception:
            return '',''
    def get_problems(self):
        self.problem_list = ["ExpectationVariance/cov_dep_uncor.imd"]
        return self.problem_list