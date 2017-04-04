class Prob2_Part8:
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

        return "Check out the table to see if they are identically distributed. If they are not symmetrical, are they identically distributed?", "0"

    def get_problems(self):
        self.problem_list = ["Covariance/ContingencyTables1/part4"]
        return self.problem_list