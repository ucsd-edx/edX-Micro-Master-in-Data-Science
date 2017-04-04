class Prob2_Part13:
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
				
				hint = 'Use the formula provided above to find the Cov'
				return hint + ' If E(XY) is 4, E(X)E(Y) is 2, what is Cov(X,Y)?', '2'

			elif not '+' in self.attempt:
				
				hint = 'Use the formula provided above to find the Cov'
				return hint + ' If E(XY) is 4, E(X)E(Y) is 2, what is Cov(X,Y)?', '2'


			elif not '*' in self.attempt:
				
				hint = 'Use the formula provided above to find the Cov'
				return hint + ' If E(XY) is 4, E(X)E(Y) is 2, what is Cov(X,Y)?', '2'


			elif '-' in self.attempt:

				hint = 'Use the formula provided above to find the Cov'
				return hint + ' If E(XY) is 4, E(X)E(Y) is 2, what is Cov(X,Y)?', '2'


			elif '!' in self.attempt:

				hint = 'Use the formula provided above to find the Cov'
				return hint + ' If E(XY) is 4, E(X)E(Y) is 2, what is Cov(X,Y)?', '2'


			if len(hint) > 0:


				return hint + ' If E(XY) is 4, E(X)E(Y) is 2, what is Cov(X,Y)?', '2'

			else:

				return '',''

		except Exception:

			return '',''

	def get_problems(self):
		self.problem_list = ["Covariance/ContingencyTables1/part9"]
		return self.problem_list