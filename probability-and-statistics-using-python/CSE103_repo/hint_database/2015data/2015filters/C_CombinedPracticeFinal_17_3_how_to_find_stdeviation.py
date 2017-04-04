def C_CombinedPracticeFinal_17_3_how_to_find_stdeviation(params):
  """ Written by Brian Clark Tue Dec 01 2015 23:06:57 GMT-0800 (Pacific Standard Time)
  Remind students what variance and standard deviation are for a binomial distribution
  """
  # params = {'attempt': '', 'att_tree': [], 'answer': '', 'ans_tree': [], 'variables': [{'name':,'value':}]} 
  if params['attempt'] != '0':
  	return 'Remember, the variance of a binomial distribution is [`np(1-p)`] where n is the number of trials and p is probability of success. Also recall that [`\sqrt{var} = stdeviation`].'