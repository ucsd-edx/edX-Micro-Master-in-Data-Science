def C_CombinedPracticeFinal_13_3_contains_addition(params):
  """ Written by clao Mon Nov 30 2015 11:27:29 GMT-0800 (Pacific Standard Time)
  Remind students of the task that they are present 
  """
  # params = {'attempt': '', 'att_tree': [], 'answer': '', 'ans_tree': [], 'variables': [{'name':,'value':}]} 
  import json
  print json.dumps(params)
  if '+' not in params['attempt']: 
  	return 'We are repeating what you did previouly, summing over all the possible values of [\'x_{2}\'], but over all possible vlaues of t.'
  else: 
    return ''