from hint_class_helpers.find_matches import find_matches


def check_attempt(params):
    final_pairs=find_matches(params)
    if len(final_pairs)>0:
        for node,value,ans_piece,attempt_piece in final_pairs:
            if value>20 or value != int(value):
                if attempt_piece != ans_piece:
                    return 'The sub-expression {0} is correct, it could also be written as {1}'.format(attempt_piece,ans_piece)
                else:
                    return 'The sub-expression {0} is correct.'.format(attempt_piece)
    return ""
