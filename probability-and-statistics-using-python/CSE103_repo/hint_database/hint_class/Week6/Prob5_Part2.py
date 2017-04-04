from hint_class_helpers.find_matches import find_matches

class Prob5_Part2:
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
                if 'R.1' not in m:
                    hint='Since the dice is biased, use linearity of expectation to calculate the expectation for each outcome separately'
                if 'R.0' not in m:
                    hint='Since the dice is biased, use linearity of expectation to calculate the expectation for each outcome separately'
            if len(hint)>0:
                return hint+ 'What is the expectation of number of heads coin flips where P(head)=3/4?','0*(1/4) + 1*(3/4)'
            else:
                return '',''

        except Exception:
            return '',''

    def get_problems(self):
        self.problem_list = [ "MarkovChebyshev/RiggedDice/part2" ]
        return self.problem_list
