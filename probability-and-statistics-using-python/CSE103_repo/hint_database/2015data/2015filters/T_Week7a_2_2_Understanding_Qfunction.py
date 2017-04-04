def T_Week7a_2_2_Understanding_Qfunction (params):
  """ Written by clao Mon Nov 09 2015 10:34:02 GMT-0800 (Pacific Standard Time)
  Helping the student understand which function to use to calculate the p value. 
  """
  # params = {'attempt': '', 'att_tree': [], 'answer': '', 'ans_tree': [], 'variables': [{'name':,'value':}]} 
  import json
  print json.dumps(params)
  return 'What function allows you to find the probability that a random variable is greater than x deviations from the mean? In other words what is the probability that a particular value is far from the range of likely values given that values are more likely to be close to the mean?'