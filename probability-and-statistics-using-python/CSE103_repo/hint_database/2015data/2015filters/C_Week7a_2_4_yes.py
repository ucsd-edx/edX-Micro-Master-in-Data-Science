def C_Week7a_2_4_yes(params):
  """ Written by clao Mon Nov 09 2015 11:27:49 GMT-0800 (Pacific Standard Time)
  Conditional hint based on wrong answer, 'yes'; returns time-based hint
  """
  # params = {'attempt': '', 'att_tree': [], 'answer': '', 'ans_tree': [], 'variables': [{'name':,'value':}]} 
  import json
  print json.dumps(params)
  if params['attempt'] == 'yes' or params['attempt'] == 'Yes' or params['attempt'] == 'YES': 
    return 'Given alpha = 0.01, can we reject the null hypothesis, given the p value you found?'
  else:
  	return ''