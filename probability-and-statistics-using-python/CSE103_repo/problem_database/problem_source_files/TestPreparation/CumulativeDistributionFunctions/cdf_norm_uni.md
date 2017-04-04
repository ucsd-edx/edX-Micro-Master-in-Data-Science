```python
# random variables (no need to import random library)
n = random.randrange(0,3,1)

# Solutions with variables converted to string
# Make sure you name the solution with part id at the end. e.g. 'solution1' will be solution for part 1.
problem = [["mixture_cdf_7.png","1.0", "0.5", "0.65", "-4.5", "-2.5", "0.35"]]
problem += [["mixture_cdf_11.png","-1.0", "1", "0.25", "-1.0", "2.0", "0.75"]]
problem += [["mixture_cdf_12.png","1.0", "1", "0.3", "-3.0", "-1.0", "0.7"]]

img_file, mean, solution1, solution2, solution3, solution4, solution5 = problem[n]

# Group all solutions into a list
solutions = [solution1, solution2, solution3, solution4, solution5]


```



* Below is the cumulative distribution function (CDF) of a mixture distribution with *two* components.

One of the components is a normal distribution; the other is a uniform distribution.

All parameters of component distributions are small multiples of 0.5.

Standard deviation (std) of normal components take on value 0.5, 1 or 1.5.

Component weights take on multiples of 0.05 and they need to sum to 1.

<img src="/static/$img_file"/>

Identify the component distributions:

* The normal component has mean of $mean. What is the std?

[_]

What is the component weight?

[_]

* Uniform component on the interval (a,b).

a =

[_]

b =

[_]

What is the component weight?

[_]
