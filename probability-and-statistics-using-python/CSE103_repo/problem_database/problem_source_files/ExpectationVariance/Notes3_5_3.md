```python
solution1 = "3*1+4*3+2"
solution2 = "3^2*2+4^2*2"
solutions = [solution1, solution2]
```

## Another property of the variance ##

Here's a cartoon picture of a well-behaved distribution with mean \\\(\mu\\\) and standard deviation \\\(\sigma\\\) (that is, \\\(\mu = \mathbb{E}(X)\\\) and \\\(\sigma^2 = \mbox{var}(X)\\\)).

<img src='/static/MeanStdFigure_pptx.jpg' width="80%" height="80%"/>

The standard deviation quantifies the *spread* of the distribution whereas the mean specifies its *location*. If you increase all values of \\\(X\\\) by 10, then the distribution will shift to the right and the mean will increase by 10. But the spread of the distribution -- and thus the standard deviation -- will remain unchanged.

On the other hand, if you double all values of \\\(X\\\), then its distribution becomes twice as wide, and thus its standard deviation \\\(\sigma\\\) is doubled. Which means that its variance, which is the square of the standard deviation, gets multiplied by 4.

In summary, for any constants \\\(a,b\\\), the relation between updated variance and old variance is:

\\\[ \mbox{var}(aX+b) = a^2 \mbox{var}(X) \\\]

In contrast, the updated mean will be:

\\\[ \mathbb{E}(aX + b) = a \mathbb{E}(X) + b \\\].


## Linearity of variance ##

If \\\(X\\\) and \\\(Y\\\) are independent random variables, then \\\(\mbox{var}(X+Y) = \mbox{var}(X) + \mbox{var}(Y)\\\). More generally, if \\\(X_1, \ldots, X_n\\\) are independent, then

\\\[ \mbox{var}(X_1 + \cdots + X_n) = \mbox{var}(X_1) + \cdots + \mbox{var}(X_n)\\\]

In contrast, linearity of expectation \\\(\mathbb{E}(X+Y) = \mathbb{E}(X) + \mathbb{E}(Y)\\\) holds even if the random variables are *not* independent.

Suppose \\\(X\\\) and \\\(Y\\\) are independent random variables. \\\(X\\\) has mean of 1 and variance of 2, \\\(Y\\\) has mean of 3 and variance of 2, then for the r.v. \\\(Z = 3X+4Y+2\\\), the mean is

[_]

and the variance is

[_]
