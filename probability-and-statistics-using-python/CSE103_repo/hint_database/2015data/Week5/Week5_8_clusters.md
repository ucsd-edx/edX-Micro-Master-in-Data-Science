#Problem 8

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




## Part 1

### (36) Mistake Group Digits of size 36




### (3) Mistake Group ['R.0'] of size 3
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|1/16+2/16+1/16	|1/16+2/16+3/16	|[('R.0', 0.1875, u'1/16+2/16', u'1/16+2/16')]	|
|1	|1/16+2/16+1/16	|(1/16)+(2/16)+(3/16)	|[('R.0', 0.1875, u'1/16+2/16', u'(1/16)+(2/16)')]	|




### (1) Mistake Group ['R.0.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|1/16+2/16+1/16	|1/16*(2/16)*(1/16)	|[('R.0.1', 0.125, u'2/16', u'2/16')]	|




### (1) Mistake Group ['R.0.0.0'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|1/16+2/16+1/16	|(1+2+3)/16	|[('R.0.0.0', 1.0, u'1', u'1')]	|




### (51) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:b3hwang

	first_attempt
					2015-10-28 02:11:28
	part1_incorrect_attempt
					('0:00:00', u'1/16')
	part1_correct_attempt
					['0:55:12', u'4/16']

1 Student ID:rwthomps

	first_attempt
					2015-10-30 20:39:16
	part1_incorrect_attempt
					('0:00:00', u'3/16')
	part1_correct_attempt
					['0:00:50', u'4/16']

2 Student ID:agoldsht

	first_attempt
					2015-10-29 05:18:45
	part1_incorrect_attempt
					('0:00:00', u'3/6')
					('0:00:14', u'4/6')
	part1_correct_attempt
					['0:00:25', u'4/16']

3 Student ID:galu

	first_attempt
					2015-10-30 23:48:58
	part1_incorrect_attempt
					('0:00:00', u'1/16')
					('0:02:07', u'2/16')
	part1_correct_attempt
					['0:02:41', u'4/16']

4 Student ID:t2shin

	first_attempt
					2015-10-28 00:26:24
	part1_incorrect_attempt
					('0:00:00', u'1/16')
	part1_correct_attempt
					['0:00:59', u'1/4']

5 Student ID:kbielawi

	first_attempt
					2015-10-26 22:06:45
	part1_incorrect_attempt
					('0:00:00', u'1/16')
	part1_correct_attempt
					['1 day, 1:38:43', u'4/16']

6 Student ID:glcohen

	first_attempt
					2015-10-27 15:50:27
	part1_incorrect_attempt
					('0:00:00', u'1/16')
	part1_correct_attempt
					['0:00:59', u'4/16']

7 Student ID:achava

	first_attempt
					2015-10-28 08:03:04
	part1_incorrect_attempt
					('0:00:00', u'1/16')
	part1_correct_attempt
					['0:00:56', u'1/16+(2/16)+(1/16)']

8 Student ID:d6he

	first_attempt
					2015-10-28 20:30:02
	part1_incorrect_attempt
					('0:00:00', u'1/16')
	part1_correct_attempt
					['0:00:45', u'4/16']

9 Student ID:spw006

	first_attempt
					2015-10-28 00:27:46
	part1_incorrect_attempt
					('0:00:00', u'1/16')
					('0:00:05', u'15/16')
	part1_correct_attempt
					['1:11:55', u'1/4']

10 Student ID:any027

	first_attempt
					2015-10-26 04:57:27
	part1_incorrect_attempt
					('0:00:00', u'1/16')
	part1_correct_attempt
					['0:00:22', u'(1/16) + (2/16) + (1/16)']

11 Student ID:anislam

	first_attempt
					2015-10-29 23:28:22
	part1_incorrect_attempt
					('0:00:00', u'1/4 + 1 + 3/4')
					('0:01:29', u'1/4 + 1 + 3/4')
	part1_correct_attempt
					['0:01:51', u'1/4']

12 Student ID:s1powers

	first_attempt
					2015-10-27 23:37:28
	part1_incorrect_attempt
					('0:00:00', u'1/16')
	part1_correct_attempt
					['0:01:06', u'1/4']

13 Student ID:kthui

	first_attempt
					2015-10-25 02:49:21
	part1_incorrect_attempt
					('0:00:00', u'1/16')
	part1_correct_attempt
					['0:02:39', u'4/16']

14 Student ID:mroknich

	first_attempt
					2015-10-26 04:35:52
	part1_incorrect_attempt
					('0:00:00', u'1/16')
	part1_correct_attempt
					['0:02:04', u'4/16']

15 Student ID:vsosnovs

	first_attempt
					2015-10-30 06:17:07
	part1_incorrect_attempt
					('0:00:00', u'2/16')
					('0:00:07', u'1/16')
	part1_correct_attempt
					['0:00:13', u'4/16']

16 Student ID:dkurli

	first_attempt
					2015-10-29 22:41:37
	part1_incorrect_attempt
					('0:00:00', u'1/16')
	part1_correct_attempt
					['0:01:34', u'1/4']

17 Student ID:srl006

	first_attempt
					2015-10-30 00:34:42
	part1_incorrect_attempt
					('0:00:00', u'.5')
	part1_correct_attempt
					['0:00:27', u'.25']

18 Student ID:jag028

	first_attempt
					2015-10-30 14:20:22
	part1_incorrect_attempt
					('0:00:00', u'1/16')
	part1_correct_attempt
					['0:00:29', u'1/4']

19 Student ID:s2chaudh

	first_attempt
					2015-10-29 02:34:57
	part1_incorrect_attempt
					('0:00:00', u'.5')
	part1_correct_attempt
					['0:00:49', u'1/4']

20 Student ID:dcrume

	first_attempt
					2015-10-28 20:30:10
	part1_incorrect_attempt
					('0:00:00', u'3/16')
	part1_correct_attempt
					['0:01:02', u'4/16']

21 Student ID:ksmurlo

	first_attempt
					2015-10-27 07:22:14
	part1_incorrect_attempt
					('0:00:00', u'(4/3)/16')
	part1_correct_attempt
					['0:00:21', u'4/16']

22 Student ID:ctroncos

	first_attempt
					2015-10-29 16:21:35
	part1_incorrect_attempt
					('0:00:00', u'1/16')
	part1_correct_attempt
					['0:01:26', u'(2/16)*2']

23 Student ID:jew037

	first_attempt
					2015-10-28 18:38:49
	part1_incorrect_attempt
					('0:00:00', u'1/16')
	part1_correct_attempt
					['0:01:05', u'(1/16 + 2/16 + 1/16)']

24 Student ID:cfgutier

	first_attempt
					2015-10-29 18:52:55
	part1_incorrect_attempt
					('0:00:00', u'1/16')
	part1_correct_attempt
					['7:17:16', u'4/16']

25 Student ID:anl114

	first_attempt
					2015-10-30 21:45:22
	part1_incorrect_attempt
					('0:00:00', u'1/16')
	part1_correct_attempt
					['0:00:13', u'4/16']

26 Student ID:jnatale

	first_attempt
					2015-10-26 05:27:42
	part1_incorrect_attempt
					('0:00:00', u'1/16')
	part1_correct_attempt
					['0:03:04', u'(1/16) + (1/8) + (1/16)']

27 Student ID:aordookh

	first_attempt
					2015-10-29 03:13:47
	part1_incorrect_attempt
					('0:00:00', u'1/16')
	part1_correct_attempt
					['0:05:56', u'4/16']

28 Student ID:avasavad

	first_attempt
					2015-10-27 23:28:57
	part1_incorrect_attempt
					('0:00:00', u'1/16')
					('0:02:23', u'1/16 * 1/16')
					('0:02:41', u'1/(16*16)')
	part1_correct_attempt
					['5:01:14', u'1/4']

29 Student ID:lalacson

	first_attempt
					2015-10-29 04:43:36
	part1_incorrect_attempt
					('0:00:00', u'1/16')
	part1_correct_attempt
					['0:01:19', u'4/16']

30 Student ID:jap009

	first_attempt
					2015-10-30 10:50:36
	part1_incorrect_attempt
					('0:00:00', u'3/16')
	part1_correct_attempt
					['0:00:20', u'4/16']

31 Student ID:dgunawan

	first_attempt
					2015-10-29 23:46:30
	part1_incorrect_attempt
					('0:00:00', u'1/16')
	part1_correct_attempt
					['0:00:22', u'4/16']

32 Student ID:atorr

	first_attempt
					2015-10-29 06:56:29
	part1_incorrect_attempt
					('0:00:00', u'1/16')
	part1_correct_attempt
					['0:00:30', u'1/4']

33 Student ID:rraiyyan

	first_attempt
					2015-10-28 01:02:31
	part1_incorrect_attempt
					('0:00:00', u'1/16')
					('0:05:35', u'1/16')
	part1_correct_attempt
					['0:05:55', u'1/4']

34 Student ID:r1gu

	first_attempt
					2015-10-30 09:14:02
	part1_incorrect_attempt
					('0:00:00', u'1/16')
	part1_correct_attempt
					['0:03:06', u'4/16']

35 Student ID:tcn013

	first_attempt
					2015-10-27 00:44:16
	part1_incorrect_attempt
					('0:00:00', u'1/16')
					('0:05:08', u'4/(16*3)')
	part1_correct_attempt
					['0:05:54', u'1/4']

36 Student ID:haliew

	first_attempt
					2015-10-29 02:14:08
	part1_incorrect_attempt
					('0:00:00', u'3/16')
	part1_correct_attempt
					['0:00:24', u'4/16']

37 Student ID:jel075

	first_attempt
					2015-10-29 02:12:00
	part1_incorrect_attempt
					('0:00:00', u'1/12')
	part1_correct_attempt
					['0:00:32', u'1/4']

38 Student ID:abasu

	first_attempt
					2015-10-25 01:09:30
	part1_incorrect_attempt
					('0:00:00', u'1/16')
					('0:01:23', u'3/16')
	part1_correct_attempt
					['0:02:45', u'4/16']

39 Student ID:c1sorian

	first_attempt
					2015-10-28 22:00:19
	part1_incorrect_attempt
					('0:00:00', u'1/16')
	part1_correct_attempt
					['0:01:02', u'4/16']

40 Student ID:dtea

	first_attempt
					2015-10-30 23:56:34
	part1_incorrect_attempt
					('0:00:00', u'1/16')
	part1_correct_attempt
					['0:00:08', u'4/16']

41 Student ID:csl030

	first_attempt
					2015-10-29 23:45:36
	part1_incorrect_attempt
					('0:00:00', u'1/16^2')
	part1_correct_attempt
					['0:02:26', u'4/16']

42 Student ID:aurodrig

	first_attempt
					2015-10-30 05:11:43
	part1_incorrect_attempt
					('0:00:00', u'1/16')
	part1_correct_attempt
					['0:04:28', u'4/16']

43 Student ID:starinia

	first_attempt
					2015-10-29 20:46:36
	part1_incorrect_attempt
					('0:00:00', u'1/16')
	part1_correct_attempt
					['0:10:18', u'4/16']

44 Student ID:bpandayk

	first_attempt
					2015-10-30 17:56:13
	part1_incorrect_attempt
					('0:00:00', u'1/16')
	part1_correct_attempt
					['0:02:20', u'4/16']

45 Student ID:s6deng

	first_attempt
					2015-10-30 06:59:14
	part1_incorrect_attempt
					('0:00:00', u'1/16')
					('0:00:58', u'2/3')
					('0:01:04', u'1/3')
					('0:04:04', u'1/2')
	part1_correct_attempt
					['0:07:00', u'4/16']

46 Student ID:amquinte

	first_attempt
					2015-10-30 19:22:49
	part1_incorrect_attempt
					('0:00:00', u'1/16')
	part1_correct_attempt
					['0:13:18', u'4/16']

47 Student ID:qtluong

	first_attempt
					2015-10-29 07:37:30
	part1_incorrect_attempt
					('0:00:00', u'1/3')
	part1_correct_attempt
					['0:00:29', u'1/4']

48 Student ID:ralhadda

	first_attempt
					2015-10-24 04:46:25
	part1_incorrect_attempt
					('0:00:00', u'1/16')
	part1_correct_attempt
					['0:02:01', u'4/16']

49 Student ID:small

	first_attempt
					2015-10-30 23:41:10
	part1_incorrect_attempt
					('0:00:00', u'1/16')
	part1_correct_attempt
					['0:06:31', u'1/4']

50 Student ID:mtrafeca

	first_attempt
					2015-10-25 06:50:00
	part1_incorrect_attempt
					('0:00:00', u'1/16')
	part1_correct_attempt
					['0:00:47', u'1/4']












## Part 10

### (35) Mistake Group Fraction of size 35




### (20) Mistake Group Digits of size 20




### (3) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:ggaddi

	first_attempt
					2015-10-27 15:37:26
	part1_correct_attempt
					['0:00:00', u'(1+2+1)/16']
	part2_correct_attempt
					['0:00:00', u'(2+4+2)/16']
	part3_correct_attempt
					['0:00:00', u'(1+2+1)/16']
	part4_correct_attempt
					['0:00:00', u'(1+2+1)/16']
	part5_correct_attempt
					['0:00:00', u'(2+4+2)/16']
	part6_correct_attempt
					['0:00:00', u'(1+2+1)/16']
	part7_correct_attempt
					['0:00:00', u'1']
	part8_correct_attempt
					['0:00:00', u'1']
	part10_incorrect_attempt
					('0:00:00', u'(1+2+1)/16+(2+4+2)/16+(1+2+1)/16')
	part10_correct_attempt
					['0:01:05', u'1*(1+2+1)/16+2*(2+4+2)/16+3*(1+2+1)/16']

1 Student ID:starinia

	first_attempt
					2015-10-29 20:56:54
	part1_correct_attempt
					['0:00:00', u'4/16']
	part2_correct_attempt
					['0:00:00', u'8/16']
	part3_correct_attempt
					['0:00:00', u'4/16']
	part4_correct_attempt
					['0:00:00', u'4/16']
	part5_correct_attempt
					['0:00:00', u'8/16']
	part6_correct_attempt
					['0:00:00', u'4/16']
	part7_correct_attempt
					['-1 day, 23:49:42', u'1']
	part8_correct_attempt
					['-1 day, 23:49:42', u'1']
	part10_incorrect_attempt
					('0:00:00', u'4/16 + 8/16 + 4/16')
	part10_correct_attempt
					['5:25:51', u'1/16 + 2/16+1/16 + 4/16+ 8/16+4/16+3/16+ 6/16+3/16']

2 Student ID:hachrist

	first_attempt
					2015-10-26 01:47:33
	part1_correct_attempt
					['0:00:00', u'4/16']
	part2_correct_attempt
					['0:01:07', u'8/16']
	part3_correct_attempt
					['0:01:07', u'4/16']
	part4_correct_attempt
					['0:01:07', u'4/16']
	part5_correct_attempt
					['0:01:07', u'8/16']
	part6_correct_attempt
					['0:01:07', u'4/16 ']
	part7_correct_attempt
					['0:01:07', u'1']
	part8_correct_attempt
					['0:01:07', u'1']
	part10_incorrect_attempt
					('0:04:35', u'4/16 + 8/16 + 4/16')
	part10_correct_attempt
					['0:13:02', u'2']












## Part 11

### (26) Mistake Group Fraction of size 26




### (25) Mistake Group Digits of size 25




### (6) Mistake Group redirect of size 6




### (2) Mistake Group ['R.0.0.0.1'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|1*(1/16+2/16+1/16)+2*(2/16+4/16+2/16)+3*(1/16+2/16+1/16)+1*(1/16+2/16+1/16)+2*(2/16+4/16+2/16)+3*(1/16+2/16+1/16)	|1*1/16+2*2/16+3*1/16+4*2/16+5*4/16+6*2/16+7*1/16+8*2/16+9*1/16	|[('R.0.0.0.1', 0.75, u'3*(1/16+2/16+1/16)', u'6*2/16')]	|
|1	|1*(1/16+2/16+1/16)+2*(2/16+4/16+2/16)+3*(1/16+2/16+1/16)+1*(1/16+2/16+1/16)+2*(2/16+4/16+2/16)+3*(1/16+2/16+1/16)	|(1/16)+(4/16)+(3/16)+(8/16)+(20/16)+(12/16)+(7/16)+(1)+(9/16)	|[('R.0.0.0.1', 0.75, u'3*(1/16+2/16+1/16)', u'12/16')]	|




### (3) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:bkoli

	first_attempt
					2015-10-27 05:48:38
	part1_correct_attempt
					['0:00:00', u'1/16+2/16+1/16']
	part2_correct_attempt
					['0:00:16', u'2/16+4/16+2/16']
	part3_correct_attempt
					['0:00:29', u'1/16+2/16+1/16']
	part4_correct_attempt
					['0:00:42', u'1/16+2/16+1/16']
	part5_correct_attempt
					['0:00:53', u'2/16+4/16+2/16']
	part6_correct_attempt
					['0:01:05', u'1/16+2/16+1/16']
	part7_correct_attempt
					['0:01:25', u'1']
	part8_correct_attempt
					['0:01:25', u'1']
	part9_correct_attempt
					['0:01:25', u'1*(1/16+2/16+1/16)+2*(2/16+4/16+2/16)+3*(1/16+2/16+1/16)']
	part10_correct_attempt
					['0:01:44', u'1*(1/16+2/16+1/16)+2*(2/16+4/16+2/16)+3*(1/16+2/16+1/16)']
	part11_incorrect_attempt
					('0:03:04', u'1*(1/16+2/16+1/16)+2*(2/16+4/16+2/16)+3*(1/16+2/16+1/16)+1')
	part11_correct_attempt
					['0:05:02', u'2*(1*(1/16+2/16+1/16)+2*(2/16+4/16+2/16)+3*(1/16+2/16+1/16))']

1 Student ID:agian

	first_attempt
					2015-10-30 22:32:56
	part1_correct_attempt
					['0:00:00', u'1/16+2/16+1/16']
	part2_correct_attempt
					['0:00:28', u'2/16+4/16+2/16']
	part3_correct_attempt
					['0:00:40', u'1/16+2/16+1/16']
	part4_correct_attempt
					['0:00:52', u'1/16+2/16+1/16']
	part5_correct_attempt
					['0:00:52', u'2/16+4/16+2/16']
	part6_correct_attempt
					['0:00:52', u'1/16+2/16+1/16']
	part7_correct_attempt
					['0:01:04', u'1']
	part8_correct_attempt
					['0:01:04', u'1']
	part9_correct_attempt
					['0:02:28', u'(1/16+2/16+1/16)+2(2/16+4/16+2/16)+3(1/16+2/16+1/16)']
	part10_correct_attempt
					['0:02:33', u'(1/16+2/16+1/16)+2(2/16+4/16+2/16)+3(1/16+2/16+1/16)']
	part11_incorrect_attempt
					('0:04:52', u'1/16+4/16+3/16 + 2/16+8/16+6/16 + 1/16+4/16+3/16')
	part11_correct_attempt
					['0:06:43', u'4']

2 Student ID:aggouw

	first_attempt
					2015-10-27 03:29:36
	part1_correct_attempt
					['0:00:00', u'4/16']
	part2_correct_attempt
					['0:00:09', u'8/16']
	part3_correct_attempt
					['0:00:24', u'4/16']
	part4_correct_attempt
					['0:00:30', u'4/16']
	part5_correct_attempt
					['0:00:40', u'8/16']
	part6_correct_attempt
					['0:00:55', u'4/16']
	part7_correct_attempt
					['0:00:59', u'1']
	part8_correct_attempt
					['0:01:03', u'1']
	part9_correct_attempt
					['0:01:12', u'(1*(4/16))+(2*(8/16))+(3*(4/16))']
	part10_correct_attempt
					['0:01:22', u'(1*(4/16))+(2*(8/16))+(3*(4/16))']
	part11_incorrect_attempt
					('0:02:06', u'1*(1/16+2/16+1/16)+2*(2/16+4/16+2/16)+3*(1/16+2/16+1/16)+1')
	part11_correct_attempt
					['3 days, 18:45:54', u'1*(1/16+2/16+1/16)+2*(2/16+4/16+2/16)+3*(1/16+2/16+1/16) + 1*(1/16+2/16+1/16)+2*(2/16+4/16+2/16)+3*(1/16+2/16+1/16)']












## Part 12

### (45) Mistake Group Fraction of size 45




### (29) Mistake Group Digits of size 29




### (1) Mistake Group redirect of size 1




### (1) Mistake Group Wrong_Sign of size 1




### (1) Mistake Group ['R.0.0.0.0.0.0', 'R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0.0.0.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|1*1/16+2*2/16+3*1/16+2*2/16+4*4/16+6*2/16+3*1/16+6*2/16+9*1/16	|(1/16)+2*(2/16)+3*(1/16)+4*(2/16)+5*(4/16)+6*(2/16)+7*(1/16)+8*(2/16)+9*(1/16)	|[('R.0.0.0.0.0.0', 0.5, u'1*1/16+2*2/16+3*1/16', u'(1/16)+2*(2/16)+3*(1/16)'), ('R.1', 0.5625, u'9*1/16', u'9*(1/16)')]	|




### (8) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:muy002

	first_attempt
					2015-10-28 03:14:24
	part1_correct_attempt
					['0:00:00', u'4/16']
	part2_correct_attempt
					['0:00:00', u'8/16']
	part3_correct_attempt
					['0:00:00', u'4/16']
	part4_correct_attempt
					['0:00:00', u'4/16']
	part5_correct_attempt
					['0:00:00', u'8/16']
	part6_correct_attempt
					['0:00:00', u'4/16']
	part7_correct_attempt
					['0:00:11', u'1']
	part8_correct_attempt
					['0:00:00', u'1']
	part12_incorrect_attempt
					('0:30:17', u'64/4')
	part12_correct_attempt
					['0:31:41', u'64/16']

1 Student ID:hachrist

	first_attempt
					2015-10-26 01:47:33
	part1_correct_attempt
					['0:00:00', u'4/16']
	part2_correct_attempt
					['0:01:07', u'8/16']
	part3_correct_attempt
					['0:01:07', u'4/16']
	part4_correct_attempt
					['0:01:07', u'4/16']
	part5_correct_attempt
					['0:01:07', u'8/16']
	part6_correct_attempt
					['0:01:07', u'4/16 ']
	part7_correct_attempt
					['0:01:07', u'1']
	part8_correct_attempt
					['0:01:07', u'1']
	part12_incorrect_attempt
					('0:04:35', u'(4/16 + 8/16 + 4/16) * (4/16 + 8/16 + 4/16)')
	part12_correct_attempt
					['0:13:02', u'4']

2 Student ID:r1gu

	first_attempt
					2015-10-30 09:17:08
	part1_correct_attempt
					['0:00:00', u'4/16']
	part2_correct_attempt
					['0:00:00', u'8/16']
	part3_correct_attempt
					['0:00:28', u'4/16']
	part4_correct_attempt
					['0:00:28', u'4/16']
	part5_correct_attempt
					['0:00:28', u'8/16']
	part6_correct_attempt
					['0:00:28', u'4/16']
	part7_correct_attempt
					['0:01:28', u'1']
	part8_correct_attempt
					['0:01:28', u'1']
	part12_incorrect_attempt
					('0:03:19', u'(1+4+3+8+20+12+7+16+9)/16')
	part12_correct_attempt
					['0:05:10', u'(1+4+3+4+16+12+3+12+9)/16']

3 Student ID:t1tran

	first_attempt
					2015-10-23 21:44:23
	part1_correct_attempt
					['0:00:00', u'4/16']
	part2_correct_attempt
					['0:00:00', u'8/16']
	part3_correct_attempt
					['0:00:00', u'4/16']
	part4_correct_attempt
					['0:00:00', u'4/16']
	part5_correct_attempt
					['0:00:00', u'8/16']
	part6_correct_attempt
					['0:00:00', u'4/16']
	part7_correct_attempt
					['0:00:20', u'1']
	part8_correct_attempt
					['0:00:20', u'1']
	part12_incorrect_attempt
					('0:06:38', u'2(4/16+8/16+4/16)')
	part12_correct_attempt
					['7:58:17', u'2(1/4(1+3)+1/2(2))']

4 Student ID:tpmach

	first_attempt
					2015-10-23 22:37:35
	part1_correct_attempt
					['0:00:00', u'1/16+2/16+1/16']
	part2_correct_attempt
					['0:00:00', u'(2+4+2)/16']
	part3_correct_attempt
					['0:00:00', u'(1+2+1)/16']
	part4_correct_attempt
					['0:00:46', u'(1+2+1)/16']
	part5_correct_attempt
					['0:00:46', u'(2+4+2)/16']
	part6_correct_attempt
					['0:00:46', u'(1+2+1)/16']
	part7_correct_attempt
					['0:01:45', u'1']
	part8_correct_attempt
					['0:02:50', u'1']
	part12_incorrect_attempt
					('2 days, 1:35:45', u'(1+2+3)*2+(1+2+3)*2')
	part12_correct_attempt
					['2 days, 1:37:27', u'2*2']

5 Student ID:starinia

	first_attempt
					2015-10-29 20:56:54
	part1_correct_attempt
					['0:00:00', u'4/16']
	part2_correct_attempt
					['0:00:00', u'8/16']
	part3_correct_attempt
					['0:00:00', u'4/16']
	part4_correct_attempt
					['0:00:00', u'4/16']
	part5_correct_attempt
					['0:00:00', u'8/16']
	part6_correct_attempt
					['0:00:00', u'4/16']
	part7_correct_attempt
					['-1 day, 23:49:42', u'1']
	part8_correct_attempt
					['-1 day, 23:49:42', u'1']
	part12_incorrect_attempt
					('0:00:00', u'4/16 + 8/16 + 4/16 + 4/16 + 8/16 + 4/16')
	part12_correct_attempt
					['5:26:40', u'(1*1*1/16)+(2*1*2/16)+(3*1*1/16) + (1*3*1/16)+(2*3*2/16)+(3*3*1/16) + (2*1*2/16) + (2*2*4/16)+(3*2*2/16)']

6 Student ID:bpandayk

	first_attempt
					2015-10-30 17:58:33
	part1_correct_attempt
					['0:00:00', u'4/16']
	part2_correct_attempt
					['0:00:33', u'8/16']
	part3_correct_attempt
					['0:00:33', u'4/16']
	part4_correct_attempt
					['0:00:33', u'4/16']
	part5_correct_attempt
					['0:00:33', u'8/16']
	part6_correct_attempt
					['0:00:33', u'4/16']
	part7_correct_attempt
					['0:00:57', u'1']
	part8_correct_attempt
					['0:00:47', u'1']
	part12_incorrect_attempt
					('0:02:52', u'32*32/16')
	part12_correct_attempt
					['0:03:21', u'(32*32)/(16*16)']

7 Student ID:wmiao

	first_attempt
					2015-10-29 18:00:40
	part1_correct_attempt
					['0:00:00', u'4/16']
	part2_correct_attempt
					['0:00:00', u'8/16']
	part3_correct_attempt
					['0:00:00', u'4/16']
	part4_correct_attempt
					['0:00:00', u'4/16']
	part5_correct_attempt
					['0:00:00', u'8/16']
	part6_correct_attempt
					['0:00:00', u'4/16']
	part7_correct_attempt
					['0:00:00', u'1']
	part8_correct_attempt
					['0:00:00', u'1']
	part12_incorrect_attempt
					('0:04:47', u'2*(1*4/16+4*8/16+9*4/16)')
	part12_correct_attempt
					['0:05:48', u'1*1/16+2*2/16+3*1/16+2*2/16+4*4/16+6*2/16+3*1/16+6*2/16+9*1/16']












## Part 13

### (12) Mistake Group Digits of size 12




### (7) Mistake Group Fraction of size 7




### (2) Mistake Group redirect of size 2




### (1) Mistake Group ['R.0.0', 'R.0.1', 'R.1.1.0'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.0.1', 'R.1.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|1*1/16+2*2/16+3*1/16+2*2/16+4*4/16+6*2/16+3*1/16+6*2/16+9*1/16-[1*(1/16+2/16+1/16)+2*(2/16+4/16+2/16)+3*(1/16+2/16+1/16)]*[1*(1/16+2/16+1/16)+2*(2/16+4/16+2/16)+3*(1/16+2/16+1/16)]	|(1*1/16 + 2*2/16 + 3*1/16 + 2*2/16 + 4*4/16 + 6*2/16 + 3*1/16 + 6*2/16 + 9*1/16)-((1*1/16 + 2*2/16 + 3*1/16 + 2*2/16 + 4*4/16 + 6*2/16 + 3*1/16 + 6*2/16 + 9*1/16)*(1*4/16 + 2*8/16 + 3*4/16))	|[('R.0.0', 3.4375, u'1*1/16+2*2/16+3*1/16+2*2/16+4*4/16+6*2/16+3*1/16+6*2/16', u'1*1/16 + 2*2/16 + 3*1/16 + 2*2/16 + 4*4/16 + 6*2/16 + 3*1/16 + 6*2/16'), ('R.0.1', 0.5625, u'9*1/16', u'9*1/16'), ('R.1.1.0', 1.25, u'1*(1/16+2/16+1/16)+2*(2/16+4/16+2/16)', u'1*4/16 + 2*8/16')]	|




### (5) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:jjm019

	first_attempt
					2015-10-25 23:56:23
	part1_correct_attempt
					['0:00:00', u'4/16']
	part2_correct_attempt
					['0:00:00', u'8/16']
	part3_correct_attempt
					['0:00:00', u'4/16']
	part4_correct_attempt
					['0:00:00', u'4/16']
	part5_correct_attempt
					['0:00:00', u'8/16']
	part6_correct_attempt
					['0:00:00', u'4/16']
	part7_correct_attempt
					['0:00:00', u'1']
	part8_correct_attempt
					['0:00:00', u'1']
	part9_correct_attempt
					['2 days, 20:20:06', u'1(4/16)+2(8/16)+3(4/16)']
	part10_correct_attempt
					['2 days, 20:20:06', u'1(4/16)+2(8/16)+3(4/16)']
	part12_correct_attempt
					['2 days, 20:21:57', u'1(8/16)+2(1)+3(8/16)']
	part13_incorrect_attempt
					('2 days, 20:22:33', u'4-2')
	part13_correct_attempt
					['2 days, 20:23:01', u'4-4']

1 Student ID:k5law

	first_attempt
					2015-10-26 06:52:27
	part1_correct_attempt
					['0:00:00', u'4/16']
	part2_correct_attempt
					['0:00:00', u'8/16']
	part3_correct_attempt
					['0:00:00', u'4/16']
	part4_correct_attempt
					['0:00:00', u'4/16']
	part5_correct_attempt
					['0:00:00', u'8/16']
	part6_correct_attempt
					['0:00:00', u'4/16']
	part7_correct_attempt
					['0:00:00', u'1']
	part8_correct_attempt
					['0:00:08', u'1']
	part9_correct_attempt
					['0:10:33', u'[4/16]+[2*(8/16)]+[3*(4/16)]']
	part10_correct_attempt
					['0:11:28', u'[4/16]+[2*(8/16)]+[3*(4/16)]']
	part12_correct_attempt
					['0:11:28', u'[[4/16]+[2*(8/16)]+[3*(4/16)]]+[[4/16]+[2*(8/16)]+[3*(4/16)]]']
	part13_incorrect_attempt
					('0:15:01', u'[[4/16]+[2*(8/16)]+[3*(4/16)]]+[[4/16]+[2*(8/16)]+[3*(4/16)]]')
	part13_correct_attempt
					['0:16:40', u'[[[4/16]+[2*(8/16)]+[3*(4/16)]]+[[4/16]+[2*(8/16)]+[3*(4/16)]]]-[[4/16]+[2*(8/16)]+[3*(4/16)]]*[[4/16]+[2*(8/16)]+[3*(4/16)]]']

2 Student ID:r1gu

	first_attempt
					2015-10-30 09:17:08
	part1_correct_attempt
					['0:00:00', u'4/16']
	part2_correct_attempt
					['0:00:00', u'8/16']
	part3_correct_attempt
					['0:00:28', u'4/16']
	part4_correct_attempt
					['0:00:28', u'4/16']
	part5_correct_attempt
					['0:00:28', u'8/16']
	part6_correct_attempt
					['0:00:28', u'4/16']
	part7_correct_attempt
					['0:01:28', u'1']
	part8_correct_attempt
					['0:01:28', u'1']
	part9_correct_attempt
					['0:01:28', u'(4+16+12)/16']
	part10_correct_attempt
					['0:01:28', u'(4+16+12)/16']
	part12_correct_attempt
					['0:05:10', u'(1+4+3+4+16+12+3+12+9)/16']
	part13_incorrect_attempt
					('0:05:36', u'4-1')
	part13_correct_attempt
					['0:06:44', u'4-4']

3 Student ID:ffhaddad

	first_attempt
					2015-10-25 19:50:00
	part1_correct_attempt
					['0:00:00', u'1/16+2/16+1/16']
	part2_correct_attempt
					['0:00:27', u'2/16+4/16+2/16']
	part3_correct_attempt
					['0:00:43', u'1/16+2/16+1/16']
	part4_correct_attempt
					['0:01:53', u'1/16+2/16+1/16']
	part5_correct_attempt
					['0:01:23', u'2/16+4/16+2/16']
	part6_correct_attempt
					['0:02:06', u'1/16+2/16+1/16']
	part7_correct_attempt
					['0:02:20', u'1']
	part8_correct_attempt
					['0:02:34', u'1']
	part9_correct_attempt
					['0:03:58', u'1*.25+2*.5+3*.25']
	part10_correct_attempt
					['0:06:24', u'1*.25+2*.5+3*.25']
	part12_correct_attempt
					['0:15:33', u'[1*.25+2*.5+3*.25]*[1*.25+2*.5+3*.25]']
	part13_incorrect_attempt
					('0:16:22', u'[1*.25+2*.5+3*.25]*[1*.25+2*.5+3*.25]-[([1*.25+2*.5+3*.25]*[1*.25+2*.5+3*.25])*(1*.25+2*.5+3*.25)]')
					('0:17:11', u'[1*.25+2*.5+3*.25]*[1*.25+2*.5+3*.25]')
	part13_correct_attempt
					['0:17:44', u'[1*.25+2*.5+3*.25]*[1*.25+2*.5+3*.25]-[[1*.25+2*.5+3*.25]*[1*.25+2*.5+3*.25]]']

4 Student ID:agian

	first_attempt
					2015-10-30 22:32:56
	part1_correct_attempt
					['0:00:00', u'1/16+2/16+1/16']
	part2_correct_attempt
					['0:00:28', u'2/16+4/16+2/16']
	part3_correct_attempt
					['0:00:40', u'1/16+2/16+1/16']
	part4_correct_attempt
					['0:00:52', u'1/16+2/16+1/16']
	part5_correct_attempt
					['0:00:52', u'2/16+4/16+2/16']
	part6_correct_attempt
					['0:00:52', u'1/16+2/16+1/16']
	part7_correct_attempt
					['0:01:04', u'1']
	part8_correct_attempt
					['0:01:04', u'1']
	part9_correct_attempt
					['0:02:28', u'(1/16+2/16+1/16)+2(2/16+4/16+2/16)+3(1/16+2/16+1/16)']
	part10_correct_attempt
					['0:02:33', u'(1/16+2/16+1/16)+2(2/16+4/16+2/16)+3(1/16+2/16+1/16)']
	part12_correct_attempt
					['0:06:43', u'4']
	part13_incorrect_attempt
					('0:07:41', u'1*1/16+2*2/16+3*1/16+2*2/16+4*4/16+6*2/16+3*1/16+6*2/16+9*1/16')
	part13_correct_attempt
					['0:08:24', u'0']












## Part 15

### (81) Mistake Group Digits of size 81




### (15) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:r2fisher

	first_attempt
					2015-10-26 23:25:07
	part15_incorrect_attempt
					('0:04:32', u'-1')
	part15_correct_attempt
					['0:04:39', u'0']

1 Student ID:rraiyyan

	first_attempt
					2015-10-28 01:08:26
	part15_incorrect_attempt
					('0:02:39', u'-1')
	part15_correct_attempt
					['0:02:48', u'0']

2 Student ID:hachrist

	first_attempt
					2015-10-26 01:47:33
	part15_incorrect_attempt
					('0:04:48', u'-1')
	part15_correct_attempt
					['0:04:55', u'0']

3 Student ID:t1tran

	first_attempt
					2015-10-23 21:44:23
	part15_incorrect_attempt
					('7:58:30', u'-1')
	part15_correct_attempt
					['7:59:20', u'0']

4 Student ID:starinia

	first_attempt
					2015-10-29 20:56:54
	part15_incorrect_attempt
					('0:00:00', u'-1')
	part15_correct_attempt
					['5:30:35', u'0']

5 Student ID:dcastlem

	first_attempt
					2015-10-30 21:56:14
	part15_incorrect_attempt
					('0:41:55', u'-1')
	part15_correct_attempt
					['0:42:01', u'0']

6 Student ID:krkelkar

	first_attempt
					2015-10-23 08:16:52
	part15_incorrect_attempt
					('0:00:00', u'-1')
	part15_correct_attempt
					['0:00:15', u'0']

7 Student ID:lywong

	first_attempt
					2015-10-28 08:38:01
	part15_incorrect_attempt
					('0:03:56', u'-1')
					('0:04:00', u'-11')
	part15_correct_attempt
					['0:04:11', u'0']

8 Student ID:any027

	first_attempt
					2015-10-26 04:57:49
	part15_incorrect_attempt
					('0:06:18', u'-1')
	part15_correct_attempt
					['0:06:25', u'0']

9 Student ID:akg009

	first_attempt
					2015-10-30 21:08:55
	part15_incorrect_attempt
					('0:29:13', u'-1')
	part15_correct_attempt
					['0:29:32', u'0']

10 Student ID:lguintu

	first_attempt
					2015-10-24 23:54:12
	part15_incorrect_attempt
					('0:03:04', u'-1')
	part15_correct_attempt
					['0:03:11', u'0']

11 Student ID:asetters

	first_attempt
					2015-10-27 20:00:23
	part15_incorrect_attempt
					('0:07:14', u'-1')
	part15_correct_attempt
					['0:07:20', u'0']

12 Student ID:e9brown

	first_attempt
					2015-10-27 23:18:13
	part15_incorrect_attempt
					('0:00:40', u'-1')
	part15_correct_attempt
					['0:00:45', u'0']

13 Student ID:anvan

	first_attempt
					2015-10-30 16:13:55
	part15_incorrect_attempt
					('2:09:07', u'-1')
	part15_correct_attempt
					['2:09:14', u'0']

14 Student ID:v3doan

	first_attempt
					2015-10-27 02:54:28
	part15_incorrect_attempt
					('2:20:36', u'-1')
	part15_correct_attempt
					['2:20:43', u'0']












## Part 2

### (30) Mistake Group Digits of size 30




### (27) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:galu

	first_attempt
					2015-10-30 23:51:39
	part2_incorrect_attempt
					('-1 day, 23:57:19', u'2/16')
					('-1 day, 23:59:26', u'1/16')
					('0:00:00', u'4/16')
	part2_correct_attempt
					['0:01:25', u'8/16']

1 Student ID:ctroncos

	first_attempt
					2015-10-29 16:23:01
	part2_incorrect_attempt
					('-1 day, 23:58:34', u'2/16')
	part2_correct_attempt
					['0:00:22', u'8/16']

2 Student ID:t2shin

	first_attempt
					2015-10-28 00:27:23
	part2_incorrect_attempt
					('0:00:00', u'(2/16)^(1/2)')
	part2_correct_attempt
					['0:00:32', u'2/4']

3 Student ID:kbielawi

	first_attempt
					2015-10-27 23:45:28
	part2_incorrect_attempt
					('-2 days, 22:21:17', u'2/16')
	part2_correct_attempt
					['0:09:15', u'8/16']

4 Student ID:glcohen

	first_attempt
					2015-10-27 15:51:26
	part2_incorrect_attempt
					('-1 day, 23:59:01', u'2/16')
	part2_correct_attempt
					['0:00:00', u'8/16']

5 Student ID:ppanourg

	first_attempt
					2015-10-30 20:35:08
	part2_incorrect_attempt
					('0:00:00', u'6/16')
	part2_correct_attempt
					['0:00:53', u'8/16']

6 Student ID:d6he

	first_attempt
					2015-10-28 20:30:47
	part2_incorrect_attempt
					('-1 day, 23:59:15', u'2/16')
					('-1 day, 23:59:24', u'4/16')
	part2_correct_attempt
					['0:00:00', u'8/16']

7 Student ID:any027

	first_attempt
					2015-10-26 04:57:49
	part2_incorrect_attempt
					('-1 day, 23:59:38', u'2/16')
	part2_correct_attempt
					['0:00:52', u'(2/16) + (4/16) + (2/16)']

8 Student ID:rwthomps

	first_attempt
					2015-10-30 20:40:06
	part2_incorrect_attempt
					('-1 day, 23:59:10', u'6/16')
	part2_correct_attempt
					['0:00:00', u'8/16']

9 Student ID:kthui

	first_attempt
					2015-10-25 02:52:00
	part2_incorrect_attempt
					('-1 day, 23:57:21', u'2/16')
	part2_correct_attempt
					['0:00:00', u'8/16']

10 Student ID:mroknich

	first_attempt
					2015-10-26 04:37:56
	part2_incorrect_attempt
					('-1 day, 23:57:56', u'2/16')
	part2_correct_attempt
					['0:00:00', u'8/16']

11 Student ID:dkurli

	first_attempt
					2015-10-29 22:43:11
	part2_incorrect_attempt
					('-1 day, 23:58:26', u'2/16')
	part2_correct_attempt
					['0:00:00', u'1/2']

12 Student ID:amquinte

	first_attempt
					2015-10-30 19:36:07
	part2_incorrect_attempt
					('-1 day, 23:46:42', u'2/16')
	part2_correct_attempt
					['0:00:00', u'8/16']

13 Student ID:jew037

	first_attempt
					2015-10-28 18:39:54
	part2_incorrect_attempt
					('-1 day, 23:58:55', u'2/16')
					('0:00:40', u'(1/16 + 2/16 + 1/16)')
	part2_correct_attempt
					['0:01:04', u'(2/16 + 4/16 + 2/16)']

14 Student ID:anl114

	first_attempt
					2015-10-30 21:45:35
	part2_incorrect_attempt
					('-1 day, 23:59:47', u'2/16')
	part2_correct_attempt
					['0:01:08', u'8/16']

15 Student ID:avasavad

	first_attempt
					2015-10-28 04:30:11
	part2_incorrect_attempt
					('-1 day, 18:58:46', u'2/16')
					('-1 day, 19:01:09', u'4/16')
	part2_correct_attempt
					['0:00:00', u'1/2']

16 Student ID:s6deng

	first_attempt
					2015-10-30 07:06:14
	part2_incorrect_attempt
					('-1 day, 23:53:00', u'2/16')
	part2_correct_attempt
					['0:00:00', u'8/16']

17 Student ID:rraiyyan

	first_attempt
					2015-10-28 01:08:26
	part2_incorrect_attempt
					('-1 day, 23:54:05', u'1/8')
	part2_correct_attempt
					['0:01:16', u'1/2']

18 Student ID:r1gu

	first_attempt
					2015-10-30 09:17:08
	part2_incorrect_attempt
					('-1 day, 23:56:54', u'2/16')
	part2_correct_attempt
					['0:00:00', u'8/16']

19 Student ID:jtfrankl

	first_attempt
					2015-10-28 21:16:42
	part2_incorrect_attempt
					('0:02:06', u'4/16')
	part2_correct_attempt
					['0:02:58', u'.5']

20 Student ID:c1sorian

	first_attempt
					2015-10-28 22:01:21
	part2_incorrect_attempt
					('-1 day, 23:58:58', u'2/16')
	part2_correct_attempt
					['0:00:24', u'8/16']

21 Student ID:haliew

	first_attempt
					2015-10-29 02:14:32
	part2_incorrect_attempt
					('-1 day, 23:59:36', u'10/16')
	part2_correct_attempt
					['0:00:00', u'8/16']

22 Student ID:aordookh

	first_attempt
					2015-10-29 03:19:43
	part2_incorrect_attempt
					('0:00:00', u'6/16')
	part2_correct_attempt
					['0:02:16', u'8/16']

23 Student ID:starinia

	first_attempt
					2015-10-29 20:56:54
	part2_incorrect_attempt
					('-1 day, 23:49:42', u'2/16')
	part2_correct_attempt
					['0:00:00', u'8/16']

24 Student ID:bpandayk

	first_attempt
					2015-10-30 17:58:33
	part2_incorrect_attempt
					('-1 day, 23:57:40', u'2/16')
	part2_correct_attempt
					['0:00:33', u'8/16']

25 Student ID:qtluong

	first_attempt
					2015-10-29 07:37:59
	part2_incorrect_attempt
					('-1 day, 23:59:31', u'1/3')
	part2_correct_attempt
					['0:00:00', u'2/4']

26 Student ID:small

	first_attempt
					2015-10-30 23:47:41
	part2_incorrect_attempt
					('-1 day, 23:53:56', u'2/16')
	part2_correct_attempt
					['0:00:00', u'1/2']












## Part 3

### (4) Mistake Group Digits of size 4




### (27) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:galu

	first_attempt
					2015-10-30 23:51:39
	part3_incorrect_attempt
					('-1 day, 23:57:19', u'1/16')
					('-1 day, 23:59:26', u'2/16')
	part3_correct_attempt
					['0:00:00', u'4/16']

1 Student ID:starinia

	first_attempt
					2015-10-29 20:56:54
	part3_incorrect_attempt
					('-1 day, 23:49:42', u'1/16')
	part3_correct_attempt
					['0:00:00', u'4/16']

2 Student ID:ctroncos

	first_attempt
					2015-10-29 16:23:01
	part3_incorrect_attempt
					('-1 day, 23:58:34', u'2/16')
					('-1 day, 23:59:15', u'1/16')
	part3_correct_attempt
					['0:00:22', u'4/16']

3 Student ID:aggouw

	first_attempt
					2015-10-27 03:29:36
	part3_incorrect_attempt
					('0:00:19', u'8/16')
	part3_correct_attempt
					['0:00:24', u'4/16']

4 Student ID:glcohen

	first_attempt
					2015-10-27 15:51:26
	part3_incorrect_attempt
					('-1 day, 23:59:01', u'1/16')
	part3_correct_attempt
					['0:00:00', u'4/16']

5 Student ID:c1sorian

	first_attempt
					2015-10-28 22:01:21
	part3_incorrect_attempt
					('-1 day, 23:58:58', u'1/16')
	part3_correct_attempt
					['0:00:24', u'4/16']

6 Student ID:d6he

	first_attempt
					2015-10-28 20:30:47
	part3_incorrect_attempt
					('-1 day, 23:59:15', u'1/16')
	part3_correct_attempt
					['0:00:00', u'4/16']

7 Student ID:any027

	first_attempt
					2015-10-26 04:57:49
	part3_incorrect_attempt
					('-1 day, 23:59:38', u'1/16')
	part3_correct_attempt
					['0:00:52', u'(1/16) + (2/16) + (1/16)']

8 Student ID:rwthomps

	first_attempt
					2015-10-30 20:40:06
	part3_incorrect_attempt
					('-1 day, 23:59:10', u'3/16')
	part3_correct_attempt
					['0:00:00', u'4/16']

9 Student ID:krau

	first_attempt
					2015-10-29 22:42:12
	part3_incorrect_attempt
					('0:01:33', u'1/8')
	part3_correct_attempt
					['0:01:50', u'4/16']

10 Student ID:kthui

	first_attempt
					2015-10-25 02:52:00
	part3_incorrect_attempt
					('-1 day, 23:57:21', u'1/16')
	part3_correct_attempt
					['0:00:00', u'4/16']

11 Student ID:mroknich

	first_attempt
					2015-10-26 04:37:56
	part3_incorrect_attempt
					('-1 day, 23:57:56', u'1/16')
	part3_correct_attempt
					['0:00:00', u'4/16']

12 Student ID:dkurli

	first_attempt
					2015-10-29 22:43:11
	part3_incorrect_attempt
					('-1 day, 23:58:26', u'1/16')
	part3_correct_attempt
					['0:00:00', u'1/4']

13 Student ID:s2chaudh

	first_attempt
					2015-10-29 02:35:46
	part3_incorrect_attempt
					('-1 day, 23:59:11', u'1/2')
	part3_correct_attempt
					['0:00:26', u'1/4']

14 Student ID:jew037

	first_attempt
					2015-10-28 18:39:54
	part3_incorrect_attempt
					('-1 day, 23:58:55', u'1/16')
	part3_correct_attempt
					['0:00:20', u'(1/16 + 2/16 + 1/16)']

15 Student ID:anl114

	first_attempt
					2015-10-30 21:45:35
	part3_incorrect_attempt
					('-1 day, 23:59:47', u'1/16')
	part3_correct_attempt
					['0:01:08', u'4/16']

16 Student ID:avasavad

	first_attempt
					2015-10-28 04:30:11
	part3_incorrect_attempt
					('-1 day, 18:58:46', u'1/16')
	part3_correct_attempt
					['0:00:00', u'1/4']

17 Student ID:s6deng

	first_attempt
					2015-10-30 07:06:14
	part3_incorrect_attempt
					('-1 day, 23:53:00', u'1/16')
	part3_correct_attempt
					['0:00:00', u'4/16']

18 Student ID:rraiyyan

	first_attempt
					2015-10-28 01:08:26
	part3_incorrect_attempt
					('-1 day, 23:54:05', u'1/16')
	part3_correct_attempt
					['0:01:16', u'1/4']

19 Student ID:kbielawi

	first_attempt
					2015-10-27 23:45:28
	part3_incorrect_attempt
					('-2 days, 22:21:17', u'1/16')
	part3_correct_attempt
					['0:00:00', u'4/16']

20 Student ID:seleon

	first_attempt
					2015-10-28 03:21:38
	part3_incorrect_attempt
					('0:01:17', u'5/16')
	part3_correct_attempt
					['0:01:50', u'4/16']

21 Student ID:haliew

	first_attempt
					2015-10-29 02:14:32
	part3_incorrect_attempt
					('-1 day, 23:59:36', u'3/16')
	part3_correct_attempt
					['0:00:00', u'4/16']

22 Student ID:r2fisher

	first_attempt
					2015-10-26 23:25:07
	part3_incorrect_attempt
					('-1 day, 23:59:20', u'(1+2+1+2*2+2*4+2*2+3+3*2+3)/16')
					('-1 day, 23:59:39', u'(1+2+1+2*2+2*4+2*2+3+3*2+3)/16')
	part3_correct_attempt
					['0:00:23', u'1/4']

23 Student ID:bpandayk

	first_attempt
					2015-10-30 17:58:33
	part3_incorrect_attempt
					('-1 day, 23:57:40', u'1/16')
	part3_correct_attempt
					['0:00:33', u'4/16']

24 Student ID:amquinte

	first_attempt
					2015-10-30 19:36:07
	part3_incorrect_attempt
					('-1 day, 23:46:42', u'1/16')
	part3_correct_attempt
					['0:00:00', u'4/16']

25 Student ID:qtluong

	first_attempt
					2015-10-29 07:37:59
	part3_incorrect_attempt
					('-1 day, 23:59:31', u'1/3')
					('0:00:00', u'3/4')
	part3_correct_attempt
					['0:00:07', u'1/4']

26 Student ID:small

	first_attempt
					2015-10-30 23:47:41
	part3_incorrect_attempt
					('-1 day, 23:49:53', u'1/2')
					('-1 day, 23:51:17', u'1/4 + 3/4 + 1')
					('-1 day, 23:51:43', u'1/4 + 3/4 + 1')
					('-1 day, 23:52:18', u'1/4 + 3/4 + 1')
					('-1 day, 23:52:30', u'1/4 + 3/4 + 1')
					('-1 day, 23:52:46', u'1/4 + 3/4 + 1')
					('-1 day, 23:53:09', u'1/4 + 3/4 + 1')
					('-1 day, 23:53:56', u'1/16')
	part3_correct_attempt
					['0:00:00', u'1/4']












## Part 4

### (1) Mistake Group Digits of size 1




### (1) Mistake Group ['R.0.0'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|1/16+2/16+1/16	|(1/16) + (1/14) + (1/8)	|[('R.0.0', 0.0625, u'1/16', u'1/16')]	|




### (15) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:galu

	first_attempt
					2015-10-30 23:51:39
	part4_incorrect_attempt
					('-1 day, 23:57:19', u'1/16')
					('-1 day, 23:59:26', u'2/16')
	part4_correct_attempt
					['0:00:00', u'4/16']

1 Student ID:r2fisher

	first_attempt
					2015-10-26 23:25:07
	part4_incorrect_attempt
					('-1 day, 23:59:39', u'(1+2+1+2*2+2*4+2*2+3+3*2+3)/16')
	part4_correct_attempt
					['0:00:23', u'1/4']

2 Student ID:rwthomps

	first_attempt
					2015-10-30 20:40:06
	part4_incorrect_attempt
					('-1 day, 23:59:10', u'3/16')
	part4_correct_attempt
					['0:00:00', u'4/16']

3 Student ID:t2shin

	first_attempt
					2015-10-28 00:27:23
	part4_incorrect_attempt
					('0:00:32', u'1/16')
	part4_correct_attempt
					['0:00:43', u'1/4']

4 Student ID:starinia

	first_attempt
					2015-10-29 20:56:54
	part4_incorrect_attempt
					('-1 day, 23:49:42', u'1/16')
	part4_correct_attempt
					['0:00:00', u'4/16']

5 Student ID:ffhaddad

	first_attempt
					2015-10-25 19:50:00
	part4_incorrect_attempt
					('0:01:23', u'46.9445')
	part4_correct_attempt
					['0:01:53', u'1/16+2/16+1/16']

6 Student ID:glcohen

	first_attempt
					2015-10-27 15:51:26
	part4_incorrect_attempt
					('-1 day, 23:59:01', u'1/16')
	part4_correct_attempt
					['0:01:07', u'4/16']

7 Student ID:c1sorian

	first_attempt
					2015-10-28 22:01:21
	part4_incorrect_attempt
					('-1 day, 23:58:58', u'1/16')
	part4_correct_attempt
					['0:00:24', u'4/16']

8 Student ID:anl114

	first_attempt
					2015-10-30 21:45:35
	part4_incorrect_attempt
					('-1 day, 23:59:47', u'1/16')
	part4_correct_attempt
					['0:01:08', u'4/16']

9 Student ID:seleon

	first_attempt
					2015-10-28 03:21:38
	part4_incorrect_attempt
					('0:01:17', u'5/16')
	part4_correct_attempt
					['0:01:50', u'4/16']

10 Student ID:avasavad

	first_attempt
					2015-10-28 04:30:11
	part4_incorrect_attempt
					('-1 day, 18:58:46', u'1/16')
	part4_correct_attempt
					['0:00:26', u'1/4']

11 Student ID:amquinte

	first_attempt
					2015-10-30 19:36:07
	part4_incorrect_attempt
					('-1 day, 23:46:42', u'1/16')
	part4_correct_attempt
					['0:00:00', u'4/16']

12 Student ID:small

	first_attempt
					2015-10-30 23:47:41
	part4_incorrect_attempt
					('-1 day, 23:51:43', u'1/4 + 3/4 + 1')
					('-1 day, 23:52:18', u'1/4 + 3/4 + 1')
					('-1 day, 23:52:30', u'1/4 + 3/4 + 1')
					('-1 day, 23:52:46', u'1/4 + 3/4 + 1')
					('-1 day, 23:53:09', u'1/4 + 3/4 + 1')
	part4_correct_attempt
					['0:00:00', u'1/4']

13 Student ID:kthui

	first_attempt
					2015-10-25 02:52:00
	part4_incorrect_attempt
					('-1 day, 23:57:21', u'1/16')
	part4_correct_attempt
					['0:00:00', u'4/16']

14 Student ID:s6deng

	first_attempt
					2015-10-30 07:06:14
	part4_incorrect_attempt
					('-1 day, 23:53:00', u'1/16')
	part4_correct_attempt
					['0:00:00', u'4/16']












## Part 5

### (4) Mistake Group ['R.0.0.0'] of size 4
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|2/16+4/16+2/16	|1/4 + 3/4 + 1 + 1/4 + 3/4 + 1	|[('R.0.0.0', 2.0, u'2', u'1/4 + 3/4 + 1')]	|




### (14) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:galu

	first_attempt
					2015-10-30 23:51:39
	part5_incorrect_attempt
					('-1 day, 23:57:19', u'2/16')
					('-1 day, 23:59:26', u'1/16')
					('0:00:00', u'4/16')
	part5_correct_attempt
					['0:01:25', u'8/16']

1 Student ID:jtfrankl

	first_attempt
					2015-10-28 21:16:42
	part5_incorrect_attempt
					('0:02:06', u'1/4')
	part5_correct_attempt
					['0:02:58', u'1/2']

2 Student ID:amquinte

	first_attempt
					2015-10-30 19:36:07
	part5_incorrect_attempt
					('-1 day, 23:46:42', u'2/16')
	part5_correct_attempt
					['0:00:00', u'8/16']

3 Student ID:aordookh

	first_attempt
					2015-10-29 03:19:43
	part5_incorrect_attempt
					('0:00:00', u'6/16')
	part5_correct_attempt
					['0:02:16', u'8/16']

4 Student ID:starinia

	first_attempt
					2015-10-29 20:56:54
	part5_incorrect_attempt
					('-1 day, 23:49:42', u'2/16')
	part5_correct_attempt
					['0:00:00', u'8/16']

5 Student ID:aggouw

	first_attempt
					2015-10-27 03:29:36
	part5_incorrect_attempt
					('0:00:35', u'4/16')
	part5_correct_attempt
					['0:00:40', u'8/16']

6 Student ID:jew037

	first_attempt
					2015-10-28 18:39:54
	part5_incorrect_attempt
					('0:00:40', u'(1/16 + 2/16 + 1/16)')
	part5_correct_attempt
					['0:01:04', u'(2/16 + 4/16 + 2/16)']

7 Student ID:glcohen

	first_attempt
					2015-10-27 15:51:26
	part5_incorrect_attempt
					('-1 day, 23:59:01', u'2/16')
	part5_correct_attempt
					['0:01:07', u'8/16']

8 Student ID:c1sorian

	first_attempt
					2015-10-28 22:01:21
	part5_incorrect_attempt
					('-1 day, 23:58:58', u'2/16')
	part5_correct_attempt
					['0:00:24', u'1/2']

9 Student ID:anl114

	first_attempt
					2015-10-30 21:45:35
	part5_incorrect_attempt
					('-1 day, 23:59:47', u'2/16')
	part5_correct_attempt
					['0:01:08', u'8/16']

10 Student ID:rwthomps

	first_attempt
					2015-10-30 20:40:06
	part5_incorrect_attempt
					('-1 day, 23:59:10', u'6/16')
	part5_correct_attempt
					['0:00:00', u'8/16']

11 Student ID:avasavad

	first_attempt
					2015-10-28 04:30:11
	part5_incorrect_attempt
					('-1 day, 18:58:46', u'2/16')
	part5_correct_attempt
					['0:00:26', u'1/2']

12 Student ID:kthui

	first_attempt
					2015-10-25 02:52:00
	part5_incorrect_attempt
					('-1 day, 23:57:21', u'2/16')
	part5_correct_attempt
					['0:00:00', u'8/16']

13 Student ID:s6deng

	first_attempt
					2015-10-30 07:06:14
	part5_incorrect_attempt
					('-1 day, 23:53:00', u'2/16')
	part5_correct_attempt
					['0:00:00', u'8/16']












## Part 6

### (13) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:galu

	first_attempt
					2015-10-30 23:51:39
	part6_incorrect_attempt
					('-1 day, 23:57:19', u'1/16')
					('-1 day, 23:59:26', u'2/16')
	part6_correct_attempt
					['0:00:00', u'4/16']

1 Student ID:rwthomps

	first_attempt
					2015-10-30 20:40:06
	part6_incorrect_attempt
					('-1 day, 23:59:10', u'3/16')
	part6_correct_attempt
					['0:00:00', u'4/16']

2 Student ID:amquinte

	first_attempt
					2015-10-30 19:36:07
	part6_incorrect_attempt
					('-1 day, 23:46:42', u'1/16')
	part6_correct_attempt
					['0:00:00', u'4/16']

3 Student ID:starinia

	first_attempt
					2015-10-29 20:56:54
	part6_incorrect_attempt
					('-1 day, 23:49:42', u'1/16')
	part6_correct_attempt
					['0:00:00', u'4/16']

4 Student ID:aggouw

	first_attempt
					2015-10-27 03:29:36
	part6_incorrect_attempt
					('0:00:50', u'8/16')
	part6_correct_attempt
					['0:00:55', u'4/16']

5 Student ID:glcohen

	first_attempt
					2015-10-27 15:51:26
	part6_incorrect_attempt
					('-1 day, 23:59:01', u'1/16')
	part6_correct_attempt
					['0:01:07', u'4/16']

6 Student ID:c1sorian

	first_attempt
					2015-10-28 22:01:21
	part6_incorrect_attempt
					('-1 day, 23:58:58', u'1/16')
	part6_correct_attempt
					['0:00:24', u'1/4']

7 Student ID:anl114

	first_attempt
					2015-10-30 21:45:35
	part6_incorrect_attempt
					('-1 day, 23:59:47', u'1/16')
	part6_correct_attempt
					['0:01:08', u'4/16']

8 Student ID:seleon

	first_attempt
					2015-10-28 03:21:38
	part6_incorrect_attempt
					('0:01:17', u'5/16')
	part6_correct_attempt
					['0:01:56', u'4/16']

9 Student ID:avasavad

	first_attempt
					2015-10-28 04:30:11
	part6_incorrect_attempt
					('-1 day, 18:58:46', u'1/16')
	part6_correct_attempt
					['0:00:26', u'1/4']

10 Student ID:small

	first_attempt
					2015-10-30 23:47:41
	part6_incorrect_attempt
					('-1 day, 23:53:09', u'(1/4 + 3/4 + 1)(1/4 + 3/4 + 1)')
	part6_correct_attempt
					['0:00:00', u'1/4']

11 Student ID:kthui

	first_attempt
					2015-10-25 02:52:00
	part6_incorrect_attempt
					('-1 day, 23:57:21', u'1/16')
	part6_correct_attempt
					['0:00:00', u'4/16']

12 Student ID:s6deng

	first_attempt
					2015-10-30 07:06:14
	part6_incorrect_attempt
					('-1 day, 23:53:00', u'1/16')
	part6_correct_attempt
					['0:00:00', u'4/16']












## Part 7

### (78) Mistake Group Digits of size 78




### (0) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|












## Part 8

### (31) Mistake Group Digits of size 31




### (0) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|












## Part 9

### (90) Mistake Group Fraction of size 90




### (44) Mistake Group Digits of size 44




### (1) Mistake Group redirect of size 1




### (10) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:dgunawan

	first_attempt
					2015-10-29 23:46:52
	part1_correct_attempt
					['0:00:00', u'4/16']
	part2_correct_attempt
					['0:00:29', u'8/16']
	part3_correct_attempt
					['0:00:29', u'4/16']
	part4_correct_attempt
					['0:00:29', u'4/16']
	part5_correct_attempt
					['0:00:29', u'8/16']
	part6_correct_attempt
					['0:00:29', u'4/16']
	part7_correct_attempt
					['0:00:49', u'1']
	part8_correct_attempt
					['0:00:40', u'1']
	part9_incorrect_attempt
					('0:02:07', u'(1/16)[4+8+4]')
	part9_correct_attempt
					['0:02:34', u'(1/16)[4(1)+8(2)+4(3)]']

1 Student ID:hachrist

	first_attempt
					2015-10-26 01:47:33
	part1_correct_attempt
					['0:00:00', u'4/16']
	part2_correct_attempt
					['0:01:07', u'8/16']
	part3_correct_attempt
					['0:01:07', u'4/16']
	part4_correct_attempt
					['0:01:07', u'4/16']
	part5_correct_attempt
					['0:01:07', u'8/16']
	part6_correct_attempt
					['0:01:07', u'4/16 ']
	part7_correct_attempt
					['0:01:07', u'1']
	part8_correct_attempt
					['0:01:07', u'1']
	part9_incorrect_attempt
					('0:04:35', u'4/16 + 8/16 + 4/16')
	part9_correct_attempt
					['0:12:28', u'2']

2 Student ID:ctroncos

	first_attempt
					2015-10-29 16:23:01
	part1_correct_attempt
					['0:00:00', u'(2/16)*2']
	part2_correct_attempt
					['0:00:22', u'8/16']
	part3_correct_attempt
					['0:00:22', u'4/16']
	part4_correct_attempt
					['0:00:44', u'4/16']
	part5_correct_attempt
					['0:00:44', u'8/16']
	part6_correct_attempt
					['0:00:44', u'4/16']
	part7_correct_attempt
					['0:02:09', u'1']
	part8_correct_attempt
					['0:02:09', u'1']
	part9_incorrect_attempt
					('0:02:09', u'(4/16)+(8/16)+(4/16)')
	part9_correct_attempt
					['0:03:06', u'(4/16)+2*(8/16)+(4/16)*3']

3 Student ID:ksmurlo

	first_attempt
					2015-10-27 07:22:35
	part1_correct_attempt
					['0:00:00', u'4/16']
	part2_correct_attempt
					['0:00:54', u'8/16']
	part3_correct_attempt
					['0:00:54', u'4/16']
	part4_correct_attempt
					['0:00:54', u'4/16']
	part5_correct_attempt
					['0:00:54', u'8/16']
	part6_correct_attempt
					['0:00:54', u'4/16']
	part7_correct_attempt
					['0:01:55', u'1']
	part8_correct_attempt
					['0:00:54', u'1']
	part9_incorrect_attempt
					('1 day, 22:37:37', u'(2/16)+(8/16)+(6/16)')
	part9_correct_attempt
					['1 day, 22:37:50', u'2']

4 Student ID:starinia

	first_attempt
					2015-10-29 20:56:54
	part1_correct_attempt
					['0:00:00', u'4/16']
	part2_correct_attempt
					['0:00:00', u'8/16']
	part3_correct_attempt
					['0:00:00', u'4/16']
	part4_correct_attempt
					['0:00:00', u'4/16']
	part5_correct_attempt
					['0:00:00', u'8/16']
	part6_correct_attempt
					['0:00:00', u'4/16']
	part7_correct_attempt
					['-1 day, 23:49:42', u'1']
	part8_correct_attempt
					['-1 day, 23:49:42', u'1']
	part9_incorrect_attempt
					('0:00:00', u'4/16 + 8/16 + 4/16')
	part9_correct_attempt
					['5:25:51', u'1/16 + 2/16+1/16 + 4/16+ 8/16+4/16+3/16+ 6/16+3/16']

5 Student ID:cfgutier

	first_attempt
					2015-10-30 02:10:11
	part1_correct_attempt
					['0:00:00', u'4/16']
	part2_correct_attempt
					['0:00:17', u'8/16']
	part3_correct_attempt
					['0:00:17', u'4/16']
	part4_correct_attempt
					['0:00:58', u'4/16']
	part5_correct_attempt
					['0:00:58', u'8/16']
	part6_correct_attempt
					['0:00:58', u'4/16']
	part7_correct_attempt
					['0:01:20', u'1']
	part8_correct_attempt
					['0:01:50', u'1']
	part9_incorrect_attempt
					('0:34:19', u'16/16')
	part9_correct_attempt
					['0:36:23', u'32/16']

6 Student ID:jblynch

	first_attempt
					2015-10-28 19:07:10
	part1_correct_attempt
					['0:00:00', u'4/16']
	part2_correct_attempt
					['0:00:00', u'8/16']
	part3_correct_attempt
					['0:00:00', u'4/16']
	part4_correct_attempt
					['0:01:36', u'4/16']
	part5_correct_attempt
					['0:01:36', u'8/16']
	part6_correct_attempt
					['0:01:36', u'4/16']
	part7_correct_attempt
					['0:01:57', u'1']
	part8_correct_attempt
					['0:01:36', u'1']
	part9_incorrect_attempt
					('0:04:23', u'(4/16)+(8/16)+(4/16)')
	part9_correct_attempt
					['0:04:54', u'(4/16)+(16/16)+(12/16)']

7 Student ID:ggaddi

	first_attempt
					2015-10-27 15:37:26
	part1_correct_attempt
					['0:00:00', u'(1+2+1)/16']
	part2_correct_attempt
					['0:00:00', u'(2+4+2)/16']
	part3_correct_attempt
					['0:00:00', u'(1+2+1)/16']
	part4_correct_attempt
					['0:00:00', u'(1+2+1)/16']
	part5_correct_attempt
					['0:00:00', u'(2+4+2)/16']
	part6_correct_attempt
					['0:00:00', u'(1+2+1)/16']
	part7_correct_attempt
					['0:00:00', u'1']
	part8_correct_attempt
					['0:00:00', u'1']
	part9_incorrect_attempt
					('0:00:00', u'(1+2+1)/16+(2+4+2)/16+(1+2+1)/16')
	part9_correct_attempt
					['0:01:05', u'1*(1+2+1)/16+2*(2+4+2)/16+3*(1+2+1)/16']

8 Student ID:s6deng

	first_attempt
					2015-10-30 07:06:14
	part1_correct_attempt
					['0:00:00', u'4/16']
	part2_correct_attempt
					['0:00:00', u'8/16']
	part3_correct_attempt
					['0:00:00', u'4/16']
	part4_correct_attempt
					['0:00:00', u'4/16']
	part5_correct_attempt
					['0:00:00', u'8/16']
	part6_correct_attempt
					['0:00:00', u'4/16']
	part9_incorrect_attempt
					('0:00:36', u'16/16')
	part9_correct_attempt
					['0:01:20', u'32/16']

9 Student ID:vsosnovs

	first_attempt
					2015-10-30 06:17:20
	part1_correct_attempt
					['0:00:00', u'4/16']
	part2_correct_attempt
					['0:00:47', u'1/2']
	part3_correct_attempt
					['0:00:47', u'4/16']
	part4_correct_attempt
					['0:00:47', u'4/16']
	part5_correct_attempt
					['0:00:47', u'8/16']
	part6_correct_attempt
					['0:00:47', u'4/16']
	part7_correct_attempt
					['0:00:58', u'1']
	part8_correct_attempt
					['0:00:58', u'1']
	part9_incorrect_attempt
					('0:04:47', u'(1+2+1+2+4+2+1+2+1)/16')
	part9_correct_attempt
					['13:15:46', u'1(4/16)+2(1/2)+3(4/16)']












