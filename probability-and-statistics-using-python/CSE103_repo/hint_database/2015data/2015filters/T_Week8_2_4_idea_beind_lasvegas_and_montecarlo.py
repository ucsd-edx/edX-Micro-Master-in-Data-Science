def T_Week8_2_4_idea_beind_lasvegas_and_montecarlo(params):
  """ Written by clao Mon Nov 16 2015 10:39:25 GMT-0800 (Pacific Standard Time)
  Making sure that the student understands the concept of Monte Carlo and Las Vegas algorithms
  """
  # params = {'attempt': '', 'att_tree': [], 'answer': '', 'ans_tree': [], 'variables': [{'name':,'value':}]} 
  import json
  print json.dumps(params)
  return 'A Las Vegas algorithm always produces the correct output, but takes a varying amount of time to produce an output. A Monte Carlo algorithm always completes within the same amount of time, but may not produce the correct output. To tranforms a Las Vegas algorithm to a Monte Carlo, we set the probability that it returned the wrong answer to at most 5%, found the time it would at most take to run this new algorithm. What is this time in relation to T(n)?'