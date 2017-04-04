from hint_class_helpers.find_matches import find_matches

class Prob5_Part4:
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
                    hint='To solve for k, express k in terms of expectation, which value you have from previous part.'
            if len(hint)>0:
                return hint ,'What is the bound for variable Y to have more than 5 if mean of Y, or E(Y) is 5/2 ?','5/(5/2)'
            else:
                return '',''

        except Exception:
            return '',''

    def get_problems(self):
        self.problem_list = [ "MarkovChebyshev/RiggedDice/part4" ]
        return self.problem_list
