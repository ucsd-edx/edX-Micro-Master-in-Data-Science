```python
# random variables (no need to import random library)
n = random.randrange(0,5,1)

# Solutions with variables converted to string
# Make sure you name the solution with part id at the end. e.g. 'solution1' will be solution for part 1.
problem = [["mixture_cdf_1.png","-2.0", "0.5", "0.5", "-0.5", "0.5"]]
problem += [["mixture_cdf_4.png","1.0", "1", "0.4", "2.5", "0.6"]]
problem += [["mixture_cdf_13.png","0.5", "1.5", "0.25", "1.0", "0.75"]]
problem += [["mixture_cdf_14.png","-2.0", "1", "0.35", "3.0", "0.65"]]
problem += [["mixture_cdf_17.png","1.5", "1.5", "0.5", "0.0", "0.5"]]

img_file, mean, solution1, solution2, solution3, solution4 = problem[n]

# Group all solutions into a list
solutions = [solution1, solution2, solution3, solution4]


```



* Below is the cumulative density function (CDF) of a mixture distribution with *two* components.

One of the components is a normal distribution; the other is a point mass distribution.

All parameters of component distributions are small multiples of 0.5.

Standard deviation (std) of normal components take on value 0.5, 1 or 1.5.

Component weights take on multiples of 0.05 and they need to sum to one.

<img src="/static/$img_file"/>

Identify the component distributions:

* The normal component has mean of $mean. What is the std?

[_]

What is the component weight?

[_]

* Point mass on

[_]

What is the component weight?

[_]
