def C_Week7a_7_3_Conditional(params):
  """ Written by bgl004 Mon Nov 09 2015 12:04:28 GMT-0800 (Pacific Standard Time)
  Reminder of what the chi statistic means.
  Written by Brandon Lee
  """
  # params = {'attempt': '', 'att_tree': [], 'answer': '', 'ans_tree': [], 'variables': [{'name':,'value':}]} 
  if params['attempt'] == '-1':
    return 'A higher X^2 value means that it is more likely that your hypothesis is incorrect.'
  else:
    return ''