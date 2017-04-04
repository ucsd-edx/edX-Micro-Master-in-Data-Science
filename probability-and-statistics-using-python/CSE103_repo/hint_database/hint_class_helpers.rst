hint_class_helpers
==================

☤ Subpackages
-------------

**expr_parser**

for parsing evaluating students answer

****

☤ Submodules
------------

**make_params**

**find_matches**

**find_matches_w_variables**

**get_conditional_hints**

**get_numerical_answer**

**get_universal_hints**

**NumericalAnswer**

**Parse_tree_properties**

**classify_final_value**

**common_subexpressions**

****

☤ How to use module fuctions
----------------------------

**make_params**

*this functions makes params from correct answer string and students attempt string, and return a dict*

*most of the following fuctions will use the params output as input*

INPUT: answer string, attemp string,

OPTIONAL INPUT: variable dictionary {'variable_name':value to test, 'variable_name2':value}

RETURN: list of dict with format {'user_id':d['user_id'],'answer':d['answer'], 'attempt':d['attempt'],'ans_tree':eval_tree,'att_tree':eval_tree_att}


.. code:: python

    from make_params import make_params
    ans="2*3"
    att="2*2"
    params=make_params(ans, att)
    print params
    {'answer': '2*3', 'att_tree': [['*', 4.0, [0, 2], 'R'], ['X', 2.0, [0, 0], 'R.0'], ['X', 2.0, [2, 2], 'R.1']], 'ans_tree': [['*', 6.0, [0, 2], 'R'], ['X', 2.0, [0, 0], 'R.0'], ['X', 3.0, [2, 2], 'R.1']], 'attempt': '2*2'}

----

**find_matches**

*receive answer parameters and return a list of hits between students attempt answer and correct answer*
*using the params form the above make_params example*

INPUTS: answer parameters dict from make_params fuction
OUTPUTS: a list of matching results

.. code:: python

    from find_matches import find_matches

    print params
    {'answer': '2*3', 'att_tree': [['*', 4.0, [0, 2], 'R'], ['X', 2.0, [0, 0], 'R.0'], ['X', 2.0, [2, 2], 'R.1']], 'ans_tree': [['*', 6.0, [0, 2], 'R'], ['X', 2.0, [0, 0], 'R.0'], ['X', 3.0, [2, 2], 'R.1']], 'attempt': '2*2'}

    print find_matches(params)
    [('R.0', 2.0, '2', '2')]

----

**find_matches_w_variables**

*receive correct answers, student's attempts and variables list for check and return a list of hits between students attempt answer and correct answer*

def find_matches_w_variables(ans_str, att_str, variable_values, test_all=False):

INPUTS: string of correct answers, string of students's attempts, dict of variable lists

OUTPUTS: a list of matching results

.. code:: python

    from find_matches_with_variables import find_matches_with_variables

    att="2*a"
    ans="2*a"
    values={'a': [1, 2, 3]}
    print find_matches_w_variables(ans, att, values)
    [('R', 2.0, '2*a', '2*a')]

    att="3*a"
    find_matches_w_variables(ans, att, values)
    [('R.1', 1, 'a', 'a')]

----

**get_conditional_hints**

*get conditional hints*

def get_conditional_hints(hint_text_id, i, params):

.. code:: python

    from get_conditional_hints import get_conditional_hints

----

**get_numerical_answer**

*receive evaluation tree and return the final numerical value*

def get_numerical_answer(eval_tree):

INPUT: evaluation tree

OUPUTS: numerical answer

.. code:: python

    from get_numerical_answer import get_numerical_answer
    ans="2*3"
    att="2*2"
    params=make_params(ans, att)
    print params
    {'answer': '2*3', 'att_tree': [['*', 4.0, [0, 2], 'R'], ['X', 2.0, [0, 0], 'R.0'], ['X', 2.0, [2, 2], 'R.1']], 'ans_tree': [['*', 6.0, [0, 2], 'R'], ['X', 2.0, [0, 0], 'R.0'], ['X', 3.0, [2, 2], 'R.1']], 'attempt': '2*2'}

    print get_numerical_answer(params['att_tree'])
    4
    print get_numerical_answer(params['ans_tree'])
    6

----

**get_universal_hints**

*receive answer parametes and return hints from first universal hints or first universal hints*

.. code:: python

    from get_universal_hints import get_last_universal_hints
    from get_universal_hints import get_first_universal_hints

----

**NumericalAnswer**

*Check the students attemp is valid or not*

INPUT: student answers params

OUTPUTS: two string, not valid if not all empty

.. code:: python

    import NumericalAnswer

----

**Parse_tree_properties**

*recieves an eval-tree for an expression and returns a list of the terms (numbers or variables) in the expressions*

def collect_terms(tree):

INPUTS: a evaluation tree

OUTPUTS: a list of the terms (numbers or variables) in the expressions

.. code:: python

    from Parse_tree_properties import collect_terms

    ans="2*3"
    att="2*2"
    params=make_params(ans, att)
    print params
    {'answer': '2*3', 'att_tree': [['*', 4.0, [0, 2], 'R'], ['X', 2.0, [0, 0], 'R.0'], ['X', 2.0, [2, 2], 'R.1']], 'ans_tree': [['*', 6.0, [0, 2], 'R'], ['X', 2.0, [0, 0], 'R.0'], ['X', 3.0, [2, 2], 'R.1']], 'attempt': '2*2'}

    print collect_terms(params['att_tree'])
    [2.0, 2.0]
    print collect_terms(params['ans_tree'])
    [2.0, 3.0]

----

**classify_final_value**

*classifies the final value as: correct,inf, int, not_int return value and classification of it*

def classify_final_value(params):

INPUTS: studets answer parameters

OUTPUTS: students answer value, a list of classification results

.. code:: python

    from classify_final_value import classify_final_value

    ans="2*3"
    att="2*2"
    params=make_params(ans, att)
    print params
    {'answer': '2*3', 'att_tree': [['*', 4.0, [0, 2], 'R'], ['X', 2.0, [0, 0], 'R.0'], ['X', 2.0, [2, 2], 'R.1']], 'ans_tree': [['*', 6.0, [0, 2], 'R'], ['X', 2.0, [0, 0], 'R.0'], ['X', 3.0, [2, 2], 'R.1']], 'attempt': '2*2'}

    print classify_final_value(params)
    (4.0, ['expression', 'int'])


---

**common_subexpressions**

*The function find_matches takes as input two parsed and evaluated trees, one for the correct answer and one for the attempt.It finds the subexpressions that match between the correct and the attempt and returns it as a list of tuples of the form (node,value,answer_part,attempt_part)*

INPUTS: students answer parameters

OUTPUTS: a list of tuples of the form (node,value,answer_part,attempt_part)

.. code:: python

    import common_subexpressions

----
