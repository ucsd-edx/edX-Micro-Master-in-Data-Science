def T_Week7a_2_3_name(params):
  """ Written by clao Mon Nov 09 2015 11:02:45 GMT-0800 (Pacific Standard Time)
  Helps the student understand the question in terms of alpha
  """
  # params = {'attempt': '', 'att_tree': [], 'answer': '', 'ans_tree': [], 'variables': [{'name':,'value':}]} 
  import json
  print json.dumps(params)
  return 'Given that alpha is 0.05, can you reject the null hypothesis, given the p value you found?'