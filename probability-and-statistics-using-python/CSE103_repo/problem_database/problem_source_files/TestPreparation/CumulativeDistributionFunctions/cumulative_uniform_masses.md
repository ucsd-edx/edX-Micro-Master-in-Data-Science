```python
# random variables (no need to import random library)
n = random.randrange(0,2,1)

# Solutions with variables converted to string
# Make sure you name the solution with part id at the end. e.g. 'solution1' will be solution for part 1.

variables = [["cumulative_uniform_masses_1.png", "0.3", "0.5", "0.6", "2.0", "0.2", "0.4", "0.9", "0.1"]]
variables += [["cumulative_uniform_masses_2.png", "2.0", "0.1", "5.0", "0.1", "2.5", "0.3", "6.0", "0.3"]]

img_file, solution1, solution2, solution3, solution4, solution5, solution6, solution7, solution8 = variables[n]
# Group all solutions into a list
solutions = [solution1, solution2, solution3, solution4, solution5, solution6, solution7, solution8]


```



Given the following cumulative distribution:

<img src="/static/$img_file" />

* What are the uniform densities and mass distributions that could have been summed to produce this CDF?

Uniform distributions:

- Uniform on (0.10, X) of probability density Y.

X =

[_]

Y =

[_]

- Uniform on (0.40,A) of probability density B.

A =

[_]

B =

[_]


* Point masses (ordered by the location):

- Point mass at

[_]

with probability

[_]

- Point mass at

[_]

with probability

[_]
