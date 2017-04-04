# Make sure you name your file with className.py
# To test your class make sure you add the local path of hint_class_helpers in your system path
class Prob9_Part5:
	"""
	Author: <Akanksha Maurya>
	Date: <10-17-2016>
	"""

	def check_attempt(self, params):
		self.attempt = params['attempt'] #student's attempt
		self.answer = params['answer'] #solution
		self.att_tree = params['att_tree'] #attempt tree
		self.ans_tree = params['ans_tree'] #solution tree
				
		try:
			if '!' in self.attempt:
				hint='The factorial function (!) is not relevant to this question. '
			elif '^' in self.attempt or '**' in self.attempt:
				hint='The pow function (^) or (**) is not relevant to this question. '
			elif 't' in self.attempt:
				hint='The answer should not contain any variable t. Find the sum over all values of t. '
			elif len(self.att_tree)==3 and self.att_tree[0][0]=='C':
				hint='The combination formula C(n,k) is not relevant to this question. '		

                        if len(hint)>0:
                                return hint+'Please use the result from part d. Write the answer for part d in terms of t and sum over all values of t, where t is between x1+2 to number of cards. How many values are possible for x2 when t = x1 +2.  ', ' 1' 
                        else:
                                return '',''
                except Exception:
                        return '',''

	def get_problems(self):
		self.problem_list = ["PokerConditional/poker_cond6_2/part5"]
		return self.problem_list
