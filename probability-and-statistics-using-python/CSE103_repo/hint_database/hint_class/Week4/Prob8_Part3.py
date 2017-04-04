from hint_class_helpers.find_matches import find_matches
class Prob8_Part3:
	"""
	Author: Vrushali Samant
	Date: 10/16/2016
	"""

        def check_attempt(self, params):
		
		#unpack params
		self.attempt = params['attempt'] #student's attempt
		self.answer = params['answer'] #solution
		self.att_tree = params['att_tree'] #attempt tree
		self.ans_tree = params['ans_tree'] #solution tree
		
		hint = ''
		
		matches = find_matches(params)	
		#print "Prob 8 Part 3 matches: ", matches
		try:
                        
			if '*' not in self.attempt:
				hint = 'If the probability of event A is (1/2) is the probability of event B is (1/4), then what is the probability of A and B? (Note that in this problem, event A is the case that opponent 1 wins and B is the case where opponent 2 wins, given that opponent 1 did not.): (1/2)*(__).'
				return hint,'1/4'

			else:
				return '',''

 	
                except Exception:
                        return '',''
		return '',''

	def get_problems(self):
		self.problem_list = ["PokerConditional/poker_cond3/part3"]
		return self.problem_list

