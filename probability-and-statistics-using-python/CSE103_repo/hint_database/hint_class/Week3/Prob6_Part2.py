class Prob6_Part2:
	"""
	Author: LIU HAN
	Date: 10/11/2016
	"""

        def check_attempt(self, params):
		#unpack params
		self.attempt = params['attempt'] #student's attempt
		self.answer = params['answer'] #solution
		self.att_tree = params['att_tree'] #attempt tree
		self.ans_tree = params['ans_tree'] #solution tree
		
		hint=''

		try:
			if not 'P' in self.attempt:
				hint = "Do you think whether the permutations should be used here? How should your answer in part 1 be related to this part?"
			elif not '+' in self.attempt and not '1' in self.attempt:
				hint = 'What is the formula of pigeon-hole principle? Should you add 1 at the end of your equation?'

			if len(hint)>0:
				return hint + 'There are 3 colors of marbles.How many marbles do we need in order to guarantee that there is at least one color for whicch we have at least 6 marbles?','3*(6-1)+1'
			else:
				return '',''
		except Exception:
		        return '',''

	def get_problems(self):
		self.problem_list = ["Combinatorics/PigeonHole/part2"]
		return self.problem_list
