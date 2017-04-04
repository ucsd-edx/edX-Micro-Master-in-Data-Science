from hint_class_helpers.find_matches import find_matches

class Prob6_Part2:
	"""
	Author: Jigar Patel
	Date: 10/13/2016
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
                        
			if 'R.1' in matching_node and 'R.0' not in matching_node:
				hint = "The denominator is correct. Here you need a 3 and either a 6 or A on the turn and river to get straight in given situation of cards. So the number of such card pairs, ignoring order, is?"
				return hint,'4*8'

			elif 'R.0' in matching_node and 'R.1' not in matching_node:
				hint = "The numerator is correct."
			
				
			
			if len(hint)>0:
                                return hint + ' Let say you have a heart with number 2 and a diamond with 4. How many ways you can choose three cards from remaining(52 minus 2) deck of cards? C(_,3) ','50' 
			else:
				return '',''

 	
                except Exception:
                        return '',''

	def get_problems(self):
		self.problem_list = ["PokerConditional/poker_cond4_1/part2"]
		return self.problem_list
