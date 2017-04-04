```python
# random variables (no need to import random library)
r1 = random.randrange(10,20,1)
r2 = random.randrange(5,r1,1)

# Solutions with variables converted to string
# Make sure you name the solution with part id at the end. e.g. 'solution1' will be solution for part 1.
solution1 = "1/{0}".format(r1)
solution2 = "({1}-1)/{0}".format(r1,r2)
solution3 = "({0}-{1})/{0}".format(r1,r2)
solution4 = "1"

# Group all solutions into a list
solutions = [solution1, solution2, solution3, solution4]

```
Suppose we have a stack of $r1 cards, numbered 1,...,$r1. Suppose we pick a card uniformly at random (i.e. all cards have the same probability of being picked).


* What is the probability that the number on the card we picked is
  equal to $r2?

[_]

* What is the probability that the number on the card we picked is
  smaller than $r2?

[_]

* What is the probability that the number on the card we picked is
  larger than $r2?

[_]

* What is the sum of the previous three probabilities?

[_]
