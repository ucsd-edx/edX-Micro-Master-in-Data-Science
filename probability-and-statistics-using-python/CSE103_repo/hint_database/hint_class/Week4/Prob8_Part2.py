from hint_class_helpers.find_matches import find_matches
class Prob8_Part2:
	"""
	Author: Vrushali Samant
	Date: 10/15/2016
	"""

        def check_attempt(self, params):
		
		#unpack params
		self.attempt = params['attempt'] #student's attempt
		self.answer = params['answer'] #solution
		self.att_tree = params['att_tree'] #attempt tree
		self.ans_tree = params['ans_tree'] #solution tree
		
		hint = ''
		
		matches = find_matches(params)
		#print "PROBLEM 8 PART 2: ", matches
 		
 
 		try:
			if '/' not in self.attempt:
				hint = 'To calculate the probability that an event occurs, divide the size of the event by the size of the outcome space. What is the size of the event in this case?'
				return hint,'3'
                         
 			elif '1-' not in self.attempt:
 				hint = 'The conditional probability that you win a coin toss given that you bet on heads, is 1-probability(opponent wins) = 1-(___).'
 				return hint,'1/2'
 
 			elif 'C' not in self.attempt:
 				hint = 'If you are choosing 2 cards from a pool of 26 from which 3 cards have already been drawn, how many choices do you have?: C(26-3,__)'
 				return hint, '2'
 			else:
 				return '',''

  	
                except Exception:
			return '',''
		return '',''

	def get_problems(self):
		self.problem_list = ["PokerConditional/poker_cond3/part2"]
		return self.problem_list
