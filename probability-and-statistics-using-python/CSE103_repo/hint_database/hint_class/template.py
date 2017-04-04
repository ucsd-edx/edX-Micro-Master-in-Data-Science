# Make sure you name your file with className.py
# To test your class make sure you add the local path of hint_class_helpers in your system path
class className:
	"""
	Author: <your name>
	Date: <MM-DD-YYYY HH:MM>
	"""

	def check_attempt(self, params):
		self.attempt = params['attempt'] #student's attempt
		self.answer = params['answer'] #solution
		self.att_tree = params['att_tree'] #attempt tree
		self.ans_tree = params['ans_tree'] #solution tree

		if (condition):
			return "hint","hint_solution"
		return "", ""

	def get_problems(self):
		self.problem_list = ["problemType/problemName/part1", "problemType/problemName2/part2"]
		return self.problem_list