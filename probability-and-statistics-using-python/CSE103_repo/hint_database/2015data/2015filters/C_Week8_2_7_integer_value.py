def C_Week8_2_7_integer_value(params):
  """ Written by clao Wed Nov 18 2015 12:27:07 GMT-0800 (Pacific Standard Time)
  Checking is the answer if not a number
  """
  # params = {'attempt': '', 'att_tree': [], 'answer': '', 'ans_tree': [], 'variables': [{'name':,'value':}]} 
  import json
  import math
  print json.dumps(params)
  if math.isnan(float(params['attempt'])): 
  	return 'We\'re trying to find the constant c such that when you run the algorithm you will return the correct answer with a probability of 95%.'