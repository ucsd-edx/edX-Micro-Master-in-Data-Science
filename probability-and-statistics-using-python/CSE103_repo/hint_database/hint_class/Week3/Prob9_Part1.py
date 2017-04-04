from hint_class_helpers.find_matches import find_matches

class Prob9_Part1:
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

		try:
                        
			if '!' in self.attempt:
                        	hint='The factorial function (!) is not relevant to this question.' 

			elif ('C' in self.attempt) or ('c' in self.attempt) or ('P' in self.attempt) or ('p' in self.attempt):
				hint='Is the use of permutations or combinations really necessary?'

			elif '/' in self.attempt:
				hint='Is the use of division(/) in this case really necessary?'


			if len(hint)>0:
                                return hint + ' Suppose you have 2 distinct cards and 2 envelopes(marked 1 and 2), now take the first card and choose an envelope for it, then take the second card and choose an envelope from it, so in this case how many ways are there to place cards into envelopes? ','2^2' 
			else:
				return '',''
                        
                except Exception:
                        return '',''

	def get_problems(self):
		self.problem_list = ["StarsAndBars/Envelopes1/part1"]
		return self.problem_list
