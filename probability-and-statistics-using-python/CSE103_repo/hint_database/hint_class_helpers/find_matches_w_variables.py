from expr_parser import webwork_parser
from expr_parser import Eval_parsed
from collections import deque
from collections import defaultdict
from find_matches import find_matches


def equal_len(variable_list):
    """ Check whether all variables has the same size of values to test """
    size_of_list = len(variable_list[variable_list.keys()[0]])
    for key in variable_list:
        if len(variable_list[key]) != size_of_list:
            return False
    return True

def extract_one_value_to_test(variable_values, index):
    """ Extract one value to test for each of the variable """
    variable_list = {}
    for key in variable_values:
        variable_list[key] = variable_values[key][index]
    return variable_list

def make_params_w_variables(ans_str, att_str, variable_values, index):
    """ make param using test value at the passed in index """
    v_list = extract_one_value_to_test(variable_values, index)
    return make_params(ans_str, att_str, v_list)

def find_matches_w_variables(ans_str, att_str, variable_values, test_all=False):
    """ return a list of hits """
    params = make_params_w_variables(ans_str, att_str, variable_values, 0)
    final_matches = find_matches(params)

    if test_all:
        #first check to make sure equal length
        if len(variable_values>1) and ~equal_len(variable_list):
            print 'need to make sure variables all have same number of values'
            return None

        size_of_value_list = len(variable_values[variable_values.keys()[0]])
        for i in xrange(size_of_value_list):
            params = make_params_w_variables(ans_str, att_str, variable_values, i)
            match = find_matches(params)
            if match != final_matches:
                return None
    return final_matches


def show_matching_group_w_variables(ans_str, att_str, variable_values, test_all=False):
    """ can test all values provided in variable_values
    and return a list of hits """
    matches = find_matches_w_variables(ans_str, att_str, variable_values, test_all)
    parse_tree_att = webwork_parser.parse_webwork(att_str)
    matching_exps = []
    if parse_tree_att[0] == None:
        print 'parse_tree empty'
        return None
    if matches:
        for m in matches:
            tree_index = [int(i)+1 for i in m[0].split('.')[1:]]
            node = parse_tree_att[0]
            for t in tree_index:
                node = node[t]
            matching_exps.append(att_str[node[0][1][0]:node[0][1][1]+1])
        return matching_exps
    else:
        return None




