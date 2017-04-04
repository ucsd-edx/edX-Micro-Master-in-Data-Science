# Make sure you name your file with className.py
# To test your class make sure you add the local path of hint_class_helpers in your system path
from hint_class_helpers.find_matches import find_matches
class Prob3_Part1:
	"""
	Author: Vrushali Samant
	Date: <10-11-2016 14:00>
	"""

	def check_attempt(self, params):
		self.attempt = params['attempt'] #student's attempt
		self.answer = params['answer'] #solution
		self.att_tree = params['att_tree'] #attempt tree
		self.ans_tree = params['ans_tree'] #solution tree
                matches = find_matches(params)       
                #print "Prob3_Part1 matches: ", matches

                for m in matches:
                        if 'R.0' not in m:
                                return "If you have 3 spot and 4 choices per spot, what should be the base for your exponential expression?","4"
                        if 'R.1' not in m:
                            return "If you have 3 spots and 4 choices per spot, what should be the exponent in your expression?", "3"
                if ("^" not in self.attempt):
                    return "If there are 3 spots and 4 choices for each spot, what format should your answer be in? 4^_", "3"
                else:
                    return "If there are 3 spots, and 4 choices for each spot, is the total number of combinations 3^4 or 4^3?","4^3" 
                return "", ""

	def get_problems(self):
		self.problem_list = ["Combinatorics/DiscreteProb1/part1"]
		return self.problem_list
