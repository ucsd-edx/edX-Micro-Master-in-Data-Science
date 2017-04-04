from hint_class_helpers.Parse_tree_properties import collect_terms

def check_attempt(params):
    ans_terms=collect_terms(params['ans_tree'])
    att_terms=collect_terms(params['att_tree'])
    unrecognized=set(att_terms) - set(ans_terms)-set([0,1])
    #print 'unrecognized=',unrecognized
    if len(unrecognized)>0:
        inanswerstring= ','.join([str(x) for x in set(ans_terms)-set([1])])
        unrecstring=','.join([str(x) for x in set(unrecognized)-set([1])])
        hint='The numbers in the question are: '+inanswerstring
        hint+='. Where did '+unrecstring+' come from? '
        hint+='Please replace '+unrecstring+' with expressions that use the numbers '+inanswerstring
        return hint
    return ''
