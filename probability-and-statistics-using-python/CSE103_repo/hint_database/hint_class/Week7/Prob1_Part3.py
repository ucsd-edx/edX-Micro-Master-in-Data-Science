class Prob1_Part3:
	"""
	Author: Sunil Raiyani
	Date: 11/07/2016
	"""

        def check_attempt(self, params):
		#unpack params
		self.attempt = params['attempt'] #student's attempt
		self.answer = params['answer'] #solution
		self.att_tree = params['att_tree'] #attempt tree
		self.ans_tree = params['ans_tree'] #solution tree
		
		hint=''
		
		try:
			hint='For random variables X,Y and constants a,b,c,d, E[(aX+b)(cY+d)]=E[acXY+adX+bcY+bd].Can you simplify this further using linearity of expectations?'
			
			if len(hint)>0:
                                return hint+' If E[X]=2, E[Y]=1 and E[XY]=4, what is E[(2X+1)(Y+2)]?','(2*4)+(4*2)+(1*1)+(2)'
                        else:
                                return '',''
		except Exception:
		        return '',''

	def get_problems(self):
		self.problem_list = ["ExpectationVariance/ExpectationScaling/part3"]
		return self.problem_list
