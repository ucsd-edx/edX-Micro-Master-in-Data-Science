from hint_class_helpers.find_matches import find_matches

class Prob12_Part4:
	"""
	Author: Jigar Patel
	Date: 10/04/2016
	"""

        def check_attempt(self, params):
		
		#unpack params
		self.attempt = params['attempt'] #student's attempt
		self.answer = params['answer'] #solution
		self.att_tree = params['att_tree'] #attempt tree
		self.ans_tree = params['ans_tree'] #solution tree

		
		
		matches = find_matches(params)
		matching_node = [m[0] for m in matches]
		

		try:
                        
			if len(self.att_tree)==3 and self.att_tree[1][0]=='X' and self.att_tree[2][0]=='X':
				
				if 'R.1' in matching_node and 'R.0.0' in matching_node:
					hint = "The denominator is correct. "
					return hint + "How many different ways to select 2 heads in the H/T sequence of length 3?","C(3,2)"
				elif 'R.1' in matching_node:
					hint = "The denominator is correct. "
					return hint + "How many different ways to select 2 heads in the H/T sequence of length 3?","C(3,2)"
				elif 'R.0' in matching_node:
					hint = "The numerator is correct. "
					return hint + "What is the number of all possible H/T sequence of length 3?", "2^3"
			
			return "",""
                        
                
                except Exception:
                        return "",""

	def get_problems(self):
		self.problem_list = ["Combinatorics/coinProblems/part4"]
		return self.problem_list
