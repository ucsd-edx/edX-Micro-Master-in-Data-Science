class Prob5_Part2:
	"""
	Author: Sunil Raiyani
	Date: 10/24/2016
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
			hint='Refer to Question 6. Make a table similar to one in Problem 6 and compute variance in a similar manner.'
			
			if len(hint)>0:
                                return hint+' If P(X=0) = 0.4 and P(X=1) = 0.6, then E[X] = 0.6, what is Var(X)?','0.4*((0-0.6)^2)+0.6*((1-0.6)^2)'
                        else:
                                return '',''
		except Exception:
		        return '',''

	def get_problems(self):
		self.problem_list = ["ExpectationVariance/probs69/part2"]
		return self.problem_list
