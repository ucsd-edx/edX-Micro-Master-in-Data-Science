```python
# random variables (no need to import random library)
p_men = random.randrange(6,8,1)
p_women = random.randrange(3,5,1)

# Solutions with variables converted to string
# Make sure you name the solution with part id at the end. e.g. 'solution1' will be solution for part 1.
solution1 = "{0}/100*0.5".format(p_men)
solution2 = "{0}/100*0.5 + {1}/100*0.5".format(p_men,p_women)
solution3 = "({0})/({1})".format(solution1,solution2)

# Group all solutions into a list
solutions = [solution1,solution2,solution3]


```
Suppose that there are equal numbers of men and women in the world, and that \\\($p_men\\\)% of men are colorblind \\\($p_women\\\)% of women are colorblind.

A person is chosen at random and found to be colorblind. What is the probability that the person is male?

We need to reverse the direction of conditioning. We are given \\\(\\text{Pr}(\\text{colorblind}|\\text{male})\\\) and we need to compute \\\(\\text{Pr}(\\text{male}|\\text{colorblind})\\\)?

To do so we use Bayes Formula, which for this setting is:
\\\[\\textbf{Pr}(\\text{male}|\\text{colorblind}) = \\frac{\\textbf{Pr}(\\text{male},\\text{colorblind)}}{\\textbf{Pr}(\\text{colorblind)}} \\\]
\\\[=\\frac{\\textbf{Pr}(\\text{colorblind}|\\text{male})\\textbf{Pr}(\\text{male})}{\\textbf{Pr}(\\text{colorblind})}\\\]

We will compute the numerator and denominator of the Bayes equation separately:

First, the numerator is
\\\[\\textbf{Pr}(\\text{male}, \\text{colorblind})
= \\textbf{Pr}(\\text{colorblind}| \\text{male})* \\textbf{Pr}(\\text{male}) \\\]

which is equal to

[_]

Second, the denominator is \\\(\\textbf{Pr}(\\text{colorblind})\\\), which can be calculated using the Law of Total Probability as follows:
\\\[\\textbf{Pr}(\\text{colorblind}) = \\textbf{Pr}(\\text{male}, \\text{colorblind}) + \\textbf{Pr}(\\text{female}, \\text{colorblind}) \\\]
\\\[= \\textbf{Pr}(\\text{colorblind}|\\text{male})\\textbf{Pr}(\\text{male}) + \\textbf{Pr}(\\text{colorblind}|\\text{female})\\textbf{Pr}(\\text{female})\\\]

Which means that the denominator is equal to:

[_]

Finally, we take the ratio of the numerator and denominator to find the final answer:

\\\[\\text{Pr}(\\text{male}|\\text{colorblind})=\\\]

[_]
