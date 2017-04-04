class Prob10_Part6:
	"""
	Author: Sunil Raiyani
	Date: 10/11/2016
	"""

        def check_attempt(self, params):
		#unpack params
		self.attempt = params['attempt'] #student's attempt
		self.answer = params['answer'] #solution
		self.att_tree = params['att_tree'] #attempt tree
		self.ans_tree = params['ans_tree'] #solution tree
		
		#print self.answer[7]
		hint=''
		
		try:
			if not 'P' in self.attempt and not 'C' in self.attempt:
                        	hint='Try to rewrite your expression in terms of permutations and combinations. Perhaps it will be more intuitive then.'  

			elif '+' in self.attempt:
				hint='Should you add or multiply different parts of your expression?'
 
			elif not 'C(4,1)*' in self.attempt and not '4*' in self.attempt:
				hint='Shouldn\'t the number of ways to select a suit(part 2) appear in your solution?'

			elif not ('C(13,'+self.answer[7]+')') in self.attempt:
				hint='Shouldn\'t the number of ways to select ranks for the cards in same suit(part 4) appear in your solution?'
			elif not '39' in self.attempt:
				hint='Shouldn\'t the number of ways to select the remaining cards(part 5) appear in your solution?'
			
			if len(hint)>0:
                                return hint+' From a deck of cards with 2 suits and 3 ranks, what is the number of ways to get a hand of 3 cards in which exactly 2 cards are from the same suit?','2 * 3 * 3'
                        else:
                                return '',''
		except Exception:
		        return '',''

	def get_problems(self):
		self.problem_list = ["Poker/q2/part6"]
		return self.problem_list
