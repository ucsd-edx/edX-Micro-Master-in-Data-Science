class Prob3_Part2:
    """
    Author: Liu Han
    Date: 11/14/2016
    """

    def check_attempt(self, params):
        # unpack params
        self.attempt = params['attempt']  # student's attempt
        self.answer = params['answer']  # solution
        self.att_tree = params['att_tree']  # attempt tree
        self.ans_tree = params['ans_tree']  # solution tree

        hint = ''

        try:
            if not '/' in self.attempt or not '*' in self.attempt or not '!' in self.attempt:
                hint = 'Suppose you want to calculate the probability that your square will receive ' \
                       'exactly 10 hits in 24 hours. '

            if len(hint) > 0:
                return hint + 'What is the value of k you should use for P(X=k)?', '10'
            else:
                return '', ''

        except Exception:

            return '', ''

    def get_problems(self):
        self.problem_list = ["ExponentialPoisson/poisson_zz/part2"]
        return self.problem_list