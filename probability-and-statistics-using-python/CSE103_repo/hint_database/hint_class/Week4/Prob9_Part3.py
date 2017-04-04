# Make sure you name your file with className.py
# To test your class make sure you add the local path of hint_class_helpers in your system path
class Prob9_Part3:
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
			elif '+' in self.attempt:
				hint='The sum fuction (+) is not relevant to this question. '
			elif len(self.att_tree)==3 and self.att_tree[0][0]=='C':
				hint='The combination formula C(n,k) is not relevant to this question. '
			elif len(self.att_tree)==3 and self.att_tree[0][0] == '*' and self.att_tree[1][0]=='X' and self.att_tree[2][0]=='X':
				hint='Please use the resultant expression from part a and part b. '		

                        if len(hint)>0:
                                return hint+'How many different ways are possible to select x2 in B= {x1, x2} given x1 is 2, where x1 and x2 can be any number between 1 to 5. ','5-1'
                        else:
                                return '',''
                except Exception:
                        return '',''

	def get_problems(self):
		self.problem_list = ["PokerConditional/poker_cond6_2/part3"]
		return self.problem_list
