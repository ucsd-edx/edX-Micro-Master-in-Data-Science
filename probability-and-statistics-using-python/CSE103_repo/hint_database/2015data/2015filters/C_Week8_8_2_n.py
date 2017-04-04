def C_Week8_8_2_n(params):
  """ Written by bgl004 Wed Nov 18 2015 10:32:16 GMT-0800 (Pacific Standard Time)
  Condition for an "n" input.
  Written by Brandon Lee.
  """
  # params = {'attempt': '', 'att_tree': [], 'answer': '', 'ans_tree': [], 'variables': [{'name':,'value':}]} 
  if params['attempt'] == 'n':
  	return 'Your answer of "n" implies that the worst case scenario is if 1 bin has ALL of the balls in there. However, the statement "(with probability as high as 1 - 1/n)" means that we can assume that the worst case is a bin filled with a number of balls that is at most 1/n. That means that our worst case can now be checking a bin that has >= a certain number of balls. Where else have we seen something greater than or equal to something?'
  else:
  	return ''