class Prob3_Part8:
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
            hint = 'The two random variables are identically distributed if each random variable ' \
                   'has the same probability distribution as the others and is mutually independent'

            if len(hint) > 0:
                return hint + 'Suppose you know P(X=1) = 1/3, P(X=2) = 0, P(Y=1) = 1/3, and P(Y=2) = 0;' \
                              'Are X and Y identically distributed?(0=no, 1=yes)', '1'
            else:
                return '', ''

        except Exception:

            return '', ''

    def get_problems(self):
        self.problem_list = ["Covariance/ContingencyTables5/part8"]
        return self.problem_list