def C_Week4_7_3_not_int(params):
  """ Written by yfreund Tue Oct 20 2015 21:33:12 GMT-0700 (PDT)
  the size of a set has to be an integer number
  """
  value,classes=classify_final_value(params)
  if 'not int' in classes:
    #print params['attempt'],value
    print 'The value of the expression you entered is %f, but the sze of set has to be a non-negative integer!'%value
  return ''