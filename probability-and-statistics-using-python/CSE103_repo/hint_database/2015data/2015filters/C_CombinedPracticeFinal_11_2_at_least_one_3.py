def C_CombinedPracticeFinal_11_2_at_least_one_3(params):
  """ Written by clao Mon Nov 30 2015 10:57:09 GMT-0800 (Pacific Standard Time)
  Inform the student that the question is asking for at least one 3, and remind them about the complement.
  """
  # params = {'attempt': '', 'att_tree': [], 'answer': '', 'ans_tree': [], 'variables': [{'name':,'value':}]} 
  import json
  print json.dumps(params)
  if 'C(43,2)' not in params['attempt'] or 'C(52-5-4)' not in params['attempt']: 
  	return 'We need at least one 3 in the turn or the river. Given that we need \'at least\' one 3, we can take the complement of that set, producing the set card 7-card hands that contain no 3. And we know that if we subtract from the universe of this set, in this case, picking the turn and the river from the rest of the deck, we are left with all the hands that do contain at least 1 3.'
  else: 
    return ''