# Make sure you name your file with className.py
# To test your class make sure you add the local path of hint_class_helpers in your system path

class Prob12_Part3:
	"""     
	Author: <Akanksha Maurya>
	Date: <10-05-2016>
	"""

	def check_attempt(self, params):
		self.attempt = params['attempt'] #student's attempt
		self.answer = params['answer'] #solution
		self.att_tree = params['att_tree'] #attempt tree
		self.ans_tree = params['ans_tree'] #solution tree

		try:

			#check if the form of the parse tree has the right
			#shape: an operator and two leafs that correspond to
			#the operands
			if ('^' or '**' in self.attempt) and len(self.att_tree) == 3 and self.att_tree[1][1]==2.0:
                                hint = "It seems you are counting both heads and tails as an event output for each coin flips."
			        return hint + " What is the number of different ways to get 1 heads in 3 coin flips? ", "C(3,1)"
			
			return "",""

		except Exception:
			return '',''


	def get_problems(self):
		self.problem_list = ["Combinatorics/coinProblems/part3"]
		return self.problem_list
