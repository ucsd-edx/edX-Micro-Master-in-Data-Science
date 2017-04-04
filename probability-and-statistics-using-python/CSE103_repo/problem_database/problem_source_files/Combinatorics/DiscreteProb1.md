```python
R = random.randrange(4,9,1)
RL = R - 1

solution1 = "{0}^4".format(R)
solution2 = "4"
solution3 = "({0}-1)*{0}".format(R)
solution4 = "{0}*({0}-1)/({0}^4)".format(R)

solutions = [solution1,solution2,solution3,solution4]
```

Suppose a sequence of 4 digits in the range 1-$R, endpoints inclusive, is chosen uniformly at random. What is the probability that the first and third digits are equal, the second and the fourth digits are equal, but the first and second digits are unequal?

* We are going to use the standard formula for probability of sets in a discrete uniform distribution space: the probability of a set \\\(A\\\) in the sample space \\\(\Omega\\\) is

    \\\[P(A) = \frac{|A|}{|\Omega|}\\\]

* In the denominator we place the *size* of the sample space. This is easy, as we have $R choices for each of the four four digits. The number of sequences is equal to the size of the sample space. Thus \\\(|\Omega| = \\\)

[_]

* Now we want to compute the size of the set \\\(A\\\). To do that it is useful to realize that we need only concern ourselves with the choices of two digits, say digits 1 and 2.  This is because digit 1 determines the value of digit 3. Which digit does digit 2 determines?

[_]

* Now, how many choices do we have for digit 1? Obviously, any integer in the range \\\(1,\ldots,$R\\\), or $R choices. Once digit 1 has been chosen, we have one less choice for digit 2, in other words $RL. The size of the set \\\(A\\\) is the product of these two numbers:

[_]

* Putting this all together we get that the probability of \\\(A\\\) is

\\\(P(A)=\\\)

[_]
