def C_CombinedPracticeFinal_10_3_divide(params):
  """ Written by clao Mon Nov 30 2015 10:41:49 GMT-0800 (Pacific Standard Time)
  Check if the student is putting a fraction or a '/' in his/her answer in order to check whether they know the equation for conditional probability.
  """
  # params = {'attempt': '', 'att_tree': [], 'answer': '', 'ans_tree': [], 'variables': [{'name':,'value':}]} 
  import json
  print json.dumps(params)
  if '/' not in params['attempt']:
    return 'The conditional probability of A given B is the probability of the intersection of A and B over the probability of B. We calculated both parts previously. Now we just need to put them together.'
  else: 
  	return ''