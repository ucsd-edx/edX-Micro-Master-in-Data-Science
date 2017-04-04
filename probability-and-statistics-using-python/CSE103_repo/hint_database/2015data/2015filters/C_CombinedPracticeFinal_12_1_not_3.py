def C_CombinedPracticeFinal_12_1_not_3(params):
  """ Written by clao Mon Nov 30 2015 11:10:14 GMT-0800 (Pacific Standard Time)
  Remind students that need to consider all the possibilites that they need to win. 
  """
  # params = {'attempt': '', 'att_tree': [], 'answer': '', 'ans_tree': [], 'variables': [{'name':,'value':}]} 
  import json
  print json.dumps(params)
  if '3' not in params['attempt']: 
  	return 'Consider all the possibilities of cards that can appear on the turn and river that will allow your opponent to win.'
  else: 
  	return ''