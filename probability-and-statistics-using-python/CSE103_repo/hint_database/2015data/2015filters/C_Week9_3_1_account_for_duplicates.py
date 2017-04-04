def C_Week9_3_1_account_for_duplicates(params):
  """ Written by beerye28 Mon Nov 23 2015 10:48:28 GMT-0800 (Pacific Standard Time)
  Remind students to account for duplicate document pairs
  """
  # params = {'attempt': '', 'att_tree': [], 'answer': '', 'ans_tree': [], 'variables': [{'name':,'value':}]} 
  
  if params['attempt'] == '(n-1)n' or params['attempt'] == '(n-1)*n' or params['attempt'] == 'n(n-1)' or params['attempt'] == 'n*(n-1)':
    return 'You are close! Remember to account for duplicate document pairs in your answer!'
  else:
    return ''