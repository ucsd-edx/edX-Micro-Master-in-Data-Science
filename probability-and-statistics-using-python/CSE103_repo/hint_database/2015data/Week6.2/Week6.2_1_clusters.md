#Problem 1

    $x = random(8,10,1);
    $X = $x*$x;
    $y = random(0,5,1);
    $lambda = 400/($X);

    You will be using Poisson Distribution in this problem. Review: a discrete random variable [`X`] is said to have a Poisson distribution with parameter [`\lambda > 0`], if for k = 0, 1, 2, ... the probability mass function of [`X`]  is given by:

    [`\Pr(X=k) = e^{-\lambda} \frac{\lambda^k}{k!}`]

    Assume that you live in a district of size [`[$x]`] blocks by [`[$x]`] blocks so that the total district is divided into [`[$X]`] small squares. How likely is it that the square in which you live will receive [`[$y]`] hits if the total area is hit by [`400`] bombs. Assume the probability that a particular bomb will hit your square with probability [`1/[$X]`].

    o What is [`\lambda`] in the Poisson Distribution? [__________]{Compute("400/$X")}

    o Using Poisson Distribution, what is the approximate probability that your square will receive [`[$y]`] hits? [________________]{Compute("e^(-$lambda)*$lambda^$y/($y!)")}

    o What is the expected number of squares that will receive exactly [`[$y]`] hits using the approximate probability from above? [________________]{Compute("($x*$x)*(e^(-$lambda)*$lambda^$y/($y!))")}



## Part 1

### (338) Mistake Group Digits of size 338




### (108) Mistake Group ['R.1'] of size 108
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|400/64	|1/64	|[('R.1', 64.0, u'64', u'64')]	|
|1	|400/81	|1/81	|[('R.1', 81.0, u'81', u'81')]	|
|2	|400/64	|4/64	|[('R.1', 64.0, u'64', u'64')]	|
|3	|400/81	|2/81	|[('R.1', 81.0, u'81', u'81')]	|
|4	|400/81	|4/400*1/81	|[('R.1', 81.0, u'81', u'81')]	|
|5	|400/81	|5/81	|[('R.1', 81.0, u'81', u'81')]	|
|6	|400/64	|600/64	|[('R.1', 64.0, u'64', u'64')]	|
|7	|400/81	|(1/81)	|[('R.1', 81.0, u'81', u'81')]	|
|8	|400/100	|(1/100)*100	|[('R.1', 100.0, u'100', u'100')]	|
|9	|400/64	|3/64	|[('R.1', 64.0, u'64', u'64')]	|
|10	|400/64	|2/64	|[('R.1', 64.0, u'64', u'64')]	|
|11	|400/81	|80200/81	|[('R.1', 81.0, u'81', u'81')]	|
|12	|400/64	|15/64	|[('R.1', 64.0, u'64', u'64')]	|
|13	|400/81	|4*81	|[('R.1', 81.0, u'81', u'81')]	|
|14	|400/81	|4*1/81	|[('R.1', 81.0, u'81', u'81')]	|
|15	|400/64	|5/64	|[('R.1', 64.0, u'64', u'64')]	|
|16	|400/64	|500/64	|[('R.1', 64.0, u'64', u'64')]	|




### (61) Mistake Group Fraction of size 61




### (23) Mistake Group ['R.0'] of size 23
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|400/64	|400/8	|[('R.0', 400.0, u'400', u'400')]	|
|1	|400/64	|400/3	|[('R.0', 400.0, u'400', u'400')]	|
|2	|400/81	|400/9	|[('R.0', 400.0, u'400', u'400')]	|
|3	|400/81	|C(400, 5)	|[('R.0', 400.0, u'400', u'400')]	|
|4	|400/81	|400/5	|[('R.0', 400.0, u'400', u'400')]	|
|5	|400/100	|400/10	|[('R.0', 400.0, u'400', u'400')]	|
|6	|400/64	|400/400	|[('R.0', 400.0, u'400', u'400')]	|
|7	|400/64	|400/(64^5)	|[('R.0', 400.0, u'400', u'400')]	|
|8	|400/64	|400/81	|[('R.0', 400.0, u'400', u'400')]	|
|9	|400/64	|400/100	|[('R.0', 400.0, u'400', u'400')]	|
|10	|400/81	|400/2	|[('R.0', 400.0, u'400', u'400')]	|




### (1) Mistake Group ['R.0', 'R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|400/64	|400*64	|[('R.0', 400.0, u'400', u'400'), ('R.1', 64.0, u'64', u'64')]	|




### (1) Mistake Group Wrong_Sign of size 1




### (38) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:druble

	first_attempt
					2015-11-04 03:45:08
	part1_incorrect_attempt
					('0:00:00', u'1/400')
					('0:00:49', u'81/400')
	part1_correct_attempt
					['0:02:13', u'(1/81) * 400']

1 Student ID:kquong

	first_attempt
					2015-11-01 22:13:18
	part1_incorrect_attempt
					('0:00:00', u'(1/81)^2 * 400')
	part1_correct_attempt
					['0:05:25', u'400/81']

2 Student ID:lywong

	first_attempt
					2015-11-02 04:47:54
	part1_incorrect_attempt
					('0:00:00', u'4/400')
					('0:00:57', u'4/400*(1/81)')
					('0:00:00', u'4/400')
	part1_correct_attempt
					['2 days, 13:23:01', u'(1/81)*400']

3 Student ID:abasu

	first_attempt
					2015-10-31 23:43:50
	part1_incorrect_attempt
					('0:00:00', u'0.16')
	part1_correct_attempt
					['0:01:51', u'400*(1/64)']

4 Student ID:b1yao

	first_attempt
					2015-11-03 06:09:34
	part1_incorrect_attempt
					('0:00:00', u'(1/100)')
					('0:00:20', u'(1/81)^4')
	part1_correct_attempt
					['0:03:23', u'400/81']

5 Student ID:vsosnovs

	first_attempt
					2015-11-05 20:06:51
	part1_incorrect_attempt
					('0:00:00', u'81*400')
	part1_correct_attempt
					['0:00:06', u'1/81*400']

6 Student ID:dlt009

	first_attempt
					2015-11-04 06:06:49
	part1_incorrect_attempt
					('0:00:00', u'1/400')
	part1_correct_attempt
					['0:22:23', u'(1/81)(400)']

7 Student ID:tpmach

	first_attempt
					2015-11-03 23:59:17
	part1_incorrect_attempt
					('0:00:00', u'2/400')
					('0:00:00', u'2/400')
	part1_correct_attempt
					['23:08:47', u'(1/81)400']

8 Student ID:syc078

	first_attempt
					2015-10-30 20:24:15
	part1_incorrect_attempt
					('0:00:00', u'1/3')
	part1_correct_attempt
					['6 days, 4:48:56', u'400/81']

9 Student ID:jhw015

	first_attempt
					2015-11-04 01:31:08
	part1_incorrect_attempt
					('0:00:00', u'1/8')
	part1_correct_attempt
					['0:02:20', u'400/81']

10 Student ID:t2shin

	first_attempt
					2015-11-04 03:50:05
	part1_incorrect_attempt
					('0:00:00', u'(1/100)^400')
	part1_correct_attempt
					['0:00:45', u'4']

11 Student ID:pnquach

	first_attempt
					2015-11-06 01:19:21
	part1_incorrect_attempt
					('0:00:00', u'C(400, 5)*(1/64)^5*(1/64)^395')
					('0:01:29', u'(1/64)^5')
	part1_correct_attempt
					['0:09:19', u'400/64']

12 Student ID:rlhagen

	first_attempt
					2015-10-31 16:02:56
	part1_incorrect_attempt
					('0:00:00', u'(e^(64/400))*((64/400)^3/3)')
					('0:01:33', u'(e^(400/64))*((400/64)^3/3)')
					('0:03:34', u'(e^(400))*((400)^3/3)')
					('0:04:08', u'(e^(-64/400))*((64/400)^3/3)')
					('0:04:32', u'(e^(-400/64))*((400/64)^3/3)')
					('0:04:53', u'(e^(-400/64))*((400/64)^3/3!)')
					('0:05:14', u'(e^(-64/400))*((64/400)^3/3!)')
					('0:07:43', u'(e^(-400/64))*((400/64)^3/3!)')
	part1_correct_attempt
					['0:13:16', u'400/64']

13 Student ID:ganajera

	first_attempt
					2015-11-01 00:37:40
	part1_incorrect_attempt
					('0:00:00', u'0.000086875')
					('0:00:29', u'(1/81)*(80/81)^399')
	part1_correct_attempt
					['2 days, 23:36:28', u'400/81']

14 Student ID:nnh002

	first_attempt
					2015-11-05 01:49:49
	part1_incorrect_attempt
					('0:00:00', u'1/200')
	part1_correct_attempt
					['0:04:08', u'400/81']

15 Student ID:habuamar

	first_attempt
					2015-11-02 23:54:52
	part1_incorrect_attempt
					('0:00:00', u'81*(1/81)')
	part1_correct_attempt
					['0:02:08', u'400*(1/81)']

16 Student ID:dis003

	first_attempt
					2015-11-05 21:06:33
	part1_incorrect_attempt
					('0:00:00', u'9*9')
	part1_correct_attempt
					['0:00:34', u'400/81']

17 Student ID:aakumar

	first_attempt
					2015-11-04 03:01:28
	part1_incorrect_attempt
					('0:00:00', u'.1227')
	part1_correct_attempt
					['0:03:54', u'400/64']

18 Student ID:kew017

	first_attempt
					2015-11-05 06:00:12
	part1_incorrect_attempt
					('0:00:00', u'81/4')
	part1_correct_attempt
					['12:13:52', u'400/81']

19 Student ID:dsmonaha

	first_attempt
					2015-11-02 15:32:49
	part1_incorrect_attempt
					('0:00:00', u'3/400')
	part1_correct_attempt
					['0:06:27', u'400/64']

20 Student ID:hmnaing

	first_attempt
					2015-11-03 23:57:00
	part1_incorrect_attempt
					('0:00:00', u'1/400')
	part1_correct_attempt
					['18:14:02', u'1/81*400']

21 Student ID:eaherman

	first_attempt
					2015-11-06 19:07:56
	part1_incorrect_attempt
					('0:00:00', u'1/[1/81]')
					('0:08:10', u'e')
					('0:08:35', u'2/400')
	part1_correct_attempt
					['0:12:23', u'400/81']

22 Student ID:edescobe

	first_attempt
					2015-11-01 04:11:17
	part1_incorrect_attempt
					('0:00:00', u'79.7327')
					('0:03:13', u'399.52')
	part1_correct_attempt
					['0:07:16', u'400/81']

23 Student ID:lguintu

	first_attempt
					2015-11-03 03:54:50
	part1_incorrect_attempt
					('0:00:00', u'5/400')
	part1_correct_attempt
					['0:00:33', u'400/81']

24 Student ID:tjke

	first_attempt
					2015-11-04 20:18:54
	part1_incorrect_attempt
					('0:00:00', u'1/81^2')
	part1_correct_attempt
					['0:01:58', u'400*1/81']

25 Student ID:acs008

	first_attempt
					2015-11-04 03:48:39
	part1_incorrect_attempt
					('0:00:00', u'1/64^2')
	part1_correct_attempt
					['0:01:55', u'6.25']

26 Student ID:jtfrankl

	first_attempt
					2015-11-06 17:47:53
	part1_incorrect_attempt
					('0:00:00', u'(e**(-400))*(400)')
	part1_correct_attempt
					['0:03:00', u'400/64']

27 Student ID:lahawkin

	first_attempt
					2015-11-04 04:12:18
	part1_incorrect_attempt
					('0:00:00', u'1/400')
	part1_correct_attempt
					['0:05:28', u'400/64']

28 Student ID:cstringh

	first_attempt
					2015-11-03 00:39:45
	part1_incorrect_attempt
					('0:00:00', u'1/9')
					('0:00:13', u'5/400')
					('0:00:53', u'81/5')
	part1_correct_attempt
					['1 day, 5:22:25', u'400/81']

29 Student ID:w4shin

	first_attempt
					2015-11-04 20:50:03
	part1_incorrect_attempt
					('0:00:00', u'2*(1-((1-1/81)^400))')
					('0:01:09', u'(1-((1-1/81)^400))')
	part1_correct_attempt
					['0:04:50', u'400*(1/81)']

30 Student ID:r2fisher

	first_attempt
					2015-11-06 02:49:10
	part1_incorrect_attempt
					('0:00:00', u'(1/81)^400')
					('0:00:45', u'(1/81)^5')
	part1_correct_attempt
					['0:01:17', u'400/81']

31 Student ID:v3doan

	first_attempt
					2015-11-04 18:02:19
	part1_incorrect_attempt
					('0:00:00', u'2/400')
	part1_correct_attempt
					['10:41:39', u'400/81']

32 Student ID:jmiclat

	first_attempt
					2015-11-06 08:01:51
	part1_incorrect_attempt
					('0:00:00', u'3/400')
					('0:04:31', u'1.56')
					('0:05:41', u'3/400')
	part1_correct_attempt
					['0:06:09', u'400/64']

33 Student ID:yil035

	first_attempt
					2015-11-03 23:44:47
	part1_incorrect_attempt
					('0:00:00', u'1/8')
	part1_correct_attempt
					['6:32:45', u'400/64']

34 Student ID:m8woo

	first_attempt
					2015-11-05 20:07:00
	part1_incorrect_attempt
					('0:00:00', u'e^-(400/64) * (400/64)^2/2!')
	part1_correct_attempt
					['0:02:37', u'400/64']

35 Student ID:akg009

	first_attempt
					2015-11-06 19:39:11
	part1_incorrect_attempt
					('0:00:00', u'(1/81)*(1/100)')
	part1_correct_attempt
					['0:42:02', u'400/81']

36 Student ID:ksmurlo

	first_attempt
					2015-11-05 04:44:25
	part1_incorrect_attempt
					('0:00:00', u'64/400')
	part1_correct_attempt
					['0:00:34', u'400/64']

37 Student ID:any027

	first_attempt
					2015-11-01 18:58:58
	part1_incorrect_attempt
					('0:00:00', u'1/400')
					('0:01:47', u'81/400')
	part1_correct_attempt
					['0:01:57', u'(1/81) * 400']












## Part 2

### (20) Mistake Group ['R.0'] of size 20
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|e^-4*4^2/2!	|e^[(-400)*([400^2]/(2!))]	|[('R.0', 2.71828183, u'e', u'e')]	|
|1	|e^-4*4^4/4!	|e^((-4)((4^100)/(100!)))	|[('R.0', 2.71828183, u'e', u'e')]	|
|2	|e^-4*4^4/4!	|e^((-4)((4^1/100)/(1/100!)))	|[('R.0', 2.71828183, u'e', u'e')]	|
|3	|e^-4*4^4/4!	|e^((-4)((4^1/4)/(4!)))	|[('R.0', 2.71828183, u'e', u'e')]	|
|4	|e^-6.25*6.25^0/0!	|e^(400*(1/64))	|[('R.0', 2.71828183, u'e', u'e')]	|
|5	|e^-6.25*6.25^0/0!	|e^-(400*(1/64))*[400*(1/64)^0]	|[('R.0', 2.71828183, u'e', u'e')]	|
|6	|e^-4*4^0/0!	|e^-(1/100)	|[('R.0', 2.71828183, u'e', u'e')]	|
|7	|e^-4*4^0/0!	|e^-(4/100)	|[('R.0', 2.71828183, u'e', u'e')]	|
|8	|e^-6.25*6.25^1/1!	|e^(-400/64)	|[('R.0', 2.71828183, u'e', u'e')]	|
|9	|e^-6.25*6.25^1/1!	|e^-(400/64)	|[('R.0', 2.71828183, u'e', u'e')]	|
|10	|e^-6.25*6.25^0/0!	|e^(400/64)	|[('R.0', 2.71828183, u'e', u'e')]	|
|11	|e^-4.93827*4.93827^2/2!	|e^(3)	|[('R.0', 2.71828183, u'e', u'e')]	|
|12	|e^-4.93827*4.93827^1/1!	|e^(400/81)	|[('R.0', 2.71828183, u'e', u'e')]	|
|13	|e^-4*4^1/1!	|(e^-4)	|[('R.0', 2.71828183, u'e', u'e')]	|
|14	|e^-4.93827*4.93827^0/0!	|e^400	|[('R.0', 2.71828183, u'e', u'e')]	|
|15	|e^-4.93827*4.93827^0/0!	|e^-400	|[('R.0', 2.71828183, u'e', u'e')]	|
|16	|e^-6.25*6.25^0/0!	|(e^6.25)	|[('R.0', 2.71828183, u'e', u'e')]	|




### (13) Mistake Group Digits of size 13




### (3) Mistake Group Wrong_Sign of size 3




### (2) Mistake Group ['R.0', 'R.1.0.1'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|e^-6.25*6.25^5/5!	|e**-64 * 64**5 / 5!	|[('R.0', 2.71828183, u'e', u'e'), ('R.1.0.1', 120, u'5!', u'5!')]	|
|1	|e^-4*4^4/4!	|e^-.01 * (.01^4)/4!	|[('R.0', 2.71828183, u'e', u'e'), ('R.1.0.1', 24, u'4!', u'4!')]	|




### (1) Mistake Group ['R.0', 'R.1.0.0.1', 'R.1.0.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1.0.0.1', 'R.1.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|e^-4*4^3/3!	|e^-3 * (4^3)/3!	|[('R.0', 2.71828183, u'e', u'e'), ('R.1.0.0.1', 64.0, u'4^3', u'4^3'), ('R.1.0.1', 6, u'3!', u'3!')]	|




### (87) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:kew060

	first_attempt
					2015-11-03 02:07:15
	part2_incorrect_attempt
					('0:00:12', u'e^(-6.25) * 6.250/0!')
					('0:00:13', u'e^(-6.25) * 6.250/0!')
	part2_correct_attempt
					['0:00:21', u'0.00193']

1 Student ID:kbielawi

	first_attempt
					2015-11-03 20:28:48
	part2_incorrect_attempt
					('0:00:16', u'5*(400/81)')
					('22:47:26', u'e^(-400)*((400^5)/(5!))')
					('22:52:02', u'((400/81)^5/(5!))*e^(-5)')
	part2_correct_attempt
					['22:52:42', u'((400/81)^5/(5!))*e^(-400/81)']

2 Student ID:l5han

	first_attempt
					2015-11-06 06:11:36
	part2_incorrect_attempt
					('0:00:00', u'e^(400/64)*([(400/64)^2]/2!)')
	part2_correct_attempt
					['0:00:32', u'e^(-400/64)*([(400/64)^2]/2!)']

3 Student ID:mnrahman

	first_attempt
					2015-11-06 21:26:36
	part2_incorrect_attempt
					('-1 day, 23:58:14', u'(e^(-4)*4^1/(1!))')
					('0:00:19', u'(e^(-5)*5^1/(1!))')
					('0:00:49', u'(e^(5)*5^1/(1!))')
					('2:17:57', u'(e^(5)*5^5/(5!))')
					('2:18:54', u'e^(-4)*4^5/(5!)')
	part2_correct_attempt
					['2:20:20', u'e^(-4.93827)* 4.93827 ^5/(5!)']

4 Student ID:jmmcalex

	first_attempt
					2015-11-06 23:03:39
	part2_incorrect_attempt
					('0:01:19', u'((400/64)^5/5(5!))*e^(-400/64)')
					('0:02:24', u'((400/64)^5/(5!))*e^(-400/64)')
	part2_correct_attempt
					['0:03:10', u'((400/64)^0/(0!))*e^(-400/64)']

5 Student ID:dando

	first_attempt
					2015-11-03 16:51:56
	part2_incorrect_attempt
					('-1 day, 23:57:51', u'e^(-100) * ((100^0)/0!)')
					('-1 day, 23:58:21', u'e^(-400) * ((400^0)/0!)')
	part2_correct_attempt
					['0:00:40', u'e^(-4) * ((4^0)/0!)']

6 Student ID:sayao

	first_attempt
					2015-11-04 00:38:17
	part2_incorrect_attempt
					('0:05:22', u'(400/81)/400')
					('0:06:23', u'e^(-400/81)*(400/81)^81/81!')
					('0:06:48', u'e^(-400/9)*(400/9)^9/9!')
					('0:07:25', u'e^(-400/81)*(400/81)^9/9!')
	part2_correct_attempt
					['0:08:40', u'e^(-400/81)*(400/81)^4/4!']

7 Student ID:c1wei

	first_attempt
					2015-11-04 06:08:38
	part2_incorrect_attempt
					('-1 day, 23:54:01', u'(1/64)^3')
					('0:00:13', u'(400/64)^3')
	part2_correct_attempt
					['0:01:25', u'e^(-400/64)* ((400/64)^3)/(3!)']

8 Student ID:mitopete

	first_attempt
					2015-11-04 03:19:34
	part2_incorrect_attempt
					('0:05:53', u'6/(e^6)')
					('0:07:33', u'1/64')
	part2_correct_attempt
					['0:10:04', u'(25/4)/(e^(25/4))']

9 Student ID:tak068

	first_attempt
					2015-11-05 20:47:17
	part2_incorrect_attempt
					('0:00:00', u'"e^(-400/81)*(400/81)^3/(3!)"')
					('0:00:05', u'e^(-400/81)*(400/81)^3/(3!)"')
	part2_correct_attempt
					['0:00:29', u'e^(-400/81)*(400/81)^3/(3!)']

10 Student ID:druble

	first_attempt
					2015-11-04 03:47:21
	part2_incorrect_attempt
					('-1 day, 23:55:37', u'(e^-81)(81/1)')
					('-1 day, 23:57:09', u'(e^-400)*(400/1)')
	part2_correct_attempt
					['0:00:00', u'(e^-((1/81) * 400))*(((1/81) * 400)/1)']

11 Student ID:jag028

	first_attempt
					2015-11-02 15:56:08
	part2_incorrect_attempt
					('-1 day, 15:51:22', u'1/100')
					('0:04:10', u'(e^(-4)((4)/1!))100')
					('0:06:54', u'(e^(-4)((4(1/100))/(100)!))100')
	part2_correct_attempt
					['2:59:50', u'e^(-4)[(4^1)/(1!)]']

12 Student ID:ccn001

	first_attempt
					2015-11-02 21:59:00
	part2_incorrect_attempt
					('-1 day, 23:45:37', u'e^(-400)((400^2)/(2!))')
					('-1 day, 23:52:36', u'400(1/64)')
	part2_correct_attempt
					['0:00:00', u'e^(-400/64)(400/64)^2/(2!)']

13 Student ID:skarimik

	first_attempt
					2015-10-31 20:44:55
	part2_incorrect_attempt
					('0:02:13', u'e^(-4)4^(100)/100!')
	part2_correct_attempt
					['0:07:40', u'e^(-4)4^(4)/4!']

14 Student ID:anislam

	first_attempt
					2015-11-05 04:51:07
	part2_incorrect_attempt
					('-1 day, 23:59:20', u'e^(-40) * (40^4 / 4!)')
	part2_correct_attempt
					['0:00:00', u'e^(-4) * (4^4 / 4!)']

15 Student ID:tpmach

	first_attempt
					2015-11-04 23:08:04
	part2_incorrect_attempt
					('0:03:12', u'e^(400/81)*(((400/81)^2)/2!)')
	part2_correct_attempt
					['0:03:29', u'e^(-400/81)*(((400/81)^2)/2!)']

16 Student ID:jhw015

	first_attempt
					2015-11-04 01:33:28
	part2_incorrect_attempt
					('0:02:24', u'400 * (400/81)')
	part2_correct_attempt
					['0:08:16', u'e ^-(400/81) * ((400/81)^5 / 5!)']

17 Student ID:r1gu

	first_attempt
					2015-11-05 11:35:40
	part2_incorrect_attempt
					('0:02:34', u'e^(400/81)*(400/81)^2/2!')
					('0:02:59', u'e^(400/81)*((400/81)^2/2!)')
	part2_correct_attempt
					['0:03:51', u'e^(-400/81)*((400/81)^2/2!)']

18 Student ID:t1tran

	first_attempt
					2015-10-31 04:45:56
	part2_incorrect_attempt
					('-1 day, 23:46:01', u'2/81')
					('-1 day, 23:46:25', u'1/81^2')
	part2_correct_attempt
					['0:00:00', u'e^(-400/81)(400/81)^(2)/2!']

19 Student ID:thwan

	first_attempt
					2015-11-06 18:21:59
	part2_incorrect_attempt
					('-1 day, 23:56:56', u'1/81*e^(-400/81)')
	part2_correct_attempt
					['0:01:24', u'e^(-400/81)*(400/81)']

20 Student ID:hmnaing

	first_attempt
					2015-11-04 18:11:02
	part2_incorrect_attempt
					('0:01:23', u'2/81')
	part2_correct_attempt
					['0:04:18', u'e^(-1/81*400)* ( (1/81*400)^2/ (2)!)']

21 Student ID:edescobe

	first_attempt
					2015-11-01 04:18:33
	part2_incorrect_attempt
					('0:03:36', u'1/(81*81*81)')
	part2_correct_attempt
					['0:09:02', u'.1438']

22 Student ID:w4shin

	first_attempt
					2015-11-04 20:54:53
	part2_incorrect_attempt
					('-1 day, 23:55:10', u'(e^(-2*(1-(1-1/81)^400))*(2*(1-((1-1/81)^400)))^2)/2')
	part2_correct_attempt
					['0:00:00', u'(e^(-400*(1/81))*(400*(1/81))^2)/2']

23 Student ID:etemlock

	first_attempt
					2015-11-02 03:31:30
	part2_incorrect_attempt
					('0:02:05', u'(e^4.93827)[ (4.93827^2)/2]')
	part2_correct_attempt
					['0:02:15', u'(e^-4.93827)[ (4.93827^2)/2]']

24 Student ID:muy002

	first_attempt
					2015-11-05 03:52:30
	part2_incorrect_attempt
					('-1 day, 23:58:36', u'(1/81)^2*e^(-1/81)/2!')
	part2_correct_attempt
					['0:00:00', u'(400/81)^2*e^(-400/81)/2!']

25 Student ID:cstringh

	first_attempt
					2015-11-04 06:02:10
	part2_incorrect_attempt
					('-2 days, 17:42:36', u'1/81')
					('-2 days, 18:36:42', u'e')
	part2_correct_attempt
					['0:03:08', u'e^(-400/81)*(((400/81)^5)/(5!))']

26 Student ID:eshung

	first_attempt
					2015-10-30 21:41:44
	part2_incorrect_attempt
					('0:01:59', u'0.147')
	part2_correct_attempt
					['0:02:46', u'8/e^4']

27 Student ID:v4sharma

	first_attempt
					2015-10-31 21:43:28
	part2_incorrect_attempt
					('0:01:20', u'(e^4)(4^5)/(5!)')
	part2_correct_attempt
					['0:01:29', u'(e^-4)(4^5)/(5!)']

28 Student ID:ralhadda

	first_attempt
					2015-10-31 18:39:17
	part2_incorrect_attempt
					('0:17:46', u'1/100')
	part2_correct_attempt
					['0:19:22', u'e^-4 (4^0/0!)']

29 Student ID:yjshin

	first_attempt
					2015-11-05 20:57:33
	part2_incorrect_attempt
					('0:08:06', u'(64^(-400/64))((400/64)^3/6)')
	part2_correct_attempt
					['0:12:21', u'e^(-400/64)((400/64)^3/6)']

30 Student ID:bpandayk

	first_attempt
					2015-11-06 21:12:53
	part2_incorrect_attempt
					('0:00:38', u'e^-((400*1)/64)(((400*1)/64)^5/(5!))')
	part2_correct_attempt
					['0:01:03', u'e^-((400*1)/64)(((400*1)/64)^2/(2!))']

31 Student ID:hsc052

	first_attempt
					2015-11-05 07:03:28
	part2_incorrect_attempt
					('-1 day, 23:46:04', u'1/(e*2)')
	part2_correct_attempt
					['0:01:39', u'e^(-4) * (4^2)/2!']

32 Student ID:yil035

	first_attempt
					2015-11-04 06:17:32
	part2_incorrect_attempt
					('-1 day, 17:26:07', u'5/64')
					('-1 day, 17:27:15', u'5/8')
					('-1 day, 17:31:44', u'0.09160366')
					('0:00:00', u'e^(-400/64)*((400/64)^5)/240')
	part2_correct_attempt
					['0:00:54', u'e^(-400/64)*((400/64)^5)/120']

33 Student ID:cfgutier

	first_attempt
					2015-11-05 22:01:57
	part2_incorrect_attempt
					('0:11:50', u'.130')
					('0:21:20', u'.078')
	part2_correct_attempt
					['0:26:03', u'.0785']

34 Student ID:k3tan

	first_attempt
					2015-11-04 01:33:05
	part2_incorrect_attempt
					('0:06:27', u'e^(400/81)*((400/81)^5/(5!))')
	part2_correct_attempt
					['0:06:37', u'e^-(400/81)*((400/81)^5/(5!))']

35 Student ID:ctroncos

	first_attempt
					2015-11-04 01:30:39
	part2_incorrect_attempt
					('-1 day, 23:59:17', u'C(400,10)')
					('0:04:33', u'e^(100)*(100)^2/(2!)')
					('0:05:04', u'e^(400/100)*(400/100)^2/(2!)')
	part2_correct_attempt
					['0:06:11', u'e^(-400/100)*(400/100)^2/(2!)']

36 Student ID:jix029

	first_attempt
					2015-11-01 04:44:21
	part2_incorrect_attempt
					('0:00:00', u'.195')
	part2_correct_attempt
					['0:00:39', u'.19537']

37 Student ID:kebao

	first_attempt
					2015-11-05 18:37:39
	part2_incorrect_attempt
					('-1 day, 23:59:19', u'e^(-400/8)*(400/8)^5/5!')
	part2_correct_attempt
					['0:00:00', u'e^(-400/64)*(400/64)^5/5!']

38 Student ID:d6he

	first_attempt
					2015-11-05 02:28:46
	part2_incorrect_attempt
					('-1 day, 23:50:25', u'400/(64^5)')
	part2_correct_attempt
					['0:01:48', u'e^(-6.25)*(6.25^5)/(5!)']

39 Student ID:awollner

	first_attempt
					2015-11-03 18:13:00
	part2_incorrect_attempt
					('0:01:17', u'e^6.25(6.25^63/63!)')
					('0:01:38', u'e^-6.25(6.25^63/63!)')
					('5:01:13', u'e^-6.5(6.5^63/63!)')
					('3 days, 3:53:31', u'e^-6.5(6.5^64/64!)')
					('3 days, 3:53:56', u'e^-6.5(6.5^0/0!)')
					('3 days, 3:56:05', u'e^-6.5(6.5^64/64!)')
					('3 days, 3:58:07', u'e^-6.5(6.5^1/1!)')
					('3 days, 3:58:25', u'e^-6.5(6.5^0/0!)')
	part2_correct_attempt
					['3 days, 3:58:56', u'e^-6.25(6.25^0/0!)']

40 Student ID:dcrume

	first_attempt
					2015-11-06 16:59:20
	part2_incorrect_attempt
					('-1 day, 23:47:42', u'e^(-1/100)*(1)/0!')
	part2_correct_attempt
					['0:00:00', u'e^(-4)*(4^0)/1']

41 Student ID:jcj006

	first_attempt
					2015-11-03 01:28:33
	part2_incorrect_attempt
					('-1 day, 23:57:16', u'e^(-1/64)/(64^2*2)')
					('0:00:00', u'e^(-1/64)*160000/(64^2*2)')
	part2_correct_attempt
					['0:00:17', u'e^(-400/64)*160000/(64^2*2)']

42 Student ID:dlt009

	first_attempt
					2015-11-04 06:29:12
	part2_incorrect_attempt
					('-1 day, 16:54:47', u'(e^-(1/81))((1/81)^5)/(5!)')
					('-1 day, 23:19:18', u'(e^-(1))((1)^5)/(5!)')
					('0:02:44', u'e^((1/81)(400))([(1/81)(400)]^5)/(5!)')
	part2_correct_attempt
					['0:03:16', u'e^((-1/81)(400))([(1/81)(400)]^5)/(5!)']

43 Student ID:jeqin

	first_attempt
					2015-11-05 06:42:17
	part2_incorrect_attempt
					('0:00:31', u'[e^-4][(4^100)/100!]')
	part2_correct_attempt
					['0:01:29', u'[e^-4][(4^0)/0!]']

44 Student ID:jnatale

	first_attempt
					2015-11-04 07:19:59
	part2_incorrect_attempt
					('0:00:00', u'e^(-400) * 400')
					('0:00:14', u'e^(-4.94) * 4.94')
	part2_correct_attempt
					['0:00:30', u'e^(-(400/81)) * (400/81)']

45 Student ID:nnh002

	first_attempt
					2015-11-05 01:53:57
	part2_incorrect_attempt
					('-2 days, 15:23:51', u'800/e')
					('0:06:58', u'147.151229127')
					('0:08:12', u'e^(400/81)*((400/81)^2/2!)')
	part2_correct_attempt
					['0:09:59', u'e^(-400/81)*((400/81)^2/2!)']

46 Student ID:agian

	first_attempt
					2015-11-07 00:09:57
	part2_incorrect_attempt
					('0:00:41', u'(e^(-4)*4^1/(1!))')
					('0:01:08', u'(e^(-8)*8^1/(1!))')
					('0:01:26', u'(e^(-2)*2^1/(1!))')
					('0:01:56', u'(e^(-6.25)*6.25^1/(1!))')
					('0:02:22', u'(e^(-6.25)*6.25^2/(1!))')
	part2_correct_attempt
					['0:03:27', u'(e^(-6.25)*6.25^2/(2!))']

47 Student ID:aakumar

	first_attempt
					2015-11-04 03:05:22
	part2_incorrect_attempt
					('-1 day, 23:58:40', u'.1227')
					('0:01:12', u'1-e^(-400/64)')
	part2_correct_attempt
					['0:08:34', u'(400/64)e^-(400/64)']

48 Student ID:kew017

	first_attempt
					2015-11-05 18:14:04
	part2_incorrect_attempt
					('0:00:00', u'(e^-(400/81))(((4)^(400/81))/4!)')
	part2_correct_attempt
					['0:00:20', u'(e^-(400/81))(((400/81)^4)/4!)']

49 Student ID:q3wen

	first_attempt
					2015-11-03 21:20:02
	part2_incorrect_attempt
					('0:00:00', u'1.31*10^-41')
	part2_correct_attempt
					['0:02:28', u'0.001930']

50 Student ID:yeh013

	first_attempt
					2015-11-03 07:35:18
	part2_incorrect_attempt
					('0:01:14', u'(400/81)/e^(400/81)')
					('0:04:47', u'400/e^400')
					('0:05:10', u'(1/81)/e^(1/81)')
					('0:06:43', u'1-(1/81)')
	part2_correct_attempt
					['0:09:18', u'e^(-400/81)']

51 Student ID:eaherman

	first_attempt
					2015-11-06 19:20:19
	part2_incorrect_attempt
					('0:00:13', u'81/400')
					('0:00:50', u'[(81)(2)]/400')
					('0:01:28', u'400/[(81)(2)]')
	part2_correct_attempt
					['0:05:24', u'e^[-[400/81]]([400/81]^2)/2']

52 Student ID:arvenega

	first_attempt
					2015-11-06 23:31:58
	part2_incorrect_attempt
					('0:00:00', u'(e^6.25)*((6.25^5)/5!)')
					('0:06:17', u'(e^6.25)*((6.25^0)/0!)')
					('0:06:43', u'(e^6.25)*(6.25^0)')
	part2_correct_attempt
					['0:30:43', u'(e^-6.25)']

53 Student ID:yhhan

	first_attempt
					2015-11-06 23:27:51
	part2_incorrect_attempt
					('0:00:41', u'3/400')

54 Student ID:cagatep

	first_attempt
					2015-11-05 05:55:53
	part2_incorrect_attempt
					('-1 day, 23:42:52', u'400/(100^4)')
					('-1 day, 23:46:17', u'1/(100^4)')
	part2_correct_attempt
					['0:07:21', u'(4^4 * e ^(-4))/(4!)']

55 Student ID:ytc012

	first_attempt
					2015-11-05 09:14:14
	part2_incorrect_attempt
					('0:01:19', u'(e^-4)(4^100)/100')
					('0:01:47', u'1/5')
					('0:01:55', u'1/20')
	part2_correct_attempt
					['12:35:15', u'(e^-4)*(4^5)/5!']

56 Student ID:klala

	first_attempt
					2015-11-05 05:46:14
	part2_incorrect_attempt
					('-1 day, 23:58:39', u'(e^(-.01) * (.01)^4)/(4!)')
					('0:06:04', u'(4^100)*(e^-4)/(100!)')
	part2_correct_attempt
					['0:06:17', u'(4^4)*(e^-4)/(4!)']

57 Student ID:cprafull

	first_attempt
					2015-11-04 02:23:00
	part2_incorrect_attempt
					('0:01:48', u'((400/64)^3)*(e^(400/64))/3!')
					('0:02:25', u'((6.25)^3)*(e^(6.25))/3!')
	part2_correct_attempt
					['0:02:40', u'((6.25)^3)*(e^(-6.25))/3!']

58 Student ID:dmn009

	first_attempt
					2015-11-05 01:10:26
	part2_incorrect_attempt
					('0:01:32', u'(e^4.938)*4.938')
	part2_correct_attempt
					['0:01:59', u'(e^-4.938)*4.938']

59 Student ID:galu

	first_attempt
					2015-11-07 00:31:18
	part2_incorrect_attempt
					('0:00:00', u'1/100')
					('0:00:00', u'5/100')
					('0:00:00', u'1/1000000')

60 Student ID:t2shin

	first_attempt
					2015-11-04 03:50:50
	part2_incorrect_attempt
					('0:00:58', u'(e^-4)(e^2)/(2)')
	part2_correct_attempt
					['0:01:16', u'(e^-4)(4^2)/(2)']

61 Student ID:vsamant

	first_attempt
					2015-10-30 23:06:39
	part2_incorrect_attempt
					('-1 day, 23:53:02', u'e^(-400)*400^5/5!')
	part2_correct_attempt
					['0:00:00', u'e^(-4)*4^5/5!']

62 Student ID:rohan

	first_attempt
					2015-11-06 22:11:26
	part2_incorrect_attempt
					('0:00:00', u'400/81')
					('0:08:43', u'1-e^(-400/81)')
	part2_correct_attempt
					['0:09:54', u'e^(-400/81)']

63 Student ID:pcdo

	first_attempt
					2015-11-02 18:22:28
	part2_incorrect_attempt
					('-1 day, 23:59:32', u'e^(-400/9)*(400/9)^2/(2!)')
	part2_correct_attempt
					['0:00:08', u'e^(-400/81)*(400/81)^2/(2!)']

64 Student ID:k5law

	first_attempt
					2015-11-04 06:57:17
	part2_incorrect_attempt
					('0:00:00', u'e^(-4.9)*16/2')
					('0:02:05', u'e^([400*(1/81)])*[16/2]')
					('0:02:36', u'e^([400*(1/81)])*[[400*(1/81)]^2/2]')
	part2_correct_attempt
					['0:02:52', u'e^(-[400*(1/81)])*[[400*(1/81)]^2/2]']

65 Student ID:gsrandha

	first_attempt
					2015-11-05 00:10:02
	part2_incorrect_attempt
					('0:14:14', u'.25')
					('0:15:07', u'(e^-4) * (4^100 / 100!)')
					('0:15:18', u'(e^-4) * (4^10 / 10!)')
	part2_correct_attempt
					['6:27:58', u'(e^-4) * (4/1) ']

66 Student ID:dcgriffi

	first_attempt
					2015-11-06 23:05:39
	part2_incorrect_attempt
					('0:00:00', u'e^(-400/81)*(400/81)/(81!)')
	part2_correct_attempt
					['0:00:40', u'e^(-400/81)*(400/81)']

67 Student ID:rsmurlo

	first_attempt
					2015-11-03 16:50:01
	part2_incorrect_attempt
					('0:05:47', u'(1/6.25)(6.25^5/(5!))')
	part2_correct_attempt
					['0:06:11', u'(1/(e^6.25))(6.25^5/(5!))']

68 Student ID:anl114

	first_attempt
					2015-11-05 22:21:51
	part2_incorrect_attempt
					('0:01:58', u'(e^(-400/81)) * (((400/81)^9)/9!)')
					('0:02:37', u'81*(e^(-400/81)) * (((400/81)^9)/9!)')
					('0:03:25', u'81*(e^(-400/81)) * (((400/81)^4)/4!)')
	part2_correct_attempt
					['0:03:38', u'(e^(-400/81)) * (((400/81)^4)/4!)']

69 Student ID:pnquach

	first_attempt
					2015-11-06 01:28:40
	part2_incorrect_attempt
					('-1 day, 23:38:19', u'(e^(-1/64))*(((1/64)^5)/(5!))')
	part2_correct_attempt
					['0:00:22', u'(e^(-400/64))*(((400/64)^5)/(5!))']

70 Student ID:agarango

	first_attempt
					2015-11-05 02:16:20
	part2_incorrect_attempt
					('0:02:42', u'3.64*10^-63')
					('0:41:22', u'1.8693728 * 10^-67')
					('0:42:12', u'0.00059396572')
	part2_correct_attempt
					['1:42:14', u'0.03539246932']

71 Student ID:twsalim

	first_attempt
					2015-11-04 00:07:20
	part2_incorrect_attempt
					('0:00:00', u'0.195')
	part2_correct_attempt
					['0:02:14', u'0.1953668']

72 Student ID:jap009

	first_attempt
					2015-11-05 18:12:02
	part2_incorrect_attempt
					('0:00:19', u'4/400')
	part2_correct_attempt
					['0:00:46', u'(e^(-4))*(4/1)']

73 Student ID:b1yao

	first_attempt
					2015-11-03 06:12:57
	part2_incorrect_attempt
					('-1 day, 23:49:02', u'((1/81)^4*e^(-(1/81)))/(4!)')
					('-1 day, 23:55:16', u'((400)^4*e^(-(400)))/(4!)')
					('-1 day, 23:55:26', u'((4)^4*e^(-(4)))/(4!)')
					('-1 day, 23:55:39', u'((81)^4*e^(-(81)))/(4!)')
	part2_correct_attempt
					['0:00:09', u'((400/81)^4*e^(-(400/81)))/(4!)']

74 Student ID:aadhakal

	first_attempt
					2015-11-05 20:49:57
	part2_incorrect_attempt
					('0:00:00', u'0.732625556')
					('0:03:12', u'218.39')
					('0:03:53', u'0.073')
	part2_correct_attempt
					['0:11:03', u'(e^(-4)*4^1/(1!))']

75 Student ID:acs008

	first_attempt
					2015-11-04 03:50:34
	part2_incorrect_attempt
					('0:01:36', u'10117.438')
	part2_correct_attempt
					['0:02:07', u'e^(-6.25)*(6.25^2)/2']

76 Student ID:hmshah

	first_attempt
					2015-11-05 08:56:22
	part2_incorrect_attempt
					('0:01:42', u'(e^(6.25))*((4^6.25)/4!)')
					('0:04:26', u'1/64')
	part2_correct_attempt
					['0:06:19', u'e^(-6.25)*6.25^5/(5!)']

77 Student ID:ahh002

	first_attempt
					2015-11-04 11:07:38
	part2_incorrect_attempt
					('-1 day, 19:31:22', u'(e^-(1/81))((1/81)^5)/5!')
	part2_correct_attempt
					['0:01:25', u'(e^-(400/81))((400/81)^5)/5!']

78 Student ID:kquong

	first_attempt
					2015-11-01 22:18:43
	part2_incorrect_attempt
					('0:00:29', u'400/81/81')
	part2_correct_attempt
					['0:02:08', u'e^(-400/81) * (400/81)^2/2']

79 Student ID:xweng

	first_attempt
					2015-11-05 22:46:20
	part2_incorrect_attempt
					('0:05:24', u'1/100')
					('0:05:29', u'99/100')
					('0:07:45', u'400/100')
					('0:07:51', u'400*99/100')
					('0:10:37', u'4^100*e^-4/100!')
					('0:12:15', u'(99/100)^400')
	part2_correct_attempt
					['0:16:33', u'e^-4/1']

80 Student ID:c3chung

	first_attempt
					2015-11-05 08:42:53
	part2_incorrect_attempt
					('-1 day, 23:59:38', u'e^(-400) * 400^(100)/100!')
					('0:00:23', u'e^(-4) * 4^(100)/100!')
					('0:01:12', u'e^(-4) * 4^(1/100)/1/100!')
	part2_correct_attempt
					['0:01:56', u'e^(-4) * 4^(3)/3!']

81 Student ID:ajvanega

	first_attempt
					2015-11-05 00:19:54
	part2_incorrect_attempt
					('0:03:27', u'(e^(400/81))*(400/81)')
	part2_correct_attempt
					['0:04:05', u'(e^(-400/81))*(400/81)']

82 Student ID:zhw110

	first_attempt
					2015-11-03 21:41:45
	part2_incorrect_attempt
					('0:02:42', u'e^(-400/81)*(400/81)^81/(81!)')
	part2_correct_attempt
					['0:03:47', u'e^(-400/81)*(400/81)/(1)']

83 Student ID:mtrafeca

	first_attempt
					2015-11-01 22:37:32
	part2_incorrect_attempt
					('0:00:47', u'400/64 * 4')
					('0:00:57', u'4/64')
					('0:01:07', u'(4/64)*400')
					('0:02:38', u'e^(-6.2)*(6.25^(4)/(4!))')
	part2_correct_attempt
					['0:02:48', u'e^(-6.25)*(6.25^(4)/(4!))']

84 Student ID:kosung

	first_attempt
					2015-11-05 06:41:04
	part2_incorrect_attempt
					('0:00:26', u'0.78466')
					('0:00:36', u'0.78446')
	part2_correct_attempt
					['0:08:03', u'0.1563']

85 Student ID:whcombs

	first_attempt
					2015-11-04 18:15:12
	part2_incorrect_attempt
					('0:00:00', u'e^((1/100)(400))((1/100)(400)^5/5!)')
					('0:00:53', u'e^((1/100)(400))(((1/100)(400))^5/5!)')
	part2_correct_attempt
					['0:01:26', u'e^(-(1/100)(400))(((1/100)(400))^5/5!)']

86 Student ID:j2phung

	first_attempt
					2015-11-03 17:48:49
	part2_incorrect_attempt
					('0:09:57', u'(e^(-4))((4^(100))/(100!))')
					('0:14:41', u'(e^(-4))((4^(1))/(1!))')
					('0:15:03', u'(e^(-4))((4^(4))/(4!))')
	part2_correct_attempt
					['0:17:39', u'(e^(-4))((4^(0))/(0!))']












## Part 3

### (134) Mistake Group Digits of size 134




### (40) Mistake Group redirect of size 40




### (14) Mistake Group ['R.0'] of size 14
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|9*9*e^-4.93827*4.93827^2/2!	|81(2/400)	|[('R.0', 81.0, u'9*9', u'81')]	|
|1	|8*8*e^-6.25*6.25^4/4!	|64-49	|[('R.0', 64.0, u'8*8', u'64')]	|
|2	|9*9*e^-4.93827*4.93827^1/1!	|81/400	|[('R.0', 81.0, u'9*9', u'81')]	|
|3	|8*8*e^-6.25*6.25^1/1!	|64/(25/4)	|[('R.0', 64.0, u'8*8', u'64')]	|
|4	|9*9*e^-4.93827*4.93827^2/2!	|81*((e^(-2*(1-(1-1/81)^400))*(2*(1-((1-1/81)^400)))^2)/2)	|[('R.0', 81.0, u'9*9', u'81')]	|
|5	|8*8*e^-6.25*6.25^5/5!	|64/((e^(-6.25))*((6.25^5)/5!))	|[('R.0', 64.0, u'8*8', u'64')]	|
|6	|8*8*e^-6.25*6.25^5/5!	|64*((e^(-1/64))*(((1/64)^5)/(5!)))	|[('R.0', 64.0, u'8*8', u'64')]	|
|7	|9*9*e^-4.93827*4.93827^5/5!	|81/0.1754	|[('R.0', 81.0, u'9*9', u'81')]	|
|8	|10*10*e^-4*4^5/5!	|100 * .156	|[('R.0', 100.0, u'10*10', u'100')]	|
|9	|8*8*e^-6.25*6.25^2/2!	|64*[e^(400/64)*([(400/64)^2]/2!)]	|[('R.0', 64.0, u'8*8', u'64')]	|
|10	|9*9*e^-4.93827*4.93827^2/2!	|81/[e^[-[400/81]]([400/81]^2)/2]	|[('R.0', 81.0, u'9*9', u'81')]	|
|11	|8*8*e^-6.25*6.25^2/2!	|64*(e^-((400*1)/81)(((400*1)/64)^5/(5!)))	|[('R.0', 64.0, u'8*8', u'64')]	|
|12	|8*8*e^-6.25*6.25^2/2!	|64*(e^-((400*1)/81)(((400*1)/64)^2/(2!)))	|[('R.0', 64.0, u'8*8', u'64')]	|




### (7) Mistake Group ['R.1.0'] of size 7
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|9*9*e^-4.93827*4.93827^0/0!	|((400/81)**0)/(e**(400/81))	|[('R.1.0', 2.71828183, u'e', u'e')]	|
|1	|10*10*e^-4*4^0/0!	|1-(e^-(1/100))	|[('R.1.0', 2.71828183, u'e', u'e')]	|
|2	|10*10*e^-4*4^0/0!	|1-(e^-(4/100))	|[('R.1.0', 2.71828183, u'e', u'e')]	|
|3	|9*9*e^-4.93827*4.93827^5/5!	|100 * e ^-(400/81) * ((400/81)^5 / 5!)	|[('R.1.0', 2.71828183, u'e', u'e')]	|
|4	|8*8*e^-6.25*6.25^5/5!	|6.25^5 * e^-6.25 / 5! * 400	|[('R.1.0', 2.71828183, u'e', u'e')]	|
|5	|9*9*e^-4.93827*4.93827^4/4!	|400*e^-(400/81) * ((400/81)^4/4!)	|[('R.1.0', 2.71828183, u'e', u'e')]	|
|6	|10*10*e^-4*4^0/0!	|4^100*e^-4/100!	|[('R.1.0', 2.71828183, u'e', u'e')]	|




### (5) Mistake Group ['R.1'] of size 5
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|8*8*e^-6.25*6.25^0/0!	|400*(e^(-6.25)*(6.25^0)/0!)	|[('R.1', 0.0019304541293880429, u'e^-6.25*6.25^0/0!', u'e^(-6.25)*(6.25^0)/0!')]	|
|1	|8*8*e^-6.25*6.25^0/0!	|400/(e^(-6.25)*(6.25^0)/0!)	|[('R.1', 0.0019304541293880429, u'e^-6.25*6.25^0/0!', u'e^(-6.25)*(6.25^0)/0!')]	|
|2	|9*9*e^-4.93827*4.93827^0/0!	|(400/81)*0.00716698	|[('R.1', 0.007166986520110665, u'e^-4.93827*4.93827^0/0!', u'0.00716698')]	|
|3	|8*8*e^-6.25*6.25^0/0!	|400*(e^-(400/64))	|[('R.1', 0.0019304541293880429, u'e^-6.25*6.25^0/0!', u'e^-(400/64)')]	|
|4	|10*10*e^-4*4^0/0!	|400*([e^-4][(4^0)/0!])	|[('R.1', 0.018315638847202696, u'e^-4*4^0/0!', u'[e^-4][(4^0)/0!]')]	|




### (2) Mistake Group ['R.1.0', 'R.1.1'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.0', 'R.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|9*9*e^-4.93827*4.93827^0/0!	|1-e^(-400/81)	|[('R.1.0', 2.71828183, u'e', u'e'), ('R.1.1', -4.93827, u'-4.93827*4.93827^0/0!', u'-400/81')]	|
|1	|9*9*e^-4.93827*4.93827^0/0!	|3321(e^(-400/81))	|[('R.1.0', 2.71828183, u'e', u'e'), ('R.1.1', -4.93827, u'-4.93827*4.93827^0/0!', u'-400/81')]	|




### (1) Mistake Group ['R.0', 'R.1.0', 'R.1.1.0.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1.0', 'R.1.1.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|10*10*e^-4*4^4/4!	|100*(e^-.01 * (.01^4)/4!)	|[('R.0', 100.0, u'10*10', u'100'), ('R.1.0', 2.71828183, u'e', u'e'), ('R.1.1.0.1', 24, u'4!', u'4!')]	|




### (1) Mistake Group Wrong_Sign of size 1




### (83) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:gthorn

	first_attempt
					2015-11-02 06:46:38
	part2_correct_attempt
					['0:01:09', u'e^(-400/81)*((400/81)^3/(3!))']
	part3_incorrect_attempt
					('0:01:57', u'400 * 0.14385')
	part3_correct_attempt
					['0:02:13', u'81 * 0.14385']

1 Student ID:druble

	first_attempt
					2015-11-04 03:47:21
	part2_correct_attempt
					['0:00:00', u'(e^-((1/81) * 400))*(((1/81) * 400)/1)']
	part3_incorrect_attempt
					('0:00:00', u'400 / (1/81)')
					('0:01:38', u'1 / ((1/81) * 400)')
					('0:02:08', u'(1/81) * 400')
					('0:03:14', u'1 / ((1/81) * 400)')
	part3_correct_attempt
					['0:05:11', u'(e^-((1/81) * 400))*(((1/81) * 400)/1) * 81']

2 Student ID:yjshin

	first_attempt
					2015-11-05 20:57:33
	part2_correct_attempt
					['0:12:21', u'e^(-400/64)((400/64)^3/6)']
	part3_incorrect_attempt
					('0:16:36', u'e^(-400/64)((400/64)^64/64!)')
	part3_correct_attempt
					['0:38:18', u'64e^(-400/64)((400/64)^3/6)']

3 Student ID:rwthomps

	first_attempt
					2015-11-06 16:05:03
	part2_correct_attempt
					['0:00:00', u'(e^(-400/81)) * (((400/81)^2)/2!)']
	part3_incorrect_attempt
					('0:00:32', u'400 * (e^(-400/81)) * (((400/81)^2)/2!)')
	part3_correct_attempt
					['0:01:09', u'81 * ((e^(-400/81)) * (((400/81)^2)/2!))']

4 Student ID:jag028

	first_attempt
					2015-11-02 15:56:08
	part2_correct_attempt
					['2:59:50', u'e^(-4)[(4^1)/(1!)]']
	part3_incorrect_attempt
					('3:01:42', u'400*[e^(-4)[(4^1)/(1!)]]')
					('3:02:12', u'400*(0.0732626)')
	part3_correct_attempt
					['3:02:47', u'100*(e^(-4)[(4^1)/(1!)])']

5 Student ID:ccn001

	first_attempt
					2015-11-02 21:59:00
	part2_correct_attempt
					['0:00:00', u'e^(-400/64)(400/64)^2/(2!)']
	part3_incorrect_attempt
					('0:03:02', u'(400/64)(e^(-400/64)(400/64)^2/(2!))')
					('0:03:24', u'(400)(e^(-400/64)(400/64)^2/(2!))')
	part3_correct_attempt
					['0:03:31', u'(64)(e^(-400/64)(400/64)^2/(2!))']

6 Student ID:t2shin

	first_attempt
					2015-11-04 03:50:50
	part2_correct_attempt
					['0:01:16', u'(e^-4)(4^2)/(2)']
	part3_incorrect_attempt
					('0:01:44', u'4*0.146525')
					('0:01:59', u'400*0.146525')
	part3_correct_attempt
					['0:02:05', u'100*0.146525']

7 Student ID:quwong

	first_attempt
					2015-11-02 23:31:39
	part2_correct_attempt
					['0:00:37', u'e^(-400/81) * (400/81)']
	part3_incorrect_attempt
					('0:01:47', u'400/81')
	part3_correct_attempt
					['0:04:33', u'e^(-400/81) * (400)']

8 Student ID:kbielawi

	first_attempt
					2015-11-03 20:28:48
	part2_correct_attempt
					['22:52:42', u'((400/81)^5/(5!))*e^(-400/81)']
	part3_incorrect_attempt
					('22:53:37', u'5*(400/81)')
					('22:55:40', u'((400/81)^5/(5!))*e^(-400/81)*400')
	part3_correct_attempt
					['22:55:53', u'((400/81)^5/(5!))*e^(-400/81)*81']

9 Student ID:nisharma

	first_attempt
					2015-11-06 21:07:56
	part2_correct_attempt
					['0:01:00', u'(e^-6.25)(6.25^0)/(0!)']
	part3_incorrect_attempt
					('0:01:30', u'0(e^-6.25)(6.25^0)/(0!)')
					('0:01:36', u'0(e^-6.25)(6.25^0)/(0!)*0')
					('0:01:47', u'(e^-6.25)(6.25^0)/(0!)*0')

10 Student ID:aggouw

	first_attempt
					2015-11-03 21:26:25
	part2_correct_attempt
					['0:01:15', u'e^(-400/64)*(400/64) ^ 5/5!']
	part3_incorrect_attempt
					('0:01:47', u'10*10*(e^(-400/64)*(400/64)^5/5!)')
	part3_correct_attempt
					['0:02:00', u'8*8*(e^(-400/64)*(400/64)^5/5!)']

11 Student ID:vasharma

	first_attempt
					2015-11-04 18:24:19
	part2_correct_attempt
					['0:02:03', u'(e^-6.25)']
	part3_incorrect_attempt
					('0:02:18', u'(e^-6.25)*400')
					('0:02:32', u'6.25')
					('0:02:46', u'400-6.25')
					('0:04:15', u'(e^-6.25)')
	part3_correct_attempt
					['0:04:23', u'(e^-6.25)*64']

12 Student ID:achava

	first_attempt
					2015-11-03 07:54:25
	part2_correct_attempt
					['14:53:54', u'e^(-400*(1/81)) * (((400*(1/81))^3)/6)']
	part3_incorrect_attempt
					('14:55:25', u'e^(-400*(1/81)) * (((400*(1/81))^3)/6) + e^(-400*(1/81)) * (((400*(1/81))^2)/4) + e^(-400*(1/81)) * (((400*(1/81))^1)/1)')
					('14:55:55', u'(e^(-400*(1/81)) * (((400*(1/81))^3)/6)) + (e^(-400*(1/81)) * (((400*(1/81))^2)/4)) + (e^(-400*(1/81)) * (((400*(1/81))^1)/1))')
					('14:58:14', u'e^(-400*(1/81)) * (((400*(1/81))^3)/6) * (400/81)')
					('14:58:38', u'(e^(-400*(1/81)) * (((400*(1/81))^3)/6)) * (400/81)')
					('14:59:17', u'(e^(-400*(1/81)) * (((400*(1/81))^3)/6)) * (3)')
					('15:01:15', u'400*(1/81)')
					('15:01:24', u'(400*(1/81))*3')
	part3_correct_attempt
					['15:02:35', u'81*e^(-400*(1/81)) * (((400*(1/81))^3)/6)']

13 Student ID:abjara

	first_attempt
					2015-11-04 00:23:20
	part2_correct_attempt
					['0:02:08', u'e^-4']
	part3_incorrect_attempt
					('0:02:08', u'e^-4')
	part3_correct_attempt
					['0:03:34', u'100*e^-4']

14 Student ID:any027

	first_attempt
					2015-11-01 19:00:55
	part2_correct_attempt
					['0:04:40', u'e^-((1/81) * 400)']
	part3_incorrect_attempt
					('0:05:57', u'e^-((1/81) * 400) * ( (((1/81) * 400)^81) / 81!)')
					('0:06:08', u'e^-((1/81) * 400) * ( (((1/81) * 400)^0) / 0!)')
	part3_correct_attempt
					['0:06:47', u'e^-((1/81) * 400) * 81']

15 Student ID:anislam

	first_attempt
					2015-11-05 04:51:07
	part2_correct_attempt
					['0:00:00', u'e^(-4) * (4^4 / 4!)']
	part3_incorrect_attempt
					('0:00:00', u'16 * e^(-4) * (4^4 / 4!)')
	part3_correct_attempt
					['0:00:34', u'100 * e^(-4) * (4^4 / 4!)']

16 Student ID:aadhakal

	first_attempt
					2015-11-05 20:49:57
	part2_correct_attempt
					['0:11:03', u'(e^(-4)*4^1/(1!))']
	part3_incorrect_attempt
					('0:12:04', u'4*(e^(-4)*4^1/(1!))')
	part3_correct_attempt
					['0:12:16', u'100*(e^(-4)*4^1/(1!))']

17 Student ID:krau

	first_attempt
					2015-11-04 19:36:17
	part2_correct_attempt
					['0:00:44', u'(e^-4)*(4^1)/(1!)']
	part3_incorrect_attempt
					('0:00:59', u'(e^-4)*(4^1)/(1!)*400')
	part3_correct_attempt
					['0:01:05', u'(e^-4)*(4^1)/(1!)*100']

18 Student ID:mpanelo

	first_attempt
					2015-11-03 23:03:19
	part2_correct_attempt
					['0:03:46', u'e^-(400/81)*[(400/81)^4/4!]']
	part3_incorrect_attempt
					('0:03:46', u'400/81')
	part3_correct_attempt
					['0:21:44', u'81*e^-(400/81)*[(400/81)^4/4!]']

19 Student ID:qfu

	first_attempt
					2015-11-03 18:45:06
	part2_correct_attempt
					['0:00:00', u'e^(-400/81)*(400/81)']
	part3_incorrect_attempt
					('0:00:00', u'400/81')
					('0:03:33', u'e^(-400/81)*(400/81)')
					('0:04:25', u'1/81')
					('0:04:45', u'400/81')
					('0:09:30', u'400/9')
	part3_correct_attempt
					['0:10:18', u'e^(-400/81)*(400/81)*81']

20 Student ID:kthui

	first_attempt
					2015-11-05 03:03:04
	part2_correct_attempt
					['0:00:52', u'e^(-400/81)*((400/81)^3/3!)']
	part3_incorrect_attempt
					('0:01:15', u'400/81')
	part3_correct_attempt
					['0:03:23', u'e^(-400/81)*((400/81)^3/3!)*81']

21 Student ID:vsosnovs

	first_attempt
					2015-11-05 20:06:57
	part2_correct_attempt
					['0:01:09', u'(e^-(1/81*400)((1/81*400)^4))/4!']
	part3_incorrect_attempt
					('0:01:38', u'4*0.177592')
					('0:01:56', u'400*0.177592')
					('0:02:03', u'80*0.177592')
					('0:02:29', u'1-0.177592')
					('0:07:41', u'1-((e^-(1/81*400)((1/81*400)^4))/4!+(e^-(1/81*400)((1/81*400)^3))/3!)+(e^-(1/81*400)((1/81*400)^2))/2!+(e^-(1/81*400)((1/81*400)^1))/1!+(e^-(1/81*400)((1/81*400)^0))/0!')
					('0:09:40', u'4.93827*0.177592')
					('0:09:48', u'4.93827*0.177592*0.177592')
					('0:09:59', u'4.93827*0.177592*4.93827')
	part3_correct_attempt
					['0:10:45', u'81*0.177592']

22 Student ID:k5law

	first_attempt
					2015-11-04 06:57:17
	part2_correct_attempt
					['0:02:52', u'e^(-[400*(1/81)])*[[400*(1/81)]^2/2]']
	part3_incorrect_attempt
					('0:03:54', u'400*[e^(-[400*(1/81)])*[[400*(1/81)]^2/2]]')
	part3_correct_attempt
					['0:04:13', u'81*[e^(-[400*(1/81)])*[[400*(1/81)]^2/2]]']

23 Student ID:dlt009

	first_attempt
					2015-11-04 06:29:12
	part2_correct_attempt
					['0:03:16', u'e^((-1/81)(400))([(1/81)(400)]^5)/(5!)']
	part3_incorrect_attempt
					('0:03:16', u'[(1/81)(400)]^5')
					('0:03:31', u'[(1/81)(400)]^2')
					('0:08:05', u'1/[e^((-1/81)(400))([(1/81)(400)]^5)/(5!)]')
					('0:08:43', u'1/[(1/81)(400)]')
					('0:13:14', u'1/0.1754')
					('0:17:08', u'1/[.1754]')
	part3_correct_attempt
					['18:01:10', u'81[e^((-1/81)(400))([(1/81)(400)]^5)/(5!)]']

24 Student ID:jfalcone

	first_attempt
					2015-11-04 04:08:44
	part2_correct_attempt
					['0:01:43', u'[e^(-6.25)6.25^4]/(4!)']
	part3_incorrect_attempt
					('0:03:33', u'100 * 0.122735')
	part3_correct_attempt
					['0:03:55', u'64 * 0.122735']

25 Student ID:j5phung

	first_attempt
					2015-11-02 16:17:24
	part2_correct_attempt
					['0:02:46', u'e^(-4)*((4^3)/3!)']
	part3_incorrect_attempt
					('0:06:32', u'4/100')
	part3_correct_attempt
					['0:12:56', u'e^(-4)*((4^3)/3!) * 100']

26 Student ID:p4kumar

	first_attempt
					2015-11-05 18:45:56
	part2_correct_attempt
					['0:00:35', u'e^(-4)*(4^4)/(4!)']
	part3_incorrect_attempt
					('0:00:54', u'0.195367 * 1/100')
	part3_correct_attempt
					['0:01:28', u'100 * 0.195367']

27 Student ID:amquinte

	first_attempt
					2015-11-05 05:34:51
	part2_correct_attempt
					['0:01:53', u'0.1438']
	part3_incorrect_attempt
					('0:01:53', u'400/81')
					('0:02:45', u'400/27')
	part3_correct_attempt
					['0:03:50', u'11.65']

28 Student ID:j6quach

	first_attempt
					2015-11-05 10:32:05
	part2_correct_attempt
					['0:00:00', u'e^(-400/81)*(400/81)^2/2!']
	part3_incorrect_attempt
					('0:00:00', u'(81*80/2)*(e^(-400/81)*(400/81)^2/2!)')
					('0:00:14', u'(81*82/2)*(e^(-400/81)*(400/81)^2/2!)')
	part3_correct_attempt
					['0:00:47', u'81(e^(-400/81)*(400/81)^2/2!)']

29 Student ID:ttimmons

	first_attempt
					2015-11-02 03:35:49
	part2_correct_attempt
					['0:01:57', u'[e^(-4)]*([4^2]/(2!))']
	part3_incorrect_attempt
					('0:02:39', u'2*([e^(-4)]*([4^2]/(2!)))')
					('0:02:54', u'400/100')
					('0:17:17', u'2*400/100')
					('0:18:31', u'2*[e^(-4)]*([4^2]/(2!))')
					('0:18:36', u'4*[e^(-4)]*([4^2]/(2!))')
	part3_correct_attempt
					['0:18:49', u'100*[e^(-4)]*([4^2]/(2!))']

30 Student ID:dcastlem

	first_attempt
					2015-11-02 05:31:46
	part2_correct_attempt
					['0:02:13', u'e^(-6.25)*(6.25^0)/0!']
	part3_incorrect_attempt
					('0:02:59', u'e^(-6.25)*(6.25^0)/0!')
					('0:05:04', u'400*(0.00193045)')
	part3_correct_attempt
					['0:05:12', u'64*(0.00193045)']

31 Student ID:acvuong

	first_attempt
					2015-11-04 19:37:57
	part2_correct_attempt
					['0:00:00', u'e^(-400/81) * (400/81)']
	part3_incorrect_attempt
					('0:00:18', u'400*e^(-400/81) * (400/81)')
	part3_correct_attempt
					['0:00:57', u'81*e^(-400/81) * (400/81)']

32 Student ID:kquong

	first_attempt
					2015-11-01 22:18:43
	part2_correct_attempt
					['0:02:08', u'e^(-400/81) * (400/81)^2/2']
	part3_incorrect_attempt
					('0:10:28', u'400/81 * 2')
					('0:10:44', u'400/81/2')
	part3_correct_attempt
					['0:13:32', u'81 * (e^(-400/81) * (400/81)^2/2)']

33 Student ID:dkostins

	first_attempt
					2015-11-03 05:33:42
	part2_correct_attempt
					['0:12:53', u'((e^-(400/64))(400/64)^5)/5!']
	part3_incorrect_attempt
					('0:13:33', u'((e^-(400/64))(400/64)) * 64')
	part3_correct_attempt
					['0:14:22', u'((e^-(400/64))(400/64)^5)/5!*64']

34 Student ID:mnrahman

	first_attempt
					2015-11-06 21:26:36
	part2_correct_attempt
					['2:20:20', u'e^(-4.93827)* 4.93827 ^5/(5!)']
	part3_incorrect_attempt
					('2:23:40', u'100*(e^(-4.93827)* 4.93827^1/(1!))')
					('2:23:52', u'100*(e^(-4.93827)* 4.93827^5/(5!))')
					('2:24:26', u'100*e^(-4.93827)* 4.93827 ^5/(5!)')
					('2:24:39', u'100*(e^(-4.93827)* 4.93827 ^5/(5!))')
					('2:52:47', u'100* 0.1754')
					('2:53:36', u'400* 0.1754')
	part3_correct_attempt
					['2:53:47', u'81* 0.1754']

35 Student ID:r9jiang

	first_attempt
					2015-11-02 00:29:02
	part2_correct_attempt
					['0:00:00', u'0.1954']
	part3_incorrect_attempt
					('0:00:00', u'4/100')
	part3_correct_attempt
					['0:02:12', u'19.54']

36 Student ID:rlhagen

	first_attempt
					2015-10-31 16:16:12
	part2_correct_attempt
					['0:00:13', u'(e^(-400/64))*((400/64)^3/3!)']
	part3_incorrect_attempt
					('0:00:51', u'(e^(-400/64))*((400/64)^3/3!)*1/64')
	part3_correct_attempt
					['0:01:05', u'(e^(-400/64))*((400/64)^3/3!)*64']

37 Student ID:nnh002

	first_attempt
					2015-11-05 01:53:57
	part2_correct_attempt
					['0:09:59', u'e^(-400/81)*((400/81)^2/2!)']
	part3_incorrect_attempt
					('0:09:59', u'e^(-400/81)*((400/81)^2/2!)+1/81')
					('0:19:20', u'e^(-400/81)*((400/81)^2/2!)*1/81')
					('0:36:34', u'400/81+400*e^(-400/81)*((400/81)^2/2!)')
					('1 day, 20:13:56', u'400*e^(-400/81)*((400/81)^2/2!)')
	part3_correct_attempt
					['1 day, 20:14:06', u'81*e^(-400/81)*((400/81)^2/2!)']

38 Student ID:ralhadda

	first_attempt
					2015-10-31 18:39:17
	part2_correct_attempt
					['0:19:22', u'e^-4 (4^0/0!)']
	part3_incorrect_attempt
					('0:21:56', u'0.018')
					('0:22:08', u'0.018315')
					('2:15:22', u'e^-4(4^0/0!)')
	part3_correct_attempt
					['4:26:51', u'100*e^-4']

39 Student ID:btn023

	first_attempt
					2015-11-05 00:55:30
	part2_correct_attempt
					['0:01:02', u'e^(-((1/81)*400))*((1/81)*400)^0/(0)!']
	part3_incorrect_attempt
					('0:01:28', u'(1/81)*400')
					('0:19:40', u'e^(-((1/81)*400))*((1/81)*400)^0/(0)!')
					('0:22:51', u'1/(e^(-((1/81)*400))*((1/81)*400)^0/(0)!)')
					('0:24:00', u'(1/81)*400')
	part3_correct_attempt
					['1 day, 9:21:28', u'81*(e^(-((1/81)*400))*((1/81)*400)^0/(0)!)']

40 Student ID:mtrafeca

	first_attempt
					2015-11-01 22:37:32
	part2_correct_attempt
					['0:02:48', u'e^(-6.25)*(6.25^(4)/(4!))']
	part3_incorrect_attempt
					('0:03:28', u'400*e^(-6.25)*(6.25^(4)/(4!))')
					('0:05:12', u'e^(-6.25)*(6.25^(4)/(4!))*400/64')
					('0:06:12', u'0.122735*400')
					('0:06:36', u'0.122735*(400/64)')
					('0:15:50', u'C(64,4)*0.122735')
	part3_correct_attempt
					['0:19:14', u'0.122735*64']

41 Student ID:jap009

	first_attempt
					2015-11-05 18:12:02
	part2_correct_attempt
					['0:00:46', u'(e^(-4))*(4/1)']
	part3_incorrect_attempt
					('0:01:59', u'((e^(-4))*(4/1))/100')
	part3_correct_attempt
					['0:02:08', u'((e^(-4))*(4/1))*100']

42 Student ID:q3wen

	first_attempt
					2015-11-03 21:20:02
	part2_correct_attempt
					['0:02:28', u'0.001930']
	part3_incorrect_attempt
					('0:02:28', u'1/0.00193')
					('0:03:19', u'10.24')
					('0:05:50', u'0.16')
					('0:08:41', u'518.0128')
					('0:18:10', u'8.095')
					('0:24:43', u'33152.8192')
	part3_correct_attempt
					['9:00:27', u'0.00193*64']

43 Student ID:rraiyyan

	first_attempt
					2015-11-06 20:20:29
	part2_correct_attempt
					['0:03:23', u'e^-4 * (4^3)/3!']
	part3_incorrect_attempt
					('0:03:30', u'e^-4 * (4^3)/3!')
	part3_correct_attempt
					['0:05:22', u'100 * e^-4 * (4^3)/3!']

44 Student ID:jhw015

	first_attempt
					2015-11-04 01:33:28
	part2_correct_attempt
					['0:08:16', u'e ^-(400/81) * ((400/81)^5 / 5!)']
	part3_incorrect_attempt
					('0:10:20', u'e ^-(400/81) * ((400/81)^5 / 5)')
					('0:10:29', u'e ^-(400/81) * ((400/81)^1 / 5)')
	part3_correct_attempt
					['0:12:07', u'81 * (e ^-(400/81) * ((400/81)^5 / 5!))']

45 Student ID:jmiclat

	first_attempt
					2015-11-06 08:08:00
	part2_correct_attempt
					['0:01:38', u'e^-6.25*(6.25^3)/6']
	part3_incorrect_attempt
					('0:01:45', u'6.25')
					('0:02:46', u'[e^-6.25*(6.25^3)/6]*1/64')
					('0:04:25', u'[e^-6.25*(6.25^3)/6]*400')
					('0:05:48', u'6.25*0.0785504')
					('0:06:51', u'400/3')
	part3_correct_attempt
					['0:08:27', u'0.0785504*64']

46 Student ID:hkhodada

	first_attempt
					2015-11-02 22:21:26
	part2_correct_attempt
					['0:05:25', u'(400/81)^3/[e^(400/81)*6]']
	part3_incorrect_attempt
					('0:05:49', u'(400/81)^3/2*[e^(400/81)*6]')
					('0:14:08', u'(400/81)^3/[e^(400/81)*6]')
					('0:18:12', u'3*(400/81)^3/[e^(400/81)*6]')
	part3_correct_attempt
					['0:19:50', u'81*(400/81)^3/[e^(400/81)*6]']

47 Student ID:thwan

	first_attempt
					2015-11-06 18:21:59
	part2_correct_attempt
					['0:01:24', u'e^(-400/81)*(400/81)']
	part3_incorrect_attempt
					('0:01:24', u'400/81')
					('0:02:23', u'C(400,1)*e^(-400/81)*(400/81)*[e^(-400/81)*(400/81)]^(399)')
					('0:05:03', u'400*e^(-400/81)*(400/81)*[e^(-400/81)*(400/81)]^(399)')
					('0:06:19', u'400*e^(-400/81)*(400/81)*[1-(e^(-400/81)*(400/81))]^(399)')
					('0:07:10', u'e^(-400/81)*(400/81)')
	part3_correct_attempt
					['0:09:48', u'81*e^(-400/81)*(400/81)']

48 Student ID:tstevens

	first_attempt
					2015-11-06 23:21:53
	part2_correct_attempt
					['0:00:00', u'(e^-(400/81))*((400/81)^3)/3!']
	part3_incorrect_attempt
					('0:01:16', u'(91)*(e^-(400/81))*((400/81)^3)/3!')
	part3_correct_attempt
					['0:01:31', u'(81)*(e^-(400/81))*((400/81)^3)/3!']

49 Student ID:krkelkar

	first_attempt
					2015-10-31 19:02:57
	part2_correct_attempt
					['0:00:00', u'(e^-(400/81))*((400/81)^1/1!)']
	part3_incorrect_attempt
					('0:00:00', u'400/81')
					('0:00:36', u'(e^-(400/81))*((400/81)^1/1!)')
	part3_correct_attempt
					['0:03:45', u'81 * {(e^-(400/81))*((400/81)^1/1!)}']

50 Student ID:tcuddy

	first_attempt
					2015-11-01 19:29:21
	part2_correct_attempt
					['0:01:08', u'((400/81)**0)/(e**(400/81))']
	part3_incorrect_attempt
					('0:04:53', u'(81)/(e**(400/81))*(400/81)')
	part3_correct_attempt
					['0:06:15', u'81(((400/81)**0)/(e**(400/81)))']

51 Student ID:dlgoldbe

	first_attempt
					2015-11-05 02:05:33
	part2_correct_attempt
					['0:01:34', u'e^(-4)*((4^3)/(3!))']
	part3_incorrect_attempt
					('0:05:07', u'3*(e^(-4)*((4^3)/(3!)))')
	part3_correct_attempt
					['0:05:36', u'100*(e^(-4)*((4^3)/(3!)))']

52 Student ID:l8ngo

	first_attempt
					2015-11-03 18:49:15
	part2_correct_attempt
					['0:00:51', u'[e^-4]*[16/2]']
	part3_incorrect_attempt
					('0:05:03', u'2*[e^[-1]*4]')
					('0:13:25', u'1*[e^-4]*[16/2]+2*[e^-4]*[16/2]')
					('0:14:01', u'2*[e^-4]*[16/2]')
					('0:17:07', u'550*[e^-4]*[16/2]')
					('0:22:17', u'[1+2+3+4]*[e^-4]*[16/2]')
					('0:23:06', u'5050*[e^-4]*[16/2]')
					('4:47:23', u'4*[e^-4]*[16/2]')
					('4:47:32', u'4/[e^-4]*[16/2]')
					('4:47:42', u'[e^-4]*[16/2]/4')
					('4:55:27', u'5050*[e^-4]*[16/2]')
	part3_correct_attempt
					['4:56:02', u'100*[e^-4]*[16/2]']

53 Student ID:ajabasa

	first_attempt
					2015-11-05 07:42:33
	part2_correct_attempt
					['0:08:14', u'.1953']
	part3_incorrect_attempt
					('0:12:08', u'.1953*4')
					('0:13:26', u'.1953*4*100')
					('0:13:35', u'.1953*4*400')
					('0:14:32', u'.1953*4*100')
					('0:14:37', u'.1953*400')
					('15:22:14', u'.1953*4')
	part3_correct_attempt
					['15:24:16', u'.1953*10*10']

54 Student ID:lahawkin

	first_attempt
					2015-11-04 04:17:46
	part2_correct_attempt
					['0:01:31', u'6.25/(e^6.25)']
	part3_incorrect_attempt
					('0:02:02', u'400/64')
					('0:02:36', u'1/(400/64)')
	part3_correct_attempt
					['0:03:50', u'6.25/(e^6.25)*64']

55 Student ID:eaherman

	first_attempt
					2015-11-06 19:20:19
	part2_correct_attempt
					['0:05:24', u'e^[-[400/81]]([400/81]^2)/2']
	part3_incorrect_attempt
					('0:44:01', u'81/e^[-[400/81]]([400/81]^2)/2')
					('0:45:37', u'1/[e^[-[400/81]]([400/81]^2)/2]')
					('0:46:48', u'2/[e^[-[400/81]]([400/81]^2)]')
					('0:49:15', u'1/[e^[-[400/81]]([400/81]^2)/2]')
					('0:51:31', u'400/81')

56 Student ID:chc286

	first_attempt
					2015-11-01 00:01:32
	part2_correct_attempt
					['0:01:50', u'e^(-400*(1/81))*((400*(1/81))^4/(4!))']
	part3_incorrect_attempt
					('0:02:49', u'400*(1/81)')
	part3_correct_attempt
					['0:04:22', u'81*(e^(-400*(1/81))*((400*(1/81))^4/(4!)))']

57 Student ID:hah008

	first_attempt
					2015-11-05 22:29:48
	part2_correct_attempt
					['0:01:19', u'e^(-400/81)*(400/81)^3/6']
	part3_incorrect_attempt
					('0:01:54', u'400/81*(400/81)*(e^(-400/81)*(400/81)^3/6)')
					('0:03:04', u'81*81* 0.14385')
					('0:05:52', u'(81*81)*e^(-400/81)*(400/81)^3/6')
	part3_correct_attempt
					['0:06:05', u'(9*9)*e^(-400/81)*(400/81)^3/6']

58 Student ID:bakang

	first_attempt
					2015-11-05 06:38:48
	part2_correct_attempt
					['0:00:59', u'(e^(-4))*((4^4)/(4!))']
	part3_incorrect_attempt
					('0:02:32', u'400*((e^(-4))*((4^4)/(4!)))')
	part3_correct_attempt
					['0:02:38', u'100*((e^(-4))*((4^4)/(4!)))']

59 Student ID:ctroncos

	first_attempt
					2015-11-04 01:30:39
	part2_correct_attempt
					['0:06:11', u'e^(-400/100)*(400/100)^2/(2!)']
	part3_incorrect_attempt
					('0:07:32', u'(400*400)*(e^(-400/100)*((400/100)^2)/(2!))')
					('0:09:57', u'(10000)*(e^(-400/100)*((400/100)^2)/(2!))')
					('0:10:09', u'(100*100)*(e^(-400/100)*((400/100)^2)/(2!))')
					('0:11:15', u'(100*100)*(e^(-400/100)*(400/100)^2/(2!))')
	part3_correct_attempt
					['0:12:32', u'(10*10)*(e^(-400/100)*(400/100)^2/(2!))']

60 Student ID:acs008

	first_attempt
					2015-11-04 03:50:34
	part2_correct_attempt
					['0:02:07', u'e^(-6.25)*(6.25^2)/2']
	part3_incorrect_attempt
					('0:02:40', u'400*e^(-6.25)*(6.25^2)/2')
					('0:02:53', u'0.0377042*400')
	part3_correct_attempt
					['0:02:58', u'0.0377042*64']

61 Student ID:dpereira

	first_attempt
					2015-10-30 21:00:37
	part2_correct_attempt
					['0:00:49', u'(e^(-(400/81))) * ((400/81)^4)/(4!)']
	part3_incorrect_attempt
					('0:01:23', u'1/((e^(-(400/81))) * ((400/81)^4)/(4!))')
	part3_correct_attempt
					['0:01:49', u'81 * ((e^(-(400/81))) * ((400/81)^4)/(4!))']

62 Student ID:ppanourg

	first_attempt
					2015-11-05 08:50:33
	part2_correct_attempt
					['0:01:29', u'(e^(-6.25))*((6.25^5)/5!)']
	part3_incorrect_attempt
					('0:05:24', u'(e^(-6.25))*((6.25^5)/5!)/64')
					('0:05:47', u'64/(e^(-6.25))*((6.25^5)/5!)')
					('0:06:25', u'((e^(-6.25))*((6.25^5)/5!))/64')
	part3_correct_attempt
					['0:06:41', u'((e^(-6.25))*((6.25^5)/5!))*64']

63 Student ID:haliew

	first_attempt
					2015-11-05 06:53:43
	part2_correct_attempt
					['0:00:00', u'e^(-4)(16/2)']
	part3_incorrect_attempt
					('1 day, 17:23:45', u'e^(-1/10)(1/10)')
	part3_correct_attempt
					['1 day, 17:24:01', u'e^(-4)(16/2)(100)']

64 Student ID:a2ahmed

	first_attempt
					2015-11-04 05:19:22
	part2_correct_attempt
					['-1 day, 23:44:52', u'0.1753999673']
	part3_incorrect_attempt
					('-1 day, 23:45:54', u'291257/5000')
					('-1 day, 23:46:07', u'2912517/5000')
					('-1 day, 23:53:00', u'582.5034')
					('-1 day, 23:54:25', u'7.893')
					('-1 day, 23:54:43', u'2.631')

65 Student ID:mrchin

	first_attempt
					2015-11-06 19:25:13
	part2_correct_attempt
					['0:02:17', u'e^(-6.25)*6.25^5/(5!)']
	part3_incorrect_attempt
					('0:02:36', u'400/64*e^(-6.25)*6.25^5/(5!)')
					('0:02:50', u'(400/64)*e^(-6.25)*6.25^5/(5!)')
	part3_correct_attempt
					['0:03:03', u'64*e^(-6.25)*6.25^5/(5!)']

66 Student ID:flhernan

	first_attempt
					2015-11-01 18:53:06
	part2_correct_attempt
					['0:26:24', u'(e^-6.25 *6.25^5/5!)']
	part3_incorrect_attempt
					('0:26:24', u'(e^-6.25 *6.25^5/5!)*6.25')
	part3_correct_attempt
					['0:26:39', u'(e^-6.25 *6.25^5/5!)*64']

67 Student ID:xil109

	first_attempt
					2015-11-05 02:40:24
	part2_correct_attempt
					['0:01:20', u'[e^(-400/64)*(400/64)^3]/3!']
	part3_incorrect_attempt
					('0:02:08', u'[e^(-400/64)*(400/64)^3]/3!*400')
	part3_correct_attempt
					['0:02:33', u'[e^(-400/64)*(400/64)^3]/3!*64']

68 Student ID:azkong

	first_attempt
					2015-11-05 20:14:56
	part2_correct_attempt
					['12:57:52', u'e^(-400/81)(400/81)']
	part3_incorrect_attempt
					('12:58:34', u'e^(-400/81)(400/81)*400')
	part3_correct_attempt
					['12:58:51', u'e^(-400/81)(400/81)*81']

69 Student ID:mitopete

	first_attempt
					2015-11-04 03:19:34
	part2_correct_attempt
					['0:10:04', u'(25/4)/(e^(25/4))']
	part3_incorrect_attempt
					('0:12:37', u'1/(25/4)^2')
					('0:13:03', u'4/25')
					('0:13:39', u'25/4')
					('0:14:25', u'400/(25/4)')
					('2 days, 17:48:17', u'(25/4)/(e^(25/4))(1/64)')
					('2 days, 20:58:31', u'400/(25/4)')
	part3_correct_attempt
					['2 days, 17:48:32', u'(25/4)/(e^(25/4))(64)']

70 Student ID:b3hwang

	first_attempt
					2015-11-05 06:32:23
	part2_correct_attempt
					['0:04:07', u'e^(-4) * 4']
	part3_incorrect_attempt
					('0:04:51', u'400*(e^(-4) * 4)')
	part3_correct_attempt
					['0:05:49', u'(e^(-4) * 4 ) *100']

71 Student ID:yig015

	first_attempt
					2015-11-05 09:25:07
	part2_correct_attempt
					['0:00:00', u'e^(-400/81)*(400/81)^4/4!']
	part3_incorrect_attempt
					('0:00:19', u'400/81')
	part3_correct_attempt
					['0:01:40', u'81*0.177592']

72 Student ID:rohan

	first_attempt
					2015-11-06 22:11:26
	part2_correct_attempt
					['0:09:54', u'e^(-400/81)']
	part3_incorrect_attempt
					('0:17:07', u'80200/81')
	part3_correct_attempt
					['0:20:11', u'81(e^(-400/81))']

73 Student ID:m4salaza

	first_attempt
					2015-11-04 04:13:43
	part2_correct_attempt
					['0:02:57', u'e^(-4.938)*(4.938^3/(3*2))']
	part3_incorrect_attempt
					('0:04:44', u'e^(-4.938)')
					('0:05:01', u'e^(-400/81)')
					('0:06:04', u'e^(-4.938)*(4.938^3/(3*2))/81')
	part3_correct_attempt
					['0:06:23', u'e^(-4.938)*(4.938^3/(3*2))*81']

74 Student ID:hpc001

	first_attempt
					2015-11-01 00:39:35
	part2_correct_attempt
					['0:01:23', u'(e^-(400/64))*((400/64)^5)/5!']
	part3_incorrect_attempt
					('0:02:11', u'(64*64)*(e^-(400/64))*((400/64)^5)/5!')
	part3_correct_attempt
					['0:02:55', u'(8*8)*(e^-(400/64))*((400/64)^5)/5!']

75 Student ID:tak068

	first_attempt
					2015-11-05 20:47:17
	part2_correct_attempt
					['0:00:29', u'e^(-400/81)*(400/81)^3/(3!)']
	part3_incorrect_attempt
					('0:00:48', u'9*e^(-400/81)*(400/81)^3/(3!)')
	part3_correct_attempt
					['0:01:08', u'81*e^(-400/81)*(400/81)^3/(3!)']

76 Student ID:dtea

	first_attempt
					2015-11-06 23:51:28
	part2_correct_attempt
					['0:01:07', u'e^(-400/64)*((400/64)^3/3!)']
	part3_incorrect_attempt
					('0:01:39', u'400*0.0785504')
	part3_correct_attempt
					['0:02:31', u'64*0.0785504']

77 Student ID:atorr

	first_attempt
					2015-11-05 19:21:20
	part2_correct_attempt
					['0:00:31', u'e^(-6.25) * [(6.25^5)/5!]']
	part3_incorrect_attempt
					('0:00:45', u'5*6.25')
					('0:01:19', u'5/64')
					('0:02:01', u'(1+2+3+4+5) * (1/64)')
					('0:03:04', u'5 * (0.153419)')
					('0:03:17', u'15 * (0.153419)')
					('0:05:17', u'(5/64) * (0.153419)')
	part3_correct_attempt
					['1:23:30', u'e^(-6.25) * [(6.25^5)/5!] * 64']

78 Student ID:zig006

	first_attempt
					2015-11-01 19:47:20
	part2_correct_attempt
					['0:02:15', u'0.177592']
	part3_incorrect_attempt
					('0:02:15', u'1.234567')
					('0:02:32', u'0.81')
	part3_correct_attempt
					['0:03:06', u'14.384952']

79 Student ID:tpmach

	first_attempt
					2015-11-04 23:08:04
	part2_correct_attempt
					['0:03:29', u'e^(-400/81)*(((400/81)^2)/2!)']
	part3_incorrect_attempt
					('0:05:36', u'400/81')
					('0:08:25', u'1-(e^(-400/81)*(((400/81)^2)/2!))')
					('4:48:37', u'(e^(-400/81)*(((400/81)^2)/2!))')
	part3_correct_attempt
					['4:52:36', u'81*(e^(-400/81)*(((400/81)^2)/2!))']

80 Student ID:phodgson

	first_attempt
					2015-11-06 06:07:31
	part2_correct_attempt
					['0:00:12', u'e^(-400/81)((400/81)^4/4!)']
	part3_incorrect_attempt
					('0:00:12', u'4*e^(-400/81)((400/81)^4/4!)')
	part3_correct_attempt
					['0:00:21', u'81*e^(-400/81)((400/81)^4/4!)']

81 Student ID:aurodrig

	first_attempt
					2015-11-06 03:39:29
	part2_correct_attempt
					['0:00:00', u'e^(-4) * ((4^5)/5!)']
	part3_incorrect_attempt
					('0:03:12', u'.1562934519')
					('0:03:57', u'.156')
	part3_correct_attempt
					['0:05:12', u'100 * (e^(-4) * ((4^5)/5!))']

82 Student ID:muy002

	first_attempt
					2015-11-05 03:52:30
	part2_correct_attempt
					['0:00:00', u'(400/81)^2*e^(-400/81)/2!']
	part3_incorrect_attempt
					('0:06:13', u'(400/81)^2')
					('0:06:31', u'(1/81)^2')
	part3_correct_attempt
					['0:09:56', u'81*((400/81)^2*e^(-400/81)/2!)']












