```python
a = random.randrange(300,400,1)
b = random.randrange(15,25,1)

solution1 = "C(10,8) * 0.5^{10}"
solution2 = "C(10,9) * 0.5^{10}"
solution3 = "1 * 0.5^{10}"
solution4 = "(C(10,8) +C(10,9) + 1) * 0.5^{10}"
solution5 = "1- ((C(10,8) +C(10,9) + 1) * 0.5^{10})"
solution6 = " ({{{0}}}) ^ {{{1}}}".format(solution5,a)
solution7 = " 1 - ({0})".format(solution6)

solutions = [solution1,solution2,solution3,solution4,solution5,solution6,solution7]
```

There is a class of $a students taking a T/F quiz of 10 questions. Suppose the students are just guessing the answers by flipping fair coins. We would normally think it unlikely that a student  makes fewer than 3 mistakes,  i.e. get at least 8 questions right out of 10 in this way. However, with a class this large, it might be possible, or even probable, that at least one student gets 8 or more questions right.

Here we'll calculate the probability of at least one student in the class of size $a getting 8 or more questions right. Or equivalently: at most 2 questions wrong.

* What is the probability of a particular student getting exactly 2 questions right?

[_]

* What is the probability of a particular student getting exactly 1 question wrong?

[_]

* What is the probability of a particular student getting all questions right?

[_]

* What is the probability of a particular student getting at most 2 questions wrong?

[_]

* What is the probability of a particular student getting 3 or more questions wrong?

[_]

* What is the probability of *every* student in the class getting 3 or more questions wrong?

[_]

* What is the probability of some student in the class getting at most 2 questions wrong?

[_]
