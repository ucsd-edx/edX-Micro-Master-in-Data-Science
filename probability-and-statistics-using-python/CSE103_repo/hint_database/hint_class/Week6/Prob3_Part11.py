class Prob3_Part11:
    """
    Author: Liu Han
    Edit: Zhen Zhai
    Date: 10/31/2016
    """

    def check_attempt(self, params):
        # unpack params
        self.attempt = params['attempt']  # student's attempt
        self.answer = params['answer']  # solution
        self.att_tree = params['att_tree']  # attempt tree
        self.ans_tree = params['ans_tree']  # solution tree

        hint = ''

        try:
            hint = 'E[X+Y]=E[X]+E[Y], for random variables X and Y. '

            if len(hint) > 0:
                return hint + 'Suppose E[X] = 1/3, and E[Y] = 1/3; What is E[X+Y]?', '2/3'
            else:
                return '', ''

        except Exception:

            return '', ''

    def get_problems(self):
        self.problem_list = ["Covariance/ContingencyTables5/part11"]
        return self.problem_list