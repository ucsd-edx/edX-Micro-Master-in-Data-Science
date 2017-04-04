class Prob4_Part2:
	"""
	Author: Jigar Patel
	Date: 11/07/2016
	"""

        def check_attempt(self, params):
		
		#unpack params
		self.attempt = params['attempt'] #student's attempt
		self.answer = params['answer'] #solution
		self.att_tree = params['att_tree'] #attempt tree
		self.ans_tree = params['ans_tree'] #solution tree
		
		hint = 'Which geometric series did you choose to calculate E(X)? (r + r^2 + ...) OR (r + 2r^2 + 3r^3 + ...).'
		
		try:

			if len(hint)>0:
                                return hint + ' If p=0.4 then E(X) = 1*(0.4) + 2*(1-0.4)*0.4 + 3*((1-0.4)^2)*0.4 + ... = 0.4/(1-0.4) [(1-0.4) + 2(1-0.4)^2 + 3(1-0.4)^3 + ...] so what is r = ','0.6' 
			else:
				return '',''
                        
                except Exception:
                        return '',''

	def get_problems(self):
		self.problem_list = ["ExpectationVariance/Notes_3_2_2.imd/part2"]
		return self.problem_list
