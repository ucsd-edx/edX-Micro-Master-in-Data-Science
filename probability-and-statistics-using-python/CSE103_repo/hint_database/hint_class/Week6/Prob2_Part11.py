class Prob2_Part11:
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
				
				hint = 'Recall the formula to find the expected value of E(X+Y).'
				return hint + ' If the probability that X and Y happen is 1/2, X has the value 4, and Y has the value 6, what is the E(X+Y)?', '5'

			elif not '+' in self.attempt:
				
				hint = 'Recall the formula to find the expected value of E(X+Y).'
				return hint + ' If the probability that X and Y happen is 1/2, X has the value 4, and Y has the value 6, what is the E(X+Y)?', '5'

			elif not '*' in self.attempt:
				
				hint = 'Recall the formula to find the expected value of E(X+Y).'
				return hint + ' If the probability that X and Y happen is 1/2, X has the value 4, and Y has the value 6, what is the E(X+Y)?', '5'

			elif '-' in self.attempt:

				hint = 'Recall the formula to find the expected value of E(X+Y).'
				return hint + ' If the probability that X and Y happen is 1/2, X has the value 4, and Y has the value 6, what is the E(X+Y)?', '5'

			elif '!' in self.attempt:

				hint = 'Recall the formula to find the expected value of E(X+Y).'
				return hint + ' If the probability that X and Y happen is 1/2, X has the value 4, and Y has the value 6, what is the E(X+Y)?', '5'

			if len(hint) > 0:

				return hint + ' If the probability that X and Y happen is 1/2, X has the value 4, and Y has the value 6, what is the E(X+Y)?', '5'
			
			else:

				return '',''

		except Exception:

			return '',''

	def get_problems(self):
		self.problem_list = ["Covariance/ContingencyTables1/part7"]
		return self.problem_list