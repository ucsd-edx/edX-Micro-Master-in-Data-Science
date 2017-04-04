```python
# random variables (no need to import random library)

# Solutions with variables converted to string
# Make sure you name the solution with part id at the end. e.g. 'solution1' will be solution for part 1.
solution1 = "65"
solution2 = "65*(0.500*(((30.0/65.0)-0.500)/0.500)^2+0.250*(((20.0/65.0)-0.250)/0.250)^2+0.250*(((15.0/65.0)-0.250)/0.250)^2)"
solution3 = "65*((1/3)*(((30.0/65.0)-(1/3))/(1/3))^2+(1/3)*(((20.0/65.0)-(1/3))/(1/3))^2+(1/3)*(((15.0/65.0)-(1/3))/(1/3))^2)"

# Group all solutions into a list
solutions = [solution1, solution2, solution3]


```

Suppose there are 3 species of fish in the world, we are interested
in two fish populations: fish of the pacific ocean and fish of the atlantic ocean.
Each one of these populations is characterized by a distribution over the species of fish:
The pacific distribution is uniform over the 3  species:
\\\[P_p=(1/3,1/3,1/3)\\\] while in the Atlantic population the first species is twice more common than the other two: \\\[P_a=(1/2,1/4,1/4)\\\]

Suppose we are given a  batch of 65 fish whose source is unknown.
The number of fish of each species is \\\(30,20,15\\\).

We would like to know whether the the batch of fish is from the Atlantic or the pacific (or both).

One way of formalizing this problem is to consider two Null hypotheses:

* HA = the batch is from the Atlantic ocean. More technically, the batch was sampled from the distribution \\\(P_a\\\)
* HP = the batch is from the pacific ocean. More technically, the batch was sampled from the distribution \\\(P_b\\\).

The test that we will use is the \\\(\chi^2\\\) test. (https://en.wikipedia.org/wiki/Pearson%27s_chi-squared_test).

The \\\(\chi^2\\\) test statistic is

\\\[\chi^2 =  N \sum_{i=1}^n p_i \left(\frac{O_i/N - p_i}{p_i}\right)^2\\\]

Where:
* \\\(n\\\) is the number of species (3 in our case).
* \\\(p_i\\\) is the probability of the \\\(i\\\)th species according to the Null distribution.
* \\\(O_i\\\) is the number of observations of species \\\(i\\\)
* \\\(N\\\) is the total number of observation. \\\(N=\sum_{i=1}^n O_i\\\).

*What is \\\(N\\\) in our case?

[_]

Write expressions for the \\\(\chi^2\\\) statistic for the two null Hypotheses:

* For hypothesis HA ( batch is from Atlantic ocean), \\\[\chi^2=\\\]

[_]

* For hypothesis HP ( batch is from pacific ocean), \\\[\chi^2=\\\]

[_]

This question continues with the next problem.
