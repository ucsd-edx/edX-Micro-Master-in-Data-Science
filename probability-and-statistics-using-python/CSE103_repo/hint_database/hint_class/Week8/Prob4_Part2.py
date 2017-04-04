# Make sure you name your file with className.py
# To test your class make sure you add the local path of hint_class_helpers in your system path
class Prob4_Part2:
	"""
	Author: Vrushali Samant
	Date: 11/14/16
	"""

	def check_attempt(self, params):
		self.attempt = params['attempt'] #student's attempt
		self.answer = params['answer'] #solution
		self.att_tree = params['att_tree'] #attempt tree
		self.ans_tree = params['ans_tree'] #solution tree
		
		if 'e' not in self.attempt:
			return "For the Poisson distribution, P(S=k)=(e^-lambda)(lambda^k/k!). If If lambda=1/50, and k=3, what is the computation? (e^(-1/50))*(______)/(3!)","(1/50)^3"
		if '^' not in self.attempt or "!" not in self.attempt:
			return "For Poisson, P(S=k)=(e^-lambda)(lambda^k/k!). k is the value of S for which we're computing the probability. What is the computation when k=3 and lambda=1/50? (e^(-1/50))*(_______)/(3!)","(1/50)^3"
		else: 
			return "For Poisson, P(S=k)=(e^-lambda)(lambda^k/k!). k is the value of S and lambda is the number of mistakes per page. If lamda=1/50 and k=3, what is P(S=k)? (e^(-1/50))*(_______)/(3!)","(1/50)^3"

	def get_problems(self):
		self.problem_list = ["ExponentialPoisson/poisson_rs/part2"]
		return self.problem_list
