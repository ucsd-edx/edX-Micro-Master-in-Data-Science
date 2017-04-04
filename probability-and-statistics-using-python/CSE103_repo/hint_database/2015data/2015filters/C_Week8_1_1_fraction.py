def C_Week8_1_1_fraction(params):
  """ Written by bgl004 Wed Nov 18 2015 10:59:14 GMT-0800 (Pacific Standard Time)
  Conditional Hint for common fraction answers
  Written by Brandon Lee
  """
  # params = {'attempt': '', 'att_tree': [], 'answer': '', 'ans_tree': [], 'variables': [{'name':,'value':}]} 
  if params['attempt'] == '1\n' or params['attempt'] == '1/2':
    return 'Your answer should never be a fraction because the number of checks you do is always an integer. Remember, the Deterministic method states to check C1 (1 check) and if it\'s true, check C2 (totalling to 2 checks). If it checks C1 and finds it false, it stops checking. Thus, that means it only checked a total number of...'
  else:
    return ''