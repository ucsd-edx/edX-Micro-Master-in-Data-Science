def C_Week3_10_1_Power(params):
  """ Written by yfreund Wed Oct 14 2015 15:29:47 GMT-0700 (PDT)
  <Filter Description goes here>
  """
  # params = {'attempt': '', 'att_tree': [], 'answer': '', 'ans_tree': [], 'variables': [{'name':,'value':}]}
  operator=params['att_tree'][0][0]
  if operator=='^' or operator=='**':
    print params['attempt']
    return 'You are correct in that the expression is of the form a^b. But you choice for a or b is incorrect'
  else:
  	return ''