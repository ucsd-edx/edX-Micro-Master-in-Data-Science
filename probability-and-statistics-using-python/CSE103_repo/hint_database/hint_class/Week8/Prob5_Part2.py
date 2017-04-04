# Make sure you name your file with className.py
from hint_class_helpers.find_matches import find_matches

class Prob5_Part2:
    """
    Author: Shen Ting Ang
    Date: 11/14/2016
    """
    def check_attempt(self, params):
        self.attempt = params['attempt'] #student's attempt
        self.answer = params['answer'] #solution
        self.att_tree = params['att_tree'] #attempt tree
        self.ans_tree = params['ans_tree'] #solution tree
        matches = find_matches(params)
        matching_node = [m[0] for m in matches]

        try:
            return 'How many customers are served on average in 10 minutes if the average checkout time is 5 minutes? ', '2'

        except Exception:
            return '',''
    def get_problems(self):
        self.problem_list = ["ExponentialPoisson/stat212.imd"]
        return self.problem_list