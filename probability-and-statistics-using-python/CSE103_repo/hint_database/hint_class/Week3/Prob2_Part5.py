# Make sure you name your file with className.py
from hint_class_helpers.find_matches import find_matches

class Prob2_Part5:
    """
    Author: Shen Ting Ang
    Date: 10/11/2016
    """
    def check_attempt(self, params):
        self.attempt = params['attempt'] #student's attempt
        self.answer = params['answer'] #solution
        self.att_tree = params['att_tree'] #attempt tree
        self.ans_tree = params['ans_tree'] #solution tree
        matches = find_matches(params)
        matching_node = [m[0] for m in matches]

        try:
            if '^' not in self.attempt:
                hint='Missing ^ in the answer. '
                return hint + 'What is the probability of a specific combination of 3 coin flips? ', '1/2^3'
            #check if the form of the parse tree has the right
            #shape: an operator and two leafs that correspond to
            #the operands

            elif 'C(' not in self.attempt and '!' not in self.attempt:
                hint='Missing choose function in the answer. '
                return hint + 'How many possible ways are there to get 2 questions correct out of 5 questions? C(5,_)', '2'
            elif '+' not in self.attempt:
                hint='Missing + in the answer. '
                return hint + 'How many possible scenarios are there for a student to get at most 2 questions wrong?', '3'
            elif '1-' not in self.attempt:
                hint='The answer might be best obtained using complements. '
                return hint + 'The opposite of getting at most 2 questions wrong is getting at least _ questions wrong.', '3'

            else:
                return "",""

        except Exception:
            return '',''
    def get_problems(self):
        self.problem_list = ["Combinatorics/GrinsteadSnell3.2.18/part5"]
        return self.problem_list
