```python
# random variables (no need to import random library)
n = random.randrange(0,4,1)

# Solutions with variables converted to string
# Make sure you name the solution with part id at the end. e.g. 'solution1' will be solution for part 1.
problem = [["mixture_cdf_3.png","0.5", "0.25", "-2.5", "0.75"]]
problem += [["mixture_cdf_5.png","0.5", "0.45", "2.5", "0.55"]]
problem += [["mixture_cdf_10.png","1.0", "0.3", "2.0", "0.7"]]
problem += [["mixture_cdf_15.png","0.5", "0.3", "-0.5", "0.7"]]
img_file, lam, solution1, solution2, solution3 = problem[n]

# Group all solutions into a list
solutions = [solution1, solution2, solution3]


```



* Below is the CDF of a mixture distribution with *two* components.

One of the components is an exponential distribution; the other is a point mass.

All parameters of component distributions are small multiples of 0.5.

\\\(\lambda\\\) of exponential components take on value 0.5, 1 or 1.5.

Component weights take on multiples of 0.05 and they need to sum to one.

<img src="/static/$img_file"/>

Identify the component distributions:

* The exponential component has \\\(\lambda\\\) of $lam. Its component weight is?

[_]

* Point mass on

[_]

Its component weight is

[_]
