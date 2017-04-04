##Week8

        Assigned problem file name:
        +--------+------------+-------------------------------------------------------+
        | set_id | problem_id | source_file                                           |
        +--------+------------+-------------------------------------------------------+
        | Week8  |          1 | local/Reorganized/RandomizedAlgs/TestingOrderInAnd.pg |
        | Week8  |          2 | Reorganized/RandomizedAlgs/RandAlgs_2_1.pg            |
        | Week8  |          3 | Reorganized/RandomizedAlgs/RandAlgs_2_2.pg            |
        | Week8  |          4 | Reorganized/RandomizedAlgs/QuicksortPivot.pg          |
        | Week8  |          5 | Reorganized/RandomizedAlgs/probs9QuicksortVariant.pg  |
        | Week8  |          7 | Reorganized/RandomizedAlgs/Hashing_1.pg               |
        | Week8  |          8 | Reorganized/RandomizedAlgs/Hashing_2.pg               |
        | Week8  |          9 | Reorganized/RandomizedAlgs/Hashing_3.pg               |
        +--------+------------+-------------------------------------------------------+


### Sorted with number of attempts
	 problem  3 :  2719
			 part  1 :  944
			 part  2 :  320
			 part  3 :  615
			 part  4 :  840


	 problem  5 :  2126
			 part  1 :  387
			 part  2 :  1090
			 part  3 :  304
			 part  4 :  345


	 problem  2 :  1549
			 part  1 :  871
			 part  2 :  449
			 part  3 :  88
			 part  4 :  141


	 problem  4 :  940
			 part  1 :  227
			 part  2 :  69
			 part  3 :  251
			 part  4 :  393


	 problem  8 :  661
			 part  1 :  661


	 problem  1 :  311
			 part  1 :  93
			 part  2 :  97
			 part  3 :  48
			 part  4 :  73


	 problem  6 :  194
			 part  1 :  194


	 problem  7 :  112
			 part  1 :  112


### Problem Content

Problem 1

    $N=random(3,10,1);
    $T=random(1,$N-1,1);
    $F=$N-$T;

    [``\newcommand{\E}{\mathbb{E}}``]
    [``\newcommand{\R}{\mathbb{R}}``]
    [``\newcommand{\bP}{\mathbb{P}}``]
    [``\newcommand{\var}{\mbox{var}}``]
    [``\newcommand{\pr}{\mbox{Pr}}``]
    [``\def\X{{\cal X}}``]
    [``\def\cost{{\mbox{cost}}}``]
    [``\def\U{{\cal U}}``]
    [``\renewcommand{\log}{\mbox{log}_2}``]

    #### Order Of Evaluation ####

    Suppose C1,C2 are boolean variables and that A equal to their conjunction:

    A= C1 and C2

    Our goal is to evaluate A by checking the smallest number of C's.

    Because this is a conjunction, it is enough to find one variable that is false to make A false. Therefor a good technique is to check the two variables one after the other and stop early if the variable is false.

    However, we don't know what the values of the C's are until we check them. This is a situation in which randomization can help.

    We will contrast two methods:
    * **Deterministic Method:** Check C1, if True, check C2
    * **Randomized Method:** Chose C1 or C2 at random, by flipping a fair coin. If the chosen variable is True, check the other.

    Lets compare how many checks need to be done in difference situations:

    * **C1=False, C2=False **
        - The Deterministic method will require [_____]{1} checks.
        - The expected number of checks of the randomized method is [_____]{1}
    * **C1=True, C2=True**
        - The Deterministic method will require [_____]{2} checks.
        - The expected number of checks of the randomized method is [_____]{2}
    * **C1=True, C2=False **
        - The Deterministic method will require [_____]{2} checks.
        - The expected number of checks of the randomized method is [_____]{1.5}
    * **C1=False, C2=True **
        - The Deterministic method will require [_____]{1} checks.
        - The expected number of checks of the randomized method is [_____]{1.5}

    If we are interested in the worst case (the worst performance over the 4 choices above) we find that
        - The Deterministic method will require [_____]{2} checks in the worst case
        - The expected number of checks of the randomized method in the worst case is [_____]{1.5}



Problem 2

    # Transforming Las Vegas to Monte Carlo

    Suppose you have an algorithm A for your problem that always returns the correct answer, but takes different amounts of time each time it runs.  Let [`X_n`] be the random variable giving the time algorithm A takes to complete for input of size [`n`].  Time can't be negative, so [`X \geq 0`].
    We call A a _Las Vegas Algorithm_ if for any input size [`n`] there is a [`T(n)`] so that [`\mathbb{E}(X_n) = T(n)`].
    - Side note: it isn't always the case that a random variable has finite expectation, even the values it can take on are finite.  The assumption that there is some [`T(n)`] for any [`n`] is a non-trivial assumption.

    Let's say we have algorithm that determines whether any integer is prime.  For an integer input that takes up [`n`] bits, the algorithm takes [`n`] seconds to run with probability [`1/2`].  With probability [`1/2`] the algorithm takes 1 second to run.  What is [`T(n)`], in seconds?  [_______]{"1/2+1/2*n"}.

    Let's say you have some Las Vegas algorithm A that runs in _expected time_ [`T(n)`] for problem size [`n`].  What you would prefer, however, is an algorithm that _always_ finishes in time [`O(T(n))`], but may have up to a 5% probability of returning the wrong answer.  We will construct an algorithm A' from A that satisfies these properties.

    Recall Markov's inequality: for some random variable [`Y \geq 0`], [`P(Y >= a) \leq \mathbb{E}(Y)/a`].
    Fixing some [`n`], apply Markov's inequality to get an upper bound on [`P(X_n >= cT(n))`]: [_____]{"1/c"}.
    What is [`c`] such that [`P(X_n >= cT(n)) <= 0.05`]?  [_______]{"20"}

    Thus an algorithm A' is as follows:
    * Run A until time [_______]{"20"}T(n).  If A has completed, return the correct value.
    * Else, return a random value.

    This type of algorithm we have, where the algorithm completes in deterministic time [`Q(n)`] but is correct with some probability is called a _Monte Carlo Algorithm_.

    _Recap_:
    - For "Las Vegas" algorithms, uncertainty is in the algorithm _runtime_.  The algorithm is always correct.
    - For "Monte Carlo" algorithms, uncertainty is in the algorithm _correctness_.  The algorithm completes in deterministic time [`T(n)`].



Problem 3

    $k = random(3,5);
    $p = Compute("($k-1)/$k");
    $z = Compute("(0.5-$p)/(sqrt($p*(1-$p)/n))");
    $q = Compute("Qinv(0.05)");
    $n_normal = Compute("($q*sqrt($p*(1-$p))/(0.5-$p))**2");

    You have an algorithm A for testing whether a Boolean formula f is satisfiable or not, but it is only correct with probability [`[$k-1]/[$k]`]. More precisely, you can repeatedly run A on the same formula f, and each time it outputs the correct answer with probability [`[$k-1]/[$k]`].

    To reduce the probability of error, you run A(f) [`n`] times, and return the majority answer. What should [`n`] be if you want the probability of error to be less than 0.05?

    ---

    Let [`C_i`] be a binary random variable indicating whether the [`i^{th}`] execution of algorithm A is correct.  Let [`C = (C_1 + C_2 ... C_n)/n`].
    - What is the minimum value of [`C`] such that our method of returning the majority answer will be correct?  [_____]{"1/2"}
    - What is [`\mathbb{E}(C)`]?  [________]{"$p"}
    - What is [`var(C)`]?  [_________]{"(1/n)*$p*(1-$p)"} (Use [`n`] as variable in this answer)

    ---
    _Approach 1_:
    Chebyshev's inequality says for random variable [`Y`] with mean [`\mu`] and for any positive number [`a>0`], $$P(|Y-\\mu| \\geq a) \\leq var(Y)/a^2$$
    - Using Chebyshev's inequality, what is an upper bound on the probability your "majority algorithm" is incorrect?  [_________________]{Compute("(1/n)*$p*(1-$p)/(($p-0.5)**2)")}  (Use [`n`] as variable in this answer)
    - What is the smallest *integer* value for [`n`] so that the probability that the "majority algorithm" makes an error is  at most 0.05?  [________________]{ceil(20*$p*(1-$p)/(($p-0.5)**2))} (Give a numerical answer)

    ---

    _Approach 2_:
    Using Central Limit Theorem, approximate the distribution of [`C`] as a normal.
    - What is the z-score of [`C=0.5`] [___________]{$z} (Use [`n`] as variable in this answer)
    - What is the smallest *integer* value for [`n`] so that the "majority algorithm" makes an error with probability at most 0.05? [_____________________]{ceil($n_normal)} (Give a numerical answer. Use [`Q^{-1}(0.05) = 1.6449`], where [`Q^{-1}`] is the inverse of Q function)

    ---

    Notice that [`n`] obtained with Approach 2 is much smaller than that obtained with Approach 1, this is because using the normal approximation and Q function give us a much tighter bound than the Chebyshev bound. (The Q function drops exponentially fast as the value deviates from the mean, while the Chebyshev bound drops only quadratically fast)



Problem 4

    $t = random(2,10,1);

    ## Selecting a Percentile (Quantile) ##

    Let [`S`] be a set of [`n`] different numbers (think of [`n`] as being very large).
    Suppose we want to find the [`k^{th}`] biggest element in [`S`], for any [`k \leq n`].
    Of course, we could just sort [`S`] and then pick out the answer, but this would take [`n \log n`] time. Can we do better?

    In this problem, we will look at an (expected) linear-time algorithm
    for finding the [`k^{th}`] biggest element in [`S`], for any [`k \leq n`].
    The algorithm is randomized, and we'll specify it soon.

    First suppose we pick a random element of [`S`] - call it [`v`] - and let [`S_L = \{ x \in S \mid x < v \}`] and [`S_U = \{ x \in S \mid x > v \}`] be the elements less than and greater than [`v`].

    *(a)* What is the probability that [`\left| S_L \right|`], the size of [`S_L`], is equal to [$t]? [____________________]{1/n} (Hint: what value(s) can [`v`] take for this to happen? What's the probability of choosing such [`v`]?)

    *(b)* What is the approximate probability that [`\left| S_L \right|`] is _between_ [`\lceil n/4 \rceil`] and [`\lceil 3n/4 \rceil`]? (Round your answer to one decimal place.) [____________________]{"0.5"}

    If [`v`] is chosen so that [`\mid S_L \mid \in [n/4, 3n/4]`], then this implies [`\left| S_U \right| \in [n/4, 3n/4]`] as well, so each of the two sets has a significant fraction of the elements.
    We'll call such a choice of [`v`] _lucky_.


    *(c)* We'll consider a randomized algorithm for finding the [`k^{th}`] biggest element in [`S`] - call this value [`f (k, S)`]. (For example, [`f (1, S)`] would be the maximum element in [`S`], and [`f (\frac{1}{2} \left| S \right|, S)`] the median.)

    The algorithm chooses an element [`v`] at random from [`S`] and computes [`\left| S_L \right|`] and [`\left| S_U \right|`], to determine if this choice of [`v`] is lucky. If not, it chooses [`v`] again at random and repeats until it chooses a lucky [`v`].

    When a lucky [`v`] is chosen, the algorithm computes [`\left| S_L \right|`] and [`\left| S_U \right|`], and then does one of two things:

    1.  If [`\left| S_L \right| \geq k`], then the [`k^{th}`] biggest element in [`S`] is in [`S_L`]. Actually, it must be the [`k^{th}`] biggest element in [`S_L`] as well, so in this case the algorithm just recursively finds [`f(k, S_L)`].

    2.  If [`\left| S_L \right| < k`], then the [`k^{th}`] biggest element in [`S`] is in [`S_U`]. Specifically, it must be the [`(k - \left| S_L \right|)^{th}`] biggest element in [`S_U`], so in this case the algorithm just recursively finds [`f(k - \left| S_L \right|, S_U)`].

    Note that in both cases, we end up recursively working on a set ([`S_L`] or [`S_U`]) that is at most 3/4 the size of the current set [`S`], because our choice of [`v`] is lucky.

    However, our lucky choices take a random time to generate because of the randomized way in which they're chosen. Our randomized algorithm continues choosing values of [`v`] one at a time independently, until it makes its first lucky choice. Using the answer to part (b) and how our randomized algorithm works, the expected number of random choices of [`v`] required to generate a lucky choice is [____________________]{"2.0"}


    *(d)* Finally, consider the overall runtime of our randomized selection algorithm. This is a random variable. We will look at the _expected_ runtime [`T(n)`] on problem size [`n`] (size of [`S`]).

    Suppose [`b`] is the answer to part (b) above. Then every time the algorithm tries a random choice of [`v`], there is a probability [`b`] that the choice is lucky, in which case the remaining runtime is no more than [`T(3n/4)`]; and a probability [`1-b`] that the choice is unlucky, in which case the algorithm basically starts again from scratch with problem size [`n`]. Also, the random choice itself takes time [`n`], to verify whether it is lucky or not by building [`S_L`] and [`S_U`].

    Putting this together,
    [`T(n) \leq n + b T(3n/4) + (1-b) T(n)`]. Rearranging terms,
    [`T(n) \leq \frac{n}{b} + T(3n/4)`].
    Solving this inequality,
    [`T(n) \leq \frac{n}{b} + \frac{3n}{4b} + T((3/4)^2 n) \leq \frac{n}{b} \left( 1 + \frac{3}{4} + \left( \frac{3}{4} \right)^2 \right) + T((\frac{3}{4})^3 n)`].

    Repeating this process,
    [`T(n) \leq \frac{n}{b} \left( 1 + \frac{3}{4} + \left( \frac{3}{4} \right)^2 + \dots \right) + T(s)`], where [`s`] is some value less than 1.
    Substituting [`b`], solve for [`T(n)`]: [`T(n) \leq `][____________________]{"8*n"}




Problem 5

    $k = random(3,7,2);

    $alpha = random(0.1,0.4,0.1);

    $exp = 2;

    if ($k == 5){
      $exp = 3;
    }

    if ($k == 7){
       $exp = 4;
    }

    ## Quickselect - Algorithm for computing percentiles ##

    In this problem, we will analyze the expected running time of a variant to the  randomized percentile finding algorithm discussed in lecture. The algorithm is used to select the [`k^{th}`] smallest element in an array containing [`n`] elements. In other words, the element that would appear in location [`k`] if the array is sorted from smallest to largest.

    In this version of percentile finding algorithm we change the the way we select the pivot element. Suppose instead of a single pivot we pick [`[$k]`] numbers, sort them, and select the pivot to be the median of the numbers.

    We say that a pivot is "lucky" if it falls in the range of [`[$alpha]*n`] and  [`(1-[$alpha])*n`]. When the pivot is lucky we are guaranteed that the size of the array at the following iteration will be at most [`(1-[$alpha])*n`]
    .
    ---

    Pick one of the [`[$k]`] numbers that we have sampled. What is the probability that this number is not in the range of [`[$alpha]*n`] and [`(1-[$alpha])*n`] [_________]{Compute("2*$alpha")}
    .
    .
    [`\mbox{Hint :} \Pr( \mbox{A number is not in range}) = \Pr(\mbox{The number is below the required range}) + \Pr(\mbox{The number is beyond the required range}) `]
    .
    .
    What is the probability that the median of the [`[$k]`] numbers that we sample is not in the range of [`[$alpha]*n`] and [`(1-[$alpha])*n`] [_________]{Compute("2*($alpha)^($exp)")}
    .
    .
    [`\mbox{Hint :} \Pr( \mbox{Median of our sample is not in range}) = \Pr(\mbox{Median and the numbers smaller than the median are below the required range}) + \Pr(\mbox{Median and the numbers greater than the median are beyond the range}) `]
    .
    .
    What is the probability that the median of the [`[$k]`] numbers that we sample is  in the range of [`[$alpha]*n`] and [`(1-[$alpha])*n`] [_________]{Compute("1-2*($alpha)^($exp)")}
    .
    .
    Now, let us use the results computed above to build a recurrence relation to estimate the expected running time of the algorithm.
    .
    .
    Let [`T(n)`] denote the expected running time of the algorithm with input size n.
    .
    .
    When we get lucky, our problem reduces to a size of [`(1-[$alpha])*n`].
    When we are unlucky, our problem size remains [`n`].
    .
    .
    [`T(n) \leq n + a T((1-[$alpha])*n) + b T(n)`]
    .
    .
    In the recurrence relation, what is the value of [`a`] [_______]{Compute("1-2*($alpha)^($exp)")}
    In the recurrence relation, what is the value of [`b`] [_______]{Compute("2*($alpha)^($exp)")}
    .
    .
    Solving the recurrence relation we get [`T(n)  \leq C*n`]
    What is the value of [`C`] [_____]{Compute("1/((1-2*($alpha)^($exp))*$alpha)")}
    .
    .
    What is the expected number of random splits before we see a lucky split [_______]{Compute("1/(1-2*($alpha)^($exp))")}




Problem 6

    ## Hashing ##

    In many situations, such as a dictionary application, we need to store a vast
    collection of items in such a way that we can look up any item instantaneously.
    The way to do this is by _hashing_.

    #### The hashing framework ####

    Suppose you have a large collection of items [`x_1, \ldots, x_n`] that you want
    to store (for instance, all English words), where these items are
    drawn from some set [`\mathcal{U}`] (for instance, the set of all conceivable words).
    The requirements are:

    1. The total storage space used should be [`O(n)`].
    2. Given a query [`q \in \mathcal{U}`], it should be possible to _very rapidly_
    determine whether [`q`] is one of the stored items [`x_i`].

    #### A simple solution using randomization ####

    1. Pick a completely random function [`h: \mathcal{U} \rightarrow \{1,2,\ldots, n\}`]. This is the _hash function_.

    2. Create a table [`T`] of size [`n`], each of whose entries is a pointer to a
    linked list, initialized to null.

    3. Store each [`x_i`] in the linked list at [`T[h(x_i)]`]. We say [`x_i`] _hashes to_ location [`h(x_i)`].

    4. Given a query [`q`], look through the linked list at [`T[h(q)]`] to see if
    it's there.

    Here's a picture of the data structure.

     \{image("hash_table.png", width=>500, height=>400) \}

    The storage used is [`O(`][____]{n}) (answer in terms of [`n`]). What about the query time?




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


Problem 8

    $k = random(3,5);
    $p = "(($k-1)/$k)";

    [``\newcommand{\E}{\mathbb{E}}``]
    [``\newcommand{\R}{\mathbb{R}}``]
    [``\newcommand{\bP}{\mathbb{P}}``]
    [``\newcommand{\var}{\mbox{var}}``]
    [``\newcommand{\pr}{\mbox{Pr}}``]
    [``\def\X{{\cal X}}``]
    [``\def\cost{{\mbox{cost}}}``]
    [``\def\U{{\cal U}}``]
    [``\renewcommand{\log}{\mbox{log}_2}``]

    #### Average query time ####
    Assume [`n`] items are hashed to [`n`] locations.
    Suppose query [`q`] is picked at random, so that it is equally likely to hash to
    any of the locations [`1,2,\ldots, n`]. What is the expected query time?

    [$BCENTER]*
    [`` \begin{eqnarray*}
    \mbox{Expected query time}
    & =&
    \sum_{i=1}^n \pr(\mbox{$q$ hashes to location $i$}) \cdot \mbox{(length of list at $T[i]$)} \\
    & =&
    \frac{1}{n} \sum_i  \mbox{(length of list at $T[i]$)} \\
    & = &
    \frac{1}{n} \cdot n \ = \ 1
    \end{eqnarray*}``]
    [$ECENTER]*

    So the average query time is constant!

    #### Worst case query time, and a balls-in-bins problem ####

    What is the worst case query time; that is, what is the length of the longest linked list
    in [`T`]? Equivalently, when you throw [`n`] balls in [`n`] bins, what is the size of the
    largest bin? We'll see that with very high probability, no bin gets [``\geq \log n``]
    balls.

    For any bin [`i`], let [`E_i`] be the event that it gets [``\geq \log n``] balls.

    [$BCENTER]*
    [``` \pr(E_i) \  \leq \ {n \choose \log n} \left( \frac{1}{n} \right)^{\log n} .```]
    [$ECENTER]*

    (Do you see why? Because we want to select [``\log n``] balls to go into bin [`i`], but do not care where the other balls go.)

    To upper bound this probability we use the inequality (see cheat sheet) that

    [$BCENTER]*
    [```
    {n \choose k} \leq \left( \frac{ne}{k} \right)^k
    ```]
    [$ECENTER]*

    Applying this inequality we get:

    [$BCENTER]*
    [```
    {n \choose \log n} \left( \frac{1}{n} \right)^{\log n} \leq
    \left( \frac{ne}{n \log n}  \right)^{\log n} =
    \left( \frac{e}{\log n}  \right)^{\log n} =
    \frac{n^{\log e}}{(\log n)^{\log n}} \leq \frac{1}{n^2}
    ```]
    [$ECENTER]*

    Where the last inequality can be shown by taking the log of both sides:

    [$BCENTER]*
    [``
    \log{\frac{n^{\log e}}{(\log n) ^{\log n}} = \log \left(n^{\log e} \right) - \log \left[(\log n)^{\log n}\right] =
    \log e~\log n - \log n ~\log\log n = \log n~ (\log e - \log\log n) \le -2\log n},
    ``]
    [$ECENTER]*

    or equivalently
    >>[```\log \log n \ge 2+\log e```]<<
    which holds when [`n>2000`].

    Having shown that [`\pr(E_i) \leq 1/n^2`], it follows that

    [$BCENTER]*
    [`` \pr(\mbox{some bin gets $\geq \log n$ balls})
    \ = \
    \pr(E_1 \cup E_2 \cup \cdots \cup E_n)
    \ \leq \
    \pr(E_1) + \cdots + \pr(E_n)
    \ \leq \
    \frac{1}{n}.
    ``]
    [$ECENTER]*

    For instance, if you throw a million balls into a million bins, then the chance that
    there is a bin with [``\geq``][______]{20} (round to integer) balls is at most 1 in a million.

    Getting back to hashing, this means that for [`n`] elements, the worst case query time (with probability as high as [``1-1/n``]) is [`O`]([__________]{log(n)}). (answer in terms of [`n`], you can use "log" in the answer, but not "log2" although they are equivalent in big-O notation)

    ---

    Suppose we already hashed [`n`] elements, and bucket 1 gets half of them.

    What is the expected search time for a new element? O([___________]{1})

    What is the worst search time? Notice that this scenario is a rare one. O([___________]{"n/2"}) (answer in terms of [`n`])




Problem 9

    [``\newcommand{\E}{\mathbb{E}}``]
    [``\newcommand{\R}{\mathbb{R}}``]
    [``\newcommand{\bP}{\mathbb{P}}``]
    [``\newcommand{\var}{\mbox{var}}``]
    [``\newcommand{\pr}{\mbox{Pr}}``]
    [``\def\X{{\cal X}}``]
    [``\def\cost{{\mbox{cost}}}``]
    [``\def\U{{\cal U}}``]
    [``\renewcommand{\log}{\mbox{log}_2}``]

    #### The power of two choices ####

    Here's a variant on the balls and bins setup. As usual, you have before you a
    row of [`n`] bins, along with a collection of [`n`] identical balls. But now,
    when throwing each ball, _you pick two bins at random and you put the
    ball in whichever of them is less full_.

    It turns out, using an analysis that is too complicated to get into here, that
    under this small change, the maximum bin size will be just [`O(\log \log n)`]
    instead of [`O(\log n)`].

    This inspires an alternative hashing scheme:

    1\. Pick _two_ completely random functions [`h_1, h_2: \U \rightarrow \{1,2,\ldots, n\}`].


    2\. Create a table [`T`] of size [`n`], each of whose entries is a pointer to a
    linked list, initialized to null.


    3\. For each [`x_i`], store it in either the linked list at [`T[h_1(x_i)]`] or [`T[h_2(x_i)]`],
    whichever is shorter.


    4\. Given a query [`q`], look through _both_ the linked list at [`T[h_1(q)]`] and
    at [`T[h_2(q)]`] to see if it's there.


    The storage requirement is still [`O(n)`], the average query time is still [`O(1)`], but now
    the worst case query time drops to [`O(\log \log n)`].

    ---

    What is the worst case query time for [`n = 2^{64}`] ? O([_________]{6})
