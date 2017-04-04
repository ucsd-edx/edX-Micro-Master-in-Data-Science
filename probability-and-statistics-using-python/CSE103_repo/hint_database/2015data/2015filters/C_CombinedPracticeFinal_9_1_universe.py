def C_CombinedPracticeFinal_9_1_universe(params):
  """ Written by clao Mon Nov 30 2015 12:35:40 GMT-0800 (Pacific Standard Time)
  Defining the universe in this problem
  """
  # params = {'attempt': '', 'att_tree': [], 'answer': '', 'ans_tree': [], 'variables': [{'name':,'value':}]} 
  import json
  print json.dumps(params)
  if 'C' not in params['attempt']: 
    return 'We calculated the number of such cards we need to get a straight in the previous part. So know what is the universe of this set? How many given way can we obtain any 2 cards given the cards we are already dealt? From there we can find the conditional probabilty of obtaining a straight given that we are already dealt these 5 cards.'
  else: 
  	return ''