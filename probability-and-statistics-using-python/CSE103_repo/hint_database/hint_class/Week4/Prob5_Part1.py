class Prob5_Part1:
	"""
	Author: Chang Qiu
	Date: 10/17/2016
	"""

	def check_attempt(self, params):
		#unpack params
		self.attempt = params['attempt'] #student's attempt
		self.answer = params['answer'] #solution
		self.att_tree = params['att_tree'] #attempt tree
		self.ans_tree = params['ans_tree'] #solution tree
		
		hint = ''
		
		try:
			if not '^' in self.attempt:
				hint = 'You have 2 ranks, and each rank has 4 suits.'
				return hint + ' if you choose rank 3 and 4, and each rank has five suits, how many combinations are there?', '5^2'

			elif 'C(' in self.attempt:

				hint = 'We do not need combinations for this part.'
				return hint + ' if you choose rank 3 and 4, and each rank has five suits, how many combinations are there?', '5^2'

			elif '+' in self.attempt:
				
				hint = 'Should you add different parts of your expression?'
				return hint + ' if you choose rank 3 and 4, and each rank has five suits, how many combinations are there?', '5^2'

			elif '-' in self.attempt:

				hint = 'Should you do subtraction?'
				return hint + ' if you choose rank 3 and 4, and each rank has five suits, how many combinations are there?', '5^2'

			elif '!' in self.attempt:

				hint = 'Should you do factorial?'
				return hint + ' if you choose rank 3 and 4, and each rank has five suits, how many combinations are there?', '5^2'

			if len(hint) > 0:

				return hint + ' if you have 6, 7, 8, 9 in hand, how many ways are there to form a straight?', '5^2'
			else:

				return '',''

		except Exception:

			return '',''

	def get_problems(self):
		self.problem_list = ["PokerConditional/poker_cond2_1/part1"]
		return self.problem_list