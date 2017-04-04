```python
# random variables (no need to import random library)

# Solutions with variables converted to string
# Make sure you name the solution with part id at the end. e.g. 'solution1' will be solution for part 1.
solution1 = "0"
solution2 = "0"
solution3 = "1"
solution4 = "1"
solution5 = "1"

# Group all solutions into a list
solutions = [solution1, solution2, solution3, solution4, solution5]


```

To compute the p-value of rejecting the Null hypothesis we need to know the **number of degrees of freedom** of the distribution. As the size of the space is 3 there are three variables defining the distribution: \\\(p_1,p_2,p_3\\\) as these probabilities sum to one there \\\(v=2\\\) degrees of freedom. We then use the CDF for the \\\(\chi^2\\\) distribution with 2 degrees of freedom to calculate the p-values.

Answer the following questions yes (enter 1) or no (enter 0)

* A small value of the \\\(\chi^2\\\) statistic justifies **rejecting** the Null Hypothesis

[_]

* A small value of the \\\(\chi^2\\\) statistic justifies **accepting** the Null Hypothesis

[_]

* A large value of the \\\(\chi^2\\\) statistic justifies **rejecting** the Null Hypothesis

[_]

* It is possible to reject both of the Null hypotheses:

[_]

* It is possible to not reject either of the Null hypotheses:

[_]
