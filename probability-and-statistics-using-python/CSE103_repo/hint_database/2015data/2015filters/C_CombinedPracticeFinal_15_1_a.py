def C_CombinedPracticeFinal_15_1_a(params):
  """ Written by clao Mon Nov 30 2015 12:00:20 GMT-0800 (Pacific Standard Time)
  Inform students of what a and k are.
  """
  # params = {'attempt': '', 'att_tree': [], 'answer': '', 'ans_tree': [], 'variables': [{'name':,'value':}]} 
  import json
  print json.dumps(params)
  if '/' not in params['attempt']: 
    return 'We want to find the probability of the temperature being in this range. Chebyshev\'s Inequality gives the proability of being in a certain range around the mean or a distance a from the mean. In terms of standard deviations, k standard deviations away from the mean. How far are these values that are given to you away from the range? That is a your a. (or if your answer is in terms of standard deviations, that is your k).'
  else: 
  	return ''