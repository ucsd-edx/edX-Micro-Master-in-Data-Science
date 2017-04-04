```python
#cannot check answer
mean = 24
sd = random.randrange(30, 50, 1)/10
k = random.randrange(2,3,1)
record = 44
a = k * sd
b1 = mean - a
b2 = mean + a

solution1 = "(1-(1/{0}^2))*100".format(k) #{Compute("(1-(1/$k^2))*100")} %.
solution2 = "0.5*1/(({0}-{1})/{2})^2".format(record, mean, sd)#{Compute("0.5*1/(($record-$mean)/$sd)^2")}

solutions = [solution1, solution2]
```
### Chebyshev's Inequality ##

We will use Chebyshev's inequality in this problem. The Chebyshev's theorem is stated as below:

Let X be a random variable with finite expected value \\\(\mu\\\) and finite non-zero variance \\\(\rho^2\\\). Then for any real number \\\(k > 0\\\), \\\(\Pr(|X-\mu|\geq k\sigma) \leq \frac{1}{k^2}\\\), which is the same as \\\(\mathbb{P}(|X-\mathbb{E}(X)| \geq a) \leq \frac{\textrm{Var}(X)}{a^2}\\\) for any \\\(a>0\\\).

---

Suppose the mean noon-time temperature for September days in San Diego is \\\($mean^{\circ}\\\) and the standard deviation is $sd. (Temperature in this problem is measured in degrees celsius)

(1) Using Chebyshev's theorem, what is the *minimal* probability(**in percents**) that the noon-time temperature of a September day is between \\\($b1^{\circ}\\\) and \\\($b2^{\circ}\\\)?

[_]

(2) On September 26, 1963, the all-time record of noon-time temperature in San Diego of \\\(44^{\circ}\\\) was hit. Assume the temperature distribution is symmetric around the mean, what is the Chebyshev bound for the probability of breaking (or tieing) this record?

[_]
