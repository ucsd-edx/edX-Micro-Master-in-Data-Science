class Prob1_Part3:
    """
    Author: LIU HAN
    Date: 10/24/2016
    """

    def check_attempt(self, params):
        # unpack params
        self.attempt = params['attempt']  # student's attempt
        self.answer = params['answer']  # solution
        self.att_tree = params['att_tree']  # attempt tree
        self.ans_tree = params['ans_tree']  # solution tree

        hint = ''

        try:
            hint = 'You should have found the starting point of the distribution from previous part.'

            if len(hint) > 0:
                return hint + 'Should the slope of uniform distribution function between the interval [a,b] ' \
                              'always be the same? 1 for yes, 0 for no', '1'
            else:
                return '', ''
        except Exception:
            return '', ''

    def get_problems(self):
        self.problem_list = ["CumulativeDistributionFunctions/cdf_exp_uni/part3"]
        return self.problem_list
