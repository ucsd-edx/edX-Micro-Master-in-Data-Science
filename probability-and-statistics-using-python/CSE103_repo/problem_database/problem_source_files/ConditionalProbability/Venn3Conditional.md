```python

# P/100 is the probability of the partition of P according to the events
# A/A^C, B/B^C and C/C^C
P=[]

for i in range(2):
	P.append([])
	for j in range(2):
	   P[i].append([])
	   for k in range(2):
	      P[i][j].append(random.randrange(1,3,1)/20.)

pairs=[(0,0),(0,1),(1,0),(1,1)]
def rnd(x):
    return round(x*100.)/100.

pa=rnd(sum([P[1][i][j] for i,j in pairs]))
pb=rnd(sum([P[i][1][j] for i,j in pairs]))
pc=rnd(sum([P[i][j][1] for i,j in pairs]))
paib=rnd(sum(P[1][1][i] for i in range(2)))
paic=rnd(sum(P[1][i][1] for i in range(2)))
pbic=rnd(sum(P[i][1][1] for i in range(2)))
pabc=rnd(sum([sum([sum(L) for L in M]) for M in P]))

paub=pa+pb-paib
pauc=pa+pc-paic
pbuc=pb+pc-paic

solution1 = "{0}+{1}-{2}".format(pa,pb,paub)
solution2 = "{0}+{1}-{2}".format(pb,pc,pbuc)
solution3 = "{0}+{1}-{2}".format(pa,pc,pauc)
solution4 = "({0})/{1}".format(solution1,pb)
solution5 = "({0})/{1}".format(solution1,pa)
solution6 ="{0}+({4})+({5})+({6})-({1}+{2}+{3})".format(pabc,pa,pb,pc,solution1,solution2,solution3)
solution7 ="({0})/({1})".format(solution6,solution2)

solutions = [solution1, solution2, solution3, solution4, solution5, solution6, solution7]
```
## Conditional Probability ##

Consider the following Venn diagram, describing three events labeled A,B and C.

<img src="/static/Venn3.jpg" style="width:300px;height:300px;"/>

You are given the following information:
\\\[ P(A) = $pa \\\]
\\\[ P(B) = $pb \\\]
\\\[ P(C) = $pc \\\]
\\\[ P(A \cup B) = $paub \\\]
\\\[ P(A \cup C) = $pauc \\\]
\\\[ P(C \cup B) = $pbuc \\\]
\\\[ P(A \cup B \cup C) = $pabc \\\]

Compute the following quantities. Hint: write expressions involving the numbers above, rather than calculating the numerical result.

\\\[ P(A \cap B) = \\\]

[_]

\\\[ P(B \cap C) = \\\]

[_]

\\\[ P(A \cap C) = \\\]

[_]

\\\[ P(A | B) = \\\]

[_]

\\\[ P(B|A) = \\\]

[_]

\\\[ P(A \cap B \cap C) = \\\]

Hint: Google the "inclusion exclusion principle for three sets"


[_]

\\\[ P(A | B \cap C) = \\\]

[_]
