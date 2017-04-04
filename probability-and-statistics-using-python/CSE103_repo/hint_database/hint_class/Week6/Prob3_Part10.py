class Prob3_Part10:
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
            hint = 'E[X] = x1*p1 + x2*p2 + ... + xk*pk, where pk is the probability associated with xk'

            if len(hint) > 0:
                return hint + 'From the previous parts, you know the values of P(Y=1),P(Y=2),and P(Y=3);' \
                              ' Should the E[Y] = 1*P(Y=1)+2*P(Y=2)+3*P(Y=3)? (1=YES,0=NO)', '1'
            else:
                return '', ''

        except Exception:

            return '', ''

    def get_problems(self):
        self.problem_list = ["Covariance/ContingencyTables5/part10"]
        return self.problem_list