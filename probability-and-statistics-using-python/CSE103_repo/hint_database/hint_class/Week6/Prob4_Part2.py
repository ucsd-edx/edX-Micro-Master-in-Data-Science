# Make sure you name your file with className.py
from hint_class_helpers.find_matches import find_matches

class Prob4_Part2:
    """
    Author: Shen Ting Ang
    Date: 10/31/2016
    """
    def check_attempt(self, params):
        self.attempt = params['attempt'] #student's attempt
        self.answer = params['answer'] #solution
        self.att_tree = params['att_tree'] #attempt tree
        self.ans_tree = params['ans_tree'] #solution tree
        matches = find_matches(params)
        matching_node = [m[0] for m in matches]

        try:
            return "What is E(X) in terms of N if the coin is unbiased and fair? ___ * N","0.5"

        except Exception:
            return '',''
    def get_problems(self):
        self.problem_list = ["MarkovChebyshev/MarkovInequality/part2"]
        return self.problem_list