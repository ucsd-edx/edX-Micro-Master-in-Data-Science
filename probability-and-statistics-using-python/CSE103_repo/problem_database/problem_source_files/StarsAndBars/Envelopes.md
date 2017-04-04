```python
R1=random.randrange(7,15,1)    # number of cards
R2=random.randrange(2,R1-1,1)    # number of envelopes

solution1 = "{1}^{{{0}}}".format(R1,R2)
solution2 = "C({0}+{1}-1,{0})".format(R1,R2)
solution3 = "C({0}-1,{0}-{1})".format(R1,R2)

solutions = [solution1, solution2, solution3]
```

Suppose we have $R1 cards and $R2 envelopes to put them in. The envelopes are marked (1,...,$R2). We will calculate the number of ways to put the cards into the envelopes under different conditions.

* Suppose all the cards are *distinct* (i.e. are numbered (1,2,....,$R1)). How many ways are there to place cards into envelopes? As should be expected from the first part of a question, this is an easy one. Think of placing the cards into envelopes in the following way: take the first card and choose an envelope for it, then take the second card and choose an envelope for it etc. Until all of the cards have been placed. Clearly we can get any possible combination this way. It takes a little thought, but you can also convince yourself that there is only *one* way to get each combination. In other words, there is no overcounting.

Counting the number of combinations we get this way is simple. At each of the $R1 step we place one card in one of the $R2 envelopes. Taking the product over all of these steps we get that the number of combinations is

[_]

* Suppose that cards are *identical*. (The envelopes remain distinct) How many combinations are possible in this case?

Consider the difference between part 1 and part 2. In part 1, each configuration specified exactly *which* cards were placed in each envelope. Here the cards are identical, therefor we can only say how *many* cards are in each envelope, but we cannot identify them.

Thinking of the problem this way, we realize that it is mathematically equivalent to the problem of choosing $R1 candies when there are $R2 *types* of candy to choose from. As the Candies are indistinguishable, we are only interested in the number of candies chosen from each type. The correspondence is card <-> candy and candy type <-> envelope.

If you go back to this problem, you will recall the formula for it and use it to get the answer:

[_]

* Suppose the cards are identical as in 2. and, in addition, we require that each envelope contain at least one card.  In this case we first have to check that the number of cards is at least as large as the number of envelopes, otherwise there will be no way to satisfy the requirements. Luckily (thanks to the magic of EdX) $R1>$R2.

OK, good. Now we can proceed in two steps, first, take $R2 cards and put one card in each envelope, satisfying the reuirement that each envelop contains a card. The remaining cards can be placed in any envelope, with no constraints. We now have the same situation we had in part 2. but where, instead of $R1 cards, we have $R1-$R2=$R1-$R2 cards. We use the same formula that we used in 2. to find that the answer is

[_]
