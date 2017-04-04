from hint_class_helpers.find_matches import find_matches

class Prob9_Part2:
	"""
	Author: Jigar Patel
	Date: 10/11/2016
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

			if len(self.att_tree)==3 and self.att_tree[1][0]=='X' and self.att_tree[2][0]=='X':
				
				if 'R.1' in matching_node:
					hint = "The denominator is correct."
				
				elif 'R.0' in matching_node:
					hint = "The numerator is correct."
	

			if len(hint)>0:
                                return hint + ' Recall the \"Stars and Bars\" problem of choosing 3 candies when there are 2 types of candies to choose from. As we have 2 types of candies, we need only one bar to separate two types. So we have 3 stars(3 candies) and one bar. How many different strings can be generated using 3 stars and One bar? C(4,3) i.e. C(3+_-1,3)','2' 
			else:
				return '',''
                        
                except Exception:
                        return '',''

	def get_problems(self):
		self.problem_list = ["StarsAndBars/Envelopes1/part2"]
		return self.problem_list
