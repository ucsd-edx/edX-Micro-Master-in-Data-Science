from expr_parser import webwork_parser
from expr_parser import Eval_parsed
from collections import deque
from collections import defaultdict


######## Make a list of dictionaries ##########
def make_params(ans_str, att_str, variable_list={}):
    """
    input: answer string, attemp string,
    optional input: variable dictionary {'variable_name':value to test, 'variable_name2':value}
    return: list of dict with format
        'user_id':d['user_id'],'answer':d['answer'], 'attempt':d['attempt'],
        'ans_tree':eval_tree,'att_tree':eval_tree_att
    """

    parse_tree = webwork_parser.parse_webwork(ans_str)
    if parse_tree[0] == None:
        return {}
    eval_tree = Eval_parsed.eval_parsed(parse_tree[0], variable_list)
    if eval_tree == None:
        return {}

    parse_tree_att = webwork_parser.parse_webwork(att_str)
    if parse_tree_att[0] == None:
        return {}
    eval_tree_att = Eval_parsed.eval_parsed(parse_tree_att[0], variable_list)
    if eval_tree_att == None:
        return {}

    params = {'answer':ans_str, 'attempt':att_str, 'ans_tree':eval_tree, 'att_tree':eval_tree_att}
    return params



