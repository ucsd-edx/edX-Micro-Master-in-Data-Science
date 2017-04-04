#Problem 8

    $n = random(20,30,1);
    $nc = random(4,6,1);
    $p = 1/$nc;
    $mean = $n*$p;
    $low = int($mean + 4);
    $high = int($mean + 8);
    $corr = random($low, $high, 1);

    $std = sqrt( $n / $nc * (1-1/ $nc));
    $ans = Compute("Q(($corr-$mean)/$std)");
    $ans1 = BinomDistTail($n,$p,$corr);

    ### Some Definitions ###
    The *standard* normal distribution [`\mathcal{N}(0,1)`] is a special normal distribution with mean [`\mu=0`] and standard deviation [`\sigma=1`].

    - The CDF of the standard normal distribution is denoted [`\Phi`]:
    >>[``\Phi(z) = P(Z\leq z)``]. <<

    - The complement of the CDF is called the *Q-function*:
    >>[``Q(z) = P(Z>z) = 1-\Phi(z)``].<<

    While [`\Phi(z)`] measures the probability mass of a "head" of the standard normal, [`Q(z)`] measures the "tail". The values of Q are often tabulated for commonly used \(z\). One such table is _http://goo.gl/Szofn1_. One can also use _http://wolframalpha.com_ to find numeric values for Q function.


    - An alternative representation of the head probability is the *error function*, denoted [`erf`]. It is related to [`\Phi`] by:
    >>[``\Phi(x) = \frac{1}{2} + \frac{1}{2}erf(\frac{x}{\sqrt{2}})``]<<

    *For this set of assignment, you can use "Phi", "Q" or "erf" as functions in your answer.*

    ---

    ### Recap for Binomial Distribution ###

    Suppose a monkey is given a test that consists of [$n] multiple-choice questions each with [$nc] choices. By random guessing, what is the *exact* probability that the monkey gets at least [$corr] correct ?
    [_____________________________________________________________]{$ans1}

    ---
    ### Approximate Binomial Using Normal Distribution ###
    We know that the number of questions the monkey guesses correctly follows a binomial distribution, and we have computed the *exact* probability of a tail of this distribution, by summing up all cases in the tail.

    Now, we assume the number of questions is large enough so that by *central limit theorem* we can use a normal distribution to approximate the binomial distribution. This makes computing the probability of a certain part of the distribution much easier.

    ---
    Again, suppose the monkey is taking a multiple-choice test that consists of [$n] questions each with [$nc] possible answers, let us estimate the probability that it gets at least [$corr] questions correct, this time using an *approximated normal distribution*.

    Suppose [`X`] is the number of correct answers.

    - What is the mean of [`X`] ? [_______]{Compute("$n*$p")}
    - What is the standard deviation of [`X`] ? [_______]{Compute("sqrt($n*$p*(1-$p))")}
    - What is the z-score of [`X=[$corr]`]? [___________]{Compute("($corr-$mean)/$std")}
    - What is the estimated probability that [`X \ge [$corr]`] ? [_____________]{$ans}





## Part 1

### (22) Mistake Group Digits of size 22




### (5) Mistake Group Wrong_Sign of size 5




### (3) Mistake Group ['R.0'] of size 3
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|Q(0.3)	|Phi(.3)	|[('R.0', 0.3, u'0.3', u'.3)')]	|
|1	|Q(0.3)	|Phi(0.3)	|[('R.0', 0.3, u'0.3', u'0.3')]	|




### (42) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:dmn009

	first_attempt
					2015-11-05 09:12:08
	part1_incorrect_attempt
					('0:00:00', u'23/5')
					('0:02:08', u'23/5')
					('0:02:45', u'23/5')
					('0:04:11', u'23/5')
	part1_correct_attempt
					['0:06:14', u'.382089']

1 Student ID:hmshah

	first_attempt
					2015-11-05 10:23:46
	part1_incorrect_attempt
					('0:00:00', u'.5*((1.7^0 / (0! * e^1.7) ) + (1^0 / (0! * e^1) ))')
					('0:00:09', u'1-0.275281')
	part1_correct_attempt
					['0:00:23', u'Q(.3)']

2 Student ID:abjara

	first_attempt
					2015-11-04 03:03:29
	part1_incorrect_attempt
					('0:00:00', u'.7')
	part1_correct_attempt
					['0:02:33', u'Q(.3)']

3 Student ID:jfalcone

	first_attempt
					2015-11-05 05:37:08
	part1_incorrect_attempt
					('0:00:00', u'26/4')
	part1_correct_attempt
					['0:00:21', u'Q(.3)']

4 Student ID:ctroncos

	first_attempt
					2015-11-05 17:10:34
	part1_incorrect_attempt
					('0:00:00', u'24/6')
					('0:00:51', u'24/6')
					('0:00:59', u'24/6')
					('0:01:06', u'24/6')
					('0:01:22', u'24/6')
					('0:03:36', u'24/6')
					('0:05:37', u'24/6')
	part1_correct_attempt
					['0:06:20', u'Q(0.3)']

5 Student ID:yeh013

	first_attempt
					2015-11-05 03:49:56
	part1_incorrect_attempt
					('0:00:00', u'1-Phi(0.7)')
	part1_correct_attempt
					['0:00:13', u'1-Phi(0.3)']

6 Student ID:hkhodada

	first_attempt
					2015-10-31 17:42:02
	part1_incorrect_attempt
					('0:00:00', u'0.7')
	part1_correct_attempt
					['0:03:26', u'1-Phi(0.3)']

7 Student ID:mroknich

	first_attempt
					2015-11-01 21:59:53
	part1_incorrect_attempt
					('0:00:00', u'26*(1/6)')
					('0:02:27', u'26*(1/6)')
					('0:03:23', u'26*(1/6)')
					('0:04:21', u'26*(1/6)')
	part1_correct_attempt
					['0:15:53', u'1-(1/2+1/2erf(.3/sqrt(2)))']

8 Student ID:d6he

	first_attempt
					2015-11-05 05:50:11
	part1_incorrect_attempt
					('0:00:00', u'0.7')
	part1_correct_attempt
					['0:18:55', u'1-Phi(0.3)']

9 Student ID:masaro

	first_attempt
					2015-11-03 17:10:53
	part1_incorrect_attempt
					('0:00:00', u'0.6179')
	part1_correct_attempt
					['0:00:05', u'1-0.6179']

10 Student ID:krau

	first_attempt
					2015-11-05 03:11:21
	part1_incorrect_attempt
					('0:00:00', u'.7')
	part1_correct_attempt
					['0:00:18', u'Q(.3)']

11 Student ID:rsmurlo

	first_attempt
					2015-11-03 18:32:59
	part1_incorrect_attempt
					('0:00:00', u'3.820886e^-1')
	part1_correct_attempt
					['0:00:55', u'Q(.3)']

12 Student ID:pcdo

	first_attempt
					2015-11-02 18:55:14
	part1_incorrect_attempt
					('0:00:00', u'29*.25')
					('0:00:33', u'29*.25')
					('0:01:20', u'29*.25')
					('0:01:44', u'29*.25')
					('0:01:52', u'29*.25')
					('0:02:00', u'29*.25')
	part1_correct_attempt
					['0:03:24', u'Q(0.3)']

13 Student ID:pvl001

	first_attempt
					2015-11-03 20:47:23
	part1_incorrect_attempt
					('0:00:00', u'1 - Phi(3)')
	part1_correct_attempt
					['0:00:13', u'1 - Phi(0.3)']

14 Student ID:t2li

	first_attempt
					2015-11-06 02:56:38
	part1_incorrect_attempt
					('0:00:00', u'0.7')
	part1_correct_attempt
					['0:01:00', u'1-(0.5+0.5*erf(0.3/sqrt(2)))']

15 Student ID:beyounge

	first_attempt
					2015-10-30 06:03:19
	part1_incorrect_attempt
					('0:00:00', u'3.820886 ^ (-1)')
	part1_correct_attempt
					['0:01:51', u'1 - [(1/2) + ((1/2) * erf(0.3/sqrt(2)))]']

16 Student ID:amquinte

	first_attempt
					2015-11-05 06:34:01
	part1_incorrect_attempt
					('0:00:00', u'.618')
	part1_correct_attempt
					['0:00:42', u'.382']

17 Student ID:sayao

	first_attempt
					2015-11-05 03:38:46
	part1_incorrect_attempt
					('0:00:00', u'(22+23)/2/22')
	part1_correct_attempt
					['0:00:53', u'1-(1/2+1/2erf(.3/sqrt(2)))']

18 Student ID:cfgutier

	first_attempt
					2015-11-06 20:03:13
	part1_incorrect_attempt
					('0:00:00', u'30/4')
					('0:00:24', u'21/12')
	part1_correct_attempt
					['0:01:46', u'1-(1/2 + 1/2erf(.3/sqrt(2)))']

19 Student ID:jnatale

	first_attempt
					2015-11-05 02:19:05
	part1_incorrect_attempt
					('0:00:00', u'3.82*e^-1')
	part1_correct_attempt
					['0:00:31', u'.382']

20 Student ID:rlhagen

	first_attempt
					2015-10-31 19:13:39
	part1_incorrect_attempt
					('0:00:00', u'1-0.3')
	part1_correct_attempt
					['0:03:13', u'1-Phi(0.3)']

21 Student ID:agarango

	first_attempt
					2015-11-06 20:11:14
	part1_incorrect_attempt
					('0:00:00', u'(.5)+(.5)*(0.3/sqrt(2))')
	part1_correct_attempt
					['0:03:05', u'0.382']

22 Student ID:btn023

	first_attempt
					2015-11-06 11:06:26
	part1_incorrect_attempt
					('0:00:00', u'23*(1/5)')
					('0:01:37', u'23*(1/5)')
					('0:06:41', u'23*(1/5)')
					('0:06:52', u'23*(1/5)')
					('0:08:04', u'23*(1/5)')
					('0:09:06', u'23*(1/5)')
	part1_correct_attempt
					['0:14:43', u'1-(1/2+1/2erf(.3/sqrt(2)))']

23 Student ID:lalacson

	first_attempt
					2015-11-05 08:49:18
	part1_incorrect_attempt
					('0:00:00', u'24/5')
					('0:00:00', u'24/5')
					('0:00:57', u'24/5')
					('0:00:00', u'24/5')
	part1_correct_attempt
					['0:08:24', u'Q(.3)']

24 Student ID:dwzhang

	first_attempt
					2015-11-06 21:31:17
	part1_incorrect_attempt
					('0:00:00', u'20 * 6')
					('0:00:00', u'20 / 6')
	part1_correct_attempt
					['0:01:52', u'Q(0.3)']

25 Student ID:jhw015

	first_attempt
					2015-11-06 19:10:40
	part1_incorrect_attempt
					('0:00:00', u'(1/6)29')
	part1_correct_attempt
					['0:03:32', u'1-(0.5 + 0.5erf(0.3/sqrt(2)))']

26 Student ID:dsmonaha

	first_attempt
					2015-11-04 15:35:39
	part1_incorrect_attempt
					('0:00:00', u'.3')
					('0:01:33', u'e^0')
					('0:12:08', u'1-.3')
					('0:22:17', u'(1/2^(1/2))e^-(.3^2/2)')
	part1_correct_attempt
					['2 days, 3:47:47', u'Q(.3)']

27 Student ID:tstevens

	first_attempt
					2015-11-06 11:59:43
	part1_incorrect_attempt
					('0:00:00', u'24*.5')
	part1_correct_attempt
					['0:00:18', u'Q(0.3)']

28 Student ID:hah008

	first_attempt
					2015-11-06 23:08:20
	part1_incorrect_attempt
					('0:00:00', u'1/2 + 1/2')
					('0:00:30', u'21* (1/6)')
					('0:01:28', u'21* (1/6)')
					('0:03:51', u'21* (1/6)')
	part1_correct_attempt
					['0:04:16', u'Q(0.3)']

29 Student ID:l8ngo

	first_attempt
					2015-11-04 01:11:33
	part1_incorrect_attempt
					('0:00:00', u'2.7')
	part1_correct_attempt
					['0:01:06', u'0.382089']

30 Student ID:bakang

	first_attempt
					2015-11-05 08:50:00
	part1_incorrect_attempt
					('0:00:00', u'1/0.3')
					('0:00:00', u'0/0.3')
	part1_correct_attempt
					['0:01:51', u'1-Phi(0.3)']

31 Student ID:achava

	first_attempt
					2015-11-06 08:10:08
	part1_incorrect_attempt
					('0:00:00', u'.6179')
					('0:01:15', u'1-(3.820886*10^(-1))')
	part1_correct_attempt
					['0:02:11', u'3.820886*10^(-1)']

32 Student ID:cstringh

	first_attempt
					2015-11-04 07:05:51
	part1_incorrect_attempt
					('0:00:00', u'0.3')
	part1_correct_attempt
					['0:00:52', u'1-Phi(0.3)']

33 Student ID:v4sharma

	first_attempt
					2015-11-05 22:13:29
	part1_incorrect_attempt
					('0:00:00', u'1 - ((1/2) + ((1/2) (0.328627)))')
	part1_correct_attempt
					['0:01:22', u'1 - ((1/2) + ((1/2) (0.235823)))']

34 Student ID:aordookh

	first_attempt
					2015-11-04 22:21:45
	part1_incorrect_attempt
					('0:00:00', u'0.5120')
					('0:00:15', u'0.6179')
	part1_correct_attempt
					['0:00:45', u'1-0.6179']

35 Student ID:bpandayk

	first_attempt
					2015-11-06 21:31:33
	part1_incorrect_attempt
					('0:00:00', u'22/4')
	part1_correct_attempt
					['0:00:14', u'1-(1/2+(1/2)erf(0.3/sqrt2))']

36 Student ID:tak068

	first_attempt
					2015-11-05 21:10:39
	part1_incorrect_attempt
					('0:00:00', u'30*(1/4)')
					('0:00:26', u'30*(1/4)')
					('0:01:52', u'30*(1/4)')
					('0:02:29', u'30*(1/4)')
					('0:15:45', u'Q((11-30/4)/(sqrt(30*1/4*(1-1/4))))')
					('0:16:47', u'Q((0.3)/(sqrt(30*1/4*(1-1/4))))')
	part1_correct_attempt
					['0:16:58', u'Q(0.3)']

37 Student ID:s2chaudh

	first_attempt
					2015-11-06 07:05:56
	part1_incorrect_attempt
					('0:00:00', u'28/5')
	part1_correct_attempt
					['16:17:28', u'1-(1/2+1/2erf(.3/sqrt(2)))']

38 Student ID:atorr

	first_attempt
					2015-11-05 20:10:41
	part1_incorrect_attempt
					('0:00:00', u'1-0.3')
					('0:00:38', u'0.5 + 0.5*[0.3/(2^0.5)]')
	part1_correct_attempt
					['0:01:22', u'1 - Phi(0.3)']

39 Student ID:aurodrig

	first_attempt
					2015-11-06 23:31:52
	part1_incorrect_attempt
					('0:00:00', u'3.820886')
	part1_correct_attempt
					['0:02:14', u'0.382089']

40 Student ID:kosung

	first_attempt
					2015-11-05 18:15:14
	part1_incorrect_attempt
					('0:00:00', u'3.82*e^-1')
					('0:00:25', u'3.82*e^-0.1')
					('0:02:42', u'3.82e^-01')
	part1_correct_attempt
					['0:03:53', u'0.5-0.5erf(0.3/1.414)']

41 Student ID:k3tan

	first_attempt
					2015-11-04 06:07:02
	part1_incorrect_attempt
					('0:00:00', u'3.820886e^-1')
	part1_correct_attempt
					['0:00:17', u'0.3820886']












## Part 2

### (94) Mistake Group Digits of size 94




### (49) Mistake Group Fraction of size 49




### (35) Mistake Group ['R.1'] of size 35
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|25*1/4	|1/4	|[('R.1', 4.0, u'4', u'4')]	|
|1	|24*1/4	|24*4	|[('R.1', 4.0, u'4', u'4')]	|
|2	|23*1/5	|1/5	|[('R.1', 5.0, u'5', u'5')]	|
|3	|26*1/5	|C(26, 5)	|[('R.1', 5.0, u'5', u'5')]	|
|4	|30*1/4	|(15/30)*4	|[('R.1', 4.0, u'4', u'4')]	|
|5	|22*1/4	|13*6/4	|[('R.1', 4.0, u'4', u'4')]	|
|6	|24*1/5	|24*5	|[('R.1', 5.0, u'5', u'5')]	|
|7	|28*1/5	|10/5	|[('R.1', 5.0, u'5', u'5')]	|
|8	|23*1/6	|9/6	|[('R.1', 6.0, u'6', u'6')]	|
|9	|28*1/6	|1/6	|[('R.1', 6.0, u'6', u'6')]	|
|10	|29*1/5	|11/5	|[('R.1', 5.0, u'5', u'5')]	|
|11	|29*1/5	|29*5	|[('R.1', 5.0, u'5', u'5')]	|
|12	|28*1/5	|28 * 5	|[('R.1', 5.0, u'5', u'5')]	|
|13	|28*1/6	|28*6	|[('R.1', 6.0, u'6', u'6')]	|
|14	|21*1/6	|(6+15+30+15+6+1)/21*6	|[('R.1', 6.0, u'6', u'6')]	|
|15	|21*1/6	|(6+30+90+60+30+6)/21*6	|[('R.1', 6.0, u'6', u'6')]	|
|16	|26*1/5	|(1+2+3+4+5+6+7+8+9+10+11+12+13+14+15+16+17+18+19+20+21+22+23+24+25+26)/5	|[('R.1', 5.0, u'5', u'5')]	|
|17	|24*1/5	|8/5	|[('R.1', 5.0, u'5', u'5')]	|
|18	|21*1/5	|21*(8/21)*(13/21)*5	|[('R.1', 5.0, u'5', u'5')]	|
|19	|26*1/4	|13/26*4	|[('R.1', 4.0, u'4', u'4')]	|
|20	|25*1/6	|25*6	|[('R.1', 6.0, u'6', u'6')]	|
|21	|27*1/4	|27*4	|[('R.1', 4.0, u'4', u'4')]	|
|22	|26*1/4	|26*4	|[('R.1', 4.0, u'4', u'4')]	|
|23	|25*1/6	|17 / 6	|[('R.1', 6.0, u'6', u'6')]	|




### (7) Mistake Group ['R.0.0'] of size 7
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|28*1/6	|(28 * 6) / 2	|[('R.0.0', 28.0, u'28', u'28')]	|
|1	|28*1/6	|(28-9)/2	|[('R.0.0', 28.0, u'28', u'28')]	|
|2	|28*1/6	|(28-9) / 2	|[('R.0.0', 28.0, u'28', u'28')]	|
|3	|21*1/5	|21/2 / 11	|[('R.0.0', 21.0, u'21', u'21')]	|
|4	|21*1/5	|21/5-11/5	|[('R.0.0', 21.0, u'21', u'21')]	|
|5	|21*1/5	|21*(8/21)*(13/21)	|[('R.0.0', 21.0, u'21', u'21')]	|




### (4) Mistake Group ['R.0.1', 'R.1'] of size 4
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|28*1/5	|(1/5 + 2/5 + 3/5 + 4/5 + 1)/5	|[('R.0.1', 1.0, u'1', u'1'), ('R.1', 5.0, u'5', u'5')]	|
|1	|22*1/5	|22*5*1/5	|[('R.0.1', 1.0, u'1', u'1'), ('R.1', 5.0, u'5', u'5')]	|
|2	|21*1/5	|21*(8/21)*(13/21)*1/5	|[('R.0.1', 1.0, u'1', u'1'), ('R.1', 5.0, u'5', u'5')]	|
|3	|27*1/6	|12*1/6	|[('R.0.1', 1.0, u'1', u'1'), ('R.1', 6.0, u'6', u'6')]	|




### (3) Mistake Group Wrong_Sign of size 3




### (2) Mistake Group ['R.0.1'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|22*1/5	|22*5*1/2	|[('R.0.1', 1.0, u'1', u'1')]	|
|1	|30*1/5	|30*1/2	|[('R.0.1', 1.0, u'1', u'1')]	|




### (60) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:b3hwang

	first_attempt
					2015-11-05 09:45:50
	part2_incorrect_attempt
					('0:10:25', u'C(26,9)')
					('9:21:13', u'9/26')
					('9:22:00', u'1/26')
	part2_correct_attempt
					['9:32:10', u'(1/6)*26']

1 Student ID:hmshah

	first_attempt
					2015-11-05 10:24:09
	part2_incorrect_attempt
					('11:09:43', u'21/2')
					('11:09:53', u'13/2')
					('11:09:59', u'8/2')
					('11:14:18', u'21*(8/21)')
					('11:15:54', u'21*(8/21)*(13/21)*15')

2 Student ID:agoldsht

	first_attempt
					2015-11-04 20:02:15
	part2_incorrect_attempt
					('0:01:13', u'10/28')
	part2_correct_attempt
					['0:01:59', u'28/5']

3 Student ID:ccn001

	first_attempt
					2015-11-02 19:52:13
	part2_incorrect_attempt
					('0:00:00', u'11.5')
					('21:44:05', u'10/22')
					('21:50:38', u'(10+11+12+13+14+15+16+17+18+19+20+21+22)/13')
					('2 days, 6:11:16', u'22/2')
	part2_correct_attempt
					['3 days, 1:58:44', u'22(0.25)']

4 Student ID:vsamant

	first_attempt
					2015-11-04 00:59:19
	part2_incorrect_attempt
					('0:01:00', u'27/2')
	part2_correct_attempt
					['0:01:18', u'27/6']

5 Student ID:hkhodada

	first_attempt
					2015-10-31 17:45:28
	part2_incorrect_attempt
					('2 days, 7:18:32', u'C(22,11)')
					('3 days, 11:48:21', u'(12*13)/8')
	part2_correct_attempt
					['4 days, 1:06:07', u'11/2']

6 Student ID:aggouw

	first_attempt
					2015-11-04 08:53:06
	part2_incorrect_attempt
					('0:00:16', u'25(1/4)')
	part2_correct_attempt
					['0:00:52', u'29(1/5)']

7 Student ID:abasu

	first_attempt
					2015-11-05 03:07:09
	part2_incorrect_attempt
					('0:02:55', u'29/2')
					('0:03:32', u'5/145')
	part2_correct_attempt
					['0:06:00', u'29(1/5)']

8 Student ID:fichoi

	first_attempt
					2015-11-04 18:14:52
	part2_incorrect_attempt
					('0:42:26', u'1/6*8')
	part2_correct_attempt
					['0:50:42', u'27/6']

9 Student ID:abjara

	first_attempt
					2015-11-04 03:06:02
	part2_incorrect_attempt
					('0:02:57', u'8/22')
	part2_correct_attempt
					['0:10:01', u'22*1/5']

10 Student ID:jjm019

	first_attempt
					2015-11-04 23:37:26
	part2_incorrect_attempt
					('5:59:18', u'[1*(1/2)]+[2*(1/2)]+[3*(1/2)]+[4*(1/2)]+[5*(1/2)]+[6*(1/2)]+[7*(1/2)]+[8*(1/2)]+[9*(1/2)]+[10*(1/2)]+[11*(1/2)]+[12*(1/2)]+[13*(1/2)]+[14*(1/2)]+[15*(1/2)]+[16*(1/2)]+[17*(1/2)]+[18*(1/2)]+[19*(1/2)]+[20*(1/2)]+[21*(1/2)]+[22*(1/2)]+[23*(1/2)]+[24*(1/2)]+[25*(1/2)]+[26*(1/2)]')
	part2_correct_attempt
					['6:23:53', u'26*(1/6)']

11 Student ID:mhale

	first_attempt
					2015-11-05 20:28:57
	part2_incorrect_attempt
					('0:01:06', u'6/27')
	part2_correct_attempt
					['0:01:30', u'27/6']

12 Student ID:krau

	first_attempt
					2015-11-05 03:11:39
	part2_incorrect_attempt
					('0:01:16', u'40/2')
	part2_correct_attempt
					['0:01:27', u'29/5']

13 Student ID:dcrume

	first_attempt
					2015-11-06 20:38:07
	part2_incorrect_attempt
					('0:09:47', u'25(1-10/25)')
					('0:12:18', u'25*(C(25,10))')
					('0:12:37', u'25*C(25,10)')
	part2_correct_attempt
					['0:19:11', u'25(1/5)']

14 Student ID:pvl001

	first_attempt
					2015-11-03 20:47:36
	part2_incorrect_attempt
					('0:00:49', u'10.5')
	part2_correct_attempt
					['0:01:22', u'21*0.2']

15 Student ID:mrchin

	first_attempt
					2015-11-06 19:53:59
	part2_incorrect_attempt
					('0:00:23', u'25*12')
	part2_correct_attempt
					['0:06:57', u'25/6']

16 Student ID:beyounge

	first_attempt
					2015-10-30 06:05:10
	part2_incorrect_attempt
					('0:03:09', u'28 / 2')
					('18:01:18', u'28/2')
					('18:01:29', u'9/2')
					('18:12:59', u'9 + [(28-9)/2]')
					('5 days, 23:32:51', u'28/2')
					('5 days, 23:33:10', u'9/2')
					('5 days, 23:33:24', u'(28-9)')
					('5 days, 23:38:57', u'(6 * (28 - 9)) / 2')
	part2_correct_attempt
					['6 days, 0:08:52', u'28/6']

17 Student ID:psable

	first_attempt
					2015-11-06 00:30:41
	part2_incorrect_attempt
					('0:05:20', u'6/23')
					('0:05:47', u'8/23')
	part2_correct_attempt
					['0:08:56', u'23/6']

18 Student ID:dkostins

	first_attempt
					2015-11-04 07:15:29
	part2_incorrect_attempt
					('0:05:48', u'.2')
					('0:06:00', u'.2/21')
	part2_correct_attempt
					['1 day, 21:45:27', u'21/5']

19 Student ID:jmiclat

	first_attempt
					2015-11-06 09:04:02
	part2_incorrect_attempt
					('0:05:30', u'1-Phi(11)')
					('0:05:39', u'1-Phi(29)')
					('14:20:17', u'Phi(11)')
					('14:20:55', u'Q(11)')
					('14:22:20', u'11/29')
					('14:23:57', u'11/(29*4)')
					('14:24:56', u'4/29')
					('14:25:23', u'11/29^4')
					('14:28:34', u'29*(11^4/29^4)')
	part2_correct_attempt
					['14:29:16', u'29*(1/4)']

20 Student ID:ksmurlo

	first_attempt
					2015-11-05 06:45:24
	part2_incorrect_attempt
					('0:00:00', u'C(29,11)(.25^11)(.75^18)')
					('0:03:08', u'(34597290)(.25^11)(.75^18)')
	part2_correct_attempt
					['0:03:47', u'29*.25']

21 Student ID:jyc018

	first_attempt
					2015-11-04 19:01:01
	part2_incorrect_attempt
					('1:04:44', u'210/20')
					('1:05:14', u'210/21')
					('1:05:42', u'(0+1+2+3+4+5+6+7+8+9+10+11+12+13+14+15+16+17+18+19+20)/21')
					('4:55:14', u'210/6**20')
					('4:57:28', u'(C(20,0) +C(20,1)+C(20,2)+C(20,3)+C(20,4)+C(20,5)+C(20,6)+C(20,7)+C(20,18)+C(20,9)+C(20,10))/6**20*2')
	part2_correct_attempt
					['4:59:40', u'20/6']

22 Student ID:jew037

	first_attempt
					2015-11-05 00:24:42
	part2_incorrect_attempt
					('0:00:37', u'26/(1/6)')
	part2_correct_attempt
					['0:01:00', u'26/6']

23 Student ID:j6quach

	first_attempt
					2015-11-05 09:30:45
	part2_incorrect_attempt
					('0:18:30', u'(1+2+3+4+5+6+7+8+9+10+11+12+13+14+15+16+17+18+19+20+21+22+23+24+25+26)/26')
	part2_correct_attempt
					['1:20:29', u'26*1/5']

24 Student ID:mnrahman

	first_attempt
					2015-11-07 00:02:07
	part2_incorrect_attempt
					('0:00:18', u'4.16')
	part2_correct_attempt
					['0:26:56', u'26/5']

25 Student ID:agarango

	first_attempt
					2015-11-06 20:14:19
	part2_incorrect_attempt
					('0:17:16', u'21/2')
	part2_correct_attempt
					['0:18:35', u'21*(1/6)']

26 Student ID:avasavad

	first_attempt
					2015-11-04 23:24:31
	part2_incorrect_attempt
					('-1 day, 23:58:47', u'11/29')
					('1 day, 13:22:09', u'(5/29)^29')
					('1 day, 13:24:06', u'5(1/29 + 2/29+3/29+4/29+6/29+7/29+8/29+9/29+10/29+11/29+12/29+13/29+14/29+15/29+16/29+17/29+18/29+20/29+21/29+22/29+23/29+24/29+25/29+26/29+27/29+28/29+1)')
					('1 day, 13:24:36', u'5(1/29 + 5/29 + 19/299 + 2/29+3/29+4/29+6/29+7/29+8/29+9/29+10/29+11/29+12/29+13/29+14/29+15/29+16/29+17/29+18/29+20/29+21/29+22/29+23/29+24/29+25/29+26/29+27/29+28/29+1)')
					('1 day, 13:24:58', u'5(1/29 + 5/29 + 19/29 + 2/29+3/29+4/29+6/29+7/29+8/29+9/29+10/29+11/29+12/29+13/29+14/29+15/29+16/29+17/29+18/29+20/29+21/29+22/29+23/29+24/29+25/29+26/29+27/29+28/29+1)')
					('1 day, 13:25:25', u'5/11(1+2+3+4+5+6+7+8+9+10+11)')
					('1 day, 13:25:32', u'1/11(1+2+3+4+5+6+7+8+9+10+11)')

27 Student ID:c1sorian

	first_attempt
					2015-11-05 00:40:50
	part2_incorrect_attempt
					('0:09:16', u'1+2+3+4+5+6+7+8+9+10+11+12+13+14+15+16+17+18+19+20+21+22+23+24+25+26+27')
					('0:09:35', u'(1+2+3+4+5+6+7+8+9+10+11+12+13+14+15+16+17+18+19+20+21+22+23+24+25+26+27)/27')
	part2_correct_attempt
					['1:08:22', u'(1/6)27']

28 Student ID:ralhadda

	first_attempt
					2015-10-31 21:01:50
	part2_incorrect_attempt
					('0:03:39', u'1/100')
					('0:03:49', u'1/25')
					('0:04:07', u'4/25')
	part2_correct_attempt
					['0:05:12', u'6.25']

29 Student ID:v3doan

	first_attempt
					2015-11-05 05:30:30
	part2_incorrect_attempt
					('10:52:24', u'(8+25)/2')
	part2_correct_attempt
					['1 day, 19:03:32', u'25 / 6']

30 Student ID:tol003

	first_attempt
					2015-11-03 19:59:02
	part2_incorrect_attempt
					('0:04:52', u'9/28')
	part2_correct_attempt
					['0:05:33', u'28*(1/5)']

31 Student ID:skodigal

	first_attempt
					2015-11-06 05:35:00
	part2_incorrect_attempt
					('0:01:12', u'17383860(1/6)^12 * (1-1/6)^(27-12)')
					('0:01:22', u'(1/6)^12 * (1-1/6)^(27-12)')
	part2_correct_attempt
					['0:03:13', u'27* (1/6)']

32 Student ID:hachrist

	first_attempt
					2015-11-03 21:54:37
	part2_incorrect_attempt
					('1 day, 2:50:40', u'1/5 * 11')
					('1 day, 9:09:19', u'5^11')
					('1 day, 10:49:03', u'2^11')
					('1 day, 22:56:21', u'21/2')
					('1 day, 22:56:52', u'1- (21/2 / 11)')
					('1 day, 22:58:43', u'1/5 * 21 /2')
					('1 day, 22:59:07', u'5.5')
					('1 day, 23:10:26', u'1/5/21')
					('1 day, 23:11:46', u'(11/5 + 12/5 + 13/5 + 14/5 + 16/5 + 17/5 + 18/5 + 19/5 + 20/5+ 21/5)/10')
	part2_correct_attempt
					['2 days, 0:32:41', u'21 * 1/5']

33 Student ID:kew017

	first_attempt
					2015-11-06 00:03:03
	part2_incorrect_attempt
					('0:37:01', u'22/12')
					('0:37:55', u'22/12')
	part2_correct_attempt
					['0:38:21', u'22/5']

34 Student ID:t1tran

	first_attempt
					2015-11-03 19:21:22
	part2_incorrect_attempt
					('0:03:23', u'12(4/24)')
	part2_correct_attempt
					['0:07:09', u'24(1/4)']

35 Student ID:dsmonaha

	first_attempt
					2015-11-06 19:23:26
	part2_incorrect_attempt
					('0:00:41', u'28/2')
	part2_correct_attempt
					['0:13:27', u'1/4*28']

36 Student ID:haliew

	first_attempt
					2015-11-06 23:10:07
	part2_incorrect_attempt
					('0:02:29', u'13(1/5)')
					('0:02:43', u'13/27')
	part2_correct_attempt
					['0:43:58', u'27/5']

37 Student ID:l8ngo

	first_attempt
					2015-11-04 01:12:39
	part2_incorrect_attempt
					('1 day, 21:39:05', u'21/2')
					('1 day, 21:40:00', u'11/21')
					('1 day, 21:40:13', u'21/11')
					('1 day, 21:41:56', u'231/2')
					('1 day, 21:43:14', u'21/2')
	part2_correct_attempt
					['1 day, 21:43:38', u'21/4']

38 Student ID:dsriniva

	first_attempt
					2015-11-05 16:50:26
	part2_incorrect_attempt
					('0:00:56', u'13.5')
	part2_correct_attempt
					['0:03:10', u'27/6']

39 Student ID:aurodrig

	first_attempt
					2015-11-06 23:34:06
	part2_incorrect_attempt
					('0:03:55', u'(4*24)/24')
					('0:06:39', u'24*(11/24)')
					('0:12:46', u'24 * (11/24)')
	part2_correct_attempt
					['0:17:59', u'24 * 1/4']

40 Student ID:sayao

	first_attempt
					2015-11-05 03:39:39
	part2_incorrect_attempt
					('-2 days, 22:13:27', u'((22*21/2)- (8*9/2))/14')
					('-2 days, 22:13:36', u'((22*21/2)- (8*9/2))/13')
					('-1 day, 23:57:41', u'(9+10+11+12+13+14+15+16+17+18+19+20+21+22)/14')
					('-1 day, 23:59:25', u'(22+23)/2/22')
					('0:02:44', u'22*4/22')
	part2_correct_attempt
					['0:04:04', u'.25*22']

41 Student ID:anvan

	first_attempt
					2015-11-05 08:30:59
	part2_incorrect_attempt
					('8:35:43', u'28 * (28! / 10!18!) * (.2)^10*(.8)18')
					('1 day, 5:42:06', u'28! / (5!23!) * (10)^.2 * (18)^.8')
					('1 day, 5:42:25', u'28! / (10!18!) * (10)^.2 * (18)^.8')
	part2_correct_attempt
					['1 day, 5:43:16', u'28(.2)']

42 Student ID:dpereira

	first_attempt
					2015-10-30 22:16:13
	part2_incorrect_attempt
					('0:06:32', u'Q(12)')
					('0:06:45', u'Q(11)')
	part2_correct_attempt
					['6 days, 0:19:27', u'20/4']

43 Student ID:ppanourg

	first_attempt
					2015-11-06 09:57:58
	part2_incorrect_attempt
					('0:00:58', u'5.5')
					('9:24:04', u'2.5')
					('9:26:01', u'(1/5)*(1+2+3+4+5+6+7+8+9+10+11+12+13+14+15+16+17+18+19+20+21+22+23+24+25+26+27+28)')
	part2_correct_attempt
					['9:27:31', u'28/5']

44 Student ID:dtea

	first_attempt
					2015-11-07 00:23:01
	part2_incorrect_attempt
					('0:01:09', u'(0+1+2+3+4+5+6+7+8+9+10+11+12+13+14+15+16+17+18+19+20+21+22)/22')
					('0:01:16', u'(0+1+2+3+4+5+6+7+8+9+10+11+12+13+14+15+16+17+18+19+20+21+22)/23')
					('0:01:35', u'(0+1+2+3+4+5+6+7+8+9+10+11+12+13+14+15+16+17+18+19+20+21+22)/22')

45 Student ID:dcastlem

	first_attempt
					2015-11-03 00:40:08
	part2_incorrect_attempt
					('0:22:26', u'10/26')
					('0:35:34', u'5/26')
	part2_correct_attempt
					['1:14:44', u'1/5*26']

46 Student ID:bakang

	first_attempt
					2015-11-05 08:51:51
	part2_incorrect_attempt
					('0:04:33', u'6+C(6,2)+C(6,3)+C(6,4)+C(6,5)+1')
					('0:13:18', u'(6+2*15+3*40+4*15+5*6+6)/126')
	part2_correct_attempt
					['0:15:55', u'1/6*21']

47 Student ID:qfu

	first_attempt
					2015-11-05 02:59:09
	part2_incorrect_attempt
					('0:13:17', u'1/5*14*29')
	part2_correct_attempt
					['1 day, 0:06:07', u'28/5']

48 Student ID:starinia

	first_attempt
					2015-11-05 03:24:47
	part2_incorrect_attempt
					('0:53:02', u'1/5 + 2/5 + 3/5 + 4/5 + 1')
					('1:03:33', u'28 / (1/5)')
					('1:03:59', u'28 /9')
	part2_correct_attempt
					['1:04:37', u'28 *( 1/5)']

49 Student ID:vasharma

	first_attempt
					2015-11-04 19:06:11
	part2_incorrect_attempt
					('0:02:47', u'0.00990321756631932')
	part2_correct_attempt
					['0:02:58', u'28*.2']

50 Student ID:kosung

	first_attempt
					2015-11-05 18:19:07
	part2_incorrect_attempt
					('0:04:32', u'2.5')
					('0:05:57', u'52.5')
	part2_correct_attempt
					['0:17:05', u'21/4']

51 Student ID:volim

	first_attempt
					2015-11-04 23:30:44
	part2_incorrect_attempt
					('0:00:27', u'9/23')
					('0:00:49', u'9/(23*6)')
					('0:38:37', u'Phi(23)')
					('0:48:37', u'23*.5')
	part2_correct_attempt
					['0:48:55', u'23*(1/6)']

52 Student ID:yypan

	first_attempt
					2015-11-03 00:31:21
	part2_incorrect_attempt
					('0:06:17', u'0.5')
					('0:06:49', u'0.5*23')
					('0:08:52', u'0.5')
					('0:11:30', u'23/1+23/2+23/3+23/4+23/5+23/6+23/7+23/8+23/9+23/10+23/11+23/12+23/13+23/14+23/15+23/16+23/17+23/18+23/19+23/20+23/21+23/22+23/23')
					('0:46:56', u'1/0.5')
					('1:00:27', u'23*0.5')
	part2_correct_attempt
					['1:00:46', u'23*0.2']

53 Student ID:aordookh

	first_attempt
					2015-11-04 22:22:30
	part2_incorrect_attempt
					('0:06:01', u'11(1/(28*6))')
					('1:33:32', u'1/(28*6)')
	part2_correct_attempt
					['1 day, 7:31:46', u'28/6']

54 Student ID:kew060

	first_attempt
					2015-11-05 01:37:43
	part2_incorrect_attempt
					('22:02:19', u'(1/4)*13')
					('22:02:25', u'(1/4)*14')
	part2_correct_attempt
					['22:02:32', u'(1/4)*26']

55 Student ID:ajvanega

	first_attempt
					2015-11-05 18:54:48
	part2_incorrect_attempt
					('0:27:56', u'12/30')
	part2_correct_attempt
					['7:09:10', u'(1/4)30']

56 Student ID:jguanzho

	first_attempt
					2015-11-05 14:49:30
	part2_incorrect_attempt
					('0:00:00', u'28*0.5')
	part2_correct_attempt
					['0:01:00', u'28*(1/6)']

57 Student ID:tpmach

	first_attempt
					2015-11-04 23:01:27
	part2_incorrect_attempt
					('0:00:27', u'1/2')
					('17:46:59', u'22/2')
	part2_correct_attempt
					['17:50:50', u'22*(1/5)']

58 Student ID:sghouse

	first_attempt
					2015-11-05 02:43:39
	part2_incorrect_attempt
					('0:05:29', u'11.5')
	part2_correct_attempt
					['0:05:58', u'23/5']

59 Student ID:kgrozav

	first_attempt
					2015-11-05 20:31:16
	part2_incorrect_attempt
					('0:11:54', u'12 * (1/4)')
	part2_correct_attempt
					['0:12:04', u'26 * (1/4)']












## Part 3

### (106) Mistake Group Digits of size 106




### (20) Mistake Group ['R.0.0'] of size 20
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|sqrt(21*1/5*(1-1/5))	|sqrt(4.2/21)	|[('R.0.0', 4.2, u'21*1/5', u'4.2')]	|
|1	|sqrt(21*1/5*(1-1/5))	|sqrt(4.2)/sqrt(21)	|[('R.0.0', 4.2, u'21*1/5', u'4.2')]	|
|2	|sqrt(21*1/5*(1-1/5))	|sqrt(4.2)/21	|[('R.0.0', 4.2, u'21*1/5', u'4.2')]	|
|3	|sqrt(27*1/6*(1-1/6))	|((27/6)(1/26))^(1/2)	|[('R.0.0', 4.5, u'27*1/6', u'27/6')]	|
|4	|sqrt(26*1/5*(1-1/5))	|sqrt(26/5)*(1-1/5)	|[('R.0.0', 5.2, u'26*1/5', u'26/5')]	|
|5	|sqrt(22*1/4*(1-1/4))	|sqrt((22/4)*(22-13))	|[('R.0.0', 5.5, u'22*1/4', u'22/4')]	|
|6	|sqrt(21*1/6*(1-1/6))	|sqrt((1/6*21)+(1/6*21)^2)	|[('R.0.0', 3.5, u'21*1/6', u'1/6*21')]	|
|7	|sqrt(29*1/5*(1-1/5))	|29*1/5*4/5	|[('R.0.0', 5.8, u'29*1/5', u'29*1/5')]	|
|8	|sqrt(26*1/5*(1-1/5))	|sqrt(26*(1/5)) * (1-1/5)	|[('R.0.0', 5.2, u'26*1/5', u'26*(1/5)')]	|
|9	|sqrt(27*1/6*(1-1/6))	|(((1/6)27)((1/6)(5/6)27))^.5	|[('R.0.0', 4.5, u'27*1/6', u'(1/6)27')]	|
|10	|sqrt(21*1/6*(1-1/6))	|sqrt(3.5/20)	|[('R.0.0', 3.5, u'21*1/6', u'3.5')]	|
|11	|sqrt(21*1/6*(1-1/6))	|sqrt(3.5/8)	|[('R.0.0', 3.5, u'21*1/6', u'3.5')]	|
|12	|sqrt(21*1/6*(1-1/6))	|sqrt(3.5/21)	|[('R.0.0', 3.5, u'21*1/6', u'3.5')]	|
|13	|sqrt(29*1/6*(1-1/6))	|sqrt((29/6) * 0.75)	|[('R.0.0', 4.833333333333333, u'29*1/6', u'29/6')]	|
|14	|sqrt(27*1/5*(1-1/5))	|((5.4)-11)^2	|[('R.0.0', 5.4, u'27*1/5', u'5.4')]	|
|15	|sqrt(26*1/6*(1-1/6))	|sqrt((26/6)/6)	|[('R.0.0', 4.333333333333333, u'26*1/6', u'26/6')]	|
|16	|sqrt(30*1/4*(1-1/4))	|sqrt(7.5*5)	|[('R.0.0', 7.5, u'30*1/4', u'7.5')]	|
|17	|sqrt(30*1/4*(1-1/4))	|sqrt(7.5*4)	|[('R.0.0', 7.5, u'30*1/4', u'7.5')]	|
|18	|sqrt(30*1/6*(1-1/6))	|sqrt((30/6)(1-(1/180)))	|[('R.0.0', 5.0, u'30*1/6', u'30/6')]	|
|19	|sqrt(30*1/6*(1-1/6))	|sqrt((30/6)(1-(1/5)))	|[('R.0.0', 5.0, u'30*1/6', u'30/6')]	|




### (20) Mistake Group redirect of size 20




### (13) Mistake Group ['R.0.0.0.0'] of size 13
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|sqrt(25*1/6*(1-1/6))	|(25(1/6)(1-(1/6)))^1/2	|[('R.0.0.0.0', 25.0, u'25', u'25')]	|
|1	|sqrt(30*1/4*(1-1/4))	|((30*.25)^2-(30*(.25^2))^2)^(1/2)	|[('R.0.0.0.0', 30.0, u'30', u'30')]	|
|2	|sqrt(28*1/6*(1-1/6))	|sqrt((28^2/6) - ((28/6) ^ 2))	|[('R.0.0.0.0', 28.0, u'28', u'28')]	|
|3	|sqrt(28*1/6*(1-1/6))	|sqrt(((28/3)^2) - ((28/6) ^ 2))	|[('R.0.0.0.0', 28.0, u'28', u'28')]	|
|4	|sqrt(28*1/6*(1-1/6))	|sqrt(((28/2) ^ 2)- ((28/6) ^ 2))	|[('R.0.0.0.0', 28.0, u'28', u'28')]	|
|5	|sqrt(28*1/6*(1-1/6))	|sqrt(((28^2)/6)- ((28/6) ^ 2))	|[('R.0.0.0.0', 28.0, u'28', u'28')]	|
|6	|sqrt(28*1/6*(1-1/6))	|sqrt(((28^3)/36) - ((28/6)^2))	|[('R.0.0.0.0', 28.0, u'28', u'28')]	|
|7	|sqrt(28*1/6*(1-1/6))	|sqrt((28^2/6) - ((28/6)^2))	|[('R.0.0.0.0', 28.0, u'28', u'28')]	|
|8	|sqrt(21*1/6*(1-1/6))	|sqrt((0-3.5)^2+(1-3.5)^2+(2-3.5)^2+(3-3.5)^2+(4-3.5)^2+(5-3.5)^2+(6-3.5)^2)	|[('R.0.0.0.0', 21.0, u'21', u'(0-3.5)^2+(1-3.5)^2+(2-3.5)^2+(3-3.5)^2')]	|
|9	|sqrt(30*1/4*(1-1/4))	|sqrt((30^2/4)-(30/4)^2)	|[('R.0.0.0.0', 30.0, u'30', u'30')]	|
|10	|sqrt(30*1/4*(1-1/4))	|(((30*.25)-11)^2)^(1/2)	|[('R.0.0.0.0', 30.0, u'30', u'30')]	|
|11	|sqrt(24*1/4*(1-1/4))	|sqrt((24-6)^2)/4	|[('R.0.0.0.0', 24.0, u'24', u'24')]	|
|12	|sqrt(24*1/4*(1-1/4))	|sqrt(((24-6)^2)/4)	|[('R.0.0.0.0', 24.0, u'24', u'24')]	|




### (11) Mistake Group ['R.0'] of size 11
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|sqrt(26*1/5*(1-1/5))	|(26*0.8*0.2)*0.5	|[('R.0', 4.16, u'26*1/5*(1-1/5)', u'26*0.8*0.2')]	|
|1	|sqrt(27*1/4*(1-1/4))	|(27(.25)(.75))^2	|[('R.0', 5.0625, u'27*1/4*(1-1/4)', u'27(.25)(.75)')]	|
|2	|sqrt(29*1/5*(1-1/5))	|(29(1/5)*(4/5))^2	|[('R.0', 4.64, u'29*1/5*(1-1/5)', u'29(1/5)*(4/5)')]	|
|3	|sqrt(23*1/6*(1-1/6))	|(23*5/36)^1/2	|[('R.0', 3.1944444444444446, u'23*1/6*(1-1/6)', u'(23*5/36)^1')]	|
|4	|sqrt(30*1/4*(1-1/4))	|((30*.25)*.75)^1/2	|[('R.0', 5.625, u'30*1/4*(1-1/4)', u'((30*.25)*.75)^1')]	|
|5	|sqrt(22*1/6*(1-1/6))	|(22/6*(1-1/6))^1/2	|[('R.0', 3.0555555555555554, u'22*1/6*(1-1/6)', u'(22/6*(1-1/6))^1')]	|
|6	|sqrt(28*1/4*(1-1/4))	|((1/4) * 28 (1-1/4))^1/2	|[('R.0', 5.25, u'28*1/4*(1-1/4)', u'((1/4) * 28 (1-1/4))^1')]	|
|7	|sqrt(23*1/4*(1-1/4))	|(1/4 * (1 - 1/4 ) * 23 )^1/2	|[('R.0', 4.3125, u'23*1/4*(1-1/4)', u'(1/4 * (1 - 1/4 ) * 23 )^1')]	|
|8	|sqrt(21*1/5*(1-1/5))	|(21*1/5*4/5)^1/2	|[('R.0', 3.3600000000000003, u'21*1/5*(1-1/5)', u'(21*1/5*4/5)^1')]	|
|9	|sqrt(21*1/5*(1-1/5))	|(21*(1/5)*(4/5))^1/2	|[('R.0', 3.3600000000000003, u'21*1/5*(1-1/5)', u'(21*(1/5)*(4/5))^1')]	|
|10	|sqrt(24*1/6*(1-1/6))	|[24(1/6)(1-1/6)]^1/2	|[('R.0', 3.3333333333333335, u'24*1/6*(1-1/6)', u'[24(1/6)(1-1/6)]^1')]	|




### (10) Mistake Group ['R.0.1'] of size 10
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|sqrt(25*1/5*(1-1/5))	|sqrt(25*5*(1-(1/5)))	|[('R.0.1', 0.8, u'1-1/5', u'1-(1/5)')]	|
|1	|sqrt(27*1/6*(1-1/6))	|sqrt( (27*6)* (1-1/6) )	|[('R.0.1', 0.8333333333333334, u'1-1/6', u'1-1/6')]	|
|2	|sqrt(24*1/4*(1-1/4))	|((1/4)(1-(1/4)))**(.5)	|[('R.0.1', 0.75, u'1-1/4', u'1-(1/4)')]	|
|3	|sqrt(21*1/5*(1-1/5))	|sqrt((.20*.80))	|[('R.0.1', 0.8, u'1-1/5', u'.80')]	|
|4	|sqrt(25*1/6*(1-1/6))	|[(1/6)(5/6)]^2	|[('R.0.1', 0.8333333333333334, u'1-1/6', u'5/6')]	|
|5	|sqrt(29*1/5*(1-1/5))	|((1/5)*(4/5))^2	|[('R.0.1', 0.8, u'1-1/5', u'4/5')]	|
|6	|sqrt(28*1/6*(1-1/6))	|sqrt((1/6) * (5/6))	|[('R.0.1', 0.8333333333333334, u'1-1/6', u'5/6')]	|
|7	|sqrt(24*1/6*(1-1/6))	|sqrt(1/6*(1-1/6))	|[('R.0.1', 0.8333333333333334, u'1-1/6', u'1-1/6')]	|
|8	|sqrt(21*1/6*(1-1/6))	|(1/6)*(5/6)*21	|[('R.0.1', 0.8333333333333334, u'1-1/6', u'5/6')]	|
|9	|sqrt(27*1/5*(1-1/5))	|(1/5)*(4/5)*27	|[('R.0.1', 0.8, u'1-1/5', u'4/5')]	|




### (7) Mistake Group Wrong_Sign of size 7




### (2) Mistake Group ['R.0.1.1'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|sqrt(28*1/5*(1-1/5))	|sqrt(28*(21.16*(1/5)))	|[('R.0.1.1', 0.2, u'1/5', u'1/5')]	|
|1	|sqrt(21*1/5*(1-1/5))	|(8 - (21*0.2))^2	|[('R.0.1.1', 0.2, u'1/5', u'0.2')]	|




### (1) Mistake Group ['R.0.0', 'R.0.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|sqrt(30*1/4*(1-1/4))	|((30*.25)-.75)^(1/2)	|[('R.0.0', 7.5, u'30*1/4', u'30*.25)'), ('R.0.1', 0.75, u'1-1/4', u'.75)')]	|




### (1) Mistake Group Fraction of size 1




### (111) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:gthorn

	first_attempt
					2015-11-05 07:00:22
	part2_correct_attempt
					['0:00:59', u'28/5']
	part3_incorrect_attempt
					('10:46:57', u'sqrt((.2 * .8)/28)')
					('11:02:19', u'(28^2/5)-(28/5)^2')
	part3_correct_attempt
					['11:05:57', u'sqrt(.2*.8*28)']

1 Student ID:kbielawi

	first_attempt
					2015-11-05 21:20:09
	part2_correct_attempt
					['0:02:14', u'24/5']
	part3_incorrect_attempt
					('0:06:18', u'sqrt((24/5)*(1-(1/5))*24)')
	part3_correct_attempt
					['0:07:20', u'sqrt((1/5)*(1-(1/5))*24)']

2 Student ID:jguanzho

	first_attempt
					2015-11-05 14:49:30
	part2_correct_attempt
					['0:01:00', u'28*(1/6)']
	part3_incorrect_attempt
					('0:01:00', u'(28*(1/6))**0.5')
	part3_correct_attempt
					['2:52:03', u'(1/6*5/6*28)**0.5']

3 Student ID:alakamsa

	first_attempt
					2015-11-04 18:21:07
	part2_correct_attempt
					['0:00:00', u'4']
	part3_incorrect_attempt
					('0:00:00', u'24*(1/6)*(1-(1/6))')
	part3_correct_attempt
					['0:00:27', u'sqrt(24*(1/6)*(1-(1/6)))']

4 Student ID:ctgraves

	first_attempt
					2015-11-03 05:25:59
	part2_correct_attempt
					['0:01:06', u'29/6']
	part3_incorrect_attempt
					('2 days, 20:36:30', u'1/6')
					('2 days, 20:41:33', u'( 29*29/36- 29/36)**0.5')
					('2 days, 20:50:29', u'(5/36/29)**0.5')
	part3_correct_attempt
					['2 days, 21:04:23', u'(5/36*29)**0.5']

5 Student ID:dkurli

	first_attempt
					2015-11-05 03:11:30
	part2_correct_attempt
					['0:00:54', u'22/4']
	part3_incorrect_attempt
					('0:02:28', u'22/4')
					('0:05:13', u'3.31662479036')
					('0:13:49', u'Phi(1)')
	part3_correct_attempt
					['0:14:54', u'sqrt(22*3/16)']

6 Student ID:dan029

	first_attempt
					2015-11-05 09:16:18
	part2_correct_attempt
					['0:06:47', u'5']
	part3_incorrect_attempt
					('0:07:20', u'3.75')
	part3_correct_attempt
					['0:07:40', u'sqrt(3.75)']

7 Student ID:jyc018

	first_attempt
					2015-11-04 19:01:01
	part2_correct_attempt
					['4:59:40', u'20/6']
	part3_incorrect_attempt
					('5:04:16', u'0.5')
					('5:04:22', u'1/6')
					('5:06:40', u'20*1/6*(5/6)')
	part3_correct_attempt
					['5:07:40', u'sqrt(20*1/6*(5/6))']

8 Student ID:vqt004

	first_attempt
					2015-11-06 05:57:50
	part2_correct_attempt
					['0:10:09', u'30*1/5']
	part3_incorrect_attempt
					('0:10:09', u'sqrt(1/25*30)')
	part3_correct_attempt
					['0:10:45', u'sqrt(4/25*30)']

9 Student ID:dgunawan

	first_attempt
					2015-11-05 08:48:59
	part2_correct_attempt
					['0:00:00', u'(1/4) * 28']
	part3_incorrect_attempt
					('0:00:00', u'([(1/4) * 28]^2)^(1/2)')
					('1:03:33', u'([(1/4) * 28]^2/28)^(1/2)')
					('1:05:01', u'1/4')
					('1:06:24', u'(13-7)^2')
					('1:06:54', u'(13-7)^2/28')
					('1:07:07', u'[(13-7)^2/28]^(1/2)')
					('1:07:19', u'[(13-7)^2/4]^(1/2)')
	part3_correct_attempt
					['15:23:45', u'((1/4) * 28 (1-1/4))^(1/2)']

10 Student ID:mpanelo

	first_attempt
					2015-11-05 22:51:02
	part2_correct_attempt
					['0:00:00', u'13/3']
	part3_incorrect_attempt
					('0:04:36', u'65/18')
	part3_correct_attempt
					['0:09:29', u'sqrt(65/18)']

11 Student ID:tstevens

	first_attempt
					2015-11-06 12:00:01
	part2_correct_attempt
					['0:00:10', u'24*.2']
	part3_incorrect_attempt
					('0:00:40', u'.2')
	part3_correct_attempt
					['0:05:23', u'1.959591794']

12 Student ID:tcuddy

	first_attempt
					2015-11-03 17:42:18
	part2_correct_attempt
					['0:47:02', u'(1/4)24']
	part3_incorrect_attempt
					('0:48:21', u'(1/4)(1-(1/4))**(.5)')
	part3_correct_attempt
					['2 days, 0:11:33', u'[ (1/4)(1-.25)24 ]**.5']

13 Student ID:djk006

	first_attempt
					2015-11-04 00:35:35
	part2_correct_attempt
					['0:25:13', u'27/4']
	part3_incorrect_attempt
					('0:25:13', u'.341*27/4')
					('0:30:35', u'(.25*27)^(1/2)')
					('0:30:50', u'(.25*28)^(1/2)')
					('0:35:49', u'(.25^2*27)^(1/2)')
					('0:36:01', u'(.25^2*28)^(1/2)')
					('0:36:09', u'(.25^2*26)^(1/2)')
					('1:12:55', u'(.25*27)^(1/2)')
					('1:16:47', u'27*34.1')
					('1:17:00', u'27*.341')
					('1:20:54', u'27*.34')
					('1:25:59', u'6.75*.341')
					('1:26:04', u'6.75*.34')
	part3_correct_attempt
					['1:38:44', u'(27(.25)(.75))^(1/2)']

14 Student ID:dando

	first_attempt
					2015-11-06 22:50:24
	part2_correct_attempt
					['0:00:00', u'23/5']
	part3_incorrect_attempt
					('0:14:53', u'3.6')
	part3_correct_attempt
					['0:51:46', u'sqrt((1/5)(4/5)23)']

15 Student ID:dsriniva

	first_attempt
					2015-11-05 16:50:26
	part2_correct_attempt
					['0:03:10', u'27/6']
	part3_incorrect_attempt
					('0:05:38', u'0.372678')
					('0:12:05', u'1/27')
					('0:12:17', u'1/6')
					('2:32:58', u'27*(1/6)(5/6)')
	part3_correct_attempt
					['2:33:19', u'sqrt(27*(1/6)(5/6))']

16 Student ID:sayao

	first_attempt
					2015-11-05 03:39:39
	part2_correct_attempt
					['0:04:04', u'.25*22']
	part3_incorrect_attempt
					('0:09:27', u'sqrt(((1-5.5)^2+(2-5.5)^2+(3-5.5)^2+(4-5.5)^2+(5-5.5)^2+(6-5.5)^2+(7-5.5)^2+(8-5.5)^2+(9-5.5)^2+(10-5.5)^2+(11-5.5)^2+(12-5.5)^2+(13-5.5)^2+(14-5.5)^2+(15-5.5)^2+(16-5.5)^2+(17-5.5)^2+(18-5.5)^2+(19-5.5)^2+(20-5.5)^2+(21-5.5)^2+(22-5.5)^2)/22)')
					('0:12:15', u'sqrt(((1-5.5)^2+(2-5.5)^2+(3-5.5)^2+(4-5.5)^2+(5-5.5)^2+(6-5.5)^2+(7-5.5)^2+(8-5.5)^2+(9-5.5)^2+(10-5.5)^2+(11-5.5)^2+(12-5.5)^2+(13-5.5)^2+(14-5.5)^2+(15-5.5)^2+(16-5.5)^2+(17-5.5)^2+(18-5.5)^2+(19-5.5)^2+(20-5.5)^2+(21-5.5)^2+(22-5.5)^2)/21)')
					('0:16:50', u'sqrt(((1-5.5)^2+(2-5.5)^2+(3-5.5)^2+(4-5.5)^2+(5-5.5)^2+(6-5.5)^2+(7-5.5)^2+(8-5.5)^2+(9-5.5)^2+(10-5.5)^2+(11-5.5)^2+(12-5.5)^2+(13-5.5)^2+(14-5.5)^2+(15-5.5)^2+(16-5.5)^2+(17-5.5)^2+(18-5.5)^2+(19-5.5)^2+(20-5.5)^2+(21-5.5)^2+(22-5.5)^2)/21)/4')
					('0:17:01', u'sqrt(((1-5.5)^2+(2-5.5)^2+(3-5.5)^2+(4-5.5)^2+(5-5.5)^2+(6-5.5)^2+(7-5.5)^2+(8-5.5)^2+(9-5.5)^2+(10-5.5)^2+(11-5.5)^2+(12-5.5)^2+(13-5.5)^2+(14-5.5)^2+(15-5.5)^2+(16-5.5)^2+(17-5.5)^2+(18-5.5)^2+(19-5.5)^2+(20-5.5)^2+(21-5.5)^2+(22-5.5)^2)/21)*4')
					('0:17:13', u'sqrt(((1-5.5)^2+(2-5.5)^2+(3-5.5)^2+(4-5.5)^2+(5-5.5)^2+(6-5.5)^2+(7-5.5)^2+(8-5.5)^2+(9-5.5)^2+(10-5.5)^2+(11-5.5)^2+(12-5.5)^2+(13-5.5)^2+(14-5.5)^2+(15-5.5)^2+(16-5.5)^2+(17-5.5)^2+(18-5.5)^2+(19-5.5)^2+(20-5.5)^2+(21-5.5)^2+(22-5.5)^2)/21)/2')
	part3_correct_attempt
					['19:33:44', u'sqrt(.25*.75*22)']

17 Student ID:m4bui

	first_attempt
					2015-11-06 04:35:06
	part2_correct_attempt
					['0:02:35', u'21/6']
	part3_incorrect_attempt
					('0:04:07', u'sqrt(21)*(1/6)*(1-1/6)')
	part3_correct_attempt
					['0:04:49', u'sqrt(21*(1/6)*(1-1/6))']

18 Student ID:flhernan

	first_attempt
					2015-11-03 20:40:09
	part2_correct_attempt
					['0:00:00', u'26/5']
	part3_incorrect_attempt
					('0:00:45', u'(26/5)^2')
	part3_correct_attempt
					['0:04:04', u'sqrt(26/5*(4/5))']

19 Student ID:a2ahmed

	first_attempt
					2015-11-07 00:47:00
	part2_correct_attempt
					['0:04:25', u'3.5']
	part3_incorrect_attempt
					('0:05:58', u'2.5')
					('0:08:07', u'.119047')
					('0:11:12', u'35/12')
	part3_correct_attempt
					['0:12:26', u'1.707825128']

20 Student ID:c1wei

	first_attempt
					2015-11-04 06:53:18
	part2_correct_attempt
					['0:06:47', u'6']
	part3_incorrect_attempt
					('0:20:04', u'1-Phi(1/5)')
					('0:20:37', u'1/5')
	part3_correct_attempt
					['0:22:21', u'sqrt(6*.8)']

21 Student ID:m8woo

	first_attempt
					2015-11-05 21:11:06
	part2_correct_attempt
					['-1 day, 23:57:29', u'1/6 * 30']
	part3_incorrect_attempt
					('0:05:54', u'[(1/6)*(5/6)/30]^(1/2)')
	part3_correct_attempt
					['0:09:55', u'[(1/6)*(5/6)*30]^(1/2)']

22 Student ID:akg009

	first_attempt
					2015-11-06 21:52:34
	part2_correct_attempt
					['0:01:35', u'27*(1/5)']
	part3_incorrect_attempt
					('0:02:14', u'1/5')
	part3_correct_attempt
					['0:04:31', u'(6/5)*sqrt(3)']

23 Student ID:jhp077

	first_attempt
					2015-11-05 13:19:35
	part2_correct_attempt
					['0:00:57', u'5']
	part3_incorrect_attempt
					('0:02:06', u'(75)^(1/2)')
					('0:03:35', u'75^(1/2)')
					('0:08:28', u'5^(3/2)')
					('0:14:07', u'15/4')
					('0:17:07', u'75^(1/2)')
					('0:21:29', u'(3/320)^(1/2)')
	part3_correct_attempt
					['0:22:54', u'(15)^(1/2) / 2']

24 Student ID:b3hwang

	first_attempt
					2015-11-05 09:45:50
	part2_correct_attempt
					['9:32:10', u'(1/6)*26']
	part3_incorrect_attempt
					('9:34:17', u'((1/6)*26)(1-(1/6))^1/2')
					('9:34:32', u'((1/6)*26)(1-(1/6))^(1/2)')
	part3_correct_attempt
					['9:34:47', u'(((1/6)*26)(1-(1/6)))^(1/2)']

25 Student ID:ccn001

	first_attempt
					2015-11-02 19:52:13
	part2_correct_attempt
					['3 days, 1:58:44', u'22(0.25)']
	part3_incorrect_attempt
					('3 days, 1:58:44', u'((0.25(1-0.25))/22)^(0.5)')
	part3_correct_attempt
					['3 days, 2:07:39', u'((0.25(1-0.25))22)^(0.5)']

26 Student ID:lguintu

	first_attempt
					2015-11-03 04:53:50
	part2_correct_attempt
					['0:03:20', u'24/5']
	part3_incorrect_attempt
					('0:05:21', u'4.8')
					('0:05:55', u'(24-4.8)^(1/2)')
	part3_correct_attempt
					['0:14:03', u'(24*(1/5)*(4/5))^(1/2)']

27 Student ID:c1sorian

	first_attempt
					2015-11-05 00:40:50
	part2_correct_attempt
					['1:08:22', u'(1/6)27']
	part3_incorrect_attempt
					('1:13:53', u'6(7^.5)')
	part3_correct_attempt
					['1 day, 3:18:02', u'(((1/6)(5/6)27))^.5']

28 Student ID:atorr

	first_attempt
					2015-11-05 20:12:03
	part2_correct_attempt
					['0:00:54', u'(1/5) * 30']
	part3_incorrect_attempt
					('0:03:24', u'((1/5) * 30)^0.5')
	part3_correct_attempt
					['0:06:22', u'(30 * 0.2 * 0.8)^0.5']

29 Student ID:b1yao

	first_attempt
					2015-11-04 19:19:02
	part2_correct_attempt
					['0:11:45', u'(29/6)']
	part3_incorrect_attempt
					('0:11:45', u'((-2*(29/6)*29+8555-29*(29/6)^2)/29)^0.5')
					('0:17:14', u'((-2*(29/6)*30+8555-30*(29/6)^2)/29)^0.5')
					('0:17:43', u'((-2*(29/6)*30+8555+30*(29/6)^2)/29)^0.5')
					('0:18:08', u'29/6')
	part3_correct_attempt
					['0:21:04', u'(29*1*5/36)^0.5']

30 Student ID:thk002

	first_attempt
					2015-11-03 23:40:48
	part2_correct_attempt
					['1 day, 6:12:15', u'4']
	part3_incorrect_attempt
					('1 day, 7:09:11', u'4* (1-1/6)')
	part3_correct_attempt
					['1 day, 7:09:29', u'sqrt(4* (1-1/6))']

31 Student ID:krau

	first_attempt
					2015-11-05 03:11:39
	part2_correct_attempt
					['0:01:27', u'29/5']
	part3_incorrect_attempt
					('0:02:29', u'11/5')
					('0:06:00', u'5.62731')
					('0:13:05', u'sqrt((11-29/5)/29)')
	part3_correct_attempt
					['0:15:22', u'(29*4/25)^.5']

32 Student ID:crmirand

	first_attempt
					2015-11-03 05:26:40
	part2_correct_attempt
					['0:01:16', u'27/5']
	part3_incorrect_attempt
					('0:06:57', u'27/5 + 1')
					('0:08:11', u'27/15')
					('0:12:30', u'27-(27/5)/3')
					('0:12:41', u'(27-(27/5))/3')
					('0:13:39', u'(27/5)^1/2')
					('0:16:15', u'(27-27/5)^2+ (27/5)^2')
					('0:16:41', u'(((27-27/5)^2+ (27/5)^2)/2)^1/2')
					('0:17:00', u'(((27-27/5)^2+ (27/5)^2)/2)^(1/2)')
	part3_correct_attempt
					['0:43:11', u'(27*4/25)^.5']

33 Student ID:beyounge

	first_attempt
					2015-10-30 06:05:10
	part2_correct_attempt
					['6 days, 0:08:52', u'28/6']
	part3_incorrect_attempt
					('6 days, 0:13:14', u'sqrt((28^2) - ((28/6) ^ 2))')
					('6 days, 0:17:24', u'sqrt((28) - ((28/6) ^ 2))')
					('6 days, 0:22:05', u'sqrt((28 * (28/6)^2) - ((28/6) ^ 2))')
					('6 days, 0:30:27', u'sqrt((28 - (28/6)) ^ 2)')
					('6 days, 0:45:20', u'sqrt(7714 - ((28/6) ^ 2))')
					('6 days, 0:50:08', u'sqrt((((28*5)/6) ^2) - ((28/6)^2))')
					('6 days, 1:11:42', u'sqrt(((28/6)^2))')
					('6 days, 1:38:06', u'sqrt((406) - ((28/6)^2))')
					('6 days, 1:38:24', u'sqrt((406/6) - ((28/6)^2))')
					('6 days, 1:43:13', u'sqrt(5/36)')
					('6 days, 1:44:16', u'sqrt(5/(36*28))')
					('6 days, 1:47:53', u'sqrt(((29*57)/6) - ((28/6) ^2))')
	part3_correct_attempt
					['6 days, 1:50:13', u'sqrt(28*(5/36))']

34 Student ID:tpmach

	first_attempt
					2015-11-04 23:01:27
	part2_correct_attempt
					['17:50:50', u'22*(1/5)']
	part3_incorrect_attempt
					('17:51:07', u'sqrt(22*(1/5))')
	part3_correct_attempt
					['17:57:41', u'sqrt(1/5(1-1/5)22)']

35 Student ID:jhw015

	first_attempt
					2015-11-06 19:14:12
	part3_incorrect_attempt
					('0:00:00', u'sqrt((29/6))')
	part3_correct_attempt
					['0:01:17', u'sqrt((29/6) * (5/6))']

36 Student ID:t1tran

	first_attempt
					2015-11-03 19:21:22
	part2_correct_attempt
					['0:07:09', u'24(1/4)']
	part3_incorrect_attempt
					('0:16:11', u'24(1/4)(1-1/4)')
	part3_correct_attempt
					['0:51:33', u'(24(1/4)(1-(1/4)))^(1/2)']

37 Student ID:z3meng

	first_attempt
					2015-11-05 08:07:19
	part2_correct_attempt
					['0:14:18', u'4.8']
	part3_incorrect_attempt
					('0:20:13', u'2/25')
					('0:20:28', u'4/25')
					('0:36:17', u'4.8*0.8')
					('0:36:30', u'4.8*0.2')
					('0:36:36', u'4.8*0.8')
					('0:37:28', u'3.84')
	part3_correct_attempt
					['0:38:23', u'(3.84)^0.5']

38 Student ID:akalathi

	first_attempt
					2015-11-04 06:30:40
	part2_correct_attempt
					['0:00:17', u'1/5 * 29']
	part3_incorrect_attempt
					('0:01:49', u'((12/5)*(36/5))^2')
	part3_correct_attempt
					['0:02:46', u'sqrt((29(1/5)*(4/5)))']

39 Student ID:jel075

	first_attempt
					2015-11-05 09:10:18
	part2_correct_attempt
					['0:02:18', u'5.2']
	part3_incorrect_attempt
					('0:03:05', u'0.2')
					('13:32:36', u'sqrt(5.2)')
					('13:36:00', u'.1')
					('13:36:06', u'.3')
					('13:36:11', u'.4')
					('13:36:14', u'.5')
	part3_correct_attempt
					['13:40:20', u'sqrt(26*(1/5) * (1-1/5))']

40 Student ID:edescobe

	first_attempt
					2015-11-01 09:54:00
	part2_correct_attempt
					['3 days, 1:45:13', u'20/6']
	part3_incorrect_attempt
					('3 days, 1:47:21', u'1.3416')
	part3_correct_attempt
					['3 days, 1:50:16', u'( 20 / 6* (1-1/ 6))^(1/2)']

41 Student ID:etemlock

	first_attempt
					2015-11-06 21:35:14
	part2_correct_attempt
					['0:27:23', u'28/5']
	part3_incorrect_attempt
					('0:30:53', u'(4/25)^.5')
					('0:31:01', u'28(4/25)^.5')
	part3_correct_attempt
					['0:31:26', u'(112/25)^.5']

42 Student ID:ggaddi

	first_attempt
					2015-11-05 05:19:24
	part2_correct_attempt
					['0:05:04', u'6']
	part3_incorrect_attempt
					('0:12:34', u'(25+16+9+4+1+0+1+4+9+16+25+36+49+64+81+100+121+144+169+196+225+256+289+324)/24')
					('0:13:19', u'(25+16+9+4+1+0+1+4+9+16+25+36+49+64+81+100+121+144+169+196+225+256+289+324)/4/24')
					('0:21:21', u'sqrt((25+16+9+4+1+0+1+4+9+16+25+36+49+64+81+100+121+144+169+196+225+256+289+324)/24)')
					('0:21:39', u'sqrt((25+16+9+4+1+0+1+4+9+16+25+36+49+64+81+100+121+144+169+196+225+256+289+324)/4/24)')
	part3_correct_attempt
					['12:34:05', u'sqrt((3/16)*24)']

43 Student ID:muy002

	first_attempt
					2015-11-06 00:19:06
	part2_correct_attempt
					['4:12:15', u'4']
	part3_incorrect_attempt
					('4:12:52', u'80/25')
	part3_correct_attempt
					['4:13:31', u'sqrt(80/25)']

44 Student ID:v4sharma

	first_attempt
					2015-11-05 22:14:51
	part2_correct_attempt
					['0:07:23', u'4']
	part3_incorrect_attempt
					('0:51:21', u'(20)(1/5)(4/5)')
	part3_correct_attempt
					['0:51:52', u'sqrt((20)(1/5)(4/5))']

45 Student ID:qfu

	first_attempt
					2015-11-05 02:59:09
	part2_correct_attempt
					['1 day, 0:06:07', u'28/5']
	part3_incorrect_attempt
					('1 day, 0:06:07', u'sqrt(5*(4/25))')
	part3_correct_attempt
					['1 day, 0:07:24', u'sqrt(28*(4/25))']

46 Student ID:yjshin

	first_attempt
					2015-11-06 23:59:29
	part2_correct_attempt
					['0:00:42', u'22/6']
	part3_incorrect_attempt
					('0:02:16', u'sqrt(((1/6)(5/6))/22)')
	part3_correct_attempt
					['0:03:01', u'sqrt(((1/6)(5/6))22)']

47 Student ID:bpandayk

	first_attempt
					2015-11-06 21:31:47
	part3_incorrect_attempt
					('0:00:37', u'sqrt((1-1/5)*22/4)')
					('0:01:47', u'sqrt((1- 4/22)*22/4)')
					('0:02:25', u'sqrt((1- 4/22)*(22/4))')
	part3_correct_attempt
					['0:14:27', u'sqrt((1- 1/4)*(22/4))']

48 Student ID:hsc052

	first_attempt
					2015-11-06 22:42:39
	part2_correct_attempt
					['0:00:00', u'24*(1/6)']
	part3_incorrect_attempt
					('0:00:00', u'4(1-(1/6))')
	part3_correct_attempt
					['0:01:52', u'sqrt(4(1-(1/6)))']

49 Student ID:xil109

	first_attempt
					2015-11-06 01:09:45
	part2_correct_attempt
					['0:06:08', u'25/6']
	part3_incorrect_attempt
					('0:07:21', u'5/6')
					('0:07:38', u'25/36')
					('0:08:05', u'1/36')
	part3_correct_attempt
					['0:14:28', u'sqrt(25*1/6*(1-1/6))']

50 Student ID:sghouse

	first_attempt
					2015-11-05 02:43:39
	part2_correct_attempt
					['0:05:58', u'23/5']
	part3_incorrect_attempt
					('0:07:48', u'sqrt(23^2/12)')
					('0:08:21', u'sqrt(18.4^2/12)')
					('0:08:31', u'sqrt(4.6^2/12)')
	part3_correct_attempt
					['18:32:48', u'sqrt(.2(.8)23)']

51 Student ID:wmiao

	first_attempt
					2015-11-05 01:13:16
	part2_correct_attempt
					['21:13:10', u'21*1/5']
	part3_incorrect_attempt
					('21:13:10', u'21*1/5')
	part3_correct_attempt
					['21:16:47', u'(0.2*(1-0.2)*21)^0.5']

52 Student ID:k3tan

	first_attempt
					2015-11-04 06:07:19
	part2_correct_attempt
					['0:04:54', u'27/6']
	part3_incorrect_attempt
					('2 days, 17:07:23', u'27*5/6*6')
					('2 days, 17:07:37', u'27*5/36')
	part3_correct_attempt
					['2 days, 17:19:49', u'sqrt(27*5/36)']

53 Student ID:lywong

	first_attempt
					2015-11-04 07:31:23
	part2_correct_attempt
					['1 day, 12:29:27', u'(1/4)*23']
	part3_incorrect_attempt
					('1 day, 16:05:44', u'Q((1/4)*23)')
					('1 day, 16:08:11', u'23*(1/4)(1-(1/4))')
	part3_correct_attempt
					['1 day, 16:09:21', u'(23*(1/4)(1-(1/4)))^(1/2)']

54 Student ID:kebao

	first_attempt
					2015-11-05 21:42:57
	part2_correct_attempt
					['0:08:58', u'26/5']
	part3_incorrect_attempt
					('0:09:13', u'sqrt(26*5*4)')
	part3_correct_attempt
					['0:11:06', u'sqrt(26*(1/5)*(4/5))']

55 Student ID:abasu

	first_attempt
					2015-11-05 03:07:09
	part2_correct_attempt
					['0:06:00', u'29(1/5)']
	part3_incorrect_attempt
					('0:34:26', u'12.2735')
					('0:59:10', u'16.8868785353')
					('2:03:10', u'8.80341')
					('2:07:15', u'12.2264194813')
	part3_correct_attempt
					['2:13:59', u'2.15406592285']

56 Student ID:sachadal

	first_attempt
					2015-11-05 20:09:44
	part2_correct_attempt
					['0:01:35', u'30*(1*(1/4)+0*(3/4))']
	part3_incorrect_attempt
					('0:06:53', u'30*((1*(1/4)+0*(3/4)) - (1*(1/4)+0*(3/4))^2)')
	part3_correct_attempt
					['0:07:17', u'sqrt(30*((1*(1/4)+0*(3/4)) - (1*(1/4)+0*(3/4))^2))']

57 Student ID:pvl001

	first_attempt
					2015-11-03 20:47:36
	part2_correct_attempt
					['0:01:22', u'21*0.2']
	part3_incorrect_attempt
					('0:04:41', u'8 - (21*0.2)')
					('0:07:25', u'(21*0.2)^2')
					('0:09:06', u'.5')
					('0:22:34', u'(.2 * (1 - 4.2)^2) + (.8 * (-1 - 4.2)^2)')
					('0:22:46', u'((.2 * (1 - 4.2)^2) + (.8 * (-1 - 4.2)^2))/21')
					('0:24:00', u'((.2 * (1 - 4.2)^2) + (.8 * (-1 - 4.2)^2))/sqrt(21)')
					('0:26:59', u'sqrt(((.2 * (1 - 4.2)^2) + (.8 * (-1 - 4.2)^2)))')
					('0:27:12', u'sqrt(((.2 * (1 - 4.2)^2) + (.8 * (-1 - 4.2)^2)))/sqrt(21)')
					('0:34:56', u'8/21')
					('0:35:17', u'sqrt(8/21)')
					('0:40:32', u'(1-4.2)^2')
					('0:40:47', u'sqrt((1-4.2)^2)')
					('0:44:30', u'((1 - 4.2)^2 + (2 - 4.2)^2 + (3 - 4.2)^2 + (4 - 4.2)^2 + (5 - 4.2)^2 + (6 - 4.2)^2 + (7 - 4.2)^2 + (8 - 4.2)^2 + (9 - 4.2)^2 + (10 - 4.2)^2 + (11 - 4.2)^2 + (12 - 4.2)^2 + (13 - 4.2)^2 + (14 - 4.2)^2 + (15 - 4.2)^2 + (16 - 4.2)^2 + (17 - 4.2)^2 + (18 - 4.2)^2 + (19 - 4.2)^2 + (20 - 4.2)^2 + (21 - 4.2)^2) / 21')
					('0:45:17', u'sqrt(((1 - 4.2)^2 + (2 - 4.2)^2 + (3 - 4.2)^2 + (4 - 4.2)^2 + (5 - 4.2)^2 + (6 - 4.2)^2 + (7 - 4.2)^2 + (8 - 4.2)^2 + (9 - 4.2)^2 + (10 - 4.2)^2 + (11 - 4.2)^2 + (12 - 4.2)^2 + (13 - 4.2)^2 + (14 - 4.2)^2 + (15 - 4.2)^2 + (16 - 4.2)^2 + (17 - 4.2)^2 + (18 - 4.2)^2 + (19 - 4.2)^2 + (20 - 4.2)^2 + (21 - 4.2)^2) / 21)')
					('0:46:57', u'4.2/21')
					('0:47:30', u'sqrt(4.2)')
					('0:52:58', u'sqrt((.20*.80)/21)')
	part3_correct_attempt
					['6:49:47', u'sqrt(21 * .2 * .8)']

58 Student ID:jcj006

	first_attempt
					2015-11-04 06:04:21
	part2_correct_attempt
					['-1 day, 23:59:50', u'29/5']
	part3_incorrect_attempt
					('16:22:30', u'29*.2*.8')
	part3_correct_attempt
					['16:23:19', u'sqrt(29*.2*.8)']

59 Student ID:mbl003

	first_attempt
					2015-11-05 21:04:59
	part2_correct_attempt
					['0:08:37', u'24/6']
	part3_incorrect_attempt
					('0:10:58', u'(1/6-24/6)^2')
					('0:11:19', u'sqrt((1/6-24/6)^2*24)')
					('23:59:55', u'sqrt((24/6-1/6)*24)')
	part3_correct_attempt
					['1 day, 0:01:03', u'sqrt(1/6(1-1/6)24)']

60 Student ID:bakang

	first_attempt
					2015-11-05 08:51:51
	part2_correct_attempt
					['0:15:55', u'1/6*21']
	part3_incorrect_attempt
					('0:19:26', u'sqrt((1/36*21)+(1/6*21)^2)')
					('0:27:48', u'1/6*21')
					('0:33:20', u'sqrt(((5/6)^2+5*(1/6)^2)*21)')
	part3_correct_attempt
					['8:04:15', u'sqrt(1/6*(5/6)*21)']

61 Student ID:ksmurlo

	first_attempt
					2015-11-05 06:45:24
	part2_correct_attempt
					['0:03:47', u'29*.25']
	part3_incorrect_attempt
					('0:50:00', u'sqrt((49*29)/29)')
	part3_correct_attempt
					['8:23:07', u'sqrt(29*.25*.75)']

62 Student ID:ttimmons

	first_attempt
					2015-11-03 18:36:16
	part2_correct_attempt
					['0:09:13', u'(1/4)*30']
	part3_incorrect_attempt
					('0:10:19', u'sqrt((1/4)*30^2-[(1/4)*30]^2)')
					('0:11:57', u'sqrt((1/4)*30^2-[(1/4)*30]^2)')
					('0:12:15', u'15-7.5')
					('0:12:34', u'sqrt((1/4)*30^2-[(1/4)*30]^2)')
					('0:19:37', u'30*(1/4)*(1-(1/4))')
	part3_correct_attempt
					['0:19:47', u'sqrt(30*(1/4)*(1-(1/4)))']

63 Student ID:jnatale

	first_attempt
					2015-11-05 02:19:36
	part2_correct_attempt
					['0:00:41', u'23/4']
	part3_incorrect_attempt
					('0:01:41', u'sqrt(23/(1/4))')
	part3_correct_attempt
					['0:04:44', u'sqrt(23*(1/4)*(1-.25))']

64 Student ID:jblynch

	first_attempt
					2015-11-04 21:04:35
	part2_correct_attempt
					['0:00:57', u'(1/5)*20']
	part3_incorrect_attempt
					('0:01:39', u'sqrt((1/5)*20^2 - 4^2)')
					('0:03:01', u'(1/5)(20-4)')
	part3_correct_attempt
					['9:13:39', u'sqrt((1/5)(20)(4/5))']

65 Student ID:nnh002

	first_attempt
					2015-11-05 05:08:53
	part2_correct_attempt
					['0:01:20', u'0.2*22']
	part3_incorrect_attempt
					('1 day, 3:52:43', u'sqrt((1/5)^12*(1-(1/5)^12)*22)')
					('1 day, 4:00:26', u'sqrt((12/22)^12*(1-(12/22)^12)*22)')
					('1 day, 4:10:13', u'sqrt((12/22)*(1-(12/22))*22)')
					('1 day, 15:57:51', u'sqrt((1/5)^12*(1-((4/5)^12))*22)')
					('1 day, 15:58:15', u'sqrt((1/5)^22*(1-((4/5)^22))*22)')
					('1 day, 15:58:41', u'sqrt((1/5)*(1-((4/5)))*22)')
	part3_correct_attempt
					['1 day, 15:59:05', u'sqrt((1/5)*(4/5)*22)']

66 Student ID:agian

	first_attempt
					2015-11-07 00:29:52
	part2_correct_attempt
					['0:13:31', u'30/4']
	part3_incorrect_attempt
					('0:14:23', u'sqrt(7.5)')
	part3_correct_attempt
					['0:16:32', u'sqrt((30-7.5)/4)']

67 Student ID:tol003

	first_attempt
					2015-11-03 19:59:02
	part2_correct_attempt
					['0:05:33', u'28*(1/5)']
	part3_incorrect_attempt
					('0:12:46', u'28*(21.16*(1/5))')
					('0:19:32', u'28*[1-(28*1/5)]^2')
					('0:21:39', u'sqrt(28*[1-(28*(1/5))]^2)')
					('0:31:59', u'5.07543')
					('0:38:16', u'5.075431016')
	part3_correct_attempt
					['0:41:09', u'sqrt(28*(1/5)*(1-(1/5)))']

68 Student ID:aakumar

	first_attempt
					2015-11-05 03:13:47
	part2_correct_attempt
					['0:12:20', u'23(1/6)']
	part3_incorrect_attempt
					('1:29:41', u'15.077689')
					('1:47:28', u'6.913')
					('2:03:35', u'31.9133')
	part3_correct_attempt
					['2:09:35', u'(23*5/36)^(1/2)']

69 Student ID:yeh013

	first_attempt
					2015-11-05 03:50:09
	part2_correct_attempt
					['2:26:57', u'6']
	part3_incorrect_attempt
					('2:47:35', u'36-24/16')
					('2:47:48', u'34.5^(1/2)')
					('2:58:09', u'108^(1/2)')
					('3:13:50', u'75^(1/2)')
	part3_correct_attempt
					['3:17:42', u'4.5^(1/2)']

70 Student ID:asetters

	first_attempt
					2015-11-05 20:08:55
	part2_correct_attempt
					['0:00:00', u'21/6']
	part3_incorrect_attempt
					('0:00:39', u'(21/6)^2 - 21/6')
	part3_correct_attempt
					['0:04:10', u'sqrt(21/6*(5/6))']

71 Student ID:ppanourg

	first_attempt
					2015-11-06 09:57:58
	part2_correct_attempt
					['9:27:31', u'28/5']
	part3_incorrect_attempt
					('9:29:09', u'(28/5)(1-1/5)')
	part3_correct_attempt
					['9:30:01', u'sqrt((28/5)(1-1/5))']

72 Student ID:ksrijong

	first_attempt
					2015-11-06 20:22:16
	part2_correct_attempt
					['0:03:45', u'(1/6)*25']
	part3_incorrect_attempt
					('0:05:33', u'(1/6)*25')
	part3_correct_attempt
					['0:07:53', u'sqrt((1/6)(5/6)(25))']

73 Student ID:yhhan

	first_attempt
					2015-11-07 00:05:22
	part2_correct_attempt
					['0:00:38', u'28/4']
	part3_incorrect_attempt
					('0:03:06', u'.25')
					('0:03:24', u'.5')
	part3_correct_attempt
					['0:05:10', u'(.25*.75*28)^.5']

74 Student ID:j2phung

	first_attempt
					2015-11-05 09:45:24
	part2_correct_attempt
					['0:01:53', u'30/4']
	part3_incorrect_attempt
					('0:17:47', u'30/4')
	part3_correct_attempt
					['0:34:15', u'(30*(1/4)*(3/4))^(1/2)']

75 Student ID:cagatep

	first_attempt
					2015-11-05 07:44:14
	part2_correct_attempt
					['0:01:39', u'.2 * 21']
	part3_incorrect_attempt
					('0:02:08', u'Phi(.2 * 21)')
					('0:23:58', u'Q(.2 * 21)')
	part3_correct_attempt
					['1 day, 11:45:41', u'sqrt(.2 * .8 * 21)']

76 Student ID:hmnaing

	first_attempt
					2015-11-06 18:32:06
	part2_correct_attempt
					['3:41:28', u'26/4']
	part3_incorrect_attempt
					('3:45:21', u'sqrt(26/12)')
					('3:49:13', u'sqrt(26*25/4)')
					('3:51:05', u'sqrt(0.25*3/4/4)')
					('3:52:03', u'sqrt(0.25*0.75/26)')
	part3_correct_attempt
					['3:52:15', u'sqrt(0.25*0.75*26)']

77 Student ID:tjke

	first_attempt
					2015-11-06 17:13:34
	part2_correct_attempt
					['0:00:00', u'24*1/6']
	part3_incorrect_attempt
					('0:01:00', u'sqrt(1/6*24^2 - (1/6*24)^2)')
	part3_correct_attempt
					['0:04:00', u'sqrt(1/6*(1-1/6)*24)']

78 Student ID:klala

	first_attempt
					2015-11-05 06:24:05
	part2_correct_attempt
					['0:09:26', u'28 * (1/6)']
	part3_incorrect_attempt
					('0:10:50', u'(1/6) * (5/6)')
	part3_correct_attempt
					['0:13:03', u'sqrt(28*(1/6)*(5/6))']

79 Student ID:asp025

	first_attempt
					2015-11-06 22:08:56
	part2_correct_attempt
					['0:43:48', u'24/6']
	part3_incorrect_attempt
					('0:45:51', u'24(1/6)(1-1/6)')
	part3_correct_attempt
					['0:49:11', u'[24(1/6)(1-1/6)]^(1/2)']

80 Student ID:dlgoldbe

	first_attempt
					2015-11-05 06:23:46
	part2_correct_attempt
					['0:05:09', u'22/4']
	part3_incorrect_attempt
					('0:06:37', u'1/(sqrt(22-13))')
					('0:07:37', u'sqrt((22/4)*22-13)')
	part3_correct_attempt
					['0:09:26', u'sqrt((22/4)*(1-(1/4)))']

81 Student ID:yig015

	first_attempt
					2015-11-05 10:50:36
	part2_correct_attempt
					['0:09:09', u'30/4']
	part3_incorrect_attempt
					('0:11:27', u'0.0585207071')
	part3_correct_attempt
					['0:31:26', u'2.371708245']

82 Student ID:t2shin

	first_attempt
					2015-11-05 21:33:48
	part2_correct_attempt
					['0:04:23', u'1/4*24']
	part3_incorrect_attempt
					('0:05:34', u'0.1')
					('0:07:33', u'sqrt(((4-6)^2)/24)')
					('0:08:50', u'sqrt(((1-6)^2)/24)')
					('0:11:07', u'0.5')
					('0:11:15', u'0.4')
					('0:13:25', u'sqrt(24*3)')
	part3_correct_attempt
					['0:13:43', u'sqrt(24*1/4*3/4)']

83 Student ID:vsamant

	first_attempt
					2015-11-04 00:59:19
	part2_correct_attempt
					['0:01:18', u'27/6']
	part3_incorrect_attempt
					('0:14:22', u'(27/6)^(1/2)')
					('22:22:01', u'(27/6)^(1/2)')
	part3_correct_attempt
					['1 day, 2:55:53', u'((1-1/6)*(27/6))^(1/2)']

84 Student ID:fichoi

	first_attempt
					2015-11-04 18:14:52
	part2_correct_attempt
					['0:50:42', u'27/6']
	part3_incorrect_attempt
					('0:52:03', u'1.5')
					('0:52:57', u'27-4.5')
					('0:56:42', u'21/162')
					('0:57:32', u'5.196')
					('1:21:53', u'0.3727')
					('1:25:35', u'0.04137')
	part3_correct_attempt
					['6:12:31', u'sqrt(27 * 1/6(1 - 1/6))']

85 Student ID:rohan

	first_attempt
					2015-11-07 00:10:27
	part3_incorrect_attempt
					('0:02:23', u'sqrt(15/28(1-15/28)4)')

86 Student ID:any027

	first_attempt
					2015-11-01 20:36:42
	part2_correct_attempt
					['0:02:37', u'27/6']
	part3_incorrect_attempt
					('0:07:40', u'sqrt (( ((0-4.5)^2) + ((1-4.5)^2) + ((2-4.5)^2) + ((3-4.5)^2) + ((4-4.5)^2) + ((5-4.5)^2) + ((6-4.5)^2) +((7-4.5)^2) + ((8-4.5)^2) + ((9-4.5)^2) + ((10-4.5)^2) + ((11-4.5)^2) + ((12-4.5)^2) + ((13-4.5)^2) + ((14-4.5)^2) +  ((15-4.5)^2) + ((16-4.5)^2) + ((17-4.5)^2) + ((18-4.5)^2) + ((19-4.5)^2) + ((20-4.5)^2) + ((21-4.5)^2) + ((22-4.5)^2) + ((23-4.5)^2) + ((24-4.5)^2) +((25-4.5)^2) + ((26-4.5)^2) + ((27-4.5)^2) ) / 27 )')
					('0:09:17', u'sqrt (( ((0-4.5)^2) + ((1-4.5)^2) + ((2-4.5)^2) + ((3-4.5)^2) + ((4-4.5)^2) + ((5-4.5)^2) + ((6-4.5)^2) +((7-4.5)^2) + ((8-4.5)^2) + ((9-4.5)^2) + ((10-4.5)^2) + ((11-4.5)^2) + ((12-4.5)^2) + ((13-4.5)^2) + ((14-4.5)^2) + ((15-4.5)^2) + ((16-4.5)^2) + ((17-4.5)^2) + ((18-4.5)^2) + ((19-4.5)^2) + ((20-4.5)^2) + ((21-4.5)^2) + ((22-4.5)^2) + ((23-4.5)^2) + ((24-4.5)^2) +((25-4.5)^2) + ((26-4.5)^2) + ((27-4.5)^2) ) / 28 )')
					('0:20:34', u'sqrt (( ((0/6-4.5)^2) + ((1/6-4.5)^2) + ((2/6-4.5)^2) + ((3/6-4.5)^2) + ((4/6-4.5)^2) + ((5/6-4.5)^2) + ((6/6-4.5)^2) +((7/6-4.5)^2) + ((8/6-4.5)^2) + ((9/6-4.5)^2) + ((10/6-4.5)^2) + ((11/6-4.5)^2) + ((12/6-4.5)^2) + ((13/6-4.5)^2) + ((14/6-4.5)^2) + ((15/6-4.5)^2) + ((16/6-4.5)^2) + ((17/6-4.5)^2) + ((18/6-4.5)^2) + ((19/6-4.5)^2) + ((20/6-4.5)^2) + ((21/6-4.5)^2) + ((22/6-4.5)^2) + ((23/6-4.5)^2) + ((24/6-4.5)^2) +((25/6-4.5)^2) + ((26/6-4.5)^2) + ((27/6-4.5)^2) ) / 28 )')
					('0:22:18', u'1/6')
					('0:38:47', u'sqrt (( ((0-4.5)^2) + ((1-4.5)^2) + ((2-4.5)^2) + ((3-4.5)^2) + ((4-4.5)^2) + ((5-4.5)^2) + ((6-4.5)^2) +((7-4.5)^2) + ((8-4.5)^2) + ((9-4.5)^2) + ((10-4.5)^2) + ((11-4.5)^2) + ((12-4.5)^2) + ((13-4.5)^2) + ((14-4.5)^2) + ((15-4.5)^2) + ((16-4.5)^2) + ((17-4.5)^2) + ((18-4.5)^2) + ((19-4.5)^2) + ((20-4.5)^2) + ((21-4.5)^2) + ((22-4.5)^2) + ((23-4.5)^2) + ((24-4.5)^2) +((25-4.5)^2) + ((26-4.5)^2) + ((27-4.5)^2) ) / 28 )')
					('1:18:30', u'sqrt (( ((27/1-4.5)^2) + ((2-4.5)^2) + ((3-4.5)^2) + ((4-4.5)^2) + ((5-4.5)^2) + ((6-4.5)^2) +((7-4.5)^2) + ((8-4.5)^2) + ((9-4.5)^2) + ((10-4.5)^2) + ((11-4.5)^2) + ((12-4.5)^2) + ((13-4.5)^2) + ((14-4.5)^2) + ((15-4.5)^2) + ((16-4.5)^2) + ((17-4.5)^2) + ((18-4.5)^2) + ((19-4.5)^2) + ((20-4.5)^2) + ((21-4.5)^2) + ((22-4.5)^2) + ((23-4.5)^2) + ((24-4.5)^2) +((25-4.5)^2) + ((26-4.5)^2) + ((27-4.5)^2) ) / 28 )')
					('1:20:14', u'sqrt (( ((27/1-4.5)^2) + ((27/2-4.5)^2) + ((27/3-4.5)^2) + ((27/4-4.5)^2) + ((27/5-4.5)^2) + ((27/6-4.5)^2) +((27/7-4.5)^2) + ((27/8-4.5)^2) + ((27/9-4.5)^2) + ((27/10-4.5)^2) + ((27/11-4.5)^2) + ((27/12-4.5)^2) + ((27/13-4.5)^2) + ((27/14-4.5)^2) + ((27/15-4.5)^2) + ((27/16-4.5)^2) + ((27/17-4.5)^2) + ((27/18-4.5)^2) + ((27/19-4.5)^2) + ((27/20-4.5)^2) + ((27/21-4.5)^2) + ((27/22-4.5)^2) + ((27/23-4.5)^2) + ((27/24-4.5)^2) +((27/25-4.5)^2) + ((27/26-4.5)^2) + ((27/27-4.5)^2) ) / 27 )')
					('1:23:02', u'sqrt (( ((0-4.5)^2) + ((1-4.5)^2) + ((2-4.5)^2) + ((3-4.5)^2) + ((4-4.5)^2) + ((5-4.5)^2) + ((6-4.5)^2) +((7-4.5)^2) + ((8-4.5)^2) + ((9-4.5)^2) + ((10-4.5)^2) + ((11-4.5)^2) + ((12-4.5)^2) + ((13-4.5)^2) + ((14-4.5)^2) + ((15-4.5)^2) + ((16-4.5)^2) + ((17-4.5)^2) + ((18-4.5)^2) + ((19-4.5)^2) + ((20-4.5)^2) + ((21-4.5)^2) + ((22-4.5)^2) + ((23-4.5)^2) + ((24-4.5)^2) +((25-4.5)^2) + ((26-4.5)^2) + ((27-4.5)^2) ) / 28 )')
					('1:26:17', u'27/11')
	part3_correct_attempt
					['1:32:21', u'sqrt( (27*1/6)* (1-1/6) )']

87 Student ID:jdeon

	first_attempt
					2015-11-05 20:09:34
	part2_correct_attempt
					['-2 days, 8:52:28', u'7']
	part3_incorrect_attempt
					('-2 days, 9:03:53', u'1/7')
					('-2 days, 9:05:53', u'(1/4)*(3/4)')
	part3_correct_attempt
					['-2 days, 9:15:39', u'2.29128']

88 Student ID:j6quach

	first_attempt
					2015-11-05 09:30:45
	part2_correct_attempt
					['1:20:29', u'26*1/5']
	part3_incorrect_attempt
					('1:20:29', u'5.2/4')
	part3_correct_attempt
					['1:26:23', u'sqrt(26*.2*.8)']

89 Student ID:syc078

	first_attempt
					2015-11-05 03:08:01
	part2_correct_attempt
					['22:55:37', u'(1/4)(28)']
	part3_incorrect_attempt
					('22:56:27', u'13-7')
					('22:56:43', u'((13-7)^2)/7')
	part3_correct_attempt
					['23:03:04', u'sqrt(7*(1-0.25))']

90 Student ID:jhc010

	first_attempt
					2015-11-06 10:34:37
	part2_correct_attempt
					['0:00:53', u'25/4']
	part3_incorrect_attempt
					('0:01:17', u'25/4^2')
					('0:02:11', u'25/16')
					('0:02:18', u'25/4*2')
					('0:03:04', u'(1-4/25)/(4/25)^2')
					('0:04:53', u'((1-4/25)/(4/25)^2)^2')
					('0:09:07', u'sqrt((1-.5)/(.5^2))')
					('0:09:53', u'sqrt((1-4/25)/((4/25)^2))')
					('0:10:58', u'sqrt((1-1/4)/((1/4)^2))')
					('0:12:02', u'sqrt(-1*(1-25/4)/((25/4)^2))')
					('0:13:05', u'sqrt((1-1/4)/((1/4)^2))')
					('0:13:27', u'sqrt((1-1/4)/((1/4)^2))')
					('0:17:15', u'sqrt((1-1/4)/((1/4)^2))')
					('0:17:40', u'sqrt((25-25/4)/((25/4)^2))')
					('0:18:56', u'sqrt((1-4/25)/((4/25)^2))')
	part3_correct_attempt
					['0:24:34', u'sqrt(.25(.75)25)']

91 Student ID:agarango

	first_attempt
					2015-11-06 20:14:19
	part2_correct_attempt
					['0:18:35', u'21*(1/6)']
	part3_incorrect_attempt
					('0:19:58', u'sqrt((5*21)/6)')
					('0:20:42', u'sqrt((5*21)/21)')
					('0:21:06', u'sqrt((5/6)/21)')
					('3:26:05', u'sqrt((5*21)/6)')
	part3_correct_attempt
					['3:28:35', u'sqrt(5*21)/6']

92 Student ID:twsalim

	first_attempt
					2015-11-06 02:09:27
	part2_correct_attempt
					['0:00:00', u'20/6']
	part3_incorrect_attempt
					('0:12:31', u'7.45356')
					('0:22:55', u'21.615')
	part3_correct_attempt
					['0:32:20', u'5/3']

93 Student ID:achinn

	first_attempt
					2015-11-03 21:26:44
	part2_correct_attempt
					['0:00:00', u'5']
	part3_incorrect_attempt
					('0:29:35', u'sqrt(64.75)')
					('0:30:41', u'sqrt(20*0.5)')
	part3_correct_attempt
					['0:36:02', u'sqrt(5*0.75)']

94 Student ID:mcatozzi

	first_attempt
					2015-11-03 19:47:20
	part2_correct_attempt
					['0:20:14', u'28/5']
	part3_incorrect_attempt
					('0:30:44', u'((28-5.6)^2) +((27-5.6)^2) +((26-5.6)^2) +((25-5.6)^2) +((24-5.6)^2) +((23-5.6)^2) +((22-5.6)^2) +((21-5.6)^2) +((20-5.6)^2) +((19-5.6)^2) +((18-5.6)^2) +((17-5.6)^2) +((16-5.6)^2) +((15-5.6)^2) +((14-5.6)^2) +((13-5.6)^2) +((12-5.6)^2) +((11-5.6)^2) +((10-5.6)^2) +((9-5.6)^2) +((8-5.6)^2) +((7-5.6)^2) +((6-5.6)^2) +((5-5.6)^2) +((4-5.6)^2) +((3-5.6)^2) +((2-5.6)^2) +((1-5.6)^2)')
					('0:33:15', u'sqrt((((28-5.6)^2) +((27-5.6)^2) +((26-5.6)^2) +((25-5.6)^2) +((24-5.6)^2) +((23-5.6)^2) +((22-5.6)^2) +((21-5.6)^2) +((20-5.6)^2) +((19-5.6)^2) +((18-5.6)^2) +((17-5.6)^2) +((16-5.6)^2) +((15-5.6)^2) +((14-5.6)^2) +((13-5.6)^2) +((12-5.6)^2) +((11-5.6)^2) +((10-5.6)^2) +((9-5.6)^2) +((8-5.6)^2) +((7-5.6)^2) +((6-5.6)^2) +((5-5.6)^2) +((4-5.6)^2) +((3-5.6)^2) +((2-5.6)^2) +((1-5.6)^2)+((-5.6)^2))/28 )')
					('0:36:07', u'sqrt((((28-5.6)^2) +((27-5.6)^2) +((26-5.6)^2) +((25-5.6)^2) +((24-5.6)^2) +((23-5.6)^2) +((22-5.6)^2) +((21-5.6)^2) +((20-5.6)^2) +((19-5.6)^2) +((18-5.6)^2) +((17-5.6)^2) +((16-5.6)^2) +((15-5.6)^2) +((14-5.6)^2) +((13-5.6)^2) +((12-5.6)^2) +((11-5.6)^2) +((10-5.6)^2) +((9-5.6)^2) +((8-5.6)^2) +((7-5.6)^2) +((6-5.6)^2) +((5-5.6)^2) +((4-5.6)^2) +((3-5.6)^2) +((2-5.6)^2) +((1-5.6)^2)+((-5.6)^2))/29 )')
					('0:38:45', u'sqrt((((28-5.6)^2) +((27-5.6)^2) +((26-5.6)^2) +((25-5.6)^2) +((24-5.6)^2) +((23-5.6)^2) +((22-5.6)^2) +((21-5.6)^2) +((20-5.6)^2) +((19-5.6)^2) +((18-5.6)^2) +((17-5.6)^2) +((16-5.6)^2) +((15-5.6)^2) +((14-5.6)^2) +((13-5.6)^2) +((12-5.6)^2) +((11-5.6)^2) +((10-5.6)^2) +((9-5.6)^2) +((8-5.6)^2) +((7-5.6)^2) +((6-5.6)^2) +((5-5.6)^2) +((4-5.6)^2) +((3-5.6)^2) +((2-5.6)^2) +((1-5.6)^2)/28) )')
					('0:39:19', u'sqrt((((28-5.6)^2) +((27-5.6)^2) +((26-5.6)^2) +((25-5.6)^2) +((24-5.6)^2) +((23-5.6)^2) +((22-5.6)^2) +((21-5.6)^2) +((20-5.6)^2) +((19-5.6)^2) +((18-5.6)^2) +((17-5.6)^2) +((16-5.6)^2) +((15-5.6)^2) +((14-5.6)^2) +((13-5.6)^2) +((12-5.6)^2) +((11-5.6)^2) +((10-5.6)^2) +((9-5.6)^2) +((8-5.6)^2) +((7-5.6)^2) +((6-5.6)^2) +((5-5.6)^2) +((4-5.6)^2) +((3-5.6)^2) +((2-5.6)^2) +((1-5.6)^2))/28 )')
					('0:39:39', u'12.2')
					('0:39:47', u'11.2')
	part3_correct_attempt
					['0:55:37', u'sqrt(28*(1/5)*(4/5))']

95 Student ID:aadhakal

	first_attempt
					2015-11-05 23:02:48
	part2_correct_attempt
					['0:00:00', u'4.16']
	part3_incorrect_attempt
					('0:00:00', u'sqrt(25/6)')
					('0:00:36', u'sqrt(21.84/6)')
	part3_correct_attempt
					['0:00:48', u'sqrt(20.84/6)']

96 Student ID:acs008

	first_attempt
					2015-11-05 16:06:10
	part2_correct_attempt
					['5:26:25', u'1/5*29']
	part3_incorrect_attempt
					('5:26:54', u'12-5.8')
					('5:27:03', u'(12-5.8)')
					('5:31:15', u'1.067')
					('5:31:25', u'1.069')
					('5:32:22', u'Q(12)')
					('5:35:35', u'sqrt(24*1/5*4/5)')
					('5:35:47', u'sqrt(24*4/5)')
					('5:36:16', u'sqrt(24*4/5*1/5)')
					('5:36:27', u'12*sqrt(24*4/5*1/5)')
					('5:38:09', u'1-Q(12)')
					('5:38:16', u'Q(12)')
					('5:38:23', u'Q(12/29)')
					('5:38:29', u'1-Q(12/29)')
					('5:38:38', u'1-Q(1/5)')
					('5:38:44', u'12*Q(1/5)')
	part3_correct_attempt
					['5:40:29', u'sqrt(29*1/5*4/5)']

97 Student ID:dpereira

	first_attempt
					2015-10-30 22:16:13
	part2_correct_attempt
					['6 days, 0:19:27', u'20/4']
	part3_incorrect_attempt
					('6 days, 0:24:07', u'sqrt(100-25)')
	part3_correct_attempt
					['6 days, 0:38:43', u'sqrt(.25*.75*20)']

98 Student ID:haliew

	first_attempt
					2015-11-06 23:10:07
	part2_correct_attempt
					['0:43:58', u'27/5']
	part3_incorrect_attempt
					('0:46:31', u'(13-(27/5))^2')
					('0:53:49', u'13-5.4/sqrt(27)')
					('0:54:00', u'13-5.4')
	part3_correct_attempt
					['0:56:11', u'sqrt((1/5)(4/5)27)']

99 Student ID:lahawkin

	first_attempt
					2015-11-04 17:21:24
	part2_correct_attempt
					['0:01:32', u'30*.25']
	part3_incorrect_attempt
					('0:02:42', u'((30*.25)^2-(30*(.25^2)))^(1/2)')
					('0:03:37', u'((30*(.25^2))-(30*(.25)^2))^(1/2)')
					('1 day, 2:19:07', u'((((30*.25)-.75)^2)/30)^(1/2)')
					('1 day, 2:21:28', u'((((30*.25)-11)^2)/30)^(1/2)')
					('1 day, 2:24:40', u'(30*.25)*(.75)')
	part3_correct_attempt
					['1 day, 2:24:56', u'((30*.25)*(.75))^(1/2)']

100 Student ID:z2tan

	first_attempt
					2015-11-02 05:28:45
	part2_correct_attempt
					['0:01:04', u'26/5']
	part3_incorrect_attempt
					('0:03:23', u'26-5.2')
					('0:08:31', u'(5.2^2+4.2^2+3.2^2+2.2^2+1.2^2+0.2^2+0.8^2+1.8^2+2.8^2+3.8^2+4.8^2+5.8^2+6.8^2+7.8^2+8.8^2+9.8^2+10.8^2+11.8^2+12.8^2+13.8^2+14.8^2+15.8^2+16.8^2+17.8^2+18.8^2+19.8^2+20.8^2)^0.5')
					('0:14:16', u'((5.2^2+4.2^2+3.2^2+2.2^2+1.2^2+0.2^2+0.8^2+1.8^2+2.8^2+3.8^2+4.8^2+5.8^2+6.8^2+7.8^2+8.8^2+9.8^2+10.8^2+11.8^2+12.8^2+13.8^2+14.8^2+15.8^2+16.8^2+17.8^2+18.8^2+19.8^2+20.8^2)/27)^0.5')
	part3_correct_attempt
					['0:27:53', u'(26*0.8*0.2)^0.5']

101 Student ID:kquong

	first_attempt
					2015-11-04 23:52:13
	part2_correct_attempt
					['0:00:00', u'25/6']
	part3_incorrect_attempt
					('0:00:00', u'125/36')
	part3_correct_attempt
					['0:00:56', u'sqrt(125/36)']

102 Student ID:vasharma

	first_attempt
					2015-11-04 19:06:11
	part2_correct_attempt
					['0:02:58', u'28*.2']
	part3_incorrect_attempt
					('0:03:14', u'(28*.2)(1-.2)')
	part3_correct_attempt
					['0:04:22', u'sqrt((28*.2)(1-.2))']

103 Student ID:c3chung

	first_attempt
					2015-11-06 11:03:55
	part2_correct_attempt
					['0:02:16', u'1/6(21)']
	part3_incorrect_attempt
					('0:03:35', u'3.5/20')
	part3_correct_attempt
					['0:12:04', u'sqrt(1/6(5/6)(21))']

104 Student ID:ajvanega

	first_attempt
					2015-11-05 18:54:48
	part2_correct_attempt
					['7:09:10', u'(1/4)30']
	part3_incorrect_attempt
					('7:09:40', u'(12-7.5)')
					('7:10:03', u'((12-7.5)^2)/30')
					('7:10:19', u'((12-7.5)^2)4')
					('7:10:29', u'((12-7.5)^2)/4')
					('7:10:41', u'((12-7.5)^2)/12')
					('7:11:10', u'((12-7.5)^2)')
					('7:17:21', u'sqrt(30*.24*7.5)')
					('7:17:43', u'sqrt(30*.25*7.5)')
	part3_correct_attempt
					['7:18:34', u'sqrt((30/4)*(.75))']

105 Student ID:zig006

	first_attempt
					2015-11-04 21:24:02
	part2_correct_attempt
					['0:00:21', u'7']
	part3_incorrect_attempt
					('0:08:19', u'1/2')
	part3_correct_attempt
					['0:34:12', u'((21)^0.5)/2']

106 Student ID:jmiclat

	first_attempt
					2015-11-06 09:04:02
	part2_correct_attempt
					['14:29:16', u'29*(1/4)']
	part3_incorrect_attempt
					('14:30:19', u'sqrt([(1/4)(3/4)]/29)')
	part3_correct_attempt
					['14:30:51', u'sqrt([(1/4)(3/4)]*29)']

107 Student ID:sthapa

	first_attempt
					2015-11-07 00:03:07
	part2_correct_attempt
					['0:25:33', u'26/6']
	part3_incorrect_attempt
					('0:29:34', u'sqrt((4.3*6)/6)')
					('0:31:21', u'2.08')
					('0:33:23', u'0.84')
					('0:33:35', u'0.849')
					('0:34:49', u'0.84950966249')
					('0:42:56', u'sqrt((26/5)/6)')
	part3_correct_attempt
					['0:43:22', u'sqrt((5*4.33)/6)']

108 Student ID:mjethani

	first_attempt
					2015-11-06 02:05:57
	part2_correct_attempt
					['22:51:31', u'30/6']
	part3_incorrect_attempt
					('22:51:31', u'sqrt((1-(1/180)))')

109 Student ID:kgrozav

	first_attempt
					2015-11-05 20:31:16
	part2_correct_attempt
					['0:12:04', u'26 * (1/4)']
	part3_incorrect_attempt
					('0:15:29', u'4.875')
	part3_correct_attempt
					['0:16:16', u'2.207940']

110 Student ID:arvenega

	first_attempt
					2015-11-06 23:36:36
	part2_correct_attempt
					['0:00:59', u'29/5']
	part3_incorrect_attempt
					('0:00:59', u'29/5')
	part3_correct_attempt
					['0:11:40', u'sqrt((29/5)*(1-(1/5)))']












## Part 4

### (38) Mistake Group redirect of size 38




### (28) Mistake Group ['R.1'] of size 28
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(12-24*1/4)/[sqrt(24/4*(1-1/4))]	|(24-12)/((24(1/4)(1-1/4))^(1/2))	|[('R.1', 2.1213203435596424, u'sqrt(24/4*(1-1/4))', u'(24(1/4)(1-1/4))^(1/2)')]	|
|1	|(9-28*1/5)/[sqrt(28/5*(1-1/5))]	|(28-5.6)/2.1166	|[('R.1', 2.116601048851672, u'sqrt(28/5*(1-1/5))', u'2.1166')]	|
|2	|(8-22*1/5)/[sqrt(22/5*(1-1/5))]	|(5-4.4)/[sqrt(4.4*(1-(1/5)))]	|[('R.1', 1.876166303929372, u'sqrt(22/5*(1-1/5))', u'sqrt(4.4*(1-(1/5)))')]	|
|3	|(9-28*1/5)/[sqrt(28/5*(1-1/5))]	|2.9/(2.1166)	|[('R.1', 2.116601048851672, u'sqrt(28/5*(1-1/5))', u'2.1166')]	|
|4	|(9-28*1/5)/[sqrt(28/5*(1-1/5))]	|2.9/4.48^(1/2)	|[('R.1', 2.116601048851672, u'sqrt(28/5*(1-1/5))', u'4.48^(1/2)')]	|
|5	|(9-28*1/5)/[sqrt(28/5*(1-1/5))]	|3.9/4.48^(1/2)	|[('R.1', 2.116601048851672, u'sqrt(28/5*(1-1/5))', u'4.48^(1/2)')]	|
|6	|(9-28*1/5)/[sqrt(28/5*(1-1/5))]	|(8.5-5.6)/4.48^(1/2)	|[('R.1', 2.116601048851672, u'sqrt(28/5*(1-1/5))', u'4.48^(1/2)')]	|
|7	|(9-28*1/5)/[sqrt(28/5*(1-1/5))]	|(9.5-5.6)/4.48^(1/2)	|[('R.1', 2.116601048851672, u'sqrt(28/5*(1-1/5))', u'4.48^(1/2)')]	|
|8	|(9-28*1/5)/[sqrt(28/5*(1-1/5))]	|(8.5-5.6)/2.1166	|[('R.1', 2.116601048851672, u'sqrt(28/5*(1-1/5))', u'2.1166')]	|
|9	|(11-29*1/5)/[sqrt(29/5*(1-1/5))]	|29/5((29*4/25)^.5)	|[('R.1', 2.1540659228538015, u'sqrt(29/5*(1-1/5))', u'(29*4/25)^.5)')]	|
|10	|(7-23*1/6)/[sqrt(23/6*(1-1/6))]	|[(23/6)/(23*5/36)^(1/2)]	|[('R.1', 1.7873008824606014, u'sqrt(23/6*(1-1/6))', u'(23*5/36)^(1/2)')]	|
|11	|(10-24*1/4)/[sqrt(24/4*(1-1/4))]	|2*4.5^(1/2)	|[('R.1', 2.1213203435596424, u'sqrt(24/4*(1-1/4))', u'4.5^(1/2)')]	|
|12	|(13-20*1/4)/[sqrt(20/4*(1-1/4))]	|(20-5)/ ((15)^(1/2) / 2)	|[('R.1', 1.9364916731037085, u'sqrt(20/4*(1-1/4))', u'(15)^(1/2) / 2')]	|
|13	|(11-21*1/5)/[sqrt(21/5*(1-1/5))]	|(6-[21*1/5])/[sqrt(21*1/5*(1-1/5))]	|[('R.1', 1.8330302779823362, u'sqrt(21/5*(1-1/5))', u'sqrt(21*1/5*(1-1/5))')]	|
|14	|(9-22*1/5)/[sqrt(22/5*(1-1/5))]	|(22-22/5)/1.876166	|[('R.1', 1.876166303929372, u'sqrt(22/5*(1-1/5))', u'1.876166')]	|
|15	|(9-22*1/5)/[sqrt(22/5*(1-1/5))]	|(22-22/5)/1.8761669	|[('R.1', 1.876166303929372, u'sqrt(22/5*(1-1/5))', u'1.8761669')]	|
|16	|(9-22*1/4)/[sqrt(22/4*(1-1/4))]	|(22/4)/(sqrt(22*(1/4)*(3/4)))	|[('R.1', 2.03100960115899, u'sqrt(22/4*(1-1/4))', u'sqrt(22*(1/4)*(3/4))')]	|
|17	|(8-24*1/6)/[sqrt(24/6*(1-1/6))]	|5/sqrt(1/6(1-1/6)24)	|[('R.1', 1.8257418583505538, u'sqrt(24/6*(1-1/6))', u'sqrt(1/6(1-1/6)24)')]	|
|18	|(8-24*1/6)/[sqrt(24/6*(1-1/6))]	|8/sqrt(1/6(1-1/6)24)	|[('R.1', 1.8257418583505538, u'sqrt(24/6*(1-1/6))', u'sqrt(1/6(1-1/6)24)')]	|
|19	|(12-24*1/6)/[sqrt(24/6*(1-1/6))]	|(6-4)/([24(1/6)(1-1/6)]^(1/2))	|[('R.1', 1.8257418583505538, u'sqrt(24/6*(1-1/6))', u'[24(1/6)(1-1/6)]^(1/2)')]	|
|20	|(12-24*1/6)/[sqrt(24/6*(1-1/6))]	|(24-4)/([24(1/6)(1-1/6)]^(1/2))	|[('R.1', 1.8257418583505538, u'sqrt(24/6*(1-1/6))', u'[24(1/6)(1-1/6)]^(1/2)')]	|
|21	|(13-27*1/5)/[sqrt(27/5*(1-1/5))]	|13/sqrt(27*(1/5)*(4/5))	|[('R.1', 2.078460969082653, u'sqrt(27/5*(1-1/5))', u'sqrt(27*(1/5)*(4/5))')]	|
|22	|(13-27*1/5)/[sqrt(27/5*(1-1/5))]	|27/sqrt(27*(1/5)*(4/5))	|[('R.1', 2.078460969082653, u'sqrt(27/5*(1-1/5))', u'sqrt(27*(1/5)*(4/5))')]	|
|23	|(10-24*1/5)/[sqrt(24/5*(1-1/5))]	|10 * sqrt(4*24/25)	|[('R.1', 1.9595917942265424, u'sqrt(24/5*(1-1/5))', u'sqrt(4*24/25)')]	|
|24	|(10-24*1/5)/[sqrt(24/5*(1-1/5))]	|5 sqrt(4*24/25)	|[('R.1', 1.9595917942265424, u'sqrt(24/5*(1-1/5))', u'sqrt(4*24/25)')]	|
|25	|(11-27*1/5)/[sqrt(27/5*(1-1/5))]	|11/sqrt(1/5*4/5*27)	|[('R.1', 2.078460969082653, u'sqrt(27/5*(1-1/5))', u'sqrt(1/5*4/5*27)')]	|




### (27) Mistake Group Wrong_Sign of size 27




### (24) Mistake Group Digits of size 24




### (15) Mistake Group ['R.0.0'] of size 15
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(10-22*1/4)/[sqrt(22/4*(1-1/4))]	|(10-(10/22))/1	|[('R.0.0', 10.0, u'10', u'10')]	|
|1	|(10-27*1/6)/[sqrt(27/6*(1-1/6))]	|(10-26/7)/(26/7)^(1/2)	|[('R.0.0', 10.0, u'10', u'10')]	|
|2	|(9-23*1/6)/[sqrt(23/6*(1-1/6))]	|Q(9/23)	|[('R.0.0', 9.0, u'9', u'9')]	|
|3	|(12-21*1/5)/[sqrt(21/5*(1-1/5))]	|Q(12-4.2/(1.83303))	|[('R.0.0', 12.0, u'12', u'12')]	|
|4	|(12-20*1/4)/[sqrt(20/4*(1-1/4))]	|Phi(12/20)	|[('R.0.0', 12.0, u'12', u'12')]	|
|5	|(8-25*1/6)/[sqrt(25/6*(1-1/6))]	|(8-4.16)/sqrt(25/6)	|[('R.0.0', 8.0, u'8', u'8')]	|
|6	|(8-25*1/6)/[sqrt(25/6*(1-1/6))]	|(8-4.16)/sqrt(21.84/6)	|[('R.0.0', 8.0, u'8', u'8')]	|
|7	|(9-22*1/6)/[sqrt(22/6*(1-1/6))]	|(9-(22/6*(1-1/6))^1/2)/(22/6)	|[('R.0.0', 9.0, u'9', u'9')]	|
|8	|(9-22*1/6)/[sqrt(22/6*(1-1/6))]	|(9-(22/6*(1-6))^1/2)/(22/6)	|[('R.0.0', 9.0, u'9', u'9')]	|
|9	|(9-22*1/6)/[sqrt(22/6*(1-1/6))]	|(9-(22/6*(1-1/6))^(1/2))/(22/6)	|[('R.0.0', 9.0, u'9', u'9')]	|
|10	|(8-24*1/6)/[sqrt(24/6*(1-1/6))]	|Q(8/(24/6))	|[('R.0.0', 8.0, u'8', u'8')]	|
|11	|(12-25*1/4)/[sqrt(25/4*(1-1/4))]	|Q(12/6.5)	|[('R.0.0', 12.0, u'12', u'12')]	|
|12	|(12-25*1/4)/[sqrt(25/4*(1-1/4))]	|Q(12-6.25/2.16506)	|[('R.0.0', 12.0, u'12', u'12')]	|
|13	|(8-25*1/6)/[sqrt(25/6*(1-1/6))]	|Q(8/25)	|[('R.0.0', 8.0, u'8', u'8')]	|
|14	|(12-26*1/6)/[sqrt(26/6*(1-1/6))]	|(12-4.33)/sqrt((6*4.33)/6)	|[('R.0.0', 12.0, u'12', u'12')]	|




### (11) Mistake Group ['R.0'] of size 11
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(10-27*1/6)/[sqrt(27/6*(1-1/6))]	|(10-27/6)/(27/6)^(1/2)	|[('R.0', 5.5, u'10-27*1/6', u'10-27/6')]	|
|1	|(8-29*1/6)/[sqrt(29/6*(1-1/6))]	|(8-(29/6))/((29*1*5/36)^0.5/(29)^0.5)	|[('R.0', 3.166666666666667, u'8-29*1/6', u'8-(29/6)')]	|
|2	|(12-20*1/4)/[sqrt(20/4*(1-1/4))]	|Q(12-5)	|[('R.0', 7.0, u'12-20*1/4', u'12-5')]	|
|3	|(11-28*1/5)/[sqrt(28/5*(1-1/5))]	|(11-28/5)/sqrt(5*(4/25))	|[('R.0', 5.4, u'11-28*1/5', u'11-28/5')]	|
|4	|(12-25*1/6)/[sqrt(25/6*(1-1/6))]	|(12 - (25/6)) / [(25/6)*((1 - (1/6)))]	|[('R.0', 7.833333333333333, u'12-25*1/6', u'12 - (25/6)')]	|
|5	|(15-28*1/4)/[sqrt(28/4*(1-1/4))]	|[15 - (28 * (1/4))]/[(sqrt((1/4)(3/4)*28))*sqrt(28)]	|[('R.0', 8.0, u'15-28*1/4', u'15 - (28 * (1/4))')]	|
|6	|(13-27*1/5)/[sqrt(27/5*(1-1/5))]	|(13-(27/5))/((13-(27/5))^2)	|[('R.0', 7.6, u'13-27*1/5', u'13-(27/5)')]	|
|7	|(10-26*1/5)/[sqrt(26/5*(1-1/5))]	|(10-5.2)/sqrt(20.84/6)	|[('R.0', 4.8, u'10-26*1/5', u'10-5.2')]	|
|8	|(8-25*1/6)/[sqrt(25/6*(1-1/6))]	|Q(8 - 25 / 6)	|[('R.0', 3.833333333333333, u'8-25*1/6', u'8 - 25 / 6')]	|
|9	|(10-26*1/5)/[sqrt(26/5*(1-1/5))]	|(10-5.2)/sqrt(26/6)	|[('R.0', 4.8, u'10-26*1/5', u'10-5.2')]	|
|10	|(10-26*1/5)/[sqrt(26/5*(1-1/5))]	|(10-5.2)/sqrt(26/5)	|[('R.0', 4.8, u'10-26*1/5', u'10-5.2')]	|




### (2) Mistake Group ['R.0.0', 'R.1'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(11-29*1/5)/[sqrt(29/5*(1-1/5))]	|(11-19/5)/(29*4/25)^.5	|[('R.0.0', 11.0, u'11', u'11'), ('R.1', 2.1540659228538015, u'sqrt(29/5*(1-1/5))', u'(29*4/25)^.5')]	|
|1	|(11-27*1/6)/[sqrt(27/6*(1-1/6))]	|(11-27/8)/sqrt(27*5/36)	|[('R.0.0', 11.0, u'11', u'11'), ('R.1', 1.9364916731037085, u'sqrt(27/6*(1-1/6))', u'sqrt(27*5/36)')]	|




### (1) Mistake Group ['R.1.0.0'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(12-29*1/5)/[sqrt(29/5*(1-1/5))]	|12-(5.8/2.15406592285/sqrt(23))	|[('R.1.0.0', 5.8, u'29/5', u'5.8')]	|




### (1) Mistake Group ['R.0.0', 'R.1.0.0'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.1.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(12-26*1/6)/[sqrt(26/6*(1-1/6))]	|(12-4.33)/sqrt((26/6)6)	|[('R.0.0', 12.0, u'12', u'12'), ('R.1.0.0', 4.333333333333333, u'26/6', u'26/6')]	|




### (41) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:dlgoldbe

	first_attempt
					2015-11-05 06:23:46
	part2_correct_attempt
					['0:05:09', u'22/4']
	part3_correct_attempt
					['0:09:26', u'sqrt((22/4)*(1-(1/4)))']
	part4_incorrect_attempt
					('0:12:41', u'Q(13)')
	part4_correct_attempt
					['0:13:59', u'(13-(22/4))/(sqrt((22/4)*(1-(1/4))))']

1 Student ID:h4tu

	first_attempt
					2015-11-06 23:39:46
	part2_correct_attempt
					['0:16:55', u'6']
	part3_correct_attempt
					['0:18:42', u'sqrt((1/5)*(1-1/5)*30)']
	part4_incorrect_attempt
					('0:24:31', u'6/14')
					('0:24:39', u'14/6')
					('0:24:45', u'14-6')
					('0:29:58', u'1-Phi(14)')
					('0:30:43', u'Phi(14)')
					('0:30:56', u'Q(14)')
	part4_correct_attempt
					['0:33:22', u'(14-6)/sqrt((1/5)*(1-1/5)*30)']

2 Student ID:lywong

	first_attempt
					2015-11-04 07:31:23
	part2_correct_attempt
					['1 day, 12:29:27', u'(1/4)*23']
	part3_correct_attempt
					['1 day, 16:09:21', u'(23*(1/4)(1-(1/4)))^(1/2)']
	part4_incorrect_attempt
					('1 day, 16:14:36', u'Q((23*(1/4)(1-(1/4)))^(1/2))')
	part4_correct_attempt
					['1 day, 16:18:11', u'(9-(1/4)*23)/(23*(1/4)(1-(1/4)))^(1/2)']

3 Student ID:abasu

	first_attempt
					2015-11-05 03:07:09
	part2_correct_attempt
					['0:06:00', u'29(1/5)']
	part3_correct_attempt
					['2:13:59', u'2.15406592285']
	part4_incorrect_attempt
					('2:15:56', u'12-(5.8/2.154065)')
					('2:16:05', u'12-(5.8/2.15406592285)')
					('2:20:03', u'7.20416847669')
	part4_correct_attempt
					['2:21:25', u'2.8783']

4 Student ID:alakamsa

	first_attempt
					2015-11-04 18:21:07
	part2_correct_attempt
					['0:00:00', u'4']
	part3_correct_attempt
					['0:00:27', u'sqrt(24*(1/6)*(1-(1/6)))']
	part4_incorrect_attempt
					('0:02:07', u'0.0005075')
					('0:05:29', u'0.000507494')
	part4_correct_attempt
					['0:25:58', u'3.2863']

5 Student ID:any027

	first_attempt
					2015-11-01 20:36:42
	part2_correct_attempt
					['0:02:37', u'27/6']
	part3_correct_attempt
					['1:32:21', u'sqrt( (27*1/6)* (1-1/6) )']
	part4_incorrect_attempt
					('1:33:11', u'11 - (27/6) / (sqrt( (27*1/6)* (1-1/6) ))')
	part4_correct_attempt
					['1:33:24', u'(11 - (27/6)) / (sqrt( (27*1/6)* (1-1/6) ))']

6 Student ID:rwthomps

	first_attempt
					2015-11-06 21:39:26
	part2_correct_attempt
					['0:00:44', u'4']
	part3_correct_attempt
					['0:08:03', u'sqrt(0.2 * 0.8 * 20)']
	part4_incorrect_attempt
					('0:08:20', u'Q(11)')
	part4_correct_attempt
					['0:09:59', u'(11 - 4)/sqrt(0.2 * 0.8 * 20)']

7 Student ID:awollner

	first_attempt
					2015-11-06 23:45:59
	part2_correct_attempt
					['0:00:43', u'25/4']
	part3_correct_attempt
					['0:04:41', u'sqrt(.25*.75*25)']
	part4_incorrect_attempt
					('0:05:11', u'Q(12)')
					('0:07:30', u'Q(2.16506)')
					('0:11:37', u'Q(6.25/2.16506)')
					('0:13:00', u'Q(5.75/2.16506)')
					('0:13:32', u'Q((12-6.25)/2.16506)')
	part4_correct_attempt
					['0:20:43', u'(12-6.25)/sqrt(.25*.75*25)']

8 Student ID:kthui

	first_attempt
					2015-11-06 08:10:25
	part2_correct_attempt
					['0:08:57', u'20/6']
	part3_correct_attempt
					['0:12:11', u'((1/6)(1-1/6)20)^(1/2)']
	part4_incorrect_attempt
					('0:14:48', u'(8-20/6)/10+5/2+10/9+5/8+2/5')
	part4_correct_attempt
					['0:15:08', u'(8-20/6)/((1/6)(1-1/6)20)^(1/2)']

9 Student ID:aakumar

	first_attempt
					2015-11-05 03:13:47
	part2_correct_attempt
					['0:12:20', u'23(1/6)']
	part3_correct_attempt
					['2:09:35', u'(23*5/36)^(1/2)']
	part4_incorrect_attempt
					('2:19:24', u'1.4771')
	part4_correct_attempt
					['2:34:32', u'1.7719']

10 Student ID:dan029

	first_attempt
					2015-11-05 09:16:18
	part2_correct_attempt
					['0:06:47', u'5']
	part3_correct_attempt
					['0:07:40', u'sqrt(3.75)']
	part4_incorrect_attempt
					('0:08:07', u'Q(12)')
					('0:09:28', u'Phi(12)')
					('0:13:38', u'Q(5-12)')
					('0:14:05', u'Phi(12)')
	part4_correct_attempt
					['0:16:01', u'(12-5)/sqrt(3.75)']

11 Student ID:gsrandha

	first_attempt
					2015-11-05 08:11:06
	part2_correct_attempt
					['0:06:51', u'21 * .2']
	part3_correct_attempt
					['0:11:23', u'sqrt(4.2(1-.2))']
	part4_incorrect_attempt
					('0:12:23', u'Q((12-4.2)/(1.83303))')
	part4_correct_attempt
					['0:13:31', u'((12-4.2)/(1.83303))']

12 Student ID:ttimmons

	first_attempt
					2015-11-03 18:36:16
	part2_correct_attempt
					['0:09:13', u'(1/4)*30']
	part3_correct_attempt
					['0:19:47', u'sqrt(30*(1/4)*(1-(1/4)))']
	part4_incorrect_attempt
					('1 day, 0:40:51', u'Q(7)')
					('1 day, 0:40:57', u'Q(15)')
	part4_correct_attempt
					['1 day, 1:14:20', u'[15 - (1/4)*30]/[sqrt(30*(1/4)*(1-(1/4)))]']

13 Student ID:jew037

	first_attempt
					2015-11-05 00:24:42
	part2_correct_attempt
					['0:01:00', u'26/6']
	part3_correct_attempt
					['0:01:44', u'sqrt(26*(1/6)*(1-(1/6)))']
	part4_incorrect_attempt
					('0:04:03', u'12-(26*(1/6))/ (sqrt( 26 / 6 * (1-1/ 6)))')
	part4_correct_attempt
					['0:05:38', u'( 12 - (26* (1/6)) ) / ( sqrt( 26 / 6 * (1-1/ 6)) )']

14 Student ID:mnrahman

	first_attempt
					2015-11-07 00:02:07
	part2_correct_attempt
					['0:26:56', u'26/5']
	part3_correct_attempt
					['0:28:01', u'sqrt(20.84/5)']
	part4_incorrect_attempt
					('0:28:01', u'(8-5.2)/sqrt(20.84/6)')
	part4_correct_attempt
					['0:43:37', u'(10-5.2)/sqrt(20.84/5)']

15 Student ID:rlhagen

	first_attempt
					2015-10-31 19:16:52
	part2_correct_attempt
					['0:02:09', u'25*(1/5)']
	part3_correct_attempt
					['0:03:30', u'sqrt(25*(1/5)*(1-(1/5)))']
	part4_incorrect_attempt
					('0:06:25', u'10-(25*(1/5))/(sqrt(25*(1/5)*(1-(1/5))))')
	part4_correct_attempt
					['0:06:51', u'(10-(25*(1/5)))/(sqrt(25*(1/5)*(1-(1/5))))']

16 Student ID:agarango

	first_attempt
					2015-11-06 20:14:19
	part2_correct_attempt
					['0:18:35', u'21*(1/6)']
	part3_correct_attempt
					['3:28:35', u'sqrt(5*21)/6']
	part4_incorrect_attempt
					('3:39:23', u'11-(1/6)/(sqrt(5*1)/6)')
					('3:39:49', u'11-(21/6)/(sqrt(5*21)/6)')
					('3:40:13', u'11-(11/6)/(sqrt(5*11)/6)')
					('3:40:49', u'11-(21/6)/(sqrt(5*21)/6)')
	part4_correct_attempt
					['3:41:30', u'(11-(21/6))/(sqrt(5*21)/6)']

17 Student ID:avasavad

	first_attempt
					2015-11-04 23:24:31
	part4_incorrect_attempt
					('0:11:48', u'Q(11)')
					('0:12:14', u'Phi(11)')

18 Student ID:s6deng

	first_attempt
					2015-11-05 07:34:09
	part4_incorrect_attempt
					('0:46:30', u'(23-8)/(1/5)')

19 Student ID:dgunawan

	first_attempt
					2015-11-05 08:48:59
	part2_correct_attempt
					['0:00:00', u'(1/4) * 28']
	part3_correct_attempt
					['15:23:45', u'((1/4) * 28 (1-1/4))^(1/2)']
	part4_incorrect_attempt
					('15:24:13', u'13-7/[((1/4) * 28 (1-1/4))^(1/2)]')
	part4_correct_attempt
					['15:24:23', u'[13-7]/[((1/4) * 28 (1-1/4))^(1/2)]']

20 Student ID:rraiyyan

	first_attempt
					2015-11-06 23:38:15
	part2_correct_attempt
					['0:04:10', u'24/5']
	part3_correct_attempt
					['0:05:19', u'sqrt(4*24/25)']
	part4_incorrect_attempt
					('0:09:49', u'24/5 + 10 * sqrt(4*24/25)')
					('0:12:35', u'10 * (24/5 + sqrt(4*24/25))')
					('0:13:25', u'24/5 + 10 * sqrt(4*24/25)')
					('0:17:22', u'10-4.8/(sqrt(4*24/25))')
	part4_correct_attempt
					['0:17:36', u'(10-4.8)/(sqrt(4*24/25))']

21 Student ID:yeh013

	first_attempt
					2015-11-05 03:50:09
	part2_correct_attempt
					['2:26:57', u'6']
	part3_correct_attempt
					['3:17:42', u'4.5^(1/2)']
	part4_incorrect_attempt
					('3:18:27', u'9^(1/2)')
					('3:20:12', u'2*(30/16)^(1/2)')
	part4_correct_attempt
					['3:22:10', u'4/(4.5^(1/2))']

22 Student ID:tcn013

	first_attempt
					2015-11-05 20:47:22
	part2_correct_attempt
					['0:00:00', u'23/6']
	part3_correct_attempt
					['0:05:58', u'sqrt( (1/6)* (5/6) * 23)']
	part4_incorrect_attempt
					('0:06:20', u'23/6+1.7873*9')
	part4_correct_attempt
					['0:08:29', u'(9-23/6)/1.7873']

23 Student ID:tstevens

	first_attempt
					2015-11-06 12:00:01
	part2_correct_attempt
					['0:00:10', u'24*.2']
	part3_correct_attempt
					['0:05:23', u'1.959591794']
	part4_incorrect_attempt
					('0:07:37', u'2.3474')
	part4_correct_attempt
					['0:08:17', u'2.143303628']

24 Student ID:akalathi

	first_attempt
					2015-11-04 06:30:40
	part2_correct_attempt
					['0:00:17', u'1/5 * 29']
	part3_correct_attempt
					['0:02:46', u'sqrt((29(1/5)*(4/5)))']
	part4_incorrect_attempt
					('0:04:37', u'12 - (5.8/(sqrt((29(1/5)*(4/5)))))')
	part4_correct_attempt
					['0:05:44', u'(12- 5.8)/(sqrt((29(1/5)*(4/5))))']

25 Student ID:lcardoso

	first_attempt
					2015-11-06 21:19:27
	part2_correct_attempt
					['-1 day, 23:58:55', u'28*(1/5)']
	part3_correct_attempt
					['-1 day, 23:58:55', u'sqrt((28*(1/5))*(1-(1/5)))']
	part4_incorrect_attempt
					('-1 day, 23:58:55', u'11-[28*(1/5)]/[sqrt((28*(1/5))*(1-(1/5)))]')
	part4_correct_attempt
					['0:00:24', u'(11-[28*(1/5)])/[sqrt((28*(1/5))*(1-(1/5)))]']

26 Student ID:jel075

	first_attempt
					2015-11-05 09:10:18
	part2_correct_attempt
					['0:02:18', u'5.2']
	part3_correct_attempt
					['13:40:20', u'sqrt(26*(1/5) * (1-1/5))']
	part4_incorrect_attempt
					('13:41:49', u'(26-5.2)/2.03961')
	part4_correct_attempt
					['13:42:16', u'(9-5.2)/2.03961']

27 Student ID:dsriniva

	first_attempt
					2015-11-05 16:50:26
	part2_correct_attempt
					['0:03:10', u'27/6']
	part3_correct_attempt
					['2:33:19', u'sqrt(27*(1/6)(5/6))']
	part4_incorrect_attempt
					('2:34:52', u'1.390345*10^-2')
					('2:35:04', u'1.390345*10^2')
					('2:35:50', u'2.23')
	part4_correct_attempt
					['2:36:08', u'2.32379201545']

28 Student ID:edescobe

	first_attempt
					2015-11-01 09:54:00
	part2_correct_attempt
					['3 days, 1:45:13', u'20/6']
	part3_correct_attempt
					['3 days, 1:50:16', u'( 20 / 6* (1-1/ 6))^(1/2)']
	part4_incorrect_attempt
					('3 days, 2:10:00', u'.99999')
	part4_correct_attempt
					['3 days, 2:11:43', u'(10-20/6)/1.6666']

29 Student ID:w4shin

	first_attempt
					2015-11-06 23:31:49
	part2_correct_attempt
					['-1 day, 23:59:40', u'27*(1/5)']
	part3_correct_attempt
					['0:05:56', u'sqrt(27*(1/5)*(4/5))']
	part4_incorrect_attempt
					('0:09:02', u'Phi(13)')
	part4_correct_attempt
					['0:11:46', u'(13-27*(1/5))/sqrt(27*(1/5)*(4/5))']

30 Student ID:hmshah

	first_attempt
					2015-11-05 10:24:09
	part4_incorrect_attempt
					('0:15:53', u'Q(8)')

31 Student ID:ralhadda

	first_attempt
					2015-10-31 21:01:50
	part2_correct_attempt
					['0:05:12', u'6.25']
	part3_correct_attempt
					['4:20:31', u'2.165']
	part4_incorrect_attempt
					('4:21:18', u'2.8867')
	part4_correct_attempt
					['4:22:08', u'1.732']

32 Student ID:yig015

	first_attempt
					2015-11-05 10:50:36
	part2_correct_attempt
					['0:09:09', u'30/4']
	part3_correct_attempt
					['0:31:26', u'2.371708245']
	part4_incorrect_attempt
					('0:33:55', u'Phi(11)')
					('0:34:37', u'0.7')
	part4_correct_attempt
					['23:27:03', u'7*sqrt(10)/15']

33 Student ID:xweng

	first_attempt
					2015-11-06 00:34:03
	part2_correct_attempt
					['0:15:30', u'22/5']
	part3_correct_attempt
					['0:17:39', u'1.876166']
	part4_incorrect_attempt
					('0:19:57', u'0.876166')
	part4_correct_attempt
					['0:24:36', u'(9-22/5)/1.8761669']

34 Student ID:yypan

	first_attempt
					2015-11-03 00:31:21
	part2_correct_attempt
					['1:00:46', u'23*0.2']
	part3_correct_attempt
					['1:19:07', u'sqrt((23*0.2*23*0.8)/23)']
	part4_incorrect_attempt
					('1:49:07', u'(8!/(23!*15!))*0.2^8*0.8^15')
					('1:49:29', u'1-(8!/(23!*15!))*0.2^8*0.8^15')
	part4_correct_attempt
					['2 days, 5:40:05', u'(8-23*0.2)/sqrt((23*0.2*23*0.8)/23)']

35 Student ID:k4ma

	first_attempt
					2015-11-06 21:29:44
	part2_correct_attempt
					['0:03:46', u'27*(.25)']
	part3_correct_attempt
					['0:04:13', u'sqrt(.25(1-.25)27)']
	part4_incorrect_attempt
					('0:05:04', u'1-Phi(12)')
					('0:05:41', u'Phi(12)')
	part4_correct_attempt
					['0:08:47', u'[12-(27*.25)]/sqrt(.25(1-.25)27)']

36 Student ID:v3doan

	first_attempt
					2015-11-05 05:30:30
	part2_correct_attempt
					['1 day, 19:03:32', u'25 / 6']
	part3_correct_attempt
					['1 day, 19:04:23', u'sqrt(1/6 (5/6) 25)']
	part4_incorrect_attempt
					('1 day, 19:04:44', u'1 - Phi(8)')
					('1 day, 19:05:16', u'Q(8)')
					('1 day, 19:05:25', u'Q(1/25)')
	part4_correct_attempt
					['1 day, 19:08:19', u'(8 - 25 / 6) / (sqrt(1/6 (5/6) 25))']

37 Student ID:zig006

	first_attempt
					2015-11-04 21:24:02
	part2_correct_attempt
					['0:00:21', u'7']
	part3_correct_attempt
					['0:34:12', u'((21)^0.5)/2']
	part4_incorrect_attempt
					('0:35:19', u'7.93327*10^(-7)')
					('0:36:37', u'0.04456')
					('0:37:19', u'0.035930')
	part4_correct_attempt
					['0:38:41', u'1.745743']

38 Student ID:hmnaing

	first_attempt
					2015-11-06 18:32:06
	part2_correct_attempt
					['3:41:28', u'26/4']
	part3_correct_attempt
					['3:52:15', u'sqrt(0.25*0.75*26)']
	part4_incorrect_attempt
					('3:52:57', u'13- (26/4)/ (sqrt(0.25*0.75*26))')
	part4_correct_attempt
					['3:53:12', u'(13- (26/4))/ (sqrt(0.25*0.75*26))']

39 Student ID:mjethani

	first_attempt
					2015-11-06 02:05:57
	part2_correct_attempt
					['22:51:31', u'30/6']
	part4_incorrect_attempt
					('22:52:56', u'(11-5)')

40 Student ID:asp025

	first_attempt
					2015-11-06 22:08:56
	part2_correct_attempt
					['0:43:48', u'24/6']
	part3_correct_attempt
					['0:49:11', u'[24(1/6)(1-1/6)]^(1/2)']
	part4_incorrect_attempt
					('0:56:50', u'1-Phi(12)')
					('0:57:02', u'1-Phi(12/6)')
					('0:57:14', u'1-Phi(6/12)')
	part4_correct_attempt
					['1:04:30', u'(12-4)/([24(1/6)(1-1/6)]^(1/2))']












## Part 5

### (47) Mistake Group redirect of size 47




### (23) Mistake Group Wrong_Sign of size 23




### (12) Mistake Group Digits of size 12




### (7) Mistake Group ['R.0.0'] of size 7
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|Q((10-27*1/6)/[sqrt(27/6*(1-1/6))])	|Q((10-27/6)/(26/7)^(1/2))	|[('R.0.0', 5.5, u'10-27*1/6', u'10-27/6')]	|
|1	|Q((12-26*1/6)/[sqrt(26/6*(1-1/6))])	|Q(12-(26*(1/6))) / ( sqrt( 26 / 6 * (1-1/ 6)))	|[('R.0.0', 7.666666666666667, u'12-26*1/6', u'12-(26*(1/6))')]	|
|2	|Q((11-29*1/5)/[sqrt(29/5*(1-1/5))])	|sqrt((11-29/5)/29)	|[('R.0.0', 5.2, u'11-29*1/5', u'11-29/5')]	|
|3	|Q((9-28*1/5)/[sqrt(28/5*(1-1/5))])	|Q((9-5.6)/((9-5.6)/(sqrt(28 * 1/5 *(1-1/5)))))	|[('R.0.0', 3.4000000000000004, u'9-28*1/5', u'9-5.6')]	|
|4	|Q((11-27*1/4)/[sqrt(27/4*(1-1/4))])	|Q(11-6.75)/[sqrt((1/4)[3/4][27])]	|[('R.0.0', 4.25, u'11-27*1/4', u'11-6.75')]	|
|5	|Q((11-24*1/4)/[sqrt(24/4*(1-1/4))])	|Q(11 - (24 * 1/4)) / sqrt(24*1/4*(1-1/4))	|[('R.0.0', 5.0, u'11-24*1/4', u'11 - (24 * 1/4)')]	|




### (6) Mistake Group ['R.0'] of size 6
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|Q((12-24*1/6)/[sqrt(24/6*(1-1/6))])	|(((12)-(24*1/6))/(sqrt(24*1/6*(1-1/6))))/12	|[('R.0', 4.381780460041329, u'(12-24*1/6)/[sqrt(24/6*(1-1/6))]', u'((12)-(24*1/6))/(sqrt(24*1/6*(1-1/6)))')]	|
|1	|Q((13-22*1/4)/[sqrt(22/4*(1-1/4))])	|(13-(22/4))/(sqrt((22/4)*(1-(1/4))))+Q((13-(22/4))/(sqrt((22/4)*(1-(1/4)))))	|[('R.0', 3.6927447293799815, u'(13-22*1/4)/[sqrt(22/4*(1-1/4))]', u'(13-(22/4))/(sqrt((22/4)*(1-(1/4))))')]	|
|2	|Q((10-27*1/6)/[sqrt(27/6*(1-1/6))])	|Phi((10-4.5)/(((1/6)(5/6)27))^.5)	|[('R.0', 2.840187787218772, u'(10-27*1/6)/[sqrt(27/6*(1-1/6))]', u'(10-4.5)/(((1/6)(5/6)27))^.5)')]	|
|3	|Q((13-27*1/5)/[sqrt(27/5*(1-1/5))])	|Phi((13-27*(1/5))/sqrt(27*(1/5)*(4/5)))	|[('R.0', 3.656551704867629, u'(13-27*1/5)/[sqrt(27/5*(1-1/5))]', u'(13-27*(1/5))/sqrt(27*(1/5)*(4/5))')]	|
|4	|Q((9-23*1/5)/[sqrt(23/5*(1-1/5))])	|Phi((9 - 4.6)/(sqrt((1/5)(4/5)23)))	|[('R.0', 2.293658554627823, u'(9-23*1/5)/[sqrt(23/5*(1-1/5))]', u'(9 - 4.6)/(sqrt((1/5)(4/5)23))')]	|
|5	|Q((15-28*1/4)/[sqrt(28/4*(1-1/4))])	|8/((.25*.75*28)^.5)/28	|[('R.0', 3.4914862437758782, u'(15-28*1/4)/[sqrt(28/4*(1-1/4))]', u'8/((.25*.75*28)^.5)')]	|




### (5) Mistake Group ['R.0.1'] of size 5
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|Q((9-28*1/5)/[sqrt(28/5*(1-1/5))])	|[10-(28/5)]/[sqrt(28*(1/5)*(1-(1/5)))]-[9-(28/5)]/2.1166	|[('R.0.1', 2.116601048851672, u'sqrt(28/5*(1-1/5))', u'sqrt(28*(1/5)*(1-(1/5)))')]	|
|1	|Q((10-26*1/5)/[sqrt(26/5*(1-1/5))])	|Q(10/sqrt(26/5*4/5))	|[('R.0.1', 2.039607805437114, u'sqrt(26/5*(1-1/5))', u'sqrt(26/5*4/5)')]	|
|2	|Q((10-26*1/5)/[sqrt(26/5*(1-1/5))])	|Q(10/(sqrt(26*1/5*4/5)))	|[('R.0.1', 2.039607805437114, u'sqrt(26/5*(1-1/5))', u'sqrt(26*1/5*4/5)')]	|
|3	|Q((10-26*1/5)/[sqrt(26/5*(1-1/5))])	|Q(26/(sqrt(26*1/5*4/5)))	|[('R.0.1', 2.039607805437114, u'sqrt(26/5*(1-1/5))', u'sqrt(26*1/5*4/5)')]	|
|4	|Q((10-30*1/5)/[sqrt(30/5*(1-1/5))])	|Q((10 - 6)/(sqrt(30/5 * (4/5)))/(sqrt(30/5 * (4/5))))	|[('R.0.1', 2.1908902300206647, u'sqrt(30/5*(1-1/5))', u'sqrt(30/5 * (4/5))')]	|




### (4) Mistake Group ['R.0.0.0'] of size 4
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|Q((10-27*1/6)/[sqrt(27/6*(1-1/6))])	|Q((10-26/7)/(26/7)^(1/2))	|[('R.0.0.0', 10.0, u'10', u'10')]	|
|1	|Q((12-26*1/6)/[sqrt(26/6*(1-1/6))])	|Q((12-4.33)/sqrt((5*4.33)/6))	|[('R.0.0.0', 12.0, u'12', u'12')]	|
|2	|Q((12-26*1/6)/[sqrt(26/6*(1-1/6))])	|Q(12-4.33)/sqrt((5*4.33)/6)	|[('R.0.0.0', 12.0, u'12', u'12')]	|




### (1) Mistake Group ['R.0.0', 'R.0.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|Q((8-22*1/5)/[sqrt(22/5*(1-1/5))])	|Q((8-4.4)*[sqrt(4.4*(1-(1/5)))])	|[('R.0.0', 3.5999999999999996, u'8-22*1/5', u'8-4.4'), ('R.0.1', 1.876166303929372, u'sqrt(22/5*(1-1/5))', u'sqrt(4.4*(1-(1/5)))')]	|




### (81) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:dmn009

	first_attempt
					2015-11-05 09:18:22
	part2_correct_attempt
					['-1 day, 23:57:57', u'1.91833']
	part3_correct_attempt
					['-1 day, 23:57:57', u'3.336']
	part5_incorrect_attempt
					('0:01:05', u'3.336')
	part5_correct_attempt
					['0:01:15', u'.000424966']

1 Student ID:b3hwang

	first_attempt
					2015-11-05 09:45:50
	part2_correct_attempt
					['9:32:10', u'(1/6)*26']
	part3_correct_attempt
					['9:34:47', u'(((1/6)*26)(1-(1/6)))^(1/2)']
	part4_correct_attempt
					['9:39:31', u'(9-((1/6)*26))/(((1/6)*26)(1-(1/6)))^(1/2)']
	part5_incorrect_attempt
					('9:41:06', u'.008')
					('9:44:28', u'(.5-0.4929)')
					('9:45:04', u'(.5+0.4929)')
					('9:45:18', u'(.5+0.4931)')
					('9:45:25', u'(.5-0.4931)')
					('9:47:37', u'0.16157')
					('9:48:17', u'0.992971')
	part5_correct_attempt
					['9:50:26', u'1 - Phi(2.45576)']

2 Student ID:hmshah

	first_attempt
					2015-11-05 10:24:09
	part5_incorrect_attempt
					('0:14:16', u'Q(8)')

3 Student ID:v4zhang

	first_attempt
					2015-11-06 07:21:17
	part2_correct_attempt
					['0:03:40', u'29/6']
	part3_correct_attempt
					['0:07:45', u'sqrt((1/6)*(1-1/6)*29)']
	part4_correct_attempt
					['0:07:45', u'(9-(29/6))/[sqrt((1/6)*(1-1/6)*29)]']
	part5_incorrect_attempt
					('0:07:45', u'1.8e^-2')
	part5_correct_attempt
					['0:08:28', u'Q((9-(29/6))/[sqrt((1/6)*(1-1/6)*29)])']

4 Student ID:quwong

	first_attempt
					2015-11-03 01:16:34
	part2_correct_attempt
					['0:17:06', u'27/6']
	part3_correct_attempt
					['0:17:57', u'(27/6*5/6)^0.5']
	part4_correct_attempt
					['0:21:36', u'(10 - 27/6)/((27/6*5/6)^0.5)']
	part5_incorrect_attempt
					('0:21:36', u'0.81421')
					('0:22:11', u'0.981421')
					('0:22:34', u'0.018579')
	part5_correct_attempt
					['0:23:21', u'0.002254']

5 Student ID:kbielawi

	first_attempt
					2015-11-05 21:20:09
	part2_correct_attempt
					['0:02:14', u'24/5']
	part3_correct_attempt
					['0:07:20', u'sqrt((1/5)*(1-(1/5))*24)']
	part4_correct_attempt
					['0:11:13', u'(8-(24/5))/(1.95959)']
	part5_incorrect_attempt
					('0:12:55', u'1-Phi(8)')
					('0:13:34', u'1-(1-Phi(8))')
	part5_correct_attempt
					['4:15:14', u'Q((8-(24/5))/(1.95959))']

6 Student ID:lguintu

	first_attempt
					2015-11-03 04:53:50
	part2_correct_attempt
					['0:03:20', u'24/5']
	part3_correct_attempt
					['0:14:03', u'(24*(1/5)*(4/5))^(1/2)']
	part4_correct_attempt
					['0:14:23', u'(11-24/5)/(24*(1/5)*(4/5))^(1/2)']
	part5_incorrect_attempt
					('0:17:59', u'13/24')
					('0:25:04', u'C(24,0)*(1/5)^0*(4/5)^24+C(24,1)+C(24,2)+C(24,3)+C(24,4)+C(24,5)+C(24,6)+C(24,7)+C(24,8)+C(24,9)+C(24,10)')
					('0:29:01', u'.9992')
					('0:29:07', u'1-.9992')
					('0:31:04', u'1-Phi(0.3)')
	part5_correct_attempt
					['0:31:16', u'1-Phi((11-24/5)/(24*(1/5)*(4/5))^(1/2))']

7 Student ID:acvuong

	first_attempt
					2015-11-05 00:53:44
	part2_correct_attempt
					['0:00:00', u'30/4']
	part3_correct_attempt
					['0:00:00', u'(30(1/4)(3/4))^0.5']
	part4_correct_attempt
					['0:00:00', u'(12-(30/4))/((30(1/4)(3/4))^0.5)']
	part5_incorrect_attempt
					('0:01:12', u'e^(-12*30/4)')
	part5_correct_attempt
					['0:03:37', u'Q((12-(30/4))/((30(1/4)(3/4))^0.5))']

8 Student ID:alakamsa

	first_attempt
					2015-11-04 18:21:07
	part2_correct_attempt
					['0:00:00', u'4']
	part3_correct_attempt
					['0:00:27', u'sqrt(24*(1/6)*(1-(1/6)))']
	part4_correct_attempt
					['0:25:58', u'3.2863']
	part5_incorrect_attempt
					('0:29:28', u'Q(3.2863) + e^-4*(4^10/10!)')
	part5_correct_attempt
					['0:30:03', u'Q(3.2863)']

9 Student ID:abjara

	first_attempt
					2015-11-04 03:06:02
	part2_correct_attempt
					['0:10:01', u'22*1/5']
	part3_correct_attempt
					['0:14:03', u'sqrt(4.4*(1-(1/5)))']
	part4_correct_attempt
					['0:16:06', u'(8-4.4)/[sqrt(4.4*(1-(1/5)))]']
	part5_incorrect_attempt
					('0:18:19', u'(8-4.4)*[sqrt(4.4*(1-(1/5)))]')
	part5_correct_attempt
					['0:26:05', u'Q((8-4.4)/[sqrt(4.4*(1-(1/5)))])']

10 Student ID:spw006

	first_attempt
					2015-11-04 02:48:59
	part2_correct_attempt
					['0:26:44', u'22*(1/4)']
	part3_correct_attempt
					['0:37:03', u'sqrt(22*(1/4)*(3/4))']
	part4_correct_attempt
					['0:37:34', u'(11 - 22*(1/4))/sqrt(22*(1/4)*(3/4))']
	part5_incorrect_attempt
					('0:39:16', u'1-Phi(11 - 22*(1/4))/sqrt(22*(1/4)*(3/4))')
	part5_correct_attempt
					['0:39:26', u'1-Phi((11 - 22*(1/4))/sqrt(22*(1/4)*(3/4)))']

11 Student ID:masaro

	first_attempt
					2015-11-03 17:10:58
	part2_correct_attempt
					['-1 day, 23:59:21', u'sqrt(3.75)']
	part3_correct_attempt
					['-1 day, 23:59:21', u'6/sqrt(3.75)']
	part4_correct_attempt
					['-1 day, 23:59:21', u'0.1']
	part5_incorrect_attempt
					('0:12:49', u'0.0013498')
	part5_correct_attempt
					['0:13:30', u'0.0009676']

12 Student ID:hkhodada

	first_attempt
					2015-10-31 17:45:28
	part2_correct_attempt
					['4 days, 1:06:07', u'11/2']
	part3_correct_attempt
					['4 days, 1:07:18', u'sqrt(66)/4']
	part4_correct_attempt
					['4 days, 1:11:06', u'14/sqrt(66)']
	part5_incorrect_attempt
					('4 days, 1:26:13', u'1-Q(9)')
					('4 days, 1:26:19', u'Q(9)')
	part5_correct_attempt
					['4 days, 1:28:29', u'Q(14/sqrt(66))']

13 Student ID:l5han

	first_attempt
					2015-11-06 19:37:46
	part2_correct_attempt
					['0:00:00', u'25*1/4']
	part3_correct_attempt
					['0:00:00', u'[(1/4)*(3/4)*25]^(1/2)']
	part4_correct_attempt
					['0:00:00', u'(10-25/4)/[[(1/4)*(3/4)*25]^(1/2)]']
	part5_incorrect_attempt
					('0:00:00', u'Q(10)')
	part5_correct_attempt
					['0:02:29', u'Q((10-25/4)/[[(1/4)*(3/4)*25]^(1/2)])']

14 Student ID:bakang

	first_attempt
					2015-11-05 08:51:51
	part2_correct_attempt
					['0:15:55', u'1/6*21']
	part3_correct_attempt
					['8:04:15', u'sqrt(1/6*(5/6)*21)']
	part4_correct_attempt
					['8:05:24', u'(9-(1/6*21))/(sqrt(1/6*(5/6)*21))']
	part5_incorrect_attempt
					('8:05:37', u'Q(9)')
					('8:06:01', u'Q(9)+(9-(1/6*21))/(sqrt(1/6*(5/6)*21))')
	part5_correct_attempt
					['8:08:49', u'Q((9-(1/6*21))/(sqrt(1/6*(5/6)*21)))']

15 Student ID:jcj006

	first_attempt
					2015-11-04 06:04:21
	part2_correct_attempt
					['-1 day, 23:59:50', u'29/5']
	part3_correct_attempt
					['16:23:19', u'sqrt(29*.2*.8)']
	part4_correct_attempt
					['16:23:19', u'(9-29/5)/sqrt(29*.2*.8)']
	part5_incorrect_attempt
					('16:32:09', u'Q(9)')
	part5_correct_attempt
					['16:33:01', u'Q((9-29/5)/sqrt(29*.2*.8))']

16 Student ID:crmirand

	first_attempt
					2015-11-03 05:26:40
	part2_correct_attempt
					['0:01:16', u'27/5']
	part3_correct_attempt
					['0:43:11', u'(27*4/25)^.5']
	part4_correct_attempt
					['0:45:06', u'(12-(27/5))/(27*4/25)^.5']
	part5_incorrect_attempt
					('0:47:20', u'0.0762')
					('0:49:39', u'1 - .99924')
					('0:51:09', u'(1-.99924)/2')
					('0:53:03', u'0.1496111')
					('0:53:20', u'0.0748055')
					('0:55:30', u'0.0748055 + C(27, 12)*(1/5)^12*(4/5)^15')
					('0:56:50', u'C(27, 12)*(1/5)^12*(4/5)^15')
					('0:57:17', u'27!/(12!15!)*(1/5)^12*(4/5)^15')
					('0:57:30', u'0.0748055+27!/(12!15!)*(1/5)^12*(4/5)^15')
					('1:06:40', u'(12-(27/5))/(27*4/25)^.5')
					('1:08:09', u'100 - 99.9251945')
					('1:10:02', u'27!/(12!15!)*(1/5)^12*(4/5)^15 + 0.0748055')
	part5_correct_attempt
					['1:17:50', u'0.000748']

17 Student ID:dkurli

	first_attempt
					2015-11-05 03:11:30
	part2_correct_attempt
					['0:00:54', u'22/4']
	part3_correct_attempt
					['0:14:54', u'sqrt(22*3/16)']
	part4_correct_attempt
					['0:15:39', u'4.5/(sqrt(22*3/16))']
	part5_incorrect_attempt
					('0:15:52', u'Phi(2.21565)')
	part5_correct_attempt
					['0:16:00', u'Q(2.21565)']

18 Student ID:dlt009

	first_attempt
					2015-11-05 08:17:51
	part2_correct_attempt
					['0:00:00', u'21(1/4)']
	part3_correct_attempt
					['0:00:31', u'sqrt [21*.25*0.75] ']
	part4_correct_attempt
					['0:01:40', u'(9-5.25) / sqrt [21*0.25*0.75]']
	part5_incorrect_attempt
					('0:02:14', u'1-Q(9)')
					('0:02:36', u'1-Q(1.88982)')
	part5_correct_attempt
					['0:06:26', u'Q([(9-5.25) / sqrt [21*0.25*0.75] ])']

19 Student ID:dan029

	first_attempt
					2015-11-05 09:16:18
	part2_correct_attempt
					['0:06:47', u'5']
	part3_correct_attempt
					['0:07:40', u'sqrt(3.75)']
	part4_correct_attempt
					['0:16:01', u'(12-5)/sqrt(3.75)']
	part5_incorrect_attempt
					('0:16:01', u'Q(12)')
	part5_correct_attempt
					['0:16:25', u'Q((12-5)/sqrt(3.75))']

20 Student ID:n2patil

	first_attempt
					2015-11-05 02:01:47
	part2_correct_attempt
					['0:15:39', u'5.6']
	part3_correct_attempt
					['0:16:53', u'(4.48)^(1/2)']
	part4_correct_attempt
					['0:28:46', u'(9-5.6)/2.1166']
	part5_incorrect_attempt
					('0:30:02', u'.4147')
					('0:30:09', u'41.47')
					('0:32:48', u'.9147')
					('0:32:55', u'91.47')
					('0:35:06', u'.8554')
					('0:36:32', u'.91466')
	part5_correct_attempt
					['1:49:48', u'Q((9-5.6)/2.1166)']

21 Student ID:j6quach

	first_attempt
					2015-11-05 09:30:45
	part2_correct_attempt
					['1:20:29', u'26*1/5']
	part3_correct_attempt
					['1:26:23', u'sqrt(26*.2*.8)']
	part4_correct_attempt
					['1:29:43', u'(12-5.2)/2.03961']
	part5_incorrect_attempt
					('1:29:43', u'Q(12)')
					('1:31:02', u'Q(11)')
					('1:38:22', u'1 - Phi(12)')
					('1:42:23', u'1 - Phi(12) + 9657700*(.2^12)*(.8^14)')
	part5_correct_attempt
					['1:49:07', u'1 - Phi(3.33397)']

22 Student ID:syc078

	first_attempt
					2015-11-05 03:08:01
	part2_correct_attempt
					['22:55:37', u'(1/4)(28)']
	part3_correct_attempt
					['23:03:04', u'sqrt(7*(1-0.25))']
	part4_correct_attempt
					['23:07:21', u'(13-7)/(sqrt(7*(1-0.25)))']
	part5_incorrect_attempt
					('23:11:27', u'1-0.0045')
					('23:11:34', u'0.0045')
	part5_correct_attempt
					['23:11:49', u'0.0044']

23 Student ID:haw081

	first_attempt
					2015-11-01 22:30:24
	part2_correct_attempt
					['0:06:56', u'1/6*30']
	part3_correct_attempt
					['0:11:15', u'sqrt(30(1/6)(5/6))']
	part4_correct_attempt
					['0:11:58', u'(13-5)/sqrt(30(1/6)(5/6))']
	part5_incorrect_attempt
					('0:20:34', u'0.00003')
					('0:22:44', u'.00004')
					('0:23:01', u'.00005')
	part5_correct_attempt
					['1 day, 3:17:01', u'Q((13-5)/sqrt(30(1/6)(5/6)))']

24 Student ID:dcastlem

	first_attempt
					2015-11-03 00:40:08
	part2_correct_attempt
					['1:14:44', u'1/5*26']
	part3_correct_attempt
					['1:15:49', u'sqrt(26*1/5*4/5)']
	part4_correct_attempt
					['1:17:15', u'(10-5.2)/2.03961']
	part5_incorrect_attempt
					('1:24:29', u'.0031')
					('1:24:34', u'.003')
					('1 day, 23:52:58', u'Q(14/sqrt(66))')
					('1 day, 23:53:43', u'Q(10/sqrt(66))')
					('1 day, 23:54:16', u'Q(10/2.03961)')
					('1 day, 23:54:28', u'Q(10/sqrt(2.03961))')
					('1 day, 23:58:43', u'Q(10-5.2/(sqrt(26*1/5*4/5)))')
	part5_correct_attempt
					['1 day, 23:58:54', u'Q((10-5.2)/2.03961)']

25 Student ID:vqt004

	first_attempt
					2015-11-06 05:57:50
	part2_correct_attempt
					['0:10:09', u'30*1/5']
	part3_correct_attempt
					['0:10:45', u'sqrt(4/25*30)']
	part4_correct_attempt
					['0:14:25', u'(13-30*1/5)/sqrt(4/25*30)']
	part5_incorrect_attempt
					('0:14:25', u'1-Phi(13)')
					('0:15:09', u'Phi(13)')
	part5_correct_attempt
					['0:16:13', u'Q((13-30*1/5)/sqrt(4/25*30))']

26 Student ID:jew037

	first_attempt
					2015-11-05 00:24:42
	part2_correct_attempt
					['0:01:00', u'26/6']
	part3_correct_attempt
					['0:01:44', u'sqrt(26*(1/6)*(1-(1/6)))']
	part4_correct_attempt
					['0:05:38', u'( 12 - (26* (1/6)) ) / ( sqrt( 26 / 6 * (1-1/ 6)) )']
	part5_incorrect_attempt
					('0:08:27', u'(12-(26*(1/6))) / ( sqrt( 26 / 6 * (1-1/ 6)))')
	part5_correct_attempt
					['1 day, 2:39:35', u'Q((12-(26*(1/6))) / ( sqrt( 26 / 6 * (1-1/ 6))))']

27 Student ID:cfgutier

	first_attempt
					2015-11-06 20:04:59
	part2_correct_attempt
					['0:00:28', u'21/5']
	part3_correct_attempt
					['0:08:26', u'(21*(1/5)*(4/5))^(1/2)']
	part4_correct_attempt
					['0:09:13', u'(12 - 21/5)/ (21*(1/5)*(4/5))^(1/2)']
	part5_incorrect_attempt
					('0:11:27', u'1 - 0.9306')
	part5_correct_attempt
					['0:21:21', u'Q(4.25525)']

28 Student ID:jnatale

	first_attempt
					2015-11-05 02:19:36
	part2_correct_attempt
					['0:00:41', u'23/4']
	part3_correct_attempt
					['0:04:44', u'sqrt(23*(1/4)*(1-.25))']
	part4_correct_attempt
					['0:05:06', u'(13-(23/4))/(sqrt(23*(1/4)*(1-.25)))']
	part5_incorrect_attempt
					('0:06:20', u'0.5')
					('0:16:10', u'2.33E-4')
					('0:16:38', u'2.326E-4')
					('0:17:27', u'3.369E-4')
	part5_correct_attempt
					['0:19:06', u'Q(3.49119)']

29 Student ID:k4ma

	first_attempt
					2015-11-06 21:29:44
	part2_correct_attempt
					['0:03:46', u'27*(.25)']
	part3_correct_attempt
					['0:04:13', u'sqrt(.25(1-.25)27)']
	part4_correct_attempt
					['0:08:47', u'[12-(27*.25)]/sqrt(.25(1-.25)27)']
	part5_incorrect_attempt
					('0:09:19', u'1-Phi(12)')
	part5_correct_attempt
					['0:10:59', u'1-Phi([12-(27*.25)]/sqrt(.25(1-.25)27))']

30 Student ID:agarango

	first_attempt
					2015-11-06 20:14:19
	part2_correct_attempt
					['0:18:35', u'21*(1/6)']
	part3_correct_attempt
					['3:28:35', u'sqrt(5*21)/6']
	part4_correct_attempt
					['3:41:30', u'(11-(21/6))/(sqrt(5*21)/6)']
	part5_incorrect_attempt
					('3:55:46', u'5.41*10^-6')
					('4:37:16', u'0.00003')
					('4:37:31', u'0.0003')

31 Student ID:avasavad

	first_attempt
					2015-11-04 23:24:31
	part5_incorrect_attempt
					('0:11:56', u'Q(11)')
					('0:12:14', u'Phi(11)')

32 Student ID:zhz159

	first_attempt
					2015-11-05 23:25:57
	part2_correct_attempt
					['0:00:00', u'21/6']
	part3_correct_attempt
					['0:00:00', u'1.707825']
	part4_correct_attempt
					['0:00:00', u'4.391550']
	part5_incorrect_attempt
					('0:00:30', u'0.5412542*10^(-6)')
					('0:00:58', u'5.412542*10^(-6)')
	part5_correct_attempt
					['0:04:11', u'0.0000056273']

33 Student ID:b1yao

	first_attempt
					2015-11-04 19:19:02
	part2_correct_attempt
					['0:11:45', u'(29/6)']
	part3_correct_attempt
					['0:21:04', u'(29*1*5/36)^0.5']
	part4_correct_attempt
					['0:25:23', u'(8-(29/6))/((29*1*5/36)^0.5)']
	part5_incorrect_attempt
					('0:28:30', u'1-5.48*10^-2')
					('0:28:46', u'5.48*10^-2')
					('0:30:04', u'0.9429')
	part5_correct_attempt
					['0:30:11', u'1-0.9429']

34 Student ID:tol003

	first_attempt
					2015-11-03 19:59:02
	part2_correct_attempt
					['0:05:33', u'28*(1/5)']
	part3_correct_attempt
					['0:41:09', u'sqrt(28*(1/5)*(1-(1/5)))']
	part4_correct_attempt
					['0:44:44', u'[9-(28/5)]/2.1166']
	part5_incorrect_attempt
					('0:46:32', u'1-(1/5)')
					('0:48:00', u'[9-(28/5)]/[sqrt(28*(1/5)*(1-(1/5)))]')
					('0:54:38', u'[10-(28/5)]/[sqrt(28*(1/5)*(1-(1/5)))]')
					('1:05:09', u'[10-(28/5)]/2.1166-[9-(28/5)]/2.1166')
					('1:05:50', u'[10-(28/5)]/2.1166')
					('2:48:33', u'1-Phi(9)')
					('2:48:51', u'1-Phi(28/5)')
					('2:49:01', u'1-Phi(1/5)')
	part5_correct_attempt
					['2:49:21', u'1-Phi([9-(28/5)]/2.1166)']

35 Student ID:tcn013

	first_attempt
					2015-11-05 20:47:22
	part2_correct_attempt
					['0:00:00', u'23/6']
	part3_correct_attempt
					['0:05:58', u'sqrt( (1/6)* (5/6) * 23)']
	part4_correct_attempt
					['0:08:29', u'(9-23/6)/1.7873']
	part5_incorrect_attempt
					('0:08:29', u'(9)')
	part5_correct_attempt
					['0:08:56', u'Q(2.89077)']

36 Student ID:atorr

	first_attempt
					2015-11-05 20:12:03
	part2_correct_attempt
					['0:00:54', u'(1/5) * 30']
	part3_correct_attempt
					['0:06:22', u'(30 * 0.2 * 0.8)^0.5']
	part4_correct_attempt
					['0:06:58', u'(10 - 6)/((30 * 0.2 * 0.8)^0.5)']
	part5_incorrect_attempt
					('0:09:40', u'1 - [(10 - 6)/((30 * 0.2 * 0.8)^0.5)/30]')
					('0:09:49', u'1 - [(10 - 6)/((30 * 0.2 * 0.8)^0.5)/10]')
	part5_correct_attempt
					['0:12:16', u'1 - Phi((10 - 6)/((30 * 0.2 * 0.8)^0.5))']

37 Student ID:jhw015

	first_attempt
					2015-11-06 19:14:12
	part3_correct_attempt
					['0:01:17', u'sqrt((29/6) * (5/6))']
	part4_correct_attempt
					['0:01:58', u'(10-(29/6))/sqrt((29/6) * (5/6))']
	part5_incorrect_attempt
					('0:03:23', u'0.9949')
					('0:03:51', u'0.9948')
					('0:04:28', u'0.0057')
					('0:04:53', u'0.057')
					('0:05:40', u'6.20 * 10^-3')
	part5_correct_attempt
					['0:06:53', u'0.005021']

38 Student ID:ssamudra

	first_attempt
					2015-11-05 06:26:43
	part2_correct_attempt
					['0:00:43', u'4.5']
	part3_correct_attempt
					['0:12:50', u'1.9365']
	part4_correct_attempt
					['0:12:50', u'2.32379']
	part5_incorrect_attempt
					('0:12:50', u'0.0102')
					('0:13:58', u'0.9898')
					('0:14:04', u'1 - 0.9898')
					('0:14:19', u'(1 - 0.9898)100')
					('0:16:07', u'2.54 * 10^-6')
					('0:16:15', u'2.54 * 10^-4')
					('0:16:46', u'0.4657')
					('0:16:53', u'0.534')
					('0:17:43', u'1 - 0.9911')
	part5_correct_attempt
					['0:18:35', u'0.01']

39 Student ID:arvenega

	first_attempt
					2015-11-06 23:36:36
	part2_correct_attempt
					['0:00:59', u'29/5']
	part3_correct_attempt
					['0:11:40', u'sqrt((29/5)*(1-(1/5)))']
	part4_correct_attempt
					['0:11:40', u'(9-(29/5))/sqrt((29/5)*(1-(1/5)))']
	part5_incorrect_attempt
					('0:22:58', u'1-0.9306')
	part5_correct_attempt
					['0:23:53', u'1-0.9319']

40 Student ID:aggouw

	first_attempt
					2015-11-04 08:53:06
	part2_correct_attempt
					['0:00:52', u'29(1/5)']
	part3_correct_attempt
					['0:01:16', u'sqrt(29(1/5)*(1-1/5))']
	part4_correct_attempt
					['0:01:57', u'[12-[29(1/5)]]/sqrt(29(1/5)*(1-1/5))']
	part5_incorrect_attempt
					('0:02:04', u'Q([11-[25(1/4)]]/sqrt(25(1/4)*(1-1/4)))')
	part5_correct_attempt
					['0:02:21', u'Q([12-[29(1/5)]]/sqrt(29(1/5)*(1-1/5)))']

41 Student ID:q3wen

	first_attempt
					2015-11-06 19:27:15
	part2_correct_attempt
					['0:10:53', u'5']
	part3_correct_attempt
					['0:10:53', u'2']
	part4_correct_attempt
					['0:10:53', u'2.5']
	part5_incorrect_attempt
					('0:10:53', u'1-Phi(10)')
					('0:11:51', u'Q(10)')
	part5_correct_attempt
					['0:12:14', u'Q(2.5)']

42 Student ID:pthsu

	first_attempt
					2015-10-31 03:41:17
	part2_correct_attempt
					['0:01:10', u'1/5*23']
	part3_correct_attempt
					['0:02:58', u'sqrt(23*1/5*(1-1/5))']
	part4_correct_attempt
					['0:03:05', u'(12-(1/5*23) )/ sqrt(23*1/5*(1-1/5))']
	part5_incorrect_attempt
					('0:04:15', u'Q(11)')
	part5_correct_attempt
					['0:04:35', u'Q((12-(1/5*23) )/ sqrt(23*1/5*(1-1/5)))']

43 Student ID:cprafull

	first_attempt
					2015-11-05 08:58:12
	part2_correct_attempt
					['0:14:16', u'30 * 1/5']
	part3_correct_attempt
					['0:14:57', u'sqrt(30/5 * (4/5))']
	part4_correct_attempt
					['0:15:55', u'(10 - 6)/(sqrt(30/5 * (4/5)))']
	part5_incorrect_attempt
					('18:05:39', u'Q((10 - 6)/(sqrt(30/5 * (4/5))))/(sqrt(30/5 * (4/5)))')
	part5_correct_attempt
					['18:06:26', u'Q((10 - 6)/(sqrt(30/5 * (4/5))))']

44 Student ID:l8ngo

	first_attempt
					2015-11-04 01:12:39
	part2_correct_attempt
					['1 day, 21:43:38', u'21/4']
	part3_correct_attempt
					['1 day, 21:46:20', u'sqrt[21*[1/4]*[1-1/4]]']
	part4_correct_attempt
					['1 day, 21:47:57', u'{11-[21/4]}/sqrt[21*[1/4]*[1-1/4]]']
	part5_incorrect_attempt
					('1 day, 21:53:04', u'1.349^(-3)')
					('1 day, 21:53:34', u'1.8658^(-3)')
	part5_correct_attempt
					['1 day, 21:54:50', u'Q({11-[21/4]}/sqrt[21*[1/4]*[1-1/4]])']

45 Student ID:djk006

	first_attempt
					2015-11-04 00:35:35
	part2_correct_attempt
					['0:25:13', u'27/4']
	part3_correct_attempt
					['1:38:44', u'(27(.25)(.75))^(1/2)']
	part4_correct_attempt
					['1:40:36', u'(14-6.75)/2.25']
	part5_incorrect_attempt
					('1:48:13', u'.0005')
	part5_correct_attempt
					['3:34:59', u'Q((14-6.75)/2.25)']

46 Student ID:klala

	first_attempt
					2015-11-05 06:24:05
	part2_correct_attempt
					['0:09:26', u'28 * (1/6)']
	part3_correct_attempt
					['0:13:03', u'sqrt(28*(1/6)*(5/6))']
	part4_correct_attempt
					['0:13:40', u'(12-(28 * (1/6)))/(sqrt(28*(1/6)*(5/6)))']
	part5_incorrect_attempt
					('0:19:30', u'0.0001078')
	part5_correct_attempt
					['0:23:23', u'1-((1/2)+(1/2)*erf((((12-(28 * (1/6)))/(sqrt(28*(1/6)*(5/6)))))/sqrt(2)))']

47 Student ID:m8woo

	first_attempt
					2015-11-05 21:11:06
	part2_correct_attempt
					['-1 day, 23:57:29', u'1/6 * 30']
	part3_correct_attempt
					['0:09:55', u'[(1/6)*(5/6)*30]^(1/2)']
	part4_correct_attempt
					['0:13:02', u'[11-(1/6 * 30)]/[(1/6)*(5/6)*30]^(1/2)']
	part5_incorrect_attempt
					('0:18:15', u'Q(11)')
	part5_correct_attempt
					['0:18:42', u'Q([11-(1/6 * 30)]/[(1/6)*(5/6)*30]^(1/2))']

48 Student ID:dsriniva

	first_attempt
					2015-11-05 16:50:26
	part2_correct_attempt
					['0:03:10', u'27/6']
	part3_correct_attempt
					['2:33:19', u'sqrt(27*(1/6)(5/6))']
	part4_correct_attempt
					['2:36:08', u'2.32379201545']
	part5_incorrect_attempt
					('2:36:53', u'1-1.072411*10^-2')
					('2:37:17', u'1.072411*10^-2')
					('2:38:47', u'0.0102')
	part5_correct_attempt
					['2:39:18', u'Q(2.32379201545)']

49 Student ID:c1wei

	first_attempt
					2015-11-04 06:53:18
	part2_correct_attempt
					['0:06:47', u'6']
	part3_correct_attempt
					['0:22:21', u'sqrt(6*.8)']
	part4_correct_attempt
					['0:23:09', u'8/2.19089']
	part5_incorrect_attempt
					('0:26:55', u'0.0031')
					('0:29:24', u'.0001')
					('0:29:44', u'.0002')
	part5_correct_attempt
					['0:34:22', u'1-Phi(3.65148)']

50 Student ID:edescobe

	first_attempt
					2015-11-01 09:54:00
	part2_correct_attempt
					['3 days, 1:45:13', u'20/6']
	part3_correct_attempt
					['3 days, 1:50:16', u'( 20 / 6* (1-1/ 6))^(1/2)']
	part4_correct_attempt
					['3 days, 2:11:43', u'(10-20/6)/1.6666']
	part5_incorrect_attempt
					('3 days, 2:16:27', u'C(20,10)*(1/6)^10 * (1-1/6)^10')
					('3 days, 2:17:13', u'184756*(1/6)^10 * (1-1/6)^10')
	part5_correct_attempt
					['3 days, 2:18:17', u'Q(4.00016)']

51 Student ID:asetters

	first_attempt
					2015-11-05 20:08:55
	part2_correct_attempt
					['0:00:00', u'21/6']
	part3_correct_attempt
					['0:04:10', u'sqrt(21/6*(5/6))']
	part4_correct_attempt
					['0:07:14', u'(11-21/6)/sqrt(21/6*(5/6))']
	part5_incorrect_attempt
					('0:07:14', u'C(21,11)*(1/6)^11*(5/6)^(10)')
					('0:12:43', u'1- (7152001806640625/7312316880125952)')
					('0:13:47', u'Q(10)')
					('0:14:22', u'1-Phi(10)')
					('1:07:44', u'Q(10)')
					('1:07:52', u'Q(11)')
					('5:49:20', u'Q(10)')
					('5:49:35', u'1 - Q(10)')
					('5:49:48', u'Q(11)')
					('6:12:07', u'.3')
	part5_correct_attempt
					['6:19:03', u'Q((11-21/6)/sqrt(21/6*(5/6)))']

52 Student ID:etemlock

	first_attempt
					2015-11-06 21:35:14
	part2_correct_attempt
					['0:27:23', u'28/5']
	part3_correct_attempt
					['0:31:26', u'(112/25)^.5']
	part4_correct_attempt
					['0:32:11', u'(13 - 5.6)/2.1166']
	part5_incorrect_attempt
					('0:32:20', u'Q(13)')
	part5_correct_attempt
					['0:32:34', u'Q(3.49617)']

53 Student ID:anvan

	first_attempt
					2015-11-05 08:30:59
	part2_correct_attempt
					['1 day, 5:43:16', u'28(.2)']
	part3_correct_attempt
					['1 day, 5:43:52', u'sqrt(.8 * .2 * 28)']
	part4_correct_attempt
					['1 day, 5:44:49', u'( 10 - 28(.2) ) / sqrt(.8 * .2 * 28)']
	part5_incorrect_attempt
					('1 day, 5:45:31', u'98.1182')
					('1 day, 6:19:46', u'1 - Q(2.0788)')
	part5_correct_attempt
					['1 day, 6:19:56', u'Q(2.0788)']

54 Student ID:acs008

	first_attempt
					2015-11-05 16:06:10
	part2_correct_attempt
					['5:26:25', u'1/5*29']
	part3_correct_attempt
					['5:40:29', u'sqrt(29*1/5*4/5)']
	part4_correct_attempt
					['5:41:54', u'(12-5.8)/2.154']
	part5_incorrect_attempt
					('5:42:10', u'Q(2.87)')
	part5_correct_attempt
					['5:42:18', u'Q(2.87837)']

55 Student ID:habuamar

	first_attempt
					2015-11-03 00:29:11
	part2_correct_attempt
					['0:00:00', u'27*(1/4)']
	part3_correct_attempt
					['0:00:00', u'sqrt(27*(1/4)*(3/4))']
	part4_correct_attempt
					['0:00:00', u'(10-27*(1/4))/(sqrt(27*(1/4)*(3/4)))']
	part5_incorrect_attempt
					('0:00:00', u'1-Q((10-27*(1/4))/(sqrt(27*(1/4)*(3/4))))')
	part5_correct_attempt
					['0:00:30', u'Q((10-27*(1/4))/(sqrt(27*(1/4)*(3/4))))']

56 Student ID:ppanourg

	first_attempt
					2015-11-06 09:57:58
	part2_correct_attempt
					['9:27:31', u'28/5']
	part3_correct_attempt
					['9:30:01', u'sqrt((28/5)(1-1/5))']
	part4_correct_attempt
					['9:31:38', u'(11-28/5)/sqrt((28/5)(1-1/5))']
	part5_incorrect_attempt
					('9:40:11', u'.4946')
					('9:40:59', u'.9946')
	part5_correct_attempt
					['9:42:28', u'1 - .9946']

57 Student ID:flhernan

	first_attempt
					2015-11-03 20:40:09
	part2_correct_attempt
					['0:00:00', u'26/5']
	part3_correct_attempt
					['0:04:04', u'sqrt(26/5*(4/5))']
	part4_correct_attempt
					['0:05:38', u'(11-26/5)/sqrt(26/5*(4/5))']
	part5_incorrect_attempt
					('0:09:05', u'1-(e^-6.25 *6.25^5/5!)')
					('0:09:38', u'1-(e^-2.84 *2.84^11/11!)')
					('1 day, 21:37:34', u'0.00791031029834799')
					('1 day, 22:20:35', u'((11+12+13+14+15+16+17+18+19+20+21+22+23+24+25+26-26/5*16))/sqrt(26/5*(4/5))')
	part5_correct_attempt
					['1 day, 22:24:47', u'1-0.99777']

58 Student ID:tdurrer

	first_attempt
					2015-11-06 05:48:59
	part2_correct_attempt
					['0:09:41', u'4.2']
	part3_correct_attempt
					['0:09:41', u'sqrt((.2)(.8)(21))']
	part4_correct_attempt
					['0:09:41', u'(9-4.2)/(sqrt((.2)(.8)(21)))']
	part5_incorrect_attempt
					('0:12:14', u'4.661189E-3')
	part5_correct_attempt
					['0:22:07', u'.0044']

59 Student ID:cstringh

	first_attempt
					2015-11-04 07:06:43
	part2_correct_attempt
					['0:01:20', u'24*1/6']
	part3_correct_attempt
					['0:06:40', u'sqrt(24*1/6*(1-1/6))']
	part4_correct_attempt
					['0:07:52', u'(12-(24*1/6))/(sqrt(24*1/6*(1-1/6)))']
	part5_incorrect_attempt
					('0:13:31', u'([12]-[24*1/6])/(sqrt(24*1/6*(1-1/6)))')
	part5_correct_attempt
					['0:16:32', u'Q(((12)-(24*1/6))/(sqrt(24*1/6*(1-1/6))))']

60 Student ID:ksrijong

	first_attempt
					2015-11-06 20:22:16
	part2_correct_attempt
					['0:03:45', u'(1/6)*25']
	part3_correct_attempt
					['0:07:53', u'sqrt((1/6)(5/6)(25))']
	part4_correct_attempt
					['0:08:30', u'[8-(1/6)*25]/(sqrt((1/6)(5/6)(25)))']
	part5_incorrect_attempt
					('0:12:33', u'0.0188')
					('0:19:27', u'0.02580125')
					('0:23:14', u'2.27*10^-2')
	part5_correct_attempt
					['0:24:23', u'Q([8-(1/6)*25]/(sqrt((1/6)(5/6)(25))))']

61 Student ID:phodgson

	first_attempt
					2015-11-06 06:40:21
	part2_correct_attempt
					['0:00:00', u'29 * .2']
	part5_incorrect_attempt
					('0:00:00', u'Q(13/29)')
					('0:00:13', u'Phi(13/29)')

62 Student ID:dcgriffi

	first_attempt
					2015-11-07 00:03:12
	part2_correct_attempt
					['0:00:00', u'23/5']
	part3_correct_attempt
					['0:00:41', u'sqrt(23/5*(4/5))']
	part4_correct_attempt
					['0:02:56', u'(8-(23/5))/(sqrt(23/5*(4/5)))']
	part5_incorrect_attempt
					('0:03:08', u'Q((8-(23/5))/(sqrt(23/5*(4/5))))+(8-(23/5))/(sqrt(23/5*(4/5)))')
	part5_correct_attempt
					['0:03:28', u'Q((8-(23/5))/(sqrt(23/5*(4/5))))']

63 Student ID:z2tan

	first_attempt
					2015-11-02 05:28:45
	part2_correct_attempt
					['0:01:04', u'26/5']
	part3_correct_attempt
					['0:27:53', u'(26*0.8*0.2)^0.5']
	part4_correct_attempt
					['0:29:26', u'(12-5.2)/(26*0.8*0.2)^0.5']
	part5_incorrect_attempt
					('0:40:57', u'0.04')
					('0:41:06', u'0.4')
					('0:41:13', u'0.004')
					('0:41:35', u'0.0004')
	part5_correct_attempt
					['0:42:12', u'1-Phi((12-5.2)/(26*0.8*0.2)^0.5)']

64 Student ID:aordookh

	first_attempt
					2015-11-04 22:22:30
	part2_correct_attempt
					['1 day, 7:31:46', u'28/6']
	part3_correct_attempt
					['1 day, 7:39:01', u'(28(1/6)(5/6))^(1/2)']
	part4_correct_attempt
					['1 day, 7:39:01', u'(11-(28/6))/(28(1/6)(5/6))^(1/2)']
	part5_incorrect_attempt
					('1 day, 7:39:01', u'e^(-28/6(11))')
					('1 day, 7:39:43', u'e^(-6/28(11))')
					('1 day, 7:41:13', u'1-Phi(11)')
					('1 day, 9:22:21', u'Q(11)')
					('1 day, 9:25:38', u'1-(1-e^((-6/28)11))')
	part5_correct_attempt
					['1 day, 9:27:05', u'1-Phi((11-(28/6))/(28(1/6)(5/6))^(1/2))']

65 Student ID:kquong

	first_attempt
					2015-11-04 23:52:13
	part2_correct_attempt
					['0:00:00', u'25/6']
	part3_correct_attempt
					['0:00:56', u'sqrt(125/36)']
	part4_correct_attempt
					['0:00:40', u'(9 - (25/6))/sqrt(125/36)']
	part5_incorrect_attempt
					('0:02:03', u'100 - ((9 - (25/6))/sqrt(125/36))')
	part5_correct_attempt
					['3:59:18', u'Q((9 - (25/6))/sqrt(125/36))']

66 Student ID:jhp077

	first_attempt
					2015-11-05 13:19:35
	part2_correct_attempt
					['0:00:57', u'5']
	part3_correct_attempt
					['0:22:54', u'(15)^(1/2) / 2']
	part4_correct_attempt
					['0:24:06', u'(13-5)/ ((15)^(1/2) / 2)']
	part5_incorrect_attempt
					('0:28:01', u'e^(-5*13)')
					('0:28:10', u'e^(-13/5)')
					('0:28:52', u'e^(-13/4)')
					('0:31:16', u'Q(13)')
					('0:31:30', u'1 - Q(13)')
					('0:32:49', u'1-Q(13)')
					('0:33:16', u'1-Q((13-5)/ ((15)^(1/2) / 2))')
	part5_correct_attempt
					['0:33:22', u'Q((13-5)/ ((15)^(1/2) / 2))']

67 Student ID:xweng

	first_attempt
					2015-11-06 00:34:03
	part2_correct_attempt
					['0:15:30', u'22/5']
	part3_correct_attempt
					['0:17:39', u'1.876166']
	part4_correct_attempt
					['0:24:36', u'(9-22/5)/1.8761669']
	part5_incorrect_attempt
					('0:26:39', u'0.4929')
	part5_correct_attempt
					['0:27:08', u'0.5-0.4929']

68 Student ID:v4sharma

	first_attempt
					2015-11-05 22:14:51
	part2_correct_attempt
					['0:07:23', u'4']
	part3_correct_attempt
					['0:51:52', u'sqrt((20)(1/5)(4/5))']
	part4_correct_attempt
					['0:54:44', u'(9-4)/(sqrt((20)(1/5)(4/5)))']
	part5_incorrect_attempt
					('0:57:22', u'0.01')
					('0:57:43', u'0.05')
					('0:59:14', u'0.025')
	part5_correct_attempt
					['1:07:20', u'0.00259434']

69 Student ID:c3chung

	first_attempt
					2015-11-06 11:03:55
	part2_correct_attempt
					['0:02:16', u'1/6(21)']
	part3_correct_attempt
					['0:12:04', u'sqrt(1/6(5/6)(21))']
	part4_correct_attempt
					['0:12:49', u'(9-1/6(21))/sqrt(1/6(5/6)(21))']
	part5_incorrect_attempt
					('0:16:08', u'0.0014')
					('0:16:20', u'0.0007')
					('0:16:33', u'1-0.9986')
					('0:17:10', u'1-0.9994')
					('0:17:19', u'0.0003')
					('0:18:06', u'0.0006')
					('0:18:11', u'0.0003')
					('0:19:18', u'1-0.9993')
					('0:22:29', u'1-0.99872')
	part5_correct_attempt
					['0:22:55', u'0.5-0.49936']

70 Student ID:yos017

	first_attempt
					2015-11-06 08:25:22
	part2_correct_attempt
					['0:01:33', u'23 * 1/4']
	part3_correct_attempt
					['0:07:21', u'(1/4 * (1 - 1/4 ) * 23 )^(1/2)']
	part4_correct_attempt
					['0:24:15', u'[11 - 5.75 ] / 2.07']
	part5_incorrect_attempt
					('0:58:59', u'Q(11)')
					('1:11:38', u'0.9943')
					('1:20:19', u'Q(11)')
					('1:20:28', u'-Q(11)')
					('1:20:56', u'1-Q(11)')
					('1:22:13', u'Phi(11)')
					('1:22:42', u'Phi(2.53)')
	part5_correct_attempt
					['1:23:07', u'1 - Phi(2.53)']

71 Student ID:ajvanega

	first_attempt
					2015-11-05 18:54:48
	part2_correct_attempt
					['7:09:10', u'(1/4)30']
	part3_correct_attempt
					['7:18:34', u'sqrt((30/4)*(.75))']
	part4_correct_attempt
					['7:20:34', u'(12-7.5)/(sqrt((30/4)*(.75)))']
	part5_incorrect_attempt
					('7:24:52', u'.0035')
					('7:25:39', u'.0089')
					('7:25:48', u'1-.0089')
					('7:26:06', u'.0023')
					('7:26:15', u'.0233')
					('7:26:25', u'1-.0233')
					('7:26:51', u'.0294')
					('7:26:59', u'1-.0294')
					('7:29:05', u'.9706')
					('7:29:22', u'.4706')
	part5_correct_attempt
					['7:29:54', u'.0287']

72 Student ID:zig006

	first_attempt
					2015-11-04 21:24:02
	part2_correct_attempt
					['0:00:21', u'7']
	part3_correct_attempt
					['0:34:12', u'((21)^0.5)/2']
	part4_correct_attempt
					['0:38:41', u'1.745743']
	part5_incorrect_attempt
					('0:39:22', u'0.035930')
					('0:39:48', u'0.044565')
	part5_correct_attempt
					['0:41:50', u'Q(1.745743)']

73 Student ID:tpmach

	first_attempt
					2015-11-04 23:01:27
	part2_correct_attempt
					['17:50:50', u'22*(1/5)']
	part3_correct_attempt
					['17:57:41', u'sqrt(1/5(1-1/5)22)']
	part4_correct_attempt
					['18:00:41', u'(9-22/5)/(sqrt(1/5(1-1/5)22))']
	part5_incorrect_attempt
					('18:01:16', u'2*((9-22/5)/(sqrt(1/5(1-1/5)22)))')
					('19:15:40', u'2*2*((9-22/5)/(sqrt(1/5(1-1/5)22)))')
	part5_correct_attempt
					['19:23:57', u'1-Phi((9-22/5)/(sqrt(1/5(1-1/5)22)))']

74 Student ID:any027

	first_attempt
					2015-11-01 20:36:42
	part2_correct_attempt
					['0:02:37', u'27/6']
	part3_correct_attempt
					['1:32:21', u'sqrt( (27*1/6)* (1-1/6) )']
	part4_correct_attempt
					['1:33:24', u'(11 - (27/6)) / (sqrt( (27*1/6)* (1-1/6) ))']
	part5_incorrect_attempt
					('1:33:46', u'Q(11)')
	part5_correct_attempt
					['1:33:54', u'Q((11 - (27/6)) / (sqrt( (27*1/6)* (1-1/6) )))']

75 Student ID:hmnaing

	first_attempt
					2015-11-06 18:32:06
	part2_correct_attempt
					['3:41:28', u'26/4']
	part3_correct_attempt
					['3:52:15', u'sqrt(0.25*0.75*26)']
	part4_correct_attempt
					['3:53:12', u'(13- (26/4))/ (sqrt(0.25*0.75*26))']
	part5_incorrect_attempt
					('3:53:30', u'2 * (13- (26/4))/ (sqrt(0.25*0.75*26))')
					('3:55:38', u'2 * Q(13- (26/4))/ (sqrt(0.25*0.75*26))')
	part5_correct_attempt
					['3:55:57', u'Q((13- (26/4))/ (sqrt(0.25*0.75*26)))']

76 Student ID:j2phung

	first_attempt
					2015-11-05 09:45:24
	part2_correct_attempt
					['0:01:53', u'30/4']
	part3_correct_attempt
					['0:34:15', u'(30*(1/4)*(3/4))^(1/2)']
	part4_correct_attempt
					['0:36:58', u'(11-(30/4))/((30*(1/4)*(3/4))^(1/2))']
	part5_incorrect_attempt
					('0:51:52', u'(1-(.9292))*100')
					('0:52:47', u'(1-(.9306))*100')
					('0:53:10', u'(1-(.9279))*100')
					('0:55:33', u'1-(.9292)')
	part5_correct_attempt
					['0:56:22', u'1-(.9306)']

77 Student ID:wmiao

	first_attempt
					2015-11-05 01:13:16
	part2_correct_attempt
					['21:13:10', u'21*1/5']
	part3_correct_attempt
					['21:16:47', u'(0.2*(1-0.2)*21)^0.5']
	part4_correct_attempt
					['21:16:47', u'(11-21*1/5)/((0.2*(1-0.2)*21)^0.5)']
	part5_incorrect_attempt
					('21:20:12', u'1/21*(11+12+13+14+15+16+17+18+19+20+21)')
					('21:21:09', u'1/21*(1/5*11)')
	part5_correct_attempt
					['21:35:18', u'1-(0.5+0.5erf(((11-21*1/5)/((0.2*(1-0.2)*21)^0.5))/(2^0.5)))']

78 Student ID:volim

	first_attempt
					2015-11-04 23:30:44
	part2_correct_attempt
					['0:48:55', u'23*(1/6)']
	part3_correct_attempt
					['1:09:34', u'[23*(1/6)*(1-(1/6))]^(1/2)']
	part4_correct_attempt
					['1:12:26', u'[9-23*(1/6)]/[23*(1/6)*(1-(1/6))]^(1/2)']
	part5_incorrect_attempt
					('1:18:02', u'50-49.81')
					('1:18:11', u'.50-.4981')
					('1:19:10', u'.19')
	part5_correct_attempt
					['1:19:45', u'Q([9-23*(1/6)]/[23*(1/6)*(1-(1/6))]^(1/2))']

79 Student ID:k3tan

	first_attempt
					2015-11-04 06:07:19
	part2_correct_attempt
					['0:04:54', u'27/6']
	part3_correct_attempt
					['2 days, 17:19:49', u'sqrt(27*5/36)']
	part4_correct_attempt
					['2 days, 17:21:19', u'(11-27/6)/sqrt(27*5/36)']
	part5_incorrect_attempt
					('2 days, 17:24:21', u'0.5-0.49')
					('2 days, 17:24:34', u'0.5-0.4998')
					('2 days, 17:26:27', u'0.0004')
					('2 days, 17:26:45', u'0.004')
					('2 days, 17:26:55', u'0.0004')
					('2 days, 17:27:30', u'0.00039')
					('2 days, 17:27:50', u'0.00040')
					('2 days, 17:28:01', u'0.00042')
					('2 days, 17:28:10', u'0.00038')
					('2 days, 17:29:34', u'0.5-0.0004')
					('2 days, 17:29:40', u'0.5-0.00039')
					('2 days, 17:30:56', u'0.9996')
					('2 days, 17:31:12', u'1-0.9996')
					('2 days, 17:54:19', u'0.00037')
					('2 days, 17:54:26', u'0.00036')
					('2 days, 17:54:36', u'0.00041')
					('2 days, 17:54:42', u'0.00042')
					('2 days, 17:56:00', u'1-0.0004')
					('2 days, 17:56:07', u'1-0.00039')
					('2 days, 17:57:11', u'0.4996')
					('2 days, 17:57:16', u'1-0.4996')
					('2 days, 17:57:25', u'0.5-0.4996')

80 Student ID:asp025

	first_attempt
					2015-11-06 22:08:56
	part2_correct_attempt
					['0:43:48', u'24/6']
	part3_correct_attempt
					['0:49:11', u'[24(1/6)(1-1/6)]^(1/2)']
	part4_correct_attempt
					['1:04:30', u'(12-4)/([24(1/6)(1-1/6)]^(1/2))']
	part5_incorrect_attempt
					('1:06:17', u'Q(12)')
	part5_correct_attempt
					['1:08:32', u'1-Phi((12-4)/([24(1/6)(1-1/6)]^(1/2)))']












