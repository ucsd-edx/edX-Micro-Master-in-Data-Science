def C_CombinedPracticeFinal_16_3_expected_value_algebra(params):
  """ Written by clao Mon Nov 30 2015 12:24:33 GMT-0800 (Pacific Standard Time)
  Remind students of the properties of expected value.
  """
  # params = {'attempt': '', 'att_tree': [], 'answer': '', 'ans_tree': [], 'variables': [{'name':,'value':}]} 
  import json
  print json.dumps(params)
  if '5*' not in params['attempt']: 
    return 'Remember that [\'E[X_{1} + X_{2}] = E[X_{1}] + E[X_{2}]\'] and [\'E[3X] = 3E[X]\'].'
  return ''