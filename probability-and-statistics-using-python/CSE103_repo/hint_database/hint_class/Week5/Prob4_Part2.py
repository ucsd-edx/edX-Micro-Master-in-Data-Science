class Prob4_Part2:
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

        return "When does the point mass contribute to the graph? If a discrete random variable is exactly equal to some value at 1, what is the point mass?", "1"

    def get_problems(self):
        self.problem_list = ["CumulativeDistributionFunctions/cdf_exp_point/part2"]
        return self.problem_list