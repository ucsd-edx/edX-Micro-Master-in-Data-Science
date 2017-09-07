import itertools


def cartesian_product(A, B):
    C = []
    for i in itertools.product(A, B):
        C.append(i)
    return C
