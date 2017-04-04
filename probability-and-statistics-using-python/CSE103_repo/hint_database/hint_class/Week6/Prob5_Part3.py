from hint_class_helpers.find_matches import find_matches

class Prob5_Part3:
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
                if ('R.0' not in m) or ('R.1' not in m):
                    hint='Are the two dice dependent or not? What does that say about linearity of expectation.'
            if len(hint)>0:
                return hint ,'What is E(X + Y), where X and Y are independent random variable. E(X)=1 and E(Y)=2?','1+2'
            else:
                return '',''

        except Exception:
            return '',''

    def get_problems(self):
        self.problem_list = [ "MarkovChebyshev/RiggedDice/part3" ]
        return self.problem_list
