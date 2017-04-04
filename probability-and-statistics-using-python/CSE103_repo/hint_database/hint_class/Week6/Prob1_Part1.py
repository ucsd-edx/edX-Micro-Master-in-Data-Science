# Make sure you name your file with className.py
# To test your class make sure you add the local path of hint_class_helpers in your system path
from hint_class_helpers.find_matches import find_matches

class Prob1_Part1:
	"""
	Author: <Akanksha Maurya>
	Date: <10-31-2016>
	"""

	def check_attempt(self, params):
		self.attempt = params['attempt'] #student's attempt
		self.answer = params['answer'] #solution
		self.att_tree = params['att_tree'] #attempt tree
		self.ans_tree = params['ans_tree'] #solution tree
		
		matches = find_matches(params)		
		matching_node = [m[0] for m in matches]

		try:
			if 'i' in self.attempt:
				hint='The answer should not contain variable i. '
			elif 'x' in self.attempt or 'X' in self.attempt:
				hint='The answer should not contain variable x. '
			elif '-' in self.attempt and '-' not in self.answer:
				hint='The subtraction operation is not required. '
			elif 'R.1' in matching_node:
				hint='The constant used in the numerator of expectation value expression is different. '
			else:
				hint='Find the expectation values for each random variable X_i by replacing i and the find the expectation of linear combination of random variables. '
			
			if len(hint)>0:
				return hint+ ' What is the expectation value of E[2X + 3Y], where X and Y are random variable and E[X] =2 , E[Y] =1 ',' 2*2 + 3*1'
			else:
				return '',''

		except Exception:
			return '',''

	def get_problems(self):
		self.problem_list = ["ExpectationVariance/ExpVarOfSum/part1", "ExpectationVariance/ExpVarOfSum/part3", "ExpectationVariance/ExpVarOfSum/part5"]
		return self.problem_list
