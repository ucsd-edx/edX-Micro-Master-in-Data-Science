from hint_class_helpers.find_matches import find_matches

class Prob6_Part1:
	"""
	Author: Jigar Patel
	Date: 11/14/2016
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
                        
			

			if 'R.0.1' in matching_node and 'R.0.0' in matching_node:
				
				return 'The distribution choice is correct! Are these events dependent(0) or Independent(1) (Choose: 0 or 1)?','1'
			
			elif 'R.0' in matching_node:

				return 'The numerator is correct! Hint: What is the P(head) when both head and tail are equally likely?', '1/2'
			
			elif 'R.1' in matching_node and ('R.0.1' not in matching_node or 'R.0.0' not in matching_node):

				hint = 'Denominator is correct!'   

			if len(hint)>0:
                                return hint + ' What should be the distribution here(Choose 0 for Exponential or 1 for Poisson)','1' 
			else:
				return '',''
                        

                except Exception:
                        return '',''

	def get_problems(self):
		self.problem_list = ["ExponentialPoisson/ur_pb_9_4.imd/part1"]
		return self.problem_list
