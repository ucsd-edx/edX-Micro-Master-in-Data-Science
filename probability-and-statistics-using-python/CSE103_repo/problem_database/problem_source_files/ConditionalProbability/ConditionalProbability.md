```python

solution1 = "0.5-0.15"
solution2 = "1"

solutions = [solution1, solution2]
```
## Conditional Probability ##

You meet a stranger, a random citizen of the United States. What's the
chance that he (or, equally likely, she) votes for the Democratic
party? 

Who knows, but it's probably close to \\\(50%\\\). 

\\\[ \Omega = \{\mbox{citizens of the US}\}, \ \ E = \{\omega \in \Omega:
\omega \mbox{votes Dem}\}.\\\]

suppose that you find out some additional information: this stranger
likes spicy food. 

\\\[ F = \{\omega \in \Omega: \omega \mbox{likes spicy food}\}.\\\]

How does change the odds? What is \\\(P(E|F)\\\) (probability of
\\\(E\\\) given \\\(F\\\))? Again, it's hard to say, but for
illustrative purposes here is a (definitely incorrect) set of
probabilities: 

\\\[ P(E) = 0.5, P(F) = 0.2, P(E \cap F) = 0.15.\\\]

(1) What is \\\]P(E \cap F^c)?\\\]

[_]

\\\(E \setminus F\\\) means the set of elements that are in \\\(E\\\) but not in \\\(F\\\).

The Venn diagram for this scenario is:

END_PGML
BEGIN_TEXT
$BR \{ image("ConditionalProbabilityDiagram.png", width=>250, height=>200) \}
END_TEXT
BEGIN_PGML

If you stare at it a little bit, you will probably conclude, correctly, that \\\(P(E|F)\\\) is the chance that a point drawn from the small blob lies inside the large blob, namely \\\(0.15 / 0.2 = 0.75\\\). By reasoning this way, you are implicitly using \\\( P(E|F) \ = \ \frac{P(E \cap F)}{P(F)} .\\\) We will make heavy use of this and of the equivalent \\\( P(E \cap F) = P(E|F) P(F).\\\)

(2) What is \\\(P(E|F)*P(F)/P(E \cap F)\\\)?  

[_]
