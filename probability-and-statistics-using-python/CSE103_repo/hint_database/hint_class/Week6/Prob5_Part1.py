from hint_class_helpers.find_matches import find_matches

class Prob5_Part1:
    """
    Author: <Tony Salim>
    Date: <11-1-2016>
    """

    def check_attempt(self, params):
        self.attempt = params['attempt'] #student's attempt
        self.answer = params['answer'] #solution
        self.att_tree = params['att_tree'] #attempt tree
        self.ans_tree = params['ans_tree'] #solution tree

        matches = find_matches(params)
        matching_node = [m[0] for m in matches]

        try:
            for m in matching_node:
                if 'R.1' in m:
                    hint='When probability is twice as high, its 2 times the original. '
                if 'R.1.0' in m:
                    hint='Remember that the sum formula from 1 to n is  n(n+1)/2. '
            if len(hint)>0:
                return hint+ ' What is the sum from 1 to 5','5(5+1)/2'
            else:
                return '',''

        except Exception:
            return '',''

    def get_problems(self):
        self.problem_list = [ "MarkovChebyshev/RiggedDice/part1" ]
        return self.problem_list
