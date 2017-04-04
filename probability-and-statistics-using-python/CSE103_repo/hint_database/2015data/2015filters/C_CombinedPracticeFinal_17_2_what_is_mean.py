def C_CombinedPracticeFinal_17_2_what_is_mean(params):
  """ Written by Brian Clark Tue Dec 01 2015 23:00:04 GMT-0800 (Pacific Standard Time)
  Remind students how to calculate mean
  """
  # params = {'attempt': '', 'att_tree': [], 'answer': '', 'ans_tree': [], 'variables': [{'name':,'value':}]} 
  if params['attempt'] != '0':
  	return 'If the monkey picks an answer by random, the probability that he gets a problem right is 1/(#possible answers). Multiply this by the total number of problems to get the mean.'