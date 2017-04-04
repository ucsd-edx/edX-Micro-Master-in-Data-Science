class NumericalAnswer:
	"""
	Author: Yoav Freund
	Date: 9/25/2016
	"""

	def check_attempt(self, params):
		self.attempt = params['attempt'] #student's attempt
		self.answer = params['answer'] #solution
		self.att_tree = params['att_tree'] #attempt tree
		self.ans_tree = params['ans_tree'] #solution tree

                if len(self.att_tree)==4 and self.att_tree[0]=='X':
                        return 'Incorrect answer, please write an expression, not the final numerical result',''
		return "", ""

	def get_problems(self):
		self.problem_list = []
		return self.problem_list

    
