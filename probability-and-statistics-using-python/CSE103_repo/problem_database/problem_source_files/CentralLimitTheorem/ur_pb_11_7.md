```python
# random variables (no need to import random library)

n = random.randrange(40,100,5);
d = random.randrange(2,5,1);


# Solutions with variables converted to string
# Make sure you name the solution with part id at the end. e.g. 'solution1' will be solution for part 1.
solution1 = "0"
solution2 = "sqrt(1/12)"
solution3 = "0"
solution4 = "1/sqrt(12)*sqrt({0})".format(n)
solution5 = "({0}-0)/(1/sqrt(12)*sqrt({1}))".format(d,n)
solution6 = "Q({0}/(1/sqrt(12)*sqrt({1})))".format(d,n)
solution7 = "2*Q({0}/(1/sqrt(12)*sqrt({1})))".format(d,n)
# Group all solutions into a list
solutions = [solution1,solution2,solution3,solution4,solution5,solution6,solution7]

```
$n numbers are rounded off to the nearest integer and then summed. Suppose the individual round-off error are uniformly distributed over  \\\((-.5, .5)\\\).

---
Remember a random variable that follows a uniform distribution over \\\((a,b)\\\) has a mean of \\\((a+b)/2\\\), and variance of \\\(\frac{1}{12}(b-a)^2\\\).

* What is the mean of the round-off error of one number?

[_]

* What is the standard deviation of the round-off error of one number? 

[_]

---
* Suppose the *sum* of the round-off errors is \\\(Y\\\).

What is the mean of \\\(Y\\\)?

[_]

* What is the standard deviation of \\\(Y\\\)? 

[_]


---

To compute the probability that the resultant sum of the $n numbers differs from the exact sum by more than $d, we find the two tails on the distribution of \\\(Y\\\).

* What is the z-score at \\\(Y=$d\\\) ? 

[_]

* What is the probability that the rounded sum is *larger* than the exact sum by more than $d ?

[_]

* What is the probability that the rounded sum *differs* from the exact sum by more than $d ?

[_]
