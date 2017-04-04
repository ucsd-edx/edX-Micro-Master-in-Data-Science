def T_Week8_3_2_rules_of_expectedvalue(params):
  """ Written by clao Mon Nov 16 2015 11:00:11 GMT-0800 (Pacific Standard Time)
  
  """
  # params = {'attempt': '', 'att_tree': [], 'answer': '', 'ans_tree': [], 'variables': [{'name':,'value':}]} 
  import json
  print json.dumps(params)
  return 'Remember, E[X] where X = [\'X_{1}\'] + [\'X_{2}\'] is E[X] = E[\'X_{1}\'] + E[\'X_{2}\']. So first calculate the expected value of the individual ith trials of C i.e. [\'C_{1}\'] and then calculate the sum of individual trials.'