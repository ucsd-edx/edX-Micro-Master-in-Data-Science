#Problem 12

    $ns = random(4,6,1);
    $nr = random(10,16,1);
    $n = $ns*$nr;

    ## Probability of Poker Hands ##
    You are given a deck of cards with *[$ns] suites* and *[$nr] ranks*. A hand consists of 5 cards from this deck, and may fall into one of the categories. We are going to compute the probability of each category.

    First, the number of all possible hands is [_____]{Compute("C($n,5)")}.




## Part 1

### (32) Mistake Group ['R.1'] of size 32
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(78,5)	|C(52,5)	|[('R.1', 5.0, u'5', u'5')]	|
|1	|C(64,5)	|C(16,5)	|[('R.1', 5.0, u'5', u'5')]	|
|2	|C(78,5)	|C(65,5)	|[('R.1', 5.0, u'5', u'5')]	|
|3	|C(70,5)	|14^5 *5	|[('R.1', 5.0, u'5', u'5')]	|
|4	|C(70,5)	|14!/(5! *(14-5)!) * 5	|[('R.1', 5.0, u'5', u'5')]	|
|5	|C(75,5)	|C(15, 5)	|[('R.1', 5.0, u'5', u'5')]	|
|6	|C(75,5)	|15^5	|[('R.1', 5.0, u'5', u'5')]	|
|7	|C(75,5)	|C(60, 5)	|[('R.1', 5.0, u'5', u'5')]	|
|8	|C(75,5)	|C(52, 5)	|[('R.1', 5.0, u'5', u'5')]	|
|9	|C(75,5)	|C(13, 5)	|[('R.1', 5.0, u'5', u'5')]	|
|10	|C(90,5)	|C(21,5)	|[('R.1', 5.0, u'5', u'5')]	|
|11	|C(60,5)	|13*5	|[('R.1', 5.0, u'5', u'5')]	|
|12	|C(55,5)	|C(11,5)	|[('R.1', 5.0, u'5', u'5')]	|
|13	|C(60,5)	|C(6,5)	|[('R.1', 5.0, u'5', u'5')]	|
|14	|C(75,5)	|C(15,5)	|[('R.1', 5.0, u'5', u'5')]	|
|15	|C(75,5)	|(360360)^5	|[('R.1', 5.0, u'5', u'5')]	|
|16	|C(60,5)	|C(12,5)	|[('R.1', 5.0, u'5', u'5')]	|
|17	|C(80,5)	|16^5	|[('R.1', 5.0, u'5', u'5')]	|
|18	|C(44,5)	|C(11^4,5)	|[('R.1', 5.0, u'5', u'5')]	|




### (26) Mistake Group Digits of size 26




### (10) Mistake Group Fraction of size 10




### (7) Mistake Group ['R.0'] of size 7
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(56,5)	|C(56,4)	|[('R.0', 56.0, u'56', u'56')]	|
|1	|C(72,5)	|C(72,6)	|[('R.0', 72.0, u'72', u'72')]	|
|2	|C(60,5)	|(15*4)^4	|[('R.0', 60.0, u'60', u'15*4')]	|
|3	|C(65,5)	|C(13*5,4)	|[('R.0', 65.0, u'65', u'13*5')]	|
|4	|C(65,5)	|C(5*13,4)	|[('R.0', 65.0, u'65', u'5*13')]	|
|5	|C(65,5)	|C(65,4)	|[('R.0', 65.0, u'65', u'65')]	|
|6	|C(60,5)	|(5*12)!	|[('R.0', 60.0, u'60', u'5*12')]	|




### (6) Mistake Group ['R.0', 'R.1'] of size 6
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(40,5)	|40^5	|[('R.0', 40.0, u'40', u'40'), ('R.1', 5.0, u'5', u'5')]	|
|1	|C(60,5)	|60/5	|[('R.0', 60.0, u'60', u'60'), ('R.1', 5.0, u'5', u'5')]	|
|2	|C(60,5)	|60^5	|[('R.0', 60.0, u'60', u'60'), ('R.1', 5.0, u'5', u'5')]	|
|3	|C(60,5)	|60*5	|[('R.0', 60.0, u'60', u'60'), ('R.1', 5.0, u'5', u'5')]	|
|4	|C(75,5)	|(5*15)^5	|[('R.0', 75.0, u'75', u'5*15'), ('R.1', 5.0, u'5', u'5')]	|




### (56) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:h4tu

	first_attempt
					2015-10-15 07:13:31
	part1_incorrect_attempt
					('0:00:00', u'96!/91!5!')
	part1_correct_attempt
					['0:00:09', u'96!/(91!5!)']

1 Student ID:haw081

	first_attempt
					2015-10-11 00:17:24
	part1_incorrect_attempt
					('0:00:00', u'6*15')
	part1_correct_attempt
					['0:00:22', u'C(6*15,5)']

2 Student ID:lpettit

	first_attempt
					2015-10-14 20:22:25
	part1_incorrect_attempt
					('0:00:00', u'16!/(5!*11!)')
					('0:01:05', u'16!/11!')
	part1_correct_attempt
					['0:01:55', u'80!/(5!*75!)']

3 Student ID:b3hwang

	first_attempt
					2015-10-14 18:31:35
	part1_incorrect_attempt
					('0:00:00', u'65!/(65-5)*5!')
					('0:00:07', u'65!/((65-5)*5!)')
					('0:06:32', u'65*64*63*62*61')
					('0:07:07', u'65!/((65-5)*5!)')
	part1_correct_attempt
					['0:07:18', u'C(65,5)']

4 Student ID:lywong

	first_attempt
					2015-10-13 00:47:35
	part1_incorrect_attempt
					('0:00:00', u'66!(5!(61!))')
	part1_correct_attempt
					['0:00:04', u'66!/(5!(61!))']

5 Student ID:jjchung

	first_attempt
					2015-10-14 20:03:14
	part1_incorrect_attempt
					('0:00:00', u'55*54*53*52*51')
	part1_correct_attempt
					['0:00:12', u'C(55,5)']

6 Student ID:srl006

	first_attempt
					2015-10-10 05:52:41
	part1_incorrect_attempt
					('0:00:00', u'5^11')
	part1_correct_attempt
					['0:03:31', u'1086008']

7 Student ID:jguanzho

	first_attempt
					2015-10-09 20:09:36
	part1_incorrect_attempt
					('0:00:00', u'70!/65!')
	part1_correct_attempt
					['0:00:48', u'70!/(65!*5!)']

8 Student ID:qtluong

	first_attempt
					2015-10-12 20:17:18
	part1_incorrect_attempt
					('0:00:00', u'60!(5!(60-5)!)')
	part1_correct_attempt
					['0:00:06', u'60!/(5!(60-5)!)']

9 Student ID:spw006

	first_attempt
					2015-10-13 21:33:56
	part1_incorrect_attempt
					('0:00:00', u'50!/45!')
					('0:00:24', u'50!/45!5!')
	part1_correct_attempt
					['0:00:31', u'50!/(45!5!)']

10 Student ID:any027

	first_attempt
					2015-10-12 20:22:36
	part1_incorrect_attempt
					('0:00:00', u'16^6')
					('0:00:04', u'16*6')
	part1_correct_attempt
					['0:00:26', u'C(96,5)']

11 Student ID:thk002

	first_attempt
					2015-10-12 03:43:55
	part1_incorrect_attempt
					('0:00:00', u'14*6')
	part1_correct_attempt
					['0:00:09', u'C(84,5)']

12 Student ID:s1powers

	first_attempt
					2015-10-11 00:16:07
	part1_incorrect_attempt
					('0:00:00', u'60*59*58*57*56')
	part1_correct_attempt
					['0:00:33', u'60!/((60-5)!*5!)']

13 Student ID:r1gu

	first_attempt
					2015-10-15 12:21:43
	part1_incorrect_attempt
					('0:00:00', u'55!(5!50!)')
	part1_correct_attempt
					['0:00:05', u'55!/(5!50!)']

14 Student ID:mrchin

	first_attempt
					2015-10-14 19:19:28
	part1_incorrect_attempt
					('0:00:00', u'40*39*38*37*36')
					('0:02:08', u'40*39*38*37*36')
	part1_correct_attempt
					['3:14:43', u'40!/(5!*35!)']

15 Student ID:dlt009

	first_attempt
					2015-10-14 01:55:59
	part1_incorrect_attempt
					('0:00:00', u'5*[(15!/[(15-5)!5!])]')
					('0:00:51', u'[(15!/[(15-5)!5!])]')
	part1_correct_attempt
					['0:02:42', u'75!/[(75-5)!5!]']

16 Student ID:ttimmons

	first_attempt
					2015-10-12 18:59:40
	part1_incorrect_attempt
					('0:00:00', u'5*15')
	part1_correct_attempt
					['0:00:12', u'C(5*15,5)']

17 Student ID:kquong

	first_attempt
					2015-10-11 05:02:45
	part1_incorrect_attempt
					('0:00:00', u'14!/(5! *(14-5)!)')
	part1_correct_attempt
					['0:01:01', u'70!/(5! *(70-5)!)']

18 Student ID:dcgriffi

	first_attempt
					2015-10-14 07:23:43
	part1_incorrect_attempt
					('0:00:00', u'(16*5)!/(16*5-5)!')
	part1_correct_attempt
					['0:00:31', u'(16*5)!/((16*5-5)!*5!)']

19 Student ID:rsmurlo

	first_attempt
					2015-10-13 17:44:01
	part1_incorrect_attempt
					('0:00:00', u'96*95*94*93*92')
	part1_correct_attempt
					['0:02:29', u'96!/(91!5!)']

20 Student ID:jeqin

	first_attempt
					2015-10-15 12:44:15
	part1_incorrect_attempt
					('0:00:00', u'96!/(5!/91!)')
	part1_correct_attempt
					['0:01:00', u'96!/(5!91!)']

21 Student ID:hak014

	first_attempt
					2015-10-13 05:20:15
	part1_incorrect_attempt
					('0:00:00', u'40*39*38*37*36')
	part1_correct_attempt
					['0:01:38', u'40!/(35!5!)']

22 Student ID:jnatale

	first_attempt
					2015-10-13 01:34:18
	part1_incorrect_attempt
					('0:00:00', u'C(52,6)')
	part1_correct_attempt
					['0:00:13', u'C(48,5)']

23 Student ID:agian

	first_attempt
					2015-10-15 07:28:54
	part1_incorrect_attempt
					('0:00:00', u'C(78,4)')
					('0:00:20', u'C(78,4)')
	part1_correct_attempt
					['0:01:27', u'C(65,5)']

24 Student ID:dgunawan

	first_attempt
					2015-10-15 19:06:32
	part1_incorrect_attempt
					('0:00:00', u'C(13,1)*C(4,1)^5')
					('0:00:05', u'C(11,1)*C(4,1)^5')
	part1_correct_attempt
					['0:00:34', u'C(44,5)']

25 Student ID:kew017

	first_attempt
					2015-10-15 18:20:30
	part1_incorrect_attempt
					('0:00:00', u'45!/(5!40!)')
	part1_correct_attempt
					['0:00:24', u'75!/(5!70!)']

26 Student ID:wcwhite

	first_attempt
					2015-10-15 22:11:14
	part1_incorrect_attempt
					('0:00:00', u'44*43*42*41*40')
					('0:01:07', u'(11^4)(11^4-1)(11^4-2)(11^4-3)')
					('0:01:47', u'(11^4-4)(11^4)(11^4-1)(11^4-2)(11^4-3)')
	part1_correct_attempt
					['0:10:33', u'C(11*4, 5)']

27 Student ID:hah008

	first_attempt
					2015-10-13 06:32:32
	part1_incorrect_attempt
					('0:00:00', u'6*10')
					('0:02:11', u'6^10')
	part1_correct_attempt
					['0:03:10', u'C(60, 5)']

28 Student ID:cprafull

	first_attempt
					2015-10-14 08:26:04
	part1_incorrect_attempt
					('0:00:00', u'52!/((47!)(5!))')
	part1_correct_attempt
					['0:00:50', u'84!/((5!)(79!))']

29 Student ID:l8ngo

	first_attempt
					2015-10-12 16:04:33
	part1_incorrect_attempt
					('0:00:00', u'52!/[5!47!]')
	part1_correct_attempt
					['0:01:37', u'56!/[5!51!]']

30 Student ID:ajabasa

	first_attempt
					2015-10-14 07:05:31
	part1_incorrect_attempt
					('0:00:00', u'52!/(6!*46!)')
	part1_correct_attempt
					['0:00:22', u'52!/(5!*47!)']

31 Student ID:djk006

	first_attempt
					2015-10-11 02:46:57
	part1_incorrect_attempt
					('0:00:00', u'56*55*54*53*52')
	part1_correct_attempt
					['0:00:14', u'56*55*54*53*52/5!']

32 Student ID:ytc012

	first_attempt
					2015-10-15 09:00:58
	part1_incorrect_attempt
					('0:00:00', u'90*89*88*87*86')
	part1_correct_attempt
					['0:01:06', u'90!/(5!85!)']

33 Student ID:aadhakal

	first_attempt
					2015-10-12 22:17:03
	part1_incorrect_attempt
					('0:00:00', u'84!(5!*(84-5)!)')
	part1_correct_attempt
					['0:00:12', u'84!/(5!*(84-5)!)']

34 Student ID:eyhu

	first_attempt
					2015-10-09 03:01:03
	part1_incorrect_attempt
					('0:00:00', u'6*15')
	part1_correct_attempt
					['0:00:31', u'(6*15)!/(((6*15)-5)!*5!)']

35 Student ID:sayao

	first_attempt
					2015-10-12 16:13:41
	part1_incorrect_attempt
					('0:00:00', u'(4*16)!/(52-5)!/5!')
	part1_correct_attempt
					['0:00:19', u'(4*16)!/(64-5)!/5!']

36 Student ID:anvan

	first_attempt
					2015-10-15 00:55:14
	part1_incorrect_attempt
					('0:00:00', u'14!/(9!5!)')
					('0:04:14', u'5(14*13*12*11*10)')
					('0:04:28', u'5(14! / 5! 9!)')
					('0:04:44', u'5 * 14! / (5! 9!)')
					('0:21:32', u'5*(14!4!10!)')
					('0:21:38', u'5*(14!/4!10!)')
					('0:21:47', u'5*14!/(4!10!)')
	part1_correct_attempt
					['0:22:55', u'70! / (65!5!)']

37 Student ID:smohiman

	first_attempt
					2015-10-11 22:21:22
	part1_incorrect_attempt
					('0:00:00', u'16*6')
	part1_correct_attempt
					['0:00:36', u'C(96,5)']

38 Student ID:m4bui

	first_attempt
					2015-10-15 18:56:20
	part1_incorrect_attempt
					('0:00:00', u'66*65*64*63*62')
	part1_correct_attempt
					['0:01:04', u'(66!/61!)/5!']

39 Student ID:ppanourg

	first_attempt
					2015-10-15 00:13:28
	part1_incorrect_attempt
					('0:00:00', u'40*39*38*37')
					('0:00:34', u'40*39*38*37*36')
					('0:03:19', u'14*13*12*11*10')
					('0:00:00', u'4*(10!/5!)')
					('0:03:12', u'40*39*38*37*36')
					('0:00:00', u'40*39*38*37')
	part1_correct_attempt
					['6:47:07', u'(40*39*38*37*36)/(5!)']

40 Student ID:dtea

	first_attempt
					2015-10-15 23:37:29
	part1_incorrect_attempt
					('0:00:00', u'5*14')
	part1_correct_attempt
					['0:00:19', u'C(70,5)']

41 Student ID:cstringh

	first_attempt
					2015-10-12 22:37:16
	part1_incorrect_attempt
					('0:00:00', u'5^15')
					('0:02:20', u'60!')
					('0:03:50', u'C(60, 4)')
					('0:35:20', u'60*59*58*57*56*55')
					('0:35:28', u'60*59*58*57*56')
	part1_correct_attempt
					['0:37:01', u'C(75, 5)']

42 Student ID:csl030

	first_attempt
					2015-10-14 02:03:58
	part1_incorrect_attempt
					('0:00:00', u'78 * 77 * 76 * 75 * 74')
	part1_correct_attempt
					['0:01:57', u'C(78, 5)']

43 Student ID:w4shin

	first_attempt
					2015-10-14 03:14:46
	part1_incorrect_attempt
					('0:00:00', u'70!(65!5!)')
	part1_correct_attempt
					['0:00:04', u'70!/(65!5!)']

44 Student ID:asp025

	first_attempt
					2015-10-13 06:57:54
	part1_incorrect_attempt
					('0:00:00', u'21!/(21-5)!5!')
					('0:00:39', u'21!/((21-5)!5!)')
	part1_correct_attempt
					['2 days, 0:31:58', u'90!/(5!(90-5)!)']

45 Student ID:mitopete

	first_attempt
					2015-10-13 20:48:03
	part1_incorrect_attempt
					('0:00:00', u'4!11!')
	part1_correct_attempt
					['0:00:48', u'44!/(5!39!)']

46 Student ID:r2fisher

	first_attempt
					2015-10-14 23:16:19
	part1_incorrect_attempt
					('0:00:00', u'6^10')
					('0:00:06', u'10^6')
					('0:00:21', u'10!/(6!*4!)')
	part1_correct_attempt
					['0:00:42', u'60!/(5!*55!)']

47 Student ID:dcastlem

	first_attempt
					2015-10-15 03:33:04
	part1_incorrect_attempt
					('0:00:00', u'5^16')
	part1_correct_attempt
					['0:01:07', u'80!/((5!)(75!))']

48 Student ID:bkoli

	first_attempt
					2015-10-15 19:16:09
	part1_incorrect_attempt
					('0:00:00', u'50!/(2!48!)')
	part1_correct_attempt
					['0:00:24', u'50!/(5!45!)']

49 Student ID:hsc052

	first_attempt
					2015-10-15 05:43:06
	part1_incorrect_attempt
					('0:00:00', u'5*10')
	part1_correct_attempt
					['0:00:32', u'C(50,5)']

50 Student ID:abjara

	first_attempt
					2015-10-14 21:07:34
	part1_incorrect_attempt
					('0:00:00', u'44!/(39!)')
	part1_correct_attempt
					['0:00:20', u'44!/(5!*39!)']

51 Student ID:zig006

	first_attempt
					2015-10-12 23:22:34
	part1_incorrect_attempt
					('0:00:00', u'80!/76!')
					('0:00:06', u'80!/75!')
					('0:00:23', u'80*79*78*77*76')
	part1_correct_attempt
					['0:02:00', u'80!/(5!*75!)']

52 Student ID:aurodrig

	first_attempt
					2015-10-15 20:09:40
	part1_incorrect_attempt
					('0:00:00', u'C(52,4)*C(12,5)')
					('0:11:41', u'48!/5!43!')
	part1_correct_attempt
					['0:12:27', u'48!/(5!43!)']

53 Student ID:hmnaing

	first_attempt
					2015-10-13 00:41:13
	part1_incorrect_attempt
					('0:00:00', u'C(5*14, 1)')
	part1_correct_attempt
					['0:00:14', u'C(5*14, 5)']

54 Student ID:sghouse

	first_attempt
					2015-10-12 19:31:29
	part1_incorrect_attempt
					('0:00:00', u'78*77*76*75*74')
	part1_correct_attempt
					['0:01:08', u'78!/(5!*(73!))']

55 Student ID:arvenega

	first_attempt
					2015-10-14 20:48:30
	part1_incorrect_attempt
					('0:00:00', u'4^10')
					('0:00:08', u'10^4')
	part1_correct_attempt
					['0:01:09', u'(40!)/((5!)*(35!))']












