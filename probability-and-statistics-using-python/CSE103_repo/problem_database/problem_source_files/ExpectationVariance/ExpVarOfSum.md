```python
# random variables (no need to import random library)

a = random.randint(1,5);
b = random.randint(6,10);

# Solutions with variables converted to string
# Make sure you name the solution with part id at the end. e.g. 'solution1' will be solution for part 1.
solution1 = "{0}*(1+1/2+1/3+1/4+1/5)".format(a)
solution2 = "{0}*(1+1/4+1/9+1/16+1/25)".format(b)
solution3 = "{0}*(1-1/2+1/3-1/4+1/5)".format(a)
solution4 = "{0}*(1+1/4+1/9+1/16+1/25)".format(b)
solution5 = "{0}*(1-2/2+1/3-2/4+1/5)".format(a)
solution6 = "{0}*(1+1/9+1/25) +{0}*4*(1/4+1/16)".format(b)


# Group all solutions into a list
solutions = [solution1,solution2,solution3,solution4,solution5,solution6]

```

Let \\\(X_1, X_2, \cdots X_{5}\\\) be independent random variables with:

\\\[\mathbb{E}(X_i) = \frac{$a}{i} \hspace{10pt} \mbox{VAR}(X_i) = \frac{$b}{i^2}\\\]

Compute:

* What is the mean of \\\(X_1 + X_2 + X_3 + X_4 + X_5\\\) ?

[_]

* How about the variance?

[_]

* What is the mean of \\\(X_1 - X_2 + X_3 - X_4 + X_5\\\) ?

[_]

* How about the variance?

[_]

* What is the mean of \\\(X_1 - 2X_2 + X_3 - 2X_4 + X_5\\\) ?

[_]

* How about the variance?

[_]
