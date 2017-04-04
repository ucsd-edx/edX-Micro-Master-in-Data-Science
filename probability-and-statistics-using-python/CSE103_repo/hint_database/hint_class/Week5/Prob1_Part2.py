class Prob1_Part2:
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
            hint = 'What is the characteristic of the CDF to the uniform distribution?'

            if len(hint) > 0:
                return hint + 'Is the distribution function line curved or not? ' \
                              '0 for curved; 1 for non-curved', '1'
            else:
                return '', ''
        except Exception:
            return '', ''

    def get_problems(self):
        self.problem_list = ["CumulativeDistributionFunctions/cdf_exp_uni/part2"]
        return self.problem_list