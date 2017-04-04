class Prob4_Part1:
    """
    Author: Chang Qiu
    Date: 10/25/2016
    """

    def check_attempt(self, params):
        # unpack params
        self.attempt = params['attempt']  # student's attempt
        self.answer = params['answer']  # solution
        self.att_tree = params['att_tree']  # attempt tree
        self.ans_tree = params['ans_tree']  # solution tree

        hint = "Recall the formula for exponential distribution in CDF is 1 − e^(−λx), and for a pure exponential distribution, F(x) = component weight * (1 − e^(−λx))."
        return hint + " If 1 − e^(−λx) is at 2, and the F(x) for pure exponential distribution is 0.5, what is the component weight?", "0.25"

    def get_problems(self):
        self.problem_list = ["CumulativeDistributionFunctions/cdf_exp_point/part1"]
        return self.problem_list