```python
p = random.randrange(6,8,1)
ten = 10
k = p*10

if (p == 6):
    solution1 ="(C(10,{0})+C(10,{0}+1)+C(10,{0}+2)+C(10,{0}+3)+1)/(2^{{{1}}})".format(p,ten)

if (p == 7):
    solution1 = "(C(10,{0})+C(10,{0}+1)+C(10,{0}+2)+1)/(2^{{{1}}})".format(p,ten)

if (p == 8):
    solution1 = "(C(10,{0})+C(10,{0}+1)+1)/(2^{{{1}}})".format(p,ten)

solutions = [solution1]
```

Here we will calculate the probability of a student getting at least $k percent on a true/false exam with 10 questions.

The probability that a student gets a grade of $k percent or better by guessing is

[_]
