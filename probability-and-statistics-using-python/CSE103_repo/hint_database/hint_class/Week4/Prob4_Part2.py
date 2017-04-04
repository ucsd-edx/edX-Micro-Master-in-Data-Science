class Prob4_Part2:
	"""
	Author: Sunil Raiyani
	Date: 10/17/2016
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
			hint='Assume that there are 100 male and 100 female members in the population(both equal).'
			
			if len(hint)>0:
                                return hint+' If there are 2% colorblind males and 5% colorblind females, then what is the probability that a person chosen at random is colorblind i.e. P(colorblind)?','(2/100)*(100/200) + (5/100)*(100/200)'
                        else:
                                return '',''
		except Exception:
		        return '',''

	def get_problems(self):
		self.problem_list = ["BayesConditional/BayesColorBlindness/part2"]
		return self.problem_list
