```python
k = random.randrange(6,10,1);
t1 = random.randrange(2,5,1);
t2 = random.randrange(2,5,1);
r = random.randrange(1,6,1)/10; #random(0.1,0.6,0.1);

solution1 = "{0}*({0}+1)/(2*{0})".format(k);
solution2 = "2*{0}/({0}+1) + ({0}*({0}-1))/(2*({0}+1))".format(k);
solution3 = "{0}*{2} + {1}*({3})".format(t1,t2,solution1,solution2);
solution4 = "({0})/{1}".format(solution3,r);

solutions = [solution1, solution2, solution3, solution4]
```

### Rigged dice ##

We have 2 $k-sided dice. The first die is a normal fair die where each face has a probability of showing of \\\(1/$k\\\). However, the second die is rigged so that the probability of showing the largest face $k is twice as high as of the other faces and all of the other faces have equal probabilities.

(1) What is the expected value of the outcome from tossing the fair die?

[_]

(2) What is the expected value of the outcome from tossing the rigged die?

[_]

We throw the fair die $t1 times, then the rigged die $t2 times consecutively and sum up all the outcomes:

(3) What is the expected value of the sum?

[_]

Let \\\(Y\\\) denote the sum from the previous part. If we know that

\\\[P(Y > k) \le $r\\\]

(4) According to Markov's inequality, what is \\\(k\\\)?

[_]
