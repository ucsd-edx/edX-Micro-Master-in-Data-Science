class Prob2_Part9:
	"""
	Author: Chang Qiu
	Edit: Zhen Zhai
	Date: 10/31/2016
	"""

	def check_attempt(self, params):
		#unpack params
		self.attempt = params['attempt'] #student's attempt
		self.answer = params['answer'] #solution
		self.att_tree = params['att_tree'] #attempt tree
		self.ans_tree = params['ans_tree'] #solution tree
		
		hint = ''
		
		try:
			if not '/' in self.attempt:
				
				hint = 'Recall the formula to find the expected value.'
				return hint + ' If the probability that X happens is 1/2, and X has the value 4, what is the E(X)?', '2'

			elif not '+' in self.attempt:
				
				hint = 'Recall the formula to find the expected value.'
				return hint + ' If the probability that X happens is 1/2, and X has the value 4, what is the E(X)?', '2'

			elif not '*' in self.attempt:
				
				hint = 'Recall the formula to find the expected value.'
				return hint + ' If the probability that X happens is 1/2, and X has the value 4, what is the E(X)?', '2'

			elif '-' in self.attempt:

				hint = 'Should you do subtraction?'
				return hint + ' If the probability that X happens is 1/2, and X has the value 4, what is the E(X)?', '2'

			elif '!' in self.attempt:

				hint = 'Should you do factorial?'
				return hint + ' If the probability that X happens is 1/2, and X has the value 4, what is the E(X)?', '2'

			if len(hint) > 0:

				return hint + ' If the probability that X happens is 1/2, and X has the value 4, what is the E(X)?', '2'
			
			else:

				return '',''

		except Exception:

			return '',''

	def get_problems(self):
		self.problem_list = ["Covariance/ContingencyTables1/part5"]
		return self.problem_list