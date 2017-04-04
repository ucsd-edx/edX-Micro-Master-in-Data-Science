```python
# random variables (no need to import random library)
variable_values = {'n':[2,3,4], 'c':[10,25,50]}
index_of_test_value = 2
# Solutions with variables converted to string
# Make sure you name the solution with part id at the end. e.g. 'solution1' will be solution for part 1. 
solution1 = "1/2 + 1/n"
solution2 = "1/c"
solution3 = "20"
solution4 = "20"



# Group all solutions into a list
solutions = [solution1, solution2, solution3, solution4]


```


# Transforming Las Vegas to Monte Carlo

Suppose you have an algorithm A for your problem that always returns the correct answer, but takes different amounts of time each time it runs.  Let \\\(X_n\\\) be the random variable giving the time algorithm A takes to complete for input of size \\\(n\\\).  Time can't be negative, so \\\(X \\geq 0\\\).
 We call A a _Las Vegas Algorithm_ if for any input size \\\(n\\\) there is a \\\(T(n)\\\) so that \\\(\\mathbb{E}(X_n) = T(n)\\\).

- Side note: it isn't always the case that a random variable has finite expectation, even the values it can take on are finite.  The assumption that there is some \\\(T(n)\\\) for any \\\(n\\\) is a non-trivial assumption.

Let's say we have algorithm that determines whether any integer is prime.  For an integer input that takes up \\\(n\\\) bits, the algorithm takes \\\(n\\\) seconds to run with probability \\\(1/2\\\).  With probability \\\(1/2\\\) the algorithm takes 1 second to run.  What is \\\(T(n)\\\), in seconds?  

[_]

Let's say you have some Las Vegas algorithm A that runs in _expected time_ \\\(T(n)\\\) for problem size \\\(n\\\).  What you would prefer, however, is an algorithm that _always_ finishes in time \\\(O(T(n))\\\), but may have up to a 5% probability of returning the wrong answer.  We will construct an algorithm A' from A that satisfies these properties.

Recall Markov's inequality: for some random variable \\\(Y \\geq 0\\\), \\\(P(Y >= a) \\leq \\mathbb{E}(Y)/a \\\).

Fixing some \\\(n\\\), apply Markov's inequality to get an upper bound on \\\(P(X_n >= cT(n))\\\): 

[_]

What is \\\(c\\\) such that \\\(P(X_n >= cT(n)) <= 0.05\\\)?  

[_]

Thus an algorithm A' is as follows:

* Run A until 

[_]

times of \\\(T(n)\\\)

If A has completed, return the correct value, Else, return a random value.

This type of algorithm we have, where the algorithm completes in deterministic time \\\(Q(n)\\\) but is correct with some probability is called a _Monte Carlo Algorithm_.

_Recap_:

- For "Las Vegas" algorithms, uncertainty is in the algorithm _runtime_.  The algorithm is always correct.

- For "Monte Carlo" algorithms, uncertainty is in the algorithm _correctness_.  The algorithm completes in deterministic time \\\(T(n)\\\).

___
