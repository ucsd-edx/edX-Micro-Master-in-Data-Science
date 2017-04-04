from hint_class_helpers.find_matches import find_matches

class Prob7_Part1:
	"""
	Author: Jigar Patel
	Date: 10/24/2016
	"""

        def check_attempt(self, params):
		
		#unpack params
		self.attempt = params['attempt'] #student's attempt
		self.answer = params['answer'] #solution
		self.att_tree = params['att_tree'] #attempt tree
		self.ans_tree = params['ans_tree'] #solution tree
		
		hint = ''
	
		matches = find_matches(params)
		matching_node = [m[0] for m in matches]
		
		try:
                        
			if '^' in self.attempt or '**' in self.attempt:
                        	hint='The exponent operator (^ or **) is not relevant to this question.' 
			
			elif 'R.0' not in matching_node:
				hint='Make sure you are using correct scaling factors and mean values for corresponding random variables.'
			
			elif 'R.0' in matching_node and 'R.1' not in matching_node:
				hint='Make sure you are using correct additive constant value.'	
 			

			if len(hint)>0:
                                return hint + ' Let say r.v. X has mean of 1 and variance of 2, r.v. Z = 2X + 1 then E(Z) = E(2X+1) = 2E(X) + 1 = ?  (write final value only)','3' 
			else:
				return '',''
                        
                except Exception:
                        return '',''

	def get_problems(self):
		self.problem_list = ["ExpectationVariance/Notes3_5_3/part1"]
		return self.problem_list
