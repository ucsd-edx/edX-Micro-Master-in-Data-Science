# Make sure you name your file with className.py
# To test your class make sure you add the local path of hint_class_helpers in your system path
from hint_class_helpers.find_matches import find_matches
class Prob3_Part3:
	"""
	Author: <Vrushali Samant>
	Date: <10-11-2016 15:12>
	"""

	def check_attempt(self, params):
		self.attempt = params['attempt'] #student's attempt
		self.answer = params['answer'] #solution
		self.att_tree = params['att_tree'] #attempt tree
		self.ans_tree = params['ans_tree'] #solution tree
                matches = find_matches(params)
                #print "Prob3_Part3 matches: ", matches

		if ("-1" not in self.attempt):
			return "Having, for example, 6 choices for digits 1 and 3, how many choices remain for digits 2 and 4?","6-1"
		return "", ""

	def get_problems(self):
		self.problem_list = ["Combinatorics/DiscreteProb1/part3"]
		return self.problem_list

