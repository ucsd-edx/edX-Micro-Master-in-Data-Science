class Prob6_Part2:
	"""
	Author: Sunil Raiyani
	Edited: Zhen Zhai
	Date: 10/31/2016
	"""

        def check_attempt(self, params):
		#unpack params
		self.attempt = params['attempt'] #student's attempt
		self.answer = params['answer'] #solution
		self.att_tree = params['att_tree'] #attempt tree
		self.ans_tree = params['ans_tree'] #solution tree
		
		#print self.answer[7]
		hint=''
		
		try:
			if '0.5' not in self.attempt and '1/2' not in self.attempt:
				hint='The question is only asking for one of the tail probability in Chebyshev\'s equation. How will it affect your equation?'
			
			if len(hint)>0:
                                return hint+' If P(|X-u|>=a) <= 0.6 and the distribution is symmetric around u, what is P(X-u >= a)?','0.3'
                        else:
                                return '',''
		except Exception:
		        return '',''

	def get_problems(self):
		self.problem_list = ["MarkovChebyshev/chebyshev/part2"]
		return self.problem_list
