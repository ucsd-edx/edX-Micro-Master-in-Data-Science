class Prob3_Part12:
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
            hint = 'E[XY]=E[X]*E[Y] only if X and Y are two independent random variables.'

            if len(hint) > 0:
                return hint + ' If X and Y are two dependent random variables,when you calculate E[XY], ' \
                              'should you apply the formula E[XY]=E[X]*E[Y](1=YES,0=NO)', '0'
            else:
                return '', ''

        except Exception:

            return '', ''

    def get_problems(self):
        self.problem_list = ["Covariance/ContingencyTables5/part12"]
        return self.problem_list