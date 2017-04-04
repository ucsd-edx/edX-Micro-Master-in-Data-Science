# Make sure you name your file with className.py
# To test your class make sure you add the local path of hint_class_helpers in your system path
class Prob4_Part1:
	"""
	Author: Vrushali Samant
	Date: 11/14/16
	"""

	def check_attempt(self, params):
		self.attempt = params['attempt'] #student's attempt
		self.answer = params['answer'] #solution
		self.att_tree = params['att_tree'] #attempt tree
		self.ans_tree = params['ans_tree'] #solution tree
		return "The expected number of mistakes per page = (mistakes/words)*(words/page). If there are 4 mistakes every 7 words and 20 words in a page, what is the expected number of mistakes per page?","(4*20)/(7)"

	def get_problems(self):
		self.problem_list = ["ExponentialPoisson/poisson_rs/part1"]
		return self.problem_list
