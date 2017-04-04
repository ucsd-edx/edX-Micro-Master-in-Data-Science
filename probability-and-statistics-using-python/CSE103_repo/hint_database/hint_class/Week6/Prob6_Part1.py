class Prob6_Part1:
	"""
	Author: Sunil Raiyani
	Date: 10/31/2016
	"""

        def check_attempt(self, params):
		#unpack params
		self.attempt = params['attempt'] #student's attempt
		self.answer = params['answer'] #solution
		self.att_tree = params['att_tree'] #attempt tree
		self.ans_tree = params['ans_tree'] #solution tree
		
		print self.att_tree
		#final_pairs=find_matches(params)
		
		hint=''
		
		try:
			final_ans=self.att_tree[0][1]
			if '-' not in self.attempt or final_ans == 25.0:
				hint='You need to compute the probability of temperature falling within a range. Do you need to reverse Chebyshev\'s equation?'
			elif final_ans < 1.0:
				hint='Please enter a percentage i.e. multiply your probability by 100.'
			
			if len(hint)>0:
                                return hint+' If mean temperature is 5 and we want to calculate probability of temperature being within 2 and 8 i.e P(|T-5| <= a). What is a?','3'
                        else:
                                return '',''
		except Exception:
		        return '',''

	def get_problems(self):
		self.problem_list = ["MarkovChebyshev/chebyshev/part1"]
		return self.problem_list
