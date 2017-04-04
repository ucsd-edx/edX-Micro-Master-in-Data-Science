#Problem 5

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




## Part 1

### (87) Mistake Group Digits of size 87




### (50) Mistake Group Fraction of size 50




### (3) Mistake Group ['R.1.0'] of size 3
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|9*(9+1)/(2*9)	|5 + (4.5*(4/9) + 2/9 * 9)	|[('R.1.0', 2.0, u'2', u'4.5*(4/9)')]	|
|1	|6*(6+1)/(2*6)	|1/(2^6)	|[('R.1.0', 2.0, u'2', u'2')]	|
|2	|8*(8+1)/(2*8)	|(7*8)/(2*7)	|[('R.1.0', 2.0, u'2', u'2')]	|




### (3) Mistake Group ['R.1'] of size 3
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|7*(7+1)/(2*7)	|(7*6)/(2*7)	|[('R.1', 14.0, u'2*7', u'2*7')]	|
|1	|8*(8+1)/(2*8)	|(7*8)/(2*8)	|[('R.1', 16.0, u'2*8', u'2*8')]	|
|2	|8*(8+1)/(2*8)	|(8*8)/(2*8)	|[('R.1', 16.0, u'2*8', u'2*8')]	|




### (1) Mistake Group ['R.0'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|8*(8+1)/(2*8)	|8*9/18	|[('R.0', 72.0, u'8*(8+1)', u'8*9')]	|




### (1) Mistake Group ['R.0', 'R.1.0'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|8*(8+1)/(2*8)	|(8*(8+1))/(2*(8+1))	|[('R.0', 72.0, u'8*(8+1)', u'8*(8+1)'), ('R.1.0', 2.0, u'2', u'2')]	|




### (51) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:galu

	first_attempt
					2015-10-30 23:28:45
	part1_incorrect_attempt
					('0:00:00', u'1/8')
	part1_correct_attempt
					['0:30:31', u'36/8']

1 Student ID:apokhare

	first_attempt
					2015-10-26 00:59:09
	part1_incorrect_attempt
					('0:00:00', u'1/8')
	part1_correct_attempt
					['0:03:30', u'8*9/16']

2 Student ID:dlgoldbe

	first_attempt
					2015-10-30 01:29:52
	part1_incorrect_attempt
					('0:00:00', u'C(9,1)')
	part1_correct_attempt
					['4:35:02', u'5']

3 Student ID:lywong

	first_attempt
					2015-10-28 08:25:03
	part1_incorrect_attempt
					('0:00:00', u'1/10')
	part1_correct_attempt
					['0:01:27', u'5.5']

4 Student ID:mpanelo

	first_attempt
					2015-10-28 19:03:29
	part1_incorrect_attempt
					('0:00:00', u'2.5')
	part1_correct_attempt
					['0:00:24', u'4.5']

5 Student ID:hkhodada

	first_attempt
					2015-10-23 19:19:40
	part1_incorrect_attempt
					('0:00:00', u'1/8')
					('0:00:00', u'1/6')
	part1_correct_attempt
					['4 days, 5:27:04', u'36/8']

6 Student ID:asetters

	first_attempt
					2015-10-27 05:20:54
	part1_incorrect_attempt
					('0:00:00', u'(1/8)*((8+9)/2)')
					('0:00:47', u'(1/8)*((7+8)/2)')
					('0:01:40', u'(8+9)/2/8')
					('0:02:05', u'((8+9)/2)/8')
	part1_correct_attempt
					['0:07:48', u'(1/8) *((8*9)/2)']

7 Student ID:achava

	first_attempt
					2015-10-25 07:44:02
	part1_incorrect_attempt
					('0:00:00', u'1/8')
					('0:00:00', u'1/8')
					('0:00:17', u'(1/8)^8')
	part1_correct_attempt
					['3 days, 0:16:11', u'(1/8) + (2/8) + (3/8) + (4/8) + (5/8) + (6/8) + (7/8) + (1)']

8 Student ID:d6he

	first_attempt
					2015-10-28 19:19:34
	part1_incorrect_attempt
					('0:00:00', u'1/8')
	part1_correct_attempt
					['0:03:00', u'36/8']

9 Student ID:cprafull

	first_attempt
					2015-10-30 02:34:51
	part1_incorrect_attempt
					('0:00:00', u'2.5')
	part1_correct_attempt
					['0:09:16', u'3.5']

10 Student ID:jjm019

	first_attempt
					2015-10-28 20:54:54
	part1_incorrect_attempt
					('0:00:00', u'1/8')
					('0:12:11', u'1/2')
					('0:12:20', u'1/8')
	part1_correct_attempt
					['1 day, 11:02:51', u'(8*9)/(2*8)']

11 Student ID:krau

	first_attempt
					2015-10-29 21:58:53
	part1_incorrect_attempt
					('0:00:00', u'5.5')
	part1_correct_attempt
					['0:00:11', u'3.5']

12 Student ID:awollner

	first_attempt
					2015-10-27 03:26:48
	part1_incorrect_attempt
					('0:00:00', u'1/10')
	part1_correct_attempt
					['0:00:23', u'1/10(1+2+3+4+5+6+7+8+9+10)']

13 Student ID:pcdo

	first_attempt
					2015-10-28 23:37:20
	part1_incorrect_attempt
					('0:00:00', u'(8*(8+1)/2*8)')
	part1_correct_attempt
					['0:00:31', u'8*(8+1)/(2*8)']

14 Student ID:k5law

	first_attempt
					2015-10-26 06:14:11
	part1_incorrect_attempt
					('0:00:00', u'1/10')
	part1_correct_attempt
					['0:02:54', u'(1+2+3+4+5+6+7+8+9+10)/10']

15 Student ID:dlt009

	first_attempt
					2015-10-28 04:42:49
	part1_incorrect_attempt
					('0:00:00', u'1/10')
	part1_correct_attempt
					['0:04:49', u'(1/10)(1+2+3+4+5+6+7+8+9+10)']

16 Student ID:mbl003

	first_attempt
					2015-10-27 08:33:05
	part1_incorrect_attempt
					('0:00:00', u'1/8')
	part1_correct_attempt
					['0:01:19', u'(1+2+3+4+5+6+7+8)/8']

17 Student ID:psable

	first_attempt
					2015-10-30 05:56:19
	part1_incorrect_attempt
					('0:00:00', u'1/10')
	part1_correct_attempt
					['0:01:53', u'5.5']

18 Student ID:j5phung

	first_attempt
					2015-10-26 01:38:44
	part1_incorrect_attempt
					('0:00:00', u'1/8')
	part1_correct_attempt
					['1 day, 13:40:15', u'1/8 + 2/8 + 3/8 + 4/8 + 5/8 + 6/8 + 7/8 + 8/8']

19 Student ID:n2patil

	first_attempt
					2015-10-28 06:15:26
	part1_incorrect_attempt
					('0:00:00', u'1/2')
					('0:00:00', u'10.5')
	part1_correct_attempt
					['16:49:13', u'3.5']

20 Student ID:s2chaudh

	first_attempt
					2015-10-28 02:32:53
	part1_incorrect_attempt
					('0:00:00', u'1/10*10')
					('0:00:08', u'1/10')
					('0:00:00', u'1/10')
	part1_correct_attempt
					['22:06:47', u'1/10*(55)']

21 Student ID:tpmach

	first_attempt
					2015-10-28 06:17:09
	part1_incorrect_attempt
					('0:00:00', u'1/6')
	part1_correct_attempt
					['0:00:54', u'1/6(1+2+3+4+5+6)']

22 Student ID:haw081

	first_attempt
					2015-10-25 07:38:48
	part1_incorrect_attempt
					('0:00:00', u'1/8')
	part1_correct_attempt
					['0:01:59', u'(1/8)(1+2+3+4+5+6+7+8)']

23 Student ID:dcastlem

	first_attempt
					2015-10-29 18:56:37
	part1_incorrect_attempt
					('0:00:00', u'1/4')
	part1_correct_attempt
					['1 day, 0:40:13', u'36/8']

24 Student ID:cfgutier

	first_attempt
					2015-10-29 17:53:02
	part1_incorrect_attempt
					('0:00:00', u'1/6')
					('0:00:16', u'1/(6^6)')
	part1_correct_attempt
					['0:01:16', u'(1+2+3+4+5+6)/6']

25 Student ID:hak014

	first_attempt
					2015-10-26 23:04:03
	part1_incorrect_attempt
					('0:00:00', u'1/100')
					('0:00:00', u'(2/100)+(6/100)+(12/100)+(20/100)+(30/100)+(42/100)+(40/100)+(36/100)+(30/100)+(22/100)+(12/100)')
	part1_correct_attempt
					['19:07:51', u'(1+2+3+4+5+6+7+8+9+10)/10']

26 Student ID:twsalim

	first_attempt
					2015-10-30 05:41:04
	part1_incorrect_attempt
					('0:00:00', u'4.8')
					('0:00:20', u'4.888')
	part1_correct_attempt
					['0:00:35', u'4.5']

27 Student ID:dwzhang

	first_attempt
					2015-10-29 21:24:51
	part1_incorrect_attempt
					('0:00:00', u'1/6')
	part1_correct_attempt
					['0:01:06', u'1/6 + 2/6 + 3/6 + 4/6 + 5/6 + 6/6']

28 Student ID:kalang

	first_attempt
					2015-10-29 01:15:39
	part1_incorrect_attempt
					('0:00:00', u'1*(1+1)/(2*1)')
	part1_correct_attempt
					['0:00:28', u'9*(1+9)/(2*9)']

29 Student ID:dgunawan

	first_attempt
					2015-10-29 23:17:14
	part1_incorrect_attempt
					('0:00:00', u'1/6')
					('0:00:10', u'1(1/10)')
	part1_correct_attempt
					['0:01:04', u'(1/10)[1+2+3+4+5+6+7+8+9+10]']

30 Student ID:kew017

	first_attempt
					2015-10-30 01:14:38
	part1_incorrect_attempt
					('0:00:00', u'1/6')
	part1_correct_attempt
					['0:00:21', u'(1/6)+2(1/6)+3(1/6)+4(1/6)+5(1/6)+6(1/6)']

31 Student ID:yeh013

	first_attempt
					2015-10-28 06:16:11
	part1_incorrect_attempt
					('0:00:00', u'1/6')
	part1_correct_attempt
					['0:01:05', u'21/6']

32 Student ID:z3meng

	first_attempt
					2015-10-30 22:38:20
	part1_incorrect_attempt
					('0:00:00', u'2.25')
	part1_correct_attempt
					['0:03:13', u'4.5']

33 Student ID:ytc012

	first_attempt
					2015-10-29 11:34:00
	part1_incorrect_attempt
					('0:00:00', u'1/8')
					('0:00:27', u'8!/8^8')
					('0:00:39', u'8!/8')
	part1_correct_attempt
					['0:00:57', u'(8+7+6+5+4+3+2+1)/8']

34 Student ID:glcohen

	first_attempt
					2015-10-27 17:35:25
	part1_incorrect_attempt
					('0:00:00', u'(2 (1/36)) + (3 (1/36)) + (4(2/36))+(5(2/36))+(6(3/36))+(7(3/36))+(8(4/36))+(9(4/36))+(10(4/36))+(11(3/36))+(12(3/36))+(13(2/36))+(14(2/36))+(15(1/36))+(16(1/36))')
	part1_correct_attempt
					['0:01:34', u'1(1/8)+2(1/8)+3(1/8)+4(1/8)+5(1/8)+6(1/8)+7(1/8)+8(1/8)']

35 Student ID:jnn015

	first_attempt
					2015-10-27 04:39:27
	part1_incorrect_attempt
					('0:00:00', u'6!/6')
	part1_correct_attempt
					['0:00:22', u'(6+5+4+3+2+1)/6']

36 Student ID:ssamudra

	first_attempt
					2015-10-30 21:35:49
	part1_incorrect_attempt
					('0:00:00', u'1/8')
					('0:00:21', u'1/8*8')
	part1_correct_attempt
					['0:03:26', u'8(1/8) + 7(1/8) + 6(1/8)+ 5(1/8) + 4(1/8) + 3(1/8)+ 2(1/8) + 1/8']

37 Student ID:haliew

	first_attempt
					2015-10-29 01:04:24
	part1_incorrect_attempt
					('0:00:00', u'1/8')
	part1_correct_attempt
					['0:00:50', u'4.5']

38 Student ID:a2ahmed

	first_attempt
					2015-10-30 19:51:51
	part1_incorrect_attempt
					('0:00:00', u'1/10')
					('0:01:07', u'1/9')
	part1_correct_attempt
					['0:02:54', u'5.5']

39 Student ID:cstringh

	first_attempt
					2015-10-26 16:37:38
	part1_incorrect_attempt
					('0:00:00', u'1/6')
					('0:01:29', u'.1')
	part1_correct_attempt
					['0:02:53', u'3.5']

40 Student ID:arc013

	first_attempt
					2015-10-30 22:08:00
	part1_incorrect_attempt
					('0:00:00', u'4.5')
	part1_correct_attempt
					['0:01:16', u'5.5']

41 Student ID:r2fisher

	first_attempt
					2015-10-26 22:50:07
	part1_incorrect_attempt
					('0:00:00', u'1/8')
	part1_correct_attempt
					['0:00:59', u'36/8']

42 Student ID:vasharma

	first_attempt
					2015-10-30 23:21:31
	part1_incorrect_attempt
					('0:00:00', u'3.5+4')
	part1_correct_attempt
					['0:00:06', u'3.5']

43 Student ID:atorr

	first_attempt
					2015-10-29 06:37:51
	part1_incorrect_attempt
					('0:00:00', u'1/8')
	part1_correct_attempt
					['0:00:28', u'(1+2+3+4+5+6+7+8)*(1/8)']

44 Student ID:ajvanega

	first_attempt
					2015-10-23 16:57:29
	part1_incorrect_attempt
					('0:00:00', u'1/8')
	part1_correct_attempt
					['0:03:23', u'(1+2+3+4+5+6+7+8)/8']

45 Student ID:jguanzho

	first_attempt
					2015-10-23 03:23:36
	part1_incorrect_attempt
					('0:00:00', u'1*(1*9)')
	part1_correct_attempt
					['0:07:30', u'(1/9)*(1+2+3+4+5+6+7+8+9)']

46 Student ID:hmnaing

	first_attempt
					2015-10-30 07:46:41
	part1_incorrect_attempt
					('0:00:00', u'1/8')
	part1_correct_attempt
					['0:01:41', u'36/8']

47 Student ID:akg009

	first_attempt
					2015-10-30 20:43:13
	part1_incorrect_attempt
					('0:00:00', u'1/8')
					('0:05:53', u'1/8')
					('0:00:00', u'3.5')
	part1_correct_attempt
					['1:00:40', u'4.5']

48 Student ID:muy002

	first_attempt
					2015-10-29 10:52:02
	part1_incorrect_attempt
					('0:00:00', u'1/10')
	part1_correct_attempt
					['0:24:46', u'55/10']

49 Student ID:msaguiar

	first_attempt
					2015-10-29 06:43:09
	part1_incorrect_attempt
					('0:00:00', u'1+2+3+4+5+6+7+8+9+10')
	part1_correct_attempt
					['0:00:22', u'(1+2+3+4+5+6+7+8+9+10)/10']

50 Student ID:j2phung

	first_attempt
					2015-10-29 00:28:16
	part1_incorrect_attempt
					('0:00:00', u'1/6')
					('0:00:58', u'(1/6)+(1/6)+(1/6)+(1/6)+(1/6)+(1/6)')
	part1_correct_attempt
					['0:04:06', u'1(1/6)+2(1/6)+3(1/6)+4(1/6)+5(1/6)+6(1/6)']












## Part 2

### (97) Mistake Group Digits of size 97




### (6) Mistake Group ['R.0'] of size 6
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|2*9/(9+1)+9*(9-1)/[2*(9+1)]	|2/10*9+36/10*8	|[('R.0', 1.8, u'2*9/(9+1)', u'2/10*9')]	|
|1	|2*7/(7+1)+7*(7-1)/[2*(7+1)]	|21/12 + 7/2	|[('R.0', 1.75, u'2*7/(7+1)', u'21/12')]	|
|2	|2*10/(10+1)+10*(10-1)/[2*(10+1)]	|2/11*10+36/11	|[('R.0', 1.8181818181818181, u'2*10/(10+1)', u'2/11*10')]	|
|3	|2*10/(10+1)+10*(10-1)/[2*(10+1)]	|2/11*10+36/10	|[('R.0', 1.8181818181818181, u'2*10/(10+1)', u'2/11*10')]	|
|4	|2*10/(10+1)+10*(10-1)/[2*(10+1)]	|2/11*10+4	|[('R.0', 1.8181818181818181, u'2*10/(10+1)', u'2/11*10')]	|




### (4) Mistake Group ['R.1.0.1'] of size 4
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|2*6/(6+1)+6*(6-1)/[2*(6+1)]	|6(1/2) + (1+2+3+4+5)/10	|[('R.1.0.1', 5.0, u'6-1', u'5')]	|
|1	|2*10/(10+1)+10*(10-1)/[2*(10+1)]	|( (1/5)*10) + (1/9) * (9+8+7+6+5+4+3+2+1)	|[('R.1.0.1', 9.0, u'10-1', u'9')]	|
|2	|2*6/(6+1)+6*(6-1)/[2*(6+1)]	|1/6(1+2+3+4+5+12)	|[('R.1.0.1', 5.0, u'6-1', u'5')]	|
|3	|2*7/(7+1)+7*(7-1)/[2*(7+1)]	|1/7(1 + 2 + 3 + 4 + 5 + 6 + 7)	|[('R.1.0.1', 6.0, u'7-1', u'6')]	|




### (3) Mistake Group ['R.1.0.1', 'R.1.1.0'] of size 3
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.0.1', 'R.1.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|2*9/(9+1)+9*(9-1)/[2*(9+1)]	|1/9(1+2+3+4+5+6+7+8+2*9)	|[('R.1.0.1', 8.0, u'9-1', u'8'), ('R.1.1.0', 2.0, u'2', u'2')]	|
|1	|2*10/(10+1)+10*(10-1)/[2*(10+1)]	|1/10(1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 2 * 10)	|[('R.1.0.1', 9.0, u'10-1', u'9'), ('R.1.1.0', 2.0, u'2', u'2')]	|
|2	|2*10/(10+1)+10*(10-1)/[2*(10+1)]	|1/20(1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 2 * 10)	|[('R.1.0.1', 9.0, u'10-1', u'9'), ('R.1.1.0', 2.0, u'2', u'2')]	|




### (2) Mistake Group ['R.1.1.0'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|2*9/(9+1)+9*(9-1)/[2*(9+1)]	|1/8(1+2+3+4+5+6+7+8+2*9)	|[('R.1.1.0', 2.0, u'2', u'2')]	|
|1	|2*9/(9+1)+9*(9-1)/[2*(9+1)]	|(1+2+3+4+5+6+7+8)*(1/8) + 9*(2/8)	|[('R.1.1.0', 2.0, u'2', u'2')]	|




### (1) Mistake Group ['R.1.0'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|2*6/(6+1)+6*(6-1)/[2*(6+1)]	|(6/7)+(6*5/7)	|[('R.1.0', 30.0, u'6*(6-1)', u'6*5')]	|




### (1) Mistake Group ['R.0.0'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|2*7/(7+1)+7*(7-1)/[2*(7+1)]	|[(2*7) + (6*7)]/[2*8]	|[('R.0.0', 14.0, u'2*7', u'2*7')]	|




### (1) Mistake Group ['R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|2*10/(10+1)+10*(10-1)/[2*(10+1)]	|2/11+45/11	|[('R.1', 4.090909090909091, u'10*(10-1)/[2*(10+1)]', u'45/11')]	|




### (1) Mistake Group ['R.0', 'R.1.0.1', 'R.1.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1.0.1', 'R.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|2*6/(6+1)+6*(6-1)/[2*(6+1)]	|2*6/7 + ((2*5)/(2*7))	|[('R.0', 1.7142857142857142, u'2*6/(6+1)', u'2*6/7'), ('R.1.0.1', 5.0, u'6-1', u'5'), ('R.1.1', 14.0, u'2*(6+1)', u'2*7')]	|




### (1) Mistake Group ['R.0', 'R.1.0.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|2*6/(6+1)+6*(6-1)/[2*(6+1)]	|6*2/7+15*5/7	|[('R.0', 1.7142857142857142, u'2*6/(6+1)', u'6*2/7'), ('R.1.0.1', 5.0, u'6-1', u'5')]	|




### (1) Mistake Group ['R.0', 'R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|2*9/(9+1)+9*(9-1)/[2*(9+1)]	|((2*9)/(9+1)) *((9*(9-1))/(2*(9+1)))	|[('R.0', 1.8, u'2*9/(9+1)', u'(2*9)/(9+1)'), ('R.1', 3.6, u'9*(9-1)/[2*(9+1)]', u'(9*(9-1))/(2*(9+1))')]	|




### (110) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:gthorn

	first_attempt
					2015-10-26 22:32:47
	part2_incorrect_attempt
					('0:00:33', u'1/10 + 2/10 + 3/10 + 4/10  + 5/10 + 6/10 + 7/10 + 8/10 + 9/10 + 20/10')
					('0:19:05', u'1/9 + 2/9 + 3/9 + 4/9 + 5/9 + 6/9 + 7/9 + 8/9 + 9/9 + 20/9')
	part2_correct_attempt
					['0:21:52', u'1/11 + 2/11 + 3/11 + 4/11 + 5/11 + 6/11 + 7/11 + 8/11 + 9/11 + 20/11']

1 Student ID:v4zhang

	first_attempt
					2015-10-30 08:40:53
	part2_incorrect_attempt
					('-1 day, 23:54:40', u'1/9+2/9')
					('0:00:54', u'4+(9/5)')
	part2_correct_attempt
					['0:02:01', u'[(1+2+3+4+5+6+7+8)*(1/10)]+(9*(1/5))']

2 Student ID:kvass

	first_attempt
					2015-10-26 17:01:33
	part2_incorrect_attempt
					('0:00:00', u'7/2+3')
					('0:07:14', u'30/12+2')
					('0:09:12', u'5/2+6/3')
					('1:48:25', u'6+(3/7)')
	part2_correct_attempt
					['1:49:18', u'2*6/(6+1) + (6*(6-1))/(2*(6+1))']

3 Student ID:kbielawi

	first_attempt
					2015-10-26 21:39:28
	part2_incorrect_attempt
					('0:00:41', u'(1+2+3+4+5+6+7+8+18)/9')
	part2_correct_attempt
					['1 day, 3:17:00', u'(1+2+3+4+5+6+7+8+18)/10']

4 Student ID:srl006

	first_attempt
					2015-10-30 00:11:56
	part2_incorrect_attempt
					('0:00:17', u'6.5')
					('0:00:26', u'15.5')
					('0:02:50', u'7.5')
					('0:02:54', u'8.5')
					('0:02:59', u'9.5')
					('0:06:32', u'5.99')
					('0:08:39', u'5.996')
					('0:09:54', u'5.9')
	part2_correct_attempt
					['0:10:06', u'5.909090909']

5 Student ID:ssamudra

	first_attempt
					2015-10-30 21:39:15
	part2_incorrect_attempt
					('-1 day, 23:56:34', u'2/9')
	part2_correct_attempt
					['0:01:18', u'8(2/9) + 7(1/9) + 6(1/9)+ 5(1/9) + 4(1/9) + 3(1/9)+ 2(1/9) + 1/9']

6 Student ID:jjm019

	first_attempt
					2015-10-30 07:57:45
	part2_incorrect_attempt
					('-1 day, 23:42:41', u'[(2*2*7) + (6*7)]/[2*8]')
					('-1 day, 23:47:31', u'[(2*2*8) + (7*8)]/[2*8]')
					('0:00:00', u'[(2*2*8) + (8*8)]/[2*8]')
					('0:00:15', u'[(2*2*8) + (8*9)]/[2*8]')
					('0:01:53', u'[(2*2*8) + (7*8)]/[2*8]')
					('0:15:56', u'[(2*2*8) + (6*7)]/[2*8]')
					('0:16:05', u'[(2*2*8) + (8*9)]/[2*8]')
					('0:17:08', u'[(2*8) + (7*8)]/[2*8]')
					('0:17:18', u'[(2*2*8) + (7*8)]/[2*8]')
	part2_correct_attempt
					['11:00:35', u'[(2*2*8) + (7*8)]/[2*9]']

7 Student ID:mhale

	first_attempt
					2015-10-28 22:56:38
	part2_incorrect_attempt
					('0:00:26', u'2.5 + 2')
					('0:01:14', u'1/6 + 2/6 + 3/6 + 4/6 + 5/6 + 2')
	part2_correct_attempt
					['0:02:03', u'1/7 + 2/7 + 3/7 + 4/7 + 5/7 + 6/3.5']

8 Student ID:ctgraves

	first_attempt
					2015-10-27 03:37:52
	part2_incorrect_attempt
					('0:00:27', u'27/2')
					('0:00:34', u'27/6')
	part2_correct_attempt
					['0:01:29', u'(1+2+3+4+5)*1/7+6*2/7']

9 Student ID:dkurli

	first_attempt
					2015-10-29 21:58:49
	part2_incorrect_attempt
					('0:01:28', u'1/5*10+4/5*(45)')
					('0:01:50', u'1/5*10+4/5*(45/9)')
					('0:02:08', u'1/5*10+4/5*(45/10)')
					('0:04:39', u'1/5+(4/35*45)')
					('0:04:49', u'10*1/5+(4/35*45)')
	part2_correct_attempt
					['0:08:33', u'2/11*10+45/11']

10 Student ID:nhn018

	first_attempt
					2015-10-29 04:06:43
	part2_incorrect_attempt
					('0:00:00', u'6.125')
					('0:00:58', u'49/8')
					('0:51:38', u'49/7')
					('0:52:50', u'49/8')
	part2_correct_attempt
					['1:09:47', u'(1+2+3+4+5+6+14)/8']

11 Student ID:j5phung

	first_attempt
					2015-10-27 15:18:59
	part2_incorrect_attempt
					('-2 days, 10:19:45', u'1/9')
					('0:00:00', u'1/8 + 2/8 + 3/8 + 4/8 + 5/8 + 6/8 + 7/8 + 16/8')
					('0:10:24', u'1/8 + 2/8')
	part2_correct_attempt
					['0:15:35', u'1/9 + 2/9 + 3/9 + 4/9 + 5/9 + 6/9 + 7/9 + 16/9']

12 Student ID:jyc018

	first_attempt
					2015-10-28 00:44:32
	part2_incorrect_attempt
					('0:01:29', u'4.5+0.5*(4)')
					('0:02:29', u'4.5+0.5*(4/9)')
					('0:03:40', u'4.5+0.5*(40/9)')
					('0:04:12', u'4.5+0.5*(36/9)')
	part2_correct_attempt
					['0:09:33', u'2/10*9+36/10']

13 Student ID:kquong

	first_attempt
					2015-10-28 17:25:48
	part2_incorrect_attempt
					('0:00:00', u'(1 + 2 + 3 + 4 + 5 + 6 + 7 +8+9+10 + 10)/10')
	part2_correct_attempt
					['0:00:12', u'(1 + 2 + 3 + 4 + 5 + 6 + 7 +8+9+10 + 10)/11']

14 Student ID:rlhagen

	first_attempt
					2015-10-25 17:48:54
	part2_incorrect_attempt
					('-1 day, 23:58:42', u'9.5')
	part2_correct_attempt
					['0:06:33', u'(1/8)*1+(1/8)*2+(1/8)*3+(1/8)*4+(1/8)*5+(1/8)*6+(1/4)*7']

15 Student ID:mpanelo

	first_attempt
					2015-10-28 19:03:53
	part2_incorrect_attempt
					('-1 day, 23:59:36', u'5.5')
	part2_correct_attempt
					['4:36:07', u'44/9']

16 Student ID:tcn013

	first_attempt
					2015-10-27 00:23:48
	part2_incorrect_attempt
					('0:00:22', u'(1+2+3+4+5+6+7+16)/8')
					('0:01:32', u'(1+2+3+4+5+6+7+16)/7')
	part2_correct_attempt
					['0:03:19', u'(1+2+3+4+5+6+7+16)/9']

17 Student ID:tcuddy

	first_attempt
					2015-10-23 23:57:16
	part2_incorrect_attempt
					('0:00:00', u'(4/5)(8*9/2)(1/5)(9)')
					('0:30:03', u'(8/10)(8*9/2)(2/10)(9)')
					('0:30:38', u'(8/10)(36)')
	part2_correct_attempt
					['0:31:10', u'(1/10)(36)+(2/10)9']

18 Student ID:djk006

	first_attempt
					2015-10-27 02:42:45
	part2_incorrect_attempt
					('0:00:51', u'(18+8+7+6+5+4+3+2+1)/2')
					('0:01:01', u'(18+8+7+6+5+4+3+2+1)/9')
	part2_correct_attempt
					['0:03:11', u'(18+8+7+6+5+4+3+2+1)/10']

19 Student ID:dando

	first_attempt
					2015-10-29 00:45:03
	part2_incorrect_attempt
					('0:00:00', u'120/11')
	part2_correct_attempt
					['0:18:21', u'1/11 + 2/11 + 3/11 + 4 /11 + 5/11 + 6/11 + 7/11 + 8/11 + 9/11 + 20/11']

20 Student ID:sayao

	first_attempt
					2015-10-28 22:36:02
	part2_incorrect_attempt
					('0:00:11', u'7.5')
	part2_correct_attempt
					['0:09:03', u'(1+2+3+4+5+6+7+8)/10 + 9/5']

21 Student ID:anvan

	first_attempt
					2015-10-30 10:44:21
	part2_incorrect_attempt
					('5:15:41', u'6.75')
	part2_correct_attempt
					['7:55:46', u'1/10(1+2+3+4+5+6+7+8) + (1/5)(9)']

22 Student ID:acvuong

	first_attempt
					2015-10-26 23:30:12
	part2_incorrect_attempt
					('0:00:00', u'28/8')
	part2_correct_attempt
					['0:01:12', u'35/8']

23 Student ID:flhernan

	first_attempt
					2015-10-26 04:31:48
	part2_incorrect_attempt
					('0:00:20', u'4.5')
	part2_correct_attempt
					['0:04:55', u'3.85714286']

24 Student ID:starinia

	first_attempt
					2015-10-30 22:10:09
	part2_incorrect_attempt
					('0:00:00', u'27/6')
	part2_correct_attempt
					['0:04:54', u'12/7 + 30/14']

25 Student ID:tak068

	first_attempt
					2015-10-29 20:06:04
	part2_incorrect_attempt
					('0:00:16', u'9*(9+1)/(2*9)')
	part2_correct_attempt
					['0:00:36', u'2*9/(9+1)+(9*(9-1))/(2*(9+1))']

26 Student ID:jguanzho

	first_attempt
					2015-10-23 03:31:06
	part2_incorrect_attempt
					('-1 day, 23:52:30', u'1*(1/10)')
					('-1 day, 23:53:37', u'10/9')
					('0:00:00', u'(1/9)*(1+2+3+4+5+6+7+8)+9*(2/9)')
	part2_correct_attempt
					['0:00:29', u'(1/10)*(1+2+3+4+5+6+7+8+9+9)']

27 Student ID:small

	first_attempt
					2015-10-30 23:02:37
	part2_incorrect_attempt
					('0:00:49', u'(1/20)(9)(10) + 2')
					('0:02:50', u'9/2 + 2')
	part2_correct_attempt
					['0:04:57', u'(1/11)(90/2) + 2/11(10)']

28 Student ID:akg009

	first_attempt
					2015-10-30 21:43:53
	part2_incorrect_attempt
					('-1 day, 23:05:13', u'1/2')
					('0:00:00', u'4.625')
					('0:00:47', u'5.5')
					('0:48:56', u'98/9')
	part2_correct_attempt
					['0:49:19', u'44/9']

29 Student ID:ctroncos

	first_attempt
					2015-10-29 16:00:12
	part2_incorrect_attempt
					('0:00:50', u'(9*(9-1))/(2*(9+1))')
					('0:00:59', u'(9*(9-0.6))/(2*(9+1))')
	part2_correct_attempt
					['0:01:40', u'(2*9/(9+1) + (9*(9-1))/(2*(9+1)))']

30 Student ID:b3hwang

	first_attempt
					2015-10-26 04:31:18
	part2_incorrect_attempt
					('0:01:43', u'(1*1/11) +(10*2/11) +(9*1/1) +(8*1/11) +(7*1/11) +(6*1/11) +(5*1/11) +(4*1/11) +(3*1/11) +(2*1/11)')
	part2_correct_attempt
					['0:02:06', u'(1*1/11) +(10*2/11) +(9*1/11) +(8*1/11) +(7*1/11) +(6*1/11) +(5*1/11) +(4*1/11) +(3*1/11) +(2*1/11)']

31 Student ID:jag028

	first_attempt
					2015-10-29 19:19:25
	part2_incorrect_attempt
					('20:01:23', u'8(1/10)+(2/10)')
					('20:01:48', u'8(1/9)+(2/9)')
					('20:01:58', u'8(1/10)+(2/9)')
					('20:02:05', u'8(1/10)+(2/10)')
					('22:59:45', u'8*(1/10)+(1/5)')
					('22:59:57', u'8*(1/5)+(1/9)')
	part2_correct_attempt
					['23:06:04', u'(1/10)+2(1/10)+3(1/10)+4(1/10)+5(1/10)+6(1/10)+7(1/10)+8(1/10)+9(1/5)']

32 Student ID:asetters

	first_attempt
					2015-10-27 05:28:42
	part2_incorrect_attempt
					('-1 day, 23:55:59', u'5.5')
					('0:02:45', u'(1/8) *((7*8)/2) + 2')
	part2_correct_attempt
					['0:04:10', u'(1/9) *((7*8)/2) + (2/9)*8']

33 Student ID:c1sorian

	first_attempt
					2015-10-28 21:41:37
	part2_incorrect_attempt
					('0:00:45', u'(1+2+3+4+5+6+14)/7')
	part2_correct_attempt
					['0:02:43', u'((1/8)(1+2+3+4+5+6)+(.25*7))']

34 Student ID:abjara

	first_attempt
					2015-10-27 07:45:13
	part2_incorrect_attempt
					('-1 day, 23:57:37', u'((1/9)*8) + 2/9')
					('0:00:00', u'((1/9)+2*(1/9)+3*(1/9)+4*(1/9)+5*(1/9)+6*(1/9)+7*(1/9)+8*(1/9)) + 2/9')
					('0:00:15', u'((1/9)+2*(1/9)+3*(1/9)+4*(1/9)+5*(1/9)+6*(1/9)+7*(1/9)+8*(1/9)) + 9*(2/9)')
					('0:00:36', u'(1/9)+2*(1/9)+3*(1/9)+4*(1/9)+5*(1/9)+6*(1/9)+7*(1/9)+8*(1/9) + 9*(2/9)')
					('0:04:56', u'(1/9)+2*(1/9)+3*(1/9)+4*(1/9)+5*(1/9)+6*(1/9)+7*(1/9)+8*(1/9) + 9*((1/9)+2*(1/9)+3*(1/9)+4*(1/9)+5*(1/9)+6*(1/9)+7*(1/9)+8*(1/9))')
					('0:05:20', u'(1/9)+2*(1/9)+3*(1/9)+4*(1/9)+5*(1/9)+6*(1/9)+7*(1/9)+8*(1/9) + 2*((1/9)+2*(1/9)+3*(1/9)+4*(1/9)+5*(1/9)+6*(1/9)+7*(1/9)+8*(1/9))')
					('0:05:38', u'(1/9)+2*(1/9)+3*(1/9)+4*(1/9)+5*(1/9)+6*(1/9)+7*(1/9)+8*(1/9) + 2*((1/9)+2*(1/9)+3*(1/9)+4*(1/9)+5*(1/9)+6*(1/9)+7*(1/9)+8*(1/9)+9*(1/9))')
					('0:13:22', u'(1/9)+2*(1/9)+3*(1/9)+4*(1/9)+5*(1/9)+6*(1/9)+7*(1/9)+8*(1/9)+9*(2/9)')
					('0:13:37', u'(2/9)+2*(1/9)+3*(1/9)+4*(1/9)+5*(1/9)+6*(1/9)+7*(1/9)+8*(1/9)+9*(1/9)')
					('0:17:55', u'(1/9)+2*(1/9)+3*(1/9)+4*(1/9)+5*(1/9)+6*(1/9)+7*(1/9)+8*(1/9)+9*(2/9)')
	part2_correct_attempt
					['0:20:32', u'(1/10)+2*(1/10)+3*(1/10)+4*(1/10)+5*(1/10)+6*(1/10)+7*(1/10)+8*(1/10)+9*(1/5)']

35 Student ID:asp025

	first_attempt
					2015-10-30 03:34:38
	part2_incorrect_attempt
					('0:02:16', u'6.125')
	part2_correct_attempt
					['0:03:46', u'35/8']

36 Student ID:krau

	first_attempt
					2015-10-29 21:59:04
	part2_incorrect_attempt
					('0:01:28', u'6*2/6+5/6+4/6+3/6+2/6+1/6')
					('0:03:27', u'6*2/6+5*2/15+4*2/15+3*2/15+2*2/15+1*2/15')
	part2_correct_attempt
					['0:08:39', u'6*2/7+15*1/7']

37 Student ID:mroknich

	first_attempt
					2015-10-26 03:19:46
	part2_incorrect_attempt
					('0:02:10', u'1/10+2/10+3/10+4/10+5/10+6/10+7/10+8/10+9/10+2')
					('0:13:57', u'1/3+2/3+4/3+5/3+6/3+7/3+8/3+9/3+20/3')
					('0:23:49', u'1/10+2/10+3/10+4/10+5/10+6/10+7/10+8/10+9/10+2')
					('0:59:01', u'7.2')
	part2_correct_attempt
					['1:50:19', u'65/11']

38 Student ID:psable

	first_attempt
					2015-10-30 05:58:12
	part2_incorrect_attempt
					('0:05:45', u'5.2')
					('0:05:49', u'5.3')
					('0:05:54', u'5.25')
					('0:07:58', u'5.85')
					('0:08:04', u'5.86')
					('0:08:57', u'5.92')
					('0:09:31', u'5.9')
	part2_correct_attempt
					['0:15:51', u'65/11']

39 Student ID:tpmach

	first_attempt
					2015-10-28 06:18:03
	part2_incorrect_attempt
					('0:01:01', u'1*1/6+2*1/6+3*1/6+4*1/6+5*1/6+6*2/6')
					('0:03:22', u'1*1/15+2*1/15+3*1/15+4*1/15+5*1/15+6*2/6')
					('0:07:23', u'1/3(1+2+3+4+5)+6*2/3')
	part2_correct_attempt
					['0:07:56', u'1/7(1+2+3+4+5)+6*2/7']

40 Student ID:hak014

	first_attempt
					2015-10-27 18:11:54
	part2_incorrect_attempt
					('0:00:24', u'(1+2+3+4+5+6+7+8+9+20)/10')
	part2_correct_attempt
					['0:00:47', u'(1+2+3+4+5+6+7+8+9+20)/11']

41 Student ID:dwzhang

	first_attempt
					2015-10-29 21:25:57
	part2_incorrect_attempt
					('0:00:05', u'1/6 + 2/6 + 3/6 + 4/6 + 5/6 + 12/6')
	part2_correct_attempt
					['0:01:41', u'1/7 + 2/7 + 3/7 + 4/7 + 5/7 + 12/7']

42 Student ID:jhw015

	first_attempt
					2015-10-27 23:45:45
	part2_incorrect_attempt
					('0:00:31', u'54/9')
					('0:05:01', u'54/8')
	part2_correct_attempt
					['0:05:09', u'54/10']

43 Student ID:akalathi

	first_attempt
					2015-10-29 06:45:09
	part2_incorrect_attempt
					('0:01:47', u'4.5')
					('0:09:50', u'6.125')
	part2_correct_attempt
					['0:13:28', u'4.375']

44 Student ID:jel075

	first_attempt
					2015-10-30 06:31:57
	part2_incorrect_attempt
					('-1 day, 23:55:46', u'2/10*10+36/10')
					('0:02:40', u'2/10*10+36/10')
					('0:02:52', u'5.9')
					('0:03:01', u'6.1')
					('0:03:08', u'5.8')
					('0:03:11', u'5.7')
					('0:16:33', u'6.5')
					('0:25:38', u'90/22+20/4')
	part2_correct_attempt
					['0:30:17', u'10/11+10/11+1/11+2/11+3/11+4/11+5/11+6/11+7/11+8/11+9/11']

45 Student ID:hmnaing

	first_attempt
					2015-10-30 07:48:22
	part2_incorrect_attempt
					('0:10:22', u'28+16/9')
	part2_correct_attempt
					['0:10:30', u'(28+16)/9']

46 Student ID:edescobe

	first_attempt
					2015-10-28 19:47:31
	part2_incorrect_attempt
					('0:00:00', u'5.9')
	part2_correct_attempt
					['0:02:37', u'5.909']

47 Student ID:ggaddi

	first_attempt
					2015-10-27 17:00:21
	part2_incorrect_attempt
					('0:00:00', u'(1+2+3+4+5+6+7+8+9)/[(1-1/5)/9] + 10*2/10')
	part2_correct_attempt
					['0:35:11', u'(1+2+3+4+5+6+7+8+9)/11+10*2/11']

48 Student ID:muy002

	first_attempt
					2015-10-29 11:16:48
	part2_incorrect_attempt
					('0:00:52', u'65/10')
					('0:04:14', u'55/10')
					('0:10:10', u'60/10')
					('0:10:16', u'65/10')
					('0:32:28', u'45/11+10/5')
	part2_correct_attempt
					['0:33:18', u'45/11+20/11']

49 Student ID:eshung

	first_attempt
					2015-10-30 22:39:45
	part2_incorrect_attempt
					('0:00:00', u'29/7')
	part2_correct_attempt
					['0:03:10', u'27/7']

50 Student ID:v4sharma

	first_attempt
					2015-10-25 00:52:03
	part2_incorrect_attempt
					('0:00:49', u'((1/7)(1+2+3+4+5+6)) + ((2/7)(7))')
					('4 days, 0:33:11', u'((1/8)(1+2+3+4+5+6)) + ((7/4)(7))')
	part2_correct_attempt
					['4 days, 0:33:45', u'((1/8)(1+2+3+4+5+6)) + ((1/4)(7))']

51 Student ID:ralhadda

	first_attempt
					2015-10-24 02:23:35
	part2_incorrect_attempt
					('0:43:33', u'5.11')
					('0:43:43', u'5.111')
					('1:09:53', u'5.5')
					('1:10:58', u'5.25')
					('1:20:38', u'8.1')
					('1:22:42', u'10.35')
					('1:27:52', u'8.1')

52 Student ID:dcastlem

	first_attempt
					2015-10-30 19:36:50
	part2_incorrect_attempt
					('-2 days, 23:19:47', u'1/4')
	part2_correct_attempt
					['0:00:00', u'44/9']

53 Student ID:hsc052

	first_attempt
					2015-10-30 21:33:50
	part2_incorrect_attempt
					('0:00:00', u'(36/9)+(9/10)')
	part2_correct_attempt
					['0:06:50', u'(54/10)']

54 Student ID:xil109

	first_attempt
					2015-10-26 20:29:35
	part2_incorrect_attempt
					('0:00:52', u'4.5')
					('0:02:18', u'5.14')
	part2_correct_attempt
					['0:02:46', u'3.86']

55 Student ID:v3doan

	first_attempt
					2015-10-27 02:02:00
	part2_incorrect_attempt
					('0:00:31', u'56 / 7')
	part2_correct_attempt
					['0:01:16', u'7 / 4 + 42 / 2 / 8']

56 Student ID:yil035

	first_attempt
					2015-10-27 22:23:27
	part2_incorrect_attempt
					('0:02:50', u'5.5')
	part2_correct_attempt
					['0:06:54', u'5.4']

57 Student ID:k3tan

	first_attempt
					2015-10-30 01:42:09
	part2_incorrect_attempt
					('4:23:40', u'56/11')
	part2_correct_attempt
					['4:24:15', u'65/11']

58 Student ID:h4tu

	first_attempt
					2015-10-28 01:55:23
	part2_incorrect_attempt
					('0:00:17', u'36/9')
					('0:00:35', u'44/8')
	part2_correct_attempt
					['0:00:47', u'44/9']

59 Student ID:lywong

	first_attempt
					2015-10-28 08:26:30
	part2_incorrect_attempt
					('0:00:15', u'6.5')
					('0:01:14', u'5.9')
	part2_correct_attempt
					['0:01:54', u'65/11']

60 Student ID:hkhodada

	first_attempt
					2015-10-28 00:46:44
	part2_incorrect_attempt
					('-5 days, 18:32:56', u'1/9')
					('-1 day, 21:18:48', u'1/8')
	part2_correct_attempt
					['0:00:00', u'44/9']

61 Student ID:nisharma

	first_attempt
					2015-10-30 16:25:46
	part2_incorrect_attempt
					('0:02:11', u'((1/8)(1+2+3+4+5+6+7+8+9+10)) + ((1/4)(10))')
					('0:02:22', u'((1/8)(1+2+3+4+5+6+7+8+9)) + ((1/4)(10))')
					('0:03:08', u'((1/10)(1+2+3+4+5+6+7+8+9)) + ((1/4)(10))')
					('0:05:04', u'((1/11)(1+2+3+4+5+6+7+8+9)) + ((1/4)(10))')
					('1:06:49', u'((1/11)(1+2+3+4+5+6+7+8+9+10)) + ((2/11)(10))')
	part2_correct_attempt
					['1:09:36', u'((1/11)(1+2+3+4+5+6+7+8+9)) + ((2/11)(10))']

62 Student ID:achava

	first_attempt
					2015-10-28 08:00:13
	part2_incorrect_attempt
					('0:01:00', u'6.125')
					('0:26:48', u'(7*8)/(2*9) + (16/4)')
					('0:27:28', u'(7*8)/(2*7) + (16/4)')
					('1:06:43', u'35/8')
					('1:06:49', u'35/9')
	part2_correct_attempt
					['1:07:19', u' (1+2+3+4+5+6+7+[2]8) / 9']

63 Student ID:thk002

	first_attempt
					2015-10-28 04:13:07
	part2_incorrect_attempt
					('0:03:22', u'6.125')
	part2_correct_attempt
					['0:05:45', u'35/8']

64 Student ID:awollner

	first_attempt
					2015-10-27 03:27:11
	part2_incorrect_attempt
					('0:01:08', u'.1(1+2+3+4+5+6+7+8+9) +2')
	part2_correct_attempt
					['0:02:19', u'1/11(1+2+3+4+5+6+7+8+9) +2/11(10)']

65 Student ID:dcrume

	first_attempt
					2015-10-28 19:54:57
	part2_incorrect_attempt
					('0:01:36', u'1/6 + 2/6 + 3/6 +4/6 + 5/6 + 12/6')
					('0:02:30', u'1/6 + 2/6 + 3/6 +4/6 + 5/6 + 6/12')
					('0:02:55', u'1/6 + 2/6 + 3/6 +4/6 + 5/6 + 6/3')
	part2_correct_attempt
					['1 day, 21:09:27', u'(5*6/2)*(1/7) + 6*(2/7)']

66 Student ID:t2li

	first_attempt
					2015-10-30 22:54:58
	part2_incorrect_attempt
					('0:02:02', u'((1+2+3+4+5)/6) + 2')
					('0:02:20', u'((1+2+3+4+5)/5) + 2')
	part2_correct_attempt
					['0:02:59', u'12/7 + 30/14']

67 Student ID:jfalcone

	first_attempt
					2015-10-29 04:09:17
	part2_incorrect_attempt
					('0:00:22', u'(1+2+3+4+5+6+7+8+18)/9')
					('0:05:07', u'(8*9)/(2*10)')
	part2_correct_attempt
					['0:48:11', u'(1+2+3+4+5+6+7+8+18)/10']

68 Student ID:n2patil

	first_attempt
					2015-10-28 23:04:39
	part2_incorrect_attempt
					('16:28:45', u'93/7')
					('16:30:00', u'75/7')
	part2_correct_attempt
					['16:30:46', u'27/7']

69 Student ID:ttimmons

	first_attempt
					2015-10-27 04:55:02
	part2_incorrect_attempt
					('0:00:00', u'(1/10)*(1+2+3+4+5+6+7+8+9) + 10*(2/10)')
	part2_correct_attempt
					['11:39:34', u'(1/11)*(1+2+3+4+5+6+7+8+9)+(2/11)*(10)']

70 Student ID:jblynch

	first_attempt
					2015-10-28 18:34:32
	part2_incorrect_attempt
					('0:00:00', u'(1+2+3+4+5+6+7+8)/9+(18/9)')
					('0:00:49', u'(1+2+3+4+5+6+7+8)/9+(9*(2/9))')
					('0:04:46', u'(1+2+3+4+5+6+7+8)/9+(9*(6/9))')
					('0:08:26', u'(1+2+3+4+5+6+7+8)*((3/9)/8) + 9*(6/9)')
					('0:09:00', u'(1+2+3+4+5+6+7+8)*((7/9)/8) + 9*(2/9)')
					('0:09:59', u'(1+2+3+4+5+6+7+8)*(1/9) + 9*(2/9)')
	part2_correct_attempt
					['0:13:15', u'(1+2+3+4+5+6+7+8)*(1/10) + 9*(2/10)']

71 Student ID:nnh002

	first_attempt
					2015-10-30 00:23:03
	part2_incorrect_attempt
					('0:03:00', u'44/8')
					('0:13:26', u'72/9')
					('0:21:17', u'22/8')
	part2_correct_attempt
					['0:29:35', u'44/9']

72 Student ID:akhmelni

	first_attempt
					2015-10-29 00:08:10
	part2_incorrect_attempt
					('0:00:06', u'5.5')
	part2_correct_attempt
					['0:03:40', u'4.375']

73 Student ID:tol003

	first_attempt
					2015-10-28 01:02:12
	part2_incorrect_attempt
					('-1 day, 23:52:22', u'1/4')
					('0:00:00', u'1.75')
	part2_correct_attempt
					['0:05:39', u'21/8+7/4']

74 Student ID:skodigal

	first_attempt
					2015-10-28 03:37:23
	part2_incorrect_attempt
					('0:13:17', u'6/5')
	part2_correct_attempt
					['21:54:34', u'(1/10)(1+2+3+4+5+6+7+8) + (1/5)(9)']

75 Student ID:q3wen

	first_attempt
					2015-10-27 22:47:05
	part2_incorrect_attempt
					('0:00:00', u'6.5')
	part2_correct_attempt
					['0:03:52', u'65/11']

76 Student ID:arvenega

	first_attempt
					2015-10-29 17:13:10
	part2_incorrect_attempt
					('-1 day, 23:52:02', u'2*(1/7)')
					('0:00:24', u'1*(1/7) + 2*(1/7) + 3*(1/7) + 4*(1/7) + 5*(1/7) + 6*(1/7) + 7*(2/7)')
	part2_correct_attempt
					['0:08:52', u'1*(1/8) + 2*(1/8) + 3*(1/8) + 4*(1/8) + 5*(1/8) + 6*(1/8) + 7*(1/4)']

77 Student ID:ksrijong

	first_attempt
					2015-10-28 01:15:44
	part2_incorrect_attempt
					('0:02:19', u'10(2/10)+[(9)(10)/2]*(8/10)*(1/9)')
	part2_correct_attempt
					['0:05:11', u'10(2/11)+[90/2](1/11)']

78 Student ID:volim

	first_attempt
					2015-10-28 05:35:30
	part2_incorrect_attempt
					('-3 days, 19:01:25', u'1/18')
					('0:00:18', u'(1+2+3+4+5+6+7+8+18)/9')
	part2_correct_attempt
					['0:00:49', u'(1+2+3+4+5+6+7+8+9+9)/10']

79 Student ID:atorr

	first_attempt
					2015-10-29 06:38:19
	part2_incorrect_attempt
					('0:00:30', u'(1+2+3+4+5+6+7)*(1/8) + 1')
					('0:00:44', u'(1+2+3+4+5+6+7)*(1/8) + 2')
					('0:01:08', u'(1+2+3+4+5+6+7)*(1/8) + 8*(1/4)')
					('0:01:53', u'((1+2+3+4+5+6+7) * (1/8)) + (8 * ((1/4)*2))')
					('0:02:04', u'((1+2+3+4+5+6+7) * (1/8)) + (8 * ((1/8)*2))')
					('0:02:32', u'(1+2+3+4+5+6+7)*(1/8)')
					('0:02:41', u'(1+2+3+4+5+6+7+8)*(1/8)')
					('0:03:46', u'(1/8)+(2/8)+(3/8)+(4/8)+(5/8)+(6/8)+(7/8)+(16/8)')
	part2_correct_attempt
					['0:05:16', u'(1+2+3+4+5+6+7)*(1/9) + (16/9)']

80 Student ID:ytc012

	first_attempt
					2015-10-29 11:34:57
	part2_incorrect_attempt
					('0:01:01', u'(7+6+5+4+3+2+1)/8*8/2')
					('0:01:44', u'(7+6+5+4+3+2+1)/8*2')
					('0:01:56', u'(7+6+5+4+3+2+1)/7*2')
					('0:02:34', u'(7+6+5+4+3+2+1)/9*16/9')
					('0:02:42', u'(7+6+5+4+3+2+1)/9*(16/9)')
					('0:03:24', u'(7+6+5+4+3+2+1)/9*(8/9)')
					('0:04:26', u'(16+7+6+5+4+3+2+1)/8')
	part2_correct_attempt
					['0:04:38', u'(16+7+6+5+4+3+2+1)/9']

81 Student ID:klala

	first_attempt
					2015-10-27 01:05:02
	part2_incorrect_attempt
					('0:01:40', u'.9 + 2*.9 + 3*.9 + 4* .9 + 5*.9 + 6*.9 + 7*.9 + 8*.9 + 1.8 * 9')
	part2_correct_attempt
					['0:03:00', u'.1 + .2 + .3 + .4 + .5 + .6 + .7 + .8 + 1.8']

82 Student ID:skarimik

	first_attempt
					2015-10-26 00:21:31
	part2_incorrect_attempt
					('0:00:00', u'2+(5/2)')
	part2_correct_attempt
					['0:04:50', u'35/8']

83 Student ID:galu

	first_attempt
					2015-10-30 23:59:16
	part2_incorrect_attempt
					('-1 day, 23:29:29', u'2/15')
					('-1 day, 23:59:02', u'1/8')
					('0:00:00', u'44/8')

84 Student ID:fichoi

	first_attempt
					2015-10-27 22:13:01
	part2_incorrect_attempt
					('0:00:00', u'265/56')
	part2_correct_attempt
					['0:01:55', u'35/8']

85 Student ID:r2fisher

	first_attempt
					2015-10-26 22:51:06
	part2_incorrect_attempt
					('0:01:04', u'8/2 + (7+6+5+4+3+2+1)/8')
					('0:01:19', u'8/2 + (7+6+5+4+3+2+1)/14')
	part2_correct_attempt
					['0:03:05', u'(8*2 +7+6+5+4+3+2+1)/9']

86 Student ID:agoldsht

	first_attempt
					2015-10-29 04:58:19
	part2_incorrect_attempt
					('0:00:29', u'(1+2+3+4+5+6+7+14)/7')
					('0:00:49', u'(1+2+3+4+5+6+14)/7')
	part2_correct_attempt
					['0:01:31', u'(1+2+3+4+5+6+14)/(7+1)']

87 Student ID:vsamant

	first_attempt
					2015-10-23 18:17:24
	part2_incorrect_attempt
					('0:02:22', u'13/2')
	part2_correct_attempt
					['0:03:16', u'65/11']

88 Student ID:ppanourg

	first_attempt
					2015-10-30 20:40:32
	part2_incorrect_attempt
					('0:00:16', u'3.5')
	part2_correct_attempt
					['0:04:42', u'(1/7)(1+2+3+4+5) + 6*(2/7)']

89 Student ID:rohan

	first_attempt
					2015-10-30 20:36:19
	part2_incorrect_attempt
					('-1 day, 23:54:31', u'2/7')
					('0:07:18', u'4.5')
					('0:12:42', u'4.5')
					('0:15:06', u'3.5')
					('0:15:12', u'4.5')
					('0:15:18', u'5.5')
					('0:15:23', u'7.5')
	part2_correct_attempt
					['0:20:59', u'4.375']

90 Student ID:any027

	first_attempt
					2015-10-26 04:09:44
	part2_incorrect_attempt
					('0:00:53', u'(1/10) * ( 10 + 10 + 9 + 8 + 7 + 6 + 5 +4 +3 +2 + 1 )')
					('0:04:09', u'( (1/5)*10) + (1/8) * (9+8+7+6+5+4+3+2+1)')
					('0:05:08', u'( (1/5)*10) + (1/10) * (9+8+7+6+5+4+3+2+1)')
					('0:05:30', u'( (1/5)*10) + (1/6) * (9+8+7+6+5+4+3+2+1)')
					('0:05:37', u'( (1/5)*10) + (1/7) * (9+8+7+6+5+4+3+2+1)')
					('0:05:59', u'( (1/5)*10) + (1/10) * (9+8+7+6+5+4+3+2+1)')
					('0:06:24', u'( (1/5)*10) + (2/5) * (9+8+7+6+5+4+3+2+1)')
					('0:06:43', u'( (1/5)*10) + (1/10) * (9+8+7+6+5+4+3+2+1)')
					('0:07:35', u'( (2/9)*10) + (1/9) * (9+8+7+6+5+4+3+2+1)')
					('0:08:56', u'((1/2)*10) + (1/2) * (9+8+7+6+5+4+3+2+1)')
					('0:09:05', u'((1/2)*10) + (1/5) * (9+8+7+6+5+4+3+2+1)')
					('0:09:13', u'((1/2)*10) + (1/4) * (9+8+7+6+5+4+3+2+1)')
					('0:09:30', u'((1/2)*10) + (1/18) * (9+8+7+6+5+4+3+2+1)')
	part2_correct_attempt
					['0:14:10', u'((2/11)*10)+((1/11)*(9+8+7+6+5+4+3+2+1))']

91 Student ID:rwthomps

	first_attempt
					2015-10-30 19:59:07
	part2_incorrect_attempt
					('0:04:35', u'(2/7 * 7) + 1/7 * (1 + 2 + 3 + 4 + 5 + 6)')
	part2_correct_attempt
					['0:21:45', u'(1/4 * 7) + 1/8 * (1 + 2 + 3 + 4 + 5 + 6)']

92 Student ID:s1powers

	first_attempt
					2015-10-25 21:20:27
	part2_incorrect_attempt
					('0:01:08', u'[7*1/4 + (6+5+4+3+2+1) * 1/8 ]/7')
					('0:03:11', u'[7/4 + 6/8+5/8+4/8+3/8+2/8+1/8 ]/ 7')
					('0:04:19', u'[7* 2/3 + (6+5+4+3+2+1)/(3*6) ]/ 7')
	part2_correct_attempt
					['2 days, 2:01:57', u'7*2/8+(6+5+4+3+2+1)*1/8']

93 Student ID:e9brown

	first_attempt
					2015-10-27 22:41:51
	part2_incorrect_attempt
					('0:00:00', u'27/6')
	part2_correct_attempt
					['0:02:46', u'27/7']

94 Student ID:vsosnovs

	first_attempt
					2015-10-30 05:51:28
	part2_incorrect_attempt
					('0:04:20', u'(1+2+3+4+5+6+7+7) 8')
	part2_correct_attempt
					['0:04:51', u'(1+2+3+4+5+6+7+7)/ 8']

95 Student ID:k5law

	first_attempt
					2015-10-26 06:17:05
	part2_incorrect_attempt
					('0:00:00', u'(1+2+3+4+5+6+7+8+9+10+10)/10')
	part2_correct_attempt
					['0:00:24', u'(1+2+3+4+5+6+7+8+9+10+10)/11']

96 Student ID:s2chaudh

	first_attempt
					2015-10-29 00:39:40
	part2_incorrect_attempt
					('0:07:09', u'1/10(45)*1/5(10)')
					('0:07:19', u'1/10(45)')
					('0:07:36', u'1/5(55)')
					('0:08:02', u'1/10(45)*(1/5(10))')
					('0:08:10', u'1/10(45)+(1/5(10))')
					('0:25:42', u'1/10*(45)+1/5*(10)')
	part2_correct_attempt
					['4:41:04', u'1/11*(45)+2/11*(10)']

97 Student ID:bmilton

	first_attempt
					2015-10-25 00:55:33
	part2_incorrect_attempt
					('0:00:33', u'1/5+2/5+3/5+4/5+5/5+12/5')
					('0:01:12', u'1/6+2/6+3/6+4/6+5/6+2')
					('0:01:46', u'1/5+2/5+3/5+4/5+5/5+12/5')
					('0:03:19', u'1/7+2/7+3/7+4/7+5/7+6/7')
	part2_correct_attempt
					['0:03:24', u'1/7+2/7+3/7+4/7+5/7+12/7']

98 Student ID:cfgutier

	first_attempt
					2015-10-29 17:54:18
	part2_incorrect_attempt
					('0:00:25', u'(1+2+3+4+5+6+6)/6')
	part2_correct_attempt
					['0:00:34', u'(1+2+3+4+5+6+6)/7']

99 Student ID:agarango

	first_attempt
					2015-10-30 19:52:31
	part2_incorrect_attempt
					('0:00:17', u'21/6')
					('0:02:22', u'27/6')
	part2_correct_attempt
					['0:03:15', u'27/7']

100 Student ID:s6deng

	first_attempt
					2015-10-28 23:27:32
	part2_incorrect_attempt
					('0:06:40', u'49/8')
					('0:11:13', u'(42/16)+(14/4)')
	part2_correct_attempt
					['0:16:26', u'35/8']

101 Student ID:msaguiar

	first_attempt
					2015-10-29 06:43:31
	part2_incorrect_attempt
					('0:09:44', u'(1+2+3+4+5+6+7+8+9+10+10)/10')
	part2_correct_attempt
					['0:09:59', u'(1+2+3+4+5+6+7+8+9+10+10)/11']

102 Student ID:aalhaida

	first_attempt
					2015-10-30 22:51:28
	part2_incorrect_attempt
					('0:08:31', u'9/2')
					('0:10:44', u'17/7')
					('0:17:18', u'5.25')
					('0:18:41', u'4.5')
	part2_correct_attempt
					['0:19:22', u'4.375']

103 Student ID:dlgoldbe

	first_attempt
					2015-10-30 06:04:54
	part2_incorrect_attempt
					('0:04:54', u'2/10')
	part2_correct_attempt
					['11:06:51', u'(1/10)+(2/10)+(3/10)+(4/10)+(5/10)+(6/10)+(7/10)+(8/10)+(18/10)']

104 Student ID:edcole

	first_attempt
					2015-10-26 21:21:02
	part2_incorrect_attempt
					('0:00:46', u'(1+1+2+3+4+5+(2*6))/6')
					('3 days, 1:20:38', u'(1+2+3+4+5+(2*6))/6')
					('3 days, 1:28:29', u'27/6')
					('3 days, 1:32:05', u'39/6')
					('3 days, 23:57:56', u'26/6')
					('3 days, 23:58:18', u'27/6')
	part2_correct_attempt
					['4 days, 0:07:17', u'27/7']

105 Student ID:yig015

	first_attempt
					2015-10-28 09:52:57
	part2_incorrect_attempt
					('0:03:36', u'5.9')
					('0:16:36', u'8.33')
					('0:16:51', u'25/3')
	part2_correct_attempt
					['1 day, 23:45:13', u'65/11']

106 Student ID:vasharma

	first_attempt
					2015-10-30 23:21:37
	part2_incorrect_attempt
					('0:03:37', u'4.5')
					('0:06:00', u'(1+2+3+4+5+2*6)/6')
	part2_correct_attempt
					['0:12:21', u'3.86']

107 Student ID:ajvanega

	first_attempt
					2015-10-23 17:00:52
	part2_incorrect_attempt
					('0:02:51', u'(1+2+3+4+5+6+7+8)/9')
					('0:08:41', u'(1+2+3+4+5+6+7+8+8)/8')
	part2_correct_attempt
					['0:08:51', u'(1+2+3+4+5+6+7+8+8)/9']

108 Student ID:zhw110

	first_attempt
					2015-10-28 03:29:16
	part2_incorrect_attempt
					('0:00:00', u'6.5')
	part2_correct_attempt
					['0:01:54', u'(55+10)/11']

109 Student ID:mjethani

	first_attempt
					2015-10-30 16:45:52
	part2_incorrect_attempt
					('0:01:22', u'1/7(1+2+3+4+5+6) + 2')
					('0:02:24', u'1/7+2/7+3/7+4/7+5/7+6/7+2')
	part2_correct_attempt
					['0:07:04', u'1/8(1+2+3+4+5+6) + 2/8(7)']












## Part 3

### (16) Mistake Group redirect of size 16




### (16) Mistake Group ['R.0'] of size 16
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|3*5+3*5.4	|5*3+6*3	|[('R.0', 15.0, u'3*5', u'5*3')]	|
|1	|4*5.5+5*5.90909	|((1/10) * (10+9+8+7+6+5+4+3+2+1) * 4) + (((2/11)*10)+((1/11)*(9+8+7+6+5+4+3+2+1)) * 5)	|[('R.0', 22.0, u'4*5.5', u'(1/10) * (10+9+8+7+6+5+4+3+2+1) * 4')]	|
|2	|3*4.5+5*4.88889	|(((1+2+3+4+5+6+7+8)/8)*3)+((1+2+3+4+5+6+7+8+8)/9*5)/8	|[('R.0', 13.5, u'3*4.5', u'((1+2+3+4+5+6+7+8)/8)*3')]	|
|3	|4*3.5+5*3.85714	|3.5*4 + 27*5/6	|[('R.0', 14.0, u'4*3.5', u'3.5*4')]	|
|4	|5*5.5+5*5.90909	|5*5.5+5*(2/11+45/11)	|[('R.0', 27.5, u'5*5.5', u'5*5.5')]	|
|5	|5*5.5+5*5.90909	|5*5.5+5*8.33	|[('R.0', 27.5, u'5*5.5', u'5*5.5')]	|
|6	|5*5.5+5*5.90909	|5*5.5+5*25/3	|[('R.0', 27.5, u'5*5.5', u'5*5.5')]	|
|7	|3*4+4*4.375	|12+(35/4)	|[('R.0', 12.0, u'3*4', u'12')]	|
|8	|2*3.5+5*3.85714	|2*3.5+2*18/7	|[('R.0', 7.0, u'2*3.5', u'2*3.5')]	|
|9	|2*3.5+5*3.85714	|2*3.5+2*27/7	|[('R.0', 7.0, u'2*3.5', u'2*3.5')]	|
|10	|5*4+3*4.375	|20*4.375	|[('R.0', 20.0, u'5*4', u'20')]	|
|11	|3*4.5+3*4.88889	|(3*(1+2+3+4+5+6+7+8)*(1/8))+ (3*(1+2+3+4+5+6+7)*(1/9) + (16/9))	|[('R.0', 13.5, u'3*4.5', u'3*(1+2+3+4+5+6+7+8)*(1/8)')]	|
|12	|2*5.5+2*5.90909	|2*((10*(10+1))/(2*10))+2*6	|[('R.0', 11.0, u'2*5.5', u'2*((10*(10+1))/(2*10))')]	|
|13	|3*5.5+5*5.90909	|5.5*3+65*3/11	|[('R.0', 16.5, u'3*5.5', u'5.5*3')]	|
|14	|3*5+2*5.4	|15+16.2	|[('R.0', 15.0, u'3*5', u'15')]	|
|15	|5*3.5+5*3.85714	|21/6 * 5 + 27/6 * 5	|[('R.0', 17.5, u'5*3.5', u'21/6 * 5')]	|




### (12) Mistake Group Digits of size 12




### (7) Mistake Group ['R.0', 'R.1.0'] of size 7
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*4+5*4.375	|16+5*(28/8)	|[('R.0', 16.0, u'4*4', u'16'), ('R.1.0', 5.0, u'5', u'5')]	|
|1	|2*4.5+5*4.88889	|(2/8) *((8*9)/2) + 5*((1/8) *((7*8)/2) + 2)	|[('R.0', 9.0, u'2*4.5', u'(2/8) *((8*9)/2)'), ('R.1.0', 5.0, u'5', u'5')]	|
|2	|4*4+5*4.375	|16+(5*3.75)	|[('R.0', 16.0, u'4*4', u'16'), ('R.1.0', 5.0, u'5', u'5')]	|
|3	|5*5.5+4*5.90909	|27.5+4*6.5	|[('R.0', 27.5, u'5*5.5', u'27.5'), ('R.1.0', 4.0, u'4', u'4')]	|
|4	|5*4+2*4.375	|5*(28/7) + 2*(21/12 + 7/2)	|[('R.0', 20.0, u'5*4', u'5*(28/7)'), ('R.1.0', 2.0, u'2', u'2')]	|
|5	|5*5+4*5.4	|5*9*(9+1)/(2*9) + 4*(2*9/(9+1))	|[('R.0', 25.0, u'5*5', u'5*9*(9+1)/(2*9)'), ('R.1.0', 4.0, u'4', u'4')]	|
|6	|3*4.5+2*4.88889	|3*[(8*9)/(2*8)] + 2*[[(2*2*7) + (6*7)]/[2*8]]	|[('R.0', 13.5, u'3*4.5', u'3*[(8*9)/(2*8)]'), ('R.1.0', 2.0, u'2', u'2')]	|




### (6) Mistake Group ['R.1'] of size 6
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*4.5+2*4.88889	|9+(4.88889*2)	|[('R.1', 9.77778, u'2*4.88889', u'4.88889*2')]	|
|1	|4*4.5+2*4.88889	|6+88/9	|[('R.1', 9.77778, u'2*4.88889', u'88/9')]	|
|2	|2*5.5+2*5.90909	|2*2+2*((10*2)/(10+1)+(10*(10-1))/(2*(10+1)))	|[('R.1', 11.81818, u'2*5.90909', u'2*((10*2)/(10+1)+(10*(10-1))/(2*(10+1)))')]	|
|3	|5*3.5+2*3.85714	|2*7+2*3.85714	|[('R.1', 7.71428, u'2*3.85714', u'2*3.85714')]	|
|4	|5*3.5+2*3.85714	|2*2+2*3.85714	|[('R.1', 7.71428, u'2*3.85714', u'2*3.85714')]	|




### (4) Mistake Group ['R.0.0', 'R.1'] of size 4
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|2*5+4*5.4	|2*4+4*5.4	|[('R.0.0', 2.0, u'2', u'2'), ('R.1', 21.6, u'4*5.4', u'4*5.4')]	|
|1	|2*5+4*5.4	|2*4+(4*5.4)	|[('R.0.0', 2.0, u'2', u'2'), ('R.1', 21.6, u'4*5.4', u'4*5.4')]	|
|2	|5*3.5+2*3.85714	|5*5+2*3.85714	|[('R.0.0', 5.0, u'5', u'5'), ('R.1', 7.71428, u'2*3.85714', u'2*3.85714')]	|
|3	|5*3.5+2*3.85714	|5*7+2*3.85714	|[('R.0.0', 5.0, u'5', u'5'), ('R.1', 7.71428, u'2*3.85714', u'2*3.85714')]	|




### (4) Mistake Group ['R.0.1', 'R.1'] of size 4
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|2*4+5*4.375	|3*[7*(7+1)/(2*7)] + 5*[2*7/(7+1) + (7*(7-1))/(2*(7+1))]	|[('R.0.1', 4.0, u'4', u'7*(7+1)/(2*7)'), ('R.1', 21.875, u'5*4.375', u'5*[2*7/(7+1) + (7*(7-1))/(2*(7+1))]')]	|
|1	|2*4+5*4.375	|3*4+5*4.375	|[('R.0.1', 4.0, u'4', u'4'), ('R.1', 21.875, u'5*4.375', u'5*4.375')]	|
|2	|5*4+5*4.375	|(2(4)) + (5(35/8)) 	|[('R.0.1', 4.0, u'4', u'4'), ('R.1', 21.875, u'5*4.375', u'5(35/8)')]	|
|3	|4*4+2*4.375	|5( 1/7(1 + 2 + 3 + 4 + 5 + 6 + 7) ) + (2( (1/4 * 7) + 1/8 * (1 + 2 + 3 + 4 + 5 + 6) ))	|[('R.0.1', 4.0, u'4', u'1/7(1 + 2 + 3 + 4 + 5 + 6 + 7)'), ('R.1', 8.75, u'2*4.375', u'2( (1/4 * 7) + 1/8 * (1 + 2 + 3 + 4 + 5 + 6) )')]	|




### (4) Mistake Group ['R.1.1'] of size 4
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|5*3.5+2*3.85714	|2*5+5*3.85714	|[('R.1.1', 3.85714, u'3.85714', u'3.85714')]	|
|1	|5*3.5+2*3.85714	|2*5+3*3.85714	|[('R.1.1', 3.85714, u'3.85714', u'3.85714')]	|
|2	|5*3.5+2*3.85714	|2*7+3*3.85714	|[('R.1.1', 3.85714, u'3.85714', u'3.85714')]	|
|3	|5*3.5+2*3.85714	|2*7+5*3.85714	|[('R.1.1', 3.85714, u'3.85714', u'3.85714')]	|




### (4) Mistake Group ['R.0.0', 'R.1.0'] of size 4
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*3.5+5*3.85714	|4/6+5/7	|[('R.0.0', 4.0, u'4', u'4'), ('R.1.0', 5.0, u'5', u'5')]	|
|1	|3*4.5+2*4.88889	|3*[(8*9)/(2*7)] + 2*[[(2*2*7) + (6*7)]/[2*8]]	|[('R.0.0', 3.0, u'3', u'3'), ('R.1.0', 2.0, u'2', u'2')]	|
|2	|4*5+3*5.4	|4*5.5+3*5.90909	|[('R.0.0', 4.0, u'4', u'4'), ('R.1.0', 3.0, u'3', u'3')]	|
|3	|3*4.5+5*4.88889	|3*(1/8) + 5*(1/9)	|[('R.0.0', 3.0, u'3', u'3'), ('R.1.0', 5.0, u'5', u'5')]	|




### (3) Mistake Group ['R.0.1', 'R.1.1'] of size 3
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1', 'R.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*5.5+2*5.90909	|5*5.5+5*5.90909	|[('R.0.1', 5.5, u'5.5', u'5.5'), ('R.1.1', 5.90909, u'5.90909', u'5.90909')]	|
|1	|4*5+3*5.4	|2*(9*(9+1)/(2*9)) + 2*(2*9/(9+1) + (9*(9-1))/(2*(9+1)))	|[('R.0.1', 5.0, u'5', u'9*(9+1)/(2*9)'), ('R.1.1', 5.4, u'5.4', u'2*9/(9+1) + (9*(9-1))/(2*(9+1))')]	|




### (3) Mistake Group Fraction of size 3




### (2) Mistake Group ['R.0.0', 'R.1.1'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|2*5+4*5.4	|(2*4)+(5*5.4)	|[('R.0.0', 2.0, u'2', u'2'), ('R.1.1', 5.4, u'5.4', u'5.4')]	|
|1	|5*3.5+2*3.85714	|5*4 + 5*(3.85714)	|[('R.0.0', 5.0, u'5', u'5'), ('R.1.1', 3.85714, u'3.85714', u'3.85714')]	|




### (2) Mistake Group ['R.0', 'R.1.1'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|3*4.5+5*4.88889	|3*4.5 + 8*4.888889	|[('R.0', 13.5, u'3*4.5', u'3*4.5'), ('R.1.1', 4.88889, u'4.88889', u'4.888889')]	|
|1	|4*4+4*4.375	|4*4+5*4.375	|[('R.0', 16.0, u'4*4', u'4*4'), ('R.1.1', 4.375, u'4.375', u'4.375')]	|




### (1) Mistake Group ['R.0.0'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|2*5+4*5.4	|2*4+(4*5)	|[('R.0.0', 2.0, u'2', u'2')]	|




### (1) Mistake Group ['R.0', 'R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|3*5+2*5.4	|(135/9)*(108/10)	|[('R.0', 15.0, u'3*5', u'135/9'), ('R.1', 10.8, u'2*5.4', u'108/10')]	|




### (46) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:galu

	first_attempt
					2015-10-30 23:59:16
	part1_correct_attempt
					['0:00:00', u'36/8']
	part3_incorrect_attempt
					('0:00:00', u'36/8')

1 Student ID:jag028

	first_attempt
					2015-10-29 19:19:25
	part1_correct_attempt
					['0:00:00', u'(1/9)+2(1/9)+3(1/9)+4(1/9)+5(1/9)+6(1/9)+7(1/9)+8(1/9)+9(1/9)']
	part2_correct_attempt
					['23:06:04', u'(1/10)+2(1/10)+3(1/10)+4(1/10)+5(1/10)+6(1/10)+7(1/10)+8(1/10)+9(1/5)']
	part3_incorrect_attempt
					('23:06:41', u'10.4')
	part3_correct_attempt
					['23:07:31', u'15+10.8']

2 Student ID:ctroncos

	first_attempt
					2015-10-29 16:00:12
	part1_correct_attempt
					['0:00:00', u'9*(9+1)/(2*9)']
	part2_correct_attempt
					['0:01:40', u'(2*9/(9+1) + (9*(9-1))/(2*(9+1)))']
	part3_incorrect_attempt
					('0:01:58', u'4*(2*9/(9+1) + (9*(9-1))/(2*(9+1)))')
					('0:02:04', u'4*(2*9/(9) + (9*(9-1))/(2*(9+1)))')
					('0:02:12', u'4*(2*9/(9+1) + (9*(9-1))/(2*(9+1)))')
	part3_correct_attempt
					['0:03:07', u'((5*9*(9+1)/(2*9)) + 4*(2*9/(9+1) + (9*(9-1))/(2*(9+1))))']

3 Student ID:lywong

	first_attempt
					2015-10-28 08:26:30
	part1_correct_attempt
					['0:00:00', u'5.5']
	part2_correct_attempt
					['0:01:54', u'65/11']
	part3_incorrect_attempt
					('0:03:59', u'((5.5*4)+(65/11*5))/9')
	part3_correct_attempt
					['23:00:24', u'5.5*4+(65/11*5)']

4 Student ID:kvass

	first_attempt
					2015-10-26 17:01:33
	part1_correct_attempt
					['0:00:00', u'7/2']
	part2_correct_attempt
					['1:49:18', u'2*6/(6+1) + (6*(6-1))/(2*(6+1))']
	part3_incorrect_attempt
					('1:51:25', u'7/2 + 2*6/(6+1) + (6*(6-1))/(2*(6+1))')
	part3_correct_attempt
					['1:52:07', u'5(7/2) + 5(2*6/(6+1) + (6*(6-1))/(2*(6+1)))']

5 Student ID:aggouw

	first_attempt
					2015-10-27 03:25:48
	part1_correct_attempt
					['0:00:00', u'7*(7+1)/(2*7)']
	part2_correct_attempt
					['0:00:10', u'2*7/(7+1) + (7*(7-1))/(2*(7+1))']
	part3_incorrect_attempt
					('0:00:49', u'33.875/0.1')
	part3_correct_attempt
					['0:01:18', u'2*[7*(7+1)/(2*7)] + 5*[2*7/(7+1) + (7*(7-1))/(2*(7+1))]']

6 Student ID:vasharma

	first_attempt
					2015-10-30 23:21:37
	part1_correct_attempt
					['0:00:00', u'3.5']
	part2_correct_attempt
					['0:12:21', u'3.86']
	part3_incorrect_attempt
					('0:12:51', u'3.86+3.5')
	part3_correct_attempt
					['0:13:53', u'3(3.86)+4(3.5)']

7 Student ID:atorr

	first_attempt
					2015-10-29 06:38:19
	part1_correct_attempt
					['0:00:00', u'(1+2+3+4+5+6+7+8)*(1/8)']
	part2_correct_attempt
					['0:05:16', u'(1+2+3+4+5+6+7)*(1/9) + (16/9)']
	part3_incorrect_attempt
					('0:06:44', u'((1+2+3+4+5+6+7+8)*(1/8))^3+ ((1+2+3+4+5+6+7)*(1/9) + (16/9))^3')
					('0:07:12', u'((1+2+3+4+5+6+7+8)*(1/8^3))+ ((1+2+3+4+5+6+7)*(1/9^3) + (16^3/9^3))')
					('1:24:49', u'(1/36) * (3 + 12 + 30 + 60 + 105 + 168 + 225 + 270 + 297 + 300 + 273 + 210 + 150 + 96 + 51 + 18)')
	part3_correct_attempt
					['13:24:08', u'3*((4.5) + (4.88889))']

8 Student ID:spw006

	first_attempt
					2015-10-27 23:49:52
	part1_correct_attempt
					['0:00:00', u'5']
	part2_correct_attempt
					['0:00:47', u'9*(1/5) + .8 + .7 + .6 +.5 + .4 + .3 + .2 + .1']
	part3_incorrect_attempt
					('0:01:02', u'25.8')
	part3_correct_attempt
					['0:01:13', u'10 + 5.4(3)']

9 Student ID:any027

	first_attempt
					2015-10-26 04:09:44
	part1_correct_attempt
					['0:00:00', u'(1/10) * (10+9+8+7+6+5+4+3+2+1)']
	part2_correct_attempt
					['0:14:10', u'((2/11)*10)+((1/11)*(9+8+7+6+5+4+3+2+1))']
	part3_incorrect_attempt
					('0:15:55', u'((4*5.5) + (5.90909 * 5)) / 9')
	part3_correct_attempt
					['0:16:23', u'((4*5.5) + (5.90909 * 5))']

10 Student ID:krau

	first_attempt
					2015-10-29 21:59:04
	part1_correct_attempt
					['0:00:00', u'3.5']
	part2_correct_attempt
					['0:08:39', u'6*2/7+15*1/7']
	part3_incorrect_attempt
					('0:08:58', u'3.5+6*2/7+15*1/7')
	part3_correct_attempt
					['0:09:27', u'3.5*4 + (6*2/7+15*1/7)*2']

11 Student ID:kthui

	first_attempt
					2015-10-29 02:55:09
	part1_correct_attempt
					['0:00:00', u'(1+2+3+4+5+6+7+8+9+10)*(1/10)']
	part2_correct_attempt
					['0:01:26', u'(1+2+3+4+5+6+7+8+9)*(1/11)+10*(2/11)']
	part3_incorrect_attempt
					('2:36:40', u'(((1+2+3+4+5+6+7+8+9+10)*(1/10))*2+((1+2+3+4+5+6+7+8+9)*(1/11)+10*(2/11))*5)/(2+5)')
	part3_correct_attempt
					['2:37:51', u'((1+2+3+4+5+6+7+8+9+10)*(1/10))*2+((1+2+3+4+5+6+7+8+9)*(1/11)+10*(2/11))*5']

12 Student ID:w4shin

	first_attempt
					2015-10-30 17:45:04
	part1_correct_attempt
					['0:00:00', u'(1/10)*(1+2+3+4+5+6+7+8+9+10)']
	part2_correct_attempt
					['0:00:00', u'(1/11)*(1+2+3+4+5+6+7+8+9)+(2/11)*10']
	part3_incorrect_attempt
					('0:00:00', u'(1/10)*(1+2+3+4+5+6+7+8+9+10)+(1/11)*(1+2+3+4+5+6+7+8+9)+(2/11)*10')
	part3_correct_attempt
					['0:00:34', u'5*((1/10)*(1+2+3+4+5+6+7+8+9+10))+5*((1/11)*(1+2+3+4+5+6+7+8+9)+(2/11)*10)']

13 Student ID:mbl003

	first_attempt
					2015-10-27 08:34:24
	part1_correct_attempt
					['0:00:00', u'(1+2+3+4+5+6+7+8)/8']
	part2_correct_attempt
					['0:00:16', u'(1+2+3+4+5+6+7+8+8)/9']
	part3_incorrect_attempt
					('0:01:42', u'((((1+2+3+4+5+6+7+8)/8)*3)+((1+2+3+4+5+6+7+8+8)/9*5))/8')
					('0:02:15', u'((((1+2+3+4+5+6+7+8)/8)*3)*((1+2+3+4+5+6+7+8+8)/9*5))/8')
					('0:02:38', u'((((1+2+3+4+5+6+7+8)/8)*3)+((1+2+3+4+5+6+7+8+8)/9*5))/8')
	part3_correct_attempt
					['0:03:06', u'((((1+2+3+4+5+6+7+8)/8)*3)+((1+2+3+4+5+6+7+8+8)/9*5))']

14 Student ID:nhn018

	first_attempt
					2015-10-29 04:06:43
	part1_correct_attempt
					['0:00:00', u'4']
	part2_correct_attempt
					['1:09:47', u'(1+2+3+4+5+6+14)/8']
	part3_incorrect_attempt
					('1:10:20', u'8.375')
					('1:11:36', u'20*4.375*3')
	part3_correct_attempt
					['1:12:04', u'20+4.375*3']

15 Student ID:c4du

	first_attempt
					2015-10-29 04:53:08
	part1_correct_attempt
					['0:00:00', u'9/2']
	part2_correct_attempt
					['0:01:15', u'44/9']
	part3_incorrect_attempt
					('0:04:48', u'9/2+44/9')
	part3_correct_attempt
					['0:08:48', u'2*(9/2+44/9)']

16 Student ID:j6quach

	first_attempt
					2015-10-25 21:26:03
	part1_correct_attempt
					['0:00:00', u'(1+2+3+4+5+6+7+8+9)/9']
	part2_correct_attempt
					['0:00:00', u'(1+2+3+4+5+6+7+8)/10 + 18/10']
	part3_incorrect_attempt
					('0:00:00', u'1 + 5.4/4')
					('4 days, 23:35:39', u'5 + 5.4')
					('4 days, 23:36:09', u'(5*5 + 5.4*4)/9')
	part3_correct_attempt
					['4 days, 23:38:01', u'5*5 + 5.4*4']

17 Student ID:ksmurlo

	first_attempt
					2015-10-27 06:26:33
	part1_correct_attempt
					['0:00:00', u'(1+2+3+4+5+6+7)/7']
	part2_correct_attempt
					['0:00:00', u'(1+2+3+4+5+6+7+7)/8']
	part3_incorrect_attempt
					('0:02:55', u'4+4.375')
	part3_correct_attempt
					['0:03:28', u'4*3+4.375*5']

18 Student ID:jhw015

	first_attempt
					2015-10-27 23:45:45
	part1_correct_attempt
					['0:00:00', u'45/9']
	part2_correct_attempt
					['0:05:09', u'54/10']
	part3_incorrect_attempt
					('0:06:30', u'(45/9)^3  + (54/10)^2')
	part3_correct_attempt
					['0:07:43', u'(135/9)+(108/10)']

19 Student ID:airanmeh

	first_attempt
					2015-10-28 19:49:46
	part1_correct_attempt
					['0:00:00', u'36/8']
	part2_correct_attempt
					['11:34:49', u'16/9+28/9']
	part3_incorrect_attempt
					('11:35:14', u'16/9+28/9+ 16/8')
					('11:37:32', u'4*16/9+4*28/9+ 2*16/8')
	part3_correct_attempt
					['11:38:07', u'4*(16/9+28/9)+ 2*36/8']

20 Student ID:jew037

	first_attempt
					2015-10-28 18:26:26
	part1_correct_attempt
					['0:00:00', u'8*(8+1)/(2*8)']
	part2_correct_attempt
					['0:00:00', u'2*8/(8+1) + (8*(8-1))/(2*(8+1))']
	part3_incorrect_attempt
					('0:01:14', u'2*8/(8+1) + (8*(8-1))/(2*(8+1))')
	part3_correct_attempt
					['0:01:39', u'2(8*(8+1)/(2*8)) + 2(2*8/(8+1) + (8*(8-1))/(2*(8+1)))']

21 Student ID:agarango

	first_attempt
					2015-10-30 19:52:31
	part1_correct_attempt
					['0:00:00', u'21/6']
	part2_correct_attempt
					['0:03:15', u'27/7']
	part3_incorrect_attempt
					('0:04:09', u'(147+162)/42')
	part3_correct_attempt
					['0:05:28', u'(588+810)/42']

22 Student ID:s6deng

	first_attempt
					2015-10-28 23:27:32
	part1_correct_attempt
					['0:00:00', u'4']
	part2_correct_attempt
					['0:16:26', u'35/8']
	part3_incorrect_attempt
					('0:18:30', u'7+(35/4)')
	part3_correct_attempt
					['0:19:59', u'12+(35/2)']

23 Student ID:m4salaza

	first_attempt
					2015-10-29 04:59:49
	part1_correct_attempt
					['0:00:00', u'(1+2+3+4+5+6+7+8+9+10)/10']
	part2_correct_attempt
					['0:04:43', u'(1+2+3+4+5+6+7+8+9+20)/11']
	part3_incorrect_attempt
					('0:05:19', u'5.5*5.90909')
	part3_correct_attempt
					['0:09:28', u'3*5.5 + 3*5.9090']

24 Student ID:dwzhang

	first_attempt
					2015-10-29 21:25:57
	part1_correct_attempt
					['0:00:00', u'1/6 + 2/6 + 3/6 + 4/6 + 5/6 + 6/6']
	part2_correct_attempt
					['0:01:41', u'1/7 + 2/7 + 3/7 + 4/7 + 5/7 + 12/7']
	part3_incorrect_attempt
					('0:02:28', u'(1/7 + 2/7 + 3/7 + 4/7 + 5/7 + 12/7)^4 + (1/6 + 2/6 + 3/6 + 4/6 + 5/6 + 6/6)^2')
					('0:08:54', u'(1/7 + 2/7 + 3/7 + 4/7 + 5/7 + 12/7)^2 + (1/6 + 2/6 + 3/6 + 4/6 + 5/6 + 6/6)^4')
	part3_correct_attempt
					['0:09:16', u'4(1/6 + 2/6 + 3/6 + 4/6 + 5/6 + 6/6) + 2(1/7 + 2/7 + 3/7 + 4/7 + 5/7 + 12/7)']

25 Student ID:agian

	first_attempt
					2015-10-30 22:21:56
	part1_correct_attempt
					['0:00:00', u'6*(6+1)/(2*6)']
	part2_correct_attempt
					['0:00:49', u'2*6/(6+1)+(6*(6-1))/(2*(6+1))']
	part3_incorrect_attempt
					('0:02:06', u'2*5+5*3.5')
					('0:04:09', u'2*7+3*3.857146')
	part3_correct_attempt
					['0:06:53', u'5*3.5+2*3.85714']

26 Student ID:tol003

	first_attempt
					2015-10-28 01:02:12
	part1_correct_attempt
					['0:00:00', u'4']
	part2_correct_attempt
					['0:05:39', u'21/8+7/4']
	part3_incorrect_attempt
					('0:12:08', u'4+21/8+7/4')
	part3_correct_attempt
					['0:15:38', u'(2*4)+(3*(21/8+7/4))']

27 Student ID:aalhaida

	first_attempt
					2015-10-30 22:51:28
	part1_correct_attempt
					['0:00:00', u'4']
	part2_correct_attempt
					['0:19:22', u'4.375']
	part3_incorrect_attempt
					('0:27:41', u'4.26785714286')
	part3_correct_attempt
					['0:28:37', u'(4+4+5(4.375))']

28 Student ID:r1gu

	first_attempt
					2015-10-30 08:52:35
	part1_correct_attempt
					['0:00:00', u'10(10+1)/(20)']
	part2_correct_attempt
					['0:00:44', u'2*10/(10+1)+(10*(10-1))/(2*(10+1))']
	part3_incorrect_attempt
					('0:00:54', u'5.5+5.909')
					('0:01:00', u'5.5+5.90909')
	part3_correct_attempt
					['0:01:29', u'4*5.5+2*5.90909']

29 Student ID:kbielawi

	first_attempt
					2015-10-26 21:39:28
	part1_correct_attempt
					['0:00:00', u'(1+2+3+4+5+6+7+8+9)/9']
	part2_correct_attempt
					['1 day, 3:17:00', u'(1+2+3+4+5+6+7+8+18)/10']
	part3_incorrect_attempt
					('1 day, 3:19:10', u'26.2/5')
					('1 day, 3:19:52', u'25.8/5')
	part3_correct_attempt
					['1 day, 3:21:35', u'25.8']

30 Student ID:thwan

	first_attempt
					2015-10-27 18:06:41
	part1_correct_attempt
					['0:00:00', u'1/7+2/7+3/7+4/7+5/7+6/7+7/7']
	part2_correct_attempt
					['0:00:00', u'2*7/8+1/8+2/8+3/8+4/8+5/8+6/8']
	part3_incorrect_attempt
					('0:06:53', u'4^2*(4.375)^4')
	part3_correct_attempt
					['0:07:37', u'4*2+4.375*4']

31 Student ID:yeh013

	first_attempt
					2015-10-28 06:17:16
	part1_correct_attempt
					['0:00:00', u'21/6']
	part2_correct_attempt
					['0:00:22', u'27/7']
	part3_incorrect_attempt
					('0:01:14', u'21/6+27/7')
	part3_correct_attempt
					['0:01:30', u'(21/6+27/7)*2']

32 Student ID:aysee

	first_attempt
					2015-10-29 23:38:52
	part1_correct_attempt
					['0:00:00', u'[10*(10+1)]/(2*10)']
	part2_correct_attempt
					['0:00:00', u'(2*10)/(10+1)+(10*(10-1))/(2*(10+1))']
	part3_incorrect_attempt
					('0:00:00', u'4*[10*(10+1)]/(2*10) + 2*(2*10)/(10+1)+(10*(10-1))/(2*(10+1))')
	part3_correct_attempt
					['0:01:26', u'4*[10*(10+1)]/(2*10) + 2*[(2*10)/(10+1)+(10*(10-1))/(2*(10+1))]']

33 Student ID:ytc012

	first_attempt
					2015-10-29 11:34:57
	part1_correct_attempt
					['0:00:00', u'(8+7+6+5+4+3+2+1)/8']
	part2_correct_attempt
					['0:04:38', u'(16+7+6+5+4+3+2+1)/9']
	part3_incorrect_attempt
					('0:05:42', u'(8+7+6+5+4+3+2+1)(16+7+6+5+4+3+2+1)/9/8')
					('0:06:05', u'5(8+7+6+5+4+3+2+1)3(16+7+6+5+4+3+2+1)/9/8')
					('0:06:34', u'((8+7+6+5+4+3+2+1)/8)^5')
					('0:07:17', u'(((8+7+6+5+4+3+2+1)/8)^5)(((16+7+6+5+4+3+2+1)/9)^3)')
					('0:07:51', u'5(8+7+6+5+4+3+2+1)/8')
	part3_correct_attempt
					['0:08:06', u'5(8+7+6+5+4+3+2+1)/8+3(16+7+6+5+4+3+2+1)/9']

34 Student ID:aadhakal

	first_attempt
					2015-10-29 23:53:13
	part1_correct_attempt
					['0:00:00', u'(10*(10+1))/(2*10)']
	part2_correct_attempt
					['0:00:00', u'(10*2)/(10+1)+(10*(10-1))/(2*(10+1))']
	part3_incorrect_attempt
					('0:05:45', u'2*2+2*6')
	part3_correct_attempt
					['0:08:31', u'2*((10*(10+1))/(2*10))+2*((10*2)/(10+1)+(10*(10-1))/(2*(10+1)))']

35 Student ID:glcohen

	first_attempt
					2015-10-27 17:36:59
	part1_correct_attempt
					['0:00:00', u'1(1/8)+2(1/8)+3(1/8)+4(1/8)+5(1/8)+6(1/8)+7(1/8)+8(1/8)']
	part2_correct_attempt
					['0:01:44', u'1(1/9)+2(1/9)+3(1/9)+4(1/9)+5(1/9)+6(1/9)+7(1/9)+8(2/9)']
	part3_incorrect_attempt
					('0:02:33', u'9+(4.8888*2)')
	part3_correct_attempt
					['0:03:05', u'(4.5*4)+(4.88889*2)']

36 Student ID:tdurrer

	first_attempt
					2015-10-27 04:40:33
	part1_correct_attempt
					['0:00:00', u'5.5']
	part2_correct_attempt
					['0:00:00', u'65/11']
	part3_incorrect_attempt
					('0:00:00', u'(5.5)+(65/11)')
	part3_correct_attempt
					['0:00:36', u'2(5.5)+3(65/11)']

37 Student ID:qfu

	first_attempt
					2015-10-23 02:59:25
	part1_correct_attempt
					['0:00:00', u'4']
	part2_correct_attempt
					['0:00:00', u'7/4+(1+2+3+4+5+6)/8']
	part3_incorrect_attempt
					('0:00:17', u'(1+2+3+4+5+6+7)/5+7+(1+2+3+4+5+6)/2')
					('0:01:49', u'4+7/4+(1+2+3+4+5+6)/8')
	part3_correct_attempt
					['0:11:28', u'4*5+ 4.375*2']

38 Student ID:starinia

	first_attempt
					2015-10-30 22:10:09
	part1_correct_attempt
					['0:00:00', u'21/6']
	part2_correct_attempt
					['0:04:54', u'12/7 + 30/14']
	part3_incorrect_attempt
					('0:04:54', u'12/7 + 30/14 + 21/6')
					('0:05:12', u'12/7 + 30/14 * 21/6 *2')
					('0:05:17', u'12/7 + 30/14 + 21/6 *2')
	part3_correct_attempt
					['0:05:41', u'5 * (12/7 + 30/14) + 21/6 *5']

39 Student ID:dcastlem

	first_attempt
					2015-10-30 19:36:50
	part1_correct_attempt
					['0:00:00', u'36/8']
	part2_correct_attempt
					['0:00:00', u'44/9']
	part3_incorrect_attempt
					('0:00:00', u'382/9')
	part3_correct_attempt
					['2:37:19', u'595/18']

40 Student ID:volim

	first_attempt
					2015-10-28 05:35:30
	part1_correct_attempt
					['0:00:00', u'(1+2+3+4+5+6+7+8+9)/9']
	part2_correct_attempt
					['0:00:49', u'(1+2+3+4+5+6+7+8+9+9)/10']
	part3_incorrect_attempt
					('0:01:22', u'(5+5+5+5.4+5.4+5.4)/7')
					('0:01:28', u'(5+5+5+5.4+5.4+5.4)/9')
					('0:01:44', u'(5+5+5)/9+(5.4+5.4+5.4)/10')
	part3_correct_attempt
					['0:02:21', u'15+(4*5.4)']

41 Student ID:hsc052

	first_attempt
					2015-10-30 21:33:50
	part1_correct_attempt
					['0:00:00', u'45/9']
	part2_correct_attempt
					['0:06:50', u'(54/10)']
	part3_incorrect_attempt
					('0:06:50', u'(45/9)+54/10')
	part3_correct_attempt
					['0:15:08', u'3*(45/9)+(54/10)*2']

42 Student ID:yos017

	first_attempt
					2015-10-29 06:07:42
	part1_correct_attempt
					['0:00:00', u'(1+2+3+4+5+6+7+8+9+10)/10']
	part2_correct_attempt
					['0:01:18', u'(1+2+3+4+5+6+7+8+9+20)/11']
	part3_incorrect_attempt
					('0:02:24', u'[(1+2+3+4+5+6+7+8+9+10)/10]+[(1+2+3+4+5+6+7+8+9+20)/11]')
	part3_correct_attempt
					['0:03:11', u'4*[(1+2+3+4+5+6+7+8+9+10)/10]+5*[(1+2+3+4+5+6+7+8+9+20)/11]']

43 Student ID:aordookh

	first_attempt
					2015-10-28 22:14:15
	part1_correct_attempt
					['0:00:00', u'(1+2+3+4+5+6+7+8+9)*(1/9)']
	part2_correct_attempt
					['0:00:00', u'(.9/9)*(1+2+3+4+5+6+7+8) + (1.8/9)*9']
	part3_incorrect_attempt
					('0:01:18', u'5+5.4')
					('0:32:52', u'((1+1)*((1/9)(.9/9)))+ (2*(1+2)((1/9)(.9/9)))+(2*(1+3)((1/9)(.9/9)))+(2*(1+4)((1/9)(.9/9))) + (2*(1+5)((1/9)(.9/9))) + (2*(1+6)((1/9)(.9/9)))+(2*(1+7)((1/9)(.9/9)))+(2*(1+8)((1/9)(.9/9)))+((1+9)((1/9)(.9/9)))+((1+9)((1/9)(1.8/9)))+((2+2)((1/9)(.9/9))) + (2*(2+3)((1/9)(.9/9)))+(2*(2+4)((1/9)(.9/9))) + (2*(2+5)((1/9)(.9/9)))+(2*(2+6)((1/9)(.9/9))) + (2*(2+7)((1/9)(.9/9))) + (2*(2+8)((1/9)(.9/9)))+((2+9)((1/9)(.9/9)))+((2+9)((1/9)(1.8/9))) + ((3+3)((1/9)(.9/9)))+(2*(3+4)((1/9)(.9/9)))+(2*(3+5)((1/9)(.9/9)))+(2*(3+6)((1/9)(.9/9)))+(2*(3+6)((1/9)(.9/9)))+(2*(3+7)((1/9)(.9/9)))+(2*(3+8)((1/9)(.9/9)))+(2*(3+9)((1/9)(.9/9)))+((3+9)((1/9)(.9/9)))+((4+4)((1/9)(.9/9)))+(2*(4+5)((1/9)(.9/9)))+(2*(4+6)((1/9)(.9/9)))+(2*(4+7)((1/9)(.9/9)))+ (2*(4+8)((1/9)(.9/9)))+(2*(4+9)((1/9)(.9/9)))+((4+9)((1/9)(.9/9)))+((5+5)((1/9)(.9/9)))+(2*(5+6)((1/9)(.9/9)))+((2*(5+7)((1/9)(.9/9))))+(2*(5+8)((1/9)(.9/9)))+(2*(5+9)((1/9)(.9/9)))+((5+9)((1/9)(.9/9)))+((6+6)((1/9)(.9/9)))')
					('4:16:06', u'(1*(2)*((1/9)(.9/9)))+ (2*(3)((1/9)(.9/9)))+(3*(4)((1/9)(.9/9)))+(4*(5)((1/9)(.9/9))) + (5*(6)((1/9)(.9/9))) + (6*(7)((1/9)(.9/9)))+(7*(8)((1/9)(.9/9)))+(8*(9)((1/9)(.9/9)))+(8*(10)((1/9)(.9/9)))+((1+9)((1/9)(1.8/9)))+(9*(11)((1/9)(.9/9))) + (10*(12)((1/9)(.9/9)))+(11*(13)((1/9)(.9/9))) + (12*(14)((1/9)(.9/9)))+(13*(15)((1/9)(.9/9))) + (14*(16)((1/9)(.9/9))) + (15*(17)((1/9)(.9/9)))+((18)((1/9)(1.8/9)))+((11)((1/9)(1.8/9)))+((12)((1/9)(1.8/9)))+((13)((1/9)(1.8/9)))+((14)((1/9)(1.8/9)))+((15)((1/9)(1.8/9)))+((16)((1/9)(1.8/9)))+((17)((1/9)(1.8/9)))')
					('4:20:33', u'(1*(2)*((1/9)(.9/9)))+ (2*(3)((1/9)(.9/9)))+(3*(4)((1/9)(.9/9)))+(4*(5)((1/9)(.9/9))) + (5*(6)((1/9)(.9/9))) + (6*(7)((1/9)(.9/9)))+(7*(8)((1/9)(.9/9)))+(8*(9)((1/9)(.9/9)))+(8*(10)((1/9)(.9/9)))+((1+9)((1/9)(1.8/9)))+(7*(11)((1/9)(.9/9))) + (6*(12)((1/9)(.9/9)))+(5*(13)((1/9)(.9/9))) + (4*(14)((1/9)(.9/9)))+(3*(15)((1/9)(.9/9))) + (2*(16)((1/9)(.9/9))) + (1*(17)((1/9)(.9/9)))+((18)((1/9)(1.8/9)))+((11)((1/9)(1.8/9)))+((12)((1/9)(1.8/9)))+((13)((1/9)(1.8/9)))+((14)((1/9)(1.8/9)))+((15)((1/9)(1.8/9)))+((16)((1/9)(1.8/9)))+((17)((1/9)(1.8/9)))')
	part3_correct_attempt
					['4:33:45', u'2(5.4+5)']

44 Student ID:hmnaing

	first_attempt
					2015-10-30 07:48:22
	part1_correct_attempt
					['0:00:00', u'36/8']
	part2_correct_attempt
					['0:10:30', u'(28+16)/9']
	part3_incorrect_attempt
					('0:10:55', u'36/8 +(28+16)/9')
	part3_correct_attempt
					['0:11:44', u'5*36/8 +2*(28+16)/9']

45 Student ID:tjke

	first_attempt
					2015-10-30 22:57:35
	part1_correct_attempt
					['0:00:00', u'1*1/7+2*1/7+3*1/7+4*1/7+5*1/7+6*1/7+7*1/7']
	part2_correct_attempt
					['0:00:00', u'7*2/8+6*1/8+5*1/8+4*1/8+3*1/8+2*1/8+1*1/8']
	part3_incorrect_attempt
					('0:00:00', u'[1*1/7+2*1/7+3*1/7+4*1/7+5*1/7+6*1/7+7*1/7]^4+[7*2/8+6*1/8+5*1/8+4*1/8+3*1/8+2*1/8+1*1/8]^2')
	part3_correct_attempt
					['0:01:09', u'[1*1/7+2*1/7+3*1/7+4*1/7+5*1/7+6*1/7+7*1/7]*4+[7*2/8+6*1/8+5*1/8+4*1/8+3*1/8+2*1/8+1*1/8]*2']












## Part 4

### (87) Mistake Group Digits of size 87




### (22) Mistake Group ['R.1'] of size 22
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|33.4445/0.3	|((1+2+3+4+5+6+7+8+8)/9)/.3	|[('R.1', 0.3, u'0.3', u'.3')]	|
|1	|33.8182/0.3	|57.0455/0.3	|[('R.1', 0.3, u'0.3', u'0.3')]	|
|2	|33.875/0.4	|(4+4.375)/.4	|[('R.1', 0.4, u'0.4', u'.4')]	|
|3	|37.5556/0.4	|((4.5*4)+(((1/9*1)+(1/9*2)+(1/9*3)+(1/9*4)+(1/9*5)+(1/9*6)+(1/9*7)+(2/9*8))*4))*0.4	|[('R.1', 0.4, u'0.4', u'0.4')]	|
|4	|18.7778/0.1	|(2*8/(8+1) + (8*(8-1))/(2*(8+1)))/.1	|[('R.1', 0.1, u'0.1', u'.1')]	|
|5	|36.2/0.5	|20.7/0.5	|[('R.1', 0.5, u'0.5', u'0.5')]	|
|6	|33.125/0.2	|8.375/.2	|[('R.1', 0.2, u'0.2', u'.2')]	|
|7	|29.7857/0.5	|(27/7)/.5	|[('R.1', 0.5, u'0.5', u'.5')]	|
|8	|34.2273/0.2	|.5/.2	|[('R.1', 0.2, u'0.2', u'.2')]	|
|9	|39.7273/0.2	|1-0.2	|[('R.1', 0.2, u'0.2', u'0.2')]	|
|10	|33.8182/0.4	|(4*[10*(10+1)]/(2*10) + 2*(2*10)/(10+1)+(10*(10-1))/(2*(10+1)))/0.4	|[('R.1', 0.4, u'0.4', u'0.4')]	|
|11	|22.8182/0.4	|(2*2+2*((10*2)/(10+1)+(10*(10-1))/(2*(10+1))))/0.4	|[('R.1', 0.4, u'0.4', u'0.4')]	|
|12	|33.5/0.4	|33.875/0.4	|[('R.1', 0.4, u'0.4', u'0.4')]	|
|13	|23.2778/0.3	|[4*[(8*9)/(2*8)] + 2*[[(2*2*7) + (7*8)]/[2*8]]]/0.3	|[('R.1', 0.3, u'0.3', u'0.3')]	|
|14	|35.8/0.4	|5.1*0.4	|[('R.1', 0.4, u'0.4', u'0.4')]	|
|15	|57.0455/0.3	|((1/10)*(1+2+3+4+5+6+7+8+9+10)+(1/11)*(1+2+3+4+5+6+7+8+9)+(2/11)*10)/0.3	|[('R.1', 0.3, u'0.3', u'0.3')]	|
|16	|35.8/0.4	|35.0/0.4	|[('R.1', 0.4, u'0.4', u'0.4')]	|
|17	|23.2778/0.3	|[4*[(8*9)/(2*8)] + 2*[[(2*2*8) + (7*8)]/[2*9]]]/0.3	|[('R.1', 0.3, u'0.3', u'0.3')]	|
|18	|25.8/0.5	|((45/9)+(36/9)+(9/10))/0.5	|[('R.1', 0.5, u'0.5', u'0.5')]	|
|19	|25.8/0.5	|((45/9)+54/10)/0.5	|[('R.1', 0.5, u'0.5', u'0.5')]	|
|20	|33.0556/0.3	|25.8/.3	|[('R.1', 0.3, u'0.3', u'.3')]	|
|21	|29.875/0.2	|(3*[7*(7+1)/(2*7)] + 5*[2*7/(7+1) + (7*(7-1))/(2*(7+1))])/0.2	|[('R.1', 0.2, u'0.2', u'0.2')]	|




### (18) Mistake Group ['R.0'] of size 18
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|29.875/0.2	|29.875/0.1	|[('R.0', 29.875, u'29.875', u'29.875')]	|
|1	|20.75/0.5	|(12+(.25*7 + .75*(3.5))*2)/(1/7)	|[('R.0', 20.75, u'20.75', u'12+(.25*7 + .75*(3.5))*2')]	|
|2	|45.2273/0.6	|[(5*5.5)+(3*5.90909)]/10	|[('R.0', 45.2273, u'45.2273', u'(5*5.5)+(3*5.90909)')]	|
|3	|45.2273/0.6	|[(5*5.5)+(3*5.90909)]/11	|[('R.0', 45.2273, u'45.2273', u'(5*5.5)+(3*5.90909)')]	|
|4	|34.6364/0.5	|34.6364/10^6	|[('R.0', 34.6364, u'34.6364', u'34.6364')]	|
|5	|25.2143/0.1	|((3.5 * 5) + (27/7 * 2)) / (10 * (3.5 * 5) + (27/7 * 2))	|[('R.0', 25.2143, u'25.2143', u'(3.5 * 5) + (27/7 * 2)')]	|
|6	|37.1667/0.6	|(4.5*5+44/9*3)/8	|[('R.0', 37.1667, u'37.1667', u'4.5*5+44/9*3')]	|
|7	|20.75/0.3	|(3*(7*8/14) + 2*(14/8 + 7*6/(2*8)))/3	|[('R.0', 20.75, u'20.75', u'3*(7*8/14) + 2*(14/8 + 7*6/(2*8))')]	|
|8	|33.2857/0.4	|33.2857/.44	|[('R.0', 33.2857, u'33.2857', u'33.2857')]	|
|9	|20.8/0.2	|20.8/.02	|[('R.0', 20.8, u'20.8', u'20.8')]	|
|10	|37.1667/0.5	|37.1667/2	|[('R.0', 37.1667, u'37.1667', u'37.1667')]	|
|11	|46.6/0.6	|(((5*9*(9+1)/(2*9)) + 4*(2*9/(9+1) + (9*(9-1))/(2*(9+1))))/06)	|[('R.0', 46.6, u'46.6', u'(5*9*(9+1)/(2*9)) + 4*(2*9/(9+1) + (9*(9-1))/(2*(9+1)))')]	|
|12	|36.2/0.3	|(4*(9*(9+1)/(2*9)) + 3*(2*9/(9+1) + (9*(9-1))/(2*(9+1))))/(9*(9+1)/(2*9))	|[('R.0', 36.2, u'36.2', u'4*(9*(9+1)/(2*9)) + 3*(2*9/(9+1) + (9*(9-1))/(2*(9+1)))')]	|
|13	|36.2/0.3	|(4*(9*(9+1)/(2*9)) + 3*(2*9/(9+1) + (9*(9-1))/(2*(9+1))))/(2*9/(9+1) + (9*(9-1))/(2*(9+1)))	|[('R.0', 36.2, u'36.2', u'4*(9*(9+1)/(2*9)) + 3*(2*9/(9+1) + (9*(9-1))/(2*(9+1)))')]	|
|14	|22.8182/0.4	|(2*((10*(10+1))/(2*10))+2*((10*2)/(10+1)+(10*(10-1))/(2*(10+1))))/2	|[('R.0', 22.8182, u'22.8182', u'2*((10*(10+1))/(2*10))+2*((10*2)/(10+1)+(10*(10-1))/(2*(10+1)))')]	|
|15	|31.2/0.3	|(15 + 16.2) /.4	|[('R.0', 31.2, u'31.2', u'15 + 16.2')]	|
|16	|36.7857/0.4	|(5 * (12/7 + 30/14) + 21/6 *5) /4	|[('R.0', 36.7857, u'36.7857', u'5 * (12/7 + 30/14) + 21/6 *5')]	|
|17	|28.3182/0.5	|((5.5*3) + ((65/11)*2))/11	|[('R.0', 28.3182, u'28.3182', u'(5.5*3) + ((65/11)*2)')]	|




### (17) Mistake Group Fraction of size 17




### (15) Mistake Group redirect of size 15




### (11) Mistake Group ['R.0', 'R.1'] of size 11
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|27.7778/0.6	|27.7778*.6	|[('R.0', 27.7778, u'27.7778', u'27.7778'), ('R.1', 0.6, u'0.6', u'.6')]	|
|1	|20.8/0.6	|20.8*0.6	|[('R.0', 20.8, u'20.8', u'20.8'), ('R.1', 0.6, u'0.6', u'0.6')]	|
|2	|36.6/0.4	|(36.6*.4)	|[('R.0', 36.6, u'36.6', u'36.6'), ('R.1', 0.4, u'0.4', u'.4)')]	|
|3	|27.7778/0.6	|(18+88/9)*0.6	|[('R.0', 27.7778, u'27.7778', u'18+88/9'), ('R.1', 0.6, u'0.6', u'0.6')]	|
|4	|26.2857/0.4	|(2*3.5+5*27/7)*0.4	|[('R.0', 26.2857, u'26.2857', u'2*3.5+5*27/7'), ('R.1', 0.4, u'0.4', u'0.4')]	|
|5	|51.5455/0.2	|5.5*4+(65/11*5)-0.2	|[('R.0', 51.5455, u'51.5455', u'5.5*4+(65/11*5)'), ('R.1', 0.2, u'0.2', u'0.2')]	|
|6	|51.5455/0.2	|5.5*4+(65/11*5)+0.2	|[('R.0', 51.5455, u'51.5455', u'5.5*4+(65/11*5)'), ('R.1', 0.2, u'0.2', u'0.2')]	|
|7	|21.7143/0.2	|(3.5*4 + (6*2/7+15*1/7)*2)*.2	|[('R.0', 21.7143, u'21.7143', u'3.5*4 + (6*2/7+15*1/7)*2'), ('R.1', 0.2, u'0.2', u'.2')]	|
|8	|32.2778/0.5	|((1+2+3+4+5+6+7+8)/8*5 + ((1+2+3+4+5+6+7)/9 +2*8/9)*2)*.5	|[('R.0', 32.2778, u'32.2778', u'(1+2+3+4+5+6+7+8)/8*5 + ((1+2+3+4+5+6+7)/9 +2*8/9)*2'), ('R.1', 0.5, u'0.5', u'.5')]	|
|9	|35.8/0.4	|35.8*0.4	|[('R.0', 35.8, u'35.8', u'35.8'), ('R.1', 0.4, u'0.4', u'0.4')]	|
|10	|37.9445/0.3	|37.9445*0.3	|[('R.0', 37.9445, u'37.9445', u'37.9445'), ('R.1', 0.3, u'0.3', u'0.3')]	|




### (1) Mistake Group Wrong_Sign of size 1




### (56) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:phodgson

	first_attempt
					2015-10-25 22:23:11
	part1_correct_attempt
					['0:00:00', u'(1/8)(1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)']
	part2_correct_attempt
					['0:00:13', u'(1/9)(1 + 2 + 3 + 4 + 5 + 6 + 7) + (2/9)*(8)']
	part3_correct_attempt
					['0:04:24', u'4.5 * 4 + 3*((1/9)(1 + 2 + 3 + 4 + 5 + 6 + 7) + (2/9)*(8))']
	part4_incorrect_attempt
					('23:18:02', u'4.5 * 4 + 3*((1/9)(1 + 2 + 3 + 4 + 5 + 6 + 7) + (2/9)*(8))*.6')
					('23:18:42', u'4.5 * 4 + 3*((1/9)(1 + 2 + 3 + 4 + 5 + 6 + 7) + (2/9)*(8))/.6')
	part4_correct_attempt
					['23:19:03', u'[4.5 * 4 + 3*((1/9)(1 + 2 + 3 + 4 + 5 + 6 + 7) + (2/9)*(8))]/.6']

1 Student ID:h4tu

	first_attempt
					2015-10-28 01:55:23
	part1_correct_attempt
					['0:00:00', u'36/8']
	part2_correct_attempt
					['0:00:47', u'44/9']
	part3_correct_attempt
					['0:01:22', u'4.5*5+44/9*3']
	part4_incorrect_attempt
					('0:02:25', u'4.5*5+44/9*3')
					('0:03:14', u'(36*5+44*3)/(40+27)')
	part4_correct_attempt
					['0:04:32', u'(4.5*5+44/9*3)/0.6']

2 Student ID:jyc018

	first_attempt
					2015-10-28 00:44:32
	part1_correct_attempt
					['0:00:00', u'5']
	part2_correct_attempt
					['0:09:33', u'2/10*9+36/10']
	part3_correct_attempt
					['0:09:55', u'10+10.8']
	part4_incorrect_attempt
					('0:10:28', u'20.8')
	part4_correct_attempt
					['0:13:34', u'20.8/0.6']

3 Student ID:lpettit

	first_attempt
					2015-10-30 22:13:07
	part1_correct_attempt
					['0:00:00', u'11/2']
	part2_correct_attempt
					['0:10:15', u'65/11']
	part3_correct_attempt
					['0:11:06', u'(5.5*3) + ((65/11)*2)']
	part4_incorrect_attempt
					('0:14:42', u'65*2/11')
	part4_correct_attempt
					['0:23:17', u'((5.5*3) + ((65/11)*2))*2']

4 Student ID:dlgoldbe

	first_attempt
					2015-10-30 06:04:54
	part1_correct_attempt
					['0:00:00', u'5']
	part2_correct_attempt
					['11:06:51', u'(1/10)+(2/10)+(3/10)+(4/10)+(5/10)+(6/10)+(7/10)+(8/10)+(18/10)']
	part3_correct_attempt
					['11:07:25', u'25+10.8']
	part4_incorrect_attempt
					('11:25:10', u'3.58')
					('11:27:13', u'5.1/10')
					('11:27:54', u'0.4/5.1')
	part4_correct_attempt
					['12:30:05', u'35.8/0.4']

5 Student ID:mcatozzi

	first_attempt
					2015-10-27 23:03:59
	part1_correct_attempt
					['0:00:00', u'5']
	part2_correct_attempt
					['0:08:38', u'5.4']
	part3_correct_attempt
					['0:09:58', u'31.6']
	part4_incorrect_attempt
					('0:14:42', u'1.66666')
					('0:14:49', u'1.666667')
					('0:25:55', u'1.290994449')
					('2:24:48', u'52.6')
	part4_correct_attempt
					['2:24:52', u'52.666666']

6 Student ID:kbielawi

	first_attempt
					2015-10-26 21:39:28
	part1_correct_attempt
					['0:00:00', u'(1+2+3+4+5+6+7+8+9)/9']
	part2_correct_attempt
					['1 day, 3:17:00', u'(1+2+3+4+5+6+7+8+18)/10']
	part3_correct_attempt
					['1 day, 3:21:35', u'25.8']
	part4_incorrect_attempt
					('1 day, 3:26:08', u'12.9')
	part4_correct_attempt
					['1 day, 3:26:46', u'25.8/0.4']

7 Student ID:jcl084

	first_attempt
					2015-10-28 23:35:47
	part1_correct_attempt
					['0:00:00', u'5']
	part2_correct_attempt
					['0:00:00', u'5.4']
	part3_correct_attempt
					['0:00:00', u'4(5) + 3(5.4)']
	part4_incorrect_attempt
					('0:02:18', u'70.24')
					('0:05:50', u'41.4')
	part4_correct_attempt
					['0:06:25', u'(4(5)+16.2)/0.5']

8 Student ID:abasu

	first_attempt
					2015-10-25 00:35:54
	part1_correct_attempt
					['0:00:00', u'4']
	part2_correct_attempt
					['0:04:01', u'4.375']
	part3_correct_attempt
					['0:06:07', u'33.125']
	part4_incorrect_attempt
					('0:06:42', u'0.2')
					('0:11:04', u'0.6(33.125)')
					('0:11:51', u'0.6/33.125')
	part4_correct_attempt
					['0:11:59', u'33.125/0.6']

9 Student ID:ewbrenna

	first_attempt
					2015-10-30 03:54:42
	part1_correct_attempt
					['0:00:00', u'4.5']
	part2_correct_attempt
					['0:00:00', u'4+(8/9)']
	part3_correct_attempt
					['0:00:37', u'4.5*4+4*2+(8/9)*2']
	part4_incorrect_attempt
					('0:02:42', u'(27+(7/9))')
	part4_correct_attempt
					['0:03:30', u'(27+(7/9))*2']

10 Student ID:qtluong

	first_attempt
					2015-10-29 06:44:55
	part1_correct_attempt
					['0:00:00', u'4']
	part2_correct_attempt
					['0:10:05', u'1/8*21 + 1/4*7']
	part3_correct_attempt
					['0:12:44', u'4*5 + (1/8*21 + 1/4*7)*5']
	part4_incorrect_attempt
					('0:13:38', u'4*5 + (1/8*21 + 1/4*7)*5 / .4')
	part4_correct_attempt
					['0:13:51', u'(4*5 + (1/8*21 + 1/4*7)*5 )/ .4']

11 Student ID:s1powers

	first_attempt
					2015-10-25 21:20:27
	part1_correct_attempt
					['0:00:00', u'4']
	part2_correct_attempt
					['2 days, 2:01:57', u'7*2/8+(6+5+4+3+2+1)*1/8']
	part3_correct_attempt
					['2 days, 2:02:23', u'16+(3*4.375)']
	part4_incorrect_attempt
					('2 days, 2:04:02', u'16+(3*4.375)')
					('2 days, 2:05:34', u'16+(3*4.375)/0.6')
	part4_correct_attempt
					['2 days, 2:05:43', u'[16+(3*4.375)]/0.6']

12 Student ID:e9brown

	first_attempt
					2015-10-27 22:41:51
	part1_correct_attempt
					['0:00:00', u'3.5']
	part2_correct_attempt
					['0:02:46', u'27/7']
	part3_correct_attempt
					['0:02:55', u'3.5*4 + 27*5/7']
	part4_incorrect_attempt
					('0:03:43', u'.3 / (3.5*4 + 27*5/7)')
	part4_correct_attempt
					['0:04:04', u'(3.5*4 + 27*5/7)/.3']

13 Student ID:vsosnovs

	first_attempt
					2015-10-30 05:51:28
	part1_correct_attempt
					['0:00:00', u'(1+2+3+4+5+6+7)1/7']
	part2_correct_attempt
					['0:04:51', u'(1+2+3+4+5+6+7+7)/ 8']
	part3_correct_attempt
					['0:06:03', u'2(4)+ 2(4.375)']
	part4_incorrect_attempt
					('0:07:23', u'.3')
					('0:07:32', u'.2')
					('0:07:35', u'.1')
	part4_correct_attempt
					['0:08:17', u'16.75/.3']

14 Student ID:dkurli

	first_attempt
					2015-10-29 21:58:49
	part1_correct_attempt
					['0:00:00', u'5.5']
	part2_correct_attempt
					['0:08:33', u'2/11*10+45/11']
	part3_correct_attempt
					['0:09:05', u'(5.5+5.91)*3']
	part4_incorrect_attempt
					('0:10:33', u'(5.5+5.91)*3/5')
	part4_correct_attempt
					['0:12:52', u'34.23/.2']

15 Student ID:mbl003

	first_attempt
					2015-10-27 08:34:24
	part1_correct_attempt
					['0:00:00', u'(1+2+3+4+5+6+7+8)/8']
	part2_correct_attempt
					['0:00:16', u'(1+2+3+4+5+6+7+8+8)/9']
	part3_correct_attempt
					['0:03:06', u'((((1+2+3+4+5+6+7+8)/8)*3)+((1+2+3+4+5+6+7+8+8)/9*5))']
	part4_incorrect_attempt
					('0:15:17', u'2.5')
					('0:15:29', u'1/2.5')
	part4_correct_attempt
					['0:16:23', u'((((1+2+3+4+5+6+7+8)/8)*3)+((1+2+3+4+5+6+7+8+8)/9*5))/.4']

16 Student ID:amquinte

	first_attempt
					2015-10-30 17:35:45
	part1_correct_attempt
					['0:00:00', u'5']
	part2_correct_attempt
					['0:13:37', u'5.4']
	part3_correct_attempt
					['0:14:19', u'47']
	part4_incorrect_attempt
					('0:19:54', u'0.4')
					('0:28:36', u'13.5')
					('0:28:47', u'12.5')
	part4_correct_attempt
					['0:29:17', u'117.5']

17 Student ID:haw081

	first_attempt
					2015-10-25 07:40:47
	part1_correct_attempt
					['0:00:00', u'(1/8)(1+2+3+4+5+6+7+8)']
	part2_correct_attempt
					['0:08:41', u'(1/9)(1+2+3+4+5+6+7)+(2/9)(8)']
	part3_correct_attempt
					['0:14:29', u'4.5*3+3*4.88889']
	part4_incorrect_attempt
					('0:17:49', u'4.5*3+3*4.88889/0.4')
	part4_correct_attempt
					['0:18:00', u'(4.5*3+3*4.88889)/0.4']

18 Student ID:dcastlem

	first_attempt
					2015-10-30 19:36:50
	part1_correct_attempt
					['0:00:00', u'36/8']
	part2_correct_attempt
					['0:00:00', u'44/9']
	part3_correct_attempt
					['2:37:19', u'595/18']
	part4_incorrect_attempt
					('2:40:38', u'2975/36')
	part4_correct_attempt
					['2:43:22', u'33.0556/.3']

19 Student ID:dcgriffi

	first_attempt
					2015-10-29 13:29:18
	part1_correct_attempt
					['0:00:00', u'4.5']
	part2_correct_attempt
					['0:00:00', u'44/9']
	part3_correct_attempt
					['0:00:00', u'9+(3*44/9)']
	part4_incorrect_attempt
					('0:02:39', u'2.5/(9+(3*44/9))')
					('0:03:24', u'(9+(3*44/9))/2.5')
	part4_correct_attempt
					['0:04:41', u'(9+(3*44/9))/0.4']

20 Student ID:pvl001

	first_attempt
					2015-10-27 04:14:36
	part1_correct_attempt
					['0:00:00', u'3.5']
	part2_correct_attempt
					['0:00:00', u'27/7']
	part3_correct_attempt
					['0:50:36', u'(3.5 * 5) + (27/7 * 2)']
	part4_incorrect_attempt
					('1:23:51', u'0.1 / ((3.5 * 5) + (27/7 * 2))')
					('1:28:22', u'(3.5 * 5) + (27/7 * 2) / (10 * (3.5 * 5) + (27/7 * 2))')
					('1:32:14', u'(3.5 * 5) + (27/7 * 2) * 10')
	part4_correct_attempt
					['1:32:25', u'((3.5 * 5) + (27/7 * 2)) * 10']

21 Student ID:anl114

	first_attempt
					2015-10-29 20:16:02
	part1_correct_attempt
					['0:00:00', u'5']
	part2_correct_attempt
					['0:00:30', u'5.4']
	part3_correct_attempt
					['0:00:30', u'25+10.8']
	part4_incorrect_attempt
					('0:01:48', u'7.16')
	part4_correct_attempt
					['0:03:02', u'179']

22 Student ID:r9jiang

	first_attempt
					2015-10-24 06:54:45
	part1_correct_attempt
					['0:00:00', u'3.5']
	part2_correct_attempt
					['0:00:00', u'27/7']
	part3_correct_attempt
					['0:00:00', u'14+(54/7)']
	part4_incorrect_attempt
					('0:00:00', u'1250/7')
	part4_correct_attempt
					['0:02:15', u'(14+(54/7))/0.1']

23 Student ID:c2qiu

	first_attempt
					2015-10-29 08:48:14
	part1_correct_attempt
					['0:00:00', u'4']
	part2_correct_attempt
					['0:00:00', u'7/4+21/8']
	part3_correct_attempt
					['0:00:00', u'12+17.5']
	part4_incorrect_attempt
					('0:00:00', u'395/3')
					('0:01:47', u'298/3')
	part4_correct_attempt
					['0:02:09', u'295/3']

24 Student ID:btn023

	first_attempt
					2015-10-30 05:59:26
	part1_correct_attempt
					['0:00:00', u'(1+2+3+4+5+6+7+8)/8']
	part2_correct_attempt
					['0:00:00', u'(1+2+3+4+5+6+7)/9 +2*8/9']
	part3_correct_attempt
					['0:00:48', u'(1+2+3+4+5+6+7+8)/8*5 + ((1+2+3+4+5+6+7)/9 +2*8/9)*2']
	part4_incorrect_attempt
					('1:08:47', u'(1+2+3+4+5+6+7+8)/8*5 + ((1+2+3+4+5+6+7)/9 +2*8/9)*2/.5')
	part4_correct_attempt
					['1:09:06', u'((1+2+3+4+5+6+7+8)/8*5 + ((1+2+3+4+5+6+7)/9 +2*8/9)*2)/.5']

25 Student ID:achinn

	first_attempt
					2015-10-28 03:52:48
	part1_correct_attempt
					['0:00:00', u'4.5']
	part2_correct_attempt
					['0:00:00', u'(1/9*1)+(1/9*2)+(1/9*3)+(1/9*4)+(1/9*5)+(1/9*6)+(1/9*7)+(2/9*8)']
	part3_correct_attempt
					['0:00:00', u'(4.5*4)+(((1/9*1)+(1/9*2)+(1/9*3)+(1/9*4)+(1/9*5)+(1/9*6)+(1/9*7)+(2/9*8))*4)']
	part4_incorrect_attempt
					('4:25:01', u'(4.5*4)+(((1/9*1)+(1/9*2)+(1/9*3)+(1/9*4)+(1/9*5)+(1/9*6)+(1/9*7)+(2/9*8))*4)*0.4')
	part4_correct_attempt
					['4:26:48', u'((4.5*4)+(((1/9*1)+(1/9*2)+(1/9*3)+(1/9*4)+(1/9*5)+(1/9*6)+(1/9*7)+(2/9*8))*4))/0.4']

26 Student ID:galu

	first_attempt
					2015-10-30 23:59:16
	part1_correct_attempt
					['0:00:00', u'36/8']
	part4_incorrect_attempt
					('0:00:00', u'36/8')

27 Student ID:agian

	first_attempt
					2015-10-30 22:21:56
	part1_correct_attempt
					['0:00:00', u'6*(6+1)/(2*6)']
	part2_correct_attempt
					['0:00:49', u'2*6/(6+1)+(6*(6-1))/(2*(6+1))']
	part3_correct_attempt
					['0:06:53', u'5*3.5+2*3.85714']
	part4_incorrect_attempt
					('0:07:14', u'25.2/0.4')
	part4_correct_attempt
					['0:07:24', u'25.2/0.3']

28 Student ID:dgunawan

	first_attempt
					2015-10-29 23:18:18
	part1_correct_attempt
					['0:00:00', u'(1/10)[1+2+3+4+5+6+7+8+9+10]']
	part2_correct_attempt
					['0:02:33', u'(1/11)[1+2+3+4+5+6+7+8+9] + (2/11)[10]']
	part3_correct_attempt
					['0:04:07', u'4*5.5 + 3* 5.90909']
	part4_incorrect_attempt
					('0:05:22', u'0.2')
					('0:16:03', u'1/(1-0.2)')
					('0:16:56', u'39.7273')
					('0:17:18', u'5.5 + 5.90909')

29 Student ID:chc286

	first_attempt
					2015-10-28 06:29:42
	part1_correct_attempt
					['0:00:00', u'5.5']
	part2_correct_attempt
					['0:00:00', u'65/11']
	part3_correct_attempt
					['0:01:12', u'5.5*2+(65/11)*5']
	part4_incorrect_attempt
					('0:02:29', u'(5.5*2+(65/11)*5)/.04')
	part4_correct_attempt
					['0:02:38', u'(5.5*2+(65/11)*5)/0.4']

30 Student ID:aalhaida

	first_attempt
					2015-10-30 22:51:28
	part1_correct_attempt
					['0:00:00', u'4']
	part2_correct_attempt
					['0:19:22', u'4.375']
	part3_correct_attempt
					['0:28:37', u'(4+4+5(4.375))']
	part4_incorrect_attempt
					('0:31:51', u'.4/29.875')
	part4_correct_attempt
					['0:52:39', u'(4+4+5(4.375))/.4']

31 Student ID:hachrist

	first_attempt
					2015-10-29 07:10:55
	part1_correct_attempt
					['0:00:00', u'28/7']
	part2_correct_attempt
					['9:42:26', u'35/8']
	part3_correct_attempt
					['9:42:26', u'4*28/7 + 3*35/8']
	part4_incorrect_attempt
					('9:42:26', u'0.3*(4*28/7 + 3*35/8)')
	part4_correct_attempt
					['9:43:15', u'(4*28/7 + 3*35/8)/0.3']

32 Student ID:jhw015

	first_attempt
					2015-10-27 23:45:45
	part1_correct_attempt
					['0:00:00', u'45/9']
	part2_correct_attempt
					['0:05:09', u'54/10']
	part3_correct_attempt
					['0:07:43', u'(135/9)+(108/10)']
	part4_incorrect_attempt
					('0:15:05', u'(27/2)^1/2')
	part4_correct_attempt
					['2 days, 17:37:05', u'51.6']

33 Student ID:aggouw

	first_attempt
					2015-10-27 03:25:48
	part1_correct_attempt
					['0:00:00', u'7*(7+1)/(2*7)']
	part2_correct_attempt
					['0:00:10', u'2*7/(7+1) + (7*(7-1))/(2*(7+1))']
	part3_correct_attempt
					['0:01:18', u'2*[7*(7+1)/(2*7)] + 5*[2*7/(7+1) + (7*(7-1))/(2*(7+1))]']
	part4_incorrect_attempt
					('0:01:51', u'2*[7*(7+1)/(2*7)] + 5*[2*7/(7+1) + (7*(7-1))/(2*(7+1))]')
					('0:02:09', u'2*[7*(7+1)/(2*7)] + 5*[2*7/(7+1) + (7*(7-1))/(2*(7+1))]/0.2')
					('3 days, 18:58:34', u'(3*[7*(7+1)/(2*7)] + 5*[2*7/(7+1) + (7*(7-1))/(2*(7+1))])/3*[7*(7+1)/(2*7)] + 5*[2*7/(7+1) + (7*(7-1))/(2*(7+1))]')
					('3 days, 18:59:39', u'(3*[7*(7+1)/(2*7)] + 5*[2*7/(7+1) + (7*(7-1))/(2*(7+1))])/0.1')
					('3 days, 19:08:40', u'2*[7*(7+1)/(2*7)] + 5*[2*7/(7+1) + (7*(7-1))/(2*(7+1))] / 0.2')
	part4_correct_attempt
					['3 days, 19:08:55', u'[2*[7*(7+1)/(2*7)] + 5*[2*7/(7+1) + (7*(7-1))/(2*(7+1))]] / 0.2']

34 Student ID:dis003

	first_attempt
					2015-10-29 19:53:53
	part1_correct_attempt
					['0:00:00', u'9*(9+1)/(2*9)']
	part2_correct_attempt
					['0:00:00', u'2*9/(9+1) + (9*(9-1))/(2*(9+1))']
	part3_correct_attempt
					['0:00:31', u'4*(9*(9+1)/(2*9)) + 3*(2*9/(9+1) + (9*(9-1))/(2*(9+1)))']
	part4_incorrect_attempt
					('0:01:09', u'(2*(9*(9+1)/(2*9)) + 2*(2*9/(9+1) + (9*(9-1))/(2*(9+1))))/(9*(9+1)/(2*9))')
					('0:09:40', u'4*(9*(9+1)/(2*9)) + 3*(2*9/(9+1) + (9*(9-1))/(2*(9+1)))/0.3')
					('0:09:59', u'4*(9*(9+1)/(2*9)) + 3*(2*9/(9+1) + (9*(9-1))/(2*(9+1)))/9*(9+1)/(2*9)')
					('0:10:11', u'4*(9*(9+1)/(2*9)) + 3*(2*9/(9+1) + (9*(9-1))/(2*(9+1)))/(9*(9+1)/(2*9))')
					('0:12:58', u'4*(9*(9+1)/(2*9)) + 3*(2*9/(9+1) + (9*(9-1))/(2*(9+1)))/(4*(9*(9+1)/(2*9)) + 3*(2*9/(9+1) + (9*(9-1))/(2*(9+1))))')
	part4_correct_attempt
					['0:16:19', u'(4*(9*(9+1)/(2*9)) + 3*(2*9/(9+1) + (9*(9-1))/(2*(9+1))))/0.3']

35 Student ID:tcuddy

	first_attempt
					2015-10-23 23:57:16
	part1_correct_attempt
					['0:00:00', u'(1/9)(9(10)/2)']
	part2_correct_attempt
					['0:31:10', u'(1/10)(36)+(2/10)9']
	part3_correct_attempt
					['16:40:22', u'5(5) + 5(5.4)']
	part4_incorrect_attempt
					('16:40:22', u'.6(52)')
	part4_correct_attempt
					['16:40:33', u'(52)/.6']

36 Student ID:dando

	first_attempt
					2015-10-29 00:45:03
	part1_correct_attempt
					['0:00:00', u'5.5']
	part2_correct_attempt
					['0:18:21', u'1/11 + 2/11 + 3/11 + 4 /11 + 5/11 + 6/11 + 7/11 + 8/11 + 9/11 + 20/11']
	part3_correct_attempt
					['0:19:49', u'11 + 5 * 65/11']
	part4_incorrect_attempt
					('0:26:41', u'5.5')
					('0:27:16', u'65/11')
					('0:27:24', u'5.5')
					('15:03:30', u'27.5')
					('15:10:02', u'40.5455')
					('15:10:13', u'5.90909')
	part4_correct_attempt
					['15:14:15', u'5 * (11 + 5 * 65/11)']

37 Student ID:edescobe

	first_attempt
					2015-10-28 19:47:31
	part1_correct_attempt
					['0:00:00', u'5.5']
	part2_correct_attempt
					['0:02:37', u'5.909']
	part3_correct_attempt
					['0:03:06', u'5.5*4+5.909*3']
	part4_incorrect_attempt
					('0:03:50', u'.4')
	part4_correct_attempt
					['0:06:54', u'39.727/.6']

38 Student ID:srl006

	first_attempt
					2015-10-30 00:11:56
	part1_correct_attempt
					['0:00:00', u'5.5']
	part2_correct_attempt
					['0:10:06', u'5.909090909']
	part3_correct_attempt
					['0:11:03', u'33.818']
	part4_incorrect_attempt
					('0:11:41', u'6.76')
					('0:11:56', u'6.7636')
	part4_correct_attempt
					['0:15:23', u'169.09']

39 Student ID:bakang

	first_attempt
					2015-10-26 21:44:29
	part1_correct_attempt
					['0:00:00', u'36/8']
	part2_correct_attempt
					['0:00:50', u'(28+8*2)/9']
	part3_correct_attempt
					['0:01:59', u'2*(36/8)+5*((28+8*2)/9)']
	part4_incorrect_attempt
					('0:03:04', u'(2*(36/8)+5*((28+8*2)/9))/4')
	part4_correct_attempt
					['0:03:11', u'(2*(36/8)+5*((28+8*2)/9))/0.4']

40 Student ID:smohiman

	first_attempt
					2015-10-27 05:44:52
	part1_correct_attempt
					['0:00:00', u'4']
	part2_correct_attempt
					['0:00:00', u'35/8']
	part3_correct_attempt
					['0:00:00', u'(2*4)+(3*35/8)']
	part4_incorrect_attempt
					('0:04:30', u'0.4/((2*4)+(3*35/8))')
	part4_correct_attempt
					['0:05:34', u'((2*4)+(3*35/8))/0.4']

41 Student ID:dpereira

	first_attempt
					2015-10-23 18:09:24
	part1_correct_attempt
					['0:00:00', u'1/9 + 2/9 + 3/9 + 4/9 + 5/9 + 6/9 + 7/9 + 8/9 + 9/9']
	part2_correct_attempt
					['0:01:05', u'1/10 + 2/10 + 3/10 + 4/10 + 5/10 + 6/10 + 7/10 + 8/10 + 18/10']
	part3_correct_attempt
					['0:01:35', u'5*4 + (5.4 * 4)']
	part4_incorrect_attempt
					('0:04:38', u'5*4 + (5.4 * 4) / .2')
	part4_correct_attempt
					['0:04:47', u'(5*4 + (5.4 * 4)) / .2']

42 Student ID:flhernan

	first_attempt
					2015-10-26 04:31:48
	part1_correct_attempt
					['0:00:00', u'3.5']
	part2_correct_attempt
					['0:04:55', u'3.85714286']
	part3_correct_attempt
					['0:08:27', u'3*3.5 + 2*3.85714286']
	part4_incorrect_attempt
					('0:09:26', u'.1/(3*3.5 + 2*3.85714286)')
					('0:09:40', u'.1*(3*3.5 + 2*3.85714286)')
	part4_correct_attempt
					['0:11:10', u'(3*3.5 + 2*3.85714286)/(.1)']

43 Student ID:yos017

	first_attempt
					2015-10-29 06:07:42
	part1_correct_attempt
					['0:00:00', u'(1+2+3+4+5+6+7+8+9+10)/10']
	part2_correct_attempt
					['0:01:18', u'(1+2+3+4+5+6+7+8+9+20)/11']
	part3_correct_attempt
					['0:03:11', u'4*[(1+2+3+4+5+6+7+8+9+10)/10]+5*[(1+2+3+4+5+6+7+8+9+20)/11]']
	part4_incorrect_attempt
					('0:16:53', u'4*[(1+2+3+4+5+6+7+8+9+10)/10]+5*[(1+2+3+4+5+6+7+8+9+20)/11]/0.4')
	part4_correct_attempt
					['0:17:13', u'[4*[(1+2+3+4+5+6+7+8+9+10)/10]+5*[(1+2+3+4+5+6+7+8+9+20)/11]]/0.4']

44 Student ID:xil109

	first_attempt
					2015-10-26 20:29:35
	part1_correct_attempt
					['0:00:00', u'3.5']
	part2_correct_attempt
					['0:02:46', u'3.86']
	part3_correct_attempt
					['0:03:24', u'22.08']
	part4_incorrect_attempt
					('0:05:15', u'45.6')
	part4_correct_attempt
					['0:05:31', u'22.08*2']

45 Student ID:awollner

	first_attempt
					2015-10-27 03:27:11
	part1_correct_attempt
					['0:00:00', u'1/10(1+2+3+4+5+6+7+8+9+10)']
	part2_correct_attempt
					['0:02:19', u'1/11(1+2+3+4+5+6+7+8+9) +2/11(10)']
	part3_correct_attempt
					['0:03:10', u'11 + 4*(5.90909)']
	part4_incorrect_attempt
					('0:05:53', u'1/10^6')
	part4_correct_attempt
					['3 days, 7:59:56', u'34.6364/.5']

46 Student ID:yig015

	first_attempt
					2015-10-28 09:52:57
	part1_correct_attempt
					['0:00:00', u'5.5']
	part2_correct_attempt
					['1 day, 23:45:13', u'65/11']
	part3_correct_attempt
					['1 day, 23:45:33', u'5*5.5+5*65/11']
	part4_incorrect_attempt
					('1 day, 23:48:21', u'1.5811')
					('1 day, 23:49:58', u'1.003')
					('1 day, 23:50:05', u'1.00301')
	part4_correct_attempt
					['2 days, 0:02:47', u'57.0455/0.6']

47 Student ID:vasharma

	first_attempt
					2015-10-30 23:21:37
	part1_correct_attempt
					['0:00:00', u'3.5']
	part2_correct_attempt
					['0:12:21', u'3.86']
	part3_correct_attempt
					['0:13:53', u'3(3.86)+4(3.5)']
	part4_incorrect_attempt
					('0:30:28', u'(4*5.5)+4*5.90909')
	part4_correct_attempt
					['0:34:36', u'(4(3.5)+ 3(3.86))/0.6']

48 Student ID:ytc012

	first_attempt
					2015-10-29 11:34:57
	part1_correct_attempt
					['0:00:00', u'(8+7+6+5+4+3+2+1)/8']
	part2_correct_attempt
					['0:04:38', u'(16+7+6+5+4+3+2+1)/9']
	part3_correct_attempt
					['0:08:06', u'5(8+7+6+5+4+3+2+1)/8+3(16+7+6+5+4+3+2+1)/9']
	part4_incorrect_attempt
					('0:13:26', u'16+7+6+5+4+3+2+19')
					('0:13:37', u'(8+7+6+5+4+3+2+1)/8')
					('0:13:45', u'(16+7+6+5+4+3+2+1)/9')
	part4_correct_attempt
					['0:17:47', u'2(5(8+7+6+5+4+3+2+1)/8+3(16+7+6+5+4+3+2+1)/9)']

49 Student ID:volim

	first_attempt
					2015-10-28 05:35:30
	part1_correct_attempt
					['0:00:00', u'(1+2+3+4+5+6+7+8+9)/9']
	part2_correct_attempt
					['0:00:49', u'(1+2+3+4+5+6+7+8+9+9)/10']
	part3_correct_attempt
					['0:02:21', u'15+(4*5.4)']
	part4_incorrect_attempt
					('0:07:22', u'.4/36.6')
	part4_correct_attempt
					['0:07:41', u'36.6/.4']

50 Student ID:c3chung

	first_attempt
					2015-10-29 01:33:48
	part1_correct_attempt
					['0:00:00', u'1(1/8)+2(1/8)+3(1/8)+4(1/8)+5(1/8)+6(1/8)+7(1/8)+8(1/8)']
	part2_correct_attempt
					['0:02:27', u'1(1/9)+2(1/9)+3(1/9)+4(1/9)+5(1/9)+6(1/9)+7(1/9)+8(2/9)']
	part3_correct_attempt
					['0:03:07', u'4.5(3)+4.88889(5)']
	part4_incorrect_attempt
					('0:03:33', u'4.5')
	part4_correct_attempt
					['1 day, 11:33:53', u'2(4.5(3)+4.88889(5))']

51 Student ID:d6he

	first_attempt
					2015-10-28 19:22:34
	part1_correct_attempt
					['0:00:00', u'36/8']
	part2_correct_attempt
					['0:01:51', u'44/9']
	part3_correct_attempt
					['0:04:27', u'18+88/9']
	part4_incorrect_attempt
					('0:10:17', u'16.66668')
	part4_correct_attempt
					['0:13:12', u'(18+88/9)/0.6']

52 Student ID:r2fisher

	first_attempt
					2015-10-26 22:51:06
	part1_correct_attempt
					['0:00:00', u'36/8']
	part2_correct_attempt
					['0:03:05', u'(8*2 +7+6+5+4+3+2+1)/9']
	part3_correct_attempt
					['0:03:55', u'4.5*4 + ((8*2 +7+6+5+4+3+2+1)/9)*4']
	part4_incorrect_attempt
					('0:05:09', u'36/8+ (8*2 +7+6+5+4+3+2+1)/9')
	part4_correct_attempt
					['0:13:31', u'(4.5*4 + ((8*2 +7+6+5+4+3+2+1)/9)*4)/0.2']

53 Student ID:cagatep

	first_attempt
					2015-10-30 20:53:13
	part1_correct_attempt
					['0:00:00', u'4']
	part2_correct_attempt
					['0:00:00', u'4.375']
	part3_correct_attempt
					['0:00:00', u'12 + 3*4.375']
	part4_incorrect_attempt
					('0:02:37', u'4+4.375')
	part4_correct_attempt
					['0:03:44', u'(12 + 3*4.375)/.2']

54 Student ID:hmnaing

	first_attempt
					2015-10-30 07:48:22
	part1_correct_attempt
					['0:00:00', u'36/8']
	part2_correct_attempt
					['0:10:30', u'(28+16)/9']
	part3_correct_attempt
					['0:11:44', u'5*36/8 +2*(28+16)/9']
	part4_incorrect_attempt
					('0:12:40', u'0.6')
	part4_correct_attempt
					['0:13:08', u'(5*36/8 +2*(28+16)/9 )/0.6']

55 Student ID:tjke

	first_attempt
					2015-10-30 22:57:35
	part1_correct_attempt
					['0:00:00', u'1*1/7+2*1/7+3*1/7+4*1/7+5*1/7+6*1/7+7*1/7']
	part2_correct_attempt
					['0:00:00', u'7*2/8+6*1/8+5*1/8+4*1/8+3*1/8+2*1/8+1*1/8']
	part3_correct_attempt
					['0:01:09', u'[1*1/7+2*1/7+3*1/7+4*1/7+5*1/7+6*1/7+7*1/7]*4+[7*2/8+6*1/8+5*1/8+4*1/8+3*1/8+2*1/8+1*1/8]*2']
	part4_incorrect_attempt
					('0:05:32', u'[1*1/7+2*1/7+3*1/7+4*1/7+5*1/7+6*1/7+7*1/7]*4+[7*2/8+6*1/8+5*1/8+4*1/8+3*1/8+2*1/8+1*1/8]*2/0.1')
	part4_correct_attempt
					['0:05:52', u'([1*1/7+2*1/7+3*1/7+4*1/7+5*1/7+6*1/7+7*1/7]*4+[7*2/8+6*1/8+5*1/8+4*1/8+3*1/8+2*1/8+1*1/8]*2)/0.1']












