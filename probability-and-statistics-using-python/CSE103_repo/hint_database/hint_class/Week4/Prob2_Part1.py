class Prob2_Part1:
	"""
	Author: Sunil Raiyani
	Date: 10/13/2016
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
			hint='Assume that there are 100 male and 100 female members in the population(since they are equal). Now, using these figures, calculate the number of colorblind males and colorblind females based on the percentages and use them to find the probabilities used in the equation.'
			
			if len(hint)>0:
                                return hint+' If there are 2 colorblind males and 3 colorblind females, then what is the probability that a person chosen at random is male if we know that the person is colorblind?','2/(2+3)'
                        else:
                                return '',''
		except Exception:
		        return '',''

	def get_problems(self):
		self.problem_list = ["BayesConditional/probs_43_w_randomization/part1"]
		return self.problem_list
