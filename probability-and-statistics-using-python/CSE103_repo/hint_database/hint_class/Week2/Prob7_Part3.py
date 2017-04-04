class Prob7_Part3:
	"""
	Author: Sunil Raiyani
	Date: 10/04/2016
	"""

        def check_attempt(self, params):
		#unpack params
		self.attempt = params['attempt'] #student's attempt
		self.answer = params['answer'] #solution
		self.att_tree = params['att_tree'] #attempt tree
		self.ans_tree = params['ans_tree'] #solution tree

		hint=''

		#print 'Prob7_Part3'
		#print self.att_tree
		#print self.ans_tree #debug print
		
		try:
			if '!' in self.attempt:
                        	hint='The factorial function (!) is not relevant to this question.'
			
			elif ('C' in self.attempt) or ('c' in self.attempt) or ('P' in self.attempt) or ('p' in self.attempt):
				hint='Is the use of permutations or combinations really necessary?'

			elif not '-' in self.attempt:
				hint='Please solve question 2 first and relate to its solution. From the number of all possible strings that you have already calculated, is it easy to calculate and subtract the ones that do not fit the requirement?'    
			
			if len(hint)>0:
                                return hint+' What is the number of strings of 2 lower case English letter that contain at least one letter \'x\'?','26^2-25^2'
                        else:
                                return '',''
		except Exception:
		        return '',''

	def get_problems(self):
		self.problem_list = ["Combinatorics/p12/part3"]
		return self.problem_list
