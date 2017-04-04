class Prob3_Part7:
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
            hint = 'For independence, you need to make sure P(X=x,Y=y)=P(X=x)P(Y=y).'

            if len(hint) > 0:
                return hint + 'Suppose you know that P(X=1,Y=1) = 1/6, P(X=1) = 1/2, and P(Y=1) = 1/3;' \
                              'Is X and Y independent for this specific case?(1=yes,0=no)', '1'
            else:
                return '', ''

        except Exception:

            return '', ''

    def get_problems(self):
        self.problem_list = ["Covariance/ContingencyTables5/part7"]
        return self.problem_list