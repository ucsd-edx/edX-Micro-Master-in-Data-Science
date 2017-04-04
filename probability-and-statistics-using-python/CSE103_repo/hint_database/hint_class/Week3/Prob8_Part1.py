# Make sure you name your file with className.py
# To test your class make sure you add the local path of hint_class_helpers in your system path
class Prob8_Part1:
	"""
	Author: <Akanksha Maurya>
	Date: <10-11-2016>
	"""

	def check_attempt(self, params):
		self.attempt = params['attempt'] #student's attempt
		self.answer = params['answer'] #solution
		self.att_tree = params['att_tree'] #attempt tree
		self.ans_tree = params['ans_tree'] #solution tree
		
		print "Answer : ", self.answer
		print " Ans Tree: ", self.ans_tree
		print "Attempt : ", self.attempt
		print " Att Tree: ", self.att_tree 

                hint=''

                # all print commands inside a check_attempt filter are for debugging only and should be disabled before deploying the hint.
                # print 'Prob13_Part1',self.answer,self.attempt #debug print

                try:
                        if '!' in self.attempt:
                            hint='The factorial function (!) is not relevant to this question. '
                        #check if the form of the parse tree has the right
                        #shape: an operator and two leafs that correspond to
                        #the operands
                        elif '^' in self.attempt or '**' in self.attempt:
			    hint='The pow function (^) or (**) is not relevant to this question. '
			elif '*' in self.attempt:
			    hint='The product function (*) is not relevant to this question. '
			elif len(self.att_tree)==3 and self.att_tree[0][0]=='C':
			    hint='The combination formula C(n,k) is not relevant to this question. '
			elif len(self.att_tree)==3 and self.att_tree[0][0]=='P':
			    hint='The permutation formula P(n,k) is not relevant to this question. '
			elif 'R.1' not in self.att_tree and 'R.0' not in self.att_tree:
			    attempt_val = int(self.att_tree[1])
			    answer_val = int(self.ans_tree[1])
			    if attempt_val > answer_val:
			    	hint='The number of bars should be less than the total number of colors i.e. {0}  '.format(str(answer_val +1))
			    elif attempt_val < answer_val:
				hint=' '

                        if len(hint)>0:
                                return hint+'How many bars are needed for 3 categories?','3-1'
                        else:
                                return '',''
                except Exception:
                        return '',''


	def get_problems(self):
		self.problem_list = ["StarsAndBars/ChoosingCandies/part1"]
		return self.problem_list
