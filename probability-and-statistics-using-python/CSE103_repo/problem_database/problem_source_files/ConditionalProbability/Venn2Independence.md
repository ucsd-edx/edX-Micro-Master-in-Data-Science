```python
# random variables (no need to import random library)
pa = random.randrange(1,6,1)/10.
pb = random.randrange(1,6,1)/10.
is_indep=(random.random()>0.5)*1

if is_indep == 1:
	paub=pa+pb-pa*pb
else:
	paub=pa+pb-pa*pb*2

solution1="{0} + {1} - ({2})".format(pa,pb,paub)
solution2="({0})/{1}".format(solution1,pb)
solution3= str(is_indep)
solutions = [solution1,solution2,solution3]

```

## Independence ##

Two events are called _independent_ if the outcome of one (that is, whether or not it occurs) does not affect the probability that the other will occur. For instance, suppose you flip two fair coins. The outcome of either coin does not influence the other; therefore the two outcomes are independent.

Formally, we say events \\\(A\\\) and \\\(B\\\)  (defined on some
sample space \\\(\Omega\\\)   are independent if \\\( P(A \cap B)\ =
P(A) P(B).\\\)

Consider the following Venn Diagram describing two events:

\{ image(src="/static/Venn2.jpg" style="width:300px;height:200px;") \}

Suppose you know that \\\(P(A)=$pa\\\), \\\(P(B)=$pb\\\) and \\\(P(A
\cup B)=$paub\\\),

What is \\\( P(A\cap B)\\\)?

[_]


What is \\\(P(A | B)\\\)?

[_]

are \\\(A\\\) and \\\(B\\\) independent? (enter 1 for yes, 0 for no)

[_]
