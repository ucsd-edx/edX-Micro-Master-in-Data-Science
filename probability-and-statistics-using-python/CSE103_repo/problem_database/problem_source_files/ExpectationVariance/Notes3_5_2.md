```python
# variable names and values
# if multiple variables, the number of values to test should be the same
variable_values = {'p':[0.1, 0.2, 0.3]}

# value index used to extract hint
index_of_test_value = 2

solution1 = "0.3*(1-0.3)"
solution2 = "(1 + 2 + 3 + 4)/4"
solution3 = "(1+4+9+16)/4"
solution4 = "1.25"
solution5 = "(2.25 + 0.25 + 0.25 + 2.25)/4"

solutions = [solution1, solution2, solution3, solution4, solution5]
```

### Examples of Variances ###

* Suppose you toss a coin with bias \\\(p\\\), and let \\\(X\\\) be \\\(1\\\) if the outcome is heads, or \\\(0\\\) if the outcome is tails.

Let's look at the distribution of \\\(X\\\) and of \\\(X^2\\\).

<table border="1">
  <tr>
    <th>Prob</th>
    <th>\(X\)</th>
    <th>\(X^2\)</th>
  </tr>
  <tr>
    <td>\(p\)</td>
    <td>1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>1-\(p\)</td>
    <td>0</td>
    <td>0</td>
  </tr>
</table>


From this table, \\\(\mathbb{E}(X) = p\\\) and \\\(\mathbb{E}(X^2) = p\\\). Let \(p=0.3\). Thus the variance is \\\(\mbox{var}(X) = \mathbb{E}(X^2) - (\mathbb{E}(X))^2 = \\\)

[_]


* Roll a 4-sided die (a tetrahedron) in which each face is equally likely to come up, and let the outcome be \\\(X \in \\\{1,2,3,4\\\}\\\).

We have two formulas for the variance:
\\\[ \mbox{var}(X) = \mathbb{E} \left( (X - \mu)^2 \right) \\\]
\\\[ \mbox{var}(X) = \mathbb{E}(X^2) - \mu^2 \\\]
where \\\(\mu = \mathbb{E}(X)\\\).


Let's try both and make sure we get the same answer.

First of all, \\\(\mu = \mathbb{E}(X) =\\\)

[_]

Now, let's tabulate the distribution of \\\(X^2\\\) and \\\((X-\mu)^2\\\).


<table border="1">
  <colgroup align="center"/>
  <colgroup align="left"/>
  <tr>
    <th>Prob</th>
    <th>\(X\)</th>
    <th>\(X^2\)</th>
    <th>\((X-\mu)^2\)</th>
  </tr>
  <tr>
    <td>\(\frac{1}{4}\) </td>
    <td>1</td>
    <td>1</td>
    <td>2.25</td>
  </tr>
  <tr>
    <td>\(\frac{1}{4}\)</td>
    <td>2</td>
    <td>4</td>
    <td>0.25</td>
  </tr>
  <tr>
    <td>\(\frac{1}{4}\)</td>
    <td>3</td>
    <td>9</td>
    <td>0.25</td>
  </tr>
  <tr>
    <td>\(\frac{1}{4}\)</td>
    <td>4</td>
    <td>16</td>
    <td>2.25</td>
  </tr>
</table>


Reading from this table, \\\(\mathbb{E}(X^2) = \\\)

[_]

Using the second formula for variance we have

\\\(\mbox{var}(X) = \mathbb{E}(X^2) - \mu^2 = \\\)

[_]

\\\(\mathbb{E}\left((X-\mu)^2\right) = \\\)

[_]

Using the first formula for variance we have \\\(\mbox{var}(X) = \mathbb{E}\left((X-\mu)^2\right)\\\). Notice that both formulae give the same answer.