##Week7a

            Assigned problem file name:
          +--------+------------+------------------------------------------------+
          | set_id | problem_id | source_file                                    |
          +--------+------------+------------------------------------------------+
          | Week7a |          1 | Reorganized/HypothesisTesting/error.pg         |
          | Week7a |          2 | Reorganized/HypothesisTesting/psychic.pg       |
          | Week7a |          3 | Reorganized/HypothesisTesting/paired_t_test.pg |
          | Week7a |          4 | Reorganized/HypothesisTesting/pooled.pg        |
          | Week7a |          5 | Reorganized/HypothesisTesting/gust63.pg        |
          | Week7a |          6 | local/Reorganized/HypothesisTesting/gust75.pg  |
          | Week7a |          7 | local/Reorganized/HypothesisTesting/Chi2.2.pg  |
          | Week7a |          8 | local/Reorganized/HypothesisTesting/Chi2.3.pg  |
          | Week7a |          9 | local/setTestPreparationST/prob4.pg            |
          +--------+------------+------------------------------------------------+


### Sorted with number of attempts

problem 9 (Answer include variables): 2497

		 part  1 :  400
		 part  2 :  419
		 part  3 :  370
		 part  4 :  404
		 part  5 :  904


[problem 6](https://github.com/cse103/Attempt_Analysis/blob/master/clustering_code/clusters/Week7a/md_files/Week7a_6_clusters.md): 1214

		 part  1 :  158
		 part  2 :  639
		 part  3 :  377
		 part  4 :  11
		 part  5 :  9
		 part  6 :  7
		 part  7 :  8
		 part  8 :  5


[problem 2](https://github.com/cse103/Attempt_Analysis/blob/master/clustering_code/clusters/Week7a/md_files/Week7a_2_clusters.md): 945

		 part  1 :  511
		 part  2 :  324
		 part  3 :  48
		 part  4 :  62


[problem 7](https://github.com/cse103/Attempt_Analysis/blob/master/clustering_code/clusters/Week7a/md_files/Week7a_7_clusters.md): 559

		 part  1 :  159
		 part  2 :  181
		 part  3 :  82
		 part  4 :  66
		 part  5 :  71


[problem 8](https://github.com/cse103/Attempt_Analysis/blob/master/clustering_code/clusters/Week7a/md_files/Week7a_8_clusters.md): 204

		 part  1 :  84
		 part  2 :  120


problem 1 (Multiple Choice): 49

		 part  1 :  49


### Problem Content

Problem 1 (Multiple choice problem)

    $mc1 = new_multiple_choice();
    $mc1->qa('Increasing \(\alpha\) will: ',
    	'Increase Type I error, decrease type II error'
    );
    $mc1->extra(
    	'Increase Type II error, decrease type I error',
    	'Decrease both.',
    	'Increase both.'
    );

    BEGIN_TEXT

    $PAR
    Choosing \(\alpha\) is a compromise between two types of errors: $BR
    $BBOLD Type I error $EBOLD: Rejecting the null hypothesis when it is correct $BR
    $BBOLD Type II error $EBOLD: Failing to reject the null hypothesis when it is
    incorrect.

    $PAR
    $BCENTER
    \{ begintable(3) \}
    \{ row( " ", "Null hypothesis true (Seatbelts don't help)", "Null hypothesis false (Seatbelts help)") \}
    \{ row( "Fail to reject", "correct", "Type II" ) \}
    \{ row( "Reject null", "Type I", "correct" ) \}
    \{ endtable() \}
    $ECENTER

    $PAR
    \{ $mc1->print_q() \}
    $BR
    \{ $mc1->print_a() \}

    $PAR
    Alpha value is an upper bound on the probability of making a type I error (Incorrect rejection). $PAR

    END_TEXT
    ANS(radio_cmp($mc1->correct_ans));




Problem 2:

      $a = Compute("0.05/sqrt(0.16/200)");
      $q = Compute("Q($a)");

      A noted psychic was tested for extrasensory perception. The psychic was presented
      with 200 cards face down and asked to determine if the card were one of five symbols.
      The psychic was correct in 50 cases. Let p represent the probability that the psychic
      correctly identifies the symbol on the card in a random trial. Assume the 200 trials
      can be treated as a simple random sample.

      Suppose you wished to see if there were evidence that the psychic is
      doing better than just guessing. To do this, you test the hypotheses [`H_0 : p = .20`]
      versus [`H_{alternative} : p > .20`].

      What is the z-score? [__________________________________________]{$a}

      What is the p-value for the test statistic? (You can use Q function in the answer) [_________]{$q}

      Can you reject at the .05 significance level? (answer "yes" or "no") [_______]{"yes"}

      Can you reject at the .01 significance level? (answer "yes" or "no") [_______]{"no"}


Problem 3: (Multiple choice problem)

    $mc1 = new_multiple_choice();
    $mc1->qa('We have two alternatives layouts of the web pages A/B and want to decide which keeps the user on our web site for a longer time. To
    avoid confusing the user with constantly changing design, we use the same layout to the web pages presented to each user whenever they visit the site. which hypothesis test should we use?',
    	'two sample t-test, pooled variance'
    );
    $mc1->makeLast(
    	'1-sided z-value',
    	'One sample t-test',
            'two sample t-test, pooled variance',
    	'paired t-test'
    );

    $mc2 = new_multiple_choice();
    $mc2->qa('If we show both layouts to the same user upon his different visits, which hypothesis test should we use?', 'paired t-test'
    );
    $mc2->makeLast(
    	'1-sided z-value',
    	'One sample t-test',
    	'two sample t-test, pooled variance',
            'paired t-test'
    );

    $mc3 = new_multiple_choice();
    $mc3->qa("Which testing will better help us identify the superior layout? Consider the following scenario. Suppose layout B is generally more attractive than layout A. User John and user Peter both visited the website twice, and are presented with both layouts. With layout B, John's visit time increases from 60 seconds to 61 seconds, and Peter's visit time increases from 90 seconds to 91 seconds. The variance of the $BBOLD sample difference of average time $EBOLD is higher than the variance of the $BBOLD sample average of difference $EBOLD. Different users have varied behavior, but the trend is more clear if we focus on the change of each individual. Pairing data can factor out variations from one user to the next. In other words, compared to two sample t-test, paired t-test",  'lowers probability of Type II error, for the same probability of Type I error'
    );
    $mc3->makeLast(
            'lowers probability of Type II error, for the same probability of Type I error',
    	'lowers probability of Type I error, for the same probability of Type II error',
            'does not help. Both types of error still have the same probability'
    );

    BEGIN_PGML
    ## The Student t-Test ##

    The t-test, invented in 1908 by William Sealy Gosset (whose pen-name was "Student") is one of the most commonly used statistical tests.

    The basic premise of the test is that we have two populations and we wish to know whether there is a significant difference between their means. For example, we would like to know whether kids that drink at least one glass of milk each day are significantly taller than their peers. The null hypothesis is that the means of both populations are the same.

    The two populations are assumed to be normally distributed. Or, invoking the central limit theorm, they are assumed to be the sum or mean of a large number of IID random variables.

    There are many variants of the t-test. We list some of the most popular.
    1. *One sample t-test:* We assume that we know the mean of one population and that we have a sample from the other population. Note that this is still different from the Z-test, because we do not a-priori know the variance of the sampled population.
    2. *Two sample t-test, Pooled std:* We have samples from both populations, and we assume that their variances are equal. Therefor we can pool both samples to estimate the variance.
    3. *Two sample t-test, un-Pooled std:* As in 2. but we don't assume that variances of the two populations are equal.
    4. *Paired t-test:* Suppose we want to show that coffee effects the speed with which people can perform calculations. We can test each person before and after drinking coffee and compare the two performances. In this situation we can "pair" the measurements, which here simply means take their difference. The test we then perform is a one-sample t-test in which the null hypothesis is that the mean is zero. We could, of course, use the same samples to perform a two-sample t-test, however, this would be a *weaker* test, i.e. it will have a higher probability of making a type II error (fail to reject the null hypothesis) for the same probability of making a type I error.

    ----
    END_PGML

    BEGIN_TEXT
    $PAR$PAR
    $BBOLD A/B testing of web pages $EBOLD $PAR

    Suppose we want people to stay on our web page as long as possible,
    measure time between first and last click-on-site. $BR

    \{ $mc1->print_q() \}
    \{ $mc1->print_a() \}

    $PAR
    \{ $mc2->print_q() \}
    \{ $mc2->print_a() \}

    $PAR
    \{ $mc3->print_q() \}
    \{ $mc3->print_a() \}

    END_TEXT
    ANS(radio_cmp($mc1->correct_ans));
    ANS(radio_cmp($mc2->correct_ans));
    ANS(radio_cmp($mc3->correct_ans));




Problem 4: (Multiple choice problem)

    $mc1 = new_multiple_choice();
    $mc1->qa('Cholesterol levels are measured for 28 heart attack patients (2 days after their attacks) and 30 other hospital patients who did not have a heart attack. We test if the means are no difference for the two groups. Sample standard deviation for the heart attack group is 9.0, and that for the control group is 4.1. Which test should we use?',
    	'two sample t-test, un-pooled variance'
    );
    $mc1->makeLast(
    	 'two sample t-test, un-pooled variance',
            'two sample t-test, pooled variance',
    	'paired t-test'
    );

    $mc2 = new_multiple_choice();
    $mc2->qa('Hours spent studying per week are reported by students in a class survey. Students who say they usually sit in the front are compared to students who say they usually sit in the back. The sample std for the front group is 1.09, and that for the back group is 0.89. Which test should we use?', 'two sample t-test, pooled variance'
    );
    $mc2->makeLast(
    	'two sample t-test, un-pooled variance',
            'two sample t-test, pooled variance',
    	'paired t-test'
    );

    $mc3 = new_multiple_choice();
    $mc3->qa("Which test will yield more significant results (lower p-value for the same observation)? ",  'two sample t-test, pooled variance'
    );
    $mc3->makeLast(
            'two sample t-test, un-pooled variance',
    	'two sample t-test, pooled variance'
    );


    BEGIN_PGML
    ## Two-sample t-Tests##
    ---
    END_PGML

    BEGIN_TEXT
    $PAR$PAR

    \{ $mc1->print_q() \}
    \{ $mc1->print_a() \}

    $PAR
    \{ $mc2->print_q() \}
    \{ $mc2->print_a() \}

    $PAR
    \{ $mc3->print_q() \}
    \{ $mc3->print_a() \}

    END_TEXT

    ANS(radio_cmp($mc1->correct_ans));
    ANS(radio_cmp($mc2->correct_ans));
    ANS(radio_cmp($mc3->correct_ans));




Problem 5:

    ## Paired t-Tests##
    ---

    In this problem, we consider a * paired t-test* (defined in 8.6.2 in "Notes on hypothesis testing and central limit theorem" on moodle). The setting is that two normal random variables [`X`] and [`Y`] are sampled. We pair each of the samples from the first variable with each of the samples from the second variable, and we check the "null hypothesis" that the two elements in each pair have the same mean, i.e. [`\mu_X = \mu_Y`], against the alternative hypothesis that [`\mu_X \neq \mu_Y`]. Now create a new random variable [`D`] by taking the difference between the two elements in each pair. The "null hypothesis" can therefore be defined as [`\mu_D = 0`], and the alternative hypothesis [`\mu_D \neq 0`]. Note that if the two variables are normally distributed, their difference is also normally distributed, so [`D`] is a Normal variable. We then calculate the confidence interval for the mean of [`D`] .

    1.  Suppose that for a given data set of [`D`], a 95% confidence interval is calculated to be (-3.45,1.78).  If you were to perform a hypothesis test at the 5% significance level to test the null hypothesis, would you reject it?  Answer "yes", "no", or "can't tell". [____________________]{"no"}

    2.  Suppose that for a given data set of [`D`], a 99% confidence interval is calculated to be (-10.77,-2.35).  If you were to perform a hypothesis test at the 1% significance level to test the null hypothesis, would you reject it?  Answer "yes", "no", or "can't tell".  [____________________]{"yes"}

    3.  Suppose that for a given data set of [`D`], a 97% confidence interval is calculated to be (25.6,41.1).  If you were to perform a hypothesis test at the 3% significance level to test the null hypothesis, would you reject it?  Answer "yes", "no", or "can't tell".  [____________________]{"yes"}






Problem 6:

      Suppose there are 3 species of fish in the world, we are interested
      in two fish populations: fish of the pacific ocean and fish of the atlantic ocean.
      Each one of these populations is characterized by a distribution over the species of fish:
      The pacific distribution is uniform over the 3  species:
      [`P_p=(1/3,1/3,1/3)`] while in the atlantic population the first species is twice more common thand the other two: [`P_a=(1/2,1/4,1/4)`]

      Suppose we are given a  batch of 65 fish whose source is unknown.
      The number of fish of each species is [`(30,20,15)`].

      We would like to know whether the the batch of fish is from the atlantic or the pacific (or both).

      One way of formalizing this problem is to consider two Null hypotheses:

      * HA = the batch is from the atlantic ocean. More technically, the batch was sampled from the distribution [`P_a`]
      * HP = the batch is from the pacific ocean. More technically, the batch was sampled from the distribution [`P_b`].

      The test that we will use is the [`\chi^2`] test. (https://en.wikipedia.org/wiki/Pearson%27s_chi-squared_test).

      The [`\chi^2`] test statistic is

      [``\chi^2 =  N \sum_{i=1}^n p_i \left(\frac{O_i/N - p_i}{p_i}\right)^2``]

      Where:
      * [`n`] is the number of species (3 in our case).
      * [`p_i`] is the probability of the [`i`]'th species according to the Null distribution.
      * [`O_i`] is the number of observations of species [`i`]
      * [`N`] is the total number of observation. [`N=\sum_{i=1}^n O_i`]. Which is [_____]{65} in our case.

      Write expressions for the [`\chi^2`] statistic for the two null Hypotheses:

      * For hypothesis HA ( batch is from atlantic ocean), [`\chi^2=`] [___________________________________________________________________]{Compute("65*(0.500*(((30.0/65.0)-0.500)/0.500)**2+0.250*(((20.0/65.0)-0.250)/0.250)**2+0.250*(((15.0/65.0)-0.250)/0.250)**2)")}
      * For hypothesis HP ( batch is from pacific ocean), [`\chi^2=`] [___________________________________________________________________]{Compute("65*((1./3)*(((30.0/65.0)-(1./3))/(1./3))**2+(1./3)*(((20.0/65.0)-(1./3))/(1./3))**2+(1./3)*(((15.0/65.0)-(1./3))/(1./3))**2)")}

      This question continues with the next problem.




Problem 7:

      To compute the p-value of rejecting the Null hypothesis we need to know the **number of degrees of freedom** of the distribution. As the size of the space is 3 there are three variables defining the distribution: [`p_1,p_2,p_3`] as these probabilities sum to one there [`v=2`] degrees of freedom. We then use the CDF for the [`\chi^2`] distribution with 2 degrees of freedom to calculate the p-values.

      Answer the following questions yes (enter +1) or no (enter -1)

      * A small value of the [`\chi^2`] statistic justifies **rejecting** the Null Hypothesis [______]{-1}
      * A small value of the [`\chi^2`] statistic justifies **accepting** the Null Hypothesis [______]{-1}
      * A large value of the [`\chi^2`] statistic justifies **rejecting** the Null Hypothesis [______]{+1}
      * It is possible to reject both of the Null hypotheses:[__________]{+1}
      * It is possible to not reject either of the Null hypotheses: [___________]{+1}




Problem 8:

      Using the data given in the problem regarding the source of a batch of fish we get the following:
      * The p-value associated with rejecting the HA hypothesis is 0.5616
      * The p value associated with rejecting the HP hypothesis is  0.0677

      Which hypothesis can we reject if we set our confidence level to be [`\alpha=10%`] ?
      (use 1 for reject, 0 for not reject)

      * We can reject the hypothesis that the batch is from the pacific ocean [____]{1}
      * We can reject the hypothesis that the batch is from the atlantic ocean [_____]{0}




Problem 9:

      ## Counting the number of fish in a lake.
      A lake contains an unknown number of fish. 1000 of them are caught, marked with red spots, and then
      returned to the water. Later, a random subset of 100 fish are caught from the lake, and it is found
      that [`x`] of them have red spots.
      1. In terms of [`x`], what estimate would you give for the number of fish in the lake?  [_______]{"1000*100/x"}
      2. Let n be the true number of fish in the lake. Then distribution of the random variable X (the number of fish in your second sample of size 100), follows a Binomial distribution with what parameters?  [`\mathbb{E}(X) = `][______]{"100*1000/n"} and [`\mbox{var}(X) = `][______]{"100*(1000/n)*(1-1000/n)"}  Give your answers in terms of [`n`].
      3. For standard normal random variable [`S`], what is [`P(-1.96 < S < 1.96)`]?  [_________]{"1-2*0.025"}
      4. If you had to give a 95% confidence interval of [`\mathbb{E}(X)`] in terms of [`n`], what would it be?  [`X\pm`][_______]{"1.96*sqrt(100*(1000/n)*(1-1000/n))"}
      5. Use the approximation technique you learned from class, the confidence interval of [`n`] is from [____________]{"1000*100/(x + sqrt(100))"} to [____________]{"1000*100/(x - sqrt(100))"}
