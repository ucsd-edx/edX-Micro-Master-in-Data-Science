class Prob3_Part3:
    """
    Author: Liu Han
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
            if not '+' in self.attempt:
                hint = 'Should P(X=3) equal to the sum of probabilities of all cases when X = 3?'

            if len(hint) > 0:
                return hint + 'Suppose P(X = 3|Y = 1) = 1/3, and P(X = 3|Y = 2) = 1/3 (Note: The value ' \
                              'of Y can only be 1 or 2); What is P(X = 3)?', '2/3'
            else:
                return '', ''

        except Exception:

            return '', ''

    def get_problems(self):
        self.problem_list = ["Covariance/ContingencyTables5/part3"]
        return self.problem_list