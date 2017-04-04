#Problem 7

    $a=random(2,3,1);
    $n=Compute("P(26,$a)");
    $b=random(3,6,1);
    $b2=Compute("$b+2");
    $c=Compute("($b+1)*P(26,$a)+1");
    $cr=$c->eval();
    $d=Compute("($b-1)*P(26,$a)+1");
    $showHint = 3;

    Consider a list of randomly generated [$a]-letter "words" printed on a paper. The letters cannot be repeated.
    (a) What is the size of the set of allowed words?
    Answer = [__________]{Compute("P(26,$a)")}
    (b) At least how many of these "words" should be printed to be sure of having at least [$b] identical "words" on the list?
    Answer = [_______________]{Compute("($b-1)*P(26,$a)+1")}
    (c) At least how many identical "words" are printed if there are [`[$c]`] "words" on the list?
    Answer = [_______________]{Compute("$b+2")}



## Part 1

### (25) Mistake Group ['R.0', 'R.1'] of size 25
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|P(26,3)	|C(26,3)	|[('R.0', 26.0, u'26', u'26'), ('R.1', 3.0, u'3', u'3')]	|
|1	|P(26,3)	|26^3	|[('R.0', 26.0, u'26', u'26'), ('R.1', 3.0, u'3', u'3')]	|
|2	|P(26,2)	|26^2	|[('R.0', 26.0, u'26', u'26'), ('R.1', 2.0, u'2', u'2')]	|
|3	|P(26,2)	|C(26,2)	|[('R.0', 26.0, u'26', u'26'), ('R.1', 2.0, u'2', u'2')]	|
|4	|P(26,3)	|26**3	|[('R.0', 26.0, u'26', u'26'), ('R.1', 3.0, u'3', u'3')]	|




### (20) Mistake Group Digits of size 20




### (8) Mistake Group ['R.1'] of size 8
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|P(26,2)	|4*3*2	|[('R.1', 2.0, u'2', u'2')]	|
|1	|P(26,2)	|26*25*2	|[('R.1', 2.0, u'2', u'2')]	|
|2	|P(26,3)	|5*4*3	|[('R.1', 3.0, u'3', u'3')]	|
|3	|P(26,3)	|C(5,3)	|[('R.1', 3.0, u'3', u'3')]	|
|4	|P(26,2)	|5!/2!	|[('R.1', 2.0, u'2', u'2!')]	|
|5	|P(26,2)	|(26*25)/2	|[('R.1', 2.0, u'2', u'2')]	|




### (7) Mistake Group ['R.0'] of size 7
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|P(26,3)	|26!	|[('R.0', 26.0, u'26', u'26')]	|
|1	|P(26,2)	|26 * 24	|[('R.0', 26.0, u'26', u'26')]	|
|2	|P(26,2)	|26*252	|[('R.0', 26.0, u'26', u'26')]	|




### (32) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:phodgson

	first_attempt
					2015-10-13 02:07:32
	part1_incorrect_attempt
					('0:00:00', u'25*24')
					('0:00:34', u'24!')
	part1_correct_attempt
					['0:01:26', u'26*25']

1 Student ID:galu

	first_attempt
					2015-10-15 22:52:33
	part1_incorrect_attempt
					('0:00:00', u'26!*25!')
	part1_correct_attempt
					['0:00:24', u'26*25']

2 Student ID:kquong

	first_attempt
					2015-10-10 21:38:49
	part1_incorrect_attempt
					('0:00:00', u'3!')
					('0:02:03', u'27*26*25')
					('0:02:48', u'27!*26!*25!')
					('0:08:28', u'26! *25! * 24!')
	part1_correct_attempt
					['0:12:29', u'26 *25 * 24']

3 Student ID:vsamant

	first_attempt
					2015-10-10 00:39:29
	part1_incorrect_attempt
					('0:00:00', u'3!')
	part1_correct_attempt
					['0:08:49', u'26*25*24']

4 Student ID:kebao

	first_attempt
					2015-10-15 04:39:06
	part1_incorrect_attempt
					('0:00:00', u'28!/25!')
	part1_correct_attempt
					['0:00:34', u'26!/23!']

5 Student ID:abasu

	first_attempt
					2015-10-11 01:24:50
	part1_incorrect_attempt
					('0:00:00', u'27*26*25')
	part1_correct_attempt
					['0:00:31', u'26*25*24']

6 Student ID:fichoi

	first_attempt
					2015-10-14 01:19:22
	part1_incorrect_attempt
					('0:00:00', u'3^26')
	part1_correct_attempt
					['0:00:32', u'26*25*24']

7 Student ID:asp025

	first_attempt
					2015-10-13 06:49:56
	part1_incorrect_attempt
					('0:00:00', u'5!')
	part1_correct_attempt
					['2 days, 11:19:55', u'26*25']

8 Student ID:s1powers

	first_attempt
					2015-10-11 00:28:47
	part1_incorrect_attempt
					('0:00:00', u'26!/2')
					('0:00:22', u'26!/6')
	part1_correct_attempt
					['0:01:00', u'26*25*24']

9 Student ID:vsosnovs

	first_attempt
					2015-10-12 19:45:26
	part1_incorrect_attempt
					('0:00:00', u'3!')
	part1_correct_attempt
					['0:00:24', u'26*25*24']

10 Student ID:mbl003

	first_attempt
					2015-10-15 06:43:36
	part1_incorrect_attempt
					('0:00:00', u'28*27*26')
	part1_correct_attempt
					['0:00:23', u'26*25*24']

11 Student ID:s2chaudh

	first_attempt
					2015-10-11 20:40:21
	part1_incorrect_attempt
					('0:00:00', u'52*51')
	part1_correct_attempt
					['0:00:34', u'26*25']

12 Student ID:bmilton

	first_attempt
					2015-10-09 22:51:26
	part1_incorrect_attempt
					('0:00:00', u'3!')
	part1_correct_attempt
					['0:00:30', u'26*25*24']

13 Student ID:acvuong

	first_attempt
					2015-10-13 03:06:44
	part1_incorrect_attempt
					('0:00:00', u'3!')
	part1_correct_attempt
					['0:00:54', u'26*25*24']

14 Student ID:nnh002

	first_attempt
					2015-10-13 03:53:06
	part1_incorrect_attempt
					('0:00:00', u'27*26')
	part1_correct_attempt
					['1:44:49', u'26*25']

15 Student ID:s6deng

	first_attempt
					2015-10-13 22:58:21
	part1_incorrect_attempt
					('0:00:00', u'27*26')
	part1_correct_attempt
					['0:02:04', u'26*25']

16 Student ID:agian

	first_attempt
					2015-10-15 07:41:13
	part1_incorrect_attempt
					('0:00:00', u'26*25*24*23*2')
					('0:00:15', u'26*25*24*23*2+1')
					('0:00:27', u'26*25*24*23')
	part1_correct_attempt
					['0:01:03', u'26*25*24']

17 Student ID:jcl084

	first_attempt
					2015-10-13 18:02:05
	part1_incorrect_attempt
					('0:00:00', u'3!')
					('0:00:10', u'3*2')
	part1_correct_attempt
					['0:02:09', u'26 * 25 * 24']

18 Student ID:r1gu

	first_attempt
					2015-10-15 11:17:31
	part1_incorrect_attempt
					('0:00:00', u'3!')
	part1_correct_attempt
					['0:01:27', u'26*25*24']

19 Student ID:dsmonaha

	first_attempt
					2015-10-13 16:57:04
	part1_incorrect_attempt
					('0:00:00', u'26!25!')
					('0:00:19', u'26!26!')
	part1_correct_attempt
					['0:01:41', u'(26!/25!)(25!/24!)']

20 Student ID:ajabasa

	first_attempt
					2015-10-13 07:10:59
	part1_incorrect_attempt
					('0:00:00', u'26!+25!')
					('0:00:27', u'26!*25!')
	part1_correct_attempt
					['0:00:45', u'26*25']

21 Student ID:asetters

	first_attempt
					2015-10-12 02:18:09
	part1_incorrect_attempt
					('0:00:00', u'27*26')
	part1_correct_attempt
					['0:00:19', u'26*25']

22 Student ID:bakang

	first_attempt
					2015-10-15 01:04:14
	part1_incorrect_attempt
					('0:00:00', u'24*23')
	part1_correct_attempt
					['0:00:33', u'26*25']

23 Student ID:seleon

	first_attempt
					2015-10-14 04:09:01
	part1_incorrect_attempt
					('0:00:00', u'3!')
	part1_correct_attempt
					['0:00:17', u'26*25*24']

24 Student ID:dtea

	first_attempt
					2015-10-15 22:36:24
	part1_incorrect_attempt
					('0:00:00', u'3!')
					('0:00:09', u'3!/2')
	part1_correct_attempt
					['0:00:34', u'26*25*24']

25 Student ID:tdurrer

	first_attempt
					2015-10-09 03:53:26
	part1_incorrect_attempt
					('0:00:00', u'3!')
	part1_correct_attempt
					['0:00:59', u'C(26,3)*6']

26 Student ID:c1wei

	first_attempt
					2015-10-09 19:58:34
	part1_incorrect_attempt
					('0:00:00', u'4*3')
	part1_correct_attempt
					['0:00:54', u'26*25']

27 Student ID:starinia

	first_attempt
					2015-10-13 05:40:25
	part1_incorrect_attempt
					('0:00:00', u'26!/(3!23!)')
	part1_correct_attempt
					['0:00:25', u'26 * 25 * 24']

28 Student ID:lalacson

	first_attempt
					2015-10-11 15:49:46
	part1_incorrect_attempt
					('0:00:00', u'5!/2!')
	part1_correct_attempt
					['0:01:20', u'26!/(26-3)!']

29 Student ID:akg009

	first_attempt
					2015-10-15 21:36:42
	part1_incorrect_attempt
					('0:00:00', u'26*25*23')
	part1_correct_attempt
					['0:01:18', u'26*25*24']

30 Student ID:sthapa

	first_attempt
					2015-10-15 04:11:13
	part1_incorrect_attempt
					('0:00:00', u'5!/3!')
	part1_correct_attempt
					['0:04:00', u'26*25']

31 Student ID:skarimik

	first_attempt
					2015-10-09 08:26:05
	part1_incorrect_attempt
					('0:00:00', u'26!/(26-23)!')
	part1_correct_attempt
					['0:03:09', u'26!/(26-3)!']












## Part 2

### (111) Mistake Group Digits of size 111




### (25) Mistake Group Fraction of size 25




### (18) Mistake Group redirect of size 18




### (14) Mistake Group ['R.0.0'] of size 14
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(3-1)*P(26,3)+1	|2*25*24	|[('R.0.0', 2.0, u'3-1', u'2')]	|
|1	|(4-1)*P(26,2)+1	|(4-1)(26)+1	|[('R.0.0', 3.0, u'4-1', u'4-1')]	|
|2	|(4-1)*P(26,2)+1	|(3-1)*(26*25+1)	|[('R.0.0', 3.0, u'4-1', u'3')]	|
|3	|(5-1)*P(26,3)+1	|4(26) + 1	|[('R.0.0', 4.0, u'5-1', u'4')]	|
|4	|(3-1)*P(26,3)+1	|(3-1)26+1	|[('R.0.0', 2.0, u'3-1', u'3-1')]	|
|5	|(3-1)*P(26,3)+1	|(3-1)*3+1	|[('R.0.0', 2.0, u'3-1', u'3-1')]	|
|6	|(5-1)*P(26,3)+1	|4*26+1	|[('R.0.0', 4.0, u'5-1', u'4')]	|
|7	|(5-1)*P(26,3)+1	|((5-1)* 26) +1	|[('R.0.0', 4.0, u'5-1', u'5-1')]	|
|8	|(6-1)*P(26,2)+1	|(5*26)+1	|[('R.0.0', 5.0, u'6-1', u'5')]	|
|9	|(5-1)*P(26,2)+1	|4*630+1	|[('R.0.0', 4.0, u'5-1', u'4')]	|
|10	|(4-1)*P(26,2)+1	|(4 - 1)26 + 1	|[('R.0.0', 3.0, u'4-1', u'4 - 1')]	|
|11	|(5-1)*P(26,2)+1	|(5-1)26+1	|[('R.0.0', 4.0, u'5-1', u'5-1')]	|
|12	|(3-1)*P(26,3)+1	|(3-1) 3 + 1	|[('R.0.0', 2.0, u'3-1', u'3-1')]	|




### (13) Mistake Group ['R.0.0.0'] of size 13
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(4-1)*P(26,3)+1	|4*26*25*24	|[('R.0.0.0', 4.0, u'4', u'4')]	|
|1	|(4-1)*P(26,2)+1	|4*26*25+1	|[('R.0.0.0', 4.0, u'4', u'4')]	|
|2	|(3-1)*P(26,2)+1	|3*26*25 + 1	|[('R.0.0.0', 3.0, u'3', u'3')]	|
|3	|(3-1)*P(26,2)+1	|(3*26*25) + 1	|[('R.0.0.0', 3.0, u'3', u'3')]	|
|4	|(6-1)*P(26,2)+1	|6*25*26+1	|[('R.0.0.0', 6.0, u'6', u'6')]	|
|5	|(5-1)*P(26,3)+1	|5*26*25*24	|[('R.0.0.0', 5.0, u'5', u'5')]	|
|6	|(4-1)*P(26,3)+1	|(4-1)26+1	|[('R.0.0.0', 4.0, u'4', u'4')]	|
|7	|(3-1)*P(26,2)+1	|(3-1)2+1	|[('R.0.0.0', 3.0, u'3', u'3')]	|
|8	|(4-1)*P(26,3)+1	|(4-3)26+1	|[('R.0.0.0', 4.0, u'4', u'4')]	|
|9	|(3-1)*P(26,2)+1	|(3-1)23+1	|[('R.0.0.0', 3.0, u'3', u'3')]	|




### (10) Mistake Group ['R.0.1'] of size 10
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(4-1)*P(26,2)+1	|4(26!/((26-2)!)) + 1	|[('R.0.1', 650, u'P(26,2)', u'26!/((26-2)!)')]	|
|1	|(5-1)*P(26,2)+1	|5(26*25)+1	|[('R.0.1', 650, u'P(26,2)', u'26*25')]	|
|2	|(4-1)*P(26,3)+1	|4*(26*25*24) + 1	|[('R.0.1', 15600, u'P(26,3)', u'26*25*24')]	|
|3	|(5-1)*P(26,3)+1	|5* ( 26*25*24) + 1	|[('R.0.1', 15600, u'P(26,3)', u'26*25*24')]	|
|4	|(6-1)*P(26,3)+1	|2*[26*25*24]+1	|[('R.0.1', 15600, u'P(26,3)', u'26*25*24')]	|
|5	|(4-1)*P(26,2)+1	|(3-1)*(26*25)+1	|[('R.0.1', 650, u'P(26,2)', u'26*25')]	|
|6	|(3-1)*P(26,3)+1	|((3)[(26)(25)(24)])+1	|[('R.0.1', 15600, u'P(26,3)', u'(26)(25)(24)')]	|
|7	|(6-1)*P(26,3)+1	|(3 - 1)(26*25*24)+1	|[('R.0.1', 15600, u'P(26,3)', u'26*25*24')]	|
|8	|(3-1)*P(26,3)+1	|3*(26*25*24)+1	|[('R.0.1', 15600, u'P(26,3)', u'26*25*24')]	|
|9	|(4-1)*P(26,3)+1	|4(26!/23!) + 1	|[('R.0.1', 15600, u'P(26,3)', u'26!/23!')]	|




### (4) Mistake Group ['R.0.1.0'] of size 4
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(4-1)*P(26,3)+1	|4*26!/23!	|[('R.0.1.0', 26.0, u'26', u'26')]	|
|1	|(6-1)*P(26,2)+1	|2*(26-1)+6	|[('R.0.1.0', 26.0, u'26', u'26')]	|
|2	|(6-1)*P(26,2)+1	|2*(26-1)+1	|[('R.0.1.0', 26.0, u'26', u'26')]	|




### (2) Mistake Group Wrong_Sign of size 2




### (1) Mistake Group ['R.0.0.0', 'R.0.1.0'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0', 'R.0.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(4-1)*P(26,3)+1	|(4-1)26!+1	|[('R.0.0.0', 4.0, u'4', u'4'), ('R.0.1.0', 26.0, u'26', u'26')]	|




### (1) Mistake Group ['R.0'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(4-1)*P(26,2)+1	|26*25*3+4	|[('R.0', 1950.0, u'(4-1)*P(26,2)', u'26*25*3')]	|




### (1) Mistake Group ['R.0.1.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(4-1)*P(26,2)+1	|26 * 25^2 * 24^2 * 23	|[('R.0.1.1', 2.0, u'2', u'2')]	|




### (1) Mistake Group ['R.0.1.0', 'R.0.1.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1.0', 'R.0.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(5-1)*P(26,2)+1	|5(26^2)+1	|[('R.0.1.0', 26.0, u'26', u'26'), ('R.0.1.1', 2.0, u'2', u'2')]	|




### (1) Mistake Group ['R.0.0', 'R.0.1.0'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.0.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(5-1)*P(26,2)+1	|(5-1)(26*26)+1	|[('R.0.0', 4.0, u'5-1', u'5-1'), ('R.0.1.0', 26.0, u'26', u'26')]	|




### (162) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:gthorn

	first_attempt
					2015-10-13 17:01:08
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:14:11', u'650 * 5!')
	part2_correct_attempt
					['0:16:53', u'(5 - 1)650 + 1']

1 Student ID:kew060

	first_attempt
					2015-10-14 01:13:21
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:02:10', u'(26*25)+1')
	part2_correct_attempt
					['0:02:46', u'2(26*25)+1']

2 Student ID:kvass

	first_attempt
					2015-10-13 21:34:29
	part1_correct_attempt
					['0:00:00', u'26!/(26-3)!']
	part2_incorrect_attempt
					('0:03:25', u'(26-1)3+1')
					('0:05:35', u'(3-1)26+1')
	part2_correct_attempt
					['0:07:13', u'(4-1)26!/(26-3)!+1']

3 Student ID:ssamudra

	first_attempt
					2015-10-15 03:14:36
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('0:00:48', u'26 * 26* 26')
	part2_correct_attempt
					['0:03:15', u'2(26*25*24) + 1']

4 Student ID:alakamsa

	first_attempt
					2015-10-10 19:36:22
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('0:00:00', u'15600*3')
	part2_correct_attempt
					['0:03:39', u'(3-1)15600 +1']

5 Student ID:l5han

	first_attempt
					2015-10-14 05:07:24
	part1_correct_attempt
					['0:00:00', u'26!/23!']
	part2_incorrect_attempt
					('0:01:06', u'(26!/23!)^4')
	part2_correct_attempt
					['0:07:20', u'3*(26!/23!)+1']

6 Student ID:ctgraves

	first_attempt
					2015-10-13 00:23:51
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:00:29', u'650*4')
	part2_correct_attempt
					['0:00:36', u'650*3+1']

7 Student ID:dan029

	first_attempt
					2015-10-09 22:39:05
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:00:00', u'(26*25)^3')
	part2_correct_attempt
					['0:03:03', u'(26*25)*2+1']

8 Student ID:jyc018

	first_attempt
					2015-10-12 01:42:16
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('0:00:42', u'26*25*24 + 4')
					('0:04:38', u'26*25*24 + 5')
					('0:05:36', u'26*25*24*5')
	part2_correct_attempt
					['0:06:19', u'26*25*24*(5-1)+1']

9 Student ID:vqt004

	first_attempt
					2015-10-13 03:33:30
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:00:00', u'26*25*5+1')
	part2_correct_attempt
					['0:01:39', u'26*25*4+1']

10 Student ID:ffhaddad

	first_attempt
					2015-10-10 14:33:31
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('0:05:10', u'15600^5')
					('0:13:48', u'5*15600')
	part2_correct_attempt
					['0:15:44', u'4*15600+1']

11 Student ID:mnrahman

	first_attempt
					2015-10-15 07:45:33
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('0:00:36', u'26*25*2482+1')
					('0:01:10', u'(26*25*2482)+1')
	part2_correct_attempt
					['0:03:36', u'(26*25*24*3) + 1']

12 Student ID:btn023

	first_attempt
					2015-10-10 08:16:54
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('0:00:00', u'26*25*24*4')
	part2_correct_attempt
					['0:02:28', u'26*25*24*3+1']

13 Student ID:lalacson

	first_attempt
					2015-10-11 15:51:06
	part1_correct_attempt
					['0:00:00', u'26!/(26-3)!']
	part2_incorrect_attempt
					('0:02:42', u'(3-1)26+1')
	part2_correct_attempt
					['0:07:10', u'(4-1)(26!/(26-3)!)+1']

14 Student ID:dgunawan

	first_attempt
					2015-10-14 19:55:10
	part1_correct_attempt
					['0:00:00', u'26 * 25']
	part2_incorrect_attempt
					('0:04:00', u'5((26 *25) + 1)')
					('0:07:12', u'6((26 *25) + 1)')
					('0:07:48', u'((26 *25) + 1)')
					('0:11:39', u'6((26 *25))')
	part2_correct_attempt
					['0:12:56', u'5((26 *25))']

15 Student ID:tcn013

	first_attempt
					2015-10-13 05:32:52
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('0:00:36', u'26*25*24*4')
	part2_correct_attempt
					['1 day, 22:51:08', u'26*25*24*3+1']

16 Student ID:tstevens

	first_attempt
					2015-10-10 10:28:04
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('0:00:00', u'26*25*24+4')
	part2_correct_attempt
					['0:01:02', u'62401']

17 Student ID:pthsu

	first_attempt
					2015-10-10 19:10:01
	part1_correct_attempt
					['0:00:00', u'P(26,3)']
	part2_incorrect_attempt
					('0:01:32', u'P(26,3)+6')
	part2_correct_attempt
					['0:05:43', u'5*P(26,3)+1']

18 Student ID:tcuddy

	first_attempt
					2015-10-10 18:38:46
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('0:02:24', u'26*25*24 +4')
					('0:04:59', u'(26*25*24) + 4')
	part2_correct_attempt
					['0:10:29', u'(26*25*24)(4-1) +1']

19 Student ID:l8ngo

	first_attempt
					2015-10-09 16:24:17
	part1_correct_attempt
					['0:00:00', u'26 * 25* 24']
	part2_incorrect_attempt
					('0:00:00', u'[26 * 25* 24] ^ 6')
					('0:06:39', u'[26 * 25* 24]*6')
					('0:13:54', u'[26 * 25* 24] +1')
	part2_correct_attempt
					['0:15:25', u'[26 * 25* 24]*5 +1']

20 Student ID:djk006

	first_attempt
					2015-10-10 20:58:15
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:00:19', u'4(26*25)^2')
					('0:00:41', u'2(26*25)^2')
					('0:01:23', u'4(26*25)^2')
					('0:02:47', u'3(26*25+1)')
					('0:04:53', u'4(26*25+1)')
					('0:09:40', u'(4-1)((26*25)+1)')
	part2_correct_attempt
					['0:10:44', u'(4-1)((26*25))+1']

21 Student ID:chc286

	first_attempt
					2015-10-11 22:03:31
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:01:47', u'26*25*4+2')
					('0:02:05', u'26*25*4+4')
	part2_correct_attempt
					['0:05:48', u'26*25*3+1']

22 Student ID:glcohen

	first_attempt
					2015-10-13 04:34:04
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('0:01:05', u'5(26*25*24)')
	part2_correct_attempt
					['0:02:20', u'4(26*25*24+1)']

23 Student ID:anvan

	first_attempt
					2015-10-14 19:49:45
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('0:04:49', u'(26*25*24)*2 + 1')
	part2_correct_attempt
					['0:05:35', u'(26*25*24)4 + 1']

24 Student ID:csl030

	first_attempt
					2015-10-14 00:23:24
	part1_correct_attempt
					['0:00:00', u'26 * 25']
	part2_incorrect_attempt
					('0:00:00', u'(26 * 25) * 5')
	part2_correct_attempt
					['0:02:30', u'(26 * 25) * 4 + 1']

25 Student ID:achava

	first_attempt
					2015-10-12 05:11:21
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('1 day, 2:00:51', u'26*25*24')
	part2_correct_attempt
					['1 day, 2:01:37', u'3* 15601']

26 Student ID:arc013

	first_attempt
					2015-10-13 01:58:28
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('0:02:36', u'(26*25*24)^2')
	part2_correct_attempt
					['1 day, 0:50:05', u'(2*(26*25*24))+1']

27 Student ID:mitopete

	first_attempt
					2015-10-13 17:19:41
	part1_correct_attempt
					['0:00:00', u'26!/((26-3)!)']
	part2_incorrect_attempt
					('0:07:15', u'26!/(22!*4!)+26!/(23!*3!)+26!/(22!*4!)')
					('0:08:05', u'26!/(22!*4!)+26!/(23!*3!)+26!/(24!*2!)+26!/(25!*1!)+26!/(26!*0!)')
	part2_correct_attempt
					['0:10:30', u'(5-1)(15600+1)']

28 Student ID:starinia

	first_attempt
					2015-10-13 05:40:50
	part1_correct_attempt
					['0:00:00', u'26 * 25 * 24']
	part2_incorrect_attempt
					('0:44:42', u'26!/23! +3')
					('0:49:58', u'26!/23! +4')
	part2_correct_attempt
					['0:53:40', u'(4-1)15600 +1']

29 Student ID:tak068

	first_attempt
					2015-10-14 04:57:06
	part1_correct_attempt
					['0:00:00', u'2600*6']
	part2_incorrect_attempt
					('0:13:21', u'15600*(15600-1)*(15600-2)*(15600-3)')
					('0:14:55', u'15600^3')
					('0:15:01', u'15600^4')
	part2_correct_attempt
					['0:16:06', u'3*15600+1']

30 Student ID:jguanzho

	first_attempt
					2015-10-09 19:52:22
	part1_correct_attempt
					['0:00:00', u'26!/(23!)']
	part2_incorrect_attempt
					('0:36:09', u'26!/(23!) - 20!/17!')
	part2_correct_attempt
					['0:39:18', u'(6-1) * 26!/(23!) + 1']

31 Student ID:ggaddi

	first_attempt
					2015-10-10 06:17:59
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:00:00', u'26*25*4')
					('0:00:23', u'26*25+4')
					('0:02:43', u'26*25+3')
					('0:04:44', u'26*25*4')
					('0:05:47', u'3*(26*25+1)')
					('0:08:13', u'(4-1)*(26*25+1)')
	part2_correct_attempt
					['2 days, 10:28:02', u'(4-1)*(26*25)+1']

32 Student ID:jit002

	first_attempt
					2015-10-15 00:35:21
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('0:00:00', u'26*25*24+6')
	part2_correct_attempt
					['0:39:39', u'26*25*24*5+1']

33 Student ID:h4tu

	first_attempt
					2015-10-15 05:23:14
	part1_correct_attempt
					['0:00:00', u'26!/23!']
	part2_incorrect_attempt
					('0:01:25', u'(26!/23!)^5')
					('0:03:08', u'(26!/23!)*5')
					('0:03:53', u'(26!/23!)*5!')
	part2_correct_attempt
					['0:05:49', u'(26!/23!)*(5-1)+1']

34 Student ID:jag028

	first_attempt
					2015-10-14 23:31:17
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:00:54', u'3(26*25)')
					('0:03:11', u'26*26*26')
					('0:03:40', u'26*25*24')
					('0:03:50', u'26*25*24*23')
					('0:03:56', u'26*25*24*23*22')
					('0:04:10', u'26*25*26*26*26')
					('0:04:19', u'26*26*26')
					('0:05:01', u'26*25+1')
	part2_correct_attempt
					['0:06:24', u'26*25*2+1']

35 Student ID:ccn001

	first_attempt
					2015-10-12 21:07:07
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:00:38', u'4 * 26 * 25')
	part2_correct_attempt
					['0:03:17', u'(3)(650)+1']

36 Student ID:lguintu

	first_attempt
					2015-10-09 21:00:12
	part1_correct_attempt
					['0:00:00', u'26!/23!']
	part2_incorrect_attempt
					('0:02:52', u'26!/23!+3')
	part2_correct_attempt
					['0:03:47', u'26!/23!*3+1']

37 Student ID:jjchung

	first_attempt
					2015-10-14 18:52:45
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:01:48', u'(26^2)^3')
					('0:02:01', u'(26)^3')
	part2_correct_attempt
					['0:05:20', u'(26*25)*2 + 1']

38 Student ID:jcl084

	first_attempt
					2015-10-13 18:04:14
	part1_correct_attempt
					['0:00:00', u'26 * 25 * 24']
	part2_incorrect_attempt
					('0:00:25', u'15600 * 5 + 1')
					('0:00:57', u'15599 * 5 + 1')
	part2_correct_attempt
					['0:01:37', u'15600 * 4 + 1']

39 Student ID:skarimik

	first_attempt
					2015-10-09 08:29:14
	part1_correct_attempt
					['0:00:00', u'26!/(26-3)!']
	part2_incorrect_attempt
					('0:00:00', u'3(26!/(26-3)!)')
	part2_correct_attempt
					['0:03:18', u'2(26!/(26-3)!)+1']

40 Student ID:anislam

	first_attempt
					2015-10-15 08:48:31
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('13:56:39', u'26*25*24*6')
	part2_correct_attempt
					['13:56:46', u'26*25*24*5 + 1']

41 Student ID:sachadal

	first_attempt
					2015-10-09 18:06:02
	part1_correct_attempt
					['0:00:00', u'26!/((26-2)!)']
	part2_incorrect_attempt
					('0:01:45', u'4(26!/((26-2)!))')
	part2_correct_attempt
					['0:07:32', u'(4-1)(26!/((26-2)!))+1']

42 Student ID:kthui

	first_attempt
					2015-10-11 07:37:09
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:00:00', u'26*25+3')
	part2_correct_attempt
					['0:16:22', u'(3-1)(26*25)+1']

43 Student ID:mroknich

	first_attempt
					2015-10-13 18:17:46
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:02:41', u'26!/(20!)')
					('0:03:04', u'26!/(20!6!)')
	part2_correct_attempt
					['0:04:11', u'5(26*25)+1']

44 Student ID:tpmach

	first_attempt
					2015-10-11 00:52:35
	part1_correct_attempt
					['0:00:00', u'26!/(26-3)!']
	part2_incorrect_attempt
					('0:00:00', u'26^3+1')
					('0:00:14', u'3^26+1')
					('0:01:27', u'26*3+1')
					('0:03:10', u'26!*3+1')
					('0:03:44', u'25*3+1')
					('0:05:43', u'(26-1)*3+1')
					('0:07:22', u'(2-1)*3+1')
	part2_correct_attempt
					['0:08:24', u'(3-1)*15600+1']

45 Student ID:r1gu

	first_attempt
					2015-10-15 11:18:58
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('0:00:30', u'26*25*24*4')
	part2_correct_attempt
					['0:02:48', u'3(26*25*24)+1']

46 Student ID:hak014

	first_attempt
					2015-10-13 04:11:25
	part1_correct_attempt
					['0:00:00', u'26!/23!']
	part2_incorrect_attempt
					('0:04:41', u'15600*3+1')
					('0:05:32', u'15600*3')
					('0:08:44', u'21*5*21+20*5*21+19*5*21')
					('0:16:11', u'(26!/23!)^3')
	part2_correct_attempt
					['2 days, 14:37:24', u'(26*25*24)*2+1']

47 Student ID:jcj006

	first_attempt
					2015-10-13 20:18:27
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('0:01:06', u'5+26*25*24')
	part2_correct_attempt
					['0:01:36', u'4*26*25*24']

48 Student ID:dwzhang

	first_attempt
					2015-10-13 21:40:42
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:00:48', u'26*2+1')
	part2_correct_attempt
					['0:01:53', u'26*25*2 + 1']

49 Student ID:dis003

	first_attempt
					2015-10-15 10:46:31
	part1_correct_attempt
					['0:00:00', u'26 * 25']
	part2_incorrect_attempt
					('0:00:18', u'26*25  + 1')
					('0:00:32', u'26*25  **5 + 1')
					('0:00:51', u'26*25 **5 + 6')
					('0:01:53', u'26*25 * 24*23 * 22*21 * 20*19 * 18*17 * 16*15')
	part2_correct_attempt
					['0:05:31', u'(6-1)*(26*25)+1']

50 Student ID:rraiyyan

	first_attempt
					2015-10-14 05:35:35
	part1_correct_attempt
					['0:00:00', u'26!/23!']
	part2_incorrect_attempt
					('0:00:00', u'26!/23! + 5')
					('2:11:32', u'(26!/23!)^5')
	part2_correct_attempt
					['2:13:06', u'(26!/23!)*4 + 1']

51 Student ID:jhw015

	first_attempt
					2015-10-13 07:49:52
	part1_correct_attempt
					['0:00:00', u'26!/24!']
	part2_incorrect_attempt
					('0:02:32', u'650*6+1')
					('0:02:43', u'(650*6)+1')
	part2_correct_attempt
					['0:03:29', u'(650*5)+1']

52 Student ID:thwan

	first_attempt
					2015-10-09 23:21:31
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:10:12', u'26*25*6+1')
	part2_correct_attempt
					['0:12:39', u'(5-1)*26*25+1']

53 Student ID:krkelkar

	first_attempt
					2015-10-13 17:36:45
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('0:00:00', u'26*25*24 + 6')
					('9:40:20', u'6*(26*25*24)')
	part2_correct_attempt
					['9:41:40', u'1+5*(26*25*24)']

54 Student ID:jel075

	first_attempt
					2015-10-15 00:37:45
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:01:46', u'26*25*3')
	part2_correct_attempt
					['0:03:29', u'26*25*2+1']

55 Student ID:hmnaing

	first_attempt
					2015-10-12 05:06:50
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('0:00:00', u'C(26, 3)')
	part2_correct_attempt
					['0:45:54', u'((5-1)* (26*25*24)) +1']

56 Student ID:w4shin

	first_attempt
					2015-10-12 03:20:09
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:00:00', u'26*25+4')
	part2_correct_attempt
					['0:02:22', u'(26*25)*3+1']

57 Student ID:etemlock

	first_attempt
					2015-10-09 20:56:30
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:02:06', u'5*26*25')
					('0:02:20', u'(26*25)^5')
	part2_correct_attempt
					['0:04:02', u'4*26*25 + 1']

58 Student ID:muy002

	first_attempt
					2015-10-12 16:52:12
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('2 days, 6:07:20', u'26!/(5!21!)')
	part2_correct_attempt
					['2 days, 6:08:53', u'(5-1)(26*25)+1']

59 Student ID:wcwhite

	first_attempt
					2015-10-14 01:33:29
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:00:20', u'3*26*25')
	part2_correct_attempt
					['0:01:02', u'(3-1)26*25+1']

60 Student ID:j5phung

	first_attempt
					2015-10-09 17:27:48
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:01:12', u'(26*25)^6')
	part2_correct_attempt
					['0:02:33', u'(26*25)*5+1']

61 Student ID:eshung

	first_attempt
					2015-10-14 22:08:38
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('0:00:00', u'26*25*24*6')
					('0:06:40', u'15600^6')
	part2_correct_attempt
					['0:41:40', u'5*26*25*24 + 1']

62 Student ID:v4sharma

	first_attempt
					2015-10-13 23:59:39
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:03:13', u'26*25*4')
					('0:06:29', u'26 * 25 * 24 * 23')
					('0:08:48', u'26 * 25 * 24 * 23 * 22 * 21')
					('0:19:18', u'(26 - 1)4 + 1')
	part2_correct_attempt
					['0:21:08', u'(26*25)*(3) + 1']

63 Student ID:qfu

	first_attempt
					2015-10-09 04:09:51
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('0:02:10', u'2*25*24+1')
	part2_correct_attempt
					['0:11:28', u'15600*2+1']

64 Student ID:yjshin

	first_attempt
					2015-10-14 08:12:56
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:45:50', u'4*26')
					('0:49:21', u'4*651')
	part2_correct_attempt
					['0:52:30', u'(5-1)*650 + 1']

65 Student ID:sippolit

	first_attempt
					2015-10-12 03:08:30
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:03:07', u'(26*25)*4')
					('0:03:49', u'(26*25)*4-1')
					('0:05:07', u'(4-1)(26*25+1)')
	part2_correct_attempt
					['0:06:14', u'(4-1)*(26*25)+1']

66 Student ID:bpandayk

	first_attempt
					2015-10-15 22:24:01
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:00:30', u'650*3+1')
					('0:02:28', u'26*25*3+1')
	part2_correct_attempt
					['0:02:48', u'26*25*2+1']

67 Student ID:hsc052

	first_attempt
					2015-10-15 04:28:56
	part1_correct_attempt
					['0:00:00', u'25*26']
	part2_incorrect_attempt
					('0:12:06', u'(25*26)^6 + 1')
	part2_correct_attempt
					['0:18:35', u'5*(25*26) + 1']

68 Student ID:xil109

	first_attempt
					2015-10-10 18:43:15
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:02:03', u'26*25*5')
	part2_correct_attempt
					['0:04:57', u'(5-1)*650+1']

69 Student ID:v3doan

	first_attempt
					2015-10-11 01:12:34
	part1_correct_attempt
					['0:00:00', u'26! / 23!']
	part2_incorrect_attempt
					('0:00:00', u'26! / 23! + 1')
					('0:00:08', u'26! / 23!')
					('0:00:28', u'26! / 23! * 4 + 1')
	part2_correct_attempt
					['0:01:11', u'26! / 23! * 3 + 1']

70 Student ID:yil035

	first_attempt
					2015-10-13 22:53:56
	part1_correct_attempt
					['0:00:00', u'26!/23!']
	part2_incorrect_attempt
					('0:00:00', u'26!/21!')
					('0:00:43', u'26!/22!')
	part2_correct_attempt
					['0:06:42', u'62401']

71 Student ID:sghouse

	first_attempt
					2015-10-12 18:42:23
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('1:27:05', u'26*25+5')
	part2_correct_attempt
					['1:30:12', u'4*650+1']

72 Student ID:k3tan

	first_attempt
					2015-10-13 04:28:38
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:07:00', u'26*25+3')
	part2_correct_attempt
					['0:08:02', u'26*25*2+1']

73 Student ID:haw081

	first_attempt
					2015-10-10 22:30:51
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('0:03:14', u'3*26*25*24')
					('0:05:15', u'26*25*24')
	part2_correct_attempt
					['0:06:08', u'2(26*25*24)+1']

74 Student ID:lpettit

	first_attempt
					2015-10-13 18:02:05
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:00:58', u'650*3')
					('0:01:06', u'650*3 + 1')
	part2_correct_attempt
					['0:01:48', u'650*2 + 1']

75 Student ID:b3hwang

	first_attempt
					2015-10-15 21:12:09
	part1_correct_attempt
					['0:00:00', u'26 * 25']
	part2_incorrect_attempt
					('0:00:17', u'5((26 *25))')
					('0:00:34', u'4((26 *25))')
	part2_correct_attempt
					['0:01:56', u'3((26 *25))']

76 Student ID:jix029

	first_attempt
					2015-10-09 21:51:22
	part1_correct_attempt
					['0:00:00', u'26!/23!']
	part2_incorrect_attempt
					('20:07:01', u'26!*2/23+1')
					('20:08:20', u'26!*2/23+1')
	part2_correct_attempt
					['3 days, 22:19:59', u'26!*2/23!+1']

77 Student ID:kebao

	first_attempt
					2015-10-15 04:39:40
	part1_correct_attempt
					['0:00:00', u'26!/23!']
	part2_incorrect_attempt
					('0:00:41', u'4(26!/23!)')
	part2_correct_attempt
					['0:01:39', u'3(26!/23!) + 1']

78 Student ID:abasu

	first_attempt
					2015-10-11 01:25:21
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('0:01:05', u'(26*25*24)^3')
	part2_correct_attempt
					['0:01:45', u'2((26*25*24)+1)']

79 Student ID:acvuong

	first_attempt
					2015-10-13 03:07:38
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('0:00:00', u'26*25*24 + 1')
					('0:01:59', u'26*25*24')
	part2_correct_attempt
					['0:05:23', u'3*26*25*24 + 1']

80 Student ID:thk002

	first_attempt
					2015-10-12 00:33:48
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('0:17:04', u'P(26,3)')
	part2_correct_attempt
					['0:19:07', u'(4-1)(15601)']

81 Student ID:t2li

	first_attempt
					2015-10-14 03:19:21
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('0:06:37', u'26*25*24 *5 +1')
	part2_correct_attempt
					['0:07:39', u'26*25*24*(5-1) + 1']

82 Student ID:mtrafeca

	first_attempt
					2015-10-11 03:54:17
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('0:02:03', u'26*25*24*23*22')
					('0:03:03', u'25*5+1')
					('0:10:57', u'126*5')
					('0:14:30', u'(26*25*24*23*22 -1)*5 +1')
					('0:16:02', u'(26*25*24 -1)*5 +1')
	part2_correct_attempt
					['0:20:36', u'4*(26*25*24 ) +1']

83 Student ID:n2patil

	first_attempt
					2015-10-12 07:02:18
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:04:43', u'(5)*(26*25 +1)')
					('0:04:50', u'(5)*(26+1)')
	part2_correct_attempt
					['0:05:55', u'(5*26*25)+1']

84 Student ID:bakang

	first_attempt
					2015-10-15 01:04:47
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:00:00', u'26*25*6')
	part2_correct_attempt
					['0:04:47', u'26*25*5+1']

85 Student ID:ksmurlo

	first_attempt
					2015-10-13 23:02:56
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:00:00', u'(26*25)*5')
	part2_correct_attempt
					['0:00:27', u'(26*25)*4+1']

86 Student ID:ttimmons

	first_attempt
					2015-10-11 00:47:26
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('0:00:00', u'[26*25*24] - C(26,3)')
					('0:01:13', u'[26*25*24]')
	part2_correct_attempt
					['0:04:13', u'5*[26*25*24]+1']

87 Student ID:jblynch

	first_attempt
					2015-10-12 06:49:40
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:04:13', u'26*25 + 1')
					('0:04:56', u'4(26*25 + 1)')
	part2_correct_attempt
					['0:05:26', u'4(26*25)+1']

88 Student ID:nnh002

	first_attempt
					2015-10-13 05:37:55
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:00:00', u'6*25*26')
	part2_correct_attempt
					['0:06:20', u'5(25*26)+1']

89 Student ID:agian

	first_attempt
					2015-10-15 07:42:16
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('0:00:27', u'26*25*24+1')
					('0:00:34', u'26*25*24+1*2')
	part2_correct_attempt
					['0:00:40', u'26*25*24*2+1']

90 Student ID:tol003

	first_attempt
					2015-10-13 23:17:27
	part1_correct_attempt
					['0:00:00', u'P(26,3)']
	part2_incorrect_attempt
					('0:03:32', u'P(26,3)^3')
					('0:04:19', u'P(26,3)*P(26,2)*P(26,1)')
	part2_correct_attempt
					['0:14:14', u'31202']

91 Student ID:aakumar

	first_attempt
					2015-10-11 01:09:53
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:18:18', u'26*25')
					('0:28:17', u'3*651')
					('0:29:22', u'3*(26*25+1)')
					('0:31:37', u'3*((26*25)+1)')
	part2_correct_attempt
					['0:33:36', u'(4-1)*26*25+1']

92 Student ID:hachrist

	first_attempt
					2015-10-14 15:53:08
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:00:00', u'5*25*26')
	part2_correct_attempt
					['4:57:06', u'4*650 + 1']

93 Student ID:kew017

	first_attempt
					2015-10-15 05:35:24
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('0:00:00', u'3*26*25*24')
					('0:01:01', u'(26*25*24)^3')
	part2_correct_attempt
					['0:02:08', u'(26*25*24)*2+1']

94 Student ID:yeh013

	first_attempt
					2015-10-15 06:49:55
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('0:04:04', u'26*25*24*3')
					('0:04:55', u'26*25*24+1')
	part2_correct_attempt
					['0:05:36', u'26*25*24*2+1']

95 Student ID:jtfrankl

	first_attempt
					2015-10-15 20:36:35
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('0:00:00', u'3*26*25*24')
	part2_correct_attempt
					['0:02:18', u'1+2*26*25*24']

96 Student ID:kmc012

	first_attempt
					2015-10-11 22:07:04
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('3 days, 3:25:26', u'((26*25)^4)')
					('3 days, 3:27:20', u'5*26*25+1')
	part2_correct_attempt
					['3 days, 3:28:42', u'(650*3)+1']

97 Student ID:lahawkin

	first_attempt
					2015-10-14 04:26:36
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('0:08:43', u'26!/(20!)')
					('0:10:28', u'(26*25*24)+6')
					('0:10:39', u'(26*25*24)+7')
	part2_correct_attempt
					['0:12:13', u'(26*25*24+1)5']

98 Student ID:eaherman

	first_attempt
					2015-10-13 18:36:11
	part1_correct_attempt
					['0:00:00', u'(26)(25)']
	part2_incorrect_attempt
					('0:01:40', u'([(26)(25)])(4)')
					('0:03:51', u'(4-1)(650+1)')
					('0:07:07', u'(4)(650+1)')
	part2_correct_attempt
					['0:21:16', u'(4-1)(650)+1']

99 Student ID:fichoi

	first_attempt
					2015-10-14 01:19:54
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('0:01:27', u'(26*25*24)^6')
	part2_correct_attempt
					['0:12:25', u'(6 - 1)(26*25*24)+1']

100 Student ID:ksrijong

	first_attempt
					2015-10-15 04:27:26
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:00:00', u'4*26*25')
					('0:01:56', u'5*26*25')
	part2_correct_attempt
					['0:03:42', u'3*26*25+1']

101 Student ID:azkong

	first_attempt
					2015-10-15 15:51:29
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:00:00', u'6*26*25')
	part2_correct_attempt
					['0:01:45', u'5(26*25) + 1']

102 Student ID:volim

	first_attempt
					2015-10-12 22:06:54
	part1_correct_attempt
					['0:00:00', u'(26)(25)(24)']
	part2_incorrect_attempt
					('0:00:00', u'(3)(26)(25)(24)+1')
					('0:00:17', u'((3)(26)(25)(24))+1')
	part2_correct_attempt
					['0:03:10', u'(2)(26)(25)(24)+1']

103 Student ID:k4ma

	first_attempt
					2015-10-15 02:31:06
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:01:53', u'(26*25)^4')
					('0:04:58', u'(4+1)*(650+1)')
	part2_correct_attempt
					['0:05:58', u'650*(4-1)+1']

104 Student ID:aurodrig

	first_attempt
					2015-10-15 00:55:04
	part1_correct_attempt
					['0:00:00', u'26!/(26-2)!']
	part2_incorrect_attempt
					('0:03:51', u'(26-1)6+1')
					('0:07:53', u'(26-1)*2+1')
					('0:08:46', u'(2-1)*26+1')
					('0:09:41', u'(2-1)*26+6')
					('0:09:53', u'26*(2-1)+6')
	part2_correct_attempt
					['0:13:22', u'(6-1)* [26!/(26-2)!] + 1']

105 Student ID:cagatep

	first_attempt
					2015-10-14 01:11:22
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('0:00:31', u'26*25*24 * 6')
					('0:00:37', u'26*25*24 * 6 - 1')
	part2_correct_attempt
					['0:01:01', u'26*25*24 * 5 - 1']

106 Student ID:ytc012

	first_attempt
					2015-10-14 22:01:29
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:03:09', u'5*26')
	part2_correct_attempt
					['0:31:39', u'4*650+1']

107 Student ID:tjke

	first_attempt
					2015-10-11 21:30:59
	part1_correct_attempt
					['0:00:00', u'26!/(26-3)!']
	part2_incorrect_attempt
					('0:00:38', u'26!/(26-3)!*6')
					('0:00:48', u'(26!/(26-3)!)^6')
	part2_correct_attempt
					['0:04:08', u'(6-1)(26!/(26-3)!)+1']

108 Student ID:cprafull

	first_attempt
					2015-10-14 06:43:08
	part1_correct_attempt
					['0:00:00', u'26*(25)']
	part2_incorrect_attempt
					('0:00:00', u'(26*(25)) + 6')
					('0:00:18', u'(26*(25)) * 6')
	part2_correct_attempt
					['0:02:38', u'5(650) + 1']

109 Student ID:galu

	first_attempt
					2015-10-15 22:52:57
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:05:14', u'5*651')
	part2_correct_attempt
					['0:09:54', u'3251']

110 Student ID:kquong

	first_attempt
					2015-10-10 21:51:18
	part1_correct_attempt
					['0:00:00', u'26 *25 * 24']
	part2_incorrect_attempt
					('0:00:15', u'5* ( 26*25*24 + 1)')
					('0:02:17', u'26*25*24 + 5')
					('0:03:53', u'5(25)+ 1')
	part2_correct_attempt
					['0:06:26', u'15600 * 4+ 1']

111 Student ID:jfalcone

	first_attempt
					2015-10-14 21:36:24
	part1_correct_attempt
					['0:00:00', u'26 * 25']
	part2_incorrect_attempt
					('0:06:06', u'(26 * 25) *3')
	part2_correct_attempt
					['0:07:40', u'2(26*25 +1)']

112 Student ID:akhmelni

	first_attempt
					2015-10-15 22:09:54
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:00:53', u'(26*25)*3')
					('0:00:59', u'(26*25)*1.5')
	part2_correct_attempt
					['0:02:27', u'(3-1)(26*25)+1']

113 Student ID:vsamant

	first_attempt
					2015-10-10 00:48:18
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('0:09:34', u'26*25*24+1')
	part2_correct_attempt
					['0:17:32', u'3*26*25*24+1']

114 Student ID:ppanourg

	first_attempt
					2015-10-14 21:26:49
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:00:00', u'(26*25)*3')
					('0:02:41', u'(26*25)^3')
					('0:03:12', u'(26*25)*3')
	part2_correct_attempt
					['0:03:34', u'(26*25)*2 + 1']

115 Student ID:ewbrenna

	first_attempt
					2015-10-12 19:29:02
	part1_correct_attempt
					['0:00:00', u'26^2-26']
	part2_incorrect_attempt
					('0:06:58', u'(26^2-26)^5')
	part2_correct_attempt
					['0:08:02', u'(5-1)*(26^2-26) +1']

116 Student ID:qtluong

	first_attempt
					2015-10-12 07:35:08
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:00:00', u'(26*25)*6')
	part2_correct_attempt
					['0:00:30', u'(26*25)*5 + 1']

117 Student ID:spw006

	first_attempt
					2015-10-13 21:03:54
	part1_correct_attempt
					['0:00:00', u'26!/23!']
	part2_incorrect_attempt
					('0:01:27', u'26!/23! * 6')
					('0:01:38', u'26!/23! * 6 + 1')
	part2_correct_attempt
					['0:02:01', u'26!/23! * 5 + 1']

118 Student ID:any027

	first_attempt
					2015-10-09 09:26:44
	part1_correct_attempt
					['0:00:00', u'650']
	part2_incorrect_attempt
					('0:00:30', u'650 * 4')
					('0:01:37', u'(650 *4) +1')
	part2_correct_attempt
					['0:01:44', u'(650 *3) +1']

119 Student ID:s1powers

	first_attempt
					2015-10-11 00:29:47
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('0:00:36', u'5*15600')
	part2_correct_attempt
					['0:01:09', u'4*15600+1']

120 Student ID:pcdo

	first_attempt
					2015-10-13 18:15:43
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:01:38', u'6(26*25)')
	part2_correct_attempt
					['0:02:38', u'5(26*25)']

121 Student ID:e9brown

	first_attempt
					2015-10-14 07:30:47
	part1_correct_attempt
					['0:00:00', u'26 * 25 ']
	part2_incorrect_attempt
					('0:00:00', u'13*25')
					('0:00:46', u'13 * 5 * 25')
	part2_correct_attempt
					['0:51:45', u'4*26*25']

122 Student ID:vsosnovs

	first_attempt
					2015-10-12 19:45:50
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('0:01:46', u'26^3')
					('0:04:09', u'15600*3')
					('0:04:26', u'15600*3 + 1')
					('0:04:54', u'26!*25!*24!')
	part2_correct_attempt
					['0:05:45', u'2(15600) + 1']

123 Student ID:jdeon

	first_attempt
					2015-10-10 18:11:56
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('0:01:06', u'4*(26*25*24)')
	part2_correct_attempt
					['0:01:41', u'3*(26*25*24)+1']

124 Student ID:b1green

	first_attempt
					2015-10-15 20:24:07
	part1_correct_attempt
					['0:00:00', u'26!/(26-3)!']
	part2_incorrect_attempt
					('0:02:36', u'26*25*24*6')
					('0:03:22', u'26*25*24*6+1')
	part2_correct_attempt
					['0:05:48', u'26*25*24*5+1']

125 Student ID:p4kumar

	first_attempt
					2015-10-15 08:18:06
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:00:00', u'26*25*5 + 1')
	part2_correct_attempt
					['0:02:27', u'26*25*4 + 1']

126 Student ID:s2chaudh

	first_attempt
					2015-10-11 20:40:55
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:16:01', u'4*(26*25+1)')
	part2_correct_attempt
					['0:17:28', u'4*(26*25)']

127 Student ID:jmiclat

	first_attempt
					2015-10-15 02:51:30
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('0:00:12', u'26*6')
					('0:00:47', u'26!/20!')
	part2_correct_attempt
					['16:57:19', u'(5)(26*25*24)+1']

128 Student ID:gsrandha

	first_attempt
					2015-10-12 06:48:03
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:00:51', u'650*648*649')
					('0:00:56', u'650*649')
	part2_correct_attempt
					['23:13:31', u'(2)(650) + 1']

129 Student ID:bmilton

	first_attempt
					2015-10-09 22:51:56
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('0:00:29', u'26*25*24*4')
					('0:01:51', u'26*25*24*4 + 1')
	part2_correct_attempt
					['0:02:23', u'26*25*24*3 + 1']

130 Student ID:dcgriffi

	first_attempt
					2015-10-14 06:45:49
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('0:00:00', u'(26*25*24)+1')
					('0:00:37', u'(26*25*24)+3')
	part2_correct_attempt
					['0:01:56', u'(26*25*24)*2']

131 Student ID:cfgutier

	first_attempt
					2015-10-15 16:47:40
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:02:53', u'(26*25) * 5')
					('0:05:09', u'(5-1)((26*25)+1)')
					('0:06:22', u'4*651')
					('0:10:14', u'649*6')
	part2_correct_attempt
					['0:15:29', u'(4*26*25) + 1']

132 Student ID:anl114

	first_attempt
					2015-10-15 07:14:21
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('0:00:00', u'26*25*24*6')
					('0:00:27', u'(26*25*24)^6')
	part2_correct_attempt
					['0:02:04', u'26*25*24*5 + 1']

133 Student ID:agarango

	first_attempt
					2015-10-15 14:35:28
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('0:06:13', u'15600*6')
	part2_correct_attempt
					['0:07:35', u'15600*5+1']

134 Student ID:c1sorian

	first_attempt
					2015-10-14 21:53:56
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:03:59', u'3(2-1) + 1')
					('0:04:10', u'2(3-1) + 1')
					('0:08:36', u'26*25*3 + 1')
	part2_correct_attempt
					['0:08:54', u'26*25*2 + 1']

135 Student ID:achinn

	first_attempt
					2015-10-09 02:37:31
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('0:00:00', u'(26*25*24*3)+1')
					('0:01:30', u'(26*25*24)+3')
	part2_correct_attempt
					['3 days, 21:36:47', u'1+((26*25*24)*2)']

136 Student ID:kalang

	first_attempt
					2015-10-11 23:35:57
	part1_correct_attempt
					['0:00:00', u'26!/23!']
	part2_incorrect_attempt
					('0:00:00', u'26!/23! +3')
					('0:01:25', u'26!/23! *3')
	part2_correct_attempt
					['0:02:31', u'26!/23! *2 +1']

137 Student ID:msaguiar

	first_attempt
					2015-10-12 03:45:08
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:02:37', u'(26*25)+6')
					('0:06:58', u'(26*25)*6')
	part2_correct_attempt
					['0:11:04', u'5(26*25)+1']

138 Student ID:aalhaida

	first_attempt
					2015-10-15 14:10:02
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:02:24', u'650*3')
	part2_correct_attempt
					['0:19:23', u'650*2+1']

139 Student ID:hah008

	first_attempt
					2015-10-13 04:51:17
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('0:02:49', u'25(5)')
					('0:03:13', u'3(27)')
					('0:05:05', u'15599(5)')
					('0:08:38', u'15600*4 + 1')
					('0:08:53', u'15600*(4 + 1)')
					('0:10:40', u'15600*(3 + 1)')
	part2_correct_attempt
					['0:10:46', u'15600* 3 + 1']

140 Student ID:dlgoldbe

	first_attempt
					2015-10-13 00:39:31
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:01:44', u'26*25*5')
					('0:01:54', u'(26*25)^5')
	part2_correct_attempt
					['0:02:30', u'4*(26*25)+1']

141 Student ID:ajabasa

	first_attempt
					2015-10-13 07:11:44
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:02:43', u'26*25+5')
					('0:03:18', u'26*25+4')
	part2_correct_attempt
					['22:57:44', u'4*26*25+1']

142 Student ID:mcatozzi

	first_attempt
					2015-10-13 23:17:12
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('0:00:51', u'3*26')
	part2_correct_attempt
					['0:04:53', u'2*15600 +1']

143 Student ID:jnn015

	first_attempt
					2015-10-11 03:43:28
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:00:00', u'6*26*25')
	part2_correct_attempt
					['0:01:33', u'5*26*25 + 1']

144 Student ID:acs008

	first_attempt
					2015-10-14 21:50:04
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('0:01:23', u'(26-1)4+1')
	part2_correct_attempt
					['0:02:46', u'(4-1)26!/23!+1']

145 Student ID:dpereira

	first_attempt
					2015-10-10 05:34:17
	part1_correct_attempt
					['0:00:00', u'26! / 23!']
	part2_incorrect_attempt
					('0:01:10', u'26! / 23! + 6')
					('0:01:25', u'26! / 23! + 5')
					('0:04:53', u'26! / 23! + 7')
					('0:06:23', u'(26! / 23! + 1)6')
	part2_correct_attempt
					['0:07:16', u'(26! / 23! + 1)5']

146 Student ID:haliew

	first_attempt
					2015-10-13 17:29:20
	part1_correct_attempt
					['0:00:00', u'P(26,3)']
	part2_incorrect_attempt
					('0:00:00', u'P(26,3)^5')
	part2_correct_attempt
					['0:15:29', u'(4)(P(26,3)+1)']

147 Student ID:daw023

	first_attempt
					2015-10-14 22:42:46
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:02:21', u'26*25*5+1')
	part2_correct_attempt
					['0:04:30', u'26*25*4+1']

148 Student ID:edcole

	first_attempt
					2015-10-09 21:25:09
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:00:00', u'26^6')
					('0:01:02', u'(26*25)*6')
					('0:01:15', u'(26*25)^6')
	part2_correct_attempt
					['6 days, 1:25:14', u'26*25*5 +1']

149 Student ID:aordookh

	first_attempt
					2015-10-15 14:20:55
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('0:01:27', u'(15600*6)')
	part2_correct_attempt
					['0:02:20', u'(15600*5)+1']

150 Student ID:r2fisher

	first_attempt
					2015-10-14 22:38:41
	part1_correct_attempt
					['0:00:00', u'26!/24!']
	part2_incorrect_attempt
					('0:00:00', u'26*25')
					('0:00:06', u'26*26')
					('0:00:16', u'2^26')
					('0:01:23', u'2*640 +1')
	part2_correct_attempt
					['0:01:32', u'2*650 +1']

151 Student ID:vasharma

	first_attempt
					2015-10-10 02:31:49
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:08:09', u'26*25*3')
					('0:08:14', u'26*25*3+1')
	part2_correct_attempt
					['0:08:19', u'26*25*2+1']

152 Student ID:hpc001

	first_attempt
					2015-10-14 06:42:52
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('0:00:46', u'26*26*26')
					('0:01:18', u'26*23*20')
					('0:02:05', u'15600*3 + 1')
	part2_correct_attempt
					['0:02:26', u'15600*2 + 1']

153 Student ID:kosung

	first_attempt
					2015-10-15 05:19:46
	part1_correct_attempt
					['0:00:00', u'26 *25']
	part2_incorrect_attempt
					('0:00:00', u'26*25*24*23')
	part2_correct_attempt
					['17:19:00', u'26*25*3+1']

154 Student ID:xweng

	first_attempt
					2015-10-12 22:14:48
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('0:00:39', u'26*25*24*23*22')
	part2_correct_attempt
					['0:03:11', u'4*26*25*24+1']

155 Student ID:amquinte

	first_attempt
					2015-10-12 19:47:55
	part1_correct_attempt
					['0:00:00', u'26(25)']
	part2_incorrect_attempt
					('0:00:00', u'650^3')
					('0:01:20', u'650^2')
	part2_correct_attempt
					['0:06:19', u'1301']

156 Student ID:yypan

	first_attempt
					2015-10-12 20:16:07
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:00:57', u'(26*25)^3')
					('0:01:42', u'(26*25)*3')
	part2_correct_attempt
					['0:03:44', u'(26*25+1)*2']

157 Student ID:zhw110

	first_attempt
					2015-10-09 04:17:39
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('0:33:51', u'26*25*24+3')
	part2_correct_attempt
					['0:34:26', u'3*26*25*24+1']

158 Student ID:sthapa

	first_attempt
					2015-10-15 04:15:13
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:01:18', u'(23-1)3+1')
					('0:01:26', u'(26-1)3+1')
					('0:02:15', u'(26-1)23+1')
					('0:03:59', u'26*25*3+1')
	part2_correct_attempt
					['0:04:17', u'26*25*2+1']

159 Student ID:kgrozav

	first_attempt
					2015-10-15 18:12:22
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:04:53', u'5*((26*25)+1)')
	part2_correct_attempt
					['0:06:46', u'(5*26*25)+1']

160 Student ID:whcombs

	first_attempt
					2015-10-13 00:42:43
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_incorrect_attempt
					('0:05:24', u'650^5')
					('1:31:41', u'(26*25)*5')
					('1:35:12', u'(5-1)(650+1)')
	part2_correct_attempt
					['1:40:43', u'2601']

161 Student ID:j2phung

	first_attempt
					2015-10-13 19:20:38
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_incorrect_attempt
					('0:00:40', u'26*26*26')
	part2_correct_attempt
					['0:03:57', u'15600*2+1']












## Part 3

### (246) Mistake Group Digits of size 246




### (142) Mistake Group Fraction of size 142




### (29) Mistake Group redirect of size 29




### (9) Mistake Group Wrong_Sign of size 9




### (61) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:druble

	first_attempt
					2015-10-13 00:41:28
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_correct_attempt
					['0:00:00', u'(26*25)*(6-1) + 1']
	part3_incorrect_attempt
					('0:00:00', u'(4551 - 1) / (26*25)')
	part3_correct_attempt
					['0:00:56', u'(4551 - 1) / (26*25) + 1']

1 Student ID:dlgoldbe

	first_attempt
					2015-10-13 00:39:31
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_correct_attempt
					['0:02:30', u'4*(26*25)+1']
	part3_incorrect_attempt
					('0:03:20', u'(3901-1)/(26*25)')
	part3_correct_attempt
					['0:04:06', u'7']

2 Student ID:kquong

	first_attempt
					2015-10-10 21:51:18
	part1_correct_attempt
					['0:00:00', u'26 *25 * 24']
	part2_correct_attempt
					['0:06:26', u'15600 * 4+ 1']
	part3_incorrect_attempt
					('0:06:26', u'(93601 -1)/(26 *25*24)')
	part3_correct_attempt
					['0:07:12', u'(93601 -1)/15600 + 1']

3 Student ID:lpettit

	first_attempt
					2015-10-13 18:02:05
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_correct_attempt
					['0:01:48', u'650*2 + 1']
	part3_incorrect_attempt
					('0:03:20', u'2601 - 650')
	part3_correct_attempt
					['0:11:35', u'(2600/650) + 1']

4 Student ID:jag028

	first_attempt
					2015-10-14 23:31:17
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_correct_attempt
					['0:06:24', u'26*25*2+1']
	part3_incorrect_attempt
					('0:08:15', u'(26*25*2+1-1)2601+1')
	part3_correct_attempt
					['0:16:24', u'5']

5 Student ID:v4zhang

	first_attempt
					2015-10-15 05:59:08
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_correct_attempt
					['0:02:06', u'3(26*25*24)+1']
	part3_incorrect_attempt
					('0:02:06', u'3(26*25*24)')
					('0:05:23', u'78000(26*25*24)+1')
	part3_correct_attempt
					['0:07:35', u'78000/(26*25*24)+1']

6 Student ID:vsamant

	first_attempt
					2015-10-10 00:48:18
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_correct_attempt
					['0:17:32', u'3*26*25*24+1']
	part3_incorrect_attempt
					('0:17:32', u'78001-15600')
	part3_correct_attempt
					['0:18:39', u'6']

7 Student ID:kebao

	first_attempt
					2015-10-15 04:39:40
	part1_correct_attempt
					['0:00:00', u'26!/23!']
	part2_correct_attempt
					['0:01:39', u'3(26!/23!) + 1']
	part3_incorrect_attempt
					('0:02:54', u'78000/(26!/23!)')
	part3_correct_attempt
					['0:03:14', u'78000/(26!/23!)+1']

8 Student ID:lrlai

	first_attempt
					2015-10-10 22:33:32
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_correct_attempt
					['0:32:34', u'5*650 + 1']
	part3_incorrect_attempt
					('0:33:01', u'4550/650')
	part3_correct_attempt
					['0:33:19', u'8']

9 Student ID:lguintu

	first_attempt
					2015-10-09 21:00:12
	part1_correct_attempt
					['0:00:00', u'26!/23!']
	part2_correct_attempt
					['0:03:47', u'26!/23!*3+1']
	part3_incorrect_attempt
					('0:04:19', u'78000/(26!/23!)')
	part3_correct_attempt
					['0:06:10', u'78000/(26!/23!)+1']

10 Student ID:ssamudra

	first_attempt
					2015-10-15 03:14:36
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_correct_attempt
					['0:03:15', u'2(26*25*24) + 1']
	part3_incorrect_attempt
					('0:03:15', u'(62401 - 1)/(26*25*24)')

11 Student ID:ewbrenna

	first_attempt
					2015-10-12 19:29:02
	part1_correct_attempt
					['0:00:00', u'26^2-26']
	part2_correct_attempt
					['0:08:02', u'(5-1)*(26^2-26) +1']
	part3_incorrect_attempt
					('0:08:16', u'(5-1)*(3901) +1')
	part3_correct_attempt
					['0:10:21', u'7']

12 Student ID:qtluong

	first_attempt
					2015-10-12 07:35:08
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_correct_attempt
					['0:00:30', u'(26*25)*5 + 1']
	part3_incorrect_attempt
					('0:00:53', u'4550/(26*25)')
	part3_correct_attempt
					['0:01:08', u'4550/(26*25) + 1']

13 Student ID:asp025

	first_attempt
					2015-10-15 18:09:51
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_correct_attempt
					['0:03:12', u'2(651)']
	part3_incorrect_attempt
					('0:05:04', u'2601- 650')
					('0:05:16', u'2601- 1302')
					('0:06:04', u'1301(2602)')
					('0:06:19', u'1301(2601)')
					('0:08:19', u'8(2601)')
					('0:08:47', u'8(2602)')
					('0:09:53', u'650(2602)')
					('0:10:00', u'649(2602)')
					('0:13:19', u'2(2602)')
					('0:13:26', u'2(2601)')
					('0:18:13', u'(2603)')
					('1:17:05', u'650*10+1')
	part3_correct_attempt
					['1:22:01', u'5']

14 Student ID:jjm019

	first_attempt
					2015-10-15 21:58:12
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_correct_attempt
					['0:02:33', u'2*(26*25*24)']
	part3_incorrect_attempt
					('0:09:01', u'(62400/(26*25*24))-1')
	part3_correct_attempt
					['0:13:48', u'5']

15 Student ID:sachadal

	first_attempt
					2015-10-09 18:06:02
	part1_correct_attempt
					['0:00:00', u'26!/((26-2)!)']
	part2_correct_attempt
					['0:07:32', u'(4-1)(26!/((26-2)!))+1']
	part3_incorrect_attempt
					('0:07:32', u'(3251 - 1)/(26!/((26-2)!))')
	part3_correct_attempt
					['0:07:55', u'((3251 - 1)/(26!/((26-2)!)))+1']

16 Student ID:e9brown

	first_attempt
					2015-10-14 07:30:47
	part1_correct_attempt
					['0:00:00', u'26 * 25 ']
	part2_correct_attempt
					['0:51:45', u'4*26*25']
	part3_incorrect_attempt
					('0:51:45', u'3900/4')
					('0:52:06', u'3900/4 + 1')
					('0:52:48', u'3900/(26*25)')
	part3_correct_attempt
					['0:52:52', u'3900/(26*25) + 1']

17 Student ID:ielouaae

	first_attempt
					2015-10-15 07:14:18
	part1_correct_attempt
					['0:00:00', u'26!/23!']
	part2_correct_attempt
					['0:04:06', u'4(26!/23!+1)']
	part3_incorrect_attempt
					('0:07:08', u'(93601/26!/23!)+1')
					('0:08:59', u'(93600/26!/23!)+1')
	part3_correct_attempt
					['0:10:35', u'(93600/(26!/23!+1))+1']

18 Student ID:vsosnovs

	first_attempt
					2015-10-12 19:45:50
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_correct_attempt
					['0:05:45', u'2(15600) + 1']
	part3_incorrect_attempt
					('0:06:03', u'2(62401) + 1')
					('0:09:43', u'62400/4')
	part3_correct_attempt
					['0:09:53', u'5']

19 Student ID:dkurli

	first_attempt
					2015-10-13 07:28:01
	part1_correct_attempt
					['0:00:00', u'26!/23!']
	part2_correct_attempt
					['0:02:49', u'26!/23!*4']
	part3_incorrect_attempt
					('0:03:48', u'26!/23!*93600')
					('0:05:07', u'(26!/23!+1)*93600')
					('0:05:15', u'(26!/23!-1)*93602')
					('0:05:23', u'(26!/23!)*93602')
	part3_correct_attempt
					['0:10:08', u'7']

20 Student ID:beyounge

	first_attempt
					2015-10-09 05:15:57
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_correct_attempt
					['0:00:00', u'5*26*25*24+1']
	part3_incorrect_attempt
					('0:01:41', u'26*25*24')
	part3_correct_attempt
					['0:04:18', u'8']

21 Student ID:vasharma

	first_attempt
					2015-10-10 02:31:49
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_correct_attempt
					['0:08:19', u'26*25*2+1']
	part3_incorrect_attempt
					('0:15:52', u'2600/(26*25)')
	part3_correct_attempt
					['0:16:47', u'(2600/(26*25))+1']

22 Student ID:jic212

	first_attempt
					2015-10-11 22:35:23
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_correct_attempt
					['0:03:28', u'(4-1)*25*26*24+1']
	part3_incorrect_attempt
					('0:06:51', u'((78001-1)/26*25*24)+1')
	part3_correct_attempt
					['0:08:40', u'((78001-1)/(26*25*24))+1']

23 Student ID:jmiclat

	first_attempt
					2015-10-15 02:51:30
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_correct_attempt
					['16:57:19', u'(5)(26*25*24)+1']
	part3_incorrect_attempt
					('16:57:56', u'109200/(26*25*24)')
	part3_correct_attempt
					['16:58:28', u'109200/(26*25*24)+1']

24 Student ID:haw081

	first_attempt
					2015-10-10 22:30:51
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_correct_attempt
					['0:06:08', u'2(26*25*24)+1']
	part3_incorrect_attempt
					('0:06:08', u'62400/(26*25*24)')
	part3_correct_attempt
					['0:06:49', u'62400/(26*25*24)+1']

25 Student ID:jnatale

	first_attempt
					2015-10-13 01:05:23
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_correct_attempt
					['0:07:22', u'(2)(650) + 1']
	part3_incorrect_attempt
					('0:07:22', u'(2)(2601) + 1')
	part3_correct_attempt
					['0:09:50', u'5']

26 Student ID:dcgriffi

	first_attempt
					2015-10-14 06:45:49
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_correct_attempt
					['0:01:56', u'(26*25*24)*2']
	part3_incorrect_attempt
					('0:03:40', u'26*25*24')
					('0:09:12', u'(62400)/(26*25*24)')
	part3_correct_attempt
					['0:14:17', u'(62400)/(26*25*24) + 1']

27 Student ID:rsmurlo

	first_attempt
					2015-10-13 06:11:14
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_correct_attempt
					['18:25:37', u'26*25*24*5+1']
	part3_incorrect_attempt
					('18:29:15', u'109201-(26*25*24)')
	part3_correct_attempt
					['1 day, 22:51:32', u'(109201/(26*25*24))+1']

28 Student ID:jeqin

	first_attempt
					2015-10-15 12:06:43
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_correct_attempt
					['0:00:39', u'(26*25*24)*3 + 1']
	part3_incorrect_attempt
					('0:01:00', u'78000 / (26*25*24)')
	part3_correct_attempt
					['0:02:01', u'6']

29 Student ID:mnrahman

	first_attempt
					2015-10-15 07:45:33
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_correct_attempt
					['0:03:36', u'(26*25*24*3) + 1']
	part3_incorrect_attempt
					('0:04:27', u'78000/(26*25*24)')
	part3_correct_attempt
					['0:04:44', u'6']

30 Student ID:rlhagen

	first_attempt
					2015-10-11 17:17:40
	part1_correct_attempt
					['0:00:00', u'26!/(26-3)!']
	part2_correct_attempt
					['0:06:05', u'(6-1)(26!/(26-3)!+1)']
	part3_incorrect_attempt
					('0:07:24', u'(109201/26!/(26-3)!)+1')
	part3_correct_attempt
					['0:07:53', u'(109201/(26!/(26-3)!))+1']

31 Student ID:ganajera

	first_attempt
					2015-10-10 21:01:27
	part1_correct_attempt
					['0:00:00', u'P(26,2)']
	part2_correct_attempt
					['0:13:21', u'4*(P(26,2)) +1']
	part3_incorrect_attempt
					('0:13:29', u'(3900)/(P(26,2))')
					('0:13:59', u'((3900)/(P(26,2)))-1')
	part3_correct_attempt
					['0:16:15', u'7']

32 Student ID:nnh002

	first_attempt
					2015-10-13 05:37:55
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_correct_attempt
					['0:06:20', u'5(25*26)+1']
	part3_incorrect_attempt
					('10:52:33', u'(4551-1)/(26*25)')
	part3_correct_attempt
					['10:53:03', u'(4551-1)/(26*25) +1']

33 Student ID:ctgraves

	first_attempt
					2015-10-13 00:23:51
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_correct_attempt
					['0:00:36', u'650*3+1']
	part3_incorrect_attempt
					('0:01:22', u'3250/650')
	part3_correct_attempt
					['0:01:31', u'3250/650+1']

34 Student ID:lalacson

	first_attempt
					2015-10-11 15:51:06
	part1_correct_attempt
					['0:00:00', u'26!/(26-3)!']
	part2_correct_attempt
					['0:07:10', u'(4-1)(26!/(26-3)!)+1']
	part3_incorrect_attempt
					('0:07:21', u'(78001-1)/(26!/(26-3)!)')
	part3_correct_attempt
					['0:10:06', u'((78001-1)/(26!/(26-3)!))+1']

35 Student ID:agian

	first_attempt
					2015-10-15 07:42:16
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_correct_attempt
					['0:00:40', u'26*25*24*2+1']
	part3_incorrect_attempt
					('0:02:05', u'26*25*24*3')
					('0:02:09', u'26*25*24*4')
					('0:02:14', u'26*25*24*4+1')
	part3_correct_attempt
					['0:02:37', u'5']

36 Student ID:jcl084

	first_attempt
					2015-10-13 18:04:14
	part1_correct_attempt
					['0:00:00', u'26 * 25 * 24']
	part2_correct_attempt
					['0:01:37', u'15600 * 4 + 1']
	part3_incorrect_attempt
					('0:03:22', u'93600/15600')
	part3_correct_attempt
					['0:03:55', u'93600/15600 + 1']

37 Student ID:r1gu

	first_attempt
					2015-10-15 11:18:58
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_correct_attempt
					['0:02:48', u'3(26*25*24)+1']
	part3_incorrect_attempt
					('0:03:05', u'78000/(26*25*24)')
	part3_correct_attempt
					['0:05:13', u'6']

38 Student ID:t1tran

	first_attempt
					2015-10-10 05:33:23
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_correct_attempt
					['0:00:00', u'26*25*24*3+1']
	part3_incorrect_attempt
					('0:08:14', u'(78001-1)/(26*25*24)')
	part3_correct_attempt
					['0:09:23', u'(78001-1)/(26*25*24)+1']

39 Student ID:tcn013

	first_attempt
					2015-10-13 05:32:52
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_correct_attempt
					['1 day, 22:51:08', u'26*25*24*3+1']
	part3_incorrect_attempt
					('1 day, 22:52:21', u'78001-62400')
	part3_correct_attempt
					['1 day, 22:53:17', u'6']

40 Student ID:krkelkar

	first_attempt
					2015-10-13 17:36:45
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_correct_attempt
					['9:41:40', u'1+5*(26*25*24)']
	part3_incorrect_attempt
					('9:41:40', u'(109201-1)/(26*25*24)')
	part3_correct_attempt
					['9:42:04', u'1 + (109201-1)/(26*25*24)']

41 Student ID:tcuddy

	first_attempt
					2015-10-10 18:38:46
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_correct_attempt
					['0:10:29', u'(26*25*24)(4-1) +1']
	part3_incorrect_attempt
					('0:13:50', u'(26*25*24)(78001 -1) +1')
	part3_correct_attempt
					['0:20:49', u'78001/(26*25*24) + 1']

42 Student ID:l8ngo

	first_attempt
					2015-10-09 16:24:17
	part1_correct_attempt
					['0:00:00', u'26 * 25* 24']
	part2_correct_attempt
					['0:15:25', u'[26 * 25* 24]*5 +1']
	part3_incorrect_attempt
					('0:21:43', u'[ [109201 - 1] / 5 ] + 1')
	part3_correct_attempt
					['0:24:29', u'[ [109201 - 1] / [ 26 * 25* 24 ] ] + 1']

43 Student ID:sippolit

	first_attempt
					2015-10-12 03:08:30
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_correct_attempt
					['0:06:14', u'(4-1)*(26*25)+1']
	part3_incorrect_attempt
					('0:08:03', u'(7-1)*(26*25)+1')
	part3_correct_attempt
					['0:08:16', u'6']

44 Student ID:aysee

	first_attempt
					2015-10-13 17:49:10
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_correct_attempt
					['0:00:00', u'2*(26*25)+1']
	part3_incorrect_attempt
					('0:00:18', u'4*(26*25)')
	part3_correct_attempt
					['5:22:50', u'5']

45 Student ID:bakang

	first_attempt
					2015-10-15 01:04:47
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_correct_attempt
					['0:04:47', u'26*25*5+1']
	part3_incorrect_attempt
					('0:05:41', u'4550/26/25')
					('0:05:59', u'4550/(26*25)')
	part3_correct_attempt
					['0:06:46', u'4550/(26*25)+1']

46 Student ID:hmshah

	first_attempt
					2015-10-14 01:42:08
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_correct_attempt
					['0:01:08', u'5*650 + 1']
	part3_incorrect_attempt
					('0:01:08', u'5*650 + 1')
	part3_correct_attempt
					['1 day, 6:45:31', u'8']

47 Student ID:jtfrankl

	first_attempt
					2015-10-15 20:36:35
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_correct_attempt
					['0:02:18', u'1+2*26*25*24']
	part3_incorrect_attempt
					('0:03:02', u'62400/(26*25*24)')
	part3_correct_attempt
					['0:03:45', u'62400/(26*25*24)+1']

48 Student ID:csl030

	first_attempt
					2015-10-14 00:23:24
	part1_correct_attempt
					['0:00:00', u'26 * 25']
	part2_correct_attempt
					['0:02:30', u'(26 * 25) * 4 + 1']
	part3_incorrect_attempt
					('0:03:28', u'(26 * 25) * 3900 + 1')
					('0:05:57', u'(3901 - 1)3901')
					('0:12:39', u'3901 - 650')
					('0:12:54', u'3901 - 651')
					('0:13:01', u'3901 - 649')
	part3_correct_attempt
					['0:17:48', u'(3901 + (26*25) - 1)/ (26*25)']

49 Student ID:edcole

	first_attempt
					2015-10-09 21:25:09
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_correct_attempt
					['6 days, 1:25:14', u'26*25*5 +1']
	part3_incorrect_attempt
					('6 days, 1:31:22', u'4551-(26*25)')
	part3_correct_attempt
					['6 days, 1:43:11', u'8']

50 Student ID:ahh002

	first_attempt
					2015-10-09 05:54:21
	part1_correct_attempt
					['0:00:00', u'26!/23!']
	part2_correct_attempt
					['0:00:00', u'(26!/23!) * 5 + 1']
	part3_incorrect_attempt
					('0:00:00', u'109200 / (26!/23!)')
	part3_correct_attempt
					['1:08:32', u'(109201 - 1)/(26!/23!) + 1']

51 Student ID:aurodrig

	first_attempt
					2015-10-15 00:55:04
	part1_correct_attempt
					['0:00:00', u'26!/(26-2)!']
	part2_correct_attempt
					['0:13:22', u'(6-1)* [26!/(26-2)!] + 1']
	part3_incorrect_attempt
					('17:29:46', u'(6-1)* [26!/(26-2)!] + 1 + 1')
	part3_correct_attempt
					['17:43:51', u'(4551/650)+1']

52 Student ID:r2fisher

	first_attempt
					2015-10-14 22:38:41
	part1_correct_attempt
					['0:00:00', u'26!/24!']
	part2_correct_attempt
					['0:01:32', u'2*650 +1']
	part3_incorrect_attempt
					('0:01:51', u'2601-650')
					('0:02:10', u'(2601-1)/650')
	part3_correct_attempt
					['0:03:52', u'((2601-1)/650)+1']

53 Student ID:m4salaza

	first_attempt
					2015-10-15 23:10:04
	part1_correct_attempt
					['0:00:00', u'650']
	part2_correct_attempt
					['0:00:34', u'(5-1)*650+1']
	part3_incorrect_attempt
					('0:02:22', u'(3900/650 -1)')
	part3_correct_attempt
					['0:02:51', u'(3900/650 +1)']

54 Student ID:hpc001

	first_attempt
					2015-10-14 06:42:52
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_correct_attempt
					['0:02:26', u'15600*2 + 1']
	part3_incorrect_attempt
					('0:02:39', u'62401-31201 + 1')
					('0:02:48', u'62401-31201')
	part3_correct_attempt
					['0:03:08', u'62401/15600 + 1']

55 Student ID:xweng

	first_attempt
					2015-10-12 22:14:48
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_correct_attempt
					['0:03:11', u'4*26*25*24+1']
	part3_incorrect_attempt
					('0:03:35', u'26*25*24')
					('0:03:58', u'93601*26*25*24+1')
					('0:04:56', u'93601+1')
					('0:05:03', u'93601*4+1')
					('0:05:28', u'93600/15600')
	part3_correct_attempt
					['0:06:02', u'7']

56 Student ID:k4ma

	first_attempt
					2015-10-15 02:31:06
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_correct_attempt
					['0:05:58', u'650*(4-1)+1']
	part3_incorrect_attempt
					('0:07:00', u'3251*(2-1)+1')
	part3_correct_attempt
					['0:13:23', u'6']

57 Student ID:m8woo

	first_attempt
					2015-10-10 00:40:17
	part1_correct_attempt
					['0:00:00', u'26!/23!']
	part2_correct_attempt
					['0:00:00', u'2*(26!/23!)+1']
	part3_incorrect_attempt
					('0:01:14', u'62401 - 26!/23!')
					('0:01:59', u'26!/23!')
	part3_correct_attempt
					['0:02:14', u'5']

58 Student ID:sthapa

	first_attempt
					2015-10-15 04:15:13
	part1_correct_attempt
					['0:00:00', u'26*25']
	part2_correct_attempt
					['0:04:17', u'26*25*2+1']
	part3_incorrect_attempt
					('0:08:16', u'26*25*4 +1')
	part3_correct_attempt
					['0:09:33', u'5']

59 Student ID:bkoli

	first_attempt
					2015-10-14 10:46:33
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_correct_attempt
					['0:16:26', u'26*25*24*4+1']
	part3_incorrect_attempt
					('0:16:26', u'93601*4+1')
	part3_correct_attempt
					['8:25:21', u'93600/15600 +1']

60 Student ID:klala

	first_attempt
					2015-10-12 04:02:43
	part1_correct_attempt
					['0:00:00', u'26*25*24']
	part2_correct_attempt
					['0:00:00', u'(26*25*24)*2 + 1']
	part3_incorrect_attempt
					('0:00:00', u'62400 - (26*25*24)')
					('0:00:35', u'62401 - (26*25*24) + 1')
	part3_correct_attempt
					['0:05:00', u'5']












