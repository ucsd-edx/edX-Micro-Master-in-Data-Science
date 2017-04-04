## Week5

        Assigned problem file name:
        +--------+------------+--------------------------------------------------------------+
        | set_id | problem_id | source_file                                                  |
        +--------+------------+--------------------------------------------------------------+
        | Week5  |          1 | Reorganized/ConditionalProbability/Independence_1.pg         |
        | Week5  |          2 | Reorganized/ConditionalProbability/ConditionalProbability.pg |
        | Week5  |          3 | local/Reorganized/MarkovChebyshev/MarkovInequality.pg        |
        | Week5  |          4 | Reorganized/MarkovChebyshev/chebyshev_1.pg                   |
        | Week5  |          5 | Reorganized/MarkovChebyshev/RiggedDice.pg                    |
        | Week5  |          6 | Reorganized/ExpectationVariance/Notes_3_2_1.pg               |
        | Week5  |          7 | Reorganized/ExpectationVariance/Notes_3_2_2.pg               |
        | Week5  |          8 | Reorganized/Covariance/ContingencyTables1.pg                 |
        | Week5  |          9 | local/Reorganized/Covariance/ContingencyTables5.pg           |
        +--------+------------+--------------------------------------------------------------+



### Sorted with number of attempts
[problem 9](https://github.com/cse103/Attempt_Analysis/blob/master/clustering_code/clusters/Week5/md_files/Week5_9_clusters.md): 3017

		 part  1 :  65
		 part  2 :  18
		 part  3 :  27
		 part  4 :  21
		 part  5 :  3
		 part  6 :  24
		 part  7 :  116
		 part  8 :  51
		 part  9 :  114
		 part  10 :  68
		 part  11 :  84
		 part  12 :  980
		 part  13 :  340
		 part  14 :  817
		 part  15 :  289


[problem 4](https://github.com/cse103/Attempt_Analysis/blob/master/clustering_code/clusters/Week5/md_files/Week5_4_clusters.md): 2541

		 part  1 :  1471
		 part  2 :  1070


[problem 5](https://github.com/cse103/Attempt_Analysis/blob/master/clustering_code/clusters/Week5/md_files/Week5_5_clusters.md): 1193

		 part  1 :  231
		 part  2 :  453
		 part  3 :  187
		 part  4 :  322


problem 7 (Fill in table problem): 1089

		 part  1 :  397
		 part  2 :  692


[problem 8](https://github.com/cse103/Attempt_Analysis/blob/master/clustering_code/clusters/Week5/md_files/Week5_8_clusters.md): 956

		 part  1 :  106
		 part  2 :  62
		 part  3 :  43
		 part  4 :  22
		 part  5 :  20
		 part  6 :  16
		 part  7 :  79
		 part  8 :  33
		 part  9 :  154
		 part  10 :  68
		 part  11 :  65
		 part  12 :  89
		 part  13 :  38
		 part  14 :  62
		 part  15 :  99


problem 6 (Fill in table): 567

		 part  1 :  245
		 part  2 :  43
		 part  3 :  30
		 part  4 :  26
		 part  5 :  223


problem 2 (Graph problem): 372

		 part  1 :  311
		 part  2 :  61


[problem 3](https://github.com/cse103/Attempt_Analysis/blob/master/clustering_code/clusters/Week5/md_files/Week5_3_clusters.md): 269

		 part  1 :  179
		 part  2 :  90


[problem 1](https://github.com/cse103/Attempt_Analysis/blob/master/clustering_code/clusters/Week5/md_files/Week5_1_clusters.md): 25

		 part  1 :  25




### Problem Content

Problem 1

    ## Independence ##

    Two events are called _independent_ if the outcome of one (that is, whether or not it occurs) does not affect the probability that the other will occur. For instance, suppose you flip two fair coins. The outcome of either coin does not influence the other; therefore the two outcomes are independent.

    Formally, we say events [`A`] and [`B`] (defined on some sample space [`\Omega`]  are independent if
    [`` P(A \cap B)
    \ = \
    P(A) P(B).``]
    Can you show that this definition (assuming [`A`], [`B`] are independent) implies the following?

    [`P(A | B) = P(A)`]

    [`P(B | A) = P(B)`]

    [`P(A | B^c) = P(A)`]

    Assuming [`A`], [`B`] are independent, what is [`P(A \cap B) - P(A)P(B)`]? [_____]{0}



Problem 2

    ## Conditional Probability ##

    You meet a stranger, a random citizen of the United States. What's the chance that he (or, equally likely, she) votes for the Democratic party? Who knows, but it's probably close to [`50%`].
    [`` \Omega = \{\mbox{citizens of the US}\}, \ \ E = \{\omega \in \Omega: \mbox{votes Dem}\}.``]
    Now what if you find out a little bit more information: this stranger likes spicy food.
    [`` F = \{\omega \in \Omega: \mbox{likes spicy food}\}.``]
    How does change the odds? What is [`P(E|F)`] (``probability of [`E`] given [`F`] ')? Again, it's hard to say, but for illustrative purposes here is a (definitely incorrect) set of probabilities:
    [`` P(E) = 0.5, \ \ \ \ P(F) = 0.2, \ \ \ \ P(E \cap F) = 0.15.``]

    What is [`P(E \setminus F)?`] [____]{0.35} [`E \setminus F`] means the set of elements that are in [`E`] but not in [`F`].

    The Venn diagram for this scenario is:

    END_PGML
    BEGIN_TEXT
    $BR \{ image("ConditionalProbabilityDiagram.png", width=>250, height=>200) \}
    END_TEXT
    BEGIN_PGML

    If you stare at it a little bit, you will probably conclude, correctly, that [`P(E|F)`] is the chance that a point drawn from the small blob lies inside the large blob, namely [`0.15 / 0.2 = 0.75`].  By reasoning this way, you are implicitly using
    [`` P(E|F) \ = \ \frac{P(E \cap F)}{P(F)} .``]
    We will make heavy use of this and of the equivalent
    [`` P(E \cap F) = P(E|F) P(F).``]

    What is [`P(E|F)*P(F)/P(E \cap F)`]?  [_____]{1}



Problem 3

    $r = random(0.4,0.6,0.1);
    $k = random(100,200,1);
    $p = random($r+0.1,0.9,0.1);
    $n2 = random(300,500,1);
    $k2 = random(251,299,1);
    $ans1 = ceil($p*$k/$r);

    ### Markov's Inequality
    Markov's inequality relate probabilities to expectations, and provide bounds for the cumulative distribution function of a random variable.
    The Markov's inequality is stated as follow:

    If X is any nonnegative random variable and a > 0, then  [`\mathbb{P}(X \geq a) \leq \frac{\mathbb{E}(X)}{a}`]
    ---
    John has a biased coin with [`P(\mathrm{heads}) = [$r]`].
    He tosses this coin [`N`] times and, out of the [`N`] times,
    the coin lands on heads [$k] times.
    Using Markov's inequality that he learned from CSE103,
    he says that the probabality of seeing at least this many
    heads is at most [$p].

    o Give the best lower bound, using Markov inequality, on the number of times John tossed the coin?
    [`N`] = [____________]{Compute("$p*$k/$r")}
    (Provide the exact answer, don't round it to the next larger integer number.)

    Suppose John lends you this coin. If you flip the coin [$n2] times,
    what is the upper bound of the probability of seeing at least [$k2] heads
    using Markov's inequality?

    o [`P(\mbox{Number of heads} > [$k2])`] [`\le`] [____________]{Compute("$n2*$r/$k2")->with(tolType=>'absolute', tolerance=>'0.01')}



Problem 4

    $mean = 24;
    $sd = random(3,5,.1);
    $k = random(2,3,1);
    $record = 44;
    $a = $k*$sd;
    $b1 = $mean-$a;
    $b2 = $mean+$a;

    We will use Chebyshev's inequality in this problem. The Chebyshev's theorem is stated as below:

    Let X be a random variable with finite expected value [`μ`] and finite non-zero variance [`σ^2`]. Then for any real number [`k > 0`], [`\Pr(|X-\mu|\geq k\sigma) \leq \frac{1}{k^2}`], which is the same as [`\mathbb{P}(|X-\mathbb{E}(X)| \geq a) \leq \frac{\textrm{Var}(X)}{a^2}`] for any a>0.

    ---

    Suppose the mean noon-time temperature for September days in San Diego is [`[$mean]^{\circ}`] and the standard deviation is [`[$sd]`]. (Temperature in this problem is measured in degrees celsius)

    - Using Chebyshev's theorem, what is the *minimal* probability (in percents) that the noon-time temperature of a september days is between [`[$b1]^{\circ}`] and [`[$b2]^{\circ}`]? [__________________]{Compute("(1-(1/$k^2))*100")} %.

    - On September 26, 1963, the all-time record of noon-time temperature in San Diego of [`44^{\circ}`] was hit. Assume the temperature distribution is symmetric around the mean, what is the Chebyshev bound for the probability of breaking (or tieing) this record? [__________]{Compute("0.5*1/(($record-$mean)/$sd)^2")}



Problem 5

    $k = random(6,10,1);
    $t1 = random(2,5,1);
    $t2 = random(2,5,1);
    $r = random(0.1,0.6,0.1);

    $ans1 = Compute("$k*($k+1)/(2*$k)");
    $ans2 = Compute("2*$k/($k+1) + ($k*($k-1))/(2*($k+1))");
    $ans3 = Compute("$t1*$ans1 + $t2*$ans2");
    $ans4 = Compute("$ans3/$r");

    ### Rigged dice

    We have 2 [$k]-sided dice. The first die is a normal fair die where each face has a probability of showing of [`1/[$k]`]. However, the second die is rigged so that the probability of showing the largest face ([$k]) is twice as high as of the other faces and all of the other faces have equal probabilities.

    o What is the expected value of the outcome from tossing the fair die? [________]{$ans1}

    o What is the expected value of the outcome from tossingthe rigged die? [_________]{$ans2}

    We throw the fair die [$t1] times, then the rigged die [$t2] times consecutively and sum up all the outcomes:

    o What is the expected value of the sum? [____________]{$ans3}

    Let [`Y`] denote the sum from the previous part. If we know that

    [`P(Y > k) \le [$r]`]

    o According to Markov's inequality, what is [`k`]? [________________]{$ans4}



Problem 6 (table problem)

    ## The mean, or expected value ##

    For a random variable [`X`] that takes on a finite set of possible values, the
    [$BITALIC]* mean [$EITALIC]*, or [$BITALIC]* expected value [$EITALIC]*, is

    [$BCENTER]*
    [`` \mathbb{E}(X) \ = \ \sum_{x} x \, \mbox{Pr}(X = x) ``]
    [$ECENTER]*

    (where the summation is over all the possible values [`x`] that [`X`] can have). This
    is a direct generalization of the notion of [$BITALIC]* average [$EITALIC]* (which is typically
    defined in situations where the outcomes are equally likely). If [`X`] is a continuous
    random variable, then this summation needs to be replaced by an equivalent integral;
    but we'll get to that later in the course.

    Here are some examples.

    ---
    ### [$BITALIC]* Coin with bias (heads probability) [`p`]. [$EITALIC]* ###

    Define [`X`] to be [`1`] if the outcome is heads, or [`0`] if it is tails. Then

    [$BCENTER]*
    [`` \mathbb{E}(X)
    \ = \
    0 \cdot \mbox{Pr}(X = 0) + 1 \cdot \mbox{Pr}(X = 1)  
    \ = \
    0 \cdot (1-p) + 1 \cdot p
    \ = \ ``][______]{p}
    [$ECENTER]*

    Another random variable on this space is [`X^2`], which also takes on values in [`\{0,1\}`].
    Notice that [`X^2 = X`], and in fact [`X^k = X`] for all [`k = 1,2,3,\ldots`]! Thus,
    [`\mathbb{E}(X^2) = p`] as well. This simple case shows that in general, [`\mathbb{E}(X^2) \neq \mathbb{E}(X)^2`].

    ---

    ### [$BITALIC]* Fair die. [$EITALIC]* ###

    Define [`X`] to be the outcome of the roll, so [`X \in \{1,2,3,4,5,6\}`]. Then

    [$BCENTER]*
    [`` \mathbb{E}(X)
    \ = \
    1 \cdot \frac{1}{6} + 2 \cdot \frac{1}{6} + 3 \cdot \frac{1}{6} + 4 \cdot \frac{1}{6}
    + 5 \cdot \frac{1}{6} + 6 \cdot \frac{1}{6}
    \ = \ ``][_______]{3.5}.
    [$ECENTER]*

    ---

    ### [$BITALIC]* Two dice. [$EITALIC]* ###

    Let [`X`] be their sum, so that [`X \in \{2,3,4,\ldots, 12\}`]. We can calculate the probabilities
    of each possible value of [`X`] and tabulate them as follows:

    END_PGML

    $bHTML="";
    $eHTML="";
    $F1 = PGML::Format2("[`1/36`]");
    $F2 = PGML::Format2("[`2/36`]");
    $F3 = PGML::Format2("[`3/36`]");
    $F4 = PGML::Format2("[`4/36`]");
    $F5 = PGML::Format2("[`5/36`]");
    $F6 = PGML::Format2("[`6/36`]");
    $x = PGML::Format2("[`x`]");
    $y = PGML::Format2("[`\text{Pr}(X=x)`]");

    $F5_ANS = PGML::Format2(<<END_PGML);
    [____]{5/36}
    END_PGML;

    $F3_ANS = PGML::Format2(<<END_PGML);
    [____]{3/36}
    END_PGML;


    TEXT(
    BeginTable(),
    $PAR,
    Row([$x,2,3,4,5,6,7,8,9,10,11,12],separation=>10),
    Row([$y,$F1,$F2,$F3,$F4,$F5_ANS,$F6,$F5,$F4,$F3_ANS ,$F2,$F1],separation=>10),
    EndTable()
    );

    BEGIN_PGML

    This gives [`\mathbb{E}(X) = `][_________________________________________________________________]{7}.

    END_PGML



Problem 7 (table problem)

    ## The mean, or expected value (cont.) ##
    ---
    ### [$BITALIC]* Roll n die; how many sixes appear? [$EITALIC]* ###

    Let [`X`] be the number of [`6`]'s. We've already analyzed the distribution of [`X`], so

    [$BCENTER]*
    [`` E(X)
    \ = \
    \sum_{k = 0}^n k \, \mbox{Pr}(X = k)
    \ = \
    \sum_{k = 0}^n k {n \choose k} \left(\frac{1}{6} \right)^k \left( \frac{5}{6} \right)^{n-k}
    \ = \
    \frac{n}{6}.
    ``]
    [$ECENTER]*

    The last step is somewhat mysterious; just take our word for it, and we'll get back to it later!

    ---
    ### [$BITALIC]* Toss a fair coin forever; how many tosses to the first heads? [$EITALIC]* ###

    Let [`X \in \{1,2,\ldots\}`] be the number of tosses until you first see heads. Then

    [$BCENTER]*
    [`` \mbox{Pr}(X = k)
    \ = \
    \mbox{Pr}((T,T,T,\ldots,T,H))
    \ = \
    \frac{1}{2^k}.
    ``]
    [$ECENTER]*

    It follows that

    [$BCENTER]*
    [`` \mathbb{E}(X)
    \ = \
    \sum_{k=1}^\infty \frac{k}{2^k}
    \ = \ ``][______]{2}.
    [$ECENTER]*

    To answer this question we need the following formulas for the infinite geometric series: for any  [`0 < r < 1`]

    [$BCENTER]*
    [`` r + r^2 + \cdots \ = \ \frac{r}{1-r}.``]
    [$ECENTER]*
    and
    [$BCENTER]*
    [`` r + 2r^2 + 3r^3+\cdots \ = \ \frac{r}{(1-r)^2}.``]
    [$ECENTER]*

    You can find these and other useful sums here:
    http://en.wikipedia.org/wiki/List_of_mathematical_series#Low-order_polylogarithms

    ---
    ### [$BITALIC]* Toss a coin with bias [`p`] forever; how many tosses to the first heads? [$EITALIC]* ###

    Once again, [`X \in \{1,2,\ldots\}`], but this time the distribution is different:

    [$BCENTER]*
    [`` \mbox{Pr}(X = k)
    \ = \
    \mbox{Pr}((T,T,T,\ldots,T,H))
    \ = \
    (1-p)^{k-1}p.
    ``]
    [$ECENTER]*

    Using the same technique as before, we get [`\mathbb{E}(X) =`][______]{1/p}.

    There's another way to derive this expectation. We always need at least one coin toss.
    If we're lucky (with probability [`p`]), we're done; otherwise (with probability [`1-p`]),
    we start again from scratch. Therefore [`\mathbb{E}(X) = 1 + (1-p) \mathbb{E}(X)`], and we have the same result.




Problem 8

    $C11 = "1/16";
    $C12 = "2/16";
    $C13 = "1/16";
    $C21 = "2/16";
    $C22 = "4/16";
    $C23 = "2/16";
    $C31 = "1/16";
    $C32 = "2/16";
    $C33 = "1/16";

    $X1 = "($C11 + $C21 + $C31)";
    $X2 = "($C12 + $C22 + $C32)";
    $X3 = "($C13 + $C23 + $C33)";

    $Y1 = "($C11 + $C12 + $C13)";
    $Y2 = "($C21 + $C22 + $C23)";
    $Y3 = "($C31 + $C32 + $C33)";

    $E_X = "1*$X1 + 2*$X2 + 3*$X3";
    $E_Y = "1*$Y1 + 2*$Y2 + 3*$Y3";
    $E_XY = "1*$C11 + 2*$C12 + 3*$C13 + 2*$C21 + 4*$C22 + 6*$C23 + 3*$C31 + 6*$C32 + 9*$C33";
    $COV_XY  = "$E_XY - ( ($E_X) * ($E_Y) )";
    $E_X2 = "1*$X1 + 4*$X2 + 9*$X3";
    $E_Y2 = "1*$X1 + 4*$X2 + 9*$X3";
    $STD_X = "sqrt($E_X2 - ($E_X)**2)";
    $STD_Y = "sqrt($E_Y2 - ($E_Y)**2)";

    The following formula are useful for this assignment:
    - Covariance [`COV(X,Y) = E[XY]-E[X]E[Y]`]
    - Correlation coefficient [`r(X,Y) = \frac{COV(X,Y)}{\sqrt{VAR[X]}\sqrt{VAR[Y]}}`]

    TEXT(
    BeginTable(),
    $PAR,
    Row([" ", "X=1","X=2","X=3"],separation=>10),
    Row(["Y=1 ",$C11,$C12,$C13],separation=>10),
    Row(["Y=2 ",$C21,$C22,$C23],separation=>10),
    Row(["Y=3 ",$C31,$C32,$C33],separation=>10),
    EndTable()
    );

    BEGIN_PGML
    - The marginal distribution of [`X`] is [`P(X=1)=`][____]{"$X1"}, [`P(X=2)=`][____]{"$X2"}, [`P(X=3)=`][____]{"$X3"}
    - The marginal distribution of [`Y`] is [`P(Y=1)=`][____]{"$Y1"}, [`P(Y=2)=`][____]{"$Y2"}, [`P(Y=3)=`][____]{"$Y3"}
    - Are [`X`] and [`Y`] independent? [____]{"1"} (1=independent, 0=dependent)
    - Are [`X`] and [`Y`] identically distributed? [____]{"1"} (0=no, 1=yes)
    - [`E(X) =`][____]{"$E_X"}
    - [`E(Y) =`][____]{"$E_Y"}
    - [`E(X+Y) =`][____]{"$E_X + $E_Y"}
    - [`E(XY) = `][____]{"$E_XY"}
    - [`Cov(X,Y) =`][____]{"$COV_XY"}
    - The correlation coefficient between [`X`] and [`Y`] is [____]{"($COV_XY)/(($STD_X)*($STD_Y))"}.
    - Are [`X`] and [`Y`] correlated [____]{"0"} (1=Correlated, 0=uncorrelated, -1=anticorrelated)



Problem 9

    $C11 = "1/3";
    $C12 = "0";
    $C13 = "1/6";
    $C21 = "0  ";
    $C22 = "0";
    $C23 = "0  ";
    $C31 = "1/6";
    $C32 = "0";
    $C33 = "1/3";

    $X1 = "($C11 + $C21 + $C31)";
    $X2 = "($C12 + $C22 + $C32)";
    $X3 = "($C13 + $C23 + $C33)";

    $Y1 = "($C11 + $C12 + $C13)";
    $Y2 = "($C21 + $C22 + $C23)";
    $Y3 = "($C31 + $C32 + $C33)";

    $E_X = "1*$X1 + 2*$X2 + 3*$X3";
    $E_Y = "1*$Y1 + 2*$Y2 + 3*$Y3";
    $E_XY = "1*$C11 + 2*$C12 + 3*$C13 + 2*$C21 + 4*$C22 + 6*$C23 + 3*$C31 + 6*$C32 + 9*$C33";
    $COV_XY  = "$E_XY - ( ($E_X) * ($E_Y) )";
    $E_X2 = "1*$X1 + 4*$X2 + 9*$X3";
    $E_Y2 = "1*$X1 + 4*$X2 + 9*$X3";
    $STD_X = "sqrt($E_X2 - ($E_X)**2)";
    $STD_Y = "sqrt($E_Y2 - ($E_Y)**2)";

    TEXT(
    BeginTable(),
    $PAR,
    Row([" ", "X=1","X=2","X=3"],separation=>10),
    Row(["Y=1 ",$C11,$C12,$C13],separation=>10),
    Row(["Y=2 ",$C21,$C22,$C23],separation=>10),
    Row(["Y=3 ",$C31,$C32,$C33],separation=>10),
    EndTable()
    );

    - The marginal distribution of [`X`] is [`P(X=1)=`][____]{"$X1"}, [`P(X=2)=`][____]{"$X2"}, [`P(X=3)=`][____]{"$X3"}
    - The marginal distribution of [`Y`] is [`P(Y=1)=`][____]{"$Y1"}, [`P(Y=2)=`][____]{"$Y2"}, [`P(Y=3)=`][____]{"$Y3"}
    - Are [`X`] and [`Y`] independent? [____]{"0"} (1=independent, 0=dependent)
    - Are [`X`] and [`Y`] identically distributed? [____]{"1"} (0=no, 1=yes)
    - [`E(X) =`][____]{"$E_X"}
    - [`E(Y) =`][____]{"$E_Y"}
    - [`E(X+Y) =`][____]{"$E_X + $E_Y"}
    - [`E(XY) = `][____]{"$E_XY"}
    - [`Cov(X,Y) =`][____]{"$COV_XY"}
    - The correlation coefficient between [`X`] and [`Y`] is [____]{"($COV_XY)/(($STD_X)*($STD_Y))"}.
    - Are [`X`] and [`Y`] correlated [____]{"1"} (1=Correlated, 0=uncorrelated, -1=anticorrelated)
