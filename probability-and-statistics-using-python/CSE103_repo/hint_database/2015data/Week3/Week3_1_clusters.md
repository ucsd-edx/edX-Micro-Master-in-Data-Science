#Problem 1

    $a=random(4,6,1);

    if ($a == 4){
       $lts = AABBCC;
       $ans = 6*5*4*3*2/(2*2*2);
       };
    if ($a == 5){
       $lts = AAABBC;
       $ans = 6*5*4*3*2/(3*2*2);
       };
    if ($a == 6){
       $lts = AABCD;
       $ans = 5*4*3*2/2;
       };

    1. Find the number of distinguishable ways of arranging the letters "MAMA".
    Your answer is : [_________________________]{Compute("(4*3*2)/(2*2)")}

    2. Find the number of distinguishable permutations formed by using each of the letters [$lts] once and only once.
    Your answer is : [_________________________]{$ans}


## Part 1

### (145) Mistake Group Digits of size 145




### (26) Mistake Group ['R.0'] of size 26
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*3*2/(2*2)	|4!/2!	|[('R.0', 24.0, u'4*3*2', u'4!')]	|
|1	|4*3*2/(2*2)	|4!(2!*2!)	|[('R.0', 24.0, u'4*3*2', u'4!')]	|
|2	|4*3*2/(2*2)	|4!/(3!2)	|[('R.0', 24.0, u'4*3*2', u'4!')]	|
|3	|4*3*2/(2*2)	|4!/(3!)	|[('R.0', 24.0, u'4*3*2', u'4!')]	|
|4	|4*3*2/(2*2)	|4!/2	|[('R.0', 24.0, u'4*3*2', u'4!')]	|
|5	|4*3*2/(2*2)	|4!/(4-2)!	|[('R.0', 24.0, u'4*3*2', u'4!')]	|
|6	|4*3*2/(2*2)	|4!/(2!)	|[('R.0', 24.0, u'4*3*2', u'4!')]	|
|7	|4*3*2/(2*2)	|4! * 2!	|[('R.0', 24.0, u'4*3*2', u'4!')]	|
|8	|4*3*2/(2*2)	|(4!)/(2!)	|[('R.0', 24.0, u'4*3*2', u'4!')]	|
|9	|4*3*2/(2*2)	|4! - 4	|[('R.0', 24.0, u'4*3*2', u'4!')]	|
|10	|4*3*2/(2*2)	|(4*3*2*1)/2	|[('R.0', 24.0, u'4*3*2', u'4*3*2*1')]	|
|11	|4*3*2/(2*2)	|(4!/2!)	|[('R.0', 24.0, u'4*3*2', u'4!')]	|




### (5) Mistake Group ['R.0.0.0'] of size 5
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*3*2/(2*2)	|4!/2!2!	|[('R.0.0.0', 4.0, u'4', u'4')]	|
|1	|4*3*2/(2*2)	|(4!/2!)(2!/2!)	|[('R.0.0.0', 4.0, u'4', u'4')]	|




### (3) Mistake Group ['R.0.0'] of size 3
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*3*2/(2*2)	|4*3*2*1	|[('R.0.0', 12.0, u'4*3', u'4*3')]	|




### (3) Mistake Group ['R.1.1'] of size 3
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*3*2/(2*2)	|6!/(2!*2!*2!)	|[('R.1.1', 2.0, u'2', u'2!')]	|
|1	|4*3*2/(2*2)	|6! / (2! 2! 2!)	|[('R.1.1', 2.0, u'2', u'2!')]	|
|2	|4*3*2/(2*2)	|(6!)/(3!*2!)	|[('R.1.1', 2.0, u'2', u'2!')]	|




### (2) Mistake Group ['R.0.0.1'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*3*2/(2*2)	|5*3*2*1	|[('R.0.0.1', 3.0, u'3', u'3')]	|
|1	|4*3*2/(2*2)	|6*5*4*3*2*1	|[('R.0.0.1', 3.0, u'3', u'3')]	|




### (2) Mistake Group Fraction of size 2




### (41) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:b3hwang

	first_attempt
					2015-10-15 20:48:23
	part1_incorrect_attempt
					('0:00:00', u'4!')
					('0:00:17', u'2!')
					('0:00:24', u'4!')
	part1_correct_attempt
					['0:00:44', u'4! / (2! * 2!)']

1 Student ID:jag028

	first_attempt
					2015-10-10 02:47:40
	part1_incorrect_attempt
					('0:00:00', u'2!2!')
					('0:00:43', u'4!3!2!1!')
	part1_correct_attempt
					['2 days, 11:12:28', u'[(4!)/(2!*2!)]']

2 Student ID:t2shin

	first_attempt
					2015-10-13 21:13:09
	part1_incorrect_attempt
					('0:00:00', u'4!')
	part1_correct_attempt
					['0:05:42', u'6']

3 Student ID:hkhodada

	first_attempt
					2015-10-09 02:49:24
	part1_incorrect_attempt
					('0:00:00', u'4!')
	part1_correct_attempt
					['0:25:09', u'6']

4 Student ID:aportuga

	first_attempt
					2015-10-13 21:31:08
	part1_incorrect_attempt
					('0:00:00', u'4!')
	part1_correct_attempt
					['0:02:35', u'6']

5 Student ID:c1sorian

	first_attempt
					2015-10-14 21:19:38
	part1_incorrect_attempt
					('0:00:00', u'4*3*2')
	part1_correct_attempt
					['0:01:56', u'(4!)/(2!2!)']

6 Student ID:jcl084

	first_attempt
					2015-10-12 04:06:05
	part1_incorrect_attempt
					('0:00:00', u'4*3*2/2*2')
	part1_correct_attempt
					['0:00:08', u'4*3*2/(2*2)']

7 Student ID:any027

	first_attempt
					2015-10-09 08:55:41
	part1_incorrect_attempt
					('0:00:00', u'4!')
	part1_correct_attempt
					['0:01:21', u'4 ! / (2! * 2!)']

8 Student ID:jjm019

	first_attempt
					2015-10-12 22:56:43
	part1_incorrect_attempt
					('0:00:00', u'2^2')
	part1_correct_attempt
					['0:01:14', u'2^3 - 2']

9 Student ID:awollner

	first_attempt
					2015-10-09 05:00:18
	part1_incorrect_attempt
					('0:00:00', u'P(4,2)')
	part1_correct_attempt
					['0:00:33', u'C(4,2)']

10 Student ID:dcrume

	first_attempt
					2015-10-14 18:50:52
	part1_incorrect_attempt
					('0:00:00', u'4^4')
	part1_correct_attempt
					['0:01:18', u'4!/(2!2!)']

11 Student ID:vsosnovs

	first_attempt
					2015-10-10 21:21:27
	part1_incorrect_attempt
					('0:00:00', u'4!')
					('0:00:12', u'2!')
					('0:01:02', u'2!')
					('0:12:17', u'4!')
	part1_correct_attempt
					['0:13:04', u'4!/4']

12 Student ID:w4shin

	first_attempt
					2015-10-12 02:32:48
	part1_incorrect_attempt
					('0:00:00', u'2*2')
					('0:00:35', u'4!')
	part1_correct_attempt
					['0:03:13', u'4!/(2!*2!)']

13 Student ID:haw081

	first_attempt
					2015-10-10 20:22:48
	part1_incorrect_attempt
					('0:00:00', u'4!')
	part1_correct_attempt
					['0:07:27', u'4!/(2!*2!)']

14 Student ID:dcastlem

	first_attempt
					2015-10-13 18:02:28
	part1_incorrect_attempt
					('0:00:00', u'4!')
					('0:15:06', u'12!')
	part1_correct_attempt
					['0:28:25', u'4!/(2!*2!)']

15 Student ID:mnrahman

	first_attempt
					2015-10-15 05:02:47
	part1_incorrect_attempt
					('0:00:00', u'2!')
					('0:15:32', u'(6!)/3!*2!')
	part1_correct_attempt
					['0:15:53', u'4*3*2/(2*2)']

16 Student ID:cfgutier

	first_attempt
					2015-10-14 20:17:54
	part1_incorrect_attempt
					('0:00:00', u'2^4')
					('0:15:14', u'4!')
					('0:15:24', u'2!')
	part1_correct_attempt
					['0:17:04', u'(4!)/(2!*2!)']

17 Student ID:jnatale

	first_attempt
					2015-10-12 22:43:45
	part1_incorrect_attempt
					('0:00:00', u'2!')
	part1_correct_attempt
					['0:01:09', u'6']

18 Student ID:mrchin

	first_attempt
					2015-10-12 02:08:37
	part1_incorrect_attempt
					('0:00:00', u'2^4')
	part1_correct_attempt
					['0:06:18', u'4!/(2!*2!)']

19 Student ID:s6deng

	first_attempt
					2015-10-12 19:58:32
	part1_incorrect_attempt
					('0:00:00', u'4!')
	part1_correct_attempt
					['0:00:42', u'4!/(2!2!)']

20 Student ID:dis003

	first_attempt
					2015-10-15 03:12:27
	part1_incorrect_attempt
					('0:00:00', u'4!')
	part1_correct_attempt
					['0:00:23', u'4!/(2!2!)']

21 Student ID:dgunawan

	first_attempt
					2015-10-14 17:45:44
	part1_incorrect_attempt
					('0:00:00', u'4!')
	part1_correct_attempt
					['1:52:39', u'4! / (2! * 2!)']

22 Student ID:hachrist

	first_attempt
					2015-10-10 20:11:57
	part1_incorrect_attempt
					('0:00:00', u'4!')
	part1_correct_attempt
					['2 days, 4:17:07', u'4!/(2!*2!)']

23 Student ID:mpanelo

	first_attempt
					2015-10-09 17:33:57
	part1_incorrect_attempt
					('0:00:00', u'4!')
	part1_correct_attempt
					['0:03:00', u'4!/2!/2']

24 Student ID:hpc001

	first_attempt
					2015-10-09 05:14:34
	part1_incorrect_attempt
					('0:00:00', u'4*3*2')
					('0:02:26', u'4*2')
	part1_correct_attempt
					['0:03:21', u'4*3*2/4']

25 Student ID:yeh013

	first_attempt
					2015-10-15 05:33:48
	part1_incorrect_attempt
					('0:00:00', u'2!')
					('0:00:06', u'4!')
					('0:11:44', u'4!')
	part1_correct_attempt
					['0:13:24', u'6']

26 Student ID:c1wei

	first_attempt
					2015-10-09 18:09:54
	part1_incorrect_attempt
					('0:00:00', u'4!')
	part1_correct_attempt
					['0:03:10', u'6']

27 Student ID:glcohen

	first_attempt
					2015-10-09 20:18:05
	part1_incorrect_attempt
					('0:00:00', u'2*(4!/2!(2!))')
					('0:00:10', u'2*(4!/(2!(2!)))')
	part1_correct_attempt
					['2 days, 7:29:49', u'4!/(2!2!)']

28 Student ID:sayao

	first_attempt
					2015-10-11 22:22:14
	part1_incorrect_attempt
					('0:00:00', u'4!')
	part1_correct_attempt
					['0:22:45', u'4!/(2!*2!)']

29 Student ID:muy002

	first_attempt
					2015-10-11 19:47:40
	part1_incorrect_attempt
					('0:00:00', u'4!')
	part1_correct_attempt
					['0:00:13', u'4!/(2!2!)']

30 Student ID:dtea

	first_attempt
					2015-10-09 20:15:22
	part1_incorrect_attempt
					('0:00:00', u'4!')
	part1_correct_attempt
					['0:00:48', u'4!/4']

31 Student ID:lahawkin

	first_attempt
					2015-10-13 23:08:53
	part1_incorrect_attempt
					('0:00:00', u'2*2')
					('0:01:32', u'4!')
					('0:15:52', u'4/(2!*2!)')
	part1_correct_attempt
					['0:16:46', u'4!/(2!*2!)']

32 Student ID:cstringh

	first_attempt
					2015-10-11 01:14:15
	part1_incorrect_attempt
					('0:00:00', u'4!')
					('0:00:20', u'2!')
	part1_correct_attempt
					['0:01:44', u'4!/(2!(2!))']

33 Student ID:ksrijong

	first_attempt
					2015-10-14 00:10:08
	part1_incorrect_attempt
					('0:00:00', u'C(4,2)*2')
	part1_correct_attempt
					['0:00:53', u'4!/(2!*2!)']

34 Student ID:starinia

	first_attempt
					2015-10-13 02:15:36
	part1_incorrect_attempt
					('0:00:00', u'4!')
	part1_correct_attempt
					['0:00:33', u'4!/(2!2!)']

35 Student ID:m4salaza

	first_attempt
					2015-10-14 18:56:32
	part1_incorrect_attempt
					('0:00:00', u'4!')
	part1_correct_attempt
					['0:00:36', u'4!/(2!*2!)']

36 Student ID:bpandayk

	first_attempt
					2015-10-15 00:18:00
	part1_incorrect_attempt
					('0:00:00', u'6!')
	part1_correct_attempt
					['21:24:41', u'4*3*2/(2*2)']

37 Student ID:ggaddi

	first_attempt
					2015-10-10 00:56:09
	part1_incorrect_attempt
					('0:00:00', u'2!*2')
	part1_correct_attempt
					['0:08:15', u'4!/(2!*2!)']

38 Student ID:sthapa

	first_attempt
					2015-10-15 03:16:54
	part1_incorrect_attempt
					('0:00:00', u'4!')
	part1_correct_attempt
					['0:06:39', u'4!/(2!*2!)']

39 Student ID:whcombs

	first_attempt
					2015-10-12 21:18:35
	part1_incorrect_attempt
					('0:00:00', u'P(4,2)')
	part1_correct_attempt
					['0:00:12', u'C(4,2)']

40 Student ID:asp025

	first_attempt
					2015-10-09 23:08:47
	part1_incorrect_attempt
					('0:00:00', u'4!')
	part1_correct_attempt
					['1 day, 8:44:06', u'4!/(2!2!)']












## Part 2

### (136) Mistake Group Digits of size 136




### (62) Mistake Group ['R.0'] of size 62
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|5!/2!	|5!-1	|[('R.0', 120, u'5!', u'5!')]	|
|1	|6!/(3!*2!)	| 6!/6	|[('R.0', 720, u'6!', u'6!')]	|
|2	|6!/(3!*2!)	| 6!/4	|[('R.0', 720, u'6!', u'6!')]	|
|3	|6!/(2!*2!*2!)	|6!/2	|[('R.0', 720, u'6!', u'6!')]	|
|4	|6!/(2!*2!*2!)	|6*5*4*3*2/6	|[('R.0', 720, u'6!', u'6*5*4*3*2')]	|
|5	|5!/2!	|5!/4!	|[('R.0', 120, u'5!', u'5!')]	|
|6	|6!/(2!*2!*2!)	|6!/3!	|[('R.0', 720, u'6!', u'6!')]	|
|7	|5!/2!	|5!/4	|[('R.0', 120, u'5!', u'5!')]	|
|8	|5!/2!	|5!-10	|[('R.0', 120, u'5!', u'5!')]	|
|9	|5!/2!	|5!/5	|[('R.0', 120, u'5!', u'5!')]	|
|10	|6!/(3!*2!)	|[6!]/[3!*3!*1!]	|[('R.0', 720, u'6!', u'6!')]	|
|11	|6!/(2!*2!*2!)	|6!/(2! * 3)	|[('R.0', 720, u'6!', u'6!')]	|
|12	|6!/(2!*2!*2!)	|6!/(2!)	|[('R.0', 720, u'6!', u'6!')]	|
|13	|6!/(2!*2!*2!)	|6!/(3!(3!))	|[('R.0', 720, u'6!', u'6!')]	|
|14	|6!/(2!*2!*2!)	|6!/(2!(4!))	|[('R.0', 720, u'6!', u'6!')]	|
|15	|6!/(2!*2!*2!)	|6!/(3!*3!)	|[('R.0', 720, u'6!', u'6!')]	|
|16	|6!/(2!*2!*2!)	|6!-6	|[('R.0', 720, u'6!', u'6!')]	|
|17	|6!/(2!*2!*2!)	|(6!)/(4)	|[('R.0', 720, u'6!', u'6!')]	|
|18	|6!/(2!*2!*2!)	|6!/3	|[('R.0', 720, u'6!', u'6!')]	|
|19	|5!/2!	|5!/(3!*2!)	|[('R.0', 120, u'5!', u'5!')]	|
|20	|6!/(3!*2!)	|6*5*4*3*2/(2*2*2)	|[('R.0', 720, u'6!', u'6*5*4*3*2')]	|
|21	|6!/(3!*2!)	|6!/6	|[('R.0', 720, u'6!', u'6!')]	|
|22	|6!/(3!*2!)	|6!/6!	|[('R.0', 720, u'6!', u'6!')]	|
|23	|6!/(3!*2!)	|6!/18	|[('R.0', 720, u'6!', u'6!')]	|
|24	|6!/(3!*2!)	|6!/(6!(1!))	|[('R.0', 720, u'6!', u'6!')]	|
|25	|5!/2!	|5!/(4!)	|[('R.0', 120, u'5!', u'5!')]	|
|26	|6!/(3!*2!)	|(6!)3	|[('R.0', 720, u'6!', u'6!')]	|
|27	|6!/(3!*2!)	|(6!)3!	|[('R.0', 720, u'6!', u'6!')]	|
|28	|6!/(3!*2!)	|(6!)5	|[('R.0', 720, u'6!', u'6!')]	|
|29	|6!/(3!*2!)	|(6!)6	|[('R.0', 720, u'6!', u'6!')]	|
|30	|6!/(2!*2!*2!)	|(6!)/((5!)(3!))	|[('R.0', 720, u'6!', u'6!')]	|
|31	|6!/(2!*2!*2!)	|(6!)/((3!)(3!))	|[('R.0', 720, u'6!', u'6!')]	|
|32	|6!/(3!*2!)	|6!/2!	|[('R.0', 720, u'6!', u'6!')]	|
|33	|6!/(3!*2!)	|6!/4!	|[('R.0', 720, u'6!', u'6!')]	|
|34	|5!/2!	|5!/3!	|[('R.0', 120, u'5!', u'5!')]	|
|35	|6!/(3!*2!)	|6! + 6!	|[('R.0', 720, u'6!', u'6!')]	|
|36	|6!/(2!*2!*2!)	|6!/(3!*2!)	|[('R.0', 720, u'6!', u'6!')]	|
|37	|6!/(2!*2!*2!)	|6!/12	|[('R.0', 720, u'6!', u'6!')]	|
|38	|6!/(3!*2!)	|6!*3!	|[('R.0', 720, u'6!', u'6!')]	|
|39	|6!/(2!*2!*2!)	|6! /( 3! * 2!)	|[('R.0', 720, u'6!', u'6!')]	|
|40	|6!/(2!*2!*2!)	|6! /( 3!)	|[('R.0', 720, u'6!', u'6!')]	|
|41	|6!/(2!*2!*2!)	|6! /(3!* 3!)	|[('R.0', 720, u'6!', u'6!')]	|
|42	|6!/(3!*2!)	|6!/(8)	|[('R.0', 720, u'6!', u'6!')]	|




### (34) Mistake Group redirect of size 34




### (12) Mistake Group Fraction of size 12




### (7) Mistake Group ['R.1'] of size 7
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|6!/(3!*2!)	|(7!/ (3! 2!))	|[('R.1', 12.0, u'3!*2!', u'3! 2!')]	|
|1	|6!/(2!*2!*2!)	|8!/8	|[('R.1', 8.0, u'2!*2!*2!', u'8')]	|
|2	|6!/(2!*2!*2!)	|8!/(2!*2!*2!)	|[('R.1', 8.0, u'2!*2!*2!', u'2!*2!*2!')]	|
|3	|6!/(2!*2!*2!)	|8!/(2!2!2!)	|[('R.1', 8.0, u'2!*2!*2!', u'2!2!2!')]	|
|4	|6!/(3!*2!)	|60/12	|[('R.1', 12.0, u'3!*2!', u'12')]	|




### (6) Mistake Group ['R.1.0'] of size 6
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|6!/(2!*2!*2!)	|3*C(6,2)*2*C(4,2)	|[('R.1.0', 4.0, u'2!*2!', u'4')]	|
|1	|6!/(2!*2!*2!)	|3*P(6,2)*2*P(4,2)	|[('R.1.0', 4.0, u'2!*2!', u'4')]	|
|2	|6!/(2!*2!*2!)	|3*C(6,2)*C(4,2)	|[('R.1.0', 4.0, u'2!*2!', u'4')]	|
|3	|6!/(2!*2!*2!)	|3*P(6,2)*P(4,2)	|[('R.1.0', 4.0, u'2!*2!', u'4')]	|
|4	|6!/(3!*2!)	|(7!/ (3! 4!))	|[('R.1.0', 6, u'3!', u'3!')]	|
|5	|6!/(3!*2!)	|2*6!	|[('R.1.0', 6, u'3!', u'6')]	|




### (3) Mistake Group ['R.0', 'R.1'] of size 3
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|6!/(2!*2!*2!)	|6!(2!*2!*2!)	|[('R.0', 720, u'6!', u'6!'), ('R.1', 8.0, u'2!*2!*2!', u'2!*2!*2!')]	|




### (2) Mistake Group ['R.0.0'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|6!/(2!*2!*2!)	|(2*P(3,1))(2*P(2,1))(2)	|[('R.0.0', 6.0, u'6', u'2*P(3,1)')]	|
|1	|6!/(2!*2!*2!)	|6*5*4	|[('R.0.0', 6.0, u'6', u'6')]	|




### (1) Mistake Group ['R.0', 'R.1.0.0'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|6!/(3!*2!)	|6!/(3!*3!)	|[('R.0', 720, u'6!', u'6!'), ('R.1.0.0', 3.0, u'3', u'3')]	|




### (1) Mistake Group ['R.0', 'R.1.0'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|5!/2!	|5!/(2!*3!)	|[('R.0', 120, u'5!', u'5!'), ('R.1.0', 2.0, u'2', u'2!')]	|




### (50) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:anislam

	first_attempt
					2015-10-15 06:59:55
	part1_correct_attempt
					['0:00:00', u'C(4,2)']
	part2_incorrect_attempt
					('0:02:21', u'C(5,4)')
	part2_correct_attempt
					['0:06:50', u'5!/2!']

1 Student ID:jfalcone

	first_attempt
					2015-10-14 05:58:00
	part1_correct_attempt
					['0:00:00', u'4!/(2! * 2!)']
	part2_incorrect_attempt
					('0:00:00', u'[6!/(2! * 2! * 2!)] * 6!')
	part2_correct_attempt
					['0:00:21', u'[6!/(2! * 2! * 2!)]']

2 Student ID:aggouw

	first_attempt
					2015-10-12 21:24:19
	part1_correct_attempt
					['0:00:00', u'6']
	part2_incorrect_attempt
					('2 days, 9:21:22', u'5!')
	part2_correct_attempt
					['2 days, 9:27:48', u'6! / 8']

3 Student ID:vasharma

	first_attempt
					2015-10-10 01:17:10
	part1_correct_attempt
					['0:00:00', u'6']
	part2_incorrect_attempt
					('0:05:37', u'5*4*3')
	part2_correct_attempt
					['0:10:12', u'6!/(2!2!2!)']

4 Student ID:ppanourg

	first_attempt
					2015-10-13 15:28:31
	part1_correct_attempt
					['0:00:00', u'4!/(4)']
	part2_incorrect_attempt
					('0:00:00', u'6!')
					('1 day, 3:34:06', u'6!')
	part2_correct_attempt
					['1 day, 3:50:27', u'6!/12']

5 Student ID:atorr

	first_attempt
					2015-10-11 00:17:54
	part1_correct_attempt
					['0:00:00', u'6']
	part2_incorrect_attempt
					('0:00:24', u'6!')
	part2_correct_attempt
					['0:03:47', u'6!/(2! * 2! * 2!)']

6 Student ID:any027

	first_attempt
					2015-10-09 08:57:02
	part1_correct_attempt
					['0:00:00', u'4 ! / (2! * 2!)']
	part2_incorrect_attempt
					('0:01:27', u'6^6')
	part2_correct_attempt
					['0:02:08', u'6! / ( 3! * 2!* 1!)']

7 Student ID:rwthomps

	first_attempt
					2015-10-11 20:55:59
	part1_correct_attempt
					['0:00:00', u'(4!)/[(2!) * (2!)]']
	part2_incorrect_attempt
					('0:00:00', u'C(8, 2)')
	part2_correct_attempt
					['0:01:19', u'(6!)/[(2!) * (2!) * (2!)]']

8 Student ID:mroknich

	first_attempt
					2015-10-11 02:33:13
	part1_correct_attempt
					['0:00:00', u'6']
	part2_incorrect_attempt
					('0:00:42', u'3!')
					('1 day, 22:13:43', u'30^3')
					('1 day, 22:14:04', u'6!')
	part2_correct_attempt
					['1 day, 22:26:08', u'6!/(2!2!2!)']

9 Student ID:ctgraves

	first_attempt
					2015-10-12 22:53:34
	part1_correct_attempt
					['0:00:00', u'6']
	part2_incorrect_attempt
					('0:23:37', u'5*4*4*3*2')
					('0:28:39', u'5*4*4*3')
	part2_correct_attempt
					['0:29:55', u'5*4*3']

10 Student ID:jdeon

	first_attempt
					2015-10-09 03:39:46
	part1_correct_attempt
					['0:00:00', u'C(4,2)']
	part2_incorrect_attempt
					('0:02:46', u'C(3,2)')
					('0:03:00', u'3!')
	part2_correct_attempt
					['0:03:48', u'6!/(2! * 2! * 2!)']

11 Student ID:p4kumar

	first_attempt
					2015-10-15 06:06:23
	part1_correct_attempt
					['0:00:00', u'(4*3*2*1)/4']
	part2_incorrect_attempt
					('0:00:20', u'(6!)/(2)')
	part2_correct_attempt
					['0:04:22', u'5!/2']

12 Student ID:tpmach

	first_attempt
					2015-10-10 21:59:16
	part1_correct_attempt
					['0:00:00', u'4!/(2!*2!)']
	part2_incorrect_attempt
					('0:02:06', u'4!')
					('0:02:49', u'5!')
	part2_correct_attempt
					['0:03:35', u'5!/2!']

13 Student ID:ttimmons

	first_attempt
					2015-10-09 18:13:01
	part1_correct_attempt
					['0:00:00', u'C(4,2)']
	part2_incorrect_attempt
					('0:00:13', u'C(6,3)')
					('1 day, 5:52:41', u'6!')
					('1 day, 5:53:09', u'6*5*4*3*2*1')
					('1 day, 5:55:46', u'3!*3!*1!')
					('1 day, 5:56:10', u'C(6,3)*C(6,3)*C(6,1)')
	part2_correct_attempt
					['1 day, 5:56:35', u'[6!]/[3!*2!*1!]']

14 Student ID:jew037

	first_attempt
					2015-10-14 01:19:59
	part1_correct_attempt
					['0:00:00', u'(4*3*2)/4']
	part2_incorrect_attempt
					('0:00:46', u'6!')
	part2_correct_attempt
					['0:02:16', u'6!/(3!2!)']

15 Student ID:jnatale

	first_attempt
					2015-10-12 22:44:54
	part1_correct_attempt
					['0:00:00', u'6']
	part2_incorrect_attempt
					('0:00:12', u'6!')
					('0:00:24', u'3!')
					('0:00:43', u'3! + 2! + 1!')
	part2_correct_attempt
					['0:19:38', u'60']

16 Student ID:jblynch

	first_attempt
					2015-10-12 01:36:12
	part1_correct_attempt
					['0:00:00', u'4!/(2!*2!)']
	part2_incorrect_attempt
					('0:00:00', u'3!')
					('0:04:54', u'2*3!')
	part2_correct_attempt
					['0:07:52', u'6!/(2!*2!*2!)']

17 Student ID:avasavad

	first_attempt
					2015-10-12 00:36:17
	part1_correct_attempt
					['0:00:00', u'6']
	part2_incorrect_attempt
					('0:00:00', u'6!')

18 Student ID:vsosnovs

	first_attempt
					2015-10-10 21:34:31
	part1_correct_attempt
					['0:00:00', u'4!/4']
	part2_incorrect_attempt
					('0:00:47', u'3!/6')
					('0:02:42', u'8!/6')
					('0:03:27', u'8!/(3!)(5!)')
					('0:05:02', u'8!/5!')
	part2_correct_attempt
					['0:06:49', u'6!/(2!*2!*2!)']

19 Student ID:v3doan

	first_attempt
					2015-10-11 00:12:45
	part1_correct_attempt
					['0:00:00', u'C(4,2)']
	part2_incorrect_attempt
					('0:02:01', u'5!')
					('0:02:09', u'C(5,2)')
					('0:04:32', u'4! * 4')
					('0:04:45', u'4! * 4 / 2')
					('0:05:08', u'C(4,2) * 4')
	part2_correct_attempt
					['0:09:56', u'5! / 2']

20 Student ID:haliew

	first_attempt
					2015-10-12 19:43:04
	part1_correct_attempt
					['0:00:00', u'6']
	part2_incorrect_attempt
					('0:00:00', u'4!')
					('0:01:17', u'P(4,3)')
	part2_correct_attempt
					['0:05:46', u'5!/(1!*2!*1!*1!)']

21 Student ID:agian

	first_attempt
					2015-10-15 06:50:45
	part1_correct_attempt
					['0:00:00', u'4*3*2/(2*2)']
	part2_incorrect_attempt
					('0:00:08', u' 6!/(2!*2!*2!)')
					('0:00:28', u'6!/(2!)')
	part2_correct_attempt
					['0:00:45', u'5!/(2!)']

22 Student ID:alhung

	first_attempt
					2015-10-13 06:58:45
	part1_correct_attempt
					['0:00:00', u'C(4,2)']
	part2_incorrect_attempt
					('0:00:00', u'C(5,4)')
					('0:00:30', u'P(5,4)')
					('0:07:23', u'4!')
	part2_correct_attempt
					['1:38:43', u'5!/2']

23 Student ID:tcn013

	first_attempt
					2015-10-13 05:08:02
	part1_correct_attempt
					['0:00:00', u'4!/(2!*2!)']
	part2_incorrect_attempt
					('0:02:28', u'2*3!')
					('0:02:46', u'(3!)^2')
					('0:11:12', u'C(6,2)')
					('0:11:28', u'C(6,2) + C(4,2) + C(2,2)')
	part2_correct_attempt
					['0:11:55', u'C(6,2) * C(4,2) * C(2,2)']

24 Student ID:wcwhite

	first_attempt
					2015-10-13 17:20:30
	part1_correct_attempt
					['0:00:00', u'4!/((2!(2!)))']
	part2_incorrect_attempt
					('0:01:22', u'6!')
	part2_correct_attempt
					['0:55:30', u'6!/((3!)(2!))']

25 Student ID:l8ngo

	first_attempt
					2015-10-09 14:51:48
	part1_correct_attempt
					['0:00:00', u'6']
	part2_incorrect_attempt
					('0:00:00', u'4!')
	part2_correct_attempt
					['0:01:07', u'5!/2!']

26 Student ID:lahawkin

	first_attempt
					2015-10-13 23:25:39
	part1_correct_attempt
					['0:00:00', u'4!/(2!*2!)']
	part2_incorrect_attempt
					('0:02:52', u'5!')
	part2_correct_attempt
					['0:03:05', u'5!/(2!)']

27 Student ID:aysee

	first_attempt
					2015-10-12 22:43:38
	part1_correct_attempt
					['0:00:00', u'4!/(2!2!)']
	part2_incorrect_attempt
					('0:00:00', u'4!')
	part2_correct_attempt
					['0:00:37', u'5!/2!']

28 Student ID:sghouse

	first_attempt
					2015-10-09 18:03:44
	part1_correct_attempt
					['0:00:00', u'6']
	part2_incorrect_attempt
					('0:02:15', u'5*4*3*2')
	part2_correct_attempt
					['0:03:13', u'6!/8']

29 Student ID:eaherman

	first_attempt
					2015-10-10 00:27:42
	part1_correct_attempt
					['0:00:00', u'6']
	part2_incorrect_attempt
					('0:00:00', u'4!')
					('0:01:11', u'5!')
	part2_correct_attempt
					['0:07:32', u'5!/2!']

30 Student ID:w4shin

	first_attempt
					2015-10-12 02:36:01
	part1_correct_attempt
					['0:00:00', u'4!/(2!*2!)']
	part2_incorrect_attempt
					('0:00:16', u'(5!*4!)/(3!*2!)')
	part2_correct_attempt
					['0:00:59', u'5!/(2!)']

31 Student ID:etemlock

	first_attempt
					2015-10-09 16:46:30
	part1_correct_attempt
					['0:00:00', u'(4! / (2! 2!))']
	part2_incorrect_attempt
					('0:20:04', u'[C(6,3) * C(3,1)] * [C(3,2) * C(2,1)]')
					('0:27:21', u'C(7,3)')
					('0:27:40', u'C(6,3)')
					('0:27:48', u'P(6,3)/3')
					('0:30:53', u'(7!/ (2! 4!))')
	part2_correct_attempt
					['0:32:15', u'6!/(2!3!)']

32 Student ID:hmshah

	first_attempt
					2015-10-15 00:58:47
	part1_correct_attempt
					['0:00:00', u'C(4,2)']
	part2_incorrect_attempt
					('0:00:19', u'C(6,3)')
					('0:00:23', u'P(6,3)')
					('0:01:14', u'P(6,2)')
					('0:01:18', u'C(6,2)')
	part2_correct_attempt
					['6:58:58', u'6!/(2! * 3!)']

33 Student ID:jtfrankl

	first_attempt
					2015-10-14 23:31:01
	part1_correct_attempt
					['0:00:00', u'3!']
	part2_incorrect_attempt
					('0:01:00', u'4! 3!')
					('0:02:05', u'4! 6')
	part2_correct_attempt
					['0:04:49', u'10 ( 6)']

34 Student ID:a2ahmed

	first_attempt
					2015-10-14 23:17:52
	part1_correct_attempt
					['0:00:00', u'6']
	part2_incorrect_attempt
					('0:00:00', u'C(6,3)')
					('0:01:09', u'(3!*2!)')
	part2_correct_attempt
					['3:22:50', u'(6!)/(3!*2!)']

35 Student ID:csl030

	first_attempt
					2015-10-10 02:13:42
	part1_correct_attempt
					['0:00:00', u'C(4,2)']
	part2_incorrect_attempt
					('0:01:02', u'P(5, 2)')
					('0:01:12', u'P(5, 4)')
	part2_correct_attempt
					['3:20:43', u'P(5, 5) /2']

36 Student ID:arc013

	first_attempt
					2015-10-13 01:25:49
	part1_correct_attempt
					['0:00:00', u'C(4,2)']
	part2_incorrect_attempt
					('0:01:14', u'(C(6,3))* C(3, 2) *6')
	part2_correct_attempt
					['0:01:33', u'(C(6,3))* C(3, 2)']

37 Student ID:jhc010

	first_attempt
					2015-10-15 15:29:15
	part1_correct_attempt
					['0:00:00', u'6']
	part2_incorrect_attempt
					('0:00:00', u'5*4*3*2')
					('0:00:08', u'5!')
					('0:00:12', u'4!')
	part2_correct_attempt
					['0:01:41', u'5!/2!']

38 Student ID:v4sharma

	first_attempt
					2015-10-11 22:25:36
	part1_correct_attempt
					['0:00:00', u'4!/(2! * 2!)']
	part2_incorrect_attempt
					('0:00:00', u'4!')
					('0:00:38', u'4!/2!')
	part2_correct_attempt
					['2 days, 0:24:34', u'5!/2!']

39 Student ID:qfu

	first_attempt
					2015-10-09 03:43:57
	part1_correct_attempt
					['0:00:00', u'C(4,2)']
	part2_incorrect_attempt
					('0:00:00', u'C(5,3)*C(3,2)')
	part2_correct_attempt
					['0:00:17', u'C(6,3)*C(3,2)']

40 Student ID:r2fisher

	first_attempt
					2015-10-11 21:30:44
	part1_correct_attempt
					['0:00:00', u'4!/(2!*2!)']
	part2_incorrect_attempt
					('0:00:00', u'6!')
	part2_correct_attempt
					['0:00:31', u'6!/(2!*2!*2!)']

41 Student ID:yhhan

	first_attempt
					2015-10-12 21:56:48
	part1_correct_attempt
					['0:00:00', u'6']
	part2_incorrect_attempt
					('0:00:33', u'P(6,3)')
	part2_correct_attempt
					['0:03:14', u'6!/(3!*2)']

42 Student ID:volim

	first_attempt
					2015-10-11 04:50:53
	part1_correct_attempt
					['0:00:00', u'6']
	part2_incorrect_attempt
					('0:00:51', u'4(7!)')
	part2_correct_attempt
					['0:01:39', u'(6!)/(8)']

43 Student ID:rbdoming

	first_attempt
					2015-10-13 06:53:58
	part1_correct_attempt
					['0:00:00', u'4!/ (2! * 2!)']
	part2_incorrect_attempt
					('0:00:00', u'4!/2!')
	part2_correct_attempt
					['0:00:18', u'5!/2!']

44 Student ID:tdurrer

	first_attempt
					2015-10-09 01:51:54
	part1_correct_attempt
					['0:00:00', u'4!/(2!*2!)']
	part2_incorrect_attempt
					('0:00:00', u'3!')
	part2_correct_attempt
					['0:02:53', u'6!/(2!*2!*2!)']

45 Student ID:ajvanega

	first_attempt
					2015-10-09 00:06:50
	part1_correct_attempt
					['0:00:00', u'6']
	part2_incorrect_attempt
					('0:01:15', u'5^5')
					('0:03:37', u'4!')
					('0:05:28', u'5!')
					('3 days, 0:21:27', u'5!')
	part2_correct_attempt
					['3 days, 0:24:09', u'60']

46 Student ID:jmiclat

	first_attempt
					2015-10-14 07:42:00
	part1_correct_attempt
					['0:00:00', u'6']
	part2_incorrect_attempt
					('0:23:54', u'15*15*15')
					('0:36:41', u'5!')
	part2_correct_attempt
					['0:37:05', u'3*5*3*2']

47 Student ID:ytc012

	first_attempt
					2015-10-12 22:09:11
	part1_correct_attempt
					['0:00:00', u'6']
	part2_incorrect_attempt
					('0:00:49', u'6!/3/2')
					('0:01:49', u'3!/6')
					('0:02:13', u'6!/3/3/2/1')
					('0:03:33', u'20*3/6')
					('0:04:17', u'(20/3)*(3/2)')
					('0:05:14', u'(20/3!)*(3/2)')
					('0:05:19', u'(20/3!)*(3/2!)')
					('0:07:58', u'60/6')
	part2_correct_attempt
					['7:27:56', u'6!/(3!2!)']

48 Student ID:mtrafeca

	first_attempt
					2015-10-10 18:32:18
	part1_correct_attempt
					['0:00:00', u'6']
	part2_incorrect_attempt
					('0:04:40', u'5!')
					('0:05:00', u'4!')
	part2_correct_attempt
					['0:08:05', u'5!/2']

49 Student ID:whcombs

	first_attempt
					2015-10-12 21:18:47
	part1_correct_attempt
					['0:00:00', u'C(4,2)']
	part2_incorrect_attempt
					('0:00:05', u'P(6,2)')
					('0:00:23', u'C(6,3)')
					('0:00:28', u'P(6,3)')
					('0:00:51', u'C(6,3)')
	part2_correct_attempt
					['0:04:18', u'6!/(2!2!2!)']












