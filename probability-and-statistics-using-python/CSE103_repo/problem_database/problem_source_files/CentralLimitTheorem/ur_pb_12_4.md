```python
# random variables (no need to import random library)

n = random.randrange(20,30,1);
nc = random.randrange(4,6,1);
p = 1/nc;
mean = n*p;
low = int(mean + 4);
high = int(mean + 8);
corr = random.randrange(low, high, 1);

std = math.sqrt( n / nc * (1-1/nc));

# Solutions with variables converted to string
# Make sure you name the solution with part id at the end. e.g. 'solution1' will be solution for part 1.
solution1 = "BinomDistTail({0},{1},{2})".format(n,p,corr)
solution2 = "{0}*{1}".format(n,p)
solution3 = "sqrt({0}*{1}*(1-{1}))".format(n,p)
solution4 = "({0}-{1})/(sqrt( {2} / {3} * (1-1/{3})))".format(corr,mean,n,nc)
solution5 = "Q(({0}-{1})/(sqrt( {2} / {3} * (1-1/{3}))))".format(corr,mean,n,nc)


# Group all solutions into a list
solutions = [solution1,solution2,solution3,solution4,solution5]

```
### Some Definitions ###
The *standard* normal distribution \\\(\mathcal{N}(0,1)\\\) is a special normal distribution with mean \\\(\mu=0\\\) and standard deviation \\\(\sigma=1\\\).

- The CDF of the standard normal distribution is denoted \\\(\Phi\\\):
\\\[\Phi(z) = P(Z\leq z)\\\]

- The complement of the CDF is called the *Q-function*:
\\\[Q(z) = P(Z>z) = 1-\Phi(z)\\\]

While \\\(\Phi(z)\\\) measures the probability mass of a "head" of the standard normal, \\\(Q(z)\\\) measures the "tail". The values of Q are often tabulated for commonly used \(z\). One such table is _http://goo.gl/Szofn1_. One can also use _http://wolframalpha.com_ to find numeric values for Q function.


- An alternative representation of the head probability is the *error function*, denoted \\\(erf\\\). It is related to \\\(\Phi\\\) by:
\\\[\Phi(x) = \frac{1}{2} + \frac{1}{2}erf(\frac{x}{\sqrt{2}})\\\]

*For this set of assignment, you can use "Phi", "Q" or "erf" as functions in your answer.*

---

### Recap for Binomial Distribution ###

Suppose a monkey is given a test that consists of $n multiple-choice questions each with $nc choices. By random guessing, what is the *exact* probability that the monkey gets at least $corr correct ?

[_]

---
### Approximate Binomial Using Normal Distribution ###
We know that the number of questions the monkey guesses correctly follows a binomial distribution, and we have computed the *exact* probability of a tail of this distribution, by summing up all cases in the tail.

Now, we assume the number of questions is large enough so that by *central limit theorem* we can use a normal distribution to approximate the binomial distribution. This makes computing the probability of a certain part of the distribution much easier.

---
Again, suppose the monkey is taking a multiple-choice test that consists of $n questions each with $nc possible answers, let us estimate the probability that it gets at least $corr questions correct, this time using an *approximated normal distribution*.

Suppose \\\(X\\\) is the number of correct answers.

- What is the mean of \\\(X\\\) ? 

[_]

- What is the standard deviation of \\\(X\\\) ?

[_]

- What is the z-score of \\\(X=$corr\\\)?

[_]

- What is the estimated probability that \\\(X \ge $corr\\\) ?

[_]
