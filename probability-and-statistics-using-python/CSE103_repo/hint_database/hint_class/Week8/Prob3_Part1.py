class Prob3_Part1:
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
            if not '/' in self.attempt:
                hint = 'Assume the rate of bombing is 200 bombs per day, and there are 20 equal' \
                       ' area city block.'

            if len(hint) > 0:
                return hint + 'For each block, what is the expected number of bombs that will land on it' \
                              ' in a day?', '10'
            else:
                return '', ''

        except Exception:

            return '', ''

    def get_problems(self):
        self.problem_list = ["ExponentialPoisson/poisson_zz/part1"]
        return self.problem_list