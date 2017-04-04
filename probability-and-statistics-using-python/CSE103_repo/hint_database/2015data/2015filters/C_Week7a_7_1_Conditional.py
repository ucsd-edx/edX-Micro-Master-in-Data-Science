def C_Week7a_7_1_Conditional(params):
  """ Written by bgl004 Mon Nov 09 2015 11:09:49 GMT-0800 (Pacific Standard Time)
  Conditional hint when they attempt to put 1 (or yes).
  Written by Brandon Lee
  """
  # params = {'attempt': '', 'att_tree': [], 'answer': '', 'ans_tree': [], 'variables': [{'name':,'value':}]} 
  if params['attempt'] == '+1' or params['attempt'] == '1':
    return 'A large value for the chi statistic means that we can reject the Null Hypothesis.'
  else:
    return ''