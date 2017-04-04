def C_CombinedPracticeFinal_11_1_set_of_cards_for_straight(params):
  """ Written by clao Mon Nov 30 2015 10:48:57 GMT-0800 (Pacific Standard Time)
  Making sure the student understands what set of cards they need for a striaght and how many there of these cards in a deck. 
  """
  # params = {'attempt': '', 'att_tree': [], 'answer': '', 'ans_tree': [], 'variables': [{'name':,'value':}]} 
  import json
  print json.dumps(params)
  if '16' in params['attempt']: 
  	return ''
  elif '4' not in params['attempt']: 
    return 'We need to get a 7 and an 8 on the turn and the river. How many choices do we have, regardless of whether we get 7 on the turn or 8 on the river or 8 on the turn and 7 on the river?'
  else: 
  	return ''