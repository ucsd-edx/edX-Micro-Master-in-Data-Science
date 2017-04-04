```python
R1=random.randrange(8,15,1);
R2=random.randrange(2,R1-2,1);

solution1 = "{0} - 1".format(R1)
solution2 = "{0}".format(R2)
solution3 = "(({1}+{0}-1)!)/(({1})!*({0}-1)!)".format(R1,R2)

solutions = [solution1, solution2, solution3]
```

You walk into a candy store and notice that there are five types of candy. Your mother allows you to pick exactly three pieces of candy, of whichever type(s) you want. How many ways are there to do this?

You can represent the outcome by 5-tuple \\\((n_1, n_2, \ldots, n_5)\\\) in which \\\(n_i\\\) is the number of pieces of the \\\(i\\\) th type of candy. How many such tuples are there, subject to \\\(n_1 + n_2 + \cdots + n_5 = 3\\\)

To answer the question, we'll represent each tuple in a different format, as a sequence of length 7 containing three stars and four bars. For instance, the sequence \\\(| *  * | | | * \\\) denotes \\\((0,2,0,0,1)\\\) (two candies of type 2 and one candy of type 5): the number of candies of type \\\(i\\\) is the number of stars between the \\\((i-1)\\\) th and \\\(i\\\) th bars.

So we have rephrased the question thus: how many sequences are there with four bars and three stars? Well, this is a sequence of size 7, and we must pick three of the seven positions at which to place stars. The number of such choices is \\\({7 \choose 3} = 35\\\)

Suppose balls come in $R1 colors and that you are to pick out $R2 balls. How many different color combinations are possible?

By the analogy explained above, how many bars do you need

[_]


By the analogy explained above, how many stars do you need

[_]

The number of color combinations is

[_]
