def T_Week8_3_4_majority_answer(params):
  """ Written by clao Mon Nov 16 2015 11:39:20 GMT-0800 (Pacific Standard Time)
  Explaining the majority answer in relation to Chebyshev's Inequality 
  """
  # params = {'attempt': '', 'att_tree': [], 'answer': '', 'ans_tree': [], 'variables': [{'name':,'value':}]} 
  import json
  print json.dumps(params)
  return 'There\'s some mean value of the random variable C, and some threshold for C such that when we take the majority result, the answer is actually correct (the threshold is part 1 of this question). If the particular value of C for some execution of this algorithm is a certain distance from the mean of C, E[C], we will actually be incorrect when we take the majority result as our answer. What is this distance from the mean?'