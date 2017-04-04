def C_Week8_8_1_oneInAMillion(params):
  """ Written by bgl004 Wed Nov 18 2015 10:22:02 GMT-0800 (Pacific Standard Time)
  Condition for when they input 1/1,000,000
  Written by Brandon Lee
  """
  # params = {'attempt': '', 'att_tree': [], 'answer': '', 'ans_tree': [], 'variables': [{'name':,'value':}]} 
  if params['attempt'] == '1/1000000' or params['attempt'] == '1\\1000000':
  	return 'If you used the equation in the line right above this (about "some bin getting log(n) balls") then allow me to reassure you that you\'re on the right track, though 1/n isn\'t going to work. Why not try using a part of the equation that has the "greater than or equals" sign?'
  else:
  	return ''