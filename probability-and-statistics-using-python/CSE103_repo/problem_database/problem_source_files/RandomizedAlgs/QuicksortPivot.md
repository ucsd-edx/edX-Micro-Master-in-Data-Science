```python
# random variables (no need to import random library)
variable_values = {'n':[10,20,30]}
index_of_test_value = 2
t = random.randrange(2, 10, 1)

# Solutions with variables converted to string
# Make sure you name the solution with part id at the end. e.g. 'solution1' will be solution for part 1. 
solution1 = "1/n"
solution2 = "0.5"
solution3 = "2.0"



# Group all solutions into a list
solutions = [solution1, solution2, solution3]


```


## Selecting a Percentile (Quantile) ##

Let \\\(S\\\) be a set of \\\(n\\\) different numbers (think of \\\(n\\\) as being very large).
Suppose we want to find the \\\(k^{th}\\\) biggest element in \\\(S\\\), for any \\\(k \\leq n\\\).
Of course, we could just sort \\\(S\\\) and then pick out the answer, but this would take \\\(n \\log n\\\) time. Can we do better?

In this problem, we will look at an (expected) linear-time algorithm
for finding the \\\(k^{th}\\\) biggest element in \\\(S\\\), for any \\\(k \\leq n\\\).
The algorithm is randomized, and we'll specify it soon.

First suppose we pick a random element of \\\(S\\\) - call it \\\(v\\\) - and let \\\(S_L = { x \\in S \\mid x < v }\\\) and \\\(S_U = { x \in S \mid x > v }\\\) be the elements less than and greater than \\\(v\\\).

*(a)* What is the probability that \\\(\\left| S_L \right|\\\), the size of \\\(S_L\\\), is equal to \\\($t\\\)? 

[_]

(Hint: what value(s) can \\\(v\\\) take for this to happen? What's the probability of choosing such \\\(v\\\)?)

*(b)* What is the approximate probability that \\\(\left| S_L \right|\\\) is _between_ \\\(\\lceil n/4 \\rceil\\\) and \\\(\\lceil 3n/4 \\rceil\\\)? (Round your answer to one decimal place.) 

[_]

If \\\(v\\\) is chosen so that \\\(\\mid S_L \\mid \\in [n/4, 3n/4]\\\), then this implies \\\(\\left| S_U \\right| \\in [n/4, 3n/4]\\\) as well, so each of the two sets has a significant fraction of the elements.
We'll call such a choice of \\\(v\\\) _lucky_.


*(c)* We'll consider a randomized algorithm for finding the \\\(k^{th}\\\) biggest element in \\\(S\\\) - call this value \\\(f (k, S)\\\). (For example, \\\(f (1, S)\\\) would be the maximum element in \\\(S\\\), and \\\(f (\\frac{1}{2} \\left| S \\right|, S)\\\) the median.)

The algorithm chooses an element \\\(v\\\) at random from \\\(S\\\) and computes \\\(\\left| S_L \\right|\\\) and \\\(\\left| S_U \\right|\\\), to determine if this choice of \\\(v\\\) is lucky. If not, it chooses \\\(v\\\) again at random and repeats until it chooses a lucky \\\(v\\\).

When a lucky \\\(v\\\) is chosen, the algorithm computes \\\(\\left| S_L \\right|\\\) and \\\(\\left| S_U \\right|\\\), and then does one of two things:

1.  If \\\(\\left| S_L \\right| \\geq k\\\), then the \\\(k^{th}\\\) biggest element in \\\(S\\\) is in \\\(S_L\\\). Actually, it must be the \\\(k^{th}\\\) biggest element in \\\(S_L\\\) as well, so in this case the algorithm just recursively finds \\\(f(k, S_L)\\\).

2.  If \\\(\left| S_L \right| < k\\\), then the \\\(k^{th}\\\) biggest element in \\\(S\\\) is in \\\(S_U\\\). Specifically, it must be the \\\((k - \\left| S_L \\right|)^{th}\\\) biggest element in \\\(S_U\\\), so in this case the algorithm just recursively finds \\\(f(k - \\left| S_L \\right|, S_U)\\\).

Note that in both cases, we end up recursively working on a set (\\\(S_L\\\) or \\\(S_U\\\)) that is at most 3/4 the size of the current set \\\(S\\\), because our choice of \\\(v\\\) is lucky.

However, our lucky choices take a random time to generate because of the randomized way in which they're chosen. Our randomized algorithm continues choosing values of \\\(v\\\) one at a time independently, until it makes its first lucky choice. Using the answer to part (b) and how our randomized algorithm works, the expected number of random choices of \\\(v\\\) required to generate a lucky choice is 

[_]

