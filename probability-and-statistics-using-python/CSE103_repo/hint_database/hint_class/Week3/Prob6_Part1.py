
class Prob6_Part1:
	"""
	Author: Chang Qiu
	Date: 10/11/2016
	"""

	def check_attempt(self, params):
		#unpack params
		self.attempt = params['attempt'] #student's attempt
		self.answer = params['answer'] #solution
		self.att_tree = params['att_tree'] #attempt tree
		self.ans_tree = params['ans_tree'] #solution tree
		
		hint = ''
		
		try:
			if not 'P' in self.attempt:
				hint = 'Try to rewrite your expression in terms of permutations. It is intuitive and efficient.'

			elif 'C' in self.attempt:

				hint = 'Does the order of words matter?'

			elif '^' in self.attempt:

				hint = 'Are you trying to generate a 2 letters words using 26 letters?'

			elif '+' in self.attempt:
				
				hint = 'Should you add different parts of your expression?'

			elif '*' in self.attempt:

				hint = 'Should you multiply different parts of your expression?'

			elif '!' in self.attempt:

				hint = 'Should you do factorial?'

			if len(hint) > 0:

				return hint +' If you want to generate a lowercase 3-letter word, and you can pick any letter from a to g, what is the size of set?', 'P(7,3)'

			else:

				return '',''

		except Exception:

			return '',''

	def get_problems(self):
		self.problem_list = ["Combinatorics/PigeonHole/part1"]
		return self.problem_list