```python
# random variables (no need to import random library)

a = random.randrange(-3,-1,1);
b = a + random.randrange(2,6,1);
lambd = random.randrange(1, 9, 1)/10;

n1 = random.randrange(100,500,10);
n2 = random.randrange(100,500,10);


# Solutions with variables converted to string
# Make sure you name the solution with part id at the end. e.g. 'solution1' will be solution for part 1.
solution1 = "({0}+{1})/2".format(a,b)
solution2 = "sqrt((({0}-({1}))^2/12) / {2})".format(b,a,n1)
solution3 = "1/{0}".format(lambd)
solution4 = "sqrt((1/{0}^2) / {1})".format(lambd,n2)

# Group all solutions into a list
solutions = [solution1,solution2,solution3,solution4]

```
### CLT simulation

In this problem, you may use the CLT simulation (http://webwork.cse.ucsd.edu/misc/clt.html) to help you find the answers.

---

Suppose a sample average is denoted by \\\(S_n = (\sum_{i=1}^n X_i) /n\\\) and we define \\\(T_n = (S_n - A) / B\\\).

Find the values of \\\(A\\\) and \\\(B\\\) under the following conditions so that \\\(T_n\\\) is distributed normally with \\\(\mu = 0\\\) and \\\(\sigma = 1\\\). Your answers should be correct up to 2 decimal points.

*  \\\(X_i \sim \mbox{Uniform}($a,$b)\\\) and \\\(n = $n1\\\)
    -  A = 
    
    [_]
    
    -  B = 
    
    [_]

*  \\\(X_i \sim \mbox{Exponential}($lambd)\\\) and \\\(n = $n2\\\)
    -  A = 
    
    [_]
    
    -  B = 
    
	[_]
