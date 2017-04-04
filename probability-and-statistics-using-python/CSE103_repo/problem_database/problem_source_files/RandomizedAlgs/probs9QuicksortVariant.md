```python
# random variables (no need to import random library)

k = random.randrange(3,7,2)

alpha = random.randrange(1,4,1) * 0.1
alphaC = 1 - alpha

exp = 2

if k is 5:
    exp = 3

if k is 7:
    exp = 4

alphaPow = alpha ** exp
a6 = 1 / ((1 - 2 * alphaPow) * alpha)
a7 = 1 / (1 - 2 * alphaPow)

# Solutions with variables converted to string
# Make sure you name the solution with part id at the end. e.g. 'solution1' will be solution for part 1. 
solution1 = "2*{0}".format(alpha)
solution2 = "2*{0}".format(alphaPow)
solution3 = "1 - 2 * {0}".format(alphaPow)
solution4 = "1 - 2 * {0}".format(alphaPow)
solution5 = "2*{0}".format(alphaPow)
solution6 = "1 / ((1 - 2 * ({0} ** {1})) * {0})".format(alpha, exp)
solution7 = "1 / (1 - 2 * ({0} ** {1}))".format(alpha, exp)



# Group all solutions into a list
solutions = [solution1, solution2, solution3, solution4, solution5, solution6, solution7]


```


In this problem, we will analyze the expected running time of a variant to the  randomized percentile finding algorithm discussed in lecture. The algorithm is used to select the \\\(k^{th}\\\) smallest element in an array containing \\\(n\\\) elements. In other words, the element that would appear in location \\\(k\\\) if the array is sorted from smallest to largest.

In this version of percentile finding algorithm we change the the way we select the pivot element. Suppose instead of a single pivot we pick \\\($k\\\) numbers, sort them, and select the pivot to be the median of the numbers.

We say that a pivot is "lucky" if it falls in the range of \\\($alpha n\\\) and  \\\($alphaC n\\\). When the pivot is lucky we are guaranteed that the size of the array at the following iteration will be at most \\\($alphaC n\\\)

Pick one of the \\\($k\\\) numbers that we have sampled. What is the probability that this number is not in the range of \\\($alpha n\\\) and \\\($alphaC n\\\) 

[_]

What is the probability that the median of the \\\($k\\\) numbers that we sample is not in the range of \\\($alpha n\\\) and \\\($alphaC n\\\) 

[_]

What is the probability that the median of the \\\($k\\\) numbers that we sample is  in the range of \\\($alpha n\\\) and \\\($alphaC n\\\) 

[_]

Now, let us use the results computed above to build a recurrence relation to estimate the expected running time of the algorithm.

Let \\\(T(n)\\\) denote the expected running time of the algorithm with input size n.

When we get lucky, our problem reduces to a size of \\\($alphaC n\\\).
When we are unlucky, our problem size remains \\\(n\\\).

\\\(T(n) \\leq n + a T($alphaC n) + b T(n)\\\)

In the recurrence relation, what is the value of \\\(a\\\) 

[_]

In the recurrence relation, what is the value of \\\(b\\\) 

[_]

Solving the recurrence relation we get \\\(T(n)  \\leq C*n\\\)
What is the value of \\\(C\\\) 

[_]

What is the expected number of random splits before we see a lucky split 

[_]


---
