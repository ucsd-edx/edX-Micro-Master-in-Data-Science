class Prob2_Part15:
    """
    Author: Chang Qiu
    Edit: Zhen Zhai
    Date: 10/31/2016
    """

    def check_attempt(self, params):
        # unpack params
        self.attempt = params['attempt']  # student's attempt
        self.answer = params['answer']  # solution
        self.att_tree = params['att_tree']  # attempt tree
        self.ans_tree = params['ans_tree']  # solution tree

        return 'What is the correlation coefficient between X and Y you got from part 10? If they are correlated, what is the answer?', '1'
    
    def get_problems(self):
        self.problem_list = ["Covariance/ContingencyTables1/part11"]
        return self.problem_list