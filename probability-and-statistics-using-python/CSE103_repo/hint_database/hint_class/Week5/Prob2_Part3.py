class Prob2_Part3:
    """
    Author: Geovonni Najera
    Date: 10/25/2016
    """

    def check_attempt(self, params):
        # unpack params
        self.attempt = params['attempt']  # student's attempt
        self.answer = params['answer']  # solution
        self.att_tree = params['att_tree']  # attempt tree
        self.ans_tree = params['ans_tree']  # solution tree

        

        hint = 'Recall that a point mass distribution is focused at a single point.'
        
        return hint + ' What would the probability of a point mass distribution be anywhere other than at the point?', '0'

    def get_problems(self):
        self.problem_list = ["CumulativeDistributionFunctions/cdf_norm_point/part3"]
        return self.problem_list
