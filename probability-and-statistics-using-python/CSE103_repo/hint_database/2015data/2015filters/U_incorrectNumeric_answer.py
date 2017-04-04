def U_incorrectNumeric_answer(params):
    """ Written by yfreund Tue Oct 13 2015 20:00:50 GMT-0700 
        Check if the answer is incorrect and a single number.
    """
    classification=classify_final_value(params)
    #classification=[]
    if ('number' in classification) and (not 'correct' in classification):
      	print params['attempt']
        return "Incorrect answer. Please enter an expression, not the final numerical result"
    else:
        return ""