```python

r = random.randrange(4,6,1)/10;#random(0.4,0.6,0.1);
k = random.randrange(100,200,1);

p = random.randrange(r*10+1,9,1)/10#random(r+0.1,0.9,0.1);
n2 = random.randrange(300,500,1);
k2 = random.randrange(251,299,1);
#ans1 = ceil(p*k/r);

solution1 = "{0}*{1}/{2}".format(p, k, r) #{Compute("$p*$k/$r")}
solution2 = "{0}*{1}/{2}".format(n2, r, k2) #{Compute("$n2*$r/$k2")->with(tolType=>'absolute', tolerance=>'0.01')}

solutions = [solution1, solution2]
```

### Markov's Inequality ##

Markov's inequality relate probabilities to expectations, and provide bounds for the cumulative distribution function of a random variable. The Markov's inequality is stated as follow:

If X is any nonnegative random variable and a > 0, then  \\\[\mathbb{P}(X \geq a) \leq \frac{\mathbb{E}(X)}{a}\\\]
---
John has a biased coin with \\\(P(\mathrm{heads}) = $r\\\). He tosses this coin \\\(N\\\) times and, out of the \\\(N\\\) times, the coin lands on heads $k times. Using Markov's inequality that he learned from CSE103, he says that the probability of seeing at least this many heads is at most $p.

(1) Give the best lower bound, using Markov inequality, on the number of times John tossed the coin?
\\\(N\\\) =

[_]

(Provide the exact answer, don't round it to the next larger integer number.)

Suppose John lends you this coin. If you flip the coin $n2 times, what is the upper bound of the probability of seeing at least $k2 heads using Markov's inequality?

(2) \\\(P(\mbox{Number of heads} \geq $k2)\\\) \\\(\le\\\)

[_]
