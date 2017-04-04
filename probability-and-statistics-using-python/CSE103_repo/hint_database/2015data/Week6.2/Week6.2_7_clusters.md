#Problem 7

    $a = random(1,5);
    $b = random(6,10);

    ## The mean, or expected value  ##

    ---
    Let [`X_1, X_2, \cdots X_{5}`]  be independent random variables with:
    [$BCENTER]*
    [``\mathbb{E}(X_i) = \frac{[$a]}{i} \hspace{10pt} \mbox{VAR}(X_i) = \frac{[$b]}{i^2}``]
    [$ECENTER]*
    ---
    Compute:

    * the mean of [`X_1 + X_2 + X_3 + X_4 + X_5`] [_____________________________]{Compute("$a*(1+1/2+1/3+1/4+1/5)")}
    * ...and the variance [______________________________]{Compute("$b*(1+1/4+1/9+1/16+1/25)")}

    * the mean of [`X_1 - X_2 + X_3 - X_4 + X_5`] [_______________________________]{Compute("$a*(1-1/2+1/3-1/4+1/5)")}
    * ...and the variance  [________________________________]{Compute("$b*(1+1/4+1/9+1/16+1/25)")}


    * the mean of [`X_1 - 2X_2 + X_3 - 2X_4 + X_5`] [_______________________________]{Compute("$a*(1-2/2+1/3-2/4+1/5)")}
    * ...and the variance [________________________________]{Compute("$b*(1+1/9+1/25) +$b*4*(1/4+1/16)")}





## Part 1

### (43) Mistake Group Digits of size 43




### (7) Mistake Group ['R.1'] of size 7
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|3*(1+1/2+1/3+1/4+1/5)	|5*(1+1/2+1/3+1/4+1/5)	|[('R.1', 2.283333333333333, u'1+1/2+1/3+1/4+1/5', u'1+1/2+1/3+1/4+1/5')]	|
|1	|3*(1+1/2+1/3+1/4+1/5)	|3/5(1+1/2+1/3+1/4+1/5)	|[('R.1', 2.283333333333333, u'1+1/2+1/3+1/4+1/5', u'1+1/2+1/3+1/4+1/5')]	|
|2	|1*(1+1/2+1/3+1/4+1/5)	|5*(1/1+1/2+1/3+1/4+1/5)	|[('R.1', 2.283333333333333, u'1+1/2+1/3+1/4+1/5', u'1/1+1/2+1/3+1/4+1/5')]	|
|3	|1*(1+1/2+1/3+1/4+1/5)	|8*(1+1/2+1/3+1/4+1/5)	|[('R.1', 2.283333333333333, u'1+1/2+1/3+1/4+1/5', u'1+1/2+1/3+1/4+1/5')]	|
|4	|1*(1+1/2+1/3+1/4+1/5)	|5*((1/1)+(1/2)+(1/3)+(1/4)+(1/5))	|[('R.1', 2.283333333333333, u'1+1/2+1/3+1/4+1/5', u'(1/1)+(1/2)+(1/3)+(1/4)+(1/5)')]	|




### (1) Mistake Group ['R.1.0.0.0.1.1', 'R.1.0.0.1.1', 'R.1.0.1.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.0.0.0.1.1', 'R.1.0.0.1.1', 'R.1.0.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|5*(1+1/2+1/3+1/4+1/5)	|1/5(5/1+5/2+5/3+5/4+5/5)	|[('R.1.0.0.0.1.1', 2.0, u'2', u'2'), ('R.1.0.0.1.1', 3.0, u'3', u'3'), ('R.1.0.1.1', 4.0, u'4', u'4')]	|




### (1) Mistake Group ['R.1.0.0.1', 'R.1.0.1', 'R.1.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.0.0.1', 'R.1.0.1', 'R.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|2*(1+1/2+1/3+1/4+1/5)	|2*(1/1 + 1/2 + 1/3 + 1/3 + 1/4 + 1/5)	|[('R.1.0.0.1', 0.3333333333333333, u'1/3', u'1/3'), ('R.1.0.1', 0.25, u'1/4', u'1/4'), ('R.1.1', 0.2, u'1/5', u'1/5')]	|




### (1) Mistake Group ['R.1.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|3*(1+1/2+1/3+1/4+1/5)	|3(1/3 - 1/2 +1/5)	|[('R.1.1', 0.2, u'1/5', u'1/5')]	|




### (1) Mistake Group Wrong_Sign of size 1




### (113) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:kbielawi

	first_attempt
					2015-11-04 20:36:01
	part1_incorrect_attempt
					('0:00:00', u'5/3')
					('0:00:00', u'7/35')
					('0:00:39', u'7/9')
					('0:00:00', u'(5 + 5/2 +5/3+5/4+1)/5')
					('0:00:00', u'(5/1+5/2+5/3+5/4+5/5)/5')
	part1_correct_attempt
					['1 day, 4:14:18', u'(5/1+5/2+5/3+5/4+5/5)']

1 Student ID:ssamudra

	first_attempt
					2015-11-05 06:15:19
	part1_incorrect_attempt
					('0:00:00', u'7/(25)')
	part1_correct_attempt
					['0:01:40', u'1/5 + 1/4 + 1/3 + 1/2 + 1']

2 Student ID:jjm019

	first_attempt
					2015-11-04 23:29:51
	part1_incorrect_attempt
					('0:00:00', u'3/5')
					('0:00:00', u'[(3/1)+(3/2)+(3/3)+(3/4)+(3/5)]/5')
	part1_correct_attempt
					['3:17:53', u'[(3/1)+(3/2)+(3/3)+(3/4)+(3/5)]']

3 Student ID:mhale

	first_attempt
					2015-11-05 20:21:09
	part1_incorrect_attempt
					('0:00:00', u'(1 + 1/2 + 1/3 + 1/4 + 1/5) / 5')
					('0:00:35', u'15 / 5')
	part1_correct_attempt
					['0:01:03', u'1 + 1/2 + 1/3 + 1/4 + 1/5']

4 Student ID:nhn018

	first_attempt
					2015-11-05 05:49:28
	part1_incorrect_attempt
					('0:00:00', u'2/5')
	part1_correct_attempt
					['14:19:04', u'2+2/2+2/3+2/4+2/5']

5 Student ID:dan029

	first_attempt
					2015-11-05 09:09:40
	part1_incorrect_attempt
					('0:00:00', u'77/60/5')
					('0:00:13', u'137/60/5')
	part1_correct_attempt
					['0:00:19', u'137/60']

6 Student ID:jyc018

	first_attempt
					2015-11-04 18:43:05
	part1_incorrect_attempt
					('0:00:00', u'(4+2+4/3+1+4/5)/5')
	part1_correct_attempt
					['0:06:51', u'(4+2+4/3+1+4/5)']

7 Student ID:vqt004

	first_attempt
					2015-11-06 05:33:12
	part1_incorrect_attempt
					('0:00:00', u'(4+2+4/3+1+4/5)/5')
					('0:02:13', u'(4/5)*(1+2+3+4+5)/5')
					('0:06:06', u'(4+2+4/3+1+4/5)/5')
	part1_correct_attempt
					['0:07:49', u'(4+2+4/3+1+4/5)']

8 Student ID:mnrahman

	first_attempt
					2015-11-06 23:58:37
	part1_incorrect_attempt
					('0:00:00', u'(1+1/2+1/3+1/4+1/5)*1')
	part1_correct_attempt
					['0:01:43', u'(1+1/2+1/3+1/4+1/5)*2']

9 Student ID:r9jiang

	first_attempt
					2015-11-02 02:34:25
	part1_incorrect_attempt
					('0:00:00', u'137/60')
					('0:11:13', u'1+1/2+1/3+1/4+1/5')
	part1_correct_attempt
					['0:13:07', u'5+5/2+5/3+5/4+5/5']

10 Student ID:dgunawan

	first_attempt
					2015-11-05 08:36:34
	part1_incorrect_attempt
					('0:00:00', u'5* (2*(2^(1/2)))')
	part1_correct_attempt
					['0:02:35', u'1 + 1/2 + 1/3 + 1/4 + 1/5 ']

11 Student ID:tcn013

	first_attempt
					2015-11-04 02:25:03
	part1_incorrect_attempt
					('0:00:00', u'.8')
	part1_correct_attempt
					['3:03:54', u'4+2+4/3+1+.8']

12 Student ID:tstevens

	first_attempt
					2015-11-06 11:53:34
	part1_incorrect_attempt
					('0:00:00', u'4/5')
					('0:00:42', u'(4+2+4/3+1+.8)/5')
					('0:01:22', u'4/25')
	part1_correct_attempt
					['0:01:37', u'4+2+1+4/3+.8']

13 Student ID:l8ngo

	first_attempt
					2015-10-30 16:27:14
	part1_incorrect_attempt
					('0:00:00', u'2/5')
					('0:00:59', u'2+2/2+2/3+2/4+2/3')
	part1_correct_attempt
					['0:03:52', u'2+2/2+2/3+2/4+2/5']

14 Student ID:djk006

	first_attempt
					2015-11-04 00:21:56
	part1_incorrect_attempt
					('0:00:00', u'(2/1+2/2+2/3+2/4+2/5)/5')
					('0:03:08', u'2/5')
	part1_correct_attempt
					['0:03:46', u'2/1+2/2+2/3+2/4+2/5']

15 Student ID:dsriniva

	first_attempt
					2015-11-05 09:25:10
	part1_incorrect_attempt
					('0:00:00', u'(5+5/2+5/3+5/4+1)/5')
	part1_correct_attempt
					['0:00:17', u'(5+5/2+5/3+5/4+1)']

16 Student ID:sayao

	first_attempt
					2015-11-04 01:35:01
	part1_incorrect_attempt
					('0:00:00', u'(3+3/2+1+3/4+3/5)/5')
					('0:01:58', u'3/4')
					('0:02:36', u'(3+3/2+1+3/4+3/5)/5')
					('0:02:59', u'(3+3/2+1+3/4+3/5)/3')
	part1_correct_attempt
					['0:03:14', u'(3+3/2+1+3/4+3/5)']

17 Student ID:anvan

	first_attempt
					2015-11-05 15:57:18
	part1_incorrect_attempt
					('0:00:00', u'(2 + 1 + 2/3 + 1/2 + 2/5) / 5')
	part1_correct_attempt
					['0:08:35', u'2 + 1 + 2/3 + 1/2 + 2/5']

18 Student ID:csl030

	first_attempt
					2015-11-06 00:13:28
	part1_incorrect_attempt
					('0:00:00', u'(3/1 + 3/2 + 3/3 + 3/4 + 3/5)/5')
	part1_correct_attempt
					['0:01:54', u'(3/1 + 3/2 + 3/3 + 3/4 + 3/5)']

19 Student ID:asp025

	first_attempt
					2015-11-03 21:27:22
	part1_incorrect_attempt
					('0:00:00', u'2/5')
					('0:00:00', u'4.56')
	part1_correct_attempt
					['2 days, 23:36:04', u'(2)+(1)+(2/3)+(2/4)+(2/5)']

20 Student ID:c1wei

	first_attempt
					2015-11-04 06:48:33
	part1_incorrect_attempt
					('0:00:00', u'3/5')
					('0:00:38', u'(3+(3/2)+1+3/4+3/5)/5')
	part1_correct_attempt
					['0:02:07', u'(3+(3/2)+1+3/4+3/5)']

21 Student ID:m8woo

	first_attempt
					2015-11-05 21:02:09
	part1_incorrect_attempt
					('0:00:00', u'[3/1 + 3/2 + 3/3 + 3/4 + 3/5]/5')
	part1_correct_attempt
					['0:01:00', u'[3/1 + 3/2 + 3/3 + 3/4 + 3/5]']

22 Student ID:akg009

	first_attempt
					2015-11-06 20:59:25
	part1_incorrect_attempt
					('0:00:00', u'(1+1/2+1/3+1/4+1/5)/5')
	part1_correct_attempt
					['0:01:31', u'(1+1/2+1/3+1/4+1/5)']

23 Student ID:jit002

	first_attempt
					2015-11-05 03:52:36
	part1_incorrect_attempt
					('0:00:00', u'(5+2.5+5/3+5/4+1)/5')
	part1_correct_attempt
					['0:09:02', u'5+2.5+5/3+5/4+1']

24 Student ID:b3hwang

	first_attempt
					2015-11-05 08:49:28
	part1_incorrect_attempt
					('0:00:00', u'4/5')
	part1_correct_attempt
					['0:00:59', u'(4/1) + 4/2 + 4/3 + 4/4 + 4/5']

25 Student ID:quwong

	first_attempt
					2015-10-30 01:45:05
	part1_incorrect_attempt
					('0:00:00', u'2.2833')
	part1_correct_attempt
					['4 days, 19:20:44', u'5(1 + 1/2 + 1/3 + 1/4 + 1/5)']

26 Student ID:lguintu

	first_attempt
					2015-11-03 04:48:21
	part1_incorrect_attempt
					('0:00:00', u'3+3/2+3/3+3/5+3/4+3/6')
	part1_correct_attempt
					['0:00:22', u'(3+3/2+3/3+3/4+3/5)']

27 Student ID:c1sorian

	first_attempt
					2015-11-05 00:24:33
	part1_incorrect_attempt
					('0:00:00', u'(3*(1+.5+(1/3)+.25+.2))/5')
					('0:00:31', u'(3+1.5+1+.75+.6)/5')
					('0:06:18', u'(3+1.5+1+.75+.6)/5')
					('0:12:14', u'((3/1)+(3/2)+(3/3)+(3/4)+(3/5))/5')
	part1_correct_attempt
					['0:14:24', u'((3/1)+(3/2)+(3/3)+(3/4)+(3/5))']

28 Student ID:skarimik

	first_attempt
					2015-11-01 18:23:56
	part1_incorrect_attempt
					('0:00:00', u'7+7/4+7/9+7/16+7/25')
					('0:01:16', u'7+7/4+7/9+7/16+7/25')
					('0:03:14', u'7+7/4+7/9+7/16+7/25')
					('0:03:29', u'7+7/4+7/9+7/16+7/25')
	part1_correct_attempt
					['0:07:01', u'5+5/2+5/3+5/4+1']

29 Student ID:krau

	first_attempt
					2015-11-04 20:33:16
	part1_incorrect_attempt
					('0:00:00', u'(1/1+1/2+1/3+1/4+1/5) / 5')
					('0:00:00', u'8/1+8/4+8/9+8/16+8/25')
	part1_correct_attempt
					['6:35:23', u'1+1/2+1/3+1/4+1/5']

30 Student ID:kthui

	first_attempt
					2015-11-06 07:49:41
	part1_incorrect_attempt
					('0:00:00', u'(4+2+4/3+1+4/5)/5')
	part1_correct_attempt
					['0:03:28', u'4+2+4/3+1+4/5']

31 Student ID:psable

	first_attempt
					2015-11-06 00:20:20
	part1_incorrect_attempt
					('0:00:00', u'137/300')
	part1_correct_attempt
					['0:03:19', u'137/60']

32 Student ID:dwzhang

	first_attempt
					2015-11-04 20:59:32
	part1_incorrect_attempt
					('0:00:00', u'(3 + 3/2 + 1 + 3/4 + 3/5)/5')
	part1_correct_attempt
					['0:00:12', u'3/1 + 3/2 + 3/3 + 3/4 + 3/5']

33 Student ID:rraiyyan

	first_attempt
					2015-11-06 23:09:50
	part1_incorrect_attempt
					('0:00:00', u'1/5')
					('0:00:00', u'1/25+2/25+3/25+4/25+1/5')
					('0:00:36', u'1+1/2+1/3+1/4+1/5')
					('0:01:07', u'1+2*1/2+3*1/3+4*1/4+5*1/5')
					('0:01:50', u'(1+1/2+1/3+1/4+1/5) / 5')
					('0:02:01', u'1+1/2+1/3+1/4+1/5')
					('0:03:40', u'1/2+1/4+1/9+1/16+1/25')
					('0:05:41', u'(1+1/2+1/3+1/4+1/5)/5')
	part1_correct_attempt
					['0:11:10', u'5*(1+1/2+1/3+1/4+1/5)']

34 Student ID:r1gu

	first_attempt
					2015-11-05 12:06:08
	part1_incorrect_attempt
					('0:00:00', u'9/25')
	part1_correct_attempt
					['0:04:31', u'5+5/2+5/4+5/3+1']

35 Student ID:t1tran

	first_attempt
					2015-11-03 18:03:30
	part1_incorrect_attempt
					('0:00:00', u'(4/1+4/2+4/3+4/4+4/5)/5')
					('0:07:09', u'4/5')
	part1_correct_attempt
					['0:11:24', u'(4/1+4/2+4/3+4/4+4/5)']

36 Student ID:dsmonaha

	first_attempt
					2015-11-02 17:22:58
	part1_incorrect_attempt
					('0:00:00', u'137/60')
	part1_correct_attempt
					['0:00:43', u'137/12']

37 Student ID:cprafull

	first_attempt
					2015-11-05 08:46:01
	part1_incorrect_attempt
					('0:00:00', u'(5 + 5/2 + 5/3 + 5/4 + 1)/5')
					('0:00:45', u'(1 + 2 + 3 + 4 + 5)/5')
	part1_correct_attempt
					['0:02:34', u'5 + 5/2 + 5/3 + 5/4 + 1']

38 Student ID:ggaddi

	first_attempt
					2015-11-01 21:08:49
	part1_incorrect_attempt
					('0:00:00', u'1/5')
					('0:00:49', u'(1+1/2+1/3+1/4+1/5)/5')
	part1_correct_attempt
					['0:00:56', u'(1+1/2+1/3+1/4+1/5)']

39 Student ID:muy002

	first_attempt
					2015-11-06 00:09:19
	part1_incorrect_attempt
					('0:00:00', u'(4+4/2+4/3+4/4+4/5)/5')
	part1_correct_attempt
					['0:01:34', u'(4+4/2+4/3+4/4+4/5)']

40 Student ID:jtfrankl

	first_attempt
					2015-11-06 18:35:12
	part1_incorrect_attempt
					('0:00:00', u'(1+.5+1/3+1/4+.2)/5')
	part1_correct_attempt
					['0:05:40', u'(1+.5+1/3+1/4+.2)']

41 Student ID:j5phung

	first_attempt
					2015-11-04 04:47:43
	part1_incorrect_attempt
					('0:00:00', u'1/5')
	part1_correct_attempt
					['0:02:08', u'(3+3/2+3/3+3/4+3/5)']

42 Student ID:rbdoming

	first_attempt
					2015-11-05 19:02:04
	part1_incorrect_attempt
					('0:00:00', u'25/15')
					('0:00:44', u'(5 + 5/2 + 5/3 +5/4 +1)/5')
	part1_correct_attempt
					['0:01:00', u'(5 + 5/2 + 5/3 +5/4 +1)']

43 Student ID:ralhadda

	first_attempt
					2015-10-31 20:32:11
	part1_incorrect_attempt
					('0:00:00', u'1/5')
					('0:01:39', u'1/5')
					('0:01:55', u'10/25')
	part1_correct_attempt
					['0:02:50', u'2.283333']

44 Student ID:yjshin

	first_attempt
					2015-11-06 23:12:25
	part1_incorrect_attempt
					('0:00:00', u'4/5')
	part1_correct_attempt
					['0:00:29', u'4/5+4/4+4/3+4/2+4/1']

45 Student ID:bkoli

	first_attempt
					2015-11-05 22:43:04
	part1_incorrect_attempt
					('0:00:00', u'(2/1+2/2+2/3+2/4+2/5)/5')
	part1_correct_attempt
					['0:03:48', u'(2/1+2/2+2/3+2/4+2/5)']

46 Student ID:hsc052

	first_attempt
					2015-11-05 09:16:09
	part1_incorrect_attempt
					('0:00:00', u'49/20')
	part1_correct_attempt
					['0:00:18', u'1/1+1/2+1/3+1/4+1/5']

47 Student ID:xil109

	first_attempt
					2015-11-05 03:36:35
	part1_incorrect_attempt
					('0:00:00', u'0.2')
					('0:00:16', u'0.4')
					('0:00:52', u'0.08')
	part1_correct_attempt
					['0:24:05', u'2+1+2/3+2/4+2/5']

48 Student ID:v3doan

	first_attempt
					2015-11-05 05:29:24
	part1_incorrect_attempt
					('0:00:00', u'( 1 + 1/2 + 1/3 + 1/4 + 1/5) / 5')
					('0:00:26', u'1/5')
					('0:00:00', u'( 1 + 1/2 + 1/3 + 1/4 + 1/5) / 5')
	part1_correct_attempt
					['1 day, 18:58:49', u'( 1 + 1/2 + 1/3 + 1/4 + 1/5)']

49 Student ID:yil035

	first_attempt
					2015-11-04 00:43:02
	part1_incorrect_attempt
					('0:00:00', u'1.82666667')
	part1_correct_attempt
					['0:00:33', u'1.82666667*5']

50 Student ID:wmiao

	first_attempt
					2015-11-04 20:26:55
	part1_incorrect_attempt
					('0:00:00', u'(1/1+1/2+1/3+1/4+1/5)/5')
	part1_correct_attempt
					['0:00:14', u'(1/1+1/2+1/3+1/4+1/5)']

51 Student ID:k3tan

	first_attempt
					2015-11-04 01:49:32
	part1_incorrect_attempt
					('0:00:00', u'(7+(4/3)+(4/5))/5')
	part1_correct_attempt
					['0:00:26', u'(7+(4/3)+(4/5))']

52 Student ID:lywong

	first_attempt
					2015-11-04 07:22:57
	part1_incorrect_attempt
					('0:00:00', u'2/5')
	part1_correct_attempt
					['0:01:48', u'3+(2/3)+(1/2)+(2/5)']

53 Student ID:hkhodada

	first_attempt
					2015-10-31 16:49:04
	part1_incorrect_attempt
					('0:00:00', u'5269/360')
					('0:08:00', u'5269/360')
					('3:26:56', u'121/15')
	part1_correct_attempt
					['2 days, 7:43:17', u'4+4/2+4/3+4/4+4/5']

54 Student ID:abasu

	first_attempt
					2015-11-05 02:55:33
	part1_incorrect_attempt
					('0:00:00', u'1.37')
					('0:00:09', u'6.35')
	part1_correct_attempt
					['0:01:11', u'6.85']

55 Student ID:d6he

	first_attempt
					2015-11-05 02:13:09
	part1_incorrect_attempt
					('0:00:00', u'1.37')
	part1_correct_attempt
					['4:22:44', u'3/1+3/2+1+3/4+3/5']

56 Student ID:awollner

	first_attempt
					2015-11-06 23:29:48
	part1_incorrect_attempt
					('0:00:00', u'10/15')
	part1_correct_attempt
					['0:00:51', u'2+1+2/3+1/2+ 2/5']

57 Student ID:dcrume

	first_attempt
					2015-11-06 20:29:43
	part1_incorrect_attempt
					('0:00:00', u'3/5')
	part1_correct_attempt
					['0:00:41', u'3/1 + 3/2 + 3/3 +3/4 + 3/5']

58 Student ID:mrchin

	first_attempt
					2015-11-06 19:50:05
	part1_incorrect_attempt
					('0:00:00', u'3*(2/3/4/5/5)')
	part1_correct_attempt
					['0:00:25', u'3*(1+(1/2)+(1/3)+(1/4)+(1/5))']

59 Student ID:mbl003

	first_attempt
					2015-11-05 20:55:42
	part1_incorrect_attempt
					('0:00:00', u'1/5')
					('0:00:45', u'7/1+7/4+7/9+7/16+7/25')
					('0:01:02', u'7/1+7/4+7/9+7/16+7/25')
					('0:01:26', u'7/1+7/4+7/9+7/16+7/25')
					('0:01:32', u'7/1+7/4+7/9+7/16+7/25')
					('0:01:51', u'7/1+7/4+7/9+7/16+7/25')
					('0:02:05', u'7/1+7/4+7/9+7/16+7/25')
	part1_correct_attempt
					['0:04:55', u'1/1+1/2+1/3+1/4+1/5']

60 Student ID:agoldsht

	first_attempt
					2015-11-04 19:46:32
	part1_incorrect_attempt
					('0:00:00', u'1/5')
	part1_correct_attempt
					['0:06:13', u'(1/1+1/2+1/3+1/4+1/5)']

61 Student ID:jeqin

	first_attempt
					2015-11-05 10:00:34
	part1_incorrect_attempt
					('0:00:00', u'(1 + 1/2 + 1/3 + 1/4 + 1/5)/5')
	part1_correct_attempt
					['0:00:10', u'(1 + 1/2 + 1/3 + 1/4 + 1/5)']

62 Student ID:jnatale

	first_attempt
					2015-11-04 08:33:21
	part1_incorrect_attempt
					('0:00:00', u'2/5')
					('0:03:32', u'2/1 + 2/2 + 2/3 + 2/3 + 2/4 + 2/5')
	part1_correct_attempt
					['0:10:13', u'2*(1/1 + 1/2 + 1/3 + 1/4 + 1/5)']

63 Student ID:nnh002

	first_attempt
					2015-11-05 04:31:46
	part1_incorrect_attempt
					('0:00:00', u'2/5')
					('0:02:34', u'(2+1+.5+(2/3)+(2/5))/5')
	part1_correct_attempt
					['0:23:15', u'(2+1+.5+(2/3)+(2/5))']

64 Student ID:beerye28

	first_attempt
					2015-11-03 06:30:37
	part1_incorrect_attempt
					('0:00:00', u'(3 + (3/2) + 1 + (3/4) + (3/5))/5')
	part1_correct_attempt
					['0:02:16', u'3 * ((1) + (1/2) + (1/3) + (1/4) + (1/5))']

65 Student ID:agian

	first_attempt
					2015-11-07 00:22:35
	part1_incorrect_attempt
					('0:00:00', u'(1+1/2+1/3+1/4+1/5)*1')
					('0:01:02', u'(1+1/2+1/3+1/4+1/5)*7')
					('0:01:07', u'(1+1/2+1/3+1/4+1/5)*72')
	part1_correct_attempt
					['0:01:11', u'(1+1/2+1/3+1/4+1/5)*2']

66 Student ID:aakumar

	first_attempt
					2015-11-05 03:06:10
	part1_incorrect_attempt
					('0:00:00', u'3+37/30')
	part1_correct_attempt
					['0:01:48', u'2+1+2/3+2/4+2/5']

67 Student ID:kew017

	first_attempt
					2015-11-05 22:44:19
	part1_incorrect_attempt
					('0:00:00', u'4/5')
	part1_correct_attempt
					['0:04:43', u'4+2+4/3+1+4/5']

68 Student ID:yeh013

	first_attempt
					2015-11-04 07:25:53
	part1_incorrect_attempt
					('0:00:00', u'284/150')
					('0:03:56', u'4/15')
	part1_correct_attempt
					['20:06:00', u'137/15']

69 Student ID:haliew

	first_attempt
					2015-11-06 23:08:56
	part1_incorrect_attempt
					('0:00:00', u'((2/1)+(2/2)+(2/3)+(2/4)+(2/5))/5')
	part1_correct_attempt
					['1:13:45', u'(2/1)+(2/2)+(2/3)+(2/4)+(2/5)']

70 Student ID:ksrijong

	first_attempt
					2015-11-04 23:09:16
	part1_incorrect_attempt
					('0:00:00', u'(4/5)(4/6)/(2)')
	part1_correct_attempt
					['0:00:50', u'4+2+4/3+1+4/5']

71 Student ID:azkong

	first_attempt
					2015-11-06 20:04:08
	part1_incorrect_attempt
					('0:00:00', u'6+6/4+6/9+6/16+6/25')
					('0:00:38', u'6+6/4+6/9+6/16+6/25')
					('0:00:00', u'6+6/4+6/9+6/16+6/25')
					('0:00:31', u'6+6/4+6/9+6/16+6/25')
					('0:00:45', u'6+6/4+6/9+6/16+6/25')
					('0:03:30', u'1+1/2+1/3+1/4+1/5')
	part1_correct_attempt
					['2:04:23', u'5+5/2+5/3+5/4+5/5']

72 Student ID:yhhan

	first_attempt
					2015-11-06 23:48:50
	part1_incorrect_attempt
					('0:00:00', u'(5+5/2+5/3+5/4+1)/5')
	part1_correct_attempt
					['0:01:20', u'5+5/2+5/3+5/4+1']

73 Student ID:volim

	first_attempt
					2015-11-04 23:23:54
	part1_incorrect_attempt
					('0:00:00', u'(1+(1/2)+(1/3)+(1/4)+(1/5))/5')
	part1_correct_attempt
					['0:00:14', u'(1+(1/2)+(1/3)+(1/4)+(1/5))']

74 Student ID:aurodrig

	first_attempt
					2015-11-06 22:55:26
	part1_incorrect_attempt
					('0:00:00', u'(1+1/2+1/3+1/4+1/5)/5')
					('0:00:00', u'1/5')
	part1_correct_attempt
					['0:14:12', u'1 + 1/2+1/3+1/4+1/5']

75 Student ID:cagatep

	first_attempt
					2015-11-05 07:30:04
	part1_incorrect_attempt
					('0:00:00', u'(1 + 1/2 + 1/3 + 1/4 + 1/5)/5')
	part1_correct_attempt
					['0:00:26', u'(1 + 1/2 + 1/3 + 1/4 + 1/5)']

76 Student ID:masaro

	first_attempt
					2015-11-03 23:08:39
	part1_incorrect_attempt
					('0:00:00', u'2.8333')
					('0:06:14', u'2.8333/5')
					('0:00:00', u'6/1+6/4+6/9+6/16+6/25')
					('0:02:23', u'(1+1/2+1/3+1/4+1/5)/5')
					('0:00:00', u'(1+1/2+1/3+1/4+1/5)*1/5')
					('0:00:00', u'(15)/5')
	part1_correct_attempt
					['21:41:15', u'1+1/2+1/3+1/4+1/5']

77 Student ID:dmn009

	first_attempt
					2015-11-05 03:32:21
	part1_incorrect_attempt
					('0:00:00', u'1.13333')
	part1_correct_attempt
					['0:00:56', u'9.133333']

78 Student ID:yig015

	first_attempt
					2015-11-05 10:40:36
	part1_incorrect_attempt
					('0:00:00', u'1.37')
	part1_correct_attempt
					['0:00:35', u'6.85']

79 Student ID:jfalcone

	first_attempt
					2015-11-05 05:27:40
	part1_incorrect_attempt
					('0:00:00', u'1/5')
					('0:00:29', u'[1 + (1/2) + (1/3) + (1/4) + (1/5)]/5')
	part1_correct_attempt
					['0:01:47', u'1 + (1/2) + (1/3) + (1/4) + (1/5)']

80 Student ID:rohan

	first_attempt
					2015-11-07 00:03:46
	part1_incorrect_attempt
					('0:00:00', u'3/5')
					('0:00:36', u'45/5')
	part1_correct_attempt
					['0:01:42', u'3+3/2+3/3+3/4+3/5']

81 Student ID:spw006

	first_attempt
					2015-11-04 02:40:13
	part1_incorrect_attempt
					('0:00:00', u'5 + 4 + 3 + 2 + 1')
					('0:00:09', u'(5 + 4 + 3 + 2 + 1)/5')
					('0:01:17', u'(5 + 5/2 + 5/3 + 5/2 + 1)/5')
					('0:01:22', u'(5 + 5/2 + 5/3 + 5/2 + 1)')
	part1_correct_attempt
					['0:01:41', u'(5 + 5/2 + 5/3 + 5/4 + 1)']

82 Student ID:any027

	first_attempt
					2015-11-01 20:31:59
	part1_incorrect_attempt
					('0:00:00', u'(4 + 2 + 4/3 + 1 + 4/5 ) / 5')
	part1_correct_attempt
					['0:00:07', u'(4 + 2 + 4/3 + 1 + 4/5 )']

83 Student ID:rwthomps

	first_attempt
					2015-11-06 21:36:09
	part1_incorrect_attempt
					('0:00:00', u'(5/1 + 5/2 + 5/3 + 5/4 + 5/5)/5')
	part1_correct_attempt
					['0:00:12', u'(5/1 + 5/2 + 5/3 + 5/4 + 5/5)']

84 Student ID:pcdo

	first_attempt
					2015-11-02 18:48:58
	part1_incorrect_attempt
					('0:00:00', u'(1+1/2+1/3+1/4+1/5)')
	part1_correct_attempt
					['0:00:43', u'3*(1+1/2+1/3+1/4+1/5)']

85 Student ID:vsosnovs

	first_attempt
					2015-11-05 21:15:09
	part1_incorrect_attempt
					('0:00:00', u'(1+2+3+4+5)/5')
					('0:00:00', u'.5')
					('0:00:00', u'2.5')
					('0:00:00', u'(1+.5+1/3+1/4+1/5)/5')

86 Student ID:k5law

	first_attempt
					2015-11-04 07:58:48
	part1_incorrect_attempt
					('0:00:00', u'[(5/1)+(5/2)+(5/3)+(5/4)+(5/5)]/5')
	part1_correct_attempt
					['0:00:22', u'[(5/1)+(5/2)+(5/3)+(5/4)+(5/5)]']

87 Student ID:p4kumar

	first_attempt
					2015-11-06 00:06:16
	part1_incorrect_attempt
					('0:00:00', u'(3/1 + 3/2 + 3/3 + 3/4 + 3/5)/5')
	part1_correct_attempt
					['0:00:07', u'(3/1 + 3/2 + 3/3 + 3/4 + 3/5)']

88 Student ID:jmiclat

	first_attempt
					2015-11-06 09:01:17
	part1_incorrect_attempt
					('0:00:00', u'2/5')
	part1_correct_attempt
					['0:28:19', u'2/1+2/2+2/3+2/4+2/5']

89 Student ID:syc078

	first_attempt
					2015-11-05 03:29:15
	part1_incorrect_attempt
					('0:00:00', u'1/5')
					('0:00:00', u'1+2+3+4+5')
	part1_correct_attempt
					['1:05:37', u'1+(1/2)+(1/3)+(1/4)+(1/5)']

90 Student ID:cfgutier

	first_attempt
					2015-11-06 18:22:54
	part1_incorrect_attempt
					('0:00:00', u'137/75')
	part1_correct_attempt
					['0:00:24', u'137/15']

91 Student ID:pnquach

	first_attempt
					2015-11-06 05:40:27
	part1_incorrect_attempt
					('0:00:00', u'(1.5 + 1/3 + 1/4 + 1/5)/5')
	part1_correct_attempt
					['0:01:10', u'1.5 + 1/3 + 1/4 + 1/5']

92 Student ID:agarango

	first_attempt
					2015-11-05 23:53:43
	part1_incorrect_attempt
					('0:00:00', u'1/5')
					('0:00:31', u'3/5')
	part1_correct_attempt
					['0:01:42', u'(1/1)+(1/2)+(1/3)+(1/4)+(1/5)']

93 Student ID:s6deng

	first_attempt
					2015-11-05 07:24:12
	part1_incorrect_attempt
					('0:00:00', u'3/15')
					('0:01:08', u'(3/1)+(3/1)+(3/3)+(3/4)+(3/5)')
	part1_correct_attempt
					['0:01:14', u'(3/1)+(3/2)+(3/3)+(3/4)+(3/5)']

94 Student ID:achinn

	first_attempt
					2015-11-03 21:20:02
	part1_incorrect_attempt
					('0:00:00', u'(7+(4/3)+(4/5))/5')
	part1_correct_attempt
					['0:01:10', u'(7+(4/3)+(4/5))']

95 Student ID:jcl084

	first_attempt
					2015-11-02 19:41:43
	part1_incorrect_attempt
					('0:00:00', u'4/5')
					('0:01:52', u'(4/1 + 4/2 + 4/3 +4/4 + 4/5)/5')
	part1_correct_attempt
					['0:58:38', u'4*(1+1/2+1/3+1/4+1/5)']

96 Student ID:aalhaida

	first_attempt
					2015-11-05 23:43:21
	part1_incorrect_attempt
					('0:00:00', u'3/1 + 3/2 + 3/4 + 3/5')
	part1_correct_attempt
					['0:00:15', u'3/1 + 3/2 + 3/3 + 3/4 + 3/5']

97 Student ID:jdeon

	first_attempt
					2015-11-04 23:19:51
	part1_incorrect_attempt
					('0:00:00', u'(1+1/2+1/3+1/4+1/5)/5')
	part1_correct_attempt
					['0:00:12', u'(1+1/2+1/3+1/4+1/5)']

98 Student ID:b1yao

	first_attempt
					2015-11-03 08:08:42
	part1_incorrect_attempt
					('0:00:00', u'(1+1/2+1/3+1/4+1/5)*3/5')
					('0:01:01', u'(3+3/2+3/3+3/4+3/5)/5')
	part1_correct_attempt
					['1 day, 11:05:59', u'(3+3/2+3/3+3/4+3/5)']

99 Student ID:ajabasa

	first_attempt
					2015-11-05 21:44:30
	part1_incorrect_attempt
					('0:00:00', u'(1/1+1/2+1/3+1/4+1/5)/5')
	part1_correct_attempt
					['0:03:08', u'(1/1+1/2+1/3+1/4+1/5)']

100 Student ID:mcatozzi

	first_attempt
					2015-11-03 19:28:10
	part1_incorrect_attempt
					('0:00:00', u'(2+1+(2/3)+(2/4)+(2/5))/5')
					('0:00:26', u'2/5')
					('0:00:42', u'(2+1+(2/3)+(2/4)+(2/5))/5')
					('0:01:42', u'(2+1+(2/3)+(2/4)+(2/5))/15')
	part1_correct_attempt
					['0:02:10', u'(2+1+(2/3)+(2/4)+(2/5))']

101 Student ID:hmshah

	first_attempt
					2015-11-05 09:40:18
	part1_incorrect_attempt
					('0:00:00', u'6/25')
	part1_correct_attempt
					['0:00:42', u'2 + 1 + 2/3 + 2/4 + 2/5']

102 Student ID:dtea

	first_attempt
					2015-11-07 00:17:45
	part1_incorrect_attempt
					('0:00:00', u'(4/1+4/2+4/3+4/4+4/5)/5')
	part1_correct_attempt
					['0:00:52', u'(4/1+4/2+4/3+4/4+4/5)']

103 Student ID:mtrafeca

	first_attempt
					2015-11-02 01:49:53
	part1_incorrect_attempt
					('0:00:00', u'6^.5')
					('0:00:22', u'1/6')
					('0:00:30', u'1/5')
					('0:05:12', u'35/7')
					('0:06:23', u'(1+1/2+1/3+1/4+1/5)/5')
					('0:07:07', u'(1+2+3+4+5)/5')
					('0:19:13', u'6/5')
					('0:19:28', u'1/5')
	part1_correct_attempt
					['2 days, 22:30:20', u'1+1/2+1/3+1/4+1/5']

104 Student ID:edcole

	first_attempt
					2015-11-06 23:34:39
	part1_incorrect_attempt
					('0:00:00', u'3/5')
					('0:00:18', u'3/(1+2+3+4+5)')
					('0:00:39', u'15/(1+2+3+4+5)')
					('0:01:20', u'1+(3/2)+3/3+3/4+3/5')
	part1_correct_attempt
					['0:05:35', u'3+(3/2)+3/3+3/4+3/5']

105 Student ID:aordookh

	first_attempt
					2015-11-04 22:07:09
	part1_incorrect_attempt
					('0:00:00', u'4/5')
					('0:05:36', u'(4/1)+(4/2)+(4/3)+(4/4)+(5/4)')
	part1_correct_attempt
					['0:06:41', u'(4/1)+(4/2)+(4/3)+(4/4)+(4/5)']

106 Student ID:kquong

	first_attempt
					2015-11-02 04:52:54
	part1_incorrect_attempt
					('0:00:00', u'(4 + 2 + 4/3 + 1 + 4/5)/5')
					('0:01:18', u'4/5')
					('0:23:10', u'(4 + 2 + 4/3 + 1 + 4/5)/5')
	part1_correct_attempt
					['0:23:20', u'(4 + 2 + 4/3 + 1 + 4/5)']

107 Student ID:xweng

	first_attempt
					2015-11-06 00:07:59
	part1_incorrect_attempt
					('0:00:00', u'11*5/12')
					('0:00:00', u'11*12+5/12')
	part1_correct_attempt
					['0:00:34', u'(11*12+5)/12']

108 Student ID:yypan

	first_attempt
					2015-11-03 00:25:03
	part1_incorrect_attempt
					('0:00:00', u'(1+2+3+4+5)/5')
					('0:00:38', u'(5/1+5/2+5/3+5/4+5/5)/5')
	part1_correct_attempt
					['0:00:47', u'(5/1+5/2+5/3+5/4+5/5)']

109 Student ID:zig006

	first_attempt
					2015-11-01 20:17:01
	part1_incorrect_attempt
					('0:00:00', u'137/150')
	part1_correct_attempt
					['0:00:42', u'137/30']

110 Student ID:sthapa

	first_attempt
					2015-11-06 23:59:10
	part1_incorrect_attempt
					('0:00:00', u'(1+1/2+1/3+1/4+1/5)*1')
	part1_correct_attempt
					['0:00:28', u'(1+1/2+1/3+1/4+1/5)*3']

111 Student ID:gsrandha

	first_attempt
					2015-11-05 08:03:56
	part1_incorrect_attempt
					('0:00:00', u'(3 + 1.5 + 1 + .75 + .6)/5')
					('0:05:15', u'10/1 + 10/4 + 10/9 + 10/16 + 10/25')
	part1_correct_attempt
					['0:05:51', u'3/1 + 3/2 + 1+ 3/4 + 3/5']

112 Student ID:j2phung

	first_attempt
					2015-11-05 08:54:49
	part1_incorrect_attempt
					('0:00:00', u'2/5')
					('0:00:47', u'(2/1+2/2+2/3+2/4+2/5)/5')
	part1_correct_attempt
					['0:27:35', u'(2/1+2/2+2/3+2/4+2/5)']












## Part 2

### (27) Mistake Group ['R.0'] of size 27
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|7*(1+1/4+1/9+1/16+1/25)	|7/25	|[('R.0', 7.0, u'7', u'7')]	|
|1	|10*(1+1/4+1/9+1/16+1/25)	|10/25	|[('R.0', 10.0, u'10', u'10')]	|
|2	|6*(1+1/4+1/9+1/16+1/25)	|6/32	|[('R.0', 6.0, u'6', u'6')]	|
|3	|10*(1+1/4+1/9+1/16+1/25)	|10/5^2	|[('R.0', 10.0, u'10', u'10')]	|
|4	|6*(1+1/4+1/9+1/16+1/25)	|6/25	|[('R.0', 6.0, u'6', u'6')]	|
|5	|10*(1+1/4+1/9+1/16+1/25)	|10/(5^2)	|[('R.0', 10.0, u'10', u'10')]	|
|6	|6*(1+1/4+1/9+1/16+1/25)	|6/30	|[('R.0', 6.0, u'6', u'6')]	|
|7	|7*(1+1/4+1/9+1/16+1/25)	|7/5^2	|[('R.0', 7.0, u'7', u'7')]	|
|8	|8*(1+1/4+1/9+1/16+1/25)	|8/4^2	|[('R.0', 8.0, u'8', u'8')]	|
|9	|8*(1+1/4+1/9+1/16+1/25)	|8/25	|[('R.0', 8.0, u'8', u'8')]	|
|10	|8*(1+1/4+1/9+1/16+1/25)	|8/(5^2)	|[('R.0', 8.0, u'8', u'8')]	|
|11	|8*(1+1/4+1/9+1/16+1/25)	|8/5^2	|[('R.0', 8.0, u'8', u'8')]	|
|12	|6*(1+1/4+1/9+1/16+1/25)	|6/(1+4+9+16+25)	|[('R.0', 6.0, u'6', u'6')]	|
|13	|6*(1+1/4+1/9+1/16+1/25)	|6*(1+1/2+1/3+1/4+1/5)	|[('R.0', 6.0, u'6', u'6')]	|
|14	|7*(1+1/4+1/9+1/16+1/25)	|7/(1+2^2 + 3^2 + 4^2 + 5^2)	|[('R.0', 7.0, u'7', u'7')]	|
|15	|8*(1+1/4+1/9+1/16+1/25)	|8/5**2	|[('R.0', 8.0, u'8', u'8')]	|
|16	|7*(1+1/4+1/9+1/16+1/25)	|7/16	|[('R.0', 7.0, u'7', u'7')]	|
|17	|10*(1+1/4+1/9+1/16+1/25)	|10*(1/1 + 1/2 + 1/3 + 1/4 + 1/5)	|[('R.0', 10.0, u'10', u'10')]	|
|18	|10*(1+1/4+1/9+1/16+1/25)	|10/(1 + 1/2+1/3+1/4+1/5)^2	|[('R.0', 10.0, u'10', u'10')]	|
|19	|10*(1+1/4+1/9+1/16+1/25)	|10/2.83^2	|[('R.0', 10.0, u'10', u'10')]	|




### (15) Mistake Group redirect of size 15




### (5) Mistake Group Digits of size 5




### (2) Mistake Group ['R.1.1'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|10*(1+1/4+1/9+1/16+1/25)	|10/(1^2) + 10/((1/2)^2) + 10/((1/3)^2) + 10/((1/4)^2) + 10/((1/5)^2)	|[('R.1.1', 0.04, u'1/25', u'(1/5)^2')]	|
|1	|10*(1+1/4+1/9+1/16+1/25)	|10/(1^2) - 10/((1/2)^2) + 10/((1/3)^2) - 10/((1/4)^2) + 10/((1/5)^2)	|[('R.1.1', 0.04, u'1/25', u'(1/5)^2')]	|




### (2) Mistake Group Wrong_Sign of size 2




### (1) Mistake Group ['R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|8*(1+1/4+1/9+1/16+1/25)	|5*(1 + 1/4 + 1/9 + 1/16 + 1/25)	|[('R.1', 1.4636111111111112, u'1+1/4+1/9+1/16+1/25', u'1 + 1/4 + 1/9 + 1/16 + 1/25')]	|




### (1) Mistake Group ['R.0', 'R.1.0.0.0.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1.0.0.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|10*(1+1/4+1/9+1/16+1/25)	|10/((1 + 1/2+1/3+1/4+1/5)^2)^2	|[('R.0', 10.0, u'10', u'10'), ('R.1.0.0.0.1', 0.25, u'1/4', u'1/4')]	|




### (1) Mistake Group ['R.0', 'R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|10*(1+1/4+1/9+1/16+1/25)	|10/((1^2 + (1/2)^2+(1/3)^2+(1/4)^2+(1/5)^2))	|[('R.0', 10.0, u'10', u'10'), ('R.1', 1.4636111111111112, u'1+1/4+1/9+1/16+1/25', u'1^2 + (1/2)^2+(1/3)^2+(1/4)^2+(1/5)^2')]	|




### (25) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:b3hwang

	first_attempt
					2015-11-05 08:50:27
	part1_correct_attempt
					['0:00:00', u'(4/1) + 4/2 + 4/3 + 4/4 + 4/5']
	part2_incorrect_attempt
					('0:00:30', u'(4/1)^2 + (4/2)^2 + (4/3)^2 + (4/4)^2 + (4/5)^2')
					('0:00:40', u'((4/1)^2 + (4/2)^2 + (4/3)^2 + (4/4)^2 + (4/5)^2)/5')
					('0:04:43', u'((9/1)+ (9/2^2) + (9/3^2) + (4/4^2) + (4/5^2))/5')
					('0:05:09', u'((9/1)+ (9/2^2) + (9/3^2) + (9/4^2) + (9/5^2))/5')
	part2_correct_attempt
					['0:05:18', u'((9/1)+ (9/2^2) + (9/3^2) + (9/4^2) + (9/5^2))']

1 Student ID:apokhare

	first_attempt
					2015-11-05 21:40:12
	part1_correct_attempt
					['0:00:00', u'(1+1/2+1/3+1/4+1/5)*3']
	part2_incorrect_attempt
					('0:00:00', u'(1+1/2+1/3+1/4+1/5)*6')
	part2_correct_attempt
					['0:00:54', u'(1+1/4+1/9+1/16+1/25)*6']

2 Student ID:achava

	first_attempt
					2015-11-06 07:27:32
	part1_correct_attempt
					['0:00:00', u'3+(3/2)+(1)+(3/4)+(3/5)']
	part2_incorrect_attempt
					('0:01:09', u'8+(8/2)+(8/9)+(8/16)+(8/25)')
	part2_correct_attempt
					['0:31:45', u'8+(8/4)+(8/9)+(8/16)+(8/25)']

3 Student ID:mhale

	first_attempt
					2015-11-05 20:22:12
	part1_correct_attempt
					['0:00:00', u'1 + 1/2 + 1/3 + 1/4 + 1/5']
	part2_incorrect_attempt
					('0:00:20', u'6 + 6/2 + 6/9 + 6/16 + 6/25')
	part2_correct_attempt
					['0:00:30', u'6 + 6/4 + 6/9 + 6/16 + 6/25']

4 Student ID:k5law

	first_attempt
					2015-11-04 07:59:10
	part1_correct_attempt
					['0:00:00', u'[(5/1)+(5/2)+(5/3)+(5/4)+(5/5)]']
	part2_incorrect_attempt
					('0:00:12', u'[(5/1)+(5/2)+(5/3)+(5/4)+(5/5)]^2')
					('0:04:33', u'[((5/1)-(11.4167))^2]+[((5/2)-(11.4167))^2]+[((5/3)-(11.4167))^2]+[((5/4)-(11.4167))^2]+[((5/5)-(11.4167))^2]')
					('0:04:56', u'[[((5/1)-(11.4167))^2]+[((5/2)-(11.4167))^2]+[((5/3)-(11.4167))^2]+[((5/4)-(11.4167))^2]+[((5/5)-(11.4167))^2]]/5')
	part2_correct_attempt
					['0:09:26', u'(7/((1)^2))+(7/((2)^2))+(7/((3)^2))+(7/((4)^2))+(7/((5)^2))']

5 Student ID:dan029

	first_attempt
					2015-11-05 09:09:59
	part1_correct_attempt
					['0:00:00', u'137/60']
	part2_incorrect_attempt
					('0:01:46', u'.2641')
	part2_correct_attempt
					['0:02:23', u'6+6/4+6/9+6/16+6/25']

6 Student ID:jeqin

	first_attempt
					2015-11-05 10:00:44
	part1_correct_attempt
					['0:00:00', u'(1 + 1/2 + 1/3 + 1/4 + 1/5)']
	part2_incorrect_attempt
					('0:00:33', u'1 + 8/4 + 8/9 + 8/16 + 8/25')
	part2_correct_attempt
					['0:01:06', u'8*(1+1/4+1/9+1/16+1/25)']

7 Student ID:agarango

	first_attempt
					2015-11-05 23:55:25
	part1_correct_attempt
					['0:00:00', u'(1/1)+(1/2)+(1/3)+(1/4)+(1/5)']
	part2_incorrect_attempt
					('0:00:38', u'(1/1)+(1/4)+(1/9)+(1/16)+(1/25)')
	part2_correct_attempt
					['0:00:53', u'(7/1)+(7/4)+(7/9)+(7/16)+(7/25)']

8 Student ID:avasavad

	first_attempt
					2015-11-04 23:13:33
	part1_correct_attempt
					['0:00:00', u'5 + 5/2 + 5/3 + 5/4 + 1']
	part2_incorrect_attempt
					('0:00:31', u'10 + 10/2 + 10/9 + 10/16 + 10/25')
	part2_correct_attempt
					['0:00:39', u'10 + 10/4 + 10/9 + 10/16 + 10/25']

9 Student ID:btn023

	first_attempt
					2015-11-06 10:51:15
	part1_correct_attempt
					['0:00:00', u'1/5+1/4+1/3+1/2+1/1']
	part2_incorrect_attempt
					('0:01:03', u'8/1+8/4+8/8+8/16+8/32')
	part2_correct_attempt
					['0:02:13', u'8/1+8/4+8/9+8/16+8/25']

10 Student ID:dwzhang

	first_attempt
					2015-11-04 20:59:44
	part1_correct_attempt
					['0:00:00', u'3/1 + 3/2 + 3/3 + 3/4 + 3/5']
	part2_incorrect_attempt
					('0:00:15', u'7/1 + 7/2 + 7/3 + 7/4 + 7/5')
	part2_correct_attempt
					['0:00:31', u'7/1 + 7/4 + 7/9 + 7/16 + 7/25']

11 Student ID:agian

	first_attempt
					2015-11-07 00:23:46
	part1_correct_attempt
					['0:00:00', u'(1+1/2+1/3+1/4+1/5)*2']
	part2_incorrect_attempt
					('0:00:15', u'(1+1/2+1/3+1/4+1/5)*10')
	part2_correct_attempt
					['0:00:37', u'(1+1/4+1/9+1/16+1/25)*10']

12 Student ID:dgunawan

	first_attempt
					2015-11-05 08:39:09
	part1_correct_attempt
					['0:00:00', u'1 + 1/2 + 1/3 + 1/4 + 1/5 ']
	part2_incorrect_attempt
					('0:00:00', u'(1/1^2) + (1/2^2) + (1/3^2) + (1/4^2) + (1/5^2)')
	part2_correct_attempt
					['0:01:31', u'(8/1^2) + (8/2^2) + (8/3^2) + (8/4^2) + (8/5^2)']

13 Student ID:dsmonaha

	first_attempt
					2015-11-02 17:23:41
	part1_correct_attempt
					['0:00:00', u'137/12']
	part2_incorrect_attempt
					('0:01:49', u'3019/600')
	part2_correct_attempt
					['0:04:43', u'5269/600']

14 Student ID:akalathi

	first_attempt
					2015-11-04 06:24:24
	part1_correct_attempt
					['0:00:00', u'4/1 + 4/2 + 4/3 + 4/4 + 4/5']
	part2_incorrect_attempt
					('0:00:17', u'7/1 + 7/2 + 7/3 + 7/4 + 7/5')
					('0:00:57', u'7 + 7/14 + 7/21 + 7/28 + 7/35')
	part2_correct_attempt
					['0:02:21', u'7 + 7/4 + 7/9 + 7/16 + 7/25']

15 Student ID:c1wei

	first_attempt
					2015-11-04 06:50:40
	part1_correct_attempt
					['0:00:00', u'(3+(3/2)+1+3/4+3/5)']
	part2_incorrect_attempt
					('0:00:00', u'6/1+6/2+6/3+6/4+6/5')
	part2_correct_attempt
					['0:00:48', u'6/1+6/4+6/9+6/16+6/25']

16 Student ID:csl030

	first_attempt
					2015-11-06 00:15:22
	part1_correct_attempt
					['0:00:00', u'(3/1 + 3/2 + 3/3 + 3/4 + 3/5)']
	part2_incorrect_attempt
					('0:00:40', u'6/1^2 + 6/2^2 + 6/3^2 + 6/4^4 + 6/5^2')
					('0:02:54', u'(6/1^2 - 6.85)^2 + (6/2^2- 6.85)^2  + (6/3^- 6.85)^2 + (6/4^4- 6.85)^2  + (6/5^2- 6.85)^2')
					('0:03:29', u'(6/1^2 - 6.85)^2 + (6/2^2- 6.85)^2 + (6/3^2- 6.85)^2 + (6/4^4- 6.85)^2 + (6/5^2- 6.85)^2')
					('0:05:29', u'((6/1^2 - 6.85)^2 + (6/2^2- 6.85)^2 + (6/3^2- 6.85)^2 + (6/4^4- 6.85)^2 + (6/5^2- 6.85)^2) / 5')

17 Student ID:eshung

	first_attempt
					2015-11-05 23:07:39
	part1_correct_attempt
					['0:00:00', u'1+0.5+0.25+(1/3)+0.2']
	part2_incorrect_attempt
					('0:00:00', u'7+3.5+(7/9)+(7/16)+(7/25)')
	part2_correct_attempt
					['0:00:09', u'7+(7/4)+(7/9)+(7/16)+(7/25)']

18 Student ID:ralhadda

	first_attempt
					2015-10-31 20:35:01
	part1_correct_attempt
					['0:00:00', u'2.283333']
	part2_incorrect_attempt
					('0:01:04', u'1.91805')
					('0:01:39', u'0.0444444')
	part2_correct_attempt
					['0:03:56', u'14.63611']

19 Student ID:yjshin

	first_attempt
					2015-11-06 23:12:54
	part1_correct_attempt
					['0:00:00', u'4/5+4/4+4/3+4/2+4/1']
	part2_incorrect_attempt
					('0:00:34', u'(4/5)^2+(1)+(4/3)^2+(4/2)^2+(4/1)^2')
					('0:00:50', u'(4/5+4/4+4/3+4/2+4/1)^2')
					('0:01:33', u'(4/5)^2+(4/4)^2+(4/3)^2+(4/2)^2+(4/1)^2')
					('0:02:34', u'(4/5-4/4)^2+(1-4/3)^2+(4/3-4/2)^2+(4/2-4/1)^2')
					('0:02:59', u'(4/5-4/4)^2+(1-4/3)^2+(4/3-4/2)^2+(4/2-4/1)^2+4^2')
	part2_correct_attempt
					['0:04:15', u'(8/1)+(8/4)+(8/9)+(8/16)+(8/25)']

20 Student ID:vasharma

	first_attempt
					2015-11-04 18:56:53
	part1_correct_attempt
					['0:00:00', u'3/1+3/2+3/3+3/4+3/5']
	part2_incorrect_attempt
					('0:03:18', u'8/1+8/4+8/16+8/32+8/64')
	part2_correct_attempt
					['0:03:41', u'8/1+8/4+8/9+8/16+8/25']

21 Student ID:cagatep

	first_attempt
					2015-11-05 07:30:30
	part1_correct_attempt
					['0:00:00', u'(1 + 1/2 + 1/3 + 1/4 + 1/5)']
	part2_incorrect_attempt
					('0:00:12', u'(8 + 2 + 1 + 1/2 + 1/4)/5')
	part2_correct_attempt
					['0:00:39', u'(8 + 2 + 8/9 + 1/2 + 8/25)']

22 Student ID:aurodrig

	first_attempt
					2015-11-06 23:09:38
	part1_correct_attempt
					['0:00:00', u'1 + 1/2+1/3+1/4+1/5']
	part2_incorrect_attempt
					('0:03:28', u'2.83^2')
	part2_correct_attempt
					['0:12:57', u'10/(1^2) + 10/((2)^2) + 10/((3)^2) + 10/((4)^2) + 10/((5)^2)']

23 Student ID:yil035

	first_attempt
					2015-11-04 00:43:35
	part1_correct_attempt
					['0:00:00', u'1.82666667*5']
	part2_incorrect_attempt
					('0:02:10', u'6169/450')
	part2_correct_attempt
					['0:03:11', u'5269/450']

24 Student ID:m8woo

	first_attempt
					2015-11-05 21:03:09
	part1_correct_attempt
					['0:00:00', u'[3/1 + 3/2 + 3/3 + 3/4 + 3/5]']
	part2_incorrect_attempt
					('0:00:00', u'[3/1 + 3/4 + 3/9 + 3/16 + 3/25]')
	part2_correct_attempt
					['0:00:47', u'[10/1 + 10/4 + 10/9 + 10/16 + 10/25]']












## Part 3

### (6) Mistake Group Digits of size 6




### (5) Mistake Group Wrong_Sign of size 5




### (2) Mistake Group ['R.1.0.0.1', 'R.1.0.1', 'R.1.1'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.0.0.1', 'R.1.0.1', 'R.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|2*(1-1/2+1/3-1/4+1/5)	|2*(1/1 - 1/2 + 1/3 - 1/3 + 1/4 - 1/5)	|[('R.1.0.0.1', 0.3333333333333333, u'1/3', u'1/3'), ('R.1.0.1', 0.25, u'1/4', u'1/4'), ('R.1.1', 0.2, u'1/5', u'1/5')]	|
|1	|2*(1-1/2+1/3-1/4+1/5)	|2*(1/1 - 1/2 - 1/3 + 1/4 - 1/5)	|[('R.1.0.0.1', 0.3333333333333333, u'1/3', u'1/3'), ('R.1.0.1', 0.25, u'1/4', u'1/4'), ('R.1.1', 0.2, u'1/5', u'1/5')]	|




### (1) Mistake Group ['R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|1*(1-1/2+1/3-1/4+1/5)	|5*((1/1)-(1/2)+(1/3)-(1/4)+(1/5))	|[('R.1', 0.7833333333333332, u'1-1/2+1/3-1/4+1/5', u'(1/1)-(1/2)+(1/3)-(1/4)+(1/5)')]	|




### (42) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:gthorn

	first_attempt
					2015-11-05 06:52:54
	part3_incorrect_attempt
					('0:01:13', u'2-3/2-3/4+3/5')
	part3_correct_attempt
					['0:01:31', u'3/1-3/2+1-3/4+3/5']

1 Student ID:h4tu

	first_attempt
					2015-11-06 23:23:42
	part3_incorrect_attempt
					('0:01:32', u'4+2+4/3+1+4/5')
	part3_correct_attempt
					['0:01:52', u'4-2+4/3-1+4/5']

2 Student ID:apokhare

	first_attempt
					2015-11-05 21:40:12
	part3_incorrect_attempt
					('0:00:54', u'(1-1/4+1/9-1/16+1/25)*3')
	part3_correct_attempt
					['0:01:37', u'(1-1/2+1/3-1/4+1/5)*3']

3 Student ID:jfalcone

	first_attempt
					2015-11-05 05:29:27
	part3_incorrect_attempt
					('0:01:01', u'1 + (1/2) + (1/3) + (1/4) + (1/5)')
	part3_correct_attempt
					['0:01:46', u'1 - (1/2) + (1/3) - (1/4) + (1/5)']

4 Student ID:ctroncos

	first_attempt
					2015-11-05 16:54:27
	part3_incorrect_attempt
					('0:00:45', u'8*(1-1/2+1/3-1/4)')
	part3_correct_attempt
					['0:01:19', u'4*(1-1/2+1/3-1/4+1/5)']

5 Student ID:t2shin

	first_attempt
					2015-11-04 05:19:40
	part3_incorrect_attempt
					('0:01:50', u'4+2+(4/3)+1+(4/5)')
	part3_correct_attempt
					['0:02:03', u'4-2+(4/3)-1+(4/5)']

6 Student ID:quwong

	first_attempt
					2015-11-03 21:05:49
	part3_incorrect_attempt
					('-5 days, 4:39:16', u'0.78333')
	part3_correct_attempt
					['-1 day, 23:57:34', u'5(1 - 1/2 + 1/3 - 1/4 + 1/5)']

7 Student ID:hkhodada

	first_attempt
					2015-11-03 00:32:21
	part3_incorrect_attempt
					('-3 days, 16:24:43', u'3019/360')
	part3_correct_attempt
					['0:00:00', u'4-4/2+4/3-4/4+4/5']

8 Student ID:ssamudra

	first_attempt
					2015-11-05 06:16:59
	part3_incorrect_attempt
					('0:05:00', u'1/5 + 1/4 + 1/3 + 1/2 + 1')
	part3_correct_attempt
					['0:05:12', u'1/5 - 1/4 + 1/3 - 1/2 + 1']

9 Student ID:skarimik

	first_attempt
					2015-11-01 18:30:57
	part3_incorrect_attempt
					('-1 day, 23:54:15', u'7-7/4+7/9-7/16+7/25')
					('-1 day, 23:56:13', u'7+7/4+7/9+7/16+7/25')
					('-1 day, 23:56:28', u'7+7/4+7/9+7/16+7/25')
	part3_correct_attempt
					['0:06:15', u'5-5/2+5/3-5/4+1']

10 Student ID:sachadal

	first_attempt
					2015-11-05 20:07:32
	part3_incorrect_attempt
					('0:00:18', u'(1/1)+(1/2)+(1/3)+(1/4)+(1/5)')
	part3_correct_attempt
					['0:00:37', u'(1/1)-(1/2)+(1/3)-(1/4)+(1/5)']

11 Student ID:krau

	first_attempt
					2015-11-05 03:08:39
	part3_incorrect_attempt
					('-1 day, 17:24:37', u'(1/1-1/2+1/3-1/4+1/5) / 5')
	part3_correct_attempt
					['0:00:22', u'1-1/2+1/3-1/4+1/5']

12 Student ID:dcrume

	first_attempt
					2015-11-06 20:30:24
	part3_incorrect_attempt
					('0:01:52', u'3/1 - 3/3 + 3/3 - 3/4 + 3/5')
	part3_correct_attempt
					['0:03:45', u'3/1 - 3/2 + 3/3 - 3/4 + 3/5']

13 Student ID:alhung

	first_attempt
					2015-11-06 23:25:00
	part3_incorrect_attempt
					('0:00:00', u'1/1-1/2+1/3+1/4+1/5')
	part3_correct_attempt
					['0:00:24', u'1/1-1/2+1/3-1/4+1/5']

14 Student ID:mbl003

	first_attempt
					2015-11-05 21:00:37
	part3_incorrect_attempt
					('-1 day, 23:56:07', u'7/1-7/4+7/9-7/16+7/25')
					('-1 day, 23:56:31', u'7/1+7/4+7/9+7/16+7/25')
					('-1 day, 23:56:37', u'7/1+7/4+7/9+7/16+7/25')
					('-1 day, 23:56:56', u'7/1+7/4+7/9+7/16+7/25')
					('-1 day, 23:57:10', u'7/1+7/4+7/9+7/16+7/25')
					('0:00:06', u'1/1+1/2+1/3+1/4+1/5')
	part3_correct_attempt
					['0:00:17', u'1/1-1/2+1/3-1/4+1/5']

15 Student ID:agoldsht

	first_attempt
					2015-11-04 19:52:45
	part3_incorrect_attempt
					('0:03:53', u'(1/1+1/2+1/3-1/4+1/5)')
	part3_correct_attempt
					['0:04:16', u'(1/1-1/2+1/3-1/4+1/5)']

16 Student ID:j5phung

	first_attempt
					2015-11-04 04:49:51
	part3_incorrect_attempt
					('-1 day, 23:57:52', u'1/5')
	part3_correct_attempt
					['0:01:59', u'(3-3/2+3/3-3/4+3/5)']

17 Student ID:tpmach

	first_attempt
					2015-10-30 21:50:06
	part3_incorrect_attempt
					('0:01:32', u'3+(-1)^2*(3/2)+3/3+(-1)^2*(3/4)+3/5')
	part3_correct_attempt
					['0:01:53', u'3+(-1)(3/2)+3/3+(-1)(3/4)+3/5']

18 Student ID:gsrandha

	first_attempt
					2015-11-05 08:09:47
	part3_incorrect_attempt
					('0:00:09', u'3/1 + 3/2 + 1+ 3/4 + 3/5')
	part3_correct_attempt
					['0:00:20', u'3/1 - 3/2 + 1- 3/4 + 3/5']

19 Student ID:jeqin

	first_attempt
					2015-11-05 10:00:44
	part3_incorrect_attempt
					('0:01:22', u'(1 + 1/2 + 1/3 + 1/4 + 1/5)')
	part3_correct_attempt
					['0:01:40', u'(1 - 1/2 + 1/3 - 1/4 + 1/5)']

20 Student ID:r9jiang

	first_attempt
					2015-11-02 02:47:32
	part3_incorrect_attempt
					('-1 day, 23:46:53', u'0.7833')
					('-1 day, 23:58:06', u'1-1/2+1/3-1/4+1/5')
	part3_correct_attempt
					['0:00:00', u'5-5/2+5/3-5/4+5/5']

21 Student ID:nnh002

	first_attempt
					2015-11-05 04:55:01
	part3_incorrect_attempt
					('-1 day, 23:36:45', u'2/5')
					('-1 day, 23:39:19', u'(2-1-.5+(2/3)+(2/5))/5')
	part3_correct_attempt
					['0:00:59', u'(2-1-.5+(2/3)+(2/5))']

22 Student ID:ralhadda

	first_attempt
					2015-10-31 20:35:01
	part3_incorrect_attempt
					('4:05:07', u'0.1024')
	part3_correct_attempt
					['4:38:43', u'0.78333']

23 Student ID:r1gu

	first_attempt
					2015-11-05 12:10:39
	part3_incorrect_attempt
					('0:00:10', u'5+5/2+5/4+5/3+1')
	part3_correct_attempt
					['0:01:04', u'5-5/2-5/4+5/3+1']

24 Student ID:kbielawi

	first_attempt
					2015-11-06 00:50:19
	part3_incorrect_attempt
					('0:00:19', u'(5/1+5/2+5/3+5/4+5/5)')
	part3_correct_attempt
					['0:00:30', u'(5/1-5/2+5/3-5/4+5/5)']

25 Student ID:pthsu

	first_attempt
					2015-10-31 03:39:30
	part3_incorrect_attempt
					('0:00:00', u'(1-1/2+1/3-1/4+1/5)')
	part3_correct_attempt
					['0:00:08', u'3*(1-1/2+1/3-1/4+1/5)']

26 Student ID:krkelkar

	first_attempt
					2015-10-31 20:55:06
	part3_incorrect_attempt
					('0:00:00', u'5 + 5/2 + 5/3 + 5/4 + 5/5')
	part3_correct_attempt
					['0:00:33', u'5 - 5/2 + 5/3 - 5/4 + 5/5']

27 Student ID:anvan

	first_attempt
					2015-11-05 16:05:53
	part3_incorrect_attempt
					('0:00:35', u'2 - 1 + 2/3 + 1/2 + 2/5')
	part3_correct_attempt
					['0:00:45', u'2 - 1 + 2/3- 1/2 + 2/5']

28 Student ID:c1sorian

	first_attempt
					2015-11-05 00:38:57
	part3_incorrect_attempt
					('-1 day, 23:55:08', u'(3-1.5+1-.75+6)/5')
					('-1 day, 23:58:24', u'(3-1.5+1-.75+6)')
	part3_correct_attempt
					['-1 day, 23:59:03', u'((3/1)-(3/2)+(3/3)-(3/4)+(3/5))']

29 Student ID:jtfrankl

	first_attempt
					2015-11-06 18:40:52
	part3_incorrect_attempt
					('-1 day, 23:54:20', u'(1-.5+1/3-1/4+.2)/5')
	part3_correct_attempt
					['0:00:07', u'(1-.5+1/3-1/4+.2)']

30 Student ID:tdurrer

	first_attempt
					2015-11-06 05:04:36
	part3_incorrect_attempt
					('0:00:00', u'(5/1)-(5/2)+(5/3)+(5/4)+(5/5)')
	part3_correct_attempt
					['0:00:34', u'(5/1)-(5/2)+(5/3)-(5/4)+(5/5)']

31 Student ID:azkong

	first_attempt
					2015-11-06 22:08:31
	part3_incorrect_attempt
					('-1 day, 21:56:15', u'6-6/4+6/9-6/16+6/25')
					('-1 day, 23:56:05', u'6-6/4+6/9-6/16+6/25')
					('-1 day, 23:56:36', u'6+6/4+6/9+6/16+6/25')
					('-1 day, 23:56:50', u'6+6/4+6/9+6/16+6/25')
	part3_correct_attempt
					['0:00:18', u'5-5/2+5/3-5/4+5/5']

32 Student ID:aurodrig

	first_attempt
					2015-11-06 23:09:38
	part3_incorrect_attempt
					('0:10:22', u'1 + 1/2 + 1/3 + 1/4 + 1/5')
	part3_correct_attempt
					['0:11:15', u'1 - 1/2 + 1/3 - 1/4 + 1/5']

33 Student ID:aordookh

	first_attempt
					2015-11-04 22:13:50
	part3_incorrect_attempt
					('-1 day, 23:53:19', u'4/1')
					('-1 day, 23:58:55', u'(4/1)-(4/2)+(4/3)-(4/4)+(5/4)')
	part3_correct_attempt
					['0:00:00', u'(4/1)-(4/2)+(4/3)-(4/4)+(4/5)']

34 Student ID:ajvanega

	first_attempt
					2015-11-05 02:57:39
	part3_incorrect_attempt
					('0:05:20', u'4-2-(4/3)-1+(4/5)')
	part3_correct_attempt
					['0:05:29', u'4-2+(4/3)-1+(4/5)']

35 Student ID:zhw110

	first_attempt
					2015-11-06 01:00:43
	part3_incorrect_attempt
					('0:00:00', u'4-2+4/3/1+4/5')
	part3_correct_attempt
					['23:27:35', u'4-2+4/3-1+4/5']

36 Student ID:yil035

	first_attempt
					2015-11-04 00:43:35
	part3_incorrect_attempt
					('-1 day, 23:59:27', u'47/75')
	part3_correct_attempt
					['0:00:00', u'47/15']

37 Student ID:m8woo

	first_attempt
					2015-11-05 21:03:09
	part3_incorrect_attempt
					('-1 day, 23:59:00', u'[3/1 - 3/2 + 3/3 - 3/4 + 3/5]/5')
	part3_correct_attempt
					['0:00:00', u'[3/1 - 3/2 + 3/3 - 3/4 + 3/5]']

38 Student ID:mtrafeca

	first_attempt
					2015-11-05 00:20:13
	part3_incorrect_attempt
					('-3 days, 1:38:56', u'1/2')
	part3_correct_attempt
					['0:03:38', u'1-1/2+1/3-1/4+1/5']

39 Student ID:wmiao

	first_attempt
					2015-11-04 20:27:09
	part3_incorrect_attempt
					('-1 day, 23:59:46', u'(1/1-1/2+1/3-1/4+1/5)/5')
	part3_correct_attempt
					['0:00:00', u'(1/1-1/2+1/3-1/4+1/5)']

40 Student ID:pnquach

	first_attempt
					2015-11-06 05:41:37
	part3_incorrect_attempt
					('-1 day, 23:58:50', u'(1 - 1/2 + 1/3 - 1/4 + 1/5)/5')
	part3_correct_attempt
					['0:00:00', u'1 - 1/2 + 1/3 - 1/4 + 1/5']

41 Student ID:jit002

	first_attempt
					2015-11-05 04:01:38
	part3_incorrect_attempt
					('-1 day, 23:50:58', u'(5-2.5+5/3-5/4+1)/5')
	part3_correct_attempt
					['0:00:00', u'5-2.5+5/3-5/4+1']












## Part 4

### (22) Mistake Group redirect of size 22




### (5) Mistake Group ['R.0', 'R.1.0.0.0.1', 'R.1.0.0.1', 'R.1.0.1', 'R.1.1'] of size 5
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1.0.0.0.1', 'R.1.0.0.1', 'R.1.0.1', 'R.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|6*(1+1/4+1/9+1/16+1/25)	|6 * (1 - (1/4) + (1/9) - (1/16) + (1/25))	|[('R.0', 6.0, u'6', u'6'), ('R.1.0.0.0.1', 0.25, u'1/4', u'1/4'), ('R.1.0.0.1', 0.1111111111111111, u'1/9', u'1/9'), ('R.1.0.1', 0.0625, u'1/16', u'1/16'), ('R.1.1', 0.04, u'1/25', u'1/25')]	|
|1	|7*(1+1/4+1/9+1/16+1/25)	|7(1-1/4+1/9-1/16+1/25)	|[('R.0', 7.0, u'7', u'7'), ('R.1.0.0.0.1', 0.25, u'1/4', u'1/4'), ('R.1.0.0.1', 0.1111111111111111, u'1/9', u'1/9'), ('R.1.0.1', 0.0625, u'1/16', u'1/16'), ('R.1.1', 0.04, u'1/25', u'1/25')]	|
|2	|8*(1+1/4+1/9+1/16+1/25)	|8*(1 - 1/4+1/9 - 1/16+1/25)	|[('R.0', 8.0, u'8', u'8'), ('R.1.0.0.0.1', 0.25, u'1/4', u'1/4'), ('R.1.0.0.1', 0.1111111111111111, u'1/9', u'1/9'), ('R.1.0.1', 0.0625, u'1/16', u'1/16'), ('R.1.1', 0.04, u'1/25', u'1/25')]	|
|3	|8*(1+1/4+1/9+1/16+1/25)	|8*(1-1/4+1/9-1/16+1/25)	|[('R.0', 8.0, u'8', u'8'), ('R.1.0.0.0.1', 0.25, u'1/4', u'1/4'), ('R.1.0.0.1', 0.1111111111111111, u'1/9', u'1/9'), ('R.1.0.1', 0.0625, u'1/16', u'1/16'), ('R.1.1', 0.04, u'1/25', u'1/25')]	|
|4	|8*(1+1/4+1/9+1/16+1/25)	|8*(1 - 1/4 + 1/9 - 1/16 + 1/25)	|[('R.0', 8.0, u'8', u'8'), ('R.1.0.0.0.1', 0.25, u'1/4', u'1/4'), ('R.1.0.0.1', 0.1111111111111111, u'1/9', u'1/9'), ('R.1.0.1', 0.0625, u'1/16', u'1/16'), ('R.1.1', 0.04, u'1/25', u'1/25')]	|




### (3) Mistake Group ['R.0'] of size 3
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|6*(1+1/4+1/9+1/16+1/25)	|6*(1-1/2+1/3-1/4+1/5)	|[('R.0', 6.0, u'6', u'6')]	|
|1	|8*(1+1/4+1/9+1/16+1/25)	|8/5^2	|[('R.0', 8.0, u'8', u'8')]	|




### (2) Mistake Group Digits of size 2




### (1) Mistake Group ['R.0', 'R.1.0.0.1', 'R.1.0.1', 'R.1.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1.0.0.1', 'R.1.0.1', 'R.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|6*(1+1/4+1/9+1/16+1/25)	|6*(1+14+1/9+1/16+1/25)	|[('R.0', 6.0, u'6', u'6'), ('R.1.0.0.1', 0.1111111111111111, u'1/9', u'1/9'), ('R.1.0.1', 0.0625, u'1/16', u'1/16'), ('R.1.1', 0.04, u'1/25', u'1/25')]	|




### (1) Mistake Group ['R.1.0.0.0.1', 'R.1.0.0.1', 'R.1.0.1', 'R.1.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.0.0.0.1', 'R.1.0.0.1', 'R.1.0.1', 'R.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|9*(1+1/4+1/9+1/16+1/25)	|9(1 - 1/4 + 1/9 - 1/16 +1/25)	|[('R.1.0.0.0.1', 0.25, u'1/4', u'1/4'), ('R.1.0.0.1', 0.1111111111111111, u'1/9', u'1/9'), ('R.1.0.1', 0.0625, u'1/16', u'1/16'), ('R.1.1', 0.04, u'1/25', u'1/25')]	|




### (93) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:v4zhang

	first_attempt
					2015-11-05 11:27:02
	part3_correct_attempt
					['0:00:39', u'(4/1)-(4/2)+(4/3)-(4/4)+(4/5)']
	part4_incorrect_attempt
					('0:00:39', u'(10/1)-(10/4)+(10/9)-(10/16)+(10/25)')
	part4_correct_attempt
					['0:01:17', u'(10/1)+(10/4)+(10/9)+(10/16)+(10/25)']

1 Student ID:kew060

	first_attempt
					2015-11-03 02:11:02
	part3_correct_attempt
					['0:00:00', u'2.35']
	part4_incorrect_attempt
					('0:00:00', u'5.0317')
					('0:00:31', u'3019/600')
	part4_correct_attempt
					['1 day, 23:25:43', u'8.78']

2 Student ID:mhale

	first_attempt
					2015-11-05 20:22:12
	part3_correct_attempt
					['0:01:06', u'1 - 1/2 + 1/3 - 1/4 + 1/5']
	part4_incorrect_attempt
					('0:01:06', u'6 - 6/4 + 6/9 - 6/16 + 6/25')
	part4_correct_attempt
					['0:01:27', u'6 + 6/4 + 6/9 + 6/16 + 6/25']

3 Student ID:dkurli

	first_attempt
					2015-11-05 03:08:22
	part3_correct_attempt
					['0:01:09', u'2-1+2/3-2/4+2/5']
	part4_incorrect_attempt
					('0:01:09', u'7/1-7/4+7/9-7/16+7/25')
	part4_correct_attempt
					['0:01:39', u'7/1+7/4+7/9+7/16+7/25']

4 Student ID:j5phung

	first_attempt
					2015-11-04 04:49:51
	part3_correct_attempt
					['0:01:59', u'(3-3/2+3/3-3/4+3/5)']
	part4_incorrect_attempt
					('0:01:59', u'7/1-7/4+7/9-7/16+7/25')
	part4_correct_attempt
					['0:02:23', u'7/1+7/4+7/9+7/16+7/25']

5 Student ID:haw081

	first_attempt
					2015-11-01 22:25:00
	part3_correct_attempt
					['0:01:38', u'2-1+2/3-2/4+2/5']
	part4_incorrect_attempt
					('0:01:38', u'6-6/4+6/9-6/16+6/25')
	part4_correct_attempt
					['0:01:58', u'6+6/4+6/9+6/16+6/25']

6 Student ID:avasavad

	first_attempt
					2015-11-04 23:13:33
	part3_correct_attempt
					['0:01:11', u'5 - 5/2 + 5/3 - 5/4 + 1']
	part4_incorrect_attempt
					('0:01:11', u'10 - 10/4 + 10/9 - 10/16 + 10/25')
	part4_correct_attempt
					['0:01:48', u'10 + 10/4 + 10/9 + 10/16 + 10/25']

7 Student ID:dgunawan

	first_attempt
					2015-11-05 08:39:09
	part3_correct_attempt
					['0:00:00', u'1 - 1/2 + 1/3 - 1/4 + 1/5 ']
	part4_incorrect_attempt
					('0:00:00', u'(1/1^2) + (1/2^2) + (1/3^2) + (1/4^2) + (1/5^2)')
					('0:00:41', u'(1/1^2) - (1/2^2) + (1/3^2) - (1/4^2) + (1/5^2)')
					('0:01:31', u'(8/1^2) - (8/2^2) + (8/3^2) - (8/4^2) + (8/5^2)')
	part4_correct_attempt
					['0:01:39', u'(8/1^2) + (8/2^2) + (8/3^2) + (8/4^2) + (8/5^2)']

8 Student ID:tstevens

	first_attempt
					2015-11-06 11:55:11
	part3_correct_attempt
					['0:00:37', u'4-2+4/3-1+.8']
	part4_incorrect_attempt
					('0:02:26', u'6-1.5+2/3-3/8+6/25')
	part4_correct_attempt
					['0:02:57', u'6+1.5+2/3+3/8+6/25']

9 Student ID:tcuddy

	first_attempt
					2015-11-02 05:02:00
	part3_correct_attempt
					['0:05:38', u'3-(3/2)+(3/3)-(3/4)+(3/5)']
	part4_incorrect_attempt
					('0:06:21', u'10-(10/4)+(10/9)-(10/16)+(10/25)')
	part4_correct_attempt
					['1 day, 13:10:57', u'10+(10/4)+(10/9)+(10/16)+(10/25)']

10 Student ID:l8ngo

	first_attempt
					2015-10-30 16:31:06
	part3_correct_attempt
					['0:00:00', u'2-1+2/3-2/4+2/5']
	part4_incorrect_attempt
					('0:00:00', u'7-7/4+7/9-7/16+7/25')
	part4_correct_attempt
					['4 days, 8:28:44', u'7+7/4+7/9+7/16+7/25']

11 Student ID:dando

	first_attempt
					2015-11-03 20:23:56
	part3_correct_attempt
					['0:00:00', u'5 - 5/2 + 5/3 - 5/4 + 1']
	part4_incorrect_attempt
					('0:00:00', u'9 - 9/4 + 1 - 9/16 + 9/25')
	part4_correct_attempt
					['0:00:51', u'9 + 9/4 + 1 + 9/16 + 9/25']

12 Student ID:dsriniva

	first_attempt
					2015-11-05 09:25:27
	part3_correct_attempt
					['0:01:06', u'5-5/2+5/3-5/4+1']
	part4_incorrect_attempt
					('0:01:06', u'9-9/4+1-9/16+9/25')
	part4_correct_attempt
					['0:01:22', u'9+9/4+1+9/16+9/25']

13 Student ID:sayao

	first_attempt
					2015-11-04 01:38:15
	part3_correct_attempt
					['0:01:01', u'3-3/2+3/3-3/4+3/5']
	part4_incorrect_attempt
					('0:01:01', u'9-9/4+9/9-9/16+9/25')
					('0:01:38', u'9/1-9/4+9/9-9/16+9/25')
	part4_correct_attempt
					['0:04:19', u'9/1+9/4+9/9+9/16+9/25']

14 Student ID:anvan

	first_attempt
					2015-11-05 16:05:53
	part3_correct_attempt
					['0:00:45', u'2 - 1 + 2/3- 1/2 + 2/5']
	part4_incorrect_attempt
					('0:01:17', u'9 - 9/4 + 1 - 9/16 + 9/25')
	part4_correct_attempt
					['0:01:34', u'9 + 9/4 + 1 + 9/16 + 9/25']

15 Student ID:flhernan

	first_attempt
					2015-11-03 19:34:53
	part3_correct_attempt
					['0:02:17', u'3/1 - 3/2 + 3/3 - 3/4 + 3/5']
	part4_incorrect_attempt
					('0:02:37', u'10 - 10/(2^2) + 10/(3^2) - 10/(4^2) + 10/(5^2)')
	part4_correct_attempt
					['0:02:55', u'10 + 10/(2^2) + 10/(3^2) + 10/(4^2) + 10/(5^2)']

16 Student ID:a2ahmed

	first_attempt
					2015-11-07 00:42:10
	part3_correct_attempt
					['0:01:45', u'47/15']
	part4_incorrect_attempt
					('0:01:45', u'22267/3600')
	part4_correct_attempt
					['0:02:13', u'36883/3600']

17 Student ID:starinia

	first_attempt
					2015-11-05 03:08:44
	part3_correct_attempt
					['0:00:00', u'5 - 5/2 + 5/3 - 5/4 + 1']
	part4_incorrect_attempt
					('0:00:00', u'7 - 7/4 + 7/9 - 7/16 + 7/25')
					('0:00:26', u'7 + 7/4 - 7/9 + 7/16 - 7/25')
	part4_correct_attempt
					['0:00:48', u'7 + 7/4 + 7/9 + 7/16 + 7/25']

18 Student ID:m8woo

	first_attempt
					2015-11-05 21:03:09
	part3_correct_attempt
					['0:00:00', u'[3/1 - 3/2 + 3/3 - 3/4 + 3/5]']
	part4_incorrect_attempt
					('0:00:00', u'[3/1 + 3/4 + 3/9 + 3/16 + 3/25]')
	part4_correct_attempt
					['0:00:47', u'[10/1 + 10/4 + 10/9 + 10/16 + 10/25]']

19 Student ID:akg009

	first_attempt
					2015-11-06 21:00:56
	part3_correct_attempt
					['0:00:52', u'(1-1/2+1/3-1/4+1/5)']
	part4_incorrect_attempt
					('0:01:08', u'6/1-6/4+6/9-6/16+6/25')
					('0:02:10', u'(6/1-6/4+6/9-6/16+6/25)')
	part4_correct_attempt
					['0:03:03', u'(6/1+6/4+6/9+6/16+6/25)']

20 Student ID:jag028

	first_attempt
					2015-11-02 22:57:47
	part3_correct_attempt
					['0:02:46', u'2-1+2/3-2/4+2/5']
	part4_incorrect_attempt
					('0:03:20', u'9-9/4+1-9/16+9/25')
	part4_correct_attempt
					['0:07:06', u'9+(-1)^2(9/4)+1+(-1)^2(9/16)+9/25']

21 Student ID:ccn001

	first_attempt
					2015-11-02 19:36:06
	part3_correct_attempt
					['0:00:00', u'(4-2+(4/3)-(4/4)+(4/5))']
	part4_incorrect_attempt
					('0:00:00', u'10-(10/4)+(10/9)-(10/16)+(10/25)')
	part4_correct_attempt
					['0:00:50', u'10+(10/4)+(10/9)+(10/16)+(10/25)']

22 Student ID:abjara

	first_attempt
					2015-11-04 02:09:05
	part3_correct_attempt
					['0:01:18', u'5 - 2.5 + 5/3 - 5/4 + 1']
	part4_incorrect_attempt
					('0:01:18', u'6 - 6/4 + 6/9 - 6/16 + 6/25')
	part4_correct_attempt
					['0:02:07', u'6 + 6/4 + 6/9 + 6/16 + 6/25']

23 Student ID:cprafull

	first_attempt
					2015-11-05 08:48:35
	part3_correct_attempt
					['0:03:30', u'5 - 5/2 + 5/3 - 5/4 + 1']
	part4_incorrect_attempt
					('0:05:32', u'10/1 - 10/4 + 10/9 - 10/16 + 10/25')
	part4_correct_attempt
					['0:05:54', u'10/1 + 10/4 + 10/9 + 10/16 + 10/25']

24 Student ID:krau

	first_attempt
					2015-11-05 03:08:39
	part3_correct_attempt
					['0:00:22', u'1-1/2+1/3-1/4+1/5']
	part4_incorrect_attempt
					('0:00:22', u'8/1-8/4+8/9-8/16+8/25')
	part4_correct_attempt
					['0:02:00', u'8/1+8/4+8/9+8/16+8/25']

25 Student ID:psable

	first_attempt
					2015-11-06 00:23:39
	part3_correct_attempt
					['0:01:28', u'47/60']
	part4_incorrect_attempt
					('0:02:04', u'21133/3600')
	part4_correct_attempt
					['0:02:49', u'36883/3600']

26 Student ID:tpmach

	first_attempt
					2015-10-30 21:50:06
	part3_correct_attempt
					['0:01:53', u'3+(-1)(3/2)+3/3+(-1)(3/4)+3/5']
	part4_incorrect_attempt
					('0:02:16', u'10/1-10/4+10/9-10/16+10/25')
	part4_correct_attempt
					['0:03:23', u'10/1+(-1)^2*(10/4)+10/9+(-1)^2*(10/16)+10/25']

27 Student ID:dwzhang

	first_attempt
					2015-11-04 20:59:44
	part3_correct_attempt
					['0:02:23', u'3/1 - 3/2 + 3/3 - 3/4 + 3/5']
	part4_incorrect_attempt
					('0:02:23', u'7/1 - 7/4 + 7/9 - 7/16 + 7/25')
	part4_correct_attempt
					['0:04:01', u'7/1 + 7/4 + 7/9 + 7/16 + 7/25']

28 Student ID:dis003

	first_attempt
					2015-11-05 21:51:39
	part3_correct_attempt
					['0:02:13', u'2/1 - 2/2 + 2/3 - 2/4 + 2/5']
	part4_incorrect_attempt
					('0:02:13', u'8/1**2 - 8/2**2 + 8/3**2 - 8/4**2 + 8/5**2')
	part4_correct_attempt
					['0:02:47', u'8/1**2 + 8/2**2 + 8/3**2 + 8/4**2 + 8/5**2']

29 Student ID:rraiyyan

	first_attempt
					2015-11-06 23:21:00
	part3_correct_attempt
					['0:03:18', u'5*(1-1/2+1/3-1/4+1/5)']
	part4_incorrect_attempt
					('0:03:18', u'(8 - 8/4 + 8/9 - 8/16 + 8/25)')
					('0:07:16', u'(8 - 8/4 + 8/9 - 8/16 + 8/25)')
	part4_correct_attempt
					['0:08:30', u'(8 + 8/4 + 8/9 + 8/16 + 8/25)']

30 Student ID:jhw015

	first_attempt
					2015-11-04 01:49:42
	part3_correct_attempt
					['0:02:31', u'2 - 1 + (2/3) - (2/4) + (2/5)']
	part4_incorrect_attempt
					('0:03:08', u'8 - (8/4) + (8/9) - (8/16) + (8/25)')
	part4_correct_attempt
					['0:04:10', u'8 + (8/4) + (8/9) + (8/16) + (8/25)']

31 Student ID:t1tran

	first_attempt
					2015-11-03 18:14:54
	part3_correct_attempt
					['0:30:51', u'(4/1-4/2+4/3-4/4+4/5)']
	part4_incorrect_attempt
					('0:30:51', u'(6/1^2-6/2^2+6/3^2-6/4^2+6/5^2)')
	part4_correct_attempt
					['0:31:20', u'(6/1^2+6/2^2+6/3^2+6/4^2+6/5^2)']

32 Student ID:dsmonaha

	first_attempt
					2015-11-02 17:23:41
	part3_correct_attempt
					['0:04:43', u'47/12']
	part4_incorrect_attempt
					('0:04:43', u'3019/600')
	part4_correct_attempt
					['0:08:34', u'5269/600']

33 Student ID:ytc012

	first_attempt
					2015-11-05 22:02:52
	part3_correct_attempt
					['0:00:44', u'2-1+2/3-2/4+2/5']
	part4_incorrect_attempt
					('0:00:56', u'8-2+8/9-8/16+8/25')
	part4_correct_attempt
					['0:01:23', u'8+2+8/9+8/16+8/25']

34 Student ID:edescobe

	first_attempt
					2015-11-01 09:11:23
	part3_correct_attempt
					['0:31:28', u'5-5/2+5/3-5/4+1']
	part4_incorrect_attempt
					('0:31:28', u'7-7/4+7/9-7/16+7/25')
	part4_correct_attempt
					['0:39:13', u'7+7/4+7/9+7/16+7/25']

35 Student ID:muy002

	first_attempt
					2015-11-06 00:10:53
	part3_correct_attempt
					['0:02:39', u'4-4/2+4/3-4/4+4/5']
	part4_incorrect_attempt
					('0:02:39', u'10-10/4+10/9-10/16+10/25')
	part4_correct_attempt
					['0:03:01', u'10+10/4+10/9+10/16+10/25']

36 Student ID:cstringh

	first_attempt
					2015-11-04 06:44:53
	part3_correct_attempt
					['0:00:40', u'5-(5/2)+5/3-5/4+1']
	part4_incorrect_attempt
					('0:03:33', u'8-2+8/9-1/2+8/25')
	part4_correct_attempt
					['0:10:26', u'8*(1+1/4+1/9+1/16+1/25)']

37 Student ID:aurodrig

	first_attempt
					2015-11-06 23:09:38
	part3_correct_attempt
					['0:11:15', u'1 - 1/2 + 1/3 - 1/4 + 1/5']
	part4_incorrect_attempt
					('0:13:40', u'10/(1^2) - 10/((2)^2) + 10/((3)^2) - 10/((4)^2) + 10/((5)^2)')
	part4_correct_attempt
					['0:17:25', u'10/1 + 10/4 + 10/9 + 10/16 + 10/25']

38 Student ID:dcastlem

	first_attempt
					2015-11-02 22:00:47
	part3_correct_attempt
					['0:03:33', u'1-1/2+1/3-1/4+1/5']
	part4_incorrect_attempt
					('0:04:10', u'6-6/4+6/9-6/16+6/25')
					('0:07:09', u'6-(6/4)+6/9-(6/16)+6/25')
					('0:07:56', u'6-6/4+6/9-6/16+6/25')
	part4_correct_attempt
					['0:10:56', u'6+6/4+6/9+6/16+6/25']

39 Student ID:bkoli

	first_attempt
					2015-11-05 22:46:52
	part3_correct_attempt
					['0:00:20', u'(2/1-2/2+2/3-2/4+2/5)']
	part4_incorrect_attempt
					('0:02:07', u'(6/1-6/4+6/9-6/16+6/25)')
	part4_correct_attempt
					['0:02:19', u'(6/1+6/4+6/9+6/16+6/25)']

40 Student ID:xil109

	first_attempt
					2015-11-05 04:00:40
	part3_correct_attempt
					['0:00:40', u'2/1-2/2+2/3-2/4+2/5']
	part4_incorrect_attempt
					('0:02:27', u'10/1-10/4+10/9-10/16+10/25')
	part4_correct_attempt
					['0:03:03', u'10/1+10/4+10/9+10/16+10/25']

41 Student ID:yil035

	first_attempt
					2015-11-04 00:43:35
	part3_correct_attempt
					['0:00:00', u'47/15']
	part4_incorrect_attempt
					('0:02:10', u'6169/450')
	part4_correct_attempt
					['0:03:11', u'5269/450']

42 Student ID:k3tan

	first_attempt
					2015-11-04 01:49:58
	part3_correct_attempt
					['0:02:08', u'1+4/3+4/5']
	part4_incorrect_attempt
					('0:02:41', u'10-10/4+10/9 - 10/16 + 10/25')
	part4_correct_attempt
					['0:03:28', u'10 +10/4+10/9 + 10/16 + 10/25']

43 Student ID:jyc018

	first_attempt
					2015-11-04 18:49:56
	part3_correct_attempt
					['0:00:51', u'4-2+4/3-1+4/5']
	part4_incorrect_attempt
					('0:01:03', u'8-2+8/9-1/2+8/25')
					('0:01:51', u'4-2+4/3-1+4/5')
	part4_correct_attempt
					['0:01:58', u'8+2+8/9+1/2+8/25']

44 Student ID:lpettit

	first_attempt
					2015-11-07 00:02:46
	part3_correct_attempt
					['0:01:51', u'1 - 1/2 + 1/3 -1/4 + 1/5']
	part4_incorrect_attempt
					('0:01:51', u'7 - 7/4 + 7/9 - 7/16 + 7/25')
					('0:04:53', u'((7 - .783333)^2 + (.5- .783333)^2 + ((1/3)- .783333)^2 + (.25- .783333)^2 + ((1/5)- .783333)^2)/5')
	part4_correct_attempt
					['0:05:22', u'7 + 7/4 + 7/9 + 7/16 + 7/25']

45 Student ID:lywong

	first_attempt
					2015-11-04 07:24:45
	part3_correct_attempt
					['0:00:55', u'2 - 1 + (2/3) - (1/2) + (2/5)']
	part4_incorrect_attempt
					('0:00:55', u'10-(10/4)+(10/9)-(10/16)+(10/25)')
	part4_correct_attempt
					['0:03:18', u'10+ (10/4)+(10/9)+(10/16)+(10/25)']

46 Student ID:kebao

	first_attempt
					2015-11-05 21:34:22
	part3_correct_attempt
					['0:00:53', u'2-2/2+2/3-2/4+2/5']
	part4_incorrect_attempt
					('0:00:53', u'8-8/4+8/9-8/16+8/25')
	part4_correct_attempt
					['0:01:35', u'8+8/4+8/9+8/16+8/25']

47 Student ID:hkhodada

	first_attempt
					2015-11-03 00:32:21
	part3_correct_attempt
					['0:00:00', u'4-4/2+4/3-4/4+4/5']
	part4_incorrect_attempt
					('0:01:01', u'10-10/2+10/3-10/4+10/5')
					('0:01:39', u'10+10/2+10/3+10/4+10/5')
	part4_correct_attempt
					['0:02:03', u'10+10/4+10/9+10/16+10/25']

48 Student ID:glcohen

	first_attempt
					2015-11-03 16:57:25
	part3_correct_attempt
					['0:01:54', u'(3/1)-(3/2)+(3/3)-(3/4)+(3/5)']
	part4_incorrect_attempt
					('0:01:54', u'(7/(1^2))-(7/(2^2))+(7/(3^2))-(7/(4^2))+(7/(5^2))')
					('0:14:55', u'(7/(1^2))+(-(7/(2^2)))+(7/(3^2))+(-(7/(4^2)))+(7/(5^2))')
					('0:17:21', u'(7/(1^2))-(7/(2^2))+(7/(3^2))-(7/(4^2))+(7/(5^2))')
	part4_correct_attempt
					['4:56:12', u'(7/(1^2))+(7/(2^2))+(7/(3^2))+(7/(4^2))+(7/(5^2))']

49 Student ID:achava

	first_attempt
					2015-11-06 07:27:32
	part3_correct_attempt
					['0:02:00', u'3-(3/2)+(1)-(3/4)+(3/5)']
	part4_incorrect_attempt
					('0:32:19', u'3-(3/2)+(1)-(3/4)+(3/5)')
	part4_correct_attempt
					['0:32:32', u'8+(8/4)+(8/9)+(8/16)+(8/25)']

50 Student ID:pvl001

	first_attempt
					2015-11-03 18:19:03
	part3_correct_attempt
					['0:00:46', u'2 - 1 + (2/3) - (2/4) + (2/5)']
	part4_incorrect_attempt
					('0:00:46', u'9 - (9/4) + 1 - (9/16) + (9/25)')
	part4_correct_attempt
					['0:01:04', u'9 + (9/4) + 1 + (9/16) + (9/25)']

51 Student ID:t2li

	first_attempt
					2015-11-06 02:40:30
	part3_correct_attempt
					['0:01:32', u'4-2+4/3-1+4/5']
	part4_incorrect_attempt
					('0:01:32', u'7-7/4+7/9-7/16+7/25')
	part4_correct_attempt
					['0:04:15', u'7+7/4+7/9+7/16+7/25']

52 Student ID:n2patil

	first_attempt
					2015-11-05 00:58:59
	part3_correct_attempt
					['0:24:24', u'3.133']
	part4_incorrect_attempt
					('0:27:11', u'5.87')
	part4_correct_attempt
					['0:28:42', u'10.245']

53 Student ID:ttimmons

	first_attempt
					2015-11-02 03:51:12
	part3_correct_attempt
					['0:00:00', u'5/1-5/2+5/3-5/4+1']
	part4_incorrect_attempt
					('0:00:00', u'(6/1)-(6/4)+(6/9)-(6/16)+(6/25)')
	part4_correct_attempt
					['0:00:17', u'(6/1)+(6/4)+(6/9)+(6/16)+(6/25)']

54 Student ID:agian

	first_attempt
					2015-11-07 00:23:46
	part3_correct_attempt
					['0:01:14', u'(1-1/2+1/3-1/4+1/5)*2']
	part4_incorrect_attempt
					('0:01:30', u'(1-1/4+1/9-1/16+1/25)*10')
	part4_correct_attempt
					['0:01:49', u'(1+1/4+1/9+1/16+1/25)*10']

55 Student ID:aakumar

	first_attempt
					2015-11-05 03:07:58
	part3_correct_attempt
					['0:01:03', u'2-1+2/3-2/4+2/5']
	part4_incorrect_attempt
					('0:01:21', u'6-6/4+6/9-6/16+6/25')
	part4_correct_attempt
					['0:01:31', u'6+6/4+6/9+6/16+6/25']

56 Student ID:hachrist

	first_attempt
					2015-11-03 21:16:33
	part3_correct_attempt
					['0:00:58', u'4 - 2 + 4/3 - 1 + 4/5']
	part4_incorrect_attempt
					('0:01:49', u'7 - 7/4 + 7/9 - 7/16 + 7/25')
	part4_correct_attempt
					['0:06:41', u'7 + 7/4 + 7/9 + 7/16 + 7/25']

57 Student ID:kew017

	first_attempt
					2015-11-05 22:49:02
	part3_correct_attempt
					['0:02:56', u'4-2+4/3-1+4/5']
	part4_incorrect_attempt
					('0:02:56', u'7/1-7/4+7/9-7/16+7/25')
	part4_correct_attempt
					['0:03:34', u'7/1+7/4+7/9+7/16+7/25']

58 Student ID:q3wen

	first_attempt
					2015-11-04 21:07:59
	part3_correct_attempt
					['0:00:00', u'47/60']
	part4_incorrect_attempt
					('0:00:00', u'7.5475')
	part4_correct_attempt
					['0:01:01', u'5269/400']

59 Student ID:yeh013

	first_attempt
					2015-11-05 03:31:53
	part3_correct_attempt
					['2:23:34', u'4-2+4/3-1+4/5']
	part4_incorrect_attempt
					('2:23:49', u'7-7/4+7/9-7/16+7/25')
	part4_correct_attempt
					['2:24:02', u'7+7/4+7/9+7/16+7/25']

60 Student ID:haliew

	first_attempt
					2015-11-07 00:22:41
	part3_correct_attempt
					['0:03:56', u'(2/1)-(2/2)+(2/3)-(2/4)+(2/5)']
	part4_incorrect_attempt
					('0:03:56', u'(6/1^2)-(6/2^2)+(6/3^2)-(6/4^2)+(6/5^2)')
	part4_correct_attempt
					['0:04:42', u'(6/1^2)+(6/2^2)+(6/3^2)+(6/4^2)+(6/5^2)']

61 Student ID:arvenega

	first_attempt
					2015-11-05 00:24:50
	part3_correct_attempt
					['0:02:42', u'(2/1) - (2/2) + (2/3) - (2/4) + (2/5)']
	part4_incorrect_attempt
					('0:02:42', u'(10/1^2) - (10/2^2) + (10/3^2) - (10/4^2) + (10/5^2)')
	part4_correct_attempt
					['0:04:09', u'(10/1^2) + (10/2^2) + (10/3^2) + (10/4^2) + (10/5^2)']

62 Student ID:ksrijong

	first_attempt
					2015-11-04 23:10:06
	part3_correct_attempt
					['0:01:32', u'4-2+4/3-1+4/5']
	part4_incorrect_attempt
					('0:01:32', u'8/1-8/4+8/9-8/16+8/25')
	part4_correct_attempt
					['0:02:03', u'8/1+8/4+8/9+8/16+8/25']

63 Student ID:atorr

	first_attempt
					2015-11-05 20:05:29
	part3_correct_attempt
					['0:01:05', u'5 - (5/2) + (5/3) - (5/4) + 1']
	part4_incorrect_attempt
					('0:01:05', u'6 - (6/4) + (6/9) - (6/16) + (6/25)')
					('0:01:27', u'6 - (6/4) + (6/9) + (6/16) + (6/25)')
					('0:01:36', u'6 - (6/4) + (6/9) - (6/16) + (6/25)')
	part4_correct_attempt
					['0:01:54', u'6 + (6/4) + (6/9) + (6/16) + (6/25)']

64 Student ID:ralhadda

	first_attempt
					2015-10-31 20:35:01
	part3_correct_attempt
					['4:38:43', u'0.78333']
	part4_incorrect_attempt
					('4:40:16', u'8.38611')

65 Student ID:cagatep

	first_attempt
					2015-11-05 07:30:30
	part3_correct_attempt
					['0:01:54', u'(1 - 1/2 + 1/3 - 1/4 + 1/5)']
	part4_incorrect_attempt
					('0:01:54', u'(8 - 2 + 8/9 - 1/2 + 8/25)')
	part4_correct_attempt
					['0:02:24', u'(8 + 2 + 8/9 + 1/2 + 8/25)']

66 Student ID:hmnaing

	first_attempt
					2015-11-04 19:06:41
	part3_correct_attempt
					['0:00:48', u'3- (3/2)+ (1)- (3/4)+ (3/5)']
	part4_incorrect_attempt
					('0:00:48', u'(9/1)-(9/4)+ (9/9) - (9/16)+ (9/25)')
	part4_correct_attempt
					['0:01:17', u'(9/1)+(9/4)+ (9/9) + (9/16)+ (9/25)']

67 Student ID:dmn009

	first_attempt
					2015-11-05 03:33:17
	part3_correct_attempt
					['0:24:28', u'3.1333']
	part4_incorrect_attempt
					('0:28:00', u'7.54')
					('0:28:06', u'7.5475')
	part4_correct_attempt
					['0:29:34', u'13.1725']

68 Student ID:yig015

	first_attempt
					2015-11-05 10:41:11
	part3_correct_attempt
					['0:04:05', u'47/20']
	part4_incorrect_attempt
					('0:04:05', u'3019/360')
	part4_correct_attempt
					['0:04:32', u'5269/360']

69 Student ID:ppanourg

	first_attempt
					2015-11-06 22:23:49
	part3_correct_attempt
					['0:01:38', u'2/1 - 2/2 + 2/3 - 2/4 + 2/5']
	part4_incorrect_attempt
					('0:01:38', u'8/1 - 8/4 + 8/9 - 8/16 + 8/25')
	part4_correct_attempt
					['0:02:13', u'8/1 + 8/4 + 8/9 + 8/16 + 8/25']

70 Student ID:qtluong

	first_attempt
					2015-11-04 06:21:55
	part3_correct_attempt
					['0:01:15', u'2/1-2/2+2/3-2/4+2/5']
	part4_incorrect_attempt
					('0:01:15', u'2/1+2/2+2/3+2/4+2/5')
	part4_correct_attempt
					['0:02:10', u'6+6/4+6/9+6/16+6/25']

71 Student ID:spw006

	first_attempt
					2015-11-04 02:41:54
	part3_correct_attempt
					['0:00:45', u'(5/1 - 5/2 + 5/3 - 5/4 + 5/5)']
	part4_incorrect_attempt
					('0:01:50', u'(10/1 - 10/4 + 10/9 - 10/16 + 10/25)')
	part4_correct_attempt
					['0:40:24', u'(10/1 + 10/4 + 10/9 + 10/16 + 10/25)']

72 Student ID:any027

	first_attempt
					2015-11-01 20:32:06
	part3_correct_attempt
					['0:01:16', u'(4/1) - ( 4/2) + (4/3) - (4/4) + (4/5)']
	part4_incorrect_attempt
					('0:01:16', u'(10/1) - (10/4) + (10/9) - (10/16) + (10/25)')
					('0:01:47', u'(10/1) + (10/4) + (10/9) - (10/16) + (10/25)')
	part4_correct_attempt
					['0:02:02', u'(10/1) + (10/4) + (10/9) + (10/16) + (10/25)']

73 Student ID:pcdo

	first_attempt
					2015-11-02 18:49:41
	part3_correct_attempt
					['0:01:06', u'3*(1-1/2+1/3-1/4+1/5)']
	part4_incorrect_attempt
					('0:01:06', u'9*(1-1/2+1/3-1/4+1/5)')
	part4_correct_attempt
					['0:01:47', u'9*(1+1/4+1/9+1/16+1/25)']

74 Student ID:k5law

	first_attempt
					2015-11-04 07:59:10
	part3_correct_attempt
					['0:09:26', u'[(5/1)-(5/2)+(5/3)-(5/4)+(5/5)]']
	part4_incorrect_attempt
					('0:12:54', u'(7/((1)^2))-(7/((2)^2))+(7/((3)^2))-(7/((4)^2))+(7/((5)^2))')
	part4_correct_attempt
					['0:13:43', u'(7/((1)^2))+(7/((2)^2))+(7/((3)^2))+(7/((4)^2))+(7/((5)^2))']

75 Student ID:amquinte

	first_attempt
					2015-11-06 23:12:40
	part3_correct_attempt
					['0:00:58', u'3.133333']
	part4_incorrect_attempt
					('0:03:24', u'5.870')
	part4_correct_attempt
					['0:04:12', u'10.245']

76 Student ID:jmiclat

	first_attempt
					2015-11-06 09:29:36
	part3_correct_attempt
					['0:00:42', u'2/1-2/2+2/3-2/4+2/5']
	part4_incorrect_attempt
					('0:00:42', u'7/1-7/4+7/9-7/16+7/25')
	part4_correct_attempt
					['0:00:53', u'7/1+7/4+7/9+7/16+7/25']

77 Student ID:syc078

	first_attempt
					2015-11-05 04:34:52
	part3_correct_attempt
					['0:00:20', u'1-(1/2)+(1/3)-(1/4)+(1/5)']
	part4_incorrect_attempt
					('0:01:49', u'(7/1)-(7/4)+(7/9)-(7/16)+(7/25)')
	part4_correct_attempt
					['1 day, 16:03:30', u'(7/1)+(7/4)+(7/9)+(7/16)+(7/25)']

78 Student ID:cfgutier

	first_attempt
					2015-11-06 18:23:18
	part3_correct_attempt
					['1:25:59', u'4/1 - 4/2 + 4/3 - 4/4 + 4/5']
	part4_incorrect_attempt
					('1:26:09', u'7 + 7/4 - 7/9 + 7/16 - 7/25')
					('1:26:46', u'7 - 7/4 + 7/9 - 7/16 + 7/25')
	part4_correct_attempt
					['1:27:03', u'7 + 7/4 + 7/9 + 7/16 + 7/25']

79 Student ID:agarango

	first_attempt
					2015-11-05 23:55:25
	part3_correct_attempt
					['0:01:33', u'(1/1)-(1/2)+(1/3)-(1/4)+(1/5)']
	part4_incorrect_attempt
					('0:02:03', u'(7/1)-(7/4)+(7/9)-(7/16)+(7/25)')
	part4_correct_attempt
					['0:03:22', u'(7/1)+(7/4)+(7/9)+(7/16)+(7/25)']

80 Student ID:s6deng

	first_attempt
					2015-11-05 07:25:26
	part3_correct_attempt
					['0:00:28', u'(3/1)-(3/2)+(3/3)-(3/4)+(3/5)']
	part4_incorrect_attempt
					('0:00:28', u'(6/1)-(6/4)+(6/9)-(6/16)+(6/25)')
	part4_correct_attempt
					['0:00:39', u'(6/1)+(6/4)+(6/9)+(6/16)+(6/25)']

81 Student ID:aalhaida

	first_attempt
					2015-11-05 23:43:36
	part3_correct_attempt
					['0:02:01', u'3/1 - 3/2 + 3/3 - 3/4 + 3/5']
	part4_incorrect_attempt
					('0:02:01', u'7/1 - 7/2^2 + 7/3^2 - 7/4^2 + 7/5^2')
					('0:02:53', u'(7/1) - (7/2^2) + (7/3^2) - (7/4^2) + (7/5^2)')

82 Student ID:hah008

	first_attempt
					2015-11-06 23:00:08
	part3_correct_attempt
					['0:01:57', u'(1-1/2+1/3-1/4+1/5) * 5']
	part4_incorrect_attempt
					('0:02:13', u'(1-1/4+1/9-1/16+1/25) * 9')
	part4_correct_attempt
					['0:02:41', u'(1+1/4+1/9+1/16+1/25) * 9']

83 Student ID:hmshah

	first_attempt
					2015-11-05 09:41:00
	part3_correct_attempt
					['0:00:56', u'2 - 1 + 2/3 - 2/4 + 2/5']
	part4_incorrect_attempt
					('0:01:13', u'6 - 6/4 + 6/9- 6/16+ 6/25')
	part4_correct_attempt
					['0:01:40', u'6 + 6/4 + 6/9+ 6/16+ 6/25']

84 Student ID:dtea

	first_attempt
					2015-11-07 00:18:37
	part3_correct_attempt
					['0:00:46', u'4/1-4/2+4/3-4/4+4/5']
	part4_incorrect_attempt
					('0:01:19', u'(6/1-6/4+6/9-6/16+6/25)')
	part4_correct_attempt
					['0:02:35', u'(6/1+6/4+6/9+6/16+6/25)']

85 Student ID:lahawkin

	first_attempt
					2015-11-04 04:48:19
	part3_correct_attempt
					['0:02:03', u'(4/1)-(4/2)+(4/3)-(4/4)+(4/5)']
	part4_incorrect_attempt
					('0:02:03', u'(6/1)-(6/4)+(6/9)-(6/16)+(6/25)')
					('0:05:07', u'((6/1)-(6/4)+(6/9)-(6/16)+(6/25))/5')
					('0:05:18', u'((6/1)-(6/4)+(6/9)-(6/16)+(6/25))/25')
	part4_correct_attempt
					['0:06:26', u'(6/1)+(6/4)+(6/9)+(6/16)+(6/25)']

86 Student ID:edcole

	first_attempt
					2015-11-06 23:40:14
	part3_correct_attempt
					['0:01:02', u'3-(3/2)+3/3-3/4+3/5']
	part4_incorrect_attempt
					('0:01:20', u'8/1-8/4+8/9-8/16+8/25')
	part4_correct_attempt
					['0:02:34', u'8/1+8/4+8/9+8/16+8/25']

87 Student ID:kquong

	first_attempt
					2015-11-02 05:16:14
	part3_correct_attempt
					['0:06:00', u'4 - 2 + 4/3 - 1 + 4/5']
	part4_incorrect_attempt
					('0:06:00', u'10 - 10/4 + 10/9 - 10/16 + 10/25')
	part4_correct_attempt
					['0:06:28', u'10 +10/4 + 10/9 + 10/16 + 10/25']

88 Student ID:c3chung

	first_attempt
					2015-11-06 10:56:06
	part3_correct_attempt
					['0:00:22', u'2-1+2/3-1/2+2/5']
	part4_incorrect_attempt
					('0:00:43', u'10-10/4+10/9-10/16+10/25')
	part4_correct_attempt
					['0:03:26', u'10+10/4+10/9+10/16+10/25']

89 Student ID:ajvanega

	first_attempt
					2015-11-05 02:57:39
	part3_correct_attempt
					['0:05:29', u'4-2+(4/3)-1+(4/5)']
	part4_incorrect_attempt
					('0:08:09', u'(8)-(2)+(8/9)-(1/2)+(8/25)')
					('1 day, 17:24:58', u'(8)-(8/4)+(8/9)-(8/16)+(8/25)')
	part4_correct_attempt
					['1 day, 17:28:43', u'(8)+(8/4)+(8/9)+(8/16)+(8/25)']

90 Student ID:mtrafeca

	first_attempt
					2015-11-05 00:20:13
	part3_correct_attempt
					['0:03:38', u'1-1/2+1/3-1/4+1/5']
	part4_incorrect_attempt
					('0:03:54', u'6-6/4+6/9-6/16+6/25')
	part4_correct_attempt
					['0:04:59', u'6+6/4+6/9+6/16+6/25']

91 Student ID:mjethani

	first_attempt
					2015-11-05 04:35:33
	part3_correct_attempt
					['0:01:49', u'(5/1) - (5/2) + (5/3) - (5/4) + (5/5)']
	part4_incorrect_attempt
					('0:02:21', u'(10/1) - (10/4) + (10/9) - (10/16) + (10/25)')
					('0:03:32', u'(10/25) - (10/16) + (10/9) - (10/4) + (10/1)')
	part4_correct_attempt
					['1 day, 16:03:17', u'(10) + (10/4) + ( 10/9) + (10/16) + (10/25)']

92 Student ID:kgrozav

	first_attempt
					2015-11-05 20:01:44
	part3_correct_attempt
					['0:03:11', u'0.783333']
	part4_incorrect_attempt
					('0:03:11', u'10.245277*5')
	part4_correct_attempt
					['0:17:40', u'10.245277']












## Part 5

### (8) Mistake Group Wrong_Sign of size 8




### (2) Mistake Group Digits of size 2




### (2) Mistake Group ['R.1'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|1*(1-2/2+1/3-2/4+1/5)	|8*(1-2/2+1/3-2/4+1/5)	|[('R.1', 0.033333333333333326, u'1-2/2+1/3-2/4+1/5', u'1-2/2+1/3-2/4+1/5')]	|
|1	|1*(1-2/2+1/3-2/4+1/5)	|5*((1/1)-(2/2)+(1/3)-(2/4)+(1/5))	|[('R.1', 0.033333333333333326, u'1-2/2+1/3-2/4+1/5', u'(1/1)-(2/2)+(1/3)-(2/4)+(1/5)')]	|




### (1) Mistake Group ['R.1.0.0.1.1', 'R.1.0.1', 'R.1.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.0.0.1.1', 'R.1.0.1', 'R.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|2*(1-2/2+1/3-2/4+1/5)	|2*(1/1 - 2/2 + 1/3 + 1/3 - 2/4 + 1/5)	|[('R.1.0.0.1.1', 3.0, u'3', u'3'), ('R.1.0.1', 0.5, u'2/4', u'2/4'), ('R.1.1', 0.2, u'1/5', u'1/5')]	|




### (41) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:b3hwang

	first_attempt
					2015-11-05 08:50:27
	part5_incorrect_attempt
					('0:07:51', u'4 - 8/2 + 4/3 - 8/4 + 8/5')
	part5_correct_attempt
					['0:11:08', u'4 - 8/2 + 4/3 - 8/4 + 4/5']

1 Student ID:lpettit

	first_attempt
					2015-11-07 00:02:46
	part5_incorrect_attempt
					('0:53:55', u'7 - 1 +1/3 - 1/2 + 1/5')
	part5_correct_attempt
					['0:54:18', u'1 - 1 +1/3 - 1/2 + 1/5']

2 Student ID:jfalcone

	first_attempt
					2015-11-05 05:29:27
	part5_incorrect_attempt
					('0:01:01', u'1 + (1/2) + (1/3) + (1/4) + (1/5)')
	part5_correct_attempt
					['0:01:46', u'1 - (2/2) + (1/3) - (2/4) + (1/5)']

3 Student ID:quwong

	first_attempt
					2015-11-03 21:05:49
	part5_incorrect_attempt
					('-5 days, 4:39:16', u'0.0333333')
	part5_correct_attempt
					['0:00:00', u'5(1 - 2/2 + 1/3 - 2/4 + 1/5)']

4 Student ID:hkhodada

	first_attempt
					2015-11-03 00:32:21
	part5_incorrect_attempt
					('-3 days, 16:24:43', u'1894/360')
	part5_correct_attempt
					['0:03:27', u'4-4+4/3-2+4/5']

5 Student ID:eyhu

	first_attempt
					2015-10-30 08:25:58
	part5_incorrect_attempt
					('0:00:00', u'(4/1)+(2*(4/2))+(4/3)+(2*(4/4))+(4/5)')
	part5_correct_attempt
					['0:00:17', u'(4/1)-(2*(4/2))+(4/3)-(2*(4/4))+(4/5)']

6 Student ID:ppanourg

	first_attempt
					2015-11-06 22:23:49
	part5_incorrect_attempt
					('0:02:39', u'2/1 - 2/2 + 2/3 - 2/4 + 2/5')
	part5_correct_attempt
					['0:02:55', u'2/1 - 4/2 + 2/3 - 4/4 + 2/5']

7 Student ID:abjara

	first_attempt
					2015-11-04 02:09:05
	part5_incorrect_attempt
					('0:01:18', u'5 + 5 + 5/3 - 10/3 + 1')
					('0:02:07', u'5 + 5 + 5/3 - 10/4 + 1')
	part5_correct_attempt
					['0:02:53', u'5 - 5 + 5/3 - 10/4 + 1']

8 Student ID:krau

	first_attempt
					2015-11-05 03:08:39
	part5_incorrect_attempt
					('-1 day, 17:24:37', u'(1/1-2*1/2+1/3-2*1/4+1/5) / 5')
	part5_correct_attempt
					['0:00:40', u'1-2/2+1/3-2/4+1/5']

9 Student ID:crmirand

	first_attempt
					2015-11-03 05:23:32
	part5_incorrect_attempt
					('0:01:53', u'2 - 2 + 1 - 1 + 2/5')
	part5_correct_attempt
					['0:02:22', u'2 - 2 + 2/3 - 1 + 2/5']

10 Student ID:jdeon

	first_attempt
					2015-11-04 23:20:03
	part5_incorrect_attempt
					('0:01:48', u'(1+2/2+1/3+2/4+1/5)')
	part5_correct_attempt
					['0:02:00', u'(1-2/2+1/3-2/4+1/5)']

11 Student ID:mbl003

	first_attempt
					2015-11-05 21:00:37
	part5_incorrect_attempt
					('-1 day, 23:56:37', u'7/1+7/4+7/9+7/16+7/25')
					('-1 day, 23:56:56', u'7/1+7*2/4+7/9+7*2/16+7/25')
					('-1 day, 23:57:10', u'7/1+7*2^2/4+7/9+7*2^2/16+7/25')
	part5_correct_attempt
					['0:00:32', u'1/1-2/2+1/3-2/4+1/5']

12 Student ID:j5phung

	first_attempt
					2015-11-04 04:49:51
	part5_incorrect_attempt
					('-1 day, 23:57:52', u'1/7')
	part5_correct_attempt
					['0:01:59', u'(3-3+3/3-3/2+3/5)']

13 Student ID:n2patil

	first_attempt
					2015-11-05 00:58:59
	part5_incorrect_attempt
					('0:29:31', u'.133')
					('0:41:45', u'3.633')
	part5_correct_attempt
					['0:46:59', u'4-4+4/3-2+4/5']

14 Student ID:gsrandha

	first_attempt
					2015-11-05 08:09:47
	part5_incorrect_attempt
					('0:00:09', u'3/1 + 3/2 + 1+ 3/4 + 3/5')
	part5_correct_attempt
					['0:00:40', u'3/1 - 3 + 1 - 3/2 + 3/5']

15 Student ID:r9jiang

	first_attempt
					2015-11-02 02:47:32
	part5_incorrect_attempt
					('-1 day, 23:46:53', u'1/30')
					('-1 day, 23:58:06', u'1-2/2+1/3-2/4+1/5')
	part5_correct_attempt
					['0:00:00', u'5-10/2+5/3-10/4+5/5']

16 Student ID:beerye28

	first_attempt
					2015-11-03 06:32:53
	part5_incorrect_attempt
					('0:01:25', u'8*(1 + (1/9) + (1/25)) + 8*4*((1/4) + (1/16))')

17 Student ID:twsalim

	first_attempt
					2015-11-06 01:32:11
	part5_incorrect_attempt
					('0:00:00', u'139/120')
	part5_correct_attempt
					['0:05:04', u'1/30']

18 Student ID:agian

	first_attempt
					2015-11-07 00:23:46
	part5_incorrect_attempt
					('0:01:58', u'(1-1/2+1/3-1/4+1/5)*2')
	part5_correct_attempt
					['0:02:15', u'(1-2*1/2+1/3-2*1/4+1/5)*2']

19 Student ID:dgunawan

	first_attempt
					2015-11-05 08:39:09
	part5_incorrect_attempt
					('0:00:00', u'1 - 1/2 + 1/3 - 1/4 + 1/5 ')
	part5_correct_attempt
					['0:00:41', u'1 - 2/2 + 1/3 - 2/4 + 1/5 ']

20 Student ID:aakumar

	first_attempt
					2015-11-05 03:07:58
	part5_incorrect_attempt
					('0:01:56', u'2-2+2/3+8/4+2/5')
	part5_correct_attempt
					['0:02:46', u'2-2+2/3-1+2/5']

21 Student ID:ssamudra

	first_attempt
					2015-11-05 06:16:59
	part5_incorrect_attempt
					('0:05:00', u'1/5 + 1/4 + 1/3 + 1/2 + 1')
	part5_correct_attempt
					['0:05:29', u'1/5 - 2/4 + 1/3 - 2/2 + 1']

22 Student ID:r1gu

	first_attempt
					2015-11-05 12:10:39
	part5_incorrect_attempt
					('0:00:10', u'9/25+9/16+9/9+9/4+9')
	part5_correct_attempt
					['0:01:04', u'5-10/2-10/4+5/3+1']

23 Student ID:alhung

	first_attempt
					2015-11-06 23:25:00
	part5_incorrect_attempt
					('0:00:00', u'1/1-(2*1/2)+1/3+(2*1/4)+1/5')
	part5_correct_attempt
					['0:00:24', u'1/1-(2*1/2)+1/3-(2*1/4)+1/5']

24 Student ID:tcn013

	first_attempt
					2015-11-04 05:28:57
	part5_incorrect_attempt
					('0:02:10', u'4/3+2+.8')
	part5_correct_attempt
					['0:02:27', u'4-4+4/3-2+.8']

25 Student ID:jtfrankl

	first_attempt
					2015-11-06 18:40:52
	part5_incorrect_attempt
					('-1 day, 23:54:20', u'(1-2*.5+1/3-2*1/4+.2)/5')
	part5_correct_attempt
					['0:00:07', u'(1-2*.5+1/3-2*1/4+.2)']

26 Student ID:m8woo

	first_attempt
					2015-11-05 21:03:09
	part5_incorrect_attempt
					('-1 day, 23:59:00', u'[3/1 - 2*3/2 + 3/3 - 2*3/4 + 3/5]/7')
	part5_correct_attempt
					['0:00:00', u'[3/1 - 2*3/2 + 3/3 - 2*3/4 + 3/5]']

27 Student ID:acs008

	first_attempt
					2015-11-04 05:20:16
	part5_incorrect_attempt
					('0:01:46', u'3-2*3/2+3/3+3/2+3/5')
	part5_correct_attempt
					['0:01:58', u'3-3+3/3-3/2+3/5']

28 Student ID:c1sorian

	first_attempt
					2015-11-05 00:38:57
	part5_incorrect_attempt
					('0:00:00', u'((3/1)-(3/2)+(3/3)-(3/4)+(3/5))')
	part5_correct_attempt
					['0:00:13', u'((3/1)-(6/2)+(3/3)-(6/4)+(3/5))']

29 Student ID:dtea

	first_attempt
					2015-11-07 00:18:37
	part5_incorrect_attempt
					('0:41:18', u'4/1-4/2^2+4/3-4/4^2+4/5')
	part5_correct_attempt
					['0:41:40', u'4/1-4/2*2+4/3-4/4*2+4/5']

30 Student ID:azkong

	first_attempt
					2015-11-06 22:08:31
	part5_incorrect_attempt
					('-1 day, 21:56:15', u'6-2*6/4+6/9-2*6/16+6/25')
					('-1 day, 23:56:05', u'6-2*6/4+6/9-2*6/16+6/25')
					('-1 day, 23:56:36', u'6-2*6/4+6/9-2*6/16+6/25')
					('-1 day, 23:56:50', u'6+4*6/4+6/9+4*6/16+6/25')
	part5_correct_attempt
					['0:00:32', u'5-5+5/3-5/2+5/5']

31 Student ID:aordookh

	first_attempt
					2015-11-04 22:13:50
	part5_incorrect_attempt
					('-1 day, 23:58:55', u'(4/1)-(8/2)+(4/3)-(8/4)+(5/4)')
	part5_correct_attempt
					['0:00:00', u'(4/1)-(8/2)+(4/3)-(8/4)+(4/5)']

32 Student ID:yhhan

	first_attempt
					2015-11-06 23:50:10
	part5_incorrect_attempt
					('0:00:59', u'9+9/2+1-9/8+9/25')
					('0:01:25', u'9+9/4+1-9/16+9/25')
	part5_correct_attempt
					['0:01:51', u'5-5+5/3-5/2+1']

33 Student ID:kgrozav

	first_attempt
					2015-11-05 20:01:44
	part5_incorrect_attempt
					('0:26:47', u'0.8333333')
					('0:26:57', u'0.08333333')
	part5_correct_attempt
					['0:28:44', u'0.03333333']

34 Student ID:rohan

	first_attempt
					2015-11-07 00:05:28
	part5_incorrect_attempt
					('0:01:37', u'3+12/2+1+12/4+3/5')
	part5_correct_attempt
					['0:02:38', u'3-3+3/3-3/2+3/5']

35 Student ID:dac064

	first_attempt
					2015-11-05 09:10:26
	part5_incorrect_attempt
					('0:02:00', u'9/1 + 9/2 + 9/9 + 9/8 + 9/25')
	part5_correct_attempt
					['0:02:21', u'4-4+4/3-2+4/5']

36 Student ID:yil035

	first_attempt
					2015-11-04 00:43:35
	part5_incorrect_attempt
					('-1 day, 23:59:27', u'2/75')
					('0:00:00', u'7.5')
	part5_correct_attempt
					['0:02:10', u'2/15']

37 Student ID:ytc012

	first_attempt
					2015-11-05 22:02:52
	part5_incorrect_attempt
					('0:01:23', u'2-1+4/3-4/4+2/5')
	part5_correct_attempt
					['0:01:41', u'2-2+2/3-4/4+2/5']

38 Student ID:wmiao

	first_attempt
					2015-11-04 20:27:09
	part5_incorrect_attempt
					('-1 day, 23:59:46', u'(1/1-2*1/2+1/3-2*1/4+1/5)/5')
	part5_correct_attempt
					['0:00:00', u'(1/1-2*1/2+1/3-2*1/4+1/5)']

39 Student ID:pnquach

	first_attempt
					2015-11-06 05:41:37
	part5_incorrect_attempt
					('-1 day, 23:58:50', u'(1 - (2*1/2) + 1/3 - (2*1/4) + 1/5)/5')
	part5_correct_attempt
					['0:00:00', u'1 - (2*1/2) + 1/3 - (2*1/4) + 1/5']

40 Student ID:jit002

	first_attempt
					2015-11-05 04:01:38
	part5_incorrect_attempt
					('-1 day, 23:50:58', u'(5-2*2.5+5/3-2*5/4+1)/5')
	part5_correct_attempt
					['0:00:00', u'5-2*2.5+5/3-2*5/4+1']












## Part 6

### (34) Mistake Group redirect of size 34




### (17) Mistake Group Wrong_Sign of size 17




### (8) Mistake Group ['R.0', 'R.1.1'] of size 8
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|10*(1+1/9+1/25)+10*4*(1/4+1/16)	|10*(1/1 + 1/9 + 1/25) + 10*(1/4 + 1/16)	|[('R.0', 11.511111111111113, u'10*(1+1/9+1/25)', u'10*(1/1 + 1/9 + 1/25)'), ('R.1.1', 0.3125, u'1/4+1/16', u'1/4 + 1/16')]	|
|1	|8*(1+1/9+1/25)+8*4*(1/4+1/16)	|8*(1+1/9+1/25)+8*2*(1/4+1/16)	|[('R.0', 9.20888888888889, u'8*(1+1/9+1/25)', u'8*(1+1/9+1/25)'), ('R.1.1', 0.3125, u'1/4+1/16', u'1/4+1/16')]	|
|2	|6*(1+1/9+1/25)+6*4*(1/4+1/16)	|6*(1+1/9+1/25)+28*(1/4+1/16)	|[('R.0', 6.906666666666667, u'6*(1+1/9+1/25)', u'6*(1+1/9+1/25)'), ('R.1.1', 0.3125, u'1/4+1/16', u'1/4+1/16')]	|
|3	|10*(1+1/9+1/25)+10*4*(1/4+1/16)	|10*(1+1/9+1/25)+28*(1/4+1/16)	|[('R.0', 11.511111111111113, u'10*(1+1/9+1/25)', u'10*(1+1/9+1/25)'), ('R.1.1', 0.3125, u'1/4+1/16', u'1/4+1/16')]	|
|4	|10*(1+1/9+1/25)+10*4*(1/4+1/16)	|10*(1+1/9+1/25)+14.6361*(1/4+1/16)	|[('R.0', 11.511111111111113, u'10*(1+1/9+1/25)', u'10*(1+1/9+1/25)'), ('R.1.1', 0.3125, u'1/4+1/16', u'1/4+1/16')]	|
|5	|10*(1+1/9+1/25)+10*4*(1/4+1/16)	|10*(1+1/9+1/25)+14*(1/4+1/16)	|[('R.0', 11.511111111111113, u'10*(1+1/9+1/25)', u'10*(1+1/9+1/25)'), ('R.1.1', 0.3125, u'1/4+1/16', u'1/4+1/16')]	|
|6	|10*(1+1/9+1/25)+10*4*(1/4+1/16)	|10*(1+1/9+1/25)+15*(1/4+1/16)	|[('R.0', 11.511111111111113, u'10*(1+1/9+1/25)', u'10*(1+1/9+1/25)'), ('R.1.1', 0.3125, u'1/4+1/16', u'1/4+1/16')]	|
|7	|10*(1+1/9+1/25)+10*4*(1/4+1/16)	|10*(1+1/9+1/25)+20*(1/4+1/16)	|[('R.0', 11.511111111111113, u'10*(1+1/9+1/25)', u'10*(1+1/9+1/25)'), ('R.1.1', 0.3125, u'1/4+1/16', u'1/4+1/16')]	|




### (2) Mistake Group Digits of size 2




### (1) Mistake Group ['R.1.0.0'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|6*(1+1/9+1/25)+6*4*(1/4+1/16)	|(6/1)+(6/9)+(6/25) + (6/4)/4+(6/16)/4	|[('R.1.0.0', 6.0, u'6', u'6')]	|




### (1) Mistake Group ['R.0.1.0.1', 'R.0.1.1', 'R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1.0.1', 'R.0.1.1', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|8*(1+1/9+1/25)+8*4*(1/4+1/16)	|8*(1+1/4+1/9+1/25) + 8*4*((1/4)+(1/16))	|[('R.0.1.0.1', 0.1111111111111111, u'1/9', u'1/9'), ('R.0.1.1', 0.04, u'1/25', u'1/25'), ('R.1', 10.0, u'8*4*(1/4+1/16)', u'8*4*((1/4)+(1/16))')]	|




### (75) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:dmn009

	first_attempt
					2015-11-05 03:33:17
	part5_correct_attempt
					['0:31:21', u'.13333']
	part6_incorrect_attempt
					('0:32:19', u'14.86')
	part6_correct_attempt
					['0:32:54', u'21.61']

1 Student ID:h4tu

	first_attempt
					2015-11-06 23:23:42
	part5_correct_attempt
					['0:02:44', u'4-2*2+4/3-2*1+4/5']
	part6_incorrect_attempt
					('0:02:44', u'10/1+10/4+10/9+10/16+10/25')
					('0:06:36', u'10/1+4*10/4+10/9+2*10/16+10/25')
	part6_correct_attempt
					['0:06:43', u'10/1+4*10/4+10/9+4*10/16+10/25']

2 Student ID:jyc018

	first_attempt
					2015-11-04 18:49:56
	part5_correct_attempt
					['0:01:29', u'4-4+4/3-2+4/5']
	part6_incorrect_attempt
					('0:02:19', u'8+4+8/9+1+8/25')
					('0:02:50', u'8+2+8/9+1/2+8/25')
					('0:05:17', u'4*(8+2+8/9+1/2+8/25)')
	part6_correct_attempt
					['0:06:52', u'8+2*4+8/9+1/2*4+8/25']

3 Student ID:lpettit

	first_attempt
					2015-11-07 00:02:46
	part5_correct_attempt
					['0:54:18', u'1 - 1 +1/3 - 1/2 + 1/5']
	part6_incorrect_attempt
					('0:54:45', u'7 + 7/4 + 7/9 + 7/16 + 7/25')
					('0:54:59', u'7 + 14/4 + 7/9 + 14/16 + 7/25')
					('0:56:16', u'7 + 7/4 + 7/4 + 7/9 + 7/16 + 7/16 + 7/25')
					('0:56:46', u'7 - 7/4 + 7/9 - 7/16 + 7/25')

4 Student ID:jfalcone

	first_attempt
					2015-11-05 05:29:27
	part5_correct_attempt
					['0:01:46', u'1 - (2/2) + (1/3) - (2/4) + (1/5)']
	part6_incorrect_attempt
					('0:01:46', u'8 + (16/2^2) + (8/3^2) + (16/4^2) + (8/5^2)')
	part6_correct_attempt
					['0:02:09', u'8 + (32/2^2) + (8/3^2) + (32/4^2) + (8/5^2)']

5 Student ID:ccn001

	first_attempt
					2015-11-02 19:36:06
	part5_correct_attempt
					['0:00:00', u'(4-(2)2+(4/3)-(8/4)+(4/5))']
	part6_incorrect_attempt
					('0:00:00', u'10-(20/4)+(10/9)-(20/16)+(10/25)')
	part6_correct_attempt
					['0:00:50', u'10+(40/4)+(10/9)+(40/16)+(10/25)']

6 Student ID:t2shin

	first_attempt
					2015-11-04 05:19:40
	part5_correct_attempt
					['0:02:35', u'4-2(2)+(4/3)-2(1)+(4/5)']
	part6_incorrect_attempt
					('0:05:32', u'4^2+4^2+(4/3)^2+2^2+(4/5)^2')
	part6_correct_attempt
					['0:06:37', u'8+4*2+(8/3^2)+4*(1/2)+(8/25)']

7 Student ID:vsamant

	first_attempt
					2015-11-02 00:33:46
	part5_correct_attempt
					['0:01:36', u'3-6/2+3/3-6/4+3/5']
	part6_incorrect_attempt
					('0:01:36', u'10+40/4+40/9+10/16+10/25')
	part6_correct_attempt
					['0:01:46', u'10+40/4+10/9+40/16+10/25']

8 Student ID:kebao

	first_attempt
					2015-11-05 21:34:22
	part5_correct_attempt
					['0:00:53', u'2-4/2+2/3-4/4+2/5']
	part6_incorrect_attempt
					('0:00:53', u'8-16/4+8/9-16/16+8/25')
					('0:01:35', u'8+16/4+8/9+16/16+8/25')
	part6_correct_attempt
					['0:01:49', u'8+32/4+8/9+32/16+8/25']

9 Student ID:glcohen

	first_attempt
					2015-11-03 16:57:25
	part5_correct_attempt
					['0:03:02', u'(3/1)-2(3/2)+(3/3)-2(3/4)+(3/5)']
	part6_incorrect_attempt
					('0:12:25', u'11.9972772864')
					('4:56:23', u'(7/(1^2))+(7/(2^2))+(7/(3^2))+(7/(4^2))+(7/(5^2))')
	part6_correct_attempt
					['4:56:46', u'(7/(1^2))+4(7/(2^2))+(7/(3^2))+4(7/(4^2))+(7/(5^2))']

10 Student ID:jguanzho

	first_attempt
					2015-11-03 17:56:24
	part5_correct_attempt
					['0:00:00', u'3(1-1+1/3-1/2+1/5)']
	part6_incorrect_attempt
					('0:00:00', u'7(1-1/2+1/9-1/8+1/25)')
	part6_correct_attempt
					['3:12:24', u'7(1+1+1/9+1/4+1/25)']

11 Student ID:abjara

	first_attempt
					2015-11-04 02:09:05
	part5_correct_attempt
					['0:02:53', u'5 - 5 + 5/3 - 10/4 + 1']
	part6_incorrect_attempt
					('0:04:28', u'6 + 3 + 6/9 + (12/16) + 6/25')
					('0:05:52', u'6 - 3 + (6/9) - (12/16) + 6/25')
					('0:06:03', u'6 + 3 + (6/9) + (12/16) + 6/25')
	part6_correct_attempt
					['0:11:06', u'6 + 4*6/4 + 6/9 + 4*6/16 + 6/25']

12 Student ID:spw006

	first_attempt
					2015-11-04 02:41:54
	part5_correct_attempt
					['0:00:45', u'(5/1 - 10/2 + 5/3 - 10/4 + 5/5)']
	part6_incorrect_attempt
					('0:01:50', u'(10/1 - 20/4 + 10/9 - 20/16 + 10/25)')
					('0:40:29', u'(10/1 + 10/4 + 10/9 + 10/16 + 10/25)')
					('0:40:42', u'(10/1 + 20/4 + 10/9 + 20/16 + 10/25)')
					('0:41:27', u'(10/1 + 10/16 + 10/9 + 10/64 + 10/25)')
					('0:41:36', u'(10/1 + 10/4 + 10/9 + 10/16 + 10/25)')
					('0:42:06', u'(10/1 + 10/8 + 10/9 + 10/32 + 10/25)')
	part6_correct_attempt
					['1:09:53', u'(10/1 + 10/25 + 10/9 + 40/4 + 40/16)']

13 Student ID:rwthomps

	first_attempt
					2015-11-06 21:36:21
	part5_correct_attempt
					['0:01:30', u'(5/1 - (2)5/2 + 5/3 - (2)5/4 + 5/5)']
	part6_incorrect_attempt
					('0:02:08', u'10/1^2  + (-2)^210/2^2 + 10/3^2 + (-2)^210/4^2 + 10/5^2')
	part6_correct_attempt
					['0:02:28', u'10/1^2 + (-2)^2 * 10/2^2 + 10/3^2 + (-2)^2 * 10/4^2 + 10/5^2']

14 Student ID:mhale

	first_attempt
					2015-11-05 20:22:12
	part5_correct_attempt
					['0:01:47', u'1 - 1 + 1/3 - 1/2 + 1/5']
	part6_incorrect_attempt
					('0:01:47', u'6 + 6/4 + 6/9 + 6/16 + 6/25')
	part6_correct_attempt
					['0:02:07', u'6 + 6 + 6/9 + 6/4 + 6/25']

15 Student ID:jhw015

	first_attempt
					2015-11-04 01:49:42
	part5_correct_attempt
					['0:05:30', u'2 - 2 + (2/3) - 1 + (2/5)']
	part6_incorrect_attempt
					('0:06:11', u'8 + 4 + (8/9) + 1 + (8/25)')
					('0:07:04', u'8 - 4 + (8/9) - 1 + (8/25)')
					('19:18:33', u'8+4+(8/9)+1+(8/25)')
	part6_correct_attempt
					['19:19:09', u'8 + 4(8/4) + (8/9) + 4(8/16) + (8/25)']

16 Student ID:edescobe

	first_attempt
					2015-11-01 09:11:23
	part5_correct_attempt
					['0:31:28', u'5-5+5/3-5/2+1']
	part6_incorrect_attempt
					('0:31:28', u'7-7/2+7/9-7/8+7/25')
					('0:39:13', u'7+7/4+7/9+7/16+7/25')
					('0:39:27', u'7+7/2+7/9+7/8+7/25')
	part6_correct_attempt
					['0:40:07', u'7+7+7/9+7/4+7/25']

17 Student ID:agian

	first_attempt
					2015-11-07 00:23:46
	part5_correct_attempt
					['0:02:15', u'(1-2*1/2+1/3-2*1/4+1/5)*2']
	part6_incorrect_attempt
					('0:02:26', u'(1+1/9+1/25)+28*(1/4+1/16)*10')
	part6_correct_attempt
					['0:04:47', u'10*(1+1/9+1/25)+40*(1/4+1/16)']

18 Student ID:t2li

	first_attempt
					2015-11-06 02:40:30
	part5_correct_attempt
					['0:05:12', u'4-4+4/3-2+4/5']
	part6_incorrect_attempt
					('0:05:47', u'7+14/4+7/9+14/16+7/25')
					('0:05:55', u'7+7/4+7/9+7/16+7/25')
	part6_correct_attempt
					['0:06:29', u'7+28/4+7/9+28/16+7/25']

19 Student ID:mtrafeca

	first_attempt
					2015-11-05 00:20:13
	part5_correct_attempt
					['0:05:47', u'1-2/2+1/3-2/4+1/5']
	part6_incorrect_attempt
					('0:06:13', u'6+12/4+6/9+12/16+6/25')
	part6_correct_attempt
					['0:12:02', u'(6+6/9+6/25)+4(6/4+6/16)']

20 Student ID:k5law

	first_attempt
					2015-11-04 07:59:10
	part5_correct_attempt
					['0:09:26', u'[(5/1)-2(5/2)+(5/3)-2(5/4)+(5/5)]']
	part6_incorrect_attempt
					('0:13:49', u'(7/((1)^2))+(7/((2)^2))+(7/((3)^2))+(7/((4)^2))+(7/((5)^2))')
	part6_correct_attempt
					['1:20:50', u'(7/((1)^2))+4(7/((2)^2))+(7/((3)^2))+4(7/((4)^2))+(7/((5)^2))']

21 Student ID:dkurli

	first_attempt
					2015-11-05 03:08:22
	part5_correct_attempt
					['0:01:09', u'2-2+2/3-4/4+2/5']
	part6_incorrect_attempt
					('0:01:09', u'7/1-14/4+7/9-14/16+7/25')
					('0:01:47', u'7/1+14/4+7/9+14/16+7/25')
	part6_correct_attempt
					['0:02:00', u'7/1+28/4+7/9+28/16+7/25']

22 Student ID:jic212

	first_attempt
					2015-11-06 23:10:17
	part5_correct_attempt
					['0:02:13', u'2-2*2/2+2/3-2*2/4+2/5']
	part6_incorrect_attempt
					('0:02:13', u'7+7/4+7/9+7/16+7/25')
	part6_correct_attempt
					['0:02:56', u'7+(-2)^2*7/4+7/9+(-2)^2*7/16+7/25']

23 Student ID:amquinte

	first_attempt
					2015-11-06 23:12:40
	part5_correct_attempt
					['0:01:44', u'0.133333']
	part6_incorrect_attempt
					('0:04:49', u'26.433')
	part6_correct_attempt
					['0:05:25', u'16.81']

24 Student ID:tpmach

	first_attempt
					2015-10-30 21:50:06
	part5_correct_attempt
					['0:03:58', u'3+(-2)(3/2)+3/3+(-2)(3/4)+3/5']
	part6_incorrect_attempt
					('0:03:58', u'3+(-2)^2*(3/2)+3/3+(-2)^2*(3/4)+3/5')
					('0:04:18', u'3+(-1)^2*(3/2)+3/3+(-1)^2*(3/4)+3/5')
	part6_correct_attempt
					['0:06:14', u'10/1+(-2)^2*(10/4)+10/9+(-2)^2*(10/16)+10/25']

25 Student ID:syc078

	first_attempt
					2015-11-05 04:34:52
	part5_correct_attempt
					['0:00:20', u'1-2(1/2)+(1/3)-2(1/4)+(1/5)']
	part6_incorrect_attempt
					('1 day, 16:03:30', u'(7/1)+(7/4)+(7/9)+(7/16)+(7/25)')
	part6_correct_attempt
					['1 day, 16:03:57', u'(7/1)+4(7/4)+(7/9)+4(7/16)+(7/25)']

26 Student ID:r1gu

	first_attempt
					2015-11-05 12:10:39
	part5_correct_attempt
					['0:01:04', u'5-10/2-10/4+5/3+1']
	part6_incorrect_attempt
					('0:01:33', u'9/25+18/16+9/9+18/4+9')
	part6_correct_attempt
					['0:02:09', u'9/25+36/16+9/9+36/4+9']

27 Student ID:acvuong

	first_attempt
					2015-11-05 00:32:37
	part5_correct_attempt
					['0:03:32', u'2 -2+2/3-1+2/5']
	part6_incorrect_attempt
					('0:03:32', u'8+8+8/9+4+8/25')
	part6_correct_attempt
					['0:05:07', u'8+8+8/9+4*8/16+8/25']

28 Student ID:lywong

	first_attempt
					2015-11-04 07:24:45
	part5_correct_attempt
					['0:01:43', u' (2/3) - 1 + (2/5)']
	part6_incorrect_attempt
					('0:02:08', u'10+ (10/4)+(10/9)+(10/16)+(10/25)')
					('0:03:25', u'10+ (10/4)+(10/9)+(10/16)+(10/25)')
					('0:03:36', u'10+ 2*(10/4)+(10/9)+2*(10/16)+(10/25)')
					('0:04:30', u'10+ (10/4)+(10/9)+(10/16)+(10/25)')
					('0:04:48', u'10+ 2*(10/4)+(10/9)+2*(10/16)+(10/25)')
					('0:05:31', u'10+ (10/4)^2+(10/9)+(10/16)^2+(10/25)')
	part6_correct_attempt
					['11:43:06', u'10+ 4(10/4)+(10/9)+4(10/16)+(10/25)']

29 Student ID:jnatale

	first_attempt
					2015-11-04 08:43:34
	part5_correct_attempt
					['0:00:00', u'2*(1/1 - 2/2 + 1/3 - 2/4 + 1/5)']
	part6_incorrect_attempt
					('0:01:43', u'10*(1/1 + 1/4 + 1/9 + 1/16 + 1/25)')
					('0:01:53', u'10*(1/16 + 1/25)')
					('0:02:16', u'10*(1+ 1/9 + 1/25)')
					('0:02:21', u'10*(1/1+ 1/9 + 1/25)')
	part6_correct_attempt
					['0:02:58', u'10*(1/1 + 1/9 + 1/25) + 10*4*(1/4 + 1/16)']

30 Student ID:ggaddi

	first_attempt
					2015-11-01 21:09:45
	part5_correct_attempt
					['0:02:58', u'1-1+1/3-1/2+1/5']
	part6_incorrect_attempt
					('0:02:58', u'8/(1^2)+8/(2^2)+8/(3^2)+8/(4^2)+8/(5^2)')
					('0:03:13', u'8/(1^2)+2*8/(2^2)+8/(3^2)+2*8/(4^2)+8/(5^2)')
					('0:03:32', u'8/(1^2)+8/(2^2)/2+8/(3^2)+8/(4^2)/2+8/(5^2)')
	part6_correct_attempt
					['0:03:52', u'8/(1^2)+4*8/(2^2)+8/(3^2)+4*8/(4^2)+8/(5^2)']

31 Student ID:aordookh

	first_attempt
					2015-11-04 22:13:50
	part5_correct_attempt
					['0:00:00', u'(4/1)-(8/2)+(4/3)-(8/4)+(4/5)']
	part6_incorrect_attempt
					('0:00:55', u'8+(8/4)+(8/9)+(8/16)+(8/25)')
					('0:02:19', u'8+(8/4)+(8/9)+(8/16)+(8/25)+(8/4)+(8/16)')
	part6_correct_attempt
					['1 day, 22:38:26', u'8+(32/4)+(8/9)+(32/16)+(8/25)']

32 Student ID:smohiman

	first_attempt
					2015-11-02 02:16:48
	part5_correct_attempt
					['0:04:47', u'3-3+3/3-3/2+3/5']
	part6_incorrect_attempt
					('0:04:47', u'3+3+3/3+3/2+3/5')
					('0:07:13', u'10+10/2+10/9+10/8+10/25')
					('0:07:34', u'10+10/4+10/9+10/16+10/25')
	part6_correct_attempt
					['0:08:53', u'10+10+10/9+10/4+10/25']

33 Student ID:agarango

	first_attempt
					2015-11-05 23:55:25
	part5_correct_attempt
					['0:01:33', u'(1/1)-(2)(1/2)+(1/3)-(2/4)+(1/5)']
	part6_incorrect_attempt
					('0:02:03', u'(7/1)-(14/4)+(7/9)-(14/16)+(7/25)')
					('0:03:22', u'(7/1)+(14/4)+(7/9)+(14/16)+(7/25)')
	part6_correct_attempt
					['0:04:03', u'(7/1)+4(7/4)+(7/9)+4(7/16)+(7/25)']

34 Student ID:jmmcalex

	first_attempt
					2015-11-06 23:19:53
	part5_correct_attempt
					['0:00:00', u'(4/1-4+4/3-4/2+4/5)']
	part6_incorrect_attempt
					('0:01:10', u'(10/1+10/4+10/9+10/16+10/25)')
	part6_correct_attempt
					['0:01:52', u'(10/1+40/4+10/9+40/16+10/25)']

35 Student ID:achinn

	first_attempt
					2015-11-03 21:21:12
	part5_correct_attempt
					['0:00:30', u'4-4+(4/3)-2+(4/5)']
	part6_incorrect_attempt
					('0:00:30', u'10+(10/4)+(10/9)+(10/16)+(10/25)')
	part6_correct_attempt
					['0:00:52', u'10+4(10/4)+(10/9)+4(10/16)+(10/25)']

36 Student ID:dwzhang

	first_attempt
					2015-11-04 20:59:44
	part5_correct_attempt
					['0:05:10', u'3/1 - 2*3/2 + 3/3 - 2*3/4 + 3/5']
	part6_incorrect_attempt
					('0:05:10', u'7/1 + 2*7/4 + 7/9 + 2*7/16 + 7/25')
					('0:05:47', u'7/1 + 7/16 + 7/9 + 7/256 + 7/25')
	part6_correct_attempt
					['2 days, 0:29:31', u'7/1 + 7/9 + 7/25 + 28/4 + 28/16']

37 Student ID:dis003

	first_attempt
					2015-11-05 21:51:39
	part5_correct_attempt
					['0:03:46', u'2/1 - 2*(2/2) + 2/3 - 2(2/4) + 2/5']
	part6_incorrect_attempt
					('0:04:04', u'8/1**2+8/2**2+8/3**2+8/4**2+8/5**2')
					('0:04:43', u'8/1**2 + 2* 8/2**2 + 8/3**2 + 2*8/4**2 + 8/5**2')
					('0:06:56', u'8/1**2+8/2**2+8/3**2+8/4**2+8/5**2')
					('1 day, 0:55:47', u'631/1125')
					('1 day, 0:58:11', u'6*(1+1/4+1/9+1/16+1/25)')
					('1 day, 0:58:32', u'8*(1+1/4+1/9+1/16+1/25)')
					('1 day, 1:02:56', u'8**(1+1/4+1/9+1/16+1/25)')
	part6_correct_attempt
					['1 day, 1:16:25', u'8*(1+1/9+1/25)+8*4*(1/4+1/16)']

38 Student ID:dgunawan

	first_attempt
					2015-11-05 08:39:09
	part5_correct_attempt
					['0:00:41', u'1 - 2/2 + 1/3 - 2/4 + 1/5 ']
	part6_incorrect_attempt
					('0:01:39', u'(8/1^2) + (8/2^2) + (8/3^2) + (8/4^2) + (8/5^2)')
	part6_correct_attempt
					['0:01:50', u'(8/1^2) + (4)(8/2^2) + (8/3^2) + (4)(8/4^2) + (8/5^2)']

39 Student ID:atorr

	first_attempt
					2015-11-05 20:05:29
	part5_correct_attempt
					['0:02:31', u'5 - (5) + (5/3) - (5/2) + 1']
	part6_incorrect_attempt
					('0:02:31', u'6 + (3) + (6/9) + (12/16) + (6/25)')
					('0:02:40', u'6 + (12) + (6/9) + (12/16) + (6/25)')
					('0:02:58', u'6 + (12/4) + (6/9) + (12/16) + (6/25)')
	part6_correct_attempt
					['0:57:42', u'6 + (24/4) + (6/9) + (24/16) + (6/25)']

40 Student ID:rraiyyan

	first_attempt
					2015-11-06 23:21:00
	part5_correct_attempt
					['0:05:48', u'5*(1-2/2+1/3-2/4+1/5)']
	part6_incorrect_attempt
					('0:08:52', u'(8 + 16/4 + 8/9 + 16/16 + 8/25)')
					('0:09:42', u'(8 + 8/4 + 8/9 + 8/16 + 8/25)')
					('0:10:08', u'(8 + 2*8/4 + 8/9 + 2*8/16 + 8/25)')
					('0:10:17', u'(8 - 2*8/4 + 8/9 - 2*8/16 + 8/25)')
					('0:10:56', u'(1 + 2*1/4 + 1/9 + 2*1/16 + 1/25)*8')
					('0:11:19', u'(1 + 1/4 + 1/9 + 1/16 + 1/25)*8')
					('0:11:32', u'(1 + 2/4 + 1/9 + 2/16 + 1/25)*8')
					('0:12:56', u'(1 + 2/4 + 1/9 + 2/16 + 1/25)*8^2')
	part6_correct_attempt
					['0:13:15', u'(1 + 4/4 + 1/9 + 4/16 + 1/25)*8']

41 Student ID:hachrist

	first_attempt
					2015-11-03 21:16:33
	part5_correct_attempt
					['0:01:49', u'4 - 4 + 4/3 - 2 + 4/5']
	part6_incorrect_attempt
					('0:01:49', u'7 - 14/4 + 7/9 - 14/16 + 7/25')
					('0:08:14', u'7 + 7/4 + 7/9 + 7/16 + 7/25')
					('0:08:34', u'7 + 14/4 + 7/9 + 14/16 + 7/25')
					('0:13:20', u'((1-0.133333)^2 + (2-0.133333)^2 + (3-0.133333)^2+(4-0.133333)^2+(5-0.133333)^2 )/4')
					('0:16:22', u'7 + 7/4 + 7/9 + 7/16 + 7/25')
					('0:31:34', u'7 - 7/4 + 7/9 - 7/16 + 7/25')
	part6_correct_attempt
					['20:45:19', u'7 + 28/4 + 7/9 + 28/16 + 7/25']

42 Student ID:kew017

	first_attempt
					2015-11-05 22:49:02
	part5_correct_attempt
					['0:04:17', u'4-4+4/3-2+4/5']
	part6_incorrect_attempt
					('0:04:17', u'7/1+7/4+7/9+7/16+7/25')
	part6_correct_attempt
					['0:04:41', u'7/1+7+7/9+7/4+7/25']

43 Student ID:dsmonaha

	first_attempt
					2015-11-02 17:23:41
	part5_correct_attempt
					['0:08:34', u'1/6']
	part6_incorrect_attempt
					('0:08:43', u'5269/600')
					('0:09:53', u'3197/300')
					('0:12:19', u'5269/600')
					('0:15:27', u'518/75')
	part6_correct_attempt
					['0:18:37', u'2161/150']

44 Student ID:apokhare

	first_attempt
					2015-11-05 21:40:12
	part5_correct_attempt
					['0:00:00', u'(1/3-1/2+1/5)*3']
	part6_incorrect_attempt
					('0:00:54', u'(1/3-1/2+1/5)*6')
					('0:02:37', u'(1-1/2+1/9-1/8+1/25)*6')
					('0:03:10', u'(1+1/2+1/9+1/8+1/25)*6')
	part6_correct_attempt
					['0:04:07', u'6*(1+1/9+ 1/25) + 24*(1/4+1/16)']

45 Student ID:avasavad

	first_attempt
					2015-11-04 23:13:33
	part5_correct_attempt
					['0:02:08', u'5 - 10/2 + 5/3 - 10/4 + 1']
	part6_incorrect_attempt
					('0:02:08', u'10 + 10/4 + 10/9 + 10/16 + 10/25')
					('0:02:20', u'10 + 20/4 + 10/9 + 20/16 + 10/25')
					('0:02:36', u'10 - 20/4 + 10/9 - 20/16 + 10/25')
	part6_correct_attempt
					['0:21:23', u'10 + 40/4 + 10/9 + 40/16 + 10/25']

46 Student ID:tstevens

	first_attempt
					2015-11-06 11:55:11
	part5_correct_attempt
					['0:01:12', u'4/3-2+.8']
	part6_incorrect_attempt
					('0:03:21', u'6+3+2/3+6/8+6/25')
	part6_correct_attempt
					['0:03:48', u'6+6+2/3+12/8+6/25']

47 Student ID:zhw110

	first_attempt
					2015-11-06 01:00:43
	part5_correct_attempt
					['0:00:00', u'4-4+4/3-2+4/5']
	part6_incorrect_attempt
					('0:00:00', u'10-20/4+10/9-20/16+10/25')
	part6_correct_attempt
					['23:38:57', u'10+40/4+10/9+40/16+10/25']

48 Student ID:l8ngo

	first_attempt
					2015-10-30 16:31:06
	part5_correct_attempt
					['0:00:00', u'2-2+2/3-2*2/4+2/5']
	part6_incorrect_attempt
					('0:00:00', u'7-2*7/4+7/9-2*7/16+7/25')
	part6_correct_attempt
					['4 days, 8:28:44', u'7+4*7/4+7/9+4*7/16+7/25']

49 Student ID:ytc012

	first_attempt
					2015-11-05 22:02:52
	part5_correct_attempt
					['0:01:41', u'2-2+2/3-4/4+2/5']
	part6_incorrect_attempt
					('0:02:00', u'8+4+8/9+16/16+8/25')
	part6_correct_attempt
					['0:02:32', u'8+8+8/9+32/16+8/25']

50 Student ID:chc286

	first_attempt
					2015-11-01 01:54:36
	part5_correct_attempt
					['0:01:37', u'5/1-2*(5/2)+5/3-2*(5/4)+5/5']
	part6_incorrect_attempt
					('0:01:37', u'5/1+4*(5/2)+5/3+4*(5/4)+5/5')
	part6_correct_attempt
					['0:02:16', u'8/1+4*(8/4)+8/9+4*(8/16)+8/25']

51 Student ID:sayao

	first_attempt
					2015-11-04 01:38:15
	part5_correct_attempt
					['0:02:38', u'3-2*3/2+3/3-2*3/4+3/5']
	part6_incorrect_attempt
					('0:03:27', u'9/1-2*9/4+9/9 - 2*9/16+9/25')
	part6_correct_attempt
					['0:04:03', u'9/1+4*9/4+9/9 + 4*9/16+9/25']

52 Student ID:anvan

	first_attempt
					2015-11-05 16:05:53
	part5_correct_attempt
					['0:00:35', u'2 - 2 + 2/3 - 1 + 2/5']
	part6_incorrect_attempt
					('0:05:21', u'9 + 18/4 + 1 + 18/16 + 9/25')
					('0:05:43', u'9 + (9/4)^2 + 1 + (9/16)^2 + 9/25')
	part6_correct_attempt
					['0:27:07', u'9 + 4(9/4) + 1 + 4(9/16) + 9/25']

53 Student ID:achava

	first_attempt
					2015-11-06 07:27:32
	part5_correct_attempt
					['0:02:50', u'3-3+1-(3/2)+(3/5)']
	part6_incorrect_attempt
					('0:33:02', u'8+(16*(8/4))+(8/9)+(16(8/16))+(8/25)')
	part6_correct_attempt
					['0:34:16', u'8+(4*(8/4))+(8/9)+(4(8/16))+(8/25)']

54 Student ID:hmshah

	first_attempt
					2015-11-05 09:41:00
	part5_correct_attempt
					['0:02:20', u'2 - 2*1 + 2/3 - 2*(2/4) + 2/5']
	part6_incorrect_attempt
					('0:02:28', u'2 - 1 + 2/3 - 2/4 + 2/5')
					('0:02:42', u'6 + 6/4 + 6/9+ 6/16+ 6/25')
					('0:02:59', u'6 + 12/4 + 6/9+ 12/16+ 6/25')
					('0:03:29', u'6 - 12/4 + 6/9 - 12/16+ 6/25')
					('0:03:44', u'6 + 6/4 + 6/9+ 6/16+ 6/25')

55 Student ID:dtea

	first_attempt
					2015-11-07 00:18:37
	part5_correct_attempt
					['0:41:40', u'4/1-4/2*2+4/3-4/4*2+4/5']
	part6_incorrect_attempt
					('0:41:40', u'(6/1-6/4^2+6/9-6/16^2+6/25)')

56 Student ID:lahawkin

	first_attempt
					2015-11-04 04:48:19
	part5_correct_attempt
					['0:02:44', u'(4/1)-2(4/2)+(4/3)-2(4/4)+(4/5)']
	part6_incorrect_attempt
					('0:06:26', u'(6/1)+(6/4)/4+(6/9)+(6/16)/4+(6/25)')
					('0:06:36', u'(6/1)+(6/4)+(6/9)+(6/16)+(6/25)')
	part6_correct_attempt
					['0:08:48', u'(6/1)+(6/9)+(6/25) + 4(6/4)+4(6/16)']

57 Student ID:cstringh

	first_attempt
					2015-11-04 06:44:53
	part5_correct_attempt
					['0:01:42', u'5-(2(5/2))+5/3-(2(5/4))+1']
	part6_incorrect_attempt
					('0:06:51', u'8-(2(2))+8/9-(2(1/2))+8/25')
	part6_correct_attempt
					['0:09:58', u'8*(1+1/9+1/25) +8*4*(1/4+1/16)']

58 Student ID:ksrijong

	first_attempt
					2015-11-04 23:10:06
	part5_correct_attempt
					['0:01:32', u'4-4+4/3-2+4/5']
	part6_incorrect_attempt
					('0:01:32', u'8/1-4+8/9-1+8/25')
					('0:02:03', u'8/1+4+8/9+1+8/25')
					('0:05:15', u'8/1+8/16+8/9+8/64+8/25')
					('0:05:33', u'8/1+8/4+8/9+8/16+8/25')
					('0:05:45', u'8/1+2*8/4+8/9+2*8/16+8/25')
					('2 days, 0:08:25', u'8/1+8/4+8/9+8/16+8/25')
					('2 days, 0:10:36', u'8/1+8/8+8/9+8/32+8/25')
	part6_correct_attempt
					['2 days, 0:13:13', u'8/1+4*8/4+8/9+4*8/16+8/25']

59 Student ID:edcole

	first_attempt
					2015-11-06 23:40:14
	part5_correct_attempt
					['0:03:10', u'3-2*(3/2)+3/3-2*(3/4)+3/5']
	part6_incorrect_attempt
					('0:03:58', u'8/1+2*(8/4)+8/9+2*(8/16)+8/25')
	part6_correct_attempt
					['0:04:08', u'8/1+4*(8/4)+8/9+4*(8/16)+8/25']

60 Student ID:v4sharma

	first_attempt
					2015-11-04 20:39:34
	part5_correct_attempt
					['0:03:07', u'4(1 - 1 + 1/3 - 2/4 + 1/5)']
	part6_incorrect_attempt
					('0:04:04', u'9(1 - 2/4 + 1/9 - 2/16 +1/25)')
					('23:26:58', u'9(1 + 2/4 + 1/9 + 2/16 +1/25)')
					('23:29:54', u'9(1 + 1/4 + 1/9 + 1/16 +1/25)')
	part6_correct_attempt
					['1 day, 0:22:00', u'9(1 + 4/4 + 1/9 + 4/16 +1/25)']

61 Student ID:ralhadda

	first_attempt
					2015-10-31 20:35:01
	part5_correct_attempt
					['0:09:59', u'0.0333333']
	part6_incorrect_attempt
					('0:11:45', u'(10/1)-(20/4)+(10/9)-(20/16)+(10/25)')
					('0:15:45', u'5.261111')

62 Student ID:kquong

	first_attempt
					2015-11-02 05:16:14
	part5_correct_attempt
					['0:07:24', u'4 -4 + 4/3 - 2 + 4/5']
	part6_incorrect_attempt
					('0:07:24', u'10 + 10/16 + 10/9 + 10/64 + 10/25')
					('0:07:45', u'10 + 10/2 + 10/9 + 10/8 + 10/25')
	part6_correct_attempt
					['0:09:52', u'10/1+ 4*10/4 + 10/9 + 4*10/16 + 10/25']

63 Student ID:rohan

	first_attempt
					2015-11-07 00:05:28
	part5_correct_attempt
					['0:02:38', u'3-3+3/3-3/2+3/5']
	part6_incorrect_attempt
					('0:03:12', u'3+6+3/3+3+3/5')
	part6_correct_attempt
					['0:03:45', u'8/1+8+8/9+8/4+8/25']

64 Student ID:k4ma

	first_attempt
					2015-11-06 21:26:38
	part5_correct_attempt
					['0:00:30', u'1-2*.5+(1/3)-2(1/4)+(1/5)']
	part6_incorrect_attempt
					('0:01:40', u'9+2*(9/2^2)+(9/3^2)+2*(9/4^2)+(9/5^2)')
	part6_correct_attempt
					['0:02:12', u'9+2^2*(9/2^2)+(9/3^2)+2^2*(9/4^2)+(9/5^2)']

65 Student ID:kew060

	first_attempt
					2015-11-03 02:11:02
	part5_correct_attempt
					['0:00:00', u'0.1']
	part6_incorrect_attempt
					('0:00:21', u'89/150')
					('0:00:31', u'89/150')
					('1 day, 23:24:55', u'89/150')
					('1 day, 23:25:43', u'14.6')
	part6_correct_attempt
					['1 day, 23:26:12', u'6 + 4(6/4) + 6/9 + 4(6/16) + 6/25']

66 Student ID:q3wen

	first_attempt
					2015-11-04 21:07:59
	part5_correct_attempt
					['0:00:00', u'1/30']
	part6_incorrect_attempt
					('0:00:00', u'4.735')
					('0:01:01', u'23.86')
	part6_correct_attempt
					['0:01:38', u'21.61']

67 Student ID:yil035

	first_attempt
					2015-11-04 00:43:35
	part5_correct_attempt
					['0:02:10', u'2/15']
	part6_incorrect_attempt
					('0:02:10', u'6122/225')
	part6_correct_attempt
					['0:03:11', u'4322/225']

68 Student ID:m8woo

	first_attempt
					2015-11-05 21:03:09
	part5_correct_attempt
					['0:00:00', u'[3/1 - 2*3/2 + 3/3 - 2*3/4 + 3/5]']
	part6_incorrect_attempt
					('0:00:00', u'[3/1 + 4*3/4 + 3/9 + 4*3/16 + 3/25]')
	part6_correct_attempt
					['0:00:47', u'[10/1 + 4*10/4 + 10/9 + 4*10/16 + 10/25]']

69 Student ID:akg009

	first_attempt
					2015-11-06 21:00:56
	part5_correct_attempt
					['0:02:10', u'(1-2*(1/2)+1/3-2*(1/4)+1/5)']
	part6_incorrect_attempt
					('0:03:12', u'(6/1+6/4+6/9+6/16+6/25)')
					('0:03:26', u'(6/1+2*(6/4)+6/9+2*(6/16)+6/25)')
	part6_correct_attempt
					['0:04:00', u'(6/1+4*(6/4)+6/9+4*(6/16)+6/25)']

70 Student ID:sghouse

	first_attempt
					2015-11-04 20:46:39
	part5_correct_attempt
					['0:40:10', u'5 - 10/2 + 5/3 - 10/4 + 1']
	part6_incorrect_attempt
					('0:40:10', u'10/1 + 20/4 + 10/9 + 20/16 + 10/25')
					('0:41:04', u'10/1 + 10/4 + 10/9 + 10/16 + 10/25')
					('0:42:14', u'(10/1 + 10/4 + 10/9 + 10/16 + 10/25) *4')
					('5:42:07', u'(10/1 + 20/4 + 10/9 + 20/16 + 10/25)')
					('1 day, 4:12:43', u'10/1 + 10/4 + 10/9 + 10/16 + 10/25')
	part6_correct_attempt
					['1 day, 6:34:51', u'10+10/9+10/25 +40/4+40/16']

71 Student ID:mjethani

	first_attempt
					2015-11-05 04:35:33
	part5_correct_attempt
					['0:02:52', u'(5/1) - ((2)5/2) + (5/3) - ((2)5/4) + (5/5)']
	part6_incorrect_attempt
					('0:03:32', u'(5/1) - ((2)5/2) + (5/3) - ((2)5/4) + (5/5)')
	part6_correct_attempt
					['1 day, 16:03:17', u'(10) + 4(10/4) + (10/9) + 4(10/16) + (10/25)']

72 Student ID:kgrozav

	first_attempt
					2015-11-05 20:01:44
	part5_correct_attempt
					['0:28:44', u'0.03333333']
	part6_incorrect_attempt
					('0:28:44', u'2.4011111')
	part6_correct_attempt
					['0:29:06', u'2.4011111*7']

73 Student ID:k3tan

	first_attempt
					2015-11-04 01:49:58
	part5_correct_attempt
					['0:05:45', u'4/3-2+4/5']
	part6_incorrect_attempt
					('0:06:11', u'10 +10/2+10/9 + 10/8 + 10/25')
					('0:06:54', u'10 -10/2+10/9 - 10/8 + 10/25')
					('0:07:08', u'10 +10/4+10/9 + 10/16 + 10/25')
	part6_correct_attempt
					['3:45:30', u'10 +10+10/9 + 10/4 + 10/25']

74 Student ID:arvenega

	first_attempt
					2015-11-05 00:24:50
	part5_correct_attempt
					['0:02:42', u'(2/1) - 2*(2/2) + (2/3) - 2*(2/4) + (2/5)']
	part6_incorrect_attempt
					('0:02:42', u'(10/1^2) - 2*(10/2^2) + (10/3^2) - 2*(10/4^2) + (10/5^2)')
					('0:04:09', u'(10/1^2) + 2*(10/2^2) + (10/3^2) + 2*(10/4^2) + (10/5^2)')
					('0:04:18', u'(10/1^2) + 2/(10/2^2) + (10/3^2) + 2/(10/4^2) + (10/5^2)')
					('1 day, 16:37:19', u'(10/1^2) + 2*(10/2^2) + (10/3^2) + 2*(10/4^2) + (10/5^2)')
	part6_correct_attempt
					['1 day, 20:08:21', u'(10/1^2) + (2^2)*(10/2^2) + (10/3^2) + (2^2)*(10/4^2) + (10/5^2)']












