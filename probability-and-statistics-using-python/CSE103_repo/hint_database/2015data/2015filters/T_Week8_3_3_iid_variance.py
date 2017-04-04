def T_Week8_3_3_iid_variance(params):
  """ Written by clao Mon Nov 16 2015 11:14:23 GMT-0800 (Pacific Standard Time)
  <Filter Description goes here>
  """
  # params = {'attempt': '', 'att_tree': [], 'answer': '', 'ans_tree': [], 'variables': [{'name':,'value':}]} 
  import json
  print json.dumps(params)
  return 'We see that [\'C_{1}\'], [\'C_{2}\'], ... [\'C_{n}\'] are idependent and identically distributed, so Var(C) can be written as Var([\'C_{1}\']) + Var[\'C_{2}\'] + ... + [\'C_{n}\']. First calculate the individual variances, then sum them all up.'