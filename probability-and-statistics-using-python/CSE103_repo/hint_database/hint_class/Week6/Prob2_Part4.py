class Prob2_Part4:
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
				
				hint = 'Recall the marginal distribution of Y is the sum of all X values.'
				return hint + ' If you have 1/4, 1/4, 1/4 when Y = 2, what is the marginal distribution of Y', '0.75'

			elif not '+' in self.attempt:
				
				hint = 'Recall the marginal distribution of Y is the sum of all X values.'
				return hint + ' If you have 1/4, 1/4, 1/4 when Y = 2, what is the marginal distribution of Y', '0.75'

			elif '-' in self.attempt:

				hint = 'Should you do subtraction?'
				return hint + ' If you have 1/4, 1/4, 1/4 when Y = 2, what is the marginal distribution of Y', '0.75'

			elif '!' in self.attempt:

				hint = 'Should you do factorial?'
				return hint + ' If you have 1/4, 1/4, 1/4 when Y = 2, what is the marginal distribution of Y', '0.75'

			if len(hint) > 0:

				return hint + ' If you have 1/4, 1/4, 1/4 when Y = 2, what is the marginal distribution of Y', '0.75'
			
			else:

				return '',''

		except Exception:

			return '',''

	def get_problems(self):
		self.problem_list = ["Covariance/ContingencyTables1/part2"]
		return self.problem_list