class Prob3_Part13:
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
            hint = 'Cov(X,Y) = E[XY]-E[X]*E[Y]. According to the previous parts, you know E[XY],E[X],and E[Y]. ' \
                   'You can calculate Cov(X,Y) based on those answers.'

            if len(hint) > 0:
                return hint + ' Suppose E[X]=1/3, E[Y]=1/3, E[XY]=1/6. What is Cov(X,Y)?', '1/18'
            else:
                return '', ''

        except Exception:

            return '', ''

    def get_problems(self):
        self.problem_list = ["Covariance/ContingencyTables5/part13"]
        return self.problem_list