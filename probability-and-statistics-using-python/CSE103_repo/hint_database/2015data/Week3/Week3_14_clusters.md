#Problem 14

    $ns = random(4,6,1);
    $nr = random(10,16,1);
    $n = $ns*$nr;

    ### Straight : Five cards in sequence, but not all from the same suit ###
    *Remember, the deck you are using has [$ns] suits and [$nr] ranks.*

    1. In the case of a standard deck, the ranks of a straight is one of (Ace,2,3,4,5) ... (10,J,Q,K,Ace). Similarly, in your deck, the number of possibilities for the ranks of a straight is [______]{Compute("$nr-3")}.

    2. The suits can be anything other than all equal, so the number of possibilities for the suits of a straight is [______]{Compute("$ns**5 - $ns")}.

    4. Thus the number of hands that is a straight is [______]{Compute("($nr-3)*($ns**5-$ns)")}.

    5. The ratio of this number to the number of all hands [______]{Compute("($nr-3)*($ns**5-$ns)/C($n,5)")}.


## Part 1

### (419) Mistake Group Digits of size 419




### (64) Mistake Group ['R.0'] of size 64
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|16-3	|C(16,5)	|[('R.0', 16.0, u'16', u'16')]	|
|1	|14-3	|C(14,5)	|[('R.0', 14.0, u'14', u'14')]	|
|2	|11-3	|C(11,5)	|[('R.0', 11.0, u'11', u'11')]	|
|3	|11-3	|C(11,6)	|[('R.0', 11.0, u'11', u'11')]	|
|4	|11-3	|C(11,7)	|[('R.0', 11.0, u'11', u'11')]	|
|5	|10-3	|C(10,5)	|[('R.0', 10.0, u'10', u'10')]	|
|6	|10-3	|10*5!	|[('R.0', 10.0, u'10', u'10')]	|
|7	|16-3	|C(16,6)	|[('R.0', 16.0, u'16', u'16')]	|
|8	|16-3	|16!	|[('R.0', 16.0, u'16', u'16')]	|
|9	|10-3	|10*5	|[('R.0', 10.0, u'10', u'10')]	|
|10	|10-3	|10*4	|[('R.0', 10.0, u'10', u'10')]	|
|11	|14-3	|14*(4^5-4)	|[('R.0', 14.0, u'14', u'14')]	|
|12	|10-3	|10-5	|[('R.0', 10.0, u'10', u'10')]	|
|13	|12-3	|C(12, 5)	|[('R.0', 12.0, u'12', u'12')]	|
|14	|12-3	|12!	|[('R.0', 12.0, u'12', u'12')]	|
|15	|12-3	|C(12,5)	|[('R.0', 12.0, u'12', u'12')]	|
|16	|15-3	|15*6	|[('R.0', 15.0, u'15', u'15')]	|
|17	|10-3	|10 * 6	|[('R.0', 10.0, u'10', u'10')]	|
|18	|14-3	|14*2	|[('R.0', 14.0, u'14', u'14')]	|
|19	|14-3	|4!/2!/2!+4+4+4	|[('R.0', 14.0, u'14', u'4!/2!/2!+4+4')]	|
|20	|10-3	|C(10,1) * (C(5,1))^4	|[('R.0', 10.0, u'10', u'C(10,1)')]	|
|21	|10-3	|C(10,1)C(9,1)C(8,1)C(7,1)C(6,1)	|[('R.0', 10.0, u'10', u'C(10,1)')]	|
|22	|10-3	|10*6	|[('R.0', 10.0, u'10', u'10')]	|
|23	|14-3	|C(14,1)C(6,1)^5	|[('R.0', 14.0, u'14', u'C(14,1)')]	|
|24	|14-3	|14*36	|[('R.0', 14.0, u'14', u'14')]	|
|25	|14-3	|14*6^5	|[('R.0', 14.0, u'14', u'14')]	|
|26	|14-3	|C(14,1)C(6,1)	|[('R.0', 14.0, u'14', u'C(14,1)')]	|
|27	|14-3	|C(14,1)*C(6,1)^5	|[('R.0', 14.0, u'14', u'C(14,1)')]	|
|28	|11-3	|11*5	|[('R.0', 11.0, u'11', u'11')]	|
|29	|15-3	|15*5^4	|[('R.0', 15.0, u'15', u'15')]	|
|30	|15-3	|15*2	|[('R.0', 15.0, u'15', u'15')]	|
|31	|16-3	|16*5	|[('R.0', 16.0, u'16', u'16')]	|
|32	|16-3	|16*4	|[('R.0', 16.0, u'16', u'16')]	|
|33	|13-3	|13-5	|[('R.0', 13.0, u'13', u'13')]	|
|34	|12-3	|P(12,5)	|[('R.0', 12.0, u'12', u'12')]	|
|35	|10-3	|C(10,6)	|[('R.0', 10.0, u'10', u'10')]	|
|36	|14-3	|14-4	|[('R.0', 14.0, u'14', u'14')]	|
|37	|13-3	|C(13,5)	|[('R.0', 13.0, u'13', u'13')]	|
|38	|10-3	|10-4	|[('R.0', 10.0, u'10', u'10')]	|
|39	|13-3	|C(13, 5)	|[('R.0', 13.0, u'13', u'13')]	|
|40	|16-3	|16*C(4,1)^5	|[('R.0', 16.0, u'16', u'16')]	|
|41	|10-3	|C(10,4)	|[('R.0', 10.0, u'10', u'10')]	|
|42	|13-3	|P(13, 5)	|[('R.0', 13.0, u'13', u'13')]	|




### (5) Mistake Group Fraction of size 5




### (2) Mistake Group ['R.1'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|14-3	|4*3	|[('R.1', 3.0, u'3', u'3')]	|
|1	|12-3	|5-3	|[('R.1', 3.0, u'3', u'3')]	|




### (2) Mistake Group Wrong_Sign of size 2




### (74) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:druble

	first_attempt
					2015-10-13 01:57:07
	part1_incorrect_attempt
					('0:00:00', u'C(14,1)')
	part1_correct_attempt
					['0:09:15', u'11']

1 Student ID:ttimmons

	first_attempt
					2015-10-12 19:09:34
	part1_incorrect_attempt
					('0:00:00', u'15-4')
					('0:09:34', u'C(15,5)')
	part1_correct_attempt
					['0:14:36', u'10']

2 Student ID:lpettit

	first_attempt
					2015-10-14 20:43:10
	part1_incorrect_attempt
					('0:00:00', u'(17!)/(5!*12!)')
	part1_correct_attempt
					['0:30:24', u'10']

3 Student ID:jag028

	first_attempt
					2015-10-15 14:33:48
	part1_incorrect_attempt
					('0:00:00', u'C(10,5)C(13,4)')
	part1_correct_attempt
					['0:18:20', u'7']

4 Student ID:v4zhang

	first_attempt
					2015-10-15 22:45:57
	part1_incorrect_attempt
					('0:00:00', u'[C(10, 1)*[C(4, 1)]^5] - [C(10, 1)*C(4, 1)]')
					('0:01:43', u'[C(12, 1)*[C(4, 1)]^5] - [C(12, 1)*C(4, 1)]')
					('0:02:36', u'C(10, 1)*[C(4, 1)]^5')
	part1_correct_attempt
					['0:02:43', u'C(10, 1)']

5 Student ID:lywong

	first_attempt
					2015-10-13 09:02:31
	part1_incorrect_attempt
					('0:00:00', u'6^5-5')
					('0:03:02', u'15!/(5!10!)')
	part1_correct_attempt
					['0:15:53', u'12']

6 Student ID:kebao

	first_attempt
					2015-10-15 06:23:20
	part1_incorrect_attempt
					('0:00:00', u'11!/(5!*6!)')
					('0:00:16', u'11!/5!')
					('0:00:59', u'11*10*9*8*7')
	part1_correct_attempt
					['0:03:09', u'8']

7 Student ID:hkhodada

	first_attempt
					2015-10-12 00:23:45
	part1_incorrect_attempt
					('0:00:00', u'5*8')
	part1_correct_attempt
					['0:06:35', u'9']

8 Student ID:lguintu

	first_attempt
					2015-10-09 22:16:22
	part1_incorrect_attempt
					('0:00:00', u'C(16,5)')
					('0:02:04', u'C(11,5)')
					('0:02:07', u'C(12,5)')
					('0:02:12', u'C(13,5)')
					('0:02:16', u'C(10,5)')
					('0:02:23', u'C(9,5)')
					('0:04:43', u'11*5^5')
					('0:04:47', u'13*5^5')
					('0:05:45', u'C(13,5)')
					('0:05:50', u'P(13,5)')
					('0:06:02', u'C(11,5)')
	part1_correct_attempt
					['0:10:43', u'11']

9 Student ID:achava

	first_attempt
					2015-10-13 08:23:38
	part1_incorrect_attempt
					('0:00:00', u'C(84,5)')
					('0:00:00', u'84!/((5!)*(79!))')
					('0:00:08', u'84!/((5!))')
	part1_correct_attempt
					['1 day, 10:55:46', u'11']

10 Student ID:ewbrenna

	first_attempt
					2015-10-12 21:30:19
	part1_incorrect_attempt
					('0:00:00', u'6^10')
					('0:00:00', u'8*4')
	part1_correct_attempt
					['8:02:31', u'8']

11 Student ID:abjara

	first_attempt
					2015-10-12 10:39:17
	part1_incorrect_attempt
					('0:00:00', u'64!/(5!*59!)')
					('0:01:55', u'13*4')
					('0:00:00', u'16!/(11!*5!)')
					('0:00:59', u'17*16*15*14*13')
	part1_correct_attempt
					['2 days, 12:22:20', u'16-5+2']

12 Student ID:spw006

	first_attempt
					2015-10-13 21:23:22
	part1_incorrect_attempt
					('0:00:00', u'4^5 * 10')
					('0:00:27', u'5^5 * 10')
					('0:00:42', u'5^5 * 12')
					('0:00:00', u'5^5 * 15')
					('0:00:27', u'5^5 * 15 - 15')
					('0:01:17', u'5^5 * 15 - 75')
					('0:01:37', u'5^4 * 4 * 15')
	part1_correct_attempt
					['1:37:47', u'12']

13 Student ID:jjm019

	first_attempt
					2015-10-15 23:43:04
	part1_incorrect_attempt
					('0:00:00', u'5!')
					('0:00:00', u'90!/5!')

14 Student ID:mhale

	first_attempt
					2015-10-14 22:14:02
	part1_incorrect_attempt
					('0:00:00', u'7 * 4')
					('0:00:40', u'10 * 5')
					('0:00:47', u'10 * 4^5')
	part1_correct_attempt
					['0:01:18', u'9']

15 Student ID:krau

	first_attempt
					2015-10-14 04:12:16
	part1_incorrect_attempt
					('0:00:00', u'56*4*4*4*4')
					('0:00:00', u'14*4*4*4*4')
					('0:00:00', u'4!/2!/2!')
					('0:00:00', u'4*3*4*4*4')
					('0:00:00', u'4!/2!/2!*4^3')
					('0:00:20', u'4!/2!/2!+4^3')
					('0:00:36', u'4!/2!/2!+4!/3!/1!')
					('0:00:00', u'4!/2!/2!+4*3')
					('0:01:42', u'4!/2!/2!+4!/3!/1!')
	part1_correct_attempt
					['0:11:03', u'11']

16 Student ID:pcdo

	first_attempt
					2015-10-13 20:28:55
	part1_incorrect_attempt
					('0:00:00', u'C(6*14, 5)')
	part1_correct_attempt
					['0:04:02', u'11']

17 Student ID:pvl001

	first_attempt
					2015-10-13 19:56:04
	part1_incorrect_attempt
					('0:00:00', u'13! / (5! * 8!)')
					('0:00:21', u'11! / (5! * 6!)')
	part1_correct_attempt
					['0:04:20', u'8']

18 Student ID:t2li

	first_attempt
					2015-10-14 07:13:56
	part1_incorrect_attempt
					('0:00:00', u'6*9')
	part1_correct_attempt
					['0:00:04', u'9']

19 Student ID:dkurli

	first_attempt
					2015-10-14 04:11:48
	part1_incorrect_attempt
					('0:00:00', u'15!/5!/10!')
					('0:00:12', u'10!/5!/5!')
					('0:00:00', u'11!/5!/6!')
					('0:00:00', u'4*3+4*3*2')
					('0:00:00', u'4*3+4*3*4')
					('0:00:00', u'4!/2!/2!+4')
					('0:00:04', u'4!/2!/2!+8')
					('0:00:00', u'4!/2!/2!+4!/3!+4!/4!')
					('0:00:00', u'4!-4!/1!/3!')
	part1_correct_attempt
					['0:12:12', u'12']

20 Student ID:nhn018

	first_attempt
					2015-10-15 20:08:21
	part1_incorrect_attempt
					('0:00:00', u'5^5-5')
					('0:02:37', u'12^5-5')
					('0:00:00', u'5^5-5')
					('0:00:04', u'5^5')
					('0:00:14', u'4^5')
					('0:01:48', u'5^5')
					('0:04:53', u'4^5-5')
					('0:05:51', u'5^5-5')
					('0:06:40', u'7^5-5')
					('0:06:44', u'7^5')
					('0:20:50', u'12*5^5-5')
					('0:00:00', u'7^5-5')
					('0:01:14', u'5^5-5')
	part1_correct_attempt
					['0:47:36', u'9']

21 Student ID:n2patil

	first_attempt
					2015-10-14 00:33:22
	part1_incorrect_attempt
					('0:00:00', u'(15!)^6')
	part1_correct_attempt
					['0:03:10', u'12']

22 Student ID:s2chaudh

	first_attempt
					2015-10-13 19:48:19
	part1_incorrect_attempt
					('0:00:00', u'C(48,5)')
	part1_correct_attempt
					['1 day, 6:32:43', u'9']

23 Student ID:jmiclat

	first_attempt
					2015-10-15 18:47:35
	part1_incorrect_attempt
					('0:00:00', u'16*6^5-6')
					('0:00:09', u'13*6^5-6')
					('0:00:00', u'18*4')
					('0:00:00', u'18*4^5')
					('0:00:07', u'15*4^5')
	part1_correct_attempt
					['2:35:35', u'13']

24 Student ID:syc078

	first_attempt
					2015-10-15 01:13:47
	part1_incorrect_attempt
					('0:00:00', u'9*8*7*6*5')
					('0:00:00', u'10*9*8*7*6')
	part1_correct_attempt
					['0:02:11', u'10']

25 Student ID:r1gu

	first_attempt
					2015-10-15 22:40:44
	part1_incorrect_attempt
					('0:00:00', u'13-5')
	part1_correct_attempt
					['0:04:15', u'13']

26 Student ID:jhw015

	first_attempt
					2015-10-15 03:03:28
	part1_incorrect_attempt
					('0:00:00', u'C(60,5)')
					('0:06:17', u'C(60,6)')
	part1_correct_attempt
					['0:17:02', u'7']

27 Student ID:mroknich

	first_attempt
					2015-10-15 00:52:01
	part1_incorrect_attempt
					('0:00:00', u'12!/5!')
					('0:00:00', u'28*4*4*4*4')
					('0:00:00', u'10C(4,1)^5')
					('0:00:09', u'9C(4,1)^5')
					('0:04:39', u'10C(4,1)^5')
					('0:00:00', u'10*4^5')
					('0:00:16', u'10*4^5-4-36')

28 Student ID:jeqin

	first_attempt
					2015-10-15 13:03:13
	part1_incorrect_attempt
					('0:00:00', u'14!/(5!9!)')
	part1_correct_attempt
					['0:02:53', u'11']

29 Student ID:t2shin

	first_attempt
					2015-10-15 16:58:32
	part1_incorrect_attempt
					('0:00:00', u'80!/75!')
	part1_correct_attempt
					['0:03:37', u'13']

30 Student ID:jnatale

	first_attempt
					2015-10-13 16:15:10
	part1_incorrect_attempt
					('0:00:00', u'12*C(5,1)')
					('0:00:19', u'12*5*4*3*2*1')
	part1_correct_attempt
					['0:06:25', u'13']

31 Student ID:xil109

	first_attempt
					2015-10-10 21:14:34
	part1_incorrect_attempt
					('0:00:00', u'C(14,1)')
	part1_correct_attempt
					['0:00:51', u'11']

32 Student ID:rlhagen

	first_attempt
					2015-10-11 19:00:50
	part1_incorrect_attempt
					('0:00:00', u'16!/(5!(16-5)!)')
	part1_correct_attempt
					['0:00:24', u'13']

33 Student ID:mrchin

	first_attempt
					2015-10-14 22:55:39
	part1_incorrect_attempt
					('0:00:00', u'15*14*12*13*11')
	part1_correct_attempt
					['0:05:20', u'12']

34 Student ID:lalacson

	first_attempt
					2015-10-11 22:56:52
	part1_incorrect_attempt
					('0:00:00', u'10 * 45 - 4 - 36')
					('0:00:36', u'5*4')
					('0:01:17', u'7*4')
					('0:01:50', u'4^7')
					('0:02:48', u'7*4^5')
					('0:10:31', u'10 * 4^5 - 4 - 36')
					('0:11:06', u'10 * 4^5 - 36')
					('0:13:27', u'7*4^5-4-(6*3)')
	part1_correct_attempt
					['0:16:43', u'7']

35 Student ID:achinn

	first_attempt
					2015-10-13 00:04:28
	part1_incorrect_attempt
					('0:00:00', u'(10*9*8*7*6)/(5*4*3*2)')
					('0:00:17', u'(13*12*11*10*9)/(5*4*3*2)')
	part1_correct_attempt
					['0:05:09', u'7']

36 Student ID:dis003

	first_attempt
					2015-10-15 11:54:13
	part1_incorrect_attempt
					('0:00:00', u'11*C(4,1)^5')
					('0:00:04', u'12*C(4,1)^5')
					('0:01:05', u'C(4,1)^5')
					('0:00:00', u'5*4*3*2*1')
					('0:00:29', u'4**5')
					('0:00:48', u'4**5-4-4*16')
	part1_correct_attempt
					['0:05:29', u'13']

37 Student ID:ppanourg

	first_attempt
					2015-10-15 19:55:39
	part1_incorrect_attempt
					('0:00:00', u'C(10,1)')
					('0:00:41', u'C(11,1)')
	part1_correct_attempt
					['0:01:21', u'C(12,1)']

38 Student ID:jcl084

	first_attempt
					2015-10-13 20:52:52
	part1_incorrect_attempt
					('0:00:00', u'C(52,5)')
					('0:00:14', u'C(13,5)')
					('0:00:33', u'13*5')
					('0:01:22', u'C(13,8)')
					('0:01:29', u'C(8,5)')
					('0:02:25', u'9*4')
					('0:03:09', u'10*4')
					('0:03:13', u'8*4')
					('0:03:52', u'5*12')
					('0:03:56', u'5*11')
					('0:04:03', u'5*13')
					('0:04:08', u'5*10')
	part1_correct_attempt
					['0:05:35', u'11']

39 Student ID:vsosnovs

	first_attempt
					2015-10-15 05:11:37
	part1_incorrect_attempt
					('0:00:00', u'6-3')
	part1_correct_attempt
					['0:01:38', u'12-3']

40 Student ID:aakumar

	first_attempt
					2015-10-11 01:58:18
	part1_incorrect_attempt
					('0:00:00', u'6*5!')
					('0:00:41', u'6*5')
					('0:00:48', u'6*5^5')
	part1_correct_attempt
					['0:45:37', u'7']

41 Student ID:kew017

	first_attempt
					2015-10-15 20:24:01
	part1_incorrect_attempt
					('0:00:00', u'5^5*12')
					('0:00:11', u'5^5*7')
					('0:00:00', u'12*5*5*4^4')
					('0:00:00', u'7!')
					('0:00:08', u'8!')
	part1_correct_attempt
					['0:30:38', u'9']

42 Student ID:tcn013

	first_attempt
					2015-10-15 04:10:33
	part1_incorrect_attempt
					('0:00:00', u'11*6')
					('0:01:05', u'11*30')
	part1_correct_attempt
					['0:02:44', u'11']

43 Student ID:cagatep

	first_attempt
					2015-10-14 05:22:12
	part1_incorrect_attempt
					('0:00:00', u'C(10,1)')
					('0:10:05', u'C(50,1)C(5,1)^4')
	part1_correct_attempt
					['0:18:46', u'7']

44 Student ID:djk006

	first_attempt
					2015-10-11 03:31:22
	part1_incorrect_attempt
					('0:00:00', u'4*9')
					('0:00:06', u'4*8')
					('0:00:00', u'(8!/(3!5!))*8')
					('0:00:53', u'((8!/(3!5!))-4)*8')
	part1_correct_attempt
					['5:18:07', u'9']

45 Student ID:jel075

	first_attempt
					2015-10-15 01:38:49
	part1_incorrect_attempt
					('0:00:00', u'10*9*8*7*6')
					('0:01:51', u'(4!/3!)^5')
	part1_correct_attempt
					['0:06:59', u'7']

46 Student ID:aysee

	first_attempt
					2015-10-13 22:38:29
	part1_incorrect_attempt
					('0:00:00', u'5*10')
	part1_correct_attempt
					['0:40:19', u'7']

47 Student ID:w4shin

	first_attempt
					2015-10-15 00:02:17
	part1_incorrect_attempt
					('0:00:00', u'11!/(5!6!)')
					('0:02:05', u'(11*10*9*8*7)/5!')
					('0:02:18', u'14!/(9!5!)')
	part1_correct_attempt
					['0:11:51', u'8']

48 Student ID:sayao

	first_attempt
					2015-10-12 18:48:09
	part1_incorrect_attempt
					('0:00:00', u'16*(4^5-4)')
					('0:00:19', u'12*(4^5-4)')
					('0:02:01', u'12*(4^5)')
					('0:02:23', u'4^5-4')
					('0:03:01', u'14!/(5!*9!)')
					('0:03:07', u'15!/(5!*9!)')
	part1_correct_attempt
					['0:03:50', u'11']

49 Student ID:anvan

	first_attempt
					2015-10-15 00:10:08
	part1_incorrect_attempt
					('0:00:00', u'4*(13!/5!8!)')
					('0:00:10', u'4*13!/(5!8!)')
					('0:00:00', u'10*5')
					('0:09:14', u'10*9*8*7*6')
					('0:10:27', u'5(10*9*8*7*6)')
					('0:00:00', u'12!/(5!7!)')
					('0:00:30', u'5!4!')
					('0:01:03', u'5^5 - 5')
	part1_correct_attempt
					['2:32:55', u'9']

50 Student ID:psable

	first_attempt
					2015-10-15 23:49:10
	part1_incorrect_attempt
					('0:00:00', u'C(11,1)')
	part1_correct_attempt
					['0:01:50', u'12']

51 Student ID:dpereira

	first_attempt
					2015-10-10 06:07:31
	part1_incorrect_attempt
					('0:00:00', u'6*6^6')
	part1_correct_attempt
					['0:02:39', u'8']

52 Student ID:jjchung

	first_attempt
					2015-10-14 20:17:31
	part1_incorrect_attempt
					('0:00:00', u'10^5')
					('0:00:26', u'10*4*4*4*4')
	part1_correct_attempt
					['0:02:25', u'15-3']

53 Student ID:flhernan

	first_attempt
					2015-10-14 20:24:29
	part1_incorrect_attempt
					('0:00:00', u'52*11')
					('0:00:48', u'52*15')
					('0:01:41', u'64*15')
					('0:05:59', u'C(15,1)')
	part1_correct_attempt
					['1:48:04', u'12']

54 Student ID:lahawkin

	first_attempt
					2015-10-14 05:38:02
	part1_incorrect_attempt
					('0:00:00', u'6*6')
					('0:00:00', u'6*6')
					('0:06:10', u'7*6')

55 Student ID:cstringh

	first_attempt
					2015-10-12 22:51:49
	part1_incorrect_attempt
					('0:00:00', u'12!/(5!(7!))')
					('0:00:00', u'C(12, 5) * 5')
					('0:03:54', u'12 ')
	part1_correct_attempt
					['1 day, 1:47:39', u'9']

56 Student ID:csl030

	first_attempt
					2015-10-14 03:10:53
	part1_incorrect_attempt
					('0:00:00', u'C(13,4)')
					('0:00:45', u'13 * 12 * 11 * 10 * 9')
					('0:04:10', u'6 * 6^5')
					('0:04:20', u'7 * 6^5')
	part1_correct_attempt
					['0:06:37', u'7']

57 Student ID:azkong

	first_attempt
					2015-10-15 18:01:43
	part1_incorrect_attempt
					('0:00:00', u'12!/7!')
	part1_correct_attempt
					['0:15:34', u'9']

58 Student ID:aurodrig

	first_attempt
					2015-10-15 21:44:38
	part1_incorrect_attempt
					('0:00:00', u'10!/(5!5!)')
	part1_correct_attempt
					['0:29:03', u'7']

59 Student ID:yjshin

	first_attempt
					2015-10-14 19:39:34
	part1_incorrect_attempt
					('0:00:00', u'11*5!')
					('0:00:00', u'10*3124')
	part1_correct_attempt
					['16:19:14', u'11']

60 Student ID:hak014

	first_attempt
					2015-10-13 06:18:45
	part1_incorrect_attempt
					('0:00:00', u'(4^5)-4')
	part1_correct_attempt
					['0:05:29', u'11']

61 Student ID:vasharma

	first_attempt
					2015-10-11 03:33:27
	part1_incorrect_attempt
					('0:00:00', u'15!')
	part1_correct_attempt
					['0:03:36', u'13']

62 Student ID:hpc001

	first_attempt
					2015-10-14 23:13:21
	part1_incorrect_attempt
					('0:00:00', u'12*11*10*9*8')
					('0:01:16', u'72*12')
					('0:02:08', u'72*12*6*6*6')
	part1_correct_attempt
					['0:04:14', u'12-3']

63 Student ID:daw023

	first_attempt
					2015-10-15 06:01:47
	part1_incorrect_attempt
					('0:00:00', u'C(10,1)*C(6,1)-C(6,1)')
					('0:01:16', u'10*C(6,1)^5')
					('0:02:15', u'10*C(6,1)^5-54-6')
	part1_correct_attempt
					['0:11:35', u'10']

64 Student ID:tak068

	first_attempt
					2015-10-14 07:39:38
	part1_incorrect_attempt
					('0:00:00', u'C(14,1)')
					('0:03:14', u'C(10,1)')
					('0:03:49', u'C(14,1)')
					('0:15:14', u'C(10,1)*C(6,1)^5')
					('0:19:08', u'C(11,1)*C(6,1)^5')
					('0:19:40', u'C(12,1)*C(6,1)^5')
					('0:19:45', u'C(13,1)*C(6,1)^5')
					('0:19:50', u'C(11,1)*C(6,1)^5')
	part1_correct_attempt
					['0:25:37', u'11']

65 Student ID:amquinte

	first_attempt
					2015-10-14 22:36:11
	part1_incorrect_attempt
					('0:00:00', u'C(16,1)')
	part1_correct_attempt
					['0:09:17', u'13']

66 Student ID:c3chung

	first_attempt
					2015-10-15 22:40:24
	part1_incorrect_attempt
					('0:00:00', u'10(6^5)-6-(54)')
					('0:00:00', u'10(6^5)')
					('0:00:47', u'10(6^4)')
	part1_correct_attempt
					['0:09:45', u'10']

67 Student ID:lcardoso

	first_attempt
					2015-10-13 21:29:02
	part1_incorrect_attempt
					('0:00:00', u'11-5+1')
					('0:01:25', u'14-5+1')
					('0:01:33', u'11-5+1')
	part1_correct_attempt
					['0:07:42', u'8']

68 Student ID:ajvanega

	first_attempt
					2015-10-15 01:14:18
	part1_incorrect_attempt
					('0:00:00', u'14*13*12*11*10')
	part1_correct_attempt
					['0:02:24', u'11']

69 Student ID:glcohen

	first_attempt
					2015-10-13 06:28:01
	part1_incorrect_attempt
					('0:00:00', u'8*3125')
					('0:04:08', u'8 * 5^5')
					('0:05:48', u'(8 * 5^5) - 40')
					('0:05:55', u'(8 * 5^5) - 45')
					('0:00:00', u'7 * (5^5)')
					('0:00:43', u'7 * (5^5) - 35')
					('0:12:46', u'7 * (5^5) - 5')
	part1_correct_attempt
					['14:51:15', u'8']

70 Student ID:zhw110

	first_attempt
					2015-10-09 05:13:12
	part1_incorrect_attempt
					('0:00:00', u'10*(4**5)')
					('0:03:09', u'10*(5**5)')
	part1_correct_attempt
					['0:11:04', u'10']

71 Student ID:hmshah

	first_attempt
					2015-10-14 03:21:22
	part1_incorrect_attempt
					('0:00:00', u'C(13,1)')
					('0:01:08', u'C(11,1)')
					('0:02:22', u'C(11,1)*C(4,1)*C(4,1)*C(4,1)*C(4,1)')
	part1_correct_attempt
					['5:34:02', u'8']

72 Student ID:klala

	first_attempt
					2015-10-12 04:49:06
	part1_incorrect_attempt
					('0:00:00', u'6* 7')
	part1_correct_attempt
					['0:03:15', u'8']

73 Student ID:j2phung

	first_attempt
					2015-10-15 08:40:33
	part1_incorrect_attempt
					('0:00:00', u'13*12*11*10*9')
					('0:00:38', u'13!/(5!8!)')
					('0:04:34', u'13*4')
	part1_correct_attempt
					['0:08:47', u'8']












## Part 2

### (215) Mistake Group Digits of size 215




### (73) Mistake Group ['R.0'] of size 73
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4^5-4	|4^5-11	|[('R.0', 1024.0, u'4^5', u'4^5')]	|
|1	|4^5-4	|4**5 - 1	|[('R.0', 1024.0, u'4^5', u'4**5')]	|
|2	|4^5-4	|4*4*4*4*4 - 1	|[('R.0', 1024.0, u'4^5', u'4*4*4*4*4')]	|
|3	|4^5-4	|(4*4*4*4*4 )- 1	|[('R.0', 1024.0, u'4^5', u'4*4*4*4*4')]	|
|4	|4^5-4	|4^5-44	|[('R.0', 1024.0, u'4^5', u'4^5')]	|
|5	|4^5-4	|4^5-1	|[('R.0', 1024.0, u'4^5', u'4^5')]	|
|6	|5^5-5	|3125-35	|[('R.0', 3125.0, u'5^5', u'3125')]	|
|7	|5^5-5	|5^5-1	|[('R.0', 3125.0, u'5^5', u'5^5')]	|
|8	|4^5-4	|4^5-(7*4)	|[('R.0', 1024.0, u'4^5', u'4^5')]	|
|9	|5^5-5	|5**5-5*5	|[('R.0', 3125.0, u'5^5', u'5**5')]	|
|10	|5^5-5	|(5^5) - 50	|[('R.0', 3125.0, u'5^5', u'5^5')]	|
|11	|5^5-5	|(5^5) - 40	|[('R.0', 3125.0, u'5^5', u'5^5')]	|
|12	|5^5-5	|(5^5)-50	|[('R.0', 3125.0, u'5^5', u'5^5')]	|
|13	|4^5-4	|(4^5)-1	|[('R.0', 1024.0, u'4^5', u'4^5')]	|
|14	|5^5-5	|5^5*8	|[('R.0', 3125.0, u'5^5', u'5^5')]	|
|15	|5^5-5	|(5^5)-(13*5)	|[('R.0', 3125.0, u'5^5', u'5^5')]	|
|16	|5^5-5	|(5^5)-(12*5)	|[('R.0', 3125.0, u'5^5', u'5^5')]	|
|17	|4^5-4	|(4^5-1)	|[('R.0', 1024.0, u'4^5', u'4^5')]	|
|18	|4^5-4	|1024-(13*4)	|[('R.0', 1024.0, u'4^5', u'1024')]	|
|19	|4^5-4	|(1024*13)	|[('R.0', 1024.0, u'4^5', u'1024')]	|
|20	|5^5-5	|5^5 -1	|[('R.0', 3125.0, u'5^5', u'5^5')]	|
|21	|5^5-5	|(5^5 -1)	|[('R.0', 3125.0, u'5^5', u'5^5')]	|
|22	|6^5-6	|C(6,1)^5 - 6*5	|[('R.0', 7776.0, u'6^5', u'C(6,1)^5')]	|
|23	|6^5-6	|6^5 - (6*5)	|[('R.0', 7776.0, u'6^5', u'6^5')]	|
|24	|6^5-6	|6^5 - (6*7)	|[('R.0', 7776.0, u'6^5', u'6^5')]	|
|25	|6^5-6	|6^5 - (30)	|[('R.0', 7776.0, u'6^5', u'6^5')]	|
|26	|6^5-6	|6^5 - (42)	|[('R.0', 7776.0, u'6^5', u'6^5')]	|
|27	|4^5-4	|4^5-10	|[('R.0', 1024.0, u'4^5', u'4^5')]	|
|28	|4^5-4	|4^5-12	|[('R.0', 1024.0, u'4^5', u'4^5')]	|
|29	|4^5-4	|4^5-24	|[('R.0', 1024.0, u'4^5', u'4^5')]	|
|30	|6^5-6	|6^5 - 15	|[('R.0', 7776.0, u'6^5', u'6^5')]	|
|31	|5^5-5	|5**5 -1	|[('R.0', 3125.0, u'5^5', u'5**5')]	|
|32	|4^5-4	|4*(4^4)*3	|[('R.0', 1024.0, u'4^5', u'4*(4^4)')]	|
|33	|5^5-5	|5^5 - (5*9)	|[('R.0', 3125.0, u'5^5', u'5^5')]	|
|34	|5^5-5	|5^5 -45	|[('R.0', 3125.0, u'5^5', u'5^5')]	|
|35	|5^5-5	|5^5 - 25	|[('R.0', 3125.0, u'5^5', u'5^5')]	|
|36	|5^5-5	|5^5 - 40	|[('R.0', 3125.0, u'5^5', u'5^5')]	|
|37	|4^5-4	|4^5 - 36	|[('R.0', 1024.0, u'4^5', u'4^5')]	|
|38	|4^5-4	|([4!/((1!)(3!))]^5) - 32	|[('R.0', 1024.0, u'4^5', u'[4!/((1!)(3!))]^5')]	|
|39	|4^5-4	|([4!/((1!)(3!))]^5) - 40	|[('R.0', 1024.0, u'4^5', u'[4!/((1!)(3!))]^5')]	|
|40	|4^5-4	|(4^5) - 32	|[('R.0', 1024.0, u'4^5', u'4^5')]	|
|41	|5^5-5	|5*5*5*5*5 -1	|[('R.0', 3125.0, u'5^5', u'5*5*5*5*5')]	|
|42	|5^5-5	|5^5-50	|[('R.0', 3125.0, u'5^5', u'5^5')]	|
|43	|5^5-5	|5^5 - 1	|[('R.0', 3125.0, u'5^5', u'5^5')]	|
|44	|4^5-4	|(4!/3!)^5-1	|[('R.0', 1024.0, u'4^5', u'(4!/3!)^5')]	|
|45	|4^5-4	|(4^5) - 1	|[('R.0', 1024.0, u'4^5', u'4^5')]	|
|46	|4^5-4	|(4^5) - 11	|[('R.0', 1024.0, u'4^5', u'4^5')]	|
|47	|6^5-6	|6^5-78	|[('R.0', 7776.0, u'6^5', u'6^5')]	|
|48	|4^5-4	|(C(4,1))^5-11*4	|[('R.0', 1024.0, u'4^5', u'(C(4,1))^5')]	|
|49	|4^5-4	|4^5-11*4	|[('R.0', 1024.0, u'4^5', u'4^5')]	|
|50	|4^5-4	|4^5 - 1	|[('R.0', 1024.0, u'4^5', u'4^5')]	|
|51	|6^5-6	|6^5*5	|[('R.0', 7776.0, u'6^5', u'6^5')]	|




### (51) Mistake Group ['R.0.1'] of size 51
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4^5-4	|6^5-13	|[('R.0.1', 5.0, u'5', u'5')]	|
|1	|6^5-6	|4^5 -4	|[('R.0.1', 5.0, u'5', u'5')]	|
|2	|5^5-5	|C(50,5)-35	|[('R.0.1', 5.0, u'5', u'5')]	|
|3	|4^5-4	|C(5,2) + C(5,3) + C(5,4) + C(5,5)	|[('R.0.1', 5.0, u'5', u'C(5,4)')]	|
|4	|6^5-6	|C(16,5)*6	|[('R.0.1', 5.0, u'5', u'5')]	|
|5	|6^5-6	|(6^4*5)/5!	|[('R.0.1', 5.0, u'5', u'5')]	|
|6	|5^5-5	|5*5*5*5*4	|[('R.0.1', 5.0, u'5', u'5')]	|
|7	|5^5-5	|(4^5) - 50	|[('R.0.1', 5.0, u'5', u'5')]	|
|8	|5^5-5	|[5*(16!/(11!5!))]-5-36	|[('R.0.1', 5.0, u'5', u'5')]	|
|9	|5^5-5	|4^5-1	|[('R.0.1', 5.0, u'5', u'5')]	|
|10	|5^5-5	|4^5 - 4	|[('R.0.1', 5.0, u'5', u'5')]	|
|11	|5^5-5	|(5^5 -5)*13	|[('R.0.1', 5.0, u'5', u'5')]	|
|12	|4^5-4	|C(11,5)*4^5	|[('R.0.1', 5.0, u'5', u'5')]	|
|13	|6^5-6	|C(66, 5)-C(11, 5)	|[('R.0.1', 5.0, u'5', u'5')]	|
|14	|6^5-6	|C(6,5) - 4	|[('R.0.1', 5.0, u'5', u'5')]	|
|15	|6^5-6	|C(6,5) - 6	|[('R.0.1', 5.0, u'5', u'5')]	|
|16	|5^5-5	|4^5-4	|[('R.0.1', 5.0, u'5', u'5')]	|
|17	|4^5-4	|6^5 -6	|[('R.0.1', 5.0, u'5', u'5')]	|
|18	|5^5-5	|(9*5)^5 - 9*5	|[('R.0.1', 5.0, u'5', u'5')]	|
|19	|5^5-5	|(9*5)^4	|[('R.0.1', 5.0, u'5', u'5')]	|
|20	|5^5-5	|9^5 - 45	|[('R.0.1', 5.0, u'5', u'5')]	|
|21	|5^5-5	|9^5 - 9	|[('R.0.1', 5.0, u'5', u'5')]	|
|22	|5^5-5	|9^5 - 40	|[('R.0.1', 5.0, u'5', u'5')]	|
|23	|5^5-5	|9 * 5^5 - 5 - 45	|[('R.0.1', 5.0, u'5', u'5')]	|
|24	|5^5-5	|C(60,5) -45	|[('R.0.1', 5.0, u'5', u'5')]	|
|25	|5^5-5	|C(12,5) -45	|[('R.0.1', 5.0, u'5', u'5')]	|
|26	|6^5-6	|C(6,5)*14	|[('R.0.1', 5.0, u'5', u'5')]	|
|27	|5^5-5	|C(9,5) - 45	|[('R.0.1', 5.0, u'5', u'5')]	|
|28	|4^5-4	|C(4,1)*5 -4	|[('R.0.1', 5.0, u'5', u'5')]	|
|29	|4^5-4	|6^5 - 4	|[('R.0.1', 5.0, u'5', u'5')]	|
|30	|4^5-4	|6^5 - 6	|[('R.0.1', 5.0, u'5', u'5')]	|
|31	|5^5-5	|4^5 - 1	|[('R.0.1', 5.0, u'5', u'5')]	|
|32	|6^5-6	|(4^5) -4	|[('R.0.1', 5.0, u'5', u'5')]	|
|33	|5^5-5	|(5!/(2!3!))+(5!/(3!2!))+(5!/(4!1!))+1	|[('R.0.1', 5.0, u'5', u'5!/(4!1!)')]	|
|34	|6^5-6	|(6*5) - 6	|[('R.0.1', 5.0, u'5', u'5')]	|
|35	|6^5-6	|(4^5)-4	|[('R.0.1', 5.0, u'5', u'5')]	|
|36	|4^5-4	|C(8,5) -4	|[('R.0.1', 5.0, u'5', u'5')]	|
|37	|4^5-4	|C(8,5)-4	|[('R.0.1', 5.0, u'5', u'5')]	|
|38	|4^5-4	|C(8,5)-1	|[('R.0.1', 5.0, u'5', u'5')]	|




### (30) Mistake Group ['R.0.0'] of size 30
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|6^5-6	|(6^4)*5	|[('R.0.0', 6.0, u'6', u'6')]	|
|1	|6^5-6	|(6^4)*5^2	|[('R.0.0', 6.0, u'6', u'6')]	|
|2	|4^5-4	|(4^4)*3	|[('R.0.0', 4.0, u'4', u'4')]	|
|3	|6^5-6	|C(6,1)*5^4*5	|[('R.0.0', 6.0, u'6', u'C(6,1)')]	|
|4	|6^5-6	|6^4*5	|[('R.0.0', 6.0, u'6', u'6')]	|
|5	|4^5-4	|4^4*15	|[('R.0.0', 4.0, u'4', u'4')]	|
|6	|6^5-6	|C(6,2)*6^3	|[('R.0.0', 6.0, u'6', u'6')]	|
|7	|4^5-4	|4^4*3	|[('R.0.0', 4.0, u'4', u'4')]	|
|8	|4^5-4	|[4^4]*3	|[('R.0.0', 4.0, u'4', u'4')]	|
|9	|4^5-4	|4*3+12*2*24	|[('R.0.0', 4.0, u'4', u'4')]	|
|10	|6^5-6	|(C(6,1)^4) * C(5,1)	|[('R.0.0', 6.0, u'6', u'C(6,1)')]	|
|11	|6^5-6	|C(6,2) * 6^3	|[('R.0.0', 6.0, u'6', u'6')]	|
|12	|4^5-4	|C(4,1)*C(4,1)*C(4,1)C(3,1)	|[('R.0.0', 4.0, u'4', u'C(4,1)')]	|
|13	|4^5-4	|4**4 * 3	|[('R.0.0', 4.0, u'4', u'4')]	|
|14	|4^5-4	|C(4,1)*5 -5	|[('R.0.0', 4.0, u'4', u'C(4,1)')]	|
|15	|4^5-4	|(C(4,2))^2	|[('R.0.0', 4.0, u'4', u'4')]	|
|16	|6^5-6	|6!*11	|[('R.0.0', 6.0, u'6', u'6')]	|
|17	|6^5-6	|6!/(2!4!)	|[('R.0.0', 6.0, u'6', u'6')]	|
|18	|6^5-6	|6! - 1	|[('R.0.0', 6.0, u'6', u'6')]	|
|19	|6^5-6	|6! - 5	|[('R.0.0', 6.0, u'6', u'6')]	|
|20	|6^5-6	|6!/(6-5)!	|[('R.0.0', 6.0, u'6', u'6')]	|
|21	|6^5-6	|6!5!	|[('R.0.0', 6.0, u'6', u'6')]	|
|22	|4^5-4	|4^4 * 3	|[('R.0.0', 4.0, u'4', u'4')]	|




### (28) Mistake Group Fraction of size 28




### (6) Mistake Group Wrong_Sign of size 6




### (1) Mistake Group ['R.0.0', 'R.0.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4^5-4	|4*5 - 1	|[('R.0.0', 4.0, u'4', u'4'), ('R.0.1', 5.0, u'5', u'5')]	|




### (135) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:apokhare

	first_attempt
					2015-10-13 19:10:59
	part2_incorrect_attempt
					('0:00:00', u'4^5')
	part2_correct_attempt
					['0:00:43', u'4^5-4']

1 Student ID:v4zhang

	first_attempt
					2015-10-15 22:48:40
	part2_incorrect_attempt
					('-1 day, 9:00:22', u'C(4, 4)*C(4, 3)*C(4, 2)')
					('-1 day, 21:11:04', u'C(4, 4)+C(4, 3)+C(4, 2)')
	part2_correct_attempt
					['0:01:13', u'(C(4, 1))^5 - C(4, 1)']

2 Student ID:kvass

	first_attempt
					2015-10-14 07:11:21
	part2_incorrect_attempt
					('0:05:59', u'4**5')
	part2_correct_attempt
					['0:07:41', u'4**5-4']

3 Student ID:msaguiar

	first_attempt
					2015-10-14 04:53:58
	part2_incorrect_attempt
					('-1 day, 23:55:41', u'(5*4)-4')
					('0:04:53', u'(5^4)-4')
	part2_correct_attempt
					['0:05:10', u'(4^5)-4']

4 Student ID:ssamudra

	first_attempt
					2015-10-15 04:11:00
	part2_incorrect_attempt
					('-1 day, 23:58:44', u'5^4 - 4 ')
	part2_correct_attempt
					['0:01:10', u'4^5 - 4 ']

5 Student ID:alakamsa

	first_attempt
					2015-10-10 20:56:42
	part2_incorrect_attempt
					('0:00:18', u'C(6,1)*5^4')
					('0:04:20', u'C(5,1)*6^4*C(6,1)')
					('0:04:45', u'6^4*5*5')
	part2_correct_attempt
					['0:06:55', u'6^5-6']

6 Student ID:dcgriffi

	first_attempt
					2015-10-14 07:38:38
	part2_incorrect_attempt
					('-1 day, 23:59:17', u'6*6*6*6*5')
	part2_correct_attempt
					['0:00:55', u'6^5-1']

7 Student ID:r1gu

	first_attempt
					2015-10-15 22:44:59
	part2_incorrect_attempt
					('0:01:04', u'4^4*3')
					('0:01:22', u'(4^4*3)*5')
	part2_correct_attempt
					['0:02:56', u'6^5-6']

8 Student ID:ctgraves

	first_attempt
					2015-10-14 00:13:45
	part2_incorrect_attempt
					('0:00:39', u'4!')
					('0:00:58', u'5!/(4!)')
					('0:01:16', u'12*5!/(4!)')
					('0:03:26', u'8!/(3!*5!) - 4')
					('0:03:32', u'8!/(3!*5!)')
					('0:08:27', u'8!/(3!*5!)')
					('1 day, 3:59:46', u'5*8!/(3!*5!) - 4')
					('1 day, 4:43:22', u'8!/(3!*5!)-4')
					('1 day, 4:49:26', u'4!')
	part2_correct_attempt
					['1 day, 4:56:10', u'4^5-4']

9 Student ID:nhn018

	first_attempt
					2015-10-15 20:55:57
	part2_incorrect_attempt
					('0:00:00', u'9*5^5-5')
	part2_correct_attempt
					['0:00:25', u'5^5-5']

10 Student ID:vqt004

	first_attempt
					2015-10-14 05:54:21
	part2_incorrect_attempt
					('-1 day, 23:56:36', u'4^5')
					('0:02:14', u'C(4,1)')
	part2_correct_attempt
					['10:30:31', u'4^5-4']

11 Student ID:ffhaddad

	first_attempt
					2015-10-10 21:20:51
	part2_incorrect_attempt
					('0:14:24', u'11*4^5-44')
					('0:18:03', u'11*4^5')
					('0:20:26', u'4^5')
					('0:22:32', u'3*4^4')
	part2_correct_attempt
					['0:26:36', u'4^5-4']

12 Student ID:btn023

	first_attempt
					2015-10-14 01:26:01
	part2_incorrect_attempt
					('-1 day, 23:59:45', u'10*4 -4')
					('0:00:00', u'11*4 -4')
	part2_correct_attempt
					['20:47:45', u'4^5-4']

13 Student ID:lalacson

	first_attempt
					2015-10-11 23:13:35
	part2_incorrect_attempt
					('0:00:40', u'C(4,2)')
					('0:02:09', u'C(4,1)*C(3,3)')
					('0:02:45', u'4^5')
					('0:03:23', u'C(4,1)*3^4')
					('0:03:57', u'4*12')
					('0:04:37', u'4*3^4')
					('0:05:40', u'8*4')
					('0:06:53', u'4*3!')
					('0:07:06', u'3!^4')
					('0:07:15', u'3^4')
					('0:07:22', u'3^4*4')
					('0:07:27', u'3^4+4')
					('0:08:10', u'4!*4')
					('0:08:16', u'4!^4')
					('0:08:23', u'4^4!')
					('0:08:30', u'4+4!')
					('0:10:15', u'4*7')
					('0:11:35', u'4*6')
					('0:12:02', u'6^4')
					('0:12:56', u'4^5')
					('0:14:13', u'3^4+4')
	part2_correct_attempt
					['0:20:53', u'4^5-4']

14 Student ID:tcn013

	first_attempt
					2015-10-15 04:13:17
	part2_incorrect_attempt
					('0:00:29', u'C(6,5)')
					('0:02:11', u'6!')
					('0:04:50', u'C(6,1)')
					('0:08:04', u'6!')
					('0:08:38', u'6*5*4*3*2')
					('0:20:09', u'5*6')
	part2_correct_attempt
					['0:20:33', u'6^5']

15 Student ID:tstevens

	first_attempt
					2015-10-10 11:17:26
	part2_incorrect_attempt
					('0:00:45', u'5!')
					('0:01:01', u'5!-5')
					('0:01:21', u'5!-35')
	part2_correct_attempt
					['0:02:35', u'3120']

16 Student ID:l8ngo

	first_attempt
					2015-10-12 16:24:15
	part2_incorrect_attempt
					('-1 day, 23:56:50', u'4^5')
	part2_correct_attempt
					['0:09:51', u'[4^5] - 4 ']

17 Student ID:djk006

	first_attempt
					2015-10-11 08:49:29
	part2_incorrect_attempt
					('-1 day, 18:49:25', u'((8!/(3!5!))-4)')
					('-1 day, 23:47:20', u'(8!/(3!5!))-4')
	part2_correct_attempt
					['0:00:44', u'4^5-4']

18 Student ID:aysee

	first_attempt
					2015-10-13 23:18:48
	part2_incorrect_attempt
					('-1 day, 23:19:41', u'C(5,4)*C(4,1)')
	part2_correct_attempt
					['0:00:00', u'5^5-5']

19 Student ID:dando

	first_attempt
					2015-10-15 21:36:54
	part2_incorrect_attempt
					('-1 day, 23:59:08', u'6 * 6 * 6 * 6 * 5')
					('0:00:46', u'5 * 6^4')
					('0:01:17', u'6^4')
	part2_correct_attempt
					['0:02:30', u'6^5']

20 Student ID:abasu

	first_attempt
					2015-10-11 02:42:49
	part2_incorrect_attempt
					('0:06:34', u'C(4,2) + C(4,3) + C(4,4)')
					('0:06:52', u'10(C(4,2) + C(4,3) + C(4,4))')
					('0:08:54', u'(C(4,2) + C(4,3) + C(4,4))*5')
					('0:18:56', u'(4!/2!) + (4!/3!) + (4!/4!)')
					('0:19:24', u'(4!/2!*2!) + (4!/3!*1!) + (4!/4!*0!)')
					('2:00:54', u'C(4,2) + C(4,3) + C(4,4)')
					('2:05:26', u'(5^4)-5')
					('2:05:40', u'(5^4)-4')
	part2_correct_attempt
					['2:06:26', u'(4^5)-4']

21 Student ID:m4bui

	first_attempt
					2015-10-15 19:21:03
	part2_incorrect_attempt
					('0:00:49', u'13*12*11*10*9')
					('1:24:37', u'13*4^5-78')
					('1:24:47', u'13*6^5-78')
					('1:29:41', u'(13*6^5)-72')
					('1:32:40', u'(13*6^5)-6')
					('2:36:38', u'13^6-6')
					('2:36:47', u'16^6-6')
					('2:37:27', u'(13*6)^6-6')
					('2:37:46', u'(16*6)^6-6')
					('2:38:04', u'78^6-6')
	part2_correct_attempt
					['2:42:49', u'6^5-6']

22 Student ID:a2ahmed

	first_attempt
					2015-10-15 22:38:37
	part2_incorrect_attempt
					('-1 day, 23:50:38', u'C(12,5)')
					('0:00:11', u'C(9,5)')
					('0:01:15', u'C(6,5)')
					('0:01:28', u'6!')
					('0:02:28', u'C(6,5)')
					('0:03:44', u'6*6*6*6*5')
					('0:05:09', u'6!')
					('0:05:17', u'6*6*6*5')
					('0:05:23', u'6*6*6*6')
	part2_correct_attempt
					['0:05:27', u'6*6*6*6*6']

23 Student ID:arc013

	first_attempt
					2015-10-14 03:47:55
	part2_incorrect_attempt
					('0:00:22', u'5*6^4')
					('0:00:47', u'6*6*6*6*5')
	part2_correct_attempt
					['0:02:41', u'6^5-6']

24 Student ID:mitopete

	first_attempt
					2015-10-13 22:53:51
	part2_incorrect_attempt
					('0:00:40', u'4!-1')
					('0:00:45', u'4!')
					('0:23:14', u'5!-5')
	part2_correct_attempt
					['0:24:28', u'5^5-5']

25 Student ID:starinia

	first_attempt
					2015-10-15 03:09:14
	part2_incorrect_attempt
					('0:00:00', u'C(15,5)')
	part2_correct_attempt
					['0:03:13', u'4^5 - 4']

26 Student ID:tak068

	first_attempt
					2015-10-14 08:05:15
	part2_incorrect_attempt
					('-1 day, 23:42:11', u'C(14,1)C(6,1)')
					('-1 day, 23:42:55', u'C(14,1)C(6,1)^5')
					('-1 day, 23:54:43', u'C(11,1)C(6,1)^5')
					('0:00:18', u'C(6,1)')
					('0:00:41', u'11*6^5')
					('0:02:35', u'11*6^1')
					('0:02:42', u'6^1')
					('0:02:54', u'11*6')
					('0:03:11', u'C(11,1)*C(6,1)^5-C(11,1)C(6,1)')
					('0:03:27', u'C(11,1)*C(6,1)^5')
					('0:03:41', u'C(11,1)C(6,1)')
					('0:19:10', u'C(6,1)-1')
					('0:20:34', u'C(6,1)-6')
	part2_correct_attempt
					['0:20:41', u'C(6,1)^5-6']

27 Student ID:habuamar

	first_attempt
					2015-10-09 06:13:09
	part2_incorrect_attempt
					('-1 day, 23:58:08', u'4^5')
	part2_correct_attempt
					['-1 day, 23:58:47', u'4^5-4']

28 Student ID:akg009

	first_attempt
					2015-10-15 22:44:00
	part2_incorrect_attempt
					('0:02:08', u'C(8,5)')
					('0:34:14', u'4^15-4')
	part2_correct_attempt
					['0:34:21', u'4^5-4']

29 Student ID:jit002

	first_attempt
					2015-10-15 06:40:15
	part2_incorrect_attempt
					('-1 day, 23:51:13', u'6*6*6*6*5')
					('-1 day, 23:54:57', u'6*5*4*3*2')
	part2_correct_attempt
					['0:12:30', u'6^5-6']

30 Student ID:druble

	first_attempt
					2015-10-13 02:06:22
	part2_incorrect_attempt
					('-1 day, 23:46:31', u'C(5,1)^5')
	part2_correct_attempt
					['0:00:00', u'6^5 - 4']

31 Student ID:b3hwang

	first_attempt
					2015-10-15 17:43:23
	part2_incorrect_attempt
					('0:01:34', u'5!')
					('0:01:44', u'6!')
					('0:02:01', u'6!/(6-1)!')
	part2_correct_attempt
					['0:03:40', u'6^5']

32 Student ID:lrlai

	first_attempt
					2015-10-13 00:24:30
	part2_incorrect_attempt
					('0:00:00', u'4^5')
	part2_correct_attempt
					['0:02:03', u'1020']

33 Student ID:asetters

	first_attempt
					2015-10-12 06:41:59
	part2_incorrect_attempt
					('0:01:41', u'C(5,4)*3')
	part2_correct_attempt
					['0:02:18', u'4^5-4']

34 Student ID:c1sorian

	first_attempt
					2015-10-14 22:33:01
	part2_incorrect_attempt
					('0:00:22', u'6!/5!')
					('0:53:05', u'6*5*6*6*6')
					('0:55:34', u'13*6')
	part2_correct_attempt
					['0:56:11', u'6^5']

35 Student ID:atorr

	first_attempt
					2015-10-11 03:43:39
	part2_incorrect_attempt
					('0:00:49', u'4! *4')
	part2_correct_attempt
					['0:01:56', u'4^5 - 4']

36 Student ID:cprafull

	first_attempt
					2015-10-14 08:32:24
	part2_incorrect_attempt
					('0:02:44', u'4!/((2!)(2!))')
					('0:04:23', u'44!/((39!)(5!))')
					('13:48:57', u'4^5')
					('13:49:16', u'4!/((1!)(3!))')
					('13:49:28', u'[4!/((1!)(3!))]^5')
					('13:51:24', u'([4!/((1!)(3!))]^5)')
					('13:58:53', u'8*(4^5) - 32')
	part2_correct_attempt
					['14:01:22', u'4^5 - 4']

37 Student ID:krau

	first_attempt
					2015-10-14 04:23:19
	part2_incorrect_attempt
					('-1 day, 23:58:52', u'4!/2!/2!')
	part2_correct_attempt
					['0:03:05', u'4^5-4']

38 Student ID:mroknich

	first_attempt
					2015-10-15 06:37:22
	part2_incorrect_attempt
					('0:00:00', u'10*4^5')

39 Student ID:psable

	first_attempt
					2015-10-15 23:51:00
	part2_incorrect_attempt
					('-1 day, 23:47:57', u'C(6,5)')
	part2_correct_attempt
					['0:02:05', u'7775']

40 Student ID:c2qiu

	first_attempt
					2015-10-11 20:40:30
	part2_incorrect_attempt
					('0:00:22', u'5^5')
	part2_correct_attempt
					['0:01:02', u'5^5-5']

41 Student ID:dis003

	first_attempt
					2015-10-15 11:59:42
	part2_incorrect_attempt
					('0:00:27', u'5*4*3*2')
					('0:02:01', u'4*3*2*1')
					('0:03:24', u'C(4,1)')
					('0:03:48', u'C(4,1)^5')
	part2_correct_attempt
					['5:33:11', u'4^5-4']

42 Student ID:rraiyyan

	first_attempt
					2015-10-15 00:53:03
	part2_incorrect_attempt
					('-1 day, 23:59:08', u'5!')
	part2_correct_attempt
					['0:05:17', u'5^5 - 4']

43 Student ID:jhw015

	first_attempt
					2015-10-15 03:20:30
	part2_incorrect_attempt
					('-1 day, 23:57:04', u'5^5 - 4')
					('0:01:09', u'(5^5) -4')
					('0:01:13', u'(5^5) -5')
	part2_correct_attempt
					['0:03:30', u'(6^5) -6']

44 Student ID:t1tran

	first_attempt
					2015-10-10 06:30:51
	part2_incorrect_attempt
					('0:00:00', u'4*4*4*4*3')
	part2_correct_attempt
					['0:02:18', u'4^5-4']

45 Student ID:dsmonaha

	first_attempt
					2015-10-13 18:42:46
	part2_incorrect_attempt
					('0:00:32', u'C(6,5)')
					('0:01:11', u'C(13,5)')
					('0:01:30', u'C(5,1)')
	part2_correct_attempt
					['0:03:07', u'6^5']

46 Student ID:krkelkar

	first_attempt
					2015-10-14 04:44:17
	part2_incorrect_attempt
					('0:00:47', u'5**4 *4')
	part2_correct_attempt
					['0:20:00', u'5**5-5']

47 Student ID:jel075

	first_attempt
					2015-10-15 01:45:48
	part2_incorrect_attempt
					('0:04:38', u'(3!/2!)*(4!/3!)^4')
					('0:04:56', u'(4!/3!)^4')
	part2_correct_attempt
					['0:09:01', u'4^5-4']

48 Student ID:hmnaing

	first_attempt
					2015-10-14 06:39:32
	part2_incorrect_attempt
					('0:00:00', u'5^5')
					('0:00:46', u'8*5^5')
	part2_correct_attempt
					['0:02:02', u'5^5-5']

49 Student ID:edescobe

	first_attempt
					2015-10-12 20:43:17
	part2_incorrect_attempt
					('0:00:19', u'7*4^5')
					('0:00:58', u'7168-7*4')
					('0:02:34', u'C(4,2)+C(4,3)+1')
					('0:02:49', u'C(4,2)+C(4,3)')
					('1:52:49', u'C(4,2)+C(4,3)+C(4,4)')
					('23:08:49', u'C(4,1)*C(3,1)*4')
	part2_correct_attempt
					['23:36:35', u'4^5-4']

50 Student ID:w4shin

	first_attempt
					2015-10-15 00:14:08
	part2_incorrect_attempt
					('-1 day, 23:50:14', u'(5^4)*4')
	part2_correct_attempt
					['-1 day, 23:53:30', u'5^5-5']

51 Student ID:bakang

	first_attempt
					2015-10-15 02:47:23
	part2_incorrect_attempt
					('0:00:00', u'4^5')
	part2_correct_attempt
					['0:00:25', u'4^5-4']

52 Student ID:smohiman

	first_attempt
					2015-10-11 22:43:45
	part2_incorrect_attempt
					('0:02:41', u'C(6,2)')
					('0:03:38', u'C(6,2)+C(6,3)+C(6,4)+C(6,5)+C(6,6)')
	part2_correct_attempt
					['0:08:48', u'6^5-6']

53 Student ID:jtfrankl

	first_attempt
					2015-10-15 21:30:19
	part2_incorrect_attempt
					('0:00:24', u'C(6,5)')
					('0:01:20', u'6!')
					('0:01:36', u'6!/5!')
					('0:01:57', u'5+4+3+2+1')
					('0:02:11', u'5!')
					('0:02:19', u'6!')
					('0:03:03', u'C(6,1)*C(5,4)')
					('0:03:33', u'C(6,1)*C(6,4)')
					('0:05:36', u'5^6-5')
	part2_correct_attempt
					['0:05:53', u'6^5-5']

54 Student ID:cstringh

	first_attempt
					2015-10-14 00:39:28
	part2_incorrect_attempt
					('-1 day, 4:14:46', u'12!/(5!(7!)) -5')
					('0:01:00', u'15!/(5!(9!))')
					('0:01:08', u'15!/(5!(9!))  - 5')
					('0:03:11', u'12!/(5!(9!))')
					('0:03:18', u'12!/(5!(9!)) -5')
					('18:21:36', u'9*5')
					('18:23:16', u'(9*5^5) - 9*5')
					('18:23:42', u'(9*5^5)')
					('18:25:21', u'(9*5) + (9*5) + (9*5) + (9*5)')
					('18:25:45', u'(9*5) + (9*5) + (9*5) + (9*5) + (9*5)')
					('18:27:04', u'5^9')
					('18:27:14', u'9^5')
					('18:28:14', u'9^4 - 45')
					('18:28:27', u'9^4 - 40')
					('18:31:12', u'9 * 5^5 - 4 - 45')
					('18:31:23', u'9 * 5^5 - 45')
					('18:32:35', u'12 * 5^5 - 45')
					('18:32:49', u'10 * 5^5 - 45')
					('18:33:24', u'9 * 5^5 - 45')
					('18:37:32', u'5^5 ')
					('18:37:44', u'5^4')
					('18:37:51', u'1+5^4')
					('18:38:17', u'1+5^4 - 45')
					('18:38:37', u'5^4 - 45')
					('18:39:33', u'12*5^5 -45')
					('18:41:20', u'C(12,5)')
					('18:44:40', u'C(9,5)')
	part2_correct_attempt
					['18:46:43', u'5^5 - 5']

55 Student ID:v4sharma

	first_attempt
					2015-10-14 02:07:48
	part2_incorrect_attempt
					('-1 day, 23:49:42', u'C(55, 5)')
					('-1 day, 23:51:26', u'6*8')
	part2_correct_attempt
					['-1 day, 23:56:01', u'(6^5) - 6']

56 Student ID:aurodrig

	first_attempt
					2015-10-15 22:13:41
	part2_incorrect_attempt
					('0:46:06', u'7*4^5')
	part2_correct_attempt
					['0:46:33', u'4^5 - 4']

57 Student ID:aportuga

	first_attempt
					2015-10-14 00:00:16
	part2_incorrect_attempt
					('0:10:55', u'4!*4')
					('0:21:24', u'(1024*13)-52')
	part2_correct_attempt
					['2:32:55', u'1020']

58 Student ID:bpandayk

	first_attempt
					2015-10-15 22:00:36
	part2_incorrect_attempt
					('0:00:10', u'4^4 - 4')
	part2_correct_attempt
					['0:00:28', u'4^5 - 4']

59 Student ID:bkoli

	first_attempt
					2015-10-15 21:03:15
	part2_incorrect_attempt
					('0:00:47', u'5^2-5')
					('0:01:43', u'10^2-5')
					('0:01:54', u'5^2-10')
	part2_correct_attempt
					['0:07:48', u'5^5-5']

60 Student ID:hsc052

	first_attempt
					2015-10-15 06:03:40
	part2_incorrect_attempt
					('0:05:49', u'5^4-5')
	part2_correct_attempt
					['0:06:17', u'5^5-5']

61 Student ID:xil109

	first_attempt
					2015-10-10 21:15:25
	part2_incorrect_attempt
					('-1 day, 23:58:44', u'5^5')
					('-1 day, 23:58:55', u'5^5-5')
	part2_correct_attempt
					['0:00:00', u'6^5-6']

62 Student ID:dac064

	first_attempt
					2015-10-15 21:54:21
	part2_incorrect_attempt
					('0:06:38', u'C(8,5)')
	part2_correct_attempt
					['0:20:55', u'(4^5) - 4']

63 Student ID:v3doan

	first_attempt
					2015-10-11 03:29:01
	part2_incorrect_attempt
					('-1 day, 23:45:16', u'C(5,4) - 1')
					('-1 day, 23:45:22', u'C(5,4) ')
					('-1 day, 23:45:37', u'P(5,4) - 1')
	part2_correct_attempt
					['-1 day, 23:47:17', u'4^5 - 4']

64 Student ID:k3tan

	first_attempt
					2015-10-13 06:56:31
	part2_incorrect_attempt
					('0:07:37', u'(4^5-1)*9')
					('0:08:13', u'(4^5)*9-1')
	part2_correct_attempt
					['9:20:22', u'4^5-4']

65 Student ID:hkhodada

	first_attempt
					2015-10-12 00:30:20
	part2_incorrect_attempt
					('0:47:51', u'C(12,5)')
					('1:18:34', u'C(52,5)-5')
					('1:18:45', u'C(60,5)-5')
	part2_correct_attempt
					['1:21:43', u'5^5-5']

66 Student ID:glcohen

	first_attempt
					2015-10-13 21:19:16
	part2_incorrect_attempt
					('-1 day, 23:59:36', u'7 * (5^5) - 5')
					('0:00:09', u'8 * (5^5) - 5')
	part2_correct_attempt
					['0:01:19', u'(5^5) - 5']

67 Student ID:achava

	first_attempt
					2015-10-14 19:19:24
	part2_incorrect_attempt
					('-1 day, 10:41:48', u'14*6')
					('0:00:56', u'C(6,6)')
					('0:01:10', u'C(6,5)')
					('0:01:42', u'6*14')
					('0:03:42', u'5!')
					('0:04:40', u'C(6,1)*14')
					('0:04:53', u'C(14,1)*6')
					('0:05:11', u'14*11')
	part2_correct_attempt
					['0:06:39', u'C(6,5)^5']

68 Student ID:awollner

	first_attempt
					2015-10-11 20:31:15
	part2_incorrect_attempt
					('0:01:29', u'5^4-1')
					('0:02:30', u'5^4-4')
	part2_correct_attempt
					['0:02:51', u'4^5-4']

69 Student ID:mrchin

	first_attempt
					2015-10-14 23:00:59
	part2_incorrect_attempt
					('0:01:24', u'4*4*4*4*3')
	part2_correct_attempt
					['0:02:29', u'4*4*4*4*4 - 4']

70 Student ID:etemlock

	first_attempt
					2015-10-11 01:42:45
	part2_incorrect_attempt
					('0:00:22', u'C(4,1)^5')
	part2_correct_attempt
					['0:00:27', u'C(6,1)^5']

71 Student ID:ksmurlo

	first_attempt
					2015-10-13 23:50:53
	part2_incorrect_attempt
					('0:00:31', u'C(4,3)')
					('0:00:56', u'C(5,4)-4')
					('0:01:02', u'P(5,4)-4')
	part2_correct_attempt
					['0:01:51', u'4^5-4']

72 Student ID:jeqin

	first_attempt
					2015-10-15 13:06:06
	part2_incorrect_attempt
					('0:08:04', u'5^6 - 5')
	part2_correct_attempt
					['0:08:21', u'6^5 - 5']

73 Student ID:jnatale

	first_attempt
					2015-10-13 16:21:35
	part2_incorrect_attempt
					('0:19:30', u'65*60*55*50*36')
	part2_correct_attempt
					['0:32:21', u'3120']

74 Student ID:jblynch

	first_attempt
					2015-10-12 07:24:23
	part2_incorrect_attempt
					('0:00:00', u'6*6*6*6*5')
	part2_correct_attempt
					['0:02:45', u'6^5-6']

75 Student ID:agian

	first_attempt
					2015-10-15 07:33:51
	part2_incorrect_attempt
					('0:00:29', u'5^0')
	part2_correct_attempt
					['0:00:41', u'5^5-6']

76 Student ID:tol003

	first_attempt
					2015-10-14 01:09:46
	part2_incorrect_attempt
					('-1 day, 23:57:11', u'C(11,5)*C(4,1)^4*3')
					('0:01:40', u'C(11,5)*4^4*3')
	part2_correct_attempt
					['0:12:35', u'(4^5) - 4']

77 Student ID:aakumar

	first_attempt
					2015-10-11 02:43:55
	part2_incorrect_attempt
					('0:17:24', u'525-35')
	part2_correct_attempt
					['2:01:37', u'3125-5']

78 Student ID:hachrist

	first_attempt
					2015-10-15 04:25:28
	part2_incorrect_attempt
					('0:06:49', u'6!')
					('0:13:00', u'6!/(5!*1!)')
					('0:14:13', u'6!/(5!*1!) * 5')
	part2_correct_attempt
					['0:14:52', u'6^5 - 6']

79 Student ID:haliew

	first_attempt
					2015-10-14 00:29:54
	part2_incorrect_attempt
					('-1 day, 23:57:48', u'C(5,4)')
	part2_correct_attempt
					['-1 day, 23:59:27', u'5^5-5']

80 Student ID:kmc012

	first_attempt
					2015-10-15 04:33:03
	part2_incorrect_attempt
					('1:47:53', u'4!')
					('1:59:52', u'4^5')
	part2_correct_attempt
					['2:08:25', u'4^5-4']

81 Student ID:lahawkin

	first_attempt
					2015-10-14 05:39:14
	part2_incorrect_attempt
					('0:00:00', u'6*5*4*3*2*1')

82 Student ID:eaherman

	first_attempt
					2015-10-14 03:28:07
	part2_incorrect_attempt
					('-1 day, 23:57:06', u'5^4(4)')
	part2_correct_attempt
					['0:00:00', u'5^5-4']

83 Student ID:lguintu

	first_attempt
					2015-10-09 22:27:05
	part2_incorrect_attempt
					('-1 day, 23:57:27', u'C(5,2)')
					('-1 day, 23:59:09', u'5^5')
	part2_correct_attempt
					['-1 day, 23:59:18', u'5^5-5']

84 Student ID:jjchung

	first_attempt
					2015-10-14 20:19:56
	part2_incorrect_attempt
					('0:00:32', u'25-5')
	part2_correct_attempt
					['0:00:52', u'5^5-5']

85 Student ID:tdurrer

	first_attempt
					2015-10-09 04:54:22
	part2_incorrect_attempt
					('-1 day, 23:55:42', u'5^4')
	part2_correct_attempt
					['-1 day, 23:57:33', u'5^5-5']

86 Student ID:csl030

	first_attempt
					2015-10-14 03:17:30
	part2_incorrect_attempt
					('0:00:24', u'C(6,5)')
					('0:05:50', u'C(6,5)')
					('0:11:30', u'C(6,1)^6')
	part2_correct_attempt
					['0:18:28', u'C(6,1)^5 - 6']

87 Student ID:azkong

	first_attempt
					2015-10-15 18:17:17
	part2_incorrect_attempt
					('-1 day, 23:43:15', u'C(6, 5)')
					('0:00:22', u'C(6, 1)')
					('0:00:53', u'C(6, 5)')
	part2_correct_attempt
					['0:03:46', u'6^5']

88 Student ID:volim

	first_attempt
					2015-10-12 22:52:43
	part2_incorrect_attempt
					('0:01:07', u'4^4')
	part2_correct_attempt
					['0:02:51', u'(4^5)-4']

89 Student ID:k4ma

	first_attempt
					2015-10-15 03:49:24
	part2_incorrect_attempt
					('0:01:41', u'5!')
					('0:05:23', u'5^5')
					('0:08:03', u'5^4*4')
	part2_correct_attempt
					['0:12:41', u'5^5-5']

90 Student ID:cagatep

	first_attempt
					2015-10-14 05:40:58
	part2_incorrect_attempt
					('0:03:17', u'4^5 - 5')
	part2_correct_attempt
					['0:03:29', u'5^5 - 5']

91 Student ID:ytc012

	first_attempt
					2015-10-15 10:31:24
	part2_incorrect_attempt
					('0:08:54', u'4^5')
					('0:09:00', u'5^4')
	part2_correct_attempt
					['0:10:52', u'6^5']

92 Student ID:jfalcone

	first_attempt
					2015-10-15 19:25:18
	part2_incorrect_attempt
					('0:03:58', u'C(4,1)')
					('0:04:06', u'4^5')
					('0:04:37', u'4*4*4*4*3')
					('0:06:20', u'4*4*4*4*4')
	part2_correct_attempt
					['0:09:03', u'(4*4*4*4*4) - 4']

93 Student ID:akhmelni

	first_attempt
					2015-10-15 23:21:10
	part2_incorrect_attempt
					('0:00:54', u'C(5,4)')
	part2_correct_attempt
					['0:04:46', u'5^5-5']

94 Student ID:t2shin

	first_attempt
					2015-10-15 17:02:09
	part2_incorrect_attempt
					('0:00:44', u'5!')
					('0:01:36', u'5!/4!')
					('0:05:22', u'5*5')
					('0:07:28', u'5*4*3*2')
					('0:07:33', u'5*4*3')
					('0:09:49', u'5^5')
					('0:13:50', u'5*(16!/(5!11!))')
					('0:17:33', u'(16!/(5!11!))^5')
					('0:24:02', u'5!/(1!4!)')
					('0:26:08', u'13*5')
					('0:28:13', u'13*5!')
					('0:33:47', u'5!')
					('4:17:17', u'5!-5')
	part2_correct_attempt
					['6:14:42', u'3120']

95 Student ID:ewbrenna

	first_attempt
					2015-10-13 05:32:50
	part2_incorrect_attempt
					('0:39:32', u'5!')
					('0:39:38', u'5!-1')
					('20:27:17', u'3^5')
	part2_correct_attempt
					['2 days, 6:23:47', u'4^5-4']

96 Student ID:spw006

	first_attempt
					2015-10-13 23:01:09
	part2_incorrect_attempt
					('0:00:17', u'5^4*4 * 12')
					('0:00:59', u'5^5 * 12 - 12')
	part2_correct_attempt
					['0:03:01', u'5^5 - 5']

97 Student ID:pcdo

	first_attempt
					2015-10-13 20:32:57
	part2_incorrect_attempt
					('0:03:11', u'C(6,5)')
	part2_correct_attempt
					['0:06:03', u'6^5-4']

98 Student ID:e9brown

	first_attempt
					2015-10-14 11:15:08
	part2_incorrect_attempt
					('0:00:53', u'C(6,1) * C(5,4)')
					('0:01:20', u'C(6,1) * C(6,4)')
					('0:01:35', u'C(6,5)')
	part2_correct_attempt
					['0:08:01', u'6^5 - 5']

99 Student ID:jdeon

	first_attempt
					2015-10-11 23:28:00
	part2_incorrect_attempt
					('0:03:13', u'C(6,2) + C(6,3) + C(6,4) + C(6,5)')
	part2_correct_attempt
					['0:07:50', u'6^5 - 1']

100 Student ID:b1green

	first_attempt
					2015-10-15 21:42:37
	part2_incorrect_attempt
					('0:05:10', u'C(6,5)')

101 Student ID:p4kumar

	first_attempt
					2015-10-15 09:54:07
	part2_incorrect_attempt
					('-1 day, 23:35:57', u'5 * 5 * 5 * 5')
					('0:07:53', u'5! - 5')
					('0:09:56', u'2500 * 5')
					('0:13:43', u'5! - 50')
					('0:30:53', u'115 * 10')
					('0:49:38', u'10 * 5^5 - 50')
	part2_correct_attempt
					['0:49:48', u' 5^5 - 5']

102 Student ID:s2chaudh

	first_attempt
					2015-10-15 02:21:02
	part2_incorrect_attempt
					('-2 days, 2:59:34', u'C(5,4)')
					('-2 days, 3:06:07', u'C(5,4)*C(5,1)')
	part2_correct_attempt
					['0:02:49', u'4^5-4']

103 Student ID:syc078

	first_attempt
					2015-10-15 01:15:58
	part2_incorrect_attempt
					('-1 day, 23:58:19', u'5^5')
					('0:01:59', u'5!')
					('0:16:27', u'5! * 4! * 3! * 2! * 1!')
					('0:17:19', u'(5^4)4')
					('0:17:47', u'5^5')
					('0:18:50', u'(5^5)')
	part2_correct_attempt
					['0:18:58', u'(5^5) - 5']

104 Student ID:bmilton

	first_attempt
					2015-10-09 23:18:38
	part2_incorrect_attempt
					('0:01:33', u'5^5')
	part2_correct_attempt
					['0:01:52', u'6^5 - 6']

105 Student ID:jhc010

	first_attempt
					2015-10-15 16:27:31
	part2_incorrect_attempt
					('0:00:51', u'C(6,5)-1')
	part2_correct_attempt
					['0:01:48', u'6^5-1']

106 Student ID:rsmurlo

	first_attempt
					2015-10-14 01:06:06
	part2_incorrect_attempt
					('16:18:03', u'4^4*3*5')
					('1 day, 0:36:19', u'4^4')
	part2_correct_attempt
					['1 day, 0:37:10', u'4^5-4']

107 Student ID:agarango

	first_attempt
					2015-10-15 22:02:27
	part2_incorrect_attempt
					('-1 day, 23:35:48', u'6^3')
					('-1 day, 23:38:42', u'4*4*4*3')
					('-1 day, 23:59:29', u'4*4*4*4*4')
	part2_correct_attempt
					['0:00:09', u'1020']

108 Student ID:s6deng

	first_attempt
					2015-10-14 04:13:23
	part2_incorrect_attempt
					('0:04:32', u'3*(4^3)')
					('1 day, 2:37:56', u'C(12,5)')
					('1 day, 2:38:20', u'C(12,4)*C(11,1)')
					('1 day, 2:39:13', u'[12!/(4!8!)]*[11!/(1!10!)]')

109 Student ID:kalang

	first_attempt
					2015-10-14 23:07:25
	part2_incorrect_attempt
					('-1 day, 23:59:04', u'5!')
	part2_correct_attempt
					['0:00:59', u'6^5']

110 Student ID:jcl084

	first_attempt
					2015-10-13 20:58:27
	part2_incorrect_attempt
					('0:01:31', u'C(5,4)')
	part2_correct_attempt
					['0:02:45', u'5^5 -4']

111 Student ID:aalhaida

	first_attempt
					2015-10-15 19:11:31
	part2_incorrect_attempt
					('0:13:38', u'5^(5-4)')
					('0:13:45', u'5^5')
					('0:15:10', u'5^4')
					('0:21:37', u'5!')
	part2_correct_attempt
					['0:25:42', u'5^(5)-4']

112 Student ID:k5law

	first_attempt
					2015-10-12 06:41:06
	part2_incorrect_attempt
					('0:04:27', u'5*5')
					('0:08:08', u'[5*(16!/(11!5!))]-4-36')
					('22:12:36', u'(5*16)!/(75!5!)')
					('22:13:44', u'(5*16)!/(75!5!)-1')
					('22:17:26', u'12^5')
					('22:17:53', u'5^5')
					('22:32:34', u'13-5')
	part2_correct_attempt
					['22:39:56', u'(5^5)-5']

113 Student ID:hah008

	first_attempt
					2015-10-15 00:02:23
	part2_incorrect_attempt
					('0:11:51', u'12 * 6')
	part2_correct_attempt
					['18:01:07', u'(6^5) - 6']

114 Student ID:sippolit

	first_attempt
					2015-10-12 05:13:49
	part2_incorrect_attempt
					('0:03:18', u'5^5')
					('0:12:12', u'10*(5^5) - 40')
					('0:13:01', u'10*(5^5)')
					('0:16:26', u'(5^5)')
					('2 days, 17:55:05', u'5^5')
	part2_correct_attempt
					['3 days, 17:55:47', u'5^5-5']

115 Student ID:mcatozzi

	first_attempt
					2015-10-14 01:03:04
	part2_incorrect_attempt
					('0:03:20', u'5^5')
					('0:05:24', u'C(5,4)*5')
					('0:06:10', u'C(5,4)')
					('0:09:26', u'(5^5 -1)*5')
					('0:10:02', u'(5^5 -1)*13')
	part2_correct_attempt
					['0:15:18', u'(5^5 -5)']

116 Student ID:jnn015

	first_attempt
					2015-10-11 23:34:22
	part2_incorrect_attempt
					('0:02:13', u'6!/5! - 6')
					('0:05:29', u'10!/5!/5! - 6')
	part2_correct_attempt
					['0:14:17', u'6^5 - 6']

117 Student ID:dpereira

	first_attempt
					2015-10-10 06:10:10
	part2_incorrect_attempt
					('0:01:06', u'6^4 - 6')
	part2_correct_attempt
					['0:01:54', u'6^5 - 6']

118 Student ID:hmshah

	first_attempt
					2015-10-14 08:55:24
	part2_incorrect_attempt
					('0:03:00', u'C(5,4)')
					('0:04:24', u'C(4,1)+C(4,1)+C(4,1)+C(4,1)+C(3,1)')
					('15:26:46', u'C(4,1)+C(4,1)+C(4,1)+C(4,1)+C(4,1) - 4')
					('15:27:35', u'C(4,1)*4 -4')
	part2_correct_attempt
					['15:28:28', u'C(4,1)^5 -5']

119 Student ID:dtea

	first_attempt
					2015-10-15 23:44:15
	part2_incorrect_attempt
					('0:00:36', u'4!-1')
					('0:00:45', u'5!-1')
					('0:00:54', u'P(5,1)-1')

120 Student ID:daw023

	first_attempt
					2015-10-15 06:13:22
	part2_incorrect_attempt
					('-1 day, 23:48:25', u'C(10,1)*C(6,1)-C(6,1)')
					('-1 day, 23:49:41', u'10*C(6,1)^5')
					('-1 day, 23:50:40', u'10*C(6,1)^5-54-6')
	part2_correct_attempt
					['-1 day, 23:59:52', u'C(6,1)^5']

121 Student ID:edcole

	first_attempt
					2015-10-14 02:19:25
	part2_incorrect_attempt
					('-1 day, 23:55:43', u'4*3')
	part2_correct_attempt
					['0:00:00', u'5^5 - 4']

122 Student ID:r2fisher

	first_attempt
					2015-10-15 22:34:54
	part2_incorrect_attempt
					('0:04:30', u'5^4-11*4')
					('0:08:38', u'44*3*3*3*3-11*4')
	part2_correct_attempt
					['0:22:08', u'4^5 - 4']

123 Student ID:vasharma

	first_attempt
					2015-10-11 03:37:03
	part2_incorrect_attempt
					('0:02:23', u'C(6,5)')
					('0:02:40', u'C(10,5)')
					('0:02:45', u'C(11,5)')
					('2:12:17', u'6*5')
	part2_correct_attempt
					['3:03:25', u'(6^5-6)']

124 Student ID:hpc001

	first_attempt
					2015-10-14 23:17:35
	part2_incorrect_attempt
					('0:05:47', u'C(6,5)')
	part2_correct_attempt
					['0:06:08', u'6^5 - 6']

125 Student ID:xweng

	first_attempt
					2015-10-13 02:20:22
	part2_incorrect_attempt
					('0:01:26', u'4^5')
	part2_correct_attempt
					['0:02:15', u'4^5-4']

126 Student ID:amquinte

	first_attempt
					2015-10-14 22:45:28
	part2_incorrect_attempt
					('0:00:00', u'6480*5')

127 Student ID:ajvanega

	first_attempt
					2015-10-15 01:16:42
	part2_incorrect_attempt
					('0:15:50', u'(5^4)*4')
					('0:16:48', u'5!')
	part2_correct_attempt
					['0:18:47', u'(5^5)-5']

128 Student ID:zig006

	first_attempt
					2015-10-12 23:33:19
	part2_incorrect_attempt
					('0:00:41', u'6*6*6*6*5')
					('0:08:00', u'10!/(5!5!)-6')
					('0:13:43', u'5^4*4')
	part2_correct_attempt
					['0:14:33', u'6^5-6']

129 Student ID:zhw110

	first_attempt
					2015-10-09 05:24:16
	part2_incorrect_attempt
					('-1 day, 23:48:56', u'10*(4**5)-40')
					('-1 day, 23:52:05', u'10*(5**5)-50')
	part2_correct_attempt
					['0:00:00', u'(5**5)-5']

130 Student ID:mtrafeca

	first_attempt
					2015-10-11 06:37:09
	part2_incorrect_attempt
					('0:06:35', u'5!/4!')
					('0:07:34', u'5*4*3*2')
					('0:07:38', u'5*4*3')
					('0:13:14', u'8*3')
	part2_correct_attempt
					['15:07:51', u'4^5-4']

131 Student ID:mjethani

	first_attempt
					2015-10-15 01:26:28
	part2_incorrect_attempt
					('0:03:41', u'44!/((8!)(36!))')
					('0:07:23', u'4*4*4*4*3')
	part2_correct_attempt
					['0:09:14', u'(4^5)-4']

132 Student ID:kgrozav

	first_attempt
					2015-10-15 19:36:48
	part2_incorrect_attempt
					('0:25:21', u'C(6,5)')
					('0:26:48', u'C(6,5)-1')
					('0:36:11', u'(5^5)-1')
					('0:38:32', u'(5^5)-4')
	part2_correct_attempt
					['0:43:34', u'6^5-4']

133 Student ID:whcombs

	first_attempt
					2015-10-13 04:22:18
	part2_incorrect_attempt
					('0:00:00', u'4^5')
	part2_correct_attempt
					['0:00:28', u'4^5-4']

134 Student ID:j2phung

	first_attempt
					2015-10-15 08:49:20
	part2_incorrect_attempt
					('0:05:22', u'5!/(2!3!)')
					('0:09:26', u'(5!/(2!3!))+(5!/(3!2!))+(5!/(4!1!))')
	part2_correct_attempt
					['0:17:50', u'5^5-5']












## Part 3

### (72) Mistake Group redirect of size 72




### (36) Mistake Group Digits of size 36




### (25) Mistake Group ['R.1'] of size 25
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(12-3)*(5^5-5)	|10*(5^5-5)	|[('R.1', 3120.0, u'5^5-5', u'5^5-5')]	|
|1	|(12-3)*(5^5-5)	|8*(5^5-5)	|[('R.1', 3120.0, u'5^5-5', u'5^5-5')]	|
|2	|(14-3)*(4^5-4)	|10*(4^5-4)	|[('R.1', 1020.0, u'4^5-4', u'4^5-4')]	|
|3	|(11-3)*(6^5-6)	|7*(6^5-6)	|[('R.1', 7770.0, u'6^5-6', u'6^5-6')]	|
|4	|(11-3)*(4^5-4)	|7(4^5-4)	|[('R.1', 1020.0, u'4^5-4', u'4^5-4')]	|
|5	|(16-3)*(4^5-4)	|12 * (4^5 - 4)	|[('R.1', 1020.0, u'4^5-4', u'4^5 - 4')]	|
|6	|(11-3)*(6^5-6)	|7(6^5-6)	|[('R.1', 7770.0, u'6^5-6', u'6^5-6')]	|
|7	|(14-3)*(5^5-5)	|14 * (5^5-5)	|[('R.1', 3120.0, u'5^5-5', u'5^5-5')]	|
|8	|(11-3)*(6^5-6)	|11*(6^5-6)	|[('R.1', 7770.0, u'6^5-6', u'6^5-6')]	|
|9	|(10-3)*(5^5-5)	|10 * (5^5 - 5)	|[('R.1', 3120.0, u'5^5-5', u'5^5 - 5')]	|
|10	|(10-3)*(5^5-5)	|6 * (5^5 - 5)	|[('R.1', 3120.0, u'5^5-5', u'5^5 - 5')]	|
|11	|(10-3)*(5^5-5)	|5 * (5^5 - 5)	|[('R.1', 3120.0, u'5^5-5', u'5^5 - 5')]	|
|12	|(10-3)*(5^5-5)	|9 * (5^5 - 5)	|[('R.1', 3120.0, u'5^5-5', u'5^5 - 5')]	|
|13	|(13-3)*(5^5-5)	|11*(5^5 - 5)	|[('R.1', 3120.0, u'5^5-5', u'5^5 - 5')]	|
|14	|(13-3)*(5^5-5)	|12*(5^5 - 5)	|[('R.1', 3120.0, u'5^5-5', u'5^5 - 5')]	|
|15	|(11-3)*(5^5-5)	|(10)*(5^5-5)	|[('R.1', 3120.0, u'5^5-5', u'5^5-5')]	|
|16	|(11-3)*(5^5-5)	|(12)*(5^5-5)	|[('R.1', 3120.0, u'5^5-5', u'5^5-5')]	|
|17	|(11-3)*(5^5-5)	|7*(5^5-5)	|[('R.1', 3120.0, u'5^5-5', u'5^5-5')]	|
|18	|(11-3)*(5^5-5)	|6*(5^5-5)	|[('R.1', 3120.0, u'5^5-5', u'5^5-5')]	|
|19	|(12-3)*(6^5-6)	|12* (6^5 - 6)	|[('R.1', 7770.0, u'6^5-6', u'6^5 - 6')]	|
|20	|(16-3)*(6^5-6)	|(12)*((6^5) - (6))	|[('R.1', 7770.0, u'6^5-6', u'(6^5) - (6)')]	|
|21	|(11-3)*(4^5-4)	|10*[4^5-4]	|[('R.1', 1020.0, u'4^5-4', u'4^5-4')]	|




### (19) Mistake Group ['R.0'] of size 19
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(16-3)*(5^5-5)	|13*5	|[('R.0', 13.0, u'16-3', u'13')]	|
|1	|(10-3)*(5^5-5)	|7*3150	|[('R.0', 7.0, u'10-3', u'7')]	|
|2	|(13-3)*(4^5-4)	|10((5^4)-5)	|[('R.0', 10.0, u'13-3', u'10')]	|
|3	|(13-3)*(4^5-4)	|10((5^4)-4)	|[('R.0', 10.0, u'13-3', u'10')]	|
|4	|(11-3)*(5^5-5)	|(8!/(1! * 7!)) * (5!/(1! * 4!))^5	|[('R.0', 8.0, u'11-3', u'8!/(1! * 7!)')]	|
|5	|(15-3)*(4^5-4)	|12(4^4)	|[('R.0', 12.0, u'15-3', u'12')]	|
|6	|(16-3)*(4^5-4)	|13*4^5	|[('R.0', 13.0, u'16-3', u'13')]	|
|7	|(13-3)*(4^5-4)	|(10*4^5)	|[('R.0', 10.0, u'13-3', u'10')]	|
|8	|(12-3)*(5^5-5)	|9 * (5**4*4)	|[('R.0', 9.0, u'12-3', u'9')]	|
|9	|(11-3)*(5^5-5)	|8*5^5	|[('R.0', 8.0, u'11-3', u'8')]	|
|10	|(13-3)*(5^5-5)	|10*(5^5)	|[('R.0', 10.0, u'13-3', u'10')]	|
|11	|(16-3)*(5^5-5)	|13*5!	|[('R.0', 13.0, u'16-3', u'13')]	|
|12	|(15-3)*(4^5-4)	|12*(4^6-4)	|[('R.0', 12.0, u'15-3', u'12')]	|
|13	|(11-3)*(4^5-4)	|8(5^4 - 4 )	|[('R.0', 8.0, u'11-3', u'8')]	|
|14	|(14-3)*(5^5-5)	|11*(5^4-5)	|[('R.0', 11.0, u'14-3', u'11')]	|
|15	|(13-3)*(5^5-5)	|10 * 5	|[('R.0', 10.0, u'13-3', u'10')]	|
|16	|(16-3)*(4^5-4)	|13C(4,1)^5	|[('R.0', 13.0, u'16-3', u'13')]	|
|17	|(11-3)*(6^5-6)	|8*5	|[('R.0', 8.0, u'11-3', u'8')]	|




### (15) Mistake Group Fraction of size 15




### (6) Mistake Group ['R.0.0'] of size 6
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(14-3)*(6^5-6)	|C(14,1) * (C(6,1)^4) * C(5,1)	|[('R.0.0', 14.0, u'14', u'C(14,1)')]	|
|1	|(12-3)*(4^5-4)	|C(12,5)*C(5,4)	|[('R.0.0', 12.0, u'12', u'12')]	|
|2	|(13-3)*(5^5-5)	|13*4*3	|[('R.0.0', 13.0, u'13', u'13')]	|
|3	|(13-3)*(4^5-4)	|13*C(4, 4)*C(4, 3)*C(4, 2)	|[('R.0.0', 13.0, u'13', u'13*C(4, 4)')]	|
|4	|(13-3)*(4^5-4)	|C(13, 5)*[C(4, 4)+C(4, 3)+C(4, 2)]	|[('R.0.0', 13.0, u'13', u'13')]	|
|5	|(10-3)*(4^5-4)	|10!/(7!4!)	|[('R.0.0', 10.0, u'10', u'10')]	|




### (4) Mistake Group ['R.1.0.1'] of size 4
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(12-3)*(6^5-6)	|10(4^5-4)	|[('R.1.0.1', 5.0, u'5', u'5')]	|
|1	|(15-3)*(4^5-4)	|(4*(C(15,5) -10))	|[('R.1.0.1', 5.0, u'5', u'5')]	|
|2	|(13-3)*(5^5-5)	|9*(4^5 - 4)	|[('R.1.0.1', 5.0, u'5', u'5')]	|
|3	|(14-3)*(6^5-6)	|10*(4^5-1)	|[('R.1.0.1', 5.0, u'5', u'5')]	|




### (3) Mistake Group ['R.1.0'] of size 3
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(10-3)*(4^5-4)	|6*((4^5)-1)	|[('R.1.0', 1024.0, u'4^5', u'4^5')]	|
|1	|(16-3)*(5^5-5)	|12(5^5-1)	|[('R.1.0', 3125.0, u'5^5', u'5^5')]	|
|2	|(11-3)*(5^5-5)	|(11!/(5!6!))*(5^5-1)	|[('R.1.0', 3125.0, u'5^5', u'5^5')]	|




### (3) Mistake Group ['R.0', 'R.1.0'] of size 3
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(12-3)*(5^5-5)	|9 * (5**5-1)	|[('R.0', 9.0, u'12-3', u'9'), ('R.1.0', 3125.0, u'5^5', u'5**5')]	|
|1	|(15-3)*(5^5-5)	|12*(5*5*5*5*5 -1)	|[('R.0', 12.0, u'15-3', u'12'), ('R.1.0', 3125.0, u'5^5', u'5*5*5*5*5')]	|
|2	|(15-3)*(5^5-5)	|12*(5^5-1)	|[('R.0', 12.0, u'15-3', u'12'), ('R.1.0', 3125.0, u'5^5', u'5^5')]	|




### (2) Mistake Group Wrong_Sign of size 2




### (1) Mistake Group ['R.0.0', 'R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(11-3)*(6^5-6)	|C(11,5)*(6^5-6)	|[('R.0.0', 11.0, u'11', u'11'), ('R.1', 7770.0, u'6^5-6', u'6^5-6')]	|




### (1) Mistake Group ['R.0', 'R.1.0.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(13-3)*(5^5-5)	|10*(4^5 - 1)	|[('R.0', 10.0, u'13-3', u'10'), ('R.1.0.1', 5.0, u'5', u'5')]	|




### (23) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:phodgson

	first_attempt
					2015-10-15 06:59:55
	part1_correct_attempt
					['0:00:00', u'12']
	part2_correct_attempt
					['-1 day, 23:58:57', u'4^5 - 4']
	part3_incorrect_attempt
					('0:00:08', u'12 * 4^5 - 4')
	part3_correct_attempt
					['0:00:32', u'12 * (4^5 - 4)']

1 Student ID:agoldsht

	first_attempt
					2015-10-15 04:40:39
	part1_correct_attempt
					['0:00:00', u'12']
	part2_correct_attempt
					['0:01:13', u'5^5-5']
	part3_incorrect_attempt
					('0:02:18', u'(C(10,2)*8*C(4,2)^2*4)*12')
	part3_correct_attempt
					['0:03:13', u'(5^5-5)*12']

2 Student ID:qtluong

	first_attempt
					2015-10-12 20:42:56
	part1_correct_attempt
					['0:00:00', u'12']
	part2_correct_attempt
					['-1 day, 23:58:03', u'4^5 - 4']
	part3_incorrect_attempt
					('0:00:00', u'(4^5-4)')
	part3_correct_attempt
					['0:00:05', u'(4^5-4)(12)']

3 Student ID:spw006

	first_attempt
					2015-10-13 23:01:09
	part1_correct_attempt
					['0:00:00', u'12']
	part2_correct_attempt
					['0:03:01', u'5^5 - 5']
	part3_incorrect_attempt
					('0:03:16', u'5^5 * 12 -5')
	part3_correct_attempt
					['0:03:30', u'12(5^5-5)']

4 Student ID:krau

	first_attempt
					2015-10-14 04:23:19
	part1_correct_attempt
					['0:00:00', u'11']
	part2_correct_attempt
					['0:03:05', u'4^5-4']
	part3_incorrect_attempt
					('0:04:49', u'11 * 4^5-4')
	part3_correct_attempt
					['0:05:01', u'11 * (4^5-4)']

5 Student ID:nhn018

	first_attempt
					2015-10-15 20:55:57
	part1_correct_attempt
					['0:00:00', u'9']
	part2_correct_attempt
					['0:00:25', u'5^5-5']
	part3_incorrect_attempt
					('0:00:36', u'9*5^5-5')
	part3_correct_attempt
					['0:01:45', u'9*(5^5-5)']

6 Student ID:k4ma

	first_attempt
					2015-10-15 03:49:24
	part1_correct_attempt
					['0:00:00', u'7']
	part2_correct_attempt
					['0:12:41', u'5^5-5']
	part3_incorrect_attempt
					('0:13:02', u'7*5^5-5')
	part3_correct_attempt
					['0:13:12', u'7*(5^5-5)']

7 Student ID:rlhagen

	first_attempt
					2015-10-11 19:01:14
	part1_correct_attempt
					['0:00:00', u'13']
	part2_correct_attempt
					['0:02:11', u'4^5-4']
	part3_incorrect_attempt
					('0:02:56', u'13*4^5-4')
	part3_correct_attempt
					['0:03:51', u'13*(4^5-4)']

8 Student ID:ganajera

	first_attempt
					2015-10-10 23:26:58
	part1_correct_attempt
					['0:00:00', u'11']
	part2_correct_attempt
					['0:00:00', u'(5^5)-(5)']
	part3_incorrect_attempt
					('0:00:00', u'11*(5^5)-(5)')
	part3_correct_attempt
					['0:00:43', u'11*((5^5)-(5))']

9 Student ID:nnh002

	first_attempt
					2015-10-15 06:20:28
	part1_correct_attempt
					['0:00:00', u'9']
	part2_correct_attempt
					['0:00:51', u'4^5-4']
	part3_incorrect_attempt
					('0:00:51', u'9*4^5-4')
	part3_correct_attempt
					['0:01:12', u'9*(4^5-4)']

10 Student ID:dis003

	first_attempt
					2015-10-15 11:59:42
	part1_correct_attempt
					['0:00:00', u'13']
	part2_correct_attempt
					['5:33:11', u'4^5-4']
	part3_incorrect_attempt
					('5:33:39', u'13*4^5-4')
					('5:33:58', u'7*4^5-4')
	part3_correct_attempt
					['5:34:08', u'13*(4^5-4)']

11 Student ID:atorr

	first_attempt
					2015-10-11 03:43:39
	part1_correct_attempt
					['0:00:00', u'7']
	part2_correct_attempt
					['0:01:56', u'4^5 - 4']
	part3_incorrect_attempt
					('0:02:17', u'7 * 4^5 - 4')
	part3_correct_attempt
					['0:02:36', u'7 * (4^5 - 4)']

12 Student ID:rraiyyan

	first_attempt
					2015-10-15 00:53:03
	part1_correct_attempt
					['0:00:00', u'13']
	part2_correct_attempt
					['0:05:17', u'5^5 - 4']
	part3_incorrect_attempt
					('0:05:35', u'13 * 5^5 - 4')
	part3_correct_attempt
					['0:05:56', u'13 * (5^5 - 4)']

13 Student ID:dsmonaha

	first_attempt
					2015-10-13 18:42:46
	part1_correct_attempt
					['0:00:00', u'13']
	part2_correct_attempt
					['0:03:07', u'6^5']
	part3_incorrect_attempt
					('0:04:39', u'13*12*11*10*9*6^5')
	part3_correct_attempt
					['0:04:58', u'13*6^5']

14 Student ID:pthsu

	first_attempt
					2015-10-10 20:39:34
	part1_correct_attempt
					['0:00:00', u'7']
	part2_correct_attempt
					['0:05:37', u'(4*4*4*4*4 )- 4']
	part3_incorrect_attempt
					('0:06:04', u'1020-7')
	part3_correct_attempt
					['0:06:22', u'1020*7']

15 Student ID:haliew

	first_attempt
					2015-10-14 00:29:54
	part1_correct_attempt
					['0:00:00', u'9']
	part2_correct_attempt
					['-1 day, 23:59:27', u'5^5-5']
	part3_incorrect_attempt
					('0:00:00', u'9*5^5-5')
	part3_correct_attempt
					['0:00:19', u'9*(5^5-5)']

16 Student ID:hmshah

	first_attempt
					2015-10-14 08:55:24
	part1_correct_attempt
					['0:00:00', u'8']
	part2_correct_attempt
					['15:28:28', u'C(4,1)^5 -5']
	part3_incorrect_attempt
					('15:29:11', u'8*C(4,1)^5 -5')
	part3_correct_attempt
					['15:29:25', u'8*(C(4,1)^5 -5)']

17 Student ID:flhernan

	first_attempt
					2015-10-14 22:12:33
	part1_correct_attempt
					['0:00:00', u'12']
	part2_correct_attempt
					['0:03:13', u'4^5-4']
	part3_incorrect_attempt
					('0:04:30', u'12*4^5-4')
	part3_correct_attempt
					['0:04:42', u'12*(4^5-4)']

18 Student ID:aurodrig

	first_attempt
					2015-10-15 22:13:41
	part1_correct_attempt
					['0:00:00', u'7']
	part2_correct_attempt
					['0:46:33', u'4^5 - 4']
	part3_incorrect_attempt
					('0:53:23', u'(4^5-4)*10')
	part3_correct_attempt
					['0:53:43', u'(4^5-4)*7']

19 Student ID:c3chung

	first_attempt
					2015-10-15 22:50:09
	part1_correct_attempt
					['0:00:00', u'10']
	part2_correct_attempt
					['0:00:00', u'6^5']
	part3_incorrect_attempt
					('0:00:00', u'7*6^5')
	part3_correct_attempt
					['0:00:48', u'10*6^5']

20 Student ID:yos017

	first_attempt
					2015-10-14 07:32:47
	part1_correct_attempt
					['0:00:00', u'10']
	part2_correct_attempt
					['0:02:25', u'5^5-5']
	part3_incorrect_attempt
					('0:02:44', u'10*5^5-5')
	part3_correct_attempt
					['0:02:54', u'10*(5^5-5)']

21 Student ID:dac064

	first_attempt
					2015-10-15 21:54:21
	part1_correct_attempt
					['0:00:00', u'11']
	part2_correct_attempt
					['0:20:55', u'(4^5) - 4']
	part3_incorrect_attempt
					('0:21:41', u'11 * (4^5)-4')
	part3_correct_attempt
					['0:21:49', u'11 * ((4^5)-4)']

22 Student ID:v3doan

	first_attempt
					2015-10-11 03:29:01
	part1_correct_attempt
					['0:00:00', u'7']
	part2_correct_attempt
					['-1 day, 23:47:17', u'4^5 - 4']
	part3_incorrect_attempt
					('0:00:13', u'4^5 - 4 * 7')
	part3_correct_attempt
					['0:00:25', u'(4^5 - 4 )* 7']












## Part 4

### (68) Mistake Group ['R.0'] of size 68
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(12-3)*(5^5-5)/[C(60,5)]	|[9*(5^5-5)]/C(70,5)	|[('R.0', 28080.0, u'(12-3)*(5^5-5)', u'9*(5^5-5)')]	|
|1	|(13-3)*(5^5-5)/[C(65,5)]	|(10*(5**5)-50)/C(52,5)	|[('R.0', 31200.0, u'(13-3)*(5^5-5)', u'10*(5**5)-50')]	|
|2	|(12-3)*(6^5-6)/[C(72,5)]	|(9*(6^5-6))/C(84,5)	|[('R.0', 69930.0, u'(12-3)*(6^5-6)', u'9*(6^5-6)')]	|
|3	|(12-3)*(6^5-6)/[C(72,5)]	|(9*(C(6,1)^5 - 6))/C(84,5)	|[('R.0', 69930.0, u'(12-3)*(6^5-6)', u'9*(C(6,1)^5 - 6)')]	|
|4	|(11-3)*(6^5-6)/[C(66,5)]	|8 * (6^5 - 6) / C(16*11, 5)	|[('R.0', 62160.0, u'(11-3)*(6^5-6)', u'8 * (6^5 - 6)')]	|
|5	|(14-3)*(5^5-5)/[C(70,5)]	|(11*((5^5)-(5)))/(C(80,5))	|[('R.0', 34320.0, u'(14-3)*(5^5-5)', u'11*((5^5)-(5))')]	|
|6	|(13-3)*(5^5-5)/[C(65,5)]	|31200/((75)!/(5!(75-5)!))	|[('R.0', 31200.0, u'(13-3)*(5^5-5)', u'31200')]	|
|7	|(10-3)*(4^5-4)/[C(40,5)]	|(4^5 - 4) * 7 / C(52,5)	|[('R.0', 7140.0, u'(10-3)*(4^5-4)', u'(4^5 - 4) * 7')]	|
|8	|(10-3)*(4^5-4)/[C(40,5)]	|[7 * (4^5 - 4)]/[10^5]	|[('R.0', 7140.0, u'(10-3)*(4^5-4)', u'7 * (4^5 - 4)')]	|
|9	|(16-3)*(6^5-6)/[C(96,5)]	|[(6^5-6)*13]/C(52,2)	|[('R.0', 101010.0, u'(16-3)*(6^5-6)', u'(6^5-6)*13')]	|
|10	|(16-3)*(6^5-6)/[C(96,5)]	|[(6^5-6)*13]/C(52,5)	|[('R.0', 101010.0, u'(16-3)*(6^5-6)', u'(6^5-6)*13')]	|
|11	|(16-3)*(6^5-6)/[C(96,5)]	|[(6^5-6)*13]/C(66,5)	|[('R.0', 101010.0, u'(16-3)*(6^5-6)', u'(6^5-6)*13')]	|
|12	|(12-3)*(4^5-4)/[C(48,5)]	|(9*(4^5-4))/(48!/5!43!)	|[('R.0', 9180.0, u'(12-3)*(4^5-4)', u'9*(4^5-4)')]	|
|13	|(10-3)*(5^5-5)/[C(50,5)]	|(7*(5^5-5))/(50!/((50-5)!-5!))	|[('R.0', 21840.0, u'(10-3)*(5^5-5)', u'7*(5^5-5)')]	|
|14	|(11-3)*(4^5-4)/[C(44,5)]	|8*1020/(52!(5!*47!))	|[('R.0', 8160.0, u'(11-3)*(4^5-4)', u'8*1020')]	|
|15	|(11-3)*(4^5-4)/[C(44,5)]	|8*1020/(52!/(5!*47!))	|[('R.0', 8160.0, u'(11-3)*(4^5-4)', u'8*1020')]	|
|16	|(10-3)*(5^5-5)/[C(50,5)]	|7*(5*5*5*5*5-5)/(60!/5!/55!)	|[('R.0', 21840.0, u'(10-3)*(5^5-5)', u'7*(5*5*5*5*5-5)')]	|
|17	|(10-3)*(5^5-5)/[C(50,5)]	|7*(5*5*5*5*5-5)/(60!/(5!55!))	|[('R.0', 21840.0, u'(10-3)*(5^5-5)', u'7*(5*5*5*5*5-5)')]	|
|18	|(10-3)*(5^5-5)/[C(50,5)]	|7*(5*5*5*5*5-5)/[60!/(5!55!)]	|[('R.0', 21840.0, u'(10-3)*(5^5-5)', u'7*(5*5*5*5*5-5)')]	|
|19	|(10-3)*(5^5-5)/[C(50,5)]	|21840/5461512	|[('R.0', 21840.0, u'(10-3)*(5^5-5)', u'21840')]	|
|20	|(10-3)*(5^5-5)/[C(50,5)]	|7*(5**5-5)/C(60,5)	|[('R.0', 21840.0, u'(10-3)*(5^5-5)', u'7*(5**5-5)')]	|
|21	|(13-3)*(5^5-5)/[C(65,5)]	|([(5^5)-5]*[10])/(C(15*5,5))	|[('R.0', 31200.0, u'(13-3)*(5^5-5)', u'[(5^5)-5]*[10]')]	|
|22	|(14-3)*(6^5-6)/[C(84,5)]	|(7770*11)/(84!/5!79!)	|[('R.0', 85470.0, u'(14-3)*(6^5-6)', u'7770*11')]	|
|23	|(16-3)*(5^5-5)/[C(80,5)]	|[13*[(5^5)-5]]/[55!/(5!50!)]	|[('R.0', 40560.0, u'(16-3)*(5^5-5)', u'13*[(5^5)-5]')]	|
|24	|(13-3)*(4^5-4)/[C(52,5)]	|10200/7624512	|[('R.0', 10200.0, u'(13-3)*(4^5-4)', u'10200')]	|
|25	|(12-3)*(5^5-5)/[C(60,5)]	|(9*(5^5-5))/C(52,5)	|[('R.0', 28080.0, u'(12-3)*(5^5-5)', u'9*(5^5-5)')]	|
|26	|(16-3)*(5^5-5)/[C(80,5)]	|((5^5 -5)*13)/C(55,5)	|[('R.0', 40560.0, u'(16-3)*(5^5-5)', u'(5^5 -5)*13')]	|
|27	|(12-3)*(5^5-5)/[C(60,5)]	|[(5^5 - 5)*9]/[60!/(60-5)!5!]	|[('R.0', 28080.0, u'(12-3)*(5^5-5)', u'(5^5 - 5)*9')]	|
|28	|(10-3)*(5^5-5)/[C(50,5)]	|7 * (5^5 - 5) / 8259888	|[('R.0', 21840.0, u'(10-3)*(5^5-5)', u'7 * (5^5 - 5)')]	|
|29	|(15-3)*(6^5-6)/[C(90,5)]	|12*(6^5 - 6)/((6*15)!/(5!*(6*5-5)!))	|[('R.0', 93240.0, u'(15-3)*(6^5-6)', u'12*(6^5 - 6)')]	|
|30	|(15-3)*(6^5-6)/[C(90,5)]	|[12*(6^5 - 6)]/(90!/85!)	|[('R.0', 93240.0, u'(15-3)*(6^5-6)', u'12*(6^5 - 6)')]	|
|31	|(13-3)*(6^5-6)/[C(78,5)]	|77700/43949268	|[('R.0', 77700.0, u'(13-3)*(6^5-6)', u'77700')]	|
|32	|(13-3)*(5^5-5)/[C(65,5)]	|[10*[(5^5) - 5]]/C(80,5)	|[('R.0', 31200.0, u'(13-3)*(5^5-5)', u'10*[(5^5) - 5]')]	|
|33	|(10-3)*(5^5-5)/[C(50,5)]	|(7 * (5^5 - 5))/(50*49*48*47*46)	|[('R.0', 21840.0, u'(10-3)*(5^5-5)', u'7 * (5^5 - 5)')]	|
|34	|(15-3)*(5^5-5)/[C(75,5)]	|(15-3)*(5^5-5)/C(55,5)	|[('R.0', 37440.0, u'(15-3)*(5^5-5)', u'(15-3)*(5^5-5)')]	|
|35	|(13-3)*(4^5-4)/[C(52,5)]	|10200/5461512	|[('R.0', 10200.0, u'(13-3)*(4^5-4)', u'10200')]	|
|36	|(13-3)*(5^5-5)/[C(65,5)]	|31200/(80!/(5!*75!))	|[('R.0', 31200.0, u'(13-3)*(5^5-5)', u'31200')]	|
|37	|(14-3)*(4^5-4)/[C(56,5)]	|11*(4^5-4)/C(52,5)	|[('R.0', 11220.0, u'(14-3)*(4^5-4)', u'11*(4^5-4)')]	|
|38	|(15-3)*(4^5-4)/[C(60,5)]	|(12*(4^5-4))/(C(52,5))	|[('R.0', 12240.0, u'(15-3)*(4^5-4)', u'12*(4^5-4)')]	|
|39	|(11-3)*(4^5-4)/[C(44,5)]	|8160/[(44!)/((40!)(4!))]	|[('R.0', 8160.0, u'(11-3)*(4^5-4)', u'8160')]	|
|40	|(13-3)*(5^5-5)/[C(65,5)]	|31200/(75!/(5!*70!))	|[('R.0', 31200.0, u'(13-3)*(5^5-5)', u'31200')]	|
|41	|(14-3)*(5^5-5)/[C(70,5)]	|(11*((5^5)-5))/(70!/65!5!)	|[('R.0', 34320.0, u'(14-3)*(5^5-5)', u'11*((5^5)-5)')]	|
|42	|(13-3)*(5^5-5)/[C(65,5)]	|(10((5^5) - 5))/((65!)/(60!)(5!))	|[('R.0', 31200.0, u'(13-3)*(5^5-5)', u'10((5^5) - 5)')]	|
|43	|(11-3)*(4^5-4)/[C(44,5)]	|8 * ((4^5)-4)/44	|[('R.0', 8160.0, u'(11-3)*(4^5-4)', u'8 * ((4^5)-4)')]	|
|44	|(12-3)*(5^5-5)/[C(60,5)]	|(9 * (5^5 - 5) ) / (60!/ 5!55!)	|[('R.0', 28080.0, u'(12-3)*(5^5-5)', u'9 * (5^5 - 5)')]	|
|45	|(11-3)*(4^5-4)/[C(44,5)]	|(8(4^5 - 4 ))/(52!/(47!5!))	|[('R.0', 8160.0, u'(11-3)*(4^5-4)', u'8(4^5 - 4 )')]	|
|46	|(12-3)*(6^5-6)/[C(72,5)]	|(9* (6^5 - 6))/(C((6*14),6))	|[('R.0', 69930.0, u'(12-3)*(6^5-6)', u'9* (6^5 - 6)')]	|
|47	|(12-3)*(6^5-6)/[C(72,5)]	|(9* (6^5 - 6))/(C((6*14),5))	|[('R.0', 69930.0, u'(12-3)*(6^5-6)', u'9* (6^5 - 6)')]	|
|48	|(14-3)*(4^5-4)/[C(56,5)]	|(14-3)*(4**5-4)/5	|[('R.0', 11220.0, u'(14-3)*(4^5-4)', u'(14-3)*(4**5-4)')]	|
|49	|(14-3)*(4^5-4)/[C(56,5)]	|(14-3)*(4**5-4)/2002	|[('R.0', 11220.0, u'(14-3)*(4^5-4)', u'(14-3)*(4**5-4)')]	|
|50	|(16-3)*(6^5-6)/[C(96,5)]	|101010/(66!/(5!*61!))	|[('R.0', 101010.0, u'(16-3)*(6^5-6)', u'101010')]	|
|51	|(11-3)*(4^5-4)/[C(44,5)]	|(8*[4^5-4])*C(52,5)	|[('R.0', 8160.0, u'(11-3)*(4^5-4)', u'8*[4^5-4]')]	|
|52	|(11-3)*(4^5-4)/[C(44,5)]	|(8*[4^5-4])/C(52,5)	|[('R.0', 8160.0, u'(11-3)*(4^5-4)', u'8*[4^5-4]')]	|
|53	|(11-3)*(4^5-4)/[C(44,5)]	|(8*(4^5-4))/21111090	|[('R.0', 8160.0, u'(11-3)*(4^5-4)', u'8*(4^5-4)')]	|
|54	|(15-3)*(4^5-4)/[C(60,5)]	|C(12,1)*(4^5 - 4)/658008	|[('R.0', 12240.0, u'(15-3)*(4^5-4)', u'C(12,1)*(4^5 - 4)')]	|
|55	|(15-3)*(4^5-4)/[C(60,5)]	|C(12,1)*(4^5 - 4)/(60*59*58*57*56)	|[('R.0', 12240.0, u'(15-3)*(4^5-4)', u'C(12,1)*(4^5 - 4)')]	|
|56	|(12-3)*(4^5-4)/[C(48,5)]	|9*(4^5-4)/C(60,5)	|[('R.0', 9180.0, u'(12-3)*(4^5-4)', u'9*(4^5-4)')]	|
|57	|(12-3)*(4^5-4)/[C(48,5)]	|9*(4^5-4)/C(60,4)	|[('R.0', 9180.0, u'(12-3)*(4^5-4)', u'9*(4^5-4)')]	|
|58	|(12-3)*(4^5-4)/[C(48,5)]	|(9*(4^5-4))/[48!/(44! * 4!)]	|[('R.0', 9180.0, u'(12-3)*(4^5-4)', u'9*(4^5-4)')]	|
|59	|(14-3)*(4^5-4)/[C(56,5)]	|(11 * ((4^5)-4)) / (C(64,5))	|[('R.0', 11220.0, u'(14-3)*(4^5-4)', u'11 * ((4^5)-4)')]	|
|60	|(14-3)*(4^5-4)/[C(56,5)]	|(11 * ((4^5)-4)) / (64*63*62*61*60)	|[('R.0', 11220.0, u'(14-3)*(4^5-4)', u'11 * ((4^5)-4)')]	|
|61	|(14-3)*(4^5-4)/[C(56,5)]	|11220/C(66,5)	|[('R.0', 11220.0, u'(14-3)*(4^5-4)', u'11220')]	|
|62	|(10-3)*(4^5-4)/[C(40,5)]	|(4^5-4)*7/[48!/(5!43!)]	|[('R.0', 7140.0, u'(10-3)*(4^5-4)', u'(4^5-4)*7')]	|
|63	|(16-3)*(5^5-5)/[C(80,5)]	|40560/5^5	|[('R.0', 40560.0, u'(16-3)*(5^5-5)', u'40560')]	|
|64	|(16-3)*(5^5-5)/[C(80,5)]	|40560/(16!/11!)	|[('R.0', 40560.0, u'(16-3)*(5^5-5)', u'40560')]	|
|65	|(16-3)*(5^5-5)/[C(80,5)]	|40560/(80!/75!)	|[('R.0', 40560.0, u'(16-3)*(5^5-5)', u'40560')]	|
|66	|(15-3)*(5^5-5)/[C(75,5)]	|12*(5^5-5)/(5*15)	|[('R.0', 37440.0, u'(15-3)*(5^5-5)', u'12*(5^5-5)')]	|




### (42) Mistake Group ['R.1'] of size 42
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(14-3)*(4^5-4)/[C(56,5)]	|(10*4^5)/(C(56,5))	|[('R.1', 3819816, u'C(56,5)', u'C(56,5)')]	|
|1	|(13-3)*(4^5-4)/[C(52,5)]	|10*4*4*4*4*3/C(52,5)	|[('R.1', 2598960, u'C(52,5)', u'C(52,5)')]	|
|2	|(15-3)*(5^5-5)/[C(75,5)]	|31210/C(75,5)	|[('R.1', 17259390, u'C(75,5)', u'C(75,5)')]	|
|3	|(13-3)*(5^5-5)/[C(65,5)]	|(3120*8)/[65!/(5!60!)]	|[('R.1', 8259888, u'C(65,5)', u'65!/(5!60!)')]	|
|4	|(13-3)*(5^5-5)/[C(65,5)]	|(3120*9)/[65!/(5!60!)]	|[('R.1', 8259888, u'C(65,5)', u'65!/(5!60!)')]	|
|5	|(12-3)*(6^5-6)/[C(72,5)]	|(6^5-6)*10/C(72,5)	|[('R.1', 13991544, u'C(72,5)', u'C(72,5)')]	|
|6	|(12-3)*(6^5-6)/[C(72,5)]	|(6^5-6)*11/C(72,5)	|[('R.1', 13991544, u'C(72,5)', u'C(72,5)')]	|
|7	|(15-3)*(6^5-6)/[C(90,5)]	|[C(12,1)*C(6,1)*5^4]/C(6*15,5)	|[('R.1', 43949268, u'C(90,5)', u'C(6*15,5)')]	|
|8	|(15-3)*(6^5-6)/[C(90,5)]	|[C(12,1)*5*C(6,1)*5^4]/C(6*15,5)	|[('R.1', 43949268, u'C(90,5)', u'C(6*15,5)')]	|
|9	|(16-3)*(5^5-5)/[C(80,5)]	|40625/(80!/(5!*75!))	|[('R.1', 24040016, u'C(80,5)', u'80!/(5!*75!)')]	|
|10	|(11-3)*(4^5-4)/[C(44,5)]	|(5^4-1)*8/C(44,5)	|[('R.1', 1086008, u'C(44,5)', u'C(44,5)')]	|
|11	|(11-3)*(4^5-4)/[C(44,5)]	|(5^4-4)*8/C(44,5)	|[('R.1', 1086008, u'C(44,5)', u'C(44,5)')]	|
|12	|(16-3)*(4^5-4)/[C(64,5)]	|(13*4^5-4)/(64!/(5!(64-5)!))	|[('R.1', 7624512, u'C(64,5)', u'64!/(5!(64-5)!)')]	|
|13	|(12-3)*(5^5-5)/[C(60,5)]	|40/C(60,5)	|[('R.1', 5461512, u'C(60,5)', u'C(60,5)')]	|
|14	|(13-3)*(6^5-6)/[C(78,5)]	|(10*6*6*6*6*5)/C(13*6,5)	|[('R.1', 21111090, u'C(78,5)', u'C(13*6,5)')]	|
|15	|(12-3)*(4^5-4)/[C(48,5)]	|4^5*4^4*3/[48!/[5!43!]]	|[('R.1', 1712304, u'C(48,5)', u'48!/[5!43!]')]	|
|16	|(12-3)*(4^5-4)/[C(48,5)]	|[9*[4^4]*3]/[48!/[5!43!]]	|[('R.1', 1712304, u'C(48,5)', u'48!/[5!43!]')]	|
|17	|(10-3)*(6^5-6)/[C(60,5)]	|[10*(1-[1/6^5])]/[60!/(5!*55!)]	|[('R.1', 5461512, u'C(60,5)', u'60!/(5!*55!)')]	|
|18	|(16-3)*(4^5-4)/[C(64,5)]	|((4^5-4)*12)/(64!/(5!(64-5)!))	|[('R.1', 7624512, u'C(64,5)', u'64!/(5!(64-5)!)')]	|
|19	|(16-3)*(4^5-4)/[C(64,5)]	|((4^5-4)*9)/(64!/(5!(64-5)!))	|[('R.1', 7624512, u'C(64,5)', u'64!/(5!(64-5)!)')]	|
|20	|(14-3)*(6^5-6)/[C(84,5)]	|(14 * C(5,1)^5) / C(6*14,5)	|[('R.1', 30872016, u'C(84,5)', u'C(6*14,5)')]	|
|21	|(14-3)*(4^5-4)/[C(56,5)]	|(11 * 4^5-4) / (56!/51!/5!)	|[('R.1', 3819816, u'C(56,5)', u'56!/51!/5!')]	|
|22	|(15-3)*(5^5-5)/[C(75,5)]	|(12*5*5*5*5*4)/C(75,5)	|[('R.1', 17259390, u'C(75,5)', u'C(75,5)')]	|
|23	|(16-3)*(6^5-6)/[C(96,5)]	|77760/C(96,5)	|[('R.1', 61124064, u'C(96,5)', u'C(96,5)')]	|
|24	|(15-3)*(4^5-4)/[C(60,5)]	|((4^5)12)/(C(60,5))	|[('R.1', 5461512, u'C(60,5)', u'C(60,5)')]	|
|25	|(15-3)*(4^5-4)/[C(60,5)]	|(4*(C(15,5) -10))/C(60,5)	|[('R.1', 5461512, u'C(60,5)', u'C(60,5)')]	|
|26	|(15-3)*(4^5-4)/[C(60,5)]	|(10*(6^5-4))/C(60,5)	|[('R.1', 5461512, u'C(60,5)', u'C(60,5)')]	|
|27	|(15-3)*(4^5-4)/[C(60,5)]	|(10*(6^5-6))/C(60,5)	|[('R.1', 5461512, u'C(60,5)', u'C(60,5)')]	|
|28	|(12-3)*(4^5-4)/[C(48,5)]	|((4^5-4)*8)/(48!/(5!*43!))	|[('R.1', 1712304, u'C(48,5)', u'48!/(5!*43!)')]	|
|29	|(15-3)*(5^5-5)/[C(75,5)]	|((C(10,2)*8*C(4,2)^2*4)*12)/C(75,5)	|[('R.1', 17259390, u'C(75,5)', u'C(75,5)')]	|
|30	|(14-3)*(5^5-5)/[C(70,5)]	|11*5*5*5*5*4/C(70,5)	|[('R.1', 12103014, u'C(70,5)', u'C(70,5)')]	|
|31	|(12-3)*(4^5-4)/[C(48,5)]	|(9*4^5-1)/C(48,5)	|[('R.1', 1712304, u'C(48,5)', u'C(48,5)')]	|
|32	|(12-3)*(4^5-4)/[C(48,5)]	|(9*4^5-4)/C(48,5)	|[('R.1', 1712304, u'C(48,5)', u'C(48,5)')]	|
|33	|(10-3)*(6^5-6)/[C(60,5)]	|6^5*5/C(60,5)	|[('R.1', 5461512, u'C(60,5)', u'C(60,5)')]	|
|34	|(15-3)*(4^5-4)/[C(60,5)]	|(11 * 4^5 - 4) / C(60,5)	|[('R.1', 5461512, u'C(60,5)', u'C(60,5)')]	|
|35	|(15-3)*(4^5-4)/[C(60,5)]	|(12 * 4^5 - 4) / C(60,5)	|[('R.1', 5461512, u'C(60,5)', u'C(60,5)')]	|
|36	|(14-3)*(6^5-6)/[C(84,5)]	|10*(4^5-1)/C(14*6,5)	|[('R.1', 30872016, u'C(84,5)', u'C(14*6,5)')]	|
|37	|(11-3)*(6^5-6)/[C(66,5)]	|(6*5)/C(11*6,5)	|[('R.1', 8936928, u'C(66,5)', u'C(11*6,5)')]	|
|38	|(11-3)*(6^5-6)/[C(66,5)]	|(7*5)/C(11*6,5)	|[('R.1', 8936928, u'C(66,5)', u'C(11*6,5)')]	|
|39	|(13-3)*(4^5-4)/[C(52,5)]	|1020/(52!/(5!*47!))	|[('R.1', 2598960, u'C(52,5)', u'52!/(5!*47!)')]	|
|40	|(13-3)*(6^5-6)/[C(78,5)]	|(7*6^5)/21111090	|[('R.1', 21111090, u'C(78,5)', u'21111090')]	|
|41	|(13-3)*(6^5-6)/[C(78,5)]	|(7*6^5)/(C(78,5))	|[('R.1', 21111090, u'C(78,5)', u'C(78,5)')]	|




### (39) Mistake Group redirect of size 39




### (14) Mistake Group ['R.0.0'] of size 14
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(12-3)*(6^5-6)/[C(72,5)]	|9*C(6,1)^5 - 1/6^5/C(84,5)	|[('R.0.0', 9.0, u'12-3', u'9')]	|
|1	|(12-3)*(6^5-6)/[C(72,5)]	|(9*C(6,1)^5)/C(84,5)	|[('R.0.0', 9.0, u'12-3', u'9')]	|
|2	|(12-3)*(6^5-6)/[C(72,5)]	|(9*(6^5))/C(84,5)	|[('R.0.0', 9.0, u'12-3', u'9')]	|
|3	|(10-3)*(6^5-6)/[C(60,5)]	|[C(7,1)*C(6,1)^5]/C(78,5)	|[('R.0.0', 7.0, u'10-3', u'C(7,1)')]	|
|4	|(16-3)*(4^5-4)/[C(64,5)]	|13*4^5/C(16,5)	|[('R.0.0', 13.0, u'16-3', u'13')]	|
|5	|(11-3)*(4^5-4)/[C(44,5)]	|8*C(4,1)^5 -5/ C(44,5)	|[('R.0.0', 8.0, u'11-3', u'8')]	|
|6	|(16-3)*(5^5-5)/[C(80,5)]	|13 * 5^5 - 4/C(16,5)	|[('R.0.0', 13.0, u'16-3', u'13')]	|
|7	|(10-3)*(6^5-6)/[C(60,5)]	|7 * (6^5) -6   / C(60,5)	|[('R.0.0', 7.0, u'10-3', u'7')]	|
|8	|(11-3)*(4^5-4)/[C(44,5)]	|(8(5^4 - 4 ))/(52!/(47!5!))	|[('R.0.0', 8.0, u'11-3', u'8')]	|
|9	|(10-3)*(6^5-6)/[C(60,5)]	|7 * (4^5) -4/ C(60,5)	|[('R.0.0', 7.0, u'10-3', u'7')]	|
|10	|(10-3)*(6^5-6)/[C(60,5)]	|[7 * (6^5) -6/ C(60,5)]	|[('R.0.0', 7.0, u'10-3', u'7')]	|
|11	|(10-3)*(6^5-6)/[C(60,5)]	|[7 * (6^5) -4/ C(60,5)]	|[('R.0.0', 7.0, u'10-3', u'7')]	|
|12	|(16-3)*(4^5-4)/[C(64,5)]	|13*4^5-4/C(4*16,5)	|[('R.0.0', 13.0, u'16-3', u'13')]	|
|13	|(10-3)*(6^5-6)/[C(60,5)]	|7*7771/C(72,5)	|[('R.0.0', 7.0, u'10-3', u'7')]	|




### (11) Mistake Group ['R.0.1', 'R.1'] of size 11
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(11-3)*(6^5-6)/[C(66,5)]	|[7*(6^5-6)] / C(66,5)	|[('R.0.1', 7770.0, u'6^5-6', u'6^5-6'), ('R.1', 8936928, u'C(66,5)', u'C(66,5)')]	|
|1	|(16-3)*(4^5-4)/[C(64,5)]	|12 * (4^5 - 4) / C(4*16,5)	|[('R.0.1', 1020.0, u'4^5-4', u'4^5 - 4'), ('R.1', 7624512, u'C(64,5)', u'C(4*16,5)')]	|
|2	|(14-3)*(5^5-5)/[C(70,5)]	|14 * (5^5-5)/C(70,5)	|[('R.0.1', 3120.0, u'5^5-5', u'5^5-5'), ('R.1', 12103014, u'C(70,5)', u'C(70,5)')]	|
|3	|(11-3)*(6^5-6)/[C(66,5)]	|11*(6^5-6) / C(6*11,5)	|[('R.0.1', 7770.0, u'6^5-6', u'6^5-6'), ('R.1', 8936928, u'C(66,5)', u'C(6*11,5)')]	|
|4	|(11-3)*(6^5-6)/[C(66,5)]	|7*(6^5-6) / C(6*11,5)	|[('R.0.1', 7770.0, u'6^5-6', u'6^5-6'), ('R.1', 8936928, u'C(66,5)', u'C(6*11,5)')]	|
|5	|(11-3)*(5^5-5)/[C(55,5)]	|((10)*(5^5-5))/(55!/(5!50!))	|[('R.0.1', 3120.0, u'5^5-5', u'5^5-5'), ('R.1', 3478761, u'C(55,5)', u'55!/(5!50!)')]	|
|6	|(11-3)*(5^5-5)/[C(55,5)]	|((12)*(5^5-5))/(55!/(5!50!))	|[('R.0.1', 3120.0, u'5^5-5', u'5^5-5'), ('R.1', 3478761, u'C(55,5)', u'55!/(5!50!)')]	|
|7	|(11-3)*(5^5-5)/[C(55,5)]	|(7*(5^5-5))/(55!/(50!5!))	|[('R.0.1', 3120.0, u'5^5-5', u'5^5-5'), ('R.1', 3478761, u'C(55,5)', u'55!/(50!5!)')]	|
|8	|(11-3)*(5^5-5)/[C(55,5)]	|(6*(5^5-5))/(55!/(50!5!))	|[('R.0.1', 3120.0, u'5^5-5', u'5^5-5'), ('R.1', 3478761, u'C(55,5)', u'55!/(50!5!)')]	|
|9	|(16-3)*(6^5-6)/[C(96,5)]	|((12)*((6^5) - (6)))/(61124064)	|[('R.0.1', 7770.0, u'6^5-6', u'(6^5) - (6)'), ('R.1', 61124064, u'C(96,5)', u'61124064')]	|
|10	|(14-3)*(5^5-5)/[C(70,5)]	|[(10)*(5^5-5)]/C(70,5)	|[('R.0.1', 3120.0, u'5^5-5', u'5^5-5'), ('R.1', 12103014, u'C(70,5)', u'C(70,5)')]	|




### (10) Mistake Group ['R.0.0', 'R.1'] of size 10
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(16-3)*(5^5-5)/[C(80,5)]	|13*5/C(80,5)	|[('R.0.0', 13.0, u'16-3', u'13'), ('R.1', 24040016, u'C(80,5)', u'C(80,5)')]	|
|1	|(13-3)*(4^5-4)/[C(52,5)]	|(10((5^4)-5))/(C(52,5))	|[('R.0.0', 10.0, u'13-3', u'10'), ('R.1', 2598960, u'C(52,5)', u'C(52,5)')]	|
|2	|(13-3)*(4^5-4)/[C(52,5)]	|(10((5^4)-4))/(C(52,5))	|[('R.0.0', 10.0, u'13-3', u'10'), ('R.1', 2598960, u'C(52,5)', u'C(52,5)')]	|
|3	|(16-3)*(4^5-4)/[C(64,5)]	|13*4^5/(C(64,5))	|[('R.0.0', 13.0, u'16-3', u'13'), ('R.1', 7624512, u'C(64,5)', u'C(64,5)')]	|
|4	|(13-3)*(4^5-4)/[C(52,5)]	|(10*4^5)/[52!/(5!*47!)]	|[('R.0.0', 10.0, u'13-3', u'10'), ('R.1', 2598960, u'C(52,5)', u'52!/(5!*47!)')]	|
|5	|(12-3)*(5^5-5)/[C(60,5)]	|[9*(5**4*4)]/ [60!/(5!55!)]	|[('R.0.0', 9.0, u'12-3', u'9'), ('R.1', 5461512, u'C(60,5)', u'60!/(5!55!)')]	|
|6	|(13-3)*(6^5-6)/[C(78,5)]	|(10*6^5)C(6*13, 5)	|[('R.0.0', 10.0, u'13-3', u'10'), ('R.1', 21111090, u'C(78,5)', u'C(6*13, 5)')]	|
|7	|(13-3)*(6^5-6)/[C(78,5)]	|(10*6^5)C((6*13), 5)	|[('R.0.0', 10.0, u'13-3', u'10'), ('R.1', 21111090, u'C(78,5)', u'C((6*13), 5)')]	|
|8	|(14-3)*(5^5-5)/[C(70,5)]	|11*(5^4-5)/C(70,5)	|[('R.0.0', 11.0, u'14-3', u'11'), ('R.1', 12103014, u'C(70,5)', u'C(70,5)')]	|
|9	|(11-3)*(6^5-6)/[C(66,5)]	|(8*5)/C(11*6,5)	|[('R.0.0', 8.0, u'11-3', u'8'), ('R.1', 8936928, u'C(66,5)', u'C(11*6,5)')]	|




### (6) Mistake Group ['R.0.1'] of size 6
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(12-3)*(5^5-5)/[C(60,5)]	|[11*(5^5-5)]/C(70,5)	|[('R.0.1', 3120.0, u'5^5-5', u'5^5-5')]	|
|1	|(12-3)*(5^5-5)/[C(60,5)]	|[8*(5^5-5)]/C(70,5)	|[('R.0.1', 3120.0, u'5^5-5', u'5^5-5')]	|
|2	|(10-3)*(5^5-5)/[C(50,5)]	|10 * (5^5 - 5) / 8259888	|[('R.0.1', 3120.0, u'5^5-5', u'5^5 - 5')]	|
|3	|(10-3)*(5^5-5)/[C(50,5)]	|6 * (5^5 - 5) / 8259888	|[('R.0.1', 3120.0, u'5^5-5', u'5^5 - 5')]	|
|4	|(10-3)*(5^5-5)/[C(50,5)]	|5 * (5^5 - 5) / 8259888	|[('R.0.1', 3120.0, u'5^5-5', u'5^5 - 5')]	|
|5	|(10-3)*(5^5-5)/[C(50,5)]	|9 * (5^5 - 5) / 8259888	|[('R.0.1', 3120.0, u'5^5-5', u'5^5 - 5')]	|




### (6) Mistake Group ['R.0.0', 'R.0.1.0'] of size 6
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.0.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(10-3)*(6^5-6)/[C(60,5)]	|[7*(6^5-1)]/[78!/(5!*73!)]	|[('R.0.0', 7.0, u'10-3', u'7'), ('R.0.1.0', 7776.0, u'6^5', u'6^5')]	|
|1	|(14-3)*(6^5-6)/[C(84,5)]	|(11*(6^5-1))/(52!/(5!47!))	|[('R.0.0', 11.0, u'14-3', u'11'), ('R.0.1.0', 7776.0, u'6^5', u'6^5')]	|
|2	|(16-3)*(5^5-5)/[C(80,5)]	|13 * (5^5 - 4)/C(16,5)	|[('R.0.0', 13.0, u'16-3', u'13'), ('R.0.1.0', 3125.0, u'5^5', u'5^5')]	|
|3	|(13-3)*(6^5-6)/[C(78,5)]	|((13-3)*(6^5 - 4))/(C(56,5))	|[('R.0.0', 10.0, u'13-3', u'13-3'), ('R.0.1.0', 7776.0, u'6^5', u'6^5')]	|
|4	|(13-3)*(6^5-6)/[C(78,5)]	|((13-3)*(6^5 - 4))/(C(4*13,5))	|[('R.0.0', 10.0, u'13-3', u'13-3'), ('R.0.1.0', 7776.0, u'6^5', u'6^5')]	|
|5	|(15-3)*(5^5-5)/[C(75,5)]	|12*(5^5-1)/(5*15)	|[('R.0.0', 12.0, u'15-3', u'12'), ('R.0.1.0', 3125.0, u'5^5', u'5^5')]	|




### (5) Mistake Group ['R.0', 'R.1.0'] of size 5
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(15-3)*(4^5-4)/[C(60,5)]	|C(12,1)*(4^5 - 4)/C(60,15)	|[('R.0', 12240.0, u'(15-3)*(4^5-4)', u'C(12,1)*(4^5 - 4)'), ('R.1.0', 60.0, u'60', u'60')]	|
|1	|(15-3)*(4^5-4)/[C(60,5)]	|C(12,1)*(4^5 - 4)/P(60,15)	|[('R.0', 12240.0, u'(15-3)*(4^5-4)', u'C(12,1)*(4^5 - 4)'), ('R.1.0', 60.0, u'60', u'60')]	|
|2	|(12-3)*(4^5-4)/[C(48,5)]	|9*(4^5-4)/C(48,4)	|[('R.0', 9180.0, u'(12-3)*(4^5-4)', u'9*(4^5-4)'), ('R.1.0', 48.0, u'48', u'48')]	|
|3	|(12-3)*(4^5-4)/[C(48,5)]	|9*(4^5-4)/[C(48,4)]	|[('R.0', 9180.0, u'(12-3)*(4^5-4)', u'9*(4^5-4)'), ('R.1.0', 48.0, u'48', u'48')]	|
|4	|(12-3)*(4^5-4)/[C(48,5)]	|(9*(4^5-4))/[C(48,4)]	|[('R.0', 9180.0, u'(12-3)*(4^5-4)', u'9*(4^5-4)'), ('R.1.0', 48.0, u'48', u'48')]	|




### (4) Mistake Group ['R.0.0.0', 'R.1'] of size 4
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(14-3)*(6^5-6)/[C(84,5)]	|(C(14,1) * (C(6,1)^4) * C(5,1)) / C(6*14,5)	|[('R.0.0.0', 14.0, u'14', u'C(14,1)'), ('R.1', 30872016, u'C(84,5)', u'C(6*14,5)')]	|
|1	|(12-3)*(4^5-4)/[C(48,5)]	|(C(12,5)*C(5,4))/C(48,5)	|[('R.0.0.0', 12.0, u'12', u'12'), ('R.1', 1712304, u'C(48,5)', u'C(48,5)')]	|
|2	|(13-3)*(4^5-4)/[C(52,5)]	|[13*C(4, 4)*C(4, 3)*C(4, 2)]/C(52, 5)	|[('R.0.0.0', 13.0, u'13', u'13*C(4, 4)'), ('R.1', 2598960, u'C(52,5)', u'C(52, 5)')]	|
|3	|(13-3)*(4^5-4)/[C(52,5)]	|[C(13, 5)*[C(4, 4)+C(4, 3)+C(4, 2)]]/C(52, 5)	|[('R.0.0.0', 13.0, u'13', u'13'), ('R.1', 2598960, u'C(52,5)', u'C(52, 5)')]	|




### (3) Mistake Group ['R.0.0', 'R.0.1.0', 'R.1'] of size 3
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.0.1.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(12-3)*(5^5-5)/[C(60,5)]	|[9*(5**5-1)]/ [60!/(5!55!)]	|[('R.0.0', 9.0, u'12-3', u'9'), ('R.0.1.0', 3125.0, u'5^5', u'5**5'), ('R.1', 5461512, u'C(60,5)', u'60!/(5!55!)')]	|
|1	|(15-3)*(5^5-5)/[C(75,5)]	|(12*(5*5*5*5*5 -1))/C(75,5)	|[('R.0.0', 12.0, u'15-3', u'12'), ('R.0.1.0', 3125.0, u'5^5', u'5*5*5*5*5'), ('R.1', 17259390, u'C(75,5)', u'C(75,5)')]	|
|2	|(14-3)*(6^5-6)/[C(84,5)]	|11*(6^5-1)*C(84,5)	|[('R.0.0', 11.0, u'14-3', u'11'), ('R.0.1.0', 7776.0, u'6^5', u'6^5'), ('R.1', 30872016, u'C(84,5)', u'C(84,5)')]	|




### (3) Mistake Group Wrong_Sign of size 3




### (2) Mistake Group ['R.0.0', 'R.0.1.0', 'R.1.0'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.0.1.0', 'R.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(10-3)*(6^5-6)/[C(60,5)]	|7* ((6^5) -4)/ C(60,2)	|[('R.0.0', 7.0, u'10-3', u'7'), ('R.0.1.0', 7776.0, u'6^5', u'6^5'), ('R.1.0', 60.0, u'60', u'60')]	|
|1	|(10-3)*(5^5-5)/[C(50,5)]	|7*(5^5-6)/[C(50,50)]	|[('R.0.0', 7.0, u'10-3', u'7'), ('R.0.1.0', 3125.0, u'5^5', u'5^5'), ('R.1.0', 50.0, u'50', u'50')]	|




### (1) Mistake Group Digits of size 1




### (1) Mistake Group ['R.0.0', 'R.0.1.0.1', 'R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.0.1.0.1', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(13-3)*(5^5-5)/[C(65,5)]	|(10*(4^5 - 1))/(65!/(5!*60!))	|[('R.0.0', 10.0, u'13-3', u'10'), ('R.0.1.0.1', 5.0, u'5', u'5'), ('R.1', 8259888, u'C(65,5)', u'65!/(5!*60!)')]	|




### (1) Mistake Group ['R.0.0.0', 'R.0.1', 'R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0', 'R.0.1', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(11-3)*(6^5-6)/[C(66,5)]	|C(11,5)*(6^5-6) / C(6*11,5)	|[('R.0.0.0', 11.0, u'11', u'11'), ('R.0.1', 7770.0, u'6^5-6', u'6^5-6'), ('R.1', 8936928, u'C(66,5)', u'C(6*11,5)')]	|




### (1) Mistake Group ['R.0.1.0.1', 'R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1.0.1', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(13-3)*(5^5-5)/[C(65,5)]	|(9*(4^5 - 4))/(65!/(5!*60!))	|[('R.0.1.0.1', 5.0, u'5', u'5'), ('R.1', 8259888, u'C(65,5)', u'65!/(5!*60!)')]	|




### (1) Mistake Group ['R.0.0.0'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(13-3)*(5^5-5)/[C(65,5)]	|13*4*3/(52!/(5!*47!))	|[('R.0.0.0', 13.0, u'13', u'13')]	|




### (1) Mistake Group ['R.0.1.0', 'R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(11-3)*(5^5-5)/[C(55,5)]	|((11!/(5!6!))*(5^5-1))/(55!/(5!50!))	|[('R.0.1.0', 3125.0, u'5^5', u'5^5'), ('R.1', 3478761, u'C(55,5)', u'55!/(5!50!)')]	|




### (17) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:ppanourg

	first_attempt
					2015-10-15 19:57:00
	part1_correct_attempt
					['0:00:00', u'C(12,1)']
	part2_correct_attempt
					['0:02:51', u'4^5 - 4']
	part3_correct_attempt
					['0:03:37', u'C(12,1)*(4^5 - 4)']
	part4_incorrect_attempt
					('0:03:37', u'C(12,1)*(4^5 - 4)')
					('0:09:08', u'C(12,1)*(4^5 - 4)/(60*59*58*57*56)/5!')
	part4_correct_attempt
					['0:12:32', u'C(12,1)*(4^5 - 4)/(60!/((5!*55!)))']

1 Student ID:a2ahmed

	first_attempt
					2015-10-15 22:38:37
	part1_correct_attempt
					['0:00:00', u'9']
	part2_correct_attempt
					['0:05:27', u'6*6*6*6*6']
	part3_correct_attempt
					['0:05:43', u'9*7776']
	part4_incorrect_attempt
					('0:06:05', u'69984/C(90,5)')
	part4_correct_attempt
					['0:06:19', u'69984/C(72,5)']

2 Student ID:hak014

	first_attempt
					2015-10-13 06:24:14
	part1_correct_attempt
					['0:00:00', u'11']
	part2_correct_attempt
					['-1 day, 23:54:31', u'10236']
	part3_correct_attempt
					['0:00:25', u'11*((4^5)-4)']
	part4_incorrect_attempt
					('0:00:55', u'311220/819816')
	part4_correct_attempt
					['0:01:05', u'11220/3819816']

3 Student ID:lywong

	first_attempt
					2015-10-13 09:18:24
	part1_correct_attempt
					['0:00:00', u'12']
	part3_correct_attempt
					['0:01:02', u'7771*12']
	part4_incorrect_attempt
					('0:01:02', u'7771*12/(80!/(5!75!))')
	part4_correct_attempt
					['0:02:00', u'7771*12/(90!/(5!85!))']

4 Student ID:abasu

	first_attempt
					2015-10-11 02:42:49
	part1_correct_attempt
					['0:00:00', u'10']
	part2_correct_attempt
					['2:06:26', u'(4^5)-4']
	part3_correct_attempt
					['2:06:26', u'10((4^5)-4)']
	part4_incorrect_attempt
					('2:06:26', u'10((4^5)-4)/(C(52,13))')
	part4_correct_attempt
					['2:06:47', u'10((4^5)-4)/(C(52,5))']

5 Student ID:seleon

	first_attempt
					2015-10-15 06:29:14
	part1_correct_attempt
					['0:00:00', u'14-3']
	part2_correct_attempt
					['0:00:33', u'4**5-4']
	part3_correct_attempt
					['0:01:23', u'(14-3)*(4**5-4)']
	part4_incorrect_attempt
					('0:01:37', u'(14-3)*(4**5-4)')
	part4_correct_attempt
					['0:02:39', u'(14-3)*(4**5-4)/3819816']

6 Student ID:dkostins

	first_attempt
					2015-10-15 18:40:56
	part1_correct_attempt
					['0:00:00', u'12']
	part2_correct_attempt
					['0:00:12', u'5^5-5']
	part3_correct_attempt
					['0:00:53', u'(5^5-5)*12']
	part4_incorrect_attempt
					('0:01:34', u'((5^5-5)*12)')
	part4_correct_attempt
					['0:02:24', u'((5^5-5)*12)/C(75,5)']

7 Student ID:c3chung

	first_attempt
					2015-10-15 22:50:09
	part1_correct_attempt
					['0:00:00', u'10']
	part2_correct_attempt
					['0:00:00', u'6^5']
	part3_correct_attempt
					['0:00:48', u'10*6^5']
	part4_incorrect_attempt
					('0:02:20', u'(7*6^5)/2533330800')
	part4_correct_attempt
					['0:09:25', u'(10*6^5)/(C(78,5))']

8 Student ID:xil109

	first_attempt
					2015-10-10 21:15:25
	part1_correct_attempt
					['0:00:00', u'11']
	part2_correct_attempt
					['0:00:00', u'6^5-6']
	part3_correct_attempt
					['0:01:24', u'11*6^5-6']
	part4_incorrect_attempt
					('0:01:43', u'85530/C(85,5)')
	part4_correct_attempt
					['0:01:51', u'85530/C(84,5)']

9 Student ID:any027

	first_attempt
					2015-10-12 20:32:44
	part1_correct_attempt
					['0:00:00', u'11']
	part2_correct_attempt
					['0:03:05', u'6^5-1']
	part3_correct_attempt
					['0:03:39', u'(6^5-1) * 11']
	part4_incorrect_attempt
					('0:04:11', u'(6^5-1) * 11 C(14*6,5)')
	part4_correct_attempt
					['0:04:31', u'((6^5-1) * 11 )/C(14*6,5)']

10 Student ID:mhale

	first_attempt
					2015-10-14 22:15:20
	part1_correct_attempt
					['0:00:00', u'9']
	part2_correct_attempt
					['0:00:35', u'6^5 - 1']
	part3_correct_attempt
					['0:01:05', u'7775 * 9']
	part4_incorrect_attempt
					('0:01:18', u'69975 / 30872016')
	part4_correct_attempt
					['0:02:18', u'69975 / 13991544']

11 Student ID:ytc012

	first_attempt
					2015-10-15 10:31:24
	part1_correct_attempt
					['0:00:00', u'10']
	part2_correct_attempt
					['0:10:52', u'6^5']
	part3_correct_attempt
					['0:24:09', u'10*6^5']
	part4_incorrect_attempt
					('0:25:25', u'77760/(90!/(5!85!))')
	part4_correct_attempt
					['0:25:58', u'77760/(78!/(5!73!))']

12 Student ID:s1powers

	first_attempt
					2015-10-11 19:53:32
	part1_correct_attempt
					['0:00:00', u'7']
	part2_correct_attempt
					['-1 day, 23:59:14', u'5*5*5*5*5-5']
	part3_correct_attempt
					['0:01:13', u'7*(5*5*5*5*5-5)']
	part4_incorrect_attempt
					('0:05:09', u'60!/5!55!')
					('0:05:18', u'60!/[5!55!]')
	part4_correct_attempt
					['0:05:43', u'7*(5*5*5*5*5-5)/(50!/[5!45!])']

13 Student ID:tcuddy

	first_attempt
					2015-10-10 20:12:12
	part1_correct_attempt
					['0:00:00', u'11']
	part2_correct_attempt
					['0:00:20', u'4^5-4']
	part3_correct_attempt
					['0:09:35', u'11(4**5-4)']
	part4_incorrect_attempt
					('0:10:14', u'11(4**5-4)/(56!/5!51!)')
	part4_correct_attempt
					['0:10:25', u'11(4**5-4)/(56!/(5!51!))']

14 Student ID:dcrume

	first_attempt
					2015-10-15 23:23:23
	part1_correct_attempt
					['0:00:00', u'8']
	part4_incorrect_attempt
					('0:00:00', u'24960/(5*11)!')

15 Student ID:yil035

	first_attempt
					2015-10-14 03:12:15
	part1_correct_attempt
					['0:00:00', u'13']
	part2_correct_attempt
					['0:00:00', u'5^5-5']
	part3_correct_attempt
					['0:00:00', u'13(5^5-5)']
	part4_incorrect_attempt
					('0:00:00', u'13(5^5-5)/43949268')
	part4_correct_attempt
					['0:01:28', u'13(5^5-5)/24040016']

16 Student ID:achava

	first_attempt
					2015-10-14 19:19:24
	part1_correct_attempt
					['0:00:00', u'11']
	part2_correct_attempt
					['0:06:39', u'C(6,5)^5']
	part3_correct_attempt
					['0:07:12', u'C(6,5)^5 * 11']
	part4_incorrect_attempt
					('0:07:42', u'85536/C(60, 5)')
	part4_correct_attempt
					['0:08:29', u'85536/C(84, 5)']












