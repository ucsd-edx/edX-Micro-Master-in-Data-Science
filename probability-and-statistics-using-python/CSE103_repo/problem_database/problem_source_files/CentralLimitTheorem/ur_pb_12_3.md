```python
# random variables (no need to import random library)

b = random.randrange(150,400,1);
p = random.randrange(80,90,1)/100;
p2 = p * 100
mean =b*p;

z = random.randrange(170, 310, 1)/100;

dev = math.sqrt (b * p * (1 - p));

s = 10*int((z * dev + mean)/10+1);



# Solutions with variables converted to string
# Make sure you name the solution with part id at the end. e.g. 'solution1' will be solution for part 1.
solution1 = "{0}".format(mean)
solution2 = "sqrt({0} * {1} * (1 - {1}))".format(b,p)
solution3 = "Q(({0}-{1})/(sqrt({2} * {3} * (1 - {3}))))".format(s,mean,b,p)

# Group all solutions into a list
solutions = [solution1,solution2,solution3]

```
An airline company is considering a new policy of booking as many as $b persons on an
airplane that can seat only $s.
(Past studies have revealed that only $p2% of the booked passengers actually arrive for the flight.)

* What is the mean of the number of passengers that arrive for the flight ? 

[_]

* What is the standard deviation ? 

[_]

* Estimate the probability that if the company books [$b] persons, not enough seats will be
available. 

[_]
