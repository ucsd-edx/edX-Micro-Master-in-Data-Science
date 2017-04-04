# Make sure you name your file with className.py
from hint_class_helpers.find_matches import find_matches

class Prob7_Part3:
    """
    Author: Shen Ting Ang
    Date: 10/13/2016
    """
    def check_attempt(self, params):
        self.attempt = params['attempt'] #student's attempt
        self.answer = params['answer'] #solution
        self.att_tree = params['att_tree'] #attempt tree
        self.ans_tree = params['ans_tree'] #solution tree
        matches = find_matches(params)
        matching_node = [m[0] for m in matches]

        try:
            if '^' in self.attempt:
                hint='This problem does not involve the power function (^).'
                return hint + 'How many cards do we have to choose? ', '5'
            #check if the form of the parse tree has the right
            #shape: an operator and two leafs that correspond to
            #the operands
            elif '+' in self.attempt:
                hint='Are you sure addition is the correct operator? '
                return hint + 'If a poker hand contains at least one royal card, how many non-royal cards can there be at most?', '4'
            elif '-' not in self.attempt:
                hint = 'You might have to remove cases.'
                return hint + 'If a poker hand contains at least one royal card, how many non-royal cards can there be at most?', '4'
            elif 'C(' not in self.attempt and '!' not in self.attempt:
                hint='Missing choose function in the answer. '
                return hint + 'How many possible ways are there to get 5 cards correct out of 32? C(_,5)', '32'

            else:
                return "",""

        except Exception:
            return '',''
    def get_problems(self):
        self.problem_list = ["PokerConditional/poker_cond5_1/part3"]
        return self.problem_list
