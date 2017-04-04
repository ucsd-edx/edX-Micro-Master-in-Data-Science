def C_Week8_8_3_nOrLogN(params):
  """ Written by bgl004 Wed Nov 18 2015 10:38:03 GMT-0800 (Pacific Standard Time)
  Condition where n or log(n) is inputted.
  Written by Brandon Lee
  """
  # params = {'attempt': '', 'att_tree': [], 'answer': '', 'ans_tree': [], 'variables': [{'name':,'value':}]} 
  if params['attempt'] == 'n' or params['attempt'] == 'logn' or params['attempt'] == 'log(n)':
  	return 'Your guess is too high! Here\'s a hint: "Expected search time" is the same thing as "Expected query time". Wasn\'t this calculated somewhere above?'
  else:
  	return ''