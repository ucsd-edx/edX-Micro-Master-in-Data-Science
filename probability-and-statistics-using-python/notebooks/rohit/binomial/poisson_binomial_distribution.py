import numpy as np


def choose_iter(elements, length):
    for i in range(0, len(elements)):
        if length == 1:
            yield elements[i]
        else:
            for next in choose_iter(elements[i + 1:len(elements)], length - 1):
                yield elements[i] * np.prod(next)


def total_prob(probs, k):
    return np.sum(choose_iter(probs, k))


print(total_prob([0.2, .5, .3], 2))
