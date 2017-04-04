def C_CombinedPracticeFinal_10_1_complement(params):
  """ Written by clao Mon Nov 30 2015 10:25:14 GMT-0800 (Pacific Standard Time)
  Remind the student to think about the complement and subtracting from a bigger set rather than adding it all together.
  """
  # params = {'attempt': '', 'att_tree': [], 'answer': '', 'ans_tree': [], 'variables': [{'name':,'value':}]} 
  import json
  print json.dumps(params)
  if 'C(20,5)' not in params['attempt']:
  	return 'We are looking for the size of the set that contains no card smaller than 7 and contains at least one face card. The key words here are \'at least\'. When seeing these words, we generally like to use the complement so that it is much easier to calculate. Try taking the complement of that set and subtracting the size of that result from the size of the other set to obtain the result that we want.'
  else:
  	return ''