def C_CombinedPracticeFinal_16_4_markov(params):
  """ Written by clao Mon Nov 30 2015 12:28:43 GMT-0800 (Pacific Standard Time)
  Reminding the students of the different parts of Markov's Inquality
  """
  # params = {'attempt': '', 'att_tree': [], 'answer': '', 'ans_tree': [], 'variables': [{'name':,'value':}]} 
  import json
  print json.dumps(params)
  if '/' not in params['attempt']: 
    return 'We know that the probability that the expected value of the sum of the rigged dice and fair dice, or Y,  is greater than k is less than or equal to 0.5. And we already solved for the expected value of Y previously. So now we just need to solve for the lower bound k using this Markov\s Inequality.'
  else: 
  	return ''