from hint_class_helpers.find_matches import find_matches

class Prob7_Part2:
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

			if not('^' in self.attempt or '**' in self.attempt):
				hint='Can you think of using ^ operation in the expression.'
	
			elif ('R.0' not in matching_node and 'R.1' in matching_node) or ('R.0' in matching_node and 'R.1' not in matching_node):
				hint='Check the variance values of corresponding random variables.'
			
			elif self.answer in self.attempt:
				hint='Variance of any constant term is zero.'	
 			

			if len(hint)>0:
                                return hint + ' Let say r.v. X has mean of 1 and variance of 2, r.v. Z = 3X + 1 then var(Z) = var(3X+1) = (3^2)*var(X) = ?  (write final value only)','18' 
			else:
				return '',''
                        
                except Exception:
                        return '',''

	def get_problems(self):
		self.problem_list = ["ExpectationVariance/Notes3_5_3/part2"]
		return self.problem_list
