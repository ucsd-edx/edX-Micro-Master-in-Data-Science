from numpy import isinf
def classify_final_value(params):
    """ Written by Yoav Freund, Sat Sep 19 17:09:48 PDT 2015
    classifies the final value as: correct,inf, int, not_int
    return value and classification of it.
    """
    classification=[]

    att_tree=params['att_tree']
    if type(att_tree[0])==list:
        classification.append('expression')
        att_final_value=att_tree[0][1]
    else:
        classification.append('number')
        att_final_value=att_tree[1]

    ans_tree=params['ans_tree']
    if type(ans_tree[0])==list:
        ans_final_value=ans_tree[0][1]
    else:
        ans_final_value=ans_tree[1]
    
    if att_final_value==ans_final_value:
        classification.append('correct')
    if isinf(att_final_value):
        classification.append('Inf')
    if abs(int(att_final_value)-att_final_value)>0.1:
        classification.append("not int")
    else:
        classification.append("int")

    return att_final_value,classification
