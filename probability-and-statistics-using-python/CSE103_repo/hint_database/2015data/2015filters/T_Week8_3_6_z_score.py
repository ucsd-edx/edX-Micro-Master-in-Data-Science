def T_Week8_3_6_z_score(params):
  """ Written by clao Mon Nov 16 2015 12:05:25 GMT-0800 (Pacific Standard Time)
  Relate the z-score to the problem and remind the student of the equation. 
  """
  # params = {'attempt': '', 'att_tree': [], 'answer': '', 'ans_tree': [], 'variables': [{'name':,'value':}]} 
  import json
  print json.dumps(params)
  return 'There\'s some mean value of the random variable we care about (C), and some threshold for C such that when we take the majority result, the answer is actually correct (the threshold is part 1 of this  gives question). Now, if the particular value of C for some execution of this algorithm is a certain distance from the mean of C (E[C]) we will actually be incorrect when we take the majority result as our answer. The z-score gives this distance from the mean, in terms of standard deviations. Remember the z-score is given as [\'z =  \frac{x-\mu}{\sigma}\'] where [\'\mu\'] is the mean and [\'\sigma\'] is the standard deviation.'