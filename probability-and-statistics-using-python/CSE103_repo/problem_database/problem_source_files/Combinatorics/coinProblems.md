```python
# random variables (no need to import random library)
coins = random.randrange(9,11,1)
heads = coins-1

# Solutions with variables converted to string
# Make sure you name the solution with part id at the end. e.g. 'solution1' will be solution for part 1.

solution1 = "2^{{{0}}}".format(coins)
solution2 = "1/2^{{{0}}}".format(coins)
solution3 = "{0}!/({0}-1)!".format(coins)
solution4 = "{0}!/({0}-1)!/2^{{{0}}}".format(coins)
solution5 = "1-1/2^{{{0}}}".format(coins)
solution6 = "({0}!/(6!({0}-6)!))/2^{{{0}}}".format(coins)

# Group all solutions into a list
solutions = [solution1, solution2, solution3, solution4, solution5, solution6]

```

A fair coin is tossed $coins times.

* The outcome space for the experiment is the set of all H/T sequences
  of length $coins, What is the size of this outcome space?

[_]

* Assuming that the coin is fair, all sequences have the same
  probability, which is:

[_]

* What is the size of the event set for getting exactly $heads heads?

[_]

* What is the probability of getting exactly $heads heads?

[_]

* What is the probability of getting at most $heads heads?

[_]

* What is the probability of getting exactly 6 heads?

[_]
