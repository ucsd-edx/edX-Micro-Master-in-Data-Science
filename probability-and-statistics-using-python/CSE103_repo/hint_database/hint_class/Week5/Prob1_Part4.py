class Prob1_Part4:
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
            hint = 'Suppose F = 0.4X + kY where X and Y are two random variable with certain distribution. '

            if len(hint) > 0:
                return hint + 'Now, you know that the component weight of X is 0.4, then what is the component weight of Y?', '0.6'
            else:
                return '', ''
        except Exception:
            return '', ''

    def get_problems(self):
        self.problem_list = ["CumulativeDistributionFunctions/cdf_exp_uni/part4"]
        return self.problem_list