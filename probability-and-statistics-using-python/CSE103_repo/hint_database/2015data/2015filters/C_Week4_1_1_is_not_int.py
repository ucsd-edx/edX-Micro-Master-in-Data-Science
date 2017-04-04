def C_Week4_1_1_is_not_int(params):
  """ Written by yfreund Thu Oct 22 2015 14:56:54 GMT-0700 (PDT)
     The enumerator is an integer
  """
  hint=''
  value,classes=classify_final_value(params)
  if 'not int' in classes:
    hint='The expression you are asked to write is the unnormalized probability which is a sum of integers. The value of the expression you wrote is %f'%value
    #print hint
  
  return hint