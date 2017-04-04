#Problem 11

    $a = random(-3,-1,1);
    $b = $a + random(2,6,1);
    $lambda = random(0.1, 0.9, 0.1);

    $n1 = random(100,500,10);
    $n2 = random(100,500,10);

    ### CLT simulation

    In this problem, you may use the CLT simulation
    (http://webwork.cse.ucsd.edu/misc/clt.html) to help you find the
    answers.

    ---

    Suppose a sample average is denoted by [`S_n = (\sum_{i=1}^n X_i) /
    n`] and we define [`T_n = (S_n - A) / B`].

    Find the values of [`A`]
    and [`B`] under the following conditions so that [`T_n`] is
    distributed normally with [`\mu = 0`] and [`\sigma = 1`]. Your answers should be correct up to 2 decimal points.

    o  [`X_i \sim \mbox{Uniform}([$a],[$b])`] and [`n = [$n1]`]
        -  A = [________]{Compute("($a+$b)/2")->with(tolType=>'absolute', tolerance=>'0.01')}
        -  B = [________]{Compute("sqrt((($b-$a)**2/12) / $n1)")->with(tolType=>'absolute', tolerance=>'0.01')}

    o  [`X_i \sim \mbox{Exponential}([$lambda])`] and [`n = [$n2]`]
        -  A = [________]{Compute("1/$lambda")->with(tolType=>'absolute', tolerance=>'0.01')}
        -  B = [________]{Compute("sqrt((1/$lambda**2) / $n2)")->with(tolType=>'absolute', tolerance=>'0.01')}


## Part 1

### (109) Mistake Group Wrong_Sign of size 109




### (84) Mistake Group Digits of size 84




### (54) Mistake Group Fraction of size 54




### (4) Mistake Group ['R.1'] of size 4
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(-1+4)/2	|7/2	|[('R.1', 2.0, u'2', u'2')]	|
|1	|(-3+-1)/2	|(1-3)/2	|[('R.1', 2.0, u'2', u'2')]	|
|2	|(-1+5)/2	|360/2	|[('R.1', 2.0, u'2', u'2')]	|




### (2) Mistake Group ['R.0.1'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(-1+4)/2	|(-1+-1+4)/2	|[('R.0.1', 4.0, u'4', u'4')]	|
|1	|(-1+4)/2	|(-1+-1+4)/240	|[('R.0.1', 4.0, u'4', u'4')]	|




### (1) Mistake Group ['R.0.0'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(-1+2)/2	|(-1+1)/2	|[('R.0.0', -1.0, u'-1', u'-1')]	|




### (1) Mistake Group ['R.0.0', 'R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(-3+-1)/2	|(-3+1)/2	|[('R.0.0', -3.0, u'-3', u'-3'), ('R.1', 2.0, u'2', u'2')]	|




### (49) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:dlgoldbe

	first_attempt
					2015-11-07 00:21:38
	part1_incorrect_attempt
					('0:00:00', u'0.25')
	part1_correct_attempt
					['0:03:34', u'0.505']

1 Student ID:apokhare

	first_attempt
					2015-11-05 22:26:12
	part1_incorrect_attempt
					('0:00:00', u'-2')
	part1_correct_attempt
					['0:03:11', u'-1/2']

2 Student ID:jag028

	first_attempt
					2015-11-06 17:40:01
	part1_incorrect_attempt
					('0:00:00', u'-3')
					('0:00:06', u'-2')
					('0:00:12', u'-1')
					('0:20:58', u'-2')
	part1_correct_attempt
					['1:44:03', u'-1.5']

3 Student ID:v4zhang

	first_attempt
					2015-11-06 08:46:07
	part1_incorrect_attempt
					('0:00:00', u'-1')
					('0:01:03', u'-1.5')
	part1_correct_attempt
					['0:03:45', u'-0.5']

4 Student ID:lywong

	first_attempt
					2015-11-05 23:25:58
	part1_incorrect_attempt
					('0:00:00', u'0.0')
	part1_correct_attempt
					['0:16:31', u'2']

5 Student ID:aggouw

	first_attempt
					2015-11-03 21:36:28
	part1_incorrect_attempt
					('0:00:00', u'(-3+1)/2')
	part1_correct_attempt
					['0:00:13', u'0']

6 Student ID:glcohen

	first_attempt
					2015-11-04 20:25:52
	part1_incorrect_attempt
					('0:00:00', u'-2')
	part1_correct_attempt
					['0:05:42', u'.5(-2+0)']

7 Student ID:c1sorian

	first_attempt
					2015-11-05 01:19:59
	part1_incorrect_attempt
					('0:00:00', u'-1')
	part1_correct_attempt
					['0:02:37', u'0']

8 Student ID:atorr

	first_attempt
					2015-11-05 21:08:46
	part1_incorrect_attempt
					('0:00:00', u'-1500')

9 Student ID:asp025

	first_attempt
					2015-11-07 00:32:29
	part1_incorrect_attempt
					('0:00:00', u'0.0')

10 Student ID:krau

	first_attempt
					2015-11-05 03:40:07
	part1_incorrect_attempt
					('0:00:00', u'0.0')
	part1_correct_attempt
					['0:10:20', u'-.999']

11 Student ID:dcrume

	first_attempt
					2015-11-06 21:32:39
	part1_incorrect_attempt
					('0:00:00', u'0 + sqrt(3*(1/12*36))')
					('0:01:28', u'200*sqrt(3*(1/12*36))')
					('0:02:01', u'sqrt(3*(1/12*36))')

12 Student ID:k5law

	first_attempt
					2015-11-04 10:13:41
	part1_incorrect_attempt
					('0:00:00', u'-1')
	part1_correct_attempt
					['1 day, 23:39:51', u'-.5']

13 Student ID:beyounge

	first_attempt
					2015-10-31 00:32:11
	part1_incorrect_attempt
					('0:00:00', u'0.00')
	part1_correct_attempt
					['5 days, 7:37:28', u'-1.00']

14 Student ID:agoldsht

	first_attempt
					2015-11-04 20:58:06
	part1_incorrect_attempt
					('0:00:00', u'-3/2')
	part1_correct_attempt
					['0:09:27', u'(-2+1)/2']

15 Student ID:j5phung

	first_attempt
					2015-11-05 01:52:57
	part1_incorrect_attempt
					('0:00:00', u'-3')
					('0:02:19', u'-2')
					('0:07:45', u'-3')
					('0:00:00', u'-2')
	part1_correct_attempt
					['17:31:53', u'-1']

16 Student ID:n2patil

	first_attempt
					2015-11-05 04:09:09
	part1_incorrect_attempt
					('0:00:00', u'-1')
	part1_correct_attempt
					['0:00:33', u'-2']

17 Student ID:tpmach

	first_attempt
					2015-11-06 02:33:06
	part1_incorrect_attempt
					('0:00:00', u'1-Phi(140)')
	part1_correct_attempt
					['0:03:42', u'1.5']

18 Student ID:syc078

	first_attempt
					2015-11-06 17:24:36
	part1_incorrect_attempt
					('0:00:00', u'(1/2)(4-(-2))')
	part1_correct_attempt
					['0:01:15', u'(1/2)(4+(-2))']

19 Student ID:ttimmons

	first_attempt
					2015-11-04 20:25:06
	part1_incorrect_attempt
					('0:00:00', u'0.0')
	part1_correct_attempt
					['0:02:46', u'-1.0']

20 Student ID:vqt004

	first_attempt
					2015-11-06 07:05:58
	part1_incorrect_attempt
					('0:00:00', u'-1')
	part1_correct_attempt
					['10:20:19', u'0']

21 Student ID:dkurli

	first_attempt
					2015-11-05 03:42:17
	part1_incorrect_attempt
					('0:00:00', u'-3')
	part1_correct_attempt
					['0:08:41', u'-1']

22 Student ID:jeqin

	first_attempt
					2015-11-05 11:02:52
	part1_incorrect_attempt
					('0:00:00', u'1.5')
	part1_correct_attempt
					['0:01:23', u'0.5']

23 Student ID:mnrahman

	first_attempt
					2015-11-07 00:11:41
	part1_incorrect_attempt
					('0:00:00', u'4/2')
					('0:00:41', u'6/2')
	part1_correct_attempt
					['0:03:35', u'2/2']

24 Student ID:yos017

	first_attempt
					2015-11-06 10:58:28
	part1_incorrect_attempt
					('0:00:00', u'0.00')
	part1_correct_attempt
					['8:09:54', u'1/2 * (-1+3)']

25 Student ID:rlhagen

	first_attempt
					2015-10-31 20:53:36
	part1_incorrect_attempt
					('0:00:00', u'0.0')
	part1_correct_attempt
					['0:05:08', u'0.5']

26 Student ID:nnh002

	first_attempt
					2015-11-06 21:58:56
	part1_incorrect_attempt
					('0:00:00', u'-0.49')
	part1_correct_attempt
					['0:00:07', u'-0.5']

27 Student ID:btn023

	first_attempt
					2015-11-06 11:40:16
	part1_incorrect_attempt
					('0:00:00', u'-3')
					('0:03:31', u'1/2*(-3+0)-sqrt(3(1/12(3)^2))')
					('0:00:00', u'0.00')
					('0:00:54', u'-1/3')
	part1_correct_attempt
					['8:27:29', u'-1.5']

28 Student ID:mpanelo

	first_attempt
					2015-11-06 00:14:06
	part1_incorrect_attempt
					('0:00:00', u'-150')
	part1_correct_attempt
					['0:19:38', u'-1']

29 Student ID:kbielawi

	first_attempt
					2015-11-06 00:41:17
	part1_incorrect_attempt
					('0:00:00', u'-3')
	part1_correct_attempt
					['18:34:17', u'-2']

30 Student ID:l8ngo

	first_attempt
					2015-11-06 00:29:13
	part1_incorrect_attempt
					('0:00:00', u'-2')
					('0:00:00', u'-2')
					('0:04:25', u'-3')
					('0:06:10', u'0.0')
					('0:00:00', u'-3')

31 Student ID:ajabasa

	first_attempt
					2015-11-06 22:38:58
	part1_incorrect_attempt
					('0:00:00', u'0.00')
	part1_correct_attempt
					['0:03:54', u'-.5']

32 Student ID:etemlock

	first_attempt
					2015-11-06 22:21:08
	part1_incorrect_attempt
					('0:00:00', u'0.0')
	part1_correct_attempt
					['0:08:42', u'-1']

33 Student ID:muy002

	first_attempt
					2015-11-06 05:21:38
	part1_incorrect_attempt
					('0:00:00', u'-1')
	part1_correct_attempt
					['0:32:25', u'0']

34 Student ID:jtfrankl

	first_attempt
					2015-11-06 19:28:26
	part1_incorrect_attempt
					('0:00:00', u'-.51')
	part1_correct_attempt
					['0:00:59', u'-.50']

35 Student ID:c1wei

	first_attempt
					2015-11-05 05:31:01
	part1_incorrect_attempt
					('0:00:00', u'0.00')
	part1_correct_attempt
					['0:02:47', u'2']

36 Student ID:edcole

	first_attempt
					2015-11-07 00:24:05
	part1_incorrect_attempt
					('0:00:00', u'-2')
	part1_correct_attempt
					['0:01:58', u'0']

37 Student ID:yig015

	first_attempt
					2015-11-06 12:02:44
	part1_incorrect_attempt
					('0:00:00', u'-2')
					('0:10:46', u'-3')
	part1_correct_attempt
					['0:17:13', u'-1.5']

38 Student ID:bpandayk

	first_attempt
					2015-11-06 21:40:10
	part1_incorrect_attempt
					('0:00:00', u'-1/1')
	part1_correct_attempt
					['0:01:29', u'-2']

39 Student ID:jyc018

	first_attempt
					2015-11-06 23:26:27
	part1_incorrect_attempt
					('0:00:00', u'-1')
					('0:01:27', u'-3')
	part1_correct_attempt
					['0:18:00', u'-0.5']

40 Student ID:yypan

	first_attempt
					2015-11-05 06:53:45
	part1_incorrect_attempt
					('0:00:00', u'0.00')
	part1_correct_attempt
					['0:10:34', u'1.00']

41 Student ID:rohan

	first_attempt
					2015-11-07 00:36:01
	part1_incorrect_attempt
					('0:00:00', u'1/10')
					('0:00:05', u'1/5')

42 Student ID:ajvanega

	first_attempt
					2015-11-06 17:23:46
	part1_incorrect_attempt
					('0:00:00', u'(1/2)(6)')
					('0:00:00', u'(1/2)(5-(-1))')
	part1_correct_attempt
					['0:02:14', u'(1/2)(5+(-1))']

43 Student ID:jmiclat

	first_attempt
					2015-11-07 00:01:48
	part1_incorrect_attempt
					('0:00:00', u'-1')
	part1_correct_attempt
					['0:07:24', u'-2']

44 Student ID:cagatep

	first_attempt
					2015-11-06 19:58:49
	part1_incorrect_attempt
					('0:00:00', u'-3')
	part1_correct_attempt
					['0:15:43', u'0']

45 Student ID:ytc012

	first_attempt
					2015-11-05 23:24:03
	part1_incorrect_attempt
					('0:00:00', u'0.1')
					('0:00:00', u'0.2')
					('0:00:02', u'0.21')
	part1_correct_attempt
					['9:32:09', u'0.5']

46 Student ID:mtrafeca

	first_attempt
					2015-11-05 22:01:56
	part1_incorrect_attempt
					('0:00:00', u'1/.8')
	part1_correct_attempt
					['0:10:11', u'3/2']

47 Student ID:klala

	first_attempt
					2015-11-05 07:20:14
	part1_incorrect_attempt
					('0:00:00', u'-1')
	part1_correct_attempt
					['0:02:23', u'-2']

48 Student ID:j2phung

	first_attempt
					2015-11-05 20:43:41
	part1_incorrect_attempt
					('0:00:00', u'0.0')
	part1_correct_attempt
					['0:10:50', u'1']












## Part 2

### (212) Mistake Group Digits of size 212




### (65) Mistake Group Wrong_Sign of size 65




### (16) Mistake Group ['R.0.0.1'] of size 16
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|sqrt((3--2)^2/12/340)	|(340/12(3+2)^2)^(1/2)	|[('R.0.0.1', 12.0, u'12', u'12')]	|
|1	|sqrt((3--2)^2/12/340)	|(340/12*(3+2)^2)^(1/2)	|[('R.0.0.1', 12.0, u'12', u'12')]	|
|2	|sqrt((3--2)^2/12/340)	|(1/12*(5/2)^2)(340^(1/2))	|[('R.0.0.1', 12.0, u'12', u'12')]	|
|3	|sqrt((3--2)^2/12/340)	|(1/12*(5/2)^2)/(340^(1/2))	|[('R.0.0.1', 12.0, u'12', u'12')]	|
|4	|sqrt((3--2)^2/12/340)	|(1/12*(5/2)^2)/340	|[('R.0.0.1', 12.0, u'12', u'12')]	|
|5	|sqrt((3--2)^2/12/340)	|(340/12*(5/2)^2)^(1/2)	|[('R.0.0.1', 12.0, u'12', u'12')]	|
|6	|sqrt((-1--3)^2/12/490)	|sqrt(1/12(1+3)^2/490)	|[('R.0.0.1', 12.0, u'12', u'12')]	|
|7	|sqrt((5--1)^2/12/400)	|sqrt((1/12)(5-(-1))^2)	|[('R.0.0.1', 12.0, u'12', u'12')]	|
|8	|sqrt((4--2)^2/12/480)	|sqrt((1/12)((4+2)^2))	|[('R.0.0.1', 12.0, u'12', u'12')]	|
|9	|sqrt((5--1)^2/12/400)	|sqrt((1/12)(5+(-1))^2)	|[('R.0.0.1', 12.0, u'12', u'12')]	|
|10	|sqrt((4--2)^2/12/480)	|sqrt((1/12)((4-(-2))^2))	|[('R.0.0.1', 12.0, u'12', u'12')]	|
|11	|sqrt((3--3)^2/12/380)	|1/12*(3-(-3))^2*sqrt(380)	|[('R.0.0.1', 12.0, u'12', u'12')]	|
|12	|sqrt((3--3)^2/12/380)	|sqrt(1/12*(3-(-3))^2)	|[('R.0.0.1', 12.0, u'12', u'12')]	|
|13	|sqrt((3--1)^2/12/200)	|[(1/12 * [(3 - (-1))^0.5])]^0.5	|[('R.0.0.1', 12.0, u'12', u'12')]	|
|14	|sqrt((3--1)^2/12/200)	|[(1/12 * [(3 - (-1))^2])]^0.5	|[('R.0.0.1', 12.0, u'12', u'12')]	|
|15	|sqrt((0--3)^2/12/100)	|sqrt((36/12)/180)	|[('R.0.0.1', 12.0, u'12', u'12')]	|




### (15) Mistake Group ['R.0.1'] of size 15
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|sqrt((0--3)^2/12/500)	|sqrt((3)^(2/12)/500)	|[('R.0.1', 500.0, u'500', u'500')]	|
|1	|sqrt((4--2)^2/12/350)	|sqrt((6^(2/12))/350)	|[('R.0.1', 350.0, u'350', u'350')]	|
|2	|sqrt((3--1)^2/12/220)	|sqrt(4/220)	|[('R.0.1', 220.0, u'220', u'220')]	|
|3	|sqrt((3--1)^2/12/220)	|sqrt(4^2/220)	|[('R.0.1', 220.0, u'220', u'220')]	|
|4	|sqrt((2--2)^2/12/430)	|0.25*430/7	|[('R.0.1', 430.0, u'430', u'430')]	|
|5	|sqrt((2--2)^2/12/110)	|sqrt(1/110)	|[('R.0.1', 110.0, u'110', u'110')]	|
|6	|sqrt((1--1)^2/12/210)	|((2^(1/6))/210)^(1/2)	|[('R.0.1', 210.0, u'210', u'210')]	|
|7	|sqrt((3--2)^2/12/320)	|sqrt(5^(2/12)/320)	|[('R.0.1', 320.0, u'320', u'320')]	|
|8	|sqrt((-1--3)^2/12/310)	|sqrt(4/310)	|[('R.0.1', 310.0, u'310', u'310')]	|
|9	|sqrt((3--2)^2/12/370)	|(1/370) * ((1/12(-2-3)2))	|[('R.0.1', 370.0, u'370', u'370')]	|
|10	|sqrt((3--2)^2/12/370)	|(1/370) * (1/12(-2-3)2)	|[('R.0.1', 370.0, u'370', u'370')]	|
|11	|sqrt((3--2)^2/12/370)	|(1/370) * (1/12(-2-3)^2)	|[('R.0.1', 370.0, u'370', u'370')]	|
|12	|sqrt((0--3)^2/12/350)	|(9/350)^(1/2)	|[('R.0.1', 350.0, u'350', u'350')]	|
|13	|sqrt((3--2)^2/12/410)	|sqrt(((3+2)^(2/12)) / 410)	|[('R.0.1', 410.0, u'410', u'410')]	|
|14	|sqrt((3--2)^2/12/410)	|sqrt(((3+2)**(2/12)) / 410)	|[('R.0.1', 410.0, u'410', u'410')]	|




### (8) Mistake Group ['R.0.0'] of size 8
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|sqrt((1--1)^2/12/420)	|((((1-(-1))^2)/12)^(1/2))/420	|[('R.0.0', 0.3333333333333333, u'(1--1)^2/12', u'((1-(-1))^2)/12')]	|
|1	|sqrt((1--2)^2/12/490)	|sqrt(((1/12)(1+2)^2))/490	|[('R.0.0', 0.75, u'(1--2)^2/12', u'(1/12)(1+2)^2')]	|
|2	|sqrt((1--3)^2/12/160)	|sqrt(4^2/12)/160	|[('R.0.0', 1.3333333333333333, u'(1--3)^2/12', u'4^2/12')]	|
|3	|sqrt((4--2)^2/12/480)	|(sqrt((1/12)((4-(-2))^2)))/480	|[('R.0.0', 3.0, u'(4--2)^2/12', u'(1/12)((4-(-2))^2)')]	|
|4	|sqrt((3--2)^2/12/410)	|sqrt((3+2)^2/12) / 410	|[('R.0.0', 2.0833333333333335, u'(3--2)^2/12', u'(3+2)^2/12')]	|
|5	|sqrt((2--2)^2/12/230)	|sqrt(16/12) / 230	|[('R.0.0', 1.3333333333333333, u'(2--2)^2/12', u'16/12')]	|
|6	|sqrt((0--3)^2/12/100)	|sqrt(((1.5*6)/12)/180)	|[('R.0.0', 0.75, u'(0--3)^2/12', u'(1.5*6)/12')]	|




### (6) Mistake Group ['R.0.0.1', 'R.0.1'] of size 6
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.1', 'R.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|sqrt((4--1)^2/12/240)	|sqrt((5/12)/240)	|[('R.0.0.1', 12.0, u'12', u'12'), ('R.0.1', 240.0, u'240', u'240')]	|
|1	|sqrt((-1--3)^2/12/170)	|sqrt(25/12/170)	|[('R.0.0.1', 12.0, u'12', u'12'), ('R.0.1', 170.0, u'170', u'170')]	|
|2	|sqrt((0--3)^2/12/100)	|sqrt((36/12)/100)	|[('R.0.0.1', 12.0, u'12', u'12'), ('R.0.1', 100.0, u'100', u'100')]	|
|3	|sqrt((0--3)^2/12/100)	|sqrt((18/12)/100)	|[('R.0.0.1', 12.0, u'12', u'12'), ('R.0.1', 100.0, u'100', u'100')]	|
|4	|sqrt((1--3)^2/12/330)	|sqrt((36/12)/330)	|[('R.0.0.1', 12.0, u'12', u'12'), ('R.0.1', 330.0, u'330', u'330')]	|




### (2) Mistake Group ['R.0.0.0.1', 'R.0.0.1', 'R.0.1'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0.1', 'R.0.0.1', 'R.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|sqrt((1--1)^2/12/210)	|sqrt((-1-1)^2 /12* 210)	|[('R.0.0.0.1', 2.0, u'2', u'2'), ('R.0.0.1', 12.0, u'12', u'12'), ('R.0.1', 210.0, u'210', u'210')]	|
|1	|sqrt((0--3)^2/12/480)	|sqrt((6**2/12)/480)	|[('R.0.0.0.1', 2.0, u'2', u'2'), ('R.0.0.1', 12.0, u'12', u'12'), ('R.0.1', 480.0, u'480', u'480')]	|




### (2) Mistake Group ['R.0.0.0', 'R.0.1'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0', 'R.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|sqrt((5--1)^2/12/190)	|sqrt((36/10)/190)	|[('R.0.0.0', 36.0, u'(5--1)^2', u'36'), ('R.0.1', 190.0, u'190', u'190')]	|
|1	|sqrt((0--3)^2/12/480)	|sqrt((3**2/6)/480)	|[('R.0.0.0', 9.0, u'(0--3)^2', u'3**2'), ('R.0.1', 480.0, u'480', u'480')]	|




### (1) Mistake Group ['R.0.0.0.0.0'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|sqrt((3--2)^2/12/410)	|sqrt((3+2)^1/6) / 410	|[('R.0.0.0.0.0', 3.0, u'3', u'3')]	|




### (118) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:apokhare

	first_attempt
					2015-11-05 22:29:23
	part2_incorrect_attempt
					('0:00:00', u'sqrt(25/12)')
	part2_correct_attempt
					['0:01:53', u'sqrt((25/12)/370)']

1 Student ID:v4zhang

	first_attempt
					2015-11-06 08:49:52
	part2_incorrect_attempt
					('0:01:43', u'0.25')
					('0:04:49', u'sqrt(12)-0.5')
					('0:05:23', u'.05')
					('0:08:46', u'0.1')
					('0:10:54', u'0.06')
	part2_correct_attempt
					['0:11:07', u'0.07']

2 Student ID:kvass

	first_attempt
					2015-11-06 23:17:55
	part2_incorrect_attempt
					('-1 day, 23:54:43', u'(-1+3)**2/12')
					('-1 day, 23:55:03', u'(1-3)**2/12')
					('-1 day, 23:55:38', u'(-3+1)**2/12')
					('0:00:00', u'(-3-1)**2/12/310')
					('0:00:08', u'(-3-1)**2/12')
					('0:00:44', u'(-1+3)**2/12')
	part2_correct_attempt
					['0:03:17', u'sqrt(((-1+3)**2/12) / 310)']

3 Student ID:kbielawi

	first_attempt
					2015-11-06 19:15:34
	part2_incorrect_attempt
					('-1 day, 23:54:24', u'0.54')
					('-1 day, 23:55:49', u'0.054')
					('0:01:10', u'0.25')
	part2_correct_attempt
					['0:01:19', u'0.025']

4 Student ID:ssamudra

	first_attempt
					2015-11-05 07:11:16
	part2_incorrect_attempt
					('0:00:47', u'2.0833')
					('0:01:08', u'1.4433')
					('0:02:13', u'0.25')
					('16:10:10', u'0.045')
					('16:10:48', u'0.04')
					('16:10:54', u'0.4')
					('16:14:40', u'2.08333')

5 Student ID:dkurli

	first_attempt
					2015-11-05 03:50:58
	part2_incorrect_attempt
					('-1 day, 23:53:02', u'.2')
	part2_correct_attempt
					['0:00:00', u'.05']

6 Student ID:j5phung

	first_attempt
					2015-11-05 19:24:50
	part2_incorrect_attempt
					('-1 day, 6:35:08', u'-1+sqrt(24)')
					('-1 day, 6:35:29', u'3.90')
					('-1 day, 23:48:08', u'2sqrt(430)')
					('-1 day, 23:48:40', u'2*430')
					('0:10:05', u'0.6')
					('0:10:23', u'0.5')
	part2_correct_attempt
					['0:11:09', u'0.05']

7 Student ID:jyc018

	first_attempt
					2015-11-06 23:44:27
	part2_incorrect_attempt
					('-1 day, 23:42:00', u'0.057')
	part2_correct_attempt
					['0:00:00', u'0.08']

8 Student ID:vqt004

	first_attempt
					2015-11-06 17:26:17
	part2_incorrect_attempt
					('-1 day, 13:53:38', u'sqrt(3)')
					('-1 day, 23:49:41', u'1/9')
					('-1 day, 23:49:57', u'sqrt(1/3)')
					('-1 day, 23:59:49', u'sqrt(1*4/12)')
					('0:00:00', u'(1*4/12)')
	part2_correct_attempt
					['0:09:34', u'sqrt(1/12*(2)^2/170)']

9 Student ID:r9jiang

	first_attempt
					2015-11-05 06:08:15
	part2_incorrect_attempt
					('0:00:00', u'0.50')
	part2_correct_attempt
					['0:01:21', u'0.15']

10 Student ID:rlhagen

	first_attempt
					2015-10-31 20:58:44
	part2_incorrect_attempt
					('-1 day, 23:54:52', u'1.0')
					('0:00:00', u'0.7')
					('0:00:15', u'0.6')
					('0:00:20', u'0.5')
					('0:00:31', u'0.8')
					('0:00:52', u'0.9')
					('0:00:58', u'0.65')
					('0:01:29', u'1.0')
	part2_correct_attempt
					['0:02:19', u'0.07']

11 Student ID:btn023

	first_attempt
					2015-11-06 20:07:45
	part2_incorrect_attempt
					('-1 day, 22:23:04', u'1.00')
					('-1 day, 22:23:58', u'1/3')
					('0:00:22', u'1.0')
					('0:01:48', u'.1')
					('0:02:13', u'.15')
	part2_correct_attempt
					['0:05:04', u'.06']

12 Student ID:lalacson

	first_attempt
					2015-11-05 09:00:30
	part2_incorrect_attempt
					('0:00:45', u'sqrt(6^(2/12))')
	part2_correct_attempt
					['0:02:07', u'sqrt((6^2/12)/210)']

13 Student ID:mpanelo

	first_attempt
					2015-11-06 00:33:44
	part2_incorrect_attempt
					('-1 day, 23:40:22', u'sqrt(50)')
					('-1 day, 23:46:15', u'sqrt(7500)')
	part2_correct_attempt
					['0:00:00', u'.047']

14 Student ID:l8ngo

	first_attempt
					2015-11-06 05:29:14
	part2_incorrect_attempt
					('0:00:00', u'1.0')
					('0:00:00', u'0.0001')
					('0:00:00', u'0.05')
					('0:00:00', u'0.046')
					('0:00:00', u'0.0445')
					('0:00:00', u'0.0475')
					('0:00:00', u'0.0455')
					('0:00:00', u'0.00005')
					('0:00:00', u'0.0455')
					('0:00:00', u'0.127')

15 Student ID:dsriniva

	first_attempt
					2015-11-05 19:54:37
	part2_incorrect_attempt
					('0:00:00', u'0.1')
					('0:00:18', u'0.13')
					('0:00:25', u'0.15')
					('0:00:39', u'0.14')
					('0:00:43', u'0.12')
					('0:00:52', u'0.13')
					('0:00:57', u'0.16')
					('0:01:10', u'0.11')
					('0:01:51', u'0.12')
					('0:02:14', u'0.117')
	part2_correct_attempt
					['0:06:52', u'0.08']

16 Student ID:abasu

	first_attempt
					2015-11-05 06:25:19
	part2_incorrect_attempt
					('0:00:35', u'0.85')
	part2_correct_attempt
					['0:02:05', u'0.05']

17 Student ID:sayao

	first_attempt
					2015-11-04 02:03:54
	part2_incorrect_attempt
					('0:00:33', u'3.5')
					('1 day, 14:41:01', u'.4')
	part2_correct_attempt
					['1 day, 14:43:00', u'.11']

18 Student ID:asp025

	first_attempt
					2015-11-07 00:32:29
	part2_incorrect_attempt
					('0:00:00', u'1.0')
					('0:00:00', u'(360)^(1/2)')

19 Student ID:achava

	first_attempt
					2015-11-06 09:44:04
	part2_incorrect_attempt
					('0:04:54', u'0.5')
					('0:14:24', u'.05')
	part2_correct_attempt
					['0:14:44', u'.04']

20 Student ID:c1wei

	first_attempt
					2015-11-05 05:33:48
	part2_incorrect_attempt
					('-1 day, 23:57:13', u'1.00')
					('0:00:06', u'.5')
	part2_correct_attempt
					['0:00:33', u'.08']

21 Student ID:mitopete

	first_attempt
					2015-11-07 00:40:45
	part2_incorrect_attempt
					('0:00:00', u'1.0')
					('0:02:27', u'1/4')
					('0:03:50', u'0.25')
	part2_correct_attempt
					['0:11:50', u'0.10']

22 Student ID:starinia

	first_attempt
					2015-11-06 00:21:16
	part2_incorrect_attempt
					('0:00:00', u'2^2/12')
	part2_correct_attempt
					['0:00:46', u'sqrt(2^2/12 /420)']

23 Student ID:yos017

	first_attempt
					2015-11-06 19:08:22
	part2_incorrect_attempt
					('-1 day, 16:44:54', u'200^0.5')
					('-1 day, 23:23:28', u'16/12')
					('-1 day, 23:23:46', u'(16/12)^2')
					('-1 day, 23:26:22', u'(16/12)^0.5')
					('-1 day, 23:56:43', u'(4/3)^0.5')
					('0:00:16', u'(1/12 * (3 - (-1))^0.5)')
					('0:00:48', u'(1/12 * [(3 - (-1))^0.5])')
	part2_correct_attempt
					['1:59:30', u'0.085']

24 Student ID:akg009

	first_attempt
					2015-11-06 23:03:47
	part2_incorrect_attempt
					('-1 day, 23:40:45', u'0.9')
					('-1 day, 23:42:54', u'.86')
					('-1 day, 23:43:51', u'0.75')
					('-1 day, 23:54:08', u'0.86')
	part2_correct_attempt
					['0:00:00', u'0.048']

25 Student ID:jit002

	first_attempt
					2015-11-06 08:39:06
	part2_incorrect_attempt
					('-1 day, 23:52:59', u'0.15')
					('-1 day, 23:54:14', u'0.11')
					('-1 day, 23:58:57', u'0.08')
	part2_correct_attempt
					['0:00:00', u'0.1']

26 Student ID:druble

	first_attempt
					2015-11-06 01:08:28
	part2_incorrect_attempt
					('-2 days, 23:47:07', u'(1/2)*12^(1/2)')
	part2_correct_attempt
					['0:00:00', u'0.045']

27 Student ID:h4tu

	first_attempt
					2015-11-07 01:00:49
	part2_incorrect_attempt
					('0:00:00', u'0.5')

28 Student ID:jag028

	first_attempt
					2015-11-06 19:24:04
	part2_incorrect_attempt
					('-1 day, 22:31:33', u'3/2')
					('0:00:00', u'.5')
	part2_correct_attempt
					['0:05:16', u'.05']

29 Student ID:quwong

	first_attempt
					2015-11-03 17:59:37
	part2_incorrect_attempt
					('0:00:59', u'(1/3)^0.5')
					('0:01:21', u'1/3')
	part2_correct_attempt
					['0:16:40', u'(1/(3*380))^0.5']

30 Student ID:asetters

	first_attempt
					2015-11-05 21:30:53
	part2_incorrect_attempt
					('0:01:34', u'2.5')
					('0:02:21', u'2.25')
					('4:51:27', u'.5')
					('5:01:22', u'.2')

31 Student ID:abjara

	first_attempt
					2015-11-04 06:30:38
	part2_incorrect_attempt
					('0:02:02', u'.7')
	part2_correct_attempt
					['0:15:12', u'sqrt(9/(12*220))']

32 Student ID:skarimik

	first_attempt
					2015-11-06 05:12:08
	part2_incorrect_attempt
					('-1 day, 23:57:44', u'.10')
	part2_correct_attempt
					['0:00:00', u'.13']

33 Student ID:krau

	first_attempt
					2015-11-05 03:50:27
	part2_incorrect_attempt
					('-1 day, 23:49:40', u'1.0')
	part2_correct_attempt
					['0:00:00', u'.027']

34 Student ID:kthui

	first_attempt
					2015-11-06 09:11:32
	part2_incorrect_attempt
					('0:00:49', u'3^(1/2)/2')
					('0:01:43', u'1/2')
					('0:02:35', u'3/(2*2^0.5)')
					('0:02:55', u'(9/12)^(1/2)')
					('0:03:10', u'(9/12)')
					('0:20:20', u'0.25')
					('0:23:36', u'0.15')
					('0:23:41', u'0.16')
	part2_correct_attempt
					['0:25:23', u'0.06']

35 Student ID:crmirand

	first_attempt
					2015-11-03 07:00:45
	part2_incorrect_attempt
					('0:00:00', u'.07')
	part2_correct_attempt
					['0:00:06', u'.08']

36 Student ID:alhung

	first_attempt
					2015-11-07 00:43:05
	part2_incorrect_attempt
					('0:00:00', u'0.7')
	part2_correct_attempt
					['0:00:06', u'0.07']

37 Student ID:beyounge

	first_attempt
					2015-11-05 08:09:39
	part2_incorrect_attempt
					('-6 days, 16:22:32', u'0.062')
	part2_correct_attempt
					['0:05:57', u'0.0385']

38 Student ID:psable

	first_attempt
					2015-11-06 01:13:48
	part2_incorrect_attempt
					('-1 day, 23:59:43', u'.15')
					('0:00:00', u'0.15')
					('0:01:08', u'0.2')
					('0:01:14', u'0.1')
					('0:01:19', u'0.15')
					('0:08:48', u'.4')
					('0:08:52', u'.45')
					('0:08:57', u'.35')
					('0:09:03', u'.2')
					('0:09:05', u'.25')

39 Student ID:tpmach

	first_attempt
					2015-11-06 02:36:48
	part2_incorrect_attempt
					('0:00:26', u'0.11')
					('0:00:38', u'0.15')
	part2_correct_attempt
					['0:00:56', u'0.125']

40 Student ID:c2qiu

	first_attempt
					2015-11-05 22:59:21
	part2_incorrect_attempt
					('0:00:00', u'sqrt(2^2/12)')
	part2_correct_attempt
					['0:00:42', u'sqrt(((2)^2/12) / 430)']

41 Student ID:rraiyyan

	first_attempt
					2015-11-07 00:31:01
	part2_incorrect_attempt
					('0:02:59', u'0.05')
	part2_correct_attempt
					['0:04:32', u'0.06']

42 Student ID:z3meng

	first_attempt
					2015-11-05 19:05:03
	part2_incorrect_attempt
					('-1 day, 22:57:17', u'0.2')
					('-1 day, 22:57:26', u'0.002')
					('-1 day, 22:58:46', u'0.07')
					('-1 day, 23:59:04', u'0.25')
					('-1 day, 23:59:12', u'0.14')
					('0:00:10', u'2.45')
					('0:00:20', u'0.02')
					('0:00:25', u'0.01')
					('0:00:28', u'0.03')
	part2_correct_attempt
					['0:00:33', u'0.04']

43 Student ID:krkelkar

	first_attempt
					2015-11-02 23:11:06
	part2_incorrect_attempt
					('-1 day, 23:58:41', u'0.115')
	part2_correct_attempt
					['0:00:00', u'.0725']

44 Student ID:cprafull

	first_attempt
					2015-11-06 03:14:19
	part2_incorrect_attempt
					('0:00:49', u'sqrt(36/(12/150))')
					('0:01:13', u'sqrt((3-(-3))^2/(12/150))')
	part2_correct_attempt
					['0:04:41', u'sqrt(((3-(-3))^2)/(12*150))']

45 Student ID:edescobe

	first_attempt
					2015-11-06 09:29:00
	part2_incorrect_attempt
					('0:00:00', u'.9')
					('0:00:39', u'.75')
	part2_correct_attempt
					['0:01:29', u'.09']

46 Student ID:w4shin

	first_attempt
					2015-11-07 00:03:36
	part2_incorrect_attempt
					('0:00:00', u'.025')
					('0:00:17', u'1.00')
	part2_correct_attempt
					['0:00:47', u'.05']

47 Student ID:etemlock

	first_attempt
					2015-11-06 22:29:50
	part2_incorrect_attempt
					('-1 day, 23:51:18', u'1.0')
	part2_correct_attempt
					['0:00:00', u'0.045']

48 Student ID:ggaddi

	first_attempt
					2015-11-05 18:07:04
	part2_incorrect_attempt
					('0:01:12', u'1.00')
	part2_correct_attempt
					['0:03:31', u'0.14']

49 Student ID:ctroncos

	first_attempt
					2015-11-05 17:32:18
	part2_incorrect_attempt
					('0:02:43', u'(-2+1)**2/2 *370')
	part2_correct_attempt
					['0:03:16', u'sqrt(((-2-1)**2/12) / 370)']

50 Student ID:v4sharma

	first_attempt
					2015-11-06 22:49:22
	part2_incorrect_attempt
					('-1 day, 23:54:27', u'0.11')
	part2_correct_attempt
					['-1 day, 23:58:44', u'0.03']

51 Student ID:ralhadda

	first_attempt
					2015-10-31 22:55:26
	part2_incorrect_attempt
					('3:04:49', u'0.05')
	part2_correct_attempt
					['3:10:59', u'0.1']

52 Student ID:dcastlem

	first_attempt
					2015-11-06 04:09:45
	part2_incorrect_attempt
					('0:06:34', u'sqrt(4/930)')
	part2_correct_attempt
					['15:35:52', u'.03']

53 Student ID:v3doan

	first_attempt
					2015-11-07 00:54:13
	part2_incorrect_attempt
					('0:00:05', u'.1')
	part2_correct_attempt
					['0:00:20', u'.075']

54 Student ID:yil035

	first_attempt
					2015-11-05 22:17:40
	part2_incorrect_attempt
					('0:16:06', u'0.25')
					('0:24:25', u'430/4')
					('0:24:45', u'0.25/430')
					('0:43:50', u'0.25/7')
					('8:39:59', u'2/sqrt(3)')
					('8:45:01', u'sqrt(12)')
					('8:54:20', u'sqrt(430)')
	part2_correct_attempt
					['8:54:33', u'1/sqrt(430)']

55 Student ID:sghouse

	first_attempt
					2015-11-06 03:11:18
	part2_incorrect_attempt
					('0:00:00', u'sqrt(5^2/12)')
	part2_correct_attempt
					['0:01:35', u'sqrt(5^2/12/320)']

56 Student ID:wmiao

	first_attempt
					2015-11-06 17:14:37
	part2_incorrect_attempt
					('0:00:00', u'1/(410)^0.5')
					('0:01:16', u'(1-0.5)/(410)^0.5')
					('0:02:27', u'0.5/sqrt(410)')
					('0:06:52', u'0.2/sqrt(410)')
					('0:08:26', u'2/sqrt(410)')
					('0:10:40', u'2.5/sqrt(410)')
					('0:11:57', u'0.5/sqrt(410)')
	part2_correct_attempt
					['0:12:26', u'1.5/sqrt(410)']

57 Student ID:k3tan

	first_attempt
					2015-11-06 23:21:04
	part2_incorrect_attempt
					('0:01:44', u'0.032')
					('0:01:53', u'0.031')
	part2_correct_attempt
					['0:02:45', u'0.09']

58 Student ID:b3hwang

	first_attempt
					2015-11-06 00:55:59
	part2_incorrect_attempt
					('-1 day, 23:50:44', u'.1')
					('0:00:26', u'.5')
					('0:01:50', u'.9')
					('0:01:56', u'.6')

59 Student ID:lywong

	first_attempt
					2015-11-05 23:42:29
	part2_incorrect_attempt
					('-1 day, 23:43:29', u'1.0')
					('0:00:00', u'.1')
	part2_correct_attempt
					['0:00:23', u'.09']

60 Student ID:jix029

	first_attempt
					2015-11-01 21:20:53
	part2_incorrect_attempt
					('0:00:45', u'.74')
	part2_correct_attempt
					['0:00:53', u'.074']

61 Student ID:hkhodada

	first_attempt
					2015-11-05 16:45:06
	part2_incorrect_attempt
					('0:01:27', u'1.0')
					('0:23:15', u'0.4')
					('6:28:31', u'1/110')
					('6:31:40', u'2/sqrt(3)')
					('6:32:16', u'4/sqrt(12)')
					('6:32:37', u'4/(sqrt(12)*110)')
	part2_correct_attempt
					['6:40:37', u'sqrt(4/330)']

62 Student ID:glcohen

	first_attempt
					2015-11-04 20:31:34
	part2_incorrect_attempt
					('0:00:00', u'(1/12)(2^2)')
					('0:01:11', u'4/12')
	part2_correct_attempt
					['1:02:29', u'sqrt((4/12)/140)']

63 Student ID:acvuong

	first_attempt
					2015-11-05 17:44:48
	part2_incorrect_attempt
					('0:00:00', u'4.75')
					('0:01:18', u'4.50')
	part2_correct_attempt
					['0:04:12', u'0.06']

64 Student ID:thk002

	first_attempt
					2015-11-05 08:11:14
	part2_incorrect_attempt
					('-1 day, 23:57:36', u'1.25')
	part2_correct_attempt
					['0:00:00', u'.08']

65 Student ID:mrchin

	first_attempt
					2015-11-06 20:12:14
	part2_incorrect_attempt
					('0:00:13', u'1/3')
					('0:00:24', u'2^(2/12)')
					('0:01:00', u'4/12')
					('0:01:12', u'4/12/410')
					('0:01:24', u'(4/12)/410')
					('0:02:05', u'(sqrt(4)^2/12)/410')
	part2_correct_attempt
					['0:02:57', u'sqrt(((1+3)^2/12) / 410)']

66 Student ID:bakang

	first_attempt
					2015-11-05 16:49:44
	part2_incorrect_attempt
					('0:00:00', u'1.00')
	part2_correct_attempt
					['0:01:09', u'0.03']

67 Student ID:ksmurlo

	first_attempt
					2015-11-05 07:17:37
	part2_incorrect_attempt
					('0:00:00', u'0.09')
					('0:00:37', u'0.1')
					('0:00:48', u'0.08')
	part2_correct_attempt
					['0:01:19', u'0.05']

68 Student ID:ttimmons

	first_attempt
					2015-11-04 20:27:52
	part2_incorrect_attempt
					('-1 day, 23:57:14', u'1.0')
	part2_correct_attempt
					['0:00:56', u'0.101']

69 Student ID:jeqin

	first_attempt
					2015-11-05 11:04:15
	part2_incorrect_attempt
					('-1 day, 23:58:37', u'0.15')
					('-1 day, 23:59:54', u'0.2')
					('0:00:14', u'0.21')
					('0:00:17', u'0.1')
					('0:00:42', u'0.16')
					('0:00:57', u'0.163')
	part2_correct_attempt
					['0:01:00', u'0.13']

70 Student ID:jnatale

	first_attempt
					2015-11-05 01:07:54
	part2_incorrect_attempt
					('0:05:03', u'4/220')
	part2_correct_attempt
					['0:07:10', u'sqrt(4^(1/6)/220)']

71 Student ID:smohiman

	first_attempt
					2015-11-02 05:28:07
	part2_incorrect_attempt
					('0:00:21', u'16/12')
					('0:00:45', u'(16/12)^.5')
					('0:01:11', u'100(16/12)^.5')
					('0:01:30', u'(1600/12)^.5')
					('0:03:02', u'100*(16/12)^.5')
					('0:07:02', u'4/3')
					('0:07:18', u'(4/3)^.5')
					('0:07:41', u'10(4/3)^.5')
	part2_correct_attempt
					['0:16:46', u'0.10(4/3)^.5']

72 Student ID:tol003

	first_attempt
					2015-11-03 23:52:42
	part2_incorrect_attempt
					('0:00:00', u'1.0')
	part2_correct_attempt
					['0:01:31', u'0.057']

73 Student ID:skodigal

	first_attempt
					2015-11-06 06:10:12
	part2_incorrect_attempt
					('0:01:35', u'.1')
	part2_correct_attempt
					['0:02:05', u'.08']

74 Student ID:hachrist

	first_attempt
					2015-11-05 08:27:22
	part2_incorrect_attempt
					('0:01:15', u'1.0')
					('0:03:20', u'0.4')
					('0:04:31', u'0.5')
					('0:05:30', u'0.47')
					('0:05:36', u'0.48')
	part2_correct_attempt
					['0:07:15', u'0.1']

75 Student ID:yeh013

	first_attempt
					2015-11-05 07:42:03
	part2_incorrect_attempt
					('0:00:00', u'0.14')
					('0:00:14', u'0.2')
					('0:00:48', u'0.13')
					('0:01:08', u'0.15')
					('0:01:26', u'0.10')
					('0:01:34', u'0.16')
					('0:01:37', u'0.12')
					('0:01:41', u'0.11')
					('0:03:34', u'0.144')
					('0:03:39', u'0.145')
	part2_correct_attempt
					['0:04:20', u'0.065']

76 Student ID:lguintu

	first_attempt
					2015-11-03 06:14:54
	part2_incorrect_attempt
					('0:00:00', u'1/12(3+2)^2')
					('0:00:36', u'340/12(3+2)^2')
					('0:03:25', u'(340*(3+2)^2)')
					('0:03:39', u'(340*(3+2)^2)^(1/2)')
					('0:04:09', u'(340/12*(3+2)^2)')
					('0:54:50', u'1/340')
					('0:55:11', u'1/(340/12*(1/2)^2)')
					('0:55:24', u'1/((340/12*(1/2)^2))^(1/2)')
					('0:57:39', u'(340^(1/2))')
					('0:59:28', u'(1/12*(5/2)^2)')
					('0:59:55', u'(340/12*(5/2)^2)')
					('1:02:40', u'1/12(3--2)^2')
					('1:03:06', u'1/12(3--2)^2*340')
					('1:03:26', u'1/12(3--2)^2/340')
					('1:07:18', u'1/12(3--2)^2')
					('1:07:41', u'(25/12)/340')
	part2_correct_attempt
					['1:07:55', u'((25/12)/340)^(1/2)']

77 Student ID:arvenega

	first_attempt
					2015-11-06 23:54:23
	part2_incorrect_attempt
					('-1 day, 23:45:38', u'.1')
	part2_correct_attempt
					['0:00:00', u'.15']

78 Student ID:azkong

	first_attempt
					2015-11-06 23:21:26
	part2_incorrect_attempt
					('-1 day, 23:19:53', u'1.73')
	part2_correct_attempt
					['0:00:00', u'0.03']

79 Student ID:volim

	first_attempt
					2015-11-05 01:02:52
	part2_incorrect_attempt
					('0:00:00', u'.17')
					('0:00:07', u'.2')
					('0:00:11', u'.6')
	part2_correct_attempt
					['0:00:34', u'.1']

80 Student ID:rbdoming

	first_attempt
					2015-11-05 19:41:55
	part2_incorrect_attempt
					('-1 day, 23:59:08', u'0.14')
	part2_correct_attempt
					['0:00:00', u'0.15']

81 Student ID:k4ma

	first_attempt
					2015-11-06 22:42:39
	part2_incorrect_attempt
					('0:01:24', u'.1')
	part2_correct_attempt
					['0:01:54', u'.07']

82 Student ID:qfu

	first_attempt
					2015-11-06 03:32:58
	part2_incorrect_attempt
					('0:07:54', u'sqrt(((2)^2/12))')
	part2_correct_attempt
					['0:08:08', u'sqrt(((2)^2/12)/240)']

83 Student ID:tjke

	first_attempt
					2015-11-06 18:04:05
	part2_incorrect_attempt
					('0:04:22', u'sqrt(1/12*(3-(-3))^2)*sqrt(380)')
	part2_correct_attempt
					['0:15:17', u'0.09']

84 Student ID:klala

	first_attempt
					2015-11-05 07:22:37
	part2_incorrect_attempt
					('-1 day, 23:56:13', u'.5')
					('-1 day, 23:56:22', u'.2')
					('-1 day, 23:56:55', u'0.21')
					('-1 day, 23:57:37', u'.1')
	part2_correct_attempt
					['0:00:00', u'0.05']

85 Student ID:b1yao

	first_attempt
					2015-11-05 19:45:44
	part2_incorrect_attempt
					('-1 day, 23:33:59', u'(36/12)^0.5')
					('-1 day, 23:35:25', u'100*(36/12)^0.5')
					('-1 day, 23:36:03', u'(100*36/12)^0.5')
					('0:13:29', u'2.5')
					('0:13:46', u'.5')
	part2_correct_attempt
					['0:50:56', u'sqrt((5-(-1))^2/1200)']

86 Student ID:dmn009

	first_attempt
					2015-11-05 10:36:02
	part2_incorrect_attempt
					('0:07:22', u'.003653')
					('0:09:53', u'.06327')
	part2_correct_attempt
					['0:13:08', u'.05']

87 Student ID:t2shin

	first_attempt
					2015-11-05 22:35:50
	part2_incorrect_attempt
					('0:00:00', u'.8')
					('0:01:43', u'.085')
	part2_correct_attempt
					['0:02:04', u'.06']

88 Student ID:vsamant

	first_attempt
					2015-11-05 04:08:06
	part2_incorrect_attempt
					('1 day, 15:12:43', u'1.5')
					('1 day, 15:13:21', u'(9/12)^(1/2)')
					('1 day, 15:13:49', u'.5')
					('1 day, 15:13:54', u'.1')
					('1 day, 15:20:06', u'2.5')
					('1 day, 15:20:12', u'1.5')
					('1 day, 15:20:29', u'.9')
					('1 day, 15:20:33', u'.8')
					('1 day, 15:20:41', u'.5')
					('1 day, 15:20:46', u'.3')
					('1 day, 15:21:15', u'2.1')
					('1 day, 15:21:21', u'1.9')
					('1 day, 15:21:29', u'1.95')
					('1 day, 15:21:34', u'1.85')
					('1 day, 15:22:50', u'3.5')
					('1 day, 15:22:55', u'4.5')
					('1 day, 15:23:11', u'5.5')

89 Student ID:qtluong

	first_attempt
					2015-11-04 07:07:38
	part2_incorrect_attempt
					('0:00:00', u'0.1')
	part2_correct_attempt
					['0:00:26', u'0.09']

90 Student ID:spw006

	first_attempt
					2015-11-04 03:54:55
	part2_incorrect_attempt
					('0:01:50', u'(6^(2/12))/350')
					('0:02:15', u'sqrt(6^(2/12))/350')
	part2_correct_attempt
					['0:03:07', u'sqrt((36/12)/350)']

91 Student ID:rwthomps

	first_attempt
					2015-11-06 22:23:23
	part2_incorrect_attempt
					('-1 day, 23:58:51', u'0.05')
					('0:00:00', u'0.055')
					('0:00:58', u'0.0575')
	part2_correct_attempt
					['0:03:23', u'0.0275']

92 Student ID:pcdo

	first_attempt
					2015-11-02 19:15:31
	part2_incorrect_attempt
					('0:00:49', u'sqrt((1+3)^(2/12))')
	part2_correct_attempt
					['0:01:33', u'sqrt(((1+3)^(2/12)) / 230)']

93 Student ID:k5law

	first_attempt
					2015-11-06 09:53:32
	part2_incorrect_attempt
					('-2 days, 0:15:05', u'.4')
	part2_correct_attempt
					['0:04:26', u'.065']

94 Student ID:p4kumar

	first_attempt
					2015-11-07 00:33:08
	part2_incorrect_attempt
					('0:00:00', u'1.0')
	part2_correct_attempt
					['0:06:25', u'0.06']

95 Student ID:s2chaudh

	first_attempt
					2015-11-06 06:38:07
	part2_incorrect_attempt
					('0:00:00', u'sqrt(4^2/12)')
	part2_correct_attempt
					['0:01:27', u'sqrt((4^2/12) /160)']

96 Student ID:jmiclat

	first_attempt
					2015-11-07 00:09:12
	part2_incorrect_attempt
					('0:00:00', u'3.5')
	part2_correct_attempt
					['0:00:15', u'0.04']

97 Student ID:syc078

	first_attempt
					2015-11-06 17:25:51
	part2_incorrect_attempt
					('0:03:04', u'(1/12)((4+2)^2)')
					('0:03:20', u'(1/12)((4-(-2))^2)')
	part2_correct_attempt
					['0:12:13', u'sqrt((1/12)((4-(-2))^2)*(1/480))']

98 Student ID:cfgutier

	first_attempt
					2015-11-06 21:09:59
	part2_incorrect_attempt
					('-1 day, 23:46:51', u'.08')
	part2_correct_attempt
					['0:00:00', u'.1']

99 Student ID:s6deng

	first_attempt
					2015-11-05 08:16:48
	part2_incorrect_attempt
					('-1 day, 23:58:45', u'.35')
					('-1 day, 23:58:50', u'.36')
					('0:00:11', u'.35')
					('0:02:45', u'.335')

100 Student ID:jap009

	first_attempt
					2015-11-05 23:11:43
	part2_incorrect_attempt
					('0:02:52', u'1/3')
					('22:42:03', u'1/2')
					('22:42:20', u'1/3')
					('22:45:25', u'(240)^(1/2)')
					('22:45:34', u'1/(240)^(1/2)')
	part2_correct_attempt
					['22:56:51', u'0.035']

101 Student ID:jcl084

	first_attempt
					2015-11-02 20:34:45
	part2_incorrect_attempt
					('0:00:56', u'sqrt(3)^(2/12)/500')
	part2_correct_attempt
					['0:02:50', u'sqrt(((3)**2/12) / 500)']

102 Student ID:hah008

	first_attempt
					2015-11-06 23:44:19
	part2_incorrect_attempt
					('0:01:19', u'sqrt((3+2)^(2/12)) / 410')
	part2_correct_attempt
					['0:03:29', u'sqrt(((2+3)^2/12)/410)']

103 Student ID:ajabasa

	first_attempt
					2015-11-06 22:42:52
	part2_incorrect_attempt
					('-1 day, 23:53:57', u'.1')
					('-1 day, 23:56:06', u'.12')
	part2_correct_attempt
					['0:00:00', u'.07']

104 Student ID:aurodrig

	first_attempt
					2015-11-07 00:18:54
	part2_incorrect_attempt
					('0:00:19', u'sqrt(16/12)')
					('0:01:45', u'1.15470053838 / 230')
	part2_correct_attempt
					['0:17:19', u'sqrt(((16/12)) / 230)']

105 Student ID:hmshah

	first_attempt
					2015-11-05 10:08:19
	part2_incorrect_attempt
					('0:00:00', u'2.5')
					('0:00:00', u'2.2')

106 Student ID:lahawkin

	first_attempt
					2015-11-06 05:13:19
	part2_incorrect_attempt
					('-1 day, 14:45:47', u'1.5')
	part2_correct_attempt
					['0:00:00', u'.038']

107 Student ID:z2tan

	first_attempt
					2015-11-02 06:30:59
	part2_incorrect_attempt
					('0:01:51', u'(470*9/12)^0.5')
					('0:02:02', u'(9/12)^0.5')
					('0:02:40', u'(470(9/12))^0.5')
					('0:05:31', u'(470*3/4)^0.5')
					('0:06:10', u'18.77')
					('0:06:15', u'18.76')
					('0:06:20', u'18.78')
					('0:07:44', u'18.7')
					('0:11:53', u'3/4')
					('0:12:02', u'3/4*470')
	part2_correct_attempt
					['0:13:05', u'(3/4)^0.5/470^0.5']

108 Student ID:yig015

	first_attempt
					2015-11-06 12:19:57
	part2_incorrect_attempt
					('-1 day, 23:58:14', u'0.05')
	part2_correct_attempt
					['0:01:03', u'0.04']

109 Student ID:vasharma

	first_attempt
					2015-11-05 23:37:18
	part2_incorrect_attempt
					('0:01:53', u'.5')
					('0:09:20', u'(1/12)(1+3)^2')
					('0:09:28', u'16/12')
					('0:09:34', u'sqrt(16/12)')
	part2_correct_attempt
					['0:11:12', u'sqrt((16/(400*12)))']

110 Student ID:kgrozav

	first_attempt
					2015-11-06 21:21:49
	part2_incorrect_attempt
					('-1 day, 10:56:18', u'0.25')
					('-1 day, 10:56:29', u'0.50')
					('-1 day, 10:59:27', u'1.25')
					('-1 day, 11:05:51', u'0.75')
	part2_correct_attempt
					['0:01:12', u'0.10']

111 Student ID:xweng

	first_attempt
					2015-11-06 05:04:05
	part2_incorrect_attempt
					('0:00:05', u'1.0')
					('0:02:54', u'0.5')
					('0:08:02', u'0.09')
	part2_correct_attempt
					['0:10:33', u'0.086']

112 Student ID:yypan

	first_attempt
					2015-11-05 07:04:19
	part2_incorrect_attempt
					('-1 day, 23:49:26', u'1.00')
					('0:00:00', u'1.50')
					('0:02:21', u'0.27')
					('0:03:05', u'0.275')
					('0:03:15', u'0.27')
	part2_correct_attempt
					['0:07:05', u'0.11']

113 Student ID:ajvanega

	first_attempt
					2015-11-06 17:26:00
	part2_incorrect_attempt
					('0:00:39', u'(1/12)(5-(-1))^2')
					('0:00:48', u'(1/12)(5+(-1))^2')
					('0:01:53', u'(1/12)(5-(-1))^2')
					('0:14:06', u'sqrt((1/12)(5-(-1))(1/400))')
					('0:14:31', u'sqrt(((1/12)(5-(-1)))(1/400))')
	part2_correct_attempt
					['0:15:12', u'sqrt(((1/12)(5-(-1))^2)(1/400))']

114 Student ID:zig006

	first_attempt
					2015-11-04 22:23:30
	part2_incorrect_attempt
					('0:00:00', u'39.1152')
	part2_correct_attempt
					['0:03:30', u'0.135']

115 Student ID:sthapa

	first_attempt
					2015-11-07 00:14:20
	part2_incorrect_attempt
					('0:27:14', u'sqrt(1.5*6/180)')
	part2_correct_attempt
					['0:27:56', u'sqrt(((1.5*6)/12)/100)']

116 Student ID:gsrandha

	first_attempt
					2015-11-05 21:57:07
	part2_incorrect_attempt
					('-1 day, 23:56:52', u'.5')
					('0:01:49', u'(390 +.5 )/ 9')
					('0:02:03', u'(1 +.5 )/ 9')
					('0:02:19', u'(9 +.5 )/ 1')
					('0:06:10', u'( 1/330+.5 )/ 9')
					('0:06:28', u'( 1/130+.5 )/ 9')
					('3:07:21', u'.5')
					('3:07:37', u'1.5')
					('3:07:44', u'2.5')
					('3:07:51', u'3.5')
					('3:09:40', u'.5')
					('3:11:57', u'2.96410161514')
					('3:12:44', u'3.96410161514')
	part2_correct_attempt
					['22:29:57', u'.043']

117 Student ID:j2phung

	first_attempt
					2015-11-05 20:54:31
	part2_incorrect_attempt
					('-1 day, 23:49:10', u'1.0')
	part2_correct_attempt
					['0:00:00', u'.08']












## Part 3

### (58) Mistake Group Digits of size 58




### (22) Mistake Group Fraction of size 22




### (13) Mistake Group Wrong_Sign of size 13




### (2) Mistake Group ['R.0'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|1/0.4	|1/.2	|[('R.0', 1.0, u'1', u'1')]	|
|1	|1/0.4	|1/0.16	|[('R.0', 1.0, u'1', u'1')]	|




### (2) Mistake Group ['R.1'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|1/0.6	|10/0.6	|[('R.1', 0.6, u'0.6', u'0.6')]	|
|1	|1/0.3	|110*.3	|[('R.1', 0.3, u'0.3', u'.3')]	|




### (54) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:dmn009

	first_attempt
					2015-11-05 10:36:02
	part3_incorrect_attempt
					('0:13:29', u'14.2857')
	part3_correct_attempt
					['0:14:03', u'1.42857']

1 Student ID:dlgoldbe

	first_attempt
					2015-11-07 00:25:12
	part3_incorrect_attempt
					('0:01:43', u'2.47')
					('0:03:24', u'2.48')
					('0:03:50', u'2.475')
					('0:04:33', u'2.479')
					('0:04:42', u'2.481')
					('0:04:47', u'2.482')
					('0:05:07', u'2.46')
	part3_correct_attempt
					['0:05:18', u'2.50']

2 Student ID:ccn001

	first_attempt
					2015-11-05 15:21:56
	part3_incorrect_attempt
					('0:00:00', u'1.11')
	part3_correct_attempt
					['0:01:15', u'1.25']

3 Student ID:t2shin

	first_attempt
					2015-11-05 22:35:50
	part3_incorrect_attempt
					('0:03:15', u'1.4')
					('0:03:37', u'1.45')
	part3_correct_attempt
					['0:06:15', u'1.43']

4 Student ID:vsamant

	first_attempt
					2015-11-05 04:08:06
	part3_incorrect_attempt
					('1 day, 15:14:25', u'.3')
					('1 day, 15:24:30', u'.2')
					('1 day, 15:24:37', u'.3')

5 Student ID:jix029

	first_attempt
					2015-11-01 21:20:53
	part3_incorrect_attempt
					('0:02:29', u'1.24')
					('0:02:35', u'1.23')
	part3_correct_attempt
					['0:02:53', u'1.246']

6 Student ID:quwong

	first_attempt
					2015-11-03 17:59:37
	part3_incorrect_attempt
					('0:02:09', u'0.4')
	part3_correct_attempt
					['0:04:06', u'1/0.4']

7 Student ID:glcohen

	first_attempt
					2015-11-04 20:31:34
	part3_incorrect_attempt
					('0:00:32', u'.5(8)')
	part3_correct_attempt
					['1:00:58', u'((.8)^-1)']

8 Student ID:ssamudra

	first_attempt
					2015-11-05 07:11:16
	part3_incorrect_attempt
					('0:03:38', u'0.5')
					('15:55:15', u'0.8')

9 Student ID:alakamsa

	first_attempt
					2015-11-04 19:16:29
	part3_incorrect_attempt
					('0:00:00', u'1.65')
	part3_correct_attempt
					['0:00:21', u'1.66']

10 Student ID:abjara

	first_attempt
					2015-11-04 06:30:38
	part3_incorrect_attempt
					('0:00:00', u'.9*e^-.9')
	part3_correct_attempt
					['0:14:51', u'1/.9']

11 Student ID:masaro

	first_attempt
					2015-11-04 21:01:36
	part3_incorrect_attempt
					('0:02:06', u'3.35')
	part3_correct_attempt
					['0:02:24', u'3.33']

12 Student ID:l8ngo

	first_attempt
					2015-11-06 05:51:19
	part3_incorrect_attempt
					('0:00:00', u'0.00005')

13 Student ID:tpmach

	first_attempt
					2015-11-06 02:36:48
	part3_incorrect_attempt
					('0:01:57', u'1.7')
					('0:02:09', u'1.65')
					('0:03:43', u'1.57')
					('0:04:08', u'1.679')
	part3_correct_attempt
					['0:04:49', u'1.67']

14 Student ID:beyounge

	first_attempt
					2015-11-05 08:09:39
	part3_incorrect_attempt
					('0:08:00', u'3.35')
					('0:08:52', u'3.30')
	part3_correct_attempt
					['0:13:33', u'10/3']

15 Student ID:j5phung

	first_attempt
					2015-11-05 19:24:50
	part3_incorrect_attempt
					('0:16:03', u'3.3')
					('0:17:03', u'3.32')
	part3_correct_attempt
					['0:17:16', u'3.33']

16 Student ID:p4kumar

	first_attempt
					2015-11-07 00:33:08
	part3_incorrect_attempt
					('0:02:17', u'0.0')
	part3_correct_attempt
					['0:08:22', u'1.11']

17 Student ID:amquinte

	first_attempt
					2015-11-05 06:56:38
	part3_incorrect_attempt
					('0:06:13', u'1.1')
	part3_correct_attempt
					['0:07:11', u'1.11']

18 Student ID:j6quach

	first_attempt
					2015-11-05 08:27:44
	part3_incorrect_attempt
					('0:00:00', u'1.1')
	part3_correct_attempt
					['0:01:43', u'1.11']

19 Student ID:ksmurlo

	first_attempt
					2015-11-05 07:17:37
	part3_incorrect_attempt
					('0:02:53', u'3.3')
					('0:03:23', u'3.31')
					('0:03:45', u'3.32')
	part3_correct_attempt
					['0:03:50', u'3.33']

20 Student ID:v4zhang

	first_attempt
					2015-11-06 08:49:52
	part3_incorrect_attempt
					('0:14:33', u'1.2')
	part3_correct_attempt
					['0:14:50', u'1.25']

21 Student ID:qtluong

	first_attempt
					2015-11-04 07:07:38
	part3_incorrect_attempt
					('0:01:20', u'1.65')
					('0:01:28', u'1.7')
	part3_correct_attempt
					['0:01:32', u'1.66']

22 Student ID:jhc010

	first_attempt
					2015-11-06 11:16:39
	part3_incorrect_attempt
					('0:04:17', u'1.2')
	part3_correct_attempt
					['0:06:40', u'1.42']

23 Student ID:rsmurlo

	first_attempt
					2015-11-05 20:38:49
	part3_incorrect_attempt
					('0:07:33', u'1.45')
					('0:07:44', u'1.4')
					('0:07:58', u'1.5')
					('0:08:08', u'1.35')
					('0:08:20', u'1.33')
					('0:08:31', u'1.30')
	part3_correct_attempt
					['0:25:06', u'1.43']

24 Student ID:jblynch

	first_attempt
					2015-11-05 06:45:22
	part3_incorrect_attempt
					('-1 day, 14:16:46', u'.1')
	part3_correct_attempt
					['0:01:07', u'2.5']

25 Student ID:rlhagen

	first_attempt
					2015-10-31 20:58:44
	part3_incorrect_attempt
					('0:00:26', u'0.5')
	part3_correct_attempt
					['0:03:11', u'1.25']

26 Student ID:c1sorian

	first_attempt
					2015-11-05 01:22:36
	part3_incorrect_attempt
					('0:07:35', u'3.35')
	part3_correct_attempt
					['0:07:43', u'3.34']

27 Student ID:k4ma

	first_attempt
					2015-11-06 22:42:39
	part3_incorrect_attempt
					('0:02:52', u'3.3')
					('0:03:00', u'3.25')
					('0:04:41', u'3.35')
					('0:04:58', u'3.32')
					('0:06:00', u'3.30')
					('0:06:35', u'3.32')
	part3_correct_attempt
					['0:18:56', u'3.33']

28 Student ID:rraiyyan

	first_attempt
					2015-11-07 00:31:01
	part3_incorrect_attempt
					('0:16:54', u'3.5')
					('0:18:18', u'3.35')
	part3_correct_attempt
					['0:19:28', u'3.33']

29 Student ID:hachrist

	first_attempt
					2015-11-05 08:27:22
	part3_incorrect_attempt
					('0:06:12', u'0.1')
					('0:08:56', u'3.3')
					('0:11:05', u'3.32')
	part3_correct_attempt
					['0:11:14', u'3.34']

30 Student ID:kew017

	first_attempt
					2015-11-06 06:25:08
	part3_incorrect_attempt
					('0:00:43', u'1.5')
					('0:18:12', u'1.51')
					('0:18:17', u'1.55')
					('0:20:43', u'1.3')
					('0:20:48', u'1.2')
					('0:20:54', u'1.4')
					('0:23:38', u'1.1')
					('0:24:06', u'1.45')
					('0:24:12', u'1.41')
					('0:25:27', u'1.41')
	part3_correct_attempt
					['0:26:40', u'1.42']

31 Student ID:q3wen

	first_attempt
					2015-11-06 20:39:46
	part3_incorrect_attempt
					('0:00:00', u'3.32')
					('0:00:27', u'3.3')
					('0:00:52', u'3.28')
	part3_correct_attempt
					['0:01:29', u'3.33']

32 Student ID:akalathi

	first_attempt
					2015-11-04 07:09:27
	part3_incorrect_attempt
					('0:03:32', u'1.1')
	part3_correct_attempt
					['0:03:55', u'1.11']

33 Student ID:abasu

	first_attempt
					2015-11-05 06:25:19
	part3_incorrect_attempt
					('0:06:23', u'0.5')
	part3_correct_attempt
					['0:07:25', u'1.25']

34 Student ID:jel075

	first_attempt
					2015-11-05 23:13:00
	part3_incorrect_attempt
					('-1 day, 23:57:00', u'1.65')
	part3_correct_attempt
					['-1 day, 23:57:14', u'1.66']

35 Student ID:asetters

	first_attempt
					2015-11-05 21:30:53
	part3_incorrect_attempt
					('5:04:20', u'1.1')
					('5:04:44', u'1.15')
					('5:04:50', u'1.05')

36 Student ID:sayao

	first_attempt
					2015-11-04 02:03:54
	part3_incorrect_attempt
					('1 day, 14:45:42', u'3.35')
					('1 day, 14:45:50', u'3.4')
					('1 day, 14:45:54', u'3.3')
					('1 day, 14:47:12', u'3.35')
					('1 day, 14:47:46', u'3.31')
					('1 day, 14:47:51', u'3.32')
					('1 day, 14:48:14', u'3.322')
	part3_correct_attempt
					['1 day, 14:49:30', u'3+1/3']

37 Student ID:gsrandha

	first_attempt
					2015-11-05 21:57:07
	part3_incorrect_attempt
					('-1 day, 12:12:14', u'1.0')
	part3_correct_attempt
					['-1 day, 23:59:02', u'5']

38 Student ID:achava

	first_attempt
					2015-11-06 09:44:04
	part3_incorrect_attempt
					('0:16:21', u'1.65')
	part3_correct_attempt
					['0:20:05', u'1.66']

39 Student ID:flhernan

	first_attempt
					2015-11-05 18:27:48
	part3_incorrect_attempt
					('0:05:17', u'3.32')
	part3_correct_attempt
					['0:06:00', u'3.33']

40 Student ID:lahawkin

	first_attempt
					2015-11-06 05:13:19
	part3_incorrect_attempt
					('0:03:59', u'1.4')
	part3_correct_attempt
					['0:04:22', u'1.42']

41 Student ID:bakang

	first_attempt
					2015-11-05 16:49:44
	part3_incorrect_attempt
					('0:03:33', u'1.69')
	part3_correct_attempt
					['0:04:02', u'1.66']

42 Student ID:edcole

	first_attempt
					2015-11-07 00:26:03
	part3_incorrect_attempt
					('0:02:32', u'.1')
					('0:06:38', u'1.1')
	part3_correct_attempt
					['0:06:59', u'1.11']

43 Student ID:dcgriffi

	first_attempt
					2015-11-07 00:45:02
	part3_incorrect_attempt
					('0:02:05', u'1.1')
	part3_correct_attempt
					['0:02:22', u'1.11']

44 Student ID:azkong

	first_attempt
					2015-11-06 23:21:26
	part3_incorrect_attempt
					('0:10:22', u'9.94')
					('0:12:40', u'9.95')
					('0:12:46', u'9.96')
					('0:12:51', u'9.97')
					('0:15:48', u'9.94')
					('0:15:52', u'9.93')
					('0:15:56', u'9.92')
					('0:16:00', u'9.91')
					('0:16:10', u'9.90')
					('0:18:19', u'9.89')
					('0:18:24', u'9.88')
					('0:18:29', u'9.87')
					('0:19:54', u'1.13')
	part3_correct_attempt
					['0:20:05', u'1.12']

45 Student ID:qfu

	first_attempt
					2015-11-06 03:32:58
	part3_incorrect_attempt
					('-1 day, 23:58:10', u'.1')
	part3_correct_attempt
					['0:00:41', u'1/0.7']

46 Student ID:dcastlem

	first_attempt
					2015-11-06 04:09:45
	part3_incorrect_attempt
					('-1 day, 23:59:39', u'10/4')
	part3_correct_attempt
					['15:41:15', u'1.67']

47 Student ID:d6he

	first_attempt
					2015-11-05 18:38:43
	part3_incorrect_attempt
					('-1 day, 23:56:08', u'3.34')
					('0:04:05', u'1.1')
	part3_correct_attempt
					['0:05:38', u'1.11']

48 Student ID:zhw110

	first_attempt
					2015-11-07 00:50:26
	part3_incorrect_attempt
					('0:01:07', u'1.1')
	part3_correct_attempt
					['0:01:24', u'1.11']

49 Student ID:tjke

	first_attempt
					2015-11-06 18:04:05
	part3_incorrect_attempt
					('0:00:00', u'1/0.8*180')
	part3_correct_attempt
					['0:00:34', u'1/0.8']

50 Student ID:jit002

	first_attempt
					2015-11-06 08:39:06
	part3_incorrect_attempt
					('-1 day, 23:56:08', u'1.5')
	part3_correct_attempt
					['-1 day, 23:57:29', u'1.42']

51 Student ID:pnquach

	first_attempt
					2015-11-06 06:22:06
	part3_incorrect_attempt
					('0:00:00', u'1.4')
					('0:00:45', u'1.41')
					('0:01:33', u'1.5')
					('0:03:34', u'1.45')
	part3_correct_attempt
					['0:04:11', u'1.42']

52 Student ID:jhp077

	first_attempt
					2015-11-05 14:38:45
	part3_incorrect_attempt
					('-1 day, 23:52:50', u'0.0')
	part3_correct_attempt
					['0:01:30', u'3.33']

53 Student ID:asp025

	first_attempt
					2015-11-07 00:04:00
	part3_incorrect_attempt
					('0:00:00', u'0.7')












## Part 4

### (50) Mistake Group Digits of size 50




### (36) Mistake Group Wrong_Sign of size 36




### (8) Mistake Group ['R.0.1'] of size 8
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|sqrt(1/(0.1^2)/210)	|sqrt((10)/210)	|[('R.0.1', 210.0, u'210', u'210')]	|
|1	|sqrt(1/(0.1^2)/210)	|sqrt(10/210)	|[('R.0.1', 210.0, u'210', u'210')]	|
|2	|sqrt(1/(0.1^2)/210)	|sqrt((10^-2)/210)	|[('R.0.1', 210.0, u'210', u'210')]	|
|3	|sqrt(1/(0.1^2)/210)	|sqrt((10^-1)/210)	|[('R.0.1', 210.0, u'210', u'210')]	|
|4	|sqrt(1/(0.2^2)/130)	|sqrt((1/.2)^5/130)	|[('R.0.1', 130.0, u'130', u'130')]	|
|5	|sqrt(1/(0.2^2)/330)	|sqrt((0.2^2)/12/330)	|[('R.0.1', 330.0, u'330', u'330')]	|
|6	|sqrt(1/(0.2^2)/330)	|sqrt((0.2^2)/330)	|[('R.0.1', 330.0, u'330', u'330')]	|
|7	|sqrt(1/(0.9^2)/370)	|sqrt((10.9**2) / 370)	|[('R.0.1', 370.0, u'370', u'370')]	|




### (6) Mistake Group ['R.0.0'] of size 6
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|sqrt(1/(0.1^2)/440)	|((1/(0.1^2))^(1/2))/440	|[('R.0.0', 99.99999999999999, u'1/(0.1^2)', u'1/(0.1^2)')]	|
|1	|sqrt(1/(0.1^2)/440)	|((.1)^(-2))^(1/2)/440	|[('R.0.0', 99.99999999999999, u'1/(0.1^2)', u'(.1)^(-2)')]	|
|2	|sqrt(1/(0.9^2)/190)	|sqrt((1/0.81)/350)	|[('R.0.0', 1.2345679012345678, u'1/(0.9^2)', u'1/0.81')]	|
|3	|sqrt(1/(0.9^2)/190)	|sqrt((1/0.9)^2/350)	|[('R.0.0', 1.2345679012345678, u'1/(0.9^2)', u'(1/0.9)^2')]	|
|4	|sqrt(1/(0.9^2)/460)	|sqrt(1/.81)/460	|[('R.0.0', 1.2345679012345678, u'1/(0.9^2)', u'1/.81)')]	|
|5	|sqrt(1/(0.8^2)/250)	|(sqrt(1/.8^2))/250	|[('R.0.0', 1.5624999999999998, u'1/(0.8^2)', u'1/.8^2')]	|




### (2) Mistake Group ['R.0.0.0', 'R.0.0.1.1', 'R.0.1'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0', 'R.0.0.1.1', 'R.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|sqrt(1/(0.9^2)/240)	|sqrt((1/1.9^2)/240)	|[('R.0.0.0', 1.0, u'1', u'1'), ('R.0.0.1.1', 2.0, u'2', u'2'), ('R.0.1', 240.0, u'240', u'240')]	|
|1	|sqrt(1/(0.1^2)/210)	|sqrt((1/10^2)/210)	|[('R.0.0.0', 1.0, u'1', u'1'), ('R.0.0.1.1', 2.0, u'2', u'2'), ('R.0.1', 210.0, u'210', u'210')]	|




### (1) Mistake Group ['R.0.0.0'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|sqrt(1/(0.9^2)/460)	|sqrt(1/.18)/460	|[('R.0.0.0', 1.0, u'1', u'1')]	|




### (1) Mistake Group ['R.0'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|sqrt(1/(0.5^2)/480)	|(1/120)^1/2	|[('R.0', 0.008333333333333333, u'1/(0.5^2)/480', u'(1/120)^1')]	|




### (93) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:gthorn

	first_attempt
					2015-11-05 18:35:33
	part4_incorrect_attempt
					('0:02:38', u'0.7')
	part4_correct_attempt
					['0:03:26', u'0.09']

1 Student ID:kbielawi

	first_attempt
					2015-11-06 19:15:34
	part4_incorrect_attempt
					('0:04:05', u'.09')
					('0:04:17', u'.094')
					('0:05:01', u'.094')
					('0:05:26', u'.09')
					('0:05:33', u'.1')
					('0:06:02', u'.095')
	part4_correct_attempt
					['0:07:54', u'.12']

2 Student ID:mhale

	first_attempt
					2015-11-05 20:51:04
	part4_incorrect_attempt
					('0:02:10', u'0.0058')
	part4_correct_attempt
					['0:02:52', u'0.058']

3 Student ID:l5han

	first_attempt
					2015-11-06 22:23:37
	part4_incorrect_attempt
					('0:00:00', u'0.237')
					('0:00:29', u'0.24')
	part4_correct_attempt
					['0:01:54', u'0.22']

4 Student ID:j5phung

	first_attempt
					2015-11-05 19:24:50
	part4_incorrect_attempt
					('0:12:11', u'0.05')
					('0:14:34', u'0.25')
	part4_correct_attempt
					['0:16:20', u'.32']

5 Student ID:r9jiang

	first_attempt
					2015-11-05 06:08:15
	part4_incorrect_attempt
					('0:03:49', u'0.08')
					('0:06:21', u'0.25')
	part4_correct_attempt
					['0:06:46', u'0.24']

6 Student ID:rlhagen

	first_attempt
					2015-10-31 20:58:44
	part4_incorrect_attempt
					('0:00:26', u'0.5')
	part4_correct_attempt
					['0:03:25', u'0.07']

7 Student ID:btn023

	first_attempt
					2015-11-06 20:07:45
	part4_incorrect_attempt
					('0:08:08', u'.2')
	part4_correct_attempt
					['0:08:35', u'.21']

8 Student ID:arvenega

	first_attempt
					2015-11-06 23:54:23
	part4_incorrect_attempt
					('-1 day, 23:45:38', u'0.26')
	part4_correct_attempt
					['0:00:43', u'.15']

9 Student ID:tstevens

	first_attempt
					2015-11-06 23:27:22
	part4_incorrect_attempt
					('0:02:08', u'100/400')
	part4_correct_attempt
					['0:02:24', u'sqrt(.25)']

10 Student ID:tcuddy

	first_attempt
					2015-11-06 17:40:58
	part4_incorrect_attempt
					('0:09:35', u'1/(390*(.6**2))')
					('0:09:59', u'1/((390*(.6))**2)')
					('0:10:15', u'1/(.6**2)')
					('0:10:31', u'.85')
	part4_correct_attempt
					['0:10:36', u'.085']

11 Student ID:l8ngo

	first_attempt
					2015-11-06 05:51:19
	part4_incorrect_attempt
					('0:00:00', u'0.0455')

12 Student ID:dsriniva

	first_attempt
					2015-11-05 19:54:37
	part4_incorrect_attempt
					('0:04:28', u'1.4')
					('0:05:04', u'1.3')
	part4_correct_attempt
					['0:05:54', u'0.4']

13 Student ID:starinia

	first_attempt
					2015-11-06 00:21:16
	part4_incorrect_attempt
					('0:01:18', u'1/.5^2/240')
	part4_correct_attempt
					['0:01:25', u'sqrt(1/.5^2/240)']

14 Student ID:yos017

	first_attempt
					2015-11-06 19:08:22
	part4_incorrect_attempt
					('-1 day, 23:11:57', u'2* [(1/2)^0.5]')
					('-1 day, 23:13:38', u'0.5* [(2)^0.5]')
					('-1 day, 23:14:20', u'0.5')
					('-1 day, 23:18:23', u'Phi(0.5)')
					('0:03:12', u'1/[(0.5)^2]')
					('0:03:26', u'[1/[(0.5)^2]]^0.5')
	part4_correct_attempt
					['2:01:04', u'0.12']

15 Student ID:akg009

	first_attempt
					2015-11-06 23:03:47
	part4_incorrect_attempt
					('0:00:18', u'0.5')
					('0:01:37', u'0.50')
	part4_correct_attempt
					['0:01:42', u'0.51']

16 Student ID:jhp077

	first_attempt
					2015-11-05 14:38:45
	part4_incorrect_attempt
					('-1 day, 23:52:50', u'1.0')
	part4_correct_attempt
					['0:01:30', u'0.15']

17 Student ID:jit002

	first_attempt
					2015-11-06 08:39:06
	part4_incorrect_attempt
					('-1 day, 23:56:08', u'0.11')
	part4_correct_attempt
					['-1 day, 23:58:26', u'0.08']

18 Student ID:b3hwang

	first_attempt
					2015-11-06 00:55:59
	part4_incorrect_attempt
					('-1 day, 23:50:44', u'.07')

19 Student ID:jag028

	first_attempt
					2015-11-06 19:24:04
	part4_incorrect_attempt
					('0:07:20', u'.5')
	part4_correct_attempt
					['0:26:10', u'.085']

20 Student ID:ccn001

	first_attempt
					2015-11-05 15:21:56
	part4_incorrect_attempt
					('0:00:00', u'0.06')
	part4_correct_attempt
					['0:01:15', u'0.07']

21 Student ID:quwong

	first_attempt
					2015-11-03 17:59:37
	part4_incorrect_attempt
					('0:02:09', u'0.4')
					('0:04:06', u'1/0.4')
					('0:04:41', u'1/(0.4)^2')
	part4_correct_attempt
					['0:16:40', u'(1/0.4)/(150)^0.5']

22 Student ID:lguintu

	first_attempt
					2015-11-03 06:14:54
	part4_incorrect_attempt
					('0:54:50', u'1/440')
					('1:08:40', u'100/440')
					('1:08:48', u'10/440')
					('1:08:58', u'10^(1/2)/440')
					('1:10:03', u'10/440')
					('1:10:08', u'100/440')
					('1:10:40', u'(.1)^(-2)/440')
					('1:11:18', u'((.1)^(-2))^(1/2)')
	part4_correct_attempt
					['1:11:32', u'((.1)^(-2)/440)^(1/2)']

23 Student ID:c1sorian

	first_attempt
					2015-11-05 01:22:36
	part4_incorrect_attempt
					('0:07:05', u'.14')
	part4_correct_attempt
					['0:07:12', u'.15']

24 Student ID:b1yao

	first_attempt
					2015-11-05 19:45:44
	part4_incorrect_attempt
					('0:01:15', u'0.7')
					('0:01:22', u'0.7^0.5')
					('0:22:10', u'100^0.5')
					('0:52:42', u'sqrt(280)')
	part4_correct_attempt
					['0:53:01', u'10/sqrt(280)']

25 Student ID:beyounge

	first_attempt
					2015-11-05 08:09:39
	part4_incorrect_attempt
					('0:13:33', u'100/9')
					('0:13:41', u'9/100')
	part4_correct_attempt
					['0:15:27', u'0.225']

26 Student ID:tpmach

	first_attempt
					2015-11-06 02:36:48
	part4_incorrect_attempt
					('0:03:43', u'0.13')
	part4_correct_attempt
					['0:04:08', u'0.11']

27 Student ID:jcj006

	first_attempt
					2015-11-04 23:04:30
	part4_incorrect_attempt
					('0:01:37', u'.1')
					('0:03:12', u'.09')
	part4_correct_attempt
					['0:03:43', u'.17']

28 Student ID:rraiyyan

	first_attempt
					2015-11-07 00:31:01
	part4_incorrect_attempt
					('0:16:54', u'0.025')
					('0:17:02', u'0.25')
					('0:18:18', u'0.15')
					('0:18:59', u'0.22')
	part4_correct_attempt
					['0:19:12', u'0.21']

29 Student ID:t1tran

	first_attempt
					2015-11-04 01:59:20
	part4_incorrect_attempt
					('0:04:41', u'0.9')
	part4_correct_attempt
					['0:05:39', u'0.95']

30 Student ID:thwan

	first_attempt
					2015-11-06 23:06:50
	part4_incorrect_attempt
					('0:02:35', u'0.17')
	part4_correct_attempt
					['0:03:21', u'0.15']

31 Student ID:ytc012

	first_attempt
					2015-11-06 08:56:12
	part4_incorrect_attempt
					('0:01:01', u'0.3')
					('0:01:13', u'0.4')
					('0:01:32', u'0.32')
					('0:01:35', u'0.33')
					('0:01:40', u'0.34')
					('0:01:43', u'0.36')
	part4_correct_attempt
					['0:02:36', u'0.29']

32 Student ID:bakang

	first_attempt
					2015-11-05 16:49:44
	part4_incorrect_attempt
					('0:03:33', u'0.72')
	part4_correct_attempt
					['0:03:42', u'0.12']

33 Student ID:smohiman

	first_attempt
					2015-11-02 05:28:07
	part4_incorrect_attempt
					('0:11:46', u'1/.16')
					('0:12:38', u'110/.16')
	part4_correct_attempt
					['0:25:19', u'1/(.16*110)^.5']

34 Student ID:muy002

	first_attempt
					2015-11-06 05:54:03
	part4_incorrect_attempt
					('0:02:40', u'0.47')
	part4_correct_attempt
					['0:02:56', u'0.46']

35 Student ID:jtfrankl

	first_attempt
					2015-11-06 19:29:25
	part4_incorrect_attempt
					('0:01:13', u'.08')
	part4_correct_attempt
					['0:02:46', u'.09']

36 Student ID:v4sharma

	first_attempt
					2015-11-06 22:49:22
	part4_incorrect_attempt
					('-1 day, 23:54:27', u'0.11')
					('0:01:54', u'0.7')
					('0:02:24', u'0.8')
					('0:02:29', u'0.6')
					('0:02:58', u'0.75')
					('0:05:10', u'0.5')
					('0:28:15', u'0.75')
					('0:49:04', u'0.8')
					('0:50:18', u'0.9')
					('1:15:09', u'0.75')
					('1:18:46', u'0.80')
	part4_correct_attempt
					['1:19:17', u'0.72']

37 Student ID:ralhadda

	first_attempt
					2015-10-31 22:55:26
	part4_incorrect_attempt
					('3:09:00', u'0.7')
	part4_correct_attempt
					['3:09:42', u'0.65']

38 Student ID:aportuga

	first_attempt
					2015-11-03 22:15:10
	part4_incorrect_attempt
					('0:02:01', u'.7')
					('0:02:26', u'.75')
	part4_correct_attempt
					['0:02:50', u'.73']

39 Student ID:xil109

	first_attempt
					2015-11-07 00:13:08
	part4_incorrect_attempt
					('0:00:32', u'0.03')
	part4_correct_attempt
					['0:12:46', u'0.08']

40 Student ID:dac064

	first_attempt
					2015-11-05 10:26:42
	part4_incorrect_attempt
					('0:01:52', u'.42')
					('0:02:16', u'.41')
					('0:02:44', u'.44')
					('0:02:55', u'.43')
					('0:03:01', u'.42')
					('0:03:05', u'.41')
	part4_correct_attempt
					['0:03:57', u'.48']

41 Student ID:v3doan

	first_attempt
					2015-11-07 00:54:13
	part4_incorrect_attempt
					('0:01:00', u'.5')
					('0:01:17', u'.45')
					('0:01:40', u'.405')
	part4_correct_attempt
					['0:01:44', u'.415']

42 Student ID:yil035

	first_attempt
					2015-11-05 22:17:40
	part4_incorrect_attempt
					('0:22:16', u'1.15')
					('8:56:59', u'1/sqrt(250)')
	part4_correct_attempt
					['8:58:54', u'5/sqrt(250)']

43 Student ID:lywong

	first_attempt
					2015-11-05 23:42:29
	part4_incorrect_attempt
					('0:02:20', u'0.6')
					('0:02:43', u'0.65')
	part4_correct_attempt
					['0:03:02', u'0.64']

44 Student ID:hkhodada

	first_attempt
					2015-11-05 16:45:06
	part4_incorrect_attempt
					('0:01:27', u'1.0')
					('6:46:00', u'sqrt(4/750)')
					('6:55:59', u'1/0.16')
					('7:01:53', u'10/4')
					('7:02:56', u'250/4')
					('7:03:11', u'2500/4')
					('7:04:14', u'250/0.16')
					('7:06:58', u'1/10')
	part4_correct_attempt
					['7:13:03', u'1/sqrt(40)']

45 Student ID:glcohen

	first_attempt
					2015-11-04 20:31:34
	part4_incorrect_attempt
					('1:00:58', u'((.8)^-1)')
					('1:01:31', u'((.8)^-2)')
					('1:02:04', u'((.8)^-2)/200')
	part4_correct_attempt
					['1:02:10', u'sqrt(((.8)^-2)/200)']

46 Student ID:acvuong

	first_attempt
					2015-11-05 17:44:48
	part4_incorrect_attempt
					('0:01:18', u'5.25')
	part4_correct_attempt
					['0:04:12', u'0.06']

47 Student ID:d6he

	first_attempt
					2015-11-05 18:38:43
	part4_incorrect_attempt
					('-1 day, 23:55:56', u'0.31')
	part4_correct_attempt
					['0:04:05', u'0.07']

48 Student ID:sachadal

	first_attempt
					2015-11-06 23:32:38
	part4_incorrect_attempt
					('0:01:59', u'0.24')
					('0:02:19', u'0.241')
					('0:02:41', u'0.25')
	part4_correct_attempt
					['0:03:41', u'0.235']

49 Student ID:dcrume

	first_attempt
					2015-11-06 23:46:38
	part4_incorrect_attempt
					('0:00:30', u'1/.4')
					('0:00:48', u'1/.4^2')

50 Student ID:t2li

	first_attempt
					2015-11-06 03:40:00
	part4_incorrect_attempt
					('0:01:11', u'sqrt(0.2^2)/330')
	part4_correct_attempt
					['0:01:54', u'sqrt((5^2)/330)']

51 Student ID:dlt009

	first_attempt
					2015-11-05 09:30:25
	part4_incorrect_attempt
					('-1 day, 23:58:34', u'0.1')
					('0:00:00', u'0.11')
	part4_correct_attempt
					['0:00:51', u'0.15']

52 Student ID:etemlock

	first_attempt
					2015-11-06 22:29:50
	part4_incorrect_attempt
					('0:02:09', u'0.075')
	part4_correct_attempt
					['0:03:09', u'0.077']

53 Student ID:jeqin

	first_attempt
					2015-11-05 11:04:15
	part4_incorrect_attempt
					('0:02:06', u'0.9')
	part4_correct_attempt
					['0:02:23', u'0.92']

54 Student ID:jnatale

	first_attempt
					2015-11-05 01:07:54
	part4_incorrect_attempt
					('0:06:03', u'sqrt(1/0.8^2)')
	part4_correct_attempt
					['0:06:27', u'sqrt((1/0.8^2)/320)']

55 Student ID:agian

	first_attempt
					2015-11-07 00:39:08
	part4_incorrect_attempt
					('0:03:10', u'sqrt(1/.7)')
	part4_correct_attempt
					['0:04:01', u'sqrt((1.42857^2)/330)']

56 Student ID:hachrist

	first_attempt
					2015-11-05 08:27:22
	part4_incorrect_attempt
					('0:08:56', u'0.3')
	part4_correct_attempt
					['0:11:05', u'0.31']

57 Student ID:yeh013

	first_attempt
					2015-11-05 07:42:03
	part4_incorrect_attempt
					('0:06:19', u'0.07')
					('0:06:27', u'0.068')
					('0:06:32', u'0.069')
	part4_correct_attempt
					['0:07:39', u'0.13']

58 Student ID:ppanourg

	first_attempt
					2015-11-06 22:03:03
	part4_incorrect_attempt
					('0:04:48', u'.3')
					('0:05:01', u'.4')
					('0:05:05', u'.2')
	part4_correct_attempt
					['0:05:54', u'.26']

59 Student ID:ksrijong

	first_attempt
					2015-11-06 23:06:10
	part4_incorrect_attempt
					('0:05:17', u'0.2')
					('0:09:44', u'sqrt(12)+1')
	part4_correct_attempt
					['0:10:28', u'0.25']

60 Student ID:azkong

	first_attempt
					2015-11-06 23:21:26
	part4_incorrect_attempt
					('0:05:03', u'0.5')
					('0:05:35', u'0.45')
					('0:06:07', u'0.47')
					('0:06:50', u'0.6')
					('0:10:22', u'0.63')
	part4_correct_attempt
					['0:20:33', u'0.07']

61 Student ID:volim

	first_attempt
					2015-11-05 01:02:52
	part4_incorrect_attempt
					('0:01:43', u'.9')
					('0:02:11', u'.8')
					('0:03:07', u'.9')
					('0:10:37', u'1.03')
					('0:11:11', u'.91')
					('0:11:52', u'.89')
					('0:11:57', u'.88')
					('0:13:14', u'.83')
	part4_correct_attempt
					['0:14:07', u'.95']

62 Student ID:k4ma

	first_attempt
					2015-11-06 22:42:39
	part4_incorrect_attempt
					('0:04:00', u'.25')
					('0:04:15', u'.27')
	part4_correct_attempt
					['0:19:10', u'.28']

63 Student ID:qfu

	first_attempt
					2015-11-06 03:32:58
	part4_incorrect_attempt
					('-1 day, 23:56:34', u'2.5')
					('0:07:34', u'sqrt((1/0.7^2) )')
	part4_correct_attempt
					['0:08:08', u'sqrt((1/0.7^2)/140 )']

64 Student ID:cagatep

	first_attempt
					2015-11-06 20:14:32
	part4_incorrect_attempt
					('0:01:54', u'.5')
					('0:04:07', u'.13')
	part4_correct_attempt
					['0:04:45', u'.12']

65 Student ID:hmnaing

	first_attempt
					2015-11-06 17:39:42
	part4_incorrect_attempt
					('0:10:54', u'1/(390* 0.5*0.5)')
	part4_correct_attempt
					['0:11:32', u'sqrt(1/(390* 0.5*0.5))']

66 Student ID:tjke

	first_attempt
					2015-11-06 18:04:05
	part4_incorrect_attempt
					('0:00:00', u'1/0.8^2*sqrt(180)')
					('0:00:44', u'1/0.8^2')
					('0:01:21', u'1/0.8')
					('0:01:28', u'1/0.8*180')
	part4_correct_attempt
					['0:15:17', u'0.09']

67 Student ID:asp025

	first_attempt
					2015-11-07 00:04:00
	part4_incorrect_attempt
					('0:00:00', u'0.7')

68 Student ID:dmn009

	first_attempt
					2015-11-05 10:36:02
	part4_incorrect_attempt
					('0:14:03', u'2.04')
					('0:14:09', u'2.05')
					('0:14:15', u'2.0408')
					('0:14:32', u'.005102')
	part4_correct_attempt
					['0:15:01', u'.071428']

69 Student ID:dlgoldbe

	first_attempt
					2015-11-07 00:25:12
	part4_incorrect_attempt
					('0:01:43', u'0.20')
	part4_correct_attempt
					['0:03:24', u'0.21']

70 Student ID:yig015

	first_attempt
					2015-11-06 12:19:57
	part4_incorrect_attempt
					('-1 day, 23:52:57', u'0.5')
	part4_correct_attempt
					['0:00:00', u'0.05']

71 Student ID:t2shin

	first_attempt
					2015-11-05 22:35:50
	part4_incorrect_attempt
					('0:05:35', u'0.12')
	part4_correct_attempt
					['0:06:15', u'0.11']

72 Student ID:vsamant

	first_attempt
					2015-11-05 04:08:06
	part4_incorrect_attempt
					('1 day, 15:21:59', u'1.9')

73 Student ID:dcastlem

	first_attempt
					2015-11-06 04:09:45
	part4_incorrect_attempt
					('0:00:47', u'1/sqrt(60)')
					('15:41:15', u'0.85')
	part4_correct_attempt
					['15:41:47', u'0.11']

74 Student ID:fichoi

	first_attempt
					2015-11-05 01:04:33
	part4_incorrect_attempt
					('0:00:51', u'0.13')
					('0:01:04', u'0.14')
					('0:01:49', u'0.135')
					('0:01:52', u'0.13')
					('0:01:55', u'0.12')
	part4_correct_attempt
					['0:02:20', u'0.17']

75 Student ID:qtluong

	first_attempt
					2015-11-04 07:07:38
	part4_incorrect_attempt
					('0:01:20', u'.5')
	part4_correct_attempt
					['0:01:50', u'.11']

76 Student ID:spw006

	first_attempt
					2015-11-04 03:54:55
	part4_incorrect_attempt
					('0:03:27', u'sqrt(1/0.9)')
					('0:03:40', u'sqrt(1/0.81)')
	part4_correct_attempt
					['0:05:18', u'sqrt((1/0.9)^2/190)']

77 Student ID:jdeon

	first_attempt
					2015-11-05 06:11:23
	part4_incorrect_attempt
					('0:01:33', u'.65')
					('0:02:09', u'.95')
					('0:03:30', u'.3')
	part4_correct_attempt
					['0:03:50', u'.31']

78 Student ID:p4kumar

	first_attempt
					2015-11-07 00:33:08
	part4_incorrect_attempt
					('0:02:17', u'1.0')
	part4_correct_attempt
					['0:08:22', u'0.07']

79 Student ID:s2chaudh

	first_attempt
					2015-11-06 06:38:07
	part4_incorrect_attempt
					('0:02:12', u'sqrt(1/.5^2)')
	part4_correct_attempt
					['0:02:33', u'sqrt((1/.5^2)/350)']

80 Student ID:gsrandha

	first_attempt
					2015-11-05 21:57:07
	part4_incorrect_attempt
					('-1 day, 12:12:14', u'1.0')
					('-1 day, 12:12:24', u'1.75')
					('-1 day, 23:56:52', u'.5')
	part4_correct_attempt
					['22:29:57', u'.24']

81 Student ID:jhc010

	first_attempt
					2015-11-06 11:16:39
	part4_incorrect_attempt
					('0:04:17', u'2.3')
	part4_correct_attempt
					['0:06:40', u'0.07']

82 Student ID:cfgutier

	first_attempt
					2015-11-06 21:09:59
	part4_incorrect_attempt
					('-1 day, 23:46:51', u'.075')
					('0:02:46', u'.3')
	part4_correct_attempt
					['0:03:18', u'.25']

83 Student ID:achinn

	first_attempt
					2015-11-04 01:15:46
	part4_incorrect_attempt
					('0:02:24', u'0.37')
	part4_correct_attempt
					['0:02:56', u'0.39']

84 Student ID:k5law

	first_attempt
					2015-11-06 09:53:32
	part4_incorrect_attempt
					('0:02:35', u'.57')
	part4_correct_attempt
					['0:03:10', u'.56']

85 Student ID:mcatozzi

	first_attempt
					2015-11-03 23:56:05
	part4_incorrect_attempt
					('0:00:51', u'.2')
					('0:01:50', u'.1')
	part4_correct_attempt
					['0:02:16', u'.13']

86 Student ID:acs008

	first_attempt
					2015-11-05 22:22:30
	part4_incorrect_attempt
					('0:01:56', u'0.17')
					('0:02:18', u'0.165')
					('0:02:58', u'0.168')
					('0:03:05', u'0.167')
					('0:03:10', u'0.169')
					('0:03:15', u'0.170')
					('0:03:20', u'0.168')
					('0:03:24', u'0.166')
					('0:03:28', u'0.165')
					('0:04:07', u'0.164')
					('0:04:12', u'0.163')
					('0:04:23', u'0.162')
					('0:04:27', u'0.161')
					('0:04:33', u'0.160')
					('0:05:12', u'0.1641')
					('0:05:17', u'0.1642')
					('0:05:21', u'0.1643')
					('0:05:24', u'0.1644')
					('0:05:28', u'0.1645')
					('0:05:31', u'0.1646')
					('0:05:35', u'0.1647')
					('0:05:40', u'0.1648')
					('0:05:43', u'0.1649')
					('0:05:49', u'0.1651')
					('0:05:53', u'0.1652')
					('0:05:57', u'0.1653')
					('0:06:00', u'0.1654')
					('0:06:04', u'0.1655')
					('0:06:08', u'0.1656')
					('0:06:11', u'0.1657')
					('0:06:14', u'0.1658')
					('0:06:17', u'0.1659')
					('0:06:22', u'0.1661')
					('0:06:27', u'0.1662')
					('0:06:30', u'0.1663')
					('0:06:34', u'0.1664')
					('0:06:40', u'0.1665')
					('0:06:44', u'0.1666')
					('0:06:47', u'0.1667')
					('0:06:50', u'0.1668')
					('0:06:52', u'0.1669')
					('0:06:57', u'0.1671')
					('0:07:01', u'0.1672')
	part4_correct_attempt
					['0:07:41', u'0.12']

87 Student ID:hmshah

	first_attempt
					2015-11-05 10:07:37
	part4_incorrect_attempt
					('0:00:00', u'12.5')

88 Student ID:z2tan

	first_attempt
					2015-11-02 06:30:59
	part4_incorrect_attempt
					('0:08:34', u'30.28')
					('0:09:39', u'((330*0.6^-2))^0.5')
					('0:13:31', u'0.6^-2/330^0.5')
	part4_correct_attempt
					['0:13:42', u'0.6^-1/330^0.5']

89 Student ID:kquong

	first_attempt
					2015-11-06 17:55:51
	part4_incorrect_attempt
					('0:04:02', u'.62')
					('0:05:03', u'.9')
					('0:05:47', u'.94')
					('0:06:47', u'.98')
	part4_correct_attempt
					['0:09:47', u'.31']

90 Student ID:vasharma

	first_attempt
					2015-11-05 23:37:18
	part4_incorrect_attempt
					('0:13:30', u'sqrt(10)')
					('0:14:11', u'sqrt(10)/210')
	part4_correct_attempt
					['0:25:09', u'sqrt((1/.1^2)/210)']

91 Student ID:xweng

	first_attempt
					2015-11-06 05:04:05
	part4_incorrect_attempt
					('0:01:00', u'1.0')
	part4_correct_attempt
					['0:13:31', u'0.1']

92 Student ID:kgrozav

	first_attempt
					2015-11-06 21:21:49
	part4_incorrect_attempt
					('0:04:06', u'0.9')
	part4_correct_attempt
					['0:04:13', u'0.09']












