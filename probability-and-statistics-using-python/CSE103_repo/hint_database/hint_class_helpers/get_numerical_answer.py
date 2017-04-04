
def get_numerical_answer(eval_tree):
    """Get the final value from and evaluation tree"""
    if type(eval_tree[0])==list:
        return eval_tree[0][1]
    else:
        return eval_tree[1]


