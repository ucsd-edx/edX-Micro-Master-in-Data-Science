#Problem 6

    $n = 2*random(40,50,1);

    Let [`X_1, X_2, \ldots, X_{100}`] be the outcomes of [`100`] independent rolls of a fair coin.
    [`P(X_i=0)=P(X_i=1)=0.5`]

    1. [`\mathbb{E}(X_1) = `][____]{"1/2"}
    2. [`var(X_1) = `][_______]{"1/4"}

    Define the random variable [`X`] to be [`X_1 - X_2`].
    3. [`\mathbb{E}(X) = `][______]{"0"}
    4. [`var(X) = `][_______]{"1/2"}
       *Hint:* if [`X,Y`] are independent random variables then [`var(X+Y)=var(X)+var(Y)`]

    Define the random variable [`Y = X_1 - 2X_2 + X_3`].
    5. [`\mathbb{E}(Y) = `][_______]{"0"}
    6. [`var(Y) = `][_________]{"6/4"}
       *Hint:* if [`a`] is a constant and [`X`] a random variable, then [`var(aX)=a^2 var(X)`].

    Define the random variable [`Z = X_1 - X_2 + X_3 - X_4 + ... + X_{[$n-1]} - X_{[$n]}`].
    7. [`\mathbb{E}(Z) = `][_______]{"0"}
    8. [`var(Z) = `][_________]{"$n/4"}




## Part 1

### (56) Mistake Group Digits of size 56




### (7) Mistake Group ['R.1'] of size 7
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|1/2	|5500/2	|[('R.1', 2.0, u'2', u'2')]	|
|1	|1/2	|5050/2	|[('R.1', 2.0, u'2', u'2')]	|
|2	|1/2	|(100*.5)^2	|[('R.1', 2.0, u'2', u'2')]	|
|3	|1/2	|7/2	|[('R.1', 2.0, u'2', u'2')]	|
|4	|1/2	|3/2	|[('R.1', 2.0, u'2', u'2')]	|




### (7) Mistake Group ['R.0'] of size 7
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|1/2	|1/(2**100)	|[('R.0', 1.0, u'1', u'1')]	|
|1	|1/2	|1/100	|[('R.0', 1.0, u'1', u'1')]	|
|2	|1/2	|1/0.5	|[('R.0', 1.0, u'1', u'1')]	|




### (1) Mistake Group Wrong_Sign of size 1




### (25) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:flhernan

	first_attempt
					2015-11-03 19:14:36
	part1_incorrect_attempt
					('0:00:00', u'100*.5')
					('0:00:11', u'100*.5 + 100*.5')
					('0:01:27', u'.5 +.5')
					('0:01:45', u'.5 +2*.5')
	part1_correct_attempt
					['0:01:54', u'.5']

1 Student ID:v4zhang

	first_attempt
					2015-11-05 11:00:02
	part1_incorrect_attempt
					('0:00:00', u'100*0.5')
					('0:01:37', u'[(100*101)/2]*100')
	part1_correct_attempt
					['0:05:42', u'0.5']

2 Student ID:lguintu

	first_attempt
					2015-11-03 04:17:09
	part1_incorrect_attempt
					('0:00:00', u'(100+101)/4')
	part1_correct_attempt
					['0:00:48', u'1/2']

3 Student ID:ppanourg

	first_attempt
					2015-11-06 08:17:03
	part1_incorrect_attempt
					('0:00:00', u'100*.5')
					('0:00:16', u'100/.5')
	part1_correct_attempt
					['0:07:22', u'.5']

4 Student ID:asp025

	first_attempt
					2015-11-06 19:55:25
	part1_incorrect_attempt
					('0:00:00', u'100*0.5')
	part1_correct_attempt
					['0:00:16', u'1*0.5']

5 Student ID:j5phung

	first_attempt
					2015-11-04 04:16:43
	part1_incorrect_attempt
					('0:00:00', u'100/0.5')
	part1_correct_attempt
					['0:01:24', u'0.5']

6 Student ID:jcl084

	first_attempt
					2015-11-02 20:07:11
	part1_incorrect_attempt
					('0:00:00', u'(1/6)(1+2+3+4+5+6)')
	part1_correct_attempt
					['0:01:24', u'0.5']

7 Student ID:skodigal

	first_attempt
					2015-11-05 09:08:31
	part1_incorrect_attempt
					('0:00:00', u'.5*100 + .5*100')
					('0:01:05', u'.5*100')
	part1_correct_attempt
					['0:02:05', u'.5']

8 Student ID:rraiyyan

	first_attempt
					2015-11-06 21:17:36
	part1_incorrect_attempt
					('0:00:00', u'C(101,2) * 1/(2^100)')
	part1_correct_attempt
					['0:00:38', u'0.5']

9 Student ID:jhw015

	first_attempt
					2015-11-04 19:35:06
	part1_incorrect_attempt
					('0:00:00', u'(0.5 + 1)')
	part1_correct_attempt
					['0:02:09', u'0.5']

10 Student ID:t1tran

	first_attempt
					2015-10-31 05:58:58
	part1_incorrect_attempt
					('0:00:00', u'100*.5')
	part1_correct_attempt
					['3 days, 3:02:44', u'1(.5)+00(1-.5)']

11 Student ID:krkelkar

	first_attempt
					2015-10-31 20:47:19
	part1_incorrect_attempt
					('0:00:00', u'100 * 0.5')
	part1_correct_attempt
					['0:00:46', u'1 * 0.5']

12 Student ID:tcuddy

	first_attempt
					2015-11-01 19:24:34
	part1_incorrect_attempt
					('0:00:00', u'100(.5)')
					('0:55:53', u'100(1/(2**100))')
					('0:56:35', u'100((1/2)**100)')
	part1_correct_attempt
					['1 day, 22:22:08', u'.5']

13 Student ID:anvan

	first_attempt
					2015-11-05 16:34:33
	part1_incorrect_attempt
					('0:00:00', u'100! / (50! 50!) * .5^50 * .5^50')
					('0:23:51', u'100! / (50!50!) * (1/2)^50(1/2)^50')
	part1_correct_attempt
					['2:03:02', u'.5']

14 Student ID:arvenega

	first_attempt
					2015-11-05 00:15:27
	part1_incorrect_attempt
					('0:00:00', u'.5 * 100')
					('0:05:12', u'(100*101)/4')
	part1_correct_attempt
					['1 day, 23:18:46', u'.5']

15 Student ID:haliew

	first_attempt
					2015-11-06 22:49:24
	part1_incorrect_attempt
					('0:00:00', u'.5(100)')
	part1_correct_attempt
					['0:03:39', u'.5']

16 Student ID:lahawkin

	first_attempt
					2015-11-04 04:45:48
	part1_incorrect_attempt
					('0:00:00', u'.5(100)')
	part1_correct_attempt
					['1 day, 14:04:36', u'.5(1)']

17 Student ID:c1wei

	first_attempt
					2015-11-04 06:40:32
	part1_incorrect_attempt
					('0:00:00', u'100*.5')
	part1_correct_attempt
					['0:01:50', u'.5']

18 Student ID:csl030

	first_attempt
					2015-11-05 04:54:09
	part1_incorrect_attempt
					('0:00:00', u'1.5')
	part1_correct_attempt
					['0:00:07', u'.5']

19 Student ID:aurodrig

	first_attempt
					2015-11-06 22:25:09
	part1_incorrect_attempt
					('0:00:00', u'1/6 * (1+2+3+4+5+6)')
					('0:00:08', u'1/2 * (1+2+3+4+5+6)')
	part1_correct_attempt
					['0:00:24', u'1/2 * (1)']

20 Student ID:vasharma

	first_attempt
					2015-11-04 18:44:56
	part1_incorrect_attempt
					('0:00:00', u'.5*100')
	part1_correct_attempt
					['0:01:04', u'.5']

21 Student ID:ajvanega

	first_attempt
					2015-11-05 02:29:47
	part1_incorrect_attempt
					('0:00:00', u'3.5')
	part1_correct_attempt
					['0:00:31', u'.5']

22 Student ID:tjke

	first_attempt
					2015-11-04 20:53:46
	part1_incorrect_attempt
					('0:00:00', u'100*0.5')
	part1_correct_attempt
					['0:00:07', u'0.5']

23 Student ID:sthapa

	first_attempt
					2015-11-06 23:55:54
	part1_incorrect_attempt
					('0:00:00', u'(1-2*1/2+1/3-2*1/4+1/5)*1')
	part1_correct_attempt
					['0:00:28', u'1/2']

24 Student ID:cprafull

	first_attempt
					2015-11-05 05:19:13
	part1_incorrect_attempt
					('0:00:00', u'3.5')
					('0:00:08', u'3.5*100')
	part1_correct_attempt
					['0:00:30', u'0.5']












## Part 2

### (128) Mistake Group Digits of size 128




### (16) Mistake Group redirect of size 16




### (14) Mistake Group ['R.0'] of size 14
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|1/4	|1 - (0.5 ^ 2)	|[('R.0', 1.0, u'1', u'1')]	|
|1	|1/4	|1-.5^2	|[('R.0', 1.0, u'1', u'1')]	|
|2	|1/4	|1/2	|[('R.0', 1.0, u'1', u'1')]	|
|3	|1/4	|1^2^0.5 - (0.5)^2	|[('R.0', 1.0, u'1', u'1^2^0.5')]	|
|4	|1/4	|1/(0.5^(2))	|[('R.0', 1.0, u'1', u'1')]	|
|5	|1/4	|1/12	|[('R.0', 1.0, u'1', u'1')]	|
|6	|1/4	|1-0.5	|[('R.0', 1.0, u'1', u'1')]	|
|7	|1/4	|1/.5^2	|[('R.0', 1.0, u'1', u'1')]	|
|8	|1/4	|1/8	|[('R.0', 1.0, u'1', u'1')]	|
|9	|1/4	|1/16	|[('R.0', 1.0, u'1', u'1')]	|




### (7) Mistake Group Wrong_Sign of size 7




### (85) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:gthorn

	first_attempt
					2015-11-02 07:26:59
	part1_correct_attempt
					['0:00:00', u'0.5']
	part2_incorrect_attempt
					('1 day, 12:31:32', u'0.5')
	part2_correct_attempt
					['1 day, 12:34:08', u'0.25']

1 Student ID:phodgson

	first_attempt
					2015-11-05 06:02:34
	part1_correct_attempt
					['0:00:00', u'.5']
	part2_incorrect_attempt
					('0:00:00', u'.5')
	part2_correct_attempt
					['0:00:08', u'.25']

2 Student ID:haw081

	first_attempt
					2015-11-01 05:01:44
	part1_correct_attempt
					['0:00:00', u'0.5']
	part2_incorrect_attempt
					('0:00:28', u'1(0.5)(1.5)')
	part2_correct_attempt
					['0:00:36', u'1(0.5)(0.5)']

3 Student ID:lpettit

	first_attempt
					2015-11-06 23:23:57
	part1_correct_attempt
					['0:00:00', u'.5']
	part2_incorrect_attempt
					('0:00:15', u'.5')
					('0:09:45', u'.5')
	part2_correct_attempt
					['0:11:02', u'(2*.5*.5)/2']

4 Student ID:jfalcone

	first_attempt
					2015-11-04 05:25:50
	part1_correct_attempt
					['0:00:00', u'.5']
	part2_incorrect_attempt
					('0:00:21', u'.5')
	part2_correct_attempt
					['23:55:11', u'(1/2)*.5']

5 Student ID:ccn001

	first_attempt
					2015-11-03 09:09:46
	part1_correct_attempt
					['0:00:00', u'(0(.5)+1(.5))']
	part2_incorrect_attempt
					('0:00:00', u'0.5')
	part2_correct_attempt
					['7:29:01', u'(0.5)^2']

6 Student ID:lywong

	first_attempt
					2015-11-04 19:08:27
	part1_correct_attempt
					['0:00:00', u'0.5']
	part2_incorrect_attempt
					('0:00:37', u'(0.5)^(1/2)')
					('0:04:17', u'(1-0.5)^2+ (-0.5)^2')
	part2_correct_attempt
					['0:05:46', u'((1-0.5)^2+ (-0.5)^2)/2']

7 Student ID:jtfrankl

	first_attempt
					2015-11-06 18:24:55
	part1_correct_attempt
					['0:00:00', u'.5']
	part2_incorrect_attempt
					('0:00:30', u'.5')
	part2_correct_attempt
					['0:02:16', u'.25']

8 Student ID:dsmonaha

	first_attempt
					2015-11-02 16:47:16
	part1_correct_attempt
					['0:00:00', u'.5']
	part2_incorrect_attempt
					('0:08:03', u'(1-.5)/(.5)^2')
					('0:13:18', u'.5')
	part2_correct_attempt
					['0:15:28', u'.25']

9 Student ID:quwong

	first_attempt
					2015-11-03 18:30:27
	part1_correct_attempt
					['0:00:00', u'0.5']
	part2_incorrect_attempt
					('2:13:26', u'1*2^0.5 - (0.5)^2')
	part2_correct_attempt
					['2:14:37', u'1^2*0.5 - (0.5)^2']

10 Student ID:kbielawi

	first_attempt
					2015-11-03 20:55:13
	part1_correct_attempt
					['0:00:00', u'.5']
	part2_incorrect_attempt
					('0:00:00', u'.5')
	part2_correct_attempt
					['23:11:51', u'.25']

11 Student ID:rbdoming

	first_attempt
					2015-11-05 18:49:18
	part1_correct_attempt
					['0:00:00', u'0.5']
	part2_incorrect_attempt
					('0:00:00', u'0.5')
	part2_correct_attempt
					['0:03:02', u'0.5-(0.5)^2']

12 Student ID:glcohen

	first_attempt
					2015-11-03 16:48:17
	part1_correct_attempt
					['0:00:00', u'0.5']
	part2_incorrect_attempt
					('0:00:00', u'0.5')
	part2_correct_attempt
					['0:05:58', u'0.25']

13 Student ID:c1sorian

	first_attempt
					2015-11-04 23:20:51
	part1_correct_attempt
					['0:00:00', u'.5']
	part2_incorrect_attempt
					('0:00:15', u'.5')
	part2_correct_attempt
					['0:02:35', u'.25']

14 Student ID:tdurrer

	first_attempt
					2015-11-06 03:30:34
	part1_correct_attempt
					['0:00:00', u'.5']
	part2_incorrect_attempt
					('0:00:00', u'.5')
	part2_correct_attempt
					['0:00:14', u'.25']

15 Student ID:rohan

	first_attempt
					2015-11-06 23:40:02
	part1_correct_attempt
					['0:00:00', u'.5']
	part2_incorrect_attempt
					('0:11:10', u'.5')
	part2_correct_attempt
					['0:11:42', u'.5-.5^2']

16 Student ID:spw006

	first_attempt
					2015-11-04 00:39:13
	part1_correct_attempt
					['0:00:00', u'0.5']
	part2_incorrect_attempt
					('0:00:00', u'0.5')
	part2_correct_attempt
					['2:16:55', u'0.5 - 0.25']

17 Student ID:masaro

	first_attempt
					2015-11-02 15:53:21
	part1_correct_attempt
					['0:00:00', u'0.5']
	part2_incorrect_attempt
					('0:14:36', u'0.5')
	part2_correct_attempt
					['0:14:46', u'0.25']

18 Student ID:krau

	first_attempt
					2015-11-04 19:46:04
	part1_correct_attempt
					['0:00:00', u'.5']
	part2_incorrect_attempt
					('0:00:00', u'.5')
	part2_correct_attempt
					['0:04:37', u'.25']

19 Student ID:mhale

	first_attempt
					2015-11-05 20:08:27
	part1_correct_attempt
					['0:00:00', u'0.5']
	part2_incorrect_attempt
					('0:02:31', u'0.5')
	part2_correct_attempt
					['0:02:42', u'0.25']

20 Student ID:thk002

	first_attempt
					2015-11-03 23:06:16
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_incorrect_attempt
					('0:04:53', u'.5-0')
	part2_correct_attempt
					['0:07:39', u'1/4']

21 Student ID:awollner

	first_attempt
					2015-11-06 22:55:15
	part1_correct_attempt
					['0:00:00', u'.5']
	part2_incorrect_attempt
					('0:02:25', u'.25/2')
	part2_correct_attempt
					['0:12:45', u'.25']

22 Student ID:dcrume

	first_attempt
					2015-11-06 19:09:00
	part1_correct_attempt
					['0:00:00', u'.5']
	part2_incorrect_attempt
					('0:00:00', u'(.5*.5/100)^.5')
					('0:00:59', u'(.5*.5/100)')
					('0:09:59', u'.5^(2)/100')
					('0:18:40', u'.5*.5*100')
	part2_correct_attempt
					['0:30:54', u'.5*.5/1']

23 Student ID:ctgraves

	first_attempt
					2015-11-03 05:16:32
	part1_correct_attempt
					['0:00:00', u'0.5']
	part2_incorrect_attempt
					('0:00:21', u'100(0.25)')
	part2_correct_attempt
					['0:00:34', u'0.25']

24 Student ID:jdeon

	first_attempt
					2015-11-04 23:14:31
	part1_correct_attempt
					['0:00:00', u'.5']
	part2_incorrect_attempt
					('0:00:20', u'.5')
	part2_correct_attempt
					['0:00:38', u'.25']

25 Student ID:dlt009

	first_attempt
					2015-11-05 07:36:02
	part1_correct_attempt
					['0:00:00', u'0.5']
	part2_incorrect_attempt
					('0:03:34', u'0.5')
	part2_correct_attempt
					['0:13:28', u'0.5-0.25']

26 Student ID:psable

	first_attempt
					2015-11-06 00:05:06
	part1_correct_attempt
					['0:00:00', u'.5']
	part2_incorrect_attempt
					('0:03:14', u'.5')
	part2_correct_attempt
					['0:04:28', u'.25']

27 Student ID:vasharma

	first_attempt
					2015-11-04 18:46:00
	part1_correct_attempt
					['0:00:00', u'.5']
	part2_incorrect_attempt
					('0:00:13', u'.5')
	part2_correct_attempt
					['0:00:50', u'.5*.5']

28 Student ID:p4kumar

	first_attempt
					2015-11-05 23:59:56
	part1_correct_attempt
					['0:00:00', u'0.5']
	part2_incorrect_attempt
					('0:00:18', u'0.5')
	part2_correct_attempt
					['0:01:04', u'0.25']

29 Student ID:b3hwang

	first_attempt
					2015-11-05 08:38:09
	part1_correct_attempt
					['0:00:00', u'.5']
	part2_incorrect_attempt
					('0:00:28', u'.5')
	part2_correct_attempt
					['0:00:38', u'.25']

30 Student ID:kthui

	first_attempt
					2015-11-06 02:15:58
	part1_correct_attempt
					['0:00:00', u'0.5']
	part2_incorrect_attempt
					('0:08:22', u'0.25/2')
	part2_correct_attempt
					['0:08:27', u'0.25']

31 Student ID:syc078

	first_attempt
					2015-11-05 03:28:26
	part1_correct_attempt
					['0:00:00', u'0.5']
	part2_incorrect_attempt
					('22:13:12', u'0.5')
	part2_correct_attempt
					['22:15:02', u'0.25']

32 Student ID:jyc018

	first_attempt
					2015-11-01 01:25:42
	part1_correct_attempt
					['0:00:00', u'0.5']
	part2_incorrect_attempt
					('0:00:05', u'0.5')
					('0:01:02', u'1/0.5/0.5')
	part2_correct_attempt
					['0:01:12', u'0.5*0.5']

33 Student ID:bmilton

	first_attempt
					2015-11-04 19:46:12
	part1_correct_attempt
					['0:00:00', u'.5']
	part2_incorrect_attempt
					('0:00:25', u'(1-.5)/.25')
					('0:01:04', u'.5/.25')
	part2_correct_attempt
					['0:03:11', u'.5 - .25']

34 Student ID:dcgriffi

	first_attempt
					2015-11-06 23:44:39
	part1_correct_attempt
					['0:00:00', u'.5']
	part2_incorrect_attempt
					('0:00:00', u'.5')
	part2_correct_attempt
					['0:03:07', u'1/4']

35 Student ID:kquong

	first_attempt
					2015-11-02 04:08:58
	part1_correct_attempt
					['0:00:00', u'.5']
	part2_incorrect_attempt
					('0:00:00', u'.5')
	part2_correct_attempt
					['0:05:59', u'.25']

36 Student ID:xil109

	first_attempt
					2015-11-05 03:20:50
	part1_correct_attempt
					['0:00:00', u'0.5']
	part2_incorrect_attempt
					('0:08:18', u'0.5')
	part2_correct_attempt
					['0:09:21', u'0.5-0.5^2']

37 Student ID:rlhagen

	first_attempt
					2015-10-31 17:11:50
	part1_correct_attempt
					['0:00:00', u'0.5']
	part2_incorrect_attempt
					('0:00:10', u'0.5')
					('0:07:24', u'0.5')
	part2_correct_attempt
					['0:07:54', u'0.5/2']

38 Student ID:avasavad

	first_attempt
					2015-11-04 23:06:05
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_incorrect_attempt
					('0:03:21', u'1/2 - 0.5')
	part2_correct_attempt
					['0:32:18', u'1/4']

39 Student ID:nnh002

	first_attempt
					2015-11-05 03:58:12
	part1_correct_attempt
					['0:00:00', u'0.5']
	part2_incorrect_attempt
					('0:00:00', u'(1-0.5)^2+(0-0.5)^2')
	part2_correct_attempt
					['0:00:20', u'(1-0.5)^2*0.5+(0-0.5)^2*0.5']

40 Student ID:dac064

	first_attempt
					2015-11-05 08:56:16
	part1_correct_attempt
					['0:00:00', u'.5']
	part2_incorrect_attempt
					('0:02:52', u'.5')
	part2_correct_attempt
					['0:06:20', u'1/4']

41 Student ID:t2li

	first_attempt
					2015-11-06 01:28:07
	part1_correct_attempt
					['0:00:00', u'0.5']
	part2_incorrect_attempt
					('0:00:00', u'0.5')
	part2_correct_attempt
					['0:00:10', u'0.5*0.5']

42 Student ID:twsalim

	first_attempt
					2015-11-04 03:30:14
	part1_correct_attempt
					['0:00:00', u'0.5']
	part2_incorrect_attempt
					('0:01:49', u'0.5')
	part2_correct_attempt
					['1:01:15', u'0.25']

43 Student ID:sachadal

	first_attempt
					2015-11-05 19:54:30
	part1_correct_attempt
					['0:00:00', u'0.5']
	part2_incorrect_attempt
					('0:03:05', u'0.5')
	part2_correct_attempt
					['0:06:17', u'0.25']

44 Student ID:jap009

	first_attempt
					2015-11-05 21:00:35
	part1_correct_attempt
					['0:00:00', u'.5']
	part2_incorrect_attempt
					('0:00:00', u'.5')
	part2_correct_attempt
					['0:01:34', u'.25']

45 Student ID:jcl084

	first_attempt
					2015-11-02 20:08:35
	part1_correct_attempt
					['0:00:00', u'0.5']
	part2_incorrect_attempt
					('0:00:41', u'0.5^2 - 0.5^2')
	part2_correct_attempt
					['0:00:46', u'0.5^2']

46 Student ID:vsosnovs

	first_attempt
					2015-11-05 20:50:05
	part1_correct_attempt
					['0:00:00', u'.5']
	part2_incorrect_attempt
					('0:02:03', u'.5')
	part2_correct_attempt
					['0:02:11', u'.5-.25']

47 Student ID:rraiyyan

	first_attempt
					2015-11-06 21:18:14
	part1_correct_attempt
					['0:00:00', u'0.5']
	part2_incorrect_attempt
					('0:00:20', u'0.5')
	part2_correct_attempt
					['0:00:26', u'0.25']

48 Student ID:hachrist

	first_attempt
					2015-11-03 20:13:34
	part1_correct_attempt
					['0:00:00', u'0.5']
	part2_incorrect_attempt
					('0:23:08', u'0.5 - 0.5')
	part2_correct_attempt
					['0:23:34', u'0.5 - 0.5^2']

49 Student ID:mpanelo

	first_attempt
					2015-11-01 23:13:44
	part1_correct_attempt
					['0:00:00', u'0.5']
	part2_incorrect_attempt
					('0:00:00', u'0.125')
	part2_correct_attempt
					['0:01:02', u'0.25']

50 Student ID:v4zhang

	first_attempt
					2015-11-05 11:05:44
	part1_correct_attempt
					['0:00:00', u'0.5']
	part2_incorrect_attempt
					('0:00:49', u'0.5')
	part2_correct_attempt
					['0:01:09', u'0.5-(0.5^2)']

51 Student ID:hkhodada

	first_attempt
					2015-10-31 15:40:08
	part1_correct_attempt
					['0:00:00', u'.5']
	part2_incorrect_attempt
					('0:00:00', u'0.5')
	part2_correct_attempt
					['0:03:53', u'0.25']

52 Student ID:zhw110

	first_attempt
					2015-11-06 00:40:42
	part1_correct_attempt
					['0:00:00', u'0.5']
	part2_incorrect_attempt
					('0:00:00', u'0.5')
					('23:40:20', u'0.5')
					('23:42:15', u'0.5^2+0.5^2')
	part2_correct_attempt
					['23:42:51', u'0.5^2']

53 Student ID:tstevens

	first_attempt
					2015-11-06 11:34:10
	part1_correct_attempt
					['0:00:00', u'.5']
	part2_incorrect_attempt
					('0:00:08', u'.5')
					('0:09:02', u'1.5')
					('0:10:15', u'.5/.25')
	part2_correct_attempt
					['0:12:46', u'.25']

54 Student ID:pthsu

	first_attempt
					2015-10-31 03:31:32
	part1_correct_attempt
					['0:00:00', u'0.5']
	part2_incorrect_attempt
					('0:00:23', u'.5')
	part2_correct_attempt
					['0:05:51', u'1/4']

55 Student ID:bkoli

	first_attempt
					2015-11-05 21:23:15
	part1_correct_attempt
					['0:00:00', u'0.5']
	part2_incorrect_attempt
					('0:02:02', u'(1-0.5)/(0.5^2)')
					('0:08:31', u'0.5')
	part2_correct_attempt
					['0:15:06', u'0.5(0.5)']

56 Student ID:cagatep

	first_attempt
					2015-11-05 06:53:46
	part1_correct_attempt
					['0:00:00', u'.5']
	part2_incorrect_attempt
					('0:00:27', u'.5')
	part2_correct_attempt
					['0:01:45', u'.25']

57 Student ID:a2ahmed

	first_attempt
					2015-11-07 00:29:33
	part1_correct_attempt
					['0:00:00', u'0.5']
	part2_incorrect_attempt
					('0:00:43', u'0.5')
	part2_correct_attempt
					['0:00:59', u'0.25']

58 Student ID:cstringh

	first_attempt
					2015-11-04 06:26:19
	part1_correct_attempt
					['0:00:00', u'0.5']
	part2_incorrect_attempt
					('0:00:00', u'0.5')
	part2_correct_attempt
					['0:15:41', u'0.25']

59 Student ID:chc286

	first_attempt
					2015-11-01 01:22:52
	part1_correct_attempt
					['0:00:00', u'1*0.5+0']
	part2_incorrect_attempt
					('0:01:01', u'0.5*(0.5-0.5)^2+0.5*(0-0.5)^2')
	part2_correct_attempt
					['0:01:49', u'0.5*(1-0.5)^2+0.5*(0-0.5)^2']

60 Student ID:sayao

	first_attempt
					2015-11-04 01:24:54
	part1_correct_attempt
					['0:00:00', u'.5']
	part2_incorrect_attempt
					('0:00:18', u'.5')
	part2_correct_attempt
					['0:06:55', u'.5*.5']

61 Student ID:anvan

	first_attempt
					2015-11-05 18:37:35
	part1_correct_attempt
					['0:00:00', u'.5']
	part2_incorrect_attempt
					('0:00:56', u'49.5^2')
	part2_correct_attempt
					['0:01:33', u'.5^2']

62 Student ID:any027

	first_attempt
					2015-11-01 20:11:07
	part1_correct_attempt
					['0:00:00', u'(0.5)']
	part2_incorrect_attempt
					('0:00:39', u'0.5')
					('0:01:17', u'(0.5 ^ 2 )/ 2')
	part2_correct_attempt
					['0:01:59', u'(0.5 ^2 + 0.5 ^ 2 )/ 2']

63 Student ID:ppanourg

	first_attempt
					2015-11-06 08:24:25
	part1_correct_attempt
					['0:00:00', u'.5']
	part2_incorrect_attempt
					('0:00:26', u'.5')
	part2_correct_attempt
					['0:09:48', u'.25']

64 Student ID:dtea

	first_attempt
					2015-11-07 00:16:24
	part1_correct_attempt
					['0:00:00', u'.5']
	part2_incorrect_attempt
					('0:00:44', u'.5')
					('0:37:06', u'(1/12)(.5-.5)^2')
					('0:37:20', u'(1/12)(.5)^2')
					('0:40:50', u'(1-.5)/.5^2')
					('0:41:27', u'(1-.5)/.5^2')

65 Student ID:btn023

	first_attempt
					2015-11-06 10:42:56
	part1_correct_attempt
					['0:00:00', u'.5']
	part2_incorrect_attempt
					('0:00:00', u'.5')
					('0:01:47', u'.5*(1-.5)^2')
	part2_correct_attempt
					['0:02:29', u'2*.5*(1-.5)^2']

66 Student ID:c1wei

	first_attempt
					2015-11-04 06:42:22
	part1_correct_attempt
					['0:00:00', u'.5']
	part2_incorrect_attempt
					('0:00:25', u'.5')
	part2_correct_attempt
					['0:02:10', u'.25']

67 Student ID:azkong

	first_attempt
					2015-11-06 19:40:48
	part1_correct_attempt
					['0:00:00', u'0.5']
	part2_incorrect_attempt
					('0:04:04', u'0.5/0.5^2')
					('0:16:51', u'0.5')
	part2_correct_attempt
					['1:09:18', u'0.25']

68 Student ID:yjshin

	first_attempt
					2015-11-06 22:57:48
	part1_correct_attempt
					['0:00:00', u'0.5']
	part2_incorrect_attempt
					('0:06:43', u'0.5')
	part2_correct_attempt
					['0:09:39', u'.5^2']

69 Student ID:yhhan

	first_attempt
					2015-11-06 23:44:23
	part1_correct_attempt
					['0:00:00', u'.5']
	part2_incorrect_attempt
					('0:00:00', u'.5')

70 Student ID:kgrozav

	first_attempt
					2015-11-05 07:35:53
	part1_correct_attempt
					['0:00:00', u'0.5']
	part2_incorrect_attempt
					('0:00:00', u'0.5')
	part2_correct_attempt
					['0:07:12', u'0.25']

71 Student ID:xweng

	first_attempt
					2015-11-06 00:01:52
	part1_correct_attempt
					['0:00:00', u'0.5']
	part2_incorrect_attempt
					('0:00:27', u'0.5')
	part2_correct_attempt
					['0:00:49', u'0.25']

72 Student ID:v4sharma

	first_attempt
					2015-11-04 02:39:57
	part1_correct_attempt
					['0:00:00', u'0.5']
	part2_incorrect_attempt
					('0:00:12', u'0.5')
					('0:02:17', u'0.5/0.25')
	part2_correct_attempt
					['1 day, 19:12:12', u'0.25']

73 Student ID:k4ma

	first_attempt
					2015-11-06 21:00:56
	part1_correct_attempt
					['0:00:00', u'.5']
	part2_incorrect_attempt
					('0:02:57', u'.5')
	part2_correct_attempt
					['0:06:42', u'.5(1-.5)']

74 Student ID:hmshah

	first_attempt
					2015-11-05 09:34:38
	part1_correct_attempt
					['0:00:00', u'.5']
	part2_incorrect_attempt
					('0:00:11', u'.5')
					('18:46:11', u'(.5 - .5)^2')
	part2_correct_attempt
					['18:46:22', u'(0 - .5)^2']

75 Student ID:ajvanega

	first_attempt
					2015-11-05 02:30:18
	part1_correct_attempt
					['0:00:00', u'.5']
	part2_incorrect_attempt
					('16:02:11', u'.5')
	part2_correct_attempt
					['16:20:04', u'1/4']

76 Student ID:tpmach

	first_attempt
					2015-10-30 21:47:51
	part1_correct_attempt
					['0:00:00', u'0.5']
	part2_incorrect_attempt
					('4 days, 2:19:18', u'0.5')
	part2_correct_attempt
					['5 days, 1:01:26', u'0.5^2']

77 Student ID:small

	first_attempt
					2015-11-05 23:36:40
	part1_correct_attempt
					['0:00:00', u'0.5']
	part2_incorrect_attempt
					('3:09:02', u'0.025')
	part2_correct_attempt
					['3:12:00', u'0.25']

78 Student ID:hmnaing

	first_attempt
					2015-11-04 19:10:30
	part1_correct_attempt
					['0:00:00', u'0.5*1']
	part2_incorrect_attempt
					('0:02:28', u'(0.5^2)-(0.5)^2')
					('0:04:25', u'(0.5^2)-(0.5)^2')
	part2_correct_attempt
					['0:08:10', u'(0.5)-(0.5)^2']

79 Student ID:haliew

	first_attempt
					2015-11-06 22:53:03
	part1_correct_attempt
					['0:00:00', u'.5']
	part2_incorrect_attempt
					('0:01:56', u'.25/100')
					('0:09:39', u'.5^2(100)')
	part2_correct_attempt
					['0:10:19', u'.25']

80 Student ID:j2phung

	first_attempt
					2015-11-03 22:43:26
	part1_correct_attempt
					['0:00:00', u'0.5']
	part2_incorrect_attempt
					('0:00:37', u'0.5')
	part2_correct_attempt
					['0:04:47', u'1/(2^(2))']

81 Student ID:wmiao

	first_attempt
					2015-11-04 20:14:51
	part1_correct_attempt
					['0:00:00', u'0.5']
	part2_incorrect_attempt
					('0:00:00', u'0.5')
	part2_correct_attempt
					['0:00:25', u'0.5*(1-0.5)']

82 Student ID:kosung

	first_attempt
					2015-11-05 08:26:55
	part1_correct_attempt
					['0:00:00', u'0.5']
	part2_incorrect_attempt
					('0:00:00', u'0.5')
					('0:14:48', u'0.5')
	part2_correct_attempt
					['0:15:33', u'0.25']

83 Student ID:jhp077

	first_attempt
					2015-11-05 13:06:29
	part1_correct_attempt
					['0:00:00', u'0.5']
	part2_incorrect_attempt
					('0:01:26', u'0.5')
	part2_correct_attempt
					['0:03:24', u'0.25']

84 Student ID:b1yao

	first_attempt
					2015-11-03 07:08:58
	part1_correct_attempt
					['0:00:00', u'0.5']
	part2_incorrect_attempt
					('0:01:28', u'0.5')
	part2_correct_attempt
					['0:02:32', u'0.25']












## Part 3

### (104) Mistake Group Fraction of size 104




### (18) Mistake Group Digits of size 18




### (6) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:dlt009

	first_attempt
					2015-11-05 07:36:02
	part3_incorrect_attempt
					('-1 day, 23:59:35', u'(1/0.5)-(3/0.5)')
					('0:01:29', u'0.5-(0.5+2*0.5)')
	part3_correct_attempt
					['0:13:59', u'0']

1 Student ID:aurodrig

	first_attempt
					2015-11-06 22:25:33
	part3_incorrect_attempt
					('0:06:25', u'-2')
	part3_correct_attempt
					['0:06:33', u'0']

2 Student ID:gsrandha

	first_attempt
					2015-11-05 07:24:37
	part3_incorrect_attempt
					('0:31:43', u'.5-1.5')
	part3_correct_attempt
					['0:33:40', u'0']

3 Student ID:hkhodada

	first_attempt
					2015-10-31 15:40:08
	part3_incorrect_attempt
					('0:10:25', u'-1')
	part3_correct_attempt
					['2 days, 8:48:22', u'0']

4 Student ID:ajabasa

	first_attempt
					2015-11-05 09:04:18
	part3_incorrect_attempt
					('0:09:20', u'.5-(1.5)')
	part3_correct_attempt
					['0:12:57', u'0']

5 Student ID:abjara

	first_attempt
					2015-11-04 01:27:47
	part3_incorrect_attempt
					('0:07:46', u'-1')
	part3_correct_attempt
					['0:14:27', u'0']












## Part 4

### (162) Mistake Group Digits of size 162




### (23) Mistake Group Wrong_Sign of size 23




### (19) Mistake Group ['R.0'] of size 19
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|1/2	|1/16	|[('R.0', 1.0, u'1', u'1')]	|
|1	|1/2	|1-0.1875	|[('R.0', 1.0, u'1', u'1')]	|
|2	|1/2	|1/8	|[('R.0', 1.0, u'1', u'1')]	|
|3	|1/2	|1/3	|[('R.0', 1.0, u'1', u'1')]	|
|4	|1/2	|1/4	|[('R.0', 1.0, u'1', u'1')]	|
|5	|1/2	|1/6	|[('R.0', 1.0, u'1', u'1')]	|
|6	|1/2	|1/100	|[('R.0', 1.0, u'1', u'1')]	|




### (6) Mistake Group ['R.1'] of size 6
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|1/2	|(0.5 ^2 + 0.5 ^ 2 )/ 2	|[('R.1', 2.0, u'2', u'2')]	|
|1	|1/2	|.25/2	|[('R.1', 2.0, u'2', u'2')]	|
|2	|1/2	|(-0.5 - 0)^2	|[('R.1', 2.0, u'2', u'2')]	|
|3	|1/2	|[0.5^2+0.5^2]/2	|[('R.1', 2.0, u'2', u'2')]	|
|4	|1/2	|(0.5)^2	|[('R.1', 2.0, u'2', u'2')]	|
|5	|1/2	|.5*.5/2	|[('R.1', 2.0, u'2', u'2')]	|




### (3) Mistake Group redirect of size 3




### (50) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:druble

	first_attempt
					2015-11-04 05:09:50
	part2_correct_attempt
					['0:00:00', u'0.5 * (1 - 0.5)']
	part4_incorrect_attempt
					('0:03:37', u'0.25 - 0.25')
	part4_correct_attempt
					['0:07:40', u'0.25 + 0.25']

1 Student ID:dlgoldbe

	first_attempt
					2015-11-05 05:38:38
	part2_correct_attempt
					['0:01:05', u'0.5*(1-0.5)']
	part4_incorrect_attempt
					('0:21:14', u'(0.25)+((-1^2)*0.25)')
	part4_correct_attempt
					['0:21:47', u'(0.25)-((-1^2)*0.25)']

2 Student ID:lpettit

	first_attempt
					2015-11-06 23:23:57
	part2_correct_attempt
					['0:11:02', u'(2*.5*.5)/2']
	part4_incorrect_attempt
					('0:12:24', u'1/2 + 1/2')
	part4_correct_attempt
					['0:12:39', u'1/2']

3 Student ID:yypan

	first_attempt
					2015-11-03 00:09:22
	part2_correct_attempt
					['0:02:28', u'0.5-0.5^2']
	part4_incorrect_attempt
					('0:05:15', u'(0.5-0.5^2)-(0.5-0.5^2)')
					('0:05:59', u'(0.5-0.5^2)-(0.5-0.5^2)^2')
	part4_correct_attempt
					['0:07:14', u'0.5-0.5^2+0.5-0.5^2']

4 Student ID:kbielawi

	first_attempt
					2015-11-03 20:55:13
	part2_correct_attempt
					['23:11:51', u'.25']
	part4_incorrect_attempt
					('23:24:16', u'0.125')
					('23:24:40', u'0.25')
					('23:34:38', u'0.1')
	part4_correct_attempt
					['2 days, 0:16:12', u'0.5']

5 Student ID:glcohen

	first_attempt
					2015-11-03 16:48:17
	part2_correct_attempt
					['0:05:58', u'0.25']
	part4_incorrect_attempt
					('0:07:15', u'0.25')
					('3:56:29', u'0.1875')
	part4_correct_attempt
					['3:57:57', u'0.5']

6 Student ID:fichoi

	first_attempt
					2015-11-04 04:32:30
	part2_correct_attempt
					['0:00:00', u'0.25']
	part4_incorrect_attempt
					('0:04:46', u'4.5')
					('0:05:23', u'2.5')
	part4_correct_attempt
					['0:14:06', u'0.5']

7 Student ID:atorr

	first_attempt
					2015-11-05 19:48:49
	part2_correct_attempt
					['0:01:37', u'0.25']
	part4_incorrect_attempt
					('0:02:35', u'0.25')
	part4_correct_attempt
					['0:03:16', u'0.5']

8 Student ID:spw006

	first_attempt
					2015-11-04 00:39:13
	part2_correct_attempt
					['2:16:55', u'0.5 - 0.25']
	part4_incorrect_attempt
					('2:22:32', u'0.25')
	part4_correct_attempt
					['3:08:40', u'0.5']

9 Student ID:any027

	first_attempt
					2015-11-01 20:11:07
	part2_correct_attempt
					['0:01:59', u'(0.5 ^2 + 0.5 ^ 2 )/ 2']
	part4_incorrect_attempt
					('0:10:36', u'((0.5 ^2 + 0.5 ^ 2 )/ 2) - ((0.5 ^2 + 0.5 ^ 2 )/ 2)')
					('0:12:18', u'((0.5 ^2 + 0.5 ^ 2 )/ 4 ) - ((0.5 ^2 + 0.5 ^ 2 )/ 4)')
	part4_correct_attempt
					['0:13:41', u'0.5']

10 Student ID:rwthomps

	first_attempt
					2015-11-06 18:18:48
	part2_correct_attempt
					['0:00:00', u'0.5 * 0.5']
	part4_incorrect_attempt
					('3:01:11', u'(1 - 0.5)/0.5^2 + (-1)^2 * (1 - (1 - 0.5)^(2 - 1) * 0.5)/0.5^2')
					('3:01:59', u'0.5 + 2 * 0.5 * 0.5')
					('3:03:46', u'0.5 * 0.5 + 2 * 0.5 * 0.5')
	part4_correct_attempt
					['3:10:48', u'0.5']

11 Student ID:mhale

	first_attempt
					2015-11-05 20:08:27
	part2_correct_attempt
					['0:02:42', u'0.25']
	part4_incorrect_attempt
					('0:04:13', u'0.25')
	part4_correct_attempt
					['0:05:38', u'0.5']

12 Student ID:awollner

	first_attempt
					2015-11-06 22:55:15
	part2_correct_attempt
					['0:12:45', u'.25']
	part4_incorrect_attempt
					('0:18:19', u'.25')
	part4_correct_attempt
					['0:21:00', u'.5']

13 Student ID:kthui

	first_attempt
					2015-11-06 02:15:58
	part2_correct_attempt
					['0:08:27', u'0.25']
	part4_incorrect_attempt
					('5:14:09', u'0.25')
	part4_correct_attempt
					['5:14:15', u'0.5']

14 Student ID:jcj006

	first_attempt
					2015-11-04 05:17:58
	part2_correct_attempt
					['0:06:28', u'.25']
	part4_incorrect_attempt
					('0:12:29', u'1.25')
					('0:13:41', u'0.75')
	part4_correct_attempt
					['0:14:04', u'.5']

15 Student ID:hachrist

	first_attempt
					2015-11-03 20:13:34
	part2_correct_attempt
					['0:23:34', u'0.5 - 0.5^2']
	part4_incorrect_attempt
					('0:24:12', u'0 ')
					('0:31:37', u'0.25')
	part4_correct_attempt
					['0:31:42', u'0.5']

16 Student ID:abasu

	first_attempt
					2015-11-05 02:12:18
	part2_correct_attempt
					['0:02:15', u'0.25']
	part4_incorrect_attempt
					('0:03:27', u'0.25')
	part4_correct_attempt
					['0:16:43', u'0.5']

17 Student ID:tpmach

	first_attempt
					2015-10-30 21:47:51
	part2_correct_attempt
					['5 days, 1:01:26', u'0.5^2']
	part4_incorrect_attempt
					('5 days, 1:05:32', u'0.25')
					('5 days, 1:06:21', u'0.25+(-1)^2*(0.5)')
	part4_correct_attempt
					['5 days, 1:06:39', u'0.25+(-1)^2*(0.25)']

18 Student ID:haw081

	first_attempt
					2015-11-01 05:01:44
	part2_correct_attempt
					['0:00:36', u'1(0.5)(0.5)']
	part4_incorrect_attempt
					('0:02:14', u'0.025-0.025')
					('0:02:34', u'0.025+0.025')
	part4_correct_attempt
					['0:03:00', u'2(0.5)(0.5)']

19 Student ID:vqt004

	first_attempt
					2015-11-04 07:33:15
	part2_correct_attempt
					['0:00:00', u'0.25']
	part4_incorrect_attempt
					('0:00:43', u'0.25')
	part4_correct_attempt
					['19:53:26', u'0.5']

20 Student ID:acvuong

	first_attempt
					2015-11-05 00:14:39
	part2_correct_attempt
					['0:00:00', u'0.5^2']
	part4_incorrect_attempt
					('0:02:35', u'0.5^2 - 0.25*0.5')
	part4_correct_attempt
					['0:15:39', u'2*0.5^2']

21 Student ID:xil109

	first_attempt
					2015-11-05 03:20:50
	part2_correct_attempt
					['0:09:21', u'0.5-0.5^2']
	part4_incorrect_attempt
					('0:26:32', u'3/4')
	part4_correct_attempt
					['0:27:47', u'1/2']

22 Student ID:rlhagen

	first_attempt
					2015-10-31 17:11:50
	part2_correct_attempt
					['0:07:54', u'0.5/2']
	part4_incorrect_attempt
					('0:10:48', u'(-1/2)+1/2')
	part4_correct_attempt
					['0:12:19', u'(0/2)+1/2']

23 Student ID:agarango

	first_attempt
					2015-11-05 23:41:15
	part2_correct_attempt
					['0:10:00', u'0.25']
	part4_incorrect_attempt
					('0:10:25', u'0.25')
	part4_correct_attempt
					['0:19:00', u'0.25+0.25']

24 Student ID:nnh002

	first_attempt
					2015-11-05 03:58:12
	part2_correct_attempt
					['0:00:20', u'(1-0.5)^2*0.5+(0-0.5)^2*0.5']
	part4_incorrect_attempt
					('0:27:02', u'2*(1-0.5)^2*0.5+(0-0.5)^2*0.5')
					('0:27:55', u'(-1-0.5)^2*0.5+(0-0.5)^2*0.5')
	part4_correct_attempt
					['0:28:54', u'(1-0.5)^2*0.5+(0-0.5)^2*0.5+(1-0.5)^2*0.5+(0-0.5)^2*0.5']

25 Student ID:ctgraves

	first_attempt
					2015-11-03 05:16:32
	part2_correct_attempt
					['0:00:34', u'0.25']
	part4_incorrect_attempt
					('0:02:06', u'0.25')
	part4_correct_attempt
					['0:02:12', u'0.5']

26 Student ID:rraiyyan

	first_attempt
					2015-11-06 21:18:14
	part2_correct_attempt
					['0:00:26', u'0.25']
	part4_incorrect_attempt
					('0:01:28', u'0.25')
	part4_correct_attempt
					['0:01:52', u'0.5']

27 Student ID:dcrume

	first_attempt
					2015-11-06 19:09:00
	part2_correct_attempt
					['0:30:54', u'.5*.5/1']
	part4_incorrect_attempt
					('0:37:04', u'.5*(1-.5)/1 - .5*(1-.5)/2')
					('0:37:49', u'.5*(1-.5)/2 - .5*(1-.5)/2')
	part4_correct_attempt
					['0:48:43', u'.5*.5/1 + .5*.5/1']

28 Student ID:hmshah

	first_attempt
					2015-11-05 09:34:38
	part2_correct_attempt
					['18:46:22', u'(0 - .5)^2']
	part4_incorrect_attempt
					('18:47:16', u'(0 - .5)^2 - (0 - .5)^2')
	part4_correct_attempt
					['18:48:14', u'(0 - .5)^2 + (0 - .5)^2']

29 Student ID:yeh013

	first_attempt
					2015-11-04 07:18:53
	part2_correct_attempt
					['0:00:00', u'0.25']
	part4_incorrect_attempt
					('0:02:42', u'0.25')
	part4_correct_attempt
					['0:02:57', u'0.5']

30 Student ID:cprafull

	first_attempt
					2015-11-05 05:19:43
	part2_correct_attempt
					['0:05:12', u'0.5 - (0.5^2)']
	part4_incorrect_attempt
					('0:34:08', u'0.25')
	part4_correct_attempt
					['3:20:47', u'0.5']

31 Student ID:djk006

	first_attempt
					2015-11-03 22:37:00
	part2_correct_attempt
					['0:00:00', u'.25']
	part4_incorrect_attempt
					('0:01:00', u'.25')
					('0:02:42', u'.1')
					('0:03:10', u'.5/4')
					('0:30:58', u'5/4')
					('0:31:07', u'.5/4')
					('0:39:36', u'.5/3')
	part4_correct_attempt
					['1:37:07', u'.5']

32 Student ID:mcatozzi

	first_attempt
					2015-11-03 19:16:19
	part2_correct_attempt
					['0:03:48', u'.5^2']
	part4_incorrect_attempt
					('0:05:27', u'.25')
	part4_correct_attempt
					['0:05:31', u'.5']

33 Student ID:chc286

	first_attempt
					2015-11-01 01:22:52
	part2_correct_attempt
					['0:01:49', u'0.5*(1-0.5)^2+0.5*(0-0.5)^2']
	part4_incorrect_attempt
					('0:03:58', u'0.25-0.25')
	part4_correct_attempt
					['0:04:21', u'0.25+0.25']

34 Student ID:w4shin

	first_attempt
					2015-11-06 22:40:03
	part2_correct_attempt
					['0:10:20', u'0.25']
	part4_incorrect_attempt
					('0:10:20', u'0.25')
	part4_correct_attempt
					['0:19:00', u'0.5']

35 Student ID:etemlock

	first_attempt
					2015-11-03 21:40:24
	part2_correct_attempt
					['0:00:00', u'0.25']
	part4_incorrect_attempt
					('2:30:10', u'1/2 - 1/8')
					('2:40:57', u'1/4 - 1/16')
					('2:41:07', u'1/4 - 1/8')
					('2:41:15', u'1/4 - 1/4')
	part4_correct_attempt
					['2 days, 2:55:17', u'1/2']

36 Student ID:acs008

	first_attempt
					2015-11-04 05:07:00
	part2_correct_attempt
					['0:00:48', u'0.5^2']
	part4_incorrect_attempt
					('0:04:25', u'0.25')
					('0:05:02', u'0.15')
	part4_correct_attempt
					['0:08:25', u'0.5^2*2']

37 Student ID:ppanourg

	first_attempt
					2015-11-06 08:24:25
	part2_correct_attempt
					['0:09:48', u'.25']
	part4_incorrect_attempt
					('0:14:14', u'.25')
	part4_correct_attempt
					['0:16:53', u'.5']

38 Student ID:lahawkin

	first_attempt
					2015-11-05 18:50:24
	part2_correct_attempt
					['0:35:41', u'(.5*.5)']
	part4_incorrect_attempt
					('0:36:14', u'(.25)+(0)')
	part4_correct_attempt
					['0:36:23', u'(.25)+(.25)']

39 Student ID:edcole

	first_attempt
					2015-11-06 23:12:52
	part2_correct_attempt
					['0:00:00', u'.25']
	part4_incorrect_attempt
					('0:00:46', u'.25')
	part4_correct_attempt
					['0:01:23', u'.5']

40 Student ID:vasharma

	first_attempt
					2015-11-04 18:46:00
	part2_correct_attempt
					['0:00:50', u'.5*.5']
	part4_incorrect_attempt
					('0:01:31', u'.5+.5')
	part4_correct_attempt
					['0:13:05', u'(.5*.5)+(.5*.5)']

41 Student ID:bkoli

	first_attempt
					2015-11-05 21:23:15
	part2_correct_attempt
					['0:15:06', u'0.5(0.5)']
	part4_incorrect_attempt
					('0:21:42', u'(0.5(0.5))-(0.5(0.5))')
	part4_correct_attempt
					['0:25:35', u'(0.5(0.5))+(0.5(0.5))']

42 Student ID:c3chung

	first_attempt
					2015-11-06 10:47:12
	part2_correct_attempt
					['0:01:11', u'0.25']
	part4_incorrect_attempt
					('0:02:05', u'0.25')
	part4_correct_attempt
					['0:02:28', u'0.5']

43 Student ID:k4ma

	first_attempt
					2015-11-06 21:00:56
	part2_correct_attempt
					['0:06:42', u'.5(1-.5)']
	part4_incorrect_attempt
					('0:13:35', u'.5(1-.5)+[(-1^2)*.25]')
	part4_correct_attempt
					['0:20:33', u'.5(1-.5)-[(-1^2)*.25]']

44 Student ID:v3doan

	first_attempt
					2015-11-07 00:21:47
	part2_correct_attempt
					['0:00:05', u'.25']
	part4_incorrect_attempt
					('0:00:28', u'.25')
	part4_correct_attempt
					['0:02:04', u'.5']

45 Student ID:cagatep

	first_attempt
					2015-11-05 06:53:46
	part2_correct_attempt
					['0:01:45', u'.25']
	part4_incorrect_attempt
					('0:02:01', u'.25')
					('0:03:10', u'.5/4')
					('0:03:52', u'(.5^2 + 1.5^2)/4')
	part4_correct_attempt
					['0:04:32', u'.5']

46 Student ID:m8woo

	first_attempt
					2015-11-05 20:48:48
	part2_correct_attempt
					['0:00:00', u'0.25']
	part4_incorrect_attempt
					('0:01:30', u'0.25')
	part4_correct_attempt
					['0:01:38', u'0.5']

47 Student ID:tjke

	first_attempt
					2015-11-04 20:53:53
	part2_correct_attempt
					['0:00:48', u'0.5*1^2 - 0.5^2']
	part4_incorrect_attempt
					('0:02:10', u'0.5*1^2 - 0.5^2 - [0.5*0^2 - 0^2]')
					('0:03:14', u'0.5*1^2 - 0.5^2 - [0.5*1^2 - 0.5^2]')
	part4_correct_attempt
					['0:05:20', u'0.5*1^2 - 0.5^2 + [0.5*(-1)^2 - (0.5*-1)^2]']

48 Student ID:kgrozav

	first_attempt
					2015-11-05 07:35:53
	part2_correct_attempt
					['0:07:12', u'0.25']
	part4_incorrect_attempt
					('11:42:55', u'2.5')
					('11:47:02', u'0.25')
					('11:56:38', u'0.25')
	part4_correct_attempt
					['12:09:00', u'0.5']

49 Student ID:j2phung

	first_attempt
					2015-11-03 22:43:26
	part2_correct_attempt
					['0:04:47', u'1/(2^(2))']
	part4_incorrect_attempt
					('1 day, 9:30:16', u'.25')
	part4_correct_attempt
					['1 day, 9:42:43', u'1/2']












## Part 5

### (30) Mistake Group Fraction of size 30




### (10) Mistake Group Digits of size 10




### (8) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:dlt009

	first_attempt
					2015-11-05 07:36:02
	part5_incorrect_attempt
					('-1 day, 23:59:35', u'(1/0.5)-2*(3/0.5)+(6/0.5)')
	part5_correct_attempt
					['0:02:20', u'(0.5)-2*(1)+(1.5)']

1 Student ID:j6quach

	first_attempt
					2015-11-05 11:32:25
	part5_incorrect_attempt
					('0:11:32', u'1/2 -1 + 3/2')
	part5_correct_attempt
					['1:57:48', u'0']

2 Student ID:gsrandha

	first_attempt
					2015-11-05 07:24:37
	part5_incorrect_attempt
					('0:34:28', u'4 * .5')
	part5_correct_attempt
					['0:34:44', u'0']

3 Student ID:haw081

	first_attempt
					2015-11-01 05:01:44
	part5_incorrect_attempt
					('0:14:48', u'0.5-05*2+0.5')
	part5_correct_attempt
					['0:14:59', u'0.5-0.5*2+0.5']

4 Student ID:z3meng

	first_attempt
					2015-11-05 07:50:27
	part5_incorrect_attempt
					('0:00:00', u'-1')
	part5_correct_attempt
					['0:05:24', u'0']

5 Student ID:vasharma

	first_attempt
					2015-11-04 18:46:00
	part5_incorrect_attempt
					('0:02:43', u'.5+2*.5+.5')
	part5_correct_attempt
					['0:02:53', u'.5-2*.5+.5']

6 Student ID:ajabasa

	first_attempt
					2015-11-05 09:04:18
	part5_incorrect_attempt
					('8:59:35', u'.5-2*.5+1.5')
					('9:00:37', u'.5-2*.5+(.5+.5+3*.5)')
	part5_correct_attempt
					['9:03:37', u'.5-2*.5+(.5)']

7 Student ID:bakang

	first_attempt
					2015-11-05 08:35:46
	part5_incorrect_attempt
					('0:03:59', u'-1')
	part5_correct_attempt
					['0:04:18', u'0']












## Part 6

### (126) Mistake Group Digits of size 126




### (68) Mistake Group Wrong_Sign of size 68




### (11) Mistake Group ['R.1'] of size 11
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|6/4	|0.25*4	|[('R.1', 4.0, u'4', u'4')]	|
|1	|6/4	|3/4	|[('R.1', 4.0, u'4', u'4')]	|
|2	|6/4	|9/4	|[('R.1', 4.0, u'4', u'4')]	|
|3	|6/4	|1/4	|[('R.1', 4.0, u'4', u'4')]	|
|4	|6/4	|2/4	|[('R.1', 4.0, u'4', u'4')]	|
|5	|6/4	|5/4	|[('R.1', 4.0, u'4', u'4')]	|




### (7) Mistake Group redirect of size 7




### (92) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:gthorn

	first_attempt
					2015-11-02 07:26:59
	part5_correct_attempt
					['1 day, 12:33:11', u'0']
	part6_incorrect_attempt
					('1 day, 12:34:50', u'0.25')
	part6_correct_attempt
					['1 day, 12:36:16', u'1.5']

1 Student ID:apokhare

	first_attempt
					2015-11-05 21:35:02
	part5_correct_attempt
					['0:01:24', u'0']
	part6_incorrect_attempt
					('0:01:24', u'0.15')
	part6_correct_attempt
					['0:01:48', u'1.5']

2 Student ID:kbielawi

	first_attempt
					2015-11-03 20:55:13
	part5_correct_attempt
					['23:30:29', u'0']
	part6_incorrect_attempt
					('2 days, 0:19:32', u'3.5')
	part6_correct_attempt
					['2 days, 0:23:00', u'1.5']

3 Student ID:haw081

	first_attempt
					2015-11-01 05:01:44
	part5_correct_attempt
					['0:14:59', u'0.5-0.5*2+0.5']
	part6_incorrect_attempt
					('0:15:49', u'0.5+4*0.5+0.5')
					('0:16:21', u'0.5-4*0.5+3*0.5')
					('2:41:23', u'0.25-2*0.25+0.25')
	part6_correct_attempt
					['2:41:37', u'0.25+4*0.25+0.25']

4 Student ID:r9jiang

	first_attempt
					2015-11-02 02:16:42
	part5_correct_attempt
					['0:00:00', u'0']
	part6_incorrect_attempt
					('0:02:32', u'0.5')
	part6_correct_attempt
					['0:03:34', u'1.5']

5 Student ID:rlhagen

	first_attempt
					2015-10-31 17:11:50
	part5_correct_attempt
					['0:42:12', u'(0+1-2-1+1+2-1+0)/8']
	part6_incorrect_attempt
					('0:48:08', u'35/12+2')
					('1:01:17', u'0.5')
	part6_correct_attempt
					['1:37:47', u'6/4']

6 Student ID:btn023

	first_attempt
					2015-11-06 10:42:56
	part5_correct_attempt
					['0:04:10', u'.5-2*.5+.5']
	part6_incorrect_attempt
					('0:04:10', u'4*2*.5*(1-.5)^2')
	part6_correct_attempt
					['0:05:17', u'2*2*.5*(1-.5)^2+4*2*.5*(1-.5)^2']

7 Student ID:tcn013

	first_attempt
					2015-11-04 02:11:53
	part5_correct_attempt
					['0:03:08', u'0']
	part6_incorrect_attempt
					('0:04:06', u'.75')
					('0:05:48', u'2.5')
	part6_correct_attempt
					['0:10:51', u'1.5']

8 Student ID:tstevens

	first_attempt
					2015-11-06 11:34:10
	part5_correct_attempt
					['0:02:35', u'0']
	part6_incorrect_attempt
					('0:07:55', u'.5')
					('0:13:22', u'.25')
					('0:13:29', u'.75')
					('0:16:53', u'.75')
					('0:16:59', u'4/3')
					('0:17:06', u'2/3')
	part6_correct_attempt
					['0:18:11', u'1.5']

9 Student ID:l8ngo

	first_attempt
					2015-10-30 16:12:29
	part5_correct_attempt
					['4 days, 8:42:33', u'1/2-2*1/2+1/2']
	part6_incorrect_attempt
					('4 days, 8:43:37', u'[1/2 - 1/4]+2*[1/2-1/4]+[1/2-1/4]')
	part6_correct_attempt
					['4 days, 8:45:25', u'[1/2 - 1/4]+4*[1/2-1/4]+[1/2-1/4]']

10 Student ID:dando

	first_attempt
					2015-11-03 20:18:15
	part5_correct_attempt
					['0:00:00', u'0']
	part6_incorrect_attempt
					('0:01:58', u'2.5')
	part6_correct_attempt
					['0:02:40', u'1.5']

11 Student ID:abasu

	first_attempt
					2015-11-05 02:12:18
	part5_correct_attempt
					['0:11:13', u'0']
	part6_incorrect_attempt
					('0:16:59', u'0.75')
	part6_correct_attempt
					['0:37:20', u'1.5']

12 Student ID:sayao

	first_attempt
					2015-11-04 01:24:54
	part5_correct_attempt
					['0:03:35', u'0']
	part6_incorrect_attempt
					('0:07:49', u'.25*.25 ')
					('0:08:06', u'4*.25')
					('0:08:32', u'.25+1')
	part6_correct_attempt
					['0:08:37', u'1.5']

13 Student ID:ksrijong

	first_attempt
					2015-11-04 22:50:25
	part5_correct_attempt
					['0:03:10', u'0']
	part6_incorrect_attempt
					('0:08:08', u'3*(0.5^2)')
					('0:09:02', u'0.5^2')
					('0:14:13', u'4*(0.5)^2')
	part6_correct_attempt
					['0:15:02', u'(0.5)^2+(0.5)^2 + 1']

14 Student ID:acvuong

	first_attempt
					2015-11-05 00:14:39
	part5_correct_attempt
					['0:15:39', u'0']
	part6_incorrect_attempt
					('0:15:39', u'7*(.5^2)')
	part6_correct_attempt
					['0:16:01', u'6*(.5^2)']

15 Student ID:flhernan

	first_attempt
					2015-11-03 19:16:30
	part5_correct_attempt
					['0:04:56', u'0']
	part6_incorrect_attempt
					('0:05:40', u'.5^2 + 2^2*.5 + .5^2')
	part6_correct_attempt
					['0:06:01', u'.5^2 + 2^2*.5^2 + .5^2']

16 Student ID:mitopete

	first_attempt
					2015-11-04 04:43:38
	part5_correct_attempt
					['0:03:35', u'0']
	part6_incorrect_attempt
					('0:03:35', u'(1/2)^2 + (1/2)^2')
	part6_correct_attempt
					['0:04:59', u'(1/2)^2 + 2^2(1/2)^2 + (1/2)^2']

17 Student ID:yos017

	first_attempt
					2015-11-06 06:07:41
	part5_correct_attempt
					['2:01:50', u'0']
	part6_incorrect_attempt
					('2:02:45', u'4*[0.5 - (0.5)^2]')
	part6_correct_attempt
					['2:03:21', u'6*[0.5 - (0.5)^2]']

18 Student ID:m8woo

	first_attempt
					2015-11-05 20:48:48
	part5_correct_attempt
					['0:09:00', u'0']
	part6_incorrect_attempt
					('0:09:09', u'0.5')
	part6_correct_attempt
					['0:09:22', u'1.5']

19 Student ID:ggaddi

	first_attempt
					2015-11-01 20:47:48
	part5_correct_attempt
					['0:11:45', u'0']
	part6_incorrect_attempt
					('0:13:08', u'0.75')
					('0:14:36', u'0.25*3')
	part6_correct_attempt
					['0:26:10', u'0.25*6']

20 Student ID:jit002

	first_attempt
					2015-11-05 01:51:15
	part5_correct_attempt
					['0:00:00', u'0']
	part6_incorrect_attempt
					('0:09:23', u'0.5')
	part6_correct_attempt
					['0:12:16', u'1.5']

21 Student ID:druble

	first_attempt
					2015-11-04 05:09:50
	part5_correct_attempt
					['0:03:37', u'0.5 - 2*0.5 + 0.5']
	part6_incorrect_attempt
					('0:04:56', u'-1*(0.25 - 2^2*0.25 + 0.25)')
	part6_correct_attempt
					['0:07:40', u'0.25 + 2^2*0.25 + 0.25']

22 Student ID:b3hwang

	first_attempt
					2015-11-05 08:38:09
	part5_correct_attempt
					['0:01:31', u'.5-1+.5']
	part6_incorrect_attempt
					('0:05:58', u'(.5^2) + 2^2 + (.5)^2')
	part6_correct_attempt
					['0:08:18', u'((.5^2) + 2^2 + (.5)^2)/3']

23 Student ID:jag028

	first_attempt
					2015-11-02 22:21:20
	part5_correct_attempt
					['0:12:18', u'.5-2(.5)+.5']
	part6_incorrect_attempt
					('0:13:17', u'1^2(.5)')
					('0:13:26', u'(.5)')
	part6_correct_attempt
					['0:19:12', u'(.5)^2+(-2)^2(.5)^2+(.5)^2']

24 Student ID:lguintu

	first_attempt
					2015-11-03 04:17:57
	part5_correct_attempt
					['0:01:03', u'0']
	part6_incorrect_attempt
					('0:01:29', u'1/4+2/4+1/4')
					('0:01:39', u'1/4-2/4+1/4')
	part6_correct_attempt
					['0:02:00', u'1/4+2^2/4+1/4']

25 Student ID:abjara

	first_attempt
					2015-11-04 01:27:47
	part5_correct_attempt
					['0:20:58', u'0']
	part6_incorrect_attempt
					('0:20:58', u'9*.5')
					('0:22:18', u'.5')
					('0:22:36', u'4*.5')
					('0:24:00', u'.5')
					('0:24:10', u'.25')
					('0:24:18', u'.75')
					('0:29:26', u'.25/3')
					('0:29:31', u'.25/2')
	part6_correct_attempt
					['0:33:28', u'1.5']

26 Student ID:krau

	first_attempt
					2015-11-04 19:46:04
	part5_correct_attempt
					['0:00:40', u'0']
	part6_incorrect_attempt
					('0:06:44', u'.75')
	part6_correct_attempt
					['0:07:25', u'.25 + .25 + 4*.25']

27 Student ID:crmirand

	first_attempt
					2015-11-03 05:16:13
	part5_correct_attempt
					['0:03:14', u'0']
	part6_incorrect_attempt
					('0:03:32', u'.5')
					('0:04:34', u'.5')
	part6_correct_attempt
					['0:05:06', u'1.5']

28 Student ID:beyounge

	first_attempt
					2015-10-30 05:23:18
	part5_correct_attempt
					['0:00:00', u'0']
	part6_incorrect_attempt
					('0:21:20', u'0.5')
					('0:23:28', u'0.5^2')
	part6_correct_attempt
					['0:26:50', u'1.50']

29 Student ID:hak014

	first_attempt
					2015-11-04 23:48:14
	part5_correct_attempt
					['0:11:31', u'0']
	part6_incorrect_attempt
					('0:12:57', u'9*0.25')
					('0:13:04', u'4*0.25')
					('0:13:10', u'1*0.25')
					('0:13:16', u'0*0.25')

30 Student ID:atorr

	first_attempt
					2015-11-05 19:48:49
	part5_correct_attempt
					['0:04:43', u'0']
	part6_incorrect_attempt
					('0:05:36', u'0.75')
					('0:06:10', u'0.5')
					('0:15:27', u'0.5')
					('1:01:36', u'0.25 + 2 * 0.25  + 0.25')
	part6_correct_attempt
					['1:03:32', u'0.25 + 4 * 0.25 + 0.25']

31 Student ID:rraiyyan

	first_attempt
					2015-11-06 21:18:14
	part5_correct_attempt
					['0:55:22', u'0']
	part6_incorrect_attempt
					('0:55:29', u'0.5')
					('0:55:54', u'0.75')
					('1:01:14', u'0.25-0.25+(3/8)^2')
					('1:04:17', u'(1^2)*(1/2)+(2^2)*(1/4)+(3^2)*(1/8)')
					('1:14:25', u'0.5')
					('1:16:06', u'0.25')
					('1:17:57', u'1.25')
					('1:23:47', u'1+4+9')
					('1:36:42', u'(1^2)*(1/2)-2*(2^2)*(1/4)+(4^2)*(1/8)')
					('1:39:59', u'4.5')
					('1:41:33', u'9*0.25')
	part6_correct_attempt
					['1:43:45', u'1.5']

32 Student ID:r1gu

	first_attempt
					2015-11-05 12:03:18
	part5_correct_attempt
					['-1 day, 23:58:36', u'0']
	part6_incorrect_attempt
					('-1 day, 23:58:36', u'35/3')
	part6_correct_attempt
					['0:01:43', u'0.25+1+0.25']

33 Student ID:dsmonaha

	first_attempt
					2015-11-02 16:47:16
	part5_correct_attempt
					['0:22:25', u'0']
	part6_incorrect_attempt
					('4 days, 4:17:15', u'1.25')
	part6_correct_attempt
					['4 days, 4:18:47', u'1.5']

34 Student ID:edescobe

	first_attempt
					2015-11-01 06:42:32
	part5_correct_attempt
					['0:08:50', u'0']
	part6_incorrect_attempt
					('0:09:34', u'.75')
	part6_correct_attempt
					['0:10:09', u'.25*6']

35 Student ID:w4shin

	first_attempt
					2015-11-06 22:40:03
	part5_correct_attempt
					['0:10:20', u'0']
	part6_incorrect_attempt
					('0:21:49', u'0.75')
					('0:34:12', u'0.25')
					('0:35:24', u'0.5')
	part6_correct_attempt
					['0:38:43', u'1.5']

36 Student ID:etemlock

	first_attempt
					2015-11-03 21:40:24
	part5_correct_attempt
					['2:28:06', u'-1/2 + 1/2']
	part6_incorrect_attempt
					('2 days, 2:56:09', u'2.5')
	part6_correct_attempt
					['2 days, 2:56:18', u'1.5']

37 Student ID:jtfrankl

	first_attempt
					2015-11-06 18:24:55
	part5_correct_attempt
					['0:04:44', u'0']
	part6_incorrect_attempt
					('0:04:44', u'.25')
	part6_correct_attempt
					['0:05:57', u'.25+1+.25']

38 Student ID:ralhadda

	first_attempt
					2015-10-31 20:03:47
	part5_correct_attempt
					['0:22:29', u'0']
	part6_incorrect_attempt
					('0:24:39', u'0-0')
					('0:26:27', u'-0')
					('0:26:44', u'0.5')
					('0:26:52', u'0.25')
					('4:28:35', u'0.5')
	part6_correct_attempt
					['4:57:20', u'1.5']

39 Student ID:yjshin

	first_attempt
					2015-11-06 22:57:48
	part5_correct_attempt
					['0:02:42', u'0']
	part6_incorrect_attempt
					('0:10:33', u'.5^2')
	part6_correct_attempt
					['0:13:18', u'.5^2+2^2*.5^2+.5^2']

40 Student ID:xil109

	first_attempt
					2015-11-05 03:20:50
	part5_correct_attempt
					['0:21:58', u'0']
	part6_incorrect_attempt
					('0:31:40', u'1/2')
	part6_correct_attempt
					['0:36:50', u'0.25+4*0.25+0.25']

41 Student ID:dac064

	first_attempt
					2015-11-05 08:56:16
	part5_correct_attempt
					['0:08:54', u'0']
	part6_incorrect_attempt
					('0:09:18', u'1/2')
	part6_correct_attempt
					['0:10:47', u'1.5']

42 Student ID:lpettit

	first_attempt
					2015-11-06 23:23:57
	part5_correct_attempt
					['0:02:21', u'0']
	part6_incorrect_attempt
					('0:17:05', u'2/3')
					('0:17:55', u'.75')
					('0:21:58', u'1/2')
					('0:22:15', u'1/3')
					('0:23:57', u'4/3')
	part6_correct_attempt
					['0:24:51', u'12/8']

43 Student ID:kebao

	first_attempt
					2015-11-05 21:26:19
	part5_correct_attempt
					['0:00:46', u'0']
	part6_incorrect_attempt
					('0:00:46', u'1/2')
	part6_correct_attempt
					['0:01:38', u'6/4']

44 Student ID:glcohen

	first_attempt
					2015-11-03 16:48:17
	part5_correct_attempt
					['0:00:42', u'0']
	part6_incorrect_attempt
					('0:07:15', u'0.25')
					('3:56:29', u'0.1875')
					('3:56:40', u'1-0.1875')
					('3:59:43', u'2.8888888888889')
	part6_correct_attempt
					['4:02:38', u'0.25+1+0.25']

45 Student ID:achava

	first_attempt
					2015-11-06 07:02:10
	part5_correct_attempt
					['0:16:03', u'0.5 - 1 + 0.5']
	part6_incorrect_attempt
					('0:17:37', u'4*0.5')
					('0:37:07', u'100*0.5(0.5)')
	part6_correct_attempt
					['0:40:31', u'0.25+((2^2)*0.25) + 0.25']

46 Student ID:d6he

	first_attempt
					2015-11-05 03:24:20
	part5_correct_attempt
					['3:07:14', u'0']
	part6_incorrect_attempt
					('3:07:14', u'1.25')
	part6_correct_attempt
					['3:09:19', u'0.5+4(0.25)']

47 Student ID:awollner

	first_attempt
					2015-11-06 22:55:15
	part5_correct_attempt
					['0:21:31', u'.5-1+.5']
	part6_incorrect_attempt
					('0:24:32', u'.25 - .5 + .25')
					('0:28:16', u'.25 - .25 + .25')
	part6_correct_attempt
					['0:30:36', u'1.5']

48 Student ID:pvl001

	first_attempt
					2015-11-03 15:27:52
	part5_correct_attempt
					['0:11:21', u'0']
	part6_incorrect_attempt
					('0:12:22', u'.5')
					('0:13:10', u'2.5')
	part6_correct_attempt
					['0:13:36', u'1.5']

49 Student ID:jcj006

	first_attempt
					2015-11-04 05:17:58
	part5_correct_attempt
					['0:00:00', u'0']
	part6_incorrect_attempt
					('0:14:34', u'.75')
	part6_correct_attempt
					['0:16:36', u'1.5']

50 Student ID:dlt009

	first_attempt
					2015-11-05 07:36:02
	part5_correct_attempt
					['0:02:20', u'(0.5)-2*(1)+(1.5)']
	part6_incorrect_attempt
					('0:03:34', u'(0.5)-2*(1)+(1.5)')
					('0:17:00', u'0.5-1+1.5')
	part6_correct_attempt
					['0:20:39', u'0.25+4*0.25+0.25']

51 Student ID:mbl003

	first_attempt
					2015-11-05 20:49:05
	part5_correct_attempt
					['0:02:41', u'0']
	part6_incorrect_attempt
					('0:03:04', u'1/2')
					('0:03:39', u'1/4-2/4+1/4')
	part6_correct_attempt
					['0:05:38', u'1/4+(2^2(1/4))+1/4']

52 Student ID:agoldsht

	first_attempt
					2015-11-04 05:16:55
	part5_correct_attempt
					['0:07:51', u'0']
	part6_incorrect_attempt
					('0:07:51', u'1/2*.5 - .5 + 1/2*.5')
	part6_correct_attempt
					['14:28:30', u'4*1/2*.5+1/2*.5+1/2*.5']

53 Student ID:n2patil

	first_attempt
					2015-11-04 02:51:17
	part5_correct_attempt
					['0:49:49', u'.5-(2*.5)+.5']
	part6_incorrect_attempt
					('0:57:58', u'(.25)-(2*(.25))+.25')
	part6_correct_attempt
					['0:58:44', u'(.25)+(4*(.25))+.25']

54 Student ID:ksmurlo

	first_attempt
					2015-11-05 06:04:45
	part5_correct_attempt
					['0:04:36', u'.5-1+.5']
	part6_incorrect_attempt
					('0:05:15', u'[(.5)^2+(1)^2+(.5)^2]/3')
					('0:06:13', u'[((2/3)-.5)^2+((2/3)-1)^2+((2/3)-.5)^2]/3')
					('0:07:05', u'[((2/3)-.5)^2+((2/3)-(-1))^2+((2/3)-.5)^2]/3')
					('0:08:06', u'[((0)-.5)^2+((0)-(-1))^2+((0)-.5)^2]/3')
	part6_correct_attempt
					['0:14:21', u'(.25)+(4*.25)+(.25)']

55 Student ID:ttimmons

	first_attempt
					2015-11-01 17:17:08
	part5_correct_attempt
					['0:23:29', u'0.5-2(0.5)+0.5']
	part6_incorrect_attempt
					('0:23:41', u'0.5')
	part6_correct_attempt
					['10:30:46', u'0.25+((-2)^2)*(0.25)+(0.25)']

56 Student ID:jnatale

	first_attempt
					2015-11-04 07:34:29
	part5_correct_attempt
					['0:18:48', u'0']
	part6_incorrect_attempt
					('0:35:00', u'3/0.5')
	part6_correct_attempt
					['17:16:49', u'3/2']

57 Student ID:hachrist

	first_attempt
					2015-11-03 20:13:34
	part5_correct_attempt
					['0:11:47', u'0']
	part6_incorrect_attempt
					('0:31:51', u'0.5')
					('21:23:32', u'0.25 + 2 + 0.5')
					('21:23:39', u'0.25 + 2 + 0.25')
	part6_correct_attempt
					['21:41:15', u'0.25 + 4(0.25) + 0.25']

58 Student ID:csl030

	first_attempt
					2015-11-05 04:54:16
	part5_correct_attempt
					['0:09:27', u'0']
	part6_incorrect_attempt
					('0:11:22', u'.5')

59 Student ID:k4ma

	first_attempt
					2015-11-06 21:00:56
	part5_correct_attempt
					['0:19:44', u'0']
	part6_incorrect_attempt
					('0:20:49', u'2^2*.25')
	part6_correct_attempt
					['0:21:45', u'.25-[(-1^2)*(2^2*.25)]+.25']

60 Student ID:aurodrig

	first_attempt
					2015-11-06 22:25:33
	part5_correct_attempt
					['0:14:40', u'0']
	part6_incorrect_attempt
					('0:20:33', u'1/4 + 2*(1/4) + 1/4')
					('0:22:03', u'4/4')
					('0:26:56', u'1/4 + 2*(1/4) + 1/4')
					('0:27:05', u'1/4 - 2*(1/4) + 1/4')
					('0:27:15', u'1/4 + 2*(1/4) + 1/4')
					('0:33:43', u'(1/4)^2 + (2^2)*((1/4)^2) + (1/4)^2')
	part6_correct_attempt
					['0:38:49', u'(1/2)^2 + (2^2)((1/2)^2) + (1/2)^2']

61 Student ID:hmnaing

	first_attempt
					2015-11-04 19:10:30
	part5_correct_attempt
					['0:00:00', u'(0.5*1)- 2(0.5*2) + (0.5*3)']
	part6_incorrect_attempt
					('0:09:54', u'(0.5)-(0.5)^2 + 4 * (0.5)-(0.5)^2 + (0.5)-(0.5)^2')
	part6_correct_attempt
					['0:11:32', u'(0.5)-(0.5)^2 + 4 * ((0.5)-(0.5)^2) + (0.5)-(0.5)^2']

62 Student ID:tjke

	first_attempt
					2015-11-04 20:53:53
	part5_correct_attempt
					['0:05:51', u'0.5*(1-2*1+1)']
	part6_incorrect_attempt
					('0:08:43', u'[0.5*1^2 - (0.5*1)^2] + [0.5*1^2 - (0.5*1)^2] + (2)^2*[0.5*-1^2 - (0.5*-1)^2]')
	part6_correct_attempt
					['0:09:42', u'[0.5*1^2 - (0.5*1)^2] + [0.5*1^2 - (0.5*1)^2] + (2)^2*[0.5*1^2 - (0.5*1)^2]']

63 Student ID:any027

	first_attempt
					2015-11-01 20:11:07
	part5_correct_attempt
					['0:15:23', u'(0.5) - 2*(0.5) + 0.5']
	part6_incorrect_attempt
					('0:16:12', u'0.75')
					('0:16:17', u'0.5')
					('0:17:07', u'((0.5)^2)*0.5')
	part6_correct_attempt
					['0:18:16', u'0.25+((2)^2)*0.25 + 0.25']

64 Student ID:dlgoldbe

	first_attempt
					2015-11-05 05:38:38
	part5_correct_attempt
					['0:04:18', u'0']
	part6_incorrect_attempt
					('0:04:56', u'0.25-(2*0.25)+0.25')
					('0:15:05', u'0.25*2+((-1^2)*0.25)')
					('0:22:29', u'0.25-((-1^2)*0.25)+0.25')
	part6_correct_attempt
					['0:22:36', u'0.25-((-2^2)*0.25)+0.25']

65 Student ID:jfalcone

	first_attempt
					2015-11-04 05:25:50
	part5_correct_attempt
					['23:57:15', u'0']
	part6_incorrect_attempt
					('23:57:15', u'4 * (1/2)*.5')
					('23:58:40', u'4*.5')
					('23:59:51', u'4 * .5 * .5')
	part6_correct_attempt
					['1 day, 0:00:08', u'4 * .5 * .5 + .5 * .5 + .5 * .5']

66 Student ID:ppanourg

	first_attempt
					2015-11-06 08:24:25
	part5_correct_attempt
					['10:32:58', u'0']
	part6_incorrect_attempt
					('10:45:07', u'1.25')
	part6_correct_attempt
					['10:47:24', u'1.5']

67 Student ID:rohan

	first_attempt
					2015-11-06 23:40:02
	part5_correct_attempt
					['0:18:52', u'0']
	part6_incorrect_attempt
					('0:20:15', u'(.5-.5^2)-(2(.5-.5^2))+(.5-.5^2)')
	part6_correct_attempt
					['0:20:55', u'(.5-.5^2)+(4(.5-.5^2))+(.5-.5^2)']

68 Student ID:masaro

	first_attempt
					2015-11-02 15:53:21
	part5_correct_attempt
					['0:02:29', u'0']
	part6_incorrect_attempt
					('0:15:10', u'0.5')
					('0:15:36', u'0.25')
					('0:21:56', u'0.5')
					('2:29:57', u'6.25')
	part6_correct_attempt
					['2:30:14', u'1.5']

69 Student ID:rwthomps

	first_attempt
					2015-11-06 18:18:48
	part5_correct_attempt
					['0:09:36', u'0.5 - 2 * 0.5 + 0.5']
	part6_incorrect_attempt
					('3:11:05', u'0.5')
					('3:11:13', u'0.75')
					('3:11:21', u'0.25')
	part6_correct_attempt
					['3:12:38', u'(0.5 * 0.5) + (-2)^2(0.25) + (0.25)']

70 Student ID:vsosnovs

	first_attempt
					2015-11-05 20:50:05
	part5_correct_attempt
					['0:10:41', u'0']
	part6_incorrect_attempt
					('0:10:41', u'.5^2')
					('0:11:08', u'.5')
					('0:19:49', u'.75')
	part6_correct_attempt
					['0:20:56', u'1.5']

71 Student ID:p4kumar

	first_attempt
					2015-11-05 23:59:56
	part5_correct_attempt
					['0:01:57', u'0']
	part6_incorrect_attempt
					('0:03:17', u'0.25 - 2 * 0.25 + 0.25')
					('0:03:26', u' 4 * 0.25')
	part6_correct_attempt
					['0:05:05', u'0.25 + 4 * 0.25 + 0.25']

72 Student ID:gsrandha

	first_attempt
					2015-11-05 07:24:37
	part5_correct_attempt
					['0:34:44', u'0']
	part6_incorrect_attempt
					('0:36:21', u'.25 +  .5 + .25')
					('0:36:46', u'.25 + 2 *.25+ .25')
					('0:37:09', u'4(.25 + .25+ .25)')
	part6_correct_attempt
					['0:37:47', u'1.5']

73 Student ID:jhc010

	first_attempt
					2015-11-06 10:26:35
	part5_correct_attempt
					['0:02:30', u'0']
	part6_incorrect_attempt
					('0:03:49', u'4.5')
	part6_correct_attempt
					['0:04:00', u'1.5']

74 Student ID:dkostins

	first_attempt
					2015-11-03 22:02:58
	part5_correct_attempt
					['0:09:16', u'0']
	part6_incorrect_attempt
					('0:13:34', u'4/4')
	part6_correct_attempt
					['0:13:51', u'6/4']

75 Student ID:twsalim

	first_attempt
					2015-11-04 03:30:14
	part5_correct_attempt
					['0:34:49', u'0']
	part6_incorrect_attempt
					('0:54:35', u'0.75')
	part6_correct_attempt
					['1:01:15', u'1.5']

76 Student ID:achinn

	first_attempt
					2015-11-03 21:11:57
	part5_correct_attempt
					['0:01:53', u'0']
	part6_incorrect_attempt
					('0:02:04', u'0.5')
	part6_correct_attempt
					['0:04:36', u'1.5']

77 Student ID:jap009

	first_attempt
					2015-11-05 21:00:35
	part5_correct_attempt
					['0:19:39', u'0']
	part6_incorrect_attempt
					('0:20:54', u'.25+2+.25')
	part6_correct_attempt
					['0:21:31', u'.25+1+.25']

78 Student ID:jcl084

	first_attempt
					2015-11-02 20:08:35
	part5_correct_attempt
					['0:02:46', u'0']
	part6_incorrect_attempt
					('0:03:39', u'0.5^2 + 2*(0.5^2) + 0.5^2')
	part6_correct_attempt
					['0:03:52', u'0.5^2 + 2^2*(0.5^2) + 0.5^2']

79 Student ID:ajabasa

	first_attempt
					2015-11-05 09:04:18
	part5_correct_attempt
					['9:03:37', u'.5-2*.5+(.5)']
	part6_incorrect_attempt
					('9:07:18', u'(.25+4*.25+.5)')
	part6_correct_attempt
					['9:50:18', u'(.25+4*.25+(.25))']

80 Student ID:hmshah

	first_attempt
					2015-11-05 09:34:38
	part5_correct_attempt
					['18:42:25', u'0']
	part6_incorrect_attempt
					('18:48:38', u'4((0 - .5)^2)')
	part6_correct_attempt
					['18:49:03', u'(0 - .5)^2 + (4*(0 - .5)^2) + (0 - .5)^2']

81 Student ID:lahawkin

	first_attempt
					2015-11-05 18:50:24
	part5_correct_attempt
					['0:02:52', u'.5-2(.5)+(.5)']
	part6_incorrect_attempt
					('0:43:56', u'(((.25)+(4*.25)+(.25))^2)/3')
	part6_correct_attempt
					['0:44:13', u'((.25)+(4*.25)+(.25))']

82 Student ID:z2tan

	first_attempt
					2015-11-02 05:18:51
	part5_correct_attempt
					['0:04:36', u'0']
	part6_incorrect_attempt
					('0:04:42', u'0.5')
	part6_correct_attempt
					['0:05:33', u'1.5']

83 Student ID:kquong

	first_attempt
					2015-11-02 04:08:58
	part5_correct_attempt
					['0:20:02', u'0']
	part6_incorrect_attempt
					('0:20:18', u'.5')
					('0:20:30', u'.25')
	part6_correct_attempt
					['0:37:38', u'1.5']

84 Student ID:kosung

	first_attempt
					2015-11-05 08:26:55
	part5_correct_attempt
					['0:00:49', u'0']
	part6_incorrect_attempt
					('0:04:43', u'0.5')
	part6_correct_attempt
					['0:39:23', u'1.5']

85 Student ID:yypan

	first_attempt
					2015-11-03 00:09:22
	part5_correct_attempt
					['0:08:40', u'0.5-2*0.5+0.5']
	part6_incorrect_attempt
					('0:09:26', u'0.5-0.5^2-2*(0.5-0.5^2)+0.5-0.5^2')
					('0:09:36', u'0.5-0.5^2+2*(0.5-0.5^2)+0.5-0.5^2')
	part6_correct_attempt
					['0:09:52', u'0.5-0.5^2+4*(0.5-0.5^2)+0.5-0.5^2']

86 Student ID:ajvanega

	first_attempt
					2015-11-05 02:30:18
	part5_correct_attempt
					['16:15:25', u'0']
	part6_incorrect_attempt
					('23:20:11', u'.5')
	part6_correct_attempt
					['1 day, 16:52:31', u'1.5']

87 Student ID:zhw110

	first_attempt
					2015-11-06 00:40:42
	part5_correct_attempt
					['0:00:00', u'0']
	part6_incorrect_attempt
					('23:38:08', u'1/3')
					('23:43:27', u'4*(0.5^2)')
					('23:53:15', u'4*(0.5^2)+2')
					('23:56:42', u'2*(0.5^2)+0.25*0.25')
					('23:57:04', u'3*(0.5^2)')
	part6_correct_attempt
					['23:57:36', u'6*(0.5^2)']

88 Student ID:mtrafeca

	first_attempt
					2015-11-02 00:15:44
	part5_correct_attempt
					['0:10:21', u'0']
	part6_incorrect_attempt
					('0:10:58', u'(.2+1+.25)/3')
					('0:11:05', u'(.25+1+.25)/3')
					('0:11:18', u'(.25+.5+.25)/3')
					('0:11:44', u'(.25-.5+.25)/3')
					('0:15:34', u'(.25+2+.25)/3')
					('0:16:35', u'1/3')
					('0:16:58', u'.25/3')
					('0:17:10', u'.5/3')
					('0:17:50', u'4/3')
					('0:32:14', u'2/3')
					('0:34:09', u'.75')
					('2:04:59', u'.25')
					('2:05:35', u'.5')
					('2:08:22', u'.25^2')
	part6_correct_attempt
					['2 days, 23:33:10', u'6/4']

89 Student ID:mjethani

	first_attempt
					2015-11-06 01:43:43
	part5_correct_attempt
					['0:00:00', u'0']
	part6_incorrect_attempt
					('0:02:59', u'1/3')
					('0:03:11', u'2/3')
					('19:08:22', u'(0.5) + ((4)0.5) + 0.5')
					('19:09:37', u'(0.25) + ((4)0.25) + 0.5')
	part6_correct_attempt
					['19:09:46', u'(0.25) + ((4)0.25) + 0.25']

90 Student ID:syc078

	first_attempt
					2015-11-05 03:28:26
	part5_correct_attempt
					['22:11:46', u'0']
	part6_incorrect_attempt
					('22:13:23', u'0.5')
					('22:18:32', u'(100^2)0.5')
					('22:22:07', u'0.5')
					('1 day, 14:58:08', u'0.5 + (((-2)^2)(0.5)) + 0.5')
	part6_correct_attempt
					['1 day, 17:11:35', u'0.25 + (((-2)^2)(0.25)) + 0.25']

91 Student ID:j2phung

	first_attempt
					2015-11-03 22:43:26
	part5_correct_attempt
					['1 day, 9:25:27', u'0']
	part6_incorrect_attempt
					('1 day, 9:45:01', u'1/2')
	part6_correct_attempt
					['1 day, 10:20:42', u'6/4']












## Part 7

### (20) Mistake Group Fraction of size 20




### (14) Mistake Group Digits of size 14




### (7) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:b3hwang

	first_attempt
					2015-11-05 08:38:09
	part7_incorrect_attempt
					('0:09:18', u'.5(84-1)84/2')
	part7_correct_attempt
					['0:09:32', u'0']

1 Student ID:m4salaza

	first_attempt
					2015-11-04 05:22:55
	part7_incorrect_attempt
					('0:02:31', u'.5*80')
					('0:02:44', u'.5*78')
	part7_correct_attempt
					['0:03:04', u'0']

2 Student ID:c1sorian

	first_attempt
					2015-11-04 23:20:51
	part7_incorrect_attempt
					('0:58:30', u'.5*98')
	part7_correct_attempt
					['0:59:02', u'0']

3 Student ID:ajabasa

	first_attempt
					2015-11-05 09:04:18
	part7_incorrect_attempt
					('12:36:52', u'.5*82')
	part7_correct_attempt
					['12:38:32', u'0']

4 Student ID:djk006

	first_attempt
					2015-11-03 22:37:00
	part7_incorrect_attempt
					('1:40:56', u'86*.5')
					('1:41:05', u'84*.5')
	part7_correct_attempt
					['1:42:16', u'0']

5 Student ID:avasavad

	first_attempt
					2015-11-04 23:06:05
	part7_incorrect_attempt
					('0:47:32', u'-82')
					('0:48:11', u'[(41/2)*82] - [(41/2)*84]')
					('10:49:42', u'82/2')

6 Student ID:c3chung

	first_attempt
					2015-11-06 10:47:12
	part7_incorrect_attempt
					('0:06:35', u'86*0.5')
	part7_correct_attempt
					['0:07:25', u'0']












## Part 8

### (129) Mistake Group Digits of size 129




### (63) Mistake Group Fraction of size 63




### (22) Mistake Group ['R.0'] of size 22
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|82/4	|82*.5	|[('R.0', 82.0, u'82', u'82')]	|
|1	|96/4	|96(0.5)	|[('R.0', 96.0, u'96', u'96')]	|
|2	|88/4	|88*.5	|[('R.0', 88.0, u'88', u'88')]	|
|3	|84/4	|84/2	|[('R.0', 84.0, u'84', u'84')]	|
|4	|92/4	|92*.5	|[('R.0', 92.0, u'92', u'92')]	|
|5	|90/4	|90/0.5	|[('R.0', 90.0, u'90', u'90')]	|
|6	|90/4	|90/2	|[('R.0', 90.0, u'90', u'90')]	|
|7	|82/4	|82/2	|[('R.0', 82.0, u'82', u'82')]	|
|8	|94/4	|94(0.5-(0.5^2)+0.5-(0.5^2))	|[('R.0', 94.0, u'94', u'94')]	|
|9	|86/4	|86(1/2*5)	|[('R.0', 86.0, u'86', u'86')]	|
|10	|82/4	|82 * .5	|[('R.0', 82.0, u'82', u'82')]	|
|11	|84/4	|84 * .5	|[('R.0', 84.0, u'84', u'84')]	|
|12	|100/4	|100*.5	|[('R.0', 100.0, u'100', u'100')]	|
|13	|82/4	|82*(1/2)	|[('R.0', 82.0, u'82', u'82')]	|
|14	|94/4	|94/2	|[('R.0', 94.0, u'94', u'94')]	|
|15	|90/4	|90*.24	|[('R.0', 90.0, u'90', u'90')]	|
|16	|84/4	|84*.5	|[('R.0', 84.0, u'84', u'84')]	|
|17	|94/4	|94(.5)	|[('R.0', 94.0, u'94', u'94')]	|
|18	|94/4	|94(.5+1.5)	|[('R.0', 94.0, u'94', u'94')]	|
|19	|94/4	|94(.1.5)	|[('R.0', 94.0, u'94', u'94')]	|
|20	|94/4	|94(1.5)	|[('R.0', 94.0, u'94', u'94')]	|
|21	|86/4	|86/12	|[('R.0', 86.0, u'86', u'86')]	|




### (14) Mistake Group ['R.1'] of size 14
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|92/4	|100/4	|[('R.1', 4.0, u'4', u'4')]	|
|1	|98/4	|(2*50)/4	|[('R.1', 4.0, u'4', u'4')]	|
|2	|86/4	|50/4	|[('R.1', 4.0, u'4', u'4')]	|
|3	|86/4	|80/4	|[('R.1', 4.0, u'4', u'4')]	|
|4	|86/4	|2/4	|[('R.1', 4.0, u'4', u'4')]	|
|5	|90/4	|90*2/4	|[('R.1', 4.0, u'4', u'4')]	|
|6	|98/4	|84/4	|[('R.1', 4.0, u'4', u'4')]	|
|7	|94/4	|1/4	|[('R.1', 4.0, u'4', u'4')]	|
|8	|90/4	|86/4	|[('R.1', 4.0, u'4', u'4')]	|




### (3) Mistake Group redirect of size 3




### (3) Mistake Group Wrong_Sign of size 3




### (45) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:b3hwang

	first_attempt
					2015-11-05 08:38:09
	part7_correct_attempt
					['0:09:32', u'0']
	part8_incorrect_attempt
					('0:09:55', u'(.5*84)^2')
	part8_correct_attempt
					['0:10:20', u'84*(.5)^2']

1 Student ID:apokhare

	first_attempt
					2015-11-05 21:35:02
	part7_correct_attempt
					['0:01:24', u'0']
	part8_incorrect_attempt
					('0:01:24', u'2.25')
	part8_correct_attempt
					['0:01:48', u'22.5']

2 Student ID:v4zhang

	first_attempt
					2015-11-05 11:05:44
	part7_correct_attempt
					['0:10:21', u'0']
	part8_incorrect_attempt
					('0:11:48', u'0.25*[(80*81)/2]')
					('0:13:39', u'(20*21)/2')
					('19:37:40', u'[((80*81*161)/6)-((80*81)/2)]*0.5')
	part8_correct_attempt
					['19:45:00', u'0.25*80']

3 Student ID:lywong

	first_attempt
					2015-11-04 19:08:27
	part7_correct_attempt
					['0:09:05', u'0']
	part8_incorrect_attempt
					('0:09:18', u'0.25(95)')
	part8_correct_attempt
					['0:09:23', u'0.25(94)']

4 Student ID:hkhodada

	first_attempt
					2015-10-31 15:40:08
	part7_correct_attempt
					['2 days, 8:48:22', u'0']
	part8_incorrect_attempt
					('2 days, 8:49:22', u'0.25*96')
	part8_correct_attempt
					['2 days, 8:49:52', u'0.25*92']

5 Student ID:kbielawi

	first_attempt
					2015-11-03 20:55:13
	part7_correct_attempt
					['23:37:06', u'0']
	part8_incorrect_attempt
					('2 days, 0:23:28', u'0.25')
	part8_correct_attempt
					['2 days, 0:23:51', u'0.25*94']

6 Student ID:glcohen

	first_attempt
					2015-11-03 16:48:17
	part7_correct_attempt
					['0:00:42', u'0']
	part8_incorrect_attempt
					('0:07:15', u'0.25')
					('3:56:29', u'0.1875')
					('3:56:40', u'1-0.1875')
					('4:03:00', u'0.25')
					('4:03:05', u'0.5')
	part8_correct_attempt
					['4:05:06', u'23.5']

7 Student ID:achava

	first_attempt
					2015-11-06 07:02:10
	part7_correct_attempt
					['0:18:14', u'0']
	part8_incorrect_attempt
					('0:18:51', u'0.5*88')
	part8_correct_attempt
					['0:21:05', u'0.5*(44)']

8 Student ID:atorr

	first_attempt
					2015-11-05 19:48:49
	part7_correct_attempt
					['0:05:55', u'0']
	part8_incorrect_attempt
					('1:04:17', u'0.25')
	part8_correct_attempt
					['1:06:32', u'(0.25) * 98']

9 Student ID:skarimik

	first_attempt
					2015-11-01 00:41:23
	part7_correct_attempt
					['0:43:21', u'0']
	part8_incorrect_attempt
					('0:43:21', u'1/2')
	part8_correct_attempt
					['2:00:17', u'47/2']

10 Student ID:rwthomps

	first_attempt
					2015-11-06 18:18:48
	part7_correct_attempt
					['3:07:51', u'0']
	part8_incorrect_attempt
					('3:11:30', u'0.5')
					('3:11:35', u'0.25')
					('3:13:00', u'(0.25) * 43')
	part8_correct_attempt
					['3:15:28', u'(0.25) * 86']

11 Student ID:mhale

	first_attempt
					2015-11-05 20:08:27
	part7_correct_attempt
					['0:09:18', u'0']
	part8_incorrect_attempt
					('0:10:09', u'0.5')
					('0:10:39', u'86^2(0.5)')
					('0:11:05', u'43^2(0.5)')
					('0:11:45', u'0.5 * 86')
	part8_correct_attempt
					['0:11:58', u'0.5 * 43']

12 Student ID:awollner

	first_attempt
					2015-11-06 22:55:15
	part7_correct_attempt
					['0:32:08', u'0']
	part8_incorrect_attempt
					('0:32:08', u'.5*88')
	part8_correct_attempt
					['0:32:21', u'.25*88']

13 Student ID:dcrume

	first_attempt
					2015-11-06 19:09:00
	part7_correct_attempt
					['1:00:29', u'0']
	part8_incorrect_attempt
					('1:06:03', u'0.5*92')
	part8_correct_attempt
					['1:08:37', u'0.5*.5*92']

14 Student ID:vsosnovs

	first_attempt
					2015-11-05 20:50:05
	part7_correct_attempt
					['0:11:38', u'0']
	part8_incorrect_attempt
					('0:12:03', u'.0')
					('0:12:08', u'.5')
					('0:12:13', u'.25')
					('0:22:50', u'37.5')
					('0:23:05', u'1.5')
					('0:23:11', u'1.5*5')
					('0:23:18', u'1.5*10')
					('0:23:25', u'1.5*20')
					('0:23:31', u'1.5*25')
					('0:23:57', u'1.5*.5')
					('0:34:02', u'.5+.25+1.5')
					('0:39:03', u'2.5')
					('0:39:08', u'2.25')
					('0:40:03', u'.5+1.5')
					('1:17:54', u'.5^2-.25^2')
					('1 day, 2:48:48', u'1.5+.5+.25')
					('1 day, 2:48:59', u'1.5+.5')
					('1 day, 2:49:16', u'47(1.5+.5)')
					('1 day, 2:49:22', u'49(1.5+.5)')

15 Student ID:n2patil

	first_attempt
					2015-11-04 02:51:17
	part7_correct_attempt
					['0:59:17', u'0']
	part8_incorrect_attempt
					('0:59:17', u'100(.25)')
	part8_correct_attempt
					['0:59:51', u'90(.25)']

16 Student ID:gsrandha

	first_attempt
					2015-11-05 07:24:37
	part7_correct_attempt
					['0:37:57', u'0']
	part8_incorrect_attempt
					('0:38:10', u'1.5 * 27')
	part8_correct_attempt
					['0:38:45', u'82*(1/4)']

17 Student ID:jit002

	first_attempt
					2015-11-05 01:51:15
	part7_correct_attempt
					['0:00:00', u'0']
	part8_incorrect_attempt
					('0:09:23', u'0.25')
	part8_correct_attempt
					['0:12:03', u'0.25*82']

18 Student ID:avasavad

	first_attempt
					2015-11-04 23:06:05
	part8_incorrect_attempt
					('0:50:43', u'(83*82)/8')

19 Student ID:hmnaing

	first_attempt
					2015-11-04 19:10:30
	part7_correct_attempt
					['0:10:55', u'0']
	part8_incorrect_attempt
					('0:12:05', u'0.25')
					('0:12:38', u'82/2* (0.25)')
	part8_correct_attempt
					['0:13:44', u'((0.5)-(0.5)^2 )* 82']

20 Student ID:jcl084

	first_attempt
					2015-11-02 20:08:35
	part7_correct_attempt
					['0:04:39', u'0']
	part8_incorrect_attempt
					('0:04:39', u'100*(0.5^2)')
					('0:04:57', u'100^2*(0.5^2)')
	part8_correct_attempt
					['0:05:08', u'82*(0.5^2)']

21 Student ID:skodigal

	first_attempt
					2015-11-05 09:10:36
	part7_correct_attempt
					['19:15:00', u'0']
	part8_incorrect_attempt
					('19:15:49', u'.5*88')
	part8_correct_attempt
					['19:16:17', u'.25*88']

22 Student ID:kew017

	first_attempt
					2015-11-05 21:33:59
	part7_correct_attempt
					['0:09:06', u'0']
	part8_incorrect_attempt
					('0:09:06', u'1/(2*86)')
					('0:09:17', u'1/(4*86)')
	part8_correct_attempt
					['0:09:30', u'86/(4)']

23 Student ID:dsmonaha

	first_attempt
					2015-11-02 16:47:16
	part7_correct_attempt
					['4 days, 4:21:01', u'0']
	part8_incorrect_attempt
					('4 days, 4:21:01', u'(.25)^82')
	part8_correct_attempt
					['4 days, 4:21:51', u'(.25)*82']

24 Student ID:tstevens

	first_attempt
					2015-11-06 11:34:10
	part7_correct_attempt
					['0:02:46', u'0']
	part8_incorrect_attempt
					('0:07:55', u'.5')
					('0:13:22', u'.25')
					('0:13:29', u'.75')
	part8_correct_attempt
					['0:18:38', u'22.5']

25 Student ID:ytc012

	first_attempt
					2015-11-05 22:01:35
	part7_correct_attempt
					['0:00:00', u'0']
	part8_incorrect_attempt
					('0:00:00', u'0.25*86')
	part8_correct_attempt
					['0:00:10', u'0.25*98']

26 Student ID:sghouse

	first_attempt
					2015-11-03 21:24:01
	part7_correct_attempt
					['0:18:41', u'0']
	part8_incorrect_attempt
					('0:18:41', u'.5*90')
	part8_correct_attempt
					['0:18:54', u'.25*90']

27 Student ID:lguintu

	first_attempt
					2015-11-03 04:17:57
	part7_correct_attempt
					['0:02:11', u'0']
	part8_incorrect_attempt
					('0:02:39', u'(94+95)/(2*4)')
	part8_correct_attempt
					['0:03:18', u'94/4']

28 Student ID:mtrafeca

	first_attempt
					2015-11-02 00:15:44
	part7_correct_attempt
					['0:18:29', u'0']
	part8_incorrect_attempt
					('0:18:46', u'.5')
					('0:23:48', u'1/2')
					('0:23:57', u'.25')
					('0:24:08', u'1/86')
					('0:24:23', u'.5/86')
					('0:24:29', u'.25/86')
					('0:24:41', u'.25*86/86')
					('2:05:08', u'.25')
					('2:05:35', u'.5')
					('2:08:14', u'.25^2')
	part8_correct_attempt
					['2 days, 23:43:15', u'86/4']

29 Student ID:acs008

	first_attempt
					2015-11-04 05:07:00
	part7_correct_attempt
					['0:08:11', u'0']
	part8_incorrect_attempt
					('0:09:35', u'0.5')
					('0:09:51', u'1.5')
					('0:10:16', u'0.25')
					('0:10:22', u'0.75')
					('0:10:29', u'1.75')
					('0:10:37', u'2.25')
	part8_correct_attempt
					['0:10:59', u'0.5^2*90']

30 Student ID:asp025

	first_attempt
					2015-11-06 19:55:41
	part7_correct_attempt
					['0:32:44', u'0']
	part8_incorrect_attempt
					('0:36:28', u'[100*(0.5)^2*(96-1)^2]^(1/2)')
					('0:37:54', u'[100*(0.5)^2*(96-1)^2]')
					('0:39:20', u'[100*(0.5)*(96-1)^2]')
					('0:52:33', u'[96*(0.5)*(0.5)^2]')
					('1:00:05', u'[100*((0.5)-(0.5)^2)]')
	part8_correct_attempt
					['1:01:20', u'[96*((0.5)-(0.5)^2)]']

31 Student ID:arvenega

	first_attempt
					2015-11-06 23:34:13
	part7_correct_attempt
					['0:00:00', u'0']
	part8_incorrect_attempt
					('0:00:00', u'46*.5')
	part8_correct_attempt
					['0:00:27', u'42*.5']

32 Student ID:haliew

	first_attempt
					2015-11-06 22:53:03
	part7_correct_attempt
					['0:12:28', u'0']
	part8_incorrect_attempt
					('0:13:06', u'.5')
					('1:27:50', u'.5')
					('1:27:56', u'.25')
	part8_correct_attempt
					['1:28:55', u'.5(94/2)']

33 Student ID:tdurrer

	first_attempt
					2015-11-06 03:30:34
	part7_correct_attempt
					['1:09:25', u'0']
	part8_incorrect_attempt
					('1:10:17', u'((82)^2)(.25)')
	part8_correct_attempt
					['1:11:07', u'(82)(.25)']

34 Student ID:eshung

	first_attempt
					2015-11-05 22:57:38
	part7_correct_attempt
					['0:03:07', u'0']
	part8_incorrect_attempt
					('0:03:07', u'45.5')
					('0:03:28', u'40.5')
					('0:05:20', u'430.5')
					('0:06:48', u'15.5')
	part8_correct_attempt
					['0:08:12', u'20.5']

35 Student ID:aurodrig

	first_attempt
					2015-11-06 22:25:33
	part7_correct_attempt
					['0:20:33', u'0']
	part8_incorrect_attempt
					('0:20:33', u'100*(1/4)')
	part8_correct_attempt
					['0:21:52', u'90*(1/4)']

36 Student ID:m4salaza

	first_attempt
					2015-11-04 05:22:55
	part7_correct_attempt
					['0:03:04', u'0']
	part8_incorrect_attempt
					('23:59:33', u'86*1/2*5')
	part8_correct_attempt
					['1 day, 0:00:18', u'86*1/2*.5']

37 Student ID:bpandayk

	first_attempt
					2015-11-06 21:27:20
	part7_correct_attempt
					['0:00:00', u'0']
	part8_incorrect_attempt
					('0:00:00', u'100*(0.5(0.5))')
	part8_correct_attempt
					['0:00:22', u'98*(0.5(0.5))']

38 Student ID:xweng

	first_attempt
					2015-11-06 00:01:52
	part7_correct_attempt
					['0:04:02', u'0']
	part8_incorrect_attempt
					('0:04:28', u'2^1000.25')
					('0:04:34', u'2^100*0.25')
	part8_correct_attempt
					['0:04:52', u'100*0.25']

39 Student ID:any027

	first_attempt
					2015-11-01 20:11:07
	part7_correct_attempt
					['0:18:43', u'0']
	part8_incorrect_attempt
					('0:18:52', u'0.5')
					('0:19:06', u'0.25')
					('0:19:31', u'0.5')
	part8_correct_attempt
					['0:19:42', u'0.25 * 90']

40 Student ID:m8woo

	first_attempt
					2015-11-05 20:48:48
	part7_correct_attempt
					['0:09:52', u'0']
	part8_incorrect_attempt
					('0:10:16', u'0.5*94')
					('0:10:22', u'0.5*100')
	part8_correct_attempt
					['0:10:47', u'0.25*94']

41 Student ID:tjke

	first_attempt
					2015-11-04 20:53:53
	part7_correct_attempt
					['0:10:17', u'0.5*0']
	part8_incorrect_attempt
					('0:10:17', u'[0.5*0^2 - (0.5*0)^2]')
					('0:11:25', u'86/2*[[0.5*1^2 - (0.5*1)^2] + [0.5*-1^2 - (0.5*-1)^2]]')
					('0:11:38', u'[[0.5*1^2 - (0.5*1)^2] + [0.5*-1^2 - (0.5*-1)^2]]')
					('0:13:27', u'86^2*[0.5*1^2 - (0.5*1)^2]')
					('0:13:41', u'(86/2)^2*[0.5*1^2 - (0.5*1)^2]')
					('0:14:06', u'0.5')
	part8_correct_attempt
					['0:14:28', u'86/2*0.5']

42 Student ID:muy002

	first_attempt
					2015-11-06 00:02:46
	part7_correct_attempt
					['0:04:32', u'0']
	part8_incorrect_attempt
					('0:04:32', u'.5*50')
	part8_correct_attempt
					['0:04:47', u'.5*45']

43 Student ID:kgrozav

	first_attempt
					2015-11-05 07:35:53
	part7_correct_attempt
					['12:24:31', u'0']
	part8_incorrect_attempt
					('12:24:31', u'.25*100')
	part8_correct_attempt
					['12:24:41', u'.25*88']

44 Student ID:masaro

	first_attempt
					2015-11-02 15:53:21
	part7_correct_attempt
					['0:02:29', u'0']
	part8_incorrect_attempt
					('0:15:10', u'0.5')
					('0:16:06', u'0.25')
					('1 day, 6:04:48', u'0.25')
					('1 day, 6:04:53', u'0.5')
	part8_correct_attempt
					['1 day, 6:48:37', u'0.25*94']












