#Problem 9

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


## Part 1

### (32) Mistake Group Digits of size 32




### (1) Mistake Group Wrong_Sign of size 1




### (1) Mistake Group ['R.1.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|1/3+0+1/6	|1/3 + 3/6	|[('R.1.1', 6.0, u'6', u'6')]	|




### (21) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:jdeon

	first_attempt
					2015-10-30 19:50:31
	part1_incorrect_attempt
					('0:00:00', u'2/3')
	part1_correct_attempt
					['0:00:38', u'1/2']

1 Student ID:skodigal

	first_attempt
					2015-10-27 06:23:15
	part1_incorrect_attempt
					('0:00:00', u'2/6')
	part1_correct_attempt
					['0:01:26', u'1/2']

2 Student ID:rraiyyan

	first_attempt
					2015-10-28 01:15:53
	part1_incorrect_attempt
					('0:00:00', u'1/3')
					('0:00:13', u'1/6')
					('0:03:30', u'2/3')
	part1_correct_attempt
					['0:13:36', u'1/2']

3 Student ID:jag028

	first_attempt
					2015-10-30 14:50:16
	part1_incorrect_attempt
					('0:00:00', u'1/3')
	part1_correct_attempt
					['0:00:37', u'1/2']

4 Student ID:t2shin

	first_attempt
					2015-10-28 00:32:42
	part1_incorrect_attempt
					('0:00:00', u'1/3^(1/2)')
					('0:00:18', u'(1/3)^(1/2)')
	part1_correct_attempt
					['0:01:10', u'1/2']

5 Student ID:ralhadda

	first_attempt
					2015-10-24 05:03:51
	part1_incorrect_attempt
					('0:00:00', u'2/6')
	part1_correct_attempt
					['0:00:09', u'3/6']

6 Student ID:hkhodada

	first_attempt
					2015-10-24 18:08:34
	part1_incorrect_attempt
					('0:00:00', u'2/3')
					('0:00:56', u'4/6')
	part1_correct_attempt
					['0:05:38', u'1/2']

7 Student ID:aportuga

	first_attempt
					2015-10-29 03:01:02
	part1_incorrect_attempt
					('0:00:00', u'1/3')
	part1_correct_attempt
					['0:00:40', u'(1/3)+(1/6)']

8 Student ID:qtluong

	first_attempt
					2015-10-29 07:43:26
	part1_incorrect_attempt
					('0:00:00', u'2/3')
	part1_correct_attempt
					['0:02:50', u'1/2']

9 Student ID:dcastlem

	first_attempt
					2015-10-30 22:28:52
	part1_incorrect_attempt
					('0:00:00', u'1/3')
	part1_correct_attempt
					['0:00:17', u'1/2']

10 Student ID:seleon

	first_attempt
					2015-10-28 03:56:24
	part1_incorrect_attempt
					('0:00:00', u'1/3')
					('0:00:27', u'4/12')
	part1_correct_attempt
					['0:02:04', u'1/3 + 1/6']

11 Student ID:hak014

	first_attempt
					2015-10-26 23:21:48
	part1_incorrect_attempt
					('0:00:00', u'4/6')
	part1_correct_attempt
					['0:00:30', u'3/6']

12 Student ID:r9jiang

	first_attempt
					2015-10-24 07:45:05
	part1_incorrect_attempt
					('0:00:00', u'5/6')
	part1_correct_attempt
					['0:01:56', u'1/2']

13 Student ID:dac064

	first_attempt
					2015-10-30 22:47:37
	part1_incorrect_attempt
					('0:00:00', u'1/18')
	part1_correct_attempt
					['0:00:15', u'1/2']

14 Student ID:ajvanega

	first_attempt
					2015-10-30 17:09:55
	part1_incorrect_attempt
					('0:00:00', u'1/3')
	part1_correct_attempt
					['0:02:19', u'1/2']

15 Student ID:anislam

	first_attempt
					2015-10-29 23:33:35
	part1_incorrect_attempt
					('0:00:00', u'1/3')
	part1_correct_attempt
					['0:00:57', u'1/2']

16 Student ID:jmiclat

	first_attempt
					2015-10-29 02:44:09
	part1_incorrect_attempt
					('0:00:00', u'1/3')
	part1_correct_attempt
					['19:35:13', u'1/2']

17 Student ID:ytc012

	first_attempt
					2015-10-29 12:28:27
	part1_incorrect_attempt
					('0:00:00', u'2/3')
	part1_correct_attempt
					['0:00:09', u'1/2']

18 Student ID:acs008

	first_attempt
					2015-10-28 00:33:17
	part1_incorrect_attempt
					('0:00:00', u'1/3')
					('0:00:13', u'2/3')
	part1_correct_attempt
					['0:01:16', u'1/2']

19 Student ID:smohiman

	first_attempt
					2015-10-29 15:57:23
	part1_incorrect_attempt
					('0:00:00', u'1/3')
	part1_correct_attempt
					['0:01:17', u'1/2']

20 Student ID:vsosnovs

	first_attempt
					2015-10-30 06:38:23
	part1_incorrect_attempt
					('0:00:00', u'(1/3)+3')
	part1_correct_attempt
					['0:00:20', u'1/3+ 0 +1/6']












## Part 10

### (38) Mistake Group Fraction of size 38




### (24) Mistake Group Digits of size 24




### (3) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:k5law

	first_attempt
					2015-10-26 06:56:26
	part1_correct_attempt
					['0:00:00', u'(1/3)+(1/6)']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'(1/6)+(1/3)']
	part4_correct_attempt
					['0:00:00', u'(1/3)+(1/6)']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'(1/6)+(1/3)']
	part10_incorrect_attempt
					('0:18:48', u'(1/3)+(1/6)+(1/6)+(1/3)')
	part10_correct_attempt
					['0:23:00', u'(1/3)+(1/6)+[3*[(1/6)+(1/3)]]']

1 Student ID:apokhare

	first_attempt
					2015-10-29 21:20:04
	part1_correct_attempt
					['0:00:00', u'1/3 + 1/6']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/6+1/3']
	part4_correct_attempt
					['0:00:00', u'1/3+1/6']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/6+1/3']
	part10_incorrect_attempt
					('0:00:00', u'2(1/3 + 1/6)')
	part10_correct_attempt
					['0:02:25', u'(1/3 + 1/6)+ 3 * (1/6+1/3)']

2 Student ID:w4shin

	first_attempt
					2015-10-30 18:41:12
	part1_correct_attempt
					['0:00:00', u'1/3+1/6']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/6+1/3']
	part4_correct_attempt
					['0:00:00', u'1/3+1/6']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/6+1/3']
	part10_incorrect_attempt
					('0:00:00', u'(1/3+1/6)+(1/6+1/3)')
	part10_correct_attempt
					['0:04:44', u'1*(1/3+1/6)+3*(1/3+1/6)']












## Part 11

### (48) Mistake Group Digits of size 48




### (26) Mistake Group Fraction of size 26




### (4) Mistake Group Wrong_Sign of size 4




### (3) Mistake Group redirect of size 3




### (1) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:haw081

	first_attempt
					2015-10-27 03:20:00
	part1_correct_attempt
					['0:00:00', u'1/3+1/6']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/6+1/3']
	part4_correct_attempt
					['0:00:00', u'1/3+1/6']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/6+1/3']
	part9_correct_attempt
					['0:00:40', u'0.5+0+3*0.5']
	part10_correct_attempt
					['0:00:40', u'0.5+0+3*0.5']
	part11_incorrect_attempt
					('0:00:54', u'1+0+1')
	part11_correct_attempt
					['0:01:07', u'1+3']












## Part 12

### (509) Mistake Group Digits of size 509




### (20) Mistake Group Wrong_Sign of size 20




### (18) Mistake Group redirect of size 18




### (5) Mistake Group ['R.1.0.0'] of size 5
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|1*1/3+2*0+3*1/6+2*0+4*0+6*0+3*1/6+6*0+9*1/3	|[1*1*[(1/3)+(1/6)]*[(1/3)+(1/6)]]+0+[3*3*[(1/6)+(1/3)]*[(1/6)+(1/3)]]	|[('R.1.0.0', 9.0, u'9', u'3*3')]	|
|1	|1*1/3+2*0+3*1/6+2*0+4*0+6*0+3*1/6+6*0+9*1/3	|0.5*0.5+9*0.5*0.5	|[('R.1.0.0', 9.0, u'9', u'9')]	|
|2	|1*1/3+2*0+3*1/6+2*0+4*0+6*0+3*1/6+6*0+9*1/3	|[1*1*(1/2)*(1/2)]+[3*3*(1/2)*(1/2)]	|[('R.1.0.0', 9.0, u'9', u'3*3')]	|
|3	|1*1/3+2*0+3*1/6+2*0+4*0+6*0+3*1/6+6*0+9*1/3	|((3/6)(3/6))+((9/6)(9/6))	|[('R.1.0.0', 9.0, u'9', u'9')]	|
|4	|1*1/3+2*0+3*1/6+2*0+4*0+6*0+3*1/6+6*0+9*1/3	|1*.5*(1/2)+3*3*(3/6)*.5	|[('R.1.0.0', 9.0, u'9', u'3*3')]	|




### (3) Mistake Group ['R.0.0'] of size 3
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|1*1/3+2*0+3*1/6+2*0+4*0+6*0+3*1/6+6*0+9*1/3	|1/3+0+1+1/2+1/2	|[('R.0.0', 1.3333333333333333, u'1*1/3+2*0+3*1/6+2*0+4*0+6*0+3*1/6', u'1/3+0+1')]	|
|1	|1*1/3+2*0+3*1/6+2*0+4*0+6*0+3*1/6+6*0+9*1/3	|(2/3+4/6+2/6+6/3)	|[('R.0.0', 1.3333333333333333, u'1*1/3+2*0+3*1/6+2*0+4*0+6*0+3*1/6', u'2/3+4/6')]	|
|2	|1*1/3+2*0+3*1/6+2*0+4*0+6*0+3*1/6+6*0+9*1/3	|(2/3+4/6+4/6+6/3)	|[('R.0.0', 1.3333333333333333, u'1*1/3+2*0+3*1/6+2*0+4*0+6*0+3*1/6', u'2/3+4/6')]	|




### (2) Mistake Group ['R.0.0.0.0.0.0.1', 'R.0.0.0.0.1.0'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0.0.0.0.1', 'R.0.0.0.0.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|1*1/3+2*0+3*1/6+2*0+4*0+6*0+3*1/6+6*0+9*1/3	|1*1/3 + 2*0 + 3*1/6 + 2*0+ 4*0 + 6*0 + 3*1/3  + 6*0 + 9*1/3 	|[('R.0.0.0.0.0.0.1', 0.5, u'3*1/6', u'3*1/6'), ('R.0.0.0.0.1.0', 4.0, u'4', u'4')]	|
|1	|1*1/3+2*0+3*1/6+2*0+4*0+6*0+3*1/6+6*0+9*1/3	|1*(1/3) + 2*0 + 3*(1/6) + 2*0 + 4*0 + 6*0 + 3*(1/3) + 6*0 + 9*(1/6)	|[('R.0.0.0.0.0.0.1', 0.5, u'3*1/6', u'3*(1/6)'), ('R.0.0.0.0.1.0', 4.0, u'4', u'4')]	|




### (1) Mistake Group ['R.0.0.0.0.1.0'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0.0.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|1*1/3+2*0+3*1/6+2*0+4*0+6*0+3*1/6+6*0+9*1/3	|1*(1/3+1/6) + 2*0 + 3*(1/3+1/6) + 2*(1/3+1/6) + 4*0 + 6*(1/3+1/6) + 3*(1/3+1/6) + 6*0 + 9*(1/3+1/6)	|[('R.0.0.0.0.1.0', 4.0, u'4', u'4')]	|




### (1) Mistake Group ['R.0.0.0.0.0.0', 'R.0.0.0.0.1.0'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0.0.0.0', 'R.0.0.0.0.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|1*1/3+2*0+3*1/6+2*0+4*0+6*0+3*1/6+6*0+9*1/3	|1*(1/3) + 2*0 + 3*(1/6) + 2*(1/3) + 4*0 + 6*(1/6) + 3*(1/3) + 6*0 + 9*(1/6)	|[('R.0.0.0.0.0.0', 0.8333333333333333, u'1*1/3+2*0+3*1/6', u'1*(1/3) + 2*0 + 3*(1/6)'), ('R.0.0.0.0.1.0', 4.0, u'4', u'4')]	|




### (118) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:gthorn

	first_attempt
					2015-10-26 23:38:56
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:00:56', u'1/2 + 3/2']
	part10_correct_attempt
					['0:00:56', u'1/2 + 3/2']
	part12_incorrect_attempt
					('17:25:21', u'2/6')
	part12_correct_attempt
					['17:28:03', u'4 + 2/6']

1 Student ID:apokhare

	first_attempt
					2015-10-29 21:20:04
	part1_correct_attempt
					['0:00:00', u'1/3 + 1/6']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/6+1/3']
	part4_correct_attempt
					['0:00:00', u'1/3+1/6']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/6+1/3']
	part9_correct_attempt
					['0:02:25', u'(1/3 + 1/6) + 3 * (1/6+1/3)']
	part10_correct_attempt
					['0:02:25', u'(1/3 + 1/6)+ 3 * (1/6+1/3)']
	part12_incorrect_attempt
					('0:02:48', u'[(1/3 + 1/6) + 3 * (1/6+1/3)]^2')
					('0:03:26', u'[(1/3 + 1/6) + 3 * (1/6+1/3)]* [(1/3 + 1/6)+ 3 * (1/6+1/3)]')
	part12_correct_attempt
					['0:07:39', u'1/3 + 3*(1/6)+ 3*(1/6)+9*(1/3)']

2 Student ID:v4zhang

	first_attempt
					2015-10-30 09:34:23
	part1_correct_attempt
					['0:00:00', u'(1/3)+(0)+(1/6)']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'(1/6)+0+(1/3)']
	part4_correct_attempt
					['0:00:00', u'(1/3)+(0)+(1/6)']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'(1/6)+0+(1/3)']
	part9_correct_attempt
					['0:02:13', u'(1*.5)+(0)+(3*.5)']
	part10_correct_attempt
					['0:02:13', u'(1*.5)+(0)+(3*.5)']
	part12_incorrect_attempt
					('0:35:09', u'14*4')
					('0:38:21', u'3+(1/3)')
	part12_correct_attempt
					['12:42:55', u'(1/3)+(1/2)+(1/2)+3']

3 Student ID:kvass

	first_attempt
					2015-10-26 20:21:19
	part1_correct_attempt
					['0:00:00', u'1/3+1/6']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/3+1/6']
	part4_correct_attempt
					['0:00:16', u'1/3+1/6']
	part5_correct_attempt
					['0:00:16', u'0']
	part6_correct_attempt
					['0:00:16', u'1/3+1/6']
	part9_correct_attempt
					['0:06:42', u'4*(1/3+1/6)']
	part10_correct_attempt
					['0:06:42', u'4*(1/3+1/6)']
	part12_incorrect_attempt
					('0:21:14', u'2*4*(1/3+1/6)')
					('0:21:51', u'(4*(1/3+1/6))**2')
					('0:37:55', u'4*(1/6+1/12)')
					('0:39:30', u'7*(1/3+1/6)')
					('0:51:25', u'1*1/3*3*1/6+3*1/6+9*1/3')
	part12_correct_attempt
					['0:52:30', u'(1/3+3*1/6+3*1/6+9*1/3)']

4 Student ID:ssamudra

	first_attempt
					2015-10-30 22:05:32
	part1_correct_attempt
					['0:00:00', u'1/3 + 1/6']
	part2_correct_attempt
					['0:01:07', u'0']
	part3_correct_attempt
					['0:01:07', u'1/ 6+ 1/3']
	part4_correct_attempt
					['0:01:07', u'1/3 + 1/6']
	part5_correct_attempt
					['0:01:07', u'0']
	part6_correct_attempt
					['0:01:07', u'1/6 + 1/3']
	part9_correct_attempt
					['0:01:51', u'1/3 + 1/2 + 1/6 + 1']
	part10_correct_attempt
					['0:02:26', u'1/3 + 1/2 + 1/6 + 1']
	part12_incorrect_attempt
					('0:02:26', u'(1/3 + 1/2 + 1/6 + 1)(1/3 + 1/2 + 1/6 + 1)')
	part12_correct_attempt
					['0:35:38', u'1/3 + 1/2 + 1/2 + 3']

5 Student ID:mhale

	first_attempt
					2015-10-28 21:54:57
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:02:51', u'2']
	part10_correct_attempt
					['0:02:51', u'2']
	part12_incorrect_attempt
					('0:13:12', u'9/2 + 1/2')
	part12_correct_attempt
					['0:18:27', u'(1/3) + 3(1/6) + 3(1/6) + 9(1/3) ']

6 Student ID:nhn018

	first_attempt
					2015-10-29 04:11:08
	part1_correct_attempt
					['0:00:00', u'1/3+1/6']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/3+1/6']
	part4_correct_attempt
					['0:00:48', u'1/3+1/6']
	part5_correct_attempt
					['0:00:48', u'0']
	part6_correct_attempt
					['0:00:48', u'1/3+1/6']
	part9_correct_attempt
					['0:05:36', u'4*(1/3+1/6)']
	part10_correct_attempt
					['0:06:14', u'4*(1/3+1/6)']
	part12_incorrect_attempt
					('0:12:18', u'4*(1/3+1/6)*4*(1/3+1/6)')
	part12_correct_attempt
					['1:36:49', u'1*1*1/3+3/6+3/6+9/3']

7 Student ID:haw081

	first_attempt
					2015-10-27 03:20:00
	part1_correct_attempt
					['0:00:00', u'1/3+1/6']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/6+1/3']
	part4_correct_attempt
					['0:00:00', u'1/3+1/6']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/6+1/3']
	part9_correct_attempt
					['0:00:40', u'0.5+0+3*0.5']
	part10_correct_attempt
					['0:00:40', u'0.5+0+3*0.5']
	part12_incorrect_attempt
					('0:01:50', u'0.5*0.5+0+3*0.5*0.5')
					('2:10:10', u'4/9')
					('2:10:23', u'2(4/9)')
					('2:12:54', u'0.5*0.5+0.5*3*0.5+0.5*0.5*3+0.5*0.5*9')
	part12_correct_attempt
					['22:34:18', u'13/3']

8 Student ID:vqt004

	first_attempt
					2015-10-30 07:33:42
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:00:00', u'2']
	part10_correct_attempt
					['0:00:00', u'2']
	part12_incorrect_attempt
					('0:00:00', u'1/3+3/6+3/6+2')
	part12_correct_attempt
					['0:11:50', u'1/3+3/6+3/6+9/3']

9 Student ID:r9jiang

	first_attempt
					2015-10-24 07:47:01
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['-1 day, 23:58:04', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['-1 day, 23:58:04', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:00:00', u'2']
	part10_correct_attempt
					['0:00:00', u'2']
	part12_incorrect_attempt
					('4 days, 18:49:09', u'1/3')
					('4 days, 18:55:49', u'0.33')
					('4 days, 19:00:16', u'(1/3)*(1-2)*(1-2)+(1/6)*(3-2)*(1-2)+(1/6)*(1-2)*(3-2)+(1/3)*(3-2)*(3-2)')
	part12_correct_attempt
					['4 days, 19:17:14', u'13/3']

10 Student ID:btn023

	first_attempt
					2015-10-30 06:21:15
	part1_correct_attempt
					['0:00:00', u'1/3+1/6']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/6+1/3']
	part4_correct_attempt
					['0:00:00', u'1/6+1/3']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/6+1/3']
	part9_correct_attempt
					['0:00:00', u'1/2*1 + 1/2*3']
	part10_correct_attempt
					['0:00:00', u'1/2*1 + 1/2*3']
	part12_incorrect_attempt
					('0:00:57', u'(1/2*1 + 1/2*3)^2')
					('0:01:22', u'(1/2*1 + 1/2*3)*(1/2*1 + 1/2*3)')
					('0:29:00', u'(1/3+1/6+1/6+3*1/3+3*1/6)')
	part12_correct_attempt
					['0:29:17', u'(1/3+1/6+1/6+3*1/3+3*1/6)*2']

11 Student ID:dgunawan

	first_attempt
					2015-10-29 23:52:19
	part1_correct_attempt
					['0:00:00', u'(1/3) + (1/6)']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'(1/3) + (1/6)']
	part4_correct_attempt
					['0:00:00', u'(1/3) + (1/6)']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'(1/3) + (1/6)']
	part9_correct_attempt
					['0:03:12', u'(1/2) + 0 + 3/2']
	part10_correct_attempt
					['0:03:28', u'(1/2) + 0 + 3/2']
	part12_incorrect_attempt
					('0:03:38', u'[(1/2) + 0 + 3/2]*2')
					('0:04:32', u'[(1/2) + 0 + 3/2] * [(1/2) + 0 + 3/2]')
					('0:05:58', u'[(1/2) + 0 + 3/2]*2')
					('0:07:47', u'(1/2) + 0 + 3/2 *2')

12 Student ID:mpanelo

	first_attempt
					2015-10-23 21:19:38
	part1_correct_attempt
					['0:00:00', u'.5']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'.5']
	part4_correct_attempt
					['0:00:00', u'.5']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'.5']
	part9_correct_attempt
					['0:00:00', u'2']
	part10_correct_attempt
					['0:00:00', u'2']
	part12_incorrect_attempt
					('0:10:16', u'10/3')
	part12_correct_attempt
					['2:44:39', u'13/3']

13 Student ID:pthsu

	first_attempt
					2015-10-23 22:26:05
	part1_correct_attempt
					['0:00:00', u'(1/6)+(1/3)']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'(1/6)+(1/3)']
	part4_correct_attempt
					['0:00:00', u'(1/6)+(1/3)']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'(1/6)+(1/3)']
	part9_correct_attempt
					['0:01:47', u'.5+1.5']
	part10_correct_attempt
					['0:02:01', u'.5+1.5']
	part12_incorrect_attempt
					('0:02:20', u'(.5+1.5)(.5+1.5)')
					('0:11:51', u'.5+1.5+.5+1.5 - ((.5+1.5)(.5+1.5))')
					('0:15:26', u'[(1/2)*1]+[(1/6)*3]+[(1/6)*3]+[(1/3)*9]')
					('0:18:16', u'[(.5*.5)*1]+[(.5*.5)*3]+[(.5*.5)*3]+[(.5*.5)*9]')
					('0:25:05', u'.5*4**2-1')
					('0:27:09', u'(1/2)*[(.5+1.5+.5+1.5)^2 - (9*.5+.5)- (9*.5+.5)]')
					('0:28:22', u'(1/2)*[(.5+3.5+.5+3.5)^2 - (9*.5+.5)- (9*.5+.5)]')
					('0:28:48', u'(1/2)*[(.5+4.5+.5+4.5)^2 - (9*.5+.5)- (9*.5+.5)]')
					('1:07:04', u'(.5*.5*1) + (.5*.5*3) + (.5*.5*3) + (.5*.5*9)')
	part12_correct_attempt
					['1:13:10', u'(1/3) + (3/6) + (3/6) + (9/3)']

14 Student ID:tcuddy

	first_attempt
					2015-10-27 19:10:36
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:00:00', u'2']
	part10_correct_attempt
					['0:00:00', u'2']
	part12_incorrect_attempt
					('0:06:29', u'10/4')
					('0:24:43', u'7/3')
	part12_correct_attempt
					['0:25:33', u'(1/3)+(3)(1/6)+(3/6)+3']

15 Student ID:l8ngo

	first_attempt
					2015-10-23 21:40:37
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:00:00', u'2']
	part10_correct_attempt
					['0:00:00', u'2']
	part12_incorrect_attempt
					('4 days, 22:36:44', u'2.5')
					('4 days, 23:08:46', u'10/3')
	part12_correct_attempt
					['4 days, 23:16:27', u'1/3+4']

16 Student ID:djk006

	first_attempt
					2015-10-29 22:12:06
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:00:00', u'2']
	part10_correct_attempt
					['0:00:00', u'2']
	part12_incorrect_attempt
					('0:00:00', u'16/3')
					('0:05:15', u'32/6')
	part12_correct_attempt
					['0:05:56', u'13/3']

17 Student ID:dsriniva

	first_attempt
					2015-10-30 17:33:38
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:00:45', u'2']
	part10_correct_attempt
					['0:00:45', u'2']
	part12_incorrect_attempt
					('0:04:07', u'1/3*3/6')
					('0:04:17', u'1/3+3/6')
	part12_correct_attempt
					['0:05:55', u'1/3+3/6+9/3+3/6']

18 Student ID:chc286

	first_attempt
					2015-10-25 09:27:51
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:01:27', u'1/2+3*(1/2)']
	part10_correct_attempt
					['0:01:27', u'1/2+3*(1/2)']
	part12_incorrect_attempt
					('0:01:38', u'2*2')
	part12_correct_attempt
					['12:35:08', u'1*(1/3)+3*(1/6)+3*(1/6)+9*(1/3)']

19 Student ID:glcohen

	first_attempt
					2015-10-27 16:04:01
	part1_correct_attempt
					['0:00:00', u'(1/3)+(1/6)']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'(1/3)+(1/6)']
	part4_correct_attempt
					['0:00:00', u'(1/3)+(1/6)']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'(1/3)+(1/6)']
	part9_correct_attempt
					['0:01:12', u'1((1/3)+(1/6))+3((1/3)+(1/6))']
	part10_correct_attempt
					['0:01:12', u'1((1/3)+(1/6))+3((1/3)+(1/6))']
	part12_incorrect_attempt
					('2:14:41', u'((2/9)^2 + (2/9)^2 + (0.5/9)^2 + (0.5/9)^2 + (1/9)^2 + (1/9)^2 + (1/9)^2 + (1/9)^2)/9')
					('2:16:42', u'4/6')
	part12_correct_attempt
					['2:39:10', u'(1/3)+2(3(1/6))+9(1/3)']

20 Student ID:anvan

	first_attempt
					2015-10-30 18:20:16
	part1_correct_attempt
					['0:00:00', u'1/3 + 1/6']
	part3_correct_attempt
					['0:00:00', u'1/3 + 1/6']
	part4_correct_attempt
					['0:00:00', u'1/3 + 1/6']
	part6_correct_attempt
					['0:00:00', u'1/3 + 1/6']
	part9_correct_attempt
					['0:00:30', u'1/3 + 1/6 + (1/3 + 1/6)*3']
	part10_correct_attempt
					['0:00:30', u'1/3 + 1/6 + (1/3 + 1/6)*3']
	part12_incorrect_attempt
					('0:00:48', u'(1/3 + 1/6 + (1/3 + 1/6)*3)(1/3 + 1/6 + (1/3 + 1/6)*3)')
					('2:14:11', u'2.5')
					('2:15:57', u'.25 + 3 * .25')
					('2:51:53', u'(1/3 + 1/6 + (1/3 + 1/6)*3) + (1/3 + 1/6) + 2')
	part12_correct_attempt
					['3:03:19', u'1/3 + 1/2 + 1/2 + 3']

21 Student ID:csl030

	first_attempt
					2015-10-29 23:59:31
	part1_correct_attempt
					['0:00:00', u'1/3 + 1/6']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/3 + 1/6']
	part4_correct_attempt
					['0:00:00', u'1/3 + 1/6']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/6 + 1/3']
	part9_correct_attempt
					['0:07:15', u'2']
	part10_correct_attempt
					['0:07:15', u'2']
	part12_incorrect_attempt
					('0:19:50', u'4(1/3^2)')
					('0:20:24', u'4(1/3 + 1/6)')
					('0:20:49', u'4(1/3 * 1/6)')
					('0:24:04', u'4(1/3 + 1/3)')

22 Student ID:jguanzho

	first_attempt
					2015-10-23 03:29:23
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:00:00', u'1/2+3/2']
	part10_correct_attempt
					['0:00:00', u'1/2+3/2']
	part12_incorrect_attempt
					('2:24:22', u'(1/2+3/2)**2')
					('5:05:09', u'1/2((2*(1/2+3/2))**2-2*(1/2+3/2))')
					('5:06:16', u'1/2((2*(1/2+3/2))**2-2*(1/2+3/2)**2)')
					('5:07:59', u'1/2+3/2')
					('5:22:39', u'2**2')
					('3 days, 17:30:36', u'((1/3)**2)/4+((1/6)**2)/4+((1/6)**2)/4+((1/3)**2)/4')
					('3 days, 17:31:41', u'2*(((1/3)**2)/4+((1/6)**2)/4+((1/6)**2)/4+((1/3)**2)/4)')
					('5 days, 21:17:58', u'1*1*1/4+3*1*1/2+1*3*1/4+3*3*1/4')
					('5 days, 21:18:12', u'1*1*1/4+3*1*1/4+1*3*1/4+3*3*1/4')
					('5 days, 21:18:37', u'1*1*1/9+3*1*1/9+1*3*1/9+3*3*1/9')
					('5 days, 21:24:19', u'(1/4)(1*1*1/9+3*1*1/9+1*3*1/9+3*3*1/9)')
					('5 days, 21:24:36', u'(1/4)(1*1*1/4+3*1*1/4+1*3*1/4+3*3*1/4)')
					('6 days, 0:33:03', u'1/9+1/3+1/9+1')
	part12_correct_attempt
					['6 days, 0:43:11', u'((-1*-1)/3+(1*-1)/6+(1*-1)/6+1/3)+2*(1/2+3/2)']

23 Student ID:yos017

	first_attempt
					2015-10-29 08:21:58
	part1_correct_attempt
					['0:00:00', u'1/3 + 1/6']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/6 + 1/3']
	part4_correct_attempt
					['0:00:14', u'1/3 + 1/6']
	part5_correct_attempt
					['0:00:14', u'0']
	part6_correct_attempt
					['0:00:14', u'1/3 + 1/6']
	part9_correct_attempt
					['0:01:53', u'2']
	part10_correct_attempt
					['0:01:53', u'2']
	part12_incorrect_attempt
					('0:07:48', u'10(0.5)^2')
	part12_correct_attempt
					['0:17:25', u'1/3 + 1/2 + 1/2 + 3']

24 Student ID:small

	first_attempt
					2015-10-30 23:45:51
	part1_correct_attempt
					['0:00:00', u'1/3 + 1/6']
	part2_correct_attempt
					['0:00:22', u'0']
	part3_correct_attempt
					['0:00:22', u'1/3 + 1/6']
	part4_correct_attempt
					['0:00:43', u'1/3 + 1/6']
	part5_correct_attempt
					['0:00:43', u'0']
	part6_correct_attempt
					['0:00:43', u'1/3 + 1/6']
	part9_correct_attempt
					['-1 day, 23:58:15', u'1']
	part12_incorrect_attempt
					('0:07:57', u'2(1/3 + 1/6 + 1 + 1/2)')

25 Student ID:ggaddi

	first_attempt
					2015-10-27 15:45:54
	part1_correct_attempt
					['0:00:00', u'1/3+1/6']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/6+1/3']
	part4_correct_attempt
					['0:00:00', u'1/3+1/6']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/3+1/6']
	part9_correct_attempt
					['0:06:56', u'1*0.5 + 3*0.5']
	part10_correct_attempt
					['0:06:56', u'1*0.5 + 3*0.5']
	part12_incorrect_attempt
					('0:06:56', u'(1*0.5 + 3*0.5)*(1*0.5 + 3*0.5)')
					('0:08:57', u'1*1*1/3+1*3*1/6 +1*3*1/6 + 1*3*1/3')
	part12_correct_attempt
					['0:15:50', u'1*1*1/3+1*3*1/6 +1*3*1/6 + 3*3*1/3']

26 Student ID:b3hwang

	first_attempt
					2015-10-28 03:26:18
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:00:00', u'(1/2) + 0 + 3/2']
	part10_correct_attempt
					['0:00:00', u'(1/2) + 0 + 3/2']
	part12_incorrect_attempt
					('0:00:00', u'((1/2) + 0 + 3/2) * ((1/2) + 0 + 3/2)')

27 Student ID:jag028

	first_attempt
					2015-10-30 14:50:53
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['-1 day, 23:59:23', u'0']
	part3_correct_attempt
					['0:00:21', u'1/2']
	part4_correct_attempt
					['0:00:21', u'1/2']
	part5_correct_attempt
					['-1 day, 23:59:23', u'0']
	part6_correct_attempt
					['0:00:21', u'1/2']
	part9_correct_attempt
					['0:02:47', u'1/2+3(1/2)']
	part10_correct_attempt
					['0:02:47', u'1/2+3(1/2)']
	part12_incorrect_attempt
					('0:25:22', u'1/2')
					('3:45:41', u'.2')
	part12_correct_attempt
					['6:57:58', u'1/3+3(1/6)+3(1/6)+9(1/3)']

28 Student ID:ccn001

	first_attempt
					2015-10-28 00:02:51
	part1_correct_attempt
					['0:00:00', u'(1/3)+(1/6)']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'(1/3)+(1/6)']
	part4_correct_attempt
					['0:00:00', u'(1/3)+(1/6)']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'(1/3)+(1/6)']
	part9_correct_attempt
					['0:00:00', u'(1/3)+(1/6)+(3/6)+1']
	part10_correct_attempt
					['0:00:00', u'(1/3)+(1/6)+(3/6)+1']
	part12_incorrect_attempt
					('0:00:00', u'((1/3)+(1/6)+(3/6)+1)((1/3)+(1/6)+(3/6)+1)')
	part12_correct_attempt
					['1 day, 3:17:16', u'1(1/3)+(1/6)(3)+(1/6)(3)+(1/3)(3)(3)']

29 Student ID:lguintu

	first_attempt
					2015-10-24 23:58:18
	part1_correct_attempt
					['0:00:00', u'3/6']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'3/6']
	part4_correct_attempt
					['0:00:46', u'3/6']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:46', u'3/6']
	part9_correct_attempt
					['0:01:37', u'(3+9)/6']
	part10_correct_attempt
					['0:01:37', u'(3+9)/6']
	part12_incorrect_attempt
					('0:01:55', u'((3+9)/6)^2')
	part12_correct_attempt
					['0:48:22', u'1/3+3/6+3/6+9/3']

30 Student ID:jjchung

	first_attempt
					2015-10-27 00:06:18
	part1_correct_attempt
					['0:00:00', u'3/6']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'3/6']
	part4_correct_attempt
					['0:00:00', u'3/6']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'3/6']
	part9_correct_attempt
					['0:00:00', u'(1*(3/6))+(2*0)+(3*(3/6))']
	part10_correct_attempt
					['0:00:00', u'(1*(3/6))+(2*0)+(3*(3/6))']
	part12_incorrect_attempt
					('0:00:00', u' 2*[(1*(3/6))+(2*0)+(3*(3/6))]')
	part12_correct_attempt
					['0:01:46', u'(1/3)+(3/6)+(1/2)+(3)']

31 Student ID:abjara

	first_attempt
					2015-10-27 20:41:04
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:00:00', u'1/2 + 3*.5']
	part10_correct_attempt
					['0:00:00', u'1/2 + 3*.5']
	part12_incorrect_attempt
					('0:00:00', u'(1/2 + 3*.5)*(1/2 + 3*.5)')
					('0:20:57', u'1*4 +8 +12')
	part12_correct_attempt
					['1 day, 14:20:00', u'13/3']

32 Student ID:cprafull

	first_attempt
					2015-10-30 03:10:53
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:00:00', u'2']
	part10_correct_attempt
					['0:00:00', u'2']
	part12_incorrect_attempt
					('0:00:00', u'16/3')
	part12_correct_attempt
					['0:00:10', u'13/3']

33 Student ID:sachadal

	first_attempt
					2015-10-24 19:36:34
	part1_correct_attempt
					['0:00:00', u'(1/3)+0+(1/6)']
	part2_correct_attempt
					['0:00:00', u'0+0+0']
	part3_correct_attempt
					['0:00:00', u'(1/6)+0+(1/3)']
	part4_correct_attempt
					['0:00:00', u'(1/3)+0+(1/6)']
	part5_correct_attempt
					['0:00:00', u'0+0+0']
	part6_correct_attempt
					['0:00:00', u'(1/6)+0+(1/3)']
	part9_correct_attempt
					['0:00:00', u'(1*(3/6))+(2*0)+(3*(3/6))']
	part10_correct_attempt
					['0:00:00', u'(1*(3/6))+(2*0)+(3*(3/6))']
	part12_incorrect_attempt
					('0:00:00', u'((1*(3/6))+(2*0)+(3*(3/6)))((1*(3/6))+(2*0)+(3*(3/6)))')
	part12_correct_attempt
					['4 days, 20:03:23', u'2*2+1/3']

34 Student ID:kthui

	first_attempt
					2015-10-25 03:12:33
	part1_correct_attempt
					['0:00:00', u'1/3+1/6']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/6+1/3']
	part4_correct_attempt
					['0:00:00', u'1/3+1/6']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/6+1/3']
	part9_correct_attempt
					['0:01:44', u'1*(1/2)+2*0+3*(1/2)']
	part10_correct_attempt
					['0:02:05', u'1*(1/2)+2*0+3*(1/2)']
	part12_incorrect_attempt
					('0:02:21', u'(1*(1/2)+2*0+3*(1/2))*(1*(1/2)+2*0+3*(1/2))')
					('0:08:02', u'1*(1/3)*(1/3)+2*0*0+3*(1/3)*(1/3)')
					('0:09:38', u'1*(1/2)*(1/2)+2*0*0+3*(1/2)*(1/2)')
					('0:24:34', u'1*(1/3)+2*(0)+3*(1/3)')
					('0:24:45', u'1*(1/6)+2*(0)+3*(1/6)')
					('0:25:05', u'1*(1/4)+2*(0)+3*(1/4)')
					('0:25:39', u'1.5')
					('3 days, 22:21:13', u'(1/2)*(1/2)*1+0*0*0+(1/2)*(1/2)*3')
					('3 days, 22:21:31', u'(1/2)*(1/2)*1+0*0*2+(1/2)*(1/2)*3')
					('3 days, 22:25:02', u'(1/2)*(1/2)*1+0*0*4+(1/2)*(1/2)*9')
					('3 days, 22:26:57', u'(1/2)*(1/2)*1+0*0*4+(1/2)*(1/2)*6')
					('3 days, 22:27:11', u'3.5')
					('3 days, 22:27:23', u'4.5')
					('3 days, 22:27:34', u'5.5')
					('3 days, 22:27:45', u'6.5')
					('3 days, 22:27:56', u'7.5')
					('3 days, 22:28:07', u'8.5')
					('3 days, 22:28:18', u'9.5')
	part12_correct_attempt
					['3 days, 22:58:59', u'(1*1)(1/3)+(1*2)(0)+(1*3)(1/6)+(2*1)(0)+(2*2)(0)+(2*3)(0)+(3*1)(1/6)+(3*2)(0)+(3*3)(1/3)']

35 Student ID:alhung

	first_attempt
					2015-10-30 22:54:37
	part1_correct_attempt
					['0:00:00', u'3/6']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'3/6']
	part4_correct_attempt
					['0:00:00', u'3/6']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'3/6']
	part9_correct_attempt
					['0:00:00', u'[1*(3/6)+2*0+3*(3/6)]']
	part10_correct_attempt
					['0:00:00', u'[1*(3/6)+2*0+3*(3/6)]']
	part12_incorrect_attempt
					('0:00:00', u'[1*(3/6)+2*0+3*(3/6)]*[1*(3/6)+2*0+3*(3/6)]')
	part12_correct_attempt
					['0:04:05', u'(1/3)+(1/2)+(1/2)+3']

36 Student ID:beyounge

	first_attempt
					2015-10-23 06:18:16
	part1_correct_attempt
					['0:00:00', u'3/6']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'3/6']
	part4_correct_attempt
					['0:00:00', u'3/6']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'3/6']
	part9_correct_attempt
					['0:01:06', u'2']
	part10_correct_attempt
					['0:01:06', u'2']
	part12_incorrect_attempt
					('0:18:52', u'20/6')
					('0:40:16', u'2/3')
					('0:44:32', u'1/2')
					('0:44:50', u'9/36')
					('13:50:01', u'5/6')
					('13:50:14', u'10/6')
					('13:50:47', u'20/6')
					('14:02:01', u'8/3')
					('14:03:22', u'20/6')
					('14:05:11', u'1/4')
					('14:05:19', u'1/16')
					('14:07:19', u'1/3')
					('14:07:29', u'2/3')
					('14:07:40', u'1/9')
					('14:07:52', u'4/9')
					('14:09:30', u'(1/9) * (1/36)')
					('14:36:32', u'4/3')
					('14:36:42', u'4/6')
					('14:42:49', u'26/3')
	part12_correct_attempt
					['14:43:02', u'26/6']

37 Student ID:jic212

	first_attempt
					2015-10-24 20:12:06
	part1_correct_attempt
					['0:00:00', u'(1/3)+(1/6)']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:09', u'(1/6)+(1/3)']
	part4_correct_attempt
					['0:00:00', u'(1/3)+(1/6)']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'(1/6)+(1/3)']
	part9_correct_attempt
					['0:02:26', u'1*0.5+0+3*0.5']
	part10_correct_attempt
					['0:02:26', u'1*0.5+0+3*0.5']
	part12_incorrect_attempt
					('0:07:51', u'1/3+0+3*3*(1/3)')
	part12_correct_attempt
					['0:08:53', u'1*1*1/3+0+3*1*1/6+0+0+0+1*3*(1/6)+0+3*3*(1/3)']

38 Student ID:tpmach

	first_attempt
					2015-10-23 22:19:47
	part1_correct_attempt
					['0:00:00', u'1/3+1/6']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/6+1/3']
	part4_correct_attempt
					['0:00:27', u'1/3+1/6']
	part5_correct_attempt
					['0:00:27', u'0']
	part6_correct_attempt
					['0:00:27', u'1/6+1/3']
	part9_correct_attempt
					['0:04:56', u'1(1/3+1/6)+3(1/3+1/6)']
	part10_correct_attempt
					['0:04:09', u'1(1/3+1/6)+3(1/3+1/6)']
	part12_incorrect_attempt
					('2 days, 2:01:02', u'2*4')
					('2 days, 2:01:26', u'2*2')
					('2 days, 2:04:01', u'2*2')
	part12_correct_attempt
					['3 days, 17:29:08', u'1*1*1/3+1*3*1/6+1*3*1/6+3*3*1/3']

39 Student ID:hak014

	first_attempt
					2015-10-26 23:22:18
	part1_correct_attempt
					['0:00:00', u'3/6']
	part2_correct_attempt
					['-1 day, 23:59:30', u'0']
	part3_correct_attempt
					['0:00:00', u'3/6']
	part4_correct_attempt
					['0:00:00', u'3/6']
	part5_correct_attempt
					['-1 day, 23:59:30', u'0']
	part6_correct_attempt
					['0:00:00', u'3/6']
	part9_correct_attempt
					['19:56:19', u'(1/2)+(3/2)']
	part10_correct_attempt
					['19:56:45', u'(1/2)+(3/2)']
	part12_incorrect_attempt
					('20:02:39', u'1+(1/3)')
					('20:08:35', u'(1/4)+(3)')
					('20:45:08', u'7.111')
	part12_correct_attempt
					['2 days, 0:03:04', u'(1/3)+(3/6)+(1/2)+(3)']

40 Student ID:dwzhang

	first_attempt
					2015-10-30 04:54:18
	part1_correct_attempt
					['0:00:00', u'1/3 + 1/6']
	part2_correct_attempt
					['-1 day, 23:58:57', u'0']
	part3_correct_attempt
					['0:00:00', u'1/6 + 1/3']
	part4_correct_attempt
					['0:00:00', u'1/3 + 1/6']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/6 + 1/3']
	part9_correct_attempt
					['0:05:22', u'(1/3 + 1/6) + 3(1/6 + 1/3)']
	part10_correct_attempt
					['0:05:22', u'(1/3 + 1/6) + 3(1/6 + 1/3)']
	part12_incorrect_attempt
					('0:10:19', u'(1/3 + 1/6)^2 + (3(1/6 + 1/3))^2')
					('16:16:55', u'(1*1*1/3) + (3*3*1/3)')
	part12_correct_attempt
					['16:18:16', u'(1*1*1/3)+(3*1*1/6)+(3*1*1/6)+(3*3*1/3)']

41 Student ID:rraiyyan

	first_attempt
					2015-10-28 01:29:29
	part1_correct_attempt
					['0:00:00', u'1/2']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['-1 day, 23:49:54', u'1/2']
	part5_correct_attempt
					['-1 day, 23:49:54', u'0']
	part6_correct_attempt
					['-1 day, 23:49:54', u'1/2']
	part9_correct_attempt
					['0:01:03', u'2']
	part10_correct_attempt
					['0:01:03', u'2']
	part12_incorrect_attempt
					('0:23:21', u'35/6')
					('0:23:58', u'35/36')
					('0:28:03', u'14/6')
	part12_correct_attempt
					['0:30:10', u'26/6']

42 Student ID:jhw015

	first_attempt
					2015-10-28 00:38:30
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:17', u'1/2']
	part5_correct_attempt
					['0:00:17', u'0']
	part6_correct_attempt
					['0:00:17', u'1/2']
	part9_correct_attempt
					['0:01:45', u'2']
	part10_correct_attempt
					['0:01:45', u'2']
	part12_incorrect_attempt
					('2 days, 16:55:40', u'14/6')
	part12_correct_attempt
					['2 days, 16:59:23', u'26/6']

43 Student ID:ajabasa

	first_attempt
					2015-10-29 23:03:26
	part1_correct_attempt
					['0:00:00', u'3/6']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'3/6']
	part4_correct_attempt
					['0:00:16', u'3/6']
	part5_correct_attempt
					['0:00:16', u'0']
	part6_correct_attempt
					['0:00:16', u'3/6']
	part9_correct_attempt
					['0:01:57', u'1/2+9/6']
	part10_correct_attempt
					['0:01:57', u'1/2+9/6']
	part12_incorrect_attempt
					('0:13:02', u'1*(1/2)*(1/2)+3*3*(3/6)')
					('0:13:14', u'1*(1/2)+3*3*(3/6)')
					('0:16:05', u'1/3+3*3*(1/3)')
	part12_correct_attempt
					['0:25:42', u'1/3+3*(1/6)+3*(1/6)+3*3*(1/3)']

44 Student ID:jel075

	first_attempt
					2015-10-29 02:21:45
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:01:37', u'1/2+3/2']
	part10_correct_attempt
					['0:01:37', u'1/2+3/2']
	part12_incorrect_attempt
					('0:01:59', u'2(1/2+3/2)')
	part12_correct_attempt
					['1 day, 3:44:53', u'1/3+1/2+1/2+3']

45 Student ID:hmnaing

	first_attempt
					2015-10-28 17:41:26
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:10:24', u'2']
	part10_correct_attempt
					['0:10:24', u'2']
	part12_incorrect_attempt
					('0:14:14', u'4/3')
	part12_correct_attempt
					['1 day, 13:47:08', u'(1* (1/3.0)) + (3 * (1/6.0)) + (3* (1/6.0)) + (9/3)']

46 Student ID:edescobe

	first_attempt
					2015-10-25 21:51:56
	part1_correct_attempt
					['0:00:00', u'3/6']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'3/6']
	part4_correct_attempt
					['0:00:00', u'3/6']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'3/6']
	part9_correct_attempt
					['0:00:00', u'2']
	part10_correct_attempt
					['0:00:00', u'2']
	part12_incorrect_attempt
					('0:02:20', u'18/36')
	part12_correct_attempt
					['2 days, 22:34:10', u'13/3']

47 Student ID:muy002

	first_attempt
					2015-10-28 03:47:29
	part1_correct_attempt
					['0:00:00', u'3/6']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'3/6']
	part4_correct_attempt
					['0:00:00', u'3/6']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'3/6']
	part9_correct_attempt
					['0:00:37', u'12/6']
	part10_correct_attempt
					['0:00:37', u'12/6']
	part12_incorrect_attempt
					('0:01:01', u'144/36')
					('0:10:51', u'144/36+12/6')
					('0:11:10', u'144/36')
					('0:57:51', u'30/6')
					('0:58:02', u'27/6')
					('0:58:22', u'24/6')
					('0:59:47', u'27/6')
					('1:00:42', u'144/6')
					('1:00:54', u'48/6')
					('1:01:07', u'96/6')
					('1:04:05', u'48/6')
					('1 day, 8:37:31', u'12/6')
					('1 day, 8:38:54', u'(12/6)^2')
					('1 day, 12:33:15', u'30/6')
					('1 day, 12:41:43', u'90/36')
					('1 day, 12:42:45', u'6/6')
					('1 day, 12:46:06', u'18/6')
					('1 day, 12:47:53', u'60/6')
	part12_correct_attempt
					['1 day, 12:52:21', u'13/3']

48 Student ID:v4sharma

	first_attempt
					2015-10-29 02:33:12
	part1_correct_attempt
					['0:00:00', u'3/6']
	part2_correct_attempt
					['0:00:18', u'0']
	part3_correct_attempt
					['0:00:29', u'3/6']
	part4_correct_attempt
					['0:00:52', u'3/6']
	part5_correct_attempt
					['0:01:02', u'0']
	part6_correct_attempt
					['0:01:02', u'3/6']
	part9_correct_attempt
					['0:02:29', u'(1)(3/6) + (2)(0) + (3)(3/6)']
	part10_correct_attempt
					['0:02:59', u'(1)(3/6) + (2)(0) + (3)(3/6)']
	part12_incorrect_attempt
					('0:03:34', u'2*2')
	part12_correct_attempt
					['0:20:05', u'13/3']

49 Student ID:ralhadda

	first_attempt
					2015-10-24 05:04:00
	part1_correct_attempt
					['0:00:00', u'3/6']
	part2_correct_attempt
					['0:01:33', u'0']
	part3_correct_attempt
					['0:01:33', u'3/6']
	part4_correct_attempt
					['0:02:10', u'3/6']
	part5_correct_attempt
					['0:02:10', u'0']
	part6_correct_attempt
					['0:02:10', u'3/6']
	part9_correct_attempt
					['0:04:03', u'2']
	part10_correct_attempt
					['0:04:03', u'2']
	part12_incorrect_attempt
					('0:10:50', u'12.33333')
	part12_correct_attempt
					['0:16:10', u'4.333']

50 Student ID:rohan

	first_attempt
					2015-10-30 21:29:50
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:00:28', u'2']
	part10_correct_attempt
					['0:00:28', u'2']
	part12_incorrect_attempt
					('0:22:42', u'4(1/3)')
	part12_correct_attempt
					['0:43:14', u'4+1/3']

51 Student ID:aportuga

	first_attempt
					2015-10-29 03:01:42
	part1_correct_attempt
					['0:00:00', u'(1/3)+(1/6)']
	part2_correct_attempt
					['0:00:05', u'0']
	part3_correct_attempt
					['0:00:13', u'(1/3)+(1/6)']
	part4_correct_attempt
					['0:00:27', u'(1/3)+(1/6)']
	part5_correct_attempt
					['0:00:27', u'0']
	part6_correct_attempt
					['0:00:27', u'(1/3)+(1/6)']
	part9_correct_attempt
					['0:01:50', u'.5+1.5']
	part10_correct_attempt
					['0:02:04', u'2']
	part12_incorrect_attempt
					('0:03:46', u'(1/3)+(3/6)+(3/6)+(1)')
	part12_correct_attempt
					['0:04:02', u'(1/3)+(3/6)+(3/6)+(3)']

52 Student ID:xil109

	first_attempt
					2015-10-26 20:54:44
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:02:56', u'2']
	part10_correct_attempt
					['0:02:56', u'2']
	part12_incorrect_attempt
					('3 days, 23:15:06', u'43/12')
	part12_correct_attempt
					['3 days, 23:16:12', u'1+1/3+3']

53 Student ID:v3doan

	first_attempt
					2015-10-27 02:58:17
	part1_correct_attempt
					['0:00:00', u'1/3 + 1/6']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/6 + 1/3']
	part4_correct_attempt
					['0:00:00', u'1/3 + 1/6']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/6 + 1/3']
	part9_correct_attempt
					['0:01:01', u'2']
	part10_correct_attempt
					['0:01:01', u'2']
	part12_incorrect_attempt
					('0:07:47', u'1/3 + 1')
					('1:56:24', u'1/9')
					('1:57:41', u'1 + 1/2 + 1/2 + 1')
	part12_correct_attempt
					['2:06:57', u'1/3 + 1/2 + 1/2 + 3']

54 Student ID:sghouse

	first_attempt
					2015-10-26 20:33:23
	part1_correct_attempt
					['0:00:00', u'3/6']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'3/6']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:20:03', u'2']
	part10_correct_attempt
					['0:20:03', u'2']
	part12_incorrect_attempt
					('2 days, 7:16:23', u'10/4')
	part12_correct_attempt
					['3 days, 9:57:10', u'4.3333']

55 Student ID:lpettit

	first_attempt
					2015-10-30 23:15:09
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:00:56', u'2']
	part10_correct_attempt
					['0:00:56', u'2']
	part12_incorrect_attempt
					('0:11:04', u'5/2')

56 Student ID:lywong

	first_attempt
					2015-10-28 08:32:29
	part1_correct_attempt
					['0:00:00', u'3/6']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'3/6']
	part4_correct_attempt
					['0:00:00', u'3/6']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'3/6']
	part9_correct_attempt
					['0:10:22', u'2']
	part10_correct_attempt
					['0:10:22', u'2']
	part12_incorrect_attempt
					('1 day, 0:37:03', u'30/6')
					('1 day, 19:02:38', u'7/3')
					('1 day, 19:03:09', u'5/3')
	part12_correct_attempt
					['1 day, 19:04:30', u'13/3']

57 Student ID:kebao

	first_attempt
					2015-10-30 04:20:43
	part1_correct_attempt
					['0:00:00', u'1/3+1/6']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/6+1/3']
	part4_correct_attempt
					['0:00:00', u'1/3+1/6']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/3+1/6']
	part9_correct_attempt
					['0:06:26', u'2']
	part10_correct_attempt
					['0:09:34', u'2']
	part12_incorrect_attempt
					('0:13:23', u'(2+3+3+18)/3')
	part12_correct_attempt
					['0:20:32', u'(2+3+3+18)/6']

58 Student ID:hkhodada

	first_attempt
					2015-10-24 18:14:12
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['-1 day, 23:54:22', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['-1 day, 23:54:22', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:01:12', u'2']
	part10_correct_attempt
					['0:01:12', u'2']
	part12_incorrect_attempt
					('3 days, 0:24:36', u'13/4')
	part12_correct_attempt
					['3 days, 0:26:40', u'13/3']

59 Student ID:airanmeh

	first_attempt
					2015-10-29 08:21:11
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:00:00', u'2']
	part10_correct_attempt
					['0:00:00', u'2']
	part12_incorrect_attempt
					('0:03:24', u'16/6')
	part12_correct_attempt
					['0:04:44', u'26/6']

60 Student ID:d6he

	first_attempt
					2015-10-28 20:37:47
	part1_correct_attempt
					['0:00:00', u'3/6']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'3/6']
	part4_correct_attempt
					['0:00:00', u'3/6']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'3/6']
	part9_correct_attempt
					['0:00:44', u'2']
	part10_correct_attempt
					['0:00:44', u'2']
	part12_incorrect_attempt
					('0:16:09', u'82/6')
	part12_correct_attempt
					['21:31:35', u'13/3']

61 Student ID:thk002

	first_attempt
					2015-10-27 09:33:58
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:00:24', u'2']
	part10_correct_attempt
					['0:00:24', u'2']
	part12_incorrect_attempt
					('0:05:22', u'(1/4)+(1/4)')
					('0:05:38', u'(1/4)+(9/4)')
					('0:06:19', u'(1/4)+(3/4)')
					('0:08:47', u'2/3')
					('0:08:57', u'(1/3)+1')
					('0:11:09', u'(1/3)+(1/2)')
					('0:22:21', u'(1/9)+(1/36)')
					('0:22:39', u'(1/9)+(3/36)')
					('0:25:57', u'(1/4)+(1/4)')
	part12_correct_attempt
					['0:34:20', u'(1/3)+(3/6)+(3/6)+(9/3)']

62 Student ID:awollner

	first_attempt
					2015-10-28 02:42:15
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:00:00', u'2']
	part10_correct_attempt
					['0:00:00', u'2']
	part12_incorrect_attempt
					('14:50:07', u'12/3')
	part12_correct_attempt
					['14:50:14', u'13/3']

63 Student ID:pvl001

	first_attempt
					2015-10-27 05:56:50
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:00:00', u'2']
	part10_correct_attempt
					['0:00:00', u'2']
	part12_incorrect_attempt
					('0:09:31', u'1/9')
	part12_correct_attempt
					['0:16:16', u'13/3']

64 Student ID:mrchin

	first_attempt
					2015-10-29 23:47:54
	part1_correct_attempt
					['0:00:00', u'3/6']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'3/6']
	part4_correct_attempt
					['0:00:00', u'3/6']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'3/6']
	part9_correct_attempt
					['0:00:00', u'2']
	part10_correct_attempt
					['0:00:00', u'2']
	part12_incorrect_attempt
					('0:02:00', u'144/36')
					('0:02:30', u'.0625')
					('0:03:08', u'144/36')
					('22:23:50', u'144/36 * 2 * 2')
					('22:31:09', u'1/3 + 3/6 + 1 + 1/6')
	part12_correct_attempt
					['22:31:51', u'1/3 + 3/6 + 3 + 3/6']

65 Student ID:dlt009

	first_attempt
					2015-10-28 05:59:24
	part1_correct_attempt
					['0:00:00', u'(1/3)+(1/6)']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'(1/3)+(1/6)']
	part4_correct_attempt
					['0:00:00', u'(1/3)+(1/6)']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'(1/3)+(1/6)']
	part9_correct_attempt
					['0:04:29', u'(1/3)+(1/6)+3*[(1/3)+(1/6)]']
	part10_correct_attempt
					['0:05:21', u'(1/3)+(1/6)+3*[(1/3)+(1/6)]']
	part12_incorrect_attempt
					('0:05:54', u'(1/3)+(1/3)')
					('0:08:11', u'(1/3)+3*(1/3)')
					('0:08:46', u'(1/3)+9*(1/3)')
					('0:09:31', u'(1/3)+27*(1/3)')
					('0:09:40', u'(1/3)+3*(1/3)')
					('0:10:42', u'(1/3)+9*(1/3)')
					('0:11:11', u'(1/3)+(1/6)+3*[(1/3)+(1/6)]^2')
					('0:11:26', u'[(1/3)+(1/6)+3*[(1/3)+(1/6)]]^2')
	part12_correct_attempt
					['0:13:09', u'(1/3)+(3/6)+(3/6)+(9/3)']

66 Student ID:mbl003

	first_attempt
					2015-10-27 23:37:04
	part1_correct_attempt
					['0:00:00', u'3/6']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'3/6']
	part4_correct_attempt
					['0:00:00', u'3/6']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'3/6']
	part9_correct_attempt
					['0:02:32', u'((1*3)+(2*0)+(3*3))/6']
	part10_correct_attempt
					['0:02:32', u'((1*3)+(2*0)+(3*3))/6']
	part12_incorrect_attempt
					('0:02:56', u'(((1*3)+(2*0)+(3*3))/6)*(((1*3)+(2*0)+(3*3))/6)')
					('0:06:22', u'((2*2)+(4*2)+(9*2))/36')
					('0:06:57', u'((2*2)+(4*2)+(9*2))/6')
					('0:27:55', u'((2*2)+(4*2)+(9*2))/6')
					('0:28:24', u'((2*2)+(4*2)+(9*2))/9')
					('0:37:34', u'((2*2)+(4*2)+(9*2))')
					('0:38:04', u'((2*2)+(4*2)+(9*2))6')
					('0:38:13', u'((2*2)+(4*2)+(9*2))/6')
					('0:49:25', u'((2*2)+(4*2)+(6*2))/6')
					('0:49:47', u'((1*2)+(4*2)+(9*2))/6')
	part12_correct_attempt
					['0:50:04', u'((1*2)+(3*2)+(9*2))/6']

67 Student ID:n2patil

	first_attempt
					2015-10-28 06:40:48
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:35', u'1/2']
	part5_correct_attempt
					['0:00:35', u'0']
	part6_correct_attempt
					['0:00:50', u'1/2']
	part9_correct_attempt
					['0:02:55', u'2']
	part10_correct_attempt
					['0:02:55', u'2']
	part12_incorrect_attempt
					('0:05:41', u'10/4')
					('0:21:12', u'5/2')
					('0:31:02', u'4/3')
					('0:31:51', u'3+(1/3)')
					('0:33:39', u'10/3')
					('0:35:36', u'10/9')
					('0:40:14', u'10/3')
					('14:13:05', u'4/3')
					('14:54:54', u'(1*1*(1/3))+(3*3*(1/3))')
	part12_correct_attempt
					['19:19:55', u'(1/3)+(1/2)+(1/2)+3']

68 Student ID:ttimmons

	first_attempt
					2015-10-27 05:20:34
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:00:00', u'1/2+3/2']
	part10_correct_attempt
					['0:00:00', u'1/2+3/2']
	part12_incorrect_attempt
					('0:02:33', u'1/4+6/4')
					('0:05:24', u'(1/2+3/2)^2')
					('0:08:06', u'2(1/2+3/2)')
					('0:08:59', u'(1/2+3/2)*(1/2) + (1/2+3/2)*(3/2)')
					('0:13:40', u'1*(1/4)+9*(1/4)')
					('0:14:12', u'2(1*(1/4)+9*(1/4))')
					('0:15:23', u'1/3+1/6+1/6+1/3')
					('0:15:55', u'1*(1/3)+3*(1/6)+3*(1/6)+1/3')
	part12_correct_attempt
					['0:16:12', u'1*(1/3)+3*(1/6)+3*(1/6)+9*(1/3)']

69 Student ID:jblynch

	first_attempt
					2015-10-28 19:15:18
	part1_correct_attempt
					['0:00:00', u'3/6']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'3/6']
	part4_correct_attempt
					['0:00:00', u'3/6']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'3/6']
	part9_correct_attempt
					['0:00:00', u'(3/6)+(9/6)']
	part10_correct_attempt
					['0:00:00', u'(3/6)+(9/6)']
	part12_incorrect_attempt
					('0:00:34', u'2+2')
					('0:07:08', u'2*2')
	part12_correct_attempt
					['7:33:39', u'(1/3)+(3/6)+(3/6)+(9/3)']

70 Student ID:ganajera

	first_attempt
					2015-10-26 00:49:30
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:00:00', u'2']
	part10_correct_attempt
					['0:00:00', u'2']
	part12_incorrect_attempt
					('0:00:00', u'13/4')
	part12_correct_attempt
					['0:02:14', u'13/3']

71 Student ID:nnh002

	first_attempt
					2015-10-30 20:59:36
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:00:00', u'2']
	part10_correct_attempt
					['0:00:00', u'2']
	part12_incorrect_attempt
					('0:47:07', u'5/3')
	part12_correct_attempt
					['0:47:48', u'13/3']

72 Student ID:tol003

	first_attempt
					2015-10-28 05:42:04
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:05:29', u'1*(1/2)+3*(1/2)']
	part10_correct_attempt
					['0:05:29', u'1*(1/2)+3*(1/2)']
	part12_incorrect_attempt
					('0:07:02', u'[1*(1/2)+3*(1/2)]*[1*(1/2)+3*(1/2)]')
					('0:32:26', u'[(1/3)*(1/3)*(1/3)]+[(1/3)*(1/3)*(1)]')
					('0:40:25', u'1*(1/2)+3*(1/2)')
					('0:48:04', u'[(1/3)*(1/3)*(1/2)]+[(1/3)*(1/3)*(3*(1/2))]')
					('3:28:41', u'[1*1*(1/2)]+[3*3*(1/2)]')
	part12_correct_attempt
					['3:39:25', u'[1*1*(1/3)]+[1*3*(1/6)]+[1*3(1/6)]+[3*3*(1/3)]']

73 Student ID:yeh013

	first_attempt
					2015-10-28 06:51:00
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:00:00', u'2']
	part10_correct_attempt
					['0:00:00', u'2']
	part12_incorrect_attempt
					('0:02:58', u'2.5')
					('0:12:51', u'10/3')
	part12_correct_attempt
					['0:14:43', u'13/3']

74 Student ID:ksrijong

	first_attempt
					2015-10-28 22:18:46
	part1_correct_attempt
					['0:00:00', u'3/6']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'3/6']
	part4_correct_attempt
					['0:00:00', u'3/6']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'3/6']
	part9_correct_attempt
					['0:00:00', u'3/6 + 9/6']
	part10_correct_attempt
					['0:00:00', u'3/6 + 9/6']
	part12_incorrect_attempt
					('0:00:00', u'[3/6 + 9/6][3/6 + 9/6]')
					('0:08:10', u'1/3 + 1/2 + 1/2 + 1/3')
	part12_correct_attempt
					['1 day, 22:51:48', u'1/3 + 3/6 + 3/6 + 9/3']

75 Student ID:azkong

	first_attempt
					2015-10-29 18:21:43
	part1_correct_attempt
					['0:00:00', u'3/6']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'3/6']
	part4_correct_attempt
					['0:00:00', u'3/6']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'3/6']
	part9_correct_attempt
					['0:00:00', u'1/2+3/2']
	part10_correct_attempt
					['0:00:00', u'1/2+3/2']
	part12_incorrect_attempt
					('0:16:19', u'2/3')
	part12_correct_attempt
					['0:59:47', u'4+1/3']

76 Student ID:volim

	first_attempt
					2015-10-26 01:09:08
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['17:04:50', u'2']
	part10_correct_attempt
					['17:04:50', u'2']
	part12_incorrect_attempt
					('17:08:16', u'4/3')
					('2 days, 4:41:47', u'2/6')
					('2 days, 4:42:49', u'2/3')
					('3 days, 0:42:36', u'1/3')
					('3 days, 1:40:41', u'4*(1/3)')
					('3 days, 1:43:10', u'(2/3)(2/3)(2/3)(2)')
	part12_correct_attempt
					['3 days, 2:47:15', u'(1/3)+(3/6)+(3/6)+(9/3)']

77 Student ID:atorr

	first_attempt
					2015-10-29 07:00:07
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:00:45', u'2']
	part10_correct_attempt
					['0:00:45', u'2']
	part12_incorrect_attempt
					('0:09:11', u'(2/3)')
					('0:09:32', u'(1/3) + (1)')
					('0:10:25', u'(1/3) + 3')
					('0:12:12', u'((5/6) + (15/6))^2')
					('0:13:44', u'1/16')
					('0:16:24', u'1/2')
					('0:19:18', u'(1/3) + (1/2) + (1/2) * 3')
	part12_correct_attempt
					['0:20:17', u'(1/3) + (1/2) + (1/2) + 3']

78 Student ID:ytc012

	first_attempt
					2015-10-29 12:28:36
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:24', u'0']
	part3_correct_attempt
					['0:00:24', u'1/2']
	part4_correct_attempt
					['0:00:24', u'1/2']
	part5_correct_attempt
					['0:00:24', u'0']
	part6_correct_attempt
					['0:00:24', u'1/2']
	part9_correct_attempt
					['0:01:01', u'1/2+3/2']
	part10_correct_attempt
					['0:01:01', u'1/2+3/2']
	part12_incorrect_attempt
					('0:01:24', u'1/2+3/2+1/2+3/2')
					('0:01:57', u'2*(1/2+3/2)')
					('0:03:21', u'(1/2+3/2)')
					('0:03:29', u'(1/2+3/2)(1/2+3/2)')
					('0:12:02', u'(1/2+3/2)^2')
					('0:15:50', u'1+1')
					('0:16:23', u'1/2+3/2')
					('0:21:36', u'1/2+3/2+1/2+3/2')
					('8:06:47', u'1/2*1*1+3/2*3*3+1/2*1*1+3/2*3*3')
					('8:06:57', u'1/2*1*1+3/2*3*3')
	part12_correct_attempt
					['8:08:40', u'(1*1*1/3+3*1*1/6)+3*1*1/6+3*3*1/3']

79 Student ID:tjke

	first_attempt
					2015-10-26 21:41:20
	part1_correct_attempt
					['0:00:00', u'1/3+1/6']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/6+1/3']
	part4_correct_attempt
					['0:00:00', u'1/3+1/6']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/6+1/3']
	part9_correct_attempt
					['0:00:00', u'1*(1/3+1/6) + 2*0 + 3*(1/6+1/3)']
	part10_correct_attempt
					['0:00:00', u'1*(1/3+1/6) + 2*0 + 3*(1/6+1/3)']
	part12_incorrect_attempt
					('0:00:00', u'[1*(1/3+1/6) + 2*0 + 3*(1/6+1/3)]*[1*(1/3+1/6) + 2*0 + 3*(1/6+1/3)]')
	part12_correct_attempt
					['0:09:33', u'1*1*1/3 + 1*2*0 + 1*3*1/6 + 2*1*0 + 2*2*0 + 2*3*0 + 3*1*1/6 + 3*2*0 + 3*3*1/3']

80 Student ID:galu

	first_attempt
					2015-10-30 23:54:46
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:00:50', u'2']
	part10_correct_attempt
					['0:00:50', u'2']
	part12_incorrect_attempt
					('0:02:09', u'1/2')
					('0:02:19', u'1/3')
					('0:02:49', u'1/18')

81 Student ID:r2fisher

	first_attempt
					2015-10-26 23:31:01
	part1_correct_attempt
					['0:00:00', u'1/3+1/6']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/3+1/6']
	part4_correct_attempt
					['0:00:00', u'1/3+1/6']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/3+1/6']
	part9_correct_attempt
					['0:01:15', u'0.5 + 3*0.5']
	part10_correct_attempt
					['0:01:15', u'0.5 + 3*0.5']
	part12_incorrect_attempt
					('0:04:38', u'(0.5 + 3*0.5)*2')

82 Student ID:t2shin

	first_attempt
					2015-10-28 00:33:52
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['-1 day, 23:58:50', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:30', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:30', u'1/2']
	part9_correct_attempt
					['0:00:57', u'1/2+0+3(1/2)']
	part10_correct_attempt
					['0:01:06', u'1/2+0+3(1/2)']
	part12_incorrect_attempt
					('0:09:28', u'1/2')
					('0:19:02', u'2*1/2+2*0+2*1/2')
					('0:20:21', u'1*1/2+4*0+9*1/2')
	part12_correct_attempt
					['0:21:11', u'1/3+3/6+3/6+9/3']

83 Student ID:vsamant

	first_attempt
					2015-10-23 22:05:05
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:00:00', u'2']
	part10_correct_attempt
					['0:00:00', u'2']
	part12_incorrect_attempt
					('0:14:12', u'1/3+0+1')
	part12_correct_attempt
					['0:15:26', u'1/3+0+3+1/2+1/2']

84 Student ID:ppanourg

	first_attempt
					2015-10-30 08:51:46
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:03:22', u'2']
	part10_correct_attempt
					['0:03:22', u'2']
	part12_incorrect_attempt
					('0:26:07', u'4.5')
					('0:28:22', u'17/6')
	part12_correct_attempt
					['0:28:46', u'1/3+1/2+1/2+3']

85 Student ID:qtluong

	first_attempt
					2015-10-29 07:46:16
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['-1 day, 23:57:10', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['-1 day, 23:57:10', u'1/2']
	part5_correct_attempt
					['-1 day, 23:57:10', u'0']
	part6_correct_attempt
					['-1 day, 23:57:10', u'1/2']
	part9_correct_attempt
					['0:00:43', u'2']
	part10_correct_attempt
					['0:00:43', u'2']
	part12_incorrect_attempt
					('0:02:15', u'7+1/3')
	part12_correct_attempt
					['0:04:12', u'4+1/3']

86 Student ID:spw006

	first_attempt
					2015-10-28 01:45:22
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:00:17', u'1/2 + 3/2']
	part10_correct_attempt
					['0:00:17', u'2']
	part12_incorrect_attempt
					('0:08:24', u'3/2')
	part12_correct_attempt
					['1:47:10', u'(1/3) + 1/2 + 1/2 + 3']

87 Student ID:any027

	first_attempt
					2015-10-26 05:05:36
	part1_correct_attempt
					['0:00:00', u'(1/3) + (1/6)']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'(1/6) + (1/3)']
	part4_correct_attempt
					['0:03:22', u'(1/3) + (1/6)']
	part5_correct_attempt
					['0:03:22', u'0']
	part6_correct_attempt
					['0:03:22', u'(1/6) + (1/3)']
	part9_correct_attempt
					['0:04:24', u' (1* (0.5)) + (3*(0.5))']
	part10_correct_attempt
					['0:04:45', u' (1* (0.5)) + (3*(0.5))']
	part12_incorrect_attempt
					('0:08:56', u'(1/3) + (3*(1/6)) + (1/6) + (3*(1/3))')
	part12_correct_attempt
					['0:09:44', u'(1/3) + (3*(1/6)) + (3*(1/6)) + (9*(1/3))']

88 Student ID:s1powers

	first_attempt
					2015-10-27 23:42:04
	part1_correct_attempt
					['0:00:00', u'1/2']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:17', u'1/2']
	part6_correct_attempt
					['0:00:17', u'1/2']
	part9_correct_attempt
					['0:00:35', u'2']
	part10_correct_attempt
					['0:00:35', u'2']
	part12_incorrect_attempt
					('1 day, 2:44:16', u'1/9')
	part12_correct_attempt
					['1 day, 2:45:24', u'1/3+9/3+1/2+1/2']

89 Student ID:pcdo

	first_attempt
					2015-10-29 00:09:36
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:20', u'1/2']
	part5_correct_attempt
					['0:00:20', u'0']
	part6_correct_attempt
					['0:00:20', u'1/2']
	part9_correct_attempt
					['0:00:58', u'1/2 + 3*.5']
	part10_correct_attempt
					['0:00:58', u'1/2 + 3*.5']
	part12_incorrect_attempt
					('0:01:12', u'(1/2 + 3*.5)^2')
					('0:02:34', u'(1/2 + 3*.5)(1/2 + 3*.5)')
	part12_correct_attempt
					['0:04:54', u'1*(1/3) + 2*0 + 3*(1/6) + 3*(1/6) + 6*0 + 9*(1/3)']

90 Student ID:e9brown

	first_attempt
					2015-10-27 23:21:57
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:02:15', u'2']
	part10_correct_attempt
					['0:02:15', u'2']
	part12_incorrect_attempt
					('0:07:16', u'.75')
					('0:10:34', u'1 + (1/3) + (1/9)')
	part12_correct_attempt
					['0:14:42', u'4 + 1/3']

91 Student ID:vsosnovs

	first_attempt
					2015-10-30 06:38:43
	part1_correct_attempt
					['0:00:00', u'1/3+ 0 +1/6']
	part2_correct_attempt
					['0:00:24', u'0']
	part3_correct_attempt
					['0:00:24', u'1/6+1/3']
	part4_correct_attempt
					['0:00:24', u'1/3+1/6']
	part5_correct_attempt
					['0:00:41', u'0']
	part6_correct_attempt
					['0:00:41', u'1/6+0+1/3']
	part9_correct_attempt
					['12:56:19', u'1(1/3)+1(1/6)+3(1/6)+3(1/3)']
	part10_correct_attempt
					['12:56:58', u'1(1/3)+1(1/6)+3(1/6)+3(1/3)']
	part12_incorrect_attempt
					('13:00:52', u'6.5')
					('15:41:38', u'13/3-4')
	part12_correct_attempt
					['15:41:57', u'13/3']

92 Student ID:k5law

	first_attempt
					2015-10-26 06:56:26
	part1_correct_attempt
					['0:00:00', u'(1/3)+(1/6)']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'(1/6)+(1/3)']
	part4_correct_attempt
					['0:00:00', u'(1/3)+(1/6)']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'(1/6)+(1/3)']
	part9_correct_attempt
					['0:22:41', u'(1/3)+(1/6)+[3*[(1/6)+(1/3)]]']
	part10_correct_attempt
					['0:23:00', u'(1/3)+(1/6)+[3*[(1/6)+(1/3)]]']
	part12_incorrect_attempt
					('0:28:52', u'[1*1*[(1/3)+(1/6)]*[(1/3)+(1/6)]]+0+[3*3*[(1/6)+(1/3)]*[(1/6)+(1/3)]]+[1*3*[(1/3)+(1/6)]*[(1/6)+(1/3)]]+[1*3*[(1/3)+(1/6)]*[(1/6)+(1/3)]]')
					('0:33:49', u'[(1/3)+(1/6)+[3*[(1/6)+(1/3)]]]*[(1/3)+(1/6)+[3*[(1/6)+(1/3)]]]*6*6')
					('0:43:14', u'2*[[1*1*[(1/3)+(1/6)]*[(1/3)+(1/6)]]+[1*3*[(1/3)+(1/6)]*[(1/6)+(1/3)]]]')
					('0:45:29', u'2*[[1*1*[(1/3)+(1/6)]]+[1*3*[(1/3)+(1/6)]]]')
					('0:48:39', u'2*[[1*1*[(1/3)+(1/6)]*[(1/3)+(1/6)]]+[1*3*[(1/3)+(1/6)]*[3*[(1/6)+(1/3)]]]]')
					('0:52:22', u'2*[[1*1*[(1/3)+(1/6)]]+[1*3*[(1/3)+(1/6)]]]')
					('0:57:32', u'2*[[[(1/3)+(1/6)+[3*[(1/6)+(1/3)]]]*[(1/3)+(1/6)+[3*[(1/6)+(1/3)]]]]+[[(1/3)+(1/6)+[3*[(1/6)+(1/3)]]]*[(1/6)+(1/3)]]]')
					('0:59:56', u'2*[[[(1/3)+(1/6)]*[(1/3)+(1/6)]]+[[(1/3)+(1/6)]*[(1/6)+(1/3)]]]')
					('1:00:11', u'2*[[[(1/3)+(1/6)]*[(1/3)+(1/6)]]+[[(1/3)+(1/6)]*[3*[(1/6)+(1/3)]]]]')
	part12_correct_attempt
					['13:18:51', u'[1*(1/3)]+[3*(1/6)]+[3*(1/6)]+[3*3*(1/3)]']

93 Student ID:cfgutier

	first_attempt
					2015-10-30 02:19:58
	part1_correct_attempt
					['0:00:00', u'3/6']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'3/6']
	part4_correct_attempt
					['0:00:17', u'3/6']
	part5_correct_attempt
					['0:00:17', u'0']
	part6_correct_attempt
					['0:00:17', u'3/6']
	part9_correct_attempt
					['17:34:08', u'12/6']
	part10_correct_attempt
					['17:34:08', u'12/6']
	part12_incorrect_attempt
					('17:34:36', u'144/36')
					('17:35:39', u'(12/6)^2')
	part12_correct_attempt
					['20:26:46', u'26/6']

94 Student ID:anl114

	first_attempt
					2015-10-30 21:50:23
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:00:00', u'2']
	part10_correct_attempt
					['0:00:00', u'2']
	part12_incorrect_attempt
					('0:18:06', u'2.5')
					('0:30:21', u'2.5')
					('0:32:04', u'.5')
					('0:36:29', u'1.25')
	part12_correct_attempt
					['0:38:53', u'13/3']

95 Student ID:s6deng

	first_attempt
					2015-10-30 07:12:26
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:00:36', u'2']
	part10_correct_attempt
					['0:00:36', u'2']
	part12_incorrect_attempt
					('0:02:43', u'2^2')

96 Student ID:achinn

	first_attempt
					2015-10-28 08:25:23
	part1_correct_attempt
					['0:00:00', u'3/6']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'3/6']
	part4_correct_attempt
					['0:00:00', u'3/6']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'3/6']
	part9_correct_attempt
					['0:00:00', u'2']
	part10_correct_attempt
					['0:00:00', u'2']
	part12_incorrect_attempt
					('0:00:00', u'1.5')
	part12_correct_attempt
					['19:44:54', u'13/3']

97 Student ID:kalang

	first_attempt
					2015-10-29 22:31:00
	part1_correct_attempt
					['0:00:00', u'1/3+1/6']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/6+1/3']
	part4_correct_attempt
					['0:00:00', u'1/3+1/6']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/3+1/6']
	part9_correct_attempt
					['0:00:48', u'1*(1/3+1/6)+3*(1/6+1/3)']
	part10_correct_attempt
					['0:00:54', u'2']
	part12_incorrect_attempt
					('0:01:17', u'2*2')
					('0:03:37', u'(1*(1/3+1/6)+3*(1/6+1/3))*(1*(1/3+1/6)+3*(1/6+1/3))')
	part12_correct_attempt
					['0:06:03', u'1*(1/3) + 2*(0) + 3*(1/6) + 0 + 3*(1/6)+9*(1/3)']

98 Student ID:jcl084

	first_attempt
					2015-10-29 00:08:54
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:17', u'1/2']
	part5_correct_attempt
					['0:00:17', u'0']
	part6_correct_attempt
					['0:00:17', u'1/2']
	part9_correct_attempt
					['0:02:20', u'1/2 + 3*1/2']
	part10_correct_attempt
					['0:02:20', u'1/2 + 3*1/2']
	part12_incorrect_attempt
					('0:02:31', u'1/2 + 3*1/2 * 1/2 + 3*1/2')
					('0:02:42', u'(1/2 + 3*1/2) * (1/2 + 3*1/2)')
	part12_correct_attempt
					['0:06:19', u'1*(1/3) + 2*0 + 3*(1/6) + 3*(1/6) + 6*0 + 9*(1/3)']

99 Student ID:sippolit

	first_attempt
					2015-10-29 00:56:22
	part1_correct_attempt
					['0:00:00', u'1/3+0+1/6']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/6+0+1/3']
	part4_correct_attempt
					['0:00:00', u'1/3+0+1/6']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/6+0+1/3']
	part9_correct_attempt
					['0:01:13', u'1*(1/3+0+1/6)+2*0+3*(1/6+0+1/3)']
	part10_correct_attempt
					['0:01:13', u'1*(1/3+0+1/6)+2*0+3*(1/6+0+1/3)']
	part12_incorrect_attempt
					('0:01:56', u'(1*(1/3+0+1/6)+2*0+3*(1/6+0+1/3))*(1*(1/3+0+1/6)+2*0+3*(1/6+0+1/3))')
	part12_correct_attempt
					['0:04:33', u'1*1/3+2*0+3*1/6+2*0+4*0+6*0+3*1/6+6*0+9*1/3']

100 Student ID:mcatozzi

	first_attempt
					2015-10-28 00:47:44
	part1_correct_attempt
					['0:00:00', u'.5']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'.5']
	part4_correct_attempt
					['0:00:00', u'.5']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'.5']
	part9_correct_attempt
					['0:00:00', u'2']
	part10_correct_attempt
					['0:00:00', u'2']
	part12_incorrect_attempt
					('0:08:13', u'1/6')
					('0:56:59', u'1/81')
					('1:01:01', u'64/91')
					('1:01:09', u'64/81')
					('1:02:32', u'49/36')
					('1:04:01', u'7/6')
					('17:17:49', u'24/6')
	part12_correct_attempt
					['17:21:17', u'26/6']

101 Student ID:aadhakal

	first_attempt
					2015-10-30 01:52:19
	part1_correct_attempt
					['0:00:00', u'1/3+1/6']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/3+1/6']
	part4_correct_attempt
					['0:00:00', u'1/3+1/6']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/3+1/6']
	part9_correct_attempt
					['0:00:00', u'1*(1/3+1/6)+2(0)+3(1/3+1/6)']
	part10_correct_attempt
					['0:02:16', u'1*(1/3+1/6)+2(0)+3(1/3+1/6)']
	part12_incorrect_attempt
					('0:50:11', u'(1/3+2/6+3/6+9/3)')
	part12_correct_attempt
					['0:50:37', u'(1/3+3/6+3/6+9/3)']

102 Student ID:jnn015

	first_attempt
					2015-10-27 05:25:01
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:00:00', u'1/2+3/2']
	part10_correct_attempt
					['0:00:00', u'1/2+3/2']
	part12_incorrect_attempt
					('0:00:41', u'(1/2+3/2)^2')
	part12_correct_attempt
					['0:07:02', u'1(1/3)+3(1/6)+3(1/6)+9/3']

103 Student ID:acs008

	first_attempt
					2015-10-28 00:34:33
	part1_correct_attempt
					['0:00:00', u'1/2']
	part3_correct_attempt
					['-1 day, 23:58:44', u'1/2']
	part4_correct_attempt
					['-1 day, 23:58:44', u'1/2']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:00:51', u'1/2+3/2']
	part10_correct_attempt
					['0:01:01', u'1/2+3/2']
	part12_incorrect_attempt
					('0:08:15', u'1/2+3/2+1/2+3/2')
					('0:20:09', u'1/4+1/4')
					('0:21:24', u'1/3+3/6+3/6+9/6')
	part12_correct_attempt
					['0:21:42', u'1/3+3/6+3/6+9/3']

104 Student ID:dpereira

	first_attempt
					2015-10-23 18:31:43
	part1_correct_attempt
					['0:00:00', u'3/6']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'3/6']
	part4_correct_attempt
					['0:00:00', u'3/6']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'3/6']
	part9_correct_attempt
					['0:00:26', u'1*3/6 + 2 * 0 + 3 * 3/6']
	part10_correct_attempt
					['0:00:26', u'1*3/6 + 2 * 0 + 3 * 3/6']
	part12_incorrect_attempt
					('0:00:42', u'(1*3/6 + 2 * 0 + 3 * 3/6)^2')
					('0:02:53', u'1*1*1/3 + 1*3*1/6 + 1*3*1/6 + 1*3*1/3')
					('0:15:04', u'52/3')
	part12_correct_attempt
					['0:18:45', u'1*1*(1/3) + 1*3*(1/6) + 1*3*(1/6) + 3*3*(1/3)']

105 Student ID:haliew

	first_attempt
					2015-10-29 02:21:33
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:00:00', u'1(1/2)+3(1/2)']
	part10_correct_attempt
					['0:00:00', u'1(1/2)+3(1/2)']
	part12_incorrect_attempt
					('1:12:54', u'1/3')
					('1 day, 21:22:02', u'4-(1/3)')
	part12_correct_attempt
					['1 day, 21:22:42', u'4+(1/3)']

106 Student ID:daw023

	first_attempt
					2015-10-30 00:10:20
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:00:00', u'1/2+3*(1/2)']
	part10_correct_attempt
					['0:00:00', u'1/2+3*(1/2)']
	part12_incorrect_attempt
					('0:00:00', u'(1/2+3*(1/2))^2')
					('0:37:20', u'(1/2+3*(1/2))*(1/2+3*(1/2))')
					('0:38:25', u'(1/2+3*(1/2))*2')
					('0:47:43', u'3/4+4')
	part12_correct_attempt
					['0:51:18', u'(1/3)*(-1)(-1)+1/6*(1)*(-1)+1/6*(-1)*(1)+1/3+4']

107 Student ID:edcole

	first_attempt
					2015-10-30 21:47:53
	part1_correct_attempt
					['0:00:00', u'1/2']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:03:29', u'2']
	part10_correct_attempt
					['0:03:29', u'2']
	part12_incorrect_attempt
					('0:04:15', u'1/2')
	part12_correct_attempt
					['0:26:32', u' 13/3']

108 Student ID:aordookh

	first_attempt
					2015-10-29 03:41:44
	part1_correct_attempt
					['0:00:00', u'3/6']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'3/6']
	part4_correct_attempt
					['0:00:00', u'3/6']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'3/6']
	part9_correct_attempt
					['0:02:14', u'2']
	part10_correct_attempt
					['0:02:14', u'2']
	part12_incorrect_attempt
					('0:02:23', u'2*2')
	part12_correct_attempt
					['1:00:22', u'(1/3)+(3/6)+ (3/6)+(9/3)']

109 Student ID:yig015

	first_attempt
					2015-10-30 10:53:01
	part1_correct_attempt
					['0:00:00', u'3/6']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'3/6']
	part4_correct_attempt
					['0:00:00', u'3/6']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'3/6']
	part9_correct_attempt
					['0:00:00', u'2']
	part10_correct_attempt
					['0:00:00', u'2']
	part12_incorrect_attempt
					('0:00:00', u'1/2')
					('0:27:25', u'0.5')
					('0:32:41', u'2.5')
	part12_correct_attempt
					['0:50:07', u'13/3']

110 Student ID:syip

	first_attempt
					2015-10-30 19:31:05
	part1_correct_attempt
					['0:00:00', u'1/3 + 1/6']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/6+1/3']
	part4_correct_attempt
					['0:00:00', u'1/3+1/6']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/6+1/3']
	part9_correct_attempt
					['0:01:11', u'0.5+1.5']
	part10_correct_attempt
					['0:01:11', u'0.5+1.5']
	part12_incorrect_attempt
					('0:01:11', u'2*2')
	part12_correct_attempt
					['0:07:04', u'1(1/3) + 3(1/6) + 3(1/6) + 9(1/3)']

111 Student ID:c3chung

	first_attempt
					2015-10-29 01:48:38
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:01:15', u'1(1/2) +3(1/2)']
	part10_correct_attempt
					['0:01:15', u'1(1/2) +3(1/2)']
	part12_incorrect_attempt
					('0:01:46', u'.5')
					('1 day, 11:30:04', u'1/2')
					('1 day, 11:30:10', u'1/4')

112 Student ID:ajvanega

	first_attempt
					2015-10-30 17:12:14
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['-1 day, 23:59:05', u'0']
	part3_correct_attempt
					['-1 day, 23:59:05', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:01:52', u'2']
	part10_correct_attempt
					['0:01:52', u'2']
	part12_incorrect_attempt
					('1:33:27', u'1/2')
					('2:36:14', u'1/2')
					('2:39:11', u'1/4')
					('2:39:25', u'3/4')
	part12_correct_attempt
					['2:47:43', u'(1/3)+(1/2)+(1/2)+3']

113 Student ID:zig006

	first_attempt
					2015-10-27 17:44:38
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:00:00', u'2']
	part10_correct_attempt
					['0:00:00', u'2']
	part12_incorrect_attempt
					('0:24:24', u'11/3')
	part12_correct_attempt
					['0:24:38', u'13/3']

114 Student ID:mtrafeca

	first_attempt
					2015-10-25 06:56:49
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:31', u'0']
	part3_correct_attempt
					['0:00:31', u'1/2']
	part4_correct_attempt
					['0:00:31', u'1/2']
	part5_correct_attempt
					['0:00:31', u'0']
	part6_correct_attempt
					['0:00:31', u'1/2']
	part9_correct_attempt
					['0:03:47', u'2']
	part10_correct_attempt
					['0:03:47', u'2']
	part12_incorrect_attempt
					('0:05:18', u'10/6')
					('0:07:35', u'1/9')
					('0:13:58', u'.5')
					('0:21:38', u'10/3')
					('0:34:49', u'4.5')
	part12_correct_attempt
					['0:38:34', u'13/3']

115 Student ID:mjethani

	first_attempt
					2015-10-30 15:12:46
	part1_correct_attempt
					['0:00:00', u'(1/3+1/6)']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'(1/3+1/6)']
	part4_correct_attempt
					['0:00:00', u'(1/3+1/6)']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'(1/3+1/6)']
	part9_correct_attempt
					['0:11:18', u'(1/3+1/6 + 3/6 + 1)']
	part10_correct_attempt
					['0:12:37', u'1/3 + 1/6 + 1/2 + 1']
	part12_incorrect_attempt
					('0:13:20', u'(1/3+1/6 + 3/6 + 1)*(1/3 + 1/6 + 1/2 + 1)')
					('4:51:58', u'(1*1*1/3) + (1*1*1/6) + (1*3*1/6) + (3*3*1/3)')
					('4:52:28', u'(1*1*(1/3)) + (1*1*(1/6)) + (1*3*(1/6)) + (3*3*(1/3))')
	part12_correct_attempt
					['4:53:02', u'(1*1*(1/3)) + (1*3*(1/6)) + (1*3*(1/6)) + (3*3*(1/3))']

116 Student ID:kosung

	first_attempt
					2015-10-28 00:16:08
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:00:00', u'2']
	part10_correct_attempt
					['0:00:00', u'2']
	part12_incorrect_attempt
					('0:16:10', u'5/3')
	part12_correct_attempt
					['0:17:21', u'13/3']

117 Student ID:j2phung

	first_attempt
					2015-10-29 10:30:54
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:00:00', u'1*(1/2)+3*(1/2)']
	part10_correct_attempt
					['0:00:00', u'1/2 + 3*(1/2)']
	part12_incorrect_attempt
					('22:34:52', u'(1/2 + 3*(1/2))(1*(1/2)+3*(1/2))')
					('22:43:30', u'(1/3)+(3/4)')
	part12_correct_attempt
					['22:53:14', u'1(1/3) + 3(1/6) + 3(1/6) + 9 (1/3)']












## Part 13

### (195) Mistake Group Digits of size 195




### (46) Mistake Group Wrong_Sign of size 46




### (36) Mistake Group redirect of size 36




### (11) Mistake Group ['R.0'] of size 11
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|1*1/3+2*0+3*1/6+2*0+4*0+6*0+3*1/6+6*0+9*1/3-[1*(1/3+0+1/6)+2*(0+0+0)+3*(1/6+0+1/3)]*[1*(1/3+0+1/6)+2*(0+0+0)+3*(1/6+0+1/3)]	|[(1/3)+(3/6)+(3/6)+(9/3)]-[(1/3)+(1/6)+3*[(1/3)+(1/6)]]^0.5	|[('R.0', 4.333333333333333, u'1*1/3+2*0+3*1/6+2*0+4*0+6*0+3*1/6+6*0+9*1/3', u'(1/3)+(3/6)+(3/6)+(9/3)')]	|
|1	|1*1/3+2*0+3*1/6+2*0+4*0+6*0+3*1/6+6*0+9*1/3-[1*(1/3+0+1/6)+2*(0+0+0)+3*(1/6+0+1/3)]*[1*(1/3+0+1/6)+2*(0+0+0)+3*(1/6+0+1/3)]	|(1*1/3+2*0+3*1/6+2*0+4*0+6*0+3*1/6+6*0+9*1/3)-(1*1/3+2*0+3*1/6+2*0+4*0+6*0+3*1/6+6*0+9*1/3)	|[('R.0', 4.333333333333333, u'1*1/3+2*0+3*1/6+2*0+4*0+6*0+3*1/6+6*0+9*1/3', u'1*1/3+2*0+3*1/6+2*0+4*0+6*0+3*1/6+6*0+9*1/3')]	|
|2	|1*1/3+2*0+3*1/6+2*0+4*0+6*0+3*1/6+6*0+9*1/3-[1*(1/3+0+1/6)+2*(0+0+0)+3*(1/6+0+1/3)]*[1*(1/3+0+1/6)+2*(0+0+0)+3*(1/6+0+1/3)]	|(1*1/3+2*0+3*1/6+2*0+4*0+6*0+3*1/6+6*0+9*1/3)-(1*(1/3+0+1/6)+2*0+3*(1/6+0+1/3)*1*(1/3+0+1/6)+2*0+3*(1/6+0+1/3))	|[('R.0', 4.333333333333333, u'1*1/3+2*0+3*1/6+2*0+4*0+6*0+3*1/6+6*0+9*1/3', u'1*1/3+2*0+3*1/6+2*0+4*0+6*0+3*1/6+6*0+9*1/3')]	|
|3	|1*1/3+2*0+3*1/6+2*0+4*0+6*0+3*1/6+6*0+9*1/3-[1*(1/3+0+1/6)+2*(0+0+0)+3*(1/6+0+1/3)]*[1*(1/3+0+1/6)+2*(0+0+0)+3*(1/6+0+1/3)]	|((1/3)+(3/6)+(3/6)+(3))/4	|[('R.0', 4.333333333333333, u'1*1/3+2*0+3*1/6+2*0+4*0+6*0+3*1/6+6*0+9*1/3', u'(1/3)+(3/6)+(3/6)+(3)')]	|
|4	|1*1/3+2*0+3*1/6+2*0+4*0+6*0+3*1/6+6*0+9*1/3-[1*(1/3+0+1/6)+2*(0+0+0)+3*(1/6+0+1/3)]*[1*(1/3+0+1/6)+2*(0+0+0)+3*(1/6+0+1/3)]	|(1*1/3 + 2*0 + 3*1/6 + 2*0 + 4*0 + 6*0 + 3*1/6 + 6*0 + 9*1/3)-1.5^2	|[('R.0', 4.333333333333333, u'1*1/3+2*0+3*1/6+2*0+4*0+6*0+3*1/6+6*0+9*1/3', u'1*1/3 + 2*0 + 3*1/6 + 2*0 + 4*0 + 6*0 + 3*1/6 + 6*0 + 9*1/3')]	|
|5	|1*1/3+2*0+3*1/6+2*0+4*0+6*0+3*1/6+6*0+9*1/3-[1*(1/3+0+1/6)+2*(0+0+0)+3*(1/6+0+1/3)]*[1*(1/3+0+1/6)+2*(0+0+0)+3*(1/6+0+1/3)]	|((3(1)(1/6))+(1/3)+(3(1/6))+(9(1/3)))^2	|[('R.0', 4.333333333333333, u'1*1/3+2*0+3*1/6+2*0+4*0+6*0+3*1/6+6*0+9*1/3', u'(3(1)(1/6))+(1/3)+(3(1/6))+(9(1/3))')]	|
|6	|1*1/3+2*0+3*1/6+2*0+4*0+6*0+3*1/6+6*0+9*1/3-[1*(1/3+0+1/6)+2*(0+0+0)+3*(1/6+0+1/3)]*[1*(1/3+0+1/6)+2*(0+0+0)+3*(1/6+0+1/3)]	|1/3+1/2+1/2+3 + 4	|[('R.0', 4.333333333333333, u'1*1/3+2*0+3*1/6+2*0+4*0+6*0+3*1/6+6*0+9*1/3', u'1/3+1/2+1/2+3')]	|
|7	|1*1/3+2*0+3*1/6+2*0+4*0+6*0+3*1/6+6*0+9*1/3-[1*(1/3+0+1/6)+2*(0+0+0)+3*(1/6+0+1/3)]*[1*(1/3+0+1/6)+2*(0+0+0)+3*(1/6+0+1/3)]	|(1*(1/3)+3*(1/6)+3*(1/6)+9*(1/3))-((1/3+1/6)+(1/6+1/3))^2	|[('R.0', 4.333333333333333, u'1*1/3+2*0+3*1/6+2*0+4*0+6*0+3*1/6+6*0+9*1/3', u'1*(1/3)+3*(1/6)+3*(1/6)+9*(1/3)')]	|
|8	|1*1/3+2*0+3*1/6+2*0+4*0+6*0+3*1/6+6*0+9*1/3-[1*(1/3+0+1/6)+2*(0+0+0)+3*(1/6+0+1/3)]*[1*(1/3+0+1/6)+2*(0+0+0)+3*(1/6+0+1/3)]	|1*1/3+2*0+3*1/6+2*0+4*0+6*0+3*1/6+6*0+9*1/3-[1*(1/3+0+1/6)]	|[('R.0', 4.333333333333333, u'1*1/3+2*0+3*1/6+2*0+4*0+6*0+3*1/6+6*0+9*1/3', u'1*1/3+2*0+3*1/6+2*0+4*0+6*0+3*1/6+6*0+9*1/3')]	|
|9	|1*1/3+2*0+3*1/6+2*0+4*0+6*0+3*1/6+6*0+9*1/3-[1*(1/3+0+1/6)+2*(0+0+0)+3*(1/6+0+1/3)]*[1*(1/3+0+1/6)+2*(0+0+0)+3*(1/6+0+1/3)]	|(1*1*(1/3)) + (1*3*(1/6)) + (1*3*(1/6)) + (3*3*(1/3))-((1/3+1/6 + 3/6 + 1)1/3 + 1/6 + 1/2 + 1)	|[('R.0', 4.333333333333333, u'1*1/3+2*0+3*1/6+2*0+4*0+6*0+3*1/6+6*0+9*1/3', u'(1*1*(1/3)) + (1*3*(1/6)) + (1*3*(1/6)) + (3*3*(1/3))')]	|
|10	|1*1/3+2*0+3*1/6+2*0+4*0+6*0+3*1/6+6*0+9*1/3-[1*(1/3+0+1/6)+2*(0+0+0)+3*(1/6+0+1/3)]*[1*(1/3+0+1/6)+2*(0+0+0)+3*(1/6+0+1/3)]	|4.33333-2	|[('R.0', 4.333333333333333, u'1*1/3+2*0+3*1/6+2*0+4*0+6*0+3*1/6+6*0+9*1/3', u'4.33333')]	|




### (14) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:galu

	first_attempt
					2015-10-30 23:54:46
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:00:50', u'2']
	part10_correct_attempt
					['0:00:50', u'2']
	part13_incorrect_attempt
					('0:02:09', u'1/2')
	part13_correct_attempt
					['0:02:19', u'1/3']

1 Student ID:b3hwang

	first_attempt
					2015-10-28 03:26:18
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:00:00', u'(1/2) + 0 + 3/2']
	part10_correct_attempt
					['0:00:00', u'(1/2) + 0 + 3/2']
	part13_incorrect_attempt
					('0:00:00', u'((1/2) + 0 + 3/2) * ((1/2) + 0 + 3/2) - ((1/2) + 0 + 3/2) * ((1/2) + 0 + 3/2)')

2 Student ID:kew017

	first_attempt
					2015-10-30 05:47:27
	part1_correct_attempt
					['0:00:00', u'3/6']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'3/6']
	part4_correct_attempt
					['0:00:00', u'3/6']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'3/6']
	part9_correct_attempt
					['0:00:00', u'(3/6)+0+(9/6)']
	part10_correct_attempt
					['0:00:00', u'(3/6)+0+(9/6)']
	part12_correct_attempt
					['0:12:31', u'13/3']
	part13_incorrect_attempt
					('0:13:57', u'4/(13/3)')
	part13_correct_attempt
					['0:14:25', u'(13/3)-4']

3 Student ID:kew060

	first_attempt
					2015-10-27 19:56:08
	part1_correct_attempt
					['0:00:00', u'0.5']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'0.5']
	part4_correct_attempt
					['0:00:00', u'0.5']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'0.5']
	part9_correct_attempt
					['0:00:42', u'2']
	part10_correct_attempt
					['0:00:42', u'2']
	part12_correct_attempt
					['0:00:42', u'4.33']
	part13_incorrect_attempt
					('0:00:42', u'0.33')
	part13_correct_attempt
					['3:20:18', u'1/3']

4 Student ID:ksmurlo

	first_attempt
					2015-10-29 04:00:19
	part1_correct_attempt
					['0:00:00', u'3/6']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['2:20:48', u'(1/3)+(1/6)+(3/6)+(1)']
	part10_correct_attempt
					['2:21:17', u'2']
	part12_correct_attempt
					['1 day, 2:46:49', u'(1*1*(1/3))+(3*1*(1/6))+(1*3*(1/6))+(3*3*(1/3))']
	part13_incorrect_attempt
					('1 day, 2:54:48', u'.1049382716')
					('1 day, 2:57:23', u'[[(1/3)^2+(1/6)^2+(3/6)^2+(1)^2]/9]-(2/9)^2')
					('1 day, 2:57:53', u'[[(1/3)^2+(1/6)^2+(3/6)^2+(1)^2]/4]-(2/4)^2')
	part13_correct_attempt
					['1 day, 3:04:16', u'(13/3)-(2*2)']

5 Student ID:kebao

	first_attempt
					2015-10-30 04:20:43
	part1_correct_attempt
					['0:00:00', u'1/3+1/6']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/6+1/3']
	part4_correct_attempt
					['0:00:00', u'1/3+1/6']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/3+1/6']
	part9_correct_attempt
					['0:06:26', u'2']
	part10_correct_attempt
					['0:09:34', u'2']
	part12_correct_attempt
					['0:20:32', u'(2+3+3+18)/6']
	part13_incorrect_attempt
					('0:21:10', u'(1/3)*((2+3+3+18)/6)')
	part13_correct_attempt
					['0:22:14', u'(2+3+3+18)/6-4']

6 Student ID:aggouw

	first_attempt
					2015-10-27 03:32:07
	part1_correct_attempt
					['0:00:00', u'1/3+0+1/6']
	part2_correct_attempt
					['0:00:06', u'0']
	part3_correct_attempt
					['0:00:17', u'1/6+1/3']
	part4_correct_attempt
					['0:00:26', u'1/6+1/3']
	part5_correct_attempt
					['0:00:31', u'0']
	part6_correct_attempt
					['0:00:39', u'1/6+1/3']
	part9_correct_attempt
					['0:01:10', u'1*(1/3+0+1/6)+2*(0+0+0)+3*(1/6+0+1/3)']
	part10_correct_attempt
					['0:01:17', u'1*(1/3+0+1/6)+2*(0+0+0)+3*(1/6+0+1/3)']
	part12_correct_attempt
					['0:01:41', u'1*1/3+2*0+3*1/6+2*0+4*0+6*0+3*1/6+6*0+9*1/3']
	part13_incorrect_attempt
					('3 days, 18:38:31', u'1*(1/3+0+1/6)+2*(0+0+0)+3*(1/6+0+1/3) + 1*(1/3+0+1/6)+2*(0+0+0)+3*(1/6+0+1/3)+1*(1/3+0+1/6)+2*(0+0+0)+3*(1/6+0+1/3)')
	part13_correct_attempt
					['3 days, 19:04:36', u'1*1/3+2*0+3*1/6+2*0+4*0+6*0+3*1/6+6*0+9*1/3 -4']

7 Student ID:aportuga

	first_attempt
					2015-10-29 03:01:42
	part1_correct_attempt
					['0:00:00', u'(1/3)+(1/6)']
	part2_correct_attempt
					['0:00:05', u'0']
	part3_correct_attempt
					['0:00:13', u'(1/3)+(1/6)']
	part4_correct_attempt
					['0:00:27', u'(1/3)+(1/6)']
	part5_correct_attempt
					['0:00:27', u'0']
	part6_correct_attempt
					['0:00:27', u'(1/3)+(1/6)']
	part9_correct_attempt
					['0:01:50', u'.5+1.5']
	part10_correct_attempt
					['0:02:04', u'2']
	part12_correct_attempt
					['0:04:02', u'(1/3)+(3/6)+(3/6)+(3)']
	part13_incorrect_attempt
					('0:04:34', u'.5+(9/6)')
	part13_correct_attempt
					['0:07:30', u'((1/3)+(3/6)+(3/6)+(3))-4']

8 Student ID:bpandayk

	first_attempt
					2015-10-30 18:04:24
	part1_correct_attempt
					['0:00:00', u'3/6']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'3/6']
	part9_correct_attempt
					['0:00:34', u'2']
	part10_correct_attempt
					['0:00:34', u'2']
	part12_correct_attempt
					['0:54:30', u'1*1/3+2*0+3*1/6+2*0+4*0+6*0+3*1/6+6*0+9*1/3']
	part13_incorrect_attempt
					('0:56:34', u'4-3.8333')
	part13_correct_attempt
					['0:57:49', u'4.333-4']

9 Student ID:asetters

	first_attempt
					2015-10-27 20:09:54
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:07:21', u'.5 +1.5']
	part10_correct_attempt
					['0:07:21', u'.5 + 1.5']
	part12_correct_attempt
					['0:10:51', u'1/3 +4']
	part13_incorrect_attempt
					('1:49:10', u'(1/3+4)')
	part13_correct_attempt
					['1:51:17', u'(1/3+4) -(4)']

10 Student ID:ajabasa

	first_attempt
					2015-10-29 23:03:26
	part1_correct_attempt
					['0:00:00', u'3/6']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'3/6']
	part4_correct_attempt
					['0:00:16', u'3/6']
	part5_correct_attempt
					['0:00:16', u'0']
	part6_correct_attempt
					['0:00:16', u'3/6']
	part9_correct_attempt
					['0:01:57', u'1/2+9/6']
	part10_correct_attempt
					['0:01:57', u'1/2+9/6']
	part12_correct_attempt
					['0:25:42', u'1/3+3*(1/6)+3*(1/6)+3*3*(1/3)']
	part13_incorrect_attempt
					('0:29:09', u'1/3+3*(1/6)+3*(1/6)+3*3*(1/3)-1/2+9/6-1/2+9/6')
	part13_correct_attempt
					['0:30:24', u'(1/3+3*(1/6)+3*(1/6)+3*3*(1/3))-(1/2+9/6)*(1/2+9/6)']

11 Student ID:masaro

	first_attempt
					2015-10-27 06:45:04
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:00:30', u'2']
	part10_correct_attempt
					['0:02:57', u'2']
	part12_correct_attempt
					['0:09:19', u'4.33']
	part13_incorrect_attempt
					('0:10:58', u'4.33-4')
	part13_correct_attempt
					['0:14:58', u'1*1*1/3+1*3*1/6+3*1*1/6+3*3*1/3-4']

12 Student ID:c3chung

	first_attempt
					2015-10-29 01:48:38
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:00', u'1/2']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/2']
	part9_correct_attempt
					['0:01:15', u'1(1/2) +3(1/2)']
	part10_correct_attempt
					['0:01:15', u'1(1/2) +3(1/2)']
	part13_incorrect_attempt
					('0:01:46', u'.5')
					('1 day, 21:59:28', u'.5')
					('1 day, 21:59:57', u'1.5')
					('1 day, 22:10:18', u'1.5')

13 Student ID:mrchin

	first_attempt
					2015-10-29 23:47:54
	part1_correct_attempt
					['0:00:00', u'3/6']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'3/6']
	part4_correct_attempt
					['0:00:00', u'3/6']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'3/6']
	part9_correct_attempt
					['0:00:00', u'2']
	part10_correct_attempt
					['0:00:00', u'2']
	part12_correct_attempt
					['22:31:51', u'1/3 + 3/6 + 3 + 3/6']
	part13_incorrect_attempt
					('22:32:14', u'4.33 - 4')
	part13_correct_attempt
					['22:32:21', u'1/3']












## Part 15

### (109) Mistake Group Digits of size 109




### (28) Mistake Group Wrong_Sign of size 28




### (16) Mistake Group Fraction of size 16




### (0) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|












## Part 2

### (16) Mistake Group Digits of size 16




### (1) Mistake Group Fraction of size 1




### (0) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|












## Part 3

### (3) Mistake Group Wrong_Sign of size 3




### (19) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:dwzhang

	first_attempt
					2015-10-30 04:54:18
	part3_incorrect_attempt
					('-1 day, 23:58:57', u'1/6 + 1')
	part3_correct_attempt
					['0:00:00', u'1/6 + 1/3']

1 Student ID:jdeon

	first_attempt
					2015-10-30 19:51:09
	part3_incorrect_attempt
					('-1 day, 23:59:22', u'1/3')
	part3_correct_attempt
					['0:00:00', u'1/2']

2 Student ID:a2ahmed

	first_attempt
					2015-10-30 21:26:21
	part3_incorrect_attempt
					('0:02:39', u'1.5')
	part3_correct_attempt
					['0:04:22', u'1/2']

3 Student ID:skodigal

	first_attempt
					2015-10-27 06:24:41
	part3_incorrect_attempt
					('-1 day, 23:58:34', u'2/6')
	part3_correct_attempt
					['0:00:00', u'1/2']

4 Student ID:rraiyyan

	first_attempt
					2015-10-28 01:29:29
	part3_incorrect_attempt
					('-1 day, 23:49:54', u'1/3')
	part3_correct_attempt
					['0:00:00', u'1/2']

5 Student ID:jag028

	first_attempt
					2015-10-30 14:50:53
	part3_incorrect_attempt
					('-1 day, 23:59:23', u'1/6')
	part3_correct_attempt
					['0:00:21', u'1/2']

6 Student ID:jic212

	first_attempt
					2015-10-24 20:12:06
	part3_incorrect_attempt
					('0:00:00', u'(1/3)+(1/3)')
	part3_correct_attempt
					['0:00:09', u'(1/6)+(1/3)']

7 Student ID:t2shin

	first_attempt
					2015-10-28 00:33:52
	part3_incorrect_attempt
					('-1 day, 23:58:50', u'(1/6)^(1/2)')
	part3_correct_attempt
					['0:00:00', u'1/2']

8 Student ID:ctroncos

	first_attempt
					2015-10-29 16:41:49
	part3_incorrect_attempt
					('-1 day, 23:58:44', u'(1/3)')
	part3_correct_attempt
					['0:00:00', u'3/6']

9 Student ID:hkhodada

	first_attempt
					2015-10-24 18:14:12
	part3_incorrect_attempt
					('-1 day, 23:54:22', u'2/3')
	part3_correct_attempt
					['0:00:00', u'1/2']

10 Student ID:dcastlem

	first_attempt
					2015-10-30 22:29:09
	part3_incorrect_attempt
					('-1 day, 23:59:43', u'1/6')
					('0:00:12', u'3/2')
					('0:01:15', u'1.5')
					('0:03:56', u'2.5')
	part3_correct_attempt
					['0:04:26', u'1/2']

11 Student ID:hak014

	first_attempt
					2015-10-26 23:22:18
	part3_incorrect_attempt
					('-1 day, 23:59:30', u'4/6')
	part3_correct_attempt
					['0:00:00', u'3/6']

12 Student ID:qtluong

	first_attempt
					2015-10-29 07:46:16
	part3_incorrect_attempt
					('-1 day, 23:57:10', u'1/3')
	part3_correct_attempt
					['0:00:00', u'1/2']

13 Student ID:r9jiang

	first_attempt
					2015-10-24 07:47:01
	part3_incorrect_attempt
					('-1 day, 23:58:04', u'7/6')
	part3_correct_attempt
					['0:00:00', u'1/2']

14 Student ID:anislam

	first_attempt
					2015-10-29 23:34:32
	part3_incorrect_attempt
					('-1 day, 23:59:03', u'1/3')
	part3_correct_attempt
					['0:00:00', u'1/2']

15 Student ID:avasavad

	first_attempt
					2015-10-28 04:38:13
	part3_incorrect_attempt
					('0:00:11', u'1/3')
	part3_correct_attempt
					['0:00:19', u'1/2']

16 Student ID:small

	first_attempt
					2015-10-30 23:45:51
	part3_incorrect_attempt
					('-1 day, 23:57:45', u'1/3 + 1/6  + 1 + 1/2')
					('-1 day, 23:58:15', u'1/3 + 1/6 + 1 + 1/2')
	part3_correct_attempt
					['0:00:22', u'1/3 + 1/6']

17 Student ID:smohiman

	first_attempt
					2015-10-29 15:58:40
	part3_incorrect_attempt
					('-1 day, 23:58:43', u'1/6')
	part3_correct_attempt
					['0:00:00', u'1/2']

18 Student ID:t2li

	first_attempt
					2015-10-30 23:12:16
	part3_incorrect_attempt
					('0:00:00', u'1.5')
	part3_correct_attempt
					['0:00:12', u'1/2']












## Part 4

### (12) Mistake Group Digits of size 12




### (8) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:skodigal

	first_attempt
					2015-10-27 06:24:41
	part4_incorrect_attempt
					('-1 day, 23:58:34', u'2/6')
	part4_correct_attempt
					['0:00:00', u'1/2']

1 Student ID:jag028

	first_attempt
					2015-10-30 14:50:53
	part4_incorrect_attempt
					('-1 day, 23:59:23', u'1/3')
	part4_correct_attempt
					['0:00:21', u'1/2']

2 Student ID:hkhodada

	first_attempt
					2015-10-24 18:14:12
	part4_incorrect_attempt
					('-1 day, 23:54:22', u'2/3')
	part4_correct_attempt
					['0:00:00', u'1/2']

3 Student ID:hak014

	first_attempt
					2015-10-26 23:22:18
	part4_incorrect_attempt
					('-1 day, 23:59:30', u'4/6')
	part4_correct_attempt
					['0:00:00', u'3/6']

4 Student ID:r9jiang

	first_attempt
					2015-10-24 07:47:01
	part4_incorrect_attempt
					('-1 day, 23:58:04', u'5/6')
	part4_correct_attempt
					['0:00:00', u'1/2']

5 Student ID:anislam

	first_attempt
					2015-10-29 23:34:32
	part4_incorrect_attempt
					('-1 day, 23:59:03', u'1/3')
	part4_correct_attempt
					['0:00:00', u'1/2']

6 Student ID:small

	first_attempt
					2015-10-30 23:45:51
	part4_incorrect_attempt
					('-1 day, 23:58:15', u'1/3 + 1/6 + 1 + 1/2')
	part4_correct_attempt
					['0:00:43', u'1/3 + 1/6']

7 Student ID:smohiman

	first_attempt
					2015-10-29 15:58:40
	part4_incorrect_attempt
					('-1 day, 23:58:43', u'1/3')
	part4_correct_attempt
					['0:00:00', u'1/2']












## Part 5

### (1) Mistake Group Fraction of size 1




### (2) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:small

	first_attempt
					2015-10-30 23:45:51
	part5_incorrect_attempt
					('-1 day, 23:58:15', u'2(1/3 + 1/6 + 1 + 1/2)')
	part5_correct_attempt
					['0:00:43', u'0']

1 Student ID:ctroncos

	first_attempt
					2015-10-29 16:41:49
	part5_incorrect_attempt
					('-1 day, 23:58:44', u'(0)')
	part5_correct_attempt
					['0:00:26', u'0']












## Part 6

### (8) Mistake Group Digits of size 8




### (1) Mistake Group Wrong_Sign of size 1




### (12) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:a2ahmed

	first_attempt
					2015-10-30 21:26:21
	part6_incorrect_attempt
					('0:02:39', u'1.5')
	part6_correct_attempt
					['0:04:22', u'1/2']

1 Student ID:skodigal

	first_attempt
					2015-10-27 06:24:41
	part6_incorrect_attempt
					('-1 day, 23:58:34', u'2/6')
	part6_correct_attempt
					['0:00:00', u'1/2']

2 Student ID:jag028

	first_attempt
					2015-10-30 14:50:53
	part6_incorrect_attempt
					('-1 day, 23:59:23', u'1/6')
	part6_correct_attempt
					['0:00:21', u'1/2']

3 Student ID:n2patil

	first_attempt
					2015-10-28 06:40:48
	part6_incorrect_attempt
					('0:00:35', u'1/3')
	part6_correct_attempt
					['0:00:50', u'1/2']

4 Student ID:hkhodada

	first_attempt
					2015-10-24 18:14:12
	part6_incorrect_attempt
					('-1 day, 23:54:22', u'2/3')
	part6_correct_attempt
					['0:00:00', u'1/2']

5 Student ID:hak014

	first_attempt
					2015-10-26 23:22:18
	part6_incorrect_attempt
					('-1 day, 23:59:30', u'4/6')
	part6_correct_attempt
					['0:00:00', u'3/6']

6 Student ID:r9jiang

	first_attempt
					2015-10-24 07:47:01
	part6_incorrect_attempt
					('-1 day, 23:58:04', u'7/6')
	part6_correct_attempt
					['0:00:00', u'1/2']

7 Student ID:anislam

	first_attempt
					2015-10-29 23:34:32
	part6_incorrect_attempt
					('-1 day, 23:59:03', u'1/3')
	part6_correct_attempt
					['0:00:00', u'1/2']

8 Student ID:small

	first_attempt
					2015-10-30 23:45:51
	part6_incorrect_attempt
					('-1 day, 23:58:15', u'(1/3 + 1/6 + 1 + 1/2)(1/3 + 1/6 + 1 + 1/2)')
	part6_correct_attempt
					['0:00:43', u'1/3 + 1/6']

9 Student ID:mroknich

	first_attempt
					2015-10-26 04:55:01
	part6_incorrect_attempt
					('0:00:00', u'1/6')
	part6_correct_attempt
					['0:00:44', u'1/3+0+1/6']

10 Student ID:smohiman

	first_attempt
					2015-10-29 15:58:40
	part6_incorrect_attempt
					('-1 day, 23:58:43', u'1/6')
	part6_correct_attempt
					['0:00:00', u'1/2']

11 Student ID:acs008

	first_attempt
					2015-10-28 00:34:33
	part6_incorrect_attempt
					('-1 day, 23:58:44', u'1/3')
					('-1 day, 23:58:57', u'2/3')
	part6_correct_attempt
					['0:00:00', u'1/2']












## Part 7

### (115) Mistake Group Digits of size 115




### (1) Mistake Group Fraction of size 1




### (0) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|












## Part 8

### (50) Mistake Group Digits of size 50




### (0) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|












## Part 9

### (66) Mistake Group Fraction of size 66




### (33) Mistake Group Digits of size 33




### (1) Mistake Group Wrong_Sign of size 1




### (4) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:w4shin

	first_attempt
					2015-10-30 18:41:12
	part1_correct_attempt
					['0:00:00', u'1/3+1/6']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/6+1/3']
	part4_correct_attempt
					['0:00:00', u'1/3+1/6']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/6+1/3']
	part9_incorrect_attempt
					('0:00:00', u'(1/3+1/6)+(1/6+1/3)')
	part9_correct_attempt
					['0:04:44', u'1*(1/3+1/6)+3*(1/3+1/6)']

1 Student ID:k5law

	first_attempt
					2015-10-26 06:56:26
	part1_correct_attempt
					['0:00:00', u'(1/3)+(1/6)']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'(1/6)+(1/3)']
	part4_correct_attempt
					['0:00:00', u'(1/3)+(1/6)']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'(1/6)+(1/3)']
	part9_incorrect_attempt
					('0:18:48', u'(1/3)+(1/6)+(1/6)+(1/3)')
	part9_correct_attempt
					['0:22:41', u'(1/3)+(1/6)+[3*[(1/6)+(1/3)]]']

2 Student ID:apokhare

	first_attempt
					2015-10-29 21:20:04
	part1_correct_attempt
					['0:00:00', u'1/3 + 1/6']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/6+1/3']
	part4_correct_attempt
					['0:00:00', u'1/3+1/6']
	part5_correct_attempt
					['0:00:00', u'0']
	part6_correct_attempt
					['0:00:00', u'1/6+1/3']
	part9_incorrect_attempt
					('0:00:00', u'2(1/3 + 1/6)')
	part9_correct_attempt
					['0:02:25', u'(1/3 + 1/6) + 3 * (1/6+1/3)']

3 Student ID:jcl084

	first_attempt
					2015-10-29 00:08:54
	part1_correct_attempt
					['0:00:00', u'1/2']
	part2_correct_attempt
					['0:00:00', u'0']
	part3_correct_attempt
					['0:00:00', u'1/2']
	part4_correct_attempt
					['0:00:17', u'1/2']
	part5_correct_attempt
					['0:00:17', u'0']
	part6_correct_attempt
					['0:00:17', u'1/2']
	part9_incorrect_attempt
					('0:02:04', u'1/2 + 1/2')
	part9_correct_attempt
					['0:02:20', u'1/2 + 3*1/2']












