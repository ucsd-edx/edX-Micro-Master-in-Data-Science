#Problem 15

    $ns = random(4,6,1);
    $nr = random(10,16,1);
    $n = $ns*$nr;

    ### Full House: 2 of one rank and 3 of another rank ###
    *Remember, the deck you are using has [$ns] suits and [$nr] ranks.*

    1. The number of possibilities for the rank of the triple is [______]{$nr}.

    2. Given the rank of the triple, the number of possibilities for the rank of the pair is [______]{$nr-1}.

    2. The number of possibilities for the suit of the triple is [_____]{Compute("C($ns,3)")}.

    3. The number of possibilities for the suit of the pair is [_____]{Compute("C($ns,2)")}.

    4. Thus the number of hands that is a full house is [______]{Compute("$nr*($nr-1)*C($ns,3)*C($ns,2)")}.

    5. The ratio of this number to the number of all hands [______]{Compute("$nr*($nr-1)*C($ns,3)*C($ns,2)/C($n,5)")}.


## Part 1

### (45) Mistake Group Digits of size 45




### (3) Mistake Group Fraction of size 3




### (53) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:hmshah

	first_attempt
					2015-10-14 09:05:41
	part1_incorrect_attempt
					('0:00:00', u'C(13,2)')
					('0:00:28', u'C(13,2)')
					('0:00:36', u'C(13,2)')
					('0:00:44', u'C(13,2)')
	part1_correct_attempt
					['0:02:37', u'C(13,1)']

1 Student ID:jag028

	first_attempt
					2015-10-15 14:05:23
	part1_incorrect_attempt
					('0:00:00', u'4*C(13,3)')
					('0:00:10', u'3*C(13,2)')
					('0:00:37', u'C(13,3)')
					('0:00:59', u'C(52,3)')
					('0:01:07', u'4*C(52,3)')
					('0:01:40', u'C(52,13)')
					('0:04:08', u'C(13,1)C(4,3)C(12,1)C(4,2)')
					('0:04:22', u'C(13,1)C(4,3)')
					('0:05:06', u'C(13,1)C(4,1)')
					('0:05:57', u'C(13,3)C(4,1)')
					('0:07:00', u'C(13,1)C(4,3)')
					('0:07:12', u'C(13,1)*C(4,3)')
					('0:08:04', u'C(13,1)*C(4,3)C(12,1)C(4,2)')
					('0:00:00', u'C(13,3)')
	part1_correct_attempt
					['7:10:16', u'C(13,1)']

2 Student ID:lywong

	first_attempt
					2015-10-13 00:56:12
	part1_incorrect_attempt
					('0:00:00', u'11!/3!(11-9)!')
					('0:00:08', u'11!/(3!(11-9)!)')
	part1_correct_attempt
					['0:00:32', u'11']

3 Student ID:hkhodada

	first_attempt
					2015-10-10 23:47:33
	part1_incorrect_attempt
					('0:00:00', u'C(4,3)')
					('0:00:00', u'4*C(14,3)')
	part1_correct_attempt
					['1 day, 1:20:38', u'14']

4 Student ID:abasu

	first_attempt
					2015-10-11 03:04:26
	part1_incorrect_attempt
					('0:00:00', u'C(13,1)')
					('0:00:00', u'C(13,2)')
	part1_correct_attempt
					['0:00:33', u'C(15,1)']

5 Student ID:achava

	first_attempt
					2015-10-13 20:05:12
	part1_incorrect_attempt
					('0:00:00', u'C(13, 3)')
					('0:00:32', u'C(10, 3)')
					('0:00:47', u'C(10, 3)*6')
					('0:00:00', u'C(10, 3)^6')
					('0:00:26', u'C(10,3)')
	part1_correct_attempt
					['23:24:19', u'C(10,1)']

6 Student ID:msaguiar

	first_attempt
					2015-10-13 04:28:58
	part1_incorrect_attempt
					('0:00:00', u'C(12,3)')
	part1_correct_attempt
					['0:00:51', u'12']

7 Student ID:spw006

	first_attempt
					2015-10-13 23:05:31
	part1_incorrect_attempt
					('0:00:00', u'5^3')
	part1_correct_attempt
					['0:02:11', u'10']

8 Student ID:cprafull

	first_attempt
					2015-10-14 08:38:07
	part1_incorrect_attempt
					('0:00:00', u'(84!)/((81!)(3!))')
	part1_correct_attempt
					['13:56:26', u'14']

9 Student ID:pcdo

	first_attempt
					2015-10-13 20:41:48
	part1_incorrect_attempt
					('0:00:00', u'C(5*16, 3)')
	part1_correct_attempt
					['0:00:21', u'16']

10 Student ID:anl114

	first_attempt
					2015-10-15 08:39:27
	part1_incorrect_attempt
					('0:00:00', u'12 * 6^3')
	part1_correct_attempt
					['0:00:26', u'12']

11 Student ID:ctgraves

	first_attempt
					2015-10-15 05:06:04
	part1_incorrect_attempt
					('0:00:00', u'11!/(3!*8!)')
	part1_correct_attempt
					['0:00:51', u'11']

12 Student ID:jdeon

	first_attempt
					2015-10-11 23:40:06
	part1_incorrect_attempt
					('0:00:00', u'C(11,3)')
	part1_correct_attempt
					['0:00:16', u'11']

13 Student ID:dlt009

	first_attempt
					2015-10-14 02:26:11
	part1_incorrect_attempt
					('0:00:00', u'15!/[(15-3)!3!]')
	part1_correct_attempt
					['0:01:30', u'15']

14 Student ID:mbl003

	first_attempt
					2015-10-15 07:34:06
	part1_incorrect_attempt
					('0:00:00', u'C(16,3)')
	part1_correct_attempt
					['0:00:47', u'C(16,1)']

15 Student ID:p4kumar

	first_attempt
					2015-10-15 09:38:00
	part1_incorrect_attempt
					('0:00:00', u'C(14, 3)')
					('0:00:05', u'C(15, 3)')
					('0:00:29', u'C(14, 3)')
					('0:50:55', u'14 * 4')
					('0:51:58', u'14 * 3')
					('0:52:25', u'15 * 3')
					('0:53:25', u'15 * 4')
	part1_correct_attempt
					['0:53:31', u'15']

16 Student ID:jmiclat

	first_attempt
					2015-10-15 19:05:54
	part1_incorrect_attempt
					('0:00:00', u'11!/(3!8!)')
	part1_correct_attempt
					['0:00:47', u'11']

17 Student ID:yypan

	first_attempt
					2015-10-12 21:07:13
	part1_incorrect_attempt
					('0:00:00', u'C(13,1)')
	part1_correct_attempt
					['0:00:07', u'C(12,1)']

18 Student ID:jhc010

	first_attempt
					2015-10-15 16:30:46
	part1_incorrect_attempt
					('0:00:00', u'C(6,3)')
	part1_correct_attempt
					['0:00:19', u'10']

19 Student ID:cfgutier

	first_attempt
					2015-10-15 22:50:45
	part1_incorrect_attempt
					('0:00:00', u'14!/11!/3!')
	part1_correct_attempt
					['0:04:33', u'14']

20 Student ID:t2shin

	first_attempt
					2015-10-15 17:39:02
	part1_incorrect_attempt
					('0:00:00', u'11!(3!8!)')
					('0:00:06', u'11!/(3!8!)')
	part1_correct_attempt
					['5:44:01', u'11']

21 Student ID:jcj006

	first_attempt
					2015-10-14 00:36:34
	part1_incorrect_attempt
					('0:00:00', u'16!/(6*13!)')
	part1_correct_attempt
					['0:03:03', u'16']

22 Student ID:ajvanega

	first_attempt
					2015-10-14 22:55:57
	part1_incorrect_attempt
					('0:00:00', u'16!/(13!3!)')
	part1_correct_attempt
					['0:00:09', u'16']

23 Student ID:akhmelni

	first_attempt
					2015-10-15 23:27:37
	part1_incorrect_attempt
					('0:00:00', u'C(12,2)')
					('0:00:46', u'12*11')
	part1_correct_attempt
					['0:02:23', u'12']

24 Student ID:kalang

	first_attempt
					2015-10-15 23:23:43
	part1_incorrect_attempt
					('0:00:00', u'16-2')
					('0:00:29', u'16-3')
	part1_correct_attempt
					['0:00:43', u'16']

25 Student ID:jcl084

	first_attempt
					2015-10-13 21:06:18
	part1_incorrect_attempt
					('0:00:00', u'C(10,3)')
	part1_correct_attempt
					['0:01:41', u'10']

26 Student ID:vsosnovs

	first_attempt
					2015-10-15 06:02:03
	part1_incorrect_attempt
					('0:00:00', u'C(14,3)')
					('0:20:50', u'C(6,1)')
					('0:21:56', u'C(14,2)C(13,3)')
					('0:22:03', u'C(14,2)*C(13,3)')
					('0:42:04', u'C(14,1)C(6,3)')
					('0:43:51', u'C(14,1)C(6,3)C(13,2)C(6,2)')
					('0:44:05', u'C(14,1)C(6,3)C(13,1)C(6,2)')
					('0:45:28', u'C(14,3)')
					('0:45:38', u'C(14,3)C(6,1)')
	part1_correct_attempt
					['0:46:00', u'C(14,1)']

27 Student ID:aakumar

	first_attempt
					2015-10-11 03:04:26
	part1_incorrect_attempt
					('0:00:00', u'13*12')
					('0:00:00', u'C(13,2)')
	part1_correct_attempt
					['0:00:48', u'C(13,1)']

28 Student ID:jhw015

	first_attempt
					2015-10-15 03:11:16
	part1_incorrect_attempt
					('0:00:00', u'C(5,3)')
					('0:00:40', u'C(5,3)')
					('0:00:40', u'C(5,3)')
	part1_correct_attempt
					['0:00:57', u'12']

29 Student ID:aggouw

	first_attempt
					2015-10-15 08:02:51
	part1_incorrect_attempt
					('0:00:00', u'(15)*(4!/3!)')

30 Student ID:tcn013

	first_attempt
					2015-10-15 04:27:33
	part1_incorrect_attempt
					('0:00:00', u'C(16,3)')
	part1_correct_attempt
					['0:00:25', u'16']

31 Student ID:flhernan

	first_attempt
					2015-10-14 22:19:03
	part1_incorrect_attempt
					('0:00:00', u'C(10,3)')
	part1_correct_attempt
					['0:00:15', u'C(10,1)']

32 Student ID:ajabasa

	first_attempt
					2015-10-14 18:24:41
	part1_incorrect_attempt
					('0:00:00', u'13*12*11')
	part1_correct_attempt
					['0:00:41', u'13']

33 Student ID:jel075

	first_attempt
					2015-10-15 04:47:11
	part1_incorrect_attempt
					('0:00:00', u'12!/(7!*3!)')
					('0:00:14', u'12!/(3!*9!)')
	part1_correct_attempt
					['0:04:54', u'12!/11!']

34 Student ID:aysee

	first_attempt
					2015-10-13 23:20:52
	part1_incorrect_attempt
					('0:00:00', u'C(13,3)')
	part1_correct_attempt
					['0:01:16', u'C(13,1)']

35 Student ID:mcatozzi

	first_attempt
					2015-10-14 01:20:39
	part1_incorrect_attempt
					('0:00:00', u'C(55,3)')
	part1_correct_attempt
					['0:01:27', u'C(11,1)']

36 Student ID:asetters

	first_attempt
					2015-10-12 06:51:21
	part1_incorrect_attempt
					('0:00:00', u'C(4,3)')
	part1_correct_attempt
					['0:01:30', u'11']

37 Student ID:anvan

	first_attempt
					2015-10-15 00:08:56
	part1_incorrect_attempt
					('0:00:00', u'13!(10!3!)')
					('0:00:10', u'13!/(10!3!)')
	part1_correct_attempt
					['1:21:01', u'14']

38 Student ID:smohiman

	first_attempt
					2015-10-11 22:56:13
	part1_incorrect_attempt
					('0:00:00', u'C(96,5)*6^3')
					('0:01:29', u'C(16,3)')
					('0:03:05', u'C(6,3)*C(16,1)')
	part1_correct_attempt
					['0:08:29', u'C(16,1)']

39 Student ID:c1sorian

	first_attempt
					2015-10-14 22:30:27
	part1_incorrect_attempt
					('0:00:00', u'12!/(3!9!)')
	part1_correct_attempt
					['0:00:13', u'12']

40 Student ID:dtea

	first_attempt
					2015-10-15 23:46:17
	part1_incorrect_attempt
					('0:00:00', u'C(14,3)')
	part1_correct_attempt
					['0:00:12', u'14']

41 Student ID:a2ahmed

	first_attempt
					2015-10-15 22:30:50
	part1_incorrect_attempt
					('0:00:00', u'C(14,3)')
					('0:00:23', u'C(15,3)')
	part1_correct_attempt
					['0:00:34', u'15']

42 Student ID:c1wei

	first_attempt
					2015-10-14 21:02:01
	part1_incorrect_attempt
					('0:00:00', u'15*14')
	part1_correct_attempt
					['0:00:31', u'15']

43 Student ID:azkong

	first_attempt
					2015-10-15 18:22:31
	part1_incorrect_attempt
					('0:00:00', u'C(15, 3)')
	part1_correct_attempt
					['0:01:21', u'C(15, 1)']

44 Student ID:mitopete

	first_attempt
					2015-10-13 23:23:35
	part1_incorrect_attempt
					('0:00:00', u'11!/(3!8!)')
					('0:00:00', u'11!/(3!8!)*2')
					('0:00:46', u'11!/(3!8!)*10!/(2!8!)')
					('0:01:02', u'11!/(3!8!)*(10!/(2!8!))')
					('0:01:15', u'11!/(3!8!)+(10!/(2!8!))')
					('0:00:00', u'11!/(3!8!)')
	part1_correct_attempt
					['17:48:58', u'11']

45 Student ID:vasharma

	first_attempt
					2015-10-11 06:42:25
	part1_incorrect_attempt
					('0:00:00', u'C(6,1)')
					('0:00:08', u'C(6,1)C(6,1)C(6,1)')
					('0:02:29', u'6^3')
					('0:03:14', u'C(11,1)*3')
					('0:03:20', u'C(11,3)')
					('0:04:25', u'C(6,1)^3')
					('0:04:35', u'C(6,1)')
					('0:04:53', u'C(6,3)')
					('0:05:03', u'C(6,3)')
					('0:05:24', u'C(11,2)')
					('0:06:01', u'C(11,2)')
					('0:06:27', u'C(11,3)')
					('0:06:48', u'11*C(11,3)')
					('0:07:02', u'C(11,3)')
	part1_correct_attempt
					['0:07:46', u'11']

46 Student ID:tak068

	first_attempt
					2015-10-14 08:12:57
	part1_incorrect_attempt
					('0:00:00', u'C(10,1)C(6,3)')
	part1_correct_attempt
					['0:00:22', u'C(10,1)']

47 Student ID:c3chung

	first_attempt
					2015-10-15 23:34:19
	part1_incorrect_attempt
					('0:00:00', u'C(15,1)C(5,3)C(14,2)C(5,2)')

48 Student ID:xweng

	first_attempt
					2015-10-13 02:23:54
	part1_incorrect_attempt
					('0:00:00', u'C(16,1)C(4,3)')
	part1_correct_attempt
					['0:00:18', u'16']

49 Student ID:zig006

	first_attempt
					2015-10-12 23:36:06
	part1_incorrect_attempt
					('0:00:00', u'5!(2!3!)')
					('0:00:51', u'16!(3!13!)')
	part1_correct_attempt
					['0:01:29', u'16']

50 Student ID:mjethani

	first_attempt
					2015-10-15 02:44:50
	part1_incorrect_attempt
					('0:00:00', u'13!/((3!)(10!))')
	part1_correct_attempt
					['12:15:54', u'13']

51 Student ID:k3tan

	first_attempt
					2015-10-13 16:10:42
	part1_incorrect_attempt
					('0:00:00', u'(15*14)/2!')
					('0:00:15', u'(15*14)/3!')
	part1_correct_attempt
					['0:00:44', u'15']

52 Student ID:asp025

	first_attempt
					2015-10-15 08:02:12
	part1_incorrect_attempt
					('0:00:00', u'15!/(3!(15-3)!)')
	part1_correct_attempt
					['0:03:24', u'15']












## Part 2

### (24) Mistake Group redirect of size 24




### (21) Mistake Group Digits of size 21




### (11) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:t2li

	first_attempt
					2015-10-14 07:17:11
	part1_correct_attempt
					['0:00:00', u'14']
	part2_incorrect_attempt
					('0:00:36', u'C(13,2)')
	part2_correct_attempt
					['0:00:59', u'13']

1 Student ID:hmshah

	first_attempt
					2015-10-14 09:08:18
	part1_correct_attempt
					['0:00:00', u'C(13,1)']
	part2_incorrect_attempt
					('0:00:14', u'C(12,2)')
	part2_correct_attempt
					['0:00:18', u'C(12,1)']

2 Student ID:daw023

	first_attempt
					2015-10-15 06:10:02
	part1_correct_attempt
					['0:00:00', u'C(15,1)']
	part2_incorrect_attempt
					('0:00:00', u'C(14,2)')
	part2_correct_attempt
					['0:01:27', u'C(14,1)']

3 Student ID:s2chaudh

	first_attempt
					2015-10-13 20:04:02
	part1_correct_attempt
					['0:00:00', u'C(14,1)']
	part2_incorrect_attempt
					('0:00:00', u'C(11,1)')
	part2_correct_attempt
					['0:00:30', u'C(13,1)']

4 Student ID:jew037

	first_attempt
					2015-10-14 04:36:33
	part1_correct_attempt
					['0:00:00', u'10']
	part2_incorrect_attempt
					('0:00:00', u'C(10-1, 2)')
					('0:00:54', u'6^2')
	part2_correct_attempt
					['0:02:03', u'10-1']

5 Student ID:tak068

	first_attempt
					2015-10-14 08:13:19
	part1_correct_attempt
					['0:00:00', u'C(10,1)']
	part2_incorrect_attempt
					('0:00:18', u'C(6,3)')
					('0:01:39', u'C(9,3)')
					('0:01:46', u'C(7,3)')
					('0:05:10', u'C(9,3)')
					('0:05:48', u'C(7,1)')
					('0:06:02', u'C(7,2)')
					('0:06:08', u'C(7,1)^2')
	part2_correct_attempt
					['0:06:45', u'C(9,1)']

6 Student ID:jel075

	first_attempt
					2015-10-15 04:52:05
	part1_correct_attempt
					['0:00:00', u'12!/11!']
	part2_incorrect_attempt
					('0:00:00', u'12!/11!')
	part2_correct_attempt
					['0:00:09', u'11!/10!']

7 Student ID:vsosnovs

	first_attempt
					2015-10-15 06:48:03
	part1_correct_attempt
					['0:00:00', u'C(14,1)']
	part2_incorrect_attempt
					('0:00:32', u'C(6,3)')
					('0:00:48', u'C(14,1)C(6,3)')
					('0:02:46', u'C(6,2)')
					('0:02:51', u'C(6,3)')
	part2_correct_attempt
					['0:03:29', u'C(13,1)']

8 Student ID:etemlock

	first_attempt
					2015-10-11 01:44:52
	part1_correct_attempt
					['0:00:00', u'C(13,1)']
	part2_incorrect_attempt
					('0:00:00', u'C(12,2)')
	part2_correct_attempt
					['0:00:06', u'C(12,1)']

9 Student ID:achava

	first_attempt
					2015-10-14 19:29:31
	part1_correct_attempt
					['0:00:00', u'C(10,1)']
	part2_incorrect_attempt
					('0:00:24', u'C(10,1)')
	part2_correct_attempt
					['0:04:23', u'C(9,1)']

10 Student ID:cprafull

	first_attempt
					2015-10-14 22:34:33
	part1_correct_attempt
					['0:00:00', u'14']
	part2_incorrect_attempt
					('0:00:19', u'6!/((3!)(3!))')
					('0:00:38', u'13!/((2!)(11!))')
	part2_correct_attempt
					['0:00:54', u'13!/((1!)(12!))']












## Part 3

### (105) Mistake Group Digits of size 105




### (24) Mistake Group ['R.1'] of size 24
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(6,3)	|C(6,3)^3	|[('R.1', 3.0, u'3', u'3')]	|
|1	|C(5,3)	|5*4*3	|[('R.1', 3.0, u'3', u'3')]	|
|2	|C(6,3)	|C(4,3)	|[('R.1', 3.0, u'3', u'3')]	|
|3	|C(6,3)	|P(4,3)	|[('R.1', 3.0, u'3', u'3')]	|
|4	|C(6,3)	|4**3	|[('R.1', 3.0, u'3', u'3')]	|
|5	|C(6,3)	|C(15,3)	|[('R.1', 3.0, u'3', u'3')]	|
|6	|C(5,3)	|(5!/(3!2!))^3	|[('R.1', 3.0, u'3', u'3')]	|
|7	|C(5,3)	|C(12,3)	|[('R.1', 3.0, u'3', u'3')]	|
|8	|C(5,3)	|C(16, 3)	|[('R.1', 3.0, u'3', u'3')]	|
|9	|C(4,3)	|4^4 -3	|[('R.1', 3.0, u'3', u'3')]	|
|10	|C(5,3)	|4^3	|[('R.1', 3.0, u'3', u'3')]	|
|11	|C(6,3)	|20^3	|[('R.1', 3.0, u'3', u'3')]	|
|12	|C(5,3)	|C(5,3)^3	|[('R.1', 3.0, u'3', u'3')]	|




### (14) Mistake Group ['R.0', 'R.1'] of size 14
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(5,3)	|C(5,1)^3	|[('R.0', 5.0, u'5', u'C(5,1)'), ('R.1', 3.0, u'3', u'3')]	|
|1	|C(6,3)	|6^3	|[('R.0', 6.0, u'6', u'6'), ('R.1', 3.0, u'3', u'3')]	|
|2	|C(5,3)	|5^3	|[('R.0', 5.0, u'5', u'5'), ('R.1', 3.0, u'3', u'3')]	|
|3	|C(6,3)	|C(6,1)^3	|[('R.0', 6.0, u'6', u'C(6,1)'), ('R.1', 3.0, u'3', u'3')]	|
|4	|C(4,3)	|4^3	|[('R.0', 4.0, u'4', u'4'), ('R.1', 3.0, u'3', u'3')]	|
|5	|C(4,3)	|(C(4, 1))^3	|[('R.0', 4.0, u'4', u'C(4, 1)'), ('R.1', 3.0, u'3', u'3')]	|




### (3) Mistake Group ['R.0'] of size 3
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(6,3)	|6*5	|[('R.0', 6.0, u'6', u'6')]	|
|1	|C(5,3)	|5 * 14	|[('R.0', 5.0, u'5', u'5')]	|
|2	|C(6,3)	|6**2	|[('R.0', 6.0, u'6', u'6')]	|




### (1) Mistake Group Fraction of size 1




### (24) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:h4tu

	first_attempt
					2015-10-15 09:39:52
	part3_incorrect_attempt
					('0:00:59', u'4*3*2/3!')
	part3_correct_attempt
					['0:01:12', u'6*5*4/3!']

1 Student ID:hah008

	first_attempt
					2015-10-15 09:18:30
	part3_incorrect_attempt
					('0:00:36', u'C(6,5)')
	part3_correct_attempt
					['0:04:40', u'C(6, 3)']

2 Student ID:hkhodada

	first_attempt
					2015-10-12 01:08:11
	part3_incorrect_attempt
					('-2 days, 22:39:22', u'C(14,11)')
	part3_correct_attempt
					['0:01:07', u'C(4,3)']

3 Student ID:glcohen

	first_attempt
					2015-10-13 21:09:52
	part3_incorrect_attempt
					('0:00:54', u'5*5*5')
	part3_correct_attempt
					['0:04:12', u'5!/(3!2!)']

4 Student ID:achava

	first_attempt
					2015-10-14 19:29:31
	part3_incorrect_attempt
					('0:04:44', u'C(6,1)')
					('0:07:44', u'C(6,3)^2')
					('0:07:51', u'C(6,3)^4')
	part3_correct_attempt
					['0:12:54', u'C(6,3)']

5 Student ID:thk002

	first_attempt
					2015-10-12 04:16:16
	part3_incorrect_attempt
					('0:00:21', u'C(6,5)')
	part3_correct_attempt
					['0:00:43', u'C(6,3)']

6 Student ID:beyounge

	first_attempt
					2015-10-09 06:19:14
	part3_incorrect_attempt
					('0:00:00', u'6*5*4')
	part3_correct_attempt
					['0:02:58', u'C(6,3)']

7 Student ID:b1green

	first_attempt
					2015-10-15 21:54:18
	part3_incorrect_attempt
					('0:00:30', u'C(6,1)')
	part3_correct_attempt
					['0:00:47', u'C(6,3)']

8 Student ID:psable

	first_attempt
					2015-10-15 23:40:51
	part3_incorrect_attempt
					('0:13:51', u'C(6,1)')
	part3_correct_attempt
					['0:14:50', u'C(6,3)']

9 Student ID:j5phung

	first_attempt
					2015-10-09 19:13:22
	part3_incorrect_attempt
					('0:00:32', u'C(5,1)')
	part3_correct_attempt
					['0:03:20', u'C(5,3)']

10 Student ID:rsmurlo

	first_attempt
					2015-10-15 00:00:11
	part3_incorrect_attempt
					('0:02:46', u'24/6')
	part3_correct_attempt
					['3:28:20', u'20']

11 Student ID:aakumar

	first_attempt
					2015-10-11 03:05:14
	part3_incorrect_attempt
					('0:01:27', u'C(5,1)')
					('0:01:58', u'3*C(5,1)')
					('0:25:52', u'C(5,3)+C(5,2)+C(5,1)')
	part3_correct_attempt
					['1:34:35', u'C(5,3)']

12 Student ID:tcuddy

	first_attempt
					2015-10-10 20:25:50
	part3_incorrect_attempt
					('0:01:01', u'6!/(2!4!)')
	part3_correct_attempt
					['0:01:20', u'6!/(3!3!)']

13 Student ID:w4shin

	first_attempt
					2015-10-15 00:16:10
	part3_incorrect_attempt
					('0:01:39', u'5^3-5')
	part3_correct_attempt
					['0:05:48', u'5!/(3!2!)']

14 Student ID:jguanzho

	first_attempt
					2015-10-09 21:05:51
	part3_incorrect_attempt
					('0:00:00', u'5!/(4!)')
	part3_correct_attempt
					['0:02:40', u'5!/(2!*3!)']

15 Student ID:csl030

	first_attempt
					2015-10-14 03:39:49
	part3_incorrect_attempt
					('0:00:00', u'C(6,1)')
	part3_correct_attempt
					['0:01:57', u'C(6,3)']

16 Student ID:arc013

	first_attempt
					2015-10-14 03:51:43
	part3_incorrect_attempt
					('0:00:28', u'6*5*4')
	part3_correct_attempt
					['0:00:55', u'C(6, 3)']

17 Student ID:azkong

	first_attempt
					2015-10-15 18:23:52
	part3_incorrect_attempt
					('0:00:30', u'C(5, 1)')
					('0:00:49', u'C(5, 1)*C(5, 1)*C(5, 1)')
					('0:01:07', u'C(5, 1)')
	part3_correct_attempt
					['0:01:17', u'C(5, 3)']

18 Student ID:mitopete

	first_attempt
					2015-10-14 17:12:33
	part3_incorrect_attempt
					('0:26:58', u'4!/(2!(4-2)!)')
	part3_correct_attempt
					['0:27:39', u'4!/(3!(4-3)!)']

19 Student ID:zig006

	first_attempt
					2015-10-12 23:37:35
	part3_incorrect_attempt
					('0:00:00', u'5!(2!3!)')
	part3_correct_attempt
					['0:00:17', u'5!/(2!3!)']

20 Student ID:sghouse

	first_attempt
					2015-10-12 20:20:13
	part3_incorrect_attempt
					('0:00:00', u'2*5*4')
	part3_correct_attempt
					['0:00:36', u'5*4']

21 Student ID:mjethani

	first_attempt
					2015-10-15 15:00:44
	part3_incorrect_attempt
					('0:01:26', u'13!/((3!)(10!))')
	part3_correct_attempt
					['0:02:00', u'6!/((3!)(3!))']

22 Student ID:kgrozav

	first_attempt
					2015-10-15 20:23:27
	part3_incorrect_attempt
					('0:00:00', u'C(6,1)')
	part3_correct_attempt
					['0:01:07', u'C(6,3)']

23 Student ID:jhp077

	first_attempt
					2015-10-15 06:40:54
	part3_incorrect_attempt
					('0:01:00', u'6*5*4')
	part3_correct_attempt
					['0:01:42', u'C(6,3)']












## Part 4

### (126) Mistake Group Digits of size 126




### (23) Mistake Group ['R.1'] of size 23
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(5,2)	|C(4,1)^2	|[('R.1', 2.0, u'2', u'2')]	|
|1	|C(6,2)	|C(6,2)^2	|[('R.1', 2.0, u'2', u'2')]	|
|2	|C(6,2)	|C(4,2)	|[('R.1', 2.0, u'2', u'2')]	|
|3	|C(4,2)	|P(14,2)	|[('R.1', 2.0, u'2', u'2')]	|
|4	|C(6,2)	|C(14,2)	|[('R.1', 2.0, u'2', u'2')]	|
|5	|C(5,2)	|(5!/(3!2!))^2	|[('R.1', 2.0, u'2', u'2')]	|
|6	|C(6,2)	|C(5,2)	|[('R.1', 2.0, u'2', u'2')]	|
|7	|C(6,2)	|C(4, 2)	|[('R.1', 2.0, u'2', u'2')]	|
|8	|C(4,2)	|4!/2!	|[('R.1', 2.0, u'2', u'2!')]	|
|9	|C(6,2)	|6*5*4/2!	|[('R.1', 2.0, u'2', u'2!')]	|
|10	|C(4,2)	|C(14, 2)	|[('R.1', 2.0, u'2', u'2')]	|
|11	|C(4,2)	|4*3*2	|[('R.1', 2.0, u'2', u'2')]	|
|12	|C(6,2)	|C(3,2)	|[('R.1', 2.0, u'2', u'2')]	|
|13	|C(5,2)	|C(5,2)^2	|[('R.1', 2.0, u'2', u'2')]	|




### (9) Mistake Group ['R.0'] of size 9
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(5,2)	|5*4	|[('R.0', 5.0, u'5', u'5')]	|
|1	|C(4,2)	|4/2!	|[('R.0', 4.0, u'4', u'4')]	|
|2	|C(6,2)	|6^5	|[('R.0', 6.0, u'6', u'6')]	|
|3	|C(5,2)	|5^5	|[('R.0', 5.0, u'5', u'5')]	|
|4	|C(5,2)	|5*5	|[('R.0', 5.0, u'5', u'5')]	|
|5	|C(6,2)	|6*5	|[('R.0', 6.0, u'6', u'6')]	|
|6	|C(4,2)	|C(4, 1)*C(3,1)	|[('R.0', 4.0, u'4', u'C(4, 1)')]	|
|7	|C(4,2)	|4*3	|[('R.0', 4.0, u'4', u'4')]	|




### (9) Mistake Group ['R.0', 'R.1'] of size 9
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(6,2)	|6^2	|[('R.0', 6.0, u'6', u'6'), ('R.1', 2.0, u'2', u'2')]	|
|1	|C(5,2)	|5^2	|[('R.0', 5.0, u'5', u'5'), ('R.1', 2.0, u'2', u'2')]	|
|2	|C(6,2)	|C(6,1)^2	|[('R.0', 6.0, u'6', u'C(6,1)'), ('R.1', 2.0, u'2', u'2')]	|
|3	|C(4,2)	|(C(4, 1))^2	|[('R.0', 4.0, u'4', u'C(4, 1)'), ('R.1', 2.0, u'2', u'2')]	|




### (1) Mistake Group Fraction of size 1




### (28) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:glcohen

	first_attempt
					2015-10-13 21:09:52
	part4_incorrect_attempt
					('0:00:54', u'4*4')
	part4_correct_attempt
					['0:04:12', u'5!/(3!2!)']

1 Student ID:jag028

	first_attempt
					2015-10-15 21:15:39
	part4_incorrect_attempt
					('-1 day, 16:59:01', u'C(12,1)C(4,2)')
	part4_correct_attempt
					['0:04:33', u'C(4,2)']

2 Student ID:abasu

	first_attempt
					2015-10-11 03:04:59
	part4_incorrect_attempt
					('0:01:10', u'C(3,1)')
	part4_correct_attempt
					['1:35:22', u'C(4,2)']

3 Student ID:jguanzho

	first_attempt
					2015-10-09 21:05:51
	part4_incorrect_attempt
					('0:00:00', u'5!/(3!)')
	part4_correct_attempt
					['0:02:40', u'5!/(2!*3!)']

4 Student ID:k5law

	first_attempt
					2015-10-13 05:00:58
	part4_incorrect_attempt
					('0:02:31', u'4!/(2!3!)')
	part4_correct_attempt
					['0:02:54', u'5!/(2!3!)']

5 Student ID:beyounge

	first_attempt
					2015-10-09 06:19:14
	part4_incorrect_attempt
					('0:00:00', u'6*5*4')
	part4_correct_attempt
					['0:03:09', u'C(6,2)']

6 Student ID:b1green

	first_attempt
					2015-10-15 21:54:18
	part4_incorrect_attempt
					('0:00:30', u'C(5,1)')
	part4_correct_attempt
					['0:01:07', u'C(6,2)']

7 Student ID:mbl003

	first_attempt
					2015-10-15 07:34:53
	part4_incorrect_attempt
					('0:00:47', u'C(4,1)')
					('0:00:54', u'C(3,1)')
					('0:03:17', u'C(4,3)')
	part4_correct_attempt
					['0:03:24', u'C(4,2)']

8 Student ID:psable

	first_attempt
					2015-10-15 23:40:51
	part4_incorrect_attempt
					('0:14:42', u'C(6,1)')
	part4_correct_attempt
					['0:14:57', u'C(6,2)']

9 Student ID:j5phung

	first_attempt
					2015-10-09 19:13:22
	part4_incorrect_attempt
					('0:00:32', u'C(4,1)')
	part4_correct_attempt
					['0:03:40', u'C(5,2)']

10 Student ID:p4kumar

	first_attempt
					2015-10-15 10:31:31
	part4_incorrect_attempt
					('0:17:55', u'C(4, 3)')
	part4_correct_attempt
					['0:18:00', u'C(4, 2)']

11 Student ID:jmiclat

	first_attempt
					2015-10-15 19:06:41
	part4_incorrect_attempt
					('0:00:45', u'6!(2!4!)')
	part4_correct_attempt
					['0:00:52', u'6!/(2!4!)']

12 Student ID:rsmurlo

	first_attempt
					2015-10-15 00:00:11
	part4_incorrect_attempt
					('3:31:15', u'4!/(2!2!)')
	part4_correct_attempt
					['3:32:27', u'6!/(4!2!)']

13 Student ID:jnatale

	first_attempt
					2015-10-13 04:15:56
	part4_incorrect_attempt
					('0:02:02', u'C(4,1)')
					('0:02:09', u'C(3,1)')
	part4_correct_attempt
					['0:14:19', u'6']

14 Student ID:jap009

	first_attempt
					2015-10-15 22:32:01
	part4_incorrect_attempt
					('0:00:33', u'4!/(2!2!)')
	part4_correct_attempt
					['0:00:59', u'6!/(2!4!)']

15 Student ID:hmshah

	first_attempt
					2015-10-14 09:08:18
	part4_incorrect_attempt
					('0:01:36', u'C(3,1)')
	part4_correct_attempt
					['0:01:58', u'C(4,2)']

16 Student ID:tcuddy

	first_attempt
					2015-10-10 20:25:50
	part4_incorrect_attempt
					('0:00:00', u'4!/4')
	part4_correct_attempt
					['0:00:40', u'6!/(2!4!)']

17 Student ID:aysee

	first_attempt
					2015-10-13 23:22:08
	part4_incorrect_attempt
					('-1 day, 23:58:44', u'C(2,2)')
	part4_correct_attempt
					['0:00:00', u'C(5,2)']

18 Student ID:w4shin

	first_attempt
					2015-10-15 00:16:10
	part4_incorrect_attempt
					('0:01:39', u'5^2-5')
					('0:05:48', u'5!(3!2!)')
	part4_correct_attempt
					['0:05:58', u'5!/(3!2!)']

19 Student ID:anvan

	first_attempt
					2015-10-15 01:29:57
	part4_incorrect_attempt
					('1:36:44', u'5!(2!3!)')
	part4_correct_attempt
					['1:36:59', u'5!/(2!3!)']

20 Student ID:muy002

	first_attempt
					2015-10-14 21:55:38
	part4_incorrect_attempt
					('0:00:00', u'4!(2!2!)')
	part4_correct_attempt
					['0:00:12', u'4!/(2!2!)']

21 Student ID:flhernan

	first_attempt
					2015-10-14 22:19:18
	part4_incorrect_attempt
					('0:02:01', u'C(3,1)')
					('0:02:28', u'C(4,1)')
	part4_correct_attempt
					['0:03:15', u'C(4,2)']

22 Student ID:cstringh

	first_attempt
					2015-10-14 00:44:45
	part4_incorrect_attempt
					('0:04:06', u'2^5')
	part4_correct_attempt
					['0:04:24', u'10']

23 Student ID:csl030

	first_attempt
					2015-10-14 03:39:49
	part4_incorrect_attempt
					('0:00:00', u'C(6,1)')
	part4_correct_attempt
					['0:01:57', u'C(6,2)']

24 Student ID:azkong

	first_attempt
					2015-10-15 18:23:52
	part4_incorrect_attempt
					('0:00:30', u'C(4, 1)')
					('0:00:49', u'C(4, 1)*C(4,1)')
	part4_correct_attempt
					['0:01:47', u'C(5, 2)']

25 Student ID:ytc012

	first_attempt
					2015-10-15 10:58:28
	part4_incorrect_attempt
					('0:01:10', u'5!(2!3!)')
					('0:01:20', u'6!(2!4!)')
	part4_correct_attempt
					['0:01:24', u'6!/(2!4!)']

26 Student ID:mtrafeca

	first_attempt
					2015-10-11 21:55:13
	part4_incorrect_attempt
					('0:00:25', u'4!(2!*2!)')
	part4_correct_attempt
					['0:00:32', u'4!/(2!*2!)']

27 Student ID:kgrozav

	first_attempt
					2015-10-15 20:23:27
	part4_incorrect_attempt
					('0:00:00', u'C(5,1)')
	part4_correct_attempt
					['0:02:31', u'C(6,2)']












## Part 5

### (14) Mistake Group ['R.0.0'] of size 14
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|11*(11-1)*C(5,3)*C(5,2)	|11*10*5*4	|[('R.0.0', 110.0, u'11*(11-1)', u'11*10')]	|
|1	|13*(13-1)*C(6,3)*C(6,2)	|13*12*3*2	|[('R.0.0', 156.0, u'13*(13-1)', u'13*12')]	|
|2	|12*(12-1)*C(5,3)*C(5,2)	|12*11*5*5	|[('R.0.0', 132.0, u'12*(12-1)', u'12*11')]	|
|3	|14*(14-1)*C(5,3)*C(5,2)	|14*13*5*4	|[('R.0.0', 182.0, u'14*(14-1)', u'14*13')]	|
|4	|12*(12-1)*C(5,3)*C(5,2)	|12*11*20*20	|[('R.0.0', 132.0, u'12*(12-1)', u'12*11')]	|
|5	|13*(13-1)*C(6,3)*C(6,2)	|C(13,1) * C(12,1) * 6 * 6	|[('R.0.0', 156.0, u'13*(13-1)', u'C(13,1) * C(12,1)')]	|
|6	|16*(16-1)*C(5,3)*C(5,2)	|16*15*5*4	|[('R.0.0', 240.0, u'16*(16-1)', u'16*15')]	|
|7	|16*(16-1)*C(5,3)*C(5,2)	|16*15*2*(5!/(3!*2!))	|[('R.0.0', 240.0, u'16*(16-1)', u'16*15')]	|
|8	|14*(14-1)*C(5,3)*C(5,2)	|14*13*(5^3-5)*(5^2-5)	|[('R.0.0', 182.0, u'14*(14-1)', u'14*13')]	|
|9	|16*(16-1)*C(5,3)*C(5,2)	|16*15*(16)*(5!/((2!)(3!)))	|[('R.0.0', 240.0, u'16*(16-1)', u'16*15')]	|
|10	|16*(16-1)*C(6,3)*C(6,2)	|16*15*C(6,1)*C(5,1)	|[('R.0.0', 240.0, u'16*(16-1)', u'16*15')]	|
|11	|12*(12-1)*C(6,3)*C(6,2)	|12*11*6*5	|[('R.0.0', 132.0, u'12*(12-1)', u'12*11')]	|
|12	|13*(13-1)*C(5,3)*C(5,2)	|13 * 12 * 5 * 5	|[('R.0.0', 156.0, u'13*(13-1)', u'13 * 12')]	|




### (11) Mistake Group redirect of size 11




### (10) Mistake Group Fraction of size 10




### (9) Mistake Group Digits of size 9




### (7) Mistake Group ['R.0'] of size 7
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|13*(13-1)*C(4,3)*C(4,2)	|13 * 12 * 4 * 3	|[('R.0', 624.0, u'13*(13-1)*C(4,3)', u'13 * 12 * 4')]	|
|1	|11*(11-1)*C(5,3)*C(5,2)	|[11 * 10 * C(5, 3) * C(5, 4)]	|[('R.0', 1100.0, u'11*(11-1)*C(5,3)', u'11 * 10 * C(5, 3)')]	|
|2	|14*(14-1)*C(4,3)*C(4,2)	|14*13*4*3	|[('R.0', 728.0, u'14*(14-1)*C(4,3)', u'14*13*4')]	|
|3	|14*(14-1)*C(4,3)*C(4,2)	|14*13*(4!/(3!))*(4!(2!2!))	|[('R.0', 728.0, u'14*(14-1)*C(4,3)', u'14*13*(4!/(3!))')]	|
|4	|16*(16-1)*C(4,3)*C(4,2)	|16*15*4*3	|[('R.0', 960.0, u'16*(16-1)*C(4,3)', u'16*15*4')]	|
|5	|16*(16-1)*C(4,3)*C(4,2)	|16*15*4*4	|[('R.0', 960.0, u'16*(16-1)*C(4,3)', u'16*15*4')]	|
|6	|12*(12-1)*C(4,3)*C(4,2)	|12*11*4*5	|[('R.0', 528.0, u'12*(12-1)*C(4,3)', u'12*11*4')]	|




### (5) Mistake Group ['R.0.0', 'R.0.1.1', 'R.1.1'] of size 5
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.0.1.1', 'R.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|13*(13-1)*C(6,3)*C(6,2)	|13 * 12 * C(6,3)^3 * C(6,2)^2	|[('R.0.0', 156.0, u'13*(13-1)', u'13 * 12'), ('R.0.1.1', 3.0, u'3', u'3'), ('R.1.1', 2.0, u'2', u'2')]	|
|1	|13*(13-1)*C(6,3)*C(6,2)	|13*12*C(4,3)*C(4,2)	|[('R.0.0', 156.0, u'13*(13-1)', u'13*12'), ('R.0.1.1', 3.0, u'3', u'3'), ('R.1.1', 2.0, u'2', u'2')]	|
|2	|15*(15-1)*C(6,3)*C(6,2)	|15*14*C(4,3)*C(4,2)	|[('R.0.0', 210.0, u'15*(15-1)', u'15*14'), ('R.0.1.1', 3.0, u'3', u'3'), ('R.1.1', 2.0, u'2', u'2')]	|
|3	|13*(13-1)*C(6,3)*C(6,2)	|C(13,1)*C(12,1)* C(4,3) * C(4,2)	|[('R.0.0', 156.0, u'13*(13-1)', u'C(13,1)*C(12,1)'), ('R.0.1.1', 3.0, u'3', u'3'), ('R.1.1', 2.0, u'2', u'2')]	|
|4	|14*(14-1)*C(5,3)*C(5,2)	|14*13*(5^3)*(5^2)	|[('R.0.0', 182.0, u'14*(14-1)', u'14*13'), ('R.0.1.1', 3.0, u'3', u'3'), ('R.1.1', 2.0, u'2', u'2')]	|




### (3) Mistake Group ['R.1.1'] of size 3
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|14*(14-1)*C(6,3)*C(6,2)	|14*13*6^2*5^2*4^2	|[('R.1.1', 2.0, u'2', u'2')]	|
|1	|14*(14-1)*C(6,3)*C(6,2)	|14*13*6^2	|[('R.1.1', 2.0, u'2', u'2')]	|
|2	|15*(15-1)*C(6,3)*C(6,2)	|C(15,3)+C(14,2)	|[('R.1.1', 2.0, u'2', u'2')]	|




### (2) Mistake Group ['R.0', 'R.1.1'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|14*(14-1)*C(5,3)*C(5,2)	|14*13*C(5,3)*C(4,2)	|[('R.0', 1820.0, u'14*(14-1)*C(5,3)', u'14*13*C(5,3)'), ('R.1.1', 2.0, u'2', u'2')]	|
|1	|16*(16-1)*C(6,3)*C(6,2)	|16*15*C(6,3)*C(5,2)	|[('R.0', 4800.0, u'16*(16-1)*C(6,3)', u'16*15*C(6,3)'), ('R.1.1', 2.0, u'2', u'2')]	|




### (1) Mistake Group ['R.0.0.1', 'R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.1', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|13*(13-1)*C(4,3)*C(4,2)	| C(13,1)+C(12,1)+C(4,1)+C(4,2)	|[('R.0.0.1', 12.0, u'13-1', u'C(12,1)'), ('R.1', 6, u'C(4,2)', u'C(4,2)')]	|




### (1) Mistake Group ['R.0.0', 'R.1.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|11*(11-1)*C(5,3)*C(5,2)	|11*10*C(5,1)*C(4,1)^2	|[('R.0.0', 110.0, u'11*(11-1)', u'11*10'), ('R.1.1', 2.0, u'2', u'2')]	|




### (1) Mistake Group ['R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|11*(11-1)*C(6,3)*C(6,2)	|20*15	|[('R.1', 15, u'C(6,2)', u'15')]	|




### (1) Mistake Group ['R.0.1', 'R.1.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1', 'R.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|15*(15-1)*C(6,3)*C(6,2)	|C(15,1)*C(14,2)*C(6,3)*C(6,1)^2	|[('R.0.1', 20, u'C(6,3)', u'C(6,3)'), ('R.1.1', 2.0, u'2', u'2')]	|




### (1) Mistake Group ['R.0.1.0'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|14*(14-1)*C(5,3)*C(5,2)	|13 * 12 * 5!/(3!(5-3)!) * 5!/(2!(5-2)!)	|[('R.0.1.0', 5.0, u'5', u'5')]	|




### (1) Mistake Group ['R.0.0', 'R.0.1.0', 'R.0.1.1', 'R.1.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.0.1.0', 'R.0.1.1', 'R.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|11*(11-1)*C(5,3)*C(5,2)	|11*10*C(5,1)^3*C(4,1)^2	|[('R.0.0', 110.0, u'11*(11-1)', u'11*10'), ('R.0.1.0', 5.0, u'5', u'C(5,1)'), ('R.0.1.1', 3.0, u'3', u'3'), ('R.1.1', 2.0, u'2', u'2')]	|




### (1) Mistake Group ['R.0.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|11*(11-1)*C(6,3)*C(6,2)	|11*C(6,3)+10*C(6,2)	|[('R.0.1', 20, u'C(6,3)', u'C(6,3)')]	|




### (1) Mistake Group ['R.0.1.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|14*(14-1)*C(4,3)*C(4,2)	|[14*C(4,3)]+[13*C(4,2)]	|[('R.0.1.1', 3.0, u'3', u'3')]	|




### (1) Mistake Group ['R.0.1.0', 'R.0.1.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1.0', 'R.0.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|15*(15-1)*C(4,3)*C(4,2)	|[C(15, 1)*[C(4, 1)]^3]*[C(14, 1)*[C(4, 1)]^2]	|[('R.0.1.0', 4.0, u'4', u'C(4, 1)'), ('R.0.1.1', 3.0, u'3', u'3')]	|




### (11) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:tak068

	first_attempt
					2015-10-14 08:13:19
	part1_correct_attempt
					['0:00:00', u'C(10,1)']
	part2_correct_attempt
					['0:06:45', u'C(9,1)']
	part3_correct_attempt
					['0:00:49', u'C(6,3)']
	part4_correct_attempt
					['0:05:10', u'C(6,2)']
	part5_incorrect_attempt
					('0:06:57', u'C(10,1)C(6,2)C(6,2)C(6,3)')
					('0:07:05', u'C(10,1)C(6,3)C(6,2)C(6,3)')
	part5_correct_attempt
					['0:07:15', u'C(10,1)C(9,1)C(6,2)C(6,3)']

1 Student ID:msaguiar

	first_attempt
					2015-10-13 04:29:49
	part1_correct_attempt
					['0:00:00', u'12']
	part2_correct_attempt
					['0:00:12', u'11']
	part3_correct_attempt
					['0:01:02', u'C(6,3)']
	part4_correct_attempt
					['0:01:15', u'C(6,2)']
	part5_incorrect_attempt
					('0:01:48', u'C(6,2)*C(6,3)')
	part5_correct_attempt
					['0:05:07', u'(12*C(6,3))*(11*C(6,2))']

2 Student ID:lpettit

	first_attempt
					2015-10-14 21:23:40
	part1_correct_attempt
					['0:00:00', u'16']
	part2_correct_attempt
					['0:00:00', u'15']
	part3_correct_attempt
					['0:02:20', u'5!/(3!*2!)']
	part4_correct_attempt
					['0:02:20', u'5!/(3!*2!)']
	part5_incorrect_attempt
					('0:08:48', u'((16^15)*100)')
	part5_correct_attempt
					['0:09:43', u'(16*15*100)']

3 Student ID:jhw015

	first_attempt
					2015-10-15 03:12:13
	part1_correct_attempt
					['0:00:00', u'12']
	part2_correct_attempt
					['0:00:21', u'11']
	part5_incorrect_attempt
					('0:01:23', u'12*11')
	part5_correct_attempt
					['0:02:51', u'12*11 * C(5,3) * C(5,2)']

4 Student ID:nisharma

	first_attempt
					2015-10-14 18:22:29
	part1_correct_attempt
					['0:00:00', u'16']
	part2_correct_attempt
					['0:00:42', u'15']
	part3_correct_attempt
					['0:00:42', u'C(6,3)']
	part4_correct_attempt
					['0:00:42', u'C(6,2)']
	part5_incorrect_attempt
					('0:01:18', u'C(6,3) * 16 *15')
	part5_correct_attempt
					['0:02:55', u'C(6,2)*C(6,3) * 16 *15']

5 Student ID:tcuddy

	first_attempt
					2015-10-10 20:25:50
	part1_correct_attempt
					['0:00:00', u'16']
	part2_correct_attempt
					['0:00:40', u'15']
	part3_correct_attempt
					['0:01:20', u'6!/(3!3!)']
	part4_correct_attempt
					['0:00:40', u'6!/(2!4!)']
	part5_incorrect_attempt
					('0:01:20', u'6!/(2!4!)6!/(2!4!)6!/(3!3!)*15*16')
	part5_correct_attempt
					['0:02:34', u'[ 15*16* ( 6!/(2!4!) ) * ( 6!/(3!3!) )]']

6 Student ID:ssamudra

	first_attempt
					2015-10-15 03:35:23
	part1_correct_attempt
					['0:00:00', u'13']
	part2_correct_attempt
					['0:00:00', u'12']
	part3_correct_attempt
					['0:00:00', u'4']
	part4_correct_attempt
					['0:07:26', u'6']
	part5_incorrect_attempt
					('0:07:26', u'(144 * 13)')
	part5_correct_attempt
					['0:08:05', u'(24 * 13* 12)']

7 Student ID:jnatale

	first_attempt
					2015-10-13 04:15:56
	part1_correct_attempt
					['0:00:00', u'12']
	part2_correct_attempt
					['0:00:14', u'11']
	part3_correct_attempt
					['0:00:21', u'4']
	part4_correct_attempt
					['0:14:19', u'6']
	part5_incorrect_attempt
					('0:14:50', u'12*11')
	part5_correct_attempt
					['0:15:08', u'12*11*4*6']

8 Student ID:abjara

	first_attempt
					2015-10-14 23:06:38
	part1_correct_attempt
					['0:00:00', u'11']
	part2_correct_attempt
					['0:00:00', u'10']
	part3_correct_attempt
					['0:00:00', u'4!/(3!)']
	part4_correct_attempt
					['0:00:00', u'4!/(2!*2!)']
	part5_incorrect_attempt
					('0:00:57', u'[4!/(3!)]*4!/(2!*2!)')
					('0:01:25', u'24*6*10*4')
	part5_correct_attempt
					['0:01:36', u'11*6*10*4']

9 Student ID:ytc012

	first_attempt
					2015-10-15 10:58:28
	part1_correct_attempt
					['0:00:00', u'15']
	part2_correct_attempt
					['0:00:15', u'14']
	part3_correct_attempt
					['0:00:48', u'6!/(3!3!)']
	part4_correct_attempt
					['0:01:24', u'6!/(2!4!)']
	part5_incorrect_attempt
					('0:01:46', u'6!6!/(3!3!2!4!)')
	part5_correct_attempt
					['0:02:00', u'15*14*6!6!/(3!3!2!4!)']

10 Student ID:e9brown

	first_attempt
					2015-10-14 11:24:35
	part1_correct_attempt
					['0:00:00', u'16 ']
	part2_correct_attempt
					['0:00:00', u'15']
	part3_correct_attempt
					['0:00:46', u'C(6,3)']
	part4_correct_attempt
					['0:01:00', u'C(6,2)']
	part5_incorrect_attempt
					('0:01:28', u'C(6,2)*C(6,3)')
	part5_correct_attempt
					['0:01:44', u'15*16*C(6,2)*C(6,3)']












## Part 6

### (22) Mistake Group ['R.1'] of size 22
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|11*(11-1)*C(5,3)*C(5,2)/[C(55,5)]	|(11*100000*C(5,2)*C(5,3))/C(55,5)	|[('R.1', 3478761, u'C(55,5)', u'C(55,5)')]	|
|1	|14*(14-1)*C(5,3)*C(5,2)/[C(70,5)]	|(14*3*(5!/4!)*(5!/3!))/(70!/(65!*5!))	|[('R.1', 12103014, u'C(70,5)', u'70!/(65!*5!)')]	|
|2	|10*(10-1)*C(5,3)*C(5,2)/[C(50,5)]	|2250/C(50,5)	|[('R.1', 2118760, u'C(50,5)', u'C(50,5)')]	|
|3	|15*(15-1)*C(5,3)*C(5,2)/[C(75,5)]	|(15*14**5*4)/[(15*5)!/[5!(15*5-5)!]]	|[('R.1', 17259390, u'C(75,5)', u'(15*5)!/[5!(15*5-5)!]')]	|
|4	|11*(11-1)*C(5,3)*C(5,2)/[C(55,5)]	|132000/(55!/(5!50!))	|[('R.1', 3478761, u'C(55,5)', u'55!/(5!50!)')]	|
|5	|14*(14-1)*C(4,3)*C(4,2)/[C(56,5)]	|(4*14*4*13)/(56!/(5!51!))	|[('R.1', 3819816, u'C(56,5)', u'56!/(5!51!)')]	|
|6	|10*(10-1)*C(5,3)*C(5,2)/[C(50,5)]	|281250/2118760	|[('R.1', 2118760, u'C(50,5)', u'2118760')]	|
|7	|10*(10-1)*C(5,3)*C(5,2)/[C(50,5)]	|108000/2118760	|[('R.1', 2118760, u'C(50,5)', u'2118760')]	|
|8	|10*(10-1)*C(5,3)*C(5,2)/[C(50,5)]	|144000/2118760	|[('R.1', 2118760, u'C(50,5)', u'2118760')]	|
|9	|14*(14-1)*C(5,3)*C(5,2)/[C(70,5)]	|14*13*(5!/(3!2!))^5/(70!/(65!5!))	|[('R.1', 12103014, u'C(70,5)', u'70!/(65!5!)')]	|
|10	|11*(11-1)*C(4,3)*C(4,2)/[C(44,5)]	|11*4*4*10 / C(44,5)	|[('R.1', 1086008, u'C(44,5)', u'C(44,5)')]	|
|11	|13*(13-1)*C(6,3)*C(6,2)/[C(78,5)]	|[13*12*2*5*4*3*5]/[78!/(5!*73!)]	|[('R.1', 21111090, u'C(78,5)', u'78!/(5!*73!)')]	|
|12	|10*(10-1)*C(6,3)*C(6,2)/[C(60,5)]	|[6!/(2!(6-2)!)]/[60!/(5!(60-5)!)]	|[('R.1', 5461512, u'C(60,5)', u'60!/(5!(60-5)!)')]	|
|13	|10*(10-1)*C(4,3)*C(4,2)/[C(40,5)]	|2160/3744/658008	|[('R.1', 658008, u'C(40,5)', u'658008')]	|
|14	|15*(15-1)*C(5,3)*C(5,2)/[C(75,5)]	|[[15!/[(15-3)!3!]]*[14!/[(14-2)!2!]]*[5!/[(5-3)!3!]]*[5!/[(5-2)!2!]]]/[75!/[70!5!]]	|[('R.1', 17259390, u'C(75,5)', u'75!/[70!5!]')]	|
|15	|16*(16-1)*C(6,3)*C(6,2)/[C(96,5)]	|(C(6,2)*C(6,3))/C(6*16,5)	|[('R.1', 61124064, u'C(96,5)', u'C(6*16,5)')]	|
|16	|16*(16-1)*C(5,3)*C(5,2)/[C(80,5)]	|((16^15)*100)/(80!/(5!*75!))	|[('R.1', 24040016, u'C(80,5)', u'80!/(5!*75!)')]	|
|17	|11*(11-1)*C(4,3)*C(4,2)/[C(44,5)]	|[[4!/(3!)]*4!/(2!*2!)]/[44!/(5!*39!)]	|[('R.1', 1086008, u'C(44,5)', u'44!/(5!*39!)')]	|
|18	|12*(12-1)*C(6,3)*C(6,2)/[C(72,5)]	|3960/C(72,5)	|[('R.1', 13991544, u'C(72,5)', u'C(72,5)')]	|
|19	|11*(11-1)*C(5,3)*C(5,2)/[C(55,5)]	|4400/C(55,5)	|[('R.1', 3478761, u'C(55,5)', u'C(55,5)')]	|
|20	|13*(13-1)*C(4,3)*C(4,2)/[C(52,5)]	|(C(13,1)*C(12,1)*C(4,3)*C(4,2)*C(13,1)*C(4,3)C(12,1)C(4,2))/(C(52,5))	|[('R.1', 2598960, u'C(52,5)', u'C(52,5)')]	|
|21	|12*(12-1)*C(6,3)*C(6,2)/[C(72,5)]	|C(6,3)/C(72,5)	|[('R.1', 13991544, u'C(72,5)', u'C(72,5)')]	|




### (16) Mistake Group ['R.0'] of size 16
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|11*(11-1)*C(6,3)*C(6,2)/[C(66,5)]	|33000/(66!/61!)	|[('R.0', 33000.0, u'11*(11-1)*C(6,3)*C(6,2)', u'33000')]	|
|1	|16*(16-1)*C(4,3)*C(4,2)/[C(64,5)]	|(16*15*4*6)/(52!/(5!*47!))	|[('R.0', 5760.0, u'16*(16-1)*C(4,3)*C(4,2)', u'16*15*4*6')]	|
|2	|11*(11-1)*C(4,3)*C(4,2)/[C(44,5)]	|11*10*4*6/(11!/(5!6!))	|[('R.0', 2640.0, u'11*(11-1)*C(4,3)*C(4,2)', u'11*10*4*6')]	|
|3	|14*(14-1)*C(5,3)*C(5,2)/[C(70,5)]	|(14 * 13 *  5!/(2!3!) * 5!/(2!3!) ) / (70!5!65!)	|[('R.0', 18200.0, u'14*(14-1)*C(5,3)*C(5,2)', u'14 * 13 *  5!/(2!3!) * 5!/(2!3!)')]	|
|4	|14*(14-1)*C(5,3)*C(5,2)/[C(70,5)]	|(14 * 13 * 5!/(2!3!) * 5!/(2!3!) ) / (70!5!/65!)	|[('R.0', 18200.0, u'14*(14-1)*C(5,3)*C(5,2)', u'14 * 13 * 5!/(2!3!) * 5!/(2!3!)')]	|
|5	|13*(13-1)*C(4,3)*C(4,2)/[C(52,5)]	|(24 * 12 * 13)/(52!/(3!49!))	|[('R.0', 3744.0, u'13*(13-1)*C(4,3)*C(4,2)', u'24 * 12 * 13')]	|
|6	|16*(16-1)*C(6,3)*C(6,2)/[C(96,5)]	|16*(16-1)*20*15/4560	|[('R.0', 72000.0, u'16*(16-1)*C(6,3)*C(6,2)', u'16*(16-1)*20*15')]	|
|7	|16*(16-1)*C(5,3)*C(5,2)/[C(80,5)]	|(16*(16-1)C(5,3)C(5,2))/(C(60,5))	|[('R.0', 24000.0, u'16*(16-1)*C(5,3)*C(5,2)', u'16*(16-1)C(5,3)C(5,2)')]	|
|8	|16*(16-1)*C(5,3)*C(5,2)/[C(80,5)]	|(16*(16-1)C(5,3)C(5,2))/(C(96,5))	|[('R.0', 24000.0, u'16*(16-1)*C(5,3)*C(5,2)', u'16*(16-1)C(5,3)C(5,2)')]	|
|9	|13*(13-1)*C(4,3)*C(4,2)/[C(52,5)]	|((4!/(3!))(4!/(2!2!))*13*12)/(52!/(5!48!))	|[('R.0', 3744.0, u'13*(13-1)*C(4,3)*C(4,2)', u'(4!/(3!))(4!/(2!2!))*13*12')]	|
|10	|16*(16-1)*C(6,3)*C(6,2)/[C(96,5)]	|16*15*(6*5*4/3!)*(6*5/2!)/(84!/(5!79!))	|[('R.0', 72000.0, u'16*(16-1)*C(6,3)*C(6,2)', u'16*15*(6*5*4/3!)*(6*5/2!)')]	|
|11	|16*(16-1)*C(6,3)*C(6,2)/[C(96,5)]	|16*15*(6*5*4/3!)*(6*5/2!)/(84!/(5!*79!))	|[('R.0', 72000.0, u'16*(16-1)*C(6,3)*C(6,2)', u'16*15*(6*5*4/3!)*(6*5/2!)')]	|
|12	|11*(11-1)*C(6,3)*C(6,2)/[C(66,5)]	|33000/(66!/(5!59!))	|[('R.0', 33000.0, u'11*(11-1)*C(6,3)*C(6,2)', u'33000')]	|
|13	|15*(15-1)*C(4,3)*C(4,2)/[C(60,5)]	|15*(15-1)*C(4,3)*C(4,2)/[C(75,4)]	|[('R.0', 5040.0, u'15*(15-1)*C(4,3)*C(4,2)', u'15*(15-1)*C(4,3)*C(4,2)')]	|
|14	|15*(15-1)*C(4,3)*C(4,2)/[C(60,5)]	|((15)(14)(C(4,3))(C(4,2)))/(C(75,4))	|[('R.0', 5040.0, u'15*(15-1)*C(4,3)*C(4,2)', u'(15)(14)(C(4,3))(C(4,2))')]	|
|15	|11*(11-1)*C(5,3)*C(5,2)/[C(55,5)]	|11000/(55!(5!50!))	|[('R.0', 11000.0, u'11*(11-1)*C(5,3)*C(5,2)', u'11000')]	|




### (10) Mistake Group ['R.0.0.0', 'R.1'] of size 10
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|11*(11-1)*C(5,3)*C(5,2)/[C(55,5)]	|(11*10*C(5,1)*C(4,1))/C(55,5)	|[('R.0.0.0', 110.0, u'11*(11-1)', u'11*10'), ('R.1', 3478761, u'C(55,5)', u'C(55,5)')]	|
|1	|11*(11-1)*C(5,3)*C(5,2)/[C(55,5)]	|(11*10*5*4)/C(55,5)	|[('R.0.0.0', 110.0, u'11*(11-1)', u'11*10'), ('R.1', 3478761, u'C(55,5)', u'C(55,5)')]	|
|2	|14*(14-1)*C(5,3)*C(5,2)/[C(70,5)]	|14*13*5*4/(70!/(65!5!))	|[('R.0.0.0', 182.0, u'14*(14-1)', u'14*13'), ('R.1', 12103014, u'C(70,5)', u'70!/(65!5!)')]	|
|3	|14*(14-1)*C(5,3)*C(5,2)/[C(70,5)]	|(14*13*5*4)/C(14*5,5)	|[('R.0.0.0', 182.0, u'14*(14-1)', u'14*13'), ('R.1', 12103014, u'C(70,5)', u'C(14*5,5)')]	|
|4	|12*(12-1)*C(5,3)*C(5,2)/[C(60,5)]	|12*11*20*20/5461512	|[('R.0.0.0', 132.0, u'12*(12-1)', u'12*11'), ('R.1', 5461512, u'C(60,5)', u'5461512')]	|
|5	|13*(13-1)*C(6,3)*C(6,2)/[C(78,5)]	|(C(13,1) * C(12,1) * 6 * 6)/C(78,5)	|[('R.0.0.0', 156.0, u'13*(13-1)', u'C(13,1) * C(12,1)'), ('R.1', 21111090, u'C(78,5)', u'C(78,5)')]	|
|6	|16*(16-1)*C(5,3)*C(5,2)/[C(80,5)]	|(16*15*5*4)/((5*16)!/(5!(5*16-5)!))	|[('R.0.0.0', 240.0, u'16*(16-1)', u'16*15'), ('R.1', 24040016, u'C(80,5)', u'(5*16)!/(5!(5*16-5)!)')]	|
|7	|16*(16-1)*C(5,3)*C(5,2)/[C(80,5)]	|(16*15*2*(5!/(3!*2!)))/(80!/(5!*75!))	|[('R.0.0.0', 240.0, u'16*(16-1)', u'16*15'), ('R.1', 24040016, u'C(80,5)', u'80!/(5!*75!)')]	|
|8	|16*(16-1)*C(6,3)*C(6,2)/[C(96,5)]	|(16*15*C(6,1)*C(5,1)) / C(96,5)	|[('R.0.0.0', 240.0, u'16*(16-1)', u'16*15'), ('R.1', 61124064, u'C(96,5)', u'C(96,5)')]	|
|9	|13*(13-1)*C(5,3)*C(5,2)/[C(65,5)]	|(13 * 12 * 5 * 5)/C(13 * 5, 5)	|[('R.0.0.0', 156.0, u'13*(13-1)', u'13 * 12'), ('R.1', 8259888, u'C(65,5)', u'C(13 * 5, 5)')]	|




### (8) Mistake Group ['R.0', 'R.1.0'] of size 8
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|13*(13-1)*C(4,3)*C(4,2)/[C(52,5)]	|(13*12*C(4,3)*C(4,2))/C(52,4)	|[('R.0', 3744.0, u'13*(13-1)*C(4,3)*C(4,2)', u'13*12*C(4,3)*C(4,2)'), ('R.1.0', 52.0, u'52', u'52')]	|
|1	|13*(13-1)*C(6,3)*C(6,2)/[C(78,5)]	|(13*12*C(6,3)*C(6,2))/C(78,6)	|[('R.0', 46800.0, u'13*(13-1)*C(6,3)*C(6,2)', u'13*12*C(6,3)*C(6,2)'), ('R.1.0', 78.0, u'78', u'78')]	|
|2	|10*(10-1)*C(4,3)*C(4,2)/[C(40,5)]	|2160/C(40,2)	|[('R.0', 2160.0, u'10*(10-1)*C(4,3)*C(4,2)', u'2160'), ('R.1.0', 40.0, u'40', u'40')]	|
|3	|15*(15-1)*C(4,3)*C(4,2)/[C(60,5)]	|15*(15-1)*C(4,3)*C(4,2)/ C(60,4)	|[('R.0', 5040.0, u'15*(15-1)*C(4,3)*C(4,2)', u'15*(15-1)*C(4,3)*C(4,2)'), ('R.1.0', 60.0, u'60', u'60')]	|
|4	|15*(15-1)*C(4,3)*C(4,2)/[C(60,5)]	|15*(15-1)*C(4,3)*C(4,2)/ [C(60,4)]	|[('R.0', 5040.0, u'15*(15-1)*C(4,3)*C(4,2)', u'15*(15-1)*C(4,3)*C(4,2)'), ('R.1.0', 60.0, u'60', u'60')]	|
|5	|15*(15-1)*C(4,3)*C(4,2)/[C(60,5)]	|15*(15-1)*C(4,3)* C(4,2)/ [C(60,4)]	|[('R.0', 5040.0, u'15*(15-1)*C(4,3)*C(4,2)', u'15*(15-1)*C(4,3)* C(4,2)'), ('R.1.0', 60.0, u'60', u'60')]	|
|6	|15*(15-1)*C(4,3)*C(4,2)/[C(60,5)]	|15*(15-1)*C(4,3)*C(4,2)/[C(60,4)]	|[('R.0', 5040.0, u'15*(15-1)*C(4,3)*C(4,2)', u'15*(15-1)*C(4,3)*C(4,2)'), ('R.1.0', 60.0, u'60', u'60')]	|
|7	|15*(15-1)*C(4,3)*C(4,2)/[C(60,5)]	|((15)(14)(C(4,3))(C(4,2)))/(C(60,4))	|[('R.0', 5040.0, u'15*(15-1)*C(4,3)*C(4,2)', u'(15)(14)(C(4,3))(C(4,2))'), ('R.1.0', 60.0, u'60', u'60')]	|




### (7) Mistake Group ['R.0', 'R.1.1'] of size 7
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|15*(15-1)*C(6,3)*C(6,2)/[C(90,5)]	|(15*14*C(6,3)*C(6,2))/C(15,5)	|[('R.0', 63000.0, u'15*(15-1)*C(6,3)*C(6,2)', u'15*14*C(6,3)*C(6,2)'), ('R.1.1', 5.0, u'5', u'5')]	|
|1	|15*(15-1)*C(4,3)*C(4,2)/[C(60,5)]	|(C(15,1)*C(14,1)*C(4,3)*C(4,2))/C(52,5)	|[('R.0', 5040.0, u'15*(15-1)*C(4,3)*C(4,2)', u'C(15,1)*C(14,1)*C(4,3)*C(4,2)'), ('R.1.1', 5.0, u'5', u'5')]	|
|2	|14*(14-1)*C(4,3)*C(4,2)/[C(56,5)]	|C(14,1)*C(13,1)*C(4,2)*4/[C(70,5)]	|[('R.0', 4368.0, u'14*(14-1)*C(4,3)*C(4,2)', u'C(14,1)*C(13,1)*C(4,2)*4'), ('R.1.1', 5.0, u'5', u'5')]	|
|3	|15*(15-1)*C(6,3)*C(6,2)/[C(90,5)]	|(C(15,1)*C(14,1)*C(6,3)*C(6,2))/C(78,5)	|[('R.0', 63000.0, u'15*(15-1)*C(6,3)*C(6,2)', u'C(15,1)*C(14,1)*C(6,3)*C(6,2)'), ('R.1.1', 5.0, u'5', u'5')]	|
|4	|13*(13-1)*C(6,3)*C(6,2)/[C(78,5)]	|13*12*C(6,3)*C(6,2) / C(48,5)	|[('R.0', 46800.0, u'13*(13-1)*C(6,3)*C(6,2)', u'13*12*C(6,3)*C(6,2)'), ('R.1.1', 5.0, u'5', u'5')]	|
|5	|15*(15-1)*C(6,3)*C(6,2)/[C(90,5)]	|(15*(15-1)*C(6,3)*C(6,2))/(C(6*13,5))	|[('R.0', 63000.0, u'15*(15-1)*C(6,3)*C(6,2)', u'15*(15-1)*C(6,3)*C(6,2)'), ('R.1.1', 5.0, u'5', u'5')]	|
|6	|15*(15-1)*C(6,3)*C(6,2)/[C(90,5)]	|(15*(15-1)*C(6,3)*C(6,2))/(C(15*5,5))	|[('R.0', 63000.0, u'15*(15-1)*C(6,3)*C(6,2)', u'15*(15-1)*C(6,3)*C(6,2)'), ('R.1.1', 5.0, u'5', u'5')]	|




### (5) Mistake Group redirect of size 5




### (5) Mistake Group ['R.0.0', 'R.1'] of size 5
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|13*(13-1)*C(4,3)*C(4,2)/[C(52,5)]	|13 * 12 * 4 * 3 / C(52,5)	|[('R.0.0', 624.0, u'13*(13-1)*C(4,3)', u'13 * 12 * 4'), ('R.1', 2598960, u'C(52,5)', u'C(52,5)')]	|
|1	|11*(11-1)*C(5,3)*C(5,2)/[C(55,5)]	|[11 * 10 * C(5, 3) * C(5, 4)] / C(55, 5)	|[('R.0.0', 1100.0, u'11*(11-1)*C(5,3)', u'11 * 10 * C(5, 3)'), ('R.1', 3478761, u'C(55,5)', u'C(55, 5)')]	|
|2	|14*(14-1)*C(4,3)*C(4,2)/[C(56,5)]	|(14*13*4*3)/C(56,5)	|[('R.0.0', 728.0, u'14*(14-1)*C(4,3)', u'14*13*4'), ('R.1', 3819816, u'C(56,5)', u'C(56,5)')]	|
|3	|16*(16-1)*C(4,3)*C(4,2)/[C(64,5)]	|(16*15*4*3)/C(64,5)	|[('R.0.0', 960.0, u'16*(16-1)*C(4,3)', u'16*15*4'), ('R.1', 7624512, u'C(64,5)', u'C(64,5)')]	|
|4	|16*(16-1)*C(4,3)*C(4,2)/[C(64,5)]	|(16*15*4*4)/C(64,5)	|[('R.0.0', 960.0, u'16*(16-1)*C(4,3)', u'16*15*4'), ('R.1', 7624512, u'C(64,5)', u'C(64,5)')]	|




### (2) Mistake Group ['R.0', 'R.1.0', 'R.1.1'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1.0', 'R.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|11*(11-1)*C(6,3)*C(6,2)/[C(66,5)]	|33000/(66^5)	|[('R.0', 33000.0, u'11*(11-1)*C(6,3)*C(6,2)', u'33000'), ('R.1.0', 66.0, u'66', u'66'), ('R.1.1', 5.0, u'5', u'5')]	|
|1	|16*(16-1)*C(6,3)*C(6,2)/[C(96,5)]	|16*15*C(6,3)*C(6,2)/(16*6*5)	|[('R.0', 72000.0, u'16*(16-1)*C(6,3)*C(6,2)', u'16*15*C(6,3)*C(6,2)'), ('R.1.0', 96.0, u'96', u'16*6'), ('R.1.1', 5.0, u'5', u'5')]	|




### (2) Mistake Group ['R.0.1.1', 'R.1'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1.1', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|14*(14-1)*C(6,3)*C(6,2)/[C(84,5)]	|[14*13*6^2*5^2*4^2] / [C(84,5)]	|[('R.0.1.1', 2.0, u'2', u'2'), ('R.1', 30872016, u'C(84,5)', u'C(84,5)')]	|
|1	|14*(14-1)*C(6,3)*C(6,2)/[C(84,5)]	|[14*13*6^2] / [C(84,5)]	|[('R.0.1.1', 2.0, u'2', u'2'), ('R.1', 30872016, u'C(84,5)', u'C(84,5)')]	|




### (1) Mistake Group ['R.1.0'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|13*(13-1)*C(6,3)*C(6,2)/[C(78,5)]	|(13*12*24)/C(78,6)	|[('R.1.0', 78.0, u'78', u'78')]	|




### (1) Mistake Group ['R.0.0.0', 'R.0.0.1.1', 'R.0.1.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0', 'R.0.0.1.1', 'R.0.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|14*(14-1)*C(5,3)*C(5,2)/[C(70,5)]	|(14*13*(5^3)*(5^2))/(70!/(65!/5!))	|[('R.0.0.0', 182.0, u'14*(14-1)', u'14*13'), ('R.0.0.1.1', 3.0, u'3', u'3'), ('R.0.1.1', 2.0, u'2', u'2')]	|




### (1) Mistake Group ['R.0.0.0'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|14*(14-1)*C(5,3)*C(5,2)/[C(70,5)]	|(14*13*(5^3-5)*(5^2-5))/(70!/(65!/5!))	|[('R.0.0.0', 182.0, u'14*(14-1)', u'14*13')]	|




### (1) Mistake Group ['R.0.0', 'R.0.1.1', 'R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.0.1.1', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|14*(14-1)*C(5,3)*C(5,2)/[C(70,5)]	|(14*13*C(5,3)*C(4,2))/C(14*5,5)	|[('R.0.0', 1820.0, u'14*(14-1)*C(5,3)', u'14*13*C(5,3)'), ('R.0.1.1', 2.0, u'2', u'2'), ('R.1', 12103014, u'C(70,5)', u'C(14*5,5)')]	|




### (1) Mistake Group ['R.0', 'R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|14*(14-1)*C(5,3)*C(5,2)/[C(70,5)]	|18200(70!/(5!65!))	|[('R.0', 18200.0, u'14*(14-1)*C(5,3)*C(5,2)', u'18200'), ('R.1', 12103014, u'C(70,5)', u'70!/(5!65!)')]	|




### (1) Mistake Group ['R.0.0.0.1', 'R.0.0.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0.1', 'R.0.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|16*(16-1)*C(6,3)*C(6,2)/[C(96,5)]	|[ 15*16* ( 6!/(2!4!) ) * ( 6!/(3!3!) )] / 96!/(5!91!)	|[('R.0.0.0.1', 15.0, u'16-1', u'6!/(2!4!)'), ('R.0.0.1', 20, u'C(6,3)', u'6!/(3!3!)')]	|




### (1) Mistake Group ['R.0.0.0', 'R.0.0.1.1', 'R.0.1.1', 'R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0', 'R.0.0.1.1', 'R.0.1.1', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|11*(11-1)*C(5,3)*C(5,2)/[C(55,5)]	|(11*10*C(5,1)^3*C(4,1)^2)/C(55,5)	|[('R.0.0.0', 110.0, u'11*(11-1)', u'11*10'), ('R.0.0.1.1', 3.0, u'3', u'3'), ('R.0.1.1', 2.0, u'2', u'2'), ('R.1', 3478761, u'C(55,5)', u'C(55,5)')]	|




### (1) Mistake Group ['R.0.1.1', 'R.1.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1.1', 'R.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|15*(15-1)*C(6,3)*C(6,2)/[C(90,5)]	|(C(15,3)+C(14,2))/C(15,5)	|[('R.0.1.1', 2.0, u'2', u'2'), ('R.1.1', 5.0, u'5', u'5')]	|




### (1) Mistake Group ['R.0.0.0', 'R.0.0.1.1', 'R.0.1.1', 'R.1.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0', 'R.0.0.1.1', 'R.0.1.1', 'R.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|15*(15-1)*C(6,3)*C(6,2)/[C(90,5)]	|(15*14*C(4,3)*C(4,2))/C(15,5)	|[('R.0.0.0', 210.0, u'15*(15-1)', u'15*14'), ('R.0.0.1.1', 3.0, u'3', u'3'), ('R.0.1.1', 2.0, u'2', u'2'), ('R.1.1', 5.0, u'5', u'5')]	|




### (1) Mistake Group ['R.0.0.1', 'R.0.1.1', 'R.1.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.1', 'R.0.1.1', 'R.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|15*(15-1)*C(6,3)*C(6,2)/[C(90,5)]	|(C(15,1)*C(14,2)*C(6,3)*C(6,1)^2)/C(78,5)	|[('R.0.0.1', 20, u'C(6,3)', u'C(6,3)'), ('R.0.1.1', 2.0, u'2', u'2'), ('R.1.1', 5.0, u'5', u'5')]	|




### (1) Mistake Group ['R.0.0.1.0', 'R.0.0.1.1', 'R.1.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.1.0', 'R.0.0.1.1', 'R.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|15*(15-1)*C(4,3)*C(4,2)/[C(60,5)]	|[[C(15, 1)*[C(4, 1)]^3]*[C(14, 1)*[C(4, 1)]^2]]/C(50, 5)	|[('R.0.0.1.0', 4.0, u'4', u'C(4, 1)'), ('R.0.0.1.1', 3.0, u'3', u'3'), ('R.1.1', 5.0, u'5', u'5')]	|




### (8) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:kquong

	first_attempt
					2015-10-11 05:44:02
	part1_correct_attempt
					['0:00:00', u'14']
	part2_correct_attempt
					['0:00:00', u'13']
	part3_correct_attempt
					['0:00:00', u'5!/(3!(5-3)!)']
	part4_correct_attempt
					['0:00:00', u'5!/(2!(5-2)!)']
	part5_correct_attempt
					['0:00:35', u'14 * 13 * 5!/(3!(5-3)!) * 5!/(2!(5-2)!)']
	part6_incorrect_attempt
					('0:00:35', u'(14 * 13 * 5!/(3!(5-3)!) * 5!/(2!(5-2)!))/ 70!/(5(70-5)!)')
					('0:00:45', u'(14 * 13 * 5!/(3!(5-3)!) * 5!/(2!(5-2)!))/ 70!/(5!*(70-5)!)')
	part6_correct_attempt
					['0:01:26', u'(14 * 13 * 5!/(3!(5-3)!) * 5!/(2!(5-2)!))/(70!/(5!*(70-5)!))']

1 Student ID:p4kumar

	first_attempt
					2015-10-15 10:31:31
	part1_correct_attempt
					['0:00:00', u'15']
	part2_correct_attempt
					['0:00:07', u'14']
	part3_correct_attempt
					['0:00:16', u'4']
	part4_correct_attempt
					['0:18:00', u'C(4, 2)']
	part5_correct_attempt
					['0:18:55', u'C(15, 1) * C(14, 1) * C(4, 3) * C(4, 2)']
	part6_incorrect_attempt
					('0:18:55', u'C(15, 1) * C(14, 1) * C(4, 3) * C(4, 2)')
	part6_correct_attempt
					['0:19:08', u'C(15, 1) * C(14, 1) * C(4, 3) * C(4, 2)/C(4 * 15, 5)']

2 Student ID:lywong

	first_attempt
					2015-10-13 00:56:44
	part1_correct_attempt
					['0:00:00', u'11']
	part2_correct_attempt
					['7:41:44', u'10']
	part3_correct_attempt
					['7:42:33', u'6!/((3!(3!)))']
	part4_correct_attempt
					['7:43:00', u'6!/(2!(4!))']
	part5_correct_attempt
					['7:44:13', u'33000']
	part6_incorrect_attempt
					('7:46:03', u'52!/47!')
	part6_correct_attempt
					['7:46:36', u'33000/(66!/(5!61!))']

3 Student ID:aurodrig

	first_attempt
					2015-10-15 21:31:50
	part1_correct_attempt
					['0:00:00', u'12']
	part2_correct_attempt
					['0:01:23', u'11']
	part3_correct_attempt
					['0:02:23', u'4!/(3!(4-3)!)']
	part4_correct_attempt
					['0:03:02', u'4!/(2!(4-2)!)']
	part5_correct_attempt
					['0:04:28', u'12*11*4*6']
	part6_incorrect_attempt
					('0:04:42', u'12*11*4*6')
	part6_correct_attempt
					['0:05:32', u'12*11*4*6/[48!/(5!43!)]']

4 Student ID:q3wen

	first_attempt
					2015-10-14 05:17:37
	part1_correct_attempt
					['0:00:00', u'10']
	part2_correct_attempt
					['0:00:00', u'9']
	part3_correct_attempt
					['-1 day, 23:58:55', u'20']
	part4_correct_attempt
					['-1 day, 23:58:55', u'15']
	part5_correct_attempt
					['0:00:00', u'27000']
	part6_incorrect_attempt
					('0:00:00', u'0.0049')
	part6_correct_attempt
					['0:01:35', u'27000/5461512']

5 Student ID:mnrahman

	first_attempt
					2015-10-15 07:04:17
	part1_correct_attempt
					['0:00:00', u'16']
	part2_correct_attempt
					['0:00:00', u'15']
	part3_correct_attempt
					['-1 day, 23:59:18', u'C(5,3)']
	part4_correct_attempt
					['0:00:19', u'C(5,2)']
	part5_correct_attempt
					['0:00:53', u'16*(16-1)C(5,3)C(5,2)']
	part6_incorrect_attempt
					('0:01:34', u'(916*(16-1)C(5,3)C(5,2))/(C(60,5))')
	part6_correct_attempt
					['0:02:46', u'(16*(16-1)C(5,3)C(5,2))/(C(80,5))']

6 Student ID:krau

	first_attempt
					2015-10-14 04:28:38
	part1_correct_attempt
					['0:00:00', u'16']
	part2_correct_attempt
					['0:00:31', u'15']
	part3_correct_attempt
					['0:01:19', u'4']
	part4_correct_attempt
					['0:01:19', u'6']
	part5_correct_attempt
					['0:01:19', u'16*15*4*6']
	part6_incorrect_attempt
					('0:01:19', u'16*15*4*6/64!/59!/5!')
	part6_correct_attempt
					['0:01:32', u'16*15*4*6/(64!/59!/5!)']

7 Student ID:mjethani

	first_attempt
					2015-10-15 15:00:44
	part1_correct_attempt
					['0:00:00', u'13']
	part2_correct_attempt
					['0:01:06', u'12']
	part3_correct_attempt
					['0:02:00', u'6!/((3!)(3!))']
	part4_correct_attempt
					['0:02:34', u'6!/((2!)(4!))']
	part5_correct_attempt
					['0:03:05', u'(13*12)(6!/((3!)(3!)))(6!/((2!)(4!)))']
	part6_incorrect_attempt
					('0:05:05', u'(13*12)(6!/((3!)(3!)))(6!/((2!)(4!)))/78')
	part6_correct_attempt
					['0:09:22', u'((13*12)(6!/((3!)(3!)))(6!/((2!)(4!))))/((78!)/((5!)(73!)))']












