def T_Week7a_2_1_Identify_Distribution(params):
  """ Written by clao Mon Nov 09 2015 10:22:27 GMT-0800 (Pacific Standard Time)
  Tells the student to first identify the distribution being described in the problem in order to calculate the z-score.
  """
  # params = {'attempt': '', 'att_tree': [], 'answer': '', 'ans_tree': [], 'variables': [{'name':,'value':}]} 
  import json
  print json.dumps(params)
  return 'First identify the type of distribution the problem falls under and then calculate the mean and standard deviation based on that distribution. In this problem, there are two outcomes: the psychic can get a card correct or the psychic can get a card wrong. What type of distribution does this sound like?'