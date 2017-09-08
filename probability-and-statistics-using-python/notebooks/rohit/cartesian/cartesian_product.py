import itertools


def cartesian_product(A, B):
    '''
    Return the cartesian product A x B
    '''
    C = []
    for i in itertools.product(A, B):
        C.append(i)
    return C
