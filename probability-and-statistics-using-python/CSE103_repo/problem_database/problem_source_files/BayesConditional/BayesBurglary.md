```python
# random variables (no need to import random library)
#false burglary percentage
atpt = random.randrange(92,96,1)
perc=atpt/100

#burglary percentage
fals = random.randrange(1,3,1)
fperc = fals/100

# Solutions with variables converted to string
# Make sure you name the solution with part id at the end. e.g. 'solution1' will be solution for part 1.
solution1 = "1/10000"
solution2 = "{0}/10000 + {1}*(1-1/10000)".format(perc, fperc)
solution3 = "{0}/10000".format(perc)
solution4 = "({1})/({0})".format(solution2,solution3)

# Group all solutions into a list
solutions = [solution1, solution2, solution3, solution4]


```

## Bayes' Burglary ##
*  The following example is taken from _Probabilistic Reasoning in Intelligent Systems_ by Judea Pearl:

You wake up in the middle of the night to the shrill sound of your burglar alarm. What is the chance that a burglary attempt has taken place? The relevant facts are:

*  There is a $atpt% chance that an attempted burglary attempt will trigger the alarm. That is
\\\[P(\\mbox{alarm} | \\mbox{burglary}) = $atpt/100\\\]

*  There is a $fals% chance of a false alarm.
\\\[P(\mbox{alarm} | \mbox{no burglary}) = $fals/100\\\]

*  Based on local crime statistics, there is a one-in-ten-thousand chance that a house will be burglarized on a given night.  

* What is \\\(P(\mbox{burglary})\\\)

[_]

*  We are interested in the chance of a burglary given that the alarm has sounded. We can use the conditional probability formula for this:
\\\[P(\\mbox{burglary} | \\mbox{alarm}) \\ = \\ \\frac{P(\\mbox{burglary and alarm})}{P(\\mbox{alarm})} \\ = \\ \\frac{P(\\mbox{alarm} | \\mbox{burglary}) P(\\mbox{burglary})}{P(\\mbox{alarm})}\\\]

*  The one term we don't immediately know is \\\(P(\mbox{alarm})\\\).  By the summation rule,
\\\[P(\\mbox{alarm}) \\ = \\ P(\\mbox{alarm} | \\mbox{burglary}) P(\\mbox{burglary}) + P(\\mbox{alarm} | \\mbox{no burglary}) P(\\mbox{no burglary})\\\]

*  What is \\\(P(\\mbox{alarm})\\\)?

[_]

*  What is \\\(P(\\mbox{burglary}, \\mbox{alarm})\\\)

[_]

*  Putting it all together, using the conditional probability definition mentioned above, what is
\\\[P(\\mbox{burglary} | \\mbox{alarm})\\\]

[_]

Thus our belief in a burglary has risen approximately a hundredfold from its default value of \\\(10^{-4}\\\)  on account of the alarm.
