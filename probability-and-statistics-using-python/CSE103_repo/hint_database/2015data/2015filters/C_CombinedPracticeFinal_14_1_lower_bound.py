def C_CombinedPracticeFinal_14_1_lower_bound(params):
  """ Written by clao Mon Nov 30 2015 11:41:14 GMT-0800 (Pacific Standard Time)
  Relate Markov's inequality to the problem
  """
  # params = {'attempt': '', 'att_tree': [], 'answer': '', 'ans_tree': [], 'variables': [{'name':,'value':}]} 
  import json
  print json.dumps(params)
  if '/' not in params['attempt'] or '*' not in params['attempt']:
  	return 'If we let the RX X be the number of heads we get, we can use Markov\'s inequality to get the bound on the proability of getting at least a many heads i.e. E[X]/a. And we are given that the probability of getting a many heads. So we can use Markov\'s Inequality and the proability given to use to get the the lower bound on the number of times John tossed the coin or N.'
  else: 
    return ''