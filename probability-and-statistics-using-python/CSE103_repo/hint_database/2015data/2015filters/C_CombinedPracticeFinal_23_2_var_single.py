def C_CombinedPracticeFinal_23_2_var_single(params):
  """ Written by beerye28 Tue Dec 01 2015 23:51:33 GMT-0800 (Pacific Standard Time)
  Explain the variance of a single coin toss
  """
  if params['attempt'] != '1/4' or params['attempt'] != '0.25' or params['attempt'] != '.25':
  	return 'Remember variance of a binomial distribution is np(1-p). Here, we only have 1 attempts, and our probability is .5.'
  else:
    return ''