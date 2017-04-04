# Make sure you name your file with className.py
# To test your class make sure you add the local path of hint_class_helpers in your system path
class Prob4_Part3:
	"""
	Author: Vrushali Samant
	Date: 11/14/16
	"""

	def check_attempt(self, params):
		self.attempt = params['attempt'] #student's attempt
		self.answer = params['answer'] #solution
		self.att_tree = params['att_tree'] #attempt tree
		self.ans_tree = params['ans_tree'] #solution tree
		
		if '1-' in self.attempt:
			return "Recall the question says 'at least' - so instead of computing the CDF, we calculate 1-CDF = 1-(1-e^(-lamda*delta))=e^(-lamda*delta). Given that lambda=1/2 and delta=4, P(X>=a)=e^_____", "(-(1/2)*(4))"
	
	def get_problems(self):
		self.problem_list = ["ExponentialPoisson/poisson_rs/part3"]
		return self.problem_list
