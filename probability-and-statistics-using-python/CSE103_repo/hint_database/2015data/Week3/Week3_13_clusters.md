#Problem 13

    $ns = random(4,6,1);
    $nr = random(10,16,1);
    $n = $ns*$nr;

    ### Two Pairs ###

    *Remember, the deck you are using has [$ns] suits and [$nr] ranks.*

    1. The number of possibilities for the ranks of the two pairs is [______]{Compute("C($nr,2)")}.

    2. The number of possibilities for the rank of the single is [______]{$nr-2}.

    2. The number of possibilities for the suits of the two pairs is [_____]{Compute("C($ns,2)**2")}.

    3. The number of possibilities for the suit of the single is [______]{$ns}.

    4. Thus the number of hands with exactly two pairs is [______]{Compute("C($nr,2)*($nr-2)*C($ns,2)**2*$ns")}.

    5. The ratio of this number to the number of all hands [______]{Compute("C($nr,2)*($nr-2)*C($ns,2)**2*$ns/C($n,5)")}.





## Part 1

### (330) Mistake Group Digits of size 330




### (117) Mistake Group ['R.0'] of size 117
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(14,2)	|14*13	|[('R.0', 14.0, u'14', u'14')]	|
|1	|C(13,2)	|13*12	|[('R.0', 13.0, u'13', u'13')]	|
|2	|C(13,2)	|C(13,1)*C(12,1)	|[('R.0', 13.0, u'13', u'C(13,1)')]	|
|3	|C(16,2)	|C(16,1)C(15,1)	|[('R.0', 16.0, u'16', u'C(16,1)')]	|
|4	|C(16,2)	|16*15	|[('R.0', 16.0, u'16', u'16')]	|
|5	|C(12,2)	|12^4	|[('R.0', 12.0, u'12', u'12')]	|
|6	|C(12,2)	|12 * 11	|[('R.0', 12.0, u'12', u'12')]	|
|7	|C(12,2)	|12*11	|[('R.0', 12.0, u'12', u'12')]	|
|8	|C(13,2)	|13*4	|[('R.0', 13.0, u'13', u'13')]	|
|9	|C(12,2)	|C(12,1)*C(11,1)	|[('R.0', 12.0, u'12', u'C(12,1)')]	|
|10	|C(12,2)	|12*C(5,2)	|[('R.0', 12.0, u'12', u'12')]	|
|11	|C(11,2)	|11*10	|[('R.0', 11.0, u'11', u'11')]	|
|12	|C(11,2)	|11+10	|[('R.0', 11.0, u'11', u'11')]	|
|13	|C(15,2)	|15*14	|[('R.0', 15.0, u'15', u'15')]	|
|14	|C(15,2)	|15+14	|[('R.0', 15.0, u'15', u'15')]	|
|15	|C(16,2)	|16 * C(16,2)	|[('R.0', 16.0, u'16', u'16')]	|
|16	|C(16,2)	|16 * C(6,2)	|[('R.0', 16.0, u'16', u'16')]	|
|17	|C(15,2)	|15^4	|[('R.0', 15.0, u'15', u'15')]	|
|18	|C(11,2)	|11^4	|[('R.0', 11.0, u'11', u'11')]	|
|19	|C(16,2)	|C(16,1)C(4,2)C(15,1)C(4,2)C(14,1)	|[('R.0', 16.0, u'16', u'C(16,1)')]	|
|20	|C(16,2)	|C(16,1)C(4,2)C(15,1)C(4,2)	|[('R.0', 16.0, u'16', u'C(16,1)')]	|
|21	|C(10,2)	|C(10,1) * C(9, 1)	|[('R.0', 10.0, u'10', u'C(10,1)')]	|
|22	|C(14,2)	|C(14,4)	|[('R.0', 14.0, u'14', u'14')]	|
|23	|C(11,2)	|C(11,1)C(10,1)	|[('R.0', 11.0, u'11', u'C(11,1)')]	|
|24	|C(13,2)	|13 * 12	|[('R.0', 13.0, u'13', u'13')]	|
|25	|C(11,2)	|11*11	|[('R.0', 11.0, u'11', u'11')]	|
|26	|C(16,2)	|16*16	|[('R.0', 16.0, u'16', u'16')]	|
|27	|C(15,2)	|C(15,4)	|[('R.0', 15.0, u'15', u'15')]	|
|28	|C(13,2)	|C(13, 1) * C(12,1)	|[('R.0', 13.0, u'13', u'C(13, 1)')]	|
|29	|C(12,2)	|C(12, 1) * C(11, 1)	|[('R.0', 12.0, u'12', u'C(12, 1)')]	|
|30	|C(12,2)	|C(12,1) * C(12,1)	|[('R.0', 12.0, u'12', u'C(12,1)')]	|
|31	|C(12,2)	|C(12,1) * C(11,1)	|[('R.0', 12.0, u'12', u'C(12,1)')]	|
|32	|C(11,2)	|11*C(11,2)	|[('R.0', 11.0, u'11', u'11')]	|
|33	|C(14,2)	|14*14	|[('R.0', 14.0, u'14', u'14')]	|
|34	|C(13,2)	|C(13, 4)	|[('R.0', 13.0, u'13', u'13')]	|
|35	|C(13,2)	|13*13	|[('R.0', 13.0, u'13', u'13')]	|
|36	|C(13,2)	|13+12	|[('R.0', 13.0, u'13', u'13')]	|
|37	|C(13,2)	|C(13, 1)*C(13, 1)	|[('R.0', 13.0, u'13', u'C(13, 1)')]	|
|38	|C(13,2)	|C(13, 1)*C(12, 1)	|[('R.0', 13.0, u'13', u'C(13, 1)')]	|
|39	|C(14,2)	|14*6	|[('R.0', 14.0, u'14', u'14')]	|
|40	|C(14,2)	|C(14,1)*C(13,1)	|[('R.0', 14.0, u'14', u'C(14,1)')]	|
|41	|C(10,2)	|10*9	|[('R.0', 10.0, u'10', u'10')]	|
|42	|C(16,2)	|16*8	|[('R.0', 16.0, u'16', u'16')]	|
|43	|C(13,2)	|13*C(6,2)	|[('R.0', 13.0, u'13', u'13')]	|
|44	|C(16,2)	|16*(5!/((2!)(3!)))	|[('R.0', 16.0, u'16', u'16')]	|
|45	|C(11,2)	|11!	|[('R.0', 11.0, u'11', u'11')]	|
|46	|C(16,2)	|16*4	|[('R.0', 16.0, u'16', u'16')]	|
|47	|C(12,2)	|12*12	|[('R.0', 12.0, u'12', u'12')]	|
|48	|C(10,2)	|C(10,1)*C(9,1)	|[('R.0', 10.0, u'10', u'C(10,1)')]	|
|49	|C(10,2)	|C(10,1)*C(10,1)	|[('R.0', 10.0, u'10', u'C(10,1)')]	|
|50	|C(10,2)	|10*10	|[('R.0', 10.0, u'10', u'10')]	|
|51	|C(16,2)	|C(16,4)	|[('R.0', 16.0, u'16', u'16')]	|
|52	|C(11,2)	|C(11,1)*C(10,1)	|[('R.0', 11.0, u'11', u'C(11,1)')]	|
|53	|C(15,2)	|C(15,1)C(14,1)C(5,2)C(5,2)C(13,1)C(5,1)	|[('R.0', 15.0, u'15', u'C(15,1)')]	|
|54	|C(10,2)	|C(10,1)C(9,1)	|[('R.0', 10.0, u'10', u'C(10,1)')]	|




### (43) Mistake Group ['R.1'] of size 43
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(10,2)	|C(10,2)^2	|[('R.1', 2.0, u'2', u'2')]	|
|1	|C(11,2)	|C(66,2)	|[('R.1', 2.0, u'2', u'2')]	|
|2	|C(11,2)	|13*2	|[('R.1', 2.0, u'2', u'2')]	|
|3	|C(12,2)	|12 * 11 * 2	|[('R.1', 2.0, u'2', u'2')]	|
|4	|C(13,2)	|13*12*2	|[('R.1', 2.0, u'2', u'2')]	|
|5	|C(12,2)	|(12*12)*2	|[('R.1', 2.0, u'2', u'2')]	|
|6	|C(13,2)	|C(6,2)	|[('R.1', 2.0, u'2', u'2')]	|
|7	|C(11,2)	|13*12/2	|[('R.1', 2.0, u'2', u'2')]	|
|8	|C(13,2)	|78^2	|[('R.1', 2.0, u'2', u'2')]	|
|9	|C(12,2)	|C(4,2)	|[('R.1', 2.0, u'2', u'2')]	|
|10	|C(12,2)	|C(13,2)	|[('R.1', 2.0, u'2', u'2')]	|
|11	|C(15,2)	|13^2	|[('R.1', 2.0, u'2', u'2')]	|
|12	|C(16,2)	|C(15,2)	|[('R.1', 2.0, u'2', u'2')]	|
|13	|C(15,2)	|(15*14*13)/2	|[('R.1', 2.0, u'2', u'2')]	|
|14	|C(15,2)	|(15*14*13)/2!	|[('R.1', 2.0, u'2', u'2!')]	|
|15	|C(11,2)	|11!/(2!)	|[('R.1', 2.0, u'2', u'2!')]	|
|16	|C(12,2)	|264*2*2	|[('R.1', 2.0, u'2', u'2')]	|
|17	|C(11,2)	|C(5,2)	|[('R.1', 2.0, u'2', u'2')]	|
|18	|C(12,2)	|11+10+9+8+7+6+5+4+3+2	|[('R.1', 2.0, u'2', u'2')]	|
|19	|C(12,2)	|C(4, 2)	|[('R.1', 2.0, u'2', u'2')]	|
|20	|C(13,2)	|C(13, 2)*2	|[('R.1', 2.0, u'2', u'2')]	|
|21	|C(13,2)	|(13!/(2!11!))^2	|[('R.1', 2.0, u'2', u'2')]	|
|22	|C(12,2)	|C(72,2)	|[('R.1', 2.0, u'2', u'2')]	|
|23	|C(11,2)	|C(11,2)*2	|[('R.1', 2.0, u'2', u'2')]	|
|24	|C(14,2)	|14!/(2!14!)2	|[('R.1', 2.0, u'2', u'2')]	|
|25	|C(12,2)	|C(6,2)^2	|[('R.1', 2.0, u'2', u'2')]	|
|26	|C(14,2)	|14!/(2!) 	|[('R.1', 2.0, u'2', u'2!')]	|
|27	|C(16,2)	|(13*12/2)^2	|[('R.1', 2.0, u'2', u'2')]	|
|28	|C(16,2)	|(16*15/2)^2	|[('R.1', 2.0, u'2', u'2')]	|
|29	|C(10,2)	|10!/8!2!	|[('R.1', 2.0, u'2', u'2!')]	|
|30	|C(11,2)	|165^2	|[('R.1', 2.0, u'2', u'2')]	|
|31	|C(10,2)	|40^2	|[('R.1', 2.0, u'2', u'2')]	|
|32	|C(11,2)	|C(11,2)^2	|[('R.1', 2.0, u'2', u'2')]	|
|33	|C(16,2)	|C(4,2)^2	|[('R.1', 2.0, u'2', u'2')]	|
|34	|C(10,2)	|45^2	|[('R.1', 2.0, u'2', u'2')]	|




### (37) Mistake Group Fraction of size 37




### (12) Mistake Group ['R.0', 'R.1'] of size 12
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(12,2)	|12^2	|[('R.0', 12.0, u'12', u'12'), ('R.1', 2.0, u'2', u'2')]	|
|1	|C(15,2)	|15^2	|[('R.0', 15.0, u'15', u'15'), ('R.1', 2.0, u'2', u'2')]	|
|2	|C(11,2)	|11^2	|[('R.0', 11.0, u'11', u'11'), ('R.1', 2.0, u'2', u'2')]	|
|3	|C(13,2)	|13^2	|[('R.0', 13.0, u'13', u'13'), ('R.1', 2.0, u'2', u'2')]	|
|4	|C(16,2)	|16^2	|[('R.0', 16.0, u'16', u'16'), ('R.1', 2.0, u'2', u'2')]	|
|5	|C(11,2)	|C(11,1)*2	|[('R.0', 11.0, u'11', u'C(11,1)'), ('R.1', 2.0, u'2', u'2')]	|
|6	|C(10,2)	|10^2	|[('R.0', 10.0, u'10', u'10'), ('R.1', 2.0, u'2', u'2')]	|
|7	|C(14,2)	|14/(2!) 	|[('R.0', 14.0, u'14', u'14'), ('R.1', 2.0, u'2', u'2!')]	|
|8	|C(11,2)	|C(11,1)^2	|[('R.0', 11.0, u'11', u'C(11,1)'), ('R.1', 2.0, u'2', u'2')]	|




### (1) Mistake Group Wrong_Sign of size 1




### (99) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:gthorn

	first_attempt
					2015-10-13 18:29:53
	part1_incorrect_attempt
					('0:00:00', u'11 * 12')
	part1_correct_attempt
					['0:02:28', u'C(13, 2)']

1 Student ID:v4zhang

	first_attempt
					2015-10-15 07:32:42
	part1_incorrect_attempt
					('0:00:00', u'C(15, 1) ')
	part1_correct_attempt
					['0:01:30', u'C(15, 2)']

2 Student ID:kvass

	first_attempt
					2015-10-14 06:37:21
	part1_incorrect_attempt
					('0:00:00', u'C(14,2)*12*C(4,2)**2*4')
	part1_correct_attempt
					['0:19:57', u'C(14,2)']

3 Student ID:jjm019

	first_attempt
					2015-10-15 23:38:04
	part1_incorrect_attempt
					('0:00:00', u'5*45')
	part1_correct_attempt
					['0:09:04', u'45']

4 Student ID:ctgraves

	first_attempt
					2015-10-13 21:54:50
	part1_incorrect_attempt
					('0:00:00', u'11!/(2!*9!)*6*5*11!/(2!*9!)*4*11')
					('0:00:20', u'11!/(2!*9!)*6*5*11!/((2!*9!))*4*11')
					('0:00:46', u'11!/(2!*9!)*6*5*(11!/((2!*9!)))*4*11')
	part1_correct_attempt
					['2:11:41', u'11!/(2!*9!)']

5 Student ID:dkurli

	first_attempt
					2015-10-14 04:01:22
	part1_incorrect_attempt
					('0:00:00', u'40*3*38*3')
					('0:00:00', u'40*3*39*3')
					('0:00:00', u'40*3*38*3*35')
					('0:00:00', u'40*3*36*3*32')
					('0:00:00', u'10*9*6*6*8*24')
					('0:00:00', u'10!/8!/2!*12*12')
					('0:00:14', u'10!/8!/2!*6*6')
	part1_correct_attempt
					['0:06:15', u'10!/8!/2!']

6 Student ID:j5phung

	first_attempt
					2015-10-09 18:45:21
	part1_incorrect_attempt
					('0:00:00', u'C(13,13)*C(13,12)')
	part1_correct_attempt
					['0:04:44', u'C(11,2)']

7 Student ID:jyc018

	first_attempt
					2015-10-12 02:27:07
	part1_incorrect_attempt
					('0:00:00', u'5*12 + 4*12')
					('0:00:20', u'5*12 + 11 +4*12')
	part1_correct_attempt
					['0:01:28', u'C(12,2)']

8 Student ID:ffhaddad

	first_attempt
					2015-10-10 21:14:48
	part1_incorrect_attempt
					('0:00:00', u'C(4,2)C(16,1)C(4,2)C(15,1)')
					('0:02:37', u'C(16,1)')
	part1_correct_attempt
					['0:02:45', u'C(16,2)']

9 Student ID:asrana

	first_attempt
					2015-10-15 12:00:55
	part1_incorrect_attempt
					('0:00:00', u'91*36*48')
					('0:12:20', u'91*9*48')
					('0:13:30', u'4*91*9*48')
					('0:00:00', u'78*6*6')
	part1_correct_attempt
					['6:33:24', u'91']

10 Student ID:jmmcalex

	first_attempt
					2015-10-15 08:46:14
	part1_incorrect_attempt
					('0:00:00', u'2*(13^2)')
					('0:04:55', u'(13^2)*(12)')
	part1_correct_attempt
					['0:12:30', u'13*6']

11 Student ID:dgunawan

	first_attempt
					2015-10-15 19:08:43
	part1_incorrect_attempt
					('0:00:00', u'C(13, 2) * (C(4,2))^2 * C(11,1) * C(4,1)')
					('0:00:31', u'C(11, 2) * (C(4,2))^2 * C(9,1) * C(4,1)')
					('0:00:00', u'C(11, 4) * (C(4,2))^2 * C(6,1) * C(4,1)')

12 Student ID:tcn013

	first_attempt
					2015-10-15 03:51:05
	part1_incorrect_attempt
					('0:00:00', u'16*C(6,2)*C(6,4)')
					('0:06:48', u'C(16,2)C(15,2)')
					('0:06:55', u'C(16,2)C(15,2)*14')
					('0:07:13', u'16*15*14')
					('0:08:02', u'16C(6,2)15C(6,2)*14*6')
					('0:09:17', u'16C(6,2)15C(6,2)')
	part1_correct_attempt
					['0:09:39', u'C(16,2)']

13 Student ID:dando

	first_attempt
					2015-10-15 20:49:05
	part1_incorrect_attempt
					('0:00:00', u'5 * 4')
	part1_correct_attempt
					['0:03:53', u'13!/(11!2)']

14 Student ID:chc286

	first_attempt
					2015-10-11 23:36:45
	part1_incorrect_attempt
					('0:00:00', u'C(13,2)*C(6,2)*12*6')
					('0:00:12', u'C(13,2)*C(6,2)*11*6')
					('0:03:37', u'C(13,2)*(C(6,2)^2)*11*6')
	part1_correct_attempt
					['0:06:08', u'C(13,2)']

15 Student ID:sayao

	first_attempt
					2015-10-12 18:44:17
	part1_incorrect_attempt
					('0:00:00', u'13!/(11!*2!)')
	part1_correct_attempt
					['0:00:09', u'16!/(14!*2!)']

16 Student ID:anvan

	first_attempt
					2015-10-15 01:19:18
	part1_incorrect_attempt
					('0:00:00', u'5*14*13')
					('0:02:07', u'14*14*5')
					('0:00:00', u'14*5 * 13 * 5')
	part1_correct_attempt
					['1:15:11', u'14!/(2!12!) ']

17 Student ID:flhernan

	first_attempt
					2015-10-14 19:34:28
	part1_incorrect_attempt
					('0:00:00', u'2*C(4,2)*10*36')
					('0:02:52', u'C(10,2)*C(4,2)*C(4,2)*C(8,1)*C(4,1)')
					('0:09:50', u'6*C(10,2)*6*C(9,2)*C(32,1)')
					('0:13:51', u'6*C(10,1)*6*C(9,1)*C(32,1)')
					('0:15:53', u'6*C(10,1)*6*C(9,1)')
					('0:16:10', u'6*C(10,1)')
	part1_correct_attempt
					['0:18:28', u'C(10,2)']

18 Student ID:a2ahmed

	first_attempt
					2015-10-15 04:25:36
	part1_incorrect_attempt
					('0:00:00', u'C(15,2)+C(14,2)')
					('0:00:49', u'C(14,2)+C(13,2)')
					('0:01:02', u'14+13')
	part1_correct_attempt
					['15:24:16', u'C(15,2)']

19 Student ID:mitopete

	first_attempt
					2015-10-13 20:50:05
	part1_incorrect_attempt
					('0:00:00', u'11!/(4!7!)')
					('0:04:11', u'(11!/(2!9!))+(10!/(2!8!))')
					('0:05:03', u'11! + 10!')
	part1_correct_attempt
					['0:07:17', u'11!/(2!9!)']

20 Student ID:starinia

	first_attempt
					2015-10-15 02:44:15
	part1_incorrect_attempt
					('0:00:00', u'C(10,2) * C(6, 2) * C(6,2) * C(8,1) * C(6,1)')
	part1_correct_attempt
					['0:15:28', u'C(10,2)']

21 Student ID:tak068

	first_attempt
					2015-10-14 07:20:05
	part1_incorrect_attempt
					('0:00:00', u'10!6!/9!/2!/4!')
					('0:04:29', u'45*15^2')
	part1_correct_attempt
					['0:11:45', u'C(10,2)']

22 Student ID:m8woo

	first_attempt
					2015-10-10 01:15:26
	part1_incorrect_attempt
					('0:00:00', u'13*12*2*39')
	part1_correct_attempt
					['0:00:45', u'13*12/2']

23 Student ID:jhp077

	first_attempt
					2015-10-15 06:05:43
	part1_incorrect_attempt
					('0:00:00', u'15*13')
					('0:01:39', u'C(6,2) * C(72,3)')
					('0:02:10', u'13*C(6,2) * C(72,3)')
					('0:00:00', u'13*C(6,2)*C(6,2)')
					('0:01:18', u'C(13,2)*C(6,2)*C(6,2)')
					('0:02:07', u'13*12*C(6,2)*C(6,2)')
					('0:05:39', u'C(13,2)*C(6,2)*C(6,2)*66')
	part1_correct_attempt
					['0:11:03', u'C(13,2)']

24 Student ID:jit002

	first_attempt
					2015-10-15 06:05:01
	part1_incorrect_attempt
					('0:00:00', u'C(13,2)+C(13,1)')
					('0:00:00', u'C(13,2)+13')
	part1_correct_attempt
					['0:12:37', u'C(13,2)']

25 Student ID:druble

	first_attempt
					2015-10-13 01:39:36
	part1_incorrect_attempt
					('0:00:00', u'C(15,1)')
	part1_correct_attempt
					['0:02:14', u'C(16,2)']

26 Student ID:h4tu

	first_attempt
					2015-10-15 07:28:45
	part1_incorrect_attempt
					('0:00:00', u'13^4')
					('0:00:28', u'13*12')
	part1_correct_attempt
					['0:03:29', u'(16*15/2)']

27 Student ID:lrlai

	first_attempt
					2015-10-12 20:41:38
	part1_incorrect_attempt
					('0:00:00', u'15^2 * 14^2')
	part1_correct_attempt
					['0:01:29', u'C(15,2)']

28 Student ID:asetters

	first_attempt
					2015-10-12 06:22:29
	part1_incorrect_attempt
					('0:00:00', u'13*12')
					('0:08:04', u'13+12')
	part1_correct_attempt
					['0:11:07', u'(11*10)/2']

29 Student ID:jjchung

	first_attempt
					2015-10-14 20:06:23
	part1_incorrect_attempt
					('0:00:00', u'C(13,2)*5')
					('0:00:20', u'C(11,2)*5')
					('0:02:04', u'C(11,1)*2*5')
					('0:02:25', u'C(11,2)*5')
					('0:02:41', u'C(11,2)^5')
	part1_correct_attempt
					['0:03:31', u'C(11,2)']

30 Student ID:abjara

	first_attempt
					2015-10-12 21:34:29
	part1_incorrect_attempt
					('0:00:00', u'[4!/(2!*2!)]*11')
					('0:00:26', u'[4!/(2!)]*11')
					('0:14:39', u'[11!/(9!*2!)]*6^2*44')
					('0:14:59', u'[11!/(9!*2!)]*6^2*36')
	part1_correct_attempt
					['0:15:24', u'[11!/(9!*2!)]']

31 Student ID:cprafull

	first_attempt
					2015-10-14 08:28:51
	part1_incorrect_attempt
					('0:00:00', u'2(14!)/((2!)(12!))')
					('0:00:00', u'(84!)/((80!)(4!))')
					('0:01:31', u'84 * 83 * 79 * 78')
					('0:01:44', u'84 * 83 * 79 * 78/4')
					('0:01:51', u'84 * 83 * 79 * 78')
	part1_correct_attempt
					['13:44:59', u'14!/((2!)(12!))']

32 Student ID:anislam

	first_attempt
					2015-10-15 23:17:36
	part1_incorrect_attempt
					('0:00:00', u'C(11,2) * C(11,1)')
					('0:11:26', u'10*9')
					('0:11:43', u'C(10,1)*C(9,1)')
	part1_correct_attempt
					['0:22:03', u'C(11,2)']

33 Student ID:thk002

	first_attempt
					2015-10-12 03:46:27
	part1_incorrect_attempt
					('0:00:00', u'C(84,28)')
	part1_correct_attempt
					['0:20:32', u'C(14,2)']

34 Student ID:krau

	first_attempt
					2015-10-14 04:01:32
	part1_incorrect_attempt
					('0:00:00', u'(4*16!/14!/2!) * 3 * (16!/2!/14!)')
					('0:00:00', u'4*16!/14!/2! * 3 * (16!/2!/14!)')
					('0:00:00', u'4*16!/14!/2! * 3 * (16!/2!/14!) * 60')
					('0:00:00', u'16*4*3')
					('0:00:00', u'16*4*3*15*4*3')
					('0:01:20', u'64*3*62*3')
	part1_correct_attempt
					['0:06:12', u'16!/2!/14!']

35 Student ID:psable

	first_attempt
					2015-10-15 23:32:24
	part1_incorrect_attempt
					('0:00:00', u'C(10,2)*C(6,1)*C(9,2)*C(6,1)')
					('0:01:10', u'C(10,2)*C(6,1)*C(6,1)')
					('0:01:50', u'C(10,1)*C(6,1)*C(9,1)*C(6,1)')
					('0:00:00', u'C(10,1)')
	part1_correct_attempt
					['0:11:19', u'C(10,2)']

36 Student ID:r1gu

	first_attempt
					2015-10-15 12:31:43
	part1_incorrect_attempt
					('0:00:00', u'4!(2!2!)')
					('0:00:07', u'4!/(2!2!)')
					('0:00:41', u'5!/(2!3!)')
	part1_correct_attempt
					['9:55:15', u'11!/(2!9!)']

37 Student ID:dsmonaha

	first_attempt
					2015-10-13 18:18:56
	part1_incorrect_attempt
					('0:00:00', u'C(5,2)11C(4,2)10*51')
					('0:02:02', u'C(5,2)11C(5,2)10*45')
					('0:03:40', u'11C(5,2)10*45')
					('0:05:09', u'11*10*45')
					('0:05:22', u'11*10*C(5,2)*45')
					('0:07:10', u'C(5,2)C(5,2)')
					('0:07:47', u'C(11,2)C(10,2)')
	part1_correct_attempt
					['0:11:23', u'C(11,2)']

38 Student ID:ajabasa

	first_attempt
					2015-10-14 07:18:33
	part1_incorrect_attempt
					('0:00:00', u'13*12*4')
					('0:00:19', u'13*12*4!')
	part1_correct_attempt
					['0:13:27', u'C(13,2)']

39 Student ID:z3meng

	first_attempt
					2015-10-15 03:18:18
	part1_incorrect_attempt
					('0:00:00', u'15*15*14*15+15^2')
					('0:03:08', u'15^2*106')
	part1_correct_attempt
					['0:10:52', u'105']

40 Student ID:lcardoso

	first_attempt
					2015-10-13 18:00:25
	part1_incorrect_attempt
					('0:00:00', u'C(13,4)')
					('0:01:26', u'C(14,2) * C(14,2)')
	part1_correct_attempt
					['0:01:36', u'C(14,2)']

41 Student ID:jel075

	first_attempt
					2015-10-15 01:27:38
	part1_incorrect_attempt
					('0:00:00', u'12!(10!*2!)')
	part1_correct_attempt
					['0:00:09', u'12!/(10!*2!)']

42 Student ID:edescobe

	first_attempt
					2015-10-12 20:31:32
	part1_incorrect_attempt
					('0:00:00', u'11*10')
					('0:04:43', u'C(4,2)*C(4,2)')
	part1_correct_attempt
					['0:08:09', u'C(12,2)']

43 Student ID:w4shin

	first_attempt
					2015-10-14 03:18:15
	part1_incorrect_attempt
					('0:00:00', u'14!/(3!2!)')
					('0:00:00', u'14!(12!2!)')
	part1_correct_attempt
					['20:28:33', u'14!/(12!2!)']

44 Student ID:etemlock

	first_attempt
					2015-10-11 01:25:08
	part1_incorrect_attempt
					('0:00:00', u'C(6,2)^2 * C(13,1) * C(12,1) * C(74, 2)')
					('0:01:47', u'C(6,2)^2 * C(13,2)* C(11,1)* C(4,1)')
					('0:02:23', u'C(6,2)^2 * C(13,2)* C(11,2)* C(4,1)')
					('0:03:28', u'C(6,2)^2 * C(13,2)* C(11,1)* C(6,1)')
	part1_correct_attempt
					['0:04:54', u'C(13,2)']

45 Student ID:jtfrankl

	first_attempt
					2015-10-15 21:10:25
	part1_incorrect_attempt
					('0:00:00', u'2C(12,2)')
	part1_correct_attempt
					['0:00:05', u'C(12,2)']

46 Student ID:cstringh

	first_attempt
					2015-10-12 22:49:40
	part1_incorrect_attempt
					('0:00:00', u'2^15')
					('0:00:14', u'2^13')
					('0:00:00', u'C(75,4)')
	part1_correct_attempt
					['0:30:02', u'C(15, 2)']

47 Student ID:dan029

	first_attempt
					2015-10-09 22:58:34
	part1_incorrect_attempt
					('0:00:00', u'C(14,2)*C(6,2)')
					('0:00:56', u'72*C(14,2)*C(6,2)')
					('0:01:52', u'72*C(14,2)*C(6,2)^2')
					('0:02:58', u'12*C(14,2)*C(6,2)^2*6')
					('0:03:42', u'12*C(14,2)*(C(6,2)^2)*6')
	part1_correct_attempt
					['0:06:08', u'C(14,2)']

48 Student ID:aurodrig

	first_attempt
					2015-10-15 21:10:14
	part1_incorrect_attempt
					('0:00:00', u'12!/(2!9!)')
	part1_correct_attempt
					['0:00:57', u'12!/(2!10!)']

49 Student ID:yjshin

	first_attempt
					2015-10-15 11:18:28
	part1_incorrect_attempt
					('0:00:00', u'4*16-4')
	part1_correct_attempt
					['0:02:37', u'120']

50 Student ID:dcastlem

	first_attempt
					2015-10-15 04:11:36
	part1_incorrect_attempt
					('0:00:00', u'16!/((1!)*15!)')
	part1_correct_attempt
					['10:36:40', u'16!/((2!)(14!))']

51 Student ID:bkoli

	first_attempt
					2015-10-15 20:29:34
	part1_incorrect_attempt
					('0:00:00', u'13*12')
					('0:00:14', u'13!/(11!2!)')
	part1_correct_attempt
					['0:00:35', u'10!/(8!2!)']

52 Student ID:xil109

	first_attempt
					2015-10-10 20:47:23
	part1_incorrect_attempt
					('0:00:00', u'C(16,2)*C(5,2)*C(5,2)*C(14,1)*C(5,1)')
					('0:18:53', u'C(16,2)*C(5,2)*C(5,2)')
	part1_correct_attempt
					['0:19:02', u'C(16,2)']

53 Student ID:dac064

	first_attempt
					2015-10-15 21:50:12
	part1_incorrect_attempt
					('0:00:00', u'16*15*14')
					('0:00:20', u'16*16*15')
					('0:00:53', u'16*15*14')
	part1_correct_attempt
					['0:01:14', u'C(16,2)']

54 Student ID:hkhodada

	first_attempt
					2015-10-10 19:45:59
	part1_incorrect_attempt
					('0:00:00', u'4*C(14,2)')
	part1_correct_attempt
					['0:00:10', u'C(14,2)']

55 Student ID:nisharma

	first_attempt
					2015-10-13 22:19:23
	part1_incorrect_attempt
					('0:00:00', u'96*95')
					('0:00:42', u'(96!)/(2!* 95!)')
					('0:00:57', u'(96!)/(2!* 94!)')
					('2:12:12', u'(6!/(2!*4!))(2*(16!/15!))')
					('2:12:56', u'(6!/(2!*4!))*(32)')
					('2:14:52', u'(6!/(2!*4!))*(16)')
					('2:16:16', u'6!/(2!*4!)')
					('0:00:00', u'6!/(2!*4!) * 16*15')
	part1_correct_attempt
					['19:52:12', u'C(16,2)']

56 Student ID:glcohen

	first_attempt
					2015-10-13 05:55:07
	part1_incorrect_attempt
					('0:00:00', u'(13!)/(8!5!)')
	part1_correct_attempt
					['0:01:13', u'(13!)/(11!2!)']

57 Student ID:achava

	first_attempt
					2015-10-13 08:07:50
	part1_incorrect_attempt
					('0:00:00', u'C(10,1)')
	part1_correct_attempt
					['0:00:18', u'C(10,2)']

58 Student ID:d6he

	first_attempt
					2015-10-15 06:51:40
	part1_incorrect_attempt
					('0:00:00', u'13!/(4!9!)')
					('0:00:31', u'13!/(2!11!)')
					('0:00:52', u'14!/(4!10!)')
	part1_correct_attempt
					['0:03:39', u'14!/(12!2!)']

59 Student ID:sachadal

	first_attempt
					2015-10-14 18:09:35
	part1_incorrect_attempt
					('0:00:00', u'C(13,2)*C(4,2)*C(12,2)*C(4,2)*C(11,1)')
					('0:00:22', u'C(14,2)*C(4,2)*C(13,2)*C(4,2)*C(12,1)')
					('0:00:41', u'C(14,2)*C(4,2)*C(13,2)*C(4,2)')
					('0:01:12', u'C(14,2)*C(13,2)')
					('0:02:15', u'C(56,2)*C(14,1)*C(13,1)')
					('0:02:55', u'14*1*13*1')
	part1_correct_attempt
					['0:04:35', u'C(14,2)']

60 Student ID:t2li

	first_attempt
					2015-10-14 06:45:36
	part1_incorrect_attempt
					('0:00:00', u'C(14,2)C(13,2)*4^2*C(76,1)')
					('0:01:11', u'C(14,2)C(13,2)*6^2*C(76,1)')
					('0:02:15', u'14*13*6^2*6*12')
					('0:02:37', u'C(6,2)^214*13*6^2*6*12')
					('0:03:30', u'C(14,2)*6^3*12')
					('0:03:57', u'C(14,2)*6^5*12')
					('0:04:03', u'C(14,2)*6^4*12')
					('0:05:53', u'C(14,2) *12*6*C(6,2)*C(6,2)')
					('0:08:15', u'C(14,3)C(6,2)^2 * 6')
					('0:10:26', u'14*13*6*6*5*5*6*12')
					('0:10:45', u'14*13*6*6*5*5*6*126')
	part1_correct_attempt
					['0:13:33', u'C(14,2)']

61 Student ID:bakang

	first_attempt
					2015-10-15 02:14:35
	part1_incorrect_attempt
					('0:00:00', u'C(4,2)*11*44')
					('0:00:38', u'C(6,2)*11*44')
					('0:02:13', u'C(6,2)*11*11*44')
	part1_correct_attempt
					['0:13:08', u'C(11,2)']

62 Student ID:jnatale

	first_attempt
					2015-10-13 01:53:24
	part1_incorrect_attempt
					('0:00:00', u'48*3*46*3')
					('0:00:00', u'1.0*C(13,2)')
					('0:00:00', u'12*C(4,2)+11*C(4,2) + 12')
	part1_correct_attempt
					['23:57:40', u'C(12,2)']

63 Student ID:nnh002

	first_attempt
					2015-10-15 05:58:06
	part1_incorrect_attempt
					('0:00:00', u'15*C(4,2)*14*C(4,2)')
	part1_correct_attempt
					['0:14:15', u'C(15,2)']

64 Student ID:tol003

	first_attempt
					2015-10-14 00:47:22
	part1_incorrect_attempt
					('0:00:00', u'13*C(4,2)*12*C(4,2)*11')
					('0:01:51', u'14*C(4,2)*13*C(4,2)*12')
	part1_correct_attempt
					['0:04:26', u'C(14,2)']

65 Student ID:hachrist

	first_attempt
					2015-10-15 01:51:50
	part1_incorrect_attempt
					('0:00:00', u'30*13')
					('0:00:00', u'11!/(10!*1!)')
	part1_correct_attempt
					['0:45:26', u'13!/(11!*2!)']

66 Student ID:kmc012

	first_attempt
					2015-10-15 02:31:28
	part1_incorrect_attempt
					('0:00:00', u'12*11*10')
	part1_correct_attempt
					['0:01:40', u'(12!)/((2!)*(10!))']

67 Student ID:lahawkin

	first_attempt
					2015-10-14 05:23:43
	part1_incorrect_attempt
					('0:00:00', u'12!/(8!*4!)')
	part1_correct_attempt
					['0:00:11', u'12!/(10!*2!)']

68 Student ID:lguintu

	first_attempt
					2015-10-09 22:00:16
	part1_incorrect_attempt
					('0:00:00', u'C(5,2)*C(16,1)')
					('0:00:06', u'2*C(5,2)*C(16,1)')
					('0:02:29', u'5*16')
					('0:03:14', u'C(16,1)')
					('0:03:35', u'C(80,1)')
					('0:06:43', u'C(76,1)')
	part1_correct_attempt
					['0:07:30', u'C(16,2)']

69 Student ID:csl030

	first_attempt
					2015-10-14 02:08:45
	part1_incorrect_attempt
					('0:00:00', u'C(13, 1) * C(12,1) * C(11, 1)')
					('0:00:18', u'C(13, 1) + C(12,1) + C(11, 1)')
					('0:06:18', u'C(13,2) * C(6,2) * C(6,2) * C(11,1) * C(6,1)')
	part1_correct_attempt
					['0:08:00', u'C(13,2)']

70 Student ID:volim

	first_attempt
					2015-10-12 22:47:56
	part1_incorrect_attempt
					('0:00:00', u'C(11,1)')
	part1_correct_attempt
					['0:01:07', u'C(11,2)']

71 Student ID:atorr

	first_attempt
					2015-10-11 02:58:38
	part1_incorrect_attempt
					('0:00:00', u'(12 ^ 2) * (11^2)')
					('0:08:55', u'24 * 23')
	part1_correct_attempt
					['0:12:29', u'C(12,2)']

72 Student ID:cagatep

	first_attempt
					2015-10-14 05:04:34
	part1_incorrect_attempt
					('0:00:00', u'C(12,2) * C(36, 3) * 4')
					('0:00:44', u'C(12,2) * C(12, 2)')
					('0:01:08', u'C(12,2) * C(12, 2) * 4')
					('0:02:08', u'C(12,1) * C(12,1) * 4')
					('0:02:45', u'C(12,1) * C(11,1)*4')
	part1_correct_attempt
					['0:08:07', u'C(12, 2)']

73 Student ID:ytc012

	first_attempt
					2015-10-15 09:03:27
	part1_incorrect_attempt
					('0:00:00', u'15*6*15*5')
					('0:00:05', u'15*6+15*5')
					('0:01:31', u'6!15!(2!4!2!13!)')
					('0:01:37', u'6!15!/(2!4!2!13!)')
					('0:13:54', u'15*5!/(2!3!)*15*5!/(2!3!)')
	part1_correct_attempt
					['0:21:23', u'15!/(2!13!)']

74 Student ID:klala

	first_attempt
					2015-10-12 04:39:56
	part1_incorrect_attempt
					('0:00:00', u'C(13,1)')
	part1_correct_attempt
					['0:01:24', u'C(13,2)']

75 Student ID:ppanourg

	first_attempt
					2015-10-15 07:46:11
	part1_incorrect_attempt
					('0:00:00', u'4(C(10,2)*C(3,1)*C(10,2))')
					('0:05:05', u'C(4,1)C(10,1)C(3,1)C(2,1)C(10,1)')
					('0:05:37', u'[C(4,1)C(10,1)C(3,1)C(2,1)C(10,1)]*4')
					('0:00:00', u'10+9+8+7+6+5+4+3+2+1')
					('0:00:00', u'40*36')
					('0:02:00', u'C(10,1)*C(4,2) + C(9,1)*C(4,2)')
					('0:02:45', u'C(10,1)*C(4,2)*C(9,1)*C(4,2)')
					('0:00:00', u'3^2(9+8+7+6+5+4+3+2+1)')
	part1_correct_attempt
					['12:02:32', u'C(10,2)']

76 Student ID:ewbrenna

	first_attempt
					2015-10-12 20:26:08
	part1_incorrect_attempt
					('0:00:00', u'6*5')
					('0:00:59', u'13*12*13*12')
					('0:01:14', u'6*5')
	part1_correct_attempt
					['0:01:53', u'78']

77 Student ID:masaro

	first_attempt
					2015-10-10 09:46:33
	part1_incorrect_attempt
					('0:00:00', u'15*6*10+14*6*10')
	part1_correct_attempt
					['0:04:53', u'105']

78 Student ID:pcdo

	first_attempt
					2015-10-13 20:19:21
	part1_incorrect_attempt
					('0:00:00', u'C(16,2)C(5,2)C(5,2)5*14')
	part1_correct_attempt
					['0:01:39', u'C(16,2)']

79 Student ID:vsosnovs

	first_attempt
					2015-10-15 04:30:34
	part1_incorrect_attempt
					('0:00:00', u'C((6*14),5)')
	part1_correct_attempt
					['0:00:42', u'C(14,2)']

80 Student ID:amquinte

	first_attempt
					2015-10-14 18:17:10
	part1_incorrect_attempt
					('0:00:00', u'C(72,4)')
	part1_correct_attempt
					['0:01:54', u'C(12,2)']

81 Student ID:gsrandha

	first_attempt
					2015-10-13 06:29:41
	part1_incorrect_attempt
					('0:00:00', u'100*100')

82 Student ID:jhc010

	first_attempt
					2015-10-15 16:12:58
	part1_incorrect_attempt
					('0:00:00', u'13*13')
					('0:01:00', u'100-10')
	part1_correct_attempt
					['0:02:01', u'C(10,2)']

83 Student ID:anl114

	first_attempt
					2015-10-15 08:23:20
	part1_incorrect_attempt
					('0:00:00', u'6^4')
					('0:00:13', u'4^6')
					('0:01:36', u'36*35')
					('0:05:54', u'12*15*11*15')
	part1_correct_attempt
					['0:07:20', u'66']

84 Student ID:twsalim

	first_attempt
					2015-10-11 23:14:15
	part1_incorrect_attempt
					('0:00:00', u'15!/(3!12!)')
	part1_correct_attempt
					['0:56:26', u'105']

85 Student ID:s6deng

	first_attempt
					2015-10-14 03:53:55
	part1_incorrect_attempt
					('0:00:00', u'11!/7!')
	part1_correct_attempt
					['0:02:11', u'C(11,2)']

86 Student ID:kalang

	first_attempt
					2015-10-14 23:19:39
	part1_incorrect_attempt
					('0:00:00', u'C(16,2)*C(5,2)^2*C(14,1)*5')
	part1_correct_attempt
					['23:55:22', u'C(16,2)']

87 Student ID:jcl084

	first_attempt
					2015-10-13 20:42:58
	part1_incorrect_attempt
					('0:00:00', u'C(10,2)*C(10,2)')
					('0:00:07', u'C(10,2)+C(10,2)')
	part1_correct_attempt
					['0:02:49', u'C(10,2)']

88 Student ID:sippolit

	first_attempt
					2015-10-12 05:06:11
	part1_incorrect_attempt
					('0:00:00', u'105*100*13*5')
					('0:00:27', u'105*10*13*5')
	part1_correct_attempt
					['0:01:01', u'105']

89 Student ID:mcatozzi

	first_attempt
					2015-10-14 00:44:58
	part1_incorrect_attempt
					('0:00:00', u'C(55,2)*C(4,2)*C(53,2)*C(4,2)*C(51,1)')
					('0:00:23', u'C(55,2)*C(5,2)*C(53,2)*C(5,2)*C(51,1)')
					('0:00:00', u'C(11,2)*C(4,2)*C(51,1)')
					('0:00:29', u'C(11,2)*C(5,2)*C(51,1)')
					('0:00:50', u'C(11,2)*C(5,2)*C(51,1)*C(4,1)')
	part1_correct_attempt
					['0:02:44', u'C(11,2)']

90 Student ID:hmshah

	first_attempt
					2015-10-14 03:02:14
	part1_incorrect_attempt
					('0:00:00', u'C(39,1)')
					('0:00:14', u'C(50,1)')
					('0:00:32', u'C(13,1)')
					('0:03:57', u'C(11,1)')
					('0:04:29', u'C(13,2)*C(12,2)')
	part1_correct_attempt
					['0:05:45', u'C(13,2)']

91 Student ID:daw023

	first_attempt
					2015-10-15 03:27:49
	part1_incorrect_attempt
					('0:00:00', u'C(15,2)^2*C(6,2)*C(15,1)*C(4,1)')
					('0:00:00', u'C(15,2)*C(6,2)^2*C(13,1)*C(6,1)')
	part1_correct_attempt
					['2:47:42', u'C(15,2)']

92 Student ID:r2fisher

	first_attempt
					2015-10-14 23:20:25
	part1_incorrect_attempt
					('0:00:00', u'2^10')
	part1_correct_attempt
					['0:03:22', u'10!/(8!*2!)']

93 Student ID:vasharma

	first_attempt
					2015-10-10 07:50:21
	part1_incorrect_attempt
					('0:00:00', u'6*11')
					('0:00:20', u'C(11,1)')
	part1_correct_attempt
					['0:00:36', u'C(11,2)']

94 Student ID:xweng

	first_attempt
					2015-10-12 23:14:14
	part1_incorrect_attempt
					('0:00:00', u'64*63*18*14*4')
					('0:00:00', u'C(16,2)C(4,2)C(4,2)C(14,1)C(4,1)')
					('0:00:35', u'C(16,2)C(4,2)C(4,2)')
					('0:00:00', u'C(16,1)C(4,2)C(15,1)C(4,2)56')
					('0:00:52', u'C(16,2)C(4,2)C(4,2)')
	part1_correct_attempt
					['3:01:17', u'C(16,2)']

95 Student ID:c3chung

	first_attempt
					2015-10-15 23:00:44
	part1_incorrect_attempt
					('0:00:00', u'5^5')
					('0:00:32', u'C(75,5)')
					('0:01:38', u'C(15,2)C(5,2)C(5,2)C(71,1)')
					('0:08:54', u'C(5,2)C(15,1)C(5,2)C(14,1)C(5,1)C(13,1)')
					('0:12:31', u'C(15,2)C(5,2)71')
					('0:13:17', u'C(15,2)C(5,2)(75-10)')
					('0:13:57', u'C(15,2)C(5,2)C(5,2)(75-10)')
					('0:15:37', u'C(15,1)C(14,1)C(5,2)C(5,2)(75-10)')

96 Student ID:mtrafeca

	first_attempt
					2015-10-11 07:35:01
	part1_incorrect_attempt
					('0:00:00', u'36*11')
					('0:00:00', u'11*12')
					('0:00:08', u'11*10')
					('0:00:40', u'4*13')
	part1_correct_attempt
					['14:03:38', u'13!/(11!*2!)']

97 Student ID:kgrozav

	first_attempt
					2015-10-15 19:22:22
	part1_incorrect_attempt
					('0:00:00', u'C(6,2)*C(16,2)*C(16,14)*C(6,4)')
	part1_correct_attempt
					['0:00:29', u'C(16,2)']

98 Student ID:j2phung

	first_attempt
					2015-10-14 07:41:08
	part1_incorrect_attempt
					('0:00:00', u'4(13!/(2!11!))')
					('0:00:16', u'4(13!/(2!11!))(13!/(2!11!))')
	part1_correct_attempt
					['0:00:58', u'13!/(2!11!)']












## Part 2

### (234) Mistake Group Digits of size 234




### (6) Mistake Group Fraction of size 6




### (3) Mistake Group Wrong_Sign of size 3




### (83) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:druble

	first_attempt
					2015-10-13 01:41:50
	part2_incorrect_attempt
					('-1 day, 23:56:31', u'C(13,1)')
	part2_correct_attempt
					['-1 day, 23:57:46', u'C(14,1)']

1 Student ID:yypan

	first_attempt
					2015-10-12 20:58:54
	part2_incorrect_attempt
					('0:00:19', u'C(12,1)')
	part2_correct_attempt
					['0:00:44', u'10']

2 Student ID:lcardoso

	first_attempt
					2015-10-13 18:02:01
	part2_incorrect_attempt
					('-1 day, 23:58:24', u'C(13,1)')
					('-1 day, 23:58:54', u'C(14,1)')
	part2_correct_attempt
					['2:51:43', u'C(14-2,1)']

3 Student ID:abjara

	first_attempt
					2015-10-12 21:49:53
	part2_incorrect_attempt
					('-1 day, 23:44:36', u'[4!/(1!*3!)]*11')
					('-1 day, 23:48:23', u'[44!/(1!*3!)]*11')
					('0:00:27', u'[11!/(10!)]')
	part2_correct_attempt
					['2 days, 0:52:54', u'9']

4 Student ID:lpettit

	first_attempt
					2015-10-14 20:25:59
	part2_incorrect_attempt
					('0:00:29', u'16*4')
					('0:02:29', u'16*3')
					('0:02:37', u'16*2')
					('0:02:58', u'16*5')
	part2_correct_attempt
					['0:06:50', u'14']

5 Student ID:jfalcone

	first_attempt
					2015-10-14 23:13:51
	part2_incorrect_attempt
					('0:03:50', u'14!/13!')
	part2_correct_attempt
					['0:11:55', u'12']

6 Student ID:v4zhang

	first_attempt
					2015-10-15 07:34:12
	part2_incorrect_attempt
					('-1 day, 23:58:30', u'C(15, 1)')
	part2_correct_attempt
					['0:01:34', u'C(13, 1)']

7 Student ID:lywong

	first_attempt
					2015-10-13 08:31:48
	part2_incorrect_attempt
					('-1 day, 16:18:50', u'6^4')
	part2_correct_attempt
					['-1 day, 16:30:43', u'20']

8 Student ID:hkhodada

	first_attempt
					2015-10-10 19:46:09
	part2_incorrect_attempt
					('-1 day, 23:59:50', u'4*C(4,1)')
					('0:00:00', u'C(4,1)')
					('0:00:21', u'C(14,1)')
					('0:11:29', u'C(56,1)')
					('0:15:51', u'C(14,13)')
					('0:20:08', u'P(14,1)')
					('0:26:09', u'C(14,1)')
					('0:39:10', u'C(56,1)')
					('3:44:33', u'4*C(14,1)')
					('3:56:35', u'C(14,4)')
					('3:59:17', u'C(4,1)')
					('10:40:31', u'C(14,1)')
	part2_correct_attempt
					['1 day, 4:25:46', u'12']

9 Student ID:lrlai

	first_attempt
					2015-10-12 20:43:07
	part2_incorrect_attempt
					('0:00:09', u'C(15,1)')
	part2_correct_attempt
					['0:00:18', u'13']

10 Student ID:srl006

	first_attempt
					2015-10-10 05:56:55
	part2_incorrect_attempt
					('0:00:25', u'11!')
					('0:00:31', u'10!')
	part2_correct_attempt
					['3 days, 9:44:00', u'9']

11 Student ID:jguanzho

	first_attempt
					2015-10-09 20:24:36
	part2_incorrect_attempt
					('0:00:00', u'10!/9!')
	part2_correct_attempt
					['0:35:52', u'12']

12 Student ID:alakamsa

	first_attempt
					2015-10-10 20:47:32
	part2_incorrect_attempt
					('0:03:18', u'11*2')
	part2_correct_attempt
					['0:23:55', u'9']

13 Student ID:ewbrenna

	first_attempt
					2015-10-12 20:28:01
	part2_incorrect_attempt
					('0:03:18', u'13*6')
	part2_correct_attempt
					['0:04:45', u'11']

14 Student ID:d6he

	first_attempt
					2015-10-15 06:55:19
	part2_incorrect_attempt
					('0:00:38', u'14!/(13!1!)')
	part2_correct_attempt
					['0:02:19', u'12']

15 Student ID:abasu

	first_attempt
					2015-10-11 02:36:01
	part2_incorrect_attempt
					('0:00:07', u'C(15,1)')
	part2_correct_attempt
					['0:01:47', u'C(13,1)']

16 Student ID:thk002

	first_attempt
					2015-10-12 04:06:59
	part2_incorrect_attempt
					('0:00:17', u'C(14,1)')
	part2_correct_attempt
					['0:00:56', u'12']

17 Student ID:akhmelni

	first_attempt
					2015-10-15 23:01:17
	part2_incorrect_attempt
					('0:00:31', u'C(12,1)')
					('0:10:25', u'C(10,2)')
	part2_correct_attempt
					['0:11:05', u'10']

18 Student ID:ctgraves

	first_attempt
					2015-10-14 00:06:31
	part2_incorrect_attempt
					('0:03:04', u'11!/(2!*9!) -2')
	part2_correct_attempt
					['1 day, 3:58:36', u'9']

19 Student ID:k5law

	first_attempt
					2015-10-12 02:50:09
	part2_incorrect_attempt
					('0:53:57', u'5*11')
					('3:45:12', u'[11!/(7!4!)]-55')
					('3:46:01', u'[11!/(8!3!)]-55')
					('1 day, 1:46:30', u'11!/(10!1!)')
					('1 day, 1:50:24', u'9*5')
					('1 day, 1:54:43', u'[9!/(8!1!)]*5')
					('1 day, 1:56:35', u'4*9')
					('1 day, 1:56:44', u'3*9')
					('1 day, 1:59:26', u'55-(3*9)')
					('1 day, 1:59:33', u'55-45')
	part2_correct_attempt
					['1 day, 2:18:34', u'9']

20 Student ID:t2shin

	first_attempt
					2015-10-15 06:11:43
	part2_incorrect_attempt
					('0:00:30', u'11!(1!10!)')
					('0:00:40', u'11!/(1!10!)')
					('0:01:31', u'55!/(1!54!)')
	part2_correct_attempt
					['0:09:13', u'9']

21 Student ID:jag028

	first_attempt
					2015-10-15 17:38:33
	part2_incorrect_attempt
					('0:00:20', u'C(13,1)')
					('0:05:53', u'C(13,1)')
	part2_correct_attempt
					['0:06:21', u'C(11,1)']

22 Student ID:dkostins

	first_attempt
					2015-10-15 18:34:04
	part2_incorrect_attempt
					('0:00:14', u'C(9,1)')
	part2_correct_attempt
					['0:02:28', u'8']

23 Student ID:s2chaudh

	first_attempt
					2015-10-13 05:01:41
	part2_incorrect_attempt
					('0:00:00', u'C(14,1)')
					('0:07:28', u'C(14,2)')
					('0:07:45', u'C(13,1)')
					('0:08:03', u'C(14,3)')
					('0:12:56', u'C(14,1)')
					('14:33:32', u'P(14,1)')
	part2_correct_attempt
					['14:46:03', u'P(12,1)']

24 Student ID:haw081

	first_attempt
					2015-10-11 00:21:36
	part2_incorrect_attempt
					('0:02:14', u'C(15,1)')
					('0:15:18', u'C(13,2)')
					('0:15:29', u'C(15,13)')
					('0:16:27', u'C(13,1)+4')
	part2_correct_attempt
					['2 days, 0:30:27', u'C(13,1)']

25 Student ID:rbdoming

	first_attempt
					2015-10-14 19:23:14
	part2_incorrect_attempt
					('0:00:33', u'C(15,1)')
					('0:01:34', u'C(14,1)')
	part2_correct_attempt
					['0:20:04', u'C(13,1)']

26 Student ID:vqt004

	first_attempt
					2015-10-14 05:47:39
	part2_incorrect_attempt
					('-1 day, 23:49:47', u'C(11,2)')
	part2_correct_attempt
					['0:00:00', u'C(9,1)']

27 Student ID:ffhaddad

	first_attempt
					2015-10-10 21:17:33
	part2_incorrect_attempt
					('0:00:19', u'C(14,2)')
	part2_correct_attempt
					['0:00:25', u'C(14,1)']

28 Student ID:kquong

	first_attempt
					2015-10-11 05:14:30
	part2_incorrect_attempt
					('0:01:21', u'5!/(2!(5-2)!)')
					('0:01:48', u'5!/(2!*(5-2)!)')
					('0:02:15', u'(5!/(2!*(5-2)!))^2')
	part2_correct_attempt
					['0:03:29', u'12']

29 Student ID:anl114

	first_attempt
					2015-10-15 08:30:40
	part2_incorrect_attempt
					('-1 day, 23:58:34', u'10*6')
	part2_correct_attempt
					['-1 day, 23:58:57', u'10']

30 Student ID:jnatale

	first_attempt
					2015-10-14 01:51:04
	part2_incorrect_attempt
					('-1 day, 0:03:39', u'48*3')
					('-1 day, 0:20:02', u'4*12')
					('-1 day, 15:31:04', u'4*12*3')
					('0:01:57', u'C(12,1)')
					('0:09:08', u'C(11,1)')
	part2_correct_attempt
					['0:12:04', u'C(10,1)']

31 Student ID:rlhagen

	first_attempt
					2015-10-11 18:43:20
	part2_incorrect_attempt
					('0:00:22', u'12!/(1!(12-1)!)')
	part2_correct_attempt
					['0:03:57', u'10']

32 Student ID:amquinte

	first_attempt
					2015-10-14 18:19:04
	part2_incorrect_attempt
					('-1 day, 23:55:25', u'C(60,1)')
	part2_correct_attempt
					['0:00:00', u'10']

33 Student ID:jmmcalex

	first_attempt
					2015-10-15 08:58:44
	part2_incorrect_attempt
					('0:11:56', u'13*12')
					('0:12:03', u'13*16')
					('0:12:08', u'13*6')
					('0:13:53', u'13^2')
	part2_correct_attempt
					['0:17:05', u'11']

34 Student ID:nnh002

	first_attempt
					2015-10-15 06:12:21
	part2_incorrect_attempt
					('-1 day, 23:40:11', u'15*2+14*2')
	part2_correct_attempt
					['0:00:00', u'13']

35 Student ID:t2li

	first_attempt
					2015-10-14 06:59:09
	part2_incorrect_attempt
					('-1 day, 23:56:57', u'14*13*6*6*5*5*6*12')
					('0:00:40', u'C(6,2)')
					('0:00:44', u'C(6,1)')
	part2_correct_attempt
					['0:00:55', u'12']

36 Student ID:twsalim

	first_attempt
					2015-10-12 00:10:41
	part2_incorrect_attempt
					('-1 day, 23:03:34', u'15!/(4!11!)')
	part2_correct_attempt
					['0:05:34', u'13']

37 Student ID:lalacson

	first_attempt
					2015-10-11 22:49:16
	part2_incorrect_attempt
					('0:00:00', u'C(13,1)')
	part2_correct_attempt
					['0:00:12', u'C(11,1)']

38 Student ID:hmnaing

	first_attempt
					2015-10-13 00:47:32
	part2_incorrect_attempt
					('0:00:00', u'C(42, 1)')
					('0:01:45', u'C((5*14)-4, 1)')
					('1 day, 5:59:03', u'C((5*14)-8, 1)')
					('1 day, 5:59:26', u'C((5*14)-10, 1)')
	part2_correct_attempt
					['1 day, 23:50:24', u'C(14-2, 1)']

39 Student ID:jap009

	first_attempt
					2015-10-15 22:18:52
	part2_incorrect_attempt
					('0:00:39', u'13!/(8!)')
	part2_correct_attempt
					['0:04:13', u'11']

40 Student ID:dis003

	first_attempt
					2015-10-15 11:43:15
	part2_incorrect_attempt
					('0:00:19', u'C(12,1)')
					('0:00:45', u'C(121,1)')
					('0:00:49', u'C(11,1)')
					('0:01:13', u'C(12,1)')
					('0:04:47', u'C(4,2)')
	part2_correct_attempt
					['0:05:52', u'C(12-2,1)']

41 Student ID:tol003

	first_attempt
					2015-10-14 00:51:48
	part2_incorrect_attempt
					('0:00:36', u'C(14,1)')
					('0:01:16', u'C(4,2)')
					('0:01:52', u'C(13,1)')
	part2_correct_attempt
					['0:02:06', u'C(12,1)']

42 Student ID:jcl084

	first_attempt
					2015-10-13 20:45:47
	part2_incorrect_attempt
					('0:00:10', u'C(10,1)')
	part2_correct_attempt
					['0:00:47', u'8']

43 Student ID:vsosnovs

	first_attempt
					2015-10-15 04:31:16
	part2_incorrect_attempt
					('0:00:00', u'C(14,2)*13')
					('0:00:15', u'C(14,1)*13')
					('0:02:17', u'C(14,2)*13')
					('0:04:19', u'C(14,1)*13')
					('0:04:28', u'C(14,1)')
					('0:21:17', u'C(14,2)*12')
					('0:22:29', u'C(14,1)*12')
					('0:22:42', u'C(14,2)*13')
					('1:21:05', u'C(14,2)*11')
					('1:21:15', u'C(14,2)*10')
					('1:21:31', u'C(14,1)*12')
					('1:21:38', u'C(14,1)*13')
					('1:23:18', u'C(14,2)*11')
					('1:23:53', u'C(14,2)C(13,1)')
					('1:25:12', u'C(14,2)C(13,1)C(13,1)')
					('1:28:35', u'C(14,2)C(6,1)C(6,1)')
					('1:35:43', u'C(14,2)C(14,1)C(14,1)C(14,1)')
					('1:37:43', u'C(14,2)*12')
					('1:40:39', u'C(14,2)*C(5,1)*C(14,1)')
					('1:45:55', u'C(14,2)*C(12,1)*C(14,1)')
					('1:46:06', u'C(14,2)*C(12,1)')
					('1:47:45', u'91*12')
					('1:56:48', u'C(13,1)')
					('1:57:07', u'C(13,1)C(6,1)')
	part2_correct_attempt
					['1:57:30', u'C(12,1)']

44 Student ID:volim

	first_attempt
					2015-10-12 22:49:03
	part2_incorrect_attempt
					('-1 day, 23:58:53', u'C(10,1)')
					('0:00:00', u'C(10,1)')
	part2_correct_attempt
					['0:00:47', u'C(9,1)']

45 Student ID:ssamudra

	first_attempt
					2015-10-15 18:28:43
	part2_incorrect_attempt
					('0:00:32', u'13!/(12!1!)')
					('0:00:44', u'12!/(11!1!)')
	part2_correct_attempt
					['0:01:09', u'11!/(10!1!)']

46 Student ID:jhw015

	first_attempt
					2015-10-15 02:51:21
	part2_incorrect_attempt
					('0:00:10', u'C(12,1)')
	part2_correct_attempt
					['0:07:08', u'10']

47 Student ID:tcn013

	first_attempt
					2015-10-15 04:00:44
	part2_incorrect_attempt
					('0:00:06', u'C(16,1)')
	part2_correct_attempt
					['0:00:19', u'14']

48 Student ID:jtfrankl

	first_attempt
					2015-10-15 21:10:30
	part2_incorrect_attempt
					('0:01:08', u'C(12,1)')
	part2_correct_attempt
					['0:02:04', u'10']

49 Student ID:hah008

	first_attempt
					2015-10-15 07:31:49
	part2_incorrect_attempt
					('0:01:33', u'C(10, 1)')
	part2_correct_attempt
					['1:35:41', u'8']

50 Student ID:djk006

	first_attempt
					2015-10-11 02:52:07
	part2_incorrect_attempt
					('0:00:34', u'14*13/2')
	part2_correct_attempt
					['0:09:41', u'12']

51 Student ID:klala

	first_attempt
					2015-10-12 04:41:20
	part2_incorrect_attempt
					('-1 day, 23:56:20', u'C(6,1)')
	part2_correct_attempt
					['0:00:16', u'C(11,1)']

52 Student ID:aysee

	first_attempt
					2015-10-13 21:27:01
	part2_incorrect_attempt
					('0:00:00', u'C(13,1)')
	part2_correct_attempt
					['0:44:48', u'C(11,1)']

53 Student ID:mcatozzi

	first_attempt
					2015-10-14 00:47:42
	part2_incorrect_attempt
					('0:00:18', u'C(5,1)')
					('0:01:06', u'C(10,1)')
					('0:01:17', u'C(11,1)')
	part2_correct_attempt
					['0:01:27', u'C(9,1)']

54 Student ID:zig006

	first_attempt
					2015-10-12 23:28:50
	part2_incorrect_attempt
					('0:00:35', u'14!/(3!11!)')
	part2_correct_attempt
					['0:01:08', u'14']

55 Student ID:w4shin

	first_attempt
					2015-10-14 23:46:48
	part2_incorrect_attempt
					('-1 day, 3:31:27', u'12!(11!1!)')
	part2_correct_attempt
					['-1 day, 23:57:19', u'12']

56 Student ID:achava

	first_attempt
					2015-10-13 08:08:08
	part2_incorrect_attempt
					('0:05:12', u'C(10,1)')
					('0:07:48', u'C(9,1)')
	part2_correct_attempt
					['0:07:57', u'C(8,1)']

57 Student ID:m4bui

	first_attempt
					2015-10-15 22:33:01
	part2_incorrect_attempt
					('0:00:00', u'C(11,1)')
					('0:01:19', u'C(6,1)')
	part2_correct_attempt
					['0:50:43', u'9']

58 Student ID:jjchung

	first_attempt
					2015-10-14 20:09:54
	part2_incorrect_attempt
					('-1 day, 23:56:49', u'C(13,2)*5')
					('-1 day, 23:57:50', u'C(11,2)*2')
					('-1 day, 23:58:33', u'C(11,2)*2*5')
					('0:00:11', u'C(11,1)')
					('0:04:21', u'C(11,2)*51')
	part2_correct_attempt
					['0:18:35', u'9']

59 Student ID:dtea

	first_attempt
					2015-10-15 23:38:24
	part2_incorrect_attempt
					('0:02:23', u'C(14,1)')
					('0:03:15', u'C(14,5)')

60 Student ID:btn023

	first_attempt
					2015-10-13 07:39:51
	part2_incorrect_attempt
					('0:00:00', u'C(16,1)')
	part2_correct_attempt
					['0:01:49', u'C(14,1)']

61 Student ID:flhernan

	first_attempt
					2015-10-14 19:52:56
	part2_incorrect_attempt
					('-1 day, 23:51:08', u'6*C(10,2)*6*C(9,2)*C(32,1)')
					('0:00:41', u'C(8,2)')
	part2_correct_attempt
					['0:00:53', u'C(8,1)']

62 Student ID:azkong

	first_attempt
					2015-10-15 16:20:36
	part2_incorrect_attempt
					('0:00:00', u'C(15, 1)')
					('0:00:19', u'C(14, 1)')
					('0:05:55', u'C(15, 1)')
	part2_correct_attempt
					['1:23:23', u'C(13, 1)']

63 Student ID:tak068

	first_attempt
					2015-10-14 07:31:50
	part2_incorrect_attempt
					('-1 day, 23:52:39', u'45*15^2')
					('0:00:29', u'C(10,1)')
	part2_correct_attempt
					['0:01:46', u'C(8,1)']

64 Student ID:jic212

	first_attempt
					2015-10-12 08:41:41
	part2_incorrect_attempt
					('0:00:10', u'C(15,1)')
	part2_correct_attempt
					['0:00:52', u'13']

65 Student ID:vasharma

	first_attempt
					2015-10-10 07:50:57
	part2_incorrect_attempt
					('0:00:20', u'C(11,1)')
					('0:00:55', u'11*6')
					('0:01:26', u'C(11,6)')
					('0:01:32', u'C(6,2)')
					('0:04:18', u'C(11,1)')
					('0:05:06', u'11!')
	part2_correct_attempt
					['18:33:26', u'C(9,1)']

66 Student ID:hpc001

	first_attempt
					2015-10-14 22:18:56
	part2_incorrect_attempt
					('0:00:22', u'C(14,1)')
					('0:01:41', u'14*5')
					('0:06:22', u'C(14,1) * 2')
					('0:09:53', u'C(14,3)')
	part2_correct_attempt
					['0:10:08', u'12']

67 Student ID:bkoli

	first_attempt
					2015-10-15 20:30:09
	part2_incorrect_attempt
					('0:00:24', u'10!/(9!1!)')
	part2_correct_attempt
					['0:18:03', u'8']

68 Student ID:hsc052

	first_attempt
					2015-10-15 05:45:08
	part2_incorrect_attempt
					('0:00:00', u'C(10,1)')
					('0:00:52', u'C(9,1)')
	part2_correct_attempt
					['0:03:59', u'C(8,1)']

69 Student ID:c3chung

	first_attempt
					2015-10-15 23:00:44
	part2_incorrect_attempt
					('0:00:00', u'5^5')
					('0:00:00', u'C(75,5)')
					('0:00:00', u'C(5,2)15*70*65*60')

70 Student ID:qtluong

	first_attempt
					2015-10-12 20:28:39
	part2_incorrect_attempt
					('0:00:15', u'8!/(1!(7-1!))')
					('0:00:22', u'8!/(1!(8-1!))')
					('0:00:49', u'8!/(1!(8-1!))')
	part2_correct_attempt
					['0:00:57', u'8!/(1!(8-1)!)']

71 Student ID:dac064

	first_attempt
					2015-10-15 21:51:26
	part2_incorrect_attempt
					('-1 day, 23:49:00', u'C(16,1)')
	part2_correct_attempt
					['-1 day, 23:56:05', u'14']

72 Student ID:jhp077

	first_attempt
					2015-10-15 06:16:46
	part2_incorrect_attempt
					('0:02:53', u'13*12*11*10')
					('0:03:03', u'C(13,4)')
					('0:03:14', u'C(13,5)')
					('0:05:46', u'C(13,1)*C(12,3)')
					('0:06:00', u'C(13,1)*C(12,4)')
					('0:07:41', u'C(13,5)')
					('0:08:21', u'13*12*11*10')
					('0:08:31', u'13*12*11*10*9')
					('0:10:25', u'C(13,5)')
					('0:11:47', u'13*12^4')
					('0:13:13', u'13*13*C(12,3)')
	part2_correct_attempt
					['0:15:13', u'11']

73 Student ID:glcohen

	first_attempt
					2015-10-13 05:56:20
	part2_incorrect_attempt
					('0:00:00', u'5*13')
					('0:00:18', u'(13!)/(12!)')
					('0:01:11', u'(12!)/(11!)')
	part2_correct_attempt
					['0:01:43', u'11']

74 Student ID:aurodrig

	first_attempt
					2015-10-15 21:11:11
	part2_incorrect_attempt
					('0:01:21', u'12!/(1!11!)')
	part2_correct_attempt
					['0:02:15', u'10!/(1!9!)']

75 Student ID:cagatep

	first_attempt
					2015-10-14 05:12:41
	part2_incorrect_attempt
					('-1 day, 23:51:53', u'C(12, 1) * C(11, 1) * C(10, 1) * C(9, 1) * C(8,1) * 4')
					('-1 day, 23:52:37', u'C(12, 1)')
	part2_correct_attempt
					['0:00:15', u'C(10,1)']

76 Student ID:ytc012

	first_attempt
					2015-10-15 09:24:50
	part2_incorrect_attempt
					('0:00:47', u'15!/(13!2!)')
	part2_correct_attempt
					['0:01:02', u'13']

77 Student ID:ggaddi

	first_attempt
					2015-10-13 18:33:28
	part2_incorrect_attempt
					('0:01:19', u'10!/(1!*9!)')
	part2_correct_attempt
					['0:04:46', u'8']

78 Student ID:j2phung

	first_attempt
					2015-10-14 07:42:06
	part2_incorrect_attempt
					('0:01:11', u'13!/(12!1!)')
					('0:01:58', u'2(13!/(12!1!))')
					('0:05:53', u'(13!/(12!1!))')
					('0:07:13', u'(12!/(11!1!))')
	part2_correct_attempt
					['0:08:11', u'(11!/(10!1!))']

79 Student ID:mjethani

	first_attempt
					2015-10-15 01:50:07
	part2_incorrect_attempt
					('0:00:23', u'13!/((1!)(12!))')
					('0:02:13', u'12!/((1!)(11!))')
	part2_correct_attempt
					['0:03:02', u'11!/((1!)(10!))']

80 Student ID:kgrozav

	first_attempt
					2015-10-15 19:22:51
	part2_incorrect_attempt
					('0:01:54', u'C(16,1)')
					('0:06:36', u'C(16,3)')
	part2_correct_attempt
					['0:09:04', u'14']

81 Student ID:msaguiar

	first_attempt
					2015-10-14 02:26:42
	part2_incorrect_attempt
					('-2 days, 1:45:11', u'12*2')
	part2_correct_attempt
					['0:00:00', u'10']

82 Student ID:jit002

	first_attempt
					2015-10-15 06:17:38
	part2_incorrect_attempt
					('-1 day, 23:47:23', u'13*6')
	part2_correct_attempt
					['0:00:00', u'11']












## Part 3

### (732) Mistake Group Digits of size 732




### (114) Mistake Group ['R.0.0'] of size 114
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|[C(5,2)]^2	|5!/(3!*2!)	|[('R.0.0', 5.0, u'5', u'5')]	|
|1	|[C(5,2)]^2	|5*4/2	|[('R.0.0', 5.0, u'5', u'5')]	|
|2	|[C(5,2)]^2	|5*4*2	|[('R.0.0', 5.0, u'5', u'5')]	|
|3	|[C(5,2)]^2	|(5*4)(5*4)	|[('R.0.0', 5.0, u'5', u'5')]	|
|4	|[C(6,2)]^2	|6!/(2!4!)	|[('R.0.0', 6.0, u'6', u'6')]	|
|5	|[C(5,2)]^2	|5!/(3!2!)	|[('R.0.0', 5.0, u'5', u'5')]	|
|6	|[C(5,2)]^2	|5!/((2!)3!)	|[('R.0.0', 5.0, u'5', u'5')]	|
|7	|[C(4,2)]^2	|4 * 3 / 2	|[('R.0.0', 4.0, u'4', u'4')]	|
|8	|[C(4,2)]^2	|4^2/2	|[('R.0.0', 4.0, u'4', u'4')]	|
|9	|[C(5,2)]^2	|(5*4)^2	|[('R.0.0', 5.0, u'5', u'5')]	|
|10	|[C(4,2)]^2	|4!/(0!*4!)	|[('R.0.0', 4.0, u'4', u'4')]	|
|11	|[C(6,2)]^2	|6!/(2!(6-2)!)	|[('R.0.0', 6.0, u'6', u'6')]	|
|12	|[C(6,2)]^2	|C(6,6)*2	|[('R.0.0', 6.0, u'6', u'6')]	|
|13	|[C(6,2)]^2	|(6*6)*2	|[('R.0.0', 6.0, u'6', u'6')]	|
|14	|[C(4,2)]^2	|(4*3)/2	|[('R.0.0', 4.0, u'4', u'4')]	|
|15	|[C(4,2)]^2	|(4*3)*2	|[('R.0.0', 4.0, u'4', u'4')]	|
|16	|[C(6,2)]^2	|6*5/2	|[('R.0.0', 6.0, u'6', u'6')]	|
|17	|[C(6,2)]^2	|6*6/2	|[('R.0.0', 6.0, u'6', u'6')]	|
|18	|[C(6,2)]^2	|6*5+6*5	|[('R.0.0', 6.0, u'6', u'6')]	|
|19	|[C(4,2)]^2	|[4!/(2!)]	|[('R.0.0', 4.0, u'4', u'4')]	|
|20	|[C(5,2)]^2	|5! * 4!	|[('R.0.0', 5.0, u'5', u'5')]	|
|21	|[C(5,2)]^2	|(5*4) * 13	|[('R.0.0', 5.0, u'5', u'5')]	|
|22	|[C(5,2)]^2	|(5*4) * 13^2	|[('R.0.0', 5.0, u'5', u'5')]	|
|23	|[C(5,2)]^2	|5*4*3	|[('R.0.0', 5.0, u'5', u'5')]	|
|24	|[C(4,2)]^2	|4*12*3	|[('R.0.0', 4.0, u'4', u'4')]	|
|25	|[C(5,2)]^2	|5! *3!	|[('R.0.0', 5.0, u'5', u'5')]	|
|26	|[C(5,2)]^2	|5! + 3!	|[('R.0.0', 5.0, u'5', u'5')]	|
|27	|[C(5,2)]^2	|5! * 3!	|[('R.0.0', 5.0, u'5', u'5')]	|
|28	|[C(5,2)]^2	|5^5 -4	|[('R.0.0', 5.0, u'5', u'5')]	|
|29	|[C(5,2)]^2	|(5!)/(3!2!)	|[('R.0.0', 5.0, u'5', u'5')]	|
|30	|[C(5,2)]^2	|5!/(12)	|[('R.0.0', 5.0, u'5', u'5')]	|
|31	|[C(5,2)]^2	|5!/2	|[('R.0.0', 5.0, u'5', u'5')]	|
|32	|[C(5,2)]^2	|5!/(2!3!)	|[('R.0.0', 5.0, u'5', u'5')]	|
|33	|[C(6,2)]^2	|6!(2!4!)	|[('R.0.0', 6.0, u'6', u'6')]	|
|34	|[C(6,2)]^2	|6!/((2!4!))	|[('R.0.0', 6.0, u'6', u'6')]	|
|35	|[C(6,2)]^2	|(6!/(2!4!))	|[('R.0.0', 6.0, u'6', u'6')]	|
|36	|[C(6,2)]^2	|6!/4!	|[('R.0.0', 6.0, u'6', u'6')]	|
|37	|[C(6,2)]^2	|6!(4!2!)	|[('R.0.0', 6.0, u'6', u'6')]	|
|38	|[C(6,2)]^2	|6!/((4!2!))	|[('R.0.0', 6.0, u'6', u'6')]	|
|39	|[C(6,2)]^2	|6!/(4!2!)	|[('R.0.0', 6.0, u'6', u'6')]	|
|40	|[C(6,2)]^2	|6^2/(2!)	|[('R.0.0', 6.0, u'6', u'6')]	|
|41	|[C(4,2)]^2	|4*3*2	|[('R.0.0', 4.0, u'4', u'4')]	|
|42	|[C(4,2)]^2	|4*3+4*3	|[('R.0.0', 4.0, u'4', u'4')]	|
|43	|[C(4,2)]^2	|4*4*2	|[('R.0.0', 4.0, u'4', u'4')]	|
|44	|[C(6,2)]^2	|6!/(2!*4!)	|[('R.0.0', 6.0, u'6', u'6')]	|
|45	|[C(6,2)]^2	|6!/(4!)	|[('R.0.0', 6.0, u'6', u'6')]	|
|46	|[C(6,2)]^2	|6!/(2*4!)	|[('R.0.0', 6.0, u'6', u'6')]	|
|47	|[C(5,2)]^2	|5!/[(5-2)!2!]	|[('R.0.0', 5.0, u'5', u'5')]	|
|48	|[C(4,2)]^2	|(4*3) + (4*3)	|[('R.0.0', 4.0, u'4', u'4')]	|
|49	|[C(5,2)]^2	|5(4)(2)	|[('R.0.0', 5.0, u'5', u'5')]	|
|50	|[C(6,2)]^2	|(6*5)*(6*5)	|[('R.0.0', 6.0, u'6', u'6')]	|
|51	|[C(6,2)]^2	|(C(6,1)*C(5,1))^2	|[('R.0.0', 6.0, u'6', u'C(6,1)')]	|
|52	|[C(4,2)]^2	|4*3*12	|[('R.0.0', 4.0, u'4', u'4')]	|
|53	|[C(4,2)]^2	|4*3+12	|[('R.0.0', 4.0, u'4', u'4')]	|
|54	|[C(4,2)]^2	|(4*3)^2	|[('R.0.0', 4.0, u'4', u'4')]	|
|55	|[C(5,2)]^2	|5!/(2!*3!)	|[('R.0.0', 5.0, u'5', u'5')]	|
|56	|[C(6,2)]^2	|6! * 6! 	|[('R.0.0', 6.0, u'6', u'6')]	|
|57	|[C(6,2)]^2	|6!/((4!)(2!))	|[('R.0.0', 6.0, u'6', u'6')]	|
|58	|[C(6,2)]^2	|6!/(2!)	|[('R.0.0', 6.0, u'6', u'6')]	|
|59	|[C(5,2)]^2	|5!(4!)	|[('R.0.0', 5.0, u'5', u'5')]	|
|60	|[C(6,2)]^2	|6!(4!*2!)	|[('R.0.0', 6.0, u'6', u'6')]	|
|61	|[C(6,2)]^2	|6!/(4!*2!)	|[('R.0.0', 6.0, u'6', u'6')]	|
|62	|[C(5,2)]^2	|(5*4) *2	|[('R.0.0', 5.0, u'5', u'5')]	|
|63	|[C(5,2)]^2	|(5*4) * (5*4)	|[('R.0.0', 5.0, u'5', u'5')]	|
|64	|[C(5,2)]^2	|5!/2!	|[('R.0.0', 5.0, u'5', u'5')]	|
|65	|[C(6,2)]^2	|6^4-6*7	|[('R.0.0', 6.0, u'6', u'6')]	|
|66	|[C(6,2)]^2	|(6!/(2!*4!))	|[('R.0.0', 6.0, u'6', u'6')]	|
|67	|[C(5,2)]^2	|5*14!/(12!2!)	|[('R.0.0', 5.0, u'5', u'5')]	|
|68	|[C(6,2)]^2	|6!/2!	|[('R.0.0', 6.0, u'6', u'6')]	|
|69	|[C(6,2)]^2	|(6*5)^2	|[('R.0.0', 6.0, u'6', u'6')]	|
|70	|[C(6,2)]^2	|6!(2!4!) * 6!/(2!4!)	|[('R.0.0', 6.0, u'6', u'6')]	|
|71	|[C(6,2)]^2	|6*5*2	|[('R.0.0', 6.0, u'6', u'6')]	|
|72	|[C(5,2)]^2	|5!/(3!2)	|[('R.0.0', 5.0, u'5', u'5')]	|
|73	|[C(5,2)]^2	|5!/(2!)	|[('R.0.0', 5.0, u'5', u'5')]	|




### (55) Mistake Group ['R.0'] of size 55
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|[C(5,2)]^2	|C(5,2)*2	|[('R.0', 10, u'C(5,2)', u'C(5,2)')]	|
|1	|[C(5,2)]^2	|10*3	|[('R.0', 10, u'C(5,2)', u'10')]	|
|2	|[C(6,2)]^2	|C(6,2)*2	|[('R.0', 15, u'C(6,2)', u'C(6,2)')]	|
|3	|[C(6,2)]^2	|C(6,2)*C(15,2)	|[('R.0', 15, u'C(6,2)', u'C(6,2)')]	|
|4	|[C(4,2)]^2	|C(4,2) * 2	|[('R.0', 6, u'C(4,2)', u'C(4,2)')]	|
|5	|[C(6,2)]^2	|C(6,4)*2	|[('R.0', 15, u'C(6,2)', u'C(6,4)')]	|
|6	|[C(6,2)]^2	|3*5*2	|[('R.0', 15, u'C(6,2)', u'3*5')]	|
|7	|[C(6,2)]^2	|C(6,2)*C(4,2)	|[('R.0', 15, u'C(6,2)', u'C(6,2)')]	|
|8	|[C(6,2)]^2	|C(6,2) * 6	|[('R.0', 15, u'C(6,2)', u'C(6,2)')]	|
|9	|[C(6,2)]^2	|C(6,2) + 6	|[('R.0', 15, u'C(6,2)', u'C(6,2)')]	|
|10	|[C(4,2)]^2	|[4!/(2!*2!)]*11	|[('R.0', 6, u'C(4,2)', u'4!/(2!*2!)')]	|
|11	|[C(5,2)]^2	|C(5,2) *5	|[('R.0', 10, u'C(5,2)', u'C(5,2)')]	|
|12	|[C(5,2)]^2	|C(5,2) *2	|[('R.0', 10, u'C(5,2)', u'C(5,2)')]	|
|13	|[C(5,2)]^2	|C(5,2) *4	|[('R.0', 10, u'C(5,2)', u'C(5,2)')]	|
|14	|[C(6,2)]^2	|C(15,2)	|[('R.0', 15, u'C(6,2)', u'15')]	|
|15	|[C(6,2)]^2	|15*6	|[('R.0', 15, u'C(6,2)', u'15')]	|
|16	|[C(4,2)]^2	|[4!/(2!*2!)]*2	|[('R.0', 6, u'C(4,2)', u'4!/(2!*2!)')]	|
|17	|[C(4,2)]^2	|C(4,2)*2	|[('R.0', 6, u'C(4,2)', u'C(4,2)')]	|
|18	|[C(4,2)]^2	|C(4,2)+C(4,2)	|[('R.0', 6, u'C(4,2)', u'C(4,2)')]	|
|19	|[C(4,2)]^2	|6+6	|[('R.0', 6, u'C(4,2)', u'6')]	|
|20	|[C(5,2)]^2	|C(5,2)(2)	|[('R.0', 10, u'C(5,2)', u'C(5,2)')]	|
|21	|[C(5,2)]^2	|C(5,2)+C(5,2)	|[('R.0', 10, u'C(5,2)', u'C(5,2)')]	|
|22	|[C(6,2)]^2	|C(6,2) * 2	|[('R.0', 15, u'C(6,2)', u'C(6,2)')]	|
|23	|[C(4,2)]^2	|(4!/(2!2!))*2	|[('R.0', 6, u'C(4,2)', u'4!/(2!2!)')]	|
|24	|[C(4,2)]^2	|4!/(2!*2!)*2	|[('R.0', 6, u'C(4,2)', u'4!/(2!*2!)')]	|
|25	|[C(6,2)]^2	|(6!/(4!*2!)) - 6	|[('R.0', 15, u'C(6,2)', u'6!/(4!*2!)')]	|
|26	|[C(6,2)]^2	|C(6,2)+C(6,1)	|[('R.0', 15, u'C(6,2)', u'C(6,2)')]	|
|27	|[C(6,2)]^2	|C(6,2)*C(6,1)	|[('R.0', 15, u'C(6,2)', u'C(6,2)')]	|
|28	|[C(6,2)]^2	|C(6,2)C(6,2)C(6,2)	|[('R.0', 15, u'C(6,2)', u'C(6,2)')]	|
|29	|[C(6,2)]^2	|C(6, 2) * 2	|[('R.0', 15, u'C(6,2)', u'C(6, 2)')]	|
|30	|[C(6,2)]^2	|6!/(2!4!) + 5!/(2!3!)	|[('R.0', 15, u'C(6,2)', u'6!/(2!4!)')]	|
|31	|[C(6,2)]^2	|6!/(2!4!) + 4!/(2!2!)	|[('R.0', 15, u'C(6,2)', u'6!/(2!4!)')]	|
|32	|[C(6,2)]^2	|15*2	|[('R.0', 15, u'C(6,2)', u'15')]	|
|33	|[C(4,2)]^2	|C(4,2) * C(3,2)	|[('R.0', 6, u'C(4,2)', u'C(4,2)')]	|
|34	|[C(6,2)]^2	|C(6,2)2	|[('R.0', 15, u'C(6,2)', u'C(6,2)')]	|
|35	|[C(6,2)]^2	|C(6,2)4	|[('R.0', 15, u'C(6,2)', u'C(6,2)')]	|
|36	|[C(6,2)]^2	|C(6,2)2*12	|[('R.0', 15, u'C(6,2)', u'C(6,2)')]	|
|37	|[C(6,2)]^2	|C(6,2)C(5,2)	|[('R.0', 15, u'C(6,2)', u'C(6,2)')]	|
|38	|[C(6,2)]^2	|C(6,2)C(4,2)	|[('R.0', 15, u'C(6,2)', u'C(6,2)')]	|
|39	|[C(6,2)]^2	|C(6,2)C(5,1)C(4,2)C(3,1)	|[('R.0', 15, u'C(6,2)', u'C(6,2)')]	|
|40	|[C(6,2)]^2	|C(6,2)C(5,1)	|[('R.0', 15, u'C(6,2)', u'C(6,2)')]	|
|41	|[C(5,2)]^2	|5!/(2!3!)+5	|[('R.0', 10, u'C(5,2)', u'5!/(2!3!)')]	|




### (48) Mistake Group redirect of size 48




### (23) Mistake Group ['R.0.1'] of size 23
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|[C(6,2)]^2	|4^2*3^2	|[('R.0.1', 2.0, u'2', u'2')]	|
|1	|[C(5,2)]^2	|C(16,2)*C(5,2)	|[('R.0.1', 2.0, u'2', u'2')]	|
|2	|[C(5,2)]^2	|5*4*3*2*1	|[('R.0.1', 2.0, u'2', u'2')]	|
|3	|[C(5,2)]^2	|5!/(2!)3!	|[('R.0.1', 2.0, u'2', u'2!')]	|
|4	|[C(6,2)]^2	|C(11,2)C(10,2)	|[('R.0.1', 2.0, u'2', u'2')]	|
|5	|[C(4,2)]^2	|C(11,2)*C(11,2)	|[('R.0.1', 2.0, u'2', u'2')]	|
|6	|[C(5,2)]^2	|C(15,2) *5	|[('R.0.1', 2.0, u'2', u'2')]	|
|7	|[C(5,2)]^2	|C(15,2) *4	|[('R.0.1', 2.0, u'2', u'2')]	|
|8	|[C(5,2)]^2	|C(15,2) *3	|[('R.0.1', 2.0, u'2', u'2')]	|
|9	|[C(6,2)]^2	|C(15,2)*C(6,2)^2	|[('R.0.1', 2.0, u'2', u'2')]	|
|10	|[C(6,2)]^2	|C(15,2)*C(6,4)^2	|[('R.0.1', 2.0, u'2', u'2')]	|
|11	|[C(6,2)]^2	|C(15,2)*C(6,4)	|[('R.0.1', 2.0, u'2', u'2')]	|
|12	|[C(5,2)]^2	|C(15,2) *13	|[('R.0.1', 2.0, u'2', u'2')]	|
|13	|[C(6,2)]^2	|C(10,2) * 6	|[('R.0.1', 2.0, u'2', u'2')]	|
|14	|[C(6,2)]^2	|6 + 5 + 4 + 3 + 2 +1 	|[('R.0.1', 2.0, u'2', u'2')]	|
|15	|[C(6,2)]^2	|5 + 4 + 3 + 2 +1 	|[('R.0.1', 2.0, u'2', u'2')]	|
|16	|[C(5,2)]^2	|C(11,2)*5	|[('R.0.1', 2.0, u'2', u'2')]	|
|17	|[C(5,2)]^2	|(C(11,2))^5	|[('R.0.1', 2.0, u'2', u'2')]	|
|18	|[C(5,2)]^2	|C(11,2)*C(5,2)	|[('R.0.1', 2.0, u'2', u'2')]	|
|19	|[C(4,2)]^2	|4*3*2*1	|[('R.0.1', 2.0, u'2', u'2')]	|
|20	|[C(5,2)]^2	|C(13,2)*2*C(5,2)	|[('R.0.1', 2.0, u'2', u'2')]	|




### (13) Mistake Group Fraction of size 13




### (4) Mistake Group ['R.0.0', 'R.0.1'] of size 4
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|[C(6,2)]^2	|6^2*5^2	|[('R.0.0', 6.0, u'6', u'6'), ('R.0.1', 2.0, u'2', u'2')]	|
|1	|[C(4,2)]^2	|C(4,2) * C(2,2)	|[('R.0.0', 4.0, u'4', u'4'), ('R.0.1', 2.0, u'2', u'2')]	|
|2	|[C(4,2)]^2	|P(4,2)+P(4,2)	|[('R.0.0', 4.0, u'4', u'4'), ('R.0.1', 2.0, u'2', u'2')]	|
|3	|[C(6,2)]^2	|6*2*5	|[('R.0.0', 6.0, u'6', u'6'), ('R.0.1', 2.0, u'2', u'2')]	|




### (1) Mistake Group Wrong_Sign of size 1




### (153) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:phodgson

	first_attempt
					2015-10-13 02:32:10
	part1_correct_attempt
					['0:00:00', u'C(10,2)']
	part3_incorrect_attempt
					('0:00:00', u'C(4,2)')
					('0:01:51', u'4^4')
					('0:02:45', u'2*C(4,2)')
					('2 days, 4:33:47', u'2 * C(4,2)')
					('2 days, 4:34:50', u'2 * C(4,2) - 1')
					('2 days, 4:35:40', u'2 * (C(4,2) -1) ')
					('2 days, 4:39:58', u'C(4,2)')
					('2 days, 4:41:26', u'2*C(4,2)')
					('2 days, 4:45:48', u'4*C(4,2)')
					('2 days, 4:46:05', u'2*C(4,3)')
					('2 days, 4:47:16', u'2*6')
					('2 days, 4:50:11', u'2*6 - 4')
					('2 days, 4:52:55', u'4^4')
	part3_correct_attempt
					['2 days, 4:54:00', u'C(4,2)*C(4,2)']

1 Student ID:apokhare

	first_attempt
					2015-10-13 18:50:53
	part1_correct_attempt
					['0:00:00', u'16!/(2!*14!)']
	part3_incorrect_attempt
					('0:00:59', u'4!/(2!*2!)')
	part3_correct_attempt
					['0:02:23', u'[4!/(2!*2!)]^2']

2 Student ID:v4zhang

	first_attempt
					2015-10-15 07:34:12
	part1_correct_attempt
					['0:00:00', u'C(15, 2)']
	part3_incorrect_attempt
					('0:00:00', u'C(4, 2)')
					('0:01:34', u'C(3, 2)')
					('0:02:07', u'4 ')
					('0:02:59', u'C(4, 1)*C(3, 1)')
					('0:03:57', u'C(4, 2)')
	part3_correct_attempt
					['0:05:20', u'C(4, 2)*C(4, 2)']

3 Student ID:kvass

	first_attempt
					2015-10-14 06:57:18
	part1_correct_attempt
					['0:00:00', u'C(14,2)']
	part3_incorrect_attempt
					('0:00:00', u'C(4,2)')
	part3_correct_attempt
					['0:01:03', u'C(4,2)**2']

4 Student ID:msaguiar

	first_attempt
					2015-10-14 02:26:42
	part1_correct_attempt
					['0:00:00', u'C(12,2)']
	part3_incorrect_attempt
					('0:00:58', u'C(6,2)')
					('0:01:08', u'2*C(6,2)')
	part3_correct_attempt
					['0:06:32', u'C(6,2)*C(6,2)']

5 Student ID:jguanzho

	first_attempt
					2015-10-09 20:24:36
	part1_correct_attempt
					['0:00:00', u'14!/(12!*2!)']
	part3_incorrect_attempt
					('0:00:00', u'4!/(2! * 2!)')
					('0:00:22', u'4!/(3!)')
					('0:00:52', u'4!/(2!)')
					('0:36:37', u'5!/(4!)')
					('0:38:22', u'5*4')
					('0:45:29', u'(5!/(2!))**2')
	part3_correct_attempt
					['0:45:42', u'(5!/(2!*3!))**2']

6 Student ID:alakamsa

	first_attempt
					2015-10-10 20:47:32
	part1_correct_attempt
					['0:00:00', u'C(11,2)']
	part3_incorrect_attempt
					('0:01:28', u'C(6,2)')
	part3_correct_attempt
					['0:25:07', u'C(6,2)^2']

7 Student ID:dcgriffi

	first_attempt
					2015-10-14 07:27:03
	part1_correct_attempt
					['0:00:00', u'16!/(2!*14!)']
	part3_incorrect_attempt
					('0:00:00', u'5*4*5*4')
					('0:00:31', u'2*(5!/(2!3!))')
					('0:02:48', u'5!/(4!*1!)')
					('0:04:01', u'5*4')
					('0:07:27', u'5*5')
					('0:07:39', u'5!')
					('0:07:52', u'5*5*5*5')
					('0:26:14', u'(5^2-1)^2')
					('0:26:26', u'(5^2-1)*2')
					('0:26:51', u'20^2')
					('0:27:09', u'5^2')
					('0:28:56', u'5!/(4!*1!)')
	part3_correct_attempt
					['0:32:53', u'(5!/(2!*3!))^2']

8 Student ID:dkurli

	first_attempt
					2015-10-14 04:07:37
	part1_correct_attempt
					['0:00:00', u'10!/8!/2!']
	part3_incorrect_attempt
					('0:00:36', u'4!/2!/2!')
	part3_correct_attempt
					['0:01:09', u'36']

9 Student ID:j5phung

	first_attempt
					2015-10-09 18:50:05
	part1_correct_attempt
					['0:00:00', u'C(11,2)']
	part3_incorrect_attempt
					('0:02:06', u'C(5,2)')
					('0:02:34', u'C(5,4)')
	part3_correct_attempt
					['0:03:22', u'C(5,2)^2']

10 Student ID:jyc018

	first_attempt
					2015-10-12 02:28:35
	part1_correct_attempt
					['0:00:00', u'C(12,2)']
	part3_incorrect_attempt
					('0:04:19', u'5*4*5*4')
					('0:05:00', u'5*5')
					('0:06:50', u'C(5,2)')
					('0:07:06', u'2*C(5,2)')
	part3_correct_attempt
					['0:07:48', u'C(5,2)**2']

11 Student ID:jew037

	first_attempt
					2015-10-14 04:29:23
	part1_correct_attempt
					['0:00:00', u'C(10,2)']
	part3_incorrect_attempt
					('0:00:31', u'C(6,2)')
	part3_correct_attempt
					['0:01:19', u'C(6,2)^2']

12 Student ID:btn023

	first_attempt
					2015-10-13 07:39:51
	part1_correct_attempt
					['0:00:00', u'C(16,2)']
	part3_incorrect_attempt
					('0:00:00', u'C(4,2)')
	part3_correct_attempt
					['1 day, 14:31:49', u'C(4,2)^2']

13 Student ID:lalacson

	first_attempt
					2015-10-11 22:49:16
	part1_correct_attempt
					['0:00:00', u'C(13,2)']
	part3_incorrect_attempt
					('0:00:00', u'C(4,2)')
					('0:00:21', u'C(4,1)')
					('0:00:28', u'C(4,2)')
					('0:00:38', u'C(4,3)')
					('0:01:34', u'2*C(4,2)')
	part3_correct_attempt
					['0:02:06', u'C(4,2)^2']

14 Student ID:ssamudra

	first_attempt
					2015-10-15 18:28:43
	part1_correct_attempt
					['0:00:00', u'13!/(11!2!)']
	part3_incorrect_attempt
					('0:01:55', u'4!/(2!2!)')

15 Student ID:tcn013

	first_attempt
					2015-10-15 04:00:44
	part1_correct_attempt
					['0:00:00', u'C(16,2)']
	part3_incorrect_attempt
					('0:00:32', u'C(6,2)')
					('0:04:37', u'2*C(6,2)')
					('0:04:54', u'4*C(13,5)*C(3*13,2)*C(6,2)')
	part3_correct_attempt
					['0:05:18', u'C(6,2)*C(6,2)']

16 Student ID:tstevens

	first_attempt
					2015-10-10 10:45:04
	part1_correct_attempt
					['0:00:00', u'66']
	part3_incorrect_attempt
					('0:07:16', u'5*4')
					('0:25:08', u'5^5')
					('0:25:16', u'2^5')
	part3_correct_attempt
					['4 days, 16:56:38', u'C(5,2)*C(5,2)']

17 Student ID:pthsu

	first_attempt
					2015-10-10 20:31:56
	part1_correct_attempt
					['0:00:00', u'C(13,2)']
	part3_incorrect_attempt
					('0:00:00', u'C(4,2)^2')
	part3_correct_attempt
					['0:00:30', u'C(6,2)^2']

18 Student ID:djk006

	first_attempt
					2015-10-11 02:52:07
	part1_correct_attempt
					['0:00:00', u'14*13/2']
	part3_incorrect_attempt
					('0:02:36', u'4!/2!(2!)')
					('0:02:47', u'4!/4')
					('0:03:22', u'4!/(2!2!)')
					('0:04:00', u'4^2')
					('0:12:11', u'6!/(2!4!)')
					('0:12:37', u'5!/(2!3!)')
	part3_correct_attempt
					['0:23:11', u'36']

19 Student ID:aysee

	first_attempt
					2015-10-13 21:27:01
	part1_correct_attempt
					['0:00:00', u'C(13,2)']
	part3_incorrect_attempt
					('0:00:00', u'C(5,2)')
	part3_correct_attempt
					['0:44:48', u'C(5,2)*C(5,2)']

20 Student ID:dando

	first_attempt
					2015-10-15 20:52:58
	part1_correct_attempt
					['0:00:00', u'13!/(11!2)']
	part3_incorrect_attempt
					('0:00:00', u'2 * 5!/(3!2)')
					('0:04:09', u'2*(5!/(3!2))')
	part3_correct_attempt
					['0:37:08', u'C(5,2)*C(5,2)']

21 Student ID:abasu

	first_attempt
					2015-10-11 02:36:01
	part1_correct_attempt
					['0:00:00', u'C(15,2)']
	part3_incorrect_attempt
					('0:02:46', u'C(4,2)')
	part3_correct_attempt
					['0:03:41', u'C(4,2)^2']

22 Student ID:anvan

	first_attempt
					2015-10-15 02:34:29
	part1_correct_attempt
					['0:00:00', u'14!/(2!12!) ']
	part3_incorrect_attempt
					('0:00:37', u'5*4')
					('0:03:06', u'(5!/2!3!)^2')
	part3_correct_attempt
					['0:03:36', u'( 5!/(2!3!) )^2']

23 Student ID:achava

	first_attempt
					2015-10-13 08:08:08
	part1_correct_attempt
					['0:00:00', u'C(10,2)']
	part3_incorrect_attempt
					('0:10:31', u'C(6,2)')
					('0:10:37', u'C(6,1)')
					('0:10:50', u'C(60,4)')
					('14:52:45', u'C(8,1) * 6')
					('21:49:45', u'C(10,4)')
					('21:49:57', u'C(10,4) * 6')
					('21:50:14', u'C(10,1) * 6')
	part3_correct_attempt
					['1 day, 11:02:06', u'C(6,2) * C(6,2)']

24 Student ID:m4bui

	first_attempt
					2015-10-15 22:33:01
	part1_correct_attempt
					['0:00:00', u'C(11,2)']
	part3_incorrect_attempt
					('0:00:40', u'C(6,2)')
					('0:03:00', u'C(9,2)')
					('0:47:55', u'55-6')
	part3_correct_attempt
					['0:52:56', u'C(6,2)C(6,2)']

25 Student ID:seleon

	first_attempt
					2015-10-15 06:23:59
	part1_correct_attempt
					['0:00:00', u'120']
	part3_incorrect_attempt
					('0:00:29', u'120*2')
					('0:00:33', u'120**2')
	part3_correct_attempt
					['0:00:59', u'15**2']

26 Student ID:flhernan

	first_attempt
					2015-10-14 19:52:56
	part1_correct_attempt
					['0:00:00', u'C(10,2)']
	part3_incorrect_attempt
					('0:02:34', u'2*C(4,2)')
	part3_correct_attempt
					['0:03:39', u'C(4,2)^2']

27 Student ID:a2ahmed

	first_attempt
					2015-10-15 19:49:52
	part1_correct_attempt
					['0:00:00', u'C(15,2)']
	part3_incorrect_attempt
					('0:00:32', u'C(6,4)')
					('0:02:24', u'C(6,2)')
					('0:02:56', u'C(6,4)')
	part3_correct_attempt
					['2:30:15', u'C(6,2)*C(6,2)']

28 Student ID:c1wei

	first_attempt
					2015-10-14 20:50:03
	part1_correct_attempt
					['0:00:00', u'105']
	part3_incorrect_attempt
					('0:01:48', u'12*12')
					('0:02:03', u'144*4')
	part3_correct_attempt
					['0:04:34', u'36']

29 Student ID:arc013

	first_attempt
					2015-10-14 03:35:49
	part1_correct_attempt
					['0:00:00', u'C(12, 2) ']
	part3_incorrect_attempt
					('0:00:56', u'6*6*6*6')
	part3_correct_attempt
					['0:02:40', u'(C(6,2))^2']

30 Student ID:mitopete

	first_attempt
					2015-10-13 20:57:22
	part1_correct_attempt
					['0:00:00', u'11!/(2!9!)']
	part3_incorrect_attempt
					('0:00:46', u'4!/(2!2!)')
					('0:00:57', u'4!')
					('0:02:47', u'4!/(1!3!)*(3!/(1!2!))')
					('0:02:59', u'4!/(1!3!)+(3!/(1!2!))')
					('0:03:24', u'4!/(2!2!)')
					('0:09:14', u'4!')
					('0:16:59', u'44!/(2!42!)')
					('0:17:58', u'44!/(4!40!)')
	part3_correct_attempt
					['0:25:30', u'36']

31 Student ID:tak068

	first_attempt
					2015-10-14 07:31:50
	part1_correct_attempt
					['0:00:00', u'C(10,2)']
	part3_incorrect_attempt
					('0:02:03', u'C(4,2)^2')
					('0:02:26', u'C(6,2)')
					('0:02:49', u'C(4,2)')
					('0:02:54', u'C(4,1)')
					('0:03:25', u'C(4,2)')
					('0:03:48', u'C(6,2)')
	part3_correct_attempt
					['0:03:54', u'C(6,2)^2']

32 Student ID:m8woo

	first_attempt
					2015-10-10 01:16:11
	part1_correct_attempt
					['0:00:00', u'13*12/2']
	part3_incorrect_attempt
					('0:01:52', u'4*3')
					('0:04:55', u'20^2')
	part3_correct_attempt
					['0:05:12', u'5*4*5*4/4']

33 Student ID:ggaddi

	first_attempt
					2015-10-13 18:33:28
	part1_correct_attempt
					['0:00:00', u'10!/(8!*2!)']
	part3_incorrect_attempt
					('0:06:52', u'5*4')
	part3_correct_attempt
					['0:10:41', u'[5!/(3!*2!)]^2']

34 Student ID:jhp077

	first_attempt
					2015-10-15 06:16:46
	part1_correct_attempt
					['0:00:00', u'C(13,2)']
	part3_incorrect_attempt
					('0:15:42', u'C(6,2)')
	part3_correct_attempt
					['0:15:58', u'C(6,2)*C(6,2)']

35 Student ID:jit002

	first_attempt
					2015-10-15 06:17:38
	part1_correct_attempt
					['0:00:00', u'C(13,2)']
	part3_incorrect_attempt
					('0:09:02', u'C(6,2)')
	part3_correct_attempt
					['0:10:17', u'C(6,2)*C(6,2)']

36 Student ID:druble

	first_attempt
					2015-10-13 01:41:50
	part1_correct_attempt
					['0:00:00', u'C(16,2)']
	part3_incorrect_attempt
					('0:00:00', u'5*4')
	part3_correct_attempt
					['0:01:16', u'C(5,2) * C(5,2)']

37 Student ID:h4tu

	first_attempt
					2015-10-15 07:32:14
	part1_correct_attempt
					['0:00:00', u'(16*15/2)']
	part3_incorrect_attempt
					('0:02:07', u'16!/12!')
					('0:03:08', u'6*5')
	part3_correct_attempt
					['0:03:23', u'(6*5/2)^2']

38 Student ID:ccn001

	first_attempt
					2015-10-12 22:48:24
	part1_correct_attempt
					['0:00:00', u'12!/(2!(10!))']
	part3_incorrect_attempt
					('0:00:00', u'(6!(2!(4!)))^2')
	part3_correct_attempt
					['0:33:20', u'(6!/(2!(4!)))^2']

39 Student ID:lrlai

	first_attempt
					2015-10-12 20:43:07
	part1_correct_attempt
					['0:00:00', u'C(15,2)']
	part3_incorrect_attempt
					('0:00:31', u'C(6,2)')
					('0:01:13', u'C(6,4)')
					('0:01:51', u'C(6,5)')
					('0:02:42', u'6*5')
	part3_correct_attempt
					['0:05:54', u'C(6,2)*C(6,2)']

40 Student ID:lguintu

	first_attempt
					2015-10-09 22:07:46
	part1_correct_attempt
					['0:00:00', u'C(16,2)']
	part3_incorrect_attempt
					('0:00:25', u'C(5,2)')
					('0:00:41', u'C(5,1)*C(4,1)')
					('0:01:58', u'C(5,1)')
	part3_correct_attempt
					['0:04:48', u'C(5,2)^2']

41 Student ID:jjchung

	first_attempt
					2015-10-14 20:09:54
	part1_correct_attempt
					['0:00:00', u'C(11,2)']
	part3_incorrect_attempt
					('0:19:31', u'C(5,2)')
					('0:20:31', u'5^4')
					('0:20:56', u'4^5')
					('0:21:07', u'5!4!3!2!')
					('0:21:24', u'5^2')
					('0:21:37', u'C(5,4)')
					('0:21:42', u'C(5,2)')
					('0:22:13', u'5*2')
					('0:22:19', u'5*4')
					('0:22:35', u'5*4*3*2')
					('2:31:25', u'5*5')
					('2:34:46', u'C(5,4)')
					('2:36:37', u'C(5,4)^2')
	part3_correct_attempt
					['2:36:59', u'C(5,2)^2']

42 Student ID:atorr

	first_attempt
					2015-10-11 03:11:07
	part1_correct_attempt
					['0:00:00', u'C(12,2)']
	part3_incorrect_attempt
					('0:01:10', u'C(4,2)')
					('0:01:34', u'P(4,2)')
					('0:02:47', u'C(4,1) * C(3,1)')
					('0:03:10', u'C(3,1) + C(4,1)')
					('0:04:03', u'C(4,2)')
					('0:11:35', u'4!')
					('0:12:39', u'24 * 4')
					('0:13:49', u'4! * 4')
					('0:15:03', u'4^4')
					('0:15:13', u'12^2')
					('0:19:13', u'12*12')
					('0:19:34', u'12^2')
					('0:22:33', u'24^2')
	part3_correct_attempt
					['0:25:47', u'[C(4,2)]^2']

43 Student ID:cprafull

	first_attempt
					2015-10-14 22:13:50
	part1_correct_attempt
					['0:00:00', u'14!/((2!)(12!))']
	part3_incorrect_attempt
					('0:00:51', u'3*5')
					('0:01:31', u'2(6!)/((4!)(2!))')
	part3_correct_attempt
					['0:01:59', u'[6!/((4!)(2!))]^2']

44 Student ID:krau

	first_attempt
					2015-10-14 04:07:44
	part1_correct_attempt
					['0:00:00', u'16!/2!/14!']
	part3_incorrect_attempt
					('0:00:33', u'4!/2!/2!')
					('0:00:44', u'4*4')
					('0:01:11', u'4^2')
	part3_correct_attempt
					['0:01:18', u'36']

45 Student ID:mroknich

	first_attempt
					2015-10-14 01:18:04
	part1_correct_attempt
					['0:00:00', u'C(15,2)']
	part3_incorrect_attempt
					('0:02:45', u'C(6,2)')
					('0:08:35', u'6^2')
					('22:36:59', u'C(6,2)')
					('22:42:28', u'C(6,4)')
					('23:24:16', u'6^2')
					('23:24:54', u'2C(6,2)')
	part3_correct_attempt
					['23:25:15', u'C(6,2)*C(6,2)']

46 Student ID:beyounge

	first_attempt
					2015-10-09 06:07:41
	part1_correct_attempt
					['0:00:00', u'C(14,2)']
	part3_incorrect_attempt
					('0:00:11', u'C(4,2)')
					('0:01:26', u'(4^2*3^2)/4')
					('0:02:38', u'6^2')
	part3_correct_attempt
					['0:03:14', u'(6^2*5^2)/4']

47 Student ID:psable

	first_attempt
					2015-10-15 23:43:43
	part1_correct_attempt
					['0:00:00', u'C(10,2)']
	part3_incorrect_attempt
					('0:00:26', u'C(6,2)')
					('0:00:34', u'C(6,1)')
					('0:00:43', u'C(6,1)*C(6,1)')
					('0:02:07', u'C(6,2)')
					('0:02:20', u'C(6,4)')
					('0:02:38', u'6^4')
	part3_correct_attempt
					['0:03:10', u'C(6,2)*C(6,2)']

48 Student ID:jic212

	first_attempt
					2015-10-12 08:41:41
	part1_correct_attempt
					['0:00:00', u'C(15,2)']
	part3_incorrect_attempt
					('0:01:19', u'C(4,2)')
					('0:02:43', u'4*3')
					('0:04:22', u'C(3,2)')
					('0:06:33', u'4^4')
					('0:07:56', u'4*3*4*3')
	part3_correct_attempt
					['0:10:59', u'C(4,2)*C(4,2)']

49 Student ID:r1gu

	first_attempt
					2015-10-15 22:26:58
	part1_correct_attempt
					['0:00:00', u'11!/(2!9!)']
	part3_incorrect_attempt
					('0:04:02', u'5!/(4!)+2*(5!/(3!2!))+5')
	part3_correct_attempt
					['0:10:45', u'10^2']

50 Student ID:hak014

	first_attempt
					2015-10-13 05:24:06
	part1_correct_attempt
					['0:00:00', u'10!/(2!8!)']
	part3_incorrect_attempt
					('0:00:53', u'4!/(2!2!)')
	part3_correct_attempt
					['0:01:39', u'36']

51 Student ID:mrchin

	first_attempt
					2015-10-14 19:27:36
	part1_correct_attempt
					['0:00:00', u'10!/(8!*2!)']
	part3_incorrect_attempt
					('0:00:15', u'4!/(2!*2!)')
					('0:02:06', u'(4+2-1)!/(2!*(2-1)!)')
					('0:03:22', u'2^4')
					('0:06:04', u'4^4')
					('3:16:54', u'4!/(2!*2!)')
	part3_correct_attempt
					['3:22:25', u'36']

52 Student ID:dis003

	first_attempt
					2015-10-15 11:43:15
	part1_correct_attempt
					['0:00:00', u'C(12,2)']
	part3_incorrect_attempt
					('0:00:19', u'C(4,2)')
					('0:01:13', u'C(4,1)*2')
					('0:02:04', u'C(4+2-1,2-1)')
					('0:02:49', u'4*4')
					('0:02:54', u'4*3')
					('0:05:52', u'C(4,2)')
	part3_correct_attempt
					['0:06:11', u'C(4,2)*C(4,2)']

53 Student ID:rraiyyan

	first_attempt
					2015-10-15 00:27:47
	part1_correct_attempt
					['0:00:00', u'C(12,2)']
	part3_incorrect_attempt
					('0:02:21', u'(5*4)')
					('0:02:56', u'C(12,2)/2')
					('0:03:55', u'C(5,2)')
	part3_correct_attempt
					['0:04:47', u'(C(5,2))^2']

54 Student ID:jhw015

	first_attempt
					2015-10-15 02:51:21
	part1_correct_attempt
					['0:00:00', u'C(12,2)']
	part3_incorrect_attempt
					('0:03:31', u'C(5,2)')
	part3_correct_attempt
					['0:05:54', u'C(5,2)^2']

55 Student ID:dsmonaha

	first_attempt
					2015-10-13 18:30:19
	part1_correct_attempt
					['0:00:00', u'C(11,2)']
	part3_incorrect_attempt
					('0:02:36', u'C(5,2)')
	part3_correct_attempt
					['0:04:01', u'C(5,2)C(5,2)']

56 Student ID:thwan

	first_attempt
					2015-10-11 19:09:01
	part1_correct_attempt
					['0:00:00', u'C(12,2)']
	part3_incorrect_attempt
					('0:00:00', u'C(4,4)*2')
	part3_correct_attempt
					['0:03:53', u'C(6,2)*C(6,2)']

57 Student ID:z3meng

	first_attempt
					2015-10-15 03:29:10
	part1_correct_attempt
					['0:00:00', u'105']
	part3_incorrect_attempt
					('0:03:50', u'6^4')
	part3_correct_attempt
					['0:05:52', u'15^2']

58 Student ID:lcardoso

	first_attempt
					2015-10-13 18:02:01
	part1_correct_attempt
					['0:00:00', u'C(14,2)']
	part3_incorrect_attempt
					('2:51:43', u'C(5,4)')
					('2:53:50', u'C(5,2)')
					('2:54:03', u'C(5,4)')
					('2:54:24', u'C(5,2)')
	part3_correct_attempt
					['3:02:14', u'C(5,2)*C(5,2)']

59 Student ID:jel075

	first_attempt
					2015-10-15 01:27:47
	part1_correct_attempt
					['0:00:00', u'12!/(10!*2!)']
	part3_incorrect_attempt
					('0:00:00', u'4!/(2!*2!)')
					('0:00:13', u'4!/(3!)')
	part3_correct_attempt
					['0:04:32', u'4!/(2!*2!)*(4!/(2!*2!))']

60 Student ID:edescobe

	first_attempt
					2015-10-12 20:39:41
	part1_correct_attempt
					['0:00:00', u'C(12,2)']
	part3_incorrect_attempt
					('0:00:14', u'C(4,2)')
					('0:00:45', u'4^4')
	part3_correct_attempt
					['0:01:16', u'C(4,2)*C(4,2)']

61 Student ID:w4shin

	first_attempt
					2015-10-14 23:46:48
	part1_correct_attempt
					['0:00:00', u'14!/(12!2!)']
	part3_incorrect_attempt
					('0:00:00', u'5*4')
					('0:03:33', u'5!')
					('0:04:05', u'(5^2/2)*2')
					('0:04:34', u'5^2')
					('0:06:51', u'8!/(4!4!)')
					('0:08:23', u'(5!/(3!2!)*5!/(3!2!))/2')
					('0:08:32', u'((5!/(3!2!))*(5!/(3!2!)))/2')
	part3_correct_attempt
					['0:08:39', u'((5!/(3!2!))*(5!/(3!2!)))']

62 Student ID:bakang

	first_attempt
					2015-10-15 02:27:43
	part1_correct_attempt
					['0:00:00', u'C(11,2)']
	part3_incorrect_attempt
					('0:00:34', u'5^4')
					('0:00:44', u'6^4')
					('0:01:28', u'2*(C(6,2))')
					('0:05:41', u'C(6,4)')
					('0:07:04', u'6^4-6')
					('0:12:17', u'2*(C(6,2))')
	part3_correct_attempt
					['0:12:48', u'(C(6,2))^2']

63 Student ID:smohiman

	first_attempt
					2015-10-11 22:29:30
	part1_correct_attempt
					['0:00:00', u'C(16,2)']
	part3_incorrect_attempt
					('0:00:00', u'C(6,2)')
					('0:00:29', u'C(6,4)')
					('0:04:04', u'6*6')
					('0:04:42', u'6*5')
	part3_correct_attempt
					['0:06:31', u'C(6,2)*C(6,2)']

64 Student ID:jtfrankl

	first_attempt
					2015-10-15 21:10:30
	part1_correct_attempt
					['0:00:00', u'C(12,2)']
	part3_incorrect_attempt
					('0:00:28', u'C(6,2)')
					('0:04:02', u'C(6,2)')
					('0:04:23', u'6*5')
					('0:04:51', u'6*6')
					('0:07:26', u'2*6*5')
					('0:07:34', u'2*36')
					('0:08:56', u'C(6,2)')
	part3_correct_attempt
					['0:15:27', u'C(6,2)**2']

65 Student ID:cstringh

	first_attempt
					2015-10-12 23:19:42
	part1_correct_attempt
					['0:00:00', u'C(15, 2)']
	part3_incorrect_attempt
					('0:00:27', u'C(5, 2)')
					('0:01:15', u'C(6, 2)')
					('0:01:25', u'C(7, 2)')
					('0:01:31', u'C(4, 2)')
					('0:01:38', u'C(15, 2)')
					('0:01:46', u'C(13, 2)')
					('0:02:25', u'5*4')
					('0:02:30', u'5*5')
					('0:05:03', u'5!')
					('0:05:12', u'5!/ 4!')
					('0:07:13', u'(5*4) * 13 * 2')
					('0:09:23', u'20 *20')
					('0:10:08', u'5*5*5')
					('4:40:06', u'13^2')
					('4:40:18', u'2^13')
					('4:40:25', u'2^5')
					('4:40:35', u'5^2')
					('4:42:07', u'4^5')
					('4:42:14', u'4^3')
					('4:42:34', u'4!')
					('4:43:19', u'4*5!')
					('4:51:36', u'4^13')
					('4:51:46', u'13^4')
					('4:52:09', u'5^4')
					('4:52:23', u'4^5')
					('4:52:32', u'4^4')
					('4:54:22', u'5^5')
					('4:54:35', u'5^3')
					('4:56:08', u'5*3')
					('4:57:26', u'5! + 4!  + 3! + 2!')
					('4:57:49', u'5! + 4! + 3! + 2')
					('4:58:02', u'5! + 4! + 3!')
					('4:58:24', u'5! * 4! * 3! *2!')
					('4:58:36', u'5! * 4! * 3!')
					('4:58:54', u'5!')
					('5:01:25', u'5! * 3! +1')
					('5:05:19', u'4^5 -4')
					('5:06:04', u'4^5 + 4')
					('5:06:48', u'5^5 ')
					('5:08:45', u'C(5,4)')
					('5:09:00', u'C(5,2)')
					('23:48:49', u'5^5 -5')
					('23:48:58', u'5^4 -5')
					('23:49:07', u'4^5 -5')
	part3_correct_attempt
					['1 day, 0:32:49', u'100']

66 Student ID:eshung

	first_attempt
					2015-10-14 22:32:12
	part1_correct_attempt
					['0:00:00', u'C(10,2)']
	part3_incorrect_attempt
					('0:00:00', u'5*5')
	part3_correct_attempt
					['0:01:21', u'C(5,2)*C(5,2)']

67 Student ID:v4sharma

	first_attempt
					2015-10-14 02:14:31
	part1_correct_attempt
					['0:00:00', u'C(13, 2)']
	part3_incorrect_attempt
					('0:01:04', u'C(4, 2)')
					('0:01:10', u'C(6, 2)')
	part3_correct_attempt
					['0:01:39', u'C(6, 2)^2']

68 Student ID:aurodrig

	first_attempt
					2015-10-15 21:11:11
	part1_correct_attempt
					['0:00:00', u'12!/(2!10!)']
	part3_incorrect_attempt
					('0:03:13', u'4!(2!2!)')
					('0:03:20', u'4!/(2!2!)')
	part3_correct_attempt
					['0:09:49', u'36']

69 Student ID:hsc052

	first_attempt
					2015-10-15 05:45:08
	part1_correct_attempt
					['0:00:00', u'C(10,2)']
	part3_incorrect_attempt
					('0:00:00', u'C(5,2)')
					('0:06:21', u'5^4')
					('0:07:14', u'5*4*5*4')
					('0:08:07', u'5!')
	part3_correct_attempt
					['0:11:16', u'C(5,2)^2']

70 Student ID:v3doan

	first_attempt
					2015-10-11 02:53:35
	part1_correct_attempt
					['0:00:00', u'C(13,2)']
	part3_incorrect_attempt
					('0:00:14', u'C(4,2)')
					('0:00:44', u'4 * 3')
	part3_correct_attempt
					['0:19:07', u'C(4,2)^2']

71 Student ID:sghouse

	first_attempt
					2015-10-12 19:44:16
	part1_correct_attempt
					['0:00:00', u'13*12/2']
	part3_incorrect_attempt
					('0:01:23', u'6*6')
					('0:04:36', u'3*5')
	part3_correct_attempt
					['0:05:10', u'3*5*3*5']

72 Student ID:k3tan

	first_attempt
					2015-10-13 06:21:53
	part1_correct_attempt
					['0:00:00', u'(15*14)/2!']
	part3_incorrect_attempt
					('0:03:35', u'(15*14*6)/2')
	part3_correct_attempt
					['0:13:22', u'36']

73 Student ID:haw081

	first_attempt
					2015-10-11 00:21:36
	part1_correct_attempt
					['0:00:00', u'C(15,2)']
	part3_incorrect_attempt
					('2 days, 0:31:10', u'C(6,4)')
					('2 days, 0:31:49', u'C(6,1)*C(5,1)*C(6,1)*C(5,1)')
					('2 days, 20:09:54', u'C(4,1)*C(3,1)')
	part3_correct_attempt
					['3 days, 0:04:13', u'C(6,2)^2']

74 Student ID:lpettit

	first_attempt
					2015-10-14 20:25:59
	part1_correct_attempt
					['0:00:00', u'16!/(2!*14!)']
	part3_incorrect_attempt
					('0:09:53', u'16*9')
	part3_correct_attempt
					['0:11:48', u'100']

75 Student ID:lywong

	first_attempt
					2015-10-13 08:31:48
	part1_correct_attempt
					['0:00:00', u'11!/(2!9!)']
	part3_incorrect_attempt
					('0:05:43', u'6!')
					('0:18:05', u'36/((2!))')
					('0:22:20', u'6^4')
					('0:31:19', u'6^2')
					('0:42:43', u'6^4')
					('0:43:11', u'C(4,2)^2')
	part3_correct_attempt
					['0:43:25', u'C(6,2)^2']

76 Student ID:hkhodada

	first_attempt
					2015-10-10 19:46:09
	part1_correct_attempt
					['0:00:00', u'C(14,2)']
	part3_incorrect_attempt
					('0:00:21', u'4*C(14,2)')
					('0:26:09', u'4*C(14,2)')
					('10:38:39', u'4*C(4,2)')
					('10:38:47', u'C(4,2)')
					('10:41:00', u'C(4,4)')
					('10:47:15', u'C(28,2)')
					('10:47:49', u'C(28,4)')
					('1 day, 4:26:37', u'2*C(14,2)')
					('1 day, 4:27:15', u'C(4,2)')
	part3_correct_attempt
					['1 day, 4:27:38', u'C(4,2)^2']

77 Student ID:glcohen

	first_attempt
					2015-10-13 05:56:20
	part1_correct_attempt
					['0:00:00', u'(13!)/(11!2!)']
	part3_incorrect_attempt
					('0:08:40', u'78/2')
	part3_correct_attempt
					['15:28:01', u'100']

78 Student ID:acvuong

	first_attempt
					2015-10-13 04:48:59
	part1_correct_attempt
					['0:00:00', u'C(10,2)']
	part3_incorrect_attempt
					('0:00:00', u'C(4,2)')
					('0:02:05', u'2*C(4,2)')
					('0:03:23', u'C(5,2)')
					('0:03:31', u'2*C(5,2)')
	part3_correct_attempt
					['0:04:14', u'C(5,2)*C(5,2)']

79 Student ID:ffhaddad

	first_attempt
					2015-10-10 21:17:33
	part1_correct_attempt
					['0:00:00', u'C(16,2)']
	part3_incorrect_attempt
					('0:00:34', u'C(4,2)')
	part3_correct_attempt
					['0:00:45', u'C(4,2)C(4,2)']

80 Student ID:thk002

	first_attempt
					2015-10-12 04:06:59
	part1_correct_attempt
					['0:00:00', u'C(14,2)']
	part3_incorrect_attempt
					('0:00:27', u'C(4,2)')
	part3_correct_attempt
					['0:00:42', u'C(6,2)^2']

81 Student ID:awollner

	first_attempt
					2015-10-11 20:25:30
	part1_correct_attempt
					['0:00:00', u'C(13,2)']
	part3_incorrect_attempt
					('0:00:23', u'C(6,2)')
	part3_correct_attempt
					['0:01:45', u'C(6,2)^2']

82 Student ID:dcrume

	first_attempt
					2015-10-15 23:20:17
	part1_correct_attempt
					['0:00:00', u'C(14,2)']
	part3_incorrect_attempt
					('0:01:08', u'C(4,2)')

83 Student ID:pvl001

	first_attempt
					2015-10-13 19:50:31
	part1_correct_attempt
					['0:00:00', u'78']
	part3_incorrect_attempt
					('0:00:55', u'5 * 4 * 5 * 4')
	part3_correct_attempt
					['0:02:52', u'10 * 10']

84 Student ID:jcj006

	first_attempt
					2015-10-14 00:13:59
	part1_correct_attempt
					['0:00:00', u'16!/(2*14!)']
	part3_incorrect_attempt
					('0:03:20', u'6*5*6*5')
	part3_correct_attempt
					['0:07:56', u'(6!/(2!4!))^2']

85 Student ID:t2li

	first_attempt
					2015-10-14 06:59:09
	part1_correct_attempt
					['0:00:00', u'C(14,2)']
	part3_incorrect_attempt
					('0:01:18', u'6*6')
					('0:01:43', u'C(6,2)')
					('0:01:46', u'C(6,3)')
					('0:01:49', u'C(6,1)')
					('0:02:05', u'6*5')
					('0:03:11', u'C(24,4)')
					('0:03:15', u'P(24,4)')
					('0:05:20', u'6^3')
					('0:06:16', u'C(6,3)')
					('0:06:19', u'C(6,2)')
	part3_correct_attempt
					['0:07:42', u'C(6,2)^2']

86 Student ID:mbl003

	first_attempt
					2015-10-15 07:20:20
	part1_correct_attempt
					['0:00:00', u'C(16,2)']
	part3_incorrect_attempt
					('0:00:34', u'C(4,2)')
	part3_correct_attempt
					['0:02:47', u'C(4,2)^2']

87 Student ID:n2patil

	first_attempt
					2015-10-13 18:10:04
	part1_correct_attempt
					['0:00:00', u'55']
	part3_incorrect_attempt
					('0:22:13', u'6*5')
					('0:24:51', u'6*55')
	part3_correct_attempt
					['6:12:43', u'225']

88 Student ID:ksmurlo

	first_attempt
					2015-10-13 23:28:25
	part1_correct_attempt
					['0:00:00', u'C(14,2)']
	part3_incorrect_attempt
					('0:01:19', u'4*3')
					('0:04:38', u'C(4,2)')
					('0:05:12', u'P(4,2)')
					('0:09:59', u'C(4,2)')
					('0:10:07', u'P(4,2)')
					('0:16:11', u'4+3+4+3')
					('0:16:17', u'4+3')
					('0:16:45', u'4!')
					('0:19:36', u'4*4')
					('0:31:46', u'4*4*4*4')
					('0:31:53', u'4*4*4')
	part3_correct_attempt
					['0:32:55', u'C(4,2)*C(4,2)']

89 Student ID:jeqin

	first_attempt
					2015-10-15 12:48:59
	part1_correct_attempt
					['0:00:00', u'16!/(2!14!)']
	part3_incorrect_attempt
					('0:01:43', u'6*5')
					('0:02:20', u'6*6*5*5')
					('0:03:36', u'12!/(4!8!)')
					('0:04:05', u'2*6!(2!4!)')
					('0:04:11', u'2*6!/(2!4!)')
					('0:09:56', u'6*5*5*5')
	part3_correct_attempt
					['0:12:26', u'6!/(2!4!) * 6!/(2!4!)']

90 Student ID:jnatale

	first_attempt
					2015-10-14 01:51:04
	part1_correct_attempt
					['0:00:00', u'C(12,2)']
	part3_incorrect_attempt
					('0:12:41', u'C(4,2)')
					('0:12:54', u'C(4,1)')
					('0:13:02', u'C(4,1) + C(4,2)')
					('0:16:56', u'4*3')
					('0:27:25', u'12*2')
	part3_correct_attempt
					['0:46:33', u'C(4,2) * C(4,2)']

91 Student ID:jblynch

	first_attempt
					2015-10-12 07:18:06
	part1_correct_attempt
					['0:00:00', u'C(15,2)']
	part3_incorrect_attempt
					('0:00:34', u'C(6,2)')
					('0:01:07', u'C(6,4)')
	part3_correct_attempt
					['0:01:59', u'C(6,2)*C(6,2)']

92 Student ID:nnh002

	first_attempt
					2015-10-15 06:12:21
	part1_correct_attempt
					['0:00:00', u'C(15,2)']
	part3_incorrect_attempt
					('0:00:00', u'4*4')
	part3_correct_attempt
					['0:03:05', u'C(4,2)^2']

93 Student ID:akhmelni

	first_attempt
					2015-10-15 23:01:17
	part1_correct_attempt
					['0:00:00', u'C(12,2)']
	part3_incorrect_attempt
					('0:05:25', u'C(4,2)')
					('0:05:31', u'C(5,2)')
					('0:11:23', u'C(5,2)')
					('0:11:43', u'C(5,4)')
					('0:13:00', u'2*C(5,2)')
	part3_correct_attempt
					['0:14:11', u'C(5,2)C(5,2)']

94 Student ID:tol003

	first_attempt
					2015-10-14 00:51:48
	part1_correct_attempt
					['0:00:00', u'C(14,2)']
	part3_incorrect_attempt
					('0:00:36', u'14*C(4,2)*13*C(4,2)*12')
					('0:02:22', u'C(4,2)')
					('0:03:47', u'14*C(4,2)*13*C(4,2)')
	part3_correct_attempt
					['0:04:18', u'C(4,2)^2']

95 Student ID:aakumar

	first_attempt
					2015-10-11 02:14:16
	part1_correct_attempt
					['0:00:00', u'78']
	part3_incorrect_attempt
					('0:11:01', u'30^2')
	part3_correct_attempt
					['0:11:44', u'100']

96 Student ID:hachrist

	first_attempt
					2015-10-15 02:37:16
	part1_correct_attempt
					['0:00:00', u'13!/(11!*2!)']
	part3_incorrect_attempt
					('1:30:14', u'5!/(4!*1!)')
					('1:30:29', u'5!/(2!*3!)')
					('1:36:18', u'30/2')
	part3_correct_attempt
					['2:04:07', u'(6!/(4!*2!))^2']

97 Student ID:kew017

	first_attempt
					2015-10-15 20:28:26
	part1_correct_attempt
					['0:00:00', u'15!/(2!13!)']
	part3_incorrect_attempt
					('0:01:06', u'5^4')
	part3_correct_attempt
					['0:13:18', u'100']

98 Student ID:haliew

	first_attempt
					2015-10-14 00:22:56
	part1_correct_attempt
					['0:00:00', u'C(14,2)']
	part3_incorrect_attempt
					('0:00:00', u'C(5,2)')
	part3_correct_attempt
					['0:01:41', u'C(5,2)^2']

99 Student ID:kmc012

	first_attempt
					2015-10-15 02:33:08
	part1_correct_attempt
					['0:00:00', u'(12!)/((2!)*(10!))']
	part3_incorrect_attempt
					('0:01:59', u'(4!)/(2!*2!)')
	part3_correct_attempt
					['0:07:01', u'(((4!)/((2!)*(2!))))^2']

100 Student ID:lahawkin

	first_attempt
					2015-10-14 05:23:54
	part1_correct_attempt
					['0:00:00', u'12!/(10!*2!)']
	part3_incorrect_attempt
					('0:02:16', u'2*10')
	part3_correct_attempt
					['0:06:37', u'((5!)/(3!*2!))^2']

101 Student ID:asetters

	first_attempt
					2015-10-12 06:33:36
	part1_correct_attempt
					['0:00:00', u'(11*10)/2']
	part3_incorrect_attempt
					('0:00:47', u'4*3')
					('0:01:25', u'4+3')
					('0:03:32', u'4*3*4*3')
	part3_correct_attempt
					['0:05:46', u'C(4,2)^2']

102 Student ID:c1sorian

	first_attempt
					2015-10-14 22:21:38
	part1_correct_attempt
					['0:00:00', u'12!/(2!10!)']
	part3_incorrect_attempt
					('0:01:04', u'72!/(6!66!)')
					('0:04:52', u'6*5')
	part3_correct_attempt
					['0:55:04', u'15*15']

103 Student ID:csl030

	first_attempt
					2015-10-14 02:16:45
	part1_correct_attempt
					['0:00:00', u'C(13,2)']
	part3_incorrect_attempt
					('0:00:25', u'C(6,2)')
					('0:00:57', u'C(6,1)')
					('0:01:03', u'C(6,2)')
	part3_correct_attempt
					['0:01:21', u'C(6,2) * C(6,2)']

104 Student ID:azkong

	first_attempt
					2015-10-15 16:20:36
	part1_correct_attempt
					['0:00:00', u'C(15, 2)']
	part3_incorrect_attempt
					('0:00:00', u'C(5, 1)')
					('1:23:55', u'C(5, 2)')
					('1:24:46', u'C(5, 1)')
					('1:25:44', u'C(5, 2)')
					('1:30:13', u'C(4, 2)')
					('1:33:18', u'C(5, 1) * C(4, 1)')
	part3_correct_attempt
					['1:37:13', u'C(5, 2)*C(5,2)']

105 Student ID:rbdoming

	first_attempt
					2015-10-14 19:23:14
	part1_correct_attempt
					['0:00:00', u'C(15,2)']
	part3_incorrect_attempt
					('0:00:00', u'C(15,1)')
					('0:01:34', u'5*5')
					('0:06:17', u'5*4')
					('0:21:20', u'5*5')
					('0:21:32', u'5*4')
					('0:23:34', u'5*2')
					('0:23:59', u'4*3')
	part3_correct_attempt
					['3:34:19', u'C(5,2)^2']

106 Student ID:k4ma

	first_attempt
					2015-10-15 03:29:26
	part1_correct_attempt
					['0:00:00', u'C(13,2)']
	part3_incorrect_attempt
					('0:00:50', u'C(5,2)')
					('0:02:13', u'5*4*5*4')
	part3_correct_attempt
					['0:04:19', u'C(5,2)*C(5,2)']

107 Student ID:ralhadda

	first_attempt
					2015-10-15 19:12:32
	part1_correct_attempt
					['0:00:00', u'45']
	part3_incorrect_attempt
					('2:47:23', u'6^6')

108 Student ID:cagatep

	first_attempt
					2015-10-14 05:12:41
	part1_correct_attempt
					['0:00:00', u'C(12, 2)']
	part3_incorrect_attempt
					('0:00:54', u'C(4,2)')
					('0:01:05', u'C(4,1)')
					('0:01:29', u'4*3')
	part3_correct_attempt
					['0:05:00', u'C(4,2) * C(4,2)']

109 Student ID:hmnaing

	first_attempt
					2015-10-13 00:47:32
	part1_correct_attempt
					['0:00:00', u'C(14,2)']
	part3_incorrect_attempt
					('0:00:00', u'C(5, 2)')
					('0:03:05', u'C(5, 1) * C(5, 1)')
					('0:03:46', u'C(5, 1)')
					('0:03:57', u'5*4')
					('1 day, 5:59:03', u'5*5')
					('1 day, 23:51:11', u'2^5')
					('1 day, 23:51:39', u'C(5, 2)')
					('1 day, 23:52:18', u'5*5')
					('1 day, 23:52:57', u'5*4')
					('1 day, 23:53:47', u'2^(5*4) ')
					('1 day, 23:55:10', u'C(5, 2)')
	part3_correct_attempt
					['1 day, 23:55:30', u'C(5, 2)* C(5, 2)']

110 Student ID:asp025

	first_attempt
					2015-10-15 07:33:26
	part1_correct_attempt
					['0:00:00', u'15!/(2!(15-2)!)']
	part3_incorrect_attempt
					('0:09:06', u'6!/4!2!')
	part3_correct_attempt
					['0:44:15', u'(6!/(2!(6-2)!))^2']

111 Student ID:jfalcone

	first_attempt
					2015-10-14 23:13:51
	part1_correct_attempt
					['0:00:00', u'14!/(2!12!)']
	part3_incorrect_attempt
					('0:04:31', u'4!/(2!2!)')
					('0:07:46', u'4 * 3')
					('20:44:47', u'C(4,2)')
	part3_correct_attempt
					['20:45:23', u'C(4,2) * C(4,2)']

112 Student ID:t2shin

	first_attempt
					2015-10-15 06:11:43
	part1_correct_attempt
					['0:00:00', u'11!/(2!9!)']
	part3_incorrect_attempt
					('0:01:54', u'5!/(1!4!)')
					('0:14:07', u'5*4')
					('0:20:30', u'5!/(1!4!)')
					('1:04:53', u'2*(5!/(2!3!))')
	part3_correct_attempt
					['1:05:24', u'(5!/(2!3!))^2']

113 Student ID:ewbrenna

	first_attempt
					2015-10-12 20:28:01
	part1_correct_attempt
					['0:00:00', u'78']
	part3_incorrect_attempt
					('0:03:00', u'5*4')
					('0:04:55', u'6*5')
					('0:05:27', u'5*4')
					('0:06:23', u'6*5*6*5')
					('0:08:08', u'6^2')
					('0:08:13', u'6^4')
					('0:26:18', u'6^4')
					('0:27:50', u'4!')
					('0:36:42', u'(36)^2/2')
					('0:37:05', u'18^2/2')
					('0:38:00', u'6^4')
	part3_correct_attempt
					['9:03:00', u'15^2']

114 Student ID:spw006

	first_attempt
					2015-10-13 22:38:52
	part1_correct_attempt
					['0:00:00', u'C(10,2)']
	part3_incorrect_attempt
					('0:04:41', u'C(5,2)')
	part3_correct_attempt
					['0:12:38', u'C(5,2)^2']

115 Student ID:s1powers

	first_attempt
					2015-10-11 00:17:11
	part1_correct_attempt
					['0:00:00', u'12!/(10!2!)']
	part3_incorrect_attempt
					('0:01:07', u'5*4')
					('0:03:01', u'5*4')
					('0:03:36', u'4/2!2!')
					('0:03:42', u'4/(2!2!)')
					('0:04:27', u'4*3')
					('19:22:12', u'4!/(2!2!)')
					('19:22:56', u'5!/(4!1!)')
					('19:23:24', u'5*4*3*2')
	part3_correct_attempt
					['19:23:57', u'5!/(3!2!)*5!/(3!2!)']

116 Student ID:e9brown

	first_attempt
					2015-10-14 08:48:39
	part1_correct_attempt
					['0:00:00', u'C(16,2)']
	part3_incorrect_attempt
					('0:00:00', u'C(4,2)')
					('0:00:17', u'6 * 6')
					('0:03:27', u'C(6,2)')
					('0:03:44', u'C(5,2)')
					('0:03:58', u'6 * 6')
					('0:04:06', u'6 * 5')
					('0:04:13', u'5 * 4')
					('0:05:34', u'C(6,4)')
					('0:05:44', u'6^4')
					('1:45:56', u'3!')
					('1:46:30', u'4!')
					('1:47:25', u'6!')
					('1:48:50', u'36*36')
					('1:49:12', u'6! ')
					('1:49:53', u'C(6,4)')
					('1:50:02', u'C(6,2)')
	part3_correct_attempt
					['1:54:42', u'C(6,2) * C(6,2)']

117 Student ID:vsosnovs

	first_attempt
					2015-10-15 04:31:16
	part1_correct_attempt
					['0:00:00', u'C(14,2)']
	part3_incorrect_attempt
					('0:00:43', u'C(4,2)')
					('0:00:50', u'C(6,2)')
					('1:48:14', u'C(6,2)')
					('1:48:41', u'C(6,1)')
					('1:48:47', u'C(4,1)')
					('1:48:54', u'C(6,1)')
					('1:49:06', u'C(4,2)')
					('1:49:34', u'6!')
					('1:57:48', u'C(6,2)')
	part3_correct_attempt
					['2:10:05', u'C(6,2)C(6,2)']

118 Student ID:jdeon

	first_attempt
					2015-10-11 19:44:27
	part1_correct_attempt
					['0:00:00', u'C(11,2)']
	part3_incorrect_attempt
					('3:35:20', u'C(6,2)')
	part3_correct_attempt
					['3:38:49', u'C(6,2)*C(6,2)']

119 Student ID:b1green

	first_attempt
					2015-10-15 21:09:19
	part1_correct_attempt
					['0:00:00', u'C(13,2)']
	part3_incorrect_attempt
					('0:01:42', u'C(6,2)')
					('0:01:54', u'C(6,3)')
					('0:02:47', u'C(5,2)')
					('0:07:51', u'C(6,2)')
					('0:09:50', u'C(6,4)')
					('0:19:45', u'C(6,2)')
					('0:19:50', u'C(6,4)')
	part3_correct_attempt
					['0:24:08', u'C(6,2)C(6,2)']

120 Student ID:p4kumar

	first_attempt
					2015-10-15 09:13:04
	part1_correct_attempt
					['0:00:00', u'C(15, 2)']
	part3_incorrect_attempt
					('0:01:47', u'C(4, 2)')
					('0:08:45', u'4!')
					('1:25:10', u'C(4, 2)')
					('1:28:34', u'C(4, 2)')
	part3_correct_attempt
					['1:29:29', u'C(4, 2)*C(4,2)']

121 Student ID:s2chaudh

	first_attempt
					2015-10-13 05:01:41
	part1_correct_attempt
					['0:00:00', u'C(14,2)']
	part3_incorrect_attempt
					('0:00:00', u'C(6,2)')
					('0:07:28', u'C(6,1)')
					('0:12:14', u'C(6,4)')
					('0:13:15', u'C(6,2)')
					('0:13:23', u'C(6,3)')
					('0:13:34', u'C(6,5)')
					('0:13:45', u'C(6,6)')
					('0:13:54', u'C(6,0)')
	part3_correct_attempt
					['14:45:51', u'C(6,2)^2']

122 Student ID:jmiclat

	first_attempt
					2015-10-15 18:33:08
	part1_correct_attempt
					['0:00:00', u'11!/(2!9!)']
	part3_incorrect_attempt
					('0:00:00', u'(11!/(2!9!))^2')
					('0:00:09', u'(11!/(2!9!))^4')
					('0:00:16', u'(11!/(2!9!))^6')
	part3_correct_attempt
					['0:01:25', u'(6!/(2!4!))^2']

123 Student ID:bmilton

	first_attempt
					2015-10-09 23:14:34
	part1_correct_attempt
					['0:00:00', u'C(13,2)']
	part3_incorrect_attempt
					('0:00:00', u'C(6,4)')
					('0:01:11', u'C(6,2)')
	part3_correct_attempt
					['0:01:36', u'C(6,2)^2']

124 Student ID:yypan

	first_attempt
					2015-10-12 20:58:54
	part1_correct_attempt
					['0:00:00', u'C(12,2)']
	part3_incorrect_attempt
					('0:01:25', u'C(4,2)')
	part3_correct_attempt
					['0:01:43', u'C(4,2)^2']

125 Student ID:jhc010

	first_attempt
					2015-10-15 16:14:59
	part1_correct_attempt
					['0:00:00', u'C(10,2)']
	part3_incorrect_attempt
					('0:01:15', u'C(6,2)')
					('0:02:10', u'C(6,4)')
					('0:02:44', u'6*5')
					('0:03:02', u'6*5*6*5')
					('0:03:53', u'C(6,2)')
					('0:04:15', u'C(6,2)+C(6,3)+C(6,4)')
					('0:04:36', u'4^6')
					('0:06:12', u'6*2')
					('0:09:20', u'C(6,2)')
	part3_correct_attempt
					['0:09:34', u'C(6,2)*C(6,2)']

126 Student ID:cfgutier

	first_attempt
					2015-10-15 23:32:23
	part1_correct_attempt
					['0:00:00', u'91']
	part3_incorrect_attempt
					('0:04:52', u'4^2')
					('0:05:02', u'4*3')

127 Student ID:dkostins

	first_attempt
					2015-10-15 18:34:04
	part1_correct_attempt
					['0:00:00', u'C(10,2)']
	part3_incorrect_attempt
					('0:02:59', u'C(5,2)')
	part3_correct_attempt
					['0:03:23', u'C(5,2)^2']

128 Student ID:agarango

	first_attempt
					2015-10-15 19:43:21
	part1_correct_attempt
					['0:00:00', u'15!/{[2!]*(13!)}']
	part3_incorrect_attempt
					('0:25:31', u'4!')
					('0:27:12', u'4^3')
	part3_correct_attempt
					['0:51:35', u'36']

129 Student ID:s6deng

	first_attempt
					2015-10-14 03:56:06
	part1_correct_attempt
					['0:00:00', u'C(11,2)']
	part3_incorrect_attempt
					('0:02:08', u'C(4,2)')
	part3_correct_attempt
					['0:03:41', u'(4!/(2!2!))*(4!/(2!2!))']

130 Student ID:achinn

	first_attempt
					2015-10-12 23:51:19
	part1_correct_attempt
					['0:00:00', u'(13*12)/2']
	part3_incorrect_attempt
					('0:04:48', u'4^4')
					('0:05:18', u'4*3*4*3')
					('0:05:50', u'(4*3*4*3)/2')
	part3_correct_attempt
					['0:06:17', u'(4*3)*(4*3)/4']

131 Student ID:jap009

	first_attempt
					2015-10-15 22:18:52
	part1_correct_attempt
					['0:00:00', u'13!/(2!11!)']
	part3_incorrect_attempt
					('0:01:13', u'4!/(2!2!)')
	part3_correct_attempt
					['0:06:26', u'(6!/(2!4!))^2']

132 Student ID:kalang

	first_attempt
					2015-10-15 23:15:01
	part1_correct_attempt
					['0:00:00', u'C(16,2)']
	part3_incorrect_attempt
					('0:01:05', u'C(5,2)')
					('0:01:21', u'C(5,1)')
					('0:01:27', u'C(5,4)')
					('0:01:34', u'C(5,3)')
	part3_correct_attempt
					['0:05:37', u'C(5,2)^2']

133 Student ID:jcl084

	first_attempt
					2015-10-13 20:45:47
	part1_correct_attempt
					['0:00:00', u'C(10,2)']
	part3_incorrect_attempt
					('0:01:53', u'C(4,2)')
	part3_correct_attempt
					['0:02:47', u'C(4,2)^2']

134 Student ID:k5law

	first_attempt
					2015-10-12 02:50:09
	part1_correct_attempt
					['0:00:00', u'55']
	part3_incorrect_attempt
					('0:02:45', u'5^2')
					('3:45:12', u'4^4')
					('3:46:01', u'5^4')
	part3_correct_attempt
					['1 day, 1:44:23', u'[5!/(3!2!)]*[5!/(3!2!)]']

135 Student ID:hah008

	first_attempt
					2015-10-15 07:31:49
	part1_correct_attempt
					['0:00:00', u'C(10, 2)']
	part3_incorrect_attempt
					('0:01:33', u'C(6, 2)')
					('1:31:51', u'C(6, 4)')
					('1:34:28', u'C(6, 2)')
	part3_correct_attempt
					['1:36:17', u'C(6, 2) ** 2']

136 Student ID:mcatozzi

	first_attempt
					2015-10-14 00:47:42
	part1_correct_attempt
					['0:00:00', u'C(11,2)']
	part3_incorrect_attempt
					('0:01:06', u'C(5,2)')
					('0:03:11', u'C(5,1)')
					('0:06:43', u'C(5,2)')
	part3_correct_attempt
					['0:09:17', u'100']

137 Student ID:jnn015

	first_attempt
					2015-10-11 23:12:06
	part1_correct_attempt
					['0:00:00', u'12!/10!/2!']
	part3_incorrect_attempt
					('0:00:00', u'(5*4)')
	part3_correct_attempt
					['0:05:38', u'(5!/2!/3!)^2']

138 Student ID:dpereira

	first_attempt
					2015-10-10 05:58:33
	part1_correct_attempt
					['0:00:00', u'C(13,2)']
	part3_incorrect_attempt
					('0:01:53', u'C(5,2)')
					('0:02:02', u'5!')
					('0:02:56', u'5*4*5*4')
					('0:03:19', u'5*4')
					('0:06:50', u'C(5,4)')
					('0:07:00', u'C(5,2)')
	part3_correct_attempt
					['0:18:25', u'C(5,2)^2']

139 Student ID:hmshah

	first_attempt
					2015-10-14 03:07:59
	part1_correct_attempt
					['0:00:00', u'C(13,2)']
	part3_incorrect_attempt
					('0:00:43', u'C(4,2)')
	part3_correct_attempt
					['0:01:10', u'C(4,2)*C(4,2)']

140 Student ID:dtea

	first_attempt
					2015-10-15 23:38:24
	part1_correct_attempt
					['0:00:00', u'C(14,2)']
	part3_incorrect_attempt
					('0:03:59', u'5*4')

141 Student ID:daw023

	first_attempt
					2015-10-15 06:15:31
	part1_correct_attempt
					['0:00:00', u'C(15,2)']
	part3_incorrect_attempt
					('0:00:00', u'C(6,2)')
	part3_correct_attempt
					['0:00:43', u'C(6,2)^2']

142 Student ID:r2fisher

	first_attempt
					2015-10-14 23:23:47
	part1_correct_attempt
					['0:00:00', u'10!/(8!*2!)']
	part3_incorrect_attempt
					('0:01:53', u'6^2')
					('0:02:00', u'2^6')
					('22:54:08', u'6!')
					('22:54:30', u'6^6')
					('22:54:51', u'2^6')
					('22:55:15', u'6*6')
	part3_correct_attempt
					['22:58:13', u'C(6,2)*C(6,2)']

143 Student ID:vasharma

	first_attempt
					2015-10-10 07:50:57
	part1_correct_attempt
					['0:00:00', u'C(11,2)']
	part3_incorrect_attempt
					('0:02:21', u'C(4,2)')
					('0:02:26', u'C(6,2)')
					('0:02:39', u'C(6,1)C(11,2)')
					('0:04:49', u'C(66,2)')
					('18:34:28', u'C(4,2)')
					('18:40:18', u'C(4,1)C(3,1)')
					('18:40:55', u'C(6,2)')
					('18:41:03', u'C(6,1)C(5,1)')
					('19:00:28', u'C(6,2)')
					('19:00:35', u'C(5,2)')
					('19:00:46', u'C(7,2)')
					('19:00:52', u'C(8,2)')
					('19:01:17', u'C(7,2)')
					('19:19:01', u'C(9,2)')
	part3_correct_attempt
					['19:20:17', u'C(6,2)C(6,2)']

144 Student ID:hpc001

	first_attempt
					2015-10-14 22:18:56
	part1_correct_attempt
					['0:00:00', u'C(14,2)']
	part3_incorrect_attempt
					('0:00:22', u'C(5,2)')
					('0:00:48', u'C(5,1)')
	part3_correct_attempt
					['0:47:46', u'C(5,2)*C(5,2)']

145 Student ID:syip

	first_attempt
					2015-10-11 23:26:48
	part1_correct_attempt
					['0:00:00', u'C(11,2)']
	part3_incorrect_attempt
					('0:00:00', u'C(4,2)')
	part3_correct_attempt
					['0:02:07', u'C(4,2) * C(4,2)']

146 Student ID:xweng

	first_attempt
					2015-10-13 02:15:31
	part1_correct_attempt
					['0:00:00', u'C(16,2)']
	part3_incorrect_attempt
					('0:00:12', u'C(4,2)')
					('0:00:19', u'C(4,1)')
					('0:01:08', u'C(4,1)C(4,1)')
					('0:01:56', u'C(4,1)')
					('0:02:23', u'C(4,2)')
	part3_correct_attempt
					['0:02:42', u'C(4,2)C(4,2)']

147 Student ID:amquinte

	first_attempt
					2015-10-14 18:19:04
	part1_correct_attempt
					['0:00:00', u'C(12,2)']
	part3_incorrect_attempt
					('0:03:40', u'30*30')
	part3_correct_attempt
					['4:06:17', u'225']

148 Student ID:c3chung

	first_attempt
					2015-10-15 23:00:44
	part3_incorrect_attempt
					('0:00:00', u'5^5')
					('0:00:00', u'C(75,5)')
					('0:00:00', u'C(15,1)C(14,1)C(5,2)C(5,2)C(13,1)C(5,1)')
					('0:00:00', u'C(15,2)(5)C(15,2)(4)(15)(3)')

149 Student ID:ajvanega

	first_attempt
					2015-10-14 18:41:47
	part1_correct_attempt
					['0:00:00', u'16!/(14!2!)']
	part3_incorrect_attempt
					('0:03:47', u'5^2')
					('0:04:37', u'5^4')
					('0:06:09', u'5*4*5*4')
					('0:07:49', u'5*4')
					('4:02:33', u'5!')
					('4:04:32', u'(5!/3!2!)^2')
	part3_correct_attempt
					['4:04:47', u'(5!/(3!2!))^2']

150 Student ID:zig006

	first_attempt
					2015-10-12 23:28:50
	part1_correct_attempt
					['0:00:00', u'16!/(2!14!)']
	part3_incorrect_attempt
					('0:01:36', u'5!/4!')
	part3_correct_attempt
					['0:02:43', u'(5!/(2!3!))*(5!/(2!3!))']

151 Student ID:kgrozav

	first_attempt
					2015-10-15 19:22:51
	part1_correct_attempt
					['0:00:00', u'C(16,2)']
	part3_incorrect_attempt
					('0:01:54', u'C(6,2)')
	part3_correct_attempt
					['0:09:04', u'C(6,2)*C(6,2)']

152 Student ID:j2phung

	first_attempt
					2015-10-14 07:42:06
	part1_correct_attempt
					['0:00:00', u'13!/(2!11!)']
	part3_incorrect_attempt
					('0:10:28', u'4!/(2!2!)')
					('0:10:50', u'4*3')
	part3_correct_attempt
					['0:13:44', u'(4!/(2!2!))^2']












## Part 4

### (85) Mistake Group Digits of size 85




### (9) Mistake Group redirect of size 9




### (2) Mistake Group Fraction of size 2




### (28) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:v4zhang

	first_attempt
					2015-10-15 07:34:12
	part2_correct_attempt
					['0:01:34', u'C(13, 1)']
	part4_incorrect_attempt
					('0:03:57', u'C(2, 1)')
	part4_correct_attempt
					['0:04:11', u'C(4, 1)']

1 Student ID:t2shin

	first_attempt
					2015-10-15 06:11:43
	part2_correct_attempt
					['0:09:13', u'9']
	part4_incorrect_attempt
					('1:05:34', u'5!/(2!3!)')
	part4_correct_attempt
					['1:44:08', u'5']

2 Student ID:achava

	first_attempt
					2015-10-13 08:08:08
	part2_correct_attempt
					['0:07:57', u'C(8,1)']
	part4_incorrect_attempt
					('1 day, 11:01:57', u'C(6,2) * C(6,2)')
					('1 day, 11:03:05', u'C(10,1)')
					('1 day, 11:03:15', u'C(10,2)')
	part4_correct_attempt
					['1 day, 11:03:23', u'C(6,1)']

3 Student ID:ewbrenna

	first_attempt
					2015-10-12 20:28:01
	part2_correct_attempt
					['0:04:45', u'11']
	part4_incorrect_attempt
					('0:27:44', u'4!')
					('9:02:48', u'15^2')
	part4_correct_attempt
					['9:03:41', u'6']

4 Student ID:mroknich

	first_attempt
					2015-10-14 01:18:04
	part2_correct_attempt
					['0:00:27', u'C(13,1)']
	part4_incorrect_attempt
					('0:06:36', u'6*5')
					('22:35:18', u'6^2')
	part4_correct_attempt
					['22:37:25', u'C(6,1)']

5 Student ID:mbl003

	first_attempt
					2015-10-15 07:20:20
	part2_correct_attempt
					['0:00:21', u'C(14,1)']
	part4_incorrect_attempt
					('0:03:02', u'C(2,1)')
	part4_correct_attempt
					['0:03:08', u'C(4,1)']

6 Student ID:j5phung

	first_attempt
					2015-10-09 18:50:05
	part2_correct_attempt
					['0:00:50', u'C(9,1)']
	part4_incorrect_attempt
					('0:02:06', u'C(3,1)')
					('0:02:34', u'C(1,1)')
	part4_correct_attempt
					['0:03:22', u'C(5,1)']

7 Student ID:p4kumar

	first_attempt
					2015-10-15 09:13:04
	part2_correct_attempt
					['0:04:21', u'13']
	part4_incorrect_attempt
					('1:28:34', u'C(4, 2)')
	part4_correct_attempt
					['1:28:42', u'4']

8 Student ID:haw081

	first_attempt
					2015-10-11 00:21:36
	part2_correct_attempt
					['2 days, 0:30:27', u'C(13,1)']
	part4_incorrect_attempt
					('2 days, 20:09:04', u'C(5,1)')
	part4_correct_attempt
					['3 days, 0:04:43', u'6']

9 Student ID:bmilton

	first_attempt
					2015-10-09 23:14:34
	part2_correct_attempt
					['0:00:00', u'11']
	part4_incorrect_attempt
					('0:00:00', u'C(2,1)')
	part4_correct_attempt
					['0:01:58', u'C(6,1)']

10 Student ID:jew037

	first_attempt
					2015-10-14 04:29:23
	part2_correct_attempt
					['0:00:12', u'(10-2)']
	part4_incorrect_attempt
					('0:01:19', u'C(10,2)*(10-2)*C(6,2)^2 * 6')
	part4_correct_attempt
					['0:01:58', u'6']

11 Student ID:c1sorian

	first_attempt
					2015-10-14 22:21:38
	part2_correct_attempt
					['0:00:16', u'10']
	part4_incorrect_attempt
					('0:04:38', u'6*5')
	part4_correct_attempt
					['0:04:45', u'6']

12 Student ID:s6deng

	first_attempt
					2015-10-14 03:56:06
	part2_correct_attempt
					['0:00:48', u'C(9,1)']
	part4_incorrect_attempt
					('0:02:08', u'C(2,1)')
	part4_correct_attempt
					['0:04:13', u'C(4,1)']

13 Student ID:akhmelni

	first_attempt
					2015-10-15 23:01:17
	part2_correct_attempt
					['0:11:05', u'10']
	part4_incorrect_attempt
					('0:12:54', u'2*C(5,2)')
	part4_correct_attempt
					['0:15:02', u'5']

14 Student ID:dis003

	first_attempt
					2015-10-15 11:43:15
	part2_correct_attempt
					['0:05:52', u'C(12-2,1)']
	part4_incorrect_attempt
					('0:07:53', u'C(4,1)C(4,2)*C(4,2)')
	part4_correct_attempt
					['0:08:41', u'C(4,1)']

15 Student ID:thwan

	first_attempt
					2015-10-11 19:09:01
	part2_correct_attempt
					['-1 day, 23:57:35', u'C(10,1)']
	part4_incorrect_attempt
					('-1 day, 23:57:35', u'C(4,1)')
					('0:00:00', u'C(4,4)')
					('0:01:25', u'C(6,6)')
	part4_correct_attempt
					['0:02:11', u'C(6,1)']

16 Student ID:anvan

	first_attempt
					2015-10-15 02:34:29
	part2_correct_attempt
					['-1 day, 22:47:33', u'2']
	part4_incorrect_attempt
					('-1 day, 23:09:56', u'12*4')
					('-1 day, 23:10:00', u'12*3')
	part4_correct_attempt
					['0:03:06', u'5']

17 Student ID:jnn015

	first_attempt
					2015-10-11 23:12:06
	part2_correct_attempt
					['-1 day, 16:24:17', u'10']
	part4_incorrect_attempt
					('0:04:54', u'(5!/2!/3!)^2')
	part4_correct_attempt
					['0:05:38', u'5']

18 Student ID:ssamudra

	first_attempt
					2015-10-15 18:28:43
	part2_correct_attempt
					['0:01:09', u'11!/(10!1!)']
	part4_incorrect_attempt
					('0:01:55', u'4!(3!1!)')
	part4_correct_attempt
					['0:02:05', u'4!/(3!1!)']

19 Student ID:haliew

	first_attempt
					2015-10-14 00:22:56
	part2_correct_attempt
					['0:00:00', u'C(12,1)']
	part4_incorrect_attempt
					('0:00:00', u'C(3,1)')
	part4_correct_attempt
					['0:02:16', u'5']

20 Student ID:azkong

	first_attempt
					2015-10-15 16:20:36
	part2_correct_attempt
					['1:23:23', u'C(13, 1)']
	part4_incorrect_attempt
					('1:23:55', u'C(3, 1)')
	part4_correct_attempt
					['1:37:36', u'C(5, 1)']

21 Student ID:mitopete

	first_attempt
					2015-10-13 20:57:22
	part2_correct_attempt
					['0:00:27', u'9!/(1!8!)']
	part4_incorrect_attempt
					('0:17:43', u'44!/(4!40!)')
					('0:27:20', u'36!/(1!35!)')
	part4_correct_attempt
					['0:27:51', u'4!/(1!3!)']

22 Student ID:r2fisher

	first_attempt
					2015-10-14 23:23:47
	part2_correct_attempt
					['-1 day, 23:57:31', u'8']
	part4_incorrect_attempt
					('22:50:07', u'6!/(4!*2!)')
	part4_correct_attempt
					['22:50:36', u'6']

23 Student ID:tak068

	first_attempt
					2015-10-14 07:31:50
	part2_correct_attempt
					['0:01:46', u'C(8,1)']
	part4_incorrect_attempt
					('0:03:25', u'C(4,1)')
	part4_correct_attempt
					['0:03:38', u'C(6,1)']

24 Student ID:hsc052

	first_attempt
					2015-10-15 05:45:08
	part2_correct_attempt
					['0:03:59', u'C(8,1)']
	part4_incorrect_attempt
					('0:03:59', u'C(3,1)')
	part4_correct_attempt
					['0:07:14', u'5']

25 Student ID:c3chung

	first_attempt
					2015-10-15 23:00:44
	part4_incorrect_attempt
					('0:00:00', u'5^5')
					('0:00:00', u'C(75,5)')
					('0:00:00', u'C(5,2)15*70*65*60')
					('0:00:00', u'15^5')
					('0:00:00', u'15^5(C(5,1))^5')
					('0:00:00', u'15^5(C(5,1))')
					('0:00:00', u'75*60*45*30*15')

26 Student ID:k4ma

	first_attempt
					2015-10-15 03:29:26
	part2_correct_attempt
					['0:00:27', u'11']
	part4_incorrect_attempt
					('0:14:31', u'C(5,2)')
					('0:14:38', u'C(4,2)')
	part4_correct_attempt
					['0:16:50', u'5']

27 Student ID:aurodrig

	first_attempt
					2015-10-15 21:11:11
	part2_correct_attempt
					['0:02:15', u'10!/(1!9!)']
	part4_incorrect_attempt
					('0:14:07', u'5!/(1!4!)')
	part4_correct_attempt
					['0:14:22', u'4!/(1!3!)']












## Part 5

### (73) Mistake Group redirect of size 73




### (42) Mistake Group Digits of size 42




### (19) Mistake Group ['R.0.0'] of size 19
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(13,2)*(13-2)*[C(6,2)]^2*6	|C(13,2)*11*C(6,4)*C(2,1)	|[('R.0.0', 858.0, u'C(13,2)*(13-2)', u'C(13,2)*11')]	|
|1	|C(15,2)*(15-2)*[C(4,2)]^2*4	|(C(15,2)*C(13,1)*C(4,2)*C(4,1))	|[('R.0.0', 1365.0, u'C(15,2)*(15-2)', u'C(15,2)*C(13,1)')]	|
|2	|C(16,2)*(16-2)*[C(6,2)]^2*6	|C(16,2)*C(14,1)*C(6,2)*6	|[('R.0.0', 1680.0, u'C(16,2)*(16-2)', u'C(16,2)*C(14,1)')]	|
|3	|C(12,2)*(12-2)*[C(6,2)]^2*6	|12!/(2!(10!))*10*((6!(2!(4!)))^2)*6	|[('R.0.0', 660.0, u'C(12,2)*(12-2)', u'12!/(2!(10!))*10')]	|
|4	|C(10,2)*(10-2)*[C(4,2)]^2*4	|C(10,2)*8*C(4,2)*2	|[('R.0.0', 360.0, u'C(10,2)*(10-2)', u'C(10,2)*8')]	|
|5	|C(16,2)*(16-2)*[C(4,2)]^2*4	|[16!/(2!*14!)]*14*2*[4!/(2!*2!)]^2	|[('R.0.0', 1680.0, u'C(16,2)*(16-2)', u'[16!/(2!*14!)]*14')]	|
|6	|C(14,2)*(14-2)*[C(4,2)]^2*4	|14*C(4,2)*13*C(4,2)*12	|[('R.0.0', 1092.0, u'C(14,2)*(14-2)', u'14*C(4,2)*13')]	|
|7	|C(14,2)*(14-2)*[C(6,2)]^2*6	|C(14,2)*12*C(6,2)*6	|[('R.0.0', 1092.0, u'C(14,2)*(14-2)', u'C(14,2)*12')]	|
|8	|C(12,2)*(12-2)*[C(5,2)]^2*5	|(12!/(10!*2!))*10*5*((5!)/(3!*2!))	|[('R.0.0', 660.0, u'C(12,2)*(12-2)', u'(12!/(10!*2!))*10')]	|
|9	|C(14,2)*(14-2)*[C(4,2)]^2*4	|C(14,2)*12*C(4,2)*4	|[('R.0.0', 1092.0, u'C(14,2)*(14-2)', u'C(14,2)*12')]	|
|10	|C(10,2)*(10-2)*[C(4,2)]^2*4	|C(4,2)*C(10,1)*C(4,2)*C(9,1)*32	|[('R.0.0', 360.0, u'C(10,2)*(10-2)', u'C(4,2)*C(10,1)*C(4,2)')]	|
|11	|C(15,2)*(15-2)*[C(6,2)]^2*6	|C(15,2)*C(13,1)*C(6,1)*C(6,2)	|[('R.0.0', 1365.0, u'C(15,2)*(15-2)', u'C(15,2)*C(13,1)')]	|
|12	|C(15,2)*(15-2)*[C(4,2)]^2*4	|(15!/(2!*13!))*13*16*4	|[('R.0.0', 1365.0, u'C(15,2)*(15-2)', u'(15!/(2!*13!))*13')]	|
|13	|C(10,2)*(10-2)*[C(5,2)]^2*5	|C(10,2)*C(8,1)*C(5,2)*C(3,1)	|[('R.0.0', 360.0, u'C(10,2)*(10-2)', u'C(10,2)*C(8,1)')]	|
|14	|C(15,2)*(15-2)*[C(6,2)]^2*6	|C(15,2)*C(13,1)*C(6,2)*C(6,1)	|[('R.0.0', 1365.0, u'C(15,2)*(15-2)', u'C(15,2)*C(13,1)')]	|
|15	|C(10,2)*(10-2)*[C(6,2)]^2*6	|8*C(10,2)*C(52,7)*6	|[('R.0.0', 360.0, u'C(10,2)*(10-2)', u'8*C(10,2)')]	|
|16	|C(10,2)*(10-2)*[C(6,2)]^2*6	|8*C(10,2)*C(6,2)*6	|[('R.0.0', 360.0, u'C(10,2)*(10-2)', u'8*C(10,2)')]	|
|17	|C(13,2)*(13-2)*[C(5,2)]^2*5	|78*11*10*3	|[('R.0.0', 858.0, u'C(13,2)*(13-2)', u'78*11')]	|
|18	|C(10,2)*(10-2)*[C(6,2)]^2*6	|45*8*255*6	|[('R.0.0', 360.0, u'C(10,2)*(10-2)', u'45*8')]	|




### (15) Mistake Group Fraction of size 15




### (12) Mistake Group ['R.0.0.0'] of size 12
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(13,2)*(13-2)*[C(6,2)]^2*6	|C(13,2)*C(6,2)*C(6,1)*C(6,2)	|[('R.0.0.0', 78, u'C(13,2)', u'C(13,2)')]	|
|1	|C(11,2)*(11-2)*[C(6,2)]^2*6	|C(11,2)*C(6,2)*2*C(58,1)	|[('R.0.0.0', 55, u'C(11,2)', u'C(11,2)')]	|
|2	|C(13,2)*(13-2)*[C(6,2)]^2*6	|C(13,2)*6*C(6,2)*12	|[('R.0.0.0', 78, u'C(13,2)', u'C(13,2)')]	|
|3	|C(13,2)*(13-2)*[C(4,2)]^2*4	|C(13,2)*C(13,1)*C(4,2)*C(4,1)	|[('R.0.0.0', 78, u'C(13,2)', u'C(13,2)')]	|
|4	|C(13,2)*(13-2)*[C(6,2)]^2*6	|C(13,2)*C(6,2)*C(6,1)*C(11,1)	|[('R.0.0.0', 78, u'C(13,2)', u'C(13,2)')]	|
|5	|C(11,2)*(11-2)*[C(4,2)]^2*4	|C(11,2)*C(4,2)*C(4,2)*4	|[('R.0.0.0', 55, u'C(11,2)', u'C(11,2)')]	|
|6	|C(14,2)*(14-2)*[C(5,2)]^2*5	|C(14,2)* C(42, 1)*C(5, 2)*C(5, 1)	|[('R.0.0.0', 91, u'C(14,2)', u'C(14,2)')]	|
|7	|C(11,2)*(11-2)*[C(5,2)]^2*5	|C(11,2)*C(5,2)*C(51,1)*C(4,1)	|[('R.0.0.0', 55, u'C(11,2)', u'C(11,2)')]	|
|8	|C(11,2)*(11-2)*[C(5,2)]^2*5	|C(11,2)*C(5,2)*C(51,1)*C(5,1)	|[('R.0.0.0', 55, u'C(11,2)', u'C(11,2)')]	|
|9	|C(14,2)*(14-2)*[C(5,2)]^2*5	|14!/(2!12!) * ( 5!/(2!3!) )* 5 * 12	|[('R.0.0.0', 91, u'C(14,2)', u'14!/(2!12!)')]	|
|10	|C(15,2)*(15-2)*[C(4,2)]^2*4	|(15!/(2!*13!))*15*6*4	|[('R.0.0.0', 105, u'C(15,2)', u'15!/(2!*13!)')]	|
|11	|C(14,2)*(14-2)*[C(6,2)]^2*6	|C(14,2)*C(6,2)*C(12,1)*C(6,1)	|[('R.0.0.0', 91, u'C(14,2)', u'C(14,2)')]	|




### (10) Mistake Group ['R.0.0.1'] of size 10
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(11,2)*(11-2)*[C(5,2)]^2*5	|C(5,2)*11*10*9*8*5^3	|[('R.0.0.1', 9.0, u'11-2', u'9')]	|
|1	|C(12,2)*(12-2)*[C(6,2)]^2*6	|C(12,1)*C(11,1)*C(10,1)*C(4,2)*C(4,1)	|[('R.0.0.1', 10.0, u'12-2', u'C(10,1)')]	|
|2	|C(12,2)*(12-2)*[C(6,2)]^2*6	|C(12,2)*C(6,4)*C(10,1)*C(6,1)*2	|[('R.0.0.1', 10.0, u'12-2', u'C(10,1)')]	|
|3	|C(12,2)*(12-2)*[C(6,2)]^2*6	|C(12,2)*C(6,2)*C(10,1)*C(6,1)*2	|[('R.0.0.1', 10.0, u'12-2', u'C(10,1)')]	|
|4	|C(12,2)*(12-2)*[C(6,2)]^2*6	|12*10*6*6	|[('R.0.0.1', 10.0, u'12-2', u'10')]	|
|5	|C(16,2)*(16-2)*[C(5,2)]^2*5	|C(15,1)*C(14,1)*C(5,2)*C(5,1)	|[('R.0.0.1', 14.0, u'16-2', u'C(14,1)')]	|
|6	|C(13,2)*(13-2)*[C(5,2)]^2*5	|(50*11)*(13!)/(11!2!)	|[('R.0.0.1', 11.0, u'13-2', u'11')]	|
|7	|C(15,2)*(15-2)*[C(4,2)]^2*4	|15*14*13*6*6	|[('R.0.0.1', 13.0, u'15-2', u'13')]	|
|8	|C(16,2)*(16-2)*[C(4,2)]^2*4	|16*15*14*3*4	|[('R.0.0.1', 14.0, u'16-2', u'14')]	|
|9	|C(14,2)*(14-2)*[C(5,2)]^2*5	|((5!/(3!2!))*(5!/(3!2!)))*(14!/(12!2!))	|[('R.0.0.1', 12.0, u'14-2', u'3!2!')]	|




### (6) Mistake Group ['R.0.1'] of size 6
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(10,2)*(10-2)*[C(4,2)]^2*4	|4*10*(C(4,2))^2*C(10,2)	|[('R.0.1', 36.0, u'[C(4,2)]^2', u'(C(4,2))^2')]	|
|1	|C(11,2)*(11-2)*[C(4,2)]^2*4	|C(13,2) * C(4,2)**2*4	|[('R.0.1', 36.0, u'[C(4,2)]^2', u'C(4,2)**2')]	|
|2	|C(15,2)*(15-2)*[C(5,2)]^2*5	|C(15, 2) *100 + 13	|[('R.0.1', 100.0, u'[C(5,2)]^2', u'100')]	|
|3	|C(15,2)*(15-2)*[C(5,2)]^2*5	|C(15, 2) *100 + 13 * 5	|[('R.0.1', 100.0, u'[C(5,2)]^2', u'100')]	|
|4	|C(11,2)*(11-2)*[C(5,2)]^2*5	|C(11,2)*C(5,2)^2*C(51,1)	|[('R.0.1', 100.0, u'[C(5,2)]^2', u'C(5,2)^2')]	|
|5	|C(12,2)*(12-2)*[C(6,2)]^2*6	|66*225*(60!/1)	|[('R.0.1', 225.0, u'[C(6,2)]^2', u'225')]	|




### (5) Mistake Group ['R.0'] of size 5
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(14,2)*(14-2)*[C(6,2)]^2*6	|(C(14,2)*12*(C(6,2)^2)*4)	|[('R.0', 245700.0, u'C(14,2)*(14-2)*[C(6,2)]^2', u'C(14,2)*12*(C(6,2)^2)')]	|
|1	|C(14,2)*(14-2)*[C(5,2)]^2*5	|C(14,2)C(12,1)C(5,2)^2(3)	|[('R.0', 109200.0, u'C(14,2)*(14-2)*[C(5,2)]^2', u'C(14,2)C(12,1)C(5,2)^2')]	|
|2	|C(10,2)*(10-2)*[C(6,2)]^2*6	|C(10,2)*8*C(6,2)**2*4	|[('R.0', 81000.0, u'C(10,2)*(10-2)*[C(6,2)]^2', u'C(10,2)*8*C(6,2)**2')]	|
|3	|C(15,2)*(15-2)*[C(5,2)]^2*5	|C(15,2)*13*(C(5,2)^2)*4	|[('R.0', 136500.0, u'C(15,2)*(15-2)*[C(5,2)]^2', u'C(15,2)*13*(C(5,2)^2)')]	|
|4	|C(15,2)*(15-2)*[C(4,2)]^2*4	|C(15,2)*(15-2)*[C(4,2)]^2*5	|[('R.0', 49140.0, u'C(15,2)*(15-2)*[C(4,2)]^2', u'C(15,2)*(15-2)*[C(4,2)]^2')]	|




### (3) Mistake Group ['R.0.0.0', 'R.0.1'] of size 3
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0', 'R.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(13,2)*(13-2)*[C(6,2)]^2*6	|C(13,2)*6*C(6,2)^2*6	|[('R.0.0.0', 78, u'C(13,2)', u'C(13,2)'), ('R.0.1', 225.0, u'[C(6,2)]^2', u'C(6,2)^2')]	|
|1	|C(15,2)*(15-2)*[C(5,2)]^2*5	|C(15,2)*12*(C(5,2)^2)*5	|[('R.0.0.0', 105, u'C(15,2)', u'C(15,2)'), ('R.0.1', 100.0, u'[C(5,2)]^2', u'C(5,2)^2')]	|
|2	|C(15,2)*(15-2)*[C(4,2)]^2*4	|105*12*36*4	|[('R.0.0.0', 105, u'C(15,2)', u'105'), ('R.0.1', 36.0, u'[C(4,2)]^2', u'36')]	|




### (3) Mistake Group ['R.0.0.1.0'] of size 3
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(11,2)*(11-2)*[C(4,2)]^2*4	|C(4,2)*C(11,2)*9*4	|[('R.0.0.1.0', 11.0, u'11', u'11')]	|
|1	|C(13,2)*(13-2)*[C(6,2)]^2*6	|C(6,2)*C(13,2)*11*6	|[('R.0.0.1.0', 13.0, u'13', u'13')]	|
|2	|C(13,2)*(13-2)*[C(6,2)]^2*6	|C(6,4)*C(13,2)*11*6	|[('R.0.0.1.0', 13.0, u'13', u'13')]	|




### (1) Mistake Group ['R.0.0.0', 'R.0.0.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0', 'R.0.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(12,2)*(12-2)*[C(6,2)]^2*6	|C(12,2)*C(6,6)*C(10,1)*C(6,6)*2	|[('R.0.0.0', 66, u'C(12,2)', u'C(12,2)*C(6,6)'), ('R.0.0.1', 10.0, u'12-2', u'C(10,1)')]	|




### (45) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:apokhare

	first_attempt
					2015-10-13 18:50:53
	part1_correct_attempt
					['0:00:00', u'16!/(2!*14!)']
	part2_correct_attempt
					['0:04:09', u'14']
	part3_correct_attempt
					['0:02:23', u'[4!/(2!*2!)]^2']
	part4_correct_attempt
					['0:02:23', u'4']
	part5_incorrect_attempt
					('0:04:48', u'[16!/(2!*14!)]*14*2*4*[4!/(2!*2!)]^2')
	part5_correct_attempt
					['0:06:24', u'[[16!/(2!*14!)]*14*4*[4!/(2!*2!)]^2]']

1 Student ID:jag028

	first_attempt
					2015-10-15 17:38:33
	part1_correct_attempt
					['0:00:00', u'C(13,2)']
	part2_correct_attempt
					['0:06:21', u'C(11,1)']
	part3_correct_attempt
					['0:14:38', u'36']
	part4_correct_attempt
					['0:16:51', u'4']
	part5_incorrect_attempt
					('3:32:41', u'C(13,2)*C(11,1)*36')
	part5_correct_attempt
					['3:32:53', u'4*C(13,2)*C(11,1)*36']

2 Student ID:vsamant

	first_attempt
					2015-10-10 17:09:14
	part1_correct_attempt
					['0:00:00', u'C(13,2)']
	part2_correct_attempt
					['-1 day, 23:58:32', u'C(11,1)']
	part3_correct_attempt
					['-1 day, 23:58:32', u'C(6,2)*C(6,2)']
	part4_correct_attempt
					['-1 day, 23:58:32', u'C(6,1)']
	part5_incorrect_attempt
					('0:00:00', u'C(13,2)*C(6,2)*C(6,2)')
	part5_correct_attempt
					['0:02:24', u'C(13,2)*C(11,1)*C(6,2)*C(6,1)*C(6,2)']

3 Student ID:kebao

	first_attempt
					2015-10-15 06:17:35
	part1_correct_attempt
					['0:00:00', u'13!/(2!*11!)']
	part2_correct_attempt
					['0:00:00', u'11']
	part3_correct_attempt
					['0:00:00', u'(4!/(2!*2!))^2']
	part4_correct_attempt
					['-1 day, 23:58:52', u'4']
	part5_incorrect_attempt
					('0:00:44', u'13!/(2!*11!)*11*(4!/(2!*2!))^2')
	part5_correct_attempt
					['0:01:39', u'13!/(2!*11!)*11*(4!/(2!*2!))^2*4']

4 Student ID:nisharma

	first_attempt
					2015-10-14 18:11:35
	part1_correct_attempt
					['0:00:00', u'C(16,2)']
	part2_correct_attempt
					['0:00:16', u'14']
	part3_correct_attempt
					['0:01:39', u'C(6,2)^2']
	part4_correct_attempt
					['0:01:39', u'6']
	part5_incorrect_attempt
					('0:18:38', u'C(16,2)')
	part5_correct_attempt
					['0:19:24', u'C(16,2)*C(6,2)^2 * 14 *6']

5 Student ID:lguintu

	first_attempt
					2015-10-09 22:07:46
	part1_correct_attempt
					['0:00:00', u'C(16,2)']
	part3_correct_attempt
					['0:04:48', u'C(5,2)^2']
	part5_incorrect_attempt
					('0:05:59', u'C(16,2)*C(5,2)^2')
	part5_correct_attempt
					['0:06:09', u'5*14*C(16,2)*C(5,2)^2']

6 Student ID:c1sorian

	first_attempt
					2015-10-14 22:21:38
	part1_correct_attempt
					['0:00:00', u'12!/(2!10!)']
	part2_correct_attempt
					['0:00:16', u'10']
	part3_correct_attempt
					['0:55:04', u'15*15']
	part4_correct_attempt
					['0:04:45', u'6']
	part5_incorrect_attempt
					('0:56:34', u'66*225')
	part5_correct_attempt
					['1:02:34', u'66*225*60']

7 Student ID:qtluong

	first_attempt
					2015-10-12 20:28:39
	part1_correct_attempt
					['0:00:00', u'10!/(2!(10-2)!)']
	part2_correct_attempt
					['0:00:57', u'8!/(1!(8-1)!)']
	part3_correct_attempt
					['0:01:45', u'[6!/(2!(6-2)!)]^2']
	part4_correct_attempt
					['0:01:45', u'6!/(1!(6-1)!)']
	part5_incorrect_attempt
					('0:03:51', u'(10!/(2!(10-2)!))(10!/(2!(10-2)!))(10!/(2!(10-2)!))(10!/(2!(10-2)!))')
	part5_correct_attempt
					['0:04:50', u'[10!/(2!(10-2)!)][8!/(1!(8-1)!)][[6!/(2!(6-2)!)]^2][6!/(1!(6-1)!)]']

8 Student ID:asp025

	first_attempt
					2015-10-15 07:33:26
	part1_correct_attempt
					['0:00:00', u'15!/(2!(15-2)!)']
	part2_correct_attempt
					['0:00:00', u'13']
	part3_correct_attempt
					['0:44:15', u'(6!/(2!(6-2)!))^2']
	part4_correct_attempt
					['0:01:45', u'6']
	part5_incorrect_attempt
					('0:44:41', u'(15!/(2!(15-2)!))*(6!/(2!(6-2)!))^2')
	part5_correct_attempt
					['0:46:28', u'6*13(15!/(2!(15-2)!))*(6!/(2!(6-2)!))^2']

9 Student ID:jjm019

	first_attempt
					2015-10-15 23:47:08
	part1_correct_attempt
					['0:00:00', u'45']
	part3_correct_attempt
					['-1 day, 23:59:08', u'100']
	part5_incorrect_attempt
					('0:02:16', u'5*45')
					('0:02:46', u'5*45*4')
					('0:03:16', u'5*45*4*120')
					('0:03:37', u'(5*45*4*120)^2')

10 Student ID:e9brown

	first_attempt
					2015-10-14 08:48:39
	part1_correct_attempt
					['0:00:00', u'C(16,2)']
	part2_correct_attempt
					['0:03:04', u'14']
	part3_correct_attempt
					['1:54:42', u'C(6,2) * C(6,2)']
	part4_correct_attempt
					['0:00:00', u'6']
	part5_incorrect_attempt
					('1:55:07', u'C(6,2) * C(6,2) * C(16,2)')
	part5_correct_attempt
					['1:55:18', u'C(6,2) * C(6,2) * C(16,2) * 14 * 6']

11 Student ID:aakumar

	first_attempt
					2015-10-11 02:14:16
	part1_correct_attempt
					['0:00:00', u'78']
	part2_correct_attempt
					['0:06:52', u'11']
	part3_correct_attempt
					['0:11:44', u'100']
	part4_correct_attempt
					['0:11:53', u'5']
	part5_incorrect_attempt
					('0:14:17', u'13*12*11')
	part5_correct_attempt
					['0:25:29', u'429000']

12 Student ID:jic212

	first_attempt
					2015-10-12 08:41:41
	part1_correct_attempt
					['0:00:00', u'C(15,2)']
	part2_correct_attempt
					['0:00:52', u'13']
	part3_correct_attempt
					['0:10:59', u'C(4,2)*C(4,2)']
	part4_correct_attempt
					['0:03:42', u'4']
	part5_incorrect_attempt
					('0:11:41', u'13*C(4,2)*C(4,2)*4')
	part5_correct_attempt
					['0:13:21', u'C(15,2)*13*C(4,2)*C(4,2)*4']

13 Student ID:ksmurlo

	first_attempt
					2015-10-13 23:28:25
	part1_correct_attempt
					['0:00:00', u'C(14,2)']
	part2_correct_attempt
					['0:00:32', u'14-2']
	part3_correct_attempt
					['0:32:55', u'C(4,2)*C(4,2)']
	part4_correct_attempt
					['0:06:39', u'4']
	part5_incorrect_attempt
					('0:33:07', u'[12*4]+[C(14,2)*36]')
	part5_correct_attempt
					['0:33:16', u'[12*4]*[C(14,2)*36]']

14 Student ID:acvuong

	first_attempt
					2015-10-13 04:48:59
	part1_correct_attempt
					['0:00:00', u'C(10,2)']
	part2_correct_attempt
					['0:02:05', u'8']
	part3_correct_attempt
					['0:04:14', u'C(5,2)*C(5,2)']
	part4_correct_attempt
					['0:03:23', u'5']
	part5_incorrect_attempt
					('0:04:14', u'40*C(5,2)*C(5,2)')
	part5_correct_attempt
					['0:05:07', u'45*8*100*5']

15 Student ID:jmmcalex

	first_attempt
					2015-10-15 08:58:44
	part1_correct_attempt
					['0:00:00', u'13*6']
	part2_correct_attempt
					['0:17:05', u'11']
	part3_correct_attempt
					['0:17:58', u'C(4,2)^2']
	part4_correct_attempt
					['0:18:11', u'4']
	part5_incorrect_attempt
					('0:22:23', u'C(13,2)*11*C(4,2)/2*4')
	part5_correct_attempt
					['0:22:51', u'C(13,2)*11*C(4,2)^2*4']

16 Student ID:mrchin

	first_attempt
					2015-10-14 19:27:36
	part1_correct_attempt
					['0:00:00', u'10!/(8!*2!)']
	part3_correct_attempt
					['3:22:25', u'36']
	part4_correct_attempt
					['3:22:16', u'4!/(1!*3!)']
	part5_incorrect_attempt
					('3:23:11', u'36*[10!/(8!*2!)]-[8*4!/(1!*3!)]')
	part5_correct_attempt
					['3:23:56', u'36*[10!/(8!*2!)]*[8*4!/(1!*3!)]']

17 Student ID:s6deng

	first_attempt
					2015-10-14 03:56:06
	part1_correct_attempt
					['0:00:00', u'C(11,2)']
	part2_correct_attempt
					['0:00:48', u'C(9,1)']
	part3_correct_attempt
					['0:03:41', u'(4!/(2!2!))*(4!/(2!2!))']
	part4_correct_attempt
					['0:04:13', u'C(4,1)']
	part5_incorrect_attempt
					('0:09:39', u'(5!/(1!4!))*(11!/(2!9!))*(4!/(1!3!))')
	part5_correct_attempt
					['0:11:52', u'[[[(44*3)/2]*[(40*3)/2]]/2]*36']

18 Student ID:dis003

	first_attempt
					2015-10-15 11:43:15
	part1_correct_attempt
					['0:00:00', u'C(12,2)']
	part2_correct_attempt
					['0:05:52', u'C(12-2,1)']
	part3_correct_attempt
					['0:06:11', u'C(4,2)*C(4,2)']
	part4_correct_attempt
					['0:08:41', u'C(4,1)']
	part5_incorrect_attempt
					('0:08:41', u'C(12,2)C(12-2,1)C(4,2)C(4,2)')
	part5_correct_attempt
					['0:08:54', u'C(12,2)C(12-2,1)C(4,2)C(4,2)C(4,1)']

19 Student ID:jcl084

	first_attempt
					2015-10-13 20:45:47
	part1_correct_attempt
					['0:00:00', u'C(10,2)']
	part2_correct_attempt
					['0:00:47', u'8']
	part3_correct_attempt
					['0:02:47', u'C(4,2)^2']
	part4_correct_attempt
					['0:03:21', u'C(4,1)']
	part5_incorrect_attempt
					('0:04:02', u'C(10,2)*C(4,2)^2')
	part5_correct_attempt
					['0:05:16', u'C(10,2)*8*C(4,2)^2*C(4,1)']

20 Student ID:skodigal

	first_attempt
					2015-10-15 01:42:02
	part1_correct_attempt
					['0:00:00', u'C(12,2)']
	part2_correct_attempt
					['-1 day, 23:59:21', u'10']
	part3_correct_attempt
					['0:00:15', u'C(6,2)^2']
	part4_correct_attempt
					['0:00:27', u'6']
	part5_incorrect_attempt
					('0:00:55', u'C(6,2)^2 * C(12,2)')
	part5_correct_attempt
					['2:26:03', u'10*6*C(12,2)*C(6,2)^2']

21 Student ID:rraiyyan

	first_attempt
					2015-10-15 00:27:47
	part1_correct_attempt
					['0:00:00', u'C(12,2)']
	part2_correct_attempt
					['0:00:00', u'10']
	part3_correct_attempt
					['0:04:47', u'(C(5,2))^2']
	part4_correct_attempt
					['0:00:00', u'5']
	part5_incorrect_attempt
					('0:09:58', u'C(12,2)*10*(C(5,2))^2')
	part5_correct_attempt
					['0:10:58', u'C(12,2)*10*5*(C(5,2))^2']

22 Student ID:jhw015

	first_attempt
					2015-10-15 02:51:21
	part1_correct_attempt
					['0:00:00', u'C(12,2)']
	part2_correct_attempt
					['0:07:08', u'10']
	part3_correct_attempt
					['0:05:54', u'C(5,2)^2']
	part4_correct_attempt
					['0:05:34', u'5']
	part5_incorrect_attempt
					('0:08:57', u'66-10')
					('0:09:13', u'60-10')
					('0:11:04', u'C(12,2) + C(5,2)^2')
	part5_correct_attempt
					['0:24:30', u'10*5*C(12,2)*C(5,2)^2']

23 Student ID:hpc001

	first_attempt
					2015-10-14 22:18:56
	part1_correct_attempt
					['0:00:00', u'C(14,2)']
	part2_correct_attempt
					['0:10:08', u'12']
	part3_correct_attempt
					['0:47:46', u'C(5,2)*C(5,2)']
	part4_correct_attempt
					['0:00:22', u'C(5,1)']
	part5_incorrect_attempt
					('0:48:09', u'100*5*14')
					('0:48:15', u'100*5')
					('0:48:45', u'100*91')
	part5_correct_attempt
					['0:49:03', u'100*91*12*5']

24 Student ID:tstevens

	first_attempt
					2015-10-10 10:45:04
	part1_correct_attempt
					['0:00:00', u'66']
	part2_correct_attempt
					['0:16:16', u'10']
	part3_correct_attempt
					['4 days, 16:56:38', u'C(5,2)*C(5,2)']
	part4_correct_attempt
					['0:00:46', u'5']
	part5_incorrect_attempt
					('4 days, 16:57:00', u'100*91*12*5')
					('4 days, 16:57:18', u'100*91*10*5')
					('4 days, 17:01:20', u'100*66*12*5')
	part5_correct_attempt
					['4 days, 17:01:37', u'100*66*10*5']

25 Student ID:kmc012

	first_attempt
					2015-10-15 02:33:08
	part1_correct_attempt
					['0:00:00', u'(12!)/((2!)*(10!))']
	part2_correct_attempt
					['0:00:00', u'10']
	part3_correct_attempt
					['0:07:01', u'(((4!)/((2!)*(2!))))^2']
	part5_incorrect_attempt
					('0:07:27', u'((((4!)/((2!)*(2!))))^2)*4')
	part5_correct_attempt
					['0:09:14', u'40*((12!)/((2!)*(10!)))*((((4!)/((2!)*(2!))))^2)']

26 Student ID:jel075

	first_attempt
					2015-10-15 01:27:47
	part1_correct_attempt
					['0:00:00', u'12!/(10!*2!)']
	part3_correct_attempt
					['0:04:32', u'4!/(2!*2!)*(4!/(2!*2!))']
	part4_correct_attempt
					['0:03:00', u'4']
	part5_incorrect_attempt
					('0:08:52', u'12!/(10!*2!)*4!/(2!*2!)*(4!/(2!*2!))*4')
	part5_correct_attempt
					['0:09:58', u'(12!/(10!*2!))*(4!/(2!*2!)*(4!/(2!*2!)))*10*4']

27 Student ID:aysee

	first_attempt
					2015-10-13 21:27:01
	part1_correct_attempt
					['0:00:00', u'C(13,2)']
	part2_correct_attempt
					['0:44:48', u'C(11,1)']
	part3_correct_attempt
					['0:44:48', u'C(5,2)*C(5,2)']
	part4_correct_attempt
					['0:00:00', u'C(5,1)']
	part5_incorrect_attempt
					('0:44:48', u'C(5,2)*C(13,2)')
					('0:47:17', u'C(5,2)*C(5,2)*C(13,2)')
					('0:48:04', u'C(5,2)*C(5,2)*C(13,2)*C(11,1)')
					('0:48:51', u'C(5,2)*C(5,2)*C(5,2)*C(13,2)*C(11,1)')
					('0:49:44', u'C(5,2)*C(13,2)*C(11,1)')
					('0:50:18', u'C(5,2)*C(5,2)*C(13,2)*C(11,1)')
	part5_correct_attempt
					['1:02:00', u'C(5,2)*C(5,2)*C(13,2)*C(11,1)*C(5,1)']

28 Student ID:msaguiar

	first_attempt
					2015-10-14 02:26:42
	part1_correct_attempt
					['0:00:00', u'C(12,2)']
	part2_correct_attempt
					['0:00:00', u'10']
	part3_correct_attempt
					['0:06:32', u'C(6,2)*C(6,2)']
	part4_correct_attempt
					['0:08:14', u'6']
	part5_incorrect_attempt
					('0:08:14', u'C(6,2)*C(6,2)*C(12,2)*10')
					('0:08:32', u'C(6,2)*C(12,2)*10')
					('2:03:28', u'(C(6,2)*C(12,1))*(C(6,2)*C(11,1))*(6*10)')
	part5_correct_attempt
					['2:12:06', u'C(12,2)*10*C(6,2)*(C(6,2))*6']

29 Student ID:eaherman

	first_attempt
					2015-10-14 02:53:58
	part1_correct_attempt
					['0:00:00', u'C(10,2)']
	part2_correct_attempt
					['0:00:15', u'8']
	part3_correct_attempt
					['0:08:18', u'C(5,2)C(5,2)']
	part4_correct_attempt
					['0:00:37', u'5']
	part5_incorrect_attempt
					('0:08:51', u'8(5)(C(5,2)^2)')
					('0:09:04', u'8(5)[(C(5,2)^2)]')
					('0:10:37', u'(C(5,2))^2(5)(8)')
	part5_correct_attempt
					['0:11:30', u'(C(10,2))(C(5,2))^2(5)(8)']

30 Student ID:bakang

	first_attempt
					2015-10-15 02:27:43
	part1_correct_attempt
					['0:00:00', u'C(11,2)']
	part2_correct_attempt
					['-1 day, 23:58:26', u'C(5,2)']
	part3_correct_attempt
					['0:12:48', u'(C(6,2))^2']
	part4_correct_attempt
					['0:10:12', u'6']
	part5_incorrect_attempt
					('0:15:36', u'C(11,2)*9*((C(6,2))^2)*6*((C(6,2))^2)')
	part5_correct_attempt
					['0:16:43', u'C(11,2)*9*((C(6,2))^2)*6']

31 Student ID:anvan

	first_attempt
					2015-10-15 02:34:29
	part1_correct_attempt
					['0:00:00', u'14!/(2!12!) ']
	part2_correct_attempt
					['-1 day, 22:47:33', u'2']
	part3_correct_attempt
					['0:03:36', u'( 5!/(2!3!) )^2']
	part4_correct_attempt
					['0:03:06', u'5']
	part5_incorrect_attempt
					('0:04:07', u'14!/(2!12!)  *60 * ( 5!/(2!3!) )')
					('0:05:04', u'14!/(2!12!) * ( 5!/(2!3!) )')
					('0:34:25', u'14!/(2!12!)  * 12')
					('0:35:11', u'14!/(2!12!) * 12')
	part5_correct_attempt
					['0:35:37', u'14!/(2!12!) * 60 * ( 5!/(2!3!) )^2']

32 Student ID:achava

	first_attempt
					2015-10-13 08:08:08
	part1_correct_attempt
					['0:00:00', u'C(10,2)']
	part2_correct_attempt
					['0:07:57', u'C(8,1)']
	part3_correct_attempt
					['1 day, 11:02:06', u'C(6,2) * C(6,2)']
	part4_correct_attempt
					['1 day, 11:03:23', u'C(6,1)']
	part5_incorrect_attempt
					('1 day, 11:04:07', u'C(8,1) * C(6,2) * C(6,2) * C(6,1)')
	part5_correct_attempt
					['1 day, 11:04:17', u'C(10,2)* C(8,1) * C(6,2) * C(6,2) * C(6,1)']

33 Student ID:lahawkin

	first_attempt
					2015-10-14 05:23:54
	part1_correct_attempt
					['0:00:00', u'12!/(10!*2!)']
	part2_correct_attempt
					['0:01:27', u'10']
	part3_correct_attempt
					['0:06:37', u'((5!)/(3!*2!))^2']
	part4_correct_attempt
					['0:06:03', u'5']
	part5_incorrect_attempt
					('0:07:31', u'(12!/(10!*2!))*10*5')
	part5_correct_attempt
					['0:08:13', u'(12!/(10!*2!))*10*5*((5!)/(3!*2!))^2']

34 Student ID:cstringh

	first_attempt
					2015-10-12 23:19:42
	part1_correct_attempt
					['0:00:00', u'C(15, 2)']
	part2_correct_attempt
					['-1 day, 23:58:12', u'3']
	part3_correct_attempt
					['1 day, 0:32:49', u'100']
	part4_correct_attempt
					['-1 day, 23:22:54', u'5']
	part5_incorrect_attempt
					('1 day, 0:48:44', u'C(15, 2) *100')
	part5_correct_attempt
					['1 day, 1:08:53', u'(C(15,2) C(5,2) C(5,2) C(13,1)C(5,1))']

35 Student ID:eshung

	first_attempt
					2015-10-14 22:32:12
	part1_correct_attempt
					['0:00:00', u'C(10,2)']
	part2_correct_attempt
					['0:01:21', u'8']
	part3_correct_attempt
					['0:01:21', u'C(5,2)*C(5,2)']
	part4_correct_attempt
					['0:00:00', u'5']
	part5_incorrect_attempt
					('0:01:21', u'C(10,2)*9*C(5,2)*C(5,2)*5')
	part5_correct_attempt
					['0:01:34', u'C(10,2)*8*C(5,2)*C(5,2)*5']

36 Student ID:ralhadda

	first_attempt
					2015-10-15 19:12:32
	part1_correct_attempt
					['0:00:00', u'45']
	part2_correct_attempt
					['0:00:30', u'8']
	part4_correct_attempt
					['0:01:24', u'6']
	part5_incorrect_attempt
					('0:03:22', u'15*15')
					('2:46:59', u'15*15')

37 Student ID:r2fisher

	first_attempt
					2015-10-14 23:23:47
	part1_correct_attempt
					['0:00:00', u'10!/(8!*2!)']
	part2_correct_attempt
					['-1 day, 23:57:31', u'8']
	part3_correct_attempt
					['22:58:13', u'C(6,2)*C(6,2)']
	part4_correct_attempt
					['22:50:36', u'6']
	part5_incorrect_attempt
					('22:58:48', u'255*45*8*6')
					('22:59:38', u'255*45+8*6')
					('23:00:24', u'(255+45)*(8+6)')
	part5_correct_attempt
					['23:07:51', u'45*8*225*6']

38 Student ID:vasharma

	first_attempt
					2015-10-10 07:50:57
	part1_correct_attempt
					['0:00:00', u'C(11,2)']
	part2_correct_attempt
					['18:33:26', u'C(9,1)']
	part3_correct_attempt
					['19:20:17', u'C(6,2)C(6,2)']
	part4_correct_attempt
					['0:04:09', u'C(6,1)']
	part5_incorrect_attempt
					('19:20:44', u'C(6,2)C(6,2)C(11,2)')
					('19:22:00', u'C(11,2)C(6,2)C(6,2)')
					('19:22:20', u'C(11,2)C(6,2)')
					('19:27:08', u'C(11,2)C(6,2)C(6,2)')
	part5_correct_attempt
					['19:28:02', u'C(6,1)C(6,2)C(6,2)C(9,1)C(11,2)']

39 Student ID:bpandayk

	first_attempt
					2015-10-15 22:04:18
	part1_correct_attempt
					['0:00:00', u'C(15,2)']
	part2_correct_attempt
					['0:00:07', u'13']
	part3_correct_attempt
					['0:00:29', u'C(4,2)^2']
	part4_correct_attempt
					['0:00:36', u'4']
	part5_incorrect_attempt
					('0:01:14', u'C(15,2)*(15-2)*[C(4,2)]^(2*5)')
	part5_correct_attempt
					['0:01:28', u'C(15,2)*(15-2)*[C(4,2)]^2*4']

40 Student ID:c3chung

	first_attempt
					2015-10-15 23:00:44
	part5_incorrect_attempt
					('0:00:00', u'5^5')
					('0:00:00', u'C(75,5)')

41 Student ID:aurodrig

	first_attempt
					2015-10-15 21:11:11
	part1_correct_attempt
					['0:00:00', u'12!/(2!10!)']
	part2_correct_attempt
					['0:02:15', u'10!/(1!9!)']
	part3_correct_attempt
					['0:09:49', u'36']
	part4_correct_attempt
					['0:14:22', u'4!/(1!3!)']
	part5_incorrect_attempt
					('0:15:47', u'12!/2!10!')
					('0:16:06', u'12!/(2!10!)')
					('0:28:50', u'12*11*4*6')
					('0:30:06', u'12!/(2!10!)')
					('1:59:21', u'13!/(2!11!)')
					('1:59:39', u'13!/(2!11!) * 11')
					('2:04:20', u'13!/(2!10!) * 11 * (4!/(1!3!))')
					('2:04:45', u'13!/(2!10!) * 11 * 4^3')
					('2:05:02', u'13!/(2!10!) * 11 * 3^4')
	part5_correct_attempt
					['2:01:55', u'12!/(2!10!) * 4!/(1!3!) * 10!/(1!9!) * 36 ']

42 Student ID:ytc012

	first_attempt
					2015-10-15 09:24:50
	part1_correct_attempt
					['0:00:00', u'15!/(2!13!)']
	part2_correct_attempt
					['0:01:02', u'13']
	part3_correct_attempt
					['0:01:55', u'6!6!/(2!4!2!4!)']
	part4_correct_attempt
					['0:02:17', u'6']
	part5_incorrect_attempt
					('0:12:34', u'15!/2!13!')
					('0:12:43', u'15!/(2!13!)')
					('0:19:03', u'6!15*15*6!/(2!4!2!4!)')
					('0:19:41', u'13*6*6!15*15*6!/(2!4!2!4!)')
					('0:51:27', u'15!6!6!/(2!2!2!4!4!13!)')
	part5_correct_attempt
					['1:36:49', u'105*13*225*6']

43 Student ID:syc078

	first_attempt
					2015-10-15 01:47:59
	part1_correct_attempt
					['0:00:00', u'16! / (14!2!)']
	part2_correct_attempt
					['0:02:50', u'14']
	part3_correct_attempt
					['0:06:59', u'( (5!) / (3!2!) ) ^2']
	part4_correct_attempt
					['0:07:05', u'5']
	part5_incorrect_attempt
					('0:07:59', u'(16! / (14!2!)) * (( (5!) / (3!2!) ) ^2)')
	part5_correct_attempt
					['0:09:07', u'(16! / (14!2!)) * (( (5!) / (3!2!) ) ^2) * (14*5)']

44 Student ID:k3tan

	first_attempt
					2015-10-13 06:21:53
	part1_correct_attempt
					['0:00:00', u'(15*14)/2!']
	part3_correct_attempt
					['0:13:22', u'36']
	part4_correct_attempt
					['0:13:32', u'4']
	part5_incorrect_attempt
					('0:19:33', u'15*14*13*6*6*4')
					('0:19:50', u'15*14*6*6')
					('0:23:03', u'15*14*13*6*6*4')
	part5_correct_attempt
					['0:24:09', u'(15*14*13*6*6*4)/2']












## Part 6

### (47) Mistake Group ['R.1'] of size 47
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(14,2)*(14-2)*[C(6,2)]^2*6/[C(84,5)]	|(14*13*12*(4^3)) / (C(84,5))	|[('R.1', 30872016, u'C(84,5)', u'C(84,5)')]	|
|1	|C(13,2)*(13-2)*[C(5,2)]^2*5/[C(65,5)]	|[33*13*12*5*4/4] / C(65,5)	|[('R.1', 8259888, u'C(65,5)', u'C(65,5)')]	|
|2	|C(13,2)*(13-2)*[C(6,2)]^2*6/[C(78,5)]	|C(13,1)*C(12,1)*C(11,1)*C(6,2)*C(6,2)*C(6,1)/C(78,5)	|[('R.1', 21111090, u'C(78,5)', u'C(78,5)')]	|
|3	|C(16,2)*(16-2)*[C(4,2)]^2*4/[C(64,5)]	|C(4,1)/C(64,5)	|[('R.1', 7624512, u'C(64,5)', u'C(64,5)')]	|
|4	|C(16,2)*(16-2)*[C(5,2)]^2*5/[C(80,5)]	|(5*C(5,2)*C(5,2)*15*14*16)/(C(80,5))	|[('R.1', 24040016, u'C(80,5)', u'C(80,5)')]	|
|5	|C(11,2)*(11-2)*[C(5,2)]^2*5/[C(55,5)]	|30250/3478761	|[('R.1', 3478761, u'C(55,5)', u'3478761')]	|
|6	|C(12,2)*(12-2)*[C(5,2)]^2*5/[C(60,5)]	|12*11*10*5*(5*4)^2/(60!/5!/55!)	|[('R.1', 5461512, u'C(60,5)', u'60!/5!/55!')]	|
|7	|C(13,2)*(13-2)*[C(6,2)]^2*6/[C(78,5)]	|C(13,2)*6*C(6,2)*12/C(78,5)	|[('R.1', 21111090, u'C(78,5)', u'C(78,5)')]	|
|8	|C(13,2)*(13-2)*[C(6,2)]^2*6/[C(78,5)]	|(6*C(13,2)*(C(6,2))^2)/C(78,5)	|[('R.1', 21111090, u'C(78,5)', u'C(78,5)')]	|
|9	|C(12,2)*(12-2)*[C(6,2)]^2*6/[C(72,5)]	|(12!/(2!(12-2)!)*10*(6!/(2!(6-2)!))^2*6)/12!/(72!/(5!(72-5)!))	|[('R.1', 13991544, u'C(72,5)', u'72!/(5!(72-5)!)')]	|
|10	|C(15,2)*(15-2)*[C(5,2)]^2*5/[C(75,5)]	|(15!/(3!12!)*500)/(75!/(5!70!))	|[('R.1', 17259390, u'C(75,5)', u'75!/(5!70!)')]	|
|11	|C(13,2)*(13-2)*[C(6,2)]^2*6/[C(78,5)]	|[13*12/2*11*6*5/2*4]/[78!/(5!*73!)]	|[('R.1', 21111090, u'C(78,5)', u'78!/(5!*73!)')]	|
|12	|C(16,2)*(16-2)*[C(4,2)]^2*4/[C(64,5)]	|C(16,2)*C(16,2)*C(16,1)*C(4,2)*C(4,1)/C(16*4,5)	|[('R.1', 7624512, u'C(64,5)', u'C(16*4,5)')]	|
|13	|C(14,2)*(14-2)*[C(5,2)]^2*5/[C(70,5)]	|C(13,4) * C(13,1) * C(5,2) * C(3,1) / C(5*14,5)	|[('R.1', 12103014, u'C(70,5)', u'C(5*14,5)')]	|
|14	|C(14,2)*(14-2)*[C(5,2)]^2*5/[C(70,5)]	|C(14,4) * C(14,1) * C(5,2) * C(3,1) / C(5*14,5)	|[('R.1', 12103014, u'C(70,5)', u'C(5*14,5)')]	|
|15	|C(13,2)*(13-2)*[C(5,2)]^2*5/[C(65,5)]	|C(5,2)*C(13,2)/(C(65,5))	|[('R.1', 8259888, u'C(65,5)', u'C(65,5)')]	|
|16	|C(13,2)*(13-2)*[C(5,2)]^2*5/[C(65,5)]	|C(5,2)*C(5,2)*C(13,2)/(C(65,5))	|[('R.1', 8259888, u'C(65,5)', u'C(65,5)')]	|
|17	|C(13,2)*(13-2)*[C(5,2)]^2*5/[C(65,5)]	|C(11,1)*C(5,2)*C(5,2)*C(13,2)/(C(65,5))	|[('R.1', 8259888, u'C(65,5)', u'C(65,5)')]	|
|18	|C(14,2)*(14-2)*[C(5,2)]^2*5/[C(70,5)]	|(C(14,2)C(12,1)C(5,2)C(3,1))/C(14*5,5)	|[('R.1', 12103014, u'C(70,5)', u'C(14*5,5)')]	|
|19	|C(15,2)*(15-2)*[C(5,2)]^2*5/[C(75,5)]	|15!/[(15-2)!2!]*13*5*5!/[(5-2)!2!]/[75!/(70!5!)]	|[('R.1', 17259390, u'C(75,5)', u'75!/(70!5!)')]	|
|20	|C(16,2)*(16-2)*[C(4,2)]^2*4/[C(64,5)]	|16*15*4*3/(64!/(59!*5!))	|[('R.1', 7624512, u'C(64,5)', u'64!/(59!*5!)')]	|
|21	|C(12,2)*(12-2)*[C(5,2)]^2*5/[C(60,5)]	|6600*5/(59*58*57*28)	|[('R.1', 5461512, u'C(60,5)', u'59*58*57*28')]	|
|22	|C(15,2)*(15-2)*[C(6,2)]^2*6/[C(90,5)]	|294840/43949268	|[('R.1', 43949268, u'C(90,5)', u'43949268')]	|
|23	|C(11,2)*(11-2)*[C(6,2)]^2*6/[C(66,5)]	|11*C(11,2)*C(10,3)*6^3/(C(66,5))	|[('R.1', 8936928, u'C(66,5)', u'C(66,5)')]	|
|24	|C(13,2)*(13-2)*[C(4,2)]^2*4/[C(52,5)]	|C(4, 2)*C(4, 2)/(52!/(5!*47!))	|[('R.1', 2598960, u'C(52,5)', u'52!/(5!*47!)')]	|
|25	|C(13,2)*(13-2)*[C(4,2)]^2*4/[C(52,5)]	|C(4, 2)*C(4, 2)/(C(52, 5))	|[('R.1', 2598960, u'C(52,5)', u'C(52, 5)')]	|
|26	|C(15,2)*(15-2)*[C(5,2)]^2*5/[C(75,5)]	|(25*C(15,2)*C(15,1))/C(75,5)	|[('R.1', 17259390, u'C(75,5)', u'C(75,5)')]	|
|27	|C(15,2)*(15-2)*[C(5,2)]^2*5/[C(75,5)]	|(125*C(15,2)*C(14,1))/C(75,5)	|[('R.1', 17259390, u'C(75,5)', u'C(75,5)')]	|
|28	|C(15,2)*(15-2)*[C(5,2)]^2*5/[C(75,5)]	|(100*C(15,2)*C(14,1))/C(75,5)	|[('R.1', 17259390, u'C(75,5)', u'C(75,5)')]	|
|29	|C(15,2)*(15-2)*[C(5,2)]^2*5/[C(75,5)]	|(100*C(15,2)*C(13,1))/C(75,5)	|[('R.1', 17259390, u'C(75,5)', u'C(75,5)')]	|
|30	|C(12,2)*(12-2)*[C(6,2)]^2*6/[C(72,5)]	|10350/C(72,5)	|[('R.1', 13991544, u'C(72,5)', u'C(72,5)')]	|
|31	|C(10,2)*(10-2)*[C(5,2)]^2*5/[C(50,5)]	|(C(10,2)*9*5*5*5)/C(50,5)	|[('R.1', 2118760, u'C(50,5)', u'C(50,5)')]	|
|32	|C(10,2)*(10-2)*[C(5,2)]^2*5/[C(50,5)]	|(C(10,2)*9*C(5,2)*C(5,2)*5)/C(50,5)	|[('R.1', 2118760, u'C(50,5)', u'C(50,5)')]	|
|33	|C(14,2)*(14-2)*[C(5,2)]^2*5/[C(70,5)]	|(5^4(14!(12!2!)))/(70!/(65!5!))	|[('R.1', 12103014, u'C(70,5)', u'70!/(65!5!)')]	|
|34	|C(14,2)*(14-2)*[C(5,2)]^2*5/[C(70,5)]	|(14!/(12!2!))/(70!/(65!5!))	|[('R.1', 12103014, u'C(70,5)', u'70!/(65!5!)')]	|
|35	|C(12,2)*(12-2)*[C(5,2)]^2*5/[C(60,5)]	|C(12,2)*10*(C(5,2))^2/C(60,5)	|[('R.1', 5461512, u'C(60,5)', u'C(60,5)')]	|
|36	|C(12,2)*(12-2)*[C(4,2)]^2*4/[C(48,5)]	|(12!/(10!*2!)*4!/(2!*2!)*(4!/(2!*2!))*4)/(48!/(43!*5!))	|[('R.1', 1712304, u'C(48,5)', u'48!/(43!*5!)')]	|
|37	|C(12,2)*(12-2)*[C(5,2)]^2*5/[C(60,5)]	|546000/C(12*5,5)	|[('R.1', 5461512, u'C(60,5)', u'C(12*5,5)')]	|
|38	|C(10,2)*(10-2)*[C(4,2)]^2*4/[C(40,5)]	|[C(10,2)*8*C(4,2)*2*4]/C(40,5)	|[('R.1', 658008, u'C(40,5)', u'C(40,5)')]	|
|39	|C(13,2)*(13-2)*[C(5,2)]^2*5/[C(65,5)]	|813/8259888	|[('R.1', 8259888, u'C(65,5)', u'8259888')]	|
|40	|C(13,2)*(13-2)*[C(4,2)]^2*4/[C(52,5)]	|(C(13,2)*11*C(4,2)/2*4)/C(52,5)	|[('R.1', 2598960, u'C(52,5)', u'C(52,5)')]	|
|41	|C(12,2)*(12-2)*[C(4,2)]^2*4/[C(48,5)]	|C(12,2)*C(12,2)*C(12,2)*C(12,2)/C(48,5)	|[('R.1', 1712304, u'C(48,5)', u'C(48,5)')]	|
|42	|C(11,2)*(11-2)*[C(6,2)]^2*6/[C(66,5)]	|11!/(2!9!)*9*6*(6!/(2!4!))^2*(6!/(2!4!))^2*9*6*11!/(2!9!)/(66!/(5!61!))	|[('R.1', 8936928, u'C(66,5)', u'66!/(5!61!)')]	|
|43	|C(11,2)*(11-2)*[C(6,2)]^2*6/[C(66,5)]	|(11!/(2!9!))*9*6*(6!/(2!4!))^2*(6!/(2!4!))^2*9*6*11!/(2!9!)/(66!/(5!61!))	|[('R.1', 8936928, u'C(66,5)', u'66!/(5!61!)')]	|
|44	|C(11,2)*(11-2)*[C(6,2)]^2*6/[C(66,5)]	|((6!/(2!4!))^2*9*6*11!/(2!9!)*6*((6!/(2!4!))^2)*9*(11!/(2!9!)))/(66!/(5!61!))	|[('R.1', 8936928, u'C(66,5)', u'66!/(5!61!)')]	|
|45	|C(13,2)*(13-2)*[C(5,2)]^2*5/[C(65,5)]	|(13!/(11!2))/(65!/(60!5!))	|[('R.1', 8259888, u'C(65,5)', u'65!/(60!5!)')]	|
|46	|C(12,2)*(12-2)*[C(4,2)]^2*4/[C(48,5)]	|12!/(2!10!)/[48!/(5!43!)]	|[('R.1', 1712304, u'C(48,5)', u'48!/(5!43!)')]	|




### (29) Mistake Group ['R.0'] of size 29
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(16,2)*(16-2)*[C(6,2)]^2*6/[C(96,5)]	|[ 6*14*((6!/(2!4!))^2)*16!/(2!*14!) ] / (96!/5!91!)	|[('R.0', 2268000.0, u'C(16,2)*(16-2)*[C(6,2)]^2*6', u'6*14*((6!/(2!4!))^2)*16!/(2!*14!)')]	|
|1	|C(14,2)*(14-2)*[C(4,2)]^2*4/[C(56,5)]	|((36*14*13/2)*48)/(56!/51!5!)	|[('R.0', 157248.0, u'C(14,2)*(14-2)*[C(4,2)]^2*4', u'(36*14*13/2)*48')]	|
|2	|C(13,2)*(13-2)*[C(4,2)]^2*4/[C(52,5)]	|((13!/((13-2)!2!))(11)((4!/((4-2)!2!))^2)(4))/(52!/(52-5)!5!)	|[('R.0', 123552.0, u'C(13,2)*(13-2)*[C(4,2)]^2*4', u'(13!/((13-2)!2!))(11)((4!/((4-2)!2!))^2)(4)')]	|
|3	|C(11,2)*(11-2)*[C(6,2)]^2*6/[C(66,5)]	|C(11,2)*9*6*225/C(11,2)	|[('R.0', 668250.0, u'C(11,2)*(11-2)*[C(6,2)]^2*6', u'C(11,2)*9*6*225')]	|
|4	|C(13,2)*(13-2)*[C(6,2)]^2*6/[C(78,5)]	|C(6,2) * C(13,2)*C(6,2)*C(6,1)*C(11,1) / (78*77*76*75*74)	|[('R.0', 1158300.0, u'C(13,2)*(13-2)*[C(6,2)]^2*6', u'C(6,2) * C(13,2)*C(6,2)*C(6,1)*C(11,1)')]	|
|5	|C(12,2)*(12-2)*[C(6,2)]^2*6/[C(72,5)]	|12!/(2!(10!))*10*((6!/(2!(4!)))^2)*6/(72!/5!(72-5)!)	|[('R.0', 891000.0, u'C(12,2)*(12-2)*[C(6,2)]^2*6', u'12!/(2!(10!))*10*((6!/(2!(4!)))^2)*6')]	|
|6	|C(10,2)*(10-2)*[C(5,2)]^2*5/[C(50,5)]	|(C(10,2)*8*C(5,2)^2 * 5 )/ C(52,5)	|[('R.0', 180000.0, u'C(10,2)*(10-2)*[C(5,2)]^2*5', u'C(10,2)*8*C(5,2)^2 * 5')]	|
|7	|C(16,2)*(16-2)*[C(4,2)]^2*4/[C(64,5)]	|(16!/2!/14!*14*36*4) / (64!/59!/4!)	|[('R.0', 241920.0, u'C(16,2)*(16-2)*[C(4,2)]^2*4', u'16!/2!/14!*14*36*4')]	|
|8	|C(13,2)*(13-2)*[C(4,2)]^2*4/[C(52,5)]	|((13!/(2!11!))((4!/(2!2!))^2)((11!/(10!1!)))*4)/(52!/(5!57!))	|[('R.0', 123552.0, u'C(13,2)*(13-2)*[C(4,2)]^2*4', u'(13!/(2!11!))((4!/(2!2!))^2)((11!/(10!1!)))*4')]	|
|9	|C(12,2)*(12-2)*[C(4,2)]^2*4/[C(48,5)]	|(12!/(2!*10!)*10*(4!/(2!*2!))^2*4)/(52!/(5!*47!))	|[('R.0', 95040.0, u'C(12,2)*(12-2)*[C(4,2)]^2*4', u'12!/(2!*10!)*10*(4!/(2!*2!))^2*4')]	|
|10	|C(16,2)*(16-2)*[C(5,2)]^2*5/[C(80,5)]	|(12000*70)/(80!/5!*75!)	|[('R.0', 840000.0, u'C(16,2)*(16-2)*[C(5,2)]^2*5', u'12000*70')]	|
|11	|C(16,2)*(16-2)*[C(5,2)]^2*5/[C(80,5)]	|840000/( 80!/75!5!)	|[('R.0', 840000.0, u'C(16,2)*(16-2)*[C(5,2)]^2*5', u'840000')]	|
|12	|C(12,2)*(12-2)*[C(6,2)]^2*6/[C(72,5)]	|891000/(72!/5!67!)	|[('R.0', 891000.0, u'C(12,2)*(12-2)*[C(6,2)]^2*6', u'891000')]	|
|13	|C(15,2)*(15-2)*[C(6,2)]^2*6/[C(90,5)]	|(C(15,2)*C(13,1)*C(6,1)*C(6,2)*C(6,2))/(C(15,2))	|[('R.0', 1842750.0, u'C(15,2)*(15-2)*[C(6,2)]^2*6', u'C(15,2)*C(13,1)*C(6,1)*C(6,2)*C(6,2)')]	|
|14	|C(14,2)*(14-2)*[C(6,2)]^2*6/[C(84,5)]	|6*C(14,2)*C(14-2,1)*C(6,2)^2/(6*14)	|[('R.0', 1474200.0, u'C(14,2)*(14-2)*[C(6,2)]^2*6', u'6*C(14,2)*C(14-2,1)*C(6,2)^2')]	|
|15	|C(16,2)*(16-2)*[C(6,2)]^2*6/[C(96,5)]	|120*14*15**2*6/5	|[('R.0', 2268000.0, u'C(16,2)*(16-2)*[C(6,2)]^2*6', u'120*14*15**2*6')]	|
|16	|C(11,2)*(11-2)*[C(5,2)]^2*5/[C(55,5)]	|(9*11!/(2!9!)*5*(5!/(2!3!))^2)/(55!/5!50!)	|[('R.0', 247500.0, u'C(11,2)*(11-2)*[C(5,2)]^2*5', u'9*11!/(2!9!)*5*(5!/(2!3!))^2')]	|
|17	|C(15,2)*(15-2)*[C(4,2)]^2*4/[C(60,5)]	|C(15, 2)*C(4, 2)*C(4, 2)*C(13, 1)*C(4, 1)/C(15, 2)	|[('R.0', 196560.0, u'C(15,2)*(15-2)*[C(4,2)]^2*4', u'C(15, 2)*C(4, 2)*C(4, 2)*C(13, 1)*C(4, 1)')]	|
|18	|C(16,2)*(16-2)*[C(4,2)]^2*4/[C(64,5)]	|241920/914941440	|[('R.0', 241920.0, u'C(16,2)*(16-2)*[C(4,2)]^2*4', u'241920')]	|
|19	|C(11,2)*(11-2)*[C(6,2)]^2*6/[C(66,5)]	|((6!/(2!4!))^2*9*6*11!)/(2!9!)/((11!)/(5!6!))	|[('R.0', 668250.0, u'C(11,2)*(11-2)*[C(6,2)]^2*6', u'((6!/(2!4!))^2*9*6*11!)/(2!9!)')]	|
|20	|C(15,2)*(15-2)*[C(5,2)]^2*5/[C(75,5)]	|682500/(75!/(71!4!))	|[('R.0', 682500.0, u'C(15,2)*(15-2)*[C(5,2)]^2*5', u'682500')]	|
|21	|C(15,2)*(15-2)*[C(5,2)]^2*5/[C(75,5)]	|682500/(70!/(71!5!))	|[('R.0', 682500.0, u'C(15,2)*(15-2)*[C(5,2)]^2*5', u'682500')]	|
|22	|C(15,2)*(15-2)*[C(4,2)]^2*4/[C(60,5)]	|196560/2598960	|[('R.0', 196560.0, u'C(15,2)*(15-2)*[C(4,2)]^2*4', u'196560')]	|
|23	|C(15,2)*(15-2)*[C(4,2)]^2*4/[C(60,5)]	|(15!/(13!2!))*(15-2)*(4!/(2!2!))^2*4/(60!/(56!4!))	|[('R.0', 196560.0, u'C(15,2)*(15-2)*[C(4,2)]^2*4', u'(15!/(13!2!))*(15-2)*(4!/(2!2!))^2*4')]	|
|24	|C(11,2)*(11-2)*[C(5,2)]^2*5/[C(55,5)]	|247500/(55*54*53*52*51*50)	|[('R.0', 247500.0, u'C(11,2)*(11-2)*[C(5,2)]^2*5', u'247500')]	|
|25	|C(11,2)*(11-2)*[C(5,2)]^2*5/[C(55,5)]	|247500/(55*54*53*52*51)	|[('R.0', 247500.0, u'C(11,2)*(11-2)*[C(5,2)]^2*5', u'247500')]	|
|26	|C(12,2)*(12-2)*[C(4,2)]^2*4/[C(48,5)]	|12!/(2!10!) * 4!/(1!3!) * 10!/(1!9!) * 36 / [48!/2!46!]	|[('R.0', 95040.0, u'C(12,2)*(12-2)*[C(4,2)]^2*4', u'12!/(2!10!) * 4!/(1!3!) * 10!/(1!9!) * 36')]	|
|27	|C(12,2)*(12-2)*[C(4,2)]^2*4/[C(48,5)]	|12!/(2!10!) * 4!/(1!3!) * 10!/(1!9!) * 36 / [48!/5!43!]	|[('R.0', 95040.0, u'C(12,2)*(12-2)*[C(4,2)]^2*4', u'12!/(2!10!) * 4!/(1!3!) * 10!/(1!9!) * 36')]	|
|28	|C(10,2)*(10-2)*[C(6,2)]^2*6/[C(60,5)]	|(C(10,2)*C(8,1)*C(6,2)*C(6,2)*C(6,1))/(60*59*58*57*56)	|[('R.0', 486000.0, u'C(10,2)*(10-2)*[C(6,2)]^2*6', u'C(10,2)*C(8,1)*C(6,2)*C(6,2)*C(6,1)')]	|




### (20) Mistake Group redirect of size 20




### (8) Mistake Group ['R.0.0.0', 'R.1'] of size 8
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(13,2)*(13-2)*[C(6,2)]^2*6/[C(78,5)]	|C(13,2)*11*C(6,4)*C(2,1)/C(13*6,5)	|[('R.0.0.0', 858.0, u'C(13,2)*(13-2)', u'C(13,2)*11'), ('R.1', 21111090, u'C(78,5)', u'C(13*6,5)')]	|
|1	|C(16,2)*(16-2)*[C(6,2)]^2*6/[C(96,5)]	|C(16,2)*C(14,1)*C(6,2)*6/C(96,5)	|[('R.0.0.0', 1680.0, u'C(16,2)*(16-2)', u'C(16,2)*C(14,1)'), ('R.1', 61124064, u'C(96,5)', u'C(96,5)')]	|
|2	|C(10,2)*(10-2)*[C(4,2)]^2*4/[C(40,5)]	|(C(10,2)*8*C(4,2)*2)/C(40,5)	|[('R.0.0.0', 360.0, u'C(10,2)*(10-2)', u'C(10,2)*8'), ('R.1', 658008, u'C(40,5)', u'C(40,5)')]	|
|3	|C(14,2)*(14-2)*[C(4,2)]^2*4/[C(56,5)]	|(C(14,2)*12*C(4,2)*4)/C(14*4,5)	|[('R.0.0.0', 1092.0, u'C(14,2)*(14-2)', u'C(14,2)*12'), ('R.1', 3819816, u'C(56,5)', u'C(14*4,5)')]	|
|4	|C(15,2)*(15-2)*[C(4,2)]^2*4/[C(60,5)]	|((15!/(2!*13!))*13*16*4)/(60!/(5!*55!))	|[('R.0.0.0', 1365.0, u'C(15,2)*(15-2)', u'(15!/(2!*13!))*13'), ('R.1', 5461512, u'C(60,5)', u'60!/(5!*55!)')]	|
|5	|C(10,2)*(10-2)*[C(5,2)]^2*5/[C(50,5)]	|C(10,2)*C(8,1)*C(5,2)*C(3,1)/C(50,5)	|[('R.0.0.0', 360.0, u'C(10,2)*(10-2)', u'C(10,2)*C(8,1)'), ('R.1', 2118760, u'C(50,5)', u'C(50,5)')]	|
|6	|C(15,2)*(15-2)*[C(6,2)]^2*6/[C(90,5)]	|(C(15,2)*C(13,1)*C(6,2)*C(6,1))/C(15*6,5)	|[('R.0.0.0', 1365.0, u'C(15,2)*(15-2)', u'C(15,2)*C(13,1)'), ('R.1', 43949268, u'C(90,5)', u'C(15*6,5)')]	|
|7	|C(13,2)*(13-2)*[C(5,2)]^2*5/[C(65,5)]	|78*11*10*3/8259888	|[('R.0.0.0', 858.0, u'C(13,2)*(13-2)', u'78*11'), ('R.1', 8259888, u'C(65,5)', u'8259888')]	|




### (6) Mistake Group ['R.0', 'R.1.0'] of size 6
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(11,2)*(11-2)*[C(6,2)]^2*6/[C(66,5)]	|C(11,2)*9*6*225/C(66,4)	|[('R.0', 668250.0, u'C(11,2)*(11-2)*[C(6,2)]^2*6', u'C(11,2)*9*6*225'), ('R.1.0', 66.0, u'66', u'66')]	|
|1	|C(16,2)*(16-2)*[C(6,2)]^2*6/[C(96,5)]	|((C(16,2)*(C(6,2)^2))*14*6)/C(96,6)	|[('R.0', 2268000.0, u'C(16,2)*(16-2)*[C(6,2)]^2*6', u'(C(16,2)*(C(6,2)^2))*14*6'), ('R.1.0', 96.0, u'96', u'96')]	|
|2	|C(12,2)*(12-2)*[C(4,2)]^2*4/[C(48,5)]	|(40*((12!)/((2!)*(10!)))*((((4!)/((2!)*(2!))))^2))/(48!)	|[('R.0', 95040.0, u'C(12,2)*(12-2)*[C(4,2)]^2*4', u'40*((12!)/((2!)*(10!)))*((((4!)/((2!)*(2!))))^2)'), ('R.1.0', 48.0, u'48', u'48')]	|
|3	|C(10,2)*(10-2)*[C(4,2)]^2*4/[C(40,5)]	|(C(10,2)*8*C(4,2)^2*4)/C(40,2)	|[('R.0', 51840.0, u'C(10,2)*(10-2)*[C(4,2)]^2*4', u'C(10,2)*8*C(4,2)^2*4'), ('R.1.0', 40.0, u'40', u'40')]	|
|4	|C(13,2)*(13-2)*[C(5,2)]^2*5/[C(65,5)]	|C(13,2)*(13-2)*[C(5,2)]^2*5/[C(5*13,4)]	|[('R.0', 429000.0, u'C(13,2)*(13-2)*[C(5,2)]^2*5', u'C(13,2)*(13-2)*[C(5,2)]^2*5'), ('R.1.0', 65.0, u'65', u'5*13')]	|
|5	|C(15,2)*(15-2)*[C(4,2)]^2*4/[C(60,5)]	|C(15,2)*(15-2)*[C(4,2)]^2*4/[C(60,4)]	|[('R.0', 196560.0, u'C(15,2)*(15-2)*[C(4,2)]^2*4', u'C(15,2)*(15-2)*[C(4,2)]^2*4'), ('R.1.0', 60.0, u'60', u'60')]	|




### (4) Mistake Group Digits of size 4




### (4) Mistake Group ['R.0.0.0.1', 'R.1'] of size 4
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0.1', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(11,2)*(11-2)*[C(5,2)]^2*5/[C(55,5)]	|C(5,2)*11*10*9*8*5^3/C(55,5)	|[('R.0.0.0.1', 9.0, u'11-2', u'9'), ('R.1', 3478761, u'C(55,5)', u'C(55,5)')]	|
|1	|C(12,2)*(12-2)*[C(6,2)]^2*6/[C(72,5)]	|C(12,1)*C(11,1)*C(10,1)*C(4,2)*C(4,1)/C(72,5)	|[('R.0.0.0.1', 10.0, u'12-2', u'C(10,1)'), ('R.1', 13991544, u'C(72,5)', u'C(72,5)')]	|
|2	|C(12,2)*(12-2)*[C(6,2)]^2*6/[C(72,5)]	|C(12,2)*C(6,4)*C(10,1)*C(6,1)*2/C(72,5)	|[('R.0.0.0.1', 10.0, u'12-2', u'C(10,1)'), ('R.1', 13991544, u'C(72,5)', u'C(72,5)')]	|
|3	|C(12,2)*(12-2)*[C(6,2)]^2*6/[C(72,5)]	|C(12,2)*C(6,2)*C(10,1)*C(6,1)*2/C(72,5)	|[('R.0.0.0.1', 10.0, u'12-2', u'C(10,1)'), ('R.1', 13991544, u'C(72,5)', u'C(72,5)')]	|




### (4) Mistake Group ['R.0.0.1'] of size 4
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(10,2)*(10-2)*[C(5,2)]^2*5/[C(50,5)]	|(C(10,2))(C(5,2))^2(5)(8)/500	|[('R.0.0.1', 100.0, u'[C(5,2)]^2', u'(C(5,2))^2')]	|
|1	|C(10,2)*(10-2)*[C(5,2)]^2*5/[C(50,5)]	|(C(10,2))(C(5,2))^2(5)(8)/C(10,5)	|[('R.0.0.1', 100.0, u'[C(5,2)]^2', u'(C(5,2))^2')]	|
|2	|C(11,2)*(11-2)*[C(6,2)]^2*6/[C(66,5)]	|(6!/(2!4!))^2*9*6*11!/(2!9!)*6*((6!/(2!4!))^2)*9*(11!/(2!9!))	|[('R.0.0.1', 225.0, u'[C(6,2)]^2', u'(6!/(2!4!))^2')]	|
|3	|C(11,2)*(11-2)*[C(6,2)]^2*6/[C(66,5)]	|((6!/(2!4!))^2*9*6*11!/(2!9!)*6*((6!/(2!4!))^2)*9*(11!/(2!9!)))	|[('R.0.0.1', 225.0, u'[C(6,2)]^2', u'(6!/(2!4!))^2')]	|




### (4) Mistake Group ['R.0.0.0.0', 'R.1'] of size 4
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(11,2)*(11-2)*[C(6,2)]^2*6/[C(66,5)]	|[C(11,2)*C(6,2)*2*C(58,1)]/C(66,5)	|[('R.0.0.0.0', 55, u'C(11,2)', u'C(11,2)'), ('R.1', 8936928, u'C(66,5)', u'C(66,5)')]	|
|1	|C(13,2)*(13-2)*[C(4,2)]^2*4/[C(52,5)]	|(C(13,2)*C(13,1)*C(4,2)*C(4,1))/C(52,5)	|[('R.0.0.0.0', 78, u'C(13,2)', u'C(13,2)'), ('R.1', 2598960, u'C(52,5)', u'C(52,5)')]	|
|2	|C(14,2)*(14-2)*[C(5,2)]^2*5/[C(70,5)]	|( C(14,2)* C(42, 1)*C(5, 2)*C(5, 1)) / C(5*14, 5)	|[('R.0.0.0.0', 91, u'C(14,2)', u'C(14,2)'), ('R.1', 12103014, u'C(70,5)', u'C(5*14, 5)')]	|
|3	|C(15,2)*(15-2)*[C(4,2)]^2*4/[C(60,5)]	|((15!/(2!*13!))*15*6*4)/(60!/(5!*55!))	|[('R.0.0.0.0', 105, u'C(15,2)', u'15!/(2!*13!)'), ('R.1', 5461512, u'C(60,5)', u'60!/(5!*55!)')]	|




### (3) Mistake Group ['R.0.0', 'R.1'] of size 3
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(14,2)*(14-2)*[C(5,2)]^2*5/[C(70,5)]	|(C(14,2)C(12,1)C(5,2)^2(3))/C(14*5,5)	|[('R.0.0', 109200.0, u'C(14,2)*(14-2)*[C(5,2)]^2', u'C(14,2)C(12,1)C(5,2)^2'), ('R.1', 12103014, u'C(70,5)', u'C(14*5,5)')]	|
|1	|C(10,2)*(10-2)*[C(6,2)]^2*6/[C(60,5)]	|(C(10,2)*8*C(6,2)**2*4)/C(60,5)	|[('R.0.0', 81000.0, u'C(10,2)*(10-2)*[C(6,2)]^2', u'C(10,2)*8*C(6,2)**2'), ('R.1', 5461512, u'C(60,5)', u'C(60,5)')]	|
|2	|C(15,2)*(15-2)*[C(5,2)]^2*5/[C(75,5)]	|C(15,2)*13*(C(5,2)^2)*4/C(5*15,5)	|[('R.0.0', 136500.0, u'C(15,2)*(15-2)*[C(5,2)]^2', u'C(15,2)*13*(C(5,2)^2)'), ('R.1', 17259390, u'C(75,5)', u'C(5*15,5)')]	|




### (3) Mistake Group ['R.0', 'R.1.1'] of size 3
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(15,2)*(15-2)*[C(4,2)]^2*4/[C(60,5)]	|(C(15,2)*13*C(4,2)*C(4,2)*4)/(C(15,5))	|[('R.0', 196560.0, u'C(15,2)*(15-2)*[C(4,2)]^2*4', u'C(15,2)*13*C(4,2)*C(4,2)*4'), ('R.1.1', 5.0, u'5', u'5')]	|
|1	|C(15,2)*(15-2)*[C(4,2)]^2*4/[C(60,5)]	|C(15, 2)*C(4, 2)*C(4, 2)*C(13, 1)*C(4, 1)/C(15, 5)	|[('R.0', 196560.0, u'C(15,2)*(15-2)*[C(4,2)]^2*4', u'C(15, 2)*C(4, 2)*C(4, 2)*C(13, 1)*C(4, 1)'), ('R.1.1', 5.0, u'5', u'5')]	|
|2	|C(15,2)*(15-2)*[C(6,2)]^2*6/[C(90,5)]	|(C(15,2)*(15-2)*[C(6,2)]^2*6)/(C(96,5))	|[('R.0', 1842750.0, u'C(15,2)*(15-2)*[C(6,2)]^2*6', u'C(15,2)*(15-2)*[C(6,2)]^2*6'), ('R.1.1', 5.0, u'5', u'5')]	|




### (2) Mistake Group ['R.0', 'R.1.0', 'R.1.1'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1.0', 'R.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(12,2)*(12-2)*[C(4,2)]^2*4/[C(48,5)]	|40*66*36/(48^5)	|[('R.0', 95040.0, u'C(12,2)*(12-2)*[C(4,2)]^2*4', u'40*66*36'), ('R.1.0', 48.0, u'48', u'48'), ('R.1.1', 5.0, u'5', u'5')]	|
|1	|C(10,2)*(10-2)*[C(6,2)]^2*6/[C(60,5)]	|(C(10,2)*C(8,1)*C(6,2)*C(6,2)*C(6,1))/(60^5)	|[('R.0', 486000.0, u'C(10,2)*(10-2)*[C(6,2)]^2*6', u'C(10,2)*C(8,1)*C(6,2)*C(6,2)*C(6,1)'), ('R.1.0', 60.0, u'60', u'60'), ('R.1.1', 5.0, u'5', u'5')]	|




### (2) Mistake Group ['R.0.0.1', 'R.1'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.1', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(10,2)*(10-2)*[C(4,2)]^2*4/[C(40,5)]	|(4*10*(C(4,2))^2*C(10,2))/(C(40,5))	|[('R.0.0.1', 36.0, u'[C(4,2)]^2', u'(C(4,2))^2'), ('R.1', 658008, u'C(40,5)', u'C(40,5)')]	|
|1	|C(13,2)*(13-2)*[C(6,2)]^2*6/[C(78,5)]	|C(13,2)*6*C(6,2)^2*6/C(78,5)	|[('R.0.0.1', 225.0, u'[C(6,2)]^2', u'C(6,2)^2'), ('R.1', 21111090, u'C(78,5)', u'C(78,5)')]	|




### (2) Mistake Group ['R.0.0.0.0', 'R.0.0.0.1', 'R.1'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0.0', 'R.0.0.0.1', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(12,2)*(12-2)*[C(6,2)]^2*6/[C(72,5)]	|C(12,2)*C(4,4)*C(10,1)*C(4,4)*2/C(72,5)	|[('R.0.0.0.0', 66, u'C(12,2)', u'C(12,2)*C(4,4)'), ('R.0.0.0.1', 10.0, u'12-2', u'C(10,1)'), ('R.1', 13991544, u'C(72,5)', u'C(72,5)')]	|
|1	|C(12,2)*(12-2)*[C(6,2)]^2*6/[C(72,5)]	|C(12,2)*C(6,6)*C(10,1)*C(6,6)*2/C(72,5)	|[('R.0.0.0.0', 66, u'C(12,2)', u'C(12,2)*C(6,6)'), ('R.0.0.0.1', 10.0, u'12-2', u'C(10,1)'), ('R.1', 13991544, u'C(72,5)', u'C(72,5)')]	|




### (2) Mistake Group ['R.0.0.0.0', 'R.0.0.1', 'R.1'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0.0', 'R.0.0.1', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(15,2)*(15-2)*[C(5,2)]^2*5/[C(75,5)]	|[C(15,2)*12*(C(5,2)^2)*5]/[C(15*5,5)]	|[('R.0.0.0.0', 105, u'C(15,2)', u'C(15,2)'), ('R.0.0.1', 100.0, u'[C(5,2)]^2', u'C(5,2)^2'), ('R.1', 17259390, u'C(75,5)', u'C(15*5,5)')]	|
|1	|C(15,2)*(15-2)*[C(4,2)]^2*4/[C(60,5)]	|105*12*36*4/5461512	|[('R.0.0.0.0', 105, u'C(15,2)', u'105'), ('R.0.0.1', 36.0, u'[C(4,2)]^2', u'36'), ('R.1', 5461512, u'C(60,5)', u'5461512')]	|




### (1) Mistake Group ['R.0.0.0.1.0', 'R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0.1.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(11,2)*(11-2)*[C(4,2)]^2*4/[C(44,5)]	|C(4,2)*C(11,2)*9*4 / C(44,5)	|[('R.0.0.0.1.0', 11.0, u'11', u'11'), ('R.1', 1086008, u'C(44,5)', u'C(44,5)')]	|




### (1) Mistake Group ['R.0.0.0.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(12,2)*(12-2)*[C(6,2)]^2*6/[C(72,5)]	|12*10*6*6/(72!/5!(72-5)!)	|[('R.0.0.0.1', 10.0, u'12-2', u'10')]	|




### (1) Mistake Group ['R.0.0.0.0'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(13,2)*(13-2)*[C(6,2)]^2*6/[C(78,5)]	|C(13,2)*C(6,2)*C(6,1)*C(11,1) / (78*77*76*75*74)	|[('R.0.0.0.0', 78, u'C(13,2)', u'C(13,2)')]	|




### (1) Mistake Group ['R.0.0.0.1', 'R.0.0.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0.1', 'R.0.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(12,2)*(12-2)*[C(6,2)]^2*6/[C(72,5)]	|6*10*12!/(2!(10!))*10*((6!/(2!(4!)))^2)*6/(72!/5!(72-5)!)	|[('R.0.0.0.1', 10.0, u'12-2', u'10'), ('R.0.0.1', 225.0, u'[C(6,2)]^2', u'(6!/(2!(4!)))^2')]	|




### (12) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:h4tu

	first_attempt
					2015-10-15 07:32:14
	part1_correct_attempt
					['0:00:00', u'(16*15/2)']
	part2_correct_attempt
					['0:01:09', u'14']
	part3_correct_attempt
					['0:03:23', u'(6*5/2)^2']
	part4_correct_attempt
					['0:03:48', u'6']
	part5_correct_attempt
					['0:04:12', u'(16*15/2)*14*(6*5/2)^2*6']
	part6_incorrect_attempt
					('0:04:25', u'(16*15/2)*14*(6*5/2)^2*6')
					('0:04:54', u'(16*15/2)*14*(6*5/2)^2*6/96!/(91!5!)')
	part6_correct_attempt
					['0:05:22', u'(16*15/2)*14*(6*5/2)^2*6/(96!/(91!5!))']

1 Student ID:jtfrankl

	first_attempt
					2015-10-15 21:10:30
	part1_correct_attempt
					['0:00:00', u'C(12,2)']
	part2_correct_attempt
					['0:02:04', u'10']
	part3_correct_attempt
					['0:15:27', u'C(6,2)**2']
	part4_correct_attempt
					['0:07:12', u'6']
	part5_correct_attempt
					['0:16:00', u'C(12,2)10C(6,2)^2*6']
	part6_incorrect_attempt
					('0:16:17', u'C(12,2)10C(6,2)^2*6')
	part6_correct_attempt
					['0:18:44', u'(C(12,2)10C(6,2)^2*6)/(C(72,5))']

2 Student ID:tak068

	first_attempt
					2015-10-14 07:31:50
	part1_correct_attempt
					['0:00:00', u'C(10,2)']
	part2_correct_attempt
					['0:01:46', u'C(8,1)']
	part3_correct_attempt
					['0:03:54', u'C(6,2)^2']
	part4_correct_attempt
					['0:03:38', u'C(6,1)']
	part5_correct_attempt
					['0:04:24', u'C(6,1)C(6,2)^2C(10,2)C(8,1)']
	part6_incorrect_attempt
					('0:04:45', u'C(6,1)(C(6,2))2C(10,2)C(8,1)/C(60,5)')
	part6_correct_attempt
					['0:05:01', u'486000/C(60,5)']

3 Student ID:achava

	first_attempt
					2015-10-13 08:08:08
	part1_correct_attempt
					['0:00:00', u'C(10,2)']
	part2_correct_attempt
					['0:07:57', u'C(8,1)']
	part3_correct_attempt
					['1 day, 11:02:06', u'C(6,2) * C(6,2)']
	part4_correct_attempt
					['1 day, 11:03:23', u'C(6,1)']
	part5_correct_attempt
					['1 day, 11:04:17', u'C(10,2)* C(8,1) * C(6,2) * C(6,2) * C(6,1)']
	part6_incorrect_attempt
					('1 day, 11:04:58', u'C(60, 5)')
	part6_correct_attempt
					['1 day, 11:05:07', u'486000 /C(60, 5)']

4 Student ID:c3chung

	first_attempt
					2015-10-15 23:00:44
	part6_incorrect_attempt
					('0:00:00', u'5^5')
					('0:00:00', u'C(75,5)')

5 Student ID:rlhagen

	first_attempt
					2015-10-11 18:43:20
	part1_correct_attempt
					['0:00:00', u'12!/(2!(12-2)!)']
	part2_correct_attempt
					['0:03:57', u'10']
	part3_correct_attempt
					['0:03:32', u'(6!/(2!(6-2)!))^2']
	part4_correct_attempt
					['0:03:15', u'6']
	part5_correct_attempt
					['0:05:02', u'12!/(2!(12-2)!)*10*(6!/(2!(6-2)!))^2*6']
	part6_incorrect_attempt
					('0:05:02', u'(12!/(2!(12-2)!)*10*(6!/(2!(6-2)!))^2*6)/12!/(2!(12-2)!)')
					('0:05:54', u'((12!/(2!(12-2)!)*10*(6!/(2!(6-2)!))^2*6)/12!/(72!)/(5!(72-5)!))')
	part6_correct_attempt
					['0:06:20', u'(12!/(2!(12-2)!)*10*(6!/(2!(6-2)!))^2*6)/(72!/(5!(72-5)!))']

6 Student ID:krau

	first_attempt
					2015-10-14 04:07:44
	part1_correct_attempt
					['0:00:00', u'16!/2!/14!']
	part2_correct_attempt
					['-1 day, 23:58:27', u'14']
	part3_correct_attempt
					['0:01:18', u'36']
	part4_correct_attempt
					['0:01:43', u'4']
	part5_correct_attempt
					['0:02:34', u'16!/2!/14!*14*36*4']
	part6_incorrect_attempt
					('0:02:34', u'16!/2!/14!*14*36*4 / 64!/59!/4!')
	part6_correct_attempt
					['0:03:04', u'(16!/2!/14!*14*36*4) / (64!/59!/5!)']

7 Student ID:aadhakal

	first_attempt
					2015-10-14 05:08:24
	part1_correct_attempt
					['0:00:00', u'C(14,2)']
	part2_correct_attempt
					['0:02:34', u'12']
	part3_correct_attempt
					['0:02:34', u'(C(6,2))^2']
	part4_correct_attempt
					['0:03:48', u'6']
	part5_correct_attempt
					['0:07:02', u'C(14,2)*12*[C(6,2)]^2*6']
	part6_incorrect_attempt
					('0:07:49', u'C(14,2)*12*[C(6,2)]^2*6/84!/(5!*(84-5)!)')
	part6_correct_attempt
					['0:08:14', u'C(14,2)*12*[C(6,2)]^2*6/(84!/(5!*(84-5)!))']

8 Student ID:twsalim

	first_attempt
					2015-10-12 00:10:41
	part1_correct_attempt
					['0:00:00', u'105']
	part2_correct_attempt
					['0:05:34', u'13']
	part3_correct_attempt
					['0:18:06', u'100']
	part4_correct_attempt
					['0:05:34', u'5']
	part5_correct_attempt
					['0:18:06', u'682500']
	part6_incorrect_attempt
					('0:18:06', u'0.0395')
	part6_correct_attempt
					['0:19:22', u'0.039543692']

9 Student ID:pvl001

	first_attempt
					2015-10-13 19:50:31
	part1_correct_attempt
					['0:00:00', u'78']
	part2_correct_attempt
					['0:00:22', u'11']
	part3_correct_attempt
					['0:02:52', u'10 * 10']
	part4_correct_attempt
					['0:03:01', u'5']
	part5_correct_attempt
					['0:03:13', u'78 * 11 * 10 * 10 * 5']
	part6_incorrect_attempt
					('0:03:37', u'5 * (13 * 12 * 11 * 10 * 9)')
					('0:04:15', u'65! / (5! * 60!)')
	part6_correct_attempt
					['0:04:37', u'78 * 11 * 10 * 10 * 5 / (65! / (5! * 60!))']

10 Student ID:k3tan

	first_attempt
					2015-10-13 06:21:53
	part1_correct_attempt
					['0:00:00', u'(15*14)/2!']
	part3_correct_attempt
					['0:13:22', u'36']
	part4_correct_attempt
					['0:13:32', u'4']
	part5_correct_attempt
					['0:24:09', u'(15*14*13*6*6*4)/2']
	part6_incorrect_attempt
					('0:24:56', u'(60!/(5!(60-5)!))')
	part6_correct_attempt
					['0:25:06', u'196560/(60!/(5!(60-5)!))']

11 Student ID:jcj006

	first_attempt
					2015-10-14 00:13:59
	part1_correct_attempt
					['0:00:00', u'16!/(2*14!)']
	part2_correct_attempt
					['0:03:20', u'14']
	part3_correct_attempt
					['0:07:56', u'(6!/(2!4!))^2']
	part4_correct_attempt
					['0:00:00', u'6']
	part5_correct_attempt
					['0:09:16', u'6*14*(6!/(2!4!))^2*(16!/(2*14!))']
	part6_incorrect_attempt
					('0:09:16', u'6*14*(6!/(2!4!))^2*(16!/(2*14!))/(6*16)!/(5!(6*16-5)!)')
	part6_correct_attempt
					['0:10:23', u'6*14*(6!/(2!4!))^2*(16!/(2*14!))/((6*16)!/(5!(6*16-5)!))']












