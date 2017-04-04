##Week3

        Assigned problem file name:
        +--------+------------+------------------------------------------------------------+
        | set_id | problem_id | source_file                                                |
        +--------+------------+------------------------------------------------------------+
        | Week3  |          1 | local/Reorganized/Combinatorics/sw10_2_21_PGML.pg          |
        | Week3  |          2 | local/Reorganized/Combinatorics/GrinsteadSnell3.2.18.pg    |
        | Week3  |          3 | Reorganized/Combinatorics/GrinsteadSnell3.2.10.pg          |
        | Week3  |          4 | Reorganized/Combinatorics/DiscreteProb1.pg                 |
        | Week3  |          5 | Reorganized/Combinatorics/q1.pg                            |
        | Week3  |          6 | Reorganized/Combinatorics/withoutReplacementExplanation.pg |
        | Week3  |          7 | Reorganized/Combinatorics/PigeonHole_PGML_ZZ.pg            |
        | Week3  |          8 | Reorganized/Combinatorics/BinomialCoeffExplanation.pg      |
        | Week3  |          9 | local/Reorganized/StarsAndBars/ChoosingCandies.pg          |
        | Week3  |         10 | Reorganized/StarsAndBars/Envelopes1.pg                     |
        | Week3  |         11 | Reorganized/Poker/q2.pg                                    |
        | Week3  |         12 | Reorganized/Poker/q4_0.pg                                  |
        | Week3  |         13 | Reorganized/Poker/q4_2.pg                                  |
        | Week3  |         14 | Reorganized/Poker/q4_4.pg                                  |
        | Week3  |         15 | Reorganized/Poker/q4_6.pg                                  |
        +--------+------------+------------------------------------------------------------+

### Sorted with number of attempts
[problem 2](https://github.com/cse103/Attempt_Analysis/blob/master/clustering_code/clusters/Week3/md_files/Week3_2_clusters.md): 3928

		 part  1 :  902
		 part  2 :  232
		 part  3 :  80
		 part  4 :  423
		 part  5 :  681
		 part  6 :  715
		 part  7 :  895


[problem 13](https://github.com/cse103/Attempt_Analysis/blob/master/clustering_code/clusters/Week3/md_files/Week3_13_clusters.md): 3515

		 part  1 :  834
		 part  2 :  461
		 part  3 :  1577
		 part  4 :  144
		 part  5 :  297
		 part  6 :  202


[problem 11](https://github.com/cse103/Attempt_Analysis/blob/master/clustering_code/clusters/Week3/md_files/Week3_11_clusters.md): 2752

		 part  1 :  261
		 part  2 :  152
		 part  3 :  1006
		 part  4 :  199
		 part  5 :  175
		 part  6 :  724
		 part  7 :  235


[problem 10](https://github.com/cse103/Attempt_Analysis/blob/master/clustering_code/clusters/Week3/md_files/Week3_10_clusters.md): 2090

		 part  1 :  1112
		 part  2 :  687
		 part  3 :  291


[problem 14](https://github.com/cse103/Attempt_Analysis/blob/master/clustering_code/clusters/Week3/md_files/Week3_14_clusters.md): 2035

		 part  1 :  740
		 part  2 :  806
		 part  3 :  219
		 part  4 :  270


[problem 9](https://github.com/cse103/Attempt_Analysis/blob/master/clustering_code/clusters/Week3/md_files/Week3_9_clusters.md): 1277

		 part  1 :  595
		 part  2 :  91
		 part  3 :  591


[problem 7](https://github.com/cse103/Attempt_Analysis/blob/master/clustering_code/clusters/Week3/md_files/Week3_7_clusters.md): 1171

		 part  1 :  107
		 part  2 :  526
		 part  3 :  538


[problem 8](https://github.com/cse103/Attempt_Analysis/blob/master/clustering_code/clusters/Week3/md_files/Week3_8_clusters.md): 886

		 part  1 :  363
		 part  2 :  108
		 part  3 :  137
		 part  4 :  278


[problem 15](https://github.com/cse103/Attempt_Analysis/blob/master/clustering_code/clusters/Week3/md_files/Week3_15_clusters.md): 842

		 part  1 :  172
		 part  2 :  68
		 part  3 :  179
		 part  4 :  207
		 part  5 :  90
		 part  6 :  126


[problem 1](https://github.com/cse103/Attempt_Analysis/blob/master/clustering_code/clusters/Week3/md_files/Week3_1_clusters.md): 632

		 part  1 :  252
		 part  2 :  380


problem 5(Set Problem): 508

		 part  1 :  508


[problem 4](https://github.com/cse103/Attempt_Analysis/blob/master/clustering_code/clusters/Week3/md_files/Week3_4_clusters.md): 463

		 part  1 :  246
		 part  2 :  22
		 part  3 :  58
		 part  4 :  28
		 part  5 :  44
		 part  6 :  65


[problem 3](https://github.com/cse103/Attempt_Analysis/blob/master/clustering_code/clusters/Week3/md_files/Week3_3_clusters.md): 455

		 part  1 :  455


[problem 6](https://github.com/cse103/Attempt_Analysis/blob/master/clustering_code/clusters/Week3/md_files/Week3_6_clusters.md): 208

		 part  1 :  7
		 part  2 :  14
		 part  3 :  187


[problem 12](https://github.com/cse103/Attempt_Analysis/blob/master/clustering_code/clusters/Week3/md_files/Week3_12_clusters.md): 185

		 part  1 :  185



### Problem Content

Problem 1

    $a=random(4,6,1);

    if ($a == 4){
       $lts = AABBCC;
       $ans = 6*5*4*3*2/(2*2*2);
       };
    if ($a == 5){
       $lts = AAABBC;
       $ans = 6*5*4*3*2/(3*2*2);
       };
    if ($a == 6){
       $lts = AABCD;
       $ans = 5*4*3*2/2;
       };

    1. Find the number of distinguishable ways of arranging the letters "MAMA".
    Your answer is : [_________________________]{Compute("(4*3*2)/(2*2)")}

    2. Find the number of distinguishable permutations formed by using each of the letters [$lts] once and only once.
    Your answer is : [_________________________]{$ans}



Problem 2

    $a = random(300,400,1);
    $b = random(15, 25, 1);

    There is a class of [$a] students taking a T/F quiz of 10 questions. We would normally think it unlikely that a student would get more than 2 questions right out of 10 by flipping a coin, but with a class this large, it might be possible. Here we'll calculate the probability of at least one student in the class of size [$a] getting more than 2 questions right.

    What is the probability of a particular student getting exactly 2 questions right? [______]{Compute("10!/(2!8!) * 0.5^10")}

    What is the probability of a particular student getting exactly 1 question right? [______]{Compute("10!/(1!9!) * 0.5^10")}

    What is the probability of a particular student getting no questions right? [______]{Compute("1 * 0.5^10")}

    What is the probability of a particular student getting at most 2 questions right?[_____]{Compute("10!/(2!8!) * 0.5^10+ 10!/(1!9!) * 0.5^10 + 1 * 0.5^10")}

    What is the probability of a particular student getting 3 or more questions right?[_____]{Compute("1- ( 10!/(2!8!) * 0.5^10+ 10!/(1!9!) * 0.5^10 + 1 * 0.5^10)")}

    What is the probability of every student in the class getting 3 or more questions right?[____]{Compute(" (1- ( 10!/(2!8!) * 0.5^10+ 10!/(1!9!) * 0.5^10 + 1 * 0.5^10) ) ^ $a ")}

    What is the probability of some student in the class getting at most 2 questions right?[_____]{Compute( " 1 -  ((1- ( 10!/(2!8!) * 0.5^10+ 10!/(1!9!) * 0.5^10 + 1 * 0.5^10) ) ^ $a ) " )}




Problem 3

    $p = random(6,8,1);
    if ($p == 6) {$a =Compute("(C(10,$p)+C(10,$p+1)+C(10,$p+2)+C(10,$p+3)+1)/(2^10)");}
    if ($p == 7) {$a = Compute("(C(10,$p)+C(10,$p+1)+C(10,$p+2)+1)/(2^10)");}
    if ($p == 8) {$a = Compute("(C(10,$p)+C(10,$p+1)+1)/(2^10)");}

    Here we will calculate the probability of a student getting at least [$p*10] percent on a true/false exam with 10 questions.

    The probability that a student gets a grade of [$p*10] percent or better by guessing is [__________________________________________________________________]{$a}




Problem 4

    $R=random(4,9,1);
    $A1=Formula("[$R]^4");

    Suppose a seqeunce of 4 digits in the range 1-[$R] is chosen uniformly
    at random. What is the probability that the first and third digit are
    equal, the second and the fourth digits are equal, but the first and
    second digits are unequal?

    1.  We are going to use the standard formula for probability of sets
        in a discrete uniform distribution space: the probability of a set
        [`A`] in an event space [`\Omega`] is

        [``P(A) = \frac{|A|}{|\Omega|}``]

    2.  In the enumerator we place the _size_ of the sample space. This is
        easy, as we have [$R1] choices in each of the four locations the
        number of sequences, which is equal to the size of the sample
        space, thus [`|\Omega| =`] [__________]{"[$R]^4"} (remember that "2^3"
        means [`2^3`] )

    3.  Now we want to compute the size of the set [`A`]. To do that it is
        useful to realize that we need only concern ourselves with the
        choices of two digits, say digits 1 and 2.  This is because digit
        1 determines the value of digit 3 and digit 2 determines the value
        of digit [_]{4}. Now, how many choices do we have for digit 1?
        Obviously, any integer in the range [`1,\ldots,[$R]`], or [$R]
        choices. Once the first digit has been chosen, we have one less
        choice for the second digit, in other words [$R-1]. The size of
        the set [`A`] is the product of these two numbers,
        i.e. [_______________]{"([$R]-1)*[$R]"}

    4.  Putting this all together we get that the probability of [`A`] is

    [`P(A)=`] [_______]{"$R*($R-1)"} / [_________]{"$R^4"} = [___________________________]{"$R*($R-1)/($R^4)"}




Problem 5
(Set problem)

    $min = random(1,5,1);
    $max = random(5,10,1);
    @R = ($min..$max);
    $oneDraw = Set(join(",",@R));
    @a = ();
    foreach $i(@R) {
        foreach $j(@R) {
            push(@a, ($i+$j))
        }
    }
    $S = Set(join(",",@a));

    BEGIN_PGML

    You are given two decks of numbered cards, each deck consists of [$max-$min+1] cards numbered from [$min] to [$max].  

    An experiment consists of drawing a card from each deck and summing their values. The sum is the outcome of the experiment. What is the outcome space?

    Recall that the outcome space is the set of all possible outcomes. Since one card draw can be any of [$oneDraw], the outcome space of the sum of two draws includes all possible results obtained by summing up two draws from [$oneDraw]. The outcome space of the sum is therefore,  [__________________________________________________]{$S}



Problem 6

    $n=random(10,20,1);
    $ans = Formula("$n*($n-1)*($n-2)");

    #### Sampling with and without replacement when the order matters ####
    Suppose there are four children---Alice, Bill, Christie, and Doug---at an animal
    shelter, checking out the current pool of [`n`] dogs. Each child writes down the
    name of the dog he or she likes most. How many possible outcomes are there?

    We can represent each outcome as a 4-tuple (Alice's choice, Bill's choice,
    Christie's choice, Doug's choice) in which each entry is the name of a dog.
    So the number of outcomes is [`n^4`]

    Now suppose that these same children are actually picking out dogs. First Alice
    chooses a dog to adopt, then Bill chooses a dog to adopt, and so on. How many
    outcomes are there now?

    In this situation, Alice has [`n`] choices, but Bill has only [`n-1`] choices,
    Christie has [`n-2`] choices, and Doug has [`n-3`] choices. So there are [`n(n-1)(n-2)(n-3)`] possible outcomes.

    The first situation is called _sampling with replacement_: the
    outcomes are tuples in which the same element (dog) can occur more
    than once. The number of such [`k`] tuples, chosen from [`n`] elements, is [`n^k`]  In the example, [`k=4`]  The second situation is _sampling
      without replacement_: the outcomes are tuples in which no element
    can be repeated. The number of such [`k`] tuples, chosen from [`n`] elements, is [`n(n-1)(n-2) \cdots (n-k+1)`]

    Here's a related question: how many ways are there to order (shuffle)
    a deck of 52 cards?  (Each such ordering is called a _permutation_
    of the cards.) Well, the result is a 52-tuple, drawn from a set of
    size 52, in which no card is repeated. Therefore, the number of
    permutations is [`52 \cdot 51 \cdot 50 \cdots 1`]  which is called [`52 `]     _factorial_ and denoted as [`52!`]  More generally, the number of permutations of [`n`] elements is [`n`] factorial or [`n!`]

    To Rcap, how many ways are there to order 10 elements? [_____]{"10!"} (you can use expressions such as 3*2 and 7! in your answer).

    Coming back to sampling [`k`] out of [`n`] elements without replacement,
    we can write it succinctly as
    [``
    n(n-1)(n-2) \cdots (n-k+1) = \frac{n!}{(n-k)!}
    ``]

    *Question:*
    Suppose you have a deck with [$n] different cards. (*Copy* the number
    of cards here [__]{$n}) How many ways are there to choose 3 cards out
    of this deck? (the order of the 3 picked out cards _does_ matter)
    o [_____________]{"$n!/($n-3)!"} (Note: You don't have to perform the
    calculation, you can instead use the notation for factorial [`n!`] in
    your answer).




Problem 7

    $a=random(2,3,1);
    $n=Compute("P(26,$a)");
    $b=random(3,6,1);
    $b2=Compute("$b+2");
    $c=Compute("($b+1)*P(26,$a)+1");
    $cr=$c->eval();
    $d=Compute("($b-1)*P(26,$a)+1");
    $showHint = 3;

    Consider a list of randomly generated [$a]-letter "words" printed on a paper. The letters cannot be repeated.
    (a) What is the size of the set of allowed words?
    Answer = [__________]{Compute("P(26,$a)")}
    (b) At least how many of these "words" should be printed to be sure of having at least [$b] identical "words" on the list?
    Answer = [_______________]{Compute("($b-1)*P(26,$a)+1")}
    (c) At least how many identical "words" are printed if there are [`[$c]`] "words" on the list?
    Answer = [_______________]{Compute("$b+2")}






Problem 8

    $R1=random(5,20,1);  # Number of balls (both white and black)
    $R2=random(2,$R1-1,1);  # Number of white balls
    $TestPoints=[[1,3],[2,3],[3,3],[2,10],[5,10],[7,10],[9,10]];
    #$TestPoints=[[1,2]];

    $F1 = Formula("n!/(n-k)");
    $F1 ->{test_points} = $TestPoints;

    $F2 = Formula("k!");
    $F2->{test_points}=[[1],[2],[3],[4],[5],[6],[7],[8],[9]];

    $F3 = Formula("n!/((n-k)!(k)!)");
    $F3->{test_points} = $TestPoints;

    TEXT(PGML::Format2(<<'END_PGML'));
    #### Sampling without replacement when the order doesn't matter ####

    Snow White is off to pick strawberries and asks three of the dwarfs (chosen
    from the set of size seven: [`\{\mbox{Dopey, Grumpy, Doc, Happy, Bashful, Sneezy, Sleepy}\}`] to join
    her. How many possible groups are there?

    In this case, it is misleading to represent an outcome as a 3-tuple,
    because, for instance, [`\mbox{(Dopey, Sleepy, Doc)}`] is a different
    3-tuple from [`\mbox{(Sleepy, Dopey, Doc)}`] but they represent the
    same group. So if we count tuples, we would be
    _over-counting_. Instead, we ought to represent an outcome as a set,
    [` \{\mbox{Dopey, Doc, Sleepy}\}`]

    So the question becomes: how many different subsets of three dwarfs are there?
    In general, a set of size [`n`] has

    (A) [``{n \choose k} \ \doteq \ \frac{n!}{k! (n-k)!} ``]

    subsets of size [`k`].  So in our example, the answer is [`{7 \choose 3} = 35`]. Formula (A) is called the _Binomial formula_ or the _Binomial coefficient_.

    Let's step back and derive Formula (A): how many subsets of size [`k`]
    does a set of [`n`] elements have? We will use the following
    strategy. First, we will assume that the order of the elements in the
    set *does* matter. Then we will calculate the amount by which we
    over-counted and divide the first result by it.

    1. How many sequences of length [`k`] (where order *does* matter) can
     we choose from a set of [`n`] different elements? We already have
     the formula for this from the analysis of "sampling without
     replacement when the order matters" (remember the children choosing
     the dogs example...). So you surely remember that the formula is
    END_PGML
    BEGIN_TEXT
    $BCENTER    (B)  \{ans_rule(15)\} $ECENTER
    END_TEXT
    $TestPoints2 = [[1,3],[3,3],[2,6],[3,5],[7,15]];
    ANS(fun_cmp("n!/(n-k)!", var=>["k","n"], test_points=>$TestPoints2));
    BEGIN_PGML
    2. Ok, so now we have the number of sequences of length [`k`], but we
     want to count *sets* not *sequences*, in other words, order does
     not matter. By counting all sequences we have counted each set a
     number of times. Convince yourself that this number is the same for
     all sets of size [`k`]. If we can calculate this number, we can
     divide formula (B) by it and get the correct number of sets. So,
     how many ways are there to order [`k`] elements? (hint, recall
     computing the number of ways to shuffle a deck of cards) it is:
    END_PGML
    BEGIN_TEXT
    $BCENTER   (C) \{ans_rule(15)\} $ECENTER
    END_TEXT
    $TestPoints1 = [1,2,3,4,5,6,7,10];
    ANS(fun_cmp("k!", var=>["k"], test_points=>$TestPoints1));
    BEGIN_PGML
    3. Dividing (B) by (C) we get the Binomial Equation:
    END_PGML
    BEGIN_TEXT
    $BCENTER    (A) \({n \choose k} = \) \{ans_rule(15)\} $ECENTER
    END_TEXT
    ANS(fun_cmp("n!/(k!(n-k)!)", var=>["k","n"], test_points=>$TestPoints2));
    BEGIN_PGML
    ---
    *EXAMPLE:*
    Binomials appear everywhere. here is another example: how many strings in [`\{0,1\}^{10}`] contain exactly
    _four_ 1s?  Well, we need to choose four positions of the ten
    possibilities in which to place the 1s; that is, we choose a subset of
    size four from [`\{1,2,\ldots,10\}`]   The number of ways to do this is [`{10 \choose 4} = 210`]

    *PROBLEM:*
    Suppose we have [$R1] bins, numbered 1,...,[$R1] and that we have [$R1] balls,
    [$R2] of them white and [$R1-$R2] of them black.

    o How many white/black patterns can one make by placing the balls in the bins? [________]{"$R1!/($R2!*($R1-$R2)!)"}




Problem 9

    $R1=random(8,15,1);
    $R2=random(2,$R1-2,1);
    $F=fact($R1)/(fact($R2)*fact($R1-$R2));

    #### Choosing candies ####
    This is a challenge problem, you have until wed to solve it.
    It is recommended that you try, this will help you understand what we
    do in class.
    ---
    You walk into a candy store and notice that there are five types of candy. Your mother allows you to pick exactly three pieces of candy, of whichever type(s)
    you want. How many ways are there to do this?

    You can represent the outcome by 5-tuple [`(n_1, n_2, \ldots, n_5)`] in
    which [`n_i`] is the number of pieces of the [`i`] h type of candy. How
    many such tuples are there, subject to [`n_1 + n_2 + \cdots + n_5 = 3`]
    To answer the question, we'll represent each tuple in a different
    format, as a sequence of length 7 containing three stars and four
    bars. For instance, the sequence [`|\,**\,|\,|\,|\,*`] denotes [`(0,2,0,0,1)`] (two candies of type 2 and one candy of type 5): the
    number of candies of type [`i`] is the number of stars between the [`(i-1)`] t and [`i`] h bars.

    So we have rephrased the question thus: how many sequences are there
    with four bars and three stars? Well, this is a sequence of size 7,
    and we must pick three of the seven positions at which to place
    stars. The number of such choices is [`{7 \choose 3} = 35`]

    *PROBLEM:*
    Suppose balls come in [$R1] colors and that you are to pick out [$R2] balls. How many different color combinations are possible?

    By the analogy explained above, how many bars do you need[______]{($R1-1)}
    By the analogy explained above, how many stars do you need[______]{($R2)}

    o The number of color combinations is [______]{"(($R2+$R1-1)!)/(($R2)!*($R1-1)!)"}





Problem 10

    $R1=random(7,15,1);	   # number of cards
    $R2=random(2,$R1-1,1);    # number of envelopes

    ### Putting cards in envelopes (Guided Problem) ###
    This is a challenge problem, you have until wed to solve it.
    It is recommended that you try, this will help you understand what we
    do in class.
    ---
    Suppose we have [$R1] cards and [$R2] envelopes to put them in. The envelopes are marked (1,...,[$R2]).
    We will calculate the number of ways to put the cards into the envelopes under different conditions.

    1.  Suppose all the cards are *distinct* (i.e. are numbered
        (1,2,....,[$R1])). How many ways are there to place cards into
        envelopes?
        As should be expected from the first part of a question, this is
        an easy one. Think of placing the cards into envelopes in the
        following way: take the first card and choose an envelope for it,
        then take the second card and choose an envelope for it etc. Until
        all of the cards have been placed. Clearly we can get any possible
        combination this way. It takes a little thought, but you can also
        convince yourself that there is only *one* way to get each
        combination. In other words, there is no overcounting.

        Counting the number of combinations we get this way is simple. At
        each of the [$R1] step we place one card in one of the [$R2]
        envelopes. Taking the product over all of these steps we get that
        the number of combinations is [____________]{Compute("$R2^$R1")}

    2.  Suppose that cards are *identical*. (The envelopes remain distinct)
        How many combinations are possible in this case?

        Consider the difference between part 1 and part 2. In part 1, each configuration
        specified exactly *which* cards were placed in each envelope. Here
        the cards are identical, therefor we can only say how *many* cards
        are in each envelope, but we cannot identify them.

        Thinking of the problem this way, we realize that it is
        mathematically equivalent to the problem of choosing [$R1] candies
        when there are [$R2] *types* of candy to choose from. As the Candies
        are indistinguishable, we are only interested in the number of
        candies chosen from each type. The correspondence is card <-> candy and candy type <-> envelope.

        If you go back to this problem, you will recall the formula for it and use it to get the
        answer: [__________]{Compute("C($R1+$R2-1,$R1)")}

    3.  Suppose the cards are identical as in 2. and, in addition, we
        require that each envelope contain at least one card.  In this
        case we first have to check that the number of cards is at least
        as large as the number of envelopes, otherwise there will be no
        way to satisfy the requirements. Luckily (thanks to the magic of
        WebWork) [`[$R1]>[$R2]`].

        OK, good. Now we can proceed in two steps, first, take [$R2] cards
        and put one card in each envelope, satisfying the reuirement that
        each envelop contains a card. The remaining cards can be placed in
        any envelope, with no constraints. We now have the same situation
        we had in part 2. but where, instead of [$R1] cards, we have
        [$R1]-[$R2]=[$R1-$R2] cards. We use the same formula that we used
        in 2. to find that the answer is
        [________________]{Compute("C($R1-1,$R1-$R2)")}




Problem 11

    $nCards=random(4,7,1);
    $b=random(2,$nCards-1,1);
    $nSame = Compute("C(13,$b)");
    $nTotal = Compute("C(52,$nCards)");
    $nOther = Compute("C(39,$nCards-$b)");
    $nEvent = Compute("$nSame * $nOther");
    $ans = Compute("4*C(13,$b)*C(39,$nCards-$b)/C(52,$nCards)");

    ## Probability of cards of the same suite ##
    A poker hand consisting of [$nCards] cards is dealt from a standard deck of 52 cards.
    Find the probability that the hand contains exactly [$b] cards of the same suite. It is allowed to have any number of cards in other suites.

    First, we know the number of all possible hands of [$nCards] cards is [______]{$nTotal}.

    Then, we calculate the number of hands that contain exactly [$b] cards of the same suite.

    	We first choose which suite the [$b] cards is. Obviously, there are [______]{4} possibilities.

    	The number of possibilities for the ranks of these cards is [_______]{$nSame}.

    	The other [$nCards-$b] cards in the hand can be any cards that has a different suite than the [$b] cards. There are a total of [______]{52-13} such cards. To choose [$nCards-$b] from them, there are [________]{$nOther} possibilities.

    	Thus we can compute the number of hands that have exactly [$b] cards of the same suite, which is [______]{Compute("4*C(13,$b)*C(39,$nCards-$b)")}.

    Finally we can calculate the probability of such hands, by calculating th ratio of the number of such hands to the number of all hands. This is [_______]{$ans}




Problem 12

    $ns = random(4,6,1);
    $nr = random(10,16,1);
    $n = $ns*$nr;

    ## Probability of Poker Hands ##
    You are given a deck of cards with *[$ns] suites* and *[$nr] ranks*. A hand consists of 5 cards from this deck, and may fall into one of the categories. We are going to compute the probability of each category.

    First, the number of all possible hands is [_____]{Compute("C($n,5)")}.




Problem 13

    $ns = random(4,6,1);
    $nr = random(10,16,1);
    $n = $ns*$nr;

    ### Two Pairs ###

    *Remember, the deck you are using has [$ns] suits and [$nr] ranks.*

    1. The number of possibilities for the ranks of the two pairs is [______]{Compute("C($nr,2)")}.

    2. The number of possibilities for the rank of the single is [______]{$nr-2}.

    2. The number of possibilities for the suits of the two pairs is [_____]{Compute("C($ns,2)**2")}.

    3. The number of possibilities for the suit of the single is [______]{$ns}.

    4. Thus the number of hands with exactly two pairs is [______]{Compute("C($nr,2)*($nr-2)*C($ns,2)**2*$ns")}.

    5. The ratio of this number to the number of all hands [______]{Compute("C($nr,2)*($nr-2)*C($ns,2)**2*$ns/C($n,5)")}.




Problem 14

    $ns = random(4,6,1);
    $nr = random(10,16,1);
    $n = $ns*$nr;

    ### Straight : Five cards in sequence, but not all from the same suit ###
    *Remember, the deck you are using has [$ns] suits and [$nr] ranks.*

    1. In the case of a standard deck, the ranks of a straight is one of (Ace,2,3,4,5) ... (10,J,Q,K,Ace). Similarly, in your deck, the number of possibilities for the ranks of a straight is [______]{Compute("$nr-3")}.

    2. The suits can be anything other than all equal, so the number of possibilities for the suits of a straight is [______]{Compute("$ns**5 - $ns")}.

    4. Thus the number of hands that is a straight is [______]{Compute("($nr-3)*($ns**5-$ns)")}.

    5. The ratio of this number to the number of all hands [______]{Compute("($nr-3)*($ns**5-$ns)/C($n,5)")}.





Problem 15

    $ns = random(4,6,1);
    $nr = random(10,16,1);
    $n = $ns*$nr;

    ### Full House: 2 of one rank and 3 of another rank ###
    *Remember, the deck you are using has [$ns] suits and [$nr] ranks.*

    1. The number of possibilities for the rank of the triple is [______]{$nr}.

    2. Given the rank of the triple, the number of possibilities for the rank of the pair is [______]{$nr-1}.

    2. The number of possibilities for the suit of the triple is [_____]{Compute("C($ns,3)")}.

    3. The number of possibilities for the suit of the pair is [_____]{Compute("C($ns,2)")}.

    4. Thus the number of hands that is a full house is [______]{Compute("$nr*($nr-1)*C($ns,3)*C($ns,2)")}.

    5. The ratio of this number to the number of all hands [______]{Compute("$nr*($nr-1)*C($ns,3)*C($ns,2)/C($n,5)")}.
