```python
from math import factorial as fac
a = random.randrange(2,3,1)
n = fac(26)/fac(26-1)
b = random.randrange(3,6,1)
c = b + 1
d = int(c * fac(26)/fac(26-a) + 1)

solution1 = "P(26,{0})".format(a)
solution2 = "({1} - 1) * P(26,{0}) + 1".format(a,b)
solution3 = "{0} + 1".format(c)

solutions = [solution1, solution2, solution3]
```

Consider a list of randomly generated $a-letter "words" printed on a paper. The letters cannot be repeated.

* What is the size of the set of allowed words?

[_]

* At least how many of these "words" should be printed to be sure of having at least $b identical "words" on the list?

[_]

* Consider a list of $d "words". What is the largest integer \(j\) such that at least one "word" appears at least \(j\) times?

[_]
