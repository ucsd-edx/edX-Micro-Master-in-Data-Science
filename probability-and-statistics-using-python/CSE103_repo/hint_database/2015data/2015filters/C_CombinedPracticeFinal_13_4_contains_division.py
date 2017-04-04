def C_CombinedPracticeFinal_13_4_contains_division(params):
  """ Written by clao Mon Nov 30 2015 11:32:42 GMT-0800 (Pacific Standard Time)
  Check that they are dividing to get the conditional probability 
  """
  # params = {'attempt': '', 'att_tree': [], 'answer': '', 'ans_tree': [], 'variables': [{'name':,'value':}]} 
  import json
  print json.dumps(params)
  if '/' not in params['attempt']:
  	return 'We are trying to find the conditional probability of getting a set of all increasing 3-card sequences given that we have a set of 3-card sequence that starts with 9, so ultimately, we are finding the probability of getting a set of increasing 3-card sequences that start with 9. Remember that conditional proability can written as probability of A inersected with B over the probability of B, both of which we have calculated in previous parts.'
  else: 
  	return ''