# Make sure you name your file with className.py

from sets import Set

class Prob12_Part1:
	"""
	Author: Yoav Freund
	Date: 9/25/2016
	"""

        def check_attempt(self, params):
                #unpack params
                self.attempt = params['attempt'] #student's attempt
                self.answer = params['answer'] #solution
                self.att_tree = params['att_tree'] #attempt tree
                self.ans_tree = params['ans_tree'] #solution tree

                hint=''

                # all print commands inside a check_attempt filter are for debugging only and should be disabled before deploying the hint.
                # print 'Prob13_Part1',self.answer,self.attempt #debug print

                try:
                        if '!' in self.attempt:
                            hint='The factorial function (!) is not relevant to this question. '
                        #check if the form of the parse tree has the right
                        #shape: an operator and two leafs that correspond to
                        #the operands
                        elif len(self.att_tree)==3 and self.att_tree[1][0]=='X' and self.att_tree[2][0]=='X':
                            # print 'attempt_tree=\n',self.att_tree #debug

                            # Preparations ---------------------------------------
                            parts={}  # A dictionary of dictionaries that
                                      # holds the 3 parts of the attempt
                                      # and the three parts of the answer.
                            operands={} # A dict of Sets which holds the
                                        # operands in the attempt and the
                                        # operands in the answer.
                            # extract the relevant parts of the parse tree.
                            for tree_name,tree in [('att',self.att_tree),('ans',self.ans_tree)]:
                                parts[tree_name]={'op':tree[0][0],
                                                  'a':tree[1][1],
                                                  'b':tree[2][1]}
                                operands[tree_name]=Set([tree[1][1], tree[2][1]])
                            #print 'parts=', parts  
                            #print 'operands',operands

                            # identifying mistakes
                            if not parts['att']['op'] in ['^','**']:
                                    hint='The operator you are using: '+parts['att']['op']+' is incorrect. '
                            elif parts['att']['b']==parts['ans']['a'] and parts['att']['a']==parts['ans']['b']:
                                    hint='It seems that you have the order of the operands reversed. '
                            elif parts['att']['a'] != parts['ans']['a']:
                                    hint='The first operand should not be {0}. '.format(str(parts['att']['a']))
                            elif parts['att']['b'] != parts['ans']['b']:
                                    hint='The second operand should not be {0}. '.format(str(parts['att']['b']))

                        if len(hint)>0:
                                return hint+'What is the number of binary strings of length 3?','2^3'
                        else:
                                return '',''
                except Exception:
                        return '',''

	def get_problems(self):
		self.problem_list = ["Combinatorics/p13/part1"]
		return self.problem_list
