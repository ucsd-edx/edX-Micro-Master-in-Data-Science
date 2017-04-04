class Prob3_Part14:
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
            hint = 'Corr(X,Y)=Cov(X,Y)/[Var(X)*Var(Y)]^(1/2). According to the previous parts, you know ' \
                   'Cov(X,Y), Var(X), Var(Y). You can calculate Corr(X,Y) based on those answers.'

            if len(hint) > 0:
                return hint + ' Suppose Cov(x,y)=1/3, Var(Y)=1/3, Var(X)=1/3. What is Corr(X,Y)?', '1'
            else:
                return '', ''

        except Exception:

            return '', ''

    def get_problems(self):
        self.problem_list = ["Covariance/ContingencyTables5/part14"]
        return self.problem_list