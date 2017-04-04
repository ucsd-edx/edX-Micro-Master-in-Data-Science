def C_Week7a_5_5_should_reject(params):
  """ Written by beerye28 Mon Nov 09 2015 11:52:48 GMT-0800 (Pacific Standard Time)
 	  Description: Point out an important aspect of the confidence interval and null hypothesis
  """
  # params = {'attempt': '', 'att_tree': [], 'answer': '', 'ans_tree': [], 'variables': [{'name':,'value':}]} 
 
  if params['attempt'] == '-1' or params['attempt'] == '0':
  	return 'If our null hypothesis is not in our confidence interval, we definitely have to reject it.'
  else:
  	return ''