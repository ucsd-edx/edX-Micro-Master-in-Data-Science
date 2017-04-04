def C_CombinedPracticeFinal_12_2_complement(params):
  """ Written by clao Mon Nov 30 2015 11:14:01 GMT-0800 (Pacific Standard Time)
  Remind students to use the complement method of computing the answer.
  """
  # params = {'attempt': '', 'att_tree': [], 'answer': '', 'ans_tree': [], 'variables': [{'name':,'value':}]} 
  import json
  print json.dumps(params)
  if '1' not in params['attempt']: 
    return 'In the first part you calculated all the possibilities that your opponent can win. Using that, you can calculate the probability that your opponent can win. And if you know the probability that your opponent wil win, you know the probability that you opponent will lose, and therefore, the probability that you will win.'
  else: 
  	return ''