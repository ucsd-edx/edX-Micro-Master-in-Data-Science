```python
# random variables (no need to import random library)

n = 2*random.randrange(40,50,1)
m = n-1


# Solutions with variables converted to string
# Make sure you name the solution with part id at the end. e.g. 'solution1' will be solution for part 1.
solution1 = "(0.5*0)+(0.5*1)"
solution2 = "(0.5*(0-0.5)^2)+(0.5*(1-0.5)^2)"
solution3 = "0.5-0.5"
solution4 = "0.25+0.25"
solution5 = "0.5-(2*0.5)+0.5"
solution6 = "0.25+(4*0.25)+0.25"
solution7 = "0"
solution8 = "{0}*0.25".format(n)

# Group all solutions into a list
solutions = [solution1,solution2,solution3,solution4,solution5,solution6,solution7,solution8]

```

Let \\\(X_1, X_2, \ldots, X_{100}\\\) be the outcomes of \\\(100\\\) independent rolls of a fair coin.

\\\[P(X_i=0)=P(X_i=1)=0.5\\\]

1) \\\(\mathbb{E}(X_1) = \\\)

[_]

2) \\\(var(X_1) = \\\)

[_]

Define the random variable \\\(X = X_1 - X_2\\\).

3) \\\(\mathbb{E}(X) = \\\)

[_]

4) \\\(var(X) = \\\)

[_]

   *Hint:* if \\\(X,Y\\\) are independent random variables then \\\(var(X\pm Y)=var(X)+var(Y)\\\)

Define the random variable \\\(Y = X_1 - 2X_2 + X_3\\\).

5) \\\(\mathbb{E}(Y) = \\\)

[_]

6) \\\(var(Y) = \\\)

[_]

   *Hint:* if \\\(a\\\) is a constant and \\\(X\\\) a random variable, then \\\(var(aX)=a^2 var(X)\\\).

Define the random variable \\\(Z = X_1 - X_2 + X_3 - X_4 + ... + X_{$m} - X_{$n}\\\).

7) \\\(\mathbb{E}(Z) = \\\)

[_]

8) \\\(var(Z) = \\\)

[_]
