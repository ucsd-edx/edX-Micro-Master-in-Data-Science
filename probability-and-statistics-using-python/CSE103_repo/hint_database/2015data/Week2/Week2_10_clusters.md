#Problem 10

    $a=random(48,55,1);

    1. Suppose we choose two *different* numbers, each from 1 to 5. If the order of the numbers is *not* important, how many different choices can we pick?
    [_______]{Compute("(5*4)/2")}

    2. In the "6/[$a]" lottery game, a player picks six numbers from 1 to [$a].
    How many different choices does the player have if repetition is not allowed?
    Note again that the order of the numbers is not important.
    Your answer is : [_______]{Compute("$a*($a-1)*($a-2)*($a-3)*($a-4)*($a-5)/(6*5*4*3*2)")}


## Part 1

### (285) Mistake Group Digits of size 285




### (30) Mistake Group ['R.0.0'] of size 30
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|5*4/2	|5! / 3!	|[('R.0.0', 5.0, u'5', u'5')]	|
|1	|5*4/2	|5! * 4!	|[('R.0.0', 5.0, u'5', u'5')]	|
|2	|5*4/2	|5!/3!	|[('R.0.0', 5.0, u'5', u'5')]	|
|3	|5*4/2	|(5!)/(3!)	|[('R.0.0', 5.0, u'5', u'5')]	|
|4	|5*4/2	|5!/(2!*(5-3)!)	|[('R.0.0', 5.0, u'5', u'5')]	|
|5	|5*4/2	|5!/(5-2)!	|[('R.0.0', 5.0, u'5', u'5')]	|
|6	|5*4/2	|5!/6	|[('R.0.0', 5.0, u'5', u'5')]	|
|7	|5*4/2	|5!/(3!)	|[('R.0.0', 5.0, u'5', u'5')]	|
|8	|5*4/2	|5!/[(5-2)!]	|[('R.0.0', 5.0, u'5', u'5')]	|
|9	|5*4/2	|5!(4!)	|[('R.0.0', 5.0, u'5', u'5')]	|
|10	|5*4/2	|5!*4!	|[('R.0.0', 5.0, u'5', u'5')]	|
|11	|5*4/2	|5!/(2!(5-3)!)	|[('R.0.0', 5.0, u'5', u'5')]	|
|12	|5*4/2	|5!/(2!(5-2!))	|[('R.0.0', 5.0, u'5', u'5')]	|
|13	|5*4/2	|(5!)/(5-2)!	|[('R.0.0', 5.0, u'5', u'5')]	|
|14	|5*4/2	|5!5!	|[('R.0.0', 5.0, u'5', u'5')]	|




### (11) Mistake Group ['R.1'] of size 11
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|5*4/2	|P(5,2)	|[('R.1', 2.0, u'2', u'2')]	|
|1	|5*4/2	|P(4,2)	|[('R.1', 2.0, u'2', u'2')]	|
|2	|5*4/2	|5^2	|[('R.1', 2.0, u'2', u'2')]	|
|3	|5*4/2	|5+4+3+2	|[('R.1', 2.0, u'2', u'2')]	|
|4	|5*4/2	|C(6,2)	|[('R.1', 2.0, u'2', u'2')]	|
|5	|5*4/2	|C(10,2)	|[('R.1', 2.0, u'2', u'2')]	|
|6	|5*4/2	|C(9,2)	|[('R.1', 2.0, u'2', u'2')]	|
|7	|5*4/2	|5 + 4 + 3 + 2	|[('R.1', 2.0, u'2', u'2')]	|




### (11) Mistake Group Fraction of size 11




### (10) Mistake Group ['R.0.0', 'R.1'] of size 10
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|5*4/2	|5!/2!	|[('R.0.0', 5.0, u'5', u'5'), ('R.1', 2.0, u'2', u'2!')]	|
|1	|5*4/2	|5*5*2	|[('R.0.0', 5.0, u'5', u'5'), ('R.1', 2.0, u'2', u'2')]	|
|2	|5*4/2	|(5!)/(2!)	|[('R.0.0', 5.0, u'5', u'5'), ('R.1', 2.0, u'2', u'2!')]	|
|3	|5*4/2	|5!*2	|[('R.0.0', 5.0, u'5', u'5'), ('R.1', 2.0, u'2', u'2')]	|
|4	|5*4/2	|5!/(5-3)!	|[('R.0.0', 5.0, u'5', u'5'), ('R.1', 2.0, u'2', u'(5-3)!')]	|




### (8) Mistake Group ['R.0', 'R.1'] of size 8
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|5*4/2	|5*4*2	|[('R.0', 20.0, u'5*4', u'5*4'), ('R.1', 2.0, u'2', u'2')]	|
|1	|5*4/2	|(5!)/(3!)(2!)	|[('R.0', 20.0, u'5*4', u'(5!)/(3!)'), ('R.1', 2.0, u'2', u'2!')]	|




### (4) Mistake Group ['R.0'] of size 4
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|5*4/2	|5*4*3	|[('R.0', 20.0, u'5*4', u'5*4')]	|
|1	|5*4/2	|5*4-5	|[('R.0', 20.0, u'5*4', u'5*4')]	|
|2	|5*4/2	|5*4 - 5	|[('R.0', 20.0, u'5*4', u'5*4')]	|




### (67) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:a8ho

	first_attempt
					2015-10-07 03:51:13
	part1_incorrect_attempt
					('0:00:00', u'2^5')
					('0:00:17', u'5*4')
					('0:01:30', u'52*51*50*49*48*47*46')
					('0:01:39', u'52*51*50*49*48*47')
	part1_correct_attempt
					['0:02:48', u'10']

1 Student ID:dlgoldbe

	first_attempt
					2015-10-08 04:41:12
	part1_incorrect_attempt
					('0:00:00', u'5*4')
	part1_correct_attempt
					['0:00:31', u'(5*4)/2']

2 Student ID:ttimmons

	first_attempt
					2015-10-02 19:33:18
	part1_incorrect_attempt
					('0:00:00', u'5!')
	part1_correct_attempt
					['0:01:20', u'C(5,2)']

3 Student ID:jfalcone

	first_attempt
					2015-10-07 03:10:11
	part1_incorrect_attempt
					('0:00:00', u'5 * 4')
	part1_correct_attempt
					['0:03:26', u'(5 * 4)/2']

4 Student ID:h4tu

	first_attempt
					2015-10-08 18:45:14
	part1_incorrect_attempt
					('0:00:00', u'5*5')
					('0:00:00', u'5*4')
	part1_correct_attempt
					['0:01:55', u'5*4/2']

5 Student ID:kebao

	first_attempt
					2015-10-03 17:42:59
	part1_incorrect_attempt
					('0:00:00', u'5 * 5')
	part1_correct_attempt
					['0:01:35', u'10']

6 Student ID:nisharma

	first_attempt
					2015-10-04 23:37:25
	part1_incorrect_attempt
					('0:00:00', u'5*4')
	part1_correct_attempt
					['2:52:10', u'(5!)/(2!*3!)']

7 Student ID:glcohen

	first_attempt
					2015-10-04 22:27:31
	part1_incorrect_attempt
					('0:00:00', u'5*4')
	part1_correct_attempt
					['0:19:08', u'(5!)/((3!)(2!))']

8 Student ID:achava

	first_attempt
					2015-10-02 04:30:27
	part1_incorrect_attempt
					('0:00:00', u'5!')
	part1_correct_attempt
					['0:25:14', u'5!/((2!)*(3!))']

9 Student ID:ewbrenna

	first_attempt
					2015-10-04 04:04:02
	part1_incorrect_attempt
					('0:00:00', u'5*4')
					('0:00:16', u'5*5')
	part1_correct_attempt
					['0:03:50', u'10']

10 Student ID:any027

	first_attempt
					2015-10-03 10:29:46
	part1_incorrect_attempt
					('0:00:00', u'5 * 4')
					('0:00:14', u'5!')
					('0:00:18', u'4!')
					('0:02:53', u'5 * 4 ')
					('0:04:42', u'4*3')
					('0:05:23', u'5 * 4!')
	part1_correct_attempt
					['0:13:46', u'10']

11 Student ID:anislam

	first_attempt
					2015-10-08 23:40:51
	part1_incorrect_attempt
					('0:00:00', u'5!')
					('0:00:46', u'5 + 4 + 3 + 2 +1')
	part1_correct_attempt
					['0:01:06', u'4 + 3 + 2 + 1']

12 Student ID:sachadal

	first_attempt
					2015-10-05 18:44:10
	part1_incorrect_attempt
					('0:00:00', u'5*4')
	part1_correct_attempt
					['0:01:18', u'C(5,2)']

13 Student ID:kthui

	first_attempt
					2015-10-04 06:12:35
	part1_incorrect_attempt
					('0:00:00', u'5*5')
	part1_correct_attempt
					['0:06:58', u'5!/((5-2)!2!)']

14 Student ID:e9brown

	first_attempt
					2015-10-08 01:57:39
	part1_incorrect_attempt
					('0:00:00', u'4!')
	part1_correct_attempt
					['0:00:13', u'10']

15 Student ID:mbl003

	first_attempt
					2015-10-02 20:46:16
	part1_incorrect_attempt
					('0:00:00', u'5*4')
	part1_correct_attempt
					['0:00:18', u'10']

16 Student ID:vasharma

	first_attempt
					2015-10-05 05:19:12
	part1_incorrect_attempt
					('0:00:00', u'5!')
					('0:00:13', u'(25)!')
	part1_correct_attempt
					['0:00:28', u'10']

17 Student ID:n2patil

	first_attempt
					2015-10-06 15:39:56
	part1_incorrect_attempt
					('0:00:00', u'5*4')
	part1_correct_attempt
					['0:00:59', u'10']

18 Student ID:s2chaudh

	first_attempt
					2015-10-05 16:59:15
	part1_incorrect_attempt
					('0:00:00', u'5*4')
					('0:00:36', u'5*5')
	part1_correct_attempt
					['1 day, 13:52:16', u'10']

19 Student ID:jmiclat

	first_attempt
					2015-10-07 23:32:07
	part1_incorrect_attempt
					('0:00:00', u'5*4')
	part1_correct_attempt
					['0:00:28', u'5!/ (2!*3!)']

20 Student ID:gsrandha

	first_attempt
					2015-10-02 01:18:00
	part1_incorrect_attempt
					('0:00:00', u'51*50*49*48*47*46')
					('0:00:13', u'50*49*48*47*46*45')
	part1_correct_attempt
					['0:01:02', u'10']

21 Student ID:ccn001

	first_attempt
					2015-10-06 05:43:27
	part1_incorrect_attempt
					('0:00:00', u'5*4')
	part1_correct_attempt
					['1:10:48', u'(5!)/((5-2)!2!)']

22 Student ID:jhc010

	first_attempt
					2015-10-08 14:21:42
	part1_incorrect_attempt
					('0:00:00', u'5!')
					('0:00:04', u'4!')
	part1_correct_attempt
					['0:00:46', u'10']

23 Student ID:kquong

	first_attempt
					2015-10-03 21:02:04
	part1_incorrect_attempt
					('0:00:00', u'5*4')
					('0:02:45', u'5*5')
					('0:09:03', u'5*5')
	part1_correct_attempt
					['0:11:27', u'(5!/3!)/2!']

24 Student ID:t1tran

	first_attempt
					2015-10-03 05:38:53
	part1_incorrect_attempt
					('0:00:00', u'5*4')
	part1_correct_attempt
					['0:02:44', u'5!/[(5-2)!2!]']

25 Student ID:avasavad

	first_attempt
					2015-10-02 04:33:06
	part1_incorrect_attempt
					('0:00:00', u'5 * 4')
					('0:00:00', u'2 * 5 * 4')
	part1_correct_attempt
					['4 days, 1:22:13', u'5!/(2!*3!)']

26 Student ID:btn023

	first_attempt
					2015-10-02 01:42:27
	part1_incorrect_attempt
					('0:00:00', u'5*4')
	part1_correct_attempt
					['0:00:29', u'C(5,2)']

27 Student ID:s6deng

	first_attempt
					2015-10-06 06:01:40
	part1_incorrect_attempt
					('0:00:00', u'5*4')
					('0:05:34', u'C(5,4)')
					('0:05:39', u'P(5,4)')
	part1_correct_attempt
					['14:39:34', u'5!/(3!2!)']

28 Student ID:jap009

	first_attempt
					2015-10-05 02:22:20
	part1_incorrect_attempt
					('0:00:00', u'5*4')
	part1_correct_attempt
					['3 days, 20:10:47', u'10']

29 Student ID:akhmelni

	first_attempt
					2015-10-08 21:26:56
	part1_incorrect_attempt
					('0:00:00', u'5 * 5')
					('0:00:08', u'5 * 4')
					('0:07:38', u'(54 * 53 * 52 * 51 * 50 * 49) / 5!')
	part1_correct_attempt
					['0:08:01', u'10']

30 Student ID:kalang

	first_attempt
					2015-10-05 22:28:38
	part1_incorrect_attempt
					('0:00:00', u'5*4')
					('0:02:39', u'5!')
	part1_correct_attempt
					['0:03:41', u'5!/(2!*3!)']

31 Student ID:msaguiar

	first_attempt
					2015-10-06 04:04:44
	part1_incorrect_attempt
					('0:00:00', u'5*4')
	part1_correct_attempt
					['0:04:06', u'5!/((2!)(3!))']

32 Student ID:rraiyyan

	first_attempt
					2015-10-06 06:32:42
	part1_incorrect_attempt
					('0:00:00', u'4*5')
	part1_correct_attempt
					['0:01:14', u'5!/(2!*3!)']

33 Student ID:yhhan

	first_attempt
					2015-10-08 18:46:21
	part1_incorrect_attempt
					('0:00:00', u'5*4')
	part1_correct_attempt
					['0:00:56', u'C(5,2)']

34 Student ID:kvass

	first_attempt
					2015-10-04 20:57:12
	part1_incorrect_attempt
					('0:00:00', u'5*5')
	part1_correct_attempt
					['0:02:42', u'10']

35 Student ID:dsmonaha

	first_attempt
					2015-10-05 18:20:29
	part1_incorrect_attempt
					('0:00:00', u'C(5,1)')
	part1_correct_attempt
					['0:00:04', u'C(5,2)']

36 Student ID:tcn013

	first_attempt
					2015-10-06 00:39:12
	part1_incorrect_attempt
					('0:00:00', u'5!/4!')
					('0:03:25', u'5!')
	part1_correct_attempt
					['0:09:45', u'5!/(2!3!)']

37 Student ID:wcwhite

	first_attempt
					2015-10-06 18:44:47
	part1_incorrect_attempt
					('0:00:00', u'5!')
					('0:02:50', u'5*4')
					('0:03:06', u'4*3')
					('0:05:11', u'5*4')
					('0:09:02', u'10*9')
	part1_correct_attempt
					['0:17:31', u'5!/(2!(5-2)!)']

38 Student ID:kmc012

	first_attempt
					2015-10-05 07:34:02
	part1_incorrect_attempt
					('0:00:00', u'(52!)/(46!)')
					('0:00:18', u'(52!)/((46!)(6!))')
	part1_correct_attempt
					['0:01:13', u'20/2']

39 Student ID:hah008

	first_attempt
					2015-10-07 23:22:50
	part1_incorrect_attempt
					('0:00:00', u'5!')
					('0:00:00', u'53*52*51*50*49*48')
					('0:00:00', u'53*52*51*50*49*48')
					('0:00:21', u'53^6')
	part1_correct_attempt
					['7:02:05', u'C(5, 2)']

40 Student ID:sippolit

	first_attempt
					2015-10-03 19:40:52
	part1_incorrect_attempt
					('0:00:00', u'5!')
	part1_correct_attempt
					['0:48:35', u'10']

41 Student ID:daw023

	first_attempt
					2015-10-03 07:47:40
	part1_incorrect_attempt
					('0:00:00', u'5*4')
	part1_correct_attempt
					['0:17:36', u'5!/(3!*2)']

42 Student ID:dando

	first_attempt
					2015-10-04 19:51:58
	part1_incorrect_attempt
					('0:00:00', u'5 * 4')
	part1_correct_attempt
					['0:00:46', u'10']

43 Student ID:eaherman

	first_attempt
					2015-10-03 20:37:33
	part1_incorrect_attempt
					('0:00:00', u'5!')
	part1_correct_attempt
					['0:08:52', u'10']

44 Student ID:sayao

	first_attempt
					2015-10-03 00:45:32
	part1_incorrect_attempt
					('0:00:00', u'5!/2!*3!')
	part1_correct_attempt
					['0:00:08', u'5!/2!/3!']

45 Student ID:ctroncos

	first_attempt
					2015-10-07 21:30:24
	part1_incorrect_attempt
					('0:00:00', u'5*4')
	part1_correct_attempt
					['0:02:45', u'(5!)/(2!(5-2)!)']

46 Student ID:acs008

	first_attempt
					2015-10-03 00:01:33
	part1_incorrect_attempt
					('0:00:00', u'5*4')
					('0:00:25', u'5*4')
					('0:01:52', u'5*5')
					('0:00:00', u'5*4')
	part1_correct_attempt
					['5 days, 4:11:37', u'10']

47 Student ID:c1sorian

	first_attempt
					2015-10-08 05:34:34
	part1_incorrect_attempt
					('0:00:00', u'5*5')
					('0:00:14', u'5*4')
	part1_correct_attempt
					['0:02:52', u'(5!)/(2!3!)']

48 Student ID:dtea

	first_attempt
					2015-10-08 18:47:47
	part1_incorrect_attempt
					('0:00:00', u'5*5')
					('0:00:07', u'5*4')
					('0:02:00', u'5!')
					('0:02:06', u'5*4')
					('0:02:35', u'5*5')
					('0:02:39', u'5*3')
					('0:02:44', u'5*4')
	part1_correct_attempt
					['0:05:54', u'5!/(2!(5-2)!)']

49 Student ID:lahawkin

	first_attempt
					2015-10-03 17:42:40
	part1_incorrect_attempt
					('0:00:00', u'5*4')
					('0:00:00', u'54*53*52*51*50*49')
	part1_correct_attempt
					['0:03:17', u'(5!)/(2!*3!)']

50 Student ID:cstringh

	first_attempt
					2015-10-03 23:52:03
	part1_incorrect_attempt
					('0:00:00', u'5*4')
					('0:01:02', u'5*5')
					('0:01:11', u'5!')
	part1_correct_attempt
					['0:03:53', u'5!/(2!(5-2)!)']

51 Student ID:csl030

	first_attempt
					2015-10-04 21:30:56
	part1_incorrect_attempt
					('0:00:00', u'5 * 4')
	part1_correct_attempt
					['0:00:24', u'C(5, 2)']

52 Student ID:rbdoming

	first_attempt
					2015-10-02 20:41:20
	part1_incorrect_attempt
					('0:00:00', u'5*4')
					('0:00:00', u'C(5,1)')
	part1_correct_attempt
					['0:05:40', u'C(5,2)']

53 Student ID:druble

	first_attempt
					2015-10-08 20:23:41
	part1_incorrect_attempt
					('0:00:00', u'5*4')
					('0:02:59', u'2*5*4')
	part1_correct_attempt
					['0:09:58', u'C(5,2)']

54 Student ID:starinia

	first_attempt
					2015-10-06 23:34:57
	part1_incorrect_attempt
					('0:00:00', u'5*4')
	part1_correct_attempt
					['0:00:36', u'5!/(2!(5-2)!)']

55 Student ID:m4salaza

	first_attempt
					2015-10-07 03:08:31
	part1_incorrect_attempt
					('0:00:00', u'48*47*46*45*44*43')
					('0:01:25', u'5*4*2-5')
	part1_correct_attempt
					['0:05:38', u'5*4/2']

56 Student ID:bpandayk

	first_attempt
					2015-10-08 15:16:07
	part1_incorrect_attempt
					('0:00:00', u'5!')
	part1_correct_attempt
					['0:27:13', u'10']

57 Student ID:xweng

	first_attempt
					2015-10-07 06:40:51
	part1_incorrect_attempt
					('0:00:00', u'50+49+48+47+46+45')
					('0:10:35', u'60^6')
					('0:12:27', u'50*49*48*47*46*45')
	part1_correct_attempt
					['0:34:28', u'10']

58 Student ID:lcardoso

	first_attempt
					2015-10-08 05:20:43
	part1_incorrect_attempt
					('0:00:00', u'5*5')
					('0:04:34', u'5*5-5')
	part1_correct_attempt
					['0:16:17', u'C(5,2)']

59 Student ID:klala

	first_attempt
					2015-10-05 20:12:47
	part1_incorrect_attempt
					('0:00:00', u'5*4')
	part1_correct_attempt
					['0:00:05', u'10']

60 Student ID:zig006

	first_attempt
					2015-10-06 00:54:18
	part1_incorrect_attempt
					('0:00:00', u'5+4+3+2+1')
					('0:06:42', u'50!/(6!44!)')
	part1_correct_attempt
					['0:08:06', u'5!/(2!3!)']

61 Student ID:cagatep

	first_attempt
					2015-10-08 00:36:46
	part1_incorrect_attempt
					('0:00:00', u'25 - 5')
	part1_correct_attempt
					['0:02:50', u'5!/(2!3!)']

62 Student ID:ggaddi

	first_attempt
					2015-10-03 00:49:48
	part1_incorrect_attempt
					('0:00:00', u'5*4')
	part1_correct_attempt
					['0:06:42', u'5!/(2!*3!)']

63 Student ID:muy002

	first_attempt
					2015-10-07 21:31:35
	part1_incorrect_attempt
					('0:00:00', u'5!')
	part1_correct_attempt
					['0:00:26', u'5!/(2!*3!)']

64 Student ID:kgrozav

	first_attempt
					2015-10-02 20:58:45
	part1_incorrect_attempt
					('0:00:00', u'5*4')
	part1_correct_attempt
					['0:01:39', u'(5!)/(2! * 3!)']

65 Student ID:whcombs

	first_attempt
					2015-10-07 18:27:39
	part1_incorrect_attempt
					('0:00:00', u'5*5')
					('0:05:26', u'5!/(5-1)!')
					('0:08:16', u'5*4')
	part1_correct_attempt
					['0:11:55', u'5!/(2!(5-2)!)']

66 Student ID:cprafull

	first_attempt
					2015-10-06 19:07:54
	part1_incorrect_attempt
					('0:00:00', u'5*4')
	part1_correct_attempt
					['0:00:16', u'5*4/2']












## Part 2

### (105) Mistake Group redirect of size 105




### (53) Mistake Group Digits of size 53




### (49) Mistake Group ['R.0'] of size 49
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|51*(51-1)*(51-2)*(51-3)*(51-4)*(51-5)/(6*5*4*3*2)	|(51*50*49*48*47*46)/2	|[('R.0', 12966811200.0, u'51*(51-1)*(51-2)*(51-3)*(51-4)*(51-5)', u'51*50*49*48*47*46')]	|
|1	|51*(51-1)*(51-2)*(51-3)*(51-4)*(51-5)/(6*5*4*3*2)	|(51*50*49*48*47*46)/6	|[('R.0', 12966811200.0, u'51*(51-1)*(51-2)*(51-3)*(51-4)*(51-5)', u'51*50*49*48*47*46')]	|
|2	|55*(55-1)*(55-2)*(55-3)*(55-4)*(55-5)/(6*5*4*3*2)	|(55*54*53*52*51*50)/(4!)	|[('R.0', 20872566000.0, u'55*(55-1)*(55-2)*(55-3)*(55-4)*(55-5)', u'55*54*53*52*51*50')]	|
|3	|55*(55-1)*(55-2)*(55-3)*(55-4)*(55-5)/(6*5*4*3*2)	|(55*54*53*52*51*50)/2	|[('R.0', 20872566000.0, u'55*(55-1)*(55-2)*(55-3)*(55-4)*(55-5)', u'55*54*53*52*51*50')]	|
|4	|55*(55-1)*(55-2)*(55-3)*(55-4)*(55-5)/(6*5*4*3*2)	|(55*54*53*52*51*50)/6	|[('R.0', 20872566000.0, u'55*(55-1)*(55-2)*(55-3)*(55-4)*(55-5)', u'55*54*53*52*51*50')]	|
|5	|55*(55-1)*(55-2)*(55-3)*(55-4)*(55-5)/(6*5*4*3*2)	|(55*54*53*52*51*50)/(6)	|[('R.0', 20872566000.0, u'55*(55-1)*(55-2)*(55-3)*(55-4)*(55-5)', u'55*54*53*52*51*50')]	|
|6	|55*(55-1)*(55-2)*(55-3)*(55-4)*(55-5)/(6*5*4*3*2)	|55*54*53*52*51*50/(5)	|[('R.0', 20872566000.0, u'55*(55-1)*(55-2)*(55-3)*(55-4)*(55-5)', u'55*54*53*52*51*50')]	|
|7	|55*(55-1)*(55-2)*(55-3)*(55-4)*(55-5)/(6*5*4*3*2)	|55*54*53*52*51*50/(36)	|[('R.0', 20872566000.0, u'55*(55-1)*(55-2)*(55-3)*(55-4)*(55-5)', u'55*54*53*52*51*50')]	|
|8	|55*(55-1)*(55-2)*(55-3)*(55-4)*(55-5)/(6*5*4*3*2)	|55*54*53*52*51*50/(6)	|[('R.0', 20872566000.0, u'55*(55-1)*(55-2)*(55-3)*(55-4)*(55-5)', u'55*54*53*52*51*50')]	|
|9	|51*(51-1)*(51-2)*(51-3)*(51-4)*(51-5)/(6*5*4*3*2)	|51*50*49*48*47*46*45	|[('R.0', 12966811200.0, u'51*(51-1)*(51-2)*(51-3)*(51-4)*(51-5)', u'51*50*49*48*47*46')]	|
|10	|53*(53-1)*(53-2)*(53-3)*(53-4)*(53-5)/(6*5*4*3*2)	|53*52*51*50*49*48*47	|[('R.0', 16529385600.0, u'53*(53-1)*(53-2)*(53-3)*(53-4)*(53-5)', u'53*52*51*50*49*48')]	|
|11	|54*(54-1)*(54-2)*(54-3)*(54-4)*(54-5)/(6*5*4*3*2)	|54*53*52*51*50*49*48	|[('R.0', 18595558800.0, u'54*(54-1)*(54-2)*(54-3)*(54-4)*(54-5)', u'54*53*52*51*50*49')]	|
|12	|54*(54-1)*(54-2)*(54-3)*(54-4)*(54-5)/(6*5*4*3*2)	|(54*53*52*51*50*49)/6	|[('R.0', 18595558800.0, u'54*(54-1)*(54-2)*(54-3)*(54-4)*(54-5)', u'54*53*52*51*50*49')]	|
|13	|48*(48-1)*(48-2)*(48-3)*(48-4)*(48-5)/(6*5*4*3*2)	|48*47*46*45*44*43/5!	|[('R.0', 8835488640.0, u'48*(48-1)*(48-2)*(48-3)*(48-4)*(48-5)', u'48*47*46*45*44*43')]	|
|14	|53*(53-1)*(53-2)*(53-3)*(53-4)*(53-5)/(6*5*4*3*2)	|(53*52*51*50*49*48) /6	|[('R.0', 16529385600.0, u'53*(53-1)*(53-2)*(53-3)*(53-4)*(53-5)', u'53*52*51*50*49*48')]	|
|15	|48*(48-1)*(48-2)*(48-3)*(48-4)*(48-5)/(6*5*4*3*2)	|48*47*46*45*44*43*42	|[('R.0', 8835488640.0, u'48*(48-1)*(48-2)*(48-3)*(48-4)*(48-5)', u'48*47*46*45*44*43')]	|
|16	|48*(48-1)*(48-2)*(48-3)*(48-4)*(48-5)/(6*5*4*3*2)	|48*47*46*45*44*43/6	|[('R.0', 8835488640.0, u'48*(48-1)*(48-2)*(48-3)*(48-4)*(48-5)', u'48*47*46*45*44*43')]	|
|17	|49*(49-1)*(49-2)*(49-3)*(49-4)*(49-5)/(6*5*4*3*2)	|49*48*47*46*45*44/6	|[('R.0', 10068347520.0, u'49*(49-1)*(49-2)*(49-3)*(49-4)*(49-5)', u'49*48*47*46*45*44')]	|
|18	|49*(49-1)*(49-2)*(49-3)*(49-4)*(49-5)/(6*5*4*3*2)	|(49*48*47*46*45*44)/(6)	|[('R.0', 10068347520.0, u'49*(49-1)*(49-2)*(49-3)*(49-4)*(49-5)', u'49*48*47*46*45*44')]	|
|19	|52*(52-1)*(52-2)*(52-3)*(52-4)*(52-5)/(6*5*4*3*2)	|(52!/(52-6)!)*6	|[('R.0', 14658134400.0, u'52*(52-1)*(52-2)*(52-3)*(52-4)*(52-5)', u'52!/(52-6)!')]	|
|20	|52*(52-1)*(52-2)*(52-3)*(52-4)*(52-5)/(6*5*4*3*2)	|((52!)/(52-6)!)-52	|[('R.0', 14658134400.0, u'52*(52-1)*(52-2)*(52-3)*(52-4)*(52-5)', u'(52!)/(52-6)!')]	|
|21	|52*(52-1)*(52-2)*(52-3)*(52-4)*(52-5)/(6*5*4*3*2)	|52*51*50*49*48*47/2	|[('R.0', 14658134400.0, u'52*(52-1)*(52-2)*(52-3)*(52-4)*(52-5)', u'52*51*50*49*48*47')]	|
|22	|52*(52-1)*(52-2)*(52-3)*(52-4)*(52-5)/(6*5*4*3*2)	|52*51*50*49*48*47/6	|[('R.0', 14658134400.0, u'52*(52-1)*(52-2)*(52-3)*(52-4)*(52-5)', u'52*51*50*49*48*47')]	|
|23	|51*(51-1)*(51-2)*(51-3)*(51-4)*(51-5)/(6*5*4*3*2)	|(51 * 50 * 49 * 48 * 47 * 46)/6	|[('R.0', 12966811200.0, u'51*(51-1)*(51-2)*(51-3)*(51-4)*(51-5)', u'51 * 50 * 49 * 48 * 47 * 46')]	|
|24	|51*(51-1)*(51-2)*(51-3)*(51-4)*(51-5)/(6*5*4*3*2)	|(51 * 50 * 49 * 48 * 47 * 46)/2	|[('R.0', 12966811200.0, u'51*(51-1)*(51-2)*(51-3)*(51-4)*(51-5)', u'51 * 50 * 49 * 48 * 47 * 46')]	|
|25	|48*(48-1)*(48-2)*(48-3)*(48-4)*(48-5)/(6*5*4*3*2)	|48*47*46*45*44*43/2	|[('R.0', 8835488640.0, u'48*(48-1)*(48-2)*(48-3)*(48-4)*(48-5)', u'48*47*46*45*44*43')]	|
|26	|48*(48-1)*(48-2)*(48-3)*(48-4)*(48-5)/(6*5*4*3*2)	|48*47*46*45*44*43/48	|[('R.0', 8835488640.0, u'48*(48-1)*(48-2)*(48-3)*(48-4)*(48-5)', u'48*47*46*45*44*43')]	|
|27	|50*(50-1)*(50-2)*(50-3)*(50-4)*(50-5)/(6*5*4*3*2)	|(50*49*48*47*46*45)/2	|[('R.0', 11441304000.0, u'50*(50-1)*(50-2)*(50-3)*(50-4)*(50-5)', u'50*49*48*47*46*45')]	|
|28	|53*(53-1)*(53-2)*(53-3)*(53-4)*(53-5)/(6*5*4*3*2)	|(53*52*51*50*49*48)/6	|[('R.0', 16529385600.0, u'53*(53-1)*(53-2)*(53-3)*(53-4)*(53-5)', u'53*52*51*50*49*48')]	|
|29	|51*(51-1)*(51-2)*(51-3)*(51-4)*(51-5)/(6*5*4*3*2)	|(51*50*49*48*47*46) - (51 + 51*51 + 51*51*51 + 51*51*51*51 + 51*51*51*51*51)	|[('R.0', 12966811200.0, u'51*(51-1)*(51-2)*(51-3)*(51-4)*(51-5)', u'51*50*49*48*47*46')]	|
|30	|51*(51-1)*(51-2)*(51-3)*(51-4)*(51-5)/(6*5*4*3*2)	|(51*50*49*48*47*46) - (51 + 51*50 + 51*50*49 + 51*50*49*48 + 51*50*49*48*47)	|[('R.0', 12966811200.0, u'51*(51-1)*(51-2)*(51-3)*(51-4)*(51-5)', u'51*50*49*48*47*46')]	|
|31	|48*(48-1)*(48-2)*(48-3)*(48-4)*(48-5)/(6*5*4*3*2)	|(48*47*46*45*44*43)/6	|[('R.0', 8835488640.0, u'48*(48-1)*(48-2)*(48-3)*(48-4)*(48-5)', u'48*47*46*45*44*43')]	|
|32	|48*(48-1)*(48-2)*(48-3)*(48-4)*(48-5)/(6*5*4*3*2)	|(48*47*46*45*44*43)/36	|[('R.0', 8835488640.0, u'48*(48-1)*(48-2)*(48-3)*(48-4)*(48-5)', u'48*47*46*45*44*43')]	|
|33	|52*(52-1)*(52-2)*(52-3)*(52-4)*(52-5)/(6*5*4*3*2)	|52 * 51 * 50 * 49 * 48 * 47 * 46	|[('R.0', 14658134400.0, u'52*(52-1)*(52-2)*(52-3)*(52-4)*(52-5)', u'52 * 51 * 50 * 49 * 48 * 47')]	|
|34	|54*(54-1)*(54-2)*(54-3)*(54-4)*(54-5)/(6*5*4*3*2)	|54*53*52*51*50*49*6	|[('R.0', 18595558800.0, u'54*(54-1)*(54-2)*(54-3)*(54-4)*(54-5)', u'54*53*52*51*50*49')]	|
|35	|50*(50-1)*(50-2)*(50-3)*(50-4)*(50-5)/(6*5*4*3*2)	|(50*49*48*47*46*45)/(5!)	|[('R.0', 11441304000.0, u'50*(50-1)*(50-2)*(50-3)*(50-4)*(50-5)', u'50*49*48*47*46*45')]	|
|36	|50*(50-1)*(50-2)*(50-3)*(50-4)*(50-5)/(6*5*4*3*2)	|(50*49*48*47*46*45)/(4!)	|[('R.0', 11441304000.0, u'50*(50-1)*(50-2)*(50-3)*(50-4)*(50-5)', u'50*49*48*47*46*45')]	|
|37	|50*(50-1)*(50-2)*(50-3)*(50-4)*(50-5)/(6*5*4*3*2)	|(50*49*48*47*46*45)/(2)	|[('R.0', 11441304000.0, u'50*(50-1)*(50-2)*(50-3)*(50-4)*(50-5)', u'50*49*48*47*46*45')]	|
|38	|50*(50-1)*(50-2)*(50-3)*(50-4)*(50-5)/(6*5*4*3*2)	|50*49*48*47*46*45*44	|[('R.0', 11441304000.0, u'50*(50-1)*(50-2)*(50-3)*(50-4)*(50-5)', u'50*49*48*47*46*45')]	|
|39	|50*(50-1)*(50-2)*(50-3)*(50-4)*(50-5)/(6*5*4*3*2)	|(50*49*48*47*46*45)/6	|[('R.0', 11441304000.0, u'50*(50-1)*(50-2)*(50-3)*(50-4)*(50-5)', u'50*49*48*47*46*45')]	|
|40	|50*(50-1)*(50-2)*(50-3)*(50-4)*(50-5)/(6*5*4*3*2)	|50*49*48*47*46*45/2	|[('R.0', 11441304000.0, u'50*(50-1)*(50-2)*(50-3)*(50-4)*(50-5)', u'50*49*48*47*46*45')]	|
|41	|50*(50-1)*(50-2)*(50-3)*(50-4)*(50-5)/(6*5*4*3*2)	|50*49*48*47*46*45/6	|[('R.0', 11441304000.0, u'50*(50-1)*(50-2)*(50-3)*(50-4)*(50-5)', u'50*49*48*47*46*45')]	|




### (32) Mistake Group Fraction of size 32




### (8) Mistake Group ['R.0.0.0.0.1', 'R.0.0.0.1', 'R.0.0.1', 'R.0.1'] of size 8
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0.0.1', 'R.0.0.0.1', 'R.0.0.1', 'R.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|51*(51-1)*(51-2)*(51-3)*(51-4)*(51-5)/(6*5*4*3*2)	|50*49*48*47*46*45	|[('R.0.0.0.0.1', 49.0, u'51-2', u'49'), ('R.0.0.0.1', 48.0, u'51-3', u'48'), ('R.0.0.1', 47.0, u'51-4', u'47'), ('R.0.1', 46.0, u'51-5', u'46')]	|
|1	|54*(54-1)*(54-2)*(54-3)*(54-4)*(54-5)/(6*5*4*3*2)	|53*52*51*50*49*48	|[('R.0.0.0.0.1', 52.0, u'54-2', u'52'), ('R.0.0.0.1', 51.0, u'54-3', u'51'), ('R.0.0.1', 50.0, u'54-4', u'50'), ('R.0.1', 49.0, u'54-5', u'49')]	|
|2	|48*(48-1)*(48-2)*(48-3)*(48-4)*(48-5)/(6*5*4*3*2)	|47*46*45*44*43*6	|[('R.0.0.0.0.1', 46.0, u'48-2', u'46'), ('R.0.0.0.1', 45.0, u'48-3', u'45'), ('R.0.0.1', 44.0, u'48-4', u'44'), ('R.0.1', 43.0, u'48-5', u'43')]	|
|3	|50*(50-1)*(50-2)*(50-3)*(50-4)*(50-5)/(6*5*4*3*2)	|49+48+47+46+45+44	|[('R.0.0.0.0.1', 48.0, u'50-2', u'48'), ('R.0.0.0.1', 47.0, u'50-3', u'47'), ('R.0.0.1', 46.0, u'50-4', u'46'), ('R.0.1', 45.0, u'50-5', u'45')]	|
|4	|54*(54-1)*(54-2)*(54-3)*(54-4)*(54-5)/(6*5*4*3*2)	|53 + 52 +51+50+49+48	|[('R.0.0.0.0.1', 52.0, u'54-2', u'52'), ('R.0.0.0.1', 51.0, u'54-3', u'51'), ('R.0.0.1', 50.0, u'54-4', u'50'), ('R.0.1', 49.0, u'54-5', u'49')]	|
|5	|54*(54-1)*(54-2)*(54-3)*(54-4)*(54-5)/(6*5*4*3*2)	|53*52*51*50*49*4825827165	|[('R.0.0.0.0.1', 52.0, u'54-2', u'52'), ('R.0.0.0.1', 51.0, u'54-3', u'51'), ('R.0.0.1', 50.0, u'54-4', u'50'), ('R.0.1', 49.0, u'54-5', u'49')]	|




### (7) Mistake Group ['R.1'] of size 7
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|53*(53-1)*(53-2)*(53-3)*(53-4)*(53-5)/(6*5*4*3*2)	|53!/6!	|[('R.1', 720.0, u'6*5*4*3*2', u'6!')]	|
|1	|54*(54-1)*(54-2)*(54-3)*(54-4)*(54-5)/(6*5*4*3*2)	|54!/(54-48)!	|[('R.1', 720.0, u'6*5*4*3*2', u'(54-48)!')]	|
|2	|50*(50-1)*(50-2)*(50-3)*(50-4)*(50-5)/(6*5*4*3*2)	|50!/(6!)	|[('R.1', 720.0, u'6*5*4*3*2', u'6!')]	|
|3	|54*(54-1)*(54-2)*(54-3)*(54-4)*(54-5)/(6*5*4*3*2)	|54!/6!	|[('R.1', 720.0, u'6*5*4*3*2', u'6!')]	|
|4	|52*(52-1)*(52-2)*(52-3)*(52-4)*(52-5)/(6*5*4*3*2)	|(56*55*54*53*52*51)/6!	|[('R.1', 720.0, u'6*5*4*3*2', u'6!')]	|
|5	|52*(52-1)*(52-2)*(52-3)*(52-4)*(52-5)/(6*5*4*3*2)	|52 * 51 * 50 * 49 * 48 * 47 * 46/(6*5*4*3*2*1)	|[('R.1', 720.0, u'6*5*4*3*2', u'6*5*4*3*2*1')]	|




### (2) Mistake Group ['R.0', 'R.1'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|54*(54-1)*(54-2)*(54-3)*(54-4)*(54-5)/(6*5*4*3*2)	|54!/48!*6!	|[('R.0', 18595558800.0, u'54*(54-1)*(54-2)*(54-3)*(54-4)*(54-5)', u'54!/48!'), ('R.1', 720.0, u'6*5*4*3*2', u'6!')]	|
|1	|51*(51-1)*(51-2)*(51-3)*(51-4)*(51-5)/(6*5*4*3*2)	|(51!)/(51-6)!(6!)	|[('R.0', 12966811200.0, u'51*(51-1)*(51-2)*(51-3)*(51-4)*(51-5)', u'(51!)/(51-6)!'), ('R.1', 720.0, u'6*5*4*3*2', u'6!')]	|




### (2) Mistake Group Wrong_Sign of size 2




### (1) Mistake Group ['R.0.1', 'R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|48*(48-1)*(48-2)*(48-3)*(48-4)*(48-5)/(6*5*4*3*2)	|(48*47*46*45*43)/6!	|[('R.0.1', 43.0, u'48-5', u'43'), ('R.1', 720.0, u'6*5*4*3*2', u'6!')]	|




### (50) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:h4tu

	first_attempt
					2015-10-08 18:47:09
	part1_correct_attempt
					['0:00:00', u'5*4/2']
	part2_incorrect_attempt
					('0:03:25', u'(50*49*48*47*46*45)')
	part2_correct_attempt
					['0:03:41', u'(50*49*48*47*46*45)/(6!)']

1 Student ID:haw081

	first_attempt
					2015-10-04 22:49:39
	part1_correct_attempt
					['0:00:00', u'10']
	part2_incorrect_attempt
					('0:00:00', u'52*51*50*49*48*47')
	part2_correct_attempt
					['0:00:22', u'20358520']

2 Student ID:lpettit

	first_attempt
					2015-10-05 00:35:28
	part1_correct_attempt
					['0:00:00', u'5!/(2!(5-2)!)']
	part2_incorrect_attempt
					('0:00:11', u'55!/6!49!')
	part2_correct_attempt
					['0:00:25', u'55!/(6!*49!)']

3 Student ID:jag028

	first_attempt
					2015-10-05 05:43:50
	part1_correct_attempt
					['0:00:00', u'10']
	part2_incorrect_attempt
					('0:01:09', u'53!')
					('0:01:17', u'52!')
	part2_correct_attempt
					['0:03:18', u'(53!)/(6!(53-6)!)']

4 Student ID:dlgoldbe

	first_attempt
					2015-10-08 04:41:43
	part1_correct_attempt
					['0:00:00', u'(5*4)/2']
	part2_incorrect_attempt
					('0:00:58', u'(48*47*46*45*44*43*42)/6')
	part2_correct_attempt
					['0:04:02', u'(48*47*46*45*44*43)/(6*5*4*3*2*1)']

5 Student ID:vsamant

	first_attempt
					2015-10-02 04:21:47
	part1_correct_attempt
					['0:00:00', u'5*4*3*2/(2*3*2)']
	part2_incorrect_attempt
					('0:00:55', u'54*53*52*51*50*49')
	part2_correct_attempt
					['0:01:31', u'54!/((6!)(48!))']

6 Student ID:kvass

	first_attempt
					2015-10-04 20:59:54
	part1_correct_attempt
					['0:00:00', u'10']
	part2_incorrect_attempt
					('0:02:47', u'50*6')
	part2_correct_attempt
					['0:05:16', u'15890700']

7 Student ID:hkhodada

	first_attempt
					2015-10-02 18:29:37
	part1_correct_attempt
					['0:00:00', u'10']
	part2_incorrect_attempt
					('0:03:28', u'52!')
	part2_correct_attempt
					['0:12:46', u'20358520']

8 Student ID:vasharma

	first_attempt
					2015-10-05 05:19:40
	part1_correct_attempt
					['0:00:00', u'10']
	part2_incorrect_attempt
					('0:00:48', u'54*53*52')
					('0:01:47', u'54!(54-6)!')
	part2_correct_attempt
					['0:02:06', u'54!/(6!(54-6)!)']

9 Student ID:acvuong

	first_attempt
					2015-10-04 00:07:17
	part1_correct_attempt
					['0:00:00', u'5!/(3!*2)']
	part2_incorrect_attempt
					('0:00:00', u'53*52*51*50*49*48')
	part2_correct_attempt
					['0:00:32', u'C(53,6)']

10 Student ID:any027

	first_attempt
					2015-10-03 10:43:32
	part1_correct_attempt
					['0:00:00', u'10']
	part2_incorrect_attempt
					('0:01:01', u' 50063860')
					('0:01:35', u'60! / (6 ! * 54!)')
	part2_correct_attempt
					['0:01:54', u'50! / (6 ! * 44!)']

11 Student ID:awollner

	first_attempt
					2015-10-02 14:36:59
	part1_correct_attempt
					['0:00:00', u'10']
	part2_incorrect_attempt
					('0:00:00', u'6*53')
	part2_correct_attempt
					['0:11:19', u'53!/(47!6!)']

12 Student ID:e9brown

	first_attempt
					2015-10-08 01:57:52
	part1_correct_attempt
					['0:00:00', u'10']
	part2_incorrect_attempt
					('0:00:00', u'(54!) - (48!)')
					('0:01:09', u'54 +53 + 52 +51+50+49')
					('0:01:24', u'53 + 52 +51+50+49')
					('0:02:37', u'54*53*52*51*50*49')
	part2_correct_attempt
					['0:06:27', u'C(54,6)']

13 Student ID:jcj006

	first_attempt
					2015-10-08 00:11:47
	part1_correct_attempt
					['0:00:00', u'4+3+2+1']
	part2_incorrect_attempt
					('0:00:00', u'54+53+52+51+50+49')
	part2_correct_attempt
					['0:02:46', u'25827165']

14 Student ID:b1green

	first_attempt
					2015-10-08 05:32:08
	part1_correct_attempt
					['0:00:00', u'C(5,2)']
	part2_incorrect_attempt
					('0:00:00', u'C(49,1)')
	part2_correct_attempt
					['0:00:08', u'C(49,6)']

15 Student ID:mbl003

	first_attempt
					2015-10-02 20:46:34
	part1_correct_attempt
					['0:00:00', u'10']
	part2_incorrect_attempt
					('0:00:42', u'55*54*53*52*51*50')
	part2_correct_attempt
					['0:01:23', u'28989675']

16 Student ID:agoldsht

	first_attempt
					2015-10-06 22:45:33
	part1_correct_attempt
					['0:00:00', u'10']
	part2_incorrect_attempt
					('0:00:27', u'48*6')
					('0:05:11', u'48*47*46*45*44*43')
	part2_correct_attempt
					['0:19:37', u'(48*47*46*45*44*43)/6!']

17 Student ID:n2patil

	first_attempt
					2015-10-06 15:40:55
	part1_correct_attempt
					['0:00:00', u'10']
	part2_incorrect_attempt
					('0:00:59', u'54*53*52*51*50*49')
	part2_correct_attempt
					['0:01:56', u'25827165']

18 Student ID:b3hwang

	first_attempt
					2015-10-08 23:23:40
	part1_correct_attempt
					['0:00:00', u'10']
	part2_incorrect_attempt
					('0:00:37', u'6*52')
	part2_correct_attempt
					['0:02:07', u'20358520']

19 Student ID:v4zhang

	first_attempt
					2015-10-08 07:49:12
	part1_correct_attempt
					['0:00:00', u'10']
	part2_incorrect_attempt
					('0:00:29', u'54*53*52*51*50*49')
					('0:01:03', u'55*54*53*52*51*50')
	part2_correct_attempt
					['0:02:19', u'(54!)/[6! * 48!]']

20 Student ID:vqt004

	first_attempt
					2015-10-04 17:45:21
	part1_correct_attempt
					['0:00:00', u'5*4/2']
	part2_incorrect_attempt
					('0:00:00', u'48*47*46*45*44*43')
	part2_correct_attempt
					['0:03:09', u' 48*47*46*45*44*43/6!']

21 Student ID:dcgriffi

	first_attempt
					2015-10-08 04:50:54
	part1_correct_attempt
					['0:00:00', u'(5!)/((2!)*(3!))']
	part2_incorrect_attempt
					('0:00:00', u'(49!)/(49!-6!)')
					('0:00:20', u'(49!)/((49-6)!)')
	part2_correct_attempt
					['0:02:21', u'(49!)/((6!)*(49-6)!)']

22 Student ID:dkostins

	first_attempt
					2015-10-05 20:53:34
	part1_correct_attempt
					['0:00:00', u'10']
	part2_incorrect_attempt
					('0:01:50', u'52+51+50+49+48+47')
					('0:02:23', u'52*51*50*49*48*47')
					('0:05:58', u'52!/((52-6)!-6!)')
	part2_correct_attempt
					['0:06:37', u'52!/((52-6)!(6!))']

23 Student ID:asrana

	first_attempt
					2015-10-03 03:45:18
	part1_correct_attempt
					['0:00:00', u'10']
	part2_incorrect_attempt
					('10:35:19', u'(50 6)')
	part2_correct_attempt
					['10:36:19', u'15890700']

24 Student ID:ctgraves

	first_attempt
					2015-10-08 08:37:29
	part1_correct_attempt
					['0:00:00', u'10']
	part2_incorrect_attempt
					('0:01:32', u'50!/(6!(50-6)!)')
	part2_correct_attempt
					['0:02:04', u'49!/(6!(49-6)!)']

25 Student ID:s6deng

	first_attempt
					2015-10-06 20:41:14
	part1_correct_attempt
					['0:00:00', u'5!/(3!2!)']
	part2_incorrect_attempt
					('0:00:53', u'5!/3!')
					('0:00:57', u'5!/2!')
					('0:02:08', u'50!/(44!6!)')
	part2_correct_attempt
					['0:05:06', u'49!/(43!6!)']

26 Student ID:dis003

	first_attempt
					2015-10-08 07:01:30
	part1_correct_attempt
					['0:00:00', u'C(5,2)']
	part2_incorrect_attempt
					('0:03:20', u'52*51*50*49*48*47')
	part2_correct_attempt
					['0:06:01', u'C(52,6)']

27 Student ID:thwan

	first_attempt
					2015-10-04 00:02:50
	part1_correct_attempt
					['0:00:00', u'C(5,2)']
	part2_incorrect_attempt
					('0:00:40', u'P(54,6)')
	part2_correct_attempt
					['0:00:47', u'C(54,6)']

28 Student ID:agarango

	first_attempt
					2015-10-08 06:23:39
	part1_correct_attempt
					['0:00:00', u'10']
	part2_incorrect_attempt
					('0:03:18', u'2.3352527*10^17')
	part2_correct_attempt
					['1:56:55', u'18009460']

29 Student ID:kew017

	first_attempt
					2015-10-04 19:33:32
	part1_correct_attempt
					['0:00:00', u'10']
	part2_incorrect_attempt
					('0:00:00', u'49!/(43!*6)')
	part2_correct_attempt
					['0:00:07', u'49!/(43!*6!)']

30 Student ID:q3wen

	first_attempt
					2015-10-07 07:15:29
	part1_correct_attempt
					['0:00:00', u'10']
	part2_incorrect_attempt
					('0:00:00', u'53^6')
	part2_correct_attempt
					['0:02:06', u'22957480']

31 Student ID:tcuddy

	first_attempt
					2015-10-02 19:45:44
	part1_correct_attempt
					['0:00:00', u'10']
	part2_incorrect_attempt
					('0:00:57', u'51*50*49*48*47*46')
					('0:03:06', u'(50!/(6!*44!))')
	part2_correct_attempt
					['0:03:43', u'(51!/(6!*45!))']

32 Student ID:cprafull

	first_attempt
					2015-10-06 19:08:10
	part1_correct_attempt
					['0:00:00', u'5*4/2']
	part2_incorrect_attempt
					('0:01:03', u'52*48*44*40*36*32')
					('0:01:10', u'52*48*44*40*36*32/2')
					('0:12:53', u'52*51*50*49*48*47')
	part2_correct_attempt
					['5:49:35', u'52!/(6!(46!))']

33 Student ID:ajabasa

	first_attempt
					2015-10-05 19:43:39
	part1_correct_attempt
					['0:00:00', u'5!/(3!2!)']
	part2_incorrect_attempt
					('1:14:05', u'52*51*50*49*48*47')
	part2_correct_attempt
					['1:15:31', u'52!/(6!*46!)']

34 Student ID:jel075

	first_attempt
					2015-10-06 16:34:02
	part1_correct_attempt
					['0:00:00', u'(5!)/(3!*2!)']
	part2_incorrect_attempt
					('0:03:49', u'54!/(54-6)!')
					('14:20:52', u'6*54*53*52*51*50*49')
					('14:20:58', u'6!*54*53*52*51*50*49')
	part2_correct_attempt
					['14:22:24', u'(54!)/(48!*6!)']

35 Student ID:sayao

	first_attempt
					2015-10-03 00:45:40
	part1_correct_attempt
					['0:00:00', u'5!/2!/3!']
	part2_incorrect_attempt
					('0:00:30', u'48!/(42!)')
	part2_correct_attempt
					['0:00:48', u'48!/(42!)/(6!)']

36 Student ID:nhn018

	first_attempt
					2015-10-07 02:52:16
	part1_correct_attempt
					['0:00:00', u'10']
	part2_incorrect_attempt
					('0:23:18', u'(50*49)/2')
					('0:25:46', u'(50*49)/2')
	part2_correct_attempt
					['0:27:09', u'50!/(44!(6!))']

37 Student ID:m4bui

	first_attempt
					2015-10-08 21:19:20
	part1_correct_attempt
					['0:00:00', u'10']
	part2_incorrect_attempt
					('0:00:41', u'55*54*53*52*51*50')
					('0:00:52', u'55*6')

38 Student ID:jjchung

	first_attempt
					2015-10-08 03:37:24
	part1_correct_attempt
					['0:00:00', u'10']
	part2_incorrect_attempt
					('0:00:47', u'51*50*49*48')
					('0:01:27', u'51*50*49*48*47*46')
					('0:25:53', u'(51*50*49*48*47*46)/2-1')
					('0:26:02', u'(51*50*49*48*47*46)/2+1')
	part2_correct_attempt
					['3:08:46', u'51!/(6! * 45!)']

39 Student ID:daw023

	first_attempt
					2015-10-03 08:05:16
	part1_correct_attempt
					['0:00:00', u'5!/(3!*2)']
	part2_incorrect_attempt
					('0:00:00', u'49!/(43!*6!)')
	part2_correct_attempt
					['0:00:44', u'48!/(42!*6!)']

40 Student ID:edcole

	first_attempt
					2015-10-04 21:47:07
	part1_correct_attempt
					['0:00:00', u'(5*4)/2']
	part2_incorrect_attempt
					('0:02:32', u'53! /(53-6)!')
	part2_correct_attempt
					['0:05:37', u'53! /(6! * ((53-6)!))']

41 Student ID:m4salaza

	first_attempt
					2015-10-07 03:14:09
	part1_correct_attempt
					['0:00:00', u'5*4/2']
	part2_incorrect_attempt
					('0:00:00', u'48*47/6')
	part2_correct_attempt
					['0:04:40', u'48!/(42!*6!)']

42 Student ID:xweng

	first_attempt
					2015-10-07 07:15:19
	part1_correct_attempt
					['0:00:00', u'10']
	part2_incorrect_attempt
					('0:00:19', u'50!-44!')
					('0:00:24', u'50!-45!')
					('0:00:49', u'49!-43!')
					('0:03:29', u'44+43+42+41+40+39+38')
					('0:03:35', u'44+43+42+41+40+39')
	part2_correct_attempt
					['0:10:54', u'50!/(6!44!)']

43 Student ID:yypan

	first_attempt
					2015-10-02 04:44:21
	part1_correct_attempt
					['0:00:00', u'5*4/2']
	part2_incorrect_attempt
					('0:01:24', u'50!/(45!)')
	part2_correct_attempt
					['0:01:58', u'50!/(44!*6!)']

44 Student ID:ajvanega

	first_attempt
					2015-10-02 18:08:03
	part1_correct_attempt
					['0:00:00', u'10']
	part2_incorrect_attempt
					('0:01:49', u'6*48')
	part2_correct_attempt
					['0:10:05', u'(48!)/((6!)*(42!))']

45 Student ID:jfalcone

	first_attempt
					2015-10-07 03:13:37
	part1_correct_attempt
					['0:00:00', u'(5 * 4)/2']
	part2_incorrect_attempt
					('0:05:11', u'(51!)/(51-6)!')
	part2_correct_attempt
					['0:06:15', u'(51!)/((51-6)!(6!))']

46 Student ID:small

	first_attempt
					2015-10-05 19:54:21
	part1_correct_attempt
					['0:00:00', u'10']
	part2_incorrect_attempt
					('3 days, 3:55:42', u'55*3*53*13*51')
	part2_correct_attempt
					['3 days, 3:55:59', u'55*3*53*5*13*51']

47 Student ID:ytc012

	first_attempt
					2015-10-06 08:35:24
	part1_correct_attempt
					['0:00:00', u'10']
	part2_incorrect_attempt
					('0:00:51', u'49!/43!')
	part2_correct_attempt
					['0:01:52', u'49!/(6!*43!)']

48 Student ID:mtrafeca

	first_attempt
					2015-10-02 04:31:20
	part1_correct_attempt
					['0:00:00', u'10']
	part2_incorrect_attempt
					('0:01:23', u'55*54*53*52*51*50')
					('1:02:54', u'(54*53*52*51*50*49)/(6)')
	part2_correct_attempt
					['1:12:26', u'(55!)/(49!*6!)']

49 Student ID:asp025

	first_attempt
					2015-10-08 06:10:06
	part1_correct_attempt
					['0:00:00', u'5!/(3!2!)']
	part2_incorrect_attempt
					('0:01:50', u'51!/((51-6)!)')
	part2_correct_attempt
					['0:08:07', u'51!/((51-6)!6!)']












