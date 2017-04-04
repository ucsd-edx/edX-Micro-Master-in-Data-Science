# Script to search for the right hint
# Given problem ID, search in hint_dict, find related hint_classes, then output the hint if certain condition is satisfied
# Name: Zhipeng Yan
# Date: Sep 21, 2016

__author__ = 'zpyan'

import pickle, json, logging, types
# import logging.handlers
from pydoc import locate


def search(id_str, p):
    #id_str is like: cse103fall2016week1problem1part1

    # constants
    json_name = 'problems_mapping.json'
    pickle_name = 'dict.pkl'
    log_path = 'log/conditional_hint.log'
    hint_class_folder = 'hint_class'

    # logging settings
    # logger = logging.getLogger('conditional_hint.search')
    # handler = logging.handlers.RotatingFileHandler(log_path, maxBytes = 262144, backupCount = 32)
    # formatter = logging.Formatter('%(asctime)s - %(names)s - %(levelname)s - %(message)s')
    # handler.setFormatter(formatter)
    # logger.addHandler(handler)
    # logger.setLevel(logging.INFO)

    # id parsing
    week_pos, problem_pos, part_pos = \
            id_str.find('week'), id_str.find('problem'), id_str.find('part')
    week_id, problem_id, part_id = \
            id_str[week_pos+4:problem_pos], id_str[problem_pos+7:part_pos], id_str[part_pos+4:]
    # print week_id, problem_id, part_id

    if not (week_id.isdigit() and problem_id.isdigit() and part_id.isdigit()):
        # logger.error('week/problem id not found.')
        return ""

    # loading mapping
    with open(json_name, 'r') as r:
        try:
            mapping_dict = json.load(r)
        except EOFError or ValueError:
            # logger.error(json_name + ' is broken.')
            return ""

    try:
        problem_id = 'Week{}_Problem{}'.format(week_id, problem_id)
        problem_key = mapping_dict[problem_id]
    except KeyError:
        # logger.error(problem_id + ' has not yet been added.')
        return ""

    # loading hint dictionary
    with open(pickle_name, 'r') as r:
        try:
            hint_dict = pickle.load(r)
        except EOFError or ValueError:
            # logger.error(pickle_name + ' is broken')
            return ""

    try:
        candidate_hint_list = hint_dict[problem_key]
    except KeyError:
        # logger.error(problem_key + ' has not yet been added')
        return ""

    # searching for appropriate hint
    for i in xrange(len(candidate_hint_list)):
        candidate_hint_class = locate(candidate_hint_list[i])
        if candidate_hint_class is None:
            # logger.error('Hint class [{}] not found. Could be file missing or class name not consistent with the file name.'.format(candidate_hint_list[i]))
            continue

        if type(candidate_hint_class) != types.ClassType:
            # logger.error(candidate_hint_list[i] + ' is not a class.')
            continue

        candidate_hint = candidate_hint_class()
        hint_content, hint_answer = candidate_hint.check_attempt(p)
        if hint_content:
            # logger.info('hint found')
            return hint_content, hint_answer

    # logger.info('No appropriate hint found')
    return ""
