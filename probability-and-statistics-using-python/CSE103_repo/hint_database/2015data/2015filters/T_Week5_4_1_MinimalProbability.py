def T_Week5_4_1_MinimalProbability(params):
  """ Written by nima Thu Oct 29 2015 09:52:59 GMT-0700 (PDT)
  <Filter Description goes here>
  """
  # params = {'attempt': '', 'att_tree': [], 'answer': '', 'ans_tree': [], 'variables': [{'name':,'value':}]} 
  import json
  print json.dumps(params)
  return 'Assume your mean noon-time temperature for September days in San Diego is 24 and the problem is asking the minimal probability that the noon-time temperature of a september days is between 12.3 and 35.7. This problem is equivalent to ask you the minimum value of the probabily P(12.3 <= X <= 35.7). In order to use Chebyshev inequality, you should notice that this probability is equal to P(12.3 - 24 <= X - 24 <= 35.7 - 24), which is equal to P(|X - 24| <= 11.7) = 1 - P(|X - 24| > 11.7) = 1 - P(|X - 24| >= 11.7). Know you can solve the problem.'