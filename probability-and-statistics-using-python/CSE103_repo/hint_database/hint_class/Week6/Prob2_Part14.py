class Prob2_Part14:
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
				
				hint = 'Use the formula provided above to find the correlation coefficient between X and Y.'
				return hint + ' If Cov(X,Y) is 4, sqrt(Var(X)) is 2 and sqrt(Var(Y)) is 2, what is the correlation coefficient between X and Y?', '1'

			elif not '+' in self.attempt:
				
				hint = 'Use the formula provided above to find the correlation coefficient between X and Y.'
				return hint + ' If Cov(X,Y) is 4, sqrt(Var(X)) is 2 and sqrt(Var(Y)) is 2, what is the correlation coefficient between X and Y?', '1'


			elif not '*' in self.attempt:
				
				hint = 'Use the formula provided above to find the correlation coefficient between X and Y.'
				return hint + ' If Cov(X,Y) is 4, sqrt(Var(X)) is 2 and sqrt(Var(Y)) is 2, what is the correlation coefficient between X and Y?', '1'


			elif '-' in self.attempt:

				hint = 'Use the formula provided above to find the correlation coefficient between X and Y.'
				return hint + ' If Cov(X,Y) is 4, sqrt(Var(X)) is 2 and sqrt(Var(Y)) is 2, what is the correlation coefficient between X and Y?', '1'


			elif '!' in self.attempt:

				hint = 'Use the formula provided above to find the correlation coefficient between X and Y.'
				return hint + ' If Cov(X,Y) is 4, sqrt(Var(X)) is 2 and sqrt(Var(Y)) is 2, what is the correlation coefficient between X and Y?', '1'


			if len(hint) > 0:

				return hint + ' If Cov(X,Y) is 4, sqrt(Var(X)) is 2 and sqrt(Var(Y)) is 2, what is the correlation coefficient between X and Y?', '1'

			else:

				return '',''

		except Exception:

			return '',''

	def get_problems(self):
		self.problem_list = ["Covariance/ContingencyTables1/part10"]
		return self.problem_list