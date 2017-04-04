def C_CombinedPracticeFinal_13_2_constant(params):
  """ Written by clao Mon Nov 30 2015 11:23:13 GMT-0800 (Pacific Standard Time)
  <Filter Description goes here>
  """
  # params = {'attempt': '', 'att_tree': [], 'answer': '', 'ans_tree': [], 'variables': [{'name':,'value':}]} 
  import json
  print json.dumps(params)
  if len(params['attempt']) > 1:
  	return 'Given that t is a constant, and the sequence must be in an increasing order, how many values of [\'x_{2}\'] are there?'
  else: 
    return ''