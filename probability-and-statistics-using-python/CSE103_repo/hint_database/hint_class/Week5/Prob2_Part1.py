class Prob2_Part1:
    """
    Author: Geovonni Najera
    Edited: Zhen Zhai
    Date: 10/25/2016
    """

    def check_attempt(self, params):
        # unpack params
        self.attempt = params['attempt']  # student's attempt
        self.answer = params['answer']  # solution
        self.att_tree = params['att_tree']  # attempt tree
        self.ans_tree = params['ans_tree']  # solution tree

        

        hint = 'According to the standard normal CDF table for N(u, 1) (can be found online),'
        
        return hint + ' CDF at u has the value of 0.5. CDF at u+3 has a value very close to 1. What value does CDF has at u-1?', '0.16'

    def get_problems(self):
        self.problem_list = ["CumulativeDistributionFunctions/cdf_norm_point/part1"]
        return self.problem_list
