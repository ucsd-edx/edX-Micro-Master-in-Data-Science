def C_CombinedPracticeFinal_16_2_probability_per_side(params):
  """ Written by clao Mon Nov 30 2015 12:18:53 GMT-0800 (Pacific Standard Time)
  Help students find the probability per side of the rigged dice.
  """
  # params = {'attempt': '', 'att_tree': [], 'answer': '', 'ans_tree': [], 'variables': [{'name':,'value':}]} 
  import json
  print json.dumps(params)
  if '+' not in params['attempt'] and '/' not in params['attempt']:
  	return 'Given that we have twice the probability of landing on the largest face of the rigged dice, we must find the new proabiliity of landing on any given face, by setting up an equation and setting that equal to 1, where the proability of landing on any particular face is 1/p except for the largest face where it is 2/p.'
  else: 
  	return ''