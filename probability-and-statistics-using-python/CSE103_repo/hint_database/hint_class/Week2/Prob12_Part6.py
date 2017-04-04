# Make sure you name your file with className.py
# To test your class make sure you add the local path of hint_class_helpers in your system path
from hint_class_helpers.find_matches import find_matches

class Prob12_Part6:
	"""
	Author: Zhen Zhai
	Date: <10-05-2016 00:06>
	"""

	def check_attempt(self, params):
		self.attempt = params['attempt'] #student's attempt
		self.answer = params['answer'] #solution
		self.att_tree = params['att_tree'] #attempt tree
		self.ans_tree = params['ans_tree'] #solution tree
		matches = find_matches(params)
		matching_node = [m[0] for m in matches]

		try:
			#check if the form of the parse tree has the right
			#shape: an operator and two leafs that correspond to
			#the operands
			if len(self.att_tree)==3 and self.att_tree[1][0]=='X' and self.att_tree[2][0]=='X':
				if 'R.1' in matching_node and 'R.0.0' in matching_node:
					hint = "The denominator is correct. "
					return hint + "How many different ways to select 2 heads in the H/T sequence of length 3(order doesn't matter)?","C(3,2)"
				elif 'R.1' in matching_node:
					hint = "The denominator is correct. "
					return hint + "How many different ways to select 2 heads in the H/T sequence of length 3?","C(3,2)"
				elif 'R.0' in matching_node:
					hint = "The numerator is correct. "
					return hint + "What is the number of all possible H/T sequence of length 3?", "2^3"
			return "", ""

		except Exception:
			return '',''

	def get_problems(self):
		self.problem_list = ["Combinatorics/coinProblems/part6"]
		return self.problem_list