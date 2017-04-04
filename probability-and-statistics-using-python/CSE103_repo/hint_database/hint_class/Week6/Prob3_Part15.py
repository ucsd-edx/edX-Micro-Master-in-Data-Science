class Prob3_Part15:
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
            return hint + 'Corr(X,Y) ranges from -1 to 1,and if Corr(X,Y) = 0, X and Y are independent' \
                          '(uncorrelated). Otherwise, X and Y are correlated. Suppose Corr(x,y)=1/3. Are X ' \
                          'and Y are correlated(1=YES,0=NO)?', '1'

        except Exception:

            return '', ''

    def get_problems(self):
        self.problem_list = ["Covariance/ContingencyTables5/part15"]
        return self.problem_list