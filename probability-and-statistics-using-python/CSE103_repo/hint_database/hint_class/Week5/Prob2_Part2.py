class Prob2_Part2:
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

        

        hint = 'Recall notes on mixtures.'
        
        return hint + ' If F(x) is a CDF of N(u,1) with a componment weight of 1, what would the value F(u)?', '0.5'

    def get_problems(self):
        self.problem_list = ["CumulativeDistributionFunctions/cdf_norm_point/part2"]
        return self.problem_list
