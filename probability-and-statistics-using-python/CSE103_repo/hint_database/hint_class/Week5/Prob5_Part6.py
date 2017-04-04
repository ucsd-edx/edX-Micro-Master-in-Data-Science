class Prob5_Part6:
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
			hint='The formula in the hint for Part 4 can be extended to more that 2 variable if the variables are independent from each other.'
			
			if len(hint)>0:
                                return hint+' If Var(X)=1, Var(Y)=2, Var(Z)=3 what is Var(X-Y+Z)?','1+2+3'
                        else:
                                return '',''
		except Exception:
		        return '',''

	def get_problems(self):
		self.problem_list = ["ExpectationVariance/probs69/part6"]
		return self.problem_list
