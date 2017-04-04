def C_CombinedPracticeFinal_15_1_lower_bound(params):
  """ Written by clao Mon Nov 30 2015 12:13:26 GMT-0800 (Pacific Standard Time)
  Remind students that Chebyshev's Inequality only gets them the upper bound
  """
  # params = {'attempt': '', 'att_tree': [], 'answer': '', 'ans_tree': [], 'variables': [{'name':,'value':}]} 
  import json
  print json.dumps(params)
  if '1' not in params['attempt']: 
  	return 'Chebyshev\'s Inequality by itself will give you the upper bound on the probability, what can we do to the answer to get the lower bound?'
  else: 
  	return ''