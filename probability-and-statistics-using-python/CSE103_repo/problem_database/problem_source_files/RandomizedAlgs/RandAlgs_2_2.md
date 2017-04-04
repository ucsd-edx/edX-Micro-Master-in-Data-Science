```python
import math
# random variables (no need to import random library)

variable_values = {'n':[20,50,100]}
index_of_test_value = 2


k = random.randrange(3,5);
uk = k - 1
p = (k-1)/k;
q = 1.6449;
n_normal = (q * math.sqrt(p * (1 - p)) / (0.5 - p)) ** 2

a5 = int(math.ceil(20 * p * (1 - p) / ((p - 0.5) ** 2)))
a7 = int(math.ceil(n_normal))

# Solutions with variables converted to string
# Make sure you name the solution with part id at the end. e.g. 'solution1' will be solution for part 1. 
solution1 = "1/2"
solution2 = "{0}".format(p)
solution3 = "(1/n) * {0} * (1 - {0})".format(p)
solution4 = "(1/n) * {0} * (1 - {0}) / (({0} - 0.5)**2)".format(p)
solution5 = "{0}".format(a5)
solution6 = "(0.5 - {0}) / (sqrt({0} * (1 - {0}) / n))".format(p)
solution7 = "{0}".format(a7)



# Group all solutions into a list
solutions = [solution1, solution2, solution3, solution4, solution5, solution6, solution7]


```


You have an algorithm A for testing whether a Boolean formula f is satisfiable or not, but it is only correct with probability \\\($uk / $k\\\). More precisely, you can repeatedly run A on the same formula f, and each time it outputs the correct answer with probability \\\($uk / $k\\\).

To reduce the probability of error, you run \\\(A(f)\\\) \\\(n\\\) times, and return the majority answer. What should \\\(n\\\) be if you want the probability of error to be less than 0.05?

---

Let \\\(C_i\\\) be a binary random variable indicating whether the \\\(i^{th}\\\) execution of algorithm A is correct.  Let \\\(C = (C_1 + C_2 ... C_n)/n\\\).

- What is the minimum value of \\\(C\\\) such that our method of returning the majority answer will be correct?  
 
[_]

- What is \\\(\\mathbb{E}(C)\\\)?  
 
[_]

- What is \\\(var(C)\\\)?  

[_]


_Approach 1_:
Chebyshev's inequality says for random variable \\\(Y\\\) with mean \\\(\\mu\\\) and for any positive number \\\(a>0\\\), \\\(P(|Y-\\mu| \\geq a) \\leq var(Y)/a^2\\\)

- Using Chebyshev's inequality, what is an upper bound on the probability your "majority algorithm" is incorrect?  

[_]

- What is the smallest *integer* value for \\\(n\\\) so that the probability that the "majority algorithm" makes an error is at most 0.05?  

[_]

---

_Approach 2_:
Using Central Limit Theorem, approximate the distribution of \\\(C\\\) as a normal.
- What is the z-score of \\\(C=0.5\\\) 

[_]


- What is the smallest *integer* value for \\\(n\\\) so that the "majority algorithm" makes an error with probability at most 0.05? 

[_]


---

Notice that \\\(n\\\) obtained with Approach 2 is much smaller than that obtained with Approach 1, this is because using the normal approximation and Q function give us a much tighter bound than the Chebyshev bound. (The Q function drops exponentially fast as the value deviates from the mean, while the Chebyshev bound drops only quadratically fast)