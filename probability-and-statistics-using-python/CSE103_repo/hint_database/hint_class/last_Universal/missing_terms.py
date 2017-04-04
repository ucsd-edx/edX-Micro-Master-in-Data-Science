from hint_class_helpers.Parse_tree_properties import collect_terms

def check_attempt(params):
    ans_terms=collect_terms(params['ans_tree'])
    att_terms=collect_terms(params['att_tree'])
    missing=set(ans_terms) - set(att_terms)- set([0,1])
    #print 'unrecognized=',unrecognized
    if len(missing)>0:
        inattemptstring= ', '.join([str(x) for x in set(att_terms)-set([1])])
        missingstring=', '.join([str(x) for x in set(missing)-set([1])])
        hint='The numbers in your answer are: '+inattemptstring

        if len(missing)>1:
            hint+='. You are not using the numbers '
            hint+= missingstring+' used in the question. '
            hint+='Figure out how to use these numbers in your answer.'
        else:
            hint+='. You are not using the number '
            hint+= missingstring+' used in the question. '
            hint+='Figure out how to use this number in your answer.'

        return hint
    return ''


