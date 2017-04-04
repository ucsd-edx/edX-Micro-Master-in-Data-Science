from hint_class_helpers.find_matches import find_matches

class Prob6_Part1:
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
                        
			if '^' in self.attempt or '**' in self.attempt:
                        	hint='The exponent operator (^ or **) is not relevant to this question.' 
			
			elif 'P' in self.attempt:
				hint='Is order important in this case?'

			elif ('R.0' in matching_node and 'R.1' in matching_node):
				
				if '+' in self.attempt:
                        		hint='Do you think \'+\' is correct choice in this case?'
			
 

			if len(hint)>0:
                                return hint + ' How many card pairs are there having a black colored number 2 card and a number 9 card in a deck? (Ignore the order)','2*4' 
			else:
				return '',''
                        
                except Exception:
                        return '',''

	def get_problems(self):
		self.problem_list = ["PokerConditional/poker_cond4_1/part1"]
		return self.problem_list
