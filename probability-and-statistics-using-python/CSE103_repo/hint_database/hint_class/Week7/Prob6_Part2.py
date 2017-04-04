# Make sure you name your file with className.py
from hint_class_helpers.find_matches import find_matches

class Prob6_Part2:
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
            hint = 'The marginal distribution of X is the sum of all Y values.'
            return hint + ' If P(Y=1,X=2) = P(Y=2,X=2) = P(Y=3,X=2) = 0.1, what is P(X=2)?', '0.3'

        except Exception:
            return '',''
    def get_problems(self):
        self.problem_list = ["ExpectationVariance/cov_dep_uncor.imd"]
        return self.problem_list