def T_Week8_3_5_upper_bound(params):
  """ Written by clao Mon Nov 16 2015 11:51:37 GMT-0800 (Pacific Standard Time)
  Relating the upper bound to the smallest integer value for n such that the 'majority' algorithm makes an error
  """
  # params = {'attempt': '', 'att_tree': [], 'answer': '', 'ans_tree': [], 'variables': [{'name':,'value':}]} 
  import json
  print json.dumps(params)
  return 'We have already calculated the probability that your majority algorithm will produce an incorrect answer. Now, using Chebyshev\'s Inequality and the upper bound given, 0.05, find the smallest n such that the algorithm will produce an incorrect majority.'