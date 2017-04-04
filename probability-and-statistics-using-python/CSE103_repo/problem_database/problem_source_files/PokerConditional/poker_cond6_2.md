```python
# random variables (no need to import random library)


n = random.choice(range(13,16,1))
x = random.choice(range(2,9,1))
y = random.choice(range(x+2,13,1))

# Solutions with variables converted to string
# Make sure you name the solution with part id at the end. e.g. 'solution1' will be solution for part 1.
solution1 = "{0}-1".format(n)
solution2 = "{0}-2".format(n)
solution3 = "({0}-1)*({0}-2)".format(n)
solution4 = "{0} - {1} - 1".format(y, x)
solution5 = "({0}-{1})*({0}-{1}-1)/2".format(n,x)
solution6 = "1 * ({0}-{1})*({0}-{1}-1)/2/(({0}-1)*({0}-2))".format(n,x)


# Group all solutions into a list
solutions = [solution1, solution2, solution3, solution4, solution5, solution6]


```


Three cards are drawn sequentially from a deck that contains \\\($n\\\) cards numbered 1 to \\\($n\\\) in an arbitrary order. Suppose the first card drawn is a \\\($x\\\), what is the probability that the three cards form an increasing sequence?

Note that unlike the previous question, we are considering a sequence instead of a set of cards, so the order matters. Define the event of interest, A, as the set of all increasing 3-card sequences, i.e.
\\\[A = \\\{(x_1,x_2,x_3) | x_1 < x_2 < x_3\\\} \\\]

where \\\(\\\{x_1, x_2, x_3\\\}\\\) in \\\(\\\{1, \\cdots, $n\\\}\\\). Define event \\\(B\\\) as the set of 3-card sequence that starts with \\\($x\\\), i.e. \\\[B = \\\{(x_1,x_2,x_3) | x_1=$x\\\} \\\] or simply  \\\(B = \\\{($x,x_2,x_3)\\\} \\\)

- How many cards can be selected as \\\(x_2\\\) in \\\(B\\\) :

[_]

- How many cards can be selected as \\\(x_3\\\) in \\\(B\\\) when \\\(x_2\\\) is already selected :

[_]

- What is the size of \\\(B\\\) i.e. \\\(|B| = \\\)

[_]

It follows that
\\\[ A \\cap B = \\\{($x,x_2,x_3) | $x < x_2 < x_3\\\} \\\]

This set can be partitioned into subsets according to \\\(x_3\\\), where in each subset \\\(x_3\\\) is a constant:
\\\[ A \\cap B = \\cup_{x_3 = $x+2}^{$n}{($x,x_2,x_3)|$x < x_2 < x_3} \\\]

Let \\\(S_{x_3=t}\\\) represent the subset
\\\[\\\{($x,x_2,t)|$x < x_2 < t\\\}\\\],

then \\\[|A \\cap B| = \\sum_{t = $x+2}^{$n} \\left|S_{x_3=t}\\right| \\\].

- To compute each \\\(\\left|S_{x_3=t}\\right|\\\), let's start with a specific case, say,  \\\(t=$y\\\),

\\\(\\left|S_{x_3=$y}\\right| = \\left| \\\{($x,x_2,$y)|$x < x_2 < $y\\\} \\right| = \\\)

[_]

- Generalize this computation, it should be straightforward to compute \\\(|A \\cap B|\\\) as the sum of \\\(S_{x_3=t}\\\) over all valid \\\(t\\\).
\\\(|A \\cap B| = \\\)

[_]

- Now we are ready to compute the conditional probability

\\\(P(A|B) = \\\)

[_]
