#Problem 9

    $n = random(40,100,5);
    $d = random(2,5,1);

    $dev = 1/sqrt(12)*sqrt($n);
    $a1 = Compute("Q($d/$dev)");
    $ans = Compute("2*Q($d/$dev)");

    [$n] numbers are rounded off to the nearest integer and then summed. Suppose the individual round-off error are uniformly distributed over [` (-.5, .5) `].

    ---
    Remember a random variable that follows a uniform distribution over [`(a,b)`] has a mean of [`(a+b)/2`], and variance of [`\frac{1}{12}(b-a)^2`].

    What is the mean of the round-off error of one number? [_____________]{0}

    What is the standard deviation of the round-off error of one number? [_____________]{"sqrt(1/12)"}

    ---
    Suppose the *sum* of the round-off errors is [`Y`].

    What is the mean of [`Y`]? [_____________]{0}

    What is the standard deviation of [`Y`]? [_____________]{"1/sqrt(12)*sqrt($n)"}

    ---
    To compute the probability that the resultant sum of the [$n] numbers differs from the exact sum by more than [$d], we find the two tails on the distribution of [`Y`].

    What is the z-score at [`Y=[$d]`] ? [__________]{"($d-0)/$dev"}.

    What is the probability that the rounded sum is *larger* than the exact sum by more than [$d] ?[____________]{$a1}

    What is the probability that the rounded sum *differs* from the exact sum by more than [$d] ?[____________]{$ans}






## Part 1

### (40) Mistake Group Fraction of size 40




### (12) Mistake Group Digits of size 12




### (6) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:v4zhang

	first_attempt
					2015-11-06 07:32:30
	part1_incorrect_attempt
					('0:00:00', u'90*1/2')
	part1_correct_attempt
					['0:00:54', u'0']

1 Student ID:t2shin

	first_attempt
					2015-11-05 21:49:52
	part1_incorrect_attempt
					('0:00:00', u'100*0.5')
	part1_correct_attempt
					['0:00:59', u'0']

2 Student ID:haw081

	first_attempt
					2015-11-03 02:09:24
	part1_incorrect_attempt
					('0:00:00', u'60*0.5')
	part1_correct_attempt
					['0:13:29', u'0']

3 Student ID:k4ma

	first_attempt
					2015-11-06 21:41:59
	part1_incorrect_attempt
					('0:00:00', u'50*.5')
	part1_correct_attempt
					['0:00:18', u'0']

4 Student ID:any027

	first_attempt
					2015-11-01 22:12:06
	part1_incorrect_attempt
					('0:00:00', u'((1+-.5) + (1+.5)) / 2')
	part1_correct_attempt
					['0:00:50', u'0']

5 Student ID:pvl001

	first_attempt
					2015-11-03 21:01:48
	part1_incorrect_attempt
					('0:00:00', u'(1 + 45)/2')
	part1_correct_attempt
					['0:00:11', u'0']












## Part 2

### (87) Mistake Group Digits of size 87




### (33) Mistake Group ['R.0.1'] of size 33
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|sqrt(1/12)	|(1/12)(0.5-(-0.5))^2	|[('R.0.1', 12.0, u'12', u'12')]	|
|1	|sqrt(1/12)	|(1/12)*(0.5-(-0.5))**2	|[('R.0.1', 12.0, u'12', u'12')]	|
|2	|sqrt(1/12)	|1/12 ( .5 - (-.5) )^2	|[('R.0.1', 12.0, u'12', u'12')]	|
|3	|sqrt(1/12)	|sqrt(.5*1/12)	|[('R.0.1', 12.0, u'12', u'12')]	|
|4	|sqrt(1/12)	|sqrt(.5*.5*1/12)	|[('R.0.1', 12.0, u'12', u'12')]	|
|5	|sqrt(1/12)	|(1/12)(1)^(1/2)	|[('R.0.1', 12.0, u'12', u'12')]	|
|6	|sqrt(1/12)	|(1/12)(1)^(2)	|[('R.0.1', 12.0, u'12', u'12')]	|
|7	|sqrt(1/12)	|(100/12)^(1/2)	|[('R.0.1', 12.0, u'12', u'12')]	|
|8	|sqrt(1/12)	|(1/12)(1)^2	|[('R.0.1', 12.0, u'12', u'12')]	|
|9	|sqrt(1/12)	|(1/12)(.5+.5)^2	|[('R.0.1', 12.0, u'12', u'12')]	|
|10	|sqrt(1/12)	|sqrt(85/12)	|[('R.0.1', 12.0, u'12', u'12')]	|
|11	|sqrt(1/12)	|(90/12)^(1/2)	|[('R.0.1', 12.0, u'12', u'12')]	|
|12	|sqrt(1/12)	|sqrt(55/12)	|[('R.0.1', 12.0, u'12', u'12')]	|
|13	|sqrt(1/12)	|1/12(.5-(-.5))^2	|[('R.0.1', 12.0, u'12', u'12')]	|
|14	|sqrt(1/12)	|sqrt(50/12)	|[('R.0.1', 12.0, u'12', u'12')]	|
|15	|sqrt(1/12)	|1/12 * (.5 + .5)^2	|[('R.0.1', 12.0, u'12', u'12')]	|
|16	|sqrt(1/12)	|1/12(1)	|[('R.0.1', 12.0, u'12', u'12')]	|
|17	|sqrt(1/12)	|1/12*(.5+.5)^2	|[('R.0.1', 12.0, u'12', u'12')]	|
|18	|sqrt(1/12)	|(1/12)*(.5--.5)^2	|[('R.0.1', 12.0, u'12', u'12')]	|
|19	|sqrt(1/12)	|(1/12)*(.5 +.5)^2	|[('R.0.1', 12.0, u'12', u'12')]	|
|20	|sqrt(1/12)	|1/12*(.5-(-.5))^2	|[('R.0.1', 12.0, u'12', u'12')]	|
|21	|sqrt(1/12)	|1/12*(.5 + .5)^2	|[('R.0.1', 12.0, u'12', u'12')]	|
|22	|sqrt(1/12)	|(1/12)*((.5-(-.5))^2)	|[('R.0.1', 12.0, u'12', u'12')]	|
|23	|sqrt(1/12)	|1/12*((.5+.5)^2)	|[('R.0.1', 12.0, u'12', u'12')]	|
|24	|sqrt(1/12)	|1/12(.5--.5)^2	|[('R.0.1', 12.0, u'12', u'12')]	|
|25	|sqrt(1/12)	|(1/12)(.5--.5)^2	|[('R.0.1', 12.0, u'12', u'12')]	|




### (20) Mistake Group ['R.0'] of size 20
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|sqrt(1/12)	|(1/12)^2	|[('R.0', 0.08333333333333333, u'1/12', u'1/12')]	|
|1	|sqrt(1/12)	|((1/12)(1)^(2))^1/2	|[('R.0', 0.08333333333333333, u'1/12', u'((1/12)(1)^(2))^1')]	|
|2	|sqrt(1/12)	|(1/12)(75)^2	|[('R.0', 0.08333333333333333, u'1/12', u'1/12')]	|
|3	|sqrt(1/12)	|((1/12)(.5+.5))^2	|[('R.0', 0.08333333333333333, u'1/12', u'(1/12)(.5+.5)')]	|
|4	|sqrt(1/12)	|(1/12)*55	|[('R.0', 0.08333333333333333, u'1/12', u'1/12')]	|
|5	|sqrt(1/12)	|1/12 (-.5-.5)^2	|[('R.0', 0.08333333333333333, u'1/12', u'1/12')]	|
|6	|sqrt(1/12)	|1/12*(.5--5)^2	|[('R.0', 0.08333333333333333, u'1/12', u'1/12')]	|
|7	|sqrt(1/12)	|(1/12)^1/2	|[('R.0', 0.08333333333333333, u'1/12', u'(1/12)^1')]	|
|8	|sqrt(1/12)	|1/12(-0.5-0.5)^2	|[('R.0', 0.08333333333333333, u'1/12', u'1/12')]	|
|9	|sqrt(1/12)	|((1/12)(.5+.5)^2)^2	|[('R.0', 0.08333333333333333, u'1/12', u'(1/12)(.5+.5)^2')]	|
|10	|sqrt(1/12)	|([(.5--.5)^2]/12)^2	|[('R.0', 0.08333333333333333, u'1/12', u'[(.5--.5)^2]/12')]	|
|11	|sqrt(1/12)	|1/12(.5)^2	|[('R.0', 0.08333333333333333, u'1/12', u'1/12')]	|
|12	|sqrt(1/12)	|1/12(.5)^2*2	|[('R.0', 0.08333333333333333, u'1/12', u'1/12')]	|
|13	|sqrt(1/12)	|.08333333333333333333330.288675135	|[('R.0', 0.08333333333333333, u'1/12', u'.08333333333333')]	|
|14	|sqrt(1/12)	|1/12*((.5-.5)^2)	|[('R.0', 0.08333333333333333, u'1/12', u'1/12')]	|




### (4) Mistake Group ['R.0.0'] of size 4
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|sqrt(1/12)	|sqrt((1/8))	|[('R.0.0', 1.0, u'1', u'1')]	|
|1	|sqrt(1/12)	|1/sqrt(12)*sqrt(50)	|[('R.0.0', 1.0, u'1', u'1')]	|
|2	|sqrt(1/12)	|(1/2)^.5	|[('R.0.0', 1.0, u'1', u'1')]	|
|3	|sqrt(1/12)	|1/sqrt(12)*sqrt(80)	|[('R.0.0', 1.0, u'1', u'1')]	|




### (4) Mistake Group Wrong_Sign of size 4




### (115) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:gthorn

	first_attempt
					2015-11-05 07:13:41
	part2_incorrect_attempt
					('0:00:15', u'1/12')
	part2_correct_attempt
					['0:01:10', u'sqrt(1/12 * (.5 + .5)^2)']

1 Student ID:phodgson

	first_attempt
					2015-11-06 06:44:32
	part2_incorrect_attempt
					('0:00:00', u'1/12')
	part2_correct_attempt
					['0:00:56', u'sqrt(1/12)']

2 Student ID:v4zhang

	first_attempt
					2015-11-06 07:33:24
	part2_incorrect_attempt
					('0:00:00', u'[(.5--.5)^2]/12')
	part2_correct_attempt
					['0:02:05', u'sqrt(1/12)']

3 Student ID:kew060

	first_attempt
					2015-11-03 02:12:39
	part2_incorrect_attempt
					('0:00:00', u'2.887')
					('0:00:28', u'25/3 ')
					('0:00:44', u'187.655')
					('2 days, 19:20:20', u'1/12')
	part2_correct_attempt
					['2 days, 21:33:22', u'(1/12)^(1/2)']

4 Student ID:kbielawi

	first_attempt
					2015-11-05 21:37:38
	part2_incorrect_attempt
					('0:01:04', u'.5')
					('0:01:09', u'.25')
					('3:00:14', u'.5')
					('3:01:36', u'1/12')
					('4:00:51', u'1/1')
	part2_correct_attempt
					['4:01:37', u'sqrt(1/12)']

5 Student ID:jguanzho

	first_attempt
					2015-11-05 17:44:38
	part2_incorrect_attempt
					('0:00:00', u'1/12')
					('0:01:28', u'(0.5*0.5*80)**0.5')
	part2_correct_attempt
					['0:19:20', u'(1/12)**0.5']

6 Student ID:alakamsa

	first_attempt
					2015-11-02 19:37:10
	part2_incorrect_attempt
					('0:00:00', u'1/12')
	part2_correct_attempt
					['1 day, 23:50:40', u'sqrt(1/12)']

7 Student ID:jjm019

	first_attempt
					2015-11-04 23:39:31
	part2_incorrect_attempt
					('3:57:34', u'.5')
	part2_correct_attempt
					['4:07:39', u'sqrt(1/12)']

8 Student ID:dkurli

	first_attempt
					2015-11-05 03:29:36
	part2_incorrect_attempt
					('0:00:19', u'1/2')
					('0:00:28', u'.25')
					('0:01:06', u'1/12')
	part2_correct_attempt
					['0:01:28', u'sqrt(1/12)']

9 Student ID:nhn018

	first_attempt
					2015-11-05 05:47:59
	part2_incorrect_attempt
					('0:13:00', u'1/sqrt(1/2)')
	part2_correct_attempt
					['0:13:44', u'1/sqrt(12)']

10 Student ID:j5phung

	first_attempt
					2015-11-04 21:17:03
	part2_incorrect_attempt
					('0:02:03', u'0.5')
					('0:04:36', u'sqrt((1/8)*(80*81)/2)')
	part2_correct_attempt
					['0:06:25', u'sqrt(1/12)']

11 Student ID:vqt004

	first_attempt
					2015-11-06 06:24:52
	part2_incorrect_attempt
					('-1 day, 23:56:57', u'1/12')
					('0:00:32', u'1/12')
					('0:02:57', u'sqrt(0.5*90)')
	part2_correct_attempt
					['0:06:03', u'sqrt(1/12)']

12 Student ID:mnrahman

	first_attempt
					2015-11-07 00:05:33
	part2_incorrect_attempt
					('0:00:00', u'1/12')
	part2_correct_attempt
					['0:00:21', u'sqrt(1/12)']

13 Student ID:btn023

	first_attempt
					2015-11-06 11:22:14
	part2_incorrect_attempt
					('0:02:51', u'.5')
					('0:03:29', u'2*.5*(-.5)^2')
					('0:04:29', u'.5*(-.5)^2')
					('0:06:01', u'1/8')
					('0:12:31', u'sqrt(1/12(.5)^2*2)')
					('0:12:47', u'sqrt(1/12(.5)^2)')
	part2_correct_attempt
					['7:04:33', u'sqrt(1/12(1)^2)']

14 Student ID:dgunawan

	first_attempt
					2015-11-05 08:57:44
	part2_incorrect_attempt
					('0:00:00', u'((.5+.5)^2)/12')
					('0:01:07', u'((.5-.5)^2)/12')
					('0:01:19', u'((.5+.5)^2)/12')
					('0:01:43', u'85*(((.5+.5)^2)/12)')
					('15:18:20', u'(1/6)(1)')
	part2_correct_attempt
					['15:18:43', u'(1/12)^(1/2)']

15 Student ID:mpanelo

	first_attempt
					2015-11-05 23:02:59
	part2_incorrect_attempt
					('0:00:00', u'1/12')
	part2_correct_attempt
					['0:01:17', u'sqrt(1/12)']

16 Student ID:tcn013

	first_attempt
					2015-11-05 20:57:24
	part2_incorrect_attempt
					('0:00:00', u'1/12')
					('0:01:24', u'1/144')
	part2_correct_attempt
					['0:01:52', u'sqrt(1/12)']

17 Student ID:tstevens

	first_attempt
					2015-11-06 12:10:21
	part2_incorrect_attempt
					('0:00:12', u'.5')
					('0:02:11', u'1/12')
					('0:02:32', u'.0833333333333333333333')
	part2_correct_attempt
					['0:02:57', u'.288675135']

18 Student ID:tcuddy

	first_attempt
					2015-11-05 18:05:57
	part2_incorrect_attempt
					('0:11:51', u'1/12')
	part2_correct_attempt
					['0:12:06', u'(1/12)**.5']

19 Student ID:dando

	first_attempt
					2015-11-06 23:46:43
	part2_incorrect_attempt
					('0:00:00', u'1/12')
	part2_correct_attempt
					['0:01:49', u'sqrt(1/12)']

20 Student ID:dsriniva

	first_attempt
					2015-11-05 16:57:53
	part2_incorrect_attempt
					('0:00:00', u'1/12')
	part2_correct_attempt
					['0:00:56', u'sqrt(1/12)']

21 Student ID:glcohen

	first_attempt
					2015-11-03 22:16:17
	part2_incorrect_attempt
					('9:22:46', u'sqrt(50)')
					('9:28:47', u'0.5')
	part2_correct_attempt
					['9:30:54', u'sqrt((1/12)((-.5-.5)^2))']

22 Student ID:sayao

	first_attempt
					2015-11-04 01:56:12
	part2_incorrect_attempt
					('0:00:30', u'.5')
					('0:03:12', u'1/12')
					('1 day, 2:03:14', u'.5')
					('1 day, 2:03:21', u'.25')
					('1 day, 15:05:12', u'1/12')
	part2_correct_attempt
					['1 day, 22:04:00', u'sqrt((1/12))']

23 Student ID:achava

	first_attempt
					2015-11-06 08:21:51
	part2_incorrect_attempt
					('0:00:14', u'1/12')
	part2_correct_attempt
					['0:03:18', u'sqrt(1/12)']

24 Student ID:mitopete

	first_attempt
					2015-11-04 05:20:00
	part2_incorrect_attempt
					('0:00:00', u'(1)^(1/2)')
	part2_correct_attempt
					['0:00:47', u'((1/12)(1)^(2))^(1/2)']

25 Student ID:starinia

	first_attempt
					2015-11-05 03:37:59
	part2_incorrect_attempt
					('0:56:33', u'sqrt(90 * 1/2 *(1-1/2))')
	part2_correct_attempt
					['1:21:40', u'sqrt(1/12)']

26 Student ID:m4salaza

	first_attempt
					2015-11-05 05:39:08
	part2_incorrect_attempt
					('0:01:00', u'sqrt(((-.5+.5)/2)*(1-1/12))')
	part2_correct_attempt
					['0:03:58', u'1/sqrt(12)']

27 Student ID:yos017

	first_attempt
					2015-11-06 09:42:21
	part2_incorrect_attempt
					('0:00:00', u'100/12')
					('0:01:06', u'1/12')
	part2_correct_attempt
					['0:06:59', u'(1/12)^(1/2)']

28 Student ID:habuamar

	first_attempt
					2015-11-03 00:33:33
	part2_incorrect_attempt
					('0:00:00', u'1/12')
	part2_correct_attempt
					['0:00:23', u'sqrt(1/12)']

29 Student ID:akg009

	first_attempt
					2015-11-06 21:08:58
	part2_incorrect_attempt
					('0:00:00', u'1/12')
	part2_correct_attempt
					['0:00:41', u'sqrt(1/12)']

30 Student ID:jit002

	first_attempt
					2015-11-05 18:29:03
	part2_incorrect_attempt
					('0:00:33', u'0.5')
					('0:09:24', u'1/12')
	part2_correct_attempt
					['0:09:50', u'(1/12)^0.5']

31 Student ID:h4tu

	first_attempt
					2015-11-06 23:48:34
	part2_incorrect_attempt
					('0:00:14', u'(1/12)')
	part2_correct_attempt
					['0:00:42', u'sqrt(1/12)']

32 Student ID:jag028

	first_attempt
					2015-11-03 21:50:42
	part2_incorrect_attempt
					('0:00:21', u'1/12')
	part2_correct_attempt
					['0:01:49', u'sqrt[1/12]']

33 Student ID:quwong

	first_attempt
					2015-11-02 23:11:22
	part2_incorrect_attempt
					('0:00:00', u'1/12')
					('0:00:20', u'0.25/12')
	part2_correct_attempt
					['2:29:28', u'1/(12^0.5)']

34 Student ID:asetters

	first_attempt
					2015-11-05 20:24:36
	part2_incorrect_attempt
					('0:00:00', u'1/12')
	part2_correct_attempt
					['0:00:23', u'sqrt(1/12)']

35 Student ID:abjara

	first_attempt
					2015-11-04 05:45:43
	part2_incorrect_attempt
					('0:00:00', u'1/12')
	part2_correct_attempt
					['0:00:12', u'sqrt(1/12)']

36 Student ID:cprafull

	first_attempt
					2015-11-06 02:56:30
	part2_incorrect_attempt
					('0:00:37', u'1/12')
	part2_correct_attempt
					['0:01:07', u'sqrt(1/12)']

37 Student ID:krau

	first_attempt
					2015-11-04 20:35:20
	part2_incorrect_attempt
					('0:00:24', u'sqrt(.5)')
					('0:01:20', u'1/12')
	part2_correct_attempt
					['6:55:53', u'sqrt(1/12)']

38 Student ID:jcj006

	first_attempt
					2015-11-04 22:41:00
	part2_incorrect_attempt
					('0:00:00', u'1/12')
	part2_correct_attempt
					['0:00:33', u'sqrt(1/12)']

39 Student ID:t1tran

	first_attempt
					2015-11-04 00:37:13
	part2_incorrect_attempt
					('0:00:00', u'sqrt(1/2(.5-(-.5))^2)')
	part2_correct_attempt
					['0:01:41', u'sqrt(1/12(.5+.5)^2)']

40 Student ID:dsmonaha

	first_attempt
					2015-11-04 16:46:52
	part2_incorrect_attempt
					('0:00:27', u'(1/12)')
	part2_correct_attempt
					['0:03:32', u'(1/12)^(1/2)']

41 Student ID:edescobe

	first_attempt
					2015-11-04 12:13:40
	part2_incorrect_attempt
					('0:00:00', u'1/12')
	part2_correct_attempt
					['0:13:07', u'1/12^(1/2)']

42 Student ID:w4shin

	first_attempt
					2015-11-06 23:46:03
	part2_incorrect_attempt
					('0:00:00', u'1/12')
	part2_correct_attempt
					['0:00:11', u'sqrt(1/12)']

43 Student ID:bakang

	first_attempt
					2015-11-05 16:30:57
	part2_incorrect_attempt
					('0:00:46', u'sqrt((1/12)*(0.9)^2)')
	part2_correct_attempt
					['0:00:53', u'sqrt((1/12)*(1)^2)']

44 Student ID:smohiman

	first_attempt
					2015-11-02 03:24:17
	part2_incorrect_attempt
					('0:00:00', u'1/12')
	part2_correct_attempt
					['0:01:18', u'(1/12)^(1/2)']

45 Student ID:muy002

	first_attempt
					2015-11-06 04:43:41
	part2_incorrect_attempt
					('0:02:58', u'1/12')
	part2_correct_attempt
					['0:03:07', u'sqrt(1/12)']

46 Student ID:jtfrankl

	first_attempt
					2015-11-06 19:06:40
	part2_incorrect_attempt
					('0:00:00', u'1/12')
	part2_correct_attempt
					['0:00:27', u'sqrt(1/12)']

47 Student ID:cstringh

	first_attempt
					2015-11-04 07:24:44
	part2_incorrect_attempt
					('0:00:00', u'1/12')
					('0:00:09', u'1/70')
	part2_correct_attempt
					['0:00:41', u'sqrt(1/12)']

48 Student ID:dan029

	first_attempt
					2015-11-05 09:34:22
	part2_incorrect_attempt
					('0:00:00', u'1/12')
	part2_correct_attempt
					['0:00:41', u'1/sqrt(12)']

49 Student ID:ralhadda

	first_attempt
					2015-10-31 22:13:59
	part2_incorrect_attempt
					('0:00:59', u'1/12')
					('3:22:43', u'1/12')
					('3:33:00', u'65/12')
					('3:35:00', u'1/12')

50 Student ID:yjshin

	first_attempt
					2015-11-06 23:24:16
	part2_incorrect_attempt
					('0:01:07', u'((.5+.5)^2)/12')
	part2_correct_attempt
					['0:02:50', u'sqrt(((.5+.5)^2)/12)']

51 Student ID:dcastlem

	first_attempt
					2015-11-03 00:41:05
	part2_incorrect_attempt
					('1:32:29', u'1/12')
	part2_correct_attempt
					['1:33:42', u'sqrt(1/12)']

52 Student ID:hsc052

	first_attempt
					2015-11-06 23:07:48
	part2_incorrect_attempt
					('0:03:21', u'1/12')
	part2_correct_attempt
					['0:04:01', u'sqrt(1/12)']

53 Student ID:xil109

	first_attempt
					2015-11-06 01:32:47
	part2_incorrect_attempt
					('0:00:00', u'1/6')
	part2_correct_attempt
					['0:00:16', u'sqrt(1/12)']

54 Student ID:zhz159

	first_attempt
					2015-11-05 23:37:06
	part2_incorrect_attempt
					('0:00:00', u'0.31622777')
	part2_correct_attempt
					['0:12:38', u'0.288675']

55 Student ID:wmiao

	first_attempt
					2015-11-05 22:53:24
	part2_incorrect_attempt
					('0:00:00', u'(0.5*(1-0.5)*0)^0.5')
					('0:02:36', u'(0.5*(1-0.5)*100)^0.5')
					('0:02:52', u'(0.5*(1-0.5)*1)^0.5')
	part2_correct_attempt
					['0:05:26', u'(1/12*1^2)^0.5']

56 Student ID:b3hwang

	first_attempt
					2015-11-05 19:43:51
	part2_incorrect_attempt
					('0:00:11', u'1/12')
	part2_correct_attempt
					['0:04:20', u'(1/12)^(1/2)']

57 Student ID:lywong

	first_attempt
					2015-11-04 07:33:22
	part2_incorrect_attempt
					('0:00:34', u'3.31662')
					('0:01:39', u'100/12')
					('1 day, 16:13:14', u'(1)^(1/2)')
					('1 day, 16:26:42', u'sqrt((1/12)(10)^2)')
	part2_correct_attempt
					['1 day, 16:27:35', u'sqrt((1/12))']

58 Student ID:hkhodada

	first_attempt
					2015-11-03 01:20:13
	part2_incorrect_attempt
					('-1 day, 23:26:51', u'1/12')
					('-1 day, 23:56:31', u'0.288')
					('-1 day, 23:58:07', u'0.29')
					('0:00:00', u'0.3')
	part2_correct_attempt
					['1 day, 2:40:21', u'1/sqrt(12)']

59 Student ID:abasu

	first_attempt
					2015-11-05 04:56:21
	part2_incorrect_attempt
					('0:01:21', u'.5')
					('0:02:52', u'.5')
					('0:35:42', u'0.25')
	part2_correct_attempt
					['0:42:28', u'sqrt(1/12)']

60 Student ID:acvuong

	first_attempt
					2015-11-05 01:09:21
	part2_incorrect_attempt
					('0:00:00', u'1/12')
	part2_correct_attempt
					['0:01:36', u'(1/12)^0.5']

61 Student ID:d6he

	first_attempt
					2015-11-05 07:07:49
	part2_incorrect_attempt
					('0:01:42', u' 0.29')
					('0:04:08', u'0.08333333')
	part2_correct_attempt
					['0:06:27', u'sqrt(1/12)']

62 Student ID:sachadal

	first_attempt
					2015-11-05 20:29:44
	part2_incorrect_attempt
					('1 day, 1:48:02', u'1/12')
	part2_correct_attempt
					['1 day, 1:50:53', u'1/sqrt(12)']

63 Student ID:pvl001

	first_attempt
					2015-11-03 21:01:59
	part2_incorrect_attempt
					('0:00:10', u'.5')
					('6:41:29', u'.5 * .5')
					('6:41:49', u'sqrt(.5 * .5)')
	part2_correct_attempt
					['6:46:43', u'sqrt(1/12)']

64 Student ID:t2li

	first_attempt
					2015-11-06 03:12:19
	part2_incorrect_attempt
					('0:00:10', u'1/12')
	part2_correct_attempt
					['0:05:58', u'sqrt(1/12)']

65 Student ID:mbl003

	first_attempt
					2015-11-06 20:33:10
	part2_incorrect_attempt
					('0:00:24', u'sqrt((1/12)*(0)^2)')
	part2_correct_attempt
					['0:01:05', u'sqrt((1/12)*(1)^2)']

66 Student ID:n2patil

	first_attempt
					2015-11-05 02:49:23
	part2_incorrect_attempt
					('0:00:22', u'1/12')
					('0:15:15', u'1/24')
	part2_correct_attempt
					['0:21:12', u'(1/12)^(1/2)']

67 Student ID:ksmurlo

	first_attempt
					2015-11-05 06:55:06
	part2_incorrect_attempt
					('0:00:11', u'1/12')
	part2_correct_attempt
					['0:01:01', u'sqrt[1/12(.5-(-.5))^2]']

68 Student ID:jblynch

	first_attempt
					2015-11-04 21:10:13
	part2_incorrect_attempt
					('-1 day, 23:59:37', u'sqrt((1/12)(75)^2)')
	part2_correct_attempt
					['0:00:29', u'sqrt(1/12)']

69 Student ID:beerye28

	first_attempt
					2015-11-03 06:39:44
	part2_incorrect_attempt
					('0:00:00', u'1/12')
	part2_correct_attempt
					['0:00:39', u'(1/12)^(.5)']

70 Student ID:aakumar

	first_attempt
					2015-11-05 05:04:40
	part2_incorrect_attempt
					('0:00:11', u'.5')
					('0:00:23', u'.25')
	part2_correct_attempt
					['0:14:52', u'(1/12)^(1/2)']

71 Student ID:hachrist

	first_attempt
					2015-11-05 08:54:30
	part2_incorrect_attempt
					('-1 day, 23:22:55', u'1- Phi(2)')
	part2_correct_attempt
					['0:00:27', u'sqrt(1/12)']

72 Student ID:kew017

	first_attempt
					2015-11-06 01:26:23
	part2_incorrect_attempt
					('0:00:00', u'80/4')
					('0:00:21', u'sqrt(80/4)')
	part2_correct_attempt
					['0:03:33', u'sqrt(1/12)']

73 Student ID:yeh013

	first_attempt
					2015-11-05 03:10:28
	part2_incorrect_attempt
					('0:02:17', u'1/12')
					('0:06:46', u'1/6')
					('0:13:55', u'90/12')
	part2_correct_attempt
					['0:15:54', u'(1/12)^(1/2)']

74 Student ID:ppanourg

	first_attempt
					2015-11-06 21:10:40
	part2_incorrect_attempt
					('0:00:45', u'1/12')
	part2_correct_attempt
					['0:01:05', u'sqrt(1/12)']

75 Student ID:ksrijong

	first_attempt
					2015-11-06 20:48:49
	part2_incorrect_attempt
					('1:41:16', u'.5/3')
	part2_correct_attempt
					['1:47:36', u'sqrt((0.5+0.5)^2/12)']

76 Student ID:bmilton

	first_attempt
					2015-11-06 22:46:04
	part2_incorrect_attempt
					('0:00:12', u'1/2')
					('0:00:19', u'1/12')
					('0:00:26', u'1/4')
	part2_correct_attempt
					['0:01:03', u'sqrt((1/12) * (1))']

77 Student ID:yhhan

	first_attempt
					2015-11-07 00:24:55
	part2_incorrect_attempt
					('0:00:25', u'1/12')

78 Student ID:volim

	first_attempt
					2015-11-04 23:32:33
	part2_incorrect_attempt
					('0:00:36', u'.25')
					('0:00:41', u'.5')
					('0:01:08', u'1/12')
	part2_correct_attempt
					['0:01:27', u'(1/12)^(1/2)']

79 Student ID:atorr

	first_attempt
					2015-11-05 20:29:27
	part2_incorrect_attempt
					('-1 day, 23:59:40', u'1/12')
	part2_correct_attempt
					['0:00:22', u'(1/12)^0.5']

80 Student ID:cagatep

	first_attempt
					2015-11-05 07:53:35
	part2_incorrect_attempt
					('0:00:00', u'1/12')
	part2_correct_attempt
					['0:00:36', u'sqrt(1/12)']

81 Student ID:masaro

	first_attempt
					2015-11-03 17:26:43
	part2_incorrect_attempt
					('0:00:00', u'1/12')
	part2_correct_attempt
					['0:00:38', u'sqrt(1/12)']

82 Student ID:dmn009

	first_attempt
					2015-11-05 09:23:52
	part2_incorrect_attempt
					('0:20:33', u'1/12')
	part2_correct_attempt
					['0:33:01', u'.288675']

83 Student ID:yig015

	first_attempt
					2015-11-05 10:57:48
	part2_incorrect_attempt
					('0:00:00', u'1/12')
	part2_correct_attempt
					['0:13:38', u'0.288675']

84 Student ID:jfalcone

	first_attempt
					2015-11-05 05:43:34
	part2_incorrect_attempt
					('0:01:39', u'1/12')
					('0:05:55', u'1/12^2')
					('0:06:05', u'1/(12^2)')
	part2_correct_attempt
					['0:07:45', u'sqrt(1/12)']

85 Student ID:fichoi

	first_attempt
					2015-11-04 20:06:44
	part2_incorrect_attempt
					('0:00:00', u'1/12')
	part2_correct_attempt
					['0:00:17', u'sqrt(1/12)']

86 Student ID:rohan

	first_attempt
					2015-11-07 00:16:39
	part2_incorrect_attempt
					('0:00:15', u'1/12')
	part2_correct_attempt
					['0:02:16', u'sqrt(1/12)']

87 Student ID:any027

	first_attempt
					2015-11-01 22:12:56
	part2_incorrect_attempt
					('0:01:03', u'1/2 ( .5 - (-.5) )^2')
	part2_correct_attempt
					['0:01:57', u'sqrt(1/12 ( .5 - (-.5) )^2)']

88 Student ID:rwthomps

	first_attempt
					2015-11-06 21:51:27
	part2_incorrect_attempt
					('0:03:41', u'sqrt(65 * 1/12 * (.5 + .5))')
	part2_correct_attempt
					['0:03:50', u'sqrt(1/12 * (.5 + .5))']

89 Student ID:amquinte

	first_attempt
					2015-11-05 06:40:14
	part2_incorrect_attempt
					('0:00:37', u'1/12')
	part2_correct_attempt
					['0:01:23', u'.2887']

90 Student ID:jmiclat

	first_attempt
					2015-11-06 23:39:28
	part2_incorrect_attempt
					('0:00:00', u'1/12')
	part2_correct_attempt
					['0:00:30', u'sqrt(1/12)']

91 Student ID:gsrandha

	first_attempt
					2015-11-05 08:25:58
	part2_incorrect_attempt
					('0:00:55', u'sqrt(75*.5(1-.5))')
	part2_correct_attempt
					['0:40:10', u'sqrt(1/12(1))']

92 Student ID:qtluong

	first_attempt
					2015-11-04 06:40:26
	part2_incorrect_attempt
					('0:00:00', u'1/2')
					('0:00:14', u'1/12')
	part2_correct_attempt
					['0:00:27', u'sqrt(1/12)']

93 Student ID:agarango

	first_attempt
					2015-11-05 03:19:35
	part2_incorrect_attempt
					('0:01:22', u'0.5')
					('0:05:27', u'1/12')
					('0:05:50', u'55/12')
	part2_correct_attempt
					['0:33:55', u'sqrt(1/12)']

94 Student ID:twsalim

	first_attempt
					2015-11-06 03:14:40
	part2_incorrect_attempt
					('0:00:00', u'1/12')
					('0:16:31', u'0.5')
					('0:20:40', u'1/3')
					('0:27:34', u'0.25')
					('0:44:38', u'0.288')
	part2_correct_attempt
					['0:44:48', u'0.28867']

95 Student ID:s6deng

	first_attempt
					2015-11-05 07:44:22
	part2_incorrect_attempt
					('0:00:39', u'1/12')
	part2_correct_attempt
					['0:01:22', u'sqrt(1/12)']

96 Student ID:achinn

	first_attempt
					2015-11-03 21:36:45
	part2_incorrect_attempt
					('0:00:00', u'1/144')
	part2_correct_attempt
					['0:00:41', u'sqrt(1/12)']

97 Student ID:jap009

	first_attempt
					2015-11-05 22:39:20
	part2_incorrect_attempt
					('0:00:00', u'1/12')
	part2_correct_attempt
					['0:00:15', u'(1/12)^(1/2)']

98 Student ID:jcl084

	first_attempt
					2015-11-02 20:43:41
	part2_incorrect_attempt
					('0:00:00', u'sqrt (112)')
	part2_correct_attempt
					['0:00:11', u'sqrt (1/12)']

99 Student ID:aalhaida

	first_attempt
					2015-11-05 23:52:07
	part2_incorrect_attempt
					('0:00:08', u'(1/12)')

100 Student ID:ajabasa

	first_attempt
					2015-11-05 22:24:29
	part2_incorrect_attempt
					('0:02:05', u'((1/12)(-.5-.5)^2)^1/2')
	part2_correct_attempt
					['0:02:24', u'((1/12)(-.5-.5)^2)^(1/2)']

101 Student ID:mcatozzi

	first_attempt
					2015-11-03 20:47:04
	part2_incorrect_attempt
					('0:02:02', u'.5')
	part2_correct_attempt
					['0:13:09', u'sqrt(1/12)']

102 Student ID:acs008

	first_attempt
					2015-11-05 21:49:23
	part2_incorrect_attempt
					('0:00:13', u'1/12')
	part2_correct_attempt
					['0:00:45', u'sqrt(1/12)']

103 Student ID:dpereira

	first_attempt
					2015-11-05 22:44:04
	part2_incorrect_attempt
					('0:00:00', u'1/12')
	part2_correct_attempt
					['0:01:51', u'sqrt(1/12)']

104 Student ID:hmshah

	first_attempt
					2015-11-05 09:49:10
	part2_incorrect_attempt
					('11:23:29', u'.5')
	part2_correct_attempt
					['11:34:19', u'sqrt(1/12)']

105 Student ID:aordookh

	first_attempt
					2015-11-06 06:07:32
	part2_incorrect_attempt
					('0:00:23', u'1/2')
	part2_correct_attempt
					['0:15:19', u'(1/12(.5-(-.5))^2)^(1/2)']

106 Student ID:kquong

	first_attempt
					2015-11-05 03:15:05
	part2_incorrect_attempt
					('0:00:08', u'.5')
					('0:09:13', u'85/12')
	part2_correct_attempt
					['0:10:36', u'sqrt(1/12)']

107 Student ID:hpc001

	first_attempt
					2015-11-06 23:33:33
	part2_incorrect_attempt
					('0:00:00', u'.5')
	part2_correct_attempt
					['0:00:58', u'sqrt(1/12)']

108 Student ID:xweng

	first_attempt
					2015-11-06 01:03:22
	part2_incorrect_attempt
					('0:00:17', u'1/12')
					('1:01:40', u'2.04124')
					('1:01:58', u'1.46969')
					('1:04:51', u'0.92918 ')
					('1:05:14', u' 25 / 6')
					('1:30:01', u'2.04124')
					('1:34:17', u'25/6')
					('1:35:02', u'1/2.04124')
					('3:34:41', u'0.5869')
	part2_correct_attempt
					['3:44:48', u'0.28867']

109 Student ID:s2chaudh

	first_attempt
					2015-11-06 06:42:11
	part2_incorrect_attempt
					('0:00:45', u'1/(sqrt(12)*sqrt(80))')
	part2_correct_attempt
					['0:03:01', u'1/sqrt(12)']

110 Student ID:c3chung

	first_attempt
					2015-11-06 22:30:22
	part2_incorrect_attempt
					('0:00:00', u'1/12')
	part2_correct_attempt
					['0:01:05', u'sqrt(1/12)']

111 Student ID:zig006

	first_attempt
					2015-11-04 21:45:16
	part2_incorrect_attempt
					('0:00:00', u'1/12')
	part2_correct_attempt
					['0:22:50', u'(1/12)^0.5']

112 Student ID:zhw110

	first_attempt
					2015-11-06 23:08:09
	part2_incorrect_attempt
					('0:01:30', u'0.5')
					('0:01:36', u'0.25')
					('0:03:13', u'0.5^0.5')
					('0:03:24', u'0.25^0.5')
					('0:56:33', u'1/12')
	part2_correct_attempt
					['0:57:06', u'(1/12)^0.5']

113 Student ID:kgrozav

	first_attempt
					2015-11-05 20:52:42
	part2_incorrect_attempt
					('0:00:42', u'(1/12)')
					('0:04:04', u'4.583333')
					('0:04:13', u'4.5833333')
					('0:04:34', u'2.140872')
					('0:07:21', u'1/12')
					('0:07:57', u'[(.5 - -.5)^2]/12')
					('0:11:23', u'60/12')
					('0:13:05', u'0.2673853')
					('0:15:27', u'0.0356912')
	part2_correct_attempt
					['10:47:40', u'0.2886751346']

114 Student ID:j2phung

	first_attempt
					2015-11-05 11:00:11
	part2_incorrect_attempt
					('-1 day, 23:55:02', u'17/20')
					('0:00:31', u'1/12')
	part2_correct_attempt
					['0:03:40', u'(1/12)^(1/2)']












## Part 3

### (14) Mistake Group Fraction of size 14




### (4) Mistake Group Digits of size 4




### (1) Mistake Group redirect of size 1




### (4) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:mbl003

	first_attempt
					2015-11-06 20:33:10
	part2_correct_attempt
					['0:01:05', u'sqrt((1/12)*(1)^2)']
	part3_incorrect_attempt
					('0:04:51', u'80/2')
	part3_correct_attempt
					['0:05:01', u'0']

1 Student ID:dlt009

	first_attempt
					2015-11-05 08:33:37
	part2_correct_attempt
					['0:05:02', u'sqrt[(1/12)]']
	part3_incorrect_attempt
					('0:05:34', u'(40)/2')
	part3_correct_attempt
					['0:07:31', u'0']

2 Student ID:bmilton

	first_attempt
					2015-11-06 22:46:04
	part2_correct_attempt
					['0:01:03', u'sqrt((1/12) * (1))']
	part3_incorrect_attempt
					('0:02:23', u'70 * (1/2)')
	part3_correct_attempt
					['0:03:14', u'0']

3 Student ID:j5phung

	first_attempt
					2015-11-04 21:17:03
	part2_correct_attempt
					['0:06:25', u'sqrt(1/12)']
	part3_incorrect_attempt
					('0:09:29', u'(80*81)/4')
					('0:13:56', u'(80)/2')
	part3_correct_attempt
					['0:14:34', u'0']












## Part 4

### (93) Mistake Group ['R.0.0'] of size 93
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|1/sqrt(12)*sqrt(100)	|(1/12) ^ 50	|[('R.0.0', 1.0, u'1', u'1')]	|
|1	|1/sqrt(12)*sqrt(100)	|sqrt(1/12)	|[('R.0.0', 1.0, u'1', u'1')]	|
|2	|1/sqrt(12)*sqrt(65)	|(1/3)^(1/2)	|[('R.0.0', 1.0, u'1', u'1')]	|
|3	|1/sqrt(12)*sqrt(60)	|(1/12)^0.5	|[('R.0.0', 1.0, u'1', u'1')]	|
|4	|1/sqrt(12)*sqrt(80)	|(1/12)^(1/2)	|[('R.0.0', 1.0, u'1', u'1')]	|
|5	|1/sqrt(12)*sqrt(90)	|(1/12)^(.5)	|[('R.0.0', 1.0, u'1', u'1')]	|
|6	|1/sqrt(12)*sqrt(75)	|(1/12)/75	|[('R.0.0', 1.0, u'1', u'1')]	|
|7	|1/sqrt(12)*sqrt(50)	|sqrt((1/12))	|[('R.0.0', 1.0, u'1', u'1')]	|
|8	|1/sqrt(12)*sqrt(75)	|(1/12)+(1/12)	|[('R.0.0', 1.0, u'1', u'1')]	|
|9	|1/sqrt(12)*sqrt(95)	|sqrt(1/3)	|[('R.0.0', 1.0, u'1', u'1')]	|
|10	|1/sqrt(12)*sqrt(75)	|(1/12)(1+1)^2	|[('R.0.0', 1.0, u'1', u'1')]	|
|11	|1/sqrt(12)*sqrt(100)	|(1/6)^(1/2)	|[('R.0.0', 1.0, u'1', u'1')]	|
|12	|1/sqrt(12)*sqrt(95)	|sqrt(1/6)	|[('R.0.0', 1.0, u'1', u'1')]	|
|13	|1/sqrt(12)*sqrt(75)	|(1/12)*2	|[('R.0.0', 1.0, u'1', u'1')]	|
|14	|1/sqrt(12)*sqrt(90)	|1/12 (-.5-.5)^2	|[('R.0.0', 1.0, u'1', u'1')]	|
|15	|1/sqrt(12)*sqrt(95)	|(1/2)^(1/2)	|[('R.0.0', 1.0, u'1', u'1')]	|
|16	|1/sqrt(12)*sqrt(80)	|sqrt(1/80)	|[('R.0.0', 1.0, u'1', u'1')]	|
|17	|1/sqrt(12)*sqrt(45)	|1/sqrt(1/2)*sqrt(50)	|[('R.0.0', 1.0, u'1', u'1')]	|
|18	|1/sqrt(12)*sqrt(80)	|(1/2) * (1/(12)^(1/2))	|[('R.0.0', 1.0, u'1', u'1')]	|
|19	|1/sqrt(12)*sqrt(80)	|(1/12)**0.5	|[('R.0.0', 1.0, u'1', u'1')]	|
|20	|1/sqrt(12)*sqrt(45)	|(1/12)**.5	|[('R.0.0', 1.0, u'1', u'1')]	|
|21	|1/sqrt(12)*sqrt(75)	|1/12(1) * 75	|[('R.0.0', 1.0, u'1', u'1')]	|
|22	|1/sqrt(12)*sqrt(45)	|(1/45)^(0.5)	|[('R.0.0', 1.0, u'1', u'1')]	|
|23	|1/sqrt(12)*sqrt(75)	|1/12 * 75	|[('R.0.0', 1.0, u'1', u'1')]	|
|24	|1/sqrt(12)*sqrt(80)	|sqrt((0.5+0.5)^2/12)	|[('R.0.0', 1.0, u'1', u'(0.5+0.5)^2')]	|
|25	|1/sqrt(12)*sqrt(80)	|(1/12)^(2)	|[('R.0.0', 1.0, u'1', u'1')]	|
|26	|1/sqrt(12)*sqrt(90)	|sqrt(((.5+.5)^2)/12)	|[('R.0.0', 1.0, u'1', u'(.5+.5)^2')]	|




### (70) Mistake Group Digits of size 70




### (70) Mistake Group ['R.0'] of size 70
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|1/sqrt(12)*sqrt(100)	|(sqrt(1/12)) ^ 100	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'sqrt(1/12)')]	|
|1	|1/sqrt(12)*sqrt(40)	|sqrt(1/12 ( .5 - (-.5) )^2) * 2	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'sqrt(1/12 ( .5 - (-.5) )^2)')]	|
|2	|1/sqrt(12)*sqrt(60)	|(1/12)^0.5^60	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'(1/12)^0.5')]	|
|3	|1/sqrt(12)*sqrt(60)	|(1/12)^0.5*60	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'(1/12)^0.5')]	|
|4	|1/sqrt(12)*sqrt(80)	|1/sqrt(12)*sqrt(50)	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'1/sqrt(12)')]	|
|5	|1/sqrt(12)*sqrt(80)	|(1/12)^(1/2)*80	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'(1/12)^(1/2)')]	|
|6	|1/sqrt(12)*sqrt(80)	|((1/12)^(1/2))*80	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'(1/12)^(1/2)')]	|
|7	|1/sqrt(12)*sqrt(80)	|sqrt((1/12))*80	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'sqrt((1/12))')]	|
|8	|1/sqrt(12)*sqrt(70)	|0.288675134595*70	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'0.288675134595')]	|
|9	|1/sqrt(12)*sqrt(65)	|(1/12)^(1/2)/65	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'(1/12)^(1/2)')]	|
|10	|1/sqrt(12)*sqrt(100)	|(1/12^(1/2))100	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'1/12^(1/2)')]	|
|11	|1/sqrt(12)*sqrt(45)	|1/sqrt(12)*sqrt(40)	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'1/sqrt(12)')]	|
|12	|1/sqrt(12)*sqrt(90)	|1/12^0.5*90	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'1/12^0.5')]	|
|13	|1/sqrt(12)*sqrt(50)	|sqrt(1/12)*50	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'sqrt(1/12)')]	|
|14	|1/sqrt(12)*sqrt(50)	|sqrt(1/12)*25	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'sqrt(1/12)')]	|
|15	|1/sqrt(12)*sqrt(50)	|sqrt(1/12) * 50	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'sqrt(1/12)')]	|
|16	|1/sqrt(12)*sqrt(80)	|sqrt(1/12) * 80	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'sqrt(1/12)')]	|
|17	|1/sqrt(12)*sqrt(65)	|sqrt(1/12)*65	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'sqrt(1/12)')]	|
|18	|1/sqrt(12)*sqrt(65)	|(sqrt(1/12))*65	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'sqrt(1/12)')]	|
|19	|1/sqrt(12)*sqrt(60)	|0.288675*60	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'0.288675')]	|
|20	|1/sqrt(12)*sqrt(60)	|sqrt(1/12(0.5--0.5)^2)/60	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'sqrt(1/12(0.5--0.5)^2)')]	|
|21	|1/sqrt(12)*sqrt(80)	|((1/12)^0.5)/(8^0.5)	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'(1/12)^0.5')]	|
|22	|1/sqrt(12)*sqrt(95)	|sqrt(1/12)/95	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'sqrt(1/12)')]	|
|23	|1/sqrt(12)*sqrt(75)	|sqrt(1/12(1))*75	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'sqrt(1/12(1))')]	|
|24	|1/sqrt(12)*sqrt(90)	|sqrt(1/12) * 90	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'sqrt(1/12)')]	|
|25	|1/sqrt(12)*sqrt(75)	|sqrt(1/12(1)) * 75	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'sqrt(1/12(1))')]	|
|26	|1/sqrt(12)*sqrt(60)	|sqrt(1/sqrt(12))	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'1/sqrt(12)')]	|
|27	|1/sqrt(12)*sqrt(90)	|(((1/12)(1))^(.5))/2	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'((1/12)(1))^(.5)')]	|
|28	|1/sqrt(12)*sqrt(90)	|(1/12)^0.5*90	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'(1/12)^0.5')]	|
|29	|1/sqrt(12)*sqrt(80)	|1/(12)^(1/2) + 1/(12)^(1/2)	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'1/(12)^(1/2)')]	|
|30	|1/sqrt(12)*sqrt(100)	|sqrt((1/12)*(1)^2)*100	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'sqrt((1/12)*(1)^2)')]	|
|31	|1/sqrt(12)*sqrt(100)	|sqrt((1/12)*(1)^2)*99	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'sqrt((1/12)*(1)^2)')]	|
|32	|1/sqrt(12)*sqrt(55)	|sqrt(1/12)*2	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'sqrt(1/12)')]	|
|33	|1/sqrt(12)*sqrt(55)	|sqrt(1/12)/2	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'sqrt(1/12)')]	|
|34	|1/sqrt(12)*sqrt(55)	|sqrt(1/12)/55	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'sqrt(1/12)')]	|
|35	|1/sqrt(12)*sqrt(75)	|(1/12(1)^2)^(1/2) * 75	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'(1/12(1)^2)^(1/2)')]	|
|36	|1/sqrt(12)*sqrt(45)	|sqrt(1/12)45	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'sqrt(1/12)')]	|
|37	|1/sqrt(12)*sqrt(65)	|sqrt(1/12)*6	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'sqrt(1/12)')]	|
|38	|1/sqrt(12)*sqrt(75)	|sqrt(1/12(1)) /2	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'sqrt(1/12(1))')]	|
|39	|1/sqrt(12)*sqrt(75)	|sqrt(1/12(1))^75	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'sqrt(1/12(1))')]	|
|40	|1/sqrt(12)*sqrt(75)	|0.288675 * 75	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'0.288675')]	|
|41	|1/sqrt(12)*sqrt(45)	|(1/12)^(0.5)(45)	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'(1/12)^(0.5)')]	|
|42	|1/sqrt(12)*sqrt(75)	|0.288675*75	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'0.288675')]	|
|43	|1/sqrt(12)*sqrt(45)	|(1/12)^(0.5)(22.5)	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'(1/12)^(0.5)')]	|
|44	|1/sqrt(12)*sqrt(45)	|(1/12)^(0.5)(90)	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'(1/12)^(0.5)')]	|
|45	|1/sqrt(12)*sqrt(50)	|sqrt((1/12))/1	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'sqrt((1/12))')]	|
|46	|1/sqrt(12)*sqrt(50)	|sqrt((1/12))*10	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'sqrt((1/12))')]	|
|47	|1/sqrt(12)*sqrt(50)	|sqrt((1/12))*50	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'sqrt((1/12))')]	|
|48	|1/sqrt(12)*sqrt(85)	|(1/12)^(1/2) * 85	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'(1/12)^(1/2)')]	|
|49	|1/sqrt(12)*sqrt(65)	|sqrt(1/12*(1)^2)*65	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'sqrt(1/12*(1)^2)')]	|
|50	|1/sqrt(12)*sqrt(95)	|0.288675135*95	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'0.288675135')]	|
|51	|1/sqrt(12)*sqrt(90)	|sqrt(1/12)/90	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'sqrt(1/12)')]	|
|52	|1/sqrt(12)*sqrt(40)	|sqrt(1/12)*40	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'sqrt(1/12)')]	|
|53	|1/sqrt(12)*sqrt(90)	|sqrt(1/12)/45	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'sqrt(1/12)')]	|
|54	|1/sqrt(12)*sqrt(100)	|0.288675*100	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'0.288675')]	|
|55	|1/sqrt(12)*sqrt(90)	|(sqrt(1/12))^90	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'sqrt(1/12)')]	|
|56	|1/sqrt(12)*sqrt(80)	|(((1/12)(1)^(2))^(1/2))*80	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'((1/12)(1)^(2))^(1/2)')]	|
|57	|1/sqrt(12)*sqrt(75)	|(sqrt(1/12))^75	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'sqrt(1/12)')]	|
|58	|1/sqrt(12)*sqrt(85)	|(1/12)^0.5/12	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'(1/12)^0.5')]	|
|59	|1/sqrt(12)*sqrt(90)	|sqrt(((.5+.5)^2)/12)*90	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'sqrt(((.5+.5)^2)/12)')]	|
|60	|1/sqrt(12)*sqrt(100)	|sqrt(1/12)*100	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'sqrt(1/12)')]	|




### (40) Mistake Group redirect of size 40




### (3) Mistake Group ['R.0', 'R.1.0'] of size 3
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|1/sqrt(12)*sqrt(80)	|sqrt(1/12) * 80^2	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'sqrt(1/12)'), ('R.1.0', 80.0, u'80', u'80')]	|
|1	|1/sqrt(12)*sqrt(55)	|sqrt(1/12)*55^2	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'sqrt(1/12)'), ('R.1.0', 55.0, u'55', u'55')]	|
|2	|1/sqrt(12)*sqrt(65)	|sqrt(1/12)*(65^2)	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'sqrt(1/12)'), ('R.1.0', 65.0, u'65', u'65')]	|




### (3) Mistake Group ['R.0.1.0'] of size 3
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|1/sqrt(12)*sqrt(65)	|sqrt(65*11/12^2)	|[('R.0.1.0', 12.0, u'12', u'12')]	|
|1	|1/sqrt(12)*sqrt(50)	|sqrt(50*11/12^2)	|[('R.0.1.0', 12.0, u'12', u'12')]	|
|2	|1/sqrt(12)*sqrt(50)	|sqrt(50/12^2)	|[('R.0.1.0', 12.0, u'12', u'12')]	|




### (2) Mistake Group ['R.1.0'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|1/sqrt(12)*sqrt(60)	|1/60sqrt(1/12(.5+.5)^2)	|[('R.1.0', 60.0, u'60', u'60')]	|
|1	|1/sqrt(12)*sqrt(100)	|1/(100*sqrt(12))	|[('R.1.0', 100.0, u'100', u'100')]	|




### (2) Mistake Group ['R.0.1'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|1/sqrt(12)*sqrt(60)	|sqrt(60/sqrt(12))	|[('R.0.1', 3.4641016151377544, u'sqrt(12)', u'sqrt(12)')]	|




### (2) Mistake Group ['R.0', 'R.1'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|1/sqrt(12)*sqrt(65)	|sqrt(1/12)/sqrt(65)	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'sqrt(1/12)'), ('R.1', 8.06225774829855, u'sqrt(65)', u'sqrt(65)')]	|
|1	|1/sqrt(12)*sqrt(65)	|(sqrt(1/12))/(sqrt(65))	|[('R.0', 0.2886751345948129, u'1/sqrt(12)', u'sqrt(1/12)'), ('R.1', 8.06225774829855, u'sqrt(65)', u'sqrt(65)')]	|




### (1) Mistake Group ['R.0.0', 'R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|1/sqrt(12)*sqrt(45)	|(1/12)(22.5+22.5)^(0.5)	|[('R.0.0', 1.0, u'1', u'1'), ('R.1', 6.708203932499369, u'sqrt(45)', u'(22.5+22.5)^(0.5)')]	|




### (1) Mistake Group Wrong_Sign of size 1




### (1) Mistake Group ['R.0.0', 'R.1.0'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|1/sqrt(12)*sqrt(85)	|(1/12)( (85*0.5) - (85*-0.5) ) **2	|[('R.0.0', 1.0, u'1', u'1'), ('R.1.0', 85.0, u'85', u'(85*0.5) - (85*-0.5)')]	|




### (127) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:gthorn

	first_attempt
					2015-11-05 07:13:41
	part2_correct_attempt
					['0:01:10', u'sqrt(1/12 * (.5 + .5)^2)']
	part3_correct_attempt
					['0:01:32', u'0']
	part4_incorrect_attempt
					('0:01:53', u'0.288675')
	part4_correct_attempt
					['0:09:26', u'sqrt(80/12 * (.5 + .5)^2)']

1 Student ID:phodgson

	first_attempt
					2015-11-06 06:44:32
	part2_correct_attempt
					['0:00:56', u'sqrt(1/12)']
	part3_correct_attempt
					['0:00:00', u'0']
	part4_incorrect_attempt
					('0:00:56', u'90*sqrt(1/12)')
	part4_correct_attempt
					['0:01:24', u'sqrt(90/12)']

2 Student ID:apokhare

	first_attempt
					2015-11-05 22:11:10
	part2_correct_attempt
					['0:00:00', u'sqrt(1/12)']
	part3_correct_attempt
					['0:00:00', u'0']
	part4_incorrect_attempt
					('0:00:00', u'1/(sqrt(12)*sqrt(40))')
	part4_correct_attempt
					['0:02:44', u'sqrt(40) / sqrt(12)']

3 Student ID:kew060

	first_attempt
					2015-11-03 02:12:39
	part2_correct_attempt
					['2 days, 21:33:22', u'(1/12)^(1/2)']
	part3_correct_attempt
					['0:00:28', u'0']
	part4_incorrect_attempt
					('3 days, 20:45:02', u'(60/12)^(1/2)')
	part4_correct_attempt
					['3 days, 20:45:17', u'(65/12)^(1/2)']

4 Student ID:kvass

	first_attempt
					2015-11-06 00:32:29
	part2_correct_attempt
					['0:00:00', u'sqrt(1/12)']
	part3_correct_attempt
					['0:08:11', u'0']
	part4_incorrect_attempt
					('0:08:11', u'1/(sqrt(1/12 * 50))')
					('0:08:45', u'1/(sqrt(12 * 50))')
					('0:09:53', u'1/(sqrt(12) * sqrt(50))')
	part4_correct_attempt
					['0:11:55', u'sqrt(1/12 * 50)']

5 Student ID:kbielawi

	first_attempt
					2015-11-05 21:37:38
	part2_correct_attempt
					['4:01:37', u'sqrt(1/12)']
	part3_correct_attempt
					['0:01:19', u'0']
	part4_incorrect_attempt
					('4:03:33', u'85*sqrt(1/12)')
	part4_correct_attempt
					['4:03:50', u'sqrt(85/12)']

6 Student ID:jguanzho

	first_attempt
					2015-11-05 17:44:38
	part2_correct_attempt
					['0:19:20', u'(1/12)**0.5']
	part3_correct_attempt
					['0:00:00', u'0']
	part4_incorrect_attempt
					('0:19:36', u'80 *(1/12)**0.5')
					('0:25:10', u'(0.25*80)**0.5')
					('0:25:49', u'40*(1/12)**0.5')
					('4:54:36', u'80*(1/12)**0.5')
	part4_correct_attempt
					['4:55:22', u'(80/12)**0.5']

7 Student ID:alakamsa

	first_attempt
					2015-11-02 19:37:10
	part2_correct_attempt
					['1 day, 23:50:40', u'sqrt(1/12)']
	part3_correct_attempt
					['0:00:00', u'0']
	part4_incorrect_attempt
					('1 day, 23:51:28', u'sqrt((1/12) * 4)')
					('1 day, 23:52:15', u'sqrt((1/12) * (50^2))')
					('1 day, 23:55:04', u'sqrt((1/12) * 25^2)')
					('1 day, 23:55:37', u'sqrt((1/12) * 2^2)')
					('2 days, 0:15:04', u'sqrt((25^2)/12)')
					('2 days, 0:15:13', u'sqrt((50^2)/12)')
					('2 days, 0:15:35', u'sqrt((12.5^2)/12)')
					('2 days, 0:43:48', u'e^25*(25^25/25!)')
					('2 days, 0:43:59', u'e^-25*(25^25/25!)')
					('2 days, 0:44:14', u'sqrt(e^-25*(25^25/25!))')
					('2 days, 0:45:00', u'sqrt(25)')
					('2 days, 0:45:11', u'sqrt(0)')
	part4_correct_attempt
					['2 days, 0:46:25', u'sqrt(1/12 * 50)']

8 Student ID:jhc010

	first_attempt
					2015-11-06 11:00:36
	part2_correct_attempt
					['0:00:00', u'sqrt(1/12)']
	part3_correct_attempt
					['0:00:20', u'0']
	part4_incorrect_attempt
					('0:00:35', u'55*sqrt(1/12)')
					('0:00:42', u'2*sqrt(1/12)')
					('0:01:00', u'55*sqrt(1/12)')
					('0:01:56', u'sqrt(55^2*(1/12))')
					('0:02:28', u'55*sqrt(1/12)')
	part4_correct_attempt
					['0:03:44', u'sqrt(55*(sqrt(1/12)^2))']

9 Student ID:mhale

	first_attempt
					2015-11-05 20:36:39
	part2_correct_attempt
					['0:00:57', u'(1/12(1)^2)^(1/2)']
	part3_correct_attempt
					['0:02:03', u'0']
	part4_incorrect_attempt
					('0:02:29', u'(75^2/12(1)^2)^(1/2)')
					('0:03:36', u'(1/12(1)^2)^(1/2)')
					('0:04:17', u'[75^2 * (1/12(1)^2)] ^ (1/2)')
	part4_correct_attempt
					['0:04:26', u'[75 * (1/12(1)^2)] ^ (1/2)']

10 Student ID:nhn018

	first_attempt
					2015-11-05 05:47:59
	part2_correct_attempt
					['0:13:44', u'1/sqrt(12)']
	part3_correct_attempt
					['0:13:00', u'0']
	part4_incorrect_attempt
					('0:14:22', u'1/(sqrt(12)*sqrt(50))')
					('0:15:06', u'1/(sqrt(12)*sqrt(45))')
	part4_correct_attempt
					['0:15:28', u'1/sqrt(12)*sqrt(45)']

11 Student ID:j5phung

	first_attempt
					2015-11-04 21:17:03
	part2_correct_attempt
					['0:06:25', u'sqrt(1/12)']
	part3_correct_attempt
					['0:14:34', u'0']
	part4_incorrect_attempt
					('0:25:36', u'sqrt(10/3)')
	part4_correct_attempt
					['0:26:07', u'sqrt(80/12)']

12 Student ID:jyc018

	first_attempt
					2015-11-05 00:14:14
	part2_correct_attempt
					['0:03:22', u'sqrt(1/12)']
	part3_correct_attempt
					['0:01:18', u'0']
	part4_incorrect_attempt
					('0:15:09', u'.5')
					('0:21:43', u'2.887')
					('23:12:07', u'sqrt(85/12)')
	part4_correct_attempt
					['23:12:13', u'sqrt(75/12)']

13 Student ID:vqt004

	first_attempt
					2015-11-06 06:24:52
	part2_correct_attempt
					['0:06:03', u'sqrt(1/12)']
	part3_correct_attempt
					['0:00:32', u'0']
	part4_incorrect_attempt
					('0:06:03', u'2*sqrt(1/12)')
					('0:06:28', u'90*sqrt(1/12)')
	part4_correct_attempt
					['0:06:40', u'sqrt(90/12)']

14 Student ID:mnrahman

	first_attempt
					2015-11-07 00:05:33
	part2_correct_attempt
					['0:00:21', u'sqrt(1/12)']
	part3_correct_attempt
					['0:00:42', u'0']
	part4_incorrect_attempt
					('0:00:42', u'sqrt(100)/sqrt(12)')
	part4_correct_attempt
					['0:02:20', u'sqrt(85)/sqrt(12)']

15 Student ID:r9jiang

	first_attempt
					2015-11-02 03:50:08
	part2_correct_attempt
					['0:00:00', u'(1/12)^(1/2)']
	part3_correct_attempt
					['0:00:00', u'0']
	part4_incorrect_attempt
					('0:04:17', u'(4/3)^(1/2)')
					('0:13:01', u'65*(1/12)^(1/2)')
					('0:14:14', u'65*65*((1/12)^(1/2))')
					('2 days, 2:05:46', u'65*(1/12)^(1/2)')
	part4_correct_attempt
					['3 days, 1:23:13', u'(65/12)^(1/2)']

16 Student ID:rlhagen

	first_attempt
					2015-10-31 19:49:30
	part2_correct_attempt
					['0:01:07', u'sqrt((1/12)(0.5-(-0.5))^2)']
	part3_correct_attempt
					['0:13:41', u'((-0.5+0.5)/2)/(sqrt((1/12)(0.5-(-0.5))^2))']
	part4_incorrect_attempt
					('0:14:14', u'((-0.5+0.5)/2)/(sqrt((1/12)(0.5-(-0.5))^2))')
					('0:15:45', u'(-0.5+0.5)/2')
	part4_correct_attempt
					['0:18:38', u'sqrt((75*1/12)(0.5-(-0.5))^2)']

17 Student ID:dgunawan

	first_attempt
					2015-11-05 08:57:44
	part2_correct_attempt
					['15:18:43', u'(1/12)^(1/2)']
	part3_correct_attempt
					['15:17:38', u'(-.5+.5)/2 *85']
	part4_incorrect_attempt
					('15:20:20', u'((-.5+.5)/2 *85 (1-(-.5+.5)/2))^(1/2)')
	part4_correct_attempt
					['15:30:45', u'(85/12)^(1/2)']

18 Student ID:aggouw

	first_attempt
					2015-11-04 09:07:52
	part2_correct_attempt
					['0:00:19', u'sqrt(1/12)']
	part3_correct_attempt
					['0:00:24', u'0']
	part4_incorrect_attempt
					('0:00:37', u'sqrt(40/12)')
					('0:00:50', u'sqrt(20/12)')
					('0:00:53', u'sqrt(30/12)')
					('0:02:53', u'sqrt(10/12)')
					('0:03:01', u'sqrt(0/12)')
					('0:03:23', u'sqrt(5/12)')
					('0:03:29', u'sqrt(2/12)')
					('0:03:33', u'sqrt(3/12)')
					('0:03:37', u'sqrt(4/12)')
					('0:03:41', u'sqrt(5/12)')
					('0:03:45', u'sqrt(6/12)')
					('0:03:50', u'sqrt(7/12)')
					('0:03:59', u'sqrt(8/12)')
					('0:04:04', u'sqrt(9/12)')
					('0:04:07', u'sqrt(10/12)')
					('0:04:13', u'sqrt(11/12)')
					('0:04:18', u'sqrt(12/12)')
					('0:04:22', u'sqrt(13/12)')
					('0:04:26', u'sqrt(14/12)')
					('0:04:32', u'sqrt(80/12)')
					('0:04:38', u'sqrt(13/12)')
					('0:04:42', u'sqrt(14/12)')
					('0:04:45', u'sqrt(15/12)')
					('0:04:49', u'sqrt(16/12)')
					('0:04:53', u'sqrt(17/12)')
	part4_correct_attempt
					['0:05:01', u'sqrt(45/12)']

19 Student ID:tcn013

	first_attempt
					2015-11-05 20:57:24
	part2_correct_attempt
					['0:01:52', u'sqrt(1/12)']
	part3_correct_attempt
					['0:02:06', u'0']
	part4_incorrect_attempt
					('0:04:35', u'.5*45')
	part4_correct_attempt
					['0:05:59', u'sqrt(45/12)']

20 Student ID:tstevens

	first_attempt
					2015-11-06 12:10:21
	part2_correct_attempt
					['0:02:57', u'.288675135']
	part3_correct_attempt
					['0:03:18', u'0']
	part4_incorrect_attempt
					('0:03:18', u'0.288675135')
					('0:03:56', u'0.288675135')
					('0:05:16', u'27.424137787')
					('0:07:45', u'54.848275573')
	part4_correct_attempt
					['0:09:50', u'2.813657164']

21 Student ID:l8ngo

	first_attempt
					2015-11-05 23:17:21
	part2_correct_attempt
					['0:00:00', u'sqrt(1/12*[0.5+0.5]^2)']
	part3_correct_attempt
					['4:35:40', u'0']
	part4_incorrect_attempt
					('4:36:22', u'sqrt(1/12*[0.5+0.5]^2)')
					('5:01:17', u'40*sqrt(1/12*[0.5+0.5]^2)')
					('5:04:20', u'sqrt([40^2]*1/12*[0.5+0.5]^2)')
	part4_correct_attempt
					['5:06:25', u'sqrt(40*1/12*[0.5+0.5]^2)']

22 Student ID:djk006

	first_attempt
					2015-11-04 06:02:17
	part2_correct_attempt
					['0:00:00', u'1/12^(1/2)']
	part3_correct_attempt
					['0:00:42', u'0']
	part4_incorrect_attempt
					('0:01:43', u'100/12^(1/2)')
					('0:08:22', u'(1/12^(1/2))')
	part4_correct_attempt
					['14:47:20', u'(10/12^(1/2))']

23 Student ID:dando

	first_attempt
					2015-11-06 23:46:43
	part2_correct_attempt
					['0:01:49', u'sqrt(1/12)']
	part3_correct_attempt
					['0:06:10', u'0']
	part4_incorrect_attempt
					('0:06:55', u'1/2')
					('0:28:09', u'1/4')
	part4_correct_attempt
					['0:50:57', u'sqrt(80/12)']

24 Student ID:abasu

	first_attempt
					2015-11-05 04:56:21
	part2_correct_attempt
					['0:42:28', u'sqrt(1/12)']
	part3_correct_attempt
					['0:08:14', u'0']
	part4_incorrect_attempt
					('0:57:43', u'80*sqrt(1/12)')
	part4_correct_attempt
					['0:57:54', u'sqrt(80/12)']

25 Student ID:achava

	first_attempt
					2015-11-06 08:21:51
	part2_correct_attempt
					['0:03:18', u'sqrt(1/12)']
	part3_correct_attempt
					['0:06:04', u'0']
	part4_incorrect_attempt
					('0:07:00', u'1/12')
					('0:07:25', u'0.5')
	part4_correct_attempt
					['0:08:27', u'sqrt(55/12)']

26 Student ID:ssamudra

	first_attempt
					2015-11-05 06:46:25
	part2_correct_attempt
					['0:00:00', u'1/sqrt(12)']
	part3_correct_attempt
					['0:01:06', u'0']
	part4_incorrect_attempt
					('0:01:06', u'75/sqrt(12)')
	part4_correct_attempt
					['0:01:37', u'sqrt(75)/sqrt(12)']

27 Student ID:flhernan

	first_attempt
					2015-11-03 20:58:27
	part2_correct_attempt
					['0:00:45', u'sqrt(1/12)']
	part3_correct_attempt
					['0:02:31', u'0']
	part4_incorrect_attempt
					('0:03:56', u'sqrt((1/12)*80^2)')
					('0:04:59', u'sqrt((1/12)*1^2)')
	part4_correct_attempt
					['0:05:35', u'sqrt((1/12)*80)']

28 Student ID:c1wei

	first_attempt
					2015-11-05 05:04:06
	part2_correct_attempt
					['0:01:16', u'sqrt(1/12)']
	part3_correct_attempt
					['0:00:21', u'0']
	part4_incorrect_attempt
					('0:03:33', u'.5')
					('0:03:41', u'sqrt(.5)')
					('0:04:04', u'sqrt(.5)')
					('0:05:28', u'1/95')
					('0:07:15', u'sqrt(95)')
					('0:08:56', u'sqrt(0)')
					('0:09:09', u'1/12')
	part4_correct_attempt
					['0:09:29', u'sqrt((1/12)*95)']

29 Student ID:mitopete

	first_attempt
					2015-11-04 05:20:00
	part2_correct_attempt
					['0:00:47', u'((1/12)(1)^(2))^(1/2)']
	part3_correct_attempt
					['2 days, 17:57:44', u'0']
	part4_incorrect_attempt
					('2 days, 17:58:36', u'((1/12)(1)^(2))^(1/2)')
					('2 days, 18:05:05', u'1/12')
					('2 days, 18:05:17', u'1/(12)^(1/2)')
					('2 days, 18:06:09', u'1/(12)^(2)')
					('2 days, 18:14:12', u'(((1/12)(80)^(2))^(1/2))')
					('2 days, 18:15:06', u'(((1/12)(3240)^(2))^(1/2))')
	part4_correct_attempt
					['2 days, 18:16:25', u'(((1/12)*80)^(1/2))']

30 Student ID:m8woo

	first_attempt
					2015-11-06 18:40:07
	part2_correct_attempt
					['0:02:05', u'sqrt(1/12 * (0.5 - -0.5)^2)']
	part3_correct_attempt
					['0:03:22', u'0']
	part4_incorrect_attempt
					('0:03:22', u'sqrt(1/12 * (0.5 - -0.5)^2)')
	part4_correct_attempt
					['0:11:59', u'sqrt(75* 1/12 * (0.5 - -0.5)^2)']

31 Student ID:akg009

	first_attempt
					2015-11-06 21:08:58
	part2_correct_attempt
					['0:00:41', u'sqrt(1/12)']
	part3_correct_attempt
					['0:01:22', u'0']
	part4_incorrect_attempt
					('0:03:15', u'90*sqrt(1/12)')
					('0:03:52', u'45sqrt(1/12)')
					('0:52:56', u'90*sqrt(1/12)')
					('1:58:43', u'sqrt((1/12)*45)')
	part4_correct_attempt
					['1:58:51', u'sqrt((1/12)*90)']

32 Student ID:jhp077

	first_attempt
					2015-11-05 13:54:00
	part2_correct_attempt
					['0:00:00', u'1/(12)^(1/2)']
	part3_correct_attempt
					['0:00:13', u'0']
	part4_incorrect_attempt
					('0:00:40', u'2/(12)^(1/2)')
					('0:00:51', u'1/(12)^(1/2)')
					('0:02:46', u'1/(6)^(1/2)')
					('0:08:46', u'1/(3)^(1/2)')
					('0:08:53', u'1/(12)^(1/2)')
					('0:08:59', u'1/(24)^(1/2)')
					('0:10:06', u'1/(3)^(1/2)')
	part4_correct_attempt
					['0:10:57', u'(80/12)^(1/2)']

33 Student ID:jit002

	first_attempt
					2015-11-05 18:29:03
	part2_correct_attempt
					['0:09:50', u'(1/12)^0.5']
	part3_correct_attempt
					['0:12:45', u'0']
	part4_incorrect_attempt
					('0:12:45', u'(1/12*(60)^2)^0.5')
					('0:19:19', u'((1/12)*60)^1/2')
	part4_correct_attempt
					['0:19:36', u'((1/12)*60)^0.5']

34 Student ID:druble

	first_attempt
					2015-11-05 00:26:41
	part2_correct_attempt
					['0:00:00', u'(1/12)^(1/2) * (0.5 + 0.5)']
	part3_correct_attempt
					['0:00:00', u'((-0.5 + 0.5) / 2) * 75']
	part4_incorrect_attempt
					('0:00:00', u'(1/12)^(1/2) * (0.5 + 0.5) * 75')
	part4_correct_attempt
					['0:03:13', u'((1/12) * (0.5 + 0.5)^2 * 75)^(1/2)']

35 Student ID:h4tu

	first_attempt
					2015-11-06 23:48:34
	part2_correct_attempt
					['0:00:42', u'sqrt(1/12)']
	part3_correct_attempt
					['0:03:30', u'0']
	part4_incorrect_attempt
					('0:03:40', u'75*sqrt(1/12)')
					('0:04:18', u'75^2 * sqrt(1/12)')
	part4_correct_attempt
					['0:04:44', u'sqrt( 75/12)']

36 Student ID:jag028

	first_attempt
					2015-11-03 21:50:42
	part2_correct_attempt
					['0:01:49', u'sqrt[1/12]']
	part3_correct_attempt
					['0:02:04', u'0']
	part4_incorrect_attempt
					('0:02:30', u'1/12')
	part4_correct_attempt
					['2 days, 19:41:42', u'sqrt[1/12*90]']

37 Student ID:ccn001

	first_attempt
					2015-11-05 16:26:42
	part2_correct_attempt
					['-1 day, 23:59:26', u'((1/12)(1))^(0.5)']
	part3_correct_attempt
					['0:02:29', u'0']
	part4_incorrect_attempt
					('0:02:29', u'((1/12)(45)^2)^(0.5)')
					('0:02:50', u'((1/12)(1)^2)^(0.5)')
					('0:06:07', u'45*((1/12)(1)^2)^(0.5)')
					('0:09:05', u'((1/12)(50)^2)^(0.5)')
					('5:55:03', u'75*(((1/12)(1))^(0.5))')
					('5:55:11', u'45*(((1/12)(1))^(0.5))')
					('5:58:51', u'((1/12)(22.5+22.5)^(2))^(0.5)')
	part4_correct_attempt
					['14:53:54', u'(45/12)^(0.5)']

38 Student ID:asetters

	first_attempt
					2015-11-05 20:24:36
	part2_correct_attempt
					['0:00:23', u'sqrt(1/12)']
	part3_correct_attempt
					['0:00:43', u'0']
	part4_incorrect_attempt
					('0:01:41', u'85*sqrt(1/12)')
	part4_correct_attempt
					['0:05:21', u'sqrt(85/12)']

39 Student ID:atorr

	first_attempt
					2015-11-05 20:29:27
	part2_correct_attempt
					['0:00:22', u'(1/12)^0.5']
	part3_correct_attempt
					['0:00:56', u'0']
	part4_incorrect_attempt
					('0:01:51', u'1/12')
					('0:02:21', u'1/12')
					('3:55:42', u'65 * (1/12)^0.5')
					('3:56:16', u'(65/2) * (1/12)^0.5')
					('3:56:28', u'65 * (1/12)^0.5')
	part4_correct_attempt
					['3:56:39', u'(65 * (1/12))^0.5']

40 Student ID:asp025

	first_attempt
					2015-11-06 23:24:43
	part2_correct_attempt
					['0:09:25', u'[(.5+.5)^2/12]^(1/2)']
	part3_correct_attempt
					['0:01:25', u'0']
	part4_incorrect_attempt
					('0:09:54', u'85[(.5+.5)^2/12]^(1/2)')
	part4_correct_attempt
					['0:11:19', u'[85(.5+.5)^2/12]^(1/2)']

41 Student ID:beyounge

	first_attempt
					2015-10-30 06:12:24
	part2_correct_attempt
					['0:00:00', u'sqrt(1/12)']
	part3_correct_attempt
					['0:02:45', u'0']
	part4_incorrect_attempt
					('0:06:18', u'100 * sqrt(1/12)')
					('0:06:29', u'50 * sqrt(1/12)')
	part4_correct_attempt
					['0:08:53', u'sqrt(100/12)']

42 Student ID:tpmach

	first_attempt
					2015-11-04 23:21:18
	part2_correct_attempt
					['0:01:03', u'sqrt(1/12(0.5+0.5)^2)']
	part3_correct_attempt
					['0:02:09', u'0']
	part4_incorrect_attempt
					('0:03:04', u'sqrt(1/12(0.5+0.5)^2)')
					('0:03:33', u'sqrt(1/12(40)^2)')
					('0:06:24', u'sqrt(1/12(0.5)^2)')
					('3:54:50', u'1/6')
					('3:55:20', u'1/3')
	part4_correct_attempt
					['4:02:20', u'sqrt(40*1/12(0.5+0.5)^2)']

43 Student ID:rraiyyan

	first_attempt
					2015-11-07 00:00:13
	part2_correct_attempt
					['0:01:01', u'sqrt(1/12)']
	part3_correct_attempt
					['0:04:28', u'0']
	part4_incorrect_attempt
					('0:04:51', u'1/12')
					('0:05:07', u'0.5')
					('0:05:43', u'85/sqrt(1/12)')
					('0:05:54', u'85 * sqrt(1/12)')
					('0:06:18', u'1/12')
					('0:07:25', u'1/2')
					('0:09:04', u'85^2/2')
					('0:09:17', u'85^2/12')
					('0:09:44', u'1/12')
					('0:09:54', u'0.25/12')
					('0:11:03', u'85/2 * sqrt(1/12)')
					('0:11:12', u'85 * sqrt(1/12)')
					('0:11:32', u'85 * (1/12)^1/2')
					('0:11:42', u'85 * (1/12)^(1/2)')
	part4_correct_attempt
					['0:12:41', u'sqrt(85/12)']

44 Student ID:t1tran

	first_attempt
					2015-11-04 00:37:13
	part2_correct_attempt
					['0:01:41', u'sqrt(1/12(.5+.5)^2)']
	part3_correct_attempt
					['0:11:06', u'60(-.5+.5)/2']
	part4_incorrect_attempt
					('0:11:06', u'60sqrt(1/12(.5+.5)^2)')
					('0:11:38', u'60^2sqrt(1/12(.5+.5)^2)')
					('0:11:59', u'sqrt(1/12(.5+.5)^2)')
	part4_correct_attempt
					['0:15:01', u'sqrt(60*1/12(.5+.5)^2)']

45 Student ID:thwan

	first_attempt
					2015-11-06 23:17:14
	part2_correct_attempt
					['0:00:00', u'1/(12)^(1/2)']
	part3_correct_attempt
					['0:00:00', u'0']
	part4_incorrect_attempt
					('0:00:00', u'1/12')
					('0:02:33', u'2/(12)^(1/2)')
					('0:03:05', u'(2/12)^(1/2)')
					('0:06:42', u'(1/12+1/12)^(1/2)')

46 Student ID:z3meng

	first_attempt
					2015-11-05 09:55:04
	part2_correct_attempt
					['0:00:47', u'(1/12)^0.5']
	part3_correct_attempt
					['0:01:33', u'0']
	part4_incorrect_attempt
					('0:03:09', u'90/(12)^2')
					('0:08:25', u'1/(12)^2')
	part4_correct_attempt
					['0:12:48', u'(90/12)^0.5']

47 Student ID:krkelkar

	first_attempt
					2015-10-31 21:49:34
	part2_correct_attempt
					['2 days, 2:40:49', u'sqrt((1/12)*(0.5-(-0.5))**2)']
	part3_correct_attempt
					['0:00:00', u'[(85*-0.5) + (85*0.5)]/2']
	part4_incorrect_attempt
					('2 days, 2:40:49', u'sqrt((1/12)( (85*0.5) - (85*-0.5) ) **2)')
	part4_correct_attempt
					['2 days, 2:46:54', u'sqrt(85*(1/12))']

48 Student ID:cprafull

	first_attempt
					2015-11-06 02:56:30
	part2_correct_attempt
					['0:01:07', u'sqrt(1/12)']
	part3_correct_attempt
					['0:01:31', u'0']
	part4_incorrect_attempt
					('0:03:06', u'80*sqrt(1/12)')
	part4_correct_attempt
					['0:03:15', u'sqrt(80/12)']

49 Student ID:jel075

	first_attempt
					2015-11-05 23:21:40
	part2_correct_attempt
					['0:00:27', u'sqrt(1/12)']
	part3_correct_attempt
					['0:00:27', u'0']
	part4_incorrect_attempt
					('0:02:22', u'85*sqrt(1/12)')
	part4_correct_attempt
					['0:02:54', u'sqrt(85/12)']

50 Student ID:edescobe

	first_attempt
					2015-11-04 12:13:40
	part2_correct_attempt
					['0:13:07', u'1/12^(1/2)']
	part3_correct_attempt
					['0:15:27', u'0']
	part4_incorrect_attempt
					('0:15:38', u'1/12^(1/2)')
					('0:18:55', u'(80/12)^(1/2)')
	part4_correct_attempt
					['0:19:21', u'(85/12)^(1/2)']

51 Student ID:etemlock

	first_attempt
					2015-11-06 00:46:10
	part2_correct_attempt
					['0:01:34', u'(1/12)^.5']
	part3_correct_attempt
					['0:02:28', u'0']
	part4_incorrect_attempt
					('0:03:11', u'65/(12)^.5')
					('0:03:36', u'65 * (1.12)^.5')
	part4_correct_attempt
					['0:04:05', u'(65/12)^.5']

52 Student ID:ggaddi

	first_attempt
					2015-11-05 05:42:50
	part2_correct_attempt
					['0:00:41', u'sqrt(1/12)']
	part3_correct_attempt
					['0:01:40', u'0']
	part4_incorrect_attempt
					('0:01:55', u'sqrt((1/12)*(75*0.5+75*0.5)^2)')
					('0:03:18', u'75*sqrt(1/12)')
	part4_correct_attempt
					['0:03:31', u'sqrt(75/12)']

53 Student ID:muy002

	first_attempt
					2015-11-06 04:43:41
	part2_correct_attempt
					['0:03:07', u'sqrt(1/12)']
	part3_correct_attempt
					['0:03:18', u'0']
	part4_incorrect_attempt
					('0:10:11', u'sqrt(2/12)')
					('0:10:16', u'sqrt(4/12)')
					('0:17:39', u'65*sqrt(1/12)')
	part4_correct_attempt
					['0:17:52', u'sqrt(65/12)']

54 Student ID:cstringh

	first_attempt
					2015-11-04 07:24:44
	part2_correct_attempt
					['0:00:41', u'sqrt(1/12)']
	part3_correct_attempt
					['0:01:23', u'0']
	part4_incorrect_attempt
					('0:03:02', u'1/((sqrt(12))*sqrt(70))')
	part4_correct_attempt
					['0:03:33', u'1/(sqrt(12))*sqrt(70)']

55 Student ID:dan029

	first_attempt
					2015-11-05 09:34:22
	part2_correct_attempt
					['0:00:41', u'1/sqrt(12)']
	part3_correct_attempt
					['0:04:41', u'0']
	part4_incorrect_attempt
					('0:04:41', u'1/sqrt(12)^60')
					('0:05:22', u'1/sqrt(12)')
					('0:06:24', u'60/sqrt(12)')
					('0:19:30', u'60/sqrt(12)')
					('0:20:18', u'120/sqrt(12)')
	part4_correct_attempt
					['0:26:07', u'sqrt(60/12)']

56 Student ID:v4sharma

	first_attempt
					2015-11-05 23:23:24
	part2_correct_attempt
					['0:00:27', u'sqrt(1/12)']
	part3_correct_attempt
					['0:00:59', u'0']
	part4_incorrect_attempt
					('22:42:01', u'sqrt(75 * (1/12) * (.5 + .5)^2)')
					('22:44:22', u'sqrt(75 * (1/12 * (.5 + .5)^2))')
					('22:57:01', u'sqrt(75 * (1/12) * (.5 + .5)^2)')
					('23:30:36', u'sqrt(75 * (1/12) * (.5 + .5)^2)')
	part4_correct_attempt
					['23:32:59', u'sqrt(40 * (1/12) * (.5 + .5)^2)']

57 Student ID:ralhadda

	first_attempt
					2015-10-31 22:13:59
	part4_incorrect_attempt
					('3:33:00', u'65/12')

58 Student ID:dcastlem

	first_attempt
					2015-11-03 00:41:05
	part2_correct_attempt
					['1:33:42', u'sqrt(1/12)']
	part3_correct_attempt
					['0:00:00', u'0']
	part4_incorrect_attempt
					('1:34:20', u'sqrt(.5)')
					('1:34:30', u'sqrt(.5*.5)')
					('1:34:38', u'sqrt(.5*.5*1/12)')
					('1:36:25', u'1/12')
					('1:37:18', u'1/2')
					('1 day, 3:32:57', u'1/sqrt(12)')
					('3 days, 19:12:14', u'sqrt(1/12*90)')
	part4_correct_attempt
					['3 days, 19:12:24', u'sqrt(1/12*50)']

59 Student ID:hsc052

	first_attempt
					2015-11-06 23:07:48
	part2_correct_attempt
					['0:04:01', u'sqrt(1/12)']
	part3_correct_attempt
					['0:00:00', u'0']
	part4_incorrect_attempt
					('0:04:01', u'70*sqrt(1/12)')
					('0:07:51', u'70^2*sqrt(1/12)')
	part4_correct_attempt
					['0:12:06', u'sqrt(70)*sqrt(1/12)']

60 Student ID:dac064

	first_attempt
					2015-11-05 09:34:31
	part2_correct_attempt
					['0:00:48', u'((1/12)(1))^(.5)']
	part3_correct_attempt
					['0:05:04', u'0']
	part4_incorrect_attempt
					('0:12:13', u'((1/12)(1))^(.5)')
					('0:12:40', u'2*((1/12)(1))^(.5)')
					('0:19:45', u'((1/12)(1))^(.5)')
	part4_correct_attempt
					['0:25:04', u'((90/12)(1))^(.5)']

61 Student ID:v3doan

	first_attempt
					2015-11-05 16:26:50
	part2_correct_attempt
					['0:00:00', u'sqrt(1/12)']
	part3_correct_attempt
					['0:00:56', u'0']
	part4_incorrect_attempt
					('0:00:56', u'2sqrt(1/12)')
					('1 day, 8:15:28', u'85 sqrt(1/12)')
					('1 day, 8:15:52', u'sqrt(75/12)')
	part4_correct_attempt
					['1 day, 8:15:58', u'sqrt(85/12)']

62 Student ID:yil035

	first_attempt
					2015-11-05 21:14:50
	part2_correct_attempt
					['0:00:00', u'1/sqrt(12)']
	part3_correct_attempt
					['0:00:00', u'0']
	part4_incorrect_attempt
					('0:00:00', u'1/sqrt(6)')
					('0:02:52', u'1/sqrt(3)')
					('0:06:39', u'1/sqrt(12)')
					('0:07:05', u'sqrt(2/12)')
					('0:09:24', u'2/sqrt(12)')
					('0:09:39', u'2/sqrt(6)')
					('0:50:52', u'1/2')
	part4_correct_attempt
					['1:15:36', u'sqrt(100/12)']

63 Student ID:sghouse

	first_attempt
					2015-11-05 03:11:28
	part2_correct_attempt
					['0:00:00', u'sqrt(1/12)']
	part3_correct_attempt
					['0:00:00', u'0']
	part4_incorrect_attempt
					('0:00:00', u'75*sqrt(1/12)')
					('0:04:55', u'1/3')
					('0:06:39', u'.5')
					('0:08:56', u'sqrt(75^2/12)')
					('0:11:54', u'sqrt(32.5^2 *2)')
					('0:13:31', u'32.5/sqrt(12)')
					('17:39:21', u'sqrt(75^2/12)')
					('17:40:06', u'75*sqrt(1/12)')
	part4_correct_attempt
					['21:42:52', u'sqrt(75/12)']

64 Student ID:wmiao

	first_attempt
					2015-11-05 22:53:24
	part2_correct_attempt
					['0:05:26', u'(1/12*1^2)^0.5']
	part3_correct_attempt
					['0:03:37', u'0']
	part4_incorrect_attempt
					('0:06:18', u'(1/12*1^2)^0.5')
	part4_correct_attempt
					['18:18:04', u'(100/12)^0.5']

65 Student ID:k3tan

	first_attempt
					2015-11-04 21:45:25
	part2_correct_attempt
					['0:00:44', u'sqrt(1/12)']
	part3_correct_attempt
					['0:01:01', u'0']
	part4_incorrect_attempt
					('0:06:17', u'65*sqrt(1/12)')
					('2 days, 1:58:36', u'2.04124')
	part4_correct_attempt
					['2 days, 2:04:03', u'sqrt(65/12)']

66 Student ID:haw081

	first_attempt
					2015-11-03 02:22:53
	part2_correct_attempt
					['0:00:41', u'sqrt(1/12(0.5--0.5)^2)']
	part3_correct_attempt
					['0:01:58', u'0']
	part4_incorrect_attempt
					('0:02:09', u'sqrt(1/12(0.5--0.5)^2)')
					('0:02:31', u'0.5')
					('1 day, 20:44:10', u'sqrt(1/60(0.5--0.5)^2)')
	part4_correct_attempt
					['1 day, 23:02:41', u'sqrt(60/12(0.5--0.5)^2)']

67 Student ID:jix029

	first_attempt
					2015-11-01 20:42:55
	part2_correct_attempt
					['0:00:00', u'1/12^.5']
	part3_correct_attempt
					['0:00:00', u'0']
	part4_incorrect_attempt
					('0:00:00', u'70/12^.5')
					('0:01:36', u'1/12^.5')
					('0:01:44', u'70/12^.5')
	part4_correct_attempt
					['0:17:18', u'(70/12)^.5']

68 Student ID:hkhodada

	first_attempt
					2015-11-03 01:20:13
	part2_correct_attempt
					['1 day, 2:40:21', u'1/sqrt(12)']
	part3_correct_attempt
					['-3 days, 18:30:34', u'0']
	part4_incorrect_attempt
					('1 day, 4:01:47', u'1/sqrt(12)')
					('1 day, 20:25:10', u'50/sqrt(12)')
					('2 days, 1:55:08', u'1/sqrt(6)')
					('2 days, 1:56:07', u'1/sqrt(3)')
					('2 days, 1:56:39', u'1/3')
					('2 days, 2:03:52', u'50/12')
					('2 days, 2:04:31', u'100/12')
	part4_correct_attempt
					['2 days, 2:04:57', u'sqrt(50/12)']

69 Student ID:glcohen

	first_attempt
					2015-11-03 22:16:17
	part2_correct_attempt
					['9:30:54', u'sqrt((1/12)((-.5-.5)^2))']
	part3_correct_attempt
					['9:02:25', u'0']
	part4_incorrect_attempt
					('9:31:18', u'sqrt((1/12)((-.5-.5)^2))')
					('9:32:34', u'0.5')
					('9:37:48', u'sqrt((1/12)((-.5-.5)^2))50')
					('9:38:58', u'(sqrt((1/12)((-.5-.5)^2)))25')
	part4_correct_attempt
					['9:41:13', u'sqrt(50/12)']

70 Student ID:acvuong

	first_attempt
					2015-11-05 01:09:21
	part2_correct_attempt
					['0:01:36', u'(1/12)^0.5']
	part3_correct_attempt
					['0:01:36', u'0']
	part4_incorrect_attempt
					('0:01:48', u'80*(1/12)^0.5')
					('0:03:04', u'(64/12)^0.5')
	part4_correct_attempt
					['0:06:28', u'(80/12)^0.5']

71 Student ID:sachadal

	first_attempt
					2015-11-05 20:29:44
	part2_correct_attempt
					['1 day, 1:50:53', u'1/sqrt(12)']
	part3_correct_attempt
					['1 day, 1:51:14', u'0']
	part4_incorrect_attempt
					('1 day, 1:51:28', u'75/sqrt(12)')
					('1 day, 1:56:45', u'1/sqrt(12)')
					('1 day, 1:59:03', u'1/sqrt(75*12)')
	part4_correct_attempt
					['1 day, 1:59:25', u'sqrt(75*(1/12))']

72 Student ID:awollner

	first_attempt
					2015-11-06 23:36:23
	part2_correct_attempt
					['0:04:05', u'sqrt(1/12)']
	part3_correct_attempt
					['0:04:49', u'0']
	part4_incorrect_attempt
					('0:04:49', u'2*sqrt(1/12)')
					('1:02:17', u'sqrt(100^2/12)')
	part4_correct_attempt
					['1:03:03', u'sqrt(100^2/1200)']

73 Student ID:pvl001

	first_attempt
					2015-11-03 21:01:59
	part2_correct_attempt
					['6:46:43', u'sqrt(1/12)']
	part3_correct_attempt
					['6:46:59', u'0']
	part4_incorrect_attempt
					('6:48:22', u'46*sqrt(1/12)')
					('6:50:56', u'45*sqrt(1/12)')
	part4_correct_attempt
					['6:51:08', u'sqrt(45/12)']

74 Student ID:mbl003

	first_attempt
					2015-11-06 20:33:10
	part2_correct_attempt
					['0:01:05', u'sqrt((1/12)*(1)^2)']
	part3_correct_attempt
					['0:05:01', u'0']
	part4_incorrect_attempt
					('0:05:11', u'sqrt((1/12)*(1)^2)')
	part4_correct_attempt
					['0:05:23', u'sqrt(80*(1/12)*(1)^2)']

75 Student ID:n2patil

	first_attempt
					2015-11-05 02:49:23
	part2_correct_attempt
					['0:21:12', u'(1/12)^(1/2)']
	part3_correct_attempt
					['0:23:57', u'0']
	part4_incorrect_attempt
					('0:34:40', u'100(1/12)')
	part4_correct_attempt
					['0:36:00', u'(100(1/12))^(1/2)']

76 Student ID:ttimmons

	first_attempt
					2015-11-03 18:57:52
	part2_correct_attempt
					['0:00:27', u'sqrt((1/12)(0.5-(-0.5))^2)']
	part3_correct_attempt
					['0:01:05', u'0']
	part4_incorrect_attempt
					('0:01:05', u'sqrt((1/12)(0.5-(-0.5))^2)')
	part4_correct_attempt
					['0:02:40', u'sqrt((80/12)(0.5-(-0.5))^2)']

77 Student ID:jblynch

	first_attempt
					2015-11-04 21:10:13
	part2_correct_attempt
					['0:00:29', u'sqrt(1/12)']
	part3_correct_attempt
					['6:03:59', u'0']
	part4_incorrect_attempt
					('6:11:05', u'(1/12)')
					('6:11:56', u'1/3')
					('6:12:03', u'1/6')
					('6:13:34', u'100(1/12)')
					('6:14:40', u'75(1/12)')
	part4_correct_attempt
					['6:14:59', u'sqrt(75(1/12))']

78 Student ID:ganajera

	first_attempt
					2015-11-06 03:30:10
	part2_correct_attempt
					['0:00:00', u'sqrt(1/12)']
	part3_correct_attempt
					['0:03:49', u'0']
	part4_incorrect_attempt
					('0:04:13', u'sqrt(4225/12)')
	part4_correct_attempt
					['0:09:48', u'sqrt(65/12)']

79 Student ID:nnh002

	first_attempt
					2015-11-06 20:58:40
	part2_correct_attempt
					['0:22:18', u'sqrt(1/12(1))']
	part3_correct_attempt
					['0:23:17', u'0']
	part4_incorrect_attempt
					('0:23:17', u'sqrt(100(sqrt(1/12)))')
	part4_correct_attempt
					['0:23:51', u'sqrt(100/12)']

80 Student ID:agian

	first_attempt
					2015-11-07 00:34:24
	part2_correct_attempt
					['0:00:16', u'sqrt(1/12)']
	part3_correct_attempt
					['0:01:05', u'0']
	part4_incorrect_attempt
					('0:01:05', u'sqrt(100)/sqrt(12)')
	part4_correct_attempt
					['0:01:27', u'sqrt(65)/sqrt(12)']

81 Student ID:skodigal

	first_attempt
					2015-11-06 04:44:04
	part2_correct_attempt
					['0:00:47', u'sqrt(1/12 *(.5+.5)^2)']
	part3_correct_attempt
					['0:03:43', u'75 * (-.5+.5)/2']
	part4_incorrect_attempt
					('0:03:43', u'75 * sqrt(1/12 *(.5+.5)^2)')
	part4_correct_attempt
					['0:04:35', u'sqrt(75 * (1/12 *(.5+.5)^2))']

82 Student ID:hachrist

	first_attempt
					2015-11-05 08:54:30
	part2_correct_attempt
					['0:00:27', u'sqrt(1/12)']
	part3_correct_attempt
					['0:00:42', u'0']
	part4_incorrect_attempt
					('0:01:11', u'40*sqrt(1/12)')
	part4_correct_attempt
					['0:02:08', u'sqrt(40/12)']

83 Student ID:kew017

	first_attempt
					2015-11-06 01:26:23
	part2_correct_attempt
					['0:03:33', u'sqrt(1/12)']
	part3_correct_attempt
					['0:12:04', u'0']
	part4_incorrect_attempt
					('0:12:04', u'80sqrt(1/12)')
	part4_correct_attempt
					['0:15:31', u'sqrt(1/12 * 80)']

84 Student ID:haliew

	first_attempt
					2015-11-06 23:36:10
	part2_correct_attempt
					['0:00:00', u'sqrt((1/12)(.5+.5)^2)']
	part3_correct_attempt
					['0:00:28', u'0']
	part4_incorrect_attempt
					('0:00:28', u'sqrt((1/12)(.5+.5)^2)')
					('0:06:27', u'65(sqrt((1/12)(.5+.5)^2))')
					('0:07:12', u'sqrt((1/12)(.5+.5)^2)')
	part4_correct_attempt
					['0:07:40', u'sqrt(65(1/12)(.5+.5)^2)']

85 Student ID:arvenega

	first_attempt
					2015-11-06 23:51:33
	part2_correct_attempt
					['0:00:00', u'sqrt(1/12)']
	part3_correct_attempt
					['0:00:00', u'0']
	part4_incorrect_attempt
					('0:00:00', u'sqrt((1/12)*40)')
	part4_correct_attempt
					['0:00:20', u'sqrt((1/12)*100)']

86 Student ID:tdurrer

	first_attempt
					2015-11-06 06:18:50
	part2_correct_attempt
					['0:00:00', u'sqrt(1/12)']
	part3_correct_attempt
					['0:00:00', u'0']
	part4_incorrect_attempt
					('0:08:29', u'sqrt((65^2)/12)')
	part4_correct_attempt
					['0:09:51', u'sqrt( 65/12 )']

87 Student ID:ksrijong

	first_attempt
					2015-11-06 20:48:49
	part2_correct_attempt
					['1:47:36', u'sqrt((0.5+0.5)^2/12)']
	part3_correct_attempt
					['0:01:58', u'0']
	part4_incorrect_attempt
					('1:56:03', u'sqrt((0.5^2+0.5^2)/2)')
					('1:57:37', u'80*sqrt((0.5+0.5)^2/12)')
	part4_correct_attempt
					['1:58:18', u'sqrt(((0.5+0.5)^2/12)*80)']

88 Student ID:volim

	first_attempt
					2015-11-04 23:32:33
	part2_correct_attempt
					['0:01:27', u'(1/12)^(1/2)']
	part3_correct_attempt
					['0:01:42', u'0']
	part4_incorrect_attempt
					('0:02:00', u'85*((1/12)^(1/2))')
	part4_correct_attempt
					['0:02:43', u'((1/12)*85)^(1/2)']

89 Student ID:qtluong

	first_attempt
					2015-11-04 06:40:26
	part2_correct_attempt
					['0:00:27', u'sqrt(1/12)']
	part3_correct_attempt
					['0:01:28', u'0']
	part4_incorrect_attempt
					('0:01:28', u'60*sqrt(1/12)')
	part4_correct_attempt
					['0:01:43', u'sqrt(60*1/12)']

90 Student ID:tjke

	first_attempt
					2015-11-06 17:29:09
	part2_correct_attempt
					['0:02:50', u'sqrt(1/12*(.5-(-.5))^2)']
	part3_correct_attempt
					['0:02:50', u'75*(-.5+.5)/2']
	part4_incorrect_attempt
					('0:02:50', u'sqrt(75^2*1/12*(.5-(-.5))^2)')
	part4_correct_attempt
					['0:03:02', u'sqrt(75*1/12*(.5-(-.5))^2)']

91 Student ID:klala

	first_attempt
					2015-11-05 06:49:03
	part2_correct_attempt
					['0:00:18', u'sqrt(1/12(1))']
	part3_correct_attempt
					['0:00:31', u'0']
	part4_incorrect_attempt
					('0:00:48', u'sqrt(1/12(1))')
	part4_correct_attempt
					['0:01:27', u'sqrt((1/12)(0.5 + 0.5)(75))']

92 Student ID:skarimik

	first_attempt
					2015-11-05 05:20:09
	part2_correct_attempt
					['0:00:00', u'1/(12)^(1/2)']
	part3_correct_attempt
					['0:06:55', u'0']
	part4_incorrect_attempt
					('0:06:55', u'1/(12)^(1/2)')
					('1:00:58', u'3/(12)^(1/2)')
					('1:01:22', u'95/(12)^(1/2)')
					('1:29:26', u'1/6')
					('1:29:52', u'2/(12)^(1/2)')
					('1:30:10', u'12/(12)^(1/2)')
	part4_correct_attempt
					['1:37:24', u'sqrt(95)/sqrt(12)']

93 Student ID:dmn009

	first_attempt
					2015-11-05 09:23:52
	part2_correct_attempt
					['0:33:01', u'.288675']
	part3_correct_attempt
					['0:20:33', u'0']
	part4_incorrect_attempt
					('0:33:01', u'.288675')
	part4_correct_attempt
					['0:35:43', u'2.32737']

94 Student ID:dlgoldbe

	first_attempt
					2015-11-05 06:43:06
	part2_correct_attempt
					['0:00:00', u'sqrt((1/12)*((0.5+0.5)^2))']
	part3_correct_attempt
					['0:01:13', u'0']
	part4_incorrect_attempt
					('0:04:10', u'sqrt(((65^2)/12)*((1)^2))')
	part4_correct_attempt
					['0:04:56', u'sqrt((1/12)*((0.5+0.5)^2)*65)']

95 Student ID:vsamant

	first_attempt
					2015-11-04 01:25:35
	part2_correct_attempt
					['0:01:33', u'(1/12(.5+.5)^2)^(1/2)']
	part3_correct_attempt
					['0:02:12', u'0']
	part4_incorrect_attempt
					('0:03:56', u'(1/12(.5+.5)^2)^(1/2)')
					('0:04:01', u'60(1/12(.5+.5)^2)^(1/2)')
	part4_correct_attempt
					['0:06:33', u'60^(1/2)(1/12(.5+.5)^2)^(1/2)']

96 Student ID:aportuga

	first_attempt
					2015-11-03 22:48:49
	part2_correct_attempt
					['0:01:25', u'0.288675134595']
	part3_correct_attempt
					['0:01:43', u'0']
	part4_incorrect_attempt
					('0:03:37', u'1/28.9827534924')
	part4_correct_attempt
					['0:04:43', u'2.4152294577']

97 Student ID:rohan

	first_attempt
					2015-11-07 00:16:39
	part2_correct_attempt
					['0:02:16', u'sqrt(1/12)']
	part3_correct_attempt
					['0:02:34', u'0']
	part4_incorrect_attempt
					('0:04:12', u'sqrt(1/12)+sqrt(1/12)')
					('0:04:27', u'sqrt(2/12)')
					('0:05:39', u'sqrt(1035/12)')
	part4_correct_attempt
					['0:06:20', u'sqrt(45/12)']

98 Student ID:spw006

	first_attempt
					2015-11-04 03:42:09
	part2_correct_attempt
					['-1 day, 23:59:26', u'sqrt(1/12)']
	part3_correct_attempt
					['-1 day, 23:59:26', u'0']
	part4_incorrect_attempt
					('-1 day, 23:59:26', u'80*(1/sqrt(12) )')
	part4_correct_attempt
					['0:00:00', u'(1/sqrt(12)*sqrt(80) )']

99 Student ID:any027

	first_attempt
					2015-11-01 22:12:56
	part2_correct_attempt
					['0:01:57', u'sqrt(1/12 ( .5 - (-.5) )^2)']
	part3_correct_attempt
					['0:02:58', u'0']
	part4_incorrect_attempt
					('0:03:39', u'sqrt(1/12 ( .5 - (-.5) )^2)')
	part4_correct_attempt
					['0:05:48', u'sqrt(1/12 ( .5 - (-.5) )^2 * 40)']

100 Student ID:k5law

	first_attempt
					2015-11-04 08:28:10
	part2_correct_attempt
					['0:00:00', u'sqrt((1/12)(.5+.5)^2)']
	part3_correct_attempt
					['0:01:43', u'0']
	part4_incorrect_attempt
					('0:02:23', u'60*(1/12)')
					('0:02:51', u'.5*(1/12)')
					('0:02:57', u'30*(1/12)')
	part4_correct_attempt
					['0:05:50', u'sqrt(60*(1/12))']

101 Student ID:amquinte

	first_attempt
					2015-11-05 06:40:14
	part2_correct_attempt
					['0:01:23', u'.2887']
	part3_correct_attempt
					['0:03:05', u'0']
	part4_incorrect_attempt
					('0:03:05', u'27.424')
					('0:05:17', u'.00304')
					('0:05:36', u'.0296')
					('1 day, 16:44:55', u'.2887')
					('1 day, 17:20:15', u'27.424')
	part4_correct_attempt
					['1 day, 17:21:32', u'2.814']

102 Student ID:j6quach

	first_attempt
					2015-11-05 08:40:50
	part2_correct_attempt
					['0:00:00', u'1/sqrt(12)']
	part3_correct_attempt
					['0:00:00', u'0']
	part4_incorrect_attempt
					('0:00:00', u'1/sqrt(12)')
					('3:37:50', u'100*sqrt(1/12)')
					('3:44:07', u'(100*101/2)*(1/sqrt(12))')
	part4_correct_attempt
					['4:31:38', u'sqrt(100/12)']

103 Student ID:syc078

	first_attempt
					2015-11-05 03:11:54
	part2_correct_attempt
					['0:01:20', u'sqrt( (1/12)((0.5+0.5)^2) )']
	part3_correct_attempt
					['0:02:10', u'0']
	part4_incorrect_attempt
					('0:02:10', u'sqrt( (1/12)((0.5+0.5)^2) )')
					('0:02:19', u'95(sqrt( (1/12)((0.5+0.5)^2) ))')
					('0:11:53', u'95 (1/12)((0.5+0.5)^2)')
					('0:12:44', u'95 (1/12)')
					('0:13:11', u'95 sqrt(1/12)')
	part4_correct_attempt
					['0:13:55', u'sqrt(95/12)']

104 Student ID:bmilton

	first_attempt
					2015-11-06 22:46:04
	part2_correct_attempt
					['0:01:03', u'sqrt((1/12) * (1))']
	part3_correct_attempt
					['0:03:14', u'0']
	part4_incorrect_attempt
					('0:03:14', u'70^2 * (sqrt((1/12) * (1)))')
					('0:03:25', u'70 * (sqrt((1/12) * (1)))')
	part4_correct_attempt
					['0:03:43', u'sqrt(70 * (1/12))']

105 Student ID:yypan

	first_attempt
					2015-11-05 06:36:42
	part2_correct_attempt
					['0:00:35', u'sqrt(1/12*(.5+.5)^2)']
	part3_correct_attempt
					['0:01:11', u'(-.5+.5)/2']
	part4_incorrect_attempt
					('0:01:24', u'sqrt(1/12*(.5+.5)^2)')
	part4_correct_attempt
					['0:02:11', u'sqrt(1/12*(.5+.5)^2*45)']

106 Student ID:dcgriffi

	first_attempt
					2015-11-07 00:08:24
	part2_correct_attempt
					['0:00:00', u'sqrt(1/12)']
	part3_correct_attempt
					['0:00:00', u'0']
	part4_incorrect_attempt
					('0:00:16', u'70*sqrt(1/12)')
	part4_correct_attempt
					['0:00:54', u'sqrt(70/12)']

107 Student ID:rsmurlo

	first_attempt
					2015-11-05 20:29:46
	part2_correct_attempt
					['0:00:00', u'sqrt((1/12)(.5+.5)^2)']
	part3_correct_attempt
					['0:00:49', u'0']
	part4_incorrect_attempt
					('0:00:49', u'sqrt(75/12)')
	part4_correct_attempt
					['0:01:23', u'sqrt(50/12)']

108 Student ID:pnquach

	first_attempt
					2015-11-06 05:50:54
	part2_correct_attempt
					['0:01:11', u'sqrt(1/12*(1)^2)']
	part3_correct_attempt
					['0:00:00', u'0']
	part4_incorrect_attempt
					('0:01:11', u'sqrt(1/12*(1)^2)')
	part4_correct_attempt
					['0:05:13', u'sqrt(1/12*(1)^2*65)']

109 Student ID:s6deng

	first_attempt
					2015-11-05 07:44:22
	part2_correct_attempt
					['0:01:22', u'sqrt(1/12)']
	part3_correct_attempt
					['0:02:13', u'0']
	part4_incorrect_attempt
					('0:02:13', u'80*sqrt(1/12)')

110 Student ID:achinn

	first_attempt
					2015-11-03 21:36:45
	part2_correct_attempt
					['0:00:41', u'sqrt(1/12)']
	part3_correct_attempt
					['0:00:00', u'0']
	part4_incorrect_attempt
					('0:00:41', u'40*sqrt(1/12)')
	part4_correct_attempt
					['0:01:02', u'sqrt(40*1/12)']

111 Student ID:jdeon

	first_attempt
					2015-11-04 05:41:59
	part2_correct_attempt
					['0:00:31', u'(1/12)^(.5)']
	part3_correct_attempt
					['0:12:57', u'0']
	part4_incorrect_attempt
					('17:48:12', u'90*(1/12)^(.5)')
	part4_correct_attempt
					['17:48:58', u'(90*(1/12))^(.5)']

112 Student ID:b1yao

	first_attempt
					2015-11-04 19:55:29
	part2_correct_attempt
					['0:01:17', u'1/12^0.5']
	part3_correct_attempt
					['0:00:18', u'0']
	part4_incorrect_attempt
					('0:01:29', u'1/12^0.5')
	part4_correct_attempt
					['22:33:45', u'(90/12)^0.5']

113 Student ID:ajabasa

	first_attempt
					2015-11-05 22:24:29
	part2_correct_attempt
					['0:02:24', u'((1/12)(-.5-.5)^2)^(1/2)']
	part3_correct_attempt
					['0:02:45', u'((-.5+.5)/2)*75']
	part4_incorrect_attempt
					('0:03:34', u'75*(((1/12)(-.5-.5)^2)^(1/2))')
					('0:04:00', u'75*((((1/12)(-.5-.5)^2)^(1/2)))')
					('0:04:55', u'((((1/12)(-.5-.5)^2)^(1/2)))*75')
	part4_correct_attempt
					['0:33:51', u'(((1/12)(-.5-.5)^2)*75)^(1/2)']

114 Student ID:mcatozzi

	first_attempt
					2015-11-03 20:47:04
	part2_correct_attempt
					['0:13:09', u'sqrt(1/12)']
	part3_correct_attempt
					['0:02:12', u'0']
	part4_incorrect_attempt
					('0:15:53', u'sqrt(55*.5*.5)')
					('0:16:18', u'sqrt(55)')
	part4_correct_attempt
					['0:17:37', u'sqrt(55*(1/12))']

115 Student ID:aadhakal

	first_attempt
					2015-11-05 22:45:06
	part2_correct_attempt
					['0:00:00', u'sqrt(1/12)']
	part3_correct_attempt
					['0:00:00', u'0']
	part4_incorrect_attempt
					('0:00:00', u'sqrt(40)/sqrt(12)')
	part4_correct_attempt
					['0:01:12', u'sqrt(100)/sqrt(12)']

116 Student ID:dtea

	first_attempt
					2015-11-07 00:51:11
	part3_correct_attempt
					['0:01:02', u'0']
	part4_incorrect_attempt
					('0:01:55', u'(1/12)(.5--.5)^2')

117 Student ID:lahawkin

	first_attempt
					2015-11-04 17:26:57
	part2_correct_attempt
					['0:00:00', u'(1/12)^(1/2)']
	part3_correct_attempt
					['0:00:00', u'0']
	part4_incorrect_attempt
					('10:26:31', u'(85/12)^1/2')
					('10:26:50', u'(1/2)^1/2')

118 Student ID:edcole

	first_attempt
					2015-11-06 23:53:13
	part2_correct_attempt
					['0:15:06', u'sqrt(1/12)']
	part3_correct_attempt
					['0:15:49', u'0']
	part4_incorrect_attempt
					('0:43:15', u'sqrt(1/12*2)')
					('0:43:25', u'sqrt(1/12*4)')
					('0:43:52', u'sqrt(1/12*.5)')
	part4_correct_attempt
					['0:47:00', u'sqrt(75*75/(75*12))']

119 Student ID:yig015

	first_attempt
					2015-11-05 10:57:48
	part2_correct_attempt
					['0:13:38', u'0.288675']
	part3_correct_attempt
					['0:14:41', u'0']
	part4_incorrect_attempt
					('0:14:41', u'65^2*217*0.87')
	part4_correct_attempt
					['0:15:35', u'8.0622578*0.288675']

120 Student ID:vasharma

	first_attempt
					2015-11-05 21:38:45
	part2_correct_attempt
					['0:00:34', u'sqrt((1/12))']
	part3_correct_attempt
					['0:06:45', u'0']
	part4_incorrect_attempt
					('0:07:21', u'95*sqrt((1/12))')
					('0:13:08', u'(95^2)*sqrt((1/12))')
	part4_correct_attempt
					['0:13:24', u'sqrt(95*(1/12))']

121 Student ID:kosung

	first_attempt
					2015-11-05 20:29:32
	part2_correct_attempt
					['0:01:21', u'1/3.464']
	part3_correct_attempt
					['0:04:26', u'0']
	part4_incorrect_attempt
					('0:04:44', u'1/3.464')
					('0:05:04', u'65/3.464')
					('0:11:03', u'65/3.464')
					('2:25:12', u'65^65/3.464')
					('2:25:18', u'65*65/3.464')
					('4:42:21', u'2.33')
	part4_correct_attempt
					['4:43:57', u'2.32735']

122 Student ID:c3chung

	first_attempt
					2015-11-06 22:30:22
	part2_correct_attempt
					['0:01:05', u'sqrt(1/12)']
	part3_correct_attempt
					['-1 day, 23:59:39', u'0']
	part4_incorrect_attempt
					('0:01:27', u'sqrt(0)')
	part4_correct_attempt
					['0:02:54', u'sqrt(95/12)']

123 Student ID:zig006

	first_attempt
					2015-11-04 21:45:16
	part2_correct_attempt
					['0:22:50', u'(1/12)^0.5']
	part3_correct_attempt
					['0:00:00', u'0']
	part4_incorrect_attempt
					('0:22:50', u'(40^2/12)^0.5')
					('0:28:59', u'40*((1/12)^0.5)')
	part4_correct_attempt
					['0:31:30', u'(40)^0.5*((1/12)^0.5)']

124 Student ID:jmiclat

	first_attempt
					2015-11-06 23:39:28
	part2_correct_attempt
					['0:00:30', u'sqrt(1/12)']
	part3_correct_attempt
					['0:03:09', u'0']
	part4_incorrect_attempt
					('0:03:19', u'95*sqrt(1/12)')
					('0:03:57', u'95^2/12')
					('0:04:17', u'sqrt(95^2/12)')
					('0:05:21', u'95*sqrt(95^2/12)')
	part4_correct_attempt
					['0:05:56', u'sqrt(95/12)']

125 Student ID:mjethani

	first_attempt
					2015-11-06 17:52:52
	part2_correct_attempt
					['0:21:19', u'sqrt((1/12)(1)^(2))']
	part3_correct_attempt
					['0:24:11', u'0']
	part4_incorrect_attempt
					('0:29:06', u'sqrt((1/12)((-0.5-0.5)^2))')
	part4_correct_attempt
					['0:29:36', u'sqrt((70)(1/12)((-0.5-0.5)^2))']

126 Student ID:gsrandha

	first_attempt
					2015-11-05 08:25:58
	part2_correct_attempt
					['0:40:10', u'sqrt(1/12(1))']
	part3_correct_attempt
					['0:00:00', u'0']
	part4_incorrect_attempt
					('0:40:10', u'sqrt(1/12(1))')
					('13:15:07', u'1/12(1)')
	part4_correct_attempt
					['13:51:31', u'sqrt(1/12 * 75)']












## Part 5

### (31) Mistake Group Digits of size 31




### (15) Mistake Group ['R.1'] of size 15
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(5-0)/2.23606797749979	|5-sqrt(60*(1/12))	|[('R.1', 2.23606797749979, u'2.2360679774', u'sqrt(60*(1/12))')]	|
|1	|(4-0)/2.04124145231932	|4*(1/sqrt(12)*sqrt(50))	|[('R.1', 2.04124145231932, u'2.04124145231', u'1/sqrt(12)*sqrt(50)')]	|
|2	|(5-0)/1.82574185835055	|2*5/sqrt(40*1/12(0.5+0.5)^2)	|[('R.1', 1.82574185835055, u'1.82574185835', u'sqrt(40*1/12(0.5+0.5)^2)')]	|
|3	|(2-0)/2.32737334062816	|.5/sqrt((1/12)*65)	|[('R.1', 2.32737334062816, u'2.32737334062', u'sqrt((1/12)*65)')]	|
|4	|(2-0)/2.32737334062816	|65/sqrt((1/12)*65)	|[('R.1', 2.32737334062816, u'2.32737334062', u'sqrt((1/12)*65)')]	|
|5	|(2-0)/2.32737334062816	|1/sqrt((1/12)*65)	|[('R.1', 2.32737334062816, u'2.32737334062', u'sqrt((1/12)*65)')]	|
|6	|(4-0)/2.81365716935569	|95/sqrt(1/12*95)	|[('R.1', 2.81365716935569, u'2.81365716935', u'sqrt(1/12*95)')]	|
|7	|(5-0)/1.82574185835055	|2/sqrt(40/12)	|[('R.1', 1.82574185835055, u'1.82574185835', u'sqrt(40/12)')]	|
|8	|(3-0)/2.04124145231932	|(50)/(sqrt(50(1/12)))	|[('R.1', 2.04124145231932, u'2.04124145231', u'sqrt(50(1/12))')]	|
|9	|(4-0)/2.14087209644419	|55/sqrt(55/12)	|[('R.1', 2.14087209644419, u'2.14087209644', u'sqrt(55/12)')]	|
|10	|(4-0)/2.04124145231932	|3/((sqrt((1/12)*50)))	|[('R.1', 2.04124145231932, u'2.04124145231', u'sqrt((1/12)*50)')]	|
|11	|(3-0)/2.66145323711189	|(85-3)/[85(.5+.5)^2/12]^(1/2)	|[('R.1', 2.66145323711189, u'2.66145323711', u'[85(.5+.5)^2/12]^(1/2)')]	|
|12	|(3-0)/2.66145323711189	|(85-0)/[85(.5+.5)^2/12]^(1/2)	|[('R.1', 2.66145323711189, u'2.66145323711', u'[85(.5+.5)^2/12]^(1/2)')]	|
|13	|(4-0)/2.32737334062816	|3/(sqrt(65)/sqrt(12))	|[('R.1', 2.32737334062816, u'2.32737334062', u'sqrt(65)/sqrt(12)')]	|
|14	|(2-0)/2.66145323711189	|85 / sqrt(85/12)	|[('R.1', 2.66145323711189, u'2.66145323711', u'sqrt(85/12)')]	|




### (14) Mistake Group ['R.0.0'] of size 14
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(4-0)/1.93649167310371	|4/1/sqrt(12)*sqrt(40)	|[('R.0.0', 4.0, u'4', u'4/1')]	|
|1	|(4-0)/2.23606797749979	|4/1/sqrt(12)*sqrt(60)	|[('R.0.0', 4.0, u'4', u'4/1')]	|
|2	|(3-0)/2.58198889747161	|Q(3/80)	|[('R.0.0', 3.0, u'3', u'3')]	|
|3	|(2-0)/2.04124145231932	|sqrt(2)/sqrt(5)	|[('R.0.0', 2.0, u'2', u'2')]	|
|4	|(4-0)/1.93649167310371	|4/sqrt(1/2)*sqrt(50)	|[('R.0.0', 4.0, u'4', u'4')]	|
|5	|(4-0)/1.93649167310371	|4/sqrt(12)*sqrt(50)	|[('R.0.0', 4.0, u'4', u'4')]	|
|6	|(4-0)/1.93649167310371	|4/sqrt(12)*sqrt(45)	|[('R.0.0', 4.0, u'4', u'4')]	|
|7	|(3-0)/2.5	|(3-2.5)/(sqrt(sqrt((1/12)(0.5 + 0.5)(75))))	|[('R.0.0', 3.0, u'3', u'3')]	|
|8	|(4-0)/2.66145323711189	|4/85*sqrt(1/12)	|[('R.0.0', 4.0, u'4', u'4')]	|
|9	|(4-0)/2.32737334062816	|(4-0)/1/sqrt(12)*sqrt(65)	|[('R.0.0', 4.0, u'4', u'(4-0)/1')]	|
|10	|(2-0)/2.88675134594813	|2/1/sqrt(12)*sqrt(100)	|[('R.0.0', 2.0, u'2', u'2/1')]	|
|11	|(3-0)/2.32737334062816	|3/8.0622578*0.288675	|[('R.0.0', 3.0, u'3', u'3')]	|
|12	|(3-0)/2.81365716935569	|sqrt(3/2.81366)	|[('R.0.0', 3.0, u'3', u'3')]	|
|13	|(5-0)/2.66145323711189	|sqrt(5/12)	|[('R.0.0', 5.0, u'5', u'5')]	|




### (5) Mistake Group Wrong_Sign of size 5




### (1) Mistake Group ['R.0.0', 'R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(3-0)/2.5	|(3-2.5)/(sqrt((1/12)(0.5 + 0.5)(75)))	|[('R.0.0', 3.0, u'3', u'3'), ('R.1', 2.5, u'2.5', u'sqrt((1/12)(0.5 + 0.5)(75))')]	|




### (67) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:druble

	first_attempt
					2015-11-05 00:26:41
	part5_incorrect_attempt
					('0:00:00', u'(2 - 0) / ((1/12)^(1/2) * (0.5 + 0.5) * 75)')
	part5_correct_attempt
					['0:03:13', u'(2 - 0) / (((1/12) * (0.5 + 0.5)^2 * 75)^(1/2))']

1 Student ID:jyc018

	first_attempt
					2015-11-05 00:14:14
	part5_incorrect_attempt
					('0:25:11', u'(3-0)/sqrt(1/12)')
					('23:11:56', u'sqrt(75/12)')
	part5_correct_attempt
					['1 day, 22:53:42', u'3/sqrt(75/12)']

2 Student ID:jfalcone

	first_attempt
					2015-11-05 05:43:34
	part5_incorrect_attempt
					('0:11:18', u'4/(sqrt(1/12))')
	part5_correct_attempt
					['0:16:22', u'4/(sqrt(1/12) * sqrt(80))']

3 Student ID:ccn001

	first_attempt
					2015-11-05 16:26:42
	part5_incorrect_attempt
					('5:38:47', u'2-0/((1/45)^(0.5))')
					('5:57:13', u'2/((1/12)(22.5+22.5)^(0.5))')
					('5:58:51', u'2/(((1/12)(22.5+22.5)^(2))^(0.5))')
					('6:02:41', u'2/((1/12)^(0.5)(45))')
					('6:11:04', u'2/((1/12)^(0.5)(22.5))')
	part5_correct_attempt
					['14:55:08', u'2/((45/12)^(0.5))']

4 Student ID:lywong

	first_attempt
					2015-11-04 07:33:22
	part5_incorrect_attempt
					('1 day, 15:46:08', u'Q(3)')
	part5_correct_attempt
					['1 day, 16:33:33', u'(3)/sqrt(50(1/12))']

5 Student ID:kew060

	first_attempt
					2015-11-03 02:12:39
	part5_incorrect_attempt
					('1 day, 23:30:00', u'6.5')
					('3 days, 20:42:57', u'3/(sqrt(5))')
					('3 days, 20:43:55', u'4/(sqrt(5))')
					('3 days, 20:47:54', u'4/(sqrt(65))')
					('3 days, 20:48:01', u'4/(sqrt(2))')
					('3 days, 20:48:06', u'4/(sqrt(3))')
					('3 days, 20:48:12', u'4/(sqrt(4))')
					('3 days, 20:48:18', u'4/(sqrt(6))')
					('3 days, 20:48:23', u'4/(sqrt(7))')
					('3 days, 20:48:29', u'4/(sqrt(8))')
					('3 days, 20:48:34', u'4/(sqrt(9))')
					('3 days, 20:48:41', u'4/(sqrt(10))')
	part5_correct_attempt
					['3 days, 20:52:44', u'4/(65/12)^(1/2)']

6 Student ID:hkhodada

	first_attempt
					2015-11-03 01:20:13
	part5_incorrect_attempt
					('1 day, 2:42:51', u'3*sqrt(12)')
	part5_correct_attempt
					['2 days, 2:07:51', u'3/sqrt(50/12)']

7 Student ID:abasu

	first_attempt
					2015-11-05 04:56:21
	part5_incorrect_attempt
					('0:09:10', u'5-0')
	part5_correct_attempt
					['0:58:16', u'1.9365']

8 Student ID:alakamsa

	first_attempt
					2015-11-02 19:37:10
	part5_incorrect_attempt
					('1 day, 23:04:53', u'.9987')
					('1 day, 23:05:12', u'0.00135')
	part5_correct_attempt
					['2 days, 0:48:38', u'1.4697']

9 Student ID:jcl084

	first_attempt
					2015-11-02 20:43:41
	part5_incorrect_attempt
					('0:00:00', u'(5-0)/(1/sqrt(12)*sqrt(50))')
	part5_correct_attempt
					['0:00:53', u'(5-0)/(1/sqrt(12)*sqrt(80))']

10 Student ID:masaro

	first_attempt
					2015-11-03 17:26:43
	part5_incorrect_attempt
					('0:02:28', u'0.9987')
					('0:02:35', u'1-0.9987')
					('0:02:56', u'1-0.00134989')
					('0:03:04', u'0.00134989')
	part5_correct_attempt
					['0:04:10', u'1.095']

11 Student ID:rwthomps

	first_attempt
					2015-11-06 21:51:27
	part5_incorrect_attempt
					('0:05:02', u'Q(3)')
	part5_correct_attempt
					['0:05:30', u'3/sqrt(65 * 1/12 * (.5 + .5))']

12 Student ID:sachadal

	first_attempt
					2015-11-05 20:29:44
	part5_incorrect_attempt
					('1 day, 1:57:11', u'Q(4)')
	part5_correct_attempt
					['1 day, 2:12:59', u'(4 - 0)/sqrt(75*(1/12))']

13 Student ID:krau

	first_attempt
					2015-11-04 20:35:20
	part5_incorrect_attempt
					('6:58:00', u'2/sqrt(2)')
					('6:58:10', u'sqrt(2)')
					('6:58:40', u'2/sqrt(5)')
	part5_correct_attempt
					['6:59:01', u'2/sqrt(50/12)']

14 Student ID:dcrume

	first_attempt
					2015-11-06 21:13:25
	part5_incorrect_attempt
					('0:05:39', u'3 - 0/2.88675')
	part5_correct_attempt
					['0:07:02', u'(3-0)/2.88675']

15 Student ID:mroknich

	first_attempt
					2015-11-01 20:00:23
	part5_incorrect_attempt
					('0:00:56', u'(5)/(sqrt(1/12))')
	part5_correct_attempt
					['0:02:06', u'(5)/(1/sqrt(12)*sqrt(55))']

16 Student ID:jcj006

	first_attempt
					2015-11-04 22:41:00
	part5_incorrect_attempt
					('0:00:00', u'24/50')
	part5_correct_attempt
					['0:00:33', u'2/sqrt(50/12)']

17 Student ID:skarimik

	first_attempt
					2015-11-05 05:20:09
	part5_incorrect_attempt
					('1:00:58', u'(3-0)')
	part5_correct_attempt
					['1:37:24', u'(3-0)/(sqrt(95)/sqrt(12))']

18 Student ID:mbl003

	first_attempt
					2015-11-06 20:33:10
	part5_incorrect_attempt
					('0:23:16', u'Phi(5)')
					('0:23:33', u'1-Phi(5)')
					('0:25:47', u'sqrt(80*(1/12)*(1)^2)/5')
	part5_correct_attempt
					['0:26:20', u'5/sqrt(80*(1/12)*(1)^2)']

19 Student ID:nhn018

	first_attempt
					2015-11-05 05:47:59
	part5_incorrect_attempt
					('0:14:22', u'4/(sqrt(12)*sqrt(50))')
					('0:15:06', u'4/(sqrt(12)*sqrt(45))')
					('14:26:45', u'4/(sqrt(12)*sqrt(45))')
	part5_correct_attempt
					['14:27:26', u'4/(sqrt(1/12)*sqrt(45))']

20 Student ID:j6quach

	first_attempt
					2015-11-05 08:40:50
	part5_incorrect_attempt
					('0:00:00', u'4*sqrt(12)')
	part5_correct_attempt
					['4:31:38', u'4/sqrt(100/12)']

21 Student ID:gsrandha

	first_attempt
					2015-11-05 08:25:58
	part5_incorrect_attempt
					('0:41:19', u'Q(3)')
					('13:14:20', u'1-Phi(3)')
					('13:17:14', u'Q(1-Phi(3))')
					('13:22:38', u'Q(3)')
					('13:50:12', u'(1-Phi(3)) * 2')
	part5_correct_attempt
					['13:52:39', u'3 / 2.5']

22 Student ID:haw081

	first_attempt
					2015-11-03 02:22:53
	part5_incorrect_attempt
					('1 day, 23:03:19', u'3/sqrt(1/12(0.5--0.5)^2)')
	part5_correct_attempt
					['1 day, 23:08:23', u'3/sqrt(5)']

23 Student ID:bmilton

	first_attempt
					2015-11-06 22:46:04
	part5_incorrect_attempt
					('0:04:06', u'4 - 0 / [sqrt(70 * (1/12))]')
	part5_correct_attempt
					['0:04:15', u'4/ [sqrt(70 * (1/12))]']

24 Student ID:jhc010

	first_attempt
					2015-11-06 11:00:36
	part5_incorrect_attempt
					('0:04:27', u'3-0/sqrt(55*(sqrt(1/12)^2))')
	part5_correct_attempt
					['0:04:35', u'(3-0)/sqrt(55*(sqrt(1/12)^2))']

25 Student ID:yil035

	first_attempt
					2015-11-05 21:14:50
	part5_incorrect_attempt
					('0:00:00', u'5*sqrt(6)')
	part5_correct_attempt
					['1:15:36', u'5/sqrt(100/12)']

26 Student ID:jeqin

	first_attempt
					2015-11-05 10:31:21
	part5_incorrect_attempt
					('0:01:54', u'(2 - 0)/sqrt(2/12)')
	part5_correct_attempt
					['0:02:33', u'(2 - 0)/sqrt(90/12)']

27 Student ID:mnrahman

	first_attempt
					2015-11-07 00:05:33
	part5_incorrect_attempt
					('0:01:20', u'3/(sqrt(100)/sqrt(12))')
	part5_correct_attempt
					['0:02:36', u'3/(sqrt(85)/sqrt(12))']

28 Student ID:r9jiang

	first_attempt
					2015-11-02 03:50:08
	part5_incorrect_attempt
					('0:00:00', u'27^(1/2)')
					('0:04:17', u'1.5*3^0.5')
	part5_correct_attempt
					['3 days, 1:46:43', u'3/2.32737']

29 Student ID:agarango

	first_attempt
					2015-11-05 03:19:35
	part5_incorrect_attempt
					('1 day, 20:54:08', u'2/sqrt(1/6)')
	part5_correct_attempt
					['1 day, 20:55:06', u'2/sqrt(55/12)']

30 Student ID:avasavad

	first_attempt
					2015-11-04 23:31:39
	part5_incorrect_attempt
					('0:00:00', u'Q(3)')

31 Student ID:s6deng

	first_attempt
					2015-11-05 07:44:22
	part5_incorrect_attempt
					('0:09:03', u'3/sqrt(1/12)')

32 Student ID:zhz159

	first_attempt
					2015-11-05 23:37:06
	part5_incorrect_attempt
					('0:00:00', u'0.21081851')
	part5_correct_attempt
					['0:12:38', u'1.0954451']

33 Student ID:agian

	first_attempt
					2015-11-07 00:34:24
	part5_incorrect_attempt
					('0:01:05', u'3/(sqrt(100)/sqrt(12))')
	part5_correct_attempt
					['0:01:47', u'4/(sqrt(65)/sqrt(12))']

34 Student ID:dgunawan

	first_attempt
					2015-11-05 08:57:44
	part5_incorrect_attempt
					('15:21:15', u'[5-((-.5+.5)/2)]/[(1/12)^(1/2)]')
	part5_correct_attempt
					['15:34:04', u'[5-((-.5+.5)/2 *85)]/[(85/12)^(1/2)]']

35 Student ID:rraiyyan

	first_attempt
					2015-11-07 00:00:13
	part5_incorrect_attempt
					('0:18:14', u'5/sqrt(85/4)')
	part5_correct_attempt
					['0:18:21', u'5/sqrt(85/12)']

36 Student ID:mpanelo

	first_attempt
					2015-11-05 23:02:59
	part5_incorrect_attempt
					('0:10:47', u'5/(20/3*sqrt(80))')
					('0:15:55', u'5/(2sqrt(400)/sqrt(3))')
	part5_correct_attempt
					['0:30:52', u'5/sqrt(20/3)']

37 Student ID:kbielawi

	first_attempt
					2015-11-05 21:37:38
	part5_incorrect_attempt
					('4:06:10', u'(sqrt(85/12))/sqrt(1/12)')
	part5_correct_attempt
					['4:07:31', u'3/sqrt(85/12)']

38 Student ID:thwan

	first_attempt
					2015-11-06 23:17:14
	part5_incorrect_attempt
					('0:02:33', u'5/(2/(12)^(1/2))')

39 Student ID:krkelkar

	first_attempt
					2015-10-31 21:49:34
	part5_incorrect_attempt
					('0:00:00', u'[ (2)-(0) ]/ ((1/12)( (85*0.5) - (85*-0.5) ) **2)')
					('2 days, 2:48:18', u'[ (2)-(0) ]/ ((sqrt(85*(1/12))) **2)')
	part5_correct_attempt
					['2 days, 2:48:39', u'[ (2)-(0) ]/ ((sqrt(85*(1/12))) )']

40 Student ID:vsamant

	first_attempt
					2015-11-04 01:25:35
	part5_incorrect_attempt
					('0:07:22', u'2/((1/12(.5+.5)^2)^(1/2))')
	part5_correct_attempt
					['0:07:41', u'2/(60^(1/2)(1/12(.5+.5)^2)^(1/2))']

41 Student ID:l8ngo

	first_attempt
					2015-11-05 23:17:21
	part5_incorrect_attempt
					('4:46:58', u'3/sqrt(1/12*[0.5+0.5]^2)')
					('4:48:23', u'40/sqrt(1/12*[0.5+0.5]^2)')
	part5_correct_attempt
					['5:07:49', u'3/sqrt(40*1/12*[0.5+0.5]^2)']

42 Student ID:ajabasa

	first_attempt
					2015-11-05 22:24:29
	part5_incorrect_attempt
					('0:36:00', u'(4-((-.5+.5)/(2)*75)/((1/12)(-.5-.5)^2)*75)^(1/2)')
					('0:36:55', u'4-((-.5+.5)/(2)*75)/((((1/12)(-.5-.5)^2)*75)^(1/2))')
	part5_correct_attempt
					['0:37:18', u'(4-((-.5+.5)/(2)*75))/((((1/12)(-.5-.5)^2)*75)^(1/2))']

43 Student ID:starinia

	first_attempt
					2015-11-05 03:37:59
	part5_incorrect_attempt
					('1:17:51', u'Q(4)')
	part5_correct_attempt
					['1:21:40', u'4/(1/sqrt(12)*sqrt(90))']

44 Student ID:aadhakal

	first_attempt
					2015-11-05 22:45:06
	part5_incorrect_attempt
					('0:00:00', u'3/(sqrt(40)/sqrt(12))')
	part5_correct_attempt
					['0:01:12', u'3/(sqrt(100)/sqrt(12))']

45 Student ID:edescobe

	first_attempt
					2015-11-04 12:13:40
	part5_incorrect_attempt
					('0:21:55', u'.77337')
	part5_correct_attempt
					['0:48:10', u'2/2.66145']

46 Student ID:asetters

	first_attempt
					2015-11-05 20:24:36
	part5_incorrect_attempt
					('0:02:08', u'4/(85*sqrt(1/12))')
					('0:02:22', u'4/(sqrt(1/12))')
					('0:03:55', u'4/(sqrt(1/12))')
	part5_correct_attempt
					['0:05:21', u'4/(sqrt(85/12))']

47 Student ID:etemlock

	first_attempt
					2015-11-06 00:46:10
	part5_incorrect_attempt
					('0:13:30', u'(3-0)/[((65/12)^.5)(65^.5)]')
	part5_correct_attempt
					['0:24:43', u'(3-0)/[((65/12)^.5)]']

48 Student ID:smohiman

	first_attempt
					2015-11-02 03:24:17
	part5_incorrect_attempt
					('0:08:30', u'(1/6)^(1/2)')
	part5_correct_attempt
					['0:10:20', u'1/(5*(1/12)^(1/2))']

49 Student ID:acs008

	first_attempt
					2015-11-05 21:49:23
	part5_incorrect_attempt
					('0:03:47', u'95/sqrt(1/12)')
					('0:04:11', u'4/sqrt(1/12)')
	part5_correct_attempt
					['0:04:22', u'4/sqrt(1/12*95)']

50 Student ID:arvenega

	first_attempt
					2015-11-06 23:51:33
	part5_incorrect_attempt
					('0:00:00', u'4/sqrt((1/12)*40)')
	part5_correct_attempt
					['0:00:20', u'4/sqrt((1/12)*100)']

51 Student ID:edcole

	first_attempt
					2015-11-06 23:53:13
	part5_incorrect_attempt
					('0:47:34', u'.9772')
	part5_correct_attempt
					['0:47:52', u'2/sqrt(75*75/(75*12))']

52 Student ID:ralhadda

	first_attempt
					2015-10-31 22:13:59
	part5_incorrect_attempt
					('3:33:00', u'65/12')

53 Student ID:yig015

	first_attempt
					2015-11-05 10:57:48
	part5_incorrect_attempt
					('1 day, 1:50:32', u'2/8.0622578*0.288675')
	part5_correct_attempt
					['1 day, 1:55:34', u'3/8.0622578/0.288675']

54 Student ID:dcastlem

	first_attempt
					2015-11-03 00:41:05
	part5_incorrect_attempt
					('3 days, 19:15:40', u'3/((sqrt(1/12)*50))')
	part5_correct_attempt
					['3 days, 19:16:21', u'4/((sqrt((1/12)*50)))']

55 Student ID:kosung

	first_attempt
					2015-11-05 20:29:32
	part5_incorrect_attempt
					('4:55:33', u'0.159883')
					('4:57:07', u'3/((8.062257)*2.32735)')
	part5_correct_attempt
					['5:36:29', u'3/2.32735']

56 Student ID:xweng

	first_attempt
					2015-11-06 01:03:22
	part5_incorrect_attempt
					('1:01:08', u'0.14164')
					('1:01:35', u'2.04124')
					('1:04:45', u'0.92918 ')
	part5_correct_attempt
					['1:29:18', u'3/2.04124']

57 Student ID:hsc052

	first_attempt
					2015-11-06 23:07:48
	part5_incorrect_attempt
					('0:03:21', u'4/[1/12]')
					('0:04:01', u'4/[sqrt(1/12)]')
	part5_correct_attempt
					['0:14:06', u'4/[sqrt(70)*sqrt(1/12)]']

58 Student ID:hmshah

	first_attempt
					2015-11-05 09:49:10
	part5_incorrect_attempt
					('0:32:39', u'1-Phi(4)')
					('0:32:48', u'1-Q(4)')
	part5_correct_attempt
					['11:36:26', u'(4-0)/ 2.04124']

59 Student ID:v3doan

	first_attempt
					2015-11-05 16:26:50
	part5_incorrect_attempt
					('1 day, 8:30:30', u'2 / sqrt(2/12)')
	part5_correct_attempt
					['1 day, 8:31:35', u'2 / sqrt(85/12)']

60 Student ID:aordookh

	first_attempt
					2015-11-06 06:07:32
	part5_incorrect_attempt
					('0:22:53', u'5-0/(1/12(70))^(1/2)')
	part5_correct_attempt
					['0:23:06', u'(5-0)/(1/12(70))^(1/2)']

61 Student ID:small

	first_attempt
					2015-11-06 03:13:39
	part5_incorrect_attempt
					('0:03:12', u'5/(sqrt(5*1/12))')
	part5_correct_attempt
					['0:04:19', u'5/(sqrt(50*1/12))']

62 Student ID:hmnaing

	first_attempt
					2015-11-06 18:17:24
	part5_incorrect_attempt
					('0:05:18', u'5* sqrt((0.5-(-0.5))^2 / 12)')
	part5_correct_attempt
					['0:30:08', u'(5-0)/sqrt(85/12)']

63 Student ID:wmiao

	first_attempt
					2015-11-05 22:53:24
	part5_incorrect_attempt
					('0:09:12', u'(5-0)/((1/12*1^2)^0.5)')
	part5_correct_attempt
					['18:18:04', u'(5-0)/((1/12*100)^0.5)']

64 Student ID:pnquach

	first_attempt
					2015-11-06 05:50:54
	part5_incorrect_attempt
					('0:03:57', u'(4)/(sqrt(1/12*(1)^2)*65)')
	part5_correct_attempt
					['0:05:13', u'(4)/(sqrt(1/12*(1)^2*65))']

65 Student ID:k3tan

	first_attempt
					2015-11-04 21:45:25
	part5_incorrect_attempt
					('2 days, 1:31:32', u'5/(65*sqrt(1/12))')
	part5_correct_attempt
					['2 days, 2:04:28', u'5/sqrt(65/12)']

66 Student ID:cprafull

	first_attempt
					2015-11-06 02:56:30
	part5_incorrect_attempt
					('0:04:40', u'(3-0)/sqrt(1/12)')
	part5_correct_attempt
					['0:04:52', u'(3-0)/sqrt(80/12)']












## Part 6

### (94) Mistake Group redirect of size 94




### (24) Mistake Group ['R.0.0'] of size 24
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|Q(2/2.66145)	|Q([ (2)-(0) ]/ ((1/12)( (85*0.5) - (85*-0.5) ) **2))	|[('R.0.0', 2.0, u'2', u'(2)-(0)')]	|
|1	|Q(2/2.04124)	|Q(2/(Q(2/1/sqrt(12)*sqrt(50))))	|[('R.0.0', 2.0, u'2', u'2')]	|
|2	|Q(5/2.58199)	|Q(5/(1/sqrt(12)*sqrt(50)))	|[('R.0.0', 5.0, u'5', u'5')]	|
|3	|Q(2/2.04124)	|(2+50)/(100)	|[('R.0.0', 2.0, u'2', u'2')]	|
|4	|Q(2/2.5)	|Q((2 - 0) / ((1/12)^(1/2) * (0.5 + 0.5) * 75))	|[('R.0.0', 2.0, u'2', u'2 - 0')]	|
|5	|Q(3/2.32737)	|Q(3)/((65/12)^(1/2))	|[('R.0.0', 3.0, u'3', u'3')]	|
|6	|Q(4/1.93649)	|Q(4/(sqrt(12)*sqrt(50)))	|[('R.0.0', 4.0, u'4', u'4')]	|
|7	|Q(4/1.93649)	|Q(4/(sqrt(12)*sqrt(45)))	|[('R.0.0', 4.0, u'4', u'4')]	|
|8	|Q(4/2.58199)	|Q(4-0)/(Q((13-5)/ ((15)^(1/2) / 2)))	|[('R.0.0', 4.0, u'4', u'4-0')]	|
|9	|Q(4/2.58199)	|Q(4)/((13-5)/ ((15)^(1/2) / 2))	|[('R.0.0', 4.0, u'4', u'4')]	|
|10	|Q(4/2.58199)	|Q(4)/((80/12)^(1/2))	|[('R.0.0', 4.0, u'4', u'4')]	|
|11	|Q(4/2.58199)	|Q(4) / (4/((80/12)^(1/2)))	|[('R.0.0', 4.0, u'4', u'4')]	|
|12	|Q(4/2.58199)	|Q(4) / (80/12)^(1/2)	|[('R.0.0', 4.0, u'4', u'4')]	|
|13	|Q(4/2.66145)	|(4+(85/2))/85	|[('R.0.0', 4.0, u'4', u'4')]	|
|14	|Q(5/2.88675)	|Q(5*sqrt(6))	|[('R.0.0', 5.0, u'5', u'5')]	|
|15	|Q(4/2.66145)	|(Phi(4))/2	|[('R.0.0', 4.0, u'4', u'4')]	|
|16	|Q(2/1.93649)	|Q(2/((1/12)(22.5+22.5)^(0.5)))	|[('R.0.0', 2.0, u'2', u'2')]	|
|17	|Q(2/1.93649)	|Q(2/(((1/12)(22.5+22.5)^(2))^(0.5)))	|[('R.0.0', 2.0, u'2', u'2')]	|
|18	|Q(2/1.93649)	|Q(2/((1/12)^(0.5)(45)))	|[('R.0.0', 2.0, u'2', u'2')]	|
|19	|Q(3/2.88675)	|Q(3/(sqrt(40)/sqrt(12)))	|[('R.0.0', 3.0, u'3', u'3')]	|
|20	|Q(4/2.32737)	|Q((4)/(sqrt(1/12*(1)^2)*65))	|[('R.0.0', 4.0, u'4', u'4')]	|
|21	|Q(4/2.41523)	|Q(4-0)/sqrt((70)(1/12)((-0.5-0.5)^2))	|[('R.0.0', 4.0, u'4', u'4-0')]	|
|22	|Q(5/2.66145)	|Phi(5/((85/12)^0.5))	|[('R.0.0', 5.0, u'5', u'5')]	|




### (16) Mistake Group Digits of size 16




### (5) Mistake Group ['R.0'] of size 5
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|Q(5/2.5)	|2(1-.9938)	|[('R.0', 2.0, u'5/2.5', u'2')]	|
|1	|Q(5/2.5)	|2(1-.9772)	|[('R.0', 2.0, u'5/2.5', u'2')]	|
|2	|Q(2/2.88675)	|(2/(1/sqrt(12)*sqrt(100)))/2	|[('R.0', 0.6928206460552524, u'2/2.88675', u'2/(1/sqrt(12)*sqrt(100))')]	|
|3	|Q(4/2.58199)	|Phi(4/sqrt(((0.5+0.5)^2/12)*80))	|[('R.0', 1.549192676966216, u'4/2.58199', u'4/sqrt(((0.5+0.5)^2/12)*80)')]	|
|4	|Q(3/2.58199)	|Phi(3/sqrt(80/12))	|[('R.0', 1.161894507724662, u'3/2.58199', u'3/sqrt(80/12)')]	|




### (2) Mistake Group Wrong_Sign of size 2




### (2) Mistake Group ['R.0.1'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|Q(4/1.93649)	|Q(4/4/sqrt(45/12))	|[('R.0.1', 1.93649, u'1.93649', u'sqrt(45/12)')]	|
|1	|Q(3/1.93649)	|Q((3-0.5*45)/[[(1/12)*45]^(1/2)])	|[('R.0.1', 1.93649, u'1.93649', u'[(1/12)*45]^(1/2)')]	|




### (1) Mistake Group ['R.0.0', 'R.0.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|Q(4/2.23607)	|Q(4(sqrt(1/12)sqrt(60)))	|[('R.0.0', 4.0, u'4', u'4'), ('R.0.1', 2.23607, u'2.23607', u'sqrt(1/12)sqrt(60)')]	|




### (64) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:gthorn

	first_attempt
					2015-11-05 07:13:41
	part5_correct_attempt
					['0:24:11', u'2/2.58199']
	part6_incorrect_attempt
					('0:25:15', u'(1-2/2.258199)/2')
	part6_correct_attempt
					['10:56:01', u'Q(2/2.58199)']

1 Student ID:h4tu

	first_attempt
					2015-11-06 23:48:34
	part5_correct_attempt
					['0:25:50', u'(2-0)/sqrt( 75/12)']
	part6_incorrect_attempt
					('0:26:44', u'1-Phi(sqrt( 75/12))')
	part6_correct_attempt
					['0:26:59', u'1-Phi((2-0)/sqrt( 75/12))']

2 Student ID:yig015

	first_attempt
					2015-11-05 10:57:48
	part5_correct_attempt
					['1 day, 1:55:34', u'3/8.0622578/0.288675']
	part6_incorrect_attempt
					('1 day, 1:57:32', u'Phi(1.28901)')
	part6_correct_attempt
					['1 day, 1:57:44', u'Q(1.28901)']

3 Student ID:vsamant

	first_attempt
					2015-11-04 01:25:35
	part5_correct_attempt
					['0:07:41', u'2/(60^(1/2)(1/12(.5+.5)^2)^(1/2))']
	part6_incorrect_attempt
					('0:23:37', u'.017218')
	part6_correct_attempt
					['5:02:18', u'1-Phi(2/(60^(1/2)(1/12(.5+.5)^2)^(1/2)))']

4 Student ID:kvass

	first_attempt
					2015-11-06 00:32:29
	part5_correct_attempt
					['0:11:55', u'5/sqrt(1/12 * 50)']
	part6_incorrect_attempt
					('0:12:40', u'Phi(sqrt(1/12 * 50))')
					('0:13:20', u'Q(sqrt(1/12 * 50))')
	part6_correct_attempt
					['0:14:35', u'Q(5/sqrt(1/12 * 50))']

5 Student ID:lguintu

	first_attempt
					2015-11-03 05:25:56
	part5_correct_attempt
					['0:05:45', u'4/((80/12)^(1/2))']
	part6_incorrect_attempt
					('0:10:02', u'1-0.72575')
					('0:10:23', u'0.72575')
					('0:13:44', u'Phi(5)')
	part6_correct_attempt
					['0:13:59', u'1-Phi(4/((80/12)^(1/2)))']

6 Student ID:ssamudra

	first_attempt
					2015-11-05 06:46:25
	part5_correct_attempt
					['0:03:18', u'0.8']
	part6_incorrect_attempt
					('0:03:18', u'0.211')
	part6_correct_attempt
					['0:03:26', u'0.212']

7 Student ID:masaro

	first_attempt
					2015-11-03 17:26:43
	part5_correct_attempt
					['0:04:10', u'1.095']
	part6_incorrect_attempt
					('0:05:30', u'0.135666')
					('0:05:48', u'1-0.135666')
					('0:06:51', u'1-0.8621')
					('0:06:59', u'0.8621')
					('0:07:28', u'0.8632')
					('0:07:34', u'1-0.8632')
					('0:08:25', u'0.863242')
	part6_correct_attempt
					['0:08:33', u'1-0.863242']

8 Student ID:sachadal

	first_attempt
					2015-11-05 20:29:44
	part5_correct_attempt
					['1 day, 2:12:59', u'(4 - 0)/sqrt(75*(1/12))']
	part6_incorrect_attempt
					('1 day, 2:24:20', u'4/1.6')
	part6_correct_attempt
					['1 day, 2:49:57', u'Q((4 - 0)/sqrt(75*(1/12)))']

9 Student ID:tjke

	first_attempt
					2015-11-06 17:29:09
	part5_correct_attempt
					['0:06:18', u'(4-0)/sqrt(75*1/12*(.5-(-.5))^2)']
	part6_incorrect_attempt
					('0:06:18', u'Q(sqrt(75*1/12*(.5-(-.5))^2))')
	part6_correct_attempt
					['0:06:41', u'Q((4-0)/sqrt(75*1/12*(.5-(-.5))^2))']

10 Student ID:j2phung

	first_attempt
					2015-11-05 11:00:11
	part5_correct_attempt
					['0:05:24', u'(3-0)/((80/12)^(1/2))']
	part6_incorrect_attempt
					('0:09:40', u'1-.8770')
					('0:13:03', u'(1-.8770)*2')
					('0:15:42', u'1 - Phi(.3770)')
	part6_correct_attempt
					['0:16:34', u'1 - Phi((3-0)/((80/12)^(1/2)))']

11 Student ID:jcj006

	first_attempt
					2015-11-04 22:41:00
	part5_correct_attempt
					['0:00:33', u'2/sqrt(50/12)']
	part6_incorrect_attempt
					('0:04:46', u'1-(2+50)/(100)')
					('0:05:17', u'1-(2+25)/(50)')
					('0:11:44', u'1-(2+5)/(sqrt(50))')
					('0:12:06', u'1-(sqrt(2)+5)/(sqrt(50))')
	part6_correct_attempt
					['0:13:08', u'Q(2/sqrt(50/12))']

12 Student ID:crmirand

	first_attempt
					2015-11-03 06:37:30
	part5_correct_attempt
					['0:03:30', u'3/(45/12)^.5']
	part6_incorrect_attempt
					('0:04:25', u'6.0667949')
					('0:04:38', u'2*6.0667949')
					('0:06:04', u'2*0.060668')
	part6_correct_attempt
					['0:06:11', u'0.060668']

13 Student ID:jdeon

	first_attempt
					2015-11-04 05:41:59
	part5_correct_attempt
					['17:52:23', u'(3)/(90*(1/12))^(.5)']
	part6_incorrect_attempt
					('17:52:39', u'Q(3)')
					('17:52:51', u'Phi(3)')
	part6_correct_attempt
					['17:53:16', u'Q((3)/(90*(1/12))^(.5))']

14 Student ID:dkurli

	first_attempt
					2015-11-05 03:29:36
	part5_correct_attempt
					['0:03:46', u'sqrt(5)']
	part6_incorrect_attempt
					('0:05:24', u'Phi(2.23607)')
	part6_correct_attempt
					['0:05:31', u'Q(2.23607)']

15 Student ID:j5phung

	first_attempt
					2015-11-04 21:17:03
	part5_correct_attempt
					['0:28:25', u'3/(sqrt(80/12))']
	part6_incorrect_attempt
					('0:31:04', u'1-[(1/2)+(1/2)*(3/(sqrt(80/12)))/sqrt(2)]')
	part6_correct_attempt
					['0:31:39', u'1-[(1/2)+(1/2)erf((3/(sqrt(80/12)))/sqrt(2))]']

16 Student ID:jic212

	first_attempt
					2015-11-05 03:25:43
	part5_correct_attempt
					['1 day, 19:51:00', u'5/(sqrt(50/12))']
	part6_incorrect_attempt
					('1 day, 19:51:32', u'1-Phi(sqrt(50/12))')
	part6_correct_attempt
					['1 day, 19:52:07', u'1-Phi(5/(sqrt(50/12)))']

17 Student ID:s2chaudh

	first_attempt
					2015-11-06 06:42:11
	part5_correct_attempt
					['0:03:01', u'3/(1/sqrt(12)*sqrt(80))']
	part6_incorrect_attempt
					('0:03:01', u'3/(1/sqrt(12)*sqrt(80))')
	part6_correct_attempt
					['16:48:06', u'1-(1/2+1/2erf(3/(1/sqrt(12)*sqrt(80))/sqrt(2)))']

18 Student ID:jmiclat

	first_attempt
					2015-11-06 23:39:28
	part5_correct_attempt
					['0:07:19', u'5/sqrt(95/12)']
	part6_incorrect_attempt
					('0:08:12', u'1-.9616')
					('0:08:49', u'1-.9625')
					('0:10:21', u'0.9625')
					('0:10:28', u'1-0.9625')
	part6_correct_attempt
					['0:14:48', u'1-Phi(1.77705)']

19 Student ID:gsrandha

	first_attempt
					2015-11-05 08:25:58
	part5_correct_attempt
					['13:52:39', u'3 / 2.5']
	part6_incorrect_attempt
					('13:52:39', u'3 / 2.5')
	part6_correct_attempt
					['13:54:22', u'1 - Phi(1.2)']

20 Student ID:jyc018

	first_attempt
					2015-11-05 00:14:14
	part5_correct_attempt
					['1 day, 22:53:42', u'3/sqrt(75/12)']
	part6_incorrect_attempt
					('1 day, 22:55:42', u'.885')
	part6_correct_attempt
					['1 day, 22:55:52', u'1-.885']

21 Student ID:jnatale

	first_attempt
					2015-11-05 01:30:25
	part5_correct_attempt
					['0:05:07', u'5/sqrt(95/12)']
	part6_incorrect_attempt
					('0:06:02', u'1-1/(5/sqrt(95/12))')
					('0:06:11', u'1/(5/sqrt(95/12))')
					('0:07:04', u'.04006')
					('0:07:35', u'.03216')
	part6_correct_attempt
					['1:11:56', u'Q(5/sqrt(95/12))']

22 Student ID:r9jiang

	first_attempt
					2015-11-02 03:50:08
	part5_correct_attempt
					['3 days, 1:46:43', u'3/2.32737']
	part6_incorrect_attempt
					('3 days, 1:48:31', u'Q(3)')
	part6_correct_attempt
					['3 days, 1:50:13', u'Q(3/2.32737)']

23 Student ID:avasavad

	first_attempt
					2015-11-04 23:32:19
	part6_incorrect_attempt
					('0:00:00', u'1-Phi(3)')

24 Student ID:btn023

	first_attempt
					2015-11-06 11:22:14
	part5_correct_attempt
					['7:05:38', u'(5-0)/sqrt(75*1/12(1)^2)']
	part6_incorrect_attempt
					('7:06:15', u'.97')
	part6_correct_attempt
					['7:06:47', u'0.02275']

25 Student ID:s6deng

	first_attempt
					2015-11-05 07:44:22
	part6_incorrect_attempt
					('0:04:02', u'1-Phi(3)')

26 Student ID:achinn

	first_attempt
					2015-11-03 21:36:45
	part5_correct_attempt
					['0:06:09', u'4/sqrt(40*1/12)']
	part6_incorrect_attempt
					('0:09:59', u'0.0125')
					('0:10:42', u'0.0139')
					('0:28:54', u'0.0143')
					('0:30:24', u'0.00715')
					('4:10:35', u'0.0143')
	part6_correct_attempt
					['10:23:53', u'Q(4/sqrt(40*1/12))']

27 Student ID:dwzhang

	first_attempt
					2015-11-06 21:39:06
	part5_correct_attempt
					['0:00:25', u'4/(1/sqrt(12)*sqrt(90))']
	part6_incorrect_attempt
					('0:00:47', u'Q(4/1/sqrt(12)*sqrt(90))')
	part6_correct_attempt
					['0:01:37', u'Q(4/(1/sqrt(12)*sqrt(90)))']

28 Student ID:dgunawan

	first_attempt
					2015-11-05 08:57:44
	part5_correct_attempt
					['15:34:04', u'[5-((-.5+.5)/2 *85)]/[(85/12)^(1/2)]']
	part6_incorrect_attempt
					('15:38:13', u'[5-((-.5+.5)/2 *85)]/[(85/12)^(1/2)]')
	part6_correct_attempt
					['15:56:48', u'1-Phi([5-((-.5+.5)/2 *85)]/[(85/12)^(1/2)])']

29 Student ID:aordookh

	first_attempt
					2015-11-06 06:07:32
	part5_correct_attempt
					['0:23:06', u'(5-0)/(1/12(70))^(1/2)']
	part6_incorrect_attempt
					('0:29:44', u'(5-0)/(1/12(70))^(1/2)')
	part6_correct_attempt
					['0:31:30', u'1-Phi((5-0)/(1/12(70))^(1/2))']

30 Student ID:mpanelo

	first_attempt
					2015-11-05 23:02:59
	part5_correct_attempt
					['0:30:52', u'5/sqrt(20/3)']
	part6_incorrect_attempt
					('0:33:58', u'Q(5)')
	part6_correct_attempt
					['0:34:19', u'Q(5/sqrt(20/3))']

31 Student ID:dsmonaha

	first_attempt
					2015-11-04 16:46:52
	part5_correct_attempt
					['0:25:30', u'5/2.5']
	part6_incorrect_attempt
					('0:46:53', u'0.9938')
					('0:47:32', u'1-0.9938')
					('0:56:11', u'(1-.9772)')
					('0:56:31', u'2.5')
					('0:56:44', u'.25')
					('0:56:55', u'.025')
					('1:07:56', u'1-.9772')
					('1:22:28', u'.0456')
	part6_correct_attempt
					['2 days, 2:56:18', u'(1-Phi(5/2.5))']

32 Student ID:jit002

	first_attempt
					2015-11-05 18:29:03
	part5_correct_attempt
					['0:24:41', u'2/((1/12)*60)^0.5']
	part6_incorrect_attempt
					('0:24:41', u'2*(1-Phi(2*5^0.5))')
	part6_correct_attempt
					['12:00:57', u'1-Phi(2/(((1/12)*60)^0.5))']

33 Student ID:pthsu

	first_attempt
					2015-10-31 04:00:32
	part5_correct_attempt
					['0:00:00', u'(3-0)/(1/sqrt(12)*sqrt(60))']
	part6_incorrect_attempt
					('0:00:37', u'Q(3/1/sqrt(12)*sqrt(60))')
					('0:00:58', u'Q(3/sqrt(12)*sqrt(60))')
	part6_correct_attempt
					['0:01:20', u'Q(3/(1/sqrt(12)*sqrt(60)))']

34 Student ID:hah008

	first_attempt
					2015-11-06 23:13:40
	part5_correct_attempt
					['0:01:50', u'2/(1/sqrt(12)*sqrt(70))']
	part6_incorrect_attempt
					('0:02:24', u'Q(2/1/sqrt(12)*sqrt(70))')
	part6_correct_attempt
					['0:03:00', u'Q(2/(1/sqrt(12)*sqrt(70)))']

35 Student ID:abasu

	first_attempt
					2015-11-05 04:56:21
	part5_correct_attempt
					['0:58:16', u'1.9365']
	part6_incorrect_attempt
					('0:59:46', u'0.4732')
					('1:00:18', u'0.4761')
					('1:02:01', u'1/38')
					('1:02:51', u'Q(5)')
	part6_correct_attempt
					['1:03:48', u'1-Phi(1.9365)']

36 Student ID:klala

	first_attempt
					2015-11-05 06:49:03
	part5_correct_attempt
					['0:02:51', u'(3-0)/2.5']
	part6_incorrect_attempt
					('0:03:49', u'0.00621')
					('0:07:36', u'0.006209')
	part6_correct_attempt
					['0:09:57', u'1-((1/2)+(1/2)*erf((((3-0)/2.5))/sqrt(2)))']

37 Student ID:edescobe

	first_attempt
					2015-11-04 12:13:40
	part5_correct_attempt
					['0:48:10', u'2/2.66145']
	part6_incorrect_attempt
					('8:47:31', u'1-.77337')
					('8:47:45', u'.77337')
	part6_correct_attempt
					['1 day, 21:09:00', u'Q(2/2.66145)']

38 Student ID:asetters

	first_attempt
					2015-11-05 20:24:36
	part5_correct_attempt
					['0:05:21', u'4/(sqrt(85/12))']
	part6_incorrect_attempt
					('0:09:09', u'(4+.5)')
					('0:11:45', u'.5(4/(sqrt(3)*sqrt(85/12))) + 1')
					('0:12:16', u'.5(4/(sqrt(3)*sqrt(85/12)) + 1)')
					('0:59:29', u'1-Phi(4)')
					('1:02:50', u'(1-Phi(4))/2')
					('1:03:06', u'(Phi(3))/2')
					('1:03:17', u'1- (Phi(3))/2')
	part6_correct_attempt
					['6:04:03', u'Q(4/(sqrt(85/12)))']

39 Student ID:etemlock

	first_attempt
					2015-11-06 00:46:10
	part5_correct_attempt
					['0:24:43', u'(3-0)/[((65/12)^.5)]']
	part6_incorrect_attempt
					('0:24:56', u'Q(0.0013499)')
					('0:26:07', u'2*Q(0.0013499)')
	part6_correct_attempt
					['0:27:15', u'Q(1.28901)']

40 Student ID:anvan

	first_attempt
					2015-11-05 17:19:44
	part5_correct_attempt
					['0:50:17', u'2/ sqrt(80/12)']
	part6_incorrect_attempt
					('0:52:00', u'0.7794')
					('0:52:08', u'1 - 0.7794')
					('0:53:06', u'1 - .774597')
	part6_correct_attempt
					['0:54:34', u'.438578 / 2']

41 Student ID:achava

	first_attempt
					2015-11-06 08:21:51
	part5_correct_attempt
					['0:10:49', u'4/sqrt(55/12)']
	part6_incorrect_attempt
					('0:11:11', u'2.871656*10^(-2)')
					('0:12:19', u'3.593032*10^(-2)')
	part6_correct_attempt
					['1:14:57', u'Q(4/(sqrt(55/12)))']

42 Student ID:m4bui

	first_attempt
					2015-11-06 04:28:16
	part5_correct_attempt
					['0:00:25', u'2/(1/sqrt(12)*sqrt(100))']
	part6_incorrect_attempt
					('0:01:03', u'2/(1/sqrt(12)*sqrt(100))')

43 Student ID:ppanourg

	first_attempt
					2015-11-06 21:10:40
	part5_correct_attempt
					['0:08:26', u'3/sqrt((1/12)*40)']
	part6_incorrect_attempt
					('0:09:29', u'.9495')
					('0:09:50', u'1-.9495')
					('0:11:53', u'.4495')
					('0:13:25', u'1-.4495')
					('0:14:52', u'.9495')
					('0:15:03', u'1-.9495')
					('0:17:10', u'1-Phi(3)')
	part6_correct_attempt
					['0:18:00', u'1-Phi(3/sqrt((1/12)*40))']

44 Student ID:tdurrer

	first_attempt
					2015-11-06 06:18:50
	part5_correct_attempt
					['0:13:25', u'(4-0)/(sqrt(65/12))']
	part6_incorrect_attempt
					('0:16:14', u'.0436')
	part6_correct_attempt
					['0:17:16', u'Q(1.71868)']

45 Student ID:bakang

	first_attempt
					2015-11-05 16:30:57
	part5_correct_attempt
					['0:07:22', u'(2)/(sqrt((1/12)*(1)^2*100))']
	part6_incorrect_attempt
					('0:07:52', u'1-(2)/(sqrt((1/12)*(1)^2*100))')
					('0:09:21', u'Q(2)')
	part6_correct_attempt
					['0:30:03', u'Q((2)/(sqrt((1/12)*(1)^2*100)))']

46 Student ID:edcole

	first_attempt
					2015-11-06 23:53:13
	part5_correct_attempt
					['0:47:52', u'2/sqrt(75*75/(75*12))']
	part6_incorrect_attempt
					('0:48:35', u'2/sqrt(75*75/(75*12))^3')
	part6_correct_attempt
					['0:49:34', u'Q(.8)']

47 Student ID:v4sharma

	first_attempt
					2015-11-05 23:23:24
	part5_correct_attempt
					['23:33:12', u'3/(sqrt(40 * (1/12 * (.5 + .5)^2)))']
	part6_incorrect_attempt
					('1 day, 0:42:38', u'Q(1.8)')
					('1 day, 0:42:58', u'Q(1.6)')
					('1 day, 0:43:06', u'Q(0.2)')
					('1 day, 0:43:13', u'Q(0.3)')
					('1 day, 0:49:36', u'Q(0.4)')
					('1 day, 0:50:00', u'Q(6.0)')
					('1 day, 0:50:07', u'Q(6.1)')
					('1 day, 0:50:14', u'Q(6.2)')
					('1 day, 0:52:59', u'Q(1)')
					('1 day, 0:53:16', u'Q(1.1)')
					('1 day, 0:53:30', u'Q(-0.1)')
					('1 day, 0:53:41', u'Q(-0.2)')
					('1 day, 0:53:47', u'Q(-0.3)')
					('1 day, 0:53:54', u'Q(-0.4)')
					('1 day, 0:54:02', u'Q(-0.5)')
					('1 day, 0:54:09', u'Q(-0.6)')
					('1 day, 0:54:17', u'Q(-0.7)')
					('1 day, 0:54:23', u'Q(-0.8)')
					('1 day, 0:54:31', u'Q(-0.9)')
					('1 day, 0:54:39', u'Q(-1.0)')
					('1 day, 0:54:44', u'Q(-1.1)')
					('1 day, 0:54:50', u'Q(-1.2)')
					('1 day, 0:54:55', u'Q(-1.3)')
					('1 day, 0:55:01', u'Q(-1.4)')
					('1 day, 0:55:06', u'Q(-1.5)')
					('1 day, 0:55:12', u'Q(-1.6)')
					('1 day, 0:55:19', u'Q(-1.8)')
					('1 day, 0:55:26', u'Q(-1.9)')
					('1 day, 1:08:24', u'Q(1.6)')
					('1 day, 1:08:47', u'0.05')
					('1 day, 1:08:55', u'0.01')
					('1 day, 1:09:00', u'0.02')
					('1 day, 1:09:05', u'0.03')
					('1 day, 1:09:09', u'0.04')
					('1 day, 1:09:17', u'0.06')
					('1 day, 1:09:22', u'0.07')
					('1 day, 1:09:28', u'0.08')
					('1 day, 1:09:36', u'0.09')
					('1 day, 1:13:23', u'Q(0.9)')
					('1 day, 1:24:22', u'0.949826')
	part6_correct_attempt
					['1 day, 1:24:40', u'0.0501740']

48 Student ID:mitopete

	first_attempt
					2015-11-04 05:20:00
	part5_correct_attempt
					['2 days, 18:19:44', u'3/((((1/12)*80)^(1/2)))']
	part6_incorrect_attempt
					('2 days, 18:23:34', u'0.877362')
					('2 days, 18:23:46', u'0.877362 * 2')
	part6_correct_attempt
					['2 days, 18:31:56', u'1-Phi(3/((((1/12)*80)^(1/2))))']

49 Student ID:n2patil

	first_attempt
					2015-11-05 02:49:23
	part5_correct_attempt
					['1:07:26', u'5/((100(1/12))^(1/2))']
	part6_incorrect_attempt
					('1:08:33', u'Q((100(1/12))^(1/2))')
					('1:09:16', u'1- Phi((100(1/12))^(1/2))')
					('1:09:31', u'1- Phi((5/100(1/12))^(1/2))')
	part6_correct_attempt
					['1:09:52', u'1- Phi(5/((100(1/12))^(1/2)))']

50 Student ID:aportuga

	first_attempt
					2015-11-03 22:48:49
	part5_correct_attempt
					['0:06:09', u'5/2.4152294577']
	part6_incorrect_attempt
					('0:07:25', u'5/2.4152294577')

51 Student ID:xweng

	first_attempt
					2015-11-06 01:03:22
	part5_correct_attempt
					['1:29:18', u'3/2.04124']
	part6_incorrect_attempt
					('22:52:29', u'0.5-0.4249')
	part6_correct_attempt
					['22:52:46', u'0.07082 ']

52 Student ID:amquinte

	first_attempt
					2015-11-05 06:40:14
	part5_correct_attempt
					['1 day, 17:22:55', u'1.066']
	part6_incorrect_attempt
					('1 day, 17:24:46', u'.143')
	part6_correct_attempt
					['1 day, 17:25:16', u'.14319']

53 Student ID:c3chung

	first_attempt
					2015-11-06 22:30:22
	part5_correct_attempt
					['0:03:33', u'3/2.81366']
	part6_incorrect_attempt
					('0:04:48', u'1-0.8577')
					('0:04:58', u'0.8577')
					('0:05:46', u'0.8554')
					('0:05:51', u'1-0.8554')
					('0:06:23', u'1-0.85769')
					('0:06:26', u'0.85769')
					('0:08:23', u'0.9222')
					('0:08:28', u'1-0.9222')
					('0:12:39', u'1-0.92220')
					('0:15:37', u'1-0.8554')
					('0:16:04', u'1-0.8577')
					('0:16:12', u'0.8577')

54 Student ID:yos017

	first_attempt
					2015-11-06 09:42:21
	part5_correct_attempt
					['0:15:12', u'[3 - 0]/ (45/12)^(1/2)']
	part6_incorrect_attempt
					('0:20:40', u'1 - Q([3 - 0]/ (45/12)^(1/2))')
	part6_correct_attempt
					['0:21:04', u'Q([3 - 0]/ (45/12)^(1/2))']

55 Student ID:jhp077

	first_attempt
					2015-11-05 13:54:00
	part5_correct_attempt
					['0:11:14', u'4/((80/12)^(1/2))']
	part6_incorrect_attempt
					('0:13:13', u'Q(4)/4/((80/12)^(1/2))')
	part6_correct_attempt
					['0:15:47', u'Q(4/(80/12)^(1/2))']

56 Student ID:ralhadda

	first_attempt
					2015-10-31 22:13:59
	part6_incorrect_attempt
					('3:29:16', u'1/12')
					('3:33:00', u'65/12')

57 Student ID:small

	first_attempt
					2015-11-06 03:13:39
	part5_correct_attempt
					['0:04:19', u'5/(sqrt(50*1/12))']
	part6_incorrect_attempt
					('0:05:27', u'5/(sqrt(50*1/12))')

58 Student ID:sghouse

	first_attempt
					2015-11-05 03:11:28
	part5_correct_attempt
					['21:43:40', u'2']
	part6_incorrect_attempt
					('21:43:40', u'Q(5)')
	part6_correct_attempt
					['21:43:52', u'Q(2)']

59 Student ID:akg009

	first_attempt
					2015-11-06 21:08:58
	part5_correct_attempt
					['0:12:27', u'4/sqrt(30)']
	part6_incorrect_attempt
					('0:16:19', u'Q(2)')
					('0:50:31', u'1-Q(2)')
					('0:50:50', u'1-Q(4/sqrt(30))')
	part6_correct_attempt
					['0:51:00', u'Q(4/sqrt(30))']

60 Student ID:muy002

	first_attempt
					2015-11-06 04:43:41
	part5_correct_attempt
					['0:18:42', u'2/sqrt(65/12)']
	part6_incorrect_attempt
					('0:19:00', u'2/sqrt(65/12)')
	part6_correct_attempt
					['0:19:28', u'Q(2/sqrt(65/12))']

61 Student ID:syc078

	first_attempt
					2015-11-05 03:11:54
	part5_correct_attempt
					['23:16:25', u'(5-0)/sqrt(95/12)']
	part6_incorrect_attempt
					('23:17:29', u'0.0375')
					('23:17:38', u'1-0.0375')
	part6_correct_attempt
					['1 day, 15:35:10', u'Q((5-0)/sqrt(95/12))']

62 Student ID:k3tan

	first_attempt
					2015-11-04 21:45:25
	part5_correct_attempt
					['2 days, 2:04:28', u'5/sqrt(65/12)']
	part6_incorrect_attempt
					('2 days, 2:09:56', u'0.5-0.4842')

63 Student ID:b1yao

	first_attempt
					2015-11-04 19:55:29
	part5_correct_attempt
					['22:35:17', u'5/((90/12)^0.5)']
	part6_incorrect_attempt
					('22:37:59', u'1-.9664')
					('22:42:24', u'.9664')
					('22:43:58', u'1-.9656')
					('22:44:41', u'2*(1-.9664)')
					('22:48:03', u'1-.9664')
					('22:49:42', u'(1-.9664)/2')
					('22:50:23', u'(1-.9664)*2')
					('22:52:21', u'0.1456')
					('22:56:49', u'.96638')
					('22:57:04', u'.96638/2')
	part6_correct_attempt
					['23:02:52', u'Q(5/((90/12)^0.5))']












## Part 7

### (89) Mistake Group redirect of size 89




### (27) Mistake Group Digits of size 27




### (25) Mistake Group ['R.1.0'] of size 25
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|2*Q(3/2.88675)	|Phi(6/2.88675)-Phi(3/2.88675)	|[('R.1.0', 1.0392309690828787, u'3/2.88675', u'3/2.88675')]	|
|1	|2*Q(4/1.93649)	|4*Q(4/sqrt(45/12))	|[('R.1.0', 2.0655929026227864, u'4/1.93649', u'4/sqrt(45/12)')]	|
|2	|2*Q(3/2.58199)	|1-Phi([3]/[sqrt((80/12)(0.5-(-0.5))^2)])	|[('R.1.0', 1.161894507724662, u'3/2.58199', u'[3]/[sqrt((80/12)(0.5-(-0.5))^2)]')]	|
|3	|2*Q(3/2.04124)	|1-Q(3/sqrt(50/12))	|[('R.1.0', 1.4696948913405576, u'3/2.04124', u'3/sqrt(50/12)')]	|
|4	|2*Q(3/2.04124)	|1-Phi(3/sqrt(50/12))	|[('R.1.0', 1.4696948913405576, u'3/2.04124', u'3/sqrt(50/12)')]	|
|5	|2*Q(4/2.04124)	|1-Q(4/(1/sqrt(12)*sqrt(50)))	|[('R.1.0', 1.9595931884540767, u'4/2.04124', u'4/(1/sqrt(12)*sqrt(50))')]	|
|6	|2*Q(2/1.93649)	|1-Phi((2-(-.5+.5)/2)/sqrt(1/12*(.5+.5)^2*45))	|[('R.1.0', 1.0327964513113932, u'2/1.93649', u'(2-(-.5+.5)/2)/sqrt(1/12*(.5+.5)^2*45)')]	|
|7	|2*Q(2/1.93649)	|1-Q((2-(-.5+.5)/2)/sqrt(1/12*(.5+.5)^2*45))	|[('R.1.0', 1.0327964513113932, u'2/1.93649', u'(2-(-.5+.5)/2)/sqrt(1/12*(.5+.5)^2*45)')]	|
|8	|2*Q(3/2.58199)	|1 - Phi((3-0)/((80/12)^(1/2)))	|[('R.1.0', 1.161894507724662, u'3/2.58199', u'(3-0)/((80/12)^(1/2))')]	|
|9	|2*Q(2/2.88675)	|Q((2)/(sqrt((1/12)*(1)^2*100)))+Phi((2)/(sqrt((1/12)*(1)^2*100)))	|[('R.1.0', 0.6928206460552524, u'2/2.88675', u'(2)/(sqrt((1/12)*(1)^2*100))')]	|
|10	|2*Q(2/1.93649)	|2Phi(2/((45(1/12))**.5))	|[('R.1.0', 1.0327964513113932, u'2/1.93649', u'2/((45(1/12))**.5)')]	|
|11	|2*Q(4/2.88675)	|1-Q(4/sqrt(100(1/12)(.5+.5)^2))	|[('R.1.0', 1.3856412921105048, u'4/2.88675', u'4/sqrt(100(1/12)(.5+.5)^2)')]	|
|12	|2*Q(4/2.88675)	|9*Q(4/sqrt(100(1/12)(.5+.5)^2))	|[('R.1.0', 1.3856412921105048, u'4/2.88675', u'4/sqrt(100(1/12)(.5+.5)^2)')]	|
|13	|2*Q(3/2.5)	|1 - Phi(1.2)	|[('R.1.0', 1.2, u'3/2.5', u'1.2')]	|
|14	|2*Q(5/2.88675)	|1-Q(5/sqrt(100/12))	|[('R.1.0', 1.732051615138131, u'5/2.88675', u'5/sqrt(100/12)')]	|
|15	|2*Q(3/2.04124)	|1-Q((3)/sqrt(50(1/12)))	|[('R.1.0', 1.4696948913405576, u'3/2.04124', u'(3)/sqrt(50(1/12))')]	|
|16	|2*Q(4/2.58199)	|1-Q((4-0)/sqrt(1/12 * 80))	|[('R.1.0', 1.549192676966216, u'4/2.58199', u'(4-0)/sqrt(1/12 * 80)')]	|
|17	|2*Q(3/2.14087)	|Q(3/(sqrt(55/12)))+Phi(3/(sqrt(55/12)))	|[('R.1.0', 1.401299471710099, u'3/2.14087', u'3/(sqrt(55/12))')]	|
|18	|2*Q(3/2.14087)	|Q((3-0)/sqrt(55*(sqrt(1/12)^2)))+Phi((3-0)/sqrt(55*(sqrt(1/12)^2)))	|[('R.1.0', 1.401299471710099, u'3/2.14087', u'(3-0)/sqrt(55*(sqrt(1/12)^2))')]	|
|19	|2*Q(3/2.14087)	|Phi((3-0)/sqrt(55*(sqrt(1/12)^2)))-Q((3-0)/sqrt(55*(sqrt(1/12)^2)))	|[('R.1.0', 1.401299471710099, u'3/2.14087', u'(3-0)/sqrt(55*(sqrt(1/12)^2))')]	|
|20	|2*Q(3/2.23607)	|3Q((3/sqrt(60/12)))	|[('R.1.0', 1.3416395730008455, u'3/2.23607', u'3/sqrt(60/12)')]	|
|21	|2*Q(3/2.23607)	|3Q(3/sqrt(60/12))	|[('R.1.0', 1.3416395730008455, u'3/2.23607', u'3/sqrt(60/12)')]	|
|22	|2*Q(5/2.58199)	|1-Q(5/sqrt(80*(1/12)*(1)^2))	|[('R.1.0', 1.9364908462077701, u'5/2.58199', u'5/sqrt(80*(1/12)*(1)^2)')]	|
|23	|2*Q(2/2.04124)	|2*1-Phi(2/sqrt(1/12*50))	|[('R.1.0', 0.9797965942270384, u'2/2.04124', u'2/sqrt(1/12*50)')]	|
|24	|2*Q(3/2.58199)	|1-Phi(3/sqrt(80/12))	|[('R.1.0', 1.161894507724662, u'3/2.58199', u'3/sqrt(80/12)')]	|




### (19) Mistake Group ['R.0'] of size 19
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|2*Q(3/2.23607)	|2*Q(3/1/sqrt(12)*sqrt(60))	|[('R.0', 2.0, u'2', u'2')]	|
|1	|2*Q(3/2.23607)	|2*Q(3/sqrt(12)*sqrt(60))	|[('R.0', 2.0, u'2', u'2')]	|
|2	|2*Q(3/2.5)	|(2)(3)/(1/sqrt(12)*sqrt(75))	|[('R.0', 2.0, u'2', u'2')]	|
|3	|2*Q(3/2.88675)	|2-[Phi(6/2.88675)-Phi(3/2.88675)]	|[('R.0', 2.0, u'2', u'2')]	|
|4	|2*Q(3/2.88675)	|2*(1-Phi(6/2.88675))	|[('R.0', 2.0, u'2', u'2')]	|
|5	|2*Q(3/2.32737)	|2*Q(3)	|[('R.0', 2.0, u'2', u'2')]	|
|6	|2*Q(4/1.93649)	|2*Q(4/sqrt(1/2)*sqrt(50))	|[('R.0', 2.0, u'2', u'2')]	|
|7	|2*Q(4/1.93649)	|2*Q(4/sqrt(12)*sqrt(50))	|[('R.0', 2.0, u'2', u'2')]	|
|8	|2*Q(4/1.93649)	|2*Q(4/sqrt(12)*sqrt(45))	|[('R.0', 2.0, u'2', u'2')]	|
|9	|2*Q(5/2.58199)	|2Q(5)	|[('R.0', 2.0, u'2', u'2')]	|
|10	|2*Q(5/2.04124)	|2*Q(sqrt(1/12 * 50))	|[('R.0', 2.0, u'2', u'2')]	|
|11	|2*Q(3/2.58199)	|2*(3/(1/sqrt(12)*sqrt(80)))	|[('R.0', 2.0, u'2', u'2')]	|
|12	|2*Q(4/2.73861)	|2 * Q(4/1/sqrt(12)*sqrt(90))	|[('R.0', 2.0, u'2', u'2')]	|
|13	|2*Q(3/2.81366)	|2(1-0.92220)	|[('R.0', 2.0, u'2', u'2')]	|
|14	|2*Q(3/2.81366)	|2(1-0.8554)	|[('R.0', 2.0, u'2', u'2')]	|
|15	|2*Q(3/2.81366)	|2(1-0.8577)	|[('R.0', 2.0, u'2', u'2')]	|
|16	|2*Q(4/2.58199)	|2*(sqrt(((0.5+0.5)^2/12)*80))	|[('R.0', 2.0, u'2', u'2')]	|
|17	|2*Q(5/2.04124)	|2*(1-Phi(sqrt(50/12)))	|[('R.0', 2.0, u'2', u'2')]	|
|18	|2*Q(5/2.81366)	|2*(1-0.9625)	|[('R.0', 2.0, u'2', u'2')]	|




### (17) Mistake Group ['R.1.0.0'] of size 17
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|2*Q(4/1.82574)	|1- Q(( 4)/ sqrt(1/12 ( .5 - (-.5) )^2 * 40) )	|[('R.1.0.0', 4.0, u'4', u'4')]	|
|1	|2*Q(2/1.82574)	|1- Q(2/sqrt(40/12))	|[('R.1.0.0', 2.0, u'2', u'2')]	|
|2	|2*Q(5/2.88675)	|1-Q(5*sqrt(6))	|[('R.1.0.0', 5.0, u'5', u'5')]	|
|3	|2*Q(5/2.66145)	|1-Phi([5-((-.5+.5)/2 *85)]/[(85/12)^(1/2)])	|[('R.1.0.0', 5.0, u'5', u'5-((-.5+.5)/2 *85)')]	|
|4	|2*Q(3/2.32737)	|1-Q(3/2.32735)	|[('R.1.0.0', 3.0, u'3', u'3')]	|
|5	|2*Q(3/2.32737)	|1-Phi(3/2.32735)	|[('R.1.0.0', 3.0, u'3', u'3')]	|
|6	|2*Q(2/2.32737)	|1-Q(2/sqrt(65/12))	|[('R.1.0.0', 2.0, u'2', u'2')]	|
|7	|2*Q(2/2.32737)	|1-Q((2/sqrt(65/12)))	|[('R.1.0.0', 2.0, u'2', u'2')]	|
|8	|2*Q(5/2.73861)	|1-Q(5/sqrt(90/12))	|[('R.1.0.0', 5.0, u'5', u'5')]	|
|9	|2*Q(3/2.66145)	|1-Q(3/sqrt(85/12))	|[('R.1.0.0', 3.0, u'3', u'3')]	|
|10	|2*Q(5/2.81366)	|1-Q((5-0)/sqrt(95/12))	|[('R.1.0.0', 5.0, u'5', u'5-0')]	|
|11	|2*Q(4/2.41523)	|1-(Q((4-0)/sqrt((70)(1/12)((-0.5-0.5)^2))))	|[('R.1.0.0', 4.0, u'4', u'4-0')]	|
|12	|2*Q(4/2.66145)	|1-Q(4/sqrt(85/12))	|[('R.1.0.0', 4.0, u'4', u'4')]	|
|13	|2*Q(3/1.82574)	|1-Phi(3/sqrt((1/12)*40))	|[('R.1.0.0', 3.0, u'3', u'3')]	|
|14	|2*Q(3/2.32737)	|1 - Q(3/sqrt(65 * 1/12 * (.5 + .5)))	|[('R.1.0.0', 3.0, u'3', u'3')]	|
|15	|2*Q(3/2.66145)	|1-Phi((3-0)/[85(.5+.5)^2/12]^(1/2))	|[('R.1.0.0', 3.0, u'3', u'3-0')]	|




### (16) Mistake Group Wrong_Sign of size 16




### (13) Mistake Group ['R.1.0.1'] of size 13
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|2*Q(3/2.88675)	|1+Phi(3/2.88675)-Phi(6/2.88675)	|[('R.1.0.1', 2.88675, u'2.88675', u'2.88675')]	|
|1	|2*Q(4/1.93649)	|1 - Phi((4 - 0) / sqrt(45/12)) + 1 - Phi((-4 - 0) / sqrt(45/12))	|[('R.1.0.1', 1.93649, u'1.93649', u'sqrt(45/12)')]	|
|2	|2*Q(3/2.58199)	|Q([3]/[sqrt((80/12)(0.5-(-0.5))^2)])*Phi([3]/[sqrt((80/12)(0.5-(-0.5))^2)])	|[('R.1.0.1', 2.58199, u'2.58199', u'sqrt((80/12)(0.5-(-0.5))^2)')]	|
|3	|2*Q(5/2.58199)	|1 - Phi((1)/sqrt(1/12 * 80))	|[('R.1.0.1', 2.58199, u'2.58199', u'sqrt(1/12 * 80)')]	|
|4	|2*Q(5/2.58199)	|1 - Phi((6)/sqrt(1/12 * 80))	|[('R.1.0.1', 2.58199, u'2.58199', u'sqrt(1/12 * 80)')]	|
|5	|2*Q(4/2.58199)	|Q(4/(80/12)^(1/2)) + Phi(4/(80/12)^(1/2))	|[('R.1.0.1', 2.58199, u'2.58199', u'(80/12)^(1/2)')]	|
|6	|2*Q(4/2.88675)	|1-Q(1/sqrt(100(1/12)(.5+.5)^2))	|[('R.1.0.1', 2.88675, u'2.88675', u'sqrt(100(1/12)(.5+.5)^2)')]	|
|7	|2*Q(4/2.58199)	|Phi(4 / ((80/12)**0.5)) + Q(4 / ((80/12)**0.5))	|[('R.1.0.1', 2.58199, u'2.58199', u'(80/12)**0.5')]	|
|8	|2*Q(3/1.93649)	|2*Q((3-0.5*45)/[[(1/12)*45]^(1/2)])	|[('R.1.0.1', 1.93649, u'1.93649', u'[(1/12)*45]^(1/2)')]	|
|9	|2*Q(5/2.58199)	|Phi(5/sqrt(80*(1/12)*(1)^2))+Q(5/sqrt(80*(1/12)*(1)^2))	|[('R.1.0.1', 2.58199, u'2.58199', u'sqrt(80*(1/12)*(1)^2)')]	|
|10	|2*Q(4/2.41523)	|Q(4/ [sqrt(70 * (1/12))]) + Phi(4/ [sqrt(70 * (1/12))])	|[('R.1.0.1', 2.41523, u'2.41523', u'sqrt(70 * (1/12))')]	|
|11	|2*Q(2/2.5)	|1-Phi((2-0)/sqrt( 75/12))+1-Phi((-2-0)/sqrt( 75/12))	|[('R.1.0.1', 2.5, u'2.5', u'sqrt( 75/12)')]	|




### (9) Mistake Group ['R.1'] of size 9
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|2*Q(3/2.58199)	|1-Q([3]/[sqrt((80/12)(0.5-(-0.5))^2)])	|[('R.1', 0.12263915918087342, u'Q(3/2.58199)', u'Q([3]/[sqrt((80/12)(0.5-(-0.5))^2)])')]	|
|1	|2*Q(3/2.58199)	|1 - Q((3-0)/((80/12)^(1/2)))	|[('R.1', 0.12263915918087342, u'Q(3/2.58199)', u'Q((3-0)/((80/12)^(1/2)))')]	|
|2	|2*Q(3/2.58199)	|Phi([3]/[sqrt((80/12)(0.5-(-0.5))^2)])-Q([3]/[sqrt((80/12)(0.5-(-0.5))^2)])	|[('R.1', 0.12263915918087342, u'Q(3/2.58199)', u'Q([3]/[sqrt((80/12)(0.5-(-0.5))^2)])')]	|
|3	|2*Q(3/2.5)	|1-Q(3/(sqrt(75/12)))	|[('R.1', 0.11506967022170822, u'Q(3/2.5)', u'Q(3/(sqrt(75/12)))')]	|
|4	|2*Q(4/2.04124)	|1-Q(4/2.04124)	|[('R.1', 0.025021679079280101, u'Q(4/2.04124)', u'Q(4/2.04124)')]	|
|5	|2*Q(3/2.58199)	|1-Q(3/sqrt(80/12))	|[('R.1', 0.12263915918087342, u'Q(3/2.58199)', u'Q(3/sqrt(80/12))')]	|
|6	|2*Q(2/2.73861)	|1-Q(4/sqrt(30))	|[('R.1', 0.2326041820899728, u'Q(2/2.73861)', u'Q(4/sqrt(30))')]	|
|7	|2*Q(3/2.41523)	|3*Q(3/(1/sqrt(12)*sqrt(70)))	|[('R.1', 0.10709656430280812, u'Q(3/2.41523)', u'Q(3/(1/sqrt(12)*sqrt(70)))')]	|




### (5) Mistake Group ['R.0', 'R.1.0.0'] of size 5
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|2*Q(5/2.58199)	|2(Q(5/(1/sqrt(12)*sqrt(50))))	|[('R.0', 2.0, u'2', u'2'), ('R.1.0.0', 5.0, u'5', u'5')]	|
|1	|2*Q(4/1.93649)	|2*Q(4/(sqrt(12)*sqrt(50)))	|[('R.0', 2.0, u'2', u'2'), ('R.1.0.0', 4.0, u'4', u'4')]	|
|2	|2*Q(4/1.93649)	|2*Q(4/(sqrt(12)*sqrt(45)))	|[('R.0', 2.0, u'2', u'2'), ('R.1.0.0', 4.0, u'4', u'4')]	|
|3	|2*Q(3/2.66145)	|2*1-Phi((3-0)/[85(.5+.5)^2/12]^(1/2))	|[('R.0', 2.0, u'2', u'2*1'), ('R.1.0.0', 3.0, u'3', u'3-0')]	|




### (2) Mistake Group ['R.0', 'R.1.0'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|2*Q(3/2.58199)	|2*Phi([3]/[sqrt((80/12)(0.5-(-0.5))^2)])	|[('R.0', 2.0, u'2', u'2'), ('R.1.0', 1.161894507724662, u'3/2.58199', u'[3]/[sqrt((80/12)(0.5-(-0.5))^2)]')]	|
|1	|2*Q(3/1.93649)	|2* Phi([3 - 0]/ (45/12)^(1/2))	|[('R.0', 2.0, u'2', u'2'), ('R.1.0', 1.54919467696709, u'3/1.93649', u'[3 - 0]/ (45/12)^(1/2)')]	|




### (77) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:druble

	first_attempt
					2015-11-05 00:26:41
	part5_correct_attempt
					['0:03:13', u'(2 - 0) / (((1/12) * (0.5 + 0.5)^2 * 75)^(1/2))']
	part6_correct_attempt
					['0:03:13', u'Q((2-0) / ((1/12) * (0.5 + 0.5)^2 * 75)^(1/2))']
	part7_incorrect_attempt
					('0:03:13', u'Phi((2 - 0) / (((1/12) * (0.5 + 0.5)^2 * 75)^(1/2)))')
	part7_correct_attempt
					['0:05:13', u'2 * Q((2-0) / ((1/12) * (0.5 + 0.5)^2 * 75)^(1/2))']

1 Student ID:dlgoldbe

	first_attempt
					2015-11-05 06:43:06
	part5_correct_attempt
					['0:05:27', u'2/(sqrt((1/12)*((0.5+0.5)^2)*65))']
	part6_correct_attempt
					['0:06:13', u'Q(2/(sqrt((1/12)*((0.5+0.5)^2)*65)))']
	part7_incorrect_attempt
					('0:06:13', u'Phi(2/(sqrt((1/12)*((0.5+0.5)^2)*65)))')
					('0:07:47', u'Q(2/(sqrt((1/12)*((0.5+0.5)^2)*65)))+Phi(2/(sqrt((1/12)*((0.5+0.5)^2)*65)))')
					('0:08:17', u'Q(2/(sqrt((1/12)*((0.5+0.5)^2)*65)))*Phi(2/(sqrt((1/12)*((0.5+0.5)^2)*65)))')
					('0:13:03', u'Q(2/(sqrt((1/12)*((0.5+0.5)^2)*65)))+Q(-(2/(sqrt((1/12)*((0.5+0.5)^2)*65))))')
					('0:13:27', u'Q(2/(sqrt((1/12)*((0.5+0.5)^2)*65)))-Q((2/(sqrt((1/12)*((0.5+0.5)^2)*65))))')
	part7_correct_attempt
					['0:13:41', u'Q(2/(sqrt((1/12)*((0.5+0.5)^2)*65)))+Q((2/(sqrt((1/12)*((0.5+0.5)^2)*65))))']

2 Student ID:jyc018

	first_attempt
					2015-11-05 00:14:14
	part5_correct_attempt
					['1 day, 22:53:42', u'3/sqrt(75/12)']
	part6_correct_attempt
					['1 day, 22:55:52', u'1-.885']
	part7_incorrect_attempt
					('1 day, 22:55:52', u'.885')
	part7_correct_attempt
					['1 day, 22:56:54', u'2*(1-.885)']

3 Student ID:b3hwang

	first_attempt
					2015-11-05 19:43:51
	part5_correct_attempt
					['0:11:26', u'(5-0)/2.41523']
	part6_correct_attempt
					['0:12:25', u'Q(2.0702)']
	part7_incorrect_attempt
					('0:12:25', u'Q(2.0702)')
					('0:12:38', u'Phi(2.0702)')
					('0:13:42', u'1-Q(2.0702)')
					('0:13:50', u'1-Phi(2.0702)')

4 Student ID:t2shin

	first_attempt
					2015-11-05 21:50:51
	part5_correct_attempt
					['0:02:35', u'4/sqrt(100(1/12)(.5+.5)^2)']
	part6_correct_attempt
					['0:03:13', u'Q(4/sqrt(100(1/12)(.5+.5)^2))']
	part7_incorrect_attempt
					('0:04:31', u'Q(9*4/sqrt(100(1/12)(.5+.5)^2))')
					('0:05:32', u'Q(1/sqrt(100(1/12)(.5+.5)^2))')
					('0:07:03', u'Q(Q(4/sqrt(100(1/12)(.5+.5)^2)))')
					('0:07:20', u'Q(4/sqrt(100(1/12)(.5+.5)^2))')
	part7_correct_attempt
					['0:08:03', u'2*Q(4/sqrt(100(1/12)(.5+.5)^2))']

5 Student ID:kebao

	first_attempt
					2015-11-05 22:10:58
	part5_correct_attempt
					['0:01:09', u'3/(1/sqrt(12)*sqrt(85))']
	part6_correct_attempt
					['0:04:21', u'Q(3/(1/sqrt(12)*sqrt(85)))']
	part7_incorrect_attempt
					('0:04:50', u'Q(3/(1/sqrt(12)*sqrt(85)))+2')
	part7_correct_attempt
					['0:05:08', u'Q(3/(1/sqrt(12)*sqrt(85)))*2']

6 Student ID:hkhodada

	first_attempt
					2015-11-03 01:20:13
	part5_correct_attempt
					['2 days, 2:07:51', u'3/sqrt(50/12)']
	part6_correct_attempt
					['2 days, 2:10:31', u'Q(3/sqrt(50/12))']
	part7_incorrect_attempt
					('2 days, 2:12:34', u'Phi(3/sqrt(50/12))')
	part7_correct_attempt
					['2 days, 2:34:25', u'2*Q(3/sqrt(50/12))']

7 Student ID:m4salaza

	first_attempt
					2015-11-05 05:39:08
	part5_correct_attempt
					['0:04:46', u'4/(1/sqrt(12)*sqrt(50))']
	part6_correct_attempt
					['0:06:35', u'Q(4/(1/sqrt(12)*sqrt(50)))']
	part7_incorrect_attempt
					('0:08:16', u'Phi(4/(1/sqrt(12)*sqrt(50)))')
	part7_correct_attempt
					['0:08:48', u'2*Q(4/(1/sqrt(12)*sqrt(50)))']

8 Student ID:fichoi

	first_attempt
					2015-11-04 20:06:44
	part5_correct_attempt
					['1:41:44', u'(5 - 0)/sqrt(1/12 * 80)']
	part6_correct_attempt
					['1:42:27', u'1 - Phi((5 - 0)/sqrt(1/12 * 80))']
	part7_incorrect_attempt
					('1:42:27', u'1 - (1 - Phi((5 - 0)/sqrt(1/12 * 80)))')
					('1:43:04', u'Phi((5 - 0)/sqrt(1/12 * 80))')
					('1:49:34', u'Phi((5 - 0)/sqrt(1/12 * 80))')

9 Student ID:masaro

	first_attempt
					2015-11-03 17:26:43
	part5_correct_attempt
					['0:04:10', u'1.095']
	part6_correct_attempt
					['0:08:33', u'1-0.863242']
	part7_incorrect_attempt
					('1 day, 3:29:31', u'1-Phi(1.095)')
					('1 day, 3:29:51', u'1-Q(1.095)')
					('1 day, 3:30:18', u'1-Phi(1.095)')
	part7_correct_attempt
					['1 day, 3:30:57', u'2*(1-Phi(1.095))']

10 Student ID:sachadal

	first_attempt
					2015-11-05 20:29:44
	part5_correct_attempt
					['1 day, 2:12:59', u'(4 - 0)/sqrt(75*(1/12))']
	part6_correct_attempt
					['1 day, 2:49:57', u'Q((4 - 0)/sqrt(75*(1/12)))']
	part7_incorrect_attempt
					('1 day, 2:50:32', u'Q((4 - 0)/sqrt(75*(1/12)))')
	part7_correct_attempt
					['1 day, 2:51:57', u'2*(Q((4 - 0)/sqrt(75*(1/12))))']

11 Student ID:j2phung

	first_attempt
					2015-11-05 11:00:11
	part5_correct_attempt
					['0:05:24', u'(3-0)/((80/12)^(1/2))']
	part6_correct_attempt
					['0:16:34', u'1 - Phi((3-0)/((80/12)^(1/2)))']
	part7_incorrect_attempt
					('0:21:08', u'Phi((3-0)/((80/12)^(1/2)))')
					('7:27:55', u'1 - .3770')
					('7:35:13', u'(1-.3770)*2')
	part7_correct_attempt
					['7:37:50', u'(1 - Phi(3/((80/12)^(1/2))))*2']

12 Student ID:pcdo

	first_attempt
					2015-11-02 19:01:21
	part5_correct_attempt
					['0:00:52', u'(2-0)/(1/sqrt(12)*sqrt(50))']
	part6_correct_attempt
					['0:01:43', u'Q(2/(1/sqrt(12)*sqrt(50)))']
	part7_incorrect_attempt
					('0:02:14', u'2*Q(2/1/sqrt(12)*sqrt(50))')
	part7_correct_attempt
					['0:02:27', u'2(Q(2/(1/sqrt(12)*sqrt(50))))']

13 Student ID:aakumar

	first_attempt
					2015-11-05 05:04:40
	part5_correct_attempt
					['0:52:27', u'1.5492']
	part6_correct_attempt
					['0:55:48', u'1-Phi(1.5492)']
	part7_incorrect_attempt
					('0:56:07', u'1-Q(1.5492)')
	part7_correct_attempt
					['0:56:23', u'0.0606668*2']

14 Student ID:crmirand

	first_attempt
					2015-11-03 06:37:30
	part5_correct_attempt
					['0:03:30', u'3/(45/12)^.5']
	part6_correct_attempt
					['0:06:11', u'0.060668']
	part7_incorrect_attempt
					('0:06:20', u'0.060668/2')
	part7_correct_attempt
					['0:06:29', u'0.060668*2']

15 Student ID:k5law

	first_attempt
					2015-11-04 08:28:10
	part5_correct_attempt
					['1:24:15', u'(5-0)/(1/sqrt(12)*sqrt(60))']
	part6_correct_attempt
					['1:25:24', u'Q((5-0)/(1/sqrt(12)*sqrt(60)))']
	part7_incorrect_attempt
					('1:27:09', u'Q((5-0)/(1/sqrt(12)*sqrt(60)))')
	part7_correct_attempt
					['1:27:32', u'2*Q((5-0)/(1/sqrt(12)*sqrt(60)))']

16 Student ID:mbl003

	first_attempt
					2015-11-06 20:33:10
	part5_correct_attempt
					['0:26:20', u'5/sqrt(80*(1/12)*(1)^2)']
	part6_correct_attempt
					['0:26:45', u'Q(5/sqrt(80*(1/12)*(1)^2))']
	part7_incorrect_attempt
					('0:28:21', u'Q(5/sqrt(80*(1/12)*(1)^2))')
	part7_correct_attempt
					['0:50:57', u'Phi(-5/sqrt(80*(1/12)*(1)^2))+Q(5/sqrt(80*(1/12)*(1)^2))']

17 Student ID:psable

	first_attempt
					2015-11-06 00:48:15
	part5_correct_attempt
					['0:09:49', u'1.46969']
	part6_correct_attempt
					['0:11:55', u'Q(1.46969)']
	part7_incorrect_attempt
					('0:11:55', u'Phi(1.46969)+Q(1.46969)')
					('0:12:12', u'Phi(1.46969)')
	part7_correct_attempt
					['0:12:51', u'2*Q(1.46969)']

18 Student ID:j5phung

	first_attempt
					2015-11-04 21:17:03
	part5_correct_attempt
					['0:28:25', u'3/(sqrt(80/12))']
	part6_correct_attempt
					['0:31:39', u'1-[(1/2)+(1/2)erf((3/(sqrt(80/12)))/sqrt(2))]']
	part7_incorrect_attempt
					('0:42:37', u'1-6/80')
	part7_correct_attempt
					['0:46:27', u'2*(1-[(1/2)+(1/2)erf((3/(sqrt(80/12)))/sqrt(2))])']

19 Student ID:h4tu

	first_attempt
					2015-11-06 23:48:34
	part5_correct_attempt
					['0:25:50', u'(2-0)/sqrt( 75/12)']
	part6_correct_attempt
					['0:26:59', u'1-Phi((2-0)/sqrt( 75/12))']
	part7_incorrect_attempt
					('0:27:27', u'(2-0)/sqrt( 75/12)')
					('0:27:40', u'Phi((2-0)/sqrt( 75/12))')
	part7_correct_attempt
					['0:32:18', u'(1-Phi((2-0)/sqrt( 75/12)))*2']

20 Student ID:j6quach

	first_attempt
					2015-11-05 08:40:50
	part5_correct_attempt
					['4:31:38', u'4/sqrt(100/12)']
	part6_correct_attempt
					['4:31:38', u'1 - Phi(4/sqrt(100/12))']
	part7_incorrect_attempt
					('4:37:18', u'Phi(4/sqrt(100/12))')
					('4:40:46', u'Phi(-4/sqrt(100/12))')
	part7_correct_attempt
					['4:40:56', u'2*Phi(-4/sqrt(100/12))']

21 Student ID:ttimmons

	first_attempt
					2015-11-03 18:57:52
	part5_correct_attempt
					['1 day, 0:53:53', u'[3]/[sqrt((80/12)(0.5-(-0.5))^2)]']
	part6_correct_attempt
					['1 day, 0:54:01', u'Q([3]/[sqrt((80/12)(0.5-(-0.5))^2)])']
	part7_incorrect_attempt
					('1 day, 0:54:30', u'Phi([3]/[sqrt((80/12)(0.5-(-0.5))^2)])')
					('1 day, 1:13:21', u'Phi([3]/[sqrt((80/12)(0.5-(-0.5))^2)])')
	part7_correct_attempt
					['1 day, 22:38:00', u'2*Q([3]/[sqrt((80/12)(0.5-(-0.5))^2)])']

22 Student ID:yypan

	first_attempt
					2015-11-05 06:36:42
	part5_correct_attempt
					['0:02:40', u'(2-(-.5+.5)/2)/sqrt(1/12*(.5+.5)^2*45)']
	part6_correct_attempt
					['0:03:25', u'1-(0.5+0.5*erf((2-(-.5+.5)/2)/sqrt(1/12*(.5+.5)^2*45)/sqrt(2)))']
	part7_incorrect_attempt
					('0:05:28', u'Phi(2)')
					('0:05:39', u'Q(2)')
					('0:05:53', u'1-Phi(2)')
					('0:09:35', u'Q((2-(-.5+.5)/2)/sqrt(1/12*(.5+.5)^2*45))')
					('0:09:55', u'Phi((2-(-.5+.5)/2)/sqrt(1/12*(.5+.5)^2*45))')
	part7_correct_attempt
					['0:13:20', u'2*Q((2-(-.5+.5)/2)/sqrt(1/12*(.5+.5)^2*45))']

23 Student ID:jhw015

	first_attempt
					2015-11-04 21:42:40
	part5_correct_attempt
					['1 day, 20:40:37', u'3/sqrt(60/12)']
	part6_correct_attempt
					['1 day, 21:04:49', u'Q(3/sqrt(60/12))']
	part7_incorrect_attempt
					('1 day, 21:06:26', u'3(3/sqrt(60/12))')
	part7_correct_attempt
					['1 day, 21:07:46', u'2Q(3/sqrt(60/12))']

24 Student ID:kosung

	first_attempt
					2015-11-05 20:29:32
	part5_correct_attempt
					['5:36:29', u'3/2.32735']
	part6_correct_attempt
					['5:36:46', u'Q(3/2.32735)']
	part7_incorrect_attempt
					('5:39:52', u'1-2Q(3/2.32735)')
					('5:40:39', u'1-2Q(3/2.32735)')
					('5:44:18', u'Q(3/2.32735)')
					('5:46:59', u'Phi(3/2.32735)')
					('5:48:13', u'Phi(3/2.32735) + Q(3/2.32735)')
	part7_correct_attempt
					['5:54:43', u'2Q(3/2.32735)']

25 Student ID:jblynch

	first_attempt
					2015-11-04 21:10:13
	part5_correct_attempt
					['8:35:43', u'(5 - 0)/sqrt(75(1/12))']
	part6_correct_attempt
					['9:04:03', u'0.02275']
	part7_incorrect_attempt
					('9:04:03', u'0.02275')
	part7_correct_attempt
					['9:04:14', u'2*0.02275']

26 Student ID:avasavad

	first_attempt
					2015-11-04 23:32:19
	part7_incorrect_attempt
					('0:00:00', u'Phi(3)')

27 Student ID:ralhadda

	first_attempt
					2015-10-31 22:13:59
	part7_incorrect_attempt
					('3:29:16', u'1/12')
					('3:33:00', u'65/12')

28 Student ID:acs008

	first_attempt
					2015-11-05 21:49:23
	part5_correct_attempt
					['0:04:22', u'4/sqrt(1/12*95)']
	part6_correct_attempt
					['0:05:07', u'Q(1.42164)']
	part7_incorrect_attempt
					('0:05:16', u'1-Q(1.42164)')
					('0:05:46', u'Q(1.42164)*sqrt(1/12*95)')
					('0:07:26', u'1-Q(1.42164)')
					('0:08:48', u'Q(4/sqrt(1/12*91))*Q(4/sqrt(1/12*99))')
	part7_correct_attempt
					['0:09:19', u'2*Q(1.42164)']

29 Student ID:achinn

	first_attempt
					2015-11-03 21:36:45
	part5_correct_attempt
					['0:06:09', u'4/sqrt(40*1/12)']
	part6_correct_attempt
					['10:23:53', u'Q(4/sqrt(40*1/12))']
	part7_incorrect_attempt
					('10:23:53', u'Q(0.0286)')
					('10:24:09', u'Q(4/sqrt(40*1/12)*2)')
					('10:24:25', u'Q(8/sqrt(40*1/12))')
	part7_correct_attempt
					['10:24:34', u'2*Q(4/sqrt(40*1/12))']

30 Student ID:jap009

	first_attempt
					2015-11-05 22:39:20
	part5_correct_attempt
					['0:06:49', u'4/((80/12)^(1/2))']
	part6_correct_attempt
					['0:06:49', u'Q((4/((80/12)^(1/2))))']
	part7_incorrect_attempt
					('0:07:18', u'Q(4/(4/((80/12)^(1/2))))')
					('0:07:41', u'Q(4/((80/12)^(1/2)))')
	part7_correct_attempt
					['0:08:19', u'2*Q(4/((80/12)^(1/2)))']

31 Student ID:haw081

	first_attempt
					2015-11-03 02:22:53
	part5_correct_attempt
					['1 day, 23:08:23', u'3/sqrt(5)']
	part6_correct_attempt
					['1 day, 23:11:29', u'1-Phi(3/sqrt(5))']
	part7_incorrect_attempt
					('1 day, 23:11:45', u'Phi(3/sqrt(5))')
					('1 day, 23:11:52', u'Q(3/sqrt(5))')
	part7_correct_attempt
					['1 day, 23:14:48', u'2*Q(3/sqrt(5))']

32 Student ID:tol003

	first_attempt
					2015-11-03 22:54:19
	part5_correct_attempt
					['0:08:46', u'3/2.88675']
	part6_correct_attempt
					['0:12:31', u'1-Phi(3/2.88675)']
	part7_incorrect_attempt
					('0:31:47', u'1-[Phi(6/2.88675)-Phi(3/2.88675)]')
					('0:34:55', u'1+Phi(3/2.88675)-(1-Phi(6/2.88675))')
	part7_correct_attempt
					['0:38:26', u'2*(1-Phi(3/2.88675))']

33 Student ID:dgunawan

	first_attempt
					2015-11-05 08:57:44
	part5_correct_attempt
					['15:34:04', u'[5-((-.5+.5)/2 *85)]/[(85/12)^(1/2)]']
	part6_correct_attempt
					['15:56:48', u'1-Phi([5-((-.5+.5)/2 *85)]/[(85/12)^(1/2)])']
	part7_incorrect_attempt
					('15:57:05', u'Phi([5-((-.5+.5)/2 *85)]/[(85/12)^(1/2)])')

34 Student ID:skodigal

	first_attempt
					2015-11-06 04:44:04
	part5_correct_attempt
					['1:01:54', u'(4- 75 * (-.5+.5)/2)/sqrt(75 * (1/12 *(.5+.5)^2))']
	part6_correct_attempt
					['1:02:49', u'Q(1.6)']
	part7_incorrect_attempt
					('1:04:37', u'Phi(1.6)')
	part7_correct_attempt
					['1:08:32', u'2*Q(1.6)']

35 Student ID:rraiyyan

	first_attempt
					2015-11-07 00:00:13
	part5_correct_attempt
					['0:18:21', u'5/sqrt(85/12)']
	part6_correct_attempt
					['0:18:39', u'Q(5/sqrt(85/12))']
	part7_incorrect_attempt
					('0:18:47', u'Phi(5/sqrt(85/12))')
	part7_correct_attempt
					['0:19:15', u'2*Q(5/sqrt(85/12))']

36 Student ID:hachrist

	first_attempt
					2015-11-05 08:54:30
	part5_correct_attempt
					['0:02:41', u'2/sqrt(40/12)']
	part6_correct_attempt
					['0:02:56', u'1- Phi(2/sqrt(40/12))']
	part7_incorrect_attempt
					('0:03:15', u'1-(1- Phi(2/sqrt(40/12)))')
	part7_correct_attempt
					['8:57:53', u'(1- Phi(2/sqrt(40/12)))*2']

37 Student ID:kew017

	first_attempt
					2015-11-06 01:26:23
	part5_correct_attempt
					['0:30:25', u'(4-0)/sqrt(1/12 * 80)']
	part6_correct_attempt
					['0:31:39', u'Q((4-0)/sqrt(1/12 * 80))']
	part7_incorrect_attempt
					('0:32:17', u'Q((4-0)/sqrt(1/12 * 80))+(1-Q((4-0)/sqrt(1/12 * 80)))')
	part7_correct_attempt
					['0:40:52', u'2*(Q((4-0)/sqrt(1/12 * 80)))']

38 Student ID:muy002

	first_attempt
					2015-11-06 04:43:41
	part5_correct_attempt
					['0:18:42', u'2/sqrt(65/12)']
	part6_correct_attempt
					['0:19:28', u'Q(2/sqrt(65/12))']
	part7_incorrect_attempt
					('0:19:41', u'Q(1-(2/sqrt(65/12)))')
					('1:32:27', u'Q((2/sqrt(65/12)))')
					('1:32:34', u'Q(1-(2/sqrt(65/12)))')
	part7_correct_attempt
					['1:34:49', u'2*Q(2/sqrt(65/12))']

39 Student ID:dsmonaha

	first_attempt
					2015-11-04 16:46:52
	part5_correct_attempt
					['0:25:30', u'5/2.5']
	part6_correct_attempt
					['2 days, 2:56:18', u'(1-Phi(5/2.5))']
	part7_incorrect_attempt
					('2 days, 2:56:32', u'Phi(5/2.5)')
	part7_correct_attempt
					['2 days, 2:58:36', u'2(1-Phi(5/2.5))']

40 Student ID:azkong

	first_attempt
					2015-11-06 20:13:02
	part5_correct_attempt
					['0:07:33', u'4/sqrt(85/12)']
	part6_correct_attempt
					['0:08:31', u'Q(4/sqrt(85/12))']
	part7_incorrect_attempt
					('0:08:58', u'Phi((4/sqrt(85/12)))')
	part7_correct_attempt
					['0:09:31', u'2*Q(4/sqrt(85/12))']

41 Student ID:tcn013

	first_attempt
					2015-11-05 20:57:24
	part5_correct_attempt
					['0:07:16', u'5/sqrt(45/12)']
	part6_correct_attempt
					['0:07:43', u'Q(2.58199)']
	part7_incorrect_attempt
					('0:07:43', u'Phi(2.58199)')
	part7_correct_attempt
					['0:09:07', u'2*Q(2.58199)']

42 Student ID:yeh013

	first_attempt
					2015-11-05 03:10:28
	part5_correct_attempt
					['4:02:42', u'4/(90/12)^(1/2)']
	part6_correct_attempt
					['4:03:04', u'1-Phi(4/(90/12)^(1/2))']
	part7_incorrect_attempt
					('4:03:14', u'Phi(4/(90/12)^(1/2))')
					('4:05:26', u'1-0.0720635')
	part7_correct_attempt
					['4:06:35', u'2*(1-Phi(4/(90/12)^(1/2)))']

43 Student ID:flhernan

	first_attempt
					2015-11-03 20:58:27
	part5_correct_attempt
					['0:08:10', u'5/sqrt((1/12)*80)']
	part6_correct_attempt
					['1 day, 22:08:03', u'1-0.97360']
	part7_incorrect_attempt
					('1 day, 22:21:03', u'(1-0.97360)*0.97360')
					('2 days, 16:32:10', u'(1-0.97360)*0.97360')
	part7_correct_attempt
					['2 days, 16:38:13', u'(1-0.97360)*2']

44 Student ID:tcuddy

	first_attempt
					2015-11-05 18:05:57
	part5_correct_attempt
					['0:27:58', u'2/((45(1/12))**.5)']
	part6_correct_attempt
					['0:29:43', u'Q(2/((45(1/12))**.5) )']
	part7_incorrect_attempt
					('0:29:52', u'Phi(2/((45(1/12))**.5))')
	part7_correct_attempt
					['0:51:36', u'2* Q(2/((45(1/12))**.5) )']

45 Student ID:small

	first_attempt
					2015-11-06 03:13:39
	part5_correct_attempt
					['0:04:19', u'5/(sqrt(50*1/12))']
	part7_incorrect_attempt
					('0:07:07', u'5/(sqrt(50*1/12))')

46 Student ID:mcatozzi

	first_attempt
					2015-11-03 20:47:04
	part5_correct_attempt
					['0:19:13', u'4/2.14087']
	part6_correct_attempt
					['2:22:32', u'1 - Phi(4/2.14087)']
	part7_incorrect_attempt
					('2:36:20', u'Phi(4/2.14087)')
	part7_correct_attempt
					['2:46:32', u'2*(1 - Phi(4/2.14087))']

47 Student ID:aadhakal

	first_attempt
					2015-11-05 22:45:06
	part5_correct_attempt
					['0:01:12', u'3/(sqrt(100)/sqrt(12))']
	part6_correct_attempt
					['0:01:12', u'Q(3/(sqrt(100)/sqrt(12)))']
	part7_incorrect_attempt
					('0:01:12', u'Q(3/(sqrt(100)/sqrt(12)))')
	part7_correct_attempt
					['0:01:29', u'Q(3/(sqrt(100)/sqrt(12)))*2']

48 Student ID:w4shin

	first_attempt
					2015-11-06 23:46:03
	part5_correct_attempt
					['0:03:46', u'3/sqrt(80/12)']
	part6_correct_attempt
					['0:04:20', u'1-Phi(3/sqrt(80/12))']
	part7_incorrect_attempt
					('0:04:20', u'Phi(3/sqrt(80/12))')
	part7_correct_attempt
					['0:04:33', u'2*(1-Phi(3/sqrt(80/12)))']

49 Student ID:sayao

	first_attempt
					2015-11-04 01:56:12
	part5_correct_attempt
					['1 day, 22:10:53', u'(4-0)/sqrt(70(1/12))']
	part6_correct_attempt
					['1 day, 22:11:14', u'Q((4-0)/sqrt(70(1/12)))']
	part7_incorrect_attempt
					('1 day, 22:11:22', u'Phi((4-0)/sqrt(70(1/12)))')
	part7_correct_attempt
					['1 day, 22:16:21', u'2*Q((4-0)/sqrt(70(1/12)))']

50 Student ID:ggaddi

	first_attempt
					2015-11-05 05:42:50
	part5_correct_attempt
					['12:16:32', u'3/(sqrt(75/12))']
	part6_correct_attempt
					['13:21:39', u'Q(3/(sqrt(75/12)))']
	part7_incorrect_attempt
					('13:21:39', u'Q(3/(sqrt(75/12)))')
	part7_correct_attempt
					['13:22:02', u'2*Q(3/(sqrt(75/12)))']

51 Student ID:smohiman

	first_attempt
					2015-11-02 03:24:17
	part5_correct_attempt
					['0:10:20', u'1/(5*(1/12)^(1/2))']
	part6_correct_attempt
					['0:16:11', u'1-Phi(1/(5*(1/12)^(1/2)))']
	part7_incorrect_attempt
					('0:16:38', u'Phi(1/(5*(1/12)^(1/2)))')
	part7_correct_attempt
					['0:47:55', u'2-2Phi(1/(5*(1/12)^(1/2)))']

52 Student ID:jdeon

	first_attempt
					2015-11-04 05:41:59
	part5_correct_attempt
					['17:52:23', u'(3)/(90*(1/12))^(.5)']
	part6_correct_attempt
					['17:53:16', u'Q((3)/(90*(1/12))^(.5))']
	part7_incorrect_attempt
					('17:54:05', u'Q((3)/(90*(1/12))^(.5)) + Phi((3)/(90*(1/12))^(.5))')
					('17:55:13', u'1 - Q((3)/(90*(1/12))^(.5)) * Phi((3)/(90*(1/12))^(.5))')
					('17:56:06', u'(1 - Q((3)/(90*(1/12))^(.5))) *(1 - Phi((3)/(90*(1/12))^(.5)))')
					('17:56:37', u'1 - (1 - Q((3)/(90*(1/12))^(.5))) *(1 - Phi((3)/(90*(1/12))^(.5)))')
					('17:57:02', u'Phi((3)/(90*(1/12))^(.5))')
	part7_correct_attempt
					['17:57:32', u'2*Q((3)/(90*(1/12))^(.5))']

53 Student ID:jguanzho

	first_attempt
					2015-11-05 17:44:38
	part5_correct_attempt
					['4:55:54', u'4 / ((80/12)**0.5)']
	part6_correct_attempt
					['4:55:54', u'Q(4 / ((80/12)**0.5))']
	part7_incorrect_attempt
					('4:55:54', u'Phi(4 / ((80/12)**0.5))')
	part7_correct_attempt
					['5:02:40', u'2*Q(4 / ((80/12)**0.5))']

54 Student ID:jtfrankl

	first_attempt
					2015-11-06 19:06:40
	part5_correct_attempt
					['0:06:10', u'3/sqrt(80/12)']
	part6_correct_attempt
					['0:06:23', u'Q(3/sqrt(80/12))']
	part7_incorrect_attempt
					('0:06:23', u'Q(3/sqrt(80/12))')
	part7_correct_attempt
					['0:06:47', u'2Q(3/sqrt(80/12))']

55 Student ID:jhp077

	first_attempt
					2015-11-05 13:54:00
	part5_correct_attempt
					['0:11:14', u'4/((80/12)^(1/2))']
	part6_correct_attempt
					['0:15:47', u'Q(4/(80/12)^(1/2))']
	part7_incorrect_attempt
					('0:18:58', u'Q(4/(80/12)^(1/2)) + Q(1 - (4/(80/12)^(1/2)))')
					('0:26:17', u'0.939332')
	part7_correct_attempt
					['0:27:45', u'2*Q(4/(80/12)^(1/2))']

56 Student ID:xil109

	first_attempt
					2015-11-06 01:32:47
	part5_correct_attempt
					['0:02:48', u'4/sqrt(50/12)']
	part6_correct_attempt
					['0:04:37', u'0.0250219']
	part7_incorrect_attempt
					('0:05:31', u'1-0.0250219-0.974978')
					('0:06:57', u'1-(0.0250219-0.974978)')
	part7_correct_attempt
					['0:07:27', u'1-(0.974978-0.0250219)']

57 Student ID:dan029

	first_attempt
					2015-11-05 09:34:22
	part5_correct_attempt
					['0:27:02', u'4/sqrt(60/12)']
	part6_correct_attempt
					['0:27:30', u'Q(4/sqrt(60/12))']
	part7_incorrect_attempt
					('0:28:01', u'Q(4/sqrt(60/12))')
	part7_correct_attempt
					['0:28:18', u'2*Q(4/sqrt(60/12))']

58 Student ID:jhc010

	first_attempt
					2015-11-06 11:00:36
	part5_correct_attempt
					['0:04:35', u'(3-0)/sqrt(55*(sqrt(1/12)^2))']
	part6_correct_attempt
					['0:04:57', u'Q((3-0)/sqrt(55*(sqrt(1/12)^2)))']
	part7_incorrect_attempt
					('0:05:43', u'Phi((3-0)/sqrt(55*(sqrt(1/12)^2)))')
	part7_correct_attempt
					['0:06:35', u'Q((3-0)/sqrt(55*(sqrt(1/12)^2)))*2']

59 Student ID:z2tan

	first_attempt
					2015-11-02 06:14:19
	part5_correct_attempt
					['0:02:33', u'5/(60/12)^0.5']
	part6_correct_attempt
					['0:03:08', u'1-Phi(5/(60/12)^0.5)']
	part7_incorrect_attempt
					('0:03:24', u'Phi(5/(60/12)^0.5)')
					('0:05:25', u'1-(1-Phi(5/(60/12)^0.5))*2')
					('0:06:22', u'Phi(5/(60/12)^0.5)')
					('0:07:02', u'Phi(5/(60/12)^0.5)*2')
					('0:07:22', u'Phi(5/(60/12)^0.5)')
	part7_correct_attempt
					['0:09:42', u'2*(1-Phi(5/(60/12)^0.5))']

60 Student ID:mitopete

	first_attempt
					2015-11-04 05:20:00
	part5_correct_attempt
					['2 days, 18:19:44', u'3/((((1/12)*80)^(1/2)))']
	part6_correct_attempt
					['2 days, 18:31:56', u'1-Phi(3/((((1/12)*80)^(1/2))))']
	part7_incorrect_attempt
					('2 days, 18:32:15', u'Phi(3/((((1/12)*80)^(1/2))))*2')
					('2 days, 18:32:40', u'Phi(3/((((1/12)*80)^(1/2))))')
					('2 days, 18:33:38', u'(Phi(3/((((1/12)*80)^(1/2)))))/2')
	part7_correct_attempt
					['2 days, 18:35:54', u'(1-Phi(3/((((1/12)*80)^(1/2)))))*2']

61 Student ID:yig015

	first_attempt
					2015-11-05 10:57:48
	part5_correct_attempt
					['1 day, 1:55:34', u'3/8.0622578/0.288675']
	part6_correct_attempt
					['1 day, 1:57:44', u'Q(1.28901)']
	part7_incorrect_attempt
					('1 day, 1:57:44', u'1-Q(1.28901)')
	part7_correct_attempt
					['1 day, 1:58:35', u'2*Q(1.28901)']

62 Student ID:tpmach

	first_attempt
					2015-11-04 23:21:18
	part5_correct_attempt
					['19:16:40', u'5/sqrt(40*1/12(0.5+0.5)^2)']
	part6_correct_attempt
					['19:17:06', u'1-Phi(5/sqrt(40*1/12(0.5+0.5)^2))']
	part7_incorrect_attempt
					('19:18:16', u'(5/sqrt(40*1/12(0.5+0.5)^2))-(1-Phi(5/sqrt(40*1/12(0.5+0.5)^2)))')
					('19:18:58', u'(5/sqrt(40*1/12(0.5+0.5)^2))+(1-Phi(5/sqrt(40*1/12(0.5+0.5)^2)))')
					('19:19:33', u'2*5/sqrt(40*1/12(0.5+0.5)^2)')
	part7_correct_attempt
					['19:19:50', u'2*(1-Phi(5/sqrt(40*1/12(0.5+0.5)^2)))']

63 Student ID:vasharma

	first_attempt
					2015-11-05 21:38:45
	part5_correct_attempt
					['0:14:05', u'0.7108']
	part6_correct_attempt
					['0:14:27', u'0.2386']
	part7_incorrect_attempt
					('0:14:36', u'1- 0.2386')
					('0:14:48', u'0.7614')
					('0:15:35', u'0.9224- 0.2386')
					('1:16:21', u'1-0.0776')
					('1:52:11', u'.7614 - 0.2386')
	part7_correct_attempt
					['1:55:50', u'2* 0.2386']

64 Student ID:kgrozav

	first_attempt
					2015-11-05 20:52:42
	part5_correct_attempt
					['10:52:00', u'0.8944275']
	part6_correct_attempt
					['10:58:44', u'Q(0.8944275)']
	part7_incorrect_attempt
					('10:59:20', u'Q(2 *0.8944275)')
					('10:59:43', u'Q(0.8944275)')
					('11:01:46', u'1-Q(0.8944275)')
					('11:03:28', u'1 - Phi(0.8944275)')
					('11:03:37', u'Phi(0.8944275)')
	part7_correct_attempt
					['11:14:09', u'2*Q(0.8944275)']

65 Student ID:hsc052

	first_attempt
					2015-11-06 23:07:48
	part5_correct_attempt
					['0:14:06', u'4/[sqrt(70)*sqrt(1/12)]']
	part6_correct_attempt
					['0:14:06', u'Q(4/[sqrt(70)*sqrt(1/12)])']
	part7_incorrect_attempt
					('0:14:06', u'Phi(4/[sqrt(70)*sqrt(1/12)])')
					('0:16:25', u'Phi(8/[sqrt(70)*sqrt(1/12)])*2')
					('0:16:36', u'Phi(0/[sqrt(70)*sqrt(1/12)])*2')
					('0:18:32', u'Q(8/[sqrt(70)*sqrt(1/12)]) + Phi(0)')
	part7_correct_attempt
					['0:20:17', u'Q(4/[sqrt(70)*sqrt(1/12)])*2']

66 Student ID:c3chung

	first_attempt
					2015-11-06 22:30:22
	part5_correct_attempt
					['0:03:33', u'3/2.81366']
	part7_incorrect_attempt
					('0:04:48', u'0.8577')
					('0:04:58', u'1-0.8577')

67 Student ID:k4ma

	first_attempt
					2015-11-06 21:42:17
	part5_correct_attempt
					['0:16:41', u'2/sqrt(1/12*50)']
	part6_correct_attempt
					['0:17:04', u'1-Phi(2/sqrt(1/12*50))']
	part7_incorrect_attempt
					('0:21:06', u'[1-Phi(2/sqrt(1/12*50))]*[1-Phi(-2/sqrt(1/12*50))]')
					('0:21:29', u'[1-Phi(2/sqrt(1/12*50))]+[1-Phi(-2/sqrt(1/12*50))]')
	part7_correct_attempt
					['0:22:06', u'[1-Phi(2/sqrt(1/12*50))]*2']

68 Student ID:ccn001

	first_attempt
					2015-11-05 16:26:42
	part5_correct_attempt
					['14:55:08', u'2/((45/12)^(0.5))']
	part6_correct_attempt
					['14:55:08', u'Q(2/((45/12)^(0.5)))']
	part7_incorrect_attempt
					('14:55:08', u'Q(2/((45/12)^(0.5)))+Phi(2/((1/12)^(0.5)(45)))')
	part7_correct_attempt
					['14:55:52', u'2*Q(2/((45/12)^(0.5)))']

69 Student ID:v3doan

	first_attempt
					2015-11-05 16:26:50
	part5_correct_attempt
					['1 day, 8:31:35', u'2 / sqrt(85/12)']
	part6_correct_attempt
					['1 day, 8:31:49', u'Q(2 / sqrt(85/12))']
	part7_incorrect_attempt
					('1 day, 8:31:49', u'Q(2 / sqrt(85/12))')
	part7_correct_attempt
					['1 day, 8:32:22', u'2Q(2 / sqrt(85/12))']

70 Student ID:zhw110

	first_attempt
					2015-11-06 23:08:09
	part5_correct_attempt
					['0:59:09', u'5/((85/12)^0.5)']
	part6_correct_attempt
					['0:59:51', u'Q(5/((85/12)^0.5))']
	part7_incorrect_attempt
					('0:59:51', u'Phi(5/((85/12)^0.5))')
	part7_correct_attempt
					['1:02:08', u'2Q(5/((85/12)^0.5))']

71 Student ID:cagatep

	first_attempt
					2015-11-05 07:53:35
	part5_correct_attempt
					['1 day, 11:58:04', u'4/sqrt(90/12)']
	part6_correct_attempt
					['1 day, 11:59:38', u'Q(4/sqrt(90/12))']
	part7_incorrect_attempt
					('1 day, 11:59:38', u'Q(4/sqrt(90/12))')
	part7_correct_attempt
					['1 day, 11:59:57', u'Q(4/sqrt(90/12)) * 2']

72 Student ID:akg009

	first_attempt
					2015-11-06 21:08:58
	part5_correct_attempt
					['0:12:27', u'4/sqrt(30)']
	part6_correct_attempt
					['0:51:00', u'Q(4/sqrt(30))']
	part7_incorrect_attempt
					('0:51:00', u'Q(4/sqrt(30))')
	part7_correct_attempt
					['0:51:24', u'2*Q(4/sqrt(30))']

73 Student ID:sthapa

	first_attempt
					2015-11-07 00:07:09
	part5_correct_attempt
					['0:01:20', u'5/(sqrt(100)/sqrt(12))']
	part6_correct_attempt
					['0:01:52', u'Q(5/(sqrt(100)/sqrt(12)))']
	part7_incorrect_attempt
					('0:01:52', u'Q(5/(sqrt(100)/sqrt(12)))')
	part7_correct_attempt
					['0:02:33', u'Q(5/(sqrt(100)/sqrt(12)))*2']

74 Student ID:pnquach

	first_attempt
					2015-11-06 05:50:54
	part5_correct_attempt
					['0:05:13', u'(4)/(sqrt(1/12*(1)^2*65))']
	part6_correct_attempt
					['0:05:13', u'Q((4)/(sqrt(1/12*(1)^2*65)))']
	part7_incorrect_attempt
					('0:05:13', u'Phi((4)/(sqrt(1/12*(1)^2*65)))')
	part7_correct_attempt
					['0:09:57', u'Q((4)/(sqrt(1/12*(1)^2*65)))*2']

75 Student ID:k3tan

	first_attempt
					2015-11-04 21:45:25
	part5_correct_attempt
					['2 days, 2:04:28', u'5/sqrt(65/12)']
	part7_incorrect_attempt
					('2 days, 2:09:13', u'0.5-0.4842')
					('2 days, 2:09:20', u'0.4842')
					('2 days, 2:09:56', u'0.5-0.4842')

76 Student ID:asp025

	first_attempt
					2015-11-06 23:24:43
	part5_correct_attempt
					['0:15:57', u'(3-0)/[85(.5+.5)^2/12]^(1/2)']
	part6_correct_attempt
					['0:16:15', u'1-Phi((3-0)/[85(.5+.5)^2/12]^(1/2))']
	part7_incorrect_attempt
					('0:17:00', u'Phi((3-0)/[85(.5+.5)^2/12]^(1/2))')
	part7_correct_attempt
					['0:50:51', u'2(1-Phi((3-0)/[85(.5+.5)^2/12]^(1/2)))']












