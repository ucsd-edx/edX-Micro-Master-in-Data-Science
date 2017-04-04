class Prob2_Part7:
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

        return "What is the relationship between Covariance and independence? If X and Y are independent, what could be the COV?", "2"

    def get_problems(self):
        self.problem_list = ["Covariance/ContingencyTables1/part3"]
        return self.problem_list