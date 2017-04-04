def C_CombinedPracticeFinal_13_1_order(params):
  """ Written by clao Mon Nov 30 2015 11:19:36 GMT-0800 (Pacific Standard Time)
  <Filter Description goes here>
  """
  # params = {'attempt': '', 'att_tree': [], 'answer': '', 'ans_tree': [], 'variables': [{'name':,'value':}]} 
  import json
  print json.dumps(params)
  if '*' not in params['attempt']: 
  	return 'We\'re taking order into account now since we are using sequences. After picking one card, how many cards do we have left to choose from?'
  else: 
    return ''