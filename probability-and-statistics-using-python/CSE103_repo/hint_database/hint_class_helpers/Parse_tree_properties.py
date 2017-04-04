def collect_terms(tree):
    """recieves an eval-tree for an expression and returns a list of the terms (numbers or variables) in the expressions 

    :param tree: an eval-tree representing an expression.
    :returns: a list of terms (either numbers or strings)

    """
    
    if len(tree)==4 and tree[0]=='X':
        return [tree[1]]
    else:
        answer=[]
        for leaf in range(1,len(tree)):
            answer+=collect_terms(tree[leaf])
        return answer
