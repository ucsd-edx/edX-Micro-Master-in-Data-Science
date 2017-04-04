def T_Week5_7_2_BiasCoinFirstHead(params):
  """ Written by nima Wed Oct 28 2015 16:06:24 GMT-0700 (PDT)
  <Filter Description goes here>
  """
  # params = {'attempt': '', 'att_tree': [], 'answer': '', 'ans_tree': [], 'variables': [{'name':,'value':}]} 
  import json
  print json.dumps(params)
  return 'Again, you need to use the equation r+2pow(r,2) +3pow(r,3) + ... = r/pow(1-r, 2). When computing the expectation, you need sum over k*pow(1-p,k-1). Note, pow(1-p,k-1)= 1/(1 - p)pow(1 - p,k)'