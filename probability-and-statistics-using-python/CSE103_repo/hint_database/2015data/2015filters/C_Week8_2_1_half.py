def C_Week8_2_1_half(params):
  """ Written by bgl004 Wed Nov 18 2015 11:56:10 GMT-0800 (Pacific Standard Time)
  Conditional hint for 1/2 or .5
  Written by Brandon Lee
  """
  # params = {'attempt': '', 'att_tree': [], 'answer': '', 'ans_tree': [], 'variables': [{'name':,'value':}]} 
  if params['attempt'] == '1/2' or params['attempt'] == '.5' or params['attempt'] == '0.5':
    return 'You need to find the average amount of time the algorithm will take. So "1/2" is half of the answer since there\'s a probability of 1/2 that the algorithm will take 1 second (Probability of 1/2 * 1 sec = 1/2 sec). Now you just have to add the other probability too (the one with n seconds). Use the same formula that I used to get 1/2! '
  else:
    return ''