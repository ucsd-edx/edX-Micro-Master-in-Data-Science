def C_CombinedPracticeFinal_15_2_symmetric(params):
  """ Written by clao Mon Nov 30 2015 12:05:40 GMT-0800 (Pacific Standard Time)
  Remind students that the dsitribution is symmetric.
  """
  # params = {'attempt': '', 'att_tree': [], 'answer': '', 'ans_tree': [], 'variables': [{'name':,'value':}]} 
  import json
  print json.dumps(params)
  if '/2' not in params['attempt'] or '*0.5' not in params['attempt'] or '*1/2' not in params['attempt']: 
  	return 'Chebyshev\'s Inequality gives you a range around the mean, so both above the mean and below the mean. We only want the bound for breaking this record high, so we don\'t need the probability of the temperature being below the mean. We also know that the distribution is symmetric, so the probability of being a certain distance above the mean is equivalent to being a certain distance below the mean. What can we do then in order to get rid of the probability of being a certain distance below the mean?'
  else: 
  	return ''