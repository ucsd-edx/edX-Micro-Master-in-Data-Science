#Problem 11

    $nCards=random(4,7,1);
    $b=random(2,$nCards-1,1);
    $nSame = Compute("C(13,$b)");
    $nTotal = Compute("C(52,$nCards)");
    $nOther = Compute("C(39,$nCards-$b)");
    $nEvent = Compute("$nSame * $nOther");
    $ans = Compute("4*C(13,$b)*C(39,$nCards-$b)/C(52,$nCards)");

    ## Probability of cards of the same suite ##
    A poker hand consisting of [$nCards] cards is dealt from a standard deck of 52 cards.
    Find the probability that the hand contains exactly [$b] cards of the same suite. It is allowed to have any number of cards in other suites.

    First, we know the number of all possible hands of [$nCards] cards is [______]{$nTotal}.

    Then, we calculate the number of hands that contain exactly [$b] cards of the same suite.

    	We first choose which suite the [$b] cards is. Obviously, there are [______]{4} possibilities.

    	The number of possibilities for the ranks of these cards is [_______]{$nSame}.

    	The other [$nCards-$b] cards in the hand can be any cards that has a different suite than the [$b] cards. There are a total of [______]{52-13} such cards. To choose [$nCards-$b] from them, there are [________]{$nOther} possibilities.

    	Thus we can compute the number of hands that have exactly [$b] cards of the same suite, which is [______]{Compute("4*C(13,$b)*C(39,$nCards-$b)")}.

    Finally we can calculate the probability of such hands, by calculating th ratio of the number of such hands to the number of all hands. This is [_______]{$ans}





## Part 1

### (46) Mistake Group Digits of size 46




### (32) Mistake Group ['R.0', 'R.1'] of size 32
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(52,6)	|52**6	|[('R.0', 52.0, u'52', u'52'), ('R.1', 6.0, u'6', u'6')]	|
|1	|C(52,6)	|52^6	|[('R.0', 52.0, u'52', u'52'), ('R.1', 6.0, u'6', u'6')]	|
|2	|C(52,4)	|P(52,4)	|[('R.0', 52.0, u'52', u'52'), ('R.1', 4.0, u'4', u'4')]	|
|3	|C(52,6)	|P(52,6)	|[('R.0', 52.0, u'52', u'52'), ('R.1', 6.0, u'6', u'6')]	|
|4	|C(52,5)	|52^5	|[('R.0', 52.0, u'52', u'52'), ('R.1', 5.0, u'5', u'5')]	|
|5	|C(52,7)	|P(52,7)	|[('R.0', 52.0, u'52', u'52'), ('R.1', 7.0, u'7', u'7')]	|
|6	|C(52,4)	|52^4	|[('R.0', 52.0, u'52', u'52'), ('R.1', 4.0, u'4', u'4')]	|
|7	|C(52,7)	|52^7	|[('R.0', 52.0, u'52', u'52'), ('R.1', 7.0, u'7', u'7')]	|
|8	|C(52,5)	|52*5	|[('R.0', 52.0, u'52', u'52'), ('R.1', 5.0, u'5', u'5')]	|
|9	|C(52,6)	|52*6	|[('R.0', 52.0, u'52', u'52'), ('R.1', 6.0, u'6', u'6')]	|
|10	|C(52,7)	|52**7	|[('R.0', 52.0, u'52', u'52'), ('R.1', 7.0, u'7', u'7')]	|




### (15) Mistake Group Fraction of size 15




### (5) Mistake Group ['R.1'] of size 5
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(52,5)	|13^5	|[('R.1', 5.0, u'5', u'5')]	|
|1	|C(52,4)	|13^4	|[('R.1', 4.0, u'4', u'4')]	|
|2	|C(52,4)	|52*51*50*49/4	|[('R.1', 4.0, u'4', u'4')]	|




### (4) Mistake Group ['R.0'] of size 4
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(52,7)	|52!	|[('R.0', 52.0, u'52', u'52')]	|
|1	|C(52,5)	|C(52, 6) 	|[('R.0', 52.0, u'52', u'52')]	|
|2	|C(52,6)	|C(52,7)	|[('R.0', 52.0, u'52', u'52')]	|
|3	|C(52,6)	|C(52,5)	|[('R.0', 52.0, u'52', u'52')]	|




### (90) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:apokhare

	first_attempt
					2015-10-12 20:50:35
	part1_incorrect_attempt
					('0:00:00', u'52!/(52-6)!')
					('0:00:14', u'52!/6!(52-6)!')
	part1_correct_attempt
					['0:14:36', u'52!/(6!*(52-6)!)']

1 Student ID:ssamudra

	first_attempt
					2015-10-15 03:32:38
	part1_incorrect_attempt
					('0:00:00', u'5!')
	part1_correct_attempt
					['0:43:53', u'52!/(47!5!)']

2 Student ID:dcgriffi

	first_attempt
					2015-10-14 07:18:48
	part1_incorrect_attempt
					('0:00:00', u'52!/(52-7)!')
	part1_correct_attempt
					['0:02:19', u'52!/(7!(52-7)!)']

3 Student ID:mhale

	first_attempt
					2015-10-14 21:58:38
	part1_incorrect_attempt
					('0:00:00', u'52! / 46!')
					('0:00:21', u'52 * 51 * 50 * 49 * 48 * 47')
	part1_correct_attempt
					['0:00:46', u'20358520']

4 Student ID:l5han

	first_attempt
					2015-10-14 04:42:01
	part1_incorrect_attempt
					('0:00:00', u'52!/46!')
	part1_correct_attempt
					['0:02:15', u'C(52,6)']

5 Student ID:dan029

	first_attempt
					2015-10-09 22:54:35
	part1_incorrect_attempt
					('0:00:00', u'52*51*50*49*48*47*46')
	part1_correct_attempt
					['0:01:58', u'C(52,7)']

6 Student ID:jew037

	first_attempt
					2015-10-14 04:17:59
	part1_incorrect_attempt
					('0:00:00', u'7^52')
	part1_correct_attempt
					['0:00:46', u'C(52,7)']

7 Student ID:rsmurlo

	first_attempt
					2015-10-13 17:29:21
	part1_incorrect_attempt
					('0:00:00', u'52*51*50*49')
	part1_correct_attempt
					['0:18:41', u'52!/(48!4!)']

8 Student ID:asrana

	first_attempt
					2015-10-15 11:11:34
	part1_incorrect_attempt
					('0:00:00', u'52*51*50*49')
	part1_correct_attempt
					['0:03:59', u'270725']

9 Student ID:jmmcalex

	first_attempt
					2015-10-15 08:20:51
	part1_incorrect_attempt
					('0:00:00', u'52!/4!')
					('0:00:22', u'52!/[48!]')
					('0:03:25', u'52!/[48!]4!')
	part1_correct_attempt
					['0:03:35', u'52!/[4!48!]']

10 Student ID:dgunawan

	first_attempt
					2015-10-14 20:43:53
	part1_incorrect_attempt
					('0:00:00', u'52 * 51 * 50 * 49')
	part1_correct_attempt
					['0:09:41', u'270725']

11 Student ID:tstevens

	first_attempt
					2015-10-10 10:35:37
	part1_incorrect_attempt
					('0:00:00', u'52*51*50*49*48')
	part1_correct_attempt
					['0:01:19', u'2598960']

12 Student ID:djk006

	first_attempt
					2015-10-11 02:25:02
	part1_incorrect_attempt
					('0:00:00', u'52*51*50*49*48*47')
	part1_correct_attempt
					['0:03:08', u'52!/(6!46!)']

13 Student ID:dsriniva

	first_attempt
					2015-10-15 19:56:13
	part1_incorrect_attempt
					('0:00:00', u'52*51*50*49*48')
	part1_correct_attempt
					['0:01:09', u'2598960']

14 Student ID:abasu

	first_attempt
					2015-10-11 02:13:06
	part1_incorrect_attempt
					('0:00:00', u'5*4*3*2*1')
					('0:00:13', u'52!/48!')
					('0:00:33', u'52*51*50*49')
					('0:01:24', u'52*51*50*49*48')
					('0:02:08', u'52!/47!')
					('0:03:20', u'52!/47!')
	part1_correct_attempt
					['0:03:59', u'C(52,5)']

15 Student ID:m4bui

	first_attempt
					2015-10-15 22:05:10
	part1_incorrect_attempt
					('0:00:00', u'52!/46!')
					('0:00:36', u'52*51*50*49*48*47')
					('0:01:27', u'52*51*50*49')
					('0:01:46', u'52*51*50*49*48*47')
	part1_correct_attempt
					['0:15:57', u'C(52,6)']

16 Student ID:seleon

	first_attempt
					2015-10-15 06:05:32
	part1_incorrect_attempt
					('0:00:00', u'52!/(52-5)!')
					('0:00:11', u'52!/5!(52-5)!')
	part1_correct_attempt
					['0:00:19', u'52!/(5!(52-5)!)']

17 Student ID:arc013

	first_attempt
					2015-10-14 03:21:47
	part1_incorrect_attempt
					('0:00:00', u'52!/47!')
					('0:00:25', u'52!/(52-5)!')
	part1_correct_attempt
					['0:09:02', u'C(52, 5) ']

18 Student ID:starinia

	first_attempt
					2015-10-15 01:28:25
	part1_incorrect_attempt
					('0:00:00', u'52!/4!')
					('0:02:22', u'52 * 51 * 50 * 49')
	part1_correct_attempt
					['0:14:03', u'52!/(4!48!)']

19 Student ID:jguanzho

	first_attempt
					2015-10-09 20:08:31
	part1_incorrect_attempt
					('0:00:00', u'52!/(46!)')
	part1_correct_attempt
					['0:03:31', u'52!/(46! * 6!)']

20 Student ID:ggaddi

	first_attempt
					2015-10-13 18:17:47
	part1_incorrect_attempt
					('0:00:00', u'52!/48!')
	part1_correct_attempt
					['0:05:30', u'52!/(48!*4!)']

21 Student ID:h4tu

	first_attempt
					2015-10-15 06:55:49
	part1_incorrect_attempt
					('0:00:00', u'52!/45!')
					('0:01:03', u'52!/45!7!')
	part1_correct_attempt
					['0:01:10', u'52!/(45!7!)']

22 Student ID:jag028

	first_attempt
					2015-10-15 00:55:07
	part1_incorrect_attempt
					('0:00:00', u'6!')
	part1_correct_attempt
					['0:00:23', u'C(52,6)']

23 Student ID:jjchung

	first_attempt
					2015-10-14 19:51:30
	part1_incorrect_attempt
					('0:00:00', u'52*51*50*49')
					('0:00:56', u'52!/48!')
	part1_correct_attempt
					['0:01:06', u'C(52,4)']

24 Student ID:atorr

	first_attempt
					2015-10-11 01:30:03
	part1_incorrect_attempt
					('0:00:00', u'52!/47!')
	part1_correct_attempt
					['0:00:23', u'52!/(47!5!)']

25 Student ID:cprafull

	first_attempt
					2015-10-14 07:13:56
	part1_incorrect_attempt
					('0:00:00', u'52*51*50*49')
					('0:03:22', u'4^52')
					('0:03:34', u'52*51*50*49')
					('0:00:00', u'52!/(48!)(4!)')
	part1_correct_attempt
					['1:07:32', u'52!/((48!)(4!))']

26 Student ID:krau

	first_attempt
					2015-10-14 03:51:35
	part1_incorrect_attempt
					('0:00:00', u'52!/4!/48')
	part1_correct_attempt
					['0:00:12', u'52!/4!/48!']

27 Student ID:mroknich

	first_attempt
					2015-10-14 00:29:10
	part1_incorrect_attempt
					('0:00:00', u'52*51*50*49*48')
	part1_correct_attempt
					['0:00:36', u'C(52,5)']

28 Student ID:jic212

	first_attempt
					2015-10-12 08:21:42
	part1_incorrect_attempt
					('0:00:00', u'52*51*50*49')
	part1_correct_attempt
					['0:06:07', u'C(52,4)']

29 Student ID:hak014

	first_attempt
					2015-10-13 05:08:27
	part1_incorrect_attempt
					('0:00:00', u'52!/48!')
	part1_correct_attempt
					['0:03:05', u'52!/(6!46!)']

30 Student ID:mrchin

	first_attempt
					2015-10-12 03:34:34
	part1_incorrect_attempt
					('0:00:00', u'52*51*50*49')
	part1_correct_attempt
					['0:01:09', u'52!/(48!*4!)']

31 Student ID:dis003

	first_attempt
					2015-10-15 11:10:09
	part1_incorrect_attempt
					('0:00:00', u'52*51*50*49*48*47*56*45')
					('0:00:12', u'52*51*50*49*48*47*56')
	part1_correct_attempt
					['0:00:28', u'C(52,7)']

32 Student ID:r1gu

	first_attempt
					2015-10-15 12:13:46
	part1_incorrect_attempt
					('0:00:00', u'52*51*50*49*48')
	part1_correct_attempt
					['0:01:37', u'(52!)/(5!47!)']

33 Student ID:dsmonaha

	first_attempt
					2015-10-13 17:52:10
	part1_incorrect_attempt
					('0:00:00', u'5^52')
	part1_correct_attempt
					['0:01:59', u'C(52,5)']

34 Student ID:jel075

	first_attempt
					2015-10-15 01:09:53
	part1_incorrect_attempt
					('0:00:00', u'52*51*50*49')
	part1_correct_attempt
					['0:01:50', u'52!/(48!*4!)']

35 Student ID:bakang

	first_attempt
					2015-10-15 02:08:40
	part1_incorrect_attempt
					('0:00:00', u'52!/(52-7)!')
					('0:00:38', u'52!/45!')
	part1_correct_attempt
					['0:01:11', u'C(52,7)']

36 Student ID:wcwhite

	first_attempt
					2015-10-14 02:19:33
	part1_incorrect_attempt
					('0:00:00', u'5!')
	part1_correct_attempt
					['1 day, 19:29:21', u'C(52,6)']

37 Student ID:cstringh

	first_attempt
					2015-10-12 22:18:56
	part1_incorrect_attempt
					('0:00:00', u'52!/(4!(38!))')
	part1_correct_attempt
					['0:03:16', u'52!/(4!(48!))']

38 Student ID:v4sharma

	first_attempt
					2015-10-14 01:26:17
	part1_incorrect_attempt
					('0:00:00', u'4^13')
					('0:00:58', u'4*13')
	part1_correct_attempt
					['0:02:41', u'C(52, 4)']

39 Student ID:yjshin

	first_attempt
					2015-10-14 09:52:50
	part1_incorrect_attempt
					('0:00:00', u'52!/45!')
	part1_correct_attempt
					['0:03:59', u'52!/(45!7!)']

40 Student ID:ajabasa

	first_attempt
					2015-10-14 06:49:25
	part1_incorrect_attempt
					('0:00:00', u'52!/46!')
	part1_correct_attempt
					['0:00:44', u'52!/(6!*46!)']

41 Student ID:bkoli

	first_attempt
					2015-10-15 06:57:44
	part1_incorrect_attempt
					('0:00:00', u'52!/46!')
	part1_correct_attempt
					['0:20:38', u'52!/(46!6!)']

42 Student ID:xil109

	first_attempt
					2015-10-10 20:30:52
	part1_incorrect_attempt
					('0:00:00', u'52!/(52-4)!')
					('0:00:19', u'52*51*50*49')
	part1_correct_attempt
					['0:01:41', u'C(52,4)']

43 Student ID:dac064

	first_attempt
					2015-10-15 20:17:19
	part1_incorrect_attempt
					('0:00:00', u'52!/((52-5)!)')
					('0:00:16', u'52*51*50*49*48')
	part1_correct_attempt
					['0:00:33', u'C(52,5)']

44 Student ID:lywong

	first_attempt
					2015-10-13 00:25:11
	part1_incorrect_attempt
					('0:00:00', u'52!/((52-4)!)')
	part1_correct_attempt
					['0:03:06', u'52!/(4!(52-4)!)']

45 Student ID:kebao

	first_attempt
					2015-10-15 05:11:49
	part1_incorrect_attempt
					('0:00:00', u'52*51*50*49*48')
					('0:01:42', u'52!/47!')
	part1_correct_attempt
					['0:01:53', u'52!/(47!*5!)']

46 Student ID:glcohen

	first_attempt
					2015-10-13 05:43:47
	part1_incorrect_attempt
					('0:00:00', u'52*51*50*49')
					('0:00:06', u'52*51*50*49*48')
	part1_correct_attempt
					['0:00:31', u'(52!)/(47!5!)']

47 Student ID:d6he

	first_attempt
					2015-10-15 06:14:29
	part1_incorrect_attempt
					('0:00:00', u'52*51*50')
					('0:00:41', u'52*51*50*49*48')
					('0:03:25', u'52*51*50*49*48')
	part1_correct_attempt
					['0:10:46', u'52!/(5!47!)']

48 Student ID:t2li

	first_attempt
					2015-10-14 06:34:34
	part1_incorrect_attempt
					('0:00:00', u'52!/(52-7)!')
					('0:00:28', u'52*51*50*49*48*47*46')
					('0:00:37', u'52*51*50*49*48')
	part1_correct_attempt
					['0:02:15', u'C(52,7)']

49 Student ID:dlt009

	first_attempt
					2015-10-14 01:43:57
	part1_incorrect_attempt
					('0:00:00', u'52*51*50*49*48')
	part1_correct_attempt
					['0:10:19', u'52!/[(52-5)!5!]']

50 Student ID:mbl003

	first_attempt
					2015-10-15 07:10:01
	part1_incorrect_attempt
					('0:00:00', u'52*51*50*49')
	part1_correct_attempt
					['0:01:02', u'52!/(4!*48!)']

51 Student ID:n2patil

	first_attempt
					2015-10-13 16:30:32
	part1_incorrect_attempt
					('0:00:00', u'52*51*50*49*48*47*46*45')
					('0:00:12', u'52*51*50*49*48*47*46')
	part1_correct_attempt
					['0:01:50', u'133784560']

52 Student ID:ksmurlo

	first_attempt
					2015-10-13 23:18:58
	part1_incorrect_attempt
					('0:00:00', u'52*51*50*49')
	part1_correct_attempt
					['0:00:19', u'C(52,4)']

53 Student ID:jeqin

	first_attempt
					2015-10-15 12:37:29
	part1_incorrect_attempt
					('0:00:00', u'52!/46!')
					('0:00:26', u'52*51*50*49*48*47')
	part1_correct_attempt
					['0:01:54', u'52!/(6!46!)']

54 Student ID:jnatale

	first_attempt
					2015-10-13 01:16:22
	part1_incorrect_attempt
					('0:00:00', u'52*51*50*49*48*47')
	part1_correct_attempt
					['0:00:28', u'C(52,6)']

55 Student ID:akhmelni

	first_attempt
					2015-10-15 22:46:32
	part1_incorrect_attempt
					('0:00:00', u'(52!)/(52-7)!')
	part1_correct_attempt
					['0:01:39', u'C(52,7)']

56 Student ID:skodigal

	first_attempt
					2015-10-15 01:02:29
	part1_incorrect_attempt
					('0:00:00', u'7^52')
					('0:00:58', u'52*51*50*49*48*47*46')
	part1_correct_attempt
					['0:01:51', u'C(52,7)']

57 Student ID:yeh013

	first_attempt
					2015-10-15 07:33:40
	part1_incorrect_attempt
					('0:00:00', u'52!/48!')
	part1_correct_attempt
					['0:02:03', u'52!/(48!*4!)']

58 Student ID:jtfrankl

	first_attempt
					2015-10-15 20:58:31
	part1_incorrect_attempt
					('0:00:00', u'52!/48!')
					('0:00:34', u'52*51*50*49')
					('0:02:14', u'52!/48!')
	part1_correct_attempt
					['0:04:45', u'52!/(48!4!)']

59 Student ID:kmc012

	first_attempt
					2015-10-15 01:10:36
	part1_incorrect_attempt
					('0:00:00', u'(52!)/((52-7)!)')
	part1_correct_attempt
					['0:00:28', u'(52!)/((7!)*((52-7)!))']

60 Student ID:eaherman

	first_attempt
					2015-10-14 02:46:12
	part1_incorrect_attempt
					('0:00:00', u'52!/(52-4)!')
	part1_correct_attempt
					['0:00:27', u'C(52,4)']

61 Student ID:cagatep

	first_attempt
					2015-10-14 04:57:50
	part1_incorrect_attempt
					('0:00:00', u'52*51*50*49*48')
	part1_correct_attempt
					['0:01:48', u'C(52, 5)']

62 Student ID:r2fisher

	first_attempt
					2015-10-14 23:08:33
	part1_incorrect_attempt
					('0:00:00', u'6^52')
	part1_correct_attempt
					['0:00:30', u'52!/(6!*46!)']

63 Student ID:ewbrenna

	first_attempt
					2015-10-12 20:07:00
	part1_incorrect_attempt
					('0:00:00', u'52*51*50*49*48')
	part1_correct_attempt
					['0:00:47', u'2598960']

64 Student ID:spw006

	first_attempt
					2015-10-13 21:19:59
	part1_incorrect_attempt
					('0:00:00', u'7!')
					('0:00:20', u'52!/7!')
					('0:00:29', u'52!/45!')
	part1_correct_attempt
					['0:00:57', u'52!/(45!7!)']

65 Student ID:any027

	first_attempt
					2015-10-09 09:45:16
	part1_incorrect_attempt
					('0:00:00', u'13 * 4')
	part1_correct_attempt
					['0:01:29', u'2598960']

66 Student ID:jdeon

	first_attempt
					2015-10-11 19:35:59
	part1_incorrect_attempt
					('0:00:00', u'52*51*50*49')
	part1_correct_attempt
					['0:00:18', u'C(52,4)']

67 Student ID:p4kumar

	first_attempt
					2015-10-15 08:54:11
	part1_incorrect_attempt
					('0:00:00', u'52!/(52-4)!')
					('0:00:22', u'52*51*50*49')
	part1_correct_attempt
					['0:03:29', u'270725']

68 Student ID:amquinte

	first_attempt
					2015-10-12 21:00:05
	part1_incorrect_attempt
					('0:00:00', u'52*51*50*49*48*47*46')
	part1_correct_attempt
					['0:01:28', u'C(52,7)']

69 Student ID:jmiclat

	first_attempt
					2015-10-15 17:18:30
	part1_incorrect_attempt
					('0:00:00', u'52!/(52-6)!')
					('0:00:09', u'52!/52!(52-6)!')
	part1_correct_attempt
					['0:00:22', u'52!/(6!(52-6)!)']

70 Student ID:gsrandha

	first_attempt
					2015-10-12 06:58:29
	part1_incorrect_attempt
					('0:00:00', u'5!')
					('0:00:30', u'52*51*50*49*48')
	part1_correct_attempt
					['0:01:10', u'2598960']

71 Student ID:jhc010

	first_attempt
					2015-10-15 16:02:11
	part1_incorrect_attempt
					('0:00:00', u'52!/45!')
					('0:01:00', u'52*51*50*49*48*47*46')
					('0:01:32', u'7^52')
	part1_correct_attempt
					['0:06:12', u'C(52,7)']

72 Student ID:cfgutier

	first_attempt
					2015-10-15 21:27:34
	part1_incorrect_attempt
					('0:00:00', u'52*51*50*49*48*46')
					('0:00:12', u'7!')
	part1_correct_attempt
					['0:02:57', u'133784560']

73 Student ID:anl114

	first_attempt
					2015-10-15 07:52:54
	part1_incorrect_attempt
					('0:00:00', u'52*51*50*49*48*47')
					('0:00:49', u'52*51*50*49*48*47*46')
	part1_correct_attempt
					['0:06:38', u'133784560']

74 Student ID:achinn

	first_attempt
					2015-10-12 23:42:35
	part1_incorrect_attempt
					('0:00:00', u'52*51*50*49')
	part1_correct_attempt
					['0:03:10', u'(52*51*50*49)/(4*3*2)']

75 Student ID:jap009

	first_attempt
					2015-10-15 21:43:10
	part1_incorrect_attempt
					('0:00:00', u'52!/(52-7)!')
					('0:01:37', u'52*51*50*49*48*47*46')
	part1_correct_attempt
					['0:02:10', u'52!/(7!(52-7)!)']

76 Student ID:jcj006

	first_attempt
					2015-10-13 20:43:36
	part1_incorrect_attempt
					('0:00:00', u'52!/(51-7)!')
					('0:00:15', u'52!/(52-7)!')
					('0:00:57', u'52*51*50*49*48*47*46')
					('0:00:00', u'52!/45!')
	part1_correct_attempt
					['3:10:15', u'52!/(45!7!)']

77 Student ID:sippolit

	first_attempt
					2015-10-12 04:23:18
	part1_incorrect_attempt
					('0:00:00', u'4^52')
					('0:00:00', u'4^52')
					('0:00:44', u'52*51*50*49')
	part1_correct_attempt
					['0:01:59', u'270725']

78 Student ID:dtea

	first_attempt
					2015-10-15 23:20:31
	part1_incorrect_attempt
					('0:00:00', u'52*51*50*49')
	part1_correct_attempt
					['0:01:21', u'C(52,4)']

79 Student ID:lahawkin

	first_attempt
					2015-10-14 05:01:11
	part1_incorrect_attempt
					('0:00:00', u'52*51*50*49*48*46*45')
					('0:00:23', u'52*51*50*49*48*46')
					('0:00:50', u'52!/(52-7)!')
					('0:06:16', u'52!/(52-7)!7!')
	part1_correct_attempt
					['0:06:25', u'52!/((52-7)!7!)']

80 Student ID:kquong

	first_attempt
					2015-10-11 04:50:46
	part1_incorrect_attempt
					('0:00:00', u'52*51*50*49')
					('0:00:45', u'52 * 51 * 50 * 49')
	part1_correct_attempt
					['0:01:16', u'52!/(4! *(52-4)!)']

81 Student ID:vasharma

	first_attempt
					2015-10-10 05:55:48
	part1_incorrect_attempt
					('0:00:00', u'52!/(52-7)!')
	part1_correct_attempt
					['0:00:12', u'52!/[7!(52-7)!]']

82 Student ID:hpc001

	first_attempt
					2015-10-14 21:34:22
	part1_incorrect_attempt
					('0:00:00', u'52*51*50*49*48')
	part1_correct_attempt
					['0:04:02', u'C(52, 5)']

83 Student ID:xweng

	first_attempt
					2015-10-12 22:43:18
	part1_incorrect_attempt
					('0:00:00', u'52*51*50*49')
					('0:04:01', u'52*51*50*49')
	part1_correct_attempt
					['3:15:38', u'C(52,4)']

84 Student ID:yypan

	first_attempt
					2015-10-12 20:48:40
	part1_incorrect_attempt
					('0:00:00', u'52*51*50*49*48')
	part1_correct_attempt
					['0:00:32', u'C(52,5)']

85 Student ID:ajvanega

	first_attempt
					2015-10-14 18:13:18
	part1_incorrect_attempt
					('0:00:00', u'52*51*50*49')
	part1_correct_attempt
					['0:07:26', u'52!/((52-4)!4!)']

86 Student ID:zig006

	first_attempt
					2015-10-12 23:19:11
	part1_incorrect_attempt
					('0:00:00', u'52!/45!')
					('0:00:26', u'52*51*50*49*48*47*46')
	part1_correct_attempt
					['0:05:48', u'52!/(7!*45!)']

87 Student ID:mjethani

	first_attempt
					2015-10-13 06:01:41
	part1_incorrect_attempt
					('0:00:00', u'52*51*50*49*48*47*46*45')
					('0:05:14', u'52!/7!(45!)')
	part1_correct_attempt
					['0:05:22', u'52!/(7!(45!))']

88 Student ID:kosung

	first_attempt
					2015-10-15 07:00:04
	part1_incorrect_attempt
					('0:00:00', u'52*51*50*49*48*47*46/(6*5*4*3*2)')
	part1_correct_attempt
					['0:00:25', u'52*51*50*49*48*47/(6*5*4*3*2)']

89 Student ID:j2phung

	first_attempt
					2015-10-14 05:31:50
	part1_incorrect_attempt
					('0:00:00', u'52*51*50*49')
	part1_correct_attempt
					['0:00:32', u'52!/(4!48!)']












## Part 2

### (47) Mistake Group Digits of size 47




### (36) Mistake Group Fraction of size 36




### (21) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:sayao

	first_attempt
					2015-10-12 00:47:11
	part2_incorrect_attempt
					('0:00:58', u'13!/2!')
					('0:01:14', u'13!/(2!*11!)')
	part2_correct_attempt
					['0:01:31', u'4']

1 Student ID:k5law

	first_attempt
					2015-10-12 01:40:02
	part2_incorrect_attempt
					('0:01:16', u'13!/((13-3)!3!)')
					('0:01:29', u'52!/((52-13)!13!)')
	part2_correct_attempt
					['0:01:47', u'4']

2 Student ID:kalang

	first_attempt
					2015-10-15 23:04:47
	part2_incorrect_attempt
					('0:00:00', u'C(4,2)')
	part2_correct_attempt
					['0:00:58', u'C(4,1)']

3 Student ID:jcl084

	first_attempt
					2015-10-13 20:28:00
	part2_incorrect_attempt
					('0:00:30', u'C(52,4)')
					('0:00:36', u'C(13,4)')
					('0:00:57', u'C(52,13)')
	part2_correct_attempt
					['0:02:07', u'4']

4 Student ID:vasharma

	first_attempt
					2015-10-10 05:56:00
	part2_incorrect_attempt
					('0:03:40', u'52!/[5!(52-5)!]')
	part2_correct_attempt
					['0:06:36', u'4']

5 Student ID:jag028

	first_attempt
					2015-10-15 00:55:30
	part2_incorrect_attempt
					('0:03:35', u'4*C(13,6)')
					('0:03:45', u'C(13,6)')
					('0:03:51', u'C(13,4)')
					('0:03:58', u'6*C(13,4)')
	part2_correct_attempt
					['16:07:32', u'4']

6 Student ID:akhmelni

	first_attempt
					2015-10-15 22:48:11
	part2_incorrect_attempt
					('0:00:17', u'C(52,4)')
	part2_correct_attempt
					['0:00:42', u'4']

7 Student ID:rbdoming

	first_attempt
					2015-10-14 18:45:13
	part2_incorrect_attempt
					('0:00:00', u'5^4')
					('0:00:49', u'4^5')
	part2_correct_attempt
					['0:01:23', u'4']

8 Student ID:mitopete

	first_attempt
					2015-10-13 20:20:06
	part2_incorrect_attempt
					('0:00:13', u'4!')
					('0:00:39', u'13^4')
					('0:00:49', u'4^13')
	part2_correct_attempt
					['0:01:10', u'4']

9 Student ID:tcuddy

	first_attempt
					2015-10-10 19:53:54
	part2_incorrect_attempt
					('0:00:19', u'4^3')
	part2_correct_attempt
					['0:00:35', u'4']

10 Student ID:kvass

	first_attempt
					2015-10-14 05:13:51
	part2_incorrect_attempt
					('0:03:03', u'C(52,6)')
					('0:04:13', u'C(13,6)')
	part2_correct_attempt
					['0:55:45', u'4']

11 Student ID:hkhodada

	first_attempt
					2015-10-10 18:51:37
	part2_incorrect_attempt
					('0:00:00', u'C(13,5)')
					('0:02:06', u'P(13,5)')
					('0:05:51', u'C(13,8)')
					('0:06:06', u'P(13,8)')
					('0:06:50', u'4*C(13,5)')
					('0:07:00', u'4*C(13,8)')
					('0:13:38', u'(13!)/[8!*5!]')
					('1 day, 7:17:40', u'C(13,5)*C(39,1)*4')
					('1 day, 7:17:51', u'C(13,5)*C(39,1)')
					('1 day, 7:18:19', u'C(13,5)')
					('1 day, 7:18:39', u'4*C(13,5)')
					('1 day, 7:25:29', u'C(13,10)')
					('1 day, 7:25:48', u'C(13,8)')
					('1 day, 7:26:05', u'4*C(13,8)')
	part2_correct_attempt
					['1 day, 7:27:14', u'4']

12 Student ID:nisharma

	first_attempt
					2015-10-14 01:01:46
	part2_incorrect_attempt
					('0:02:02', u'4*(13!/5!*8!)')
					('0:02:29', u'4*(13!/(5!*8!))')
	part2_correct_attempt
					['0:03:00', u'4']

13 Student ID:kquong

	first_attempt
					2015-10-11 04:52:02
	part2_incorrect_attempt
					('0:00:59', u'13!/(3!*(13-3)!)')
	part2_correct_attempt
					['0:01:14', u'4']

14 Student ID:acvuong

	first_attempt
					2015-10-13 04:39:39
	part2_incorrect_attempt
					('0:00:00', u'C(4,2)')
	part2_correct_attempt
					['0:03:22', u'4']

15 Student ID:xweng

	first_attempt
					2015-10-13 01:58:56
	part2_incorrect_attempt
					('-1 day, 20:51:12', u'25*52*51/3')
					('-1 day, 20:51:30', u'100*52*51/3')
					('-1 day, 20:54:23', u'13*12*11')
					('-1 day, 20:54:47', u'13*12*11*4')
					('-1 day, 20:55:43', u'4*52*51*50/3!')
					('-1 day, 20:58:19', u'52*12*11')
	part2_correct_attempt
					['-1 day, 21:02:38', u'4']

16 Student ID:ytc012

	first_attempt
					2015-10-15 08:34:16
	part2_incorrect_attempt
					('0:00:29', u'7!/(4!3!)')
					('0:00:57', u'7*6*5*4')
					('0:01:29', u'4^4')
					('0:01:35', u'4^7')
	part2_correct_attempt
					['0:11:42', u'4!/3!1!']

17 Student ID:abasu

	first_attempt
					2015-10-11 02:17:05
	part2_incorrect_attempt
					('0:05:35', u'C(52,4)')
	part2_correct_attempt
					['0:15:50', u'C(4,1)']

18 Student ID:mjethani

	first_attempt
					2015-10-13 06:07:03
	part2_incorrect_attempt
					('0:03:09', u'4!/(2!(2!))')
					('2 days, 9:27:57', u'(4!)/((2!)(2!))')
					('2 days, 9:28:42', u'7!/((2!)(5!))')
					('2 days, 9:56:54', u'((13!)/((2!)(11!)))')
					('2 days, 10:04:29', u'52!/((2!)(50!))')
					('2 days, 10:05:11', u'13!/((2!)(11!))')
	part2_correct_attempt
					['2 days, 10:15:05', u'4']

19 Student ID:s6deng

	first_attempt
					2015-10-14 03:02:56
	part2_incorrect_attempt
					('0:02:27', u'C(52,3)')
					('0:02:34', u'P(52,3)')
					('0:04:12', u'C(13,5)')
					('0:04:53', u'C(13,4)')
	part2_correct_attempt
					['0:05:11', u'4']

20 Student ID:t2li

	first_attempt
					2015-10-14 06:36:49
	part2_incorrect_attempt
					('0:01:41', u'C(4,2)*52*C(51,5)')
					('0:01:58', u'C(4,2)*52*51*C(50,5)')
					('0:03:01', u'4*C(13,2)C(39,5)')
					('0:03:51', u'C(13,2)')
					('0:03:56', u'4C(13,2)')
	part2_correct_attempt
					['0:04:11', u'4']












## Part 3

### (592) Mistake Group Digits of size 592




### (102) Mistake Group ['R.0'] of size 102
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(13,2)	|13^4	|[('R.0', 13.0, u'13', u'13')]	|
|1	|C(13,2)	|13^5	|[('R.0', 13.0, u'13', u'13')]	|
|2	|C(13,4)	|13!	|[('R.0', 13.0, u'13', u'13')]	|
|3	|C(13,4)	|C(13,5)	|[('R.0', 13.0, u'13', u'13')]	|
|4	|C(13,2)	|13*12	|[('R.0', 13.0, u'13', u'13')]	|
|5	|C(13,5)	|C(13,7)	|[('R.0', 13.0, u'13', u'13')]	|
|6	|C(13,5)	|13*4	|[('R.0', 13.0, u'13', u'13')]	|
|7	|C(13,6)	|C(13,4)	|[('R.0', 13.0, u'13', u'13')]	|
|8	|C(13,3)	|C(13,2)	|[('R.0', 13.0, u'13', u'13')]	|
|9	|C(13,2)	|13 * 12	|[('R.0', 13.0, u'13', u'13')]	|
|10	|C(13,2)	|13 * 13	|[('R.0', 13.0, u'13', u'13')]	|
|11	|C(13,2)	|13*13	|[('R.0', 13.0, u'13', u'13')]	|
|12	|C(13,3)	|C(13, 2)	|[('R.0', 13.0, u'13', u'13')]	|
|13	|C(13,4)	|13*7	|[('R.0', 13.0, u'13', u'13')]	|
|14	|C(13,4)	|13*3	|[('R.0', 13.0, u'13', u'13')]	|
|15	|C(13,2)	|13 * 4	|[('R.0', 13.0, u'13', u'13')]	|
|16	|C(13,2)	|13+13	|[('R.0', 13.0, u'13', u'13')]	|
|17	|C(13,2)	|C(13, 4)	|[('R.0', 13.0, u'13', u'13')]	|
|18	|C(13,3)	|13*4!	|[('R.0', 13.0, u'13', u'13')]	|
|19	|C(13,4)	|13*2	|[('R.0', 13.0, u'13', u'13')]	|
|20	|C(13,4)	|C(13,3)	|[('R.0', 13.0, u'13', u'13')]	|
|21	|C(13,2)	|13^7	|[('R.0', 13.0, u'13', u'13')]	|
|22	|C(13,4)	|13^6	|[('R.0', 13.0, u'13', u'13')]	|
|23	|C(13,3)	|13 ^ 4	|[('R.0', 13.0, u'13', u'13')]	|
|24	|C(13,5)	|C(13,6)	|[('R.0', 13.0, u'13', u'13')]	|
|25	|C(13,2)	|C(13,1)*C(12,1)	|[('R.0', 13.0, u'13', u'C(13,1)')]	|




### (47) Mistake Group ['R.0', 'R.1'] of size 47
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(13,3)	|13*3	|[('R.0', 13.0, u'13', u'13'), ('R.1', 3.0, u'3', u'3')]	|
|1	|C(13,4)	|13*4	|[('R.0', 13.0, u'13', u'13'), ('R.1', 4.0, u'4', u'4')]	|
|2	|C(13,4)	|13^4	|[('R.0', 13.0, u'13', u'13'), ('R.1', 4.0, u'4', u'4')]	|
|3	|C(13,2)	|13*2	|[('R.0', 13.0, u'13', u'13'), ('R.1', 2.0, u'2', u'2')]	|
|4	|C(13,3)	|13^3	|[('R.0', 13.0, u'13', u'13'), ('R.1', 3.0, u'3', u'3')]	|
|5	|C(13,4)	|C(13,1)*C(4,1)	|[('R.0', 13.0, u'13', u'C(13,1)'), ('R.1', 4.0, u'4', u'C(4,1)')]	|
|6	|C(13,5)	|13*5	|[('R.0', 13.0, u'13', u'13'), ('R.1', 5.0, u'5', u'5')]	|
|7	|C(13,2)	|13^2	|[('R.0', 13.0, u'13', u'13'), ('R.1', 2.0, u'2', u'2')]	|
|8	|C(13,3)	|13 * 3	|[('R.0', 13.0, u'13', u'13'), ('R.1', 3.0, u'3', u'3')]	|
|9	|C(13,3)	|13 ^ 3	|[('R.0', 13.0, u'13', u'13'), ('R.1', 3.0, u'3', u'3')]	|




### (43) Mistake Group Fraction of size 43




### (17) Mistake Group ['R.1'] of size 17
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(13,4)	|C(13,4)*4	|[('R.1', 4.0, u'4', u'4')]	|
|1	|C(13,2)	|C(14,2)	|[('R.1', 2.0, u'2', u'2')]	|
|2	|C(13,3)	|14^3	|[('R.1', 3.0, u'3', u'3')]	|
|3	|C(13,3)	|14*3	|[('R.1', 3.0, u'3', u'3')]	|
|4	|C(13,3)	|C(12, 3)	|[('R.1', 3.0, u'3', u'3')]	|
|5	|C(13,2)	|C(4,2)	|[('R.1', 2.0, u'2', u'2')]	|
|6	|C(13,5)	|4^5	|[('R.1', 5.0, u'5', u'5')]	|
|7	|C(13,4)	|C(12,1)*C(4,1)	|[('R.1', 4.0, u'4', u'C(4,1)')]	|
|8	|C(13,4)	|C(52,4)	|[('R.1', 4.0, u'4', u'4')]	|
|9	|C(13,4)	|9^4	|[('R.1', 4.0, u'4', u'4')]	|
|10	|C(13,2)	|4!/2!	|[('R.1', 2.0, u'2', u'2!')]	|
|11	|C(13,5)	|C(52,5)	|[('R.1', 5.0, u'5', u'5')]	|
|12	|C(13,2)	|(4*3)/2	|[('R.1', 2.0, u'2', u'2')]	|
|13	|C(13,2)	|4^7/2	|[('R.1', 2.0, u'2', u'2')]	|
|14	|C(13,3)	|12*3	|[('R.1', 3.0, u'3', u'3')]	|
|15	|C(13,4)	|12^4	|[('R.1', 4.0, u'4', u'4')]	|
|16	|C(13,2)	|C(52,2)	|[('R.1', 2.0, u'2', u'2')]	|




### (93) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:apokhare

	first_attempt
					2015-10-12 21:05:11
	part3_incorrect_attempt
					('-1 day, 23:45:24', u'13!/(13-4)!')
					('0:01:08', u'13!/(6!*(13-6)!)')
	part3_correct_attempt
					['0:05:30', u'13!/(3!*(13-3)!)']

1 Student ID:kbielawi

	first_attempt
					2015-10-11 23:52:28
	part3_incorrect_attempt
					('0:02:04', u'13*12*11*10')
					('3:03:18', u'13*12*11')
	part3_correct_attempt
					['3:06:27', u'C(13,3)']

2 Student ID:jguanzho

	first_attempt
					2015-10-09 20:12:02
	part3_incorrect_attempt
					('-1 day, 23:55:49', u'52!/(5!*47!)')
	part3_correct_attempt
					['0:00:45', u'13! / (5! * 8!)']

3 Student ID:dcgriffi

	first_attempt
					2015-10-14 07:21:07
	part3_incorrect_attempt
					('-1 day, 23:57:41', u'13*12*11*10')
	part3_correct_attempt
					['0:00:00', u'13!/(4!*9!)']

4 Student ID:dkurli

	first_attempt
					2015-10-14 03:50:42
	part3_incorrect_attempt
					('0:00:40', u'13*12*11')
					('0:01:59', u'13!/9!/4!')
	part3_correct_attempt
					['0:02:13', u'13!/10!/3!']

5 Student ID:nhn018

	first_attempt
					2015-10-15 19:31:19
	part3_incorrect_attempt
					('0:00:00', u'4^12')
					('0:01:03', u'4^13')
	part3_correct_attempt
					['0:48:13', u'715']

6 Student ID:dan029

	first_attempt
					2015-10-09 22:56:33
	part3_incorrect_attempt
					('-1 day, 23:58:02', u'13*12*11*10')
	part3_correct_attempt
					['0:00:00', u'C(13,3)']

7 Student ID:haw081

	first_attempt
					2015-10-10 23:32:20
	part3_incorrect_attempt
					('0:02:21', u'C(4,1)')
					('0:17:09', u'4*13')
	part3_correct_attempt
					['0:18:08', u'C(13,6)']

8 Student ID:ffhaddad

	first_attempt
					2015-10-10 21:08:16
	part3_incorrect_attempt
					('0:00:38', u'C(13,1)')
	part3_correct_attempt
					['0:01:32', u'C(13,3)']

9 Student ID:jmmcalex

	first_attempt
					2015-10-15 08:24:26
	part3_incorrect_attempt
					('0:06:19', u'12*13')
	part3_correct_attempt
					['0:06:29', u'12*13/2']

10 Student ID:tstevens

	first_attempt
					2015-10-10 10:36:56
	part3_incorrect_attempt
					('0:01:39', u'4*13')
	part3_correct_attempt
					['0:05:57', u'286']

11 Student ID:pthsu

	first_attempt
					2015-10-10 20:18:37
	part3_incorrect_attempt
					('0:38:17', u'C(13,1)')
	part3_correct_attempt
					['0:39:07', u'C(13,3)']

12 Student ID:tcuddy

	first_attempt
					2015-10-10 19:53:54
	part3_incorrect_attempt
					('0:01:02', u'13*12*11')
					('0:03:31', u'13*12*11*4')
	part3_correct_attempt
					['0:04:04', u'13!/(3!10!)']

13 Student ID:l8ngo

	first_attempt
					2015-10-12 15:46:35
	part3_incorrect_attempt
					('0:05:44', u'13*12*11')
					('0:10:53', u'14!/[4!10!]')
					('1:01:03', u'13![4!9!]')
	part3_correct_attempt
					['1:01:20', u'13!/[4!9!]']

14 Student ID:djk006

	first_attempt
					2015-10-11 02:28:10
	part3_incorrect_attempt
					('0:02:10', u'52*12*11')
					('0:02:29', u'4*13*12*11')
					('0:02:37', u'4*12*11')
					('0:07:10', u'13*12*11')
					('0:11:12', u'52*12*11')
					('0:13:48', u'52*12*11/2')
	part3_correct_attempt
					['0:14:35', u'13*12*11/6']

15 Student ID:dsriniva

	first_attempt
					2015-10-15 19:57:22
	part3_incorrect_attempt
					('0:03:17', u'13*12*11*10')
	part3_correct_attempt
					['0:03:43', u'715']

16 Student ID:a2ahmed

	first_attempt
					2015-10-15 04:08:54
	part3_incorrect_attempt
					('0:02:32', u'13*12*11*10*9*8')
					('0:03:00', u'12*11*10*9*8*7')
					('0:03:43', u'13*12*11*10*9')
	part3_correct_attempt
					['0:04:19', u'C(13,5)']

17 Student ID:mitopete

	first_attempt
					2015-10-13 20:20:06
	part3_incorrect_attempt
					('0:02:05', u'4!')
					('0:04:05', u'4^13')
	part3_correct_attempt
					['0:07:13', u'13!/(4!9!)']

18 Student ID:starinia

	first_attempt
					2015-10-15 01:42:28
	part3_incorrect_attempt
					('-1 day, 23:48:19', u'52/4')
					('0:11:11', u'13!/4!')
					('0:18:14', u'39!/(2!37!)')
	part3_correct_attempt
					['2:07:22', u'C(13,2)']

19 Student ID:tak068

	first_attempt
					2015-10-14 06:49:53
	part3_incorrect_attempt
					('0:08:41', u'4^13')
	part3_correct_attempt
					['0:11:57', u'55*13']

20 Student ID:m8woo

	first_attempt
					2015-10-10 01:10:32
	part3_incorrect_attempt
					('0:00:00', u'C(12,7)')
	part3_correct_attempt
					['0:01:04', u'C(13,5)']

21 Student ID:druble

	first_attempt
					2015-10-13 01:02:05
	part3_incorrect_attempt
					('0:04:01', u'4*13')
					('0:05:57', u'2*4*13')
	part3_correct_attempt
					['0:12:40', u'C(13,2)']

22 Student ID:h4tu

	first_attempt
					2015-10-15 06:56:59
	part3_incorrect_attempt
					('0:01:18', u'4^7')
					('0:02:05', u'4^6')
	part3_correct_attempt
					['0:04:29', u'13*12/2']

23 Student ID:ccn001

	first_attempt
					2015-10-12 23:25:54
	part3_incorrect_attempt
					('-1 day, 22:57:27', u'13*12*11')
	part3_correct_attempt
					['-1 day, 22:58:05', u'13!/(3!(10!))']

24 Student ID:lrlai

	first_attempt
					2015-10-12 19:51:30
	part3_incorrect_attempt
					('0:05:20', u'13*12*11')
					('0:05:28', u'13*12*11*13')
					('0:06:39', u'13*12*11*4')
					('0:07:27', u'C(13,3)*13')
	part3_correct_attempt
					['0:07:35', u'C(13,3)']

25 Student ID:lguintu

	first_attempt
					2015-10-09 21:51:02
	part3_incorrect_attempt
					('0:01:06', u'4!')
					('0:04:54', u'C(13,1)')
	part3_correct_attempt
					['0:05:24', u'C(13,4)']

26 Student ID:c1sorian

	first_attempt
					2015-10-14 22:12:26
	part3_incorrect_attempt
					('0:02:43', u'13!/(3!)')
					('0:02:52', u'13!/(3!9!)')
	part3_correct_attempt
					['0:03:52', u'13!/(3!10!)']

27 Student ID:abjara

	first_attempt
					2015-10-12 10:47:42
	part3_incorrect_attempt
					('0:12:07', u'2^13')
	part3_correct_attempt
					['0:13:30', u'13!/(2!*11!)']

28 Student ID:mroknich

	first_attempt
					2015-10-14 00:29:46
	part3_incorrect_attempt
					('0:12:09', u'13*12*11')
	part3_correct_attempt
					['0:12:23', u'C(13,3)']

29 Student ID:beyounge

	first_attempt
					2015-10-09 06:00:12
	part3_incorrect_attempt
					('0:00:51', u'13*12*11*10')
					('1:01:07', u'13*12*11*10')
	part3_correct_attempt
					['1:02:11', u'C(13,4)']

30 Student ID:tpmach

	first_attempt
					2015-10-11 01:28:46
	part3_incorrect_attempt
					('0:06:25', u'4^13')
	part3_correct_attempt
					['0:07:28', u'13!/(4!(13-4)!)']

31 Student ID:r1gu

	first_attempt
					2015-10-15 12:15:23
	part3_incorrect_attempt
					('10:04:19', u'4*(13!/(2!11!))')
	part3_correct_attempt
					['10:05:08', u'(13!/(2!11!))']

32 Student ID:hak014

	first_attempt
					2015-10-13 05:11:32
	part3_incorrect_attempt
					('0:00:29', u'13*12*11*10')
					('0:00:45', u'(13*12*11*10)*4')
					('0:02:16', u'13*12*11*10*9*47')
					('0:05:10', u'(13*12*11*10*9*39)')
					('1:21:04', u'(13*12*11*10*9*39)/5!')
	part3_correct_attempt
					['2 days, 14:02:42', u'C(13,5)']

33 Student ID:dis003

	first_attempt
					2015-10-15 11:10:37
	part3_incorrect_attempt
					('0:02:01', u'52/4')
	part3_correct_attempt
					['0:03:32', u'C(13,2)']

34 Student ID:jhw015

	first_attempt
					2015-10-15 02:18:24
	part3_incorrect_attempt
					('0:02:14', u'C(52,4)')
					('0:05:06', u'C(52,13)')
					('0:05:13', u'C(52,4)')
					('0:05:52', u'P(52,4)')
					('0:05:58', u'P(52,13)')
					('1:12:36', u'C(52,4)')
					('1:12:41', u'C(52,13)')
	part3_correct_attempt
					['1:13:44', u'C(13,5)']

35 Student ID:dsmonaha

	first_attempt
					2015-10-13 17:54:09
	part3_incorrect_attempt
					('0:00:38', u'C(13,1)')
					('0:02:24', u'P(13,1)')
					('0:05:07', u'C(4,1)')
					('0:05:16', u'C(13,1)')
					('0:05:21', u'C(12,1)')
	part3_correct_attempt
					['0:14:16', u'C(13,4)']

36 Student ID:thwan

	first_attempt
					2015-10-10 19:15:04
	part3_incorrect_attempt
					('0:00:00', u'C(13,1)')
	part3_correct_attempt
					['0:01:33', u'C(13,4)']

37 Student ID:lcardoso

	first_attempt
					2015-10-13 17:22:51
	part3_incorrect_attempt
					('0:01:31', u'4*13')
					('0:01:49', u'2*13')
	part3_correct_attempt
					['0:03:23', u'C(13,2)']

38 Student ID:jel075

	first_attempt
					2015-10-15 01:11:43
	part3_incorrect_attempt
					('-1 day, 23:58:40', u'13*12*11')
	part3_correct_attempt
					['-1 day, 23:59:46', u'13!/(10!*3!)']

39 Student ID:ytc012

	first_attempt
					2015-10-15 08:34:16
	part3_incorrect_attempt
					('0:10:11', u'13*12*11*10')
	part3_correct_attempt
					['0:11:16', u'13!/(4!9!)']

40 Student ID:edescobe

	first_attempt
					2015-10-12 20:11:25
	part3_incorrect_attempt
					('2:19:06', u'13*12*11')
	part3_correct_attempt
					['2:19:35', u'C(13,3)']

41 Student ID:kgrozav

	first_attempt
					2015-10-15 19:07:37
	part3_incorrect_attempt
					('0:02:05', u'13!/12!')
					('0:04:31', u'13!/(5!*8!)')
	part3_correct_attempt
					['0:05:02', u'13!/(2!*11!)']

42 Student ID:muy002

	first_attempt
					2015-10-14 22:07:25
	part3_incorrect_attempt
					('0:00:33', u'13!(2!11!)')
	part3_correct_attempt
					['0:00:39', u'13!/(2!11!)']

43 Student ID:wcwhite

	first_attempt
					2015-10-15 21:48:54
	part3_incorrect_attempt
					('0:04:38', u'C(52,11)')
					('0:12:38', u'11*10*9*8*7*6*5')
					('0:13:53', u'11*10*9*8*7*6')
					('0:15:20', u'13*12*11*10*9*8')

44 Student ID:cstringh

	first_attempt
					2015-10-12 22:22:12
	part3_incorrect_attempt
					('-1 day, 23:59:04', u'14!')
					('0:02:54', u'14*13*12')
					('0:05:20', u'14*4')
					('0:09:10', u'12*4')
					('0:09:24', u'11*4')
	part3_correct_attempt
					['0:32:37', u'C(13, 3)']

45 Student ID:qfu

	first_attempt
					2015-10-10 16:21:36
	part3_incorrect_attempt
					('0:00:00', u'C(13,1)')
	part3_correct_attempt
					['0:01:26', u'C(13,4)']

46 Student ID:yjshin

	first_attempt
					2015-10-14 09:56:49
	part3_incorrect_attempt
					('1 day, 0:01:21', u'(4*286*3*715)')
					('1 day, 2:16:44', u'13!/3!')
	part3_correct_attempt
					['1 day, 2:16:53', u'13!/(3!10!)']

47 Student ID:bkoli

	first_attempt
					2015-10-15 07:18:22
	part3_incorrect_attempt
					('9:47:33', u'13!/2!11!')
	part3_correct_attempt
					['9:47:43', u'13!/(2!11!)']

48 Student ID:dac064

	first_attempt
					2015-10-15 20:17:52
	part3_incorrect_attempt
					('0:03:08', u'(13! / 8!)*(13!)')
					('0:03:20', u'(13! / 8!)*(13)')
					('0:03:33', u'(13! / 9!)*(13)')
					('0:03:54', u'(13! / 9!)')
	part3_correct_attempt
					['0:05:14', u'C(13,4)']

49 Student ID:v3doan

	first_attempt
					2015-10-11 02:30:57
	part3_incorrect_attempt
					('0:16:26', u'11 * 12')
	part3_correct_attempt
					['0:19:31', u'C(13,2)']

50 Student ID:k3tan

	first_attempt
					2015-10-13 05:46:50
	part3_incorrect_attempt
					('0:01:25', u'13!/(4!8!)')
					('0:07:30', u'13!/9!')
					('0:08:39', u'13!/6!')
					('0:08:48', u'13!/7!')
					('0:13:04', u'4(13!/9!)')
	part3_correct_attempt
					['0:18:10', u'13!/(4!9!)']

51 Student ID:b3hwang

	first_attempt
					2015-10-15 22:53:09
	part3_incorrect_attempt
					('0:04:36', u'3*13')
					('0:06:09', u'13*12*11*10*9*10')

52 Student ID:lywong

	first_attempt
					2015-10-13 00:28:17
	part3_incorrect_attempt
					('0:05:46', u'13!/(2!(13-2))')
	part3_correct_attempt
					['0:06:03', u'13!/(2!(13-2)!)']

53 Student ID:kebao

	first_attempt
					2015-10-15 05:13:42
	part3_incorrect_attempt
					('0:01:39', u'13!/(5!)')
					('0:01:48', u'13!/(5!*8!)')
	part3_correct_attempt
					['0:51:13', u'13!/(2!*11!)']

54 Student ID:nisharma

	first_attempt
					2015-10-14 01:01:46
	part3_incorrect_attempt
					('0:04:00', u'4*(13!/ 5!*8!)')
					('0:04:08', u'4*(13!/ (5!*8!))')
					('0:10:39', u'52!/(5!*47!)')
					('0:21:43', u'4*(13!/(5!*8!))')
					('0:25:50', u'52*51*50*49*48')
	part3_correct_attempt
					['21:08:05', u'C(13,5)']

55 Student ID:glcohen

	first_attempt
					2015-10-13 05:44:18
	part3_incorrect_attempt
					('0:02:32', u'(13!)/(12!)')
	part3_correct_attempt
					['0:04:56', u'13!/(10!3!)']

56 Student ID:achava

	first_attempt
					2015-10-13 07:44:33
	part3_incorrect_attempt
					('0:41:51', u'4^13')
	part3_correct_attempt
					['0:43:22', u'C(13,4)']

57 Student ID:pvl001

	first_attempt
					2015-10-13 19:10:54
	part3_incorrect_attempt
					('0:02:02', u'52 * 12')
					('0:15:02', u'13 * 12 * 4')
	part3_correct_attempt
					['0:19:45', u'78']

58 Student ID:jcj006

	first_attempt
					2015-10-13 23:53:51
	part3_incorrect_attempt
					('0:03:35', u'13!/(9!4!)')
	part3_correct_attempt
					['0:13:56', u'13!/(3!10!)']

59 Student ID:n2patil

	first_attempt
					2015-10-13 16:32:22
	part3_incorrect_attempt
					('0:10:52', u'13*12*11*10')
	part3_correct_attempt
					['0:11:09', u'715']

60 Student ID:jnatale

	first_attempt
					2015-10-13 01:16:50
	part3_incorrect_attempt
					('0:07:05', u'13*12*11*10')
	part3_correct_attempt
					['0:07:14', u'C(13,4)']

61 Student ID:ielouaae

	first_attempt
					2015-10-15 07:52:08
	part3_incorrect_attempt
					('0:02:14', u'4*13')
					('0:20:30', u'13!/(5!6!)')
	part3_correct_attempt
					['0:21:46', u'13!/(9!4!)']

62 Student ID:jjchung

	first_attempt
					2015-10-14 19:52:36
	part3_incorrect_attempt
					('0:01:31', u'13!12!11!')
	part3_correct_attempt
					['0:06:47', u'C(13,3)']

63 Student ID:csl030

	first_attempt
					2015-10-10 05:01:34
	part3_incorrect_attempt
					('0:01:09', u'4 * 13')
					('0:01:32', u'3 * 13')
	part3_correct_attempt
					['0:02:06', u'C(13, 3)']

64 Student ID:azkong

	first_attempt
					2015-10-15 16:13:41
	part3_incorrect_attempt
					('0:03:27', u'C(13, 1)')
	part3_correct_attempt
					['0:04:05', u'C(13, 4)']

65 Student ID:k4ma

	first_attempt
					2015-10-15 03:24:32
	part3_incorrect_attempt
					('-1 day, 23:55:00', u'13*12*11*10')
	part3_correct_attempt
					['-1 day, 23:59:27', u'C(13,4)']

66 Student ID:aurodrig

	first_attempt
					2015-10-15 18:19:11
	part3_incorrect_attempt
					('0:50:38', u'4*9/[36/C(52,5)]')
					('0:54:20', u'52!/33120')
	part3_correct_attempt
					['1:27:17', u'78']

67 Student ID:hmnaing

	first_attempt
					2015-10-13 00:38:44
	part3_incorrect_attempt
					('0:00:00', u'13*12*11')
	part3_correct_attempt
					['0:01:47', u'C(13, 3)']

68 Student ID:klala

	first_attempt
					2015-10-12 04:18:35
	part3_incorrect_attempt
					('0:00:52', u'4*13')
	part3_correct_attempt
					['0:01:44', u'C(13,3)']

69 Student ID:dlgoldbe

	first_attempt
					2015-10-13 01:23:40
	part3_incorrect_attempt
					('0:03:56', u'12*3')
	part3_correct_attempt
					['1 day, 23:12:53', u'13!/(4!*9!)']

70 Student ID:jfalcone

	first_attempt
					2015-10-14 22:48:45
	part3_incorrect_attempt
					('0:06:31', u'4^13')
					('0:08:47', u'2^13')
	part3_correct_attempt
					['0:11:53', u'13!/(2!11!)']

71 Student ID:t2shin

	first_attempt
					2015-10-15 05:47:08
	part3_incorrect_attempt
					('0:02:06', u'4*4*4')
					('0:03:20', u'13*12*11')
	part3_correct_attempt
					['0:04:38', u'13!/(3!10!)']

72 Student ID:ewbrenna

	first_attempt
					2015-10-12 20:07:47
	part3_incorrect_attempt
					('0:02:41', u'13*12*11*10')
	part3_correct_attempt
					['0:09:08', u'13!/(4!*(13-4)!)']

73 Student ID:spw006

	first_attempt
					2015-10-13 21:20:56
	part3_incorrect_attempt
					('1:50:33', u'C(52,7)')
	part3_correct_attempt
					['1:51:23', u'C(13,4)']

74 Student ID:any027

	first_attempt
					2015-10-09 09:46:45
	part3_incorrect_attempt
					('0:02:23', u'4 * 13')
					('0:05:02', u'2^13')
	part3_correct_attempt
					['0:05:38', u'78']

75 Student ID:vsosnovs

	first_attempt
					2015-10-15 04:18:13
	part3_incorrect_attempt
					('0:03:16', u'C(13,1)')
	part3_correct_attempt
					['0:07:15', u'C(13,2)']

76 Student ID:k5law

	first_attempt
					2015-10-12 01:40:02
	part3_incorrect_attempt
					('1:53:04', u'13*12*11')
					('1:54:59', u'13*13*13')
					('1:59:25', u'4*13')
					('1:59:58', u'4*(13!/(10!3!))')
	part3_correct_attempt
					['2:00:06', u'(13!/(10!3!))']

77 Student ID:b1green

	first_attempt
					2015-10-15 20:57:42
	part3_incorrect_attempt
					('0:00:50', u'13*12*11*10')
	part3_correct_attempt
					['0:05:29', u'C(13,4)']

78 Student ID:amquinte

	first_attempt
					2015-10-12 21:01:33
	part3_incorrect_attempt
					('0:01:43', u'C(52,2)')
	part3_correct_attempt
					['3 days, 2:26:56', u'C(13,5)']

79 Student ID:syc078

	first_attempt
					2015-10-12 21:09:54
	part3_incorrect_attempt
					('2 days, 5:13:45', u'(13*12*11*10) / (4*3*2)')
	part3_correct_attempt
					['2 days, 5:16:47', u'(13*12)/2']

80 Student ID:jhc010

	first_attempt
					2015-10-15 16:08:23
	part3_incorrect_attempt
					('0:00:41', u'3^13')
					('0:00:49', u'13*12*11')
	part3_correct_attempt
					['0:00:58', u'C(13,3)']

81 Student ID:rsmurlo

	first_attempt
					2015-10-13 17:48:02
	part3_incorrect_attempt
					('-1 day, 23:42:14', u'13*12*11*10')
					('-1 day, 23:50:51', u'13*12*11')
					('-1 day, 23:51:24', u'13*12*11*4')
					('-1 day, 23:52:04', u'13*12*11*39')
					('-1 day, 23:52:21', u'13*12*11*39*4')
					('-1 day, 23:54:16', u'13*12*11*4*4')
	part3_correct_attempt
					['0:00:00', u'13!/(10!3!)']

82 Student ID:anl114

	first_attempt
					2015-10-15 07:59:32
	part3_incorrect_attempt
					('-1 day, 23:54:32', u'(13*12*11*10*9)/52')
					('-1 day, 23:56:28', u'(13*12*11*10*9)')
	part3_correct_attempt
					['0:00:00', u'1287']

83 Student ID:kalang

	first_attempt
					2015-10-15 23:04:47
	part3_incorrect_attempt
					('0:01:09', u'C(13,1)')
	part3_correct_attempt
					['0:01:15', u'C(13,2)']

84 Student ID:ajabasa

	first_attempt
					2015-10-14 06:50:09
	part3_incorrect_attempt
					('0:07:17', u'13*13*4')
	part3_correct_attempt
					['0:09:13', u'C(13, 2)']

85 Student ID:jnn015

	first_attempt
					2015-10-11 15:24:08
	part3_incorrect_attempt
					('0:04:24', u'13*12*11')
	part3_correct_attempt
					['0:05:57', u'(13*12*11)/3!']

86 Student ID:lahawkin

	first_attempt
					2015-10-14 05:07:36
	part3_incorrect_attempt
					('0:02:57', u'4*9')
					('0:03:07', u'4*10')
					('0:04:10', u'9!/((5!)4!)')
					('0:07:14', u'9!/((7!)2!)')
	part3_correct_attempt
					['0:09:31', u'13!/((13-4)!*4!)']

87 Student ID:kosung

	first_attempt
					2015-10-15 07:00:29
	part3_incorrect_attempt
					('-1 day, 23:40:29', u'13*12*11')
	part3_correct_attempt
					['-1 day, 23:57:50', u'22*13']

88 Student ID:xweng

	first_attempt
					2015-10-13 01:58:56
	part3_incorrect_attempt
					('-1 day, 21:02:51', u'4*13*12*11')
					('-1 day, 21:03:09', u'13*12*11')
					('-1 day, 21:07:40', u'3*13*12*11')
					('-1 day, 21:08:43', u'3*13')
					('-1 day, 23:49:04', u'4*13')
					('-1 day, 23:49:24', u'4*13*12*11*10')
					('-1 day, 23:49:37', u'4*13*12*11')
					('-1 day, 23:51:01', u'10*13*12*11')
					('-1 day, 23:51:06', u'13*12*11')
					('-1 day, 23:58:48', u'C(4,1)C(13,3)')
					('0:00:25', u'C(4,1)C(52,3)')
					('0:05:15', u'C(4,1)C(13,3)')
					('0:06:20', u'C(4,1)C(13,3)*39')
					('0:06:29', u'C(4,1)C(13,3)')
	part3_correct_attempt
					['0:06:35', u'C(13,3)']

89 Student ID:yypan

	first_attempt
					2015-10-12 20:49:12
	part3_incorrect_attempt
					('0:00:26', u'13*12*11')
	part3_correct_attempt
					['0:00:41', u'C(13,3)']

90 Student ID:ajvanega

	first_attempt
					2015-10-14 18:20:44
	part3_incorrect_attempt
					('0:06:29', u'4*13')
					('0:09:12', u'3^13')
	part3_correct_attempt
					['0:09:55', u'13!/(10!3!)']

91 Student ID:mtrafeca

	first_attempt
					2015-10-11 05:59:54
	part3_incorrect_attempt
					('0:07:54', u'52!/(13!*39!)')
					('0:08:16', u'13!/(5!*8!)')
					('0:12:03', u'13!/(4!*9!)')
					('0:16:08', u'9*8')
					('0:16:37', u'9!/(7!*2!)')
	part3_correct_attempt
					['0:19:46', u'13!/(11!*2!)']

92 Student ID:gsrandha

	first_attempt
					2015-10-12 06:59:39
	part3_incorrect_attempt
					('0:04:51', u'13*12*11*10*9*8')
					('0:06:47', u'13*13*13*13')
					('0:07:41', u'125*20')
	part3_correct_attempt
					['23:17:29', u'78']












## Part 4

### (125) Mistake Group Digits of size 125




### (2) Mistake Group Fraction of size 2




### (1) Mistake Group Wrong_Sign of size 1




### (33) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:dlgoldbe

	first_attempt
					2015-10-13 01:23:40
	part4_incorrect_attempt
					('0:08:50', u'12*3')
	part4_correct_attempt
					['1 day, 23:14:11', u'13*3']

1 Student ID:jag028

	first_attempt
					2015-10-15 00:55:30
	part4_incorrect_attempt
					('16:09:44', u'C(13,2)')
					('16:09:54', u'C(13,3)')
					('16:10:18', u'C(52,2)')
					('16:11:11', u'1326-715')
	part4_correct_attempt
					['16:12:44', u'52-13']

2 Student ID:ielouaae

	first_attempt
					2015-10-15 07:52:08
	part4_incorrect_attempt
					('0:23:21', u'39!/(37!2!)')
	part4_correct_attempt
					['0:23:45', u'39']

3 Student ID:kbielawi

	first_attempt
					2015-10-11 23:52:28
	part4_incorrect_attempt
					('0:01:18', u'4*13')
	part4_correct_attempt
					['3:05:23', u'52-13']

4 Student ID:eyhu

	first_attempt
					2015-10-09 02:59:03
	part4_incorrect_attempt
					('0:00:00', u'52/2')
	part4_correct_attempt
					['0:01:26', u'3*(52/4)']

5 Student ID:alakamsa

	first_attempt
					2015-10-10 20:39:47
	part4_incorrect_attempt
					('0:00:00', u'25-13')
	part4_correct_attempt
					['0:02:01', u'52-13']

6 Student ID:any027

	first_attempt
					2015-10-09 09:46:45
	part4_incorrect_attempt
					('0:06:13', u'13^3')
	part4_correct_attempt
					['0:06:54', u'39']

7 Student ID:jjm019

	first_attempt
					2015-10-15 23:24:43
	part4_incorrect_attempt
					('0:04:52', u'4(715)')
	part4_correct_attempt
					['0:06:20', u'52-13']

8 Student ID:dcrume

	first_attempt
					2015-10-14 20:25:03
	part4_incorrect_attempt
					('1 day, 2:53:43', u'13*2')

9 Student ID:t2li

	first_attempt
					2015-10-14 06:36:49
	part4_incorrect_attempt
					('0:03:37', u'4C(13,2)C(39,5)')
	part4_correct_attempt
					['0:05:03', u'39']

10 Student ID:jfalcone

	first_attempt
					2015-10-14 22:48:45
	part4_incorrect_attempt
					('0:10:20', u'2*13')
	part4_correct_attempt
					['0:13:25', u'39']

11 Student ID:j5phung

	first_attempt
					2015-10-09 18:34:23
	part4_incorrect_attempt
					('0:02:33', u'52-6')
	part4_correct_attempt
					['0:03:46', u'39']

12 Student ID:jmiclat

	first_attempt
					2015-10-15 17:18:52
	part4_incorrect_attempt
					('0:05:41', u'3(13*12)')
					('0:08:25', u'13*3*2')
	part4_correct_attempt
					['0:09:21', u'13*3']

13 Student ID:gsrandha

	first_attempt
					2015-10-12 06:59:39
	part4_incorrect_attempt
					('0:07:41', u'125*20')
					('23:28:40', u'C(52,3)')

14 Student ID:haw081

	first_attempt
					2015-10-10 23:32:20
	part4_incorrect_attempt
					('0:00:00', u'52-6')
					('0:04:08', u'52-6-3')
					('0:04:20', u'52-6-4')
	part4_correct_attempt
					['0:06:24', u'52-13']

15 Student ID:mnrahman

	first_attempt
					2015-10-15 20:01:08
	part4_incorrect_attempt
					('0:02:20', u'C(39,6-4)')
	part4_correct_attempt
					['0:03:26', u'39']

16 Student ID:lalacson

	first_attempt
					2015-10-11 22:18:21
	part4_incorrect_attempt
					('0:00:00', u'52-14')
					('0:01:12', u'52-12')
	part4_correct_attempt
					['0:07:33', u'52-13']

17 Student ID:dis003

	first_attempt
					2015-10-15 11:10:37
	part4_incorrect_attempt
					('0:00:41', u'52/2')
					('0:00:56', u'52/2 *5')
					('0:01:29', u'52-52/2')
					('0:04:21', u'C(13*3,2)')
	part4_correct_attempt
					['0:04:32', u'13*3']

18 Student ID:tol003

	first_attempt
					2015-10-14 00:23:54
	part4_incorrect_attempt
					('0:06:02', u'C(52,3)')
					('0:08:25', u'C(13,3)')
					('0:09:08', u'C(52,1)')
					('0:13:13', u'C(39,3)')
	part4_correct_attempt
					['0:14:11', u'39']

19 Student ID:msaguiar

	first_attempt
					2015-10-12 04:07:32
	part4_incorrect_attempt
					('1 day, 22:39:18', u'C(49,2)')
					('1 day, 22:47:55', u'C(39,2)')
	part4_correct_attempt
					['1 day, 22:48:19', u'39']

20 Student ID:rraiyyan

	first_attempt
					2015-10-14 23:50:33
	part4_incorrect_attempt
					('0:01:49', u'(13-6)*3')
					('0:05:21', u'3*48/4')
	part4_correct_attempt
					['0:08:56', u'39']

21 Student ID:jhw015

	first_attempt
					2015-10-15 02:18:24
	part4_incorrect_attempt
					('1:14:35', u'C(13,2)')
					('1:15:00', u'C(11,2)')
					('1:16:56', u'C(13,4)')
					('1:17:25', u'C(4,2)')
					('1:43:15', u'C(39,2)')
	part4_correct_attempt
					['1:43:48', u'39']

22 Student ID:l8ngo

	first_attempt
					2015-10-12 15:46:35
	part4_incorrect_attempt
					('-1 day, 23:56:37', u'[13!/[2!11!] ] * 3 * 3')
					('1:05:04', u'[3^2]*[13!/[2!11!]]')
					('1:05:16', u'[3^2]')
					('1:09:00', u'[52!/[2!50!]]-13')
					('1:14:14', u'13!/[2!11!]*9')
	part4_correct_attempt
					['3:57:51', u'39']

23 Student ID:eaherman

	first_attempt
					2015-10-14 02:46:39
	part4_incorrect_attempt
					('0:01:14', u'52-3')
	part4_correct_attempt
					['0:02:18', u'52-13']

24 Student ID:edescobe

	first_attempt
					2015-10-12 20:11:25
	part4_incorrect_attempt
					('0:00:00', u'9*13')
					('0:00:35', u'9*12')
	part4_correct_attempt
					['0:02:20', u'3*13']

25 Student ID:smohiman

	first_attempt
					2015-10-11 22:03:15
	part4_incorrect_attempt
					('0:00:00', u'C(4,3)')
	part4_correct_attempt
					['0:05:46', u'39']

26 Student ID:vasharma

	first_attempt
					2015-10-10 05:56:00
	part4_incorrect_attempt
					('0:38:43', u'13!/[2!(13-2)!]')
					('0:42:17', u'45!/[2!(45-2!)]')
					('0:42:22', u'45!/[2!(45-2)!]')
					('0:44:12', u'47!')
					('0:44:30', u'47!/(2![47-2]!)')
					('0:55:42', u'13!/[2!(13-2)!]')
					('0:56:52', u'47*48')
					('0:57:06', u'47*46')
					('0:57:41', u'39*38')
	part4_correct_attempt
					['0:57:46', u'39']

27 Student ID:qfu

	first_attempt
					2015-10-10 16:21:36
	part4_incorrect_attempt
					('0:01:26', u'9*3')
	part4_correct_attempt
					['0:04:34', u'13*3']

28 Student ID:dcastlem

	first_attempt
					2015-10-15 03:21:40
	part4_incorrect_attempt
					('0:05:48', u'39!/((4!)(35!))')
	part4_correct_attempt
					['0:07:10', u'39']

29 Student ID:sthapa

	first_attempt
					2015-10-15 16:05:06
	part4_incorrect_attempt
					('0:05:33', u'13*6')
					('0:05:42', u'13*2')
	part4_correct_attempt
					['0:05:48', u'13*3']

30 Student ID:mjethani

	first_attempt
					2015-10-13 06:07:03
	part4_incorrect_attempt
					('2 days, 10:16:38', u'5!/((3!)(2!))')
	part4_correct_attempt
					['2 days, 10:38:26', u'39']

31 Student ID:kgrozav

	first_attempt
					2015-10-15 19:07:37
	part4_incorrect_attempt
					('0:06:17', u'4!/3!')
					('0:08:02', u'C(13,3)*C(4,3)')
	part4_correct_attempt
					['0:09:12', u'13*3']

32 Student ID:whcombs

	first_attempt
					2015-10-13 03:41:51
	part4_incorrect_attempt
					('0:16:19', u'C(3,1)')
					('0:16:27', u'C(4,1)')
					('0:18:18', u'52-6')
	part4_correct_attempt
					['0:26:06', u'13*3']












## Part 5

### (57) Mistake Group Digits of size 57




### (33) Mistake Group Fraction of size 33




### (29) Mistake Group ['R.1'] of size 29
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(39,7-4)	|C(13,3)	|[('R.1', 3.0, u'7-4', u'3')]	|
|1	|C(39,7-2)	|C(33,5)	|[('R.1', 5.0, u'7-2', u'5')]	|
|2	|C(39,6-4)	|C(13,2)	|[('R.1', 2.0, u'6-4', u'2')]	|
|3	|C(39,6-4)	|C(6,2)	|[('R.1', 2.0, u'6-4', u'2')]	|
|4	|C(39,6-4)	|C(9,2)	|[('R.1', 2.0, u'6-4', u'2')]	|
|5	|C(39,6-4)	|C(18,2)	|[('R.1', 2.0, u'6-4', u'2')]	|
|6	|C(39,7-6)	|C(3,1)	|[('R.1', 1.0, u'7-6', u'1')]	|
|7	|C(39,7-5)	|C(49,2)	|[('R.1', 2.0, u'7-5', u'2')]	|
|8	|C(39,7-6)	|C(46,1)	|[('R.1', 1.0, u'7-6', u'1')]	|
|9	|C(39,7-6)	|C(43,1)	|[('R.1', 1.0, u'7-6', u'1')]	|
|10	|C(39,5-2)	|C(12,3)	|[('R.1', 3.0, u'5-2', u'3')]	|
|11	|C(39,5-3)	|C(13*4,2)	|[('R.1', 2.0, u'5-3', u'2')]	|
|12	|C(39,4-3)	|C(52-14,1)	|[('R.1', 1.0, u'4-3', u'1')]	|
|13	|C(39,7-3)	|C(13,4)	|[('R.1', 4.0, u'7-3', u'4')]	|
|14	|C(39,5-3)	|C(12,2)	|[('R.1', 2.0, u'5-3', u'2')]	|
|15	|C(39,6-4)	|C(48,2)	|[('R.1', 2.0, u'6-4', u'2')]	|
|16	|C(39,6-4)	|C(30,2)	|[('R.1', 2.0, u'6-4', u'2')]	|
|17	|C(39,5-4)	|C(12,1)	|[('R.1', 1.0, u'5-4', u'1')]	|
|18	|C(39,6-4)	|C(29,2)	|[('R.1', 2.0, u'6-4', u'2')]	|
|19	|C(39,6-5)	|C(13,1)	|[('R.1', 1.0, u'6-5', u'1')]	|
|20	|C(39,4-3)	|C(40,1)	|[('R.1', 1.0, u'4-3', u'1')]	|
|21	|C(39,4-3)	|C(52,1)	|[('R.1', 1.0, u'4-3', u'1')]	|
|22	|C(39,6-2)	|(39*38*37*36)/4	|[('R.1', 4.0, u'6-2', u'4')]	|




### (8) Mistake Group ['R.0'] of size 8
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(39,5-3)	|39*38	|[('R.0', 39.0, u'39', u'39')]	|
|1	|C(39,6-4)	|(52-13)(52-13-1)	|[('R.0', 39.0, u'39', u'52-13')]	|
|2	|C(39,4-3)	|C(52-13,12)	|[('R.0', 39.0, u'39', u'52-13')]	|
|3	|C(39,4-2)	|(52-13)!	|[('R.0', 39.0, u'39', u'52-13')]	|
|4	|C(39,6-4)	|C(39,4)	|[('R.0', 39.0, u'39', u'39')]	|




### (1) Mistake Group ['R.1.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(39,4-2)	|(52/2)! / ((52/2 - 2)! * 2!)	|[('R.1.1', 2.0, u'2', u'2!')]	|




### (1) Mistake Group ['R.0', 'R.1.0'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(39,6-5)	|C(39,6-4)	|[('R.0', 39.0, u'39', u'39'), ('R.1.0', 6.0, u'6', u'6')]	|




### (30) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:dlgoldbe

	first_attempt
					2015-10-13 01:23:40
	part5_incorrect_attempt
					('0:07:38', u'(48!)/((3!)*(48-3)!)')
	part5_correct_attempt
					['1 day, 23:14:43', u'39!/(3!*36!)']

1 Student ID:kew017

	first_attempt
					2015-10-15 18:01:46
	part5_incorrect_attempt
					('0:00:00', u'48!/(45!3!)')
	part5_correct_attempt
					['0:09:13', u'39!/(36!3!)']

2 Student ID:jfalcone

	first_attempt
					2015-10-14 22:48:45
	part5_incorrect_attempt
					('0:12:20', u'26!(4!22!)')
					('0:13:25', u'39!(4!35!)')
	part5_correct_attempt
					['0:22:00', u'39!/(4!35!)']

3 Student ID:acvuong

	first_attempt
					2015-10-13 04:39:39
	part5_incorrect_attempt
					('0:00:00', u'C(26,2)')
	part5_correct_attempt
					['0:03:22', u'C(39,2)']

4 Student ID:jjm019

	first_attempt
					2015-10-15 23:24:43
	part5_incorrect_attempt
					('0:05:05', u'4(715)')
	part5_correct_attempt
					['0:06:53', u'82251']

5 Student ID:dcrume

	first_attempt
					2015-10-14 20:25:03
	part5_incorrect_attempt
					('1 day, 2:53:43', u'C(26,2)')

6 Student ID:t2li

	first_attempt
					2015-10-14 06:36:49
	part5_incorrect_attempt
					('0:03:37', u'4C(13,2)C(39,5)')
	part5_correct_attempt
					['0:05:03', u'C(39,5)']

7 Student ID:jdeon

	first_attempt
					2015-10-11 19:36:17
	part5_incorrect_attempt
					('0:00:47', u'C(50,2)')
					('0:01:44', u'C(26,2)')
	part5_correct_attempt
					['0:05:01', u'C(39,2)']

8 Student ID:dan029

	first_attempt
					2015-10-09 22:56:33
	part5_incorrect_attempt
					('-1 day, 23:58:02', u'39*38*37*36')
	part5_correct_attempt
					['0:00:00', u'C(39,4)']

9 Student ID:gsrandha

	first_attempt
					2015-10-12 06:59:39
	part5_incorrect_attempt
					('0:07:41', u'125*20')

10 Student ID:r1gu

	first_attempt
					2015-10-15 12:15:23
	part5_incorrect_attempt
					('10:06:34', u'26!/(3!/23!)')
	part5_correct_attempt
					['10:07:22', u'39!/(3!36!)']

11 Student ID:dcgriffi

	first_attempt
					2015-10-14 07:21:07
	part5_incorrect_attempt
					('-1 day, 23:57:41', u'39*38*37')
	part5_correct_attempt
					['0:00:00', u'39!/(3!*36!)']

12 Student ID:mnrahman

	first_attempt
					2015-10-15 20:01:08
	part5_incorrect_attempt
					('0:02:20', u'4C(13,4)C(39,5-4)')
	part5_correct_attempt
					['0:03:35', u'C(39,5-4)']

13 Student ID:s6deng

	first_attempt
					2015-10-14 03:02:56
	part5_incorrect_attempt
					('0:18:59', u'C(40,3)')
	part5_correct_attempt
					['0:22:46', u'C(39,1)']

14 Student ID:rraiyyan

	first_attempt
					2015-10-14 23:50:33
	part5_incorrect_attempt
					('0:01:49', u'(13-6)*3')
					('0:04:19', u'C(52,7)-C(13,6)*4')
					('0:05:21', u'3*48/4')
	part5_correct_attempt
					['0:08:56', u'39']

15 Student ID:alhung

	first_attempt
					2015-10-15 19:54:37
	part5_incorrect_attempt
					('0:00:00', u'C(50,2)')
	part5_correct_attempt
					['0:01:34', u'C(39,2)']

16 Student ID:dsmonaha

	first_attempt
					2015-10-13 17:54:09
	part5_incorrect_attempt
					('0:08:27', u'C(12,1)*4')
	part5_correct_attempt
					['0:16:47', u'C(39,1)']

17 Student ID:tcuddy

	first_attempt
					2015-10-10 19:53:54
	part5_incorrect_attempt
					('0:02:35', u'26!/(2!*24!)')
					('0:02:46', u'39!/(2!*24!)')
	part5_correct_attempt
					['0:02:59', u'39!/(2!*37!)']

18 Student ID:djk006

	first_attempt
					2015-10-11 02:28:10
	part5_incorrect_attempt
					('-1 day, 23:56:52', u'39*38*37')
	part5_correct_attempt
					['0:01:01', u'39!/(6(36!))']

19 Student ID:m4bui

	first_attempt
					2015-10-15 22:21:07
	part5_incorrect_attempt
					('0:06:26', u'39*38*37*36')
	part5_correct_attempt
					['0:06:53', u'C(39,4)']

20 Student ID:muy002

	first_attempt
					2015-10-14 22:07:25
	part5_incorrect_attempt
					('0:00:00', u'26!(2!24!)')
	part5_correct_attempt
					['0:02:03', u'39!/(2!37!)']

21 Student ID:flhernan

	first_attempt
					2015-10-14 19:10:22
	part5_incorrect_attempt
					('0:04:07', u'49*48')
	part5_correct_attempt
					['0:04:44', u'C(52-13,2)']

22 Student ID:lahawkin

	first_attempt
					2015-10-14 05:07:36
	part5_incorrect_attempt
					('0:02:05', u'39!((39-3)!3!)')
	part5_correct_attempt
					['0:02:12', u'39!/((39-3)!3!)']

23 Student ID:qfu

	first_attempt
					2015-10-10 16:21:36
	part5_incorrect_attempt
					('0:01:26', u'9*3')
	part5_correct_attempt
					['0:04:34', u'13*3']

24 Student ID:starinia

	first_attempt
					2015-10-15 01:42:28
	part5_incorrect_attempt
					('-1 day, 23:48:19', u'39!/2!')
					('0:00:00', u'49!/(2!47!)')
					('0:17:11', u'49!/(47!)')
	part5_correct_attempt
					['2:07:00', u'C(39,2)']

25 Student ID:vasharma

	first_attempt
					2015-10-10 05:56:00
	part5_incorrect_attempt
					('0:30:56', u'13!/[2!(13-2)!]')
					('0:56:06', u'13!/[2!(13-2)!]')
	part5_correct_attempt
					['0:58:10', u'39!/[2!(39-2)!]']

26 Student ID:hsc052

	first_attempt
					2015-10-15 05:37:46
	part5_incorrect_attempt
					('0:02:15', u'C(13,3)')
	part5_correct_attempt
					['0:04:48', u'C(39,3)']

27 Student ID:yos017

	first_attempt
					2015-10-14 06:44:14
	part5_incorrect_attempt
					('0:06:18', u'26!/(2!*24!)')
					('0:07:05', u'26*25')
					('0:09:08', u'26!/(2!*24!)')
	part5_correct_attempt
					['0:10:31', u'39!/(2!*37!)']

28 Student ID:cagatep

	first_attempt
					2015-10-14 04:59:38
	part5_incorrect_attempt
					('-1 day, 23:58:12', u'50*49*48')
	part5_correct_attempt
					['0:01:16', u'C(39,3)']

29 Student ID:jhp077

	first_attempt
					2015-10-15 05:54:15
	part5_incorrect_attempt
					('0:00:00', u'48*44*40')
	part5_correct_attempt
					['0:08:54', u'13*19*37']












## Part 6

### (143) Mistake Group ['R.1'] of size 143
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*C(13,2)*C(39,7-2)	|4*13*39*C(39,5)	|[('R.1', 575757, u'C(39,7-2)', u'C(39,5)')]	|
|1	|4*C(13,2)*C(39,7-2)	|4*C(13,2)*39*C(39,5)	|[('R.1', 575757, u'C(39,7-2)', u'C(39,5)')]	|
|2	|4*C(13,4)*C(39,6-4)	|4 * C(13,4) * 39 * C(39,2)	|[('R.1', 741, u'C(39,6-4)', u'C(39,2)')]	|
|3	|4*C(13,4)*C(39,6-4)	|4 * (C(13,4)) * 39 * (C(39,2))	|[('R.1', 741, u'C(39,6-4)', u'C(39,2)')]	|
|4	|4*C(13,2)*C(39,6-2)	|20358520 -82251	|[('R.1', 82251, u'C(39,6-2)', u'82251')]	|
|5	|4*C(13,5)*C(39,7-5)	|13!/[5!(13-5)!]+39!/[2!(39-2)!]	|[('R.1', 741, u'C(39,7-5)', u'39!/[2!(39-2)!]')]	|
|6	|4*C(13,5)*C(39,7-5)	|52!/[7!(52-7)!]-39!/[2!(39-2)!]	|[('R.1', 741, u'C(39,7-5)', u'39!/[2!(39-2)!]')]	|
|7	|4*C(13,2)*C(39,4-2)	|C(13,2) * C(39,2)	|[('R.1', 741, u'C(39,4-2)', u'C(39,2)')]	|
|8	|4*C(13,2)*C(39,5-2)	|(52!/(5!*47!)) - (39!/(3!*36!))	|[('R.1', 9139, u'C(39,5-2)', u'39!/(3!*36!)')]	|
|9	|4*C(13,4)*C(39,6-4)	|13!/((13-4)!4!)+39!/((39-2)!2!)	|[('R.1', 741, u'C(39,6-4)', u'39!/((39-2)!2!)')]	|
|10	|4*C(13,4)*C(39,6-4)	|(13!/((13-4)!4!))*(39!/((39-2)!2!))	|[('R.1', 741, u'C(39,6-4)', u'39!/((39-2)!2!)')]	|
|11	|4*C(13,4)*C(39,6-4)	|715*741	|[('R.1', 741, u'C(39,6-4)', u'741')]	|
|12	|4*C(13,2)*C(39,4-2)	|(13!/(11!*2!))*(39!/(2!*37!))	|[('R.1', 741, u'C(39,4-2)', u'39!/(2!*37!)')]	|
|13	|4*C(13,3)*C(39,5-3)	|[52!/((52-5)!5!)]-741	|[('R.1', 741, u'C(39,5-3)', u'741')]	|
|14	|4*C(13,3)*C(39,5-3)	|52!/((52-5)!5!)-741	|[('R.1', 741, u'C(39,5-3)', u'741')]	|
|15	|4*C(13,2)*C(39,7-2)	|C(13,2)*C(39,5)	|[('R.1', 575757, u'C(39,7-2)', u'C(39,5)')]	|
|16	|4*C(13,2)*C(39,7-2)	|C(13,2)+C(39,5)	|[('R.1', 575757, u'C(39,7-2)', u'C(39,5)')]	|
|17	|4*C(13,3)*C(39,5-3)	|[52!/((52-5)!5!)]-[39!/(37!2!)]	|[('R.1', 741, u'C(39,5-3)', u'39!/(37!2!)')]	|
|18	|4*C(13,2)*C(39,4-2)	|[52!/(48!*4!)] * [39!/(37!*2!)]	|[('R.1', 741, u'C(39,4-2)', u'39!/(37!*2!)')]	|
|19	|4*C(13,2)*C(39,4-2)	|[52!/(48!*4!)] + [39!/(37!*2!)]	|[('R.1', 741, u'C(39,4-2)', u'39!/(37!*2!)')]	|
|20	|4*C(13,2)*C(39,4-2)	|[13!/(11!*2!)] + [39!/(37!*2!)]	|[('R.1', 741, u'C(39,4-2)', u'39!/(37!*2!)')]	|
|21	|4*C(13,2)*C(39,4-2)	|[13!/(11!*2!)] * [39!/(37!*2!)]	|[('R.1', 741, u'C(39,4-2)', u'39!/(37!*2!)')]	|
|22	|4*C(13,3)*C(39,5-3)	|(13!/(10!3!))*(39!/(37!2!))	|[('R.1', 741, u'C(39,5-3)', u'39!/(37!2!)')]	|
|23	|4*C(13,3)*C(39,5-3)	|(13!/(10!3!))+(39!/(37!2!))	|[('R.1', 741, u'C(39,5-3)', u'39!/(37!2!)')]	|
|24	|4*C(13,3)*C(39,7-3)	|C(13,3) * C(39,4)	|[('R.1', 82251, u'C(39,7-3)', u'C(39,4)')]	|
|25	|4*C(13,3)*C(39,7-3)	|C(13,3) + C(39,4)	|[('R.1', 82251, u'C(39,7-3)', u'C(39,4)')]	|
|26	|4*C(13,2)*C(39,4-2)	|78*741	|[('R.1', 741, u'C(39,4-2)', u'741')]	|
|27	|4*C(13,2)*C(39,4-2)	|[52!/(4!*48!)] - [39!/(2!*37!)]	|[('R.1', 741, u'C(39,4-2)', u'39!/(2!*37!)')]	|
|28	|4*C(13,2)*C(39,5-2)	|13*6*[39!/(3!*36!)]	|[('R.1', 9139, u'C(39,5-2)', u'39!/(3!*36!)')]	|
|29	|4*C(13,4)*C(39,6-4)	|[13!/[4!9!]]*[39!/[2!37!]]	|[('R.1', 741, u'C(39,6-4)', u'39!/[2!37!]')]	|
|30	|4*C(13,2)*C(39,5-2)	|(13!/(2!(13-2)!))(39!/(3!(39-3)!))	|[('R.1', 9139, u'C(39,5-2)', u'39!/(3!(39-3)!)')]	|
|31	|4*C(13,2)*C(39,5-2)	|78 * 9139	|[('R.1', 9139, u'C(39,5-2)', u'9139')]	|
|32	|4*C(13,3)*C(39,5-3)	|C(13,3)*C(52-13,2)	|[('R.1', 741, u'C(39,5-3)', u'C(52-13,2)')]	|
|33	|4*C(13,2)*C(39,4-2)	|4*156*741	|[('R.1', 741, u'C(39,4-2)', u'741')]	|
|34	|4*C(13,3)*C(39,5-3)	|52!/(5!(52-5)!)-39!/(2!(37!))	|[('R.1', 741, u'C(39,5-3)', u'39!/(2!(37!))')]	|
|35	|4*C(13,2)*C(39,4-2)	|[C(13,2)*C((52-13),2)]	|[('R.1', 741, u'C(39,4-2)', u'C((52-13),2)')]	|
|36	|4*C(13,2)*C(39,4-2)	|[C(13,2)+C((52-13),2)]	|[('R.1', 741, u'C(39,4-2)', u'C((52-13),2)')]	|
|37	|4*C(13,2)*C(39,4-2)	|13!/(2!(13-2)!)*(39!/(2!(39-2)!))	|[('R.1', 741, u'C(39,4-2)', u'39!/(2!(39-2)!)')]	|
|38	|4*C(13,2)*C(39,4-2)	|13*13 + C(3*13,2)	|[('R.1', 741, u'C(39,4-2)', u'C(3*13,2)')]	|
|39	|4*C(13,2)*C(39,4-2)	|C(13,2) + C(3*13,2)	|[('R.1', 741, u'C(39,4-2)', u'C(3*13,2)')]	|
|40	|4*C(13,2)*C(39,4-2)	|C(13,2) * C(3*13,2)	|[('R.1', 741, u'C(39,4-2)', u'C(3*13,2)')]	|
|41	|4*C(13,4)*C(39,6-4)	|C(13,4)+C(39,2)	|[('R.1', 741, u'C(39,6-4)', u'C(39,2)')]	|
|42	|4*C(13,4)*C(39,6-4)	|C(13,4)*C(39,2)	|[('R.1', 741, u'C(39,6-4)', u'C(39,2)')]	|
|43	|4*C(13,2)*C(39,4-2)	|4 * C(4,2) * C(39,2)	|[('R.1', 741, u'C(39,4-2)', u'C(39,2)')]	|
|44	|4*C(13,4)*C(39,7-4)	|(13!/(4!9!))*((39*38*37)/3!)	|[('R.1', 9139, u'C(39,7-4)', u'(39*38*37)/3!')]	|
|45	|4*C(13,2)*C(39,5-2)	|C(13,2)*C(13*3,3)	|[('R.1', 9139, u'C(39,5-2)', u'C(13*3,3)')]	|
|46	|4*C(13,2)*C(39,7-2)	|C(13,2) * C(3*13,5)	|[('R.1', 575757, u'C(39,7-2)', u'C(3*13,5)')]	|
|47	|4*C(13,2)*C(39,7-2)	|C(13,2) + C(3*13,5)	|[('R.1', 575757, u'C(39,7-2)', u'C(3*13,5)')]	|
|48	|4*C(13,3)*C(39,6-3)	|C(13, 3) + C(39, 3)	|[('R.1', 9139, u'C(39,6-3)', u'C(39, 3)')]	|
|49	|4*C(13,2)*C(39,4-2)	|4*[13!/(2!11!)]*13*3*[(13*3)!/(2!*37!)]	|[('R.1', 741, u'C(39,4-2)', u'(13*3)!/(2!*37!)')]	|
|50	|4*C(13,4)*C(39,6-4)	|52!/(6!46!)-39!/(2!37!)	|[('R.1', 741, u'C(39,6-4)', u'39!/(2!37!)')]	|
|51	|4*C(13,4)*C(39,6-4)	|C(52,6) - C(52-13,2)	|[('R.1', 741, u'C(39,6-4)', u'C(52-13,2)')]	|
|52	|4*C(13,4)*C(39,6-4)	|C(13,4)+C(52-13,2)	|[('R.1', 741, u'C(39,6-4)', u'C(52-13,2)')]	|
|53	|4*C(13,4)*C(39,7-4)	|4*C(13,4)*39*C(39,3)	|[('R.1', 9139, u'C(39,7-4)', u'C(39,3)')]	|
|54	|4*C(13,3)*C(39,6-3)	|286+9139	|[('R.1', 9139, u'C(39,6-3)', u'9139')]	|
|55	|4*C(13,3)*C(39,6-3)	|286*9139	|[('R.1', 9139, u'C(39,6-3)', u'9139')]	|
|56	|4*C(13,3)*C(39,7-3)	|13!/(3!10!)*(39!/(4!35!))	|[('R.1', 82251, u'C(39,7-3)', u'39!/(4!35!)')]	|
|57	|4*C(13,4)*C(39,7-4)	|715*9139	|[('R.1', 9139, u'C(39,7-4)', u'9139')]	|
|58	|4*C(13,4)*C(39,7-4)	|C(13,4) + C(39,3)	|[('R.1', 9139, u'C(39,7-4)', u'C(39,3)')]	|
|59	|4*C(13,4)*C(39,7-4)	|C(13,4)*C(39,3)	|[('R.1', 9139, u'C(39,7-4)', u'C(39,3)')]	|
|60	|4*C(13,3)*C(39,5-3)	|C(13,3) * C(39,2)	|[('R.1', 741, u'C(39,5-3)', u'C(39,2)')]	|
|61	|4*C(13,2)*C(39,4-2)	|4*78*39*741	|[('R.1', 741, u'C(39,4-2)', u'741')]	|
|62	|4*C(13,2)*C(39,6-2)	|C(52,2)*4*13*C(39,4)	|[('R.1', 82251, u'C(39,6-2)', u'C(39,4)')]	|
|63	|4*C(13,2)*C(39,5-2)	|C(13,2) * C(39,3)	|[('R.1', 9139, u'C(39,5-2)', u'C(39,3)')]	|
|64	|4*C(13,4)*C(39,7-4)	|13!/((13-4)!4!)+(39!)/((36!)(3!))	|[('R.1', 9139, u'C(39,7-4)', u'(39!)/((36!)(3!))')]	|
|65	|4*C(13,2)*C(39,4-2)	|(52!/(4!48!))(39!/(2!37!))	|[('R.1', 741, u'C(39,4-2)', u'39!/(2!37!)')]	|
|66	|4*C(13,2)*C(39,4-2)	|(52!/(4!48!))-(39!/(2!37!))	|[('R.1', 741, u'C(39,4-2)', u'39!/(2!37!)')]	|
|67	|4*C(13,2)*C(39,4-2)	|(13!/(2!11!))(39!/(2!37!))	|[('R.1', 741, u'C(39,4-2)', u'39!/(2!37!)')]	|
|68	|4*C(13,2)*C(39,6-2)	|C(13, 2)*(39!/(4!*35!))	|[('R.1', 82251, u'C(39,6-2)', u'39!/(4!*35!)')]	|
|69	|4*C(13,4)*C(39,7-4)	|(13!/(4!*9!))*(39!/(3!*36!))	|[('R.1', 9139, u'C(39,7-4)', u'39!/(3!*36!)')]	|
|70	|4*C(13,4)*C(39,7-4)	|(13!/(4!*9!))+(39!/(3!*36!))	|[('R.1', 9139, u'C(39,7-4)', u'39!/(3!*36!)')]	|
|71	|4*C(13,2)*C(39,4-2)	|C(52,4) - C(39,2)	|[('R.1', 741, u'C(39,4-2)', u'C(39,2)')]	|
|72	|4*C(13,5)*C(39,7-5)	|13!/(5!*(13-5)!) + 39!/(2!*(39-2)!)	|[('R.1', 741, u'C(39,7-5)', u'39!/(2!*(39-2)!)')]	|
|73	|4*C(13,5)*C(39,7-5)	|(13!/(5!*(13-5)!) )* (39!/(2!*(39-2)!))	|[('R.1', 741, u'C(39,7-5)', u'39!/(2!*(39-2)!)')]	|
|74	|4*C(13,3)*C(39,6-3)	|C(52,6)*C(39,3)	|[('R.1', 9139, u'C(39,6-3)', u'C(39,3)')]	|
|75	|4*C(13,5)*C(39,7-5)	|C(13,5)*5^4*39*C(39,2)	|[('R.1', 741, u'C(39,7-5)', u'C(39,2)')]	|
|76	|4*C(13,5)*C(39,7-5)	|C(13,5)*4^5*39*C(39,2)	|[('R.1', 741, u'C(39,7-5)', u'C(39,2)')]	|
|77	|4*C(13,5)*C(39,7-5)	|C(13,5)*4*39*C(39,2)	|[('R.1', 741, u'C(39,7-5)', u'C(39,2)')]	|
|78	|4*C(13,3)*C(39,5-3)	|C(13,3) + C(52-13,2)	|[('R.1', 741, u'C(39,5-3)', u'C(52-13,2)')]	|
|79	|4*C(13,3)*C(39,5-3)	|286*741	|[('R.1', 741, u'C(39,5-3)', u'741')]	|
|80	|4*C(13,3)*C(39,5-3)	|286+741	|[('R.1', 741, u'C(39,5-3)', u'741')]	|
|81	|4*C(13,2)*C(39,4-2)	|[13!/(2!*11!)] + [39!/(2!*37!)]	|[('R.1', 741, u'C(39,4-2)', u'39!/(2!*37!)')]	|
|82	|4*C(13,3)*C(39,7-3)	|286*82251	|[('R.1', 82251, u'C(39,7-3)', u'82251')]	|
|83	|4*C(13,2)*C(39,4-2)	|13!/(2!*11!)*[39!/(2!*37!)]	|[('R.1', 741, u'C(39,4-2)', u'39!/(2!*37!)')]	|
|84	|4*C(13,4)*C(39,7-4)	|4*715*39*9139	|[('R.1', 9139, u'C(39,7-4)', u'9139')]	|
|85	|4*C(13,4)*C(39,7-4)	|((13!)/((13-4)!*(4!)))*((39!)/(((39-3)!)*(3!)))	|[('R.1', 9139, u'C(39,7-4)', u'(39!)/(((39-3)!)*(3!))')]	|
|86	|4*C(13,4)*C(39,7-4)	|4*C(39,3)	|[('R.1', 9139, u'C(39,7-4)', u'C(39,3)')]	|
|87	|4*C(13,2)*C(39,6-2)	|4*(13!/(2!*11!))*3*13*(39!/(4!*35!))	|[('R.1', 82251, u'C(39,6-2)', u'39!/(4!*35!)')]	|
|88	|4*C(13,5)*C(39,7-5)	|C(13,5)*C(3*13,2)	|[('R.1', 741, u'C(39,7-5)', u'C(3*13,2)')]	|
|89	|4*C(13,4)*C(39,7-4)	|(((13!)/((13-4)!*(4!)))*((39!)/(((39-3)!)*(3!))))	|[('R.1', 9139, u'C(39,7-4)', u'(39!)/(((39-3)!)*(3!))')]	|
|90	|4*C(13,3)*C(39,5-3)	|4 * 286 * 39 * 741	|[('R.1', 741, u'C(39,5-3)', u'741')]	|
|91	|4*C(13,4)*C(39,6-4)	|(4*C(13,4)*39*C(39,2))	|[('R.1', 741, u'C(39,6-4)', u'C(39,2)')]	|
|92	|4*C(13,2)*C(39,4-2)	|C(13,2)*C(39,2)	|[('R.1', 741, u'C(39,4-2)', u'C(39,2)')]	|
|93	|4*C(13,2)*C(39,4-2)	|C(13,1)*C(12,1)*C(39,2)	|[('R.1', 741, u'C(39,4-2)', u'C(39,2)')]	|
|94	|4*C(13,2)*C(39,5-2)	|13!/(2!*11!)+39!/(3!*36!)	|[('R.1', 9139, u'C(39,5-2)', u'39!/(3!*36!)')]	|
|95	|4*C(13,2)*C(39,5-2)	|(13!/(2!*11!))*(39!/(3!*36!))	|[('R.1', 9139, u'C(39,5-2)', u'39!/(3!*36!)')]	|
|96	|4*C(13,3)*C(39,5-3)	|52!/(5!47!)-39!/(2!37!)	|[('R.1', 741, u'C(39,5-3)', u'39!/(2!37!)')]	|
|97	|4*C(13,2)*C(39,7-2)	|4*12*12/2+39!/(5!34!)	|[('R.1', 575757, u'C(39,7-2)', u'39!/(5!34!)')]	|
|98	|4*C(13,2)*C(39,7-2)	|C(13, 2)*C(39, 5)	|[('R.1', 575757, u'C(39,7-2)', u'C(39, 5)')]	|
|99	|4*C(13,2)*C(39,4-2)	|4*C(52,4)*C(39,2)	|[('R.1', 741, u'C(39,4-2)', u'C(39,2)')]	|
|100	|4*C(13,3)*C(39,7-3)	|C(13,3)*C(39,4)	|[('R.1', 82251, u'C(39,7-3)', u'C(39,4)')]	|
|101	|4*C(13,3)*C(39,7-3)	|C(13,3)+C(39,4)	|[('R.1', 82251, u'C(39,7-3)', u'C(39,4)')]	|
|102	|4*C(13,5)*C(39,7-5)	|1287*741	|[('R.1', 741, u'C(39,7-5)', u'741')]	|
|103	|4*C(13,2)*C(39,4-2)	|78+741	|[('R.1', 741, u'C(39,4-2)', u'741')]	|
|104	|4*C(13,4)*C(39,7-4)	|(1.33785E+08)-9139	|[('R.1', 9139, u'C(39,7-4)', u'9139')]	|
|105	|4*C(13,4)*C(39,7-4)	|(52!)/(7!45!) - 39!/(3!36!)	|[('R.1', 9139, u'C(39,7-4)', u'39!/(3!36!)')]	|
|106	|4*C(13,4)*C(39,7-4)	|(52!/(7!45!))*4*715*39*9139	|[('R.1', 9139, u'C(39,7-4)', u'9139')]	|
|107	|4*C(13,4)*C(39,7-4)	|C(4,1)*C(13,1)*C(39,3)	|[('R.1', 9139, u'C(39,7-4)', u'C(39,3)')]	|
|108	|4*C(13,4)*C(39,7-4)	|4(13!/((13-4)!4!))*3((39!)/((36!)(3!)))	|[('R.1', 9139, u'C(39,7-4)', u'(39!)/((36!)(3!))')]	|
|109	|4*C(13,4)*C(39,7-4)	|(13!/((13-4)!4!))*((39!)/((36!)(3!)))	|[('R.1', 9139, u'C(39,7-4)', u'(39!)/((36!)(3!))')]	|
|110	|4*C(13,4)*C(39,6-4)	|4*515*39*741	|[('R.1', 741, u'C(39,6-4)', u'741')]	|
|111	|4*C(13,4)*C(39,6-4)	|4*715*39*741	|[('R.1', 741, u'C(39,6-4)', u'741')]	|
|112	|4*C(13,4)*C(39,6-4)	|C(13,4) + C(39,2)	|[('R.1', 741, u'C(39,6-4)', u'C(39,2)')]	|
|113	|4*C(13,4)*C(39,6-4)	|C(13,4) *C(39,2)	|[('R.1', 741, u'C(39,6-4)', u'C(39,2)')]	|
|114	|4*C(13,2)*C(39,7-2)	|13!/(2!11!) * (39!/(5!34!))	|[('R.1', 575757, u'C(39,7-2)', u'39!/(5!34!)')]	|
|115	|4*C(13,2)*C(39,7-2)	|4 * 78 * 39 * 575757	|[('R.1', 575757, u'C(39,7-2)', u'575757')]	|
|116	|4*C(13,2)*C(39,5-2)	|4*78*39*9139	|[('R.1', 9139, u'C(39,5-2)', u'9139')]	|
|117	|4*C(13,4)*C(39,7-4)	|C(13,4) * C((13*3), 3)	|[('R.1', 9139, u'C(39,7-4)', u'C((13*3), 3)')]	|
|118	|4*C(13,2)*C(39,5-2)	|C(13,2)*C(39,3)	|[('R.1', 9139, u'C(39,5-2)', u'C(39,3)')]	|
|119	|4*C(13,2)*C(39,5-2)	|4*C(13,2)*39*C(39,3)	|[('R.1', 9139, u'C(39,5-2)', u'C(39,3)')]	|
|120	|4*C(13,5)*C(39,7-5)	|(C(13,5))741	|[('R.1', 741, u'C(39,7-5)', u'741')]	|
|121	|4*C(13,2)*C(39,4-2)	|39*741	|[('R.1', 741, u'C(39,4-2)', u'741')]	|




### (93) Mistake Group Digits of size 93




### (76) Mistake Group Fraction of size 76




### (66) Mistake Group redirect of size 66




### (34) Mistake Group ['R.1.1'] of size 34
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*C(13,2)*C(39,7-2)	|4*C(13,2)*33*C(33,5)	|[('R.1.1', 5.0, u'7-2', u'5')]	|
|1	|4*C(13,4)*C(39,5-4)	|C(52,5)*C(4,1)	|[('R.1.1', 1.0, u'5-4', u'1')]	|
|2	|4*C(13,4)*C(39,5-4)	|C(13,4)*C(39,1)	|[('R.1.1', 1.0, u'5-4', u'1')]	|
|3	|4*C(13,5)*C(39,7-5)	|53+C(12,7)+C(49,2)	|[('R.1.1', 2.0, u'7-5', u'2')]	|
|4	|4*C(13,4)*C(39,5-4)	|C(4,1)*C(13,1)*C(39,1)	|[('R.1.1', 1.0, u'5-4', u'1')]	|
|5	|4*C(13,4)*C(39,5-4)	|C(4,1)*13*C(39,1)	|[('R.1.1', 1.0, u'5-4', u'1')]	|
|6	|4*C(13,6)*C(39,7-6)	|C(13,6)C(39,1)	|[('R.1.1', 1.0, u'7-6', u'1')]	|
|7	|4*C(13,6)*C(39,7-6)	|C(13,6)C(4,1)	|[('R.1.1', 1.0, u'7-6', u'1')]	|
|8	|4*C(13,4)*C(39,6-4)	|13!/((13-4)!4!)*39!/((39-2)!2!)	|[('R.1.1', 2.0, u'6-4', u'2!')]	|
|9	|4*C(13,3)*C(39,4-3)	|C(4,1)*C(14,3)*C(52-14,1)	|[('R.1.1', 1.0, u'4-3', u'1')]	|
|10	|4*C(13,3)*C(39,4-3)	|C(13,3)*C(52-13,1)	|[('R.1.1', 1.0, u'4-3', u'1')]	|
|11	|4*C(13,3)*C(39,4-3)	|C(13,3)+C(52-13,1)	|[('R.1.1', 1.0, u'4-3', u'1')]	|
|12	|4*C(13,3)*C(39,4-3)	|C(13,3)-C(52-13,1)	|[('R.1.1', 1.0, u'4-3', u'1')]	|
|13	|4*C(13,3)*C(39,7-3)	|C(39,3) + C(13,4)	|[('R.1.1', 4.0, u'7-3', u'4')]	|
|14	|4*C(13,4)*C(39,5-4)	|C(52, 5) - C(39,1)	|[('R.1.1', 1.0, u'5-4', u'1')]	|
|15	|4*C(13,4)*C(39,5-4)	|C(13,4) + C(39,1)	|[('R.1.1', 1.0, u'5-4', u'1')]	|
|16	|4*C(13,4)*C(39,5-4)	|(C(52, 5)) - (C(39,1))	|[('R.1.1', 1.0, u'5-4', u'1')]	|
|17	|4*C(13,4)*C(39,5-4)	|C(13,4) * C(39,1)	|[('R.1.1', 1.0, u'5-4', u'1')]	|
|18	|4*C(13,4)*C(39,5-4)	|C(13,4)+C(12,1)	|[('R.1.1', 1.0, u'5-4', u'1')]	|
|19	|4*C(13,4)*C(39,5-4)	|C(13,4)(C(39,1))	|[('R.1.1', 1.0, u'5-4', u'1')]	|
|20	|4*C(13,3)*C(39,4-3)	|(13!/10!/3!) * (39!/38!/1!)	|[('R.1.1', 1.0, u'4-3', u'1!')]	|
|21	|4*C(13,3)*C(39,4-3)	|(13!/3!/10!) * (39!/38!/1!)	|[('R.1.1', 1.0, u'4-3', u'1!')]	|
|22	|4*C(13,3)*C(39,4-3)	|(13*12*11) * (39!/38!/1!)	|[('R.1.1', 1.0, u'4-3', u'1!')]	|
|23	|4*C(13,3)*C(39,4-3)	|(4!/3!/1!)*13*12*11 * (39!/38!/1!)	|[('R.1.1', 1.0, u'4-3', u'1!')]	|
|24	|4*C(13,2)*C(39,5-2)	|C(13,2)*13^3	|[('R.1.1', 3.0, u'5-2', u'3')]	|
|25	|4*C(13,3)*C(39,4-3)	|C(13,3)*C(39,1)	|[('R.1.1', 1.0, u'4-3', u'1')]	|
|26	|4*C(13,3)*C(39,5-3)	|39!/(37! * 2!)	|[('R.1.1', 2.0, u'5-3', u'2!')]	|
|27	|4*C(13,5)*C(39,6-5)	|C(13,5)*39*C(39,1)	|[('R.1.1', 1.0, u'6-5', u'1')]	|
|28	|4*C(13,4)*C(39,5-4)	|C(13,4)*[C(13*3,1)]	|[('R.1.1', 1.0, u'5-4', u'1')]	|




### (14) Mistake Group ['R.0'] of size 14
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*C(13,3)*C(39,4-3)	|4*C(13,3)+39	|[('R.0', 1144.0, u'4*C(13,3)', u'4*C(13,3)')]	|
|1	|4*C(13,6)*C(39,7-6)	|4 * C(13, 6) * 49	|[('R.0', 6864.0, u'4*C(13,6)', u'4 * C(13, 6)')]	|
|2	|4*C(13,2)*C(39,4-2)	|4*(13!/(2!*11!))*(39!/(2!*37))	|[('R.0', 312.0, u'4*C(13,2)', u'4*(13!/(2!*11!))')]	|
|3	|4*C(13,3)*C(39,4-3)	|C(4,1)C(13,3)+39	|[('R.0', 1144.0, u'4*C(13,3)', u'C(4,1)C(13,3)')]	|
|4	|4*C(13,3)*C(39,6-3)	|C(13, 3) * 4 + C(39, 3) * 3	|[('R.0', 1144.0, u'4*C(13,3)', u'C(13, 3) * 4')]	|
|5	|4*C(13,4)*C(39,7-4)	|4*13!/((13-4)!4!)+3*(39!)/((36!)(3!))	|[('R.0', 2860.0, u'4*C(13,4)', u'4*13!/((13-4)!4!)')]	|
|6	|4*C(13,4)*C(39,5-4)	|4*C(13,4)-39	|[('R.0', 2860.0, u'4*C(13,4)', u'4*C(13,4)')]	|
|7	|4*C(13,3)*C(39,6-3)	|C(13,3)*C(4,3)*C(13,3)	|[('R.0', 1144.0, u'4*C(13,3)', u'C(13,3)*C(4,3)')]	|
|8	|4*C(13,3)*C(39,7-3)	|4*13!/(3!10!) + 4*39!/(4!35!)	|[('R.0', 1144.0, u'4*C(13,3)', u'4*13!/(3!10!)')]	|
|9	|4*C(13,3)*C(39,7-3)	|4*13!/(3!10!) + 3*39!/(4!35!)	|[('R.0', 1144.0, u'4*C(13,3)', u'4*13!/(3!10!)')]	|
|10	|4*C(13,3)*C(39,7-3)	|(4*13!/(3!10!)) * (3*39!/(4!35!))	|[('R.0', 1144.0, u'4*C(13,3)', u'4*13!/(3!10!)')]	|
|11	|4*C(13,3)*C(39,7-3)	|(4*13!/(3!10!)) + (3*39!/(4!35!))	|[('R.0', 1144.0, u'4*C(13,3)', u'4*13!/(3!10!)')]	|
|12	|4*C(13,3)*C(39,4-3)	|(286*4)-13*3	|[('R.0', 1144.0, u'4*C(13,3)', u'286*4')]	|
|13	|4*C(13,2)*C(39,6-2)	|4*(13!/(2!11!))*(39!/4!35!)	|[('R.0', 312.0, u'4*C(13,2)', u'4*(13!/(2!11!))')]	|




### (12) Mistake Group ['R.0.1', 'R.1'] of size 12
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*C(13,5)*C(39,7-5)	|53+C(13,5)+C(39,2)	|[('R.0.1', 1287, u'C(13,5)', u'C(13,5)'), ('R.1', 741, u'C(39,7-5)', u'C(39,2)')]	|
|1	|4*C(13,3)*C(39,5-3)	|2.59896E+06 - C(13,3) - C(39, 2)	|[('R.0.1', 286, u'C(13,3)', u'C(13,3)'), ('R.1', 741, u'C(39,5-3)', u'C(39, 2)')]	|
|2	|4*C(13,3)*C(39,5-3)	|3 * C(13,3) + C(39,2)	|[('R.0.1', 286, u'C(13,3)', u'C(13,3)'), ('R.1', 741, u'C(39,5-3)', u'C(39,2)')]	|
|3	|4*C(13,3)*C(39,5-3)	|3 * C(13,3) - C(39,2)	|[('R.0.1', 286, u'C(13,3)', u'C(13,3)'), ('R.1', 741, u'C(39,5-3)', u'C(39,2)')]	|
|4	|4*C(13,2)*C(39,4-2)	|4*13*3*(13!/(2!11!)) * ((13*3)!/(2!*37!))	|[('R.0.1', 78, u'C(13,2)', u'13!/(2!11!)'), ('R.1', 741, u'C(39,4-2)', u'(13*3)!/(2!*37!)')]	|
|5	|4*C(13,2)*C(39,6-2)	|C(52,2)*4*C(13,2)*C(39,4)	|[('R.0.1', 78, u'C(13,2)', u'C(13,2)'), ('R.1', 82251, u'C(39,6-2)', u'C(39,4)')]	|
|6	|4*C(13,3)*C(39,6-3)	|C(52,6)*C(4,1)*C(13,3)*C(39,3)	|[('R.0.1', 286, u'C(13,3)', u'C(13,3)'), ('R.1', 9139, u'C(39,6-3)', u'C(39,3)')]	|
|7	|4*C(13,5)*C(39,7-5)	|4*39*1287*741	|[('R.0.1', 1287, u'C(13,5)', u'1287'), ('R.1', 741, u'C(39,7-5)', u'741')]	|
|8	|4*C(13,2)*C(39,4-2)	|((52*51*50*49)/24)(4)((13*12)/2)(39*19)	|[('R.0.1', 78, u'C(13,2)', u'(13*12)/2'), ('R.1', 741, u'C(39,4-2)', u'39*19')]	|
|9	|4*C(13,2)*C(39,7-2)	|52!/(7!(45!))*4*39*(13!/((2!)(11!)))*C(39,5)	|[('R.0.1', 78, u'C(13,2)', u'13!/((2!)(11!))'), ('R.1', 575757, u'C(39,7-2)', u'C(39,5)')]	|
|10	|4*C(13,2)*C(39,7-2)	|52!/(7!(45!))*4*(13!/((2!)(11!)))*C(39,5)	|[('R.0.1', 78, u'C(13,2)', u'13!/((2!)(11!))'), ('R.1', 575757, u'C(39,7-2)', u'C(39,5)')]	|
|11	|4*C(13,2)*C(39,4-2)	|C(52,4)*C(4,1)*C(13,2)*C(39,2)	|[('R.0.1', 78, u'C(13,2)', u'C(13,2)'), ('R.1', 741, u'C(39,4-2)', u'C(39,2)')]	|




### (11) Mistake Group ['R.0', 'R.1'] of size 11
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*C(13,3)*C(39,5-3)	|4 * C(13,3) + C(39,2)	|[('R.0', 1144.0, u'4*C(13,3)', u'4 * C(13,3)'), ('R.1', 741, u'C(39,5-3)', u'C(39,2)')]	|
|1	|4*C(13,3)*C(39,5-3)	|4 * C(13,3) - C(39,2)	|[('R.0', 1144.0, u'4*C(13,3)', u'4 * C(13,3)'), ('R.1', 741, u'C(39,5-3)', u'C(39,2)')]	|
|2	|4*C(13,5)*C(39,7-5)	|C(13,5)*C(4,1)+39!/[2!(39-2)!]	|[('R.0', 5148.0, u'4*C(13,5)', u'C(13,5)*C(4,1)'), ('R.1', 741, u'C(39,7-5)', u'39!/[2!(39-2)!]')]	|
|3	|4*C(13,2)*C(39,6-2)	|4*78+C(39,4)	|[('R.0', 312.0, u'4*C(13,2)', u'4*78'), ('R.1', 82251, u'C(39,6-2)', u'C(39,4)')]	|
|4	|4*C(13,2)*C(39,6-2)	|4*78+82251	|[('R.0', 312.0, u'4*C(13,2)', u'4*78'), ('R.1', 82251, u'C(39,6-2)', u'82251')]	|
|5	|4*C(13,2)*C(39,4-2)	|4*C(13,2) + C(3*13,2)	|[('R.0', 312.0, u'4*C(13,2)', u'4*C(13,2)'), ('R.1', 741, u'C(39,4-2)', u'C(3*13,2)')]	|
|6	|4*C(13,3)*C(39,6-3)	|C(13, 3) * 4 + C(39, 3) 	|[('R.0', 1144.0, u'4*C(13,3)', u'C(13, 3) * 4'), ('R.1', 9139, u'C(39,6-3)', u'C(39, 3)')]	|
|7	|4*C(13,3)*C(39,7-3)	|4*13!/(3!10!) + 39!/(4!35!)	|[('R.0', 1144.0, u'4*C(13,3)', u'4*13!/(3!10!)'), ('R.1', 82251, u'C(39,7-3)', u'39!/(4!35!)')]	|
|8	|4*C(13,3)*C(39,7-3)	|(4*13!/(3!10!)) + (39!/(4!35!))	|[('R.0', 1144.0, u'4*C(13,3)', u'4*13!/(3!10!)'), ('R.1', 82251, u'C(39,7-3)', u'39!/(4!35!)')]	|
|9	|4*C(13,2)*C(39,7-2)	|4*13*12/2+39!/(5!34!)	|[('R.0', 312.0, u'4*C(13,2)', u'4*13*12/2'), ('R.1', 575757, u'C(39,7-2)', u'39!/(5!34!)')]	|
|10	|4*C(13,4)*C(39,6-4)	|C(13,4)*4 + C(39,2)	|[('R.0', 2860.0, u'4*C(13,4)', u'C(13,4)*4'), ('R.1', 741, u'C(39,6-4)', u'C(39,2)')]	|




### (8) Mistake Group ['R.0.1.0'] of size 8
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*C(13,3)*C(39,5-3)	|39!/(2!*37!)*13!/(3!10!)	|[('R.0.1.0', 13.0, u'13', u'13')]	|
|1	|4*C(13,3)*C(39,5-3)	|(39!/(2!*37!))*13!/(3!10!)	|[('R.0.1.0', 13.0, u'13', u'13')]	|
|2	|4*C(13,4)*C(39,5-4)	|4*13^4*39	|[('R.0.1.0', 13.0, u'13', u'13')]	|
|3	|4*C(13,2)*C(39,5-2)	|(6*13^2*2600)	|[('R.0.1.0', 13.0, u'13', u'13')]	|
|4	|4*C(13,2)*C(39,6-2)	|39!/(4!35!) * 13!/(2!11!)	|[('R.0.1.0', 13.0, u'13', u'13')]	|
|5	|4*C(13,3)*C(39,7-3)	|4*13!/(3!10!)	|[('R.0.1.0', 13.0, u'13', u'13')]	|
|6	|4*C(13,3)*C(39,4-3)	|4*13!/(10!*3!)	|[('R.0.1.0', 13.0, u'13', u'13')]	|
|7	|4*C(13,3)*C(39,4-3)	|C(13,3) * C(4, 1)* C(13, 2) *C(4,3)	|[('R.0.1.0', 13.0, u'13', u'13')]	|




### (7) Mistake Group ['R.0.1'] of size 7
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*C(13,3)*C(39,4-3)	|4+C(13,3)+39	|[('R.0.1', 286, u'C(13,3)', u'C(13,3)')]	|
|1	|4*C(13,6)*C(39,7-6)	|C(52,7)*4*C(13,6)*(1/39)	|[('R.0.1', 1716, u'C(13,6)', u'C(13,6)')]	|
|2	|4*C(13,6)*C(39,7-6)	|C(52,7)*4*C(13,6)*(39)	|[('R.0.1', 1716, u'C(13,6)', u'C(13,6)')]	|
|3	|4*C(13,3)*C(39,5-3)	|741+39+286+4	|[('R.0.1', 286, u'C(13,3)', u'286')]	|
|4	|4*C(13,3)*C(39,5-3)	|741*39*286*4	|[('R.0.1', 286, u'C(13,3)', u'286')]	|
|5	|4*C(13,5)*C(39,6-5)	|C(52,6)*4*C(13,5)*39	|[('R.0.1', 1287, u'C(13,5)', u'C(13,5)')]	|
|6	|4*C(13,2)*C(39,6-2)	|82251*78*6	|[('R.0.1', 78, u'C(13,2)', u'78')]	|




### (6) Mistake Group Wrong_Sign of size 6




### (5) Mistake Group ['R.1.1.1'] of size 5
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*C(13,2)*C(39,5-2)	|4(13!/(11!*2!))	|[('R.1.1.1', 2.0, u'2', u'2!')]	|
|1	|4*C(13,2)*C(39,5-2)	|4*(13!/(11!*2!))	|[('R.1.1.1', 2.0, u'2', u'2!')]	|
|2	|4*C(13,2)*C(39,5-2)	|3*(13!/(11!*2!))	|[('R.1.1.1', 2.0, u'2', u'2!')]	|
|3	|4*C(13,3)*C(39,5-3)	|4*(13!/(10!*3))	|[('R.1.1.1', 3.0, u'3', u'3')]	|
|4	|4*C(13,2)*C(39,5-2)	|4 * (13!/(11!2!))	|[('R.1.1.1', 2.0, u'2', u'2!')]	|




### (5) Mistake Group ['R.0.1.0', 'R.1'] of size 5
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*C(13,5)*C(39,7-5)	|53+C(13,7)+C(39,2)	|[('R.0.1.0', 13.0, u'13', u'13'), ('R.1', 741, u'C(39,7-5)', u'C(39,2)')]	|
|1	|4*C(13,2)*C(39,4-2)	|4*(13!/(11!*2!))*(13*3)*(39!/(2!*37!))	|[('R.0.1.0', 13.0, u'13', u'13'), ('R.1', 741, u'C(39,4-2)', u'39!/(2!*37!)')]	|
|2	|4*C(13,2)*C(39,4-2)	|4*[13!/(2!11!)]*[13*3]*[(13*3)!/(2!*37!)]	|[('R.0.1.0', 13.0, u'13', u'13'), ('R.1', 741, u'C(39,4-2)', u'(13*3)!/(2!*37!)')]	|
|3	|4*C(13,2)*C(39,4-2)	|(4)((13*12)/2)(13*3)(39*19)	|[('R.0.1.0', 13.0, u'13', u'13'), ('R.1', 741, u'C(39,4-2)', u'39*19')]	|
|4	|4*C(13,4)*C(39,6-4)	|4*(13!/(4!9!))*(13*3)*(39!/(37!2))	|[('R.0.1.0', 13.0, u'13', u'13'), ('R.1', 741, u'C(39,6-4)', u'39!/(37!2)')]	|




### (4) Mistake Group ['R.0.0'] of size 4
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*C(13,5)*C(39,7-5)	|4!*C(13,5)	|[('R.0.0', 4.0, u'4', u'4')]	|
|1	|4*C(13,6)*C(39,7-6)	|4 * 3 * 13^2	|[('R.0.0', 4.0, u'4', u'4')]	|
|2	|4*C(13,5)*C(39,7-5)	|4*C(52,7)*C(13,5)	|[('R.0.0', 4.0, u'4', u'4')]	|
|3	|4*C(13,5)*C(39,7-5)	|4* C(52,7) * C(13,5)	|[('R.0.0', 4.0, u'4', u'4')]	|




### (3) Mistake Group ['R.0', 'R.1.0'] of size 3
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*C(13,2)*C(39,4-2)	|(4*78)+39*741	|[('R.0', 312.0, u'4*C(13,2)', u'4*78'), ('R.1.0', 39.0, u'39', u'39')]	|
|1	|4*C(13,2)*C(39,4-2)	|C(4,1) * C(13,2) * C(39,3)	|[('R.0', 312.0, u'4*C(13,2)', u'C(4,1) * C(13,2)'), ('R.1.0', 39.0, u'39', u'39')]	|
|2	|4*C(13,5)*C(39,7-5)	|C(13,5)*4 +39*C(39,2)	|[('R.0', 5148.0, u'4*C(13,5)', u'C(13,5)*4'), ('R.1.0', 39.0, u'39', u'39')]	|




### (3) Mistake Group ['R.0.1', 'R.1.1'] of size 3
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1', 'R.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*C(13,5)*C(39,6-5)	|C(52,6)*C(4,1)*C(13,5)*C(39,1)	|[('R.0.1', 1287, u'C(13,5)', u'C(13,5)'), ('R.1.1', 1.0, u'6-5', u'1')]	|
|1	|4*C(13,4)*C(39,7-4)	|13*19*37+4+55*13+13*3	|[('R.0.1', 715, u'C(13,4)', u'55*13'), ('R.1.1', 3.0, u'7-4', u'3')]	|
|2	|4*C(13,2)*C(39,5-2)	|C(52,5) * 4 * C(13,2) * C(13,3)	|[('R.0.1', 78, u'C(13,2)', u'C(13,2)'), ('R.1.1', 3.0, u'5-2', u'3')]	|




### (3) Mistake Group ['R.1.0'] of size 3
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*C(13,3)*C(39,4-3)	|C(13,3)*C(52-13,12)	|[('R.1.0', 39.0, u'39', u'52-13')]	|
|1	|4*C(13,2)*C(39,4-2)	|C(13,2) * C(39,3)	|[('R.1.0', 39.0, u'39', u'39')]	|
|2	|4*C(13,5)*C(39,7-5)	|((13*12*11*10*9)/52)*(39*38)	|[('R.1.0', 39.0, u'39', u'39')]	|




### (3) Mistake Group ['R.0.0', 'R.0.1.0'] of size 3
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.0.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*C(13,5)*C(39,7-5)	|4*13!/[5!(13-5)!]	|[('R.0.0', 4.0, u'4', u'4'), ('R.0.1.0', 13.0, u'13', u'13')]	|
|1	|4*C(13,5)*C(39,6-5)	|4*13!/(5!(13-5)!)	|[('R.0.0', 4.0, u'4', u'4'), ('R.0.1.0', 13.0, u'13', u'13')]	|
|2	|4*C(13,3)*C(39,5-3)	|4*13!/(3!10!)	|[('R.0.0', 4.0, u'4', u'4'), ('R.0.1.0', 13.0, u'13', u'13')]	|




### (2) Mistake Group ['R.0.0', 'R.1'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*C(13,2)*C(39,5-2)	|4*13*C(39, 3)	|[('R.0.0', 4.0, u'4', u'4'), ('R.1', 9139, u'C(39,5-2)', u'C(39, 3)')]	|
|1	|4*C(13,5)*C(39,7-5)	|4*(52-13) * C(39,2)	|[('R.0.0', 4.0, u'4', u'4'), ('R.1', 741, u'C(39,7-5)', u'C(39,2)')]	|




### (2) Mistake Group ['R.0', 'R.1.1'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*C(13,4)*C(39,7-4)	|4*C(13,4)*C(13,3)	|[('R.0', 2860.0, u'4*C(13,4)', u'4*C(13,4)'), ('R.1.1', 3.0, u'7-4', u'3')]	|
|1	|4*C(13,2)*C(39,5-2)	| 4 * C(13,2) * C(13,3)	|[('R.0', 312.0, u'4*C(13,2)', u'4 * C(13,2)'), ('R.1.1', 3.0, u'5-2', u'3')]	|




### (1) Mistake Group ['R.0.0', 'R.0.1.0', 'R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.0.1.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*C(13,3)*C(39,5-3)	|C(4, 1)* C(13, 2)* C(39, 2)	|[('R.0.0', 4.0, u'4', u'C(4, 1)'), ('R.0.1.0', 13.0, u'13', u'13'), ('R.1', 741, u'C(39,5-3)', u'C(39, 2)')]	|




### (1) Mistake Group ['R.0.0', 'R.1.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*C(13,2)*C(39,5-2)	|[4*13*C(12,3)]	|[('R.0.0', 4.0, u'4', u'4'), ('R.1.1', 3.0, u'5-2', u'3')]	|




### (1) Mistake Group ['R.0', 'R.1.1.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*C(13,2)*C(39,4-2)	|4* (13!/((13-2)!*2!)) * ((52/2)! / ((52/2 - 2)! * 2!))	|[('R.0', 312.0, u'4*C(13,2)', u'4* (13!/((13-2)!*2!))'), ('R.1.1.1', 2.0, u'2', u'2!')]	|




### (94) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:gthorn

	first_attempt
					2015-10-13 18:07:37
	part1_correct_attempt
					['0:00:00', u'C(52, 6)']
	part2_correct_attempt
					['-3 days, 10:35:37', u'4']
	part3_correct_attempt
					['0:00:00', u'C(13, 3)']
	part4_correct_attempt
					['-3 days, 10:35:37', u'39']
	part5_correct_attempt
					['0:00:00', u'C(39, 3)']
	part6_incorrect_attempt
					('0:02:25', u'C(13, 3) * 4 * C(39, 3) * 3')
	part6_correct_attempt
					['0:04:36', u'4 * C(13, 3) * C(39, 3)']

1 Student ID:apokhare

	first_attempt
					2015-10-12 21:05:11
	part1_correct_attempt
					['0:00:00', u'52!/(6!*(52-6)!)']
	part2_correct_attempt
					['-1 day, 23:45:24', u'4']
	part3_correct_attempt
					['0:05:30', u'13!/(3!*(13-3)!)']
	part4_correct_attempt
					['0:09:05', u'39']
	part5_correct_attempt
					['0:09:05', u'39!/(3!*(39-3)!)']
	part6_incorrect_attempt
					('0:24:55', u'24*(13!/((13-3)!*3!))')
	part6_correct_attempt
					['0:48:39', u'4*(13!/(3!*10!)) * (39!/(3!*36!))']

2 Student ID:ssamudra

	first_attempt
					2015-10-15 04:16:31
	part1_correct_attempt
					['0:00:00', u'52!/(47!5!)']
	part2_correct_attempt
					['-1 day, 23:16:07', u'4']
	part3_correct_attempt
					['0:00:00', u'13!/(9!4!)']
	part4_correct_attempt
					['0:02:52', u'39']
	part5_correct_attempt
					['0:02:52', u'39']
	part6_incorrect_attempt
					('0:04:49', u'(4)13!/(9!4!)')
	part6_correct_attempt
					['0:05:45', u'(39)(4)13!/(9!4!)']

3 Student ID:alakamsa

	first_attempt
					2015-10-10 20:39:47
	part1_correct_attempt
					['0:00:00', u'C(52,7)']
	part2_correct_attempt
					['0:00:00', u'4']
	part3_correct_attempt
					['0:02:01', u'C(13,6)']
	part4_correct_attempt
					['0:02:01', u'52-13']
	part5_correct_attempt
					['0:02:01', u'C(52-13,1)']
	part6_incorrect_attempt
					('0:02:01', u'C(13,6)*4')
	part6_correct_attempt
					['0:02:36', u'C(13,6)*4*C(52-13,1)']

4 Student ID:jjm019

	first_attempt
					2015-10-15 23:24:43
	part1_correct_attempt
					['0:00:00', u'20358520']
	part2_correct_attempt
					['0:00:43', u'4']
	part3_correct_attempt
					['0:03:49', u'78']
	part4_correct_attempt
					['0:06:20', u'52-13']
	part5_correct_attempt
					['0:06:53', u'82251']
	part6_incorrect_attempt
					('0:10:15', u'78*4')
	part6_correct_attempt
					['0:10:46', u'78*4*82251']

5 Student ID:mhale

	first_attempt
					2015-10-14 21:59:24
	part1_correct_attempt
					['0:00:00', u'20358520']
	part2_correct_attempt
					['0:01:37', u'4']
	part3_correct_attempt
					['0:02:59', u'1287']
	part4_correct_attempt
					['0:02:36', u'39']
	part5_correct_attempt
					['0:04:35', u'39']
	part6_incorrect_attempt
					('0:04:35', u'39 * 1287')
	part6_correct_attempt
					['0:04:47', u'39 * 1287 * 4']

6 Student ID:dkurli

	first_attempt
					2015-10-14 03:50:42
	part1_correct_attempt
					['0:00:00', u'52!/7!/45!']
	part2_correct_attempt
					['0:00:40', u'4']
	part3_correct_attempt
					['0:02:13', u'13!/10!/3!']
	part4_correct_attempt
					['0:01:59', u'39']
	part5_correct_attempt
					['0:01:59', u'39!/35!/4!']
	part6_incorrect_attempt
					('0:03:10', u'13!/10!/3!*39!/35!/4!')
					('0:05:47', u'13*12*11*4!')
					('0:06:02', u'13*12*11*4')
					('0:06:28', u'13*12*11*4*39*38*37*36')
	part6_correct_attempt
					['0:08:26', u'4*13!/10!/3!*39!/35!/4!']

7 Student ID:dkostins

	first_attempt
					2015-10-15 18:29:41
	part1_correct_attempt
					['0:00:00', u'C(52,5)']
	part2_correct_attempt
					['0:00:32', u'4']
	part3_correct_attempt
					['0:01:36', u'C(13,2)']
	part4_correct_attempt
					['0:01:06', u'39']
	part5_correct_attempt
					['0:02:26', u'C(39,3)']
	part6_incorrect_attempt
					('0:02:26', u'C(13,4)C(39,3)*4')
					('0:02:35', u'C(13,4)C(39,3)*2')
	part6_correct_attempt
					['0:02:48', u'C(13,2)C(39,3)*4']

8 Student ID:haw081

	first_attempt
					2015-10-10 23:32:20
	part1_correct_attempt
					['0:00:00', u'C(52,7)']
	part2_correct_attempt
					['0:00:00', u'4']
	part3_correct_attempt
					['0:18:08', u'C(13,6)']
	part4_correct_attempt
					['0:06:24', u'52-13']
	part5_correct_attempt
					['0:06:37', u'C(39,1)']
	part6_incorrect_attempt
					('0:30:58', u'4*C(52,6)')
					('0:31:32', u'4*C(13,6)')
					('0:31:49', u'C(4,1)*C(13,6)')
					('0:34:28', u'C(4,1)*C(13,1)^6')
	part6_correct_attempt
					['2 days, 1:13:11', u'C(4,1)*C(13,6)*C(39,1)']

9 Student ID:ffhaddad

	first_attempt
					2015-10-10 21:08:16
	part1_correct_attempt
					['0:00:00', u'C(52,4)']
	part2_correct_attempt
					['0:00:28', u'C(4,1)']
	part3_correct_attempt
					['0:01:32', u'C(13,3)']
	part4_correct_attempt
					['0:01:56', u'52-13']
	part5_correct_attempt
					['0:02:13', u'39']
	part6_incorrect_attempt
					('0:02:42', u'C(4,1)C(13,3)')
	part6_correct_attempt
					['0:02:49', u'C(4,1)C(13,3)39']

10 Student ID:mnrahman

	first_attempt
					2015-10-15 20:01:08
	part1_correct_attempt
					['0:00:00', u'C(52,6)']
	part2_correct_attempt
					['0:01:06', u'4']
	part3_correct_attempt
					['0:00:52', u'C(13,5)']
	part4_correct_attempt
					['0:03:26', u'39']
	part5_correct_attempt
					['0:03:35', u'C(39,5-4)']
	part6_incorrect_attempt
					('0:04:06', u'4C(13,4)C(39,5-4)')
					('0:04:29', u'4C(13,4)C(39,6-4)')
					('0:04:44', u'4C(13,5)C(39,6-4)')
	part6_correct_attempt
					['0:04:52', u'4C(13,5)C(39,5-4)']

11 Student ID:rlhagen

	first_attempt
					2015-10-11 18:25:10
	part1_correct_attempt
					['0:00:00', u'52!/(4!(52-4)!)']
	part2_correct_attempt
					['0:00:00', u'4']
	part3_correct_attempt
					['0:01:26', u'13!/(3!(13-3)!)']
	part4_correct_attempt
					['0:00:00', u'13*3']
	part5_correct_attempt
					['0:00:00', u'13*3']
	part6_incorrect_attempt
					('0:06:36', u'13!/(3!(13-3)!)*13*3')
					('0:07:27', u'13!/(3!(13-3)!)*4')
	part6_correct_attempt
					['0:11:54', u'13!/(3!(13-3)!)*4*13*3']

12 Student ID:btn023

	first_attempt
					2015-10-13 07:29:10
	part1_correct_attempt
					['0:00:00', u'C(52,5)']
	part2_correct_attempt
					['-1 day, 23:57:47', u'4']
	part3_correct_attempt
					['0:00:00', u'C(13,2)']
	part4_correct_attempt
					['-1 day, 23:57:47', u'13*3']
	part5_correct_attempt
					['0:00:00', u'C(13*3,3)']
	part6_incorrect_attempt
					('1 day, 0:12:27', u'C(13,2)*C(13,1)*C(13,1)*C(13,1)')
					('1 day, 0:15:27', u'C(4,1)*C(13,2)*C(3,1)*13*2*13*13')
	part6_correct_attempt
					['1 day, 15:30:34', u' 4 * C(13,2) * C(13*3,3)']

13 Student ID:lalacson

	first_attempt
					2015-10-11 22:18:21
	part1_correct_attempt
					['0:00:00', u'C(52,4)']
	part2_correct_attempt
					['0:00:00', u'4']
	part3_correct_attempt
					['0:03:38', u'C(13,3)']
	part4_correct_attempt
					['0:07:33', u'52-13']
	part5_correct_attempt
					['0:07:55', u'C(52-13,1)']
	part6_incorrect_attempt
					('0:18:00', u'C(13,3)+52-13')
					('0:22:10', u'C(13,3)')
					('0:23:05', u'C(13,3)+39')
	part6_correct_attempt
					['0:26:23', u'4*C(13,3)*C(52-13,1)']

14 Student ID:dgunawan

	first_attempt
					2015-10-14 20:53:34
	part1_correct_attempt
					['0:00:00', u'270725']
	part2_correct_attempt
					['-1 day, 23:57:16', u'13 * 4']
	part4_correct_attempt
					['-1 day, 23:57:16', u'39']
	part6_incorrect_attempt
					('22:10:56', u'C(13,1) * C(4, 4)* C(13, 1) *C(4,1)^2')

15 Student ID:tcuddy

	first_attempt
					2015-10-10 19:53:54
	part1_correct_attempt
					['0:00:00', u'52!/(5!47!)']
	part2_correct_attempt
					['0:00:35', u'4']
	part3_correct_attempt
					['0:04:04', u'13!/(3!10!)']
	part4_correct_attempt
					['0:02:35', u'13*3']
	part5_correct_attempt
					['0:02:59', u'39!/(2!*37!)']
	part6_incorrect_attempt
					('0:05:27', u'(39!/(2!*37!))*(13!/(3!10!))')
	part6_correct_attempt
					['0:05:49', u'4*(39!/(2!*37!))*(13!/(3!10!))']

16 Student ID:aysee

	first_attempt
					2015-10-13 17:56:45
	part1_correct_attempt
					['0:00:00', u'C(52,7)']
	part2_correct_attempt
					['0:00:00', u'4']
	part3_correct_attempt
					['5:17:36', u'C(13,4)']
	part4_correct_attempt
					['0:00:00', u'39']
	part5_correct_attempt
					['0:00:00', u'C(39,3)']
	part6_incorrect_attempt
					('5:17:36', u'C(39,3)*C(13,4)')
	part6_correct_attempt
					['5:18:29', u'C(4,1)*C(39,3)*C(13,4)']

17 Student ID:sayao

	first_attempt
					2015-10-12 00:47:11
	part1_correct_attempt
					['0:00:00', u'52!/((52-4)!*4!)']
	part2_correct_attempt
					['0:01:31', u'4']
	part3_correct_attempt
					['0:02:57', u'13!/(11!*2!)']
	part4_correct_attempt
					['0:03:33', u'13*3']
	part5_correct_attempt
					['0:03:33', u'39!/(2!*37!)']
	part6_incorrect_attempt
					('0:04:56', u'(4*13!/(11!*2!)*13*3*39!/(2!*37!))')
	part6_correct_attempt
					['0:14:21', u'(13!/(11!*2!))*(39!/(2!*37!))*4']

18 Student ID:anvan

	first_attempt
					2015-10-14 22:41:56
	part1_correct_attempt
					['0:00:00', u'52!/(46!6!)']
	part2_correct_attempt
					['0:00:00', u'4']
	part3_correct_attempt
					['0:04:58', u'13!/(2!11!)']
	part4_correct_attempt
					['0:00:00', u'39']
	part5_correct_attempt
					['0:00:00', u'39!/(4!35!)']
	part6_incorrect_attempt
					('0:05:53', u'13!/(2!11!) * 39!/(4!35!)')
					('0:06:58', u'39!/(4!35!)')
	part6_correct_attempt
					['2:21:51', u'39!/(4!35!) * 13!/(2!11!) * 4']

19 Student ID:csl030

	first_attempt
					2015-10-10 05:01:34
	part1_correct_attempt
					['0:00:00', u'C(52, 5)']
	part2_correct_attempt
					['0:00:12', u'4']
	part3_correct_attempt
					['0:02:06', u'C(13, 3)']
	part4_correct_attempt
					['0:02:32', u'(13 * 3)']
	part5_correct_attempt
					['0:02:46', u'C((13*3), 2)']
	part6_incorrect_attempt
					('0:06:20', u'C((13*3), 2)')
	part6_correct_attempt
					['0:15:52', u'C(13,3) * 4 * C(39,2)']

20 Student ID:m4bui

	first_attempt
					2015-10-15 22:21:07
	part1_correct_attempt
					['0:00:00', u'C(52,6)']
	part2_correct_attempt
					['-1 day, 23:44:03', u'4']
	part3_correct_attempt
					['0:03:01', u'78']
	part4_correct_attempt
					['0:04:43', u'39']
	part5_correct_attempt
					['0:06:53', u'C(39,4)']
	part6_incorrect_attempt
					('0:07:39', u'82251*79*4')
					('0:07:48', u'82251*79*6')
	part6_correct_attempt
					['0:08:07', u'82251*78*4']

21 Student ID:jguanzho

	first_attempt
					2015-10-09 20:12:02
	part1_correct_attempt
					['0:00:00', u'52!/(46! * 6!)']
	part2_correct_attempt
					['-1 day, 23:55:49', u'4']
	part3_correct_attempt
					['0:00:45', u'13! / (5! * 8!)']
	part4_correct_attempt
					['-1 day, 23:55:49', u'52-13']
	part5_correct_attempt
					['-1 day, 23:55:49', u'39']
	part6_incorrect_attempt
					('0:00:45', u'13! * 4 / (5!*8!)')
	part6_correct_attempt
					['0:01:36', u'13! * 4 * 39 / (5!*8!)']

22 Student ID:flhernan

	first_attempt
					2015-10-14 19:10:22
	part1_correct_attempt
					['0:00:00', u'C(52,5)']
	part2_correct_attempt
					['0:02:06', u'4']
	part3_correct_attempt
					['0:03:08', u'C(13,3)']
	part4_correct_attempt
					['0:04:44', u'52-13']
	part5_correct_attempt
					['0:04:44', u'C(52-13,2)']
	part6_incorrect_attempt
					('0:16:28', u'741*286')
	part6_correct_attempt
					['0:17:42', u'741*286*4']

23 Student ID:a2ahmed

	first_attempt
					2015-10-15 04:08:54
	part1_correct_attempt
					['0:00:00', u'C(52,6)']
	part2_correct_attempt
					['0:00:00', u'4']
	part3_correct_attempt
					['0:04:19', u'C(13,5)']
	part4_correct_attempt
					['0:00:00', u'39']
	part5_correct_attempt
					['0:00:00', u'39']
	part6_incorrect_attempt
					('0:07:13', u'C(52,6)-(C(13,5)*4*39)')
					('0:07:23', u'C(52,6)-((C(13,5)*4*39))')
	part6_correct_attempt
					['0:08:46', u'C(13,5)*4*39']

24 Student ID:mitopete

	first_attempt
					2015-10-13 20:20:06
	part1_correct_attempt
					['0:00:00', u'52!/(6!46!)']
	part2_correct_attempt
					['0:01:10', u'4']
	part3_correct_attempt
					['0:07:13', u'13!/(4!9!)']
	part4_correct_attempt
					['0:10:10', u'52-13']
	part5_correct_attempt
					['0:10:32', u'39!/(2!37!)']
	part6_incorrect_attempt
					('0:15:43', u'39!/(2!37!)+13!/(4!9!)')
					('0:19:36', u'39!/(2!37!)-13!/(4!9!)')
					('0:20:22', u'39!/(2!37!)+4*13!/(4!9!)')
					('0:20:34', u'39!/(2!37!)+4*(13!/(4!9!))')
					('0:20:55', u'39!/(2!37!)')
	part6_correct_attempt
					['0:27:03', u'4*(13!/(4!9!))*(39!/(2!37!))']

25 Student ID:starinia

	first_attempt
					2015-10-15 01:42:28
	part1_correct_attempt
					['0:00:00', u'52!/(4!48!)']
	part2_correct_attempt
					['-1 day, 23:45:57', u'4']
	part3_correct_attempt
					['2:07:22', u'C(13,2)']
	part4_correct_attempt
					['-1 day, 23:45:57', u'52-13']
	part5_correct_attempt
					['2:07:00', u'C(39,2)']
	part6_incorrect_attempt
					('2:07:55', u'C(13,2)')
	part6_correct_attempt
					['2:32:48', u'(4*C(13,2)*C(39,2))']

26 Student ID:tak068

	first_attempt
					2015-10-14 06:49:53
	part1_correct_attempt
					['0:00:00', u'52!/7!/(52-7)!']
	part2_correct_attempt
					['0:08:20', u'4']
	part3_correct_attempt
					['0:11:57', u'55*13']
	part4_correct_attempt
					['0:12:31', u'13*3']
	part5_correct_attempt
					['0:13:47', u'13*19*37']
	part6_incorrect_attempt
					('0:14:35', u'4*55*13*13*3*13*19*37')
	part6_correct_attempt
					['0:20:19', u'4*55*13*13*19*37']

27 Student ID:m8woo

	first_attempt
					2015-10-10 01:10:32
	part1_correct_attempt
					['0:00:00', u'C(52,7)']
	part2_correct_attempt
					['0:00:00', u'4']
	part3_correct_attempt
					['0:01:04', u'C(13,5)']
	part4_correct_attempt
					['0:00:46', u'39']
	part5_correct_attempt
					['0:00:46', u'C(39,2)']
	part6_incorrect_attempt
					('0:01:58', u'4*(C(13,5) + C(39,2))')
	part6_correct_attempt
					['0:02:24', u'4*(C(13,5) * C(39,2))']

28 Student ID:jhp077

	first_attempt
					2015-10-15 05:54:15
	part1_correct_attempt
					['0:00:00', u'2598960']
	part2_correct_attempt
					['0:05:54', u'4']
	part3_correct_attempt
					['0:03:30', u'78']
	part4_correct_attempt
					['0:08:54', u'39']
	part5_correct_attempt
					['0:08:54', u'13*19*37']
	part6_incorrect_attempt
					('0:08:54', u'13*19*37*78')
	part6_correct_attempt
					['0:09:15', u'13*19*37*78*4']

29 Student ID:lrlai

	first_attempt
					2015-10-12 19:51:30
	part1_correct_attempt
					['0:00:00', u'C(52,4)']
	part2_correct_attempt
					['0:05:03', u'4']
	part3_correct_attempt
					['0:07:35', u'C(13,3)']
	part4_correct_attempt
					['0:05:03', u'39']
	part5_correct_attempt
					['0:05:03', u'39']
	part6_incorrect_attempt
					('0:08:10', u'C(13,3)*39')
	part6_correct_attempt
					['0:08:18', u'C(13,3)*4*39']

30 Student ID:lguintu

	first_attempt
					2015-10-09 21:51:02
	part1_correct_attempt
					['0:00:00', u'C(52,5)']
	part2_correct_attempt
					['0:00:41', u'4']
	part3_correct_attempt
					['0:05:24', u'C(13,4)']
	part4_correct_attempt
					['0:01:47', u'52-13']
	part5_correct_attempt
					['0:02:02', u'C(39,1)']
	part6_incorrect_attempt
					('0:06:11', u'4*C(13,4)')
					('0:06:20', u'5*C(13,4)')
					('0:06:29', u'5!*C(13,4)')
	part6_correct_attempt
					['0:07:16', u'4*C(13,4)*C(39,1)']

31 Student ID:jjchung

	first_attempt
					2015-10-14 19:52:36
	part1_correct_attempt
					['0:00:00', u'C(52,4)']
	part2_correct_attempt
					['0:00:29', u'4']
	part3_correct_attempt
					['0:06:47', u'C(13,3)']
	part4_correct_attempt
					['0:07:31', u'39']
	part5_correct_attempt
					['0:07:41', u'C(39,1)']
	part6_incorrect_attempt
					('0:09:12', u'C(13,3)*39')
	part6_correct_attempt
					['0:09:30', u'C(13,3)*39*4']

32 Student ID:abjara

	first_attempt
					2015-10-12 10:47:42
	part1_correct_attempt
					['0:00:00', u'52!/(4!*48!)']
	part2_correct_attempt
					['0:00:00', u'4']
	part3_correct_attempt
					['0:13:30', u'13!/(2!*11!)']
	part4_correct_attempt
					['0:00:00', u'39']
	part5_correct_attempt
					['0:00:00', u'39!/(2!*37!)']
	part6_incorrect_attempt
					('0:16:38', u'13!/(2!*11!)')
					('2 days, 10:34:17', u'[13!/(11!)] ')
					('2 days, 10:34:40', u'[13!/(2!*11!)] ')
	part6_correct_attempt
					['2 days, 11:50:01', u'4*[13!/(11!*2!)] * [39!/(37!*2!)]']

33 Student ID:krau

	first_attempt
					2015-10-14 03:51:47
	part1_correct_attempt
					['0:00:00', u'52!/4!/48!']
	part2_correct_attempt
					['-1 day, 23:59:48', u'4']
	part3_correct_attempt
					['0:02:28', u'13!/10!/3!']
	part4_correct_attempt
					['0:01:10', u'39']
	part5_correct_attempt
					['0:01:31', u'39!/38!/1!']
	part6_incorrect_attempt
					('0:02:28', u'(39!/38!/1!)*4')
	part6_correct_attempt
					['0:06:02', u'4 * (13!/10!/3!) * (39!/38!/1!)']

34 Student ID:kthui

	first_attempt
					2015-10-11 08:32:42
	part1_correct_attempt
					['0:00:00', u'52!/((52-6)!6!)']
	part2_correct_attempt
					['0:02:31', u'4']
	part3_correct_attempt
					['0:07:44', u'13!/((13-4)!4!)']
	part4_correct_attempt
					['0:04:23', u'52-13']
	part5_correct_attempt
					['0:06:29', u'39!/((39-2)!2!)']
	part6_incorrect_attempt
					('0:15:23', u'2(13!/((13-4)!4!))*(39!/((39-2)!2!))')
	part6_correct_attempt
					['0:17:59', u'4(13!/((13-4)!4!))(39!/((39-2)!2!))']

35 Student ID:c2qiu

	first_attempt
					2015-10-11 09:42:51
	part1_correct_attempt
					['0:00:00', u'52!/(5!*47!)']
	part2_correct_attempt
					['0:01:27', u'4']
	part3_correct_attempt
					['0:00:00', u'13!/(10!*3!)']
	part4_correct_attempt
					['0:00:00', u'39']
	part5_correct_attempt
					['0:00:00', u'39!/(37!*2)']
	part6_incorrect_attempt
					('0:02:16', u'(13!/(10!*3))*741*4')
	part6_correct_attempt
					['0:07:44', u'847704']

36 Student ID:mrchin

	first_attempt
					2015-10-12 03:35:43
	part1_correct_attempt
					['0:00:00', u'52!/(48!*4!)']
	part2_correct_attempt
					['0:00:27', u'4']
	part3_correct_attempt
					['0:01:34', u'13!/(11!*2!)']
	part4_correct_attempt
					['0:01:57', u'52-13']
	part5_correct_attempt
					['0:02:09', u'39!/(37!*2!)']
	part6_incorrect_attempt
					('0:02:36', u'52!/(48!*4!) + 52!/(48!*4!)')
					('0:03:00', u'[52!/(48!*4!)] * [52!/(48!*4!)]')
					('0:03:08', u'[52!/(48!*4!)] + [52!/(48!*4!)]')
	part6_correct_attempt
					['2 days, 19:01:33', u'39!/(37!*2!)*4*13!/(11!*2!)']

37 Student ID:jhw015

	first_attempt
					2015-10-15 02:18:24
	part1_correct_attempt
					['0:00:00', u'C(52,7)']
	part2_correct_attempt
					['0:00:20', u'4']
	part3_correct_attempt
					['1:13:44', u'C(13,5)']
	part4_correct_attempt
					['1:43:48', u'39']
	part5_correct_attempt
					['1:43:48', u'C(39,2)']
	part6_incorrect_attempt
					('1:44:14', u'C(52,7)*C(13,5)')
					('1:44:52', u'4 * C(13,5)')
	part6_correct_attempt
					['1:45:19', u'4 * C(13,5) * C(39,2)']

38 Student ID:dsmonaha

	first_attempt
					2015-10-13 17:54:09
	part1_correct_attempt
					['0:00:00', u'C(52,5)']
	part2_correct_attempt
					['-1 day, 23:58:01', u'4']
	part3_correct_attempt
					['0:14:16', u'C(13,4)']
	part4_correct_attempt
					['0:16:31', u'13*3']
	part5_correct_attempt
					['0:16:47', u'C(39,1)']
	part6_incorrect_attempt
					('0:18:02', u'715*4*3*39')
					('0:19:25', u'C(13,4)C(4,1)C(3,1)C(39,1)')
	part6_correct_attempt
					['0:19:44', u'C(13,4)C(4,1)C(39,1)']

39 Student ID:jel075

	first_attempt
					2015-10-15 01:11:43
	part1_correct_attempt
					['0:00:00', u'52!/(48!*4!)']
	part2_correct_attempt
					['-1 day, 23:58:10', u'4']
	part3_correct_attempt
					['-1 day, 23:59:46', u'13!/(10!*3!)']
	part4_correct_attempt
					['0:00:56', u'39']
	part5_correct_attempt
					['0:00:56', u'39']
	part6_incorrect_attempt
					('0:02:01', u'39+4+13!/(10!*3!)')
					('0:09:54', u'13!/(10!*3!)')
					('0:10:24', u'(4!/3!)*(13!/(10!*3!))')
					('0:12:01', u'13!/(10!*3!)*39')
	part6_correct_attempt
					['0:12:15', u'(4!/3!)*(13!/(10!*3!))*39']

40 Student ID:w4shin

	first_attempt
					2015-10-14 02:52:19
	part1_correct_attempt
					['0:00:00', u'52!/(48!4!)']
	part2_correct_attempt
					['0:00:00', u'4']
	part3_correct_attempt
					['0:15:28', u'13!/(11!2!)']
	part4_correct_attempt
					['0:00:00', u'39']
	part5_correct_attempt
					['0:00:00', u'39!/(37!2!)']
	part6_incorrect_attempt
					('0:15:28', u'(39!/(37!2!))(50!/(48!2!))')
	part6_correct_attempt
					['0:19:49', u'4*(13!/(11!2!))*(39!/(37!2!))']

41 Student ID:muy002

	first_attempt
					2015-10-14 22:07:25
	part1_correct_attempt
					['0:00:00', u'52!/(4!48!)']
	part2_correct_attempt
					['0:00:00', u'4']
	part3_correct_attempt
					['0:00:39', u'13!/(2!11!)']
	part4_correct_attempt
					['0:01:44', u'13*3']
	part5_correct_attempt
					['0:02:03', u'39!/(2!37!)']
	part6_incorrect_attempt
					('0:02:52', u'13!/(2!11!)')
	part6_correct_attempt
					['0:13:40', u'4*13!/(2!11!)*39!/(2!37!)']

42 Student ID:jtfrankl

	first_attempt
					2015-10-15 21:03:16
	part1_correct_attempt
					['0:00:00', u'52!/(48!4!)']
	part2_correct_attempt
					['0:00:00', u'4']
	part3_correct_attempt
					['0:03:13', u'C(13,2)']
	part4_correct_attempt
					['0:00:00', u'39']
	part5_correct_attempt
					['0:00:00', u'C(39,2)']
	part6_incorrect_attempt
					('0:03:13', u'C(39,2)C(13,2)')
					('0:03:31', u'C(39,2)*C(13,2)')
	part6_correct_attempt
					['0:04:38', u'4*C(39,2)*C(13,2)']

43 Student ID:cstringh

	first_attempt
					2015-10-12 22:22:12
	part1_correct_attempt
					['0:00:00', u'52!/(4!(48!))']
	part2_correct_attempt
					['-1 day, 23:56:44', u'4']
	part3_correct_attempt
					['0:32:37', u'C(13, 3)']
	part4_correct_attempt
					['-1 day, 23:56:44', u'39']
	part5_correct_attempt
					['0:04:01', u'39!/(38!)']
	part6_incorrect_attempt
					('0:36:55', u'C(13, 3) * 4')
					('0:37:31', u'C(13, 3) ^ 4')
					('5:21:13', u'(C(13, 3) *4 )')
	part6_correct_attempt
					['5:21:32', u'(C(13, 3) *4 )*39']

44 Student ID:xil109

	first_attempt
					2015-10-10 20:32:33
	part1_correct_attempt
					['0:00:00', u'C(52,4)']
	part2_correct_attempt
					['0:01:23', u'4']
	part3_correct_attempt
					['0:01:33', u'C(13,3)']
	part4_correct_attempt
					['0:01:53', u'C(3,1)*13']
	part5_correct_attempt
					['0:02:36', u'C(39,1)']
	part6_incorrect_attempt
					('0:03:00', u'4*C(13,3)')
					('0:03:22', u'C(4,1)*C(13,3)')
	part6_correct_attempt
					['0:04:49', u'C(4,1)*C(13,3)*39']

45 Student ID:sghouse

	first_attempt
					2015-10-12 19:07:01
	part1_correct_attempt
					['0:00:00', u'52!/(5!*47!)']
	part2_correct_attempt
					['0:00:00', u'4']
	part3_correct_attempt
					['0:09:54', u'13*6']
	part4_correct_attempt
					['0:00:00', u'39']
	part5_correct_attempt
					['0:00:00', u'39!/(3!*36!)']
	part6_incorrect_attempt
					('0:09:54', u'13*6*39!/(3!*36!)')
	part6_correct_attempt
					['0:15:15', u'13*6*4*[39!/(3!*36!)]']

46 Student ID:lpettit

	first_attempt
					2015-10-14 17:22:07
	part1_correct_attempt
					['0:00:00', u'52!/(7!*(52-7)!)']
	part2_correct_attempt
					['0:00:00', u'4']
	part3_correct_attempt
					['0:03:22', u'13!/(5!*(13-5)!)']
	part4_correct_attempt
					['0:01:54', u'52-13']
	part5_correct_attempt
					['0:02:26', u'39!/(2!*(39-2)!)']
	part6_incorrect_attempt
					('2:47:11', u'(13*6*11*6*3)+(39*19*9)')
					('2:47:27', u'(13*6*11*6*3*39*19*9)')
	part6_correct_attempt
					['2:54:19', u'4*1287*741']

47 Student ID:lywong

	first_attempt
					2015-10-13 00:28:17
	part1_correct_attempt
					['0:00:00', u'52!/(4!(52-4)!)']
	part2_correct_attempt
					['0:00:31', u'4']
	part3_correct_attempt
					['0:06:03', u'13!/(2!(13-2)!)']
	part4_correct_attempt
					['0:04:56', u'39']
	part5_correct_attempt
					['0:06:31', u'39!/(2!(39-2)!)']
	part6_incorrect_attempt
					('0:09:33', u'13!/(2!(13-2)!)*39!/(2!(39-2)!)')
	part6_correct_attempt
					['0:16:42', u'4*78*741']

48 Student ID:kebao

	first_attempt
					2015-10-15 05:13:42
	part1_correct_attempt
					['0:00:00', u'52!/(47!*5!)']
	part2_correct_attempt
					['0:00:24', u'4']
	part3_correct_attempt
					['0:51:13', u'13!/(2!*11!)']
	part4_correct_attempt
					['0:51:44', u'39']
	part5_correct_attempt
					['0:56:23', u'39!/(3!*36!)']
	part6_incorrect_attempt
					('0:58:54', u'13!/(2!*11!)*39!/(3!*36!)')
	part6_correct_attempt
					['1:00:40', u'4*(13!/(2!*11!))*(39!/(3!*36!))']

49 Student ID:hkhodada

	first_attempt
					2015-10-10 18:51:37
	part1_correct_attempt
					['0:00:00', u'C(52,6)']
	part2_correct_attempt
					['1 day, 7:27:14', u'4']
	part3_correct_attempt
					['0:00:00', u'1287']
	part4_correct_attempt
					['0:00:00', u'C(39,1)']
	part5_correct_attempt
					['0:00:00', u'39']
	part6_incorrect_attempt
					('1 day, 7:27:34', u'4*C(13,5)')
					('1 day, 7:28:14', u'C(39,1)*C(13,5)')
					('1 day, 7:28:30', u'C(39,1)*C(13,8)')
	part6_correct_attempt
					['1 day, 7:30:04', u'4*C(39,1)*C(13,8)']

50 Student ID:achava

	first_attempt
					2015-10-13 07:44:33
	part1_correct_attempt
					['0:00:00', u'C(52, 5)']
	part2_correct_attempt
					['0:00:39', u'4']
	part3_correct_attempt
					['0:43:22', u'C(13,4)']
	part4_correct_attempt
					['0:44:48', u'52-13']
	part5_correct_attempt
					['0:45:02', u'C(39,1)']
	part6_incorrect_attempt
					('0:46:16', u'C(52, 5) - C(13,4)')
					('0:47:05', u'C(13,4)')
					('0:47:38', u'C(13,4)*4')
					('0:57:05', u'C(13, 4)')
					('0:57:19', u'C(13, 4) * 4')
					('0:58:58', u'C(4,1)')
					('12:04:06', u'C(4,1) * C(39,1)')
					('12:07:56', u'C(52, 4)')
					('12:08:31', u'C(13, 4)')
					('12:10:12', u'C(52, 5) + C(13,4)')
					('12:34:56', u'C(4,1) * 13')
					('12:35:13', u'C(13,1)')
					('12:36:10', u'C(13,4)')
					('12:36:24', u'C(13,4) * 4')
	part6_correct_attempt
					['12:44:06', u'(C(13,4)*4) * C(39,1)']

51 Student ID:sachadal

	first_attempt
					2015-10-14 18:02:52
	part1_correct_attempt
					['0:00:00', u'C(52,6)']
	part2_correct_attempt
					['0:00:24', u'C(4,1)']
	part3_correct_attempt
					['0:00:40', u'C(13,3)']
	part4_correct_attempt
					['0:01:13', u'39']
	part5_correct_attempt
					['0:01:13', u'C(39,3)']
	part6_incorrect_attempt
					('0:02:42', u'C(52,6)*C(4,1)*C(13,3)')
					('0:02:54', u'C(4,1)*C(13,3)')
					('0:03:09', u'C(4,1)*C(52,3)')
	part6_correct_attempt
					['0:04:05', u'C(4,1)*C(13,3)*C(39,3)']

52 Student ID:dcrume

	first_attempt
					2015-10-14 20:25:03
	part1_correct_attempt
					['0:00:00', u'270725']
	part2_correct_attempt
					['0:14:12', u'4']
	part3_correct_attempt
					['1 day, 2:53:43', u'C(13,2)']
	part6_incorrect_attempt
					('1 day, 2:53:43', u'4*C(13,2)')

53 Student ID:pvl001

	first_attempt
					2015-10-13 19:10:54
	part1_correct_attempt
					['0:00:00', u'52!/(4! * 48!)']
	part2_correct_attempt
					['0:00:31', u'4']
	part3_correct_attempt
					['0:19:45', u'78']
	part4_correct_attempt
					['0:19:02', u'39']
	part5_correct_attempt
					['0:19:13', u'741']
	part6_incorrect_attempt
					('0:20:13', u'741 * 78')
					('0:20:34', u'741 + 78')
					('0:21:17', u'52 * 12 * 39 * 38')
					('0:21:31', u'32 * 12 * 39 * 38')
	part6_correct_attempt
					['0:21:41', u'741 * 78 * 4']

54 Student ID:jcj006

	first_attempt
					2015-10-13 23:53:51
	part1_correct_attempt
					['0:00:00', u'52!/(45!7!)']
	part2_correct_attempt
					['-1 day, 20:49:45', u'4']
	part3_correct_attempt
					['0:13:56', u'13!/(3!10!)']
	part4_correct_attempt
					['-1 day, 20:49:45', u'39']
	part5_correct_attempt
					['0:06:57', u'39!/(4!35!)']
	part6_incorrect_attempt
					('0:14:37', u'13!/(3!10!)*39!/(4!35!)')
	part6_correct_attempt
					['0:15:34', u'4*13!/(3!10!)*(39!/(4!35!))']

55 Student ID:mbl003

	first_attempt
					2015-10-15 07:11:03
	part1_correct_attempt
					['0:00:00', u'52!/(4!*48!)']
	part2_correct_attempt
					['0:00:34', u'4']
	part3_correct_attempt
					['0:02:29', u'13!/(10!*3!)']
	part4_correct_attempt
					['0:03:32', u'3*13']
	part5_correct_attempt
					['0:03:32', u'39']
	part6_incorrect_attempt
					('0:03:51', u'13!/(10!*3!)*39')
	part6_correct_attempt
					['0:04:57', u'4*13!/(10!*3!)*39']

56 Student ID:ksmurlo

	first_attempt
					2015-10-13 23:19:17
	part1_correct_attempt
					['0:00:00', u'C(52,4)']
	part2_correct_attempt
					['0:00:15', u'4']
	part3_correct_attempt
					['0:03:13', u'C(13,2)']
	part4_correct_attempt
					['0:00:43', u'3*13']
	part5_correct_attempt
					['0:00:43', u'C(13*3,2)']
	part6_incorrect_attempt
					('0:05:11', u'([4*C(13,2)]*[C(13*3,2)])/4!')
					('0:05:29', u'([4*C(13,2)]*[C(13*3,2)])/4')
	part6_correct_attempt
					['0:05:51', u'([4*C(13,2)]*[C(13*3,2)])']

57 Student ID:jnatale

	first_attempt
					2015-10-13 01:16:50
	part1_correct_attempt
					['0:00:00', u'C(52,6)']
	part2_correct_attempt
					['0:01:30', u'4']
	part3_correct_attempt
					['0:07:14', u'C(13,4)']
	part4_correct_attempt
					['0:07:51', u'39']
	part5_correct_attempt
					['0:07:51', u'C(39,2)']
	part6_incorrect_attempt
					('0:09:06', u'C(13,4)')
	part6_correct_attempt
					['0:10:14', u'4*C(13,4)*C(39,2)']

58 Student ID:akhmelni

	first_attempt
					2015-10-15 22:48:11
	part1_correct_attempt
					['0:00:00', u'C(52,7)']
	part2_correct_attempt
					['0:00:42', u'4']
	part3_correct_attempt
					['0:05:03', u'C(13,4)']
	part4_correct_attempt
					['0:05:40', u'13*3']
	part5_correct_attempt
					['0:05:40', u'C((13*3), 3)']
	part6_incorrect_attempt
					('0:07:06', u'C((13*3), 3) * 4')
	part6_correct_attempt
					['0:07:21', u'C((13*3), 3) * 4 * C(13,4)']

59 Student ID:skodigal

	first_attempt
					2015-10-15 01:04:20
	part1_correct_attempt
					['0:00:00', u'C(52,7)']
	part2_correct_attempt
					['0:01:50', u'4']
	part3_correct_attempt
					['0:09:26', u'C(13,4)']
	part4_correct_attempt
					['0:08:46', u'39']
	part5_correct_attempt
					['0:08:46', u'C(39,3)']
	part6_incorrect_attempt
					('0:11:40', u'4 * C(13,4)')
					('0:15:32', u'13*4 * C(13,4)')
					('0:19:44', u'4 * C(13,4) ')
					('0:19:54', u'C(13,4) ')
					('0:20:28', u'C(13,4) *4')
	part6_correct_attempt
					['0:53:51', u'[4 *C(13,4) * C(39,3)] ']

60 Student ID:hachrist

	first_attempt
					2015-10-14 23:22:52
	part1_correct_attempt
					['0:00:00', u'52!/(47!*5!)']
	part2_correct_attempt
					['1:18:42', u'4']
	part3_correct_attempt
					['1:44:21', u'13!/(10!*3!)']
	part4_correct_attempt
					['1:59:09', u'39']
	part5_correct_attempt
					['1:59:09', u'39!/(37! * 2!)']
	part6_incorrect_attempt
					('4:23:55', u'(13!/(10!*3!))*4')
					('4:37:25', u'741+286')
					('4:37:36', u'286 * 4')
					('7:09:13', u'741 - 286')
	part6_correct_attempt
					['7:16:31', u'(39!/(37! * 2!))*4*(13!/(10!*3!))']

61 Student ID:q3wen

	first_attempt
					2015-10-14 04:28:06
	part1_correct_attempt
					['0:00:00', u'270725']
	part2_correct_attempt
					['0:02:33', u'4']
	part3_correct_attempt
					['0:10:55', u'286']
	part4_correct_attempt
					['0:06:07', u'39']
	part5_correct_attempt
					['0:10:55', u'39']
	part6_incorrect_attempt
					('0:16:47', u'286^4')
	part6_correct_attempt
					['0:17:55', u'44616']

62 Student ID:yeh013

	first_attempt
					2015-10-15 07:35:43
	part1_correct_attempt
					['0:00:00', u'52!/(48!*4!)']
	part2_correct_attempt
					['0:08:01', u'4']
	part3_correct_attempt
					['0:13:02', u'78']
	part4_correct_attempt
					['0:14:33', u'39']
	part5_correct_attempt
					['0:14:59', u'39*19']
	part6_incorrect_attempt
					('0:15:50', u'78*39*19')
	part6_correct_attempt
					['0:16:48', u'78*39*19*4']

63 Student ID:eaherman

	first_attempt
					2015-10-14 02:46:39
	part1_correct_attempt
					['0:00:00', u'C(52,4)']
	part2_correct_attempt
					['0:01:14', u'4']
	part3_correct_attempt
					['0:02:18', u'C(13, 3)']
	part4_correct_attempt
					['0:02:18', u'52-13']
	part5_correct_attempt
					['0:02:55', u'39']
	part6_incorrect_attempt
					('0:03:24', u'C(13,3)(39)')
	part6_correct_attempt
					['0:03:42', u'C(13,3)(39)4']

64 Student ID:ksrijong

	first_attempt
					2015-10-15 05:37:18
	part1_correct_attempt
					['0:00:00', u'C(52,4)']
	part2_correct_attempt
					['0:00:00', u'4']
	part3_correct_attempt
					['0:03:05', u'C(13,2)']
	part4_correct_attempt
					['0:00:00', u'39']
	part5_correct_attempt
					['0:00:00', u'C(39,2)']
	part6_incorrect_attempt
					('0:05:49', u'C(13,2)*C(13,1)*C(13,1)')
					('0:07:48', u'4*C(13,2)*3*C(13,1)*2*C(13,1)')
					('0:08:12', u'4*C(13,1)*C(12,1)*3*C(13,1)*2*C(13,1)')
					('0:13:46', u'4*C(13,2)')
	part6_correct_attempt
					['0:14:36', u'4*C(13,2)*C(39,2)']

65 Student ID:ytc012

	first_attempt
					2015-10-15 08:34:16
	part1_correct_attempt
					['0:00:00', u'52!/(7!45!)']
	part2_correct_attempt
					['0:11:42', u'4!/3!1!']
	part3_correct_attempt
					['0:11:16', u'13!/(4!9!)']
	part4_correct_attempt
					['0:08:58', u'39']
	part5_correct_attempt
					['0:12:02', u'39!/(3!36!)']
	part6_incorrect_attempt
					('0:13:37', u'(52!39!)/(3!36!7!45!)')
					('0:15:04', u'715*4')
					('0:17:05', u'7!/(4!3!)')
					('0:20:36', u'13!/(4!9!)')
					('0:20:50', u'13!4/(4!9!)')
					('0:21:02', u'13!4!/(3!4!9!)')
					('0:22:26', u'52!/(7!45!)')
					('0:22:32', u'52!/(4!48!)')
					('0:23:12', u'13!/(4!9!)')
					('0:23:55', u'13*12*11*10')
					('2:30:42', u'4*52!/(7!45!)')
	part6_correct_attempt
					['2:33:18', u'4*715*9139']

66 Student ID:klala

	first_attempt
					2015-10-12 04:18:35
	part1_correct_attempt
					['0:00:00', u'C(52,7)']
	part2_correct_attempt
					['0:00:00', u'4']
	part3_correct_attempt
					['0:01:44', u'C(13,3)']
	part4_correct_attempt
					['0:00:00', u'52-13']
	part5_correct_attempt
					['0:00:00', u'C(39,4)']
	part6_incorrect_attempt
					('0:01:44', u'C(39,3) + C(13,3)')
					('0:02:09', u'C(39,3) * C(13,3)')
					('0:02:36', u'C(39,4) * C(13,3)')
					('0:02:46', u'C(39,4) + C(13,3)')
	part6_correct_attempt
					['0:17:21', u'C(4,1) * C(13,3) * C(39,4)']

67 Student ID:t2shin

	first_attempt
					2015-10-15 05:47:08
	part1_correct_attempt
					['0:00:00', u'52!/(7!45!)']
	part2_correct_attempt
					['0:00:36', u'4']
	part3_correct_attempt
					['0:04:38', u'13!/(3!10!)']
	part4_correct_attempt
					['0:05:31', u'39']
	part5_correct_attempt
					['0:05:31', u'39!/(4!35!)']
	part6_incorrect_attempt
					('0:09:39', u'13!/(3!10!)')
					('0:10:35', u'4*(13!/(3!10!))')
					('0:17:58', u'4*13!/(3!10!) * 3*39!/(4!35!)')
	part6_correct_attempt
					['0:21:28', u'(4*13!/(3!10!)) * (39!/(4!35!))']

68 Student ID:vsamant

	first_attempt
					2015-10-10 16:50:53
	part1_correct_attempt
					['0:00:00', u'C(52,5)']
	part2_correct_attempt
					['0:04:27', u'4']
	part3_correct_attempt
					['0:10:01', u'C(13,3)']
	part4_correct_attempt
					['0:04:27', u'39']
	part5_correct_attempt
					['0:04:27', u'C(39,2)']
	part6_incorrect_attempt
					('0:10:53', u'C(4,1)*C(13,3)')
	part6_correct_attempt
					['0:12:32', u'C(4,1)*C(13,3)*C(39,2)']

69 Student ID:ppanourg

	first_attempt
					2015-10-14 23:57:31
	part1_correct_attempt
					['0:00:00', u'C(52,4)']
	part2_correct_attempt
					['0:00:00', u'4']
	part3_correct_attempt
					['0:00:00', u'C(13,3)']
	part4_correct_attempt
					['0:01:57', u'13*3']
	part5_correct_attempt
					['0:00:00', u'13*3']
	part6_incorrect_attempt
					('0:02:35', u'C(52,4)*13*3')
					('0:02:44', u'C(52,4)*4*13*3')
	part6_correct_attempt
					['0:03:25', u'4*C(13,3)*13*3']

70 Student ID:ewbrenna

	first_attempt
					2015-10-12 20:07:47
	part1_correct_attempt
					['0:00:00', u'2598960']
	part2_correct_attempt
					['0:02:13', u'4']
	part3_correct_attempt
					['0:09:08', u'13!/(4!*(13-4)!)']
	part4_correct_attempt
					['0:02:13', u'13*3']
	part5_correct_attempt
					['0:10:13', u'13*3']
	part6_incorrect_attempt
					('0:10:13', u'[(13*3)*(13!/(4!*(13-4)!))]')
	part6_correct_attempt
					['0:10:40', u'[(13*3*4)*(13!/(4!*(13-4)!))]']

71 Student ID:pcdo

	first_attempt
					2015-10-13 18:42:56
	part1_correct_attempt
					['0:00:00', u'C(52,5)']
	part2_correct_attempt
					['0:00:52', u'4']
	part3_correct_attempt
					['0:04:05', u'C(13, 4)']
	part4_correct_attempt
					['0:03:39', u'39']
	part5_correct_attempt
					['0:10:35', u'C(39,1)']
	part6_incorrect_attempt
					('1:22:20', u'C(13,4)')
					('1:26:13', u'C(4,1)*C(13,4)')
	part6_correct_attempt
					['1:26:57', u'C(4,1)*C(13,4)*C(39,1)']

72 Student ID:e9brown

	first_attempt
					2015-10-14 08:42:36
	part1_correct_attempt
					['0:00:00', u'C(52,4)']
	part2_correct_attempt
					['0:01:39', u'4']
	part3_correct_attempt
					['0:02:59', u'C(13,2)']
	part4_correct_attempt
					['0:01:39', u'52-13']
	part5_correct_attempt
					['0:01:39', u'C(39,2)']
	part6_incorrect_attempt
					('0:03:31', u'4 * C(13,2)')
	part6_correct_attempt
					['2:39:28', u'C(4,1) * C(13,2) * C(39,2)']

73 Student ID:b1green

	first_attempt
					2015-10-15 20:57:42
	part1_correct_attempt
					['0:00:00', u'C(52,5)']
	part2_correct_attempt
					['0:00:00', u'4']
	part3_correct_attempt
					['0:05:29', u'C(13,4)']
	part4_correct_attempt
					['0:00:00', u'13*3']
	part5_correct_attempt
					['0:00:00', u'13*3']
	part6_incorrect_attempt
					('0:05:29', u'C(13,4)*13*3')
					('0:07:40', u'C(13,4)')
	part6_correct_attempt
					['0:08:57', u'4*C(13,4)*13*3']

74 Student ID:p4kumar

	first_attempt
					2015-10-15 08:57:40
	part1_correct_attempt
					['0:00:00', u'270725']
	part2_correct_attempt
					['0:00:00', u'4']
	part3_correct_attempt
					['0:00:40', u'286']
	part4_correct_attempt
					['0:00:00', u'52-13']
	part5_correct_attempt
					['0:00:00', u'52-13']
	part6_incorrect_attempt
					('0:06:53', u'286 * (52 - 13)')
	part6_correct_attempt
					['0:12:13', u'286 * 4 * 39']

75 Student ID:s2chaudh

	first_attempt
					2015-10-13 01:39:30
	part1_correct_attempt
					['0:00:00', u'C(52,6)']
	part2_correct_attempt
					['0:00:00', u'4']
	part3_correct_attempt
					['0:08:47', u'C(13,4)']
	part4_correct_attempt
					['0:56:54', u'39']
	part5_correct_attempt
					['0:56:54', u'C(39,2)']
	part6_incorrect_attempt
					('0:57:23', u'C(13,4)*C(39,1)')
	part6_correct_attempt
					['17:53:51', u'(C(4,1)*C(13,4)* C(39,2))']

76 Student ID:jmiclat

	first_attempt
					2015-10-15 17:18:52
	part1_correct_attempt
					['0:00:00', u'52!/(6!(52-6)!)']
	part2_correct_attempt
					['0:00:53', u'4']
	part3_correct_attempt
					['0:02:23', u'13!/(4!9!)']
	part4_correct_attempt
					['0:09:21', u'13*3']
	part5_correct_attempt
					['0:09:49', u'39!/(37!2)']
	part6_incorrect_attempt
					('0:15:57', u'(39!/(37!2)) +(13!/(4!9!))')

77 Student ID:cfgutier

	first_attempt
					2015-10-15 21:30:31
	part1_correct_attempt
					['0:00:00', u'133784560']
	part2_correct_attempt
					['0:00:19', u'4']
	part3_correct_attempt
					['0:11:58', u'78']
	part4_correct_attempt
					['0:13:57', u'52 - 13']
	part5_correct_attempt
					['0:14:39', u'575757']
	part6_incorrect_attempt
					('0:32:28', u' 575757 * 78')
					('0:36:10', u'4 * 78')
	part6_correct_attempt
					['0:43:22', u'4 * 78 * 575757']

78 Student ID:anl114

	first_attempt
					2015-10-15 07:59:32
	part1_correct_attempt
					['0:00:00', u'133784560']
	part2_correct_attempt
					['-1 day, 23:53:22', u'4']
	part3_correct_attempt
					['0:00:00', u'1287']
	part4_correct_attempt
					['-1 day, 23:53:22', u'39']
	part5_correct_attempt
					['0:00:00', u'741']
	part6_incorrect_attempt
					('0:18:36', u'1287/13')
	part6_correct_attempt
					['0:20:20', u'1287*741*4']

79 Student ID:pnquach

	first_attempt
					2015-10-15 02:38:46
	part1_correct_attempt
					['0:00:00', u'52!/(6!*46!)']
	part2_correct_attempt
					['0:00:00', u'4']
	part3_correct_attempt
					['0:03:40', u'13!/(2!*11!)']
	part4_correct_attempt
					['0:00:00', u'3*13']
	part5_correct_attempt
					['0:00:00', u'39!/(4!*35!)']
	part6_incorrect_attempt
					('0:03:40', u'4*(13!/(2!*11!))*3*13*39!/(4!*35!)')
	part6_correct_attempt
					['0:07:21', u'4*(13!/(2!*11!))*(39!/(4!*35!))']

80 Student ID:s6deng

	first_attempt
					2015-10-14 03:02:56
	part1_correct_attempt
					['0:00:00', u'C(52,4)']
	part2_correct_attempt
					['0:05:11', u'4']
	part3_correct_attempt
					['0:14:36', u'C(13,3)']
	part4_correct_attempt
					['0:22:35', u'39']
	part5_correct_attempt
					['0:22:46', u'C(39,1)']
	part6_incorrect_attempt
					('0:31:30', u'(4!/(1!3!))*(13!/(3!10!))')
	part6_correct_attempt
					['0:43:54', u'(4!/(1!3!))*(13!/(3!10!))*(3!/(1!2!))*(13!/(1!12!))']

81 Student ID:jcl084

	first_attempt
					2015-10-13 20:28:00
	part1_correct_attempt
					['0:00:00', u'C(52,6)']
	part2_correct_attempt
					['0:02:07', u'4']
	part3_correct_attempt
					['0:02:55', u'C(13,4)']
	part4_correct_attempt
					['0:03:28', u'52-13']
	part5_correct_attempt
					['0:03:55', u'C(52-13,2)']
	part6_incorrect_attempt
					('0:07:38', u'C(52-13,2)')
	part6_correct_attempt
					['0:09:45', u'C(4,1)*C(13,4)*C(52-13,2)']

82 Student ID:aalhaida

	first_attempt
					2015-10-15 18:14:15
	part1_correct_attempt
					['0:00:00', u'270725']
	part2_correct_attempt
					['0:01:34', u'4']
	part3_correct_attempt
					['0:26:37', u'286']
	part4_correct_attempt
					['0:31:57', u'13*3']
	part5_correct_attempt
					['0:32:31', u'13*3']
	part6_incorrect_attempt
					('0:36:50', u'286*4')
	part6_correct_attempt
					['0:37:56', u'(286*4)*13*3']

83 Student ID:sippolit

	first_attempt
					2015-10-12 04:25:17
	part1_correct_attempt
					['0:00:00', u'270725']
	part2_correct_attempt
					['0:00:00', u'4']
	part3_correct_attempt
					['0:09:26', u'78']
	part4_correct_attempt
					['0:00:00', u'39']
	part5_correct_attempt
					['0:02:40', u'741']
	part6_incorrect_attempt
					('0:34:50', u'741*78')
					('0:45:49', u'741*78*4*39')
	part6_correct_attempt
					['0:46:04', u'741*78*4']

84 Student ID:mcatozzi

	first_attempt
					2015-10-14 00:22:04
	part1_correct_attempt
					['0:00:00', u'C(52,7)']
	part2_correct_attempt
					['0:01:18', u'4']
	part3_correct_attempt
					['0:05:52', u'C(13,4)']
	part4_correct_attempt
					['0:05:18', u'39']
	part5_correct_attempt
					['0:05:30', u'C(39,3)']
	part6_incorrect_attempt
					('0:07:55', u'9139+715')
	part6_correct_attempt
					['0:17:06', u'(C(13,4)*C(39,3))*4']

85 Student ID:aadhakal

	first_attempt
					2015-10-12 21:08:27
	part1_correct_attempt
					['0:00:00', u'52!/(4!*(52-4)!)']
	part2_correct_attempt
					['0:00:35', u'4']
	part3_correct_attempt
					['0:02:08', u'78']
	part4_correct_attempt
					['0:04:40', u'39']
	part5_correct_attempt
					['0:05:47', u'741']
	part6_incorrect_attempt
					('0:38:33', u'936*4')
	part6_correct_attempt
					['0:49:59', u'4*(13!/(2!*11!))*(39!/(2!*37!))']

86 Student ID:hmshah

	first_attempt
					2015-10-14 02:18:58
	part1_correct_attempt
					['0:00:00', u'C(52,6)']
	part2_correct_attempt
					['0:00:16', u'4']
	part3_correct_attempt
					['0:06:53', u'C(13,4)']
	part4_correct_attempt
					['0:07:31', u'39']
	part5_correct_attempt
					['0:08:13', u'C(39,2)']
	part6_incorrect_attempt
					('0:10:01', u'C (C(52,6), 4)')
					('0:13:39', u'C (52, 6)/13')
	part6_correct_attempt
					['0:36:49', u' (4*C(13,4)*C(39,2)) ']

87 Student ID:dtea

	first_attempt
					2015-10-15 23:21:52
	part1_correct_attempt
					['0:00:00', u'C(52,4)']
	part2_correct_attempt
					['0:00:17', u'4']
	part3_correct_attempt
					['0:04:58', u'C(13,2)']
	part4_correct_attempt
					['0:06:26', u'13*3']
	part5_correct_attempt
					['0:06:39', u'C(39,2)']
	part6_incorrect_attempt
					('0:09:30', u'78*39')
					('0:10:00', u'C(52,2)')
					('0:13:36', u'78*39')

88 Student ID:aordookh

	first_attempt
					2015-10-15 20:45:30
	part1_correct_attempt
					['0:00:00', u'C(52,6)']
	part2_correct_attempt
					['0:02:35', u'4']
	part3_correct_attempt
					['0:02:58', u'C(13,4)']
	part4_correct_attempt
					['0:02:35', u'39']
	part5_correct_attempt
					['0:02:35', u'C(39,2)']
	part6_incorrect_attempt
					('0:10:15', u'C(39,2)')
					('0:10:34', u'C(39,2)-(C(13,4))')
	part6_correct_attempt
					['0:13:29', u'4*C(39,2)*(C(13,4))']

89 Student ID:vasharma

	first_attempt
					2015-10-10 05:56:00
	part1_correct_attempt
					['0:00:00', u'52!/[7!(52-7)!]']
	part2_correct_attempt
					['0:06:36', u'4']
	part3_correct_attempt
					['0:25:55', u'13!/[5!(13-5)!]']
	part4_correct_attempt
					['0:57:46', u'39']
	part5_correct_attempt
					['0:58:10', u'39!/[2!(39-2)!]']
	part6_incorrect_attempt
					('1:01:05', u'39!/[2!(39-2)!]+13!/[5!(13-5)!]')
					('1:02:37', u'39!/[2!(39-2)!]')
					('1:11:32', u'C(4,1)*C(13,5)')
					('1:17:21', u'52!/[5!(52-5)!]')
					('1:20:56', u'C(52,5)')
					('1:21:36', u'C(13,1)C(52,5)')
					('1:22:17', u'C(13,5)C(4,1)')
	part6_correct_attempt
					['1:28:55', u'C(13,5)*C(4,1)*C(39,2)']

90 Student ID:hpc001

	first_attempt
					2015-10-14 21:38:24
	part1_correct_attempt
					['0:00:00', u'C(52, 5)']
	part2_correct_attempt
					['0:02:19', u'4']
	part3_correct_attempt
					['0:11:05', u'C(13,4)']
	part4_correct_attempt
					['0:02:19', u'13*3']
	part5_correct_attempt
					['0:12:38', u'C(13*3, 1)']
	part6_incorrect_attempt
					('0:16:12', u'715*39')
	part6_correct_attempt
					['0:18:19', u'4*715*39']

91 Student ID:syip

	first_attempt
					2015-10-11 23:17:11
	part1_correct_attempt
					['0:00:00', u'C(52,4)']
	part2_correct_attempt
					['0:00:00', u'4']
	part3_correct_attempt
					['0:02:12', u'C(13,3)']
	part4_correct_attempt
					['0:00:00', u'39']
	part5_correct_attempt
					['0:00:00', u'39']
	part6_incorrect_attempt
					('0:02:12', u'C(13,3)*39')
	part6_correct_attempt
					['0:05:26', u'4*C(13,3)*39']

92 Student ID:c3chung

	first_attempt
					2015-10-15 07:04:54
	part1_correct_attempt
					['0:00:00', u'133784500']
	part2_correct_attempt
					['-1 day, 23:52:10', u'4']
	part3_correct_attempt
					['0:09:06', u'78']
	part4_correct_attempt
					['-1 day, 23:52:10', u'39']
	part5_correct_attempt
					['0:01:16', u'575757']
	part6_incorrect_attempt
					('15:59:05', u'C(13,2)C(4,1)')
	part6_correct_attempt
					['15:59:32', u'C(13,2)C(4,1)C(39,5)']

93 Student ID:j2phung

	first_attempt
					2015-10-14 05:32:22
	part1_correct_attempt
					['0:00:00', u'52!/(4!48!)']
	part2_correct_attempt
					['-1 day, 23:53:39', u'4']
	part3_correct_attempt
					['0:01:28', u'13!/(2!11!)']
	part4_correct_attempt
					['0:03:37', u'39']
	part5_correct_attempt
					['0:04:47', u'39!/(2!37!)']
	part6_incorrect_attempt
					('1:14:11', u'(13!/(2!11!))(13!/(1!12!))(13!/(1!12!))')
					('1:23:43', u'13*6*13*(4^3)')
					('1:24:08', u'13*6*(4^3)')
					('1:25:10', u'(13!/(2!11!))*4')
	part6_correct_attempt
					['1:25:38', u'(13!/(2!11!))(39!/(2!37!))*4']












## Part 7

### (44) Mistake Group ['R.1'] of size 44
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*C(13,3)*C(39,7-3)/[C(52,7)]	|[4*13*3*13*(3*13)!/[4!(3*13-4)!]]/[52!/(7!*45!)]	|[('R.1', 133784560, u'C(52,7)', u'52!/(7!*45!)')]	|
|1	|4*C(13,3)*C(39,5-3)/[C(52,5)]	|267696/2598960	|[('R.1', 2598960, u'C(52,5)', u'2598960')]	|
|2	|4*C(13,4)*C(39,5-4)/[C(52,5)]	|4*13*13/C(52,5)	|[('R.1', 2598960, u'C(52,5)', u'C(52,5)')]	|
|3	|4*C(13,4)*C(39,5-4)/[C(52,5)]	|4*27*C(13,4)/C(52,5)	|[('R.1', 2598960, u'C(52,5)', u'C(52,5)')]	|
|4	|4*C(13,4)*C(39,5-4)/[C(52,5)]	|4*13*39*1/(52!/(5!*47!))	|[('R.1', 2598960, u'C(52,5)', u'52!/(5!*47!)')]	|
|5	|4*C(13,3)*C(39,6-3)/[C(52,6)]	|4*12*11*39*38*37/(52!/(6!46!))	|[('R.1', 20358520, u'C(52,6)', u'52!/(6!46!)')]	|
|6	|4*C(13,3)*C(39,4-3)/[C(52,4)]	|13*4*48/(52!/48!/4!)	|[('R.1', 270725, u'C(52,4)', u'52!/48!/4!')]	|
|7	|4*C(13,3)*C(39,4-3)/[C(52,4)]	|13*4*39/(52!/48!/4!)	|[('R.1', 270725, u'C(52,4)', u'52!/48!/4!')]	|
|8	|4*C(13,3)*C(39,4-3)/[C(52,4)]	|13*12*11*4*39/(52!/48!/4!)	|[('R.1', 270725, u'C(52,4)', u'52!/48!/4!')]	|
|9	|4*C(13,3)*C(39,4-3)/[C(52,4)]	|4*13*39 / C(52,4)	|[('R.1', 270725, u'C(52,4)', u'C(52,4)')]	|
|10	|4*C(13,3)*C(39,4-3)/[C(52,4)]	|C(13,3)*39 / C(52,4)	|[('R.1', 270725, u'C(52,4)', u'C(52,4)')]	|
|11	|4*C(13,4)*C(39,6-4)/[C(52,6)]	|[11*4*[13!/[2!11!] ] * 3 * 3]/[52!/[6!46!]]	|[('R.1', 20358520, u'C(52,6)', u'52!/[6!46!]')]	|
|12	|4*C(13,2)*C(39,5-2)/[C(52,5)]	|1098240 / C ( 52 , 5 )	|[('R.1', 2598960, u'C(52,5)', u'C ( 52 , 5 )')]	|
|13	|4*C(13,4)*C(39,5-4)/[C(52,5)]	|[(13*3)*(13!/(4!*(13-4)!))]/2598960	|[('R.1', 2598960, u'C(52,5)', u'2598960')]	|
|14	|4*C(13,2)*C(39,4-2)/[C(52,4)]	|(39*19)/((52*51*50*49)/24)	|[('R.1', 270725, u'C(52,4)', u'(52*51*50*49)/24')]	|
|15	|4*C(13,3)*C(39,5-3)/[C(52,5)]	|(39!/(2!(37!)))/(52!/(5!(52-5)!))	|[('R.1', 2598960, u'C(52,5)', u'52!/(5!(52-5)!)')]	|
|16	|4*C(13,3)*C(39,5-3)/[C(52,5)]	|(C(4, 1)*13*12*11*39*38)/C(52, 5)	|[('R.1', 2598960, u'C(52,5)', u'C(52, 5)')]	|
|17	|4*C(13,2)*C(39,4-2)/[C(52,4)]	|C(3*13,2) / C(52,4)	|[('R.1', 270725, u'C(52,4)', u'C(52,4)')]	|
|18	|4*C(13,2)*C(39,4-2)/[C(52,4)]	|C(4*13,2) / C(52,4)	|[('R.1', 270725, u'C(52,4)', u'C(52,4)')]	|
|19	|4*C(13,4)*C(39,6-4)/[C(52,6)]	|(4*C(13,4)*C(39,2)/(7462))/(C(52,6))	|[('R.1', 20358520, u'C(52,6)', u'C(52,6)')]	|
|20	|4*C(13,2)*C(39,5-2)/[C(52,5)]	|1098240/C(52,5)	|[('R.1', 2598960, u'C(52,5)', u'C(52,5)')]	|
|21	|4*C(13,2)*C(39,7-2)/[C(52,7)]	|C(3*13,5) / C(52,7)	|[('R.1', 133784560, u'C(52,7)', u'C(52,7)')]	|
|22	|4*C(13,3)*C(39,6-3)/[C(52,6)]	|(C(13, 3) * 4 * C(39, 3) * 3)/C(52, 6)	|[('R.1', 20358520, u'C(52,6)', u'C(52, 6)')]	|
|23	|4*C(13,4)*C(39,7-4)/[C(52,7)]	|C(39,3)*C(13,4)/C(52,7)	|[('R.1', 133784560, u'C(52,7)', u'C(52,7)')]	|
|24	|4*C(13,2)*C(39,4-2)/[C(52,4)]	|57798/270725	|[('R.1', 270725, u'C(52,4)', u'270725')]	|
|25	|4*C(13,4)*C(39,5-4)/[C(52,5)]	|27885/2598960	|[('R.1', 2598960, u'C(52,5)', u'2598960')]	|
|26	|4*C(13,4)*C(39,5-4)/[C(52,5)]	|(13*12*4)/C(52,5)	|[('R.1', 2598960, u'C(52,5)', u'C(52,5)')]	|
|27	|4*C(13,2)*C(39,4-2)/[C(52,4)]	|(39!/(37!2!))/(52!/(48!4!))	|[('R.1', 270725, u'C(52,4)', u'52!/(48!4!)')]	|
|28	|4*C(13,2)*C(39,4-2)/[C(52,4)]	|(39!/(37!2!))/(52!/(48!4!))/(52!/(48!4!))	|[('R.1', 270725, u'C(52,4)', u'52!/(48!4!)')]	|
|29	|4*C(13,2)*C(39,4-2)/[C(52,4)]	|C(39,2) / C(52,4)	|[('R.1', 270725, u'C(52,4)', u'C(52,4)')]	|
|30	|4*C(13,3)*C(39,4-3)/[C(52,4)]	|(39+4+13!/(10!*3!))/(52!/(48!*4!))	|[('R.1', 270725, u'C(52,4)', u'52!/(48!*4!)')]	|
|31	|4*C(13,2)*C(39,6-2)/[C(52,6)]	|(4*13*3*13*39!/(4!*35!))/(52!/(6!*46!))	|[('R.1', 20358520, u'C(52,6)', u'52!/(6!*46!)')]	|
|32	|4*C(13,2)*C(39,6-2)/[C(52,6)]	|(4*(13!/(2!*11!))*3*13*39!/(4!*35!))/(52!/(6!*46!))	|[('R.1', 20358520, u'C(52,6)', u'52!/(6!*46!)')]	|
|33	|4*C(13,4)*C(39,7-4)/[C(52,7)]	|((((13!)/((13-4)!*(4!)))*((39!)/(((39-3)!)*(3!))))/(7!))/((52!)/((45!)*(7!)))	|[('R.1', 133784560, u'C(52,7)', u'(52!)/((45!)*(7!))')]	|
|34	|4*C(13,2)*C(39,4-2)/[C(52,4)]	|C(52,2)/C(52,4)	|[('R.1', 270725, u'C(52,4)', u'C(52,4)')]	|
|35	|4*C(13,2)*C(39,4-2)/[C(52,4)]	|C(13,2)/C(52,4)	|[('R.1', 270725, u'C(52,4)', u'C(52,4)')]	|
|36	|4*C(13,2)*C(39,4-2)/[C(52,4)]	|[C(13,2)*C(13,1)*C(13,1)]/C(52,4)	|[('R.1', 270725, u'C(52,4)', u'C(52,4)')]	|
|37	|4*C(13,2)*C(39,5-2)/[C(52,5)]	|13*6*48*44*40/(130*51*49*8)	|[('R.1', 2598960, u'C(52,5)', u'130*51*49*8')]	|
|38	|4*C(13,2)*C(39,5-2)/[C(52,5)]	|13*19*37*78/(2598960)	|[('R.1', 2598960, u'C(52,5)', u'2598960')]	|
|39	|4*C(13,3)*C(39,5-3)/[C(52,5)]	|5148/(52!/(47!*5!))	|[('R.1', 2598960, u'C(52,5)', u'52!/(47!*5!)')]	|
|40	|4*C(13,3)*C(39,5-3)/[C(52,5)]	|1144/(52!/(47!*5!))	|[('R.1', 2598960, u'C(52,5)', u'52!/(47!*5!)')]	|
|41	|4*C(13,2)*C(39,7-2)/[C(52,7)]	|26/[C(52, 7)]	|[('R.1', 133784560, u'C(52,7)', u'C(52, 7)')]	|
|42	|4*C(13,3)*C(39,4-3)/[C(52,4)]	|858/270725	|[('R.1', 270725, u'C(52,4)', u'270725')]	|
|43	|4*C(13,4)*C(39,5-4)/[C(52,5)]	|[C(13,4)*13*3]/C(52,5)	|[('R.1', 2598960, u'C(52,5)', u'C(52,5)')]	|




### (38) Mistake Group ['R.0.1', 'R.1'] of size 38
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*C(13,2)*C(39,7-2)/[C(52,7)]	|4*13*39*C(39,5)/C(52,7)	|[('R.0.1', 575757, u'C(39,7-2)', u'C(39,5)'), ('R.1', 133784560, u'C(52,7)', u'C(52,7)')]	|
|1	|4*C(13,2)*C(39,7-2)/[C(52,7)]	|4*C(13,2)*39*C(39,5)/C(52,7)	|[('R.0.1', 575757, u'C(39,7-2)', u'C(39,5)'), ('R.1', 133784560, u'C(52,7)', u'C(52,7)')]	|
|2	|4*C(13,4)*C(39,6-4)/[C(52,6)]	|[4 * C(13,4) * 39 * C(39,2)] / [C(52,6)]	|[('R.0.1', 741, u'C(39,6-4)', u'C(39,2)'), ('R.1', 20358520, u'C(52,6)', u'C(52,6)')]	|
|3	|4*C(13,4)*C(39,6-4)/[C(52,6)]	|[4 * (C(13,4)) * 39 * (C(39,2))] / [C(52,6)]	|[('R.0.1', 741, u'C(39,6-4)', u'C(39,2)'), ('R.1', 20358520, u'C(52,6)', u'C(52,6)')]	|
|4	|4*C(13,2)*C(39,4-2)/[C(52,4)]	|(C(13,2) * C(39,2))/(C(52,4))	|[('R.0.1', 741, u'C(39,4-2)', u'C(39,2)'), ('R.1', 270725, u'C(52,4)', u'C(52,4)')]	|
|5	|4*C(13,2)*C(39,7-2)/[C(52,7)]	|(C(13,2)*C(39,5))/C(52,7)	|[('R.0.1', 575757, u'C(39,7-2)', u'C(39,5)'), ('R.1', 133784560, u'C(52,7)', u'C(52,7)')]	|
|6	|4*C(13,2)*C(39,7-2)/[C(52,7)]	|(C(13,2)+C(39,5))/C(52,7)	|[('R.0.1', 575757, u'C(39,7-2)', u'C(39,5)'), ('R.1', 133784560, u'C(52,7)', u'C(52,7)')]	|
|7	|4*C(13,2)*C(39,4-2)/[C(52,4)]	|(C(13,2) + C(3*13,2)) / C(52,4)	|[('R.0.1', 741, u'C(39,4-2)', u'C(3*13,2)'), ('R.1', 270725, u'C(52,4)', u'C(52,4)')]	|
|8	|4*C(13,2)*C(39,4-2)/[C(52,4)]	|(C(13,2) * C(3*13,2)) / C(52,4)	|[('R.0.1', 741, u'C(39,4-2)', u'C(3*13,2)'), ('R.1', 270725, u'C(52,4)', u'C(52,4)')]	|
|9	|4*C(13,2)*C(39,4-2)/[C(52,4)]	|(4 * C(4,2) * C(39,2))/C(52,4)	|[('R.0.1', 741, u'C(39,4-2)', u'C(39,2)'), ('R.1', 270725, u'C(52,4)', u'C(52,4)')]	|
|10	|4*C(13,2)*C(39,5-2)/[C(52,5)]	|C(13,2)*C(13*3,3)/C(52,5)	|[('R.0.1', 9139, u'C(39,5-2)', u'C(13*3,3)'), ('R.1', 2598960, u'C(52,5)', u'C(52,5)')]	|
|11	|4*C(13,2)*C(39,7-2)/[C(52,7)]	|C(13,2) * C(3*13,5) / C(52,7)	|[('R.0.1', 575757, u'C(39,7-2)', u'C(3*13,5)'), ('R.1', 133784560, u'C(52,7)', u'C(52,7)')]	|
|12	|4*C(13,3)*C(39,6-3)/[C(52,6)]	|(C(13, 3) + C(39, 3))/C(52, 6)	|[('R.0.1', 9139, u'C(39,6-3)', u'C(39, 3)'), ('R.1', 20358520, u'C(52,6)', u'C(52, 6)')]	|
|13	|4*C(13,2)*C(39,4-2)/[C(52,4)]	|4*13*13*3*[(13*3)!/(2!*37!)]/[52!/(48!*4!)]	|[('R.0.1', 741, u'C(39,4-2)', u'(13*3)!/(2!*37!)'), ('R.1', 270725, u'C(52,4)', u'52!/(48!*4!)')]	|
|14	|4*C(13,2)*C(39,4-2)/[C(52,4)]	|4*[13!/(2!11!)]*13*3*[(13*3)!/(2!*37!)]/[52!/(48!*4!)]	|[('R.0.1', 741, u'C(39,4-2)', u'(13*3)!/(2!*37!)'), ('R.1', 270725, u'C(52,4)', u'52!/(48!*4!)')]	|
|15	|4*C(13,4)*C(39,7-4)/[C(52,7)]	|4*C(13,4)*39*C(39,3) / (52!/(45!7!))	|[('R.0.1', 9139, u'C(39,7-4)', u'C(39,3)'), ('R.1', 133784560, u'C(52,7)', u'52!/(45!7!)')]	|
|16	|4*C(13,4)*C(39,7-4)/[C(52,7)]	|((13!/(4!*9!))*(39!/(3!*36!)))/(52!/(7!(52-7)!))	|[('R.0.1', 9139, u'C(39,7-4)', u'39!/(3!*36!)'), ('R.1', 133784560, u'C(52,7)', u'52!/(7!(52-7)!)')]	|
|17	|4*C(13,4)*C(39,7-4)/[C(52,7)]	|((13!/(4!*9!))+(39!/(3!*36!)))/(52!/(7!(52-7)!))	|[('R.0.1', 9139, u'C(39,7-4)', u'39!/(3!*36!)'), ('R.1', 133784560, u'C(52,7)', u'52!/(7!(52-7)!)')]	|
|18	|4*C(13,2)*C(39,4-2)/[C(52,4)]	|(C(52,4) - C(39,2)) / C(52,4)	|[('R.0.1', 741, u'C(39,4-2)', u'C(39,2)'), ('R.1', 270725, u'C(52,4)', u'C(52,4)')]	|
|19	|4*C(13,5)*C(39,7-5)/[C(52,7)]	|C(13,5)*5^4*39*C(39,2)/C(52,7)	|[('R.0.1', 741, u'C(39,7-5)', u'C(39,2)'), ('R.1', 133784560, u'C(52,7)', u'C(52,7)')]	|
|20	|4*C(13,5)*C(39,7-5)/[C(52,7)]	|C(13,5)*4^5*39*C(39,2)/C(52,7)	|[('R.0.1', 741, u'C(39,7-5)', u'C(39,2)'), ('R.1', 133784560, u'C(52,7)', u'C(52,7)')]	|
|21	|4*C(13,5)*C(39,7-5)/[C(52,7)]	|C(13,5)*4*39*C(39,2)/C(52,7)	|[('R.0.1', 741, u'C(39,7-5)', u'C(39,2)'), ('R.1', 133784560, u'C(52,7)', u'C(52,7)')]	|
|22	|4*C(13,3)*C(39,7-3)/[C(52,7)]	|286*82251/(52!/(7!45!))	|[('R.0.1', 82251, u'C(39,7-3)', u'82251'), ('R.1', 133784560, u'C(52,7)', u'52!/(7!45!)')]	|
|23	|4*C(13,2)*C(39,6-2)/[C(52,6)]	|(4*(13!/(2!*11!))*3*13*(39!/(4!*35!)))/(52!/(6!*46!))	|[('R.0.1', 82251, u'C(39,6-2)', u'39!/(4!*35!)'), ('R.1', 20358520, u'C(52,6)', u'52!/(6!*46!)')]	|
|24	|4*C(13,3)*C(39,5-3)/[C(52,5)]	|((13!/(10!*3!))*(39!/(37! * 2!)))/(52!/(47!*5!))	|[('R.0.1', 741, u'C(39,5-3)', u'39!/(37! * 2!)'), ('R.1', 2598960, u'C(52,5)', u'52!/(47!*5!)')]	|
|25	|4*C(13,3)*C(39,5-3)/[C(52,5)]	|(4 * 286 * 39 * 741)/ (52!/(47!*5!))	|[('R.0.1', 741, u'C(39,5-3)', u'741'), ('R.1', 2598960, u'C(52,5)', u'52!/(47!*5!)')]	|
|26	|4*C(13,4)*C(39,6-4)/[C(52,6)]	|(4*C(13,4)*39*C(39,2))/C(52,6)	|[('R.0.1', 741, u'C(39,6-4)', u'C(39,2)'), ('R.1', 20358520, u'C(52,6)', u'C(52,6)')]	|
|27	|4*C(13,2)*C(39,4-2)/[C(52,4)]	|[C(13,2)*C(39,2)]/C(52,4)	|[('R.0.1', 741, u'C(39,4-2)', u'C(39,2)'), ('R.1', 270725, u'C(52,4)', u'C(52,4)')]	|
|28	|4*C(13,2)*C(39,7-2)/[C(52,7)]	|[C(13, 2)*C(39, 5)]/[C(52, 7)]	|[('R.0.1', 575757, u'C(39,7-2)', u'C(39, 5)'), ('R.1', 133784560, u'C(52,7)', u'C(52, 7)')]	|
|29	|4*C(13,3)*C(39,7-3)/[C(52,7)]	|C(13,3)*C(39,4)/C(52,7)	|[('R.0.1', 82251, u'C(39,7-3)', u'C(39,4)'), ('R.1', 133784560, u'C(52,7)', u'C(52,7)')]	|
|30	|4*C(13,3)*C(39,7-3)/[C(52,7)]	|(C(13,3)+C(39,4))/C(52,7)	|[('R.0.1', 82251, u'C(39,7-3)', u'C(39,4)'), ('R.1', 133784560, u'C(52,7)', u'C(52,7)')]	|
|31	|4*C(13,5)*C(39,7-5)/[C(52,7)]	|1287*741/133784560	|[('R.0.1', 741, u'C(39,7-5)', u'741'), ('R.1', 133784560, u'C(52,7)', u'133784560')]	|
|32	|4*C(13,4)*C(39,6-4)/[C(52,6)]	|(715+741)/2.03585E+07	|[('R.0.1', 741, u'C(39,6-4)', u'741'), ('R.1', 20358520, u'C(52,6)', u'2.03585E+0')]	|
|33	|4*C(13,4)*C(39,7-4)/[C(52,7)]	|715*9139/(52!/(7!45!))	|[('R.0.1', 9139, u'C(39,7-4)', u'9139'), ('R.1', 133784560, u'C(52,7)', u'52!/(7!45!)')]	|
|34	|4*C(13,4)*C(39,6-4)/[C(52,6)]	|(C(13,4) + C(39,2))/C(52,6)	|[('R.0.1', 741, u'C(39,6-4)', u'C(39,2)'), ('R.1', 20358520, u'C(52,6)', u'C(52,6)')]	|
|35	|4*C(13,5)*C(39,7-5)/[C(52,7)]	|((C(13,5))741)/C(52,7)	|[('R.0.1', 741, u'C(39,7-5)', u'741'), ('R.1', 133784560, u'C(52,7)', u'C(52,7)')]	|




### (37) Mistake Group redirect of size 37




### (10) Mistake Group ['R.0'] of size 10
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*C(13,4)*C(39,5-4)/[C(52,5)]	|(4*39*13!/(4!(13-4)!))/(52!/(5!*44!))	|[('R.0', 111540.0, u'4*C(13,4)*C(39,5-4)', u'4*39*13!/(4!(13-4)!)')]	|
|1	|4*C(13,4)*C(39,5-4)/[C(52,5)]	|111540/111540	|[('R.0', 111540.0, u'4*C(13,4)*C(39,5-4)', u'111540')]	|
|2	|4*C(13,2)*C(39,4-2)/[C(52,4)]	|(13*12*39*38)/(52*51*50*49)	|[('R.0', 231192.0, u'4*C(13,2)*C(39,4-2)', u'13*12*39*38')]	|
|3	|4*C(13,4)*C(39,6-4)/[C(52,6)]	|4*C(13,4)*C(39,2)/(52*51*50*49*48*47)	|[('R.0', 2119260.0, u'4*C(13,4)*C(39,6-4)', u'4*C(13,4)*C(39,2)')]	|
|4	|4*C(13,4)*C(39,6-4)/[C(52,6)]	|4*C(13,4)*C(39,2)/(7462)	|[('R.0', 2119260.0, u'4*C(13,4)*C(39,6-4)', u'4*C(13,4)*C(39,2)')]	|
|5	|4*C(13,2)*C(39,4-2)/[C(52,4)]	|(4*(13!/(11!2!))*(39!/(37!2!)))/(4*(13!/(11!2!))*(39!/(37!2!)))	|[('R.0', 231192.0, u'4*C(13,2)*C(39,4-2)', u'4*(13!/(11!2!))*(39!/(37!2!))')]	|
|6	|4*C(13,3)*C(39,4-3)/[C(52,4)]	|[(4!/(1!3!))*(13!/(3!10!))*(3!/(1!2!))*(13!/(1!12!))]/(52!/4!)	|[('R.0', 44616.0, u'4*C(13,3)*C(39,4-3)', u'(4!/(1!3!))*(13!/(3!10!))*(3!/(1!2!))*(13!/(1!12!))')]	|
|7	|4*C(13,4)*C(39,7-4)/[C(52,7)]	|4*715*9139/(51!/(7!45!))	|[('R.0', 26137540.0, u'4*C(13,4)*C(39,7-4)', u'4*715*9139')]	|
|8	|4*C(13,2)*C(39,6-2)/[C(52,6)]	|(4*(13!/(2!11!))*(39!/(4!35!)))/(39!/(4!35!))	|[('R.0', 25662312.0, u'4*C(13,2)*C(39,6-2)', u'4*(13!/(2!11!))*(39!/(4!35!))')]	|
|9	|4*C(13,4)*C(39,5-4)/[C(52,5)]	|715*4*39/289860	|[('R.0', 111540.0, u'4*C(13,4)*C(39,5-4)', u'715*4*39')]	|




### (10) Mistake Group ['R.0.1.1', 'R.1'] of size 10
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1.1', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*C(13,2)*C(39,7-2)/[C(52,7)]	|4*C(13,2)*33*C(33,5)/C(52,7)	|[('R.0.1.1', 5.0, u'7-2', u'5'), ('R.1', 133784560, u'C(52,7)', u'C(52,7)')]	|
|1	|4*C(13,5)*C(39,6-5)/[C(52,6)]	|C(13,5)*C(39,1)/[C(52,6)]	|[('R.0.1.1', 1.0, u'6-5', u'1'), ('R.1', 20358520, u'C(52,6)', u'C(52,6)')]	|
|2	|4*C(13,4)*C(39,5-4)/[C(52,5)]	|C(4,1)*C(13,1)*C(39,1)/C(52,5)	|[('R.0.1.1', 1.0, u'5-4', u'1'), ('R.1', 2598960, u'C(52,5)', u'C(52,5)')]	|
|3	|4*C(13,4)*C(39,5-4)/[C(52,5)]	|C(4,1)*13*C(39,1)/C(52,5)	|[('R.0.1.1', 1.0, u'5-4', u'1'), ('R.1', 2598960, u'C(52,5)', u'C(52,5)')]	|
|4	|4*C(13,6)*C(39,7-6)/[C(52,7)]	|[13*12*10*11*4*C(25-13,1)]/[C(52,7)]	|[('R.0.1.1', 1.0, u'7-6', u'1'), ('R.1', 133784560, u'C(52,7)', u'C(52,7)')]	|
|5	|4*C(13,6)*C(39,7-6)/[C(52,7)]	|[C(13,4)*4*C(25-13,1)]/[C(52,7)]	|[('R.0.1.1', 1.0, u'7-6', u'1'), ('R.1', 133784560, u'C(52,7)', u'C(52,7)')]	|
|6	|4*C(13,3)*C(39,4-3)/[C(52,4)]	|(C(4,1)*C(14,3)*C(52-14,1))/C(52,4)	|[('R.0.1.1', 1.0, u'4-3', u'1'), ('R.1', 270725, u'C(52,4)', u'C(52,4)')]	|
|7	|4*C(13,3)*C(39,4-3)/[C(52,4)]	|(C(13,3)*C(52-13,1))/C(52,4)	|[('R.0.1.1', 1.0, u'4-3', u'1'), ('R.1', 270725, u'C(52,4)', u'C(52,4)')]	|
|8	|4*C(13,4)*C(39,5-4)/[C(52,5)]	|(C(13,4)*C(39,1))/C(52,5)	|[('R.0.1.1', 1.0, u'5-4', u'1'), ('R.1', 2598960, u'C(52,5)', u'C(52,5)')]	|
|9	|4*C(13,4)*C(39,5-4)/[C(52,5)]	|[C(13,4)*[C(13*3,1)]]/C(52,5)	|[('R.0.1.1', 1.0, u'5-4', u'1'), ('R.1', 2598960, u'C(52,5)', u'C(52,5)')]	|




### (5) Mistake Group ['R.0.0', 'R.1'] of size 5
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*C(13,3)*C(39,4-3)/[C(52,4)]	|(4*C(13,3)+39)/C(52,4)	|[('R.0.0', 1144.0, u'4*C(13,3)', u'4*C(13,3)'), ('R.1', 270725, u'C(52,4)', u'C(52,4)')]	|
|1	|4*C(13,6)*C(39,7-6)/[C(52,7)]	|(4 * C(13, 6) * 49)/C(52, 7)	|[('R.0.0', 6864.0, u'4*C(13,6)', u'4 * C(13, 6)'), ('R.1', 133784560, u'C(52,7)', u'C(52, 7)')]	|
|2	|4*C(13,2)*C(39,4-2)/[C(52,4)]	|(4*(13!/(2!*11!))*(39!/(2!*37)))/(52!/(4!*(52-4)!))	|[('R.0.0', 312.0, u'4*C(13,2)', u'4*(13!/(2!*11!))'), ('R.1', 270725, u'C(52,4)', u'52!/(4!*(52-4)!)')]	|
|3	|4*C(13,4)*C(39,5-4)/[C(52,5)]	|(4*C(13,4)-39)/C(52,5)	|[('R.0.0', 2860.0, u'4*C(13,4)', u'4*C(13,4)'), ('R.1', 2598960, u'C(52,5)', u'C(52,5)')]	|
|4	|4*C(13,3)*C(39,6-3)/[C(52,6)]	|C(13,3)*C(4,3)*C(13,3)/C(52,6)	|[('R.0.0', 1144.0, u'4*C(13,3)', u'C(13,3)*C(4,3)'), ('R.1', 20358520, u'C(52,6)', u'C(52,6)')]	|




### (3) Mistake Group ['R.0', 'R.1.0'] of size 3
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*C(13,6)*C(39,7-6)/[C(52,7)]	|4*C(13,6)*39/52!	|[('R.0', 267696.0, u'4*C(13,6)*C(39,7-6)', u'4*C(13,6)*39'), ('R.1.0', 52.0, u'52', u'52')]	|
|1	|4*C(13,4)*C(39,6-4)/[C(52,6)]	|2119260/52!	|[('R.0', 2119260.0, u'4*C(13,4)*C(39,6-4)', u'2119260'), ('R.1.0', 52.0, u'52', u'52')]	|
|2	|4*C(13,2)*C(39,4-2)/[C(52,4)]	|(4*C(13,2)*C(39,2))/C(52,4!)	|[('R.0', 231192.0, u'4*C(13,2)*C(39,4-2)', u'4*C(13,2)*C(39,2)'), ('R.1.0', 52.0, u'52', u'52')]	|




### (3) Mistake Group ['R.0.0.1'] of size 3
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*C(13,5)*C(39,7-5)/[C(52,7)]	|[C(13,5)*C(4,1)*C(39,2)]/C(13,5)*C(4,1)*C(39,2)	|[('R.0.0.1', 1287, u'C(13,5)', u'C(13,5)')]	|
|1	|4*C(13,5)*C(39,6-5)/[C(52,6)]	|C(52,6)/C(13,5)*4*39	|[('R.0.0.1', 1287, u'C(13,5)', u'C(13,5)')]	|
|2	|4*C(13,2)*C(39,6-2)/[C(52,6)]	|4*39!/(4!(35!)) * 78 / 52!/(6!46!)	|[('R.0.0.1', 78, u'C(13,2)', u'78')]	|




### (3) Mistake Group Digits of size 3




### (2) Mistake Group ['R.0.0.1', 'R.1'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.1', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*C(13,3)*C(39,5-3)/[C(52,5)]	|(741+39+286+4)/((52!)/(47!5!))	|[('R.0.0.1', 286, u'C(13,3)', u'286'), ('R.1', 2598960, u'C(52,5)', u'(52!)/(47!5!)')]	|
|1	|4*C(13,3)*C(39,5-3)/[C(52,5)]	|(741*39*286*4)/((52!)/(47!5!))	|[('R.0.0.1', 286, u'C(13,3)', u'286'), ('R.1', 2598960, u'C(52,5)', u'(52!)/(47!5!)')]	|




### (2) Mistake Group ['R.0.0'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*C(13,2)*C(39,4-2)/[C(52,4)]	|4*(13!/(11!*2!))*(13*3)*(39!/(2!*37!))	|[('R.0.0', 312.0, u'4*C(13,2)', u'4*(13!/(11!*2!))')]	|
|1	|4*C(13,2)*C(39,4-2)/[C(52,4)]	|[4*78*74]/(39!/[2!37!])	|[('R.0.0', 312.0, u'4*C(13,2)', u'4*78')]	|




### (2) Mistake Group ['R.0.1.0'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*C(13,5)*C(39,7-5)/[C(52,7)]	|(((13*12*11*10*9)/52)*(39*38))/(52*51*50*49*48*47)	|[('R.0.1.0', 39.0, u'39', u'39')]	|
|1	|4*C(13,5)*C(39,7-5)/[C(52,7)]	|(((13*12*11*10*9)/52)*(39*38))/(52*51*50*49*48*47*46)	|[('R.0.1.0', 39.0, u'39', u'39')]	|




### (1) Mistake Group ['R.0.0.0', 'R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*C(13,6)*C(39,7-6)/[C(52,7)]	|(4 * 3 * 13^2)/C(52, 7)	|[('R.0.0.0', 4.0, u'4', u'4'), ('R.1', 133784560, u'C(52,7)', u'C(52, 7)')]	|




### (1) Mistake Group ['R.0.0', 'R.0.1', 'R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.0.1', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*C(13,2)*C(39,4-2)/[C(52,4)]	|(4*C(13,2) + C(3*13,2)) / C(52,4)	|[('R.0.0', 312.0, u'4*C(13,2)', u'4*C(13,2)'), ('R.0.1', 741, u'C(39,4-2)', u'C(3*13,2)'), ('R.1', 270725, u'C(52,4)', u'C(52,4)')]	|




### (1) Mistake Group ['R.0.0', 'R.0.1.1', 'R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.0.1.1', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*C(13,4)*C(39,7-4)/[C(52,7)]	|[4*C(13,4)*C(13,3)]/C(52,7)	|[('R.0.0', 2860.0, u'4*C(13,4)', u'4*C(13,4)'), ('R.0.1.1', 3.0, u'7-4', u'3'), ('R.1', 133784560, u'C(52,7)', u'C(52,7)')]	|




### (1) Mistake Group ['R.0', 'R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*C(13,5)*C(39,7-5)/[C(52,7)]	|4*C(13,5)*C(39,2)*C(52,7)	|[('R.0', 3814668.0, u'4*C(13,5)*C(39,7-5)', u'4*C(13,5)*C(39,2)'), ('R.1', 133784560, u'C(52,7)', u'C(52,7)')]	|




### (1) Mistake Group ['R.0.0.1.0', 'R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.1.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*C(13,2)*C(39,5-2)/[C(52,5)]	|(6*13^2*2600)/2598960	|[('R.0.0.1.0', 13.0, u'13', u'13'), ('R.1', 2598960, u'C(52,5)', u'2598960')]	|




### (1) Mistake Group ['R.0.1.1.1', 'R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1.1.1', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*C(13,2)*C(39,4-2)/[C(52,4)]	|[C(13,1)*C(12,1)C(39,2)]/C(52,4)	|[('R.0.1.1.1', 2.0, u'2', u'2'), ('R.1', 270725, u'C(52,4)', u'C(52,4)')]	|




### (1) Mistake Group ['R.0.1.0', 'R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*C(13,3)*C(39,4-3)/[C(52,4)]	|(C(13,3)*C(52-13,12))/C(52,4)	|[('R.0.1.0', 39.0, u'39', u'52-13'), ('R.1', 270725, u'C(52,4)', u'C(52,4)')]	|




### (1) Mistake Group ['R.0.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*C(13,2)*C(39,6-2)/[C(52,6)]	|[C(52,2)*4*13*C(39,4)]/[52!/46!]	|[('R.0.1', 82251, u'C(39,6-2)', u'C(39,4)')]	|




### (1) Mistake Group ['R.0.0', 'R.0.1.1.1', 'R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.0.1.1.1', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*C(13,2)*C(39,4-2)/[C(52,4)]	|4* (13!/((13-2)!*2!)) * ((52/2)! / ((52/2 - 2)! * 2!))/ (52!/((52-4)!*4!))	|[('R.0.0', 312.0, u'4*C(13,2)', u'4* (13!/((13-2)!*2!))'), ('R.0.1.1.1', 2.0, u'2', u'2!'), ('R.1', 270725, u'C(52,4)', u'52!/((52-4)!*4!)')]	|




### (1) Mistake Group ['R.0.0.1', 'R.0.1', 'R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.1', 'R.0.1', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*C(13,2)*C(39,6-2)/[C(52,6)]	|[C(52,2)*4*C(13,2)*C(39,4)]/C(52,6)	|[('R.0.0.1', 78, u'C(13,2)', u'C(13,2)'), ('R.0.1', 82251, u'C(39,6-2)', u'C(39,4)'), ('R.1', 20358520, u'C(52,6)', u'C(52,6)')]	|




### (1) Mistake Group ['R.0.1.1.0', 'R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1.1.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*C(13,2)*C(39,5-2)/[C(52,5)]	|(4 * 13 * 52!/(47!5!))/(52!/(47!5!))	|[('R.0.1.1.0', 5.0, u'5', u'5'), ('R.1', 2598960, u'C(52,5)', u'52!/(47!5!)')]	|




### (1) Mistake Group ['R.0.0.0', 'R.0.0.1.0', 'R.0.1', 'R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0', 'R.0.0.1.0', 'R.0.1', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*C(13,3)*C(39,5-3)/[C(52,5)]	|(C(4, 1)* C(13, 2)* C(39, 2))/C(52, 5)	|[('R.0.0.0', 4.0, u'4', u'C(4, 1)'), ('R.0.0.1.0', 13.0, u'13', u'13'), ('R.0.1', 741, u'C(39,5-3)', u'C(39, 2)'), ('R.1', 2598960, u'C(52,5)', u'C(52, 5)')]	|




### (1) Mistake Group ['R.0.0.0', 'R.0.1.1', 'R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0', 'R.0.1.1', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*C(13,2)*C(39,5-2)/[C(52,5)]	|[4*13*C(12,3)]/[52!/(47!5!)]	|[('R.0.0.0', 4.0, u'4', u'4'), ('R.0.1.1', 3.0, u'5-2', u'3'), ('R.1', 2598960, u'C(52,5)', u'52!/(47!5!)')]	|




### (20) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:k5law

	first_attempt
					2015-10-12 01:40:02
	part1_correct_attempt
					['0:00:00', u'52!/((52-5)!5!)']
	part2_correct_attempt
					['0:01:47', u'4']
	part3_correct_attempt
					['2:00:06', u'(13!/(10!3!))']
	part4_correct_attempt
					['0:07:03', u'52-13']
	part5_correct_attempt
					['0:07:29', u'39!/(37!2!)']
	part6_correct_attempt
					['2:01:46', u'4*(13!/(10!3!))*(39!/(37!2!))']
	part7_incorrect_attempt
					('2:02:13', u'[4*(13!/(10!3!))*(39!/(37!2!))]/52!/((52-5)!5!)')
	part7_correct_attempt
					['2:02:52', u'[4*(13!/(10!3!))*(39!/(37!2!))]/[52!/((52-5)!5!)]']

1 Student ID:jtfrankl

	first_attempt
					2015-10-15 21:03:16
	part1_correct_attempt
					['0:00:00', u'52!/(48!4!)']
	part2_correct_attempt
					['0:00:00', u'4']
	part3_correct_attempt
					['0:03:13', u'C(13,2)']
	part4_correct_attempt
					['0:00:00', u'39']
	part5_correct_attempt
					['0:00:00', u'C(39,2)']
	part6_correct_attempt
					['0:04:38', u'4*C(39,2)*C(13,2)']
	part7_incorrect_attempt
					('0:05:01', u'(C(13,2))/(C(13,2))')
	part7_correct_attempt
					['0:05:59', u'(4*C(39,2)*C(13,2))/(52!/(48!4!))']

2 Student ID:a2ahmed

	first_attempt
					2015-10-15 04:08:54
	part1_correct_attempt
					['0:00:00', u'C(52,6)']
	part2_correct_attempt
					['0:00:00', u'4']
	part3_correct_attempt
					['0:04:19', u'C(13,5)']
	part4_correct_attempt
					['0:00:00', u'39']
	part5_correct_attempt
					['0:00:00', u'39']
	part6_correct_attempt
					['0:08:46', u'C(13,5)*4*39']
	part7_incorrect_attempt
					('0:09:12', u'C(52,6)/(C(13,5)*4*39)')
					('0:09:23', u'C(52,6)-(C(13,5)*4*39)')
	part7_correct_attempt
					['0:09:53', u'(C(13,5)*4*39)/C(52,6)']

3 Student ID:haw081

	first_attempt
					2015-10-10 23:32:20
	part1_correct_attempt
					['0:00:00', u'C(52,7)']
	part2_correct_attempt
					['0:00:00', u'4']
	part3_correct_attempt
					['0:18:08', u'C(13,6)']
	part4_correct_attempt
					['0:06:24', u'52-13']
	part5_correct_attempt
					['0:06:37', u'C(39,1)']
	part6_correct_attempt
					['2 days, 1:13:11', u'C(4,1)*C(13,6)*C(39,1)']
	part7_incorrect_attempt
					('2 days, 1:13:30', u'C(52,7)/C(52,7)')
	part7_correct_attempt
					['2 days, 1:13:42', u'C(4,1)*C(13,6)*C(39,1)/C(52,7)']

4 Student ID:djk006

	first_attempt
					2015-10-11 02:28:10
	part1_correct_attempt
					['0:00:00', u'52!/(6!46!)']
	part2_correct_attempt
					['-1 day, 23:56:52', u'4']
	part3_correct_attempt
					['0:14:35', u'13*12*11/6']
	part4_correct_attempt
					['-1 day, 23:56:52', u'39']
	part5_correct_attempt
					['0:01:01', u'39!/(6(36!))']
	part6_correct_attempt
					['0:15:30', u'4*13*12*11/6*39!/(6(36!))']
	part7_incorrect_attempt
					('0:15:30', u'(4*13*12*11/6*39!/(6(36!)))/52!/(6!46!)')
	part7_correct_attempt
					['0:15:54', u'(4*13*12*11/6*39!/(6(36!)))/(52!/(6!46!))']

5 Student ID:gsrandha

	first_attempt
					2015-10-12 06:59:39
	part1_correct_attempt
					['0:00:00', u'2598960']
	part2_correct_attempt
					['0:03:26', u'4']
	part3_correct_attempt
					['23:17:29', u'78']
	part7_incorrect_attempt
					('23:27:41', u'12/51')

6 Student ID:q3wen

	first_attempt
					2015-10-14 04:28:06
	part1_correct_attempt
					['0:00:00', u'270725']
	part2_correct_attempt
					['0:02:33', u'4']
	part3_correct_attempt
					['0:10:55', u'286']
	part4_correct_attempt
					['0:06:07', u'39']
	part5_correct_attempt
					['0:10:55', u'39']
	part6_correct_attempt
					['0:17:55', u'44616']
	part7_incorrect_attempt
					('0:17:55', u'1/44616')
	part7_correct_attempt
					['0:18:19', u'44616/270725']

7 Student ID:dcastlem

	first_attempt
					2015-10-15 03:21:40
	part1_correct_attempt
					['0:00:00', u'52!/((7!)(45!))']
	part2_correct_attempt
					['0:02:19', u'4!/((1!)3!)']
	part3_correct_attempt
					['0:03:17', u'13!/((3!)(10!))']
	part4_correct_attempt
					['0:07:10', u'39']
	part5_correct_attempt
					['0:07:10', u'39!/((4!)(35!))']
	part6_correct_attempt
					['0:08:43', u'4!/((1!)3!)*13!/((3!)(10!))*39!/((4!)(35!))']
	part7_incorrect_attempt
					('0:09:14', u'(4!/((1!)3!)*13!/((3!)(10!))*39!/((4!)(35!)))/52!/((7!)(45!))')
	part7_correct_attempt
					['0:10:40', u'(4!/((1!)3!)*13!/((3!)(10!))*39!/((4!)(35!)))/(52!/((7!)(45!)))']

8 Student ID:starinia

	first_attempt
					2015-10-15 01:42:28
	part1_correct_attempt
					['0:00:00', u'52!/(4!48!)']
	part2_correct_attempt
					['-1 day, 23:45:57', u'4']
	part3_correct_attempt
					['2:07:22', u'C(13,2)']
	part4_correct_attempt
					['-1 day, 23:45:57', u'52-13']
	part5_correct_attempt
					['2:07:00', u'C(39,2)']
	part6_correct_attempt
					['2:32:48', u'(4*C(13,2)*C(39,2))']
	part7_incorrect_attempt
					('2:33:02', u'(4*C(13,2)*C(39,2))/52!/(4!48!)')
	part7_correct_attempt
					['2:33:14', u'(4*C(13,2)*C(39,2))/(52!/(4!48!))']

9 Student ID:vasharma

	first_attempt
					2015-10-10 05:56:00
	part1_correct_attempt
					['0:00:00', u'52!/[7!(52-7)!]']
	part2_correct_attempt
					['0:06:36', u'4']
	part3_correct_attempt
					['0:25:55', u'13!/[5!(13-5)!]']
	part4_correct_attempt
					['0:57:46', u'39']
	part5_correct_attempt
					['0:58:10', u'39!/[2!(39-2)!]']
	part6_correct_attempt
					['1:28:55', u'C(13,5)*C(4,1)*C(39,2)']
	part7_incorrect_attempt
					('1:29:27', u'[C(13,5)*C(4,1)*C(39,2)]/52!/[7!(52-7)!]')
	part7_correct_attempt
					['1:29:43', u'[C(13,5)*C(4,1)*C(39,2)]/[52!/[7!(52-7)!]]']

10 Student ID:jeqin

	first_attempt
					2015-10-15 12:39:23
	part1_correct_attempt
					['0:00:00', u'52!/(6!46!)']
	part2_correct_attempt
					['0:00:42', u'4']
	part3_correct_attempt
					['0:01:49', u'13!/(5!8!)']
	part4_correct_attempt
					['0:00:42', u'39']
	part5_correct_attempt
					['0:00:42', u'39']
	part6_correct_attempt
					['0:03:40', u'4*13!/(5!8!)*39']
	part7_incorrect_attempt
					('0:03:58', u'4*13!/(5!8!)*39 / 52!/(6!46!)')
	part7_correct_attempt
					['0:04:20', u'(4*13!/(5!8!)*39) / (52!/(6!46!))']

11 Student ID:jnatale

	first_attempt
					2015-10-13 01:16:50
	part1_correct_attempt
					['0:00:00', u'C(52,6)']
	part2_correct_attempt
					['0:01:30', u'4']
	part3_correct_attempt
					['0:07:14', u'C(13,4)']
	part4_correct_attempt
					['0:07:51', u'39']
	part5_correct_attempt
					['0:07:51', u'C(39,2)']
	part6_correct_attempt
					['0:10:14', u'4*C(13,4)*C(39,2)']
	part7_incorrect_attempt
					('0:12:21', u'4*C(13,4)*C(39,2)/(7462)/14658134400')
					('0:12:36', u'(4*C(13,4)*C(39,2)/(7462))/14658134400')
					('0:15:31', u'(4*C(13,4)*C(39,2)/(7462))/(2598960)')
	part7_correct_attempt
					['0:17:05', u'(4*C(13,4)*C(39,2))/C(52,6)']

12 Student ID:abjara

	first_attempt
					2015-10-12 10:47:42
	part1_correct_attempt
					['0:00:00', u'52!/(4!*48!)']
	part2_correct_attempt
					['0:00:00', u'4']
	part3_correct_attempt
					['0:13:30', u'13!/(2!*11!)']
	part4_correct_attempt
					['0:00:00', u'39']
	part5_correct_attempt
					['0:00:00', u'39!/(2!*37!)']
	part6_correct_attempt
					['2 days, 11:50:01', u'4*[13!/(11!*2!)] * [39!/(37!*2!)]']
	part7_incorrect_attempt
					('2 days, 11:51:10', u'[4*[13!/(11!*2!)] * [39!/(37!*2!)]]/52!/(4!*48!)')
					('2 days, 11:51:45', u'52!/(4!*48!)/[4*[13!/(11!*2!)] * [39!/(37!*2!)]]')
	part7_correct_attempt
					['2 days, 11:52:14', u'[4*[13!/(11!*2!)] * [39!/(37!*2!)]]/[52!/(4!*48!)]']

13 Student ID:ffhaddad

	first_attempt
					2015-10-10 21:08:16
	part1_correct_attempt
					['0:00:00', u'C(52,4)']
	part2_correct_attempt
					['0:00:28', u'C(4,1)']
	part3_correct_attempt
					['0:01:32', u'C(13,3)']
	part4_correct_attempt
					['0:01:56', u'52-13']
	part5_correct_attempt
					['0:02:13', u'39']
	part6_correct_attempt
					['0:02:49', u'C(4,1)C(13,3)39']
	part7_incorrect_attempt
					('0:03:08', u'C(52,4)')
	part7_correct_attempt
					['0:03:41', u'C(4,1)C(13,3)39/C(52,4)']

14 Student ID:m8woo

	first_attempt
					2015-10-10 01:10:32
	part1_correct_attempt
					['0:00:00', u'C(52,7)']
	part2_correct_attempt
					['0:00:00', u'4']
	part3_correct_attempt
					['0:01:04', u'C(13,5)']
	part4_correct_attempt
					['0:00:46', u'39']
	part5_correct_attempt
					['0:00:46', u'C(39,2)']
	part6_correct_attempt
					['0:02:24', u'4*(C(13,5) * C(39,2))']
	part7_incorrect_attempt
					('0:02:24', u'C(52,7)/[4*(C(13,5) * C(39,2))]')
	part7_correct_attempt
					['0:02:38', u'[4*(C(13,5) * C(39,2))]/C(52,7)']

15 Student ID:krau

	first_attempt
					2015-10-14 03:51:47
	part1_correct_attempt
					['0:00:00', u'52!/4!/48!']
	part2_correct_attempt
					['-1 day, 23:59:48', u'4']
	part3_correct_attempt
					['0:02:28', u'13!/10!/3!']
	part4_correct_attempt
					['0:01:10', u'39']
	part5_correct_attempt
					['0:01:31', u'39!/38!/1!']
	part6_correct_attempt
					['0:06:02', u'4 * (13!/10!/3!) * (39!/38!/1!)']
	part7_incorrect_attempt
					('0:07:13', u'(4 * (13!/10!/3!) * (39!/38!/1!)) / 52!/4!/48!')
	part7_correct_attempt
					['0:07:43', u'(4 * (13!/10!/3!) * (39!/38!/1!)) / (52!/4!/48!)']

16 Student ID:hah008

	first_attempt
					2015-10-13 06:21:21
	part1_correct_attempt
					['0:00:00', u'C(52, 4)']
	part2_correct_attempt
					['-1 day, 23:58:46', u'4']
	part3_correct_attempt
					['0:00:31', u'C(13, 3)']
	part4_correct_attempt
					['0:02:12', u'39']
	part5_correct_attempt
					['0:02:20', u'39']
	part6_correct_attempt
					['0:05:15', u'44616']
	part7_incorrect_attempt
					('0:06:58', u'858/425')
	part7_correct_attempt
					['0:08:30', u'3432/20825']

17 Student ID:pvl001

	first_attempt
					2015-10-13 19:10:54
	part1_correct_attempt
					['0:00:00', u'52!/(4! * 48!)']
	part2_correct_attempt
					['0:00:31', u'4']
	part3_correct_attempt
					['0:19:45', u'78']
	part4_correct_attempt
					['0:19:02', u'39']
	part5_correct_attempt
					['0:19:13', u'741']
	part6_correct_attempt
					['0:21:41', u'741 * 78 * 4']
	part7_incorrect_attempt
					('0:22:19', u'(741 * 78 * 4) / 52!/(4! * 48!)')
	part7_correct_attempt
					['0:22:30', u'(741 * 78 * 4) / (52!/(4! * 48!))']

18 Student ID:anvan

	first_attempt
					2015-10-14 22:41:56
	part1_correct_attempt
					['0:00:00', u'52!/(46!6!)']
	part2_correct_attempt
					['0:00:00', u'4']
	part3_correct_attempt
					['0:04:58', u'13!/(2!11!)']
	part4_correct_attempt
					['0:00:00', u'39']
	part5_correct_attempt
					['0:00:00', u'39!/(4!35!)']
	part6_correct_attempt
					['2:21:51', u'39!/(4!35!) * 13!/(2!11!) * 4']
	part7_incorrect_attempt
					('2:23:15', u'( 39!/(4!35!) * 13!/(2!11!) * 4 ) / 52!/(46!6!)')
					('2:23:40', u'2.56623E+07 / 52!/(46!6!)')
					('2:30:50', u'(39!/(4!35!) * 13!/(2!11!) * 4)/ 52!/(46!6!)')
					('4:29:00', u'(39!/(4!35!) * 13!/(2!11!) * 4)/ 52!/(46!6!)')
	part7_correct_attempt
					['4:29:28', u'(39!/(4!35!) * 13!/(2!11!) * 4)/ (52!/(46!6!) )']

19 Student ID:mrchin

	first_attempt
					2015-10-12 03:35:43
	part1_correct_attempt
					['0:00:00', u'52!/(48!*4!)']
	part2_correct_attempt
					['0:00:27', u'4']
	part3_correct_attempt
					['0:01:34', u'13!/(11!*2!)']
	part4_correct_attempt
					['0:01:57', u'52-13']
	part5_correct_attempt
					['0:02:09', u'39!/(37!*2!)']
	part6_correct_attempt
					['2 days, 19:01:33', u'39!/(37!*2!)*4*13!/(11!*2!)']
	part7_incorrect_attempt
					('2 days, 19:02:59', u'[39!/(37!*2!)*4*13!/(11!*2!)]/52!/(48!*4!)')
					('2 days, 19:03:26', u'231192/52!/(48!*4!)')
	part7_correct_attempt
					['2 days, 19:03:47', u'231192/[52!/(48!*4!)]']












