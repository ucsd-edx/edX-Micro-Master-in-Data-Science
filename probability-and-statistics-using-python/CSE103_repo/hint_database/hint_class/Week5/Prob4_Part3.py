class Prob4_Part3:
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

        hint =  "Recall component weights need to sum to 1 and the CDF is a mixture distribution with two components." 

        return hint + " If you know the component weight of the exponential distribution is 0.4, what is the component weight of the point mass?", "0.6"

    def get_problems(self):
        self.problem_list = ["CumulativeDistributionFunctions/cdf_exp_point/part3"]
        return self.problem_list