#Problem 14

    $n2 = random(3,6,1);

    Lower case English letters are from "a-z". The order matters here. For example, "ab" is a different string from "ba". Repetition is allowed, i.e. the same letter can occur multiple times in a string.
    1. How many strings of length [$n2] consisting of lower case English letters are there?  [__________]{Compute("26**$n2")}
    2. How many strings of length [$n2] consisting of lower case English letters, **excluding the letter "x"**, are there? [__________]{Compute("25**$n2")}
    3. How many strings of length [$n2] consisting of lower case English letters, **and including at least one "x"**, are there? [__________]{Compute("26**$n2-25**$n2")}


## Part 1

### (40) Mistake Group Digits of size 40




### (12) Mistake Group ['R.0', 'R.1'] of size 12
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|26^6	|(26)(6)	|[('R.0', 26.0, u'26', u'26'), ('R.1', 6.0, u'6', u'6')]	|
|1	|26^6	|26*6	|[('R.0', 26.0, u'26', u'26'), ('R.1', 6.0, u'6', u'6')]	|
|2	|26^4	|P(26,4)	|[('R.0', 26.0, u'26', u'26'), ('R.1', 4.0, u'4', u'4')]	|
|3	|26^3	|P(26,3)	|[('R.0', 26.0, u'26', u'26'), ('R.1', 3.0, u'3', u'3')]	|
|4	|26^5	|C(26,5)	|[('R.0', 26.0, u'26', u'26'), ('R.1', 5.0, u'5', u'5')]	|
|5	|26^4	|C(26,4)	|[('R.0', 26.0, u'26', u'26'), ('R.1', 4.0, u'4', u'4')]	|
|6	|26^4	|26*4	|[('R.0', 26.0, u'26', u'26'), ('R.1', 4.0, u'4', u'4')]	|
|7	|26^5	|26*5	|[('R.0', 26.0, u'26', u'26'), ('R.1', 5.0, u'5', u'5')]	|
|8	|26^6	|P(26, 6)	|[('R.0', 26.0, u'26', u'26'), ('R.1', 6.0, u'6', u'6')]	|




### (7) Mistake Group ['R.0'] of size 7
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|26^4	|26^3	|[('R.0', 26.0, u'26', u'26')]	|
|1	|26^6	|26^5	|[('R.0', 26.0, u'26', u'26')]	|
|2	|26^5	|26^2	|[('R.0', 26.0, u'26', u'26')]	|
|3	|26^3	|26*26	|[('R.0', 26.0, u'26', u'26')]	|
|4	|26^3	|26*25	|[('R.0', 26.0, u'26', u'26')]	|
|5	|26^5	|26*5!	|[('R.0', 26.0, u'26', u'26')]	|




### (7) Mistake Group Fraction of size 7




### (3) Mistake Group ['R.1'] of size 3
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|26^4	|P((26*4),4)	|[('R.1', 4.0, u'4', u'4')]	|
|1	|26^4	|6^4	|[('R.1', 4.0, u'4', u'4')]	|
|2	|26^5	|(26!/5!)*5	|[('R.1', 5.0, u'5', u'5')]	|




### (49) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:a8ho

	first_attempt
					2015-10-07 05:50:21
	part1_incorrect_attempt
					('0:00:00', u'3^26')
	part1_correct_attempt
					['0:00:17', u'26^3']

1 Student ID:dmn009

	first_attempt
					2015-10-08 09:24:34
	part1_incorrect_attempt
					('0:00:00', u'6^26-6^25')
	part1_correct_attempt
					['0:07:34', u'26^6']

2 Student ID:starinia

	first_attempt
					2015-10-07 01:44:03
	part1_incorrect_attempt
					('0:00:00', u'26!/(4!(22!))')
	part1_correct_attempt
					['0:01:00', u'26^4']

3 Student ID:dpereira

	first_attempt
					2015-10-03 21:15:59
	part1_incorrect_attempt
					('0:00:00', u'26! / 22!')
	part1_correct_attempt
					['0:00:32', u'26^4']

4 Student ID:jag028

	first_attempt
					2015-10-08 18:45:30
	part1_incorrect_attempt
					('0:00:00', u'26!*26!')
					('0:00:48', u'26!*26!*26!*26!*26!*26!')
					('0:05:09', u'26!*25!*24!*23!*22!*21!')
	part1_correct_attempt
					['1:28:08', u'26^6']

5 Student ID:ccn001

	first_attempt
					2015-10-06 06:28:27
	part1_incorrect_attempt
					('0:00:00', u'(26!)/(5!)(26-5)!')
	part1_correct_attempt
					['0:03:43', u'26^5']

6 Student ID:vsamant

	first_attempt
					2015-10-02 17:18:49
	part1_incorrect_attempt
					('0:00:00', u'26!/((5!)(21!))')
	part1_correct_attempt
					['0:00:45', u'26^5']

7 Student ID:aportuga

	first_attempt
					2015-10-06 05:43:16
	part1_incorrect_attempt
					('0:00:00', u'26!/5!')
					('0:01:26', u'26!/(26-5)!')
					('0:00:00', u'26!/((26-5)!5!)')
					('0:02:09', u'((26-5)!/21!)')
	part1_correct_attempt
					['0:51:59', u'26^5']

8 Student ID:abjara

	first_attempt
					2015-10-05 23:04:49
	part1_incorrect_attempt
					('0:00:00', u'5^26')
	part1_correct_attempt
					['0:00:41', u'26^5']

9 Student ID:any027

	first_attempt
					2015-10-03 11:09:25
	part1_incorrect_attempt
					('0:00:00', u'(26! / (6! * (20!)) )')
	part1_correct_attempt
					['0:00:22', u'26^6']

10 Student ID:sachadal

	first_attempt
					2015-10-05 19:05:50
	part1_incorrect_attempt
					('0:00:00', u'26!/(26-4)!')
	part1_correct_attempt
					['0:02:24', u'26^4']

11 Student ID:awollner

	first_attempt
					2015-10-06 15:45:29
	part1_incorrect_attempt
					('0:00:00', u'26!/20!')
	part1_correct_attempt
					['0:02:42', u'26^6']

12 Student ID:kthui

	first_attempt
					2015-10-04 07:35:17
	part1_incorrect_attempt
					('0:00:00', u'26!/3!')
					('0:00:28', u'26!/(26-3)!')
	part1_correct_attempt
					['0:13:40', u'26*26*26']

13 Student ID:vsosnovs

	first_attempt
					2015-10-04 18:07:56
	part1_incorrect_attempt
					('0:00:00', u'26!/20!')
	part1_correct_attempt
					['0:08:24', u'26^6']

14 Student ID:alhung

	first_attempt
					2015-10-08 07:58:03
	part1_incorrect_attempt
					('0:00:00', u'26!/22!')
					('0:00:31', u'4^26')
	part1_correct_attempt
					['0:00:51', u'26^4']

15 Student ID:jfalcone

	first_attempt
					2015-10-07 03:48:13
	part1_incorrect_attempt
					('0:00:00', u'26!/(22!4!)')
	part1_correct_attempt
					['0:01:35', u'26 * 26 * 26 * 26']

16 Student ID:vasharma

	first_attempt
					2015-10-05 06:33:05
	part1_incorrect_attempt
					('0:00:00', u'26!/(26-4)!')
					('0:11:38', u'26!/4!(26-4)!')
					('0:11:45', u'26!/(4!(26-4)!)')
	part1_correct_attempt
					['0:12:04', u'26*26*26*26']

17 Student ID:tpmach

	first_attempt
					2015-10-03 22:00:48
	part1_incorrect_attempt
					('0:00:00', u'26!/(26-6)!')
	part1_correct_attempt
					['0:01:10', u'26^6']

18 Student ID:gsrandha

	first_attempt
					2015-10-02 02:08:50
	part1_incorrect_attempt
					('0:00:00', u'6*5*4*3*2')
	part1_correct_attempt
					['0:00:17', u'26*26*26*26*26*26']

19 Student ID:ctroncos

	first_attempt
					2015-10-08 05:50:16
	part1_incorrect_attempt
					('0:00:00', u'26!/(3!(26-3)!)')
					('0:00:11', u'26!/((26-3)!)')
					('0:01:22', u'26!/((26-2)!)')
					('0:01:30', u'26!/(2!(26-2)!)')
					('0:00:00', u'26!/(26-3)!')
					('0:00:18', u'26!/(3!(26-3)!)')
					('0:00:37', u'26*25*24')
					('0:01:23', u'26^3*3!')
	part1_correct_attempt
					['18:03:29', u'26^3']

20 Student ID:jew037

	first_attempt
					2015-10-06 02:24:44
	part1_incorrect_attempt
					('0:00:00', u'1.49*10^18')
	part1_correct_attempt
					['0:00:22', u'11881376']

21 Student ID:dkostins

	first_attempt
					2015-10-05 21:16:32
	part1_incorrect_attempt
					('0:00:00', u'6!')
					('0:00:00', u'6^26')
	part1_correct_attempt
					['4:37:06', u'26^6']

22 Student ID:jblynch

	first_attempt
					2015-10-05 04:34:38
	part1_incorrect_attempt
					('0:00:00', u'26!/21!')
	part1_correct_attempt
					['0:03:10', u'26^5']

23 Student ID:rlhagen

	first_attempt
					2015-10-04 22:54:32
	part1_incorrect_attempt
					('0:00:00', u'26!/(4!(26-4)!)')
					('0:00:12', u'26!/((26-4)!)')
	part1_correct_attempt
					['0:01:02', u'26^4']

24 Student ID:s6deng

	first_attempt
					2015-10-06 21:23:09
	part1_incorrect_attempt
					('0:00:00', u'5*(26^5)')
	part1_correct_attempt
					['0:00:09', u'26^5']

25 Student ID:r2fisher

	first_attempt
					2015-10-05 16:37:51
	part1_incorrect_attempt
					('0:00:00', u'3^26')
	part1_correct_attempt
					['4:09:19', u'26^3']

26 Student ID:dis003

	first_attempt
					2015-10-08 07:25:36
	part1_incorrect_attempt
					('0:00:00', u'5^26')
	part1_correct_attempt
					['0:00:41', u'26^5']

27 Student ID:kalang

	first_attempt
					2015-10-05 22:48:58
	part1_incorrect_attempt
					('0:00:00', u'26!/20!')
					('0:00:34', u'26!/(6!*20!)')
	part1_correct_attempt
					['0:01:07', u'26^6']

28 Student ID:hachrist

	first_attempt
					2015-10-04 22:44:44
	part1_incorrect_attempt
					('0:00:00', u'26!/(20!)')
	part1_correct_attempt
					['0:08:13', u'26^6']

29 Student ID:ksmurlo

	first_attempt
					2015-10-05 22:10:46
	part1_incorrect_attempt
					('0:00:00', u'26*26*26')
	part1_correct_attempt
					['1 day, 2:31:16', u'26*26*26*26*26']

30 Student ID:tcuddy

	first_attempt
					2015-10-02 20:23:28
	part1_incorrect_attempt
					('0:00:00', u'26*26*26')
	part1_correct_attempt
					['0:00:29', u'26**5']

31 Student ID:ajabasa

	first_attempt
					2015-10-05 21:32:45
	part1_incorrect_attempt
					('0:00:00', u'26!/22!')
	part1_correct_attempt
					['0:01:33', u'26^4']

32 Student ID:jel075

	first_attempt
					2015-10-08 00:48:32
	part1_incorrect_attempt
					('0:00:00', u'(26!/(22!))/4!')
					('0:00:26', u'(26!/(22!))')
					('0:01:41', u'26*25*24*23')
	part1_correct_attempt
					['0:04:38', u'26*26*26*26']

33 Student ID:ytc012

	first_attempt
					2015-10-06 09:51:49
	part1_incorrect_attempt
					('0:00:00', u'26!/(20!6!)')
	part1_correct_attempt
					['0:00:27', u'26^6']

34 Student ID:eaherman

	first_attempt
					2015-10-03 21:07:10
	part1_incorrect_attempt
					('0:00:00', u'4!')
	part1_correct_attempt
					['0:00:29', u'26^4']

35 Student ID:sayao

	first_attempt
					2015-10-03 00:41:11
	part1_incorrect_attempt
					('0:00:00', u'(26*4)!/7!')
	part1_correct_attempt
					['0:00:43', u'26^4']

36 Student ID:m4bui

	first_attempt
					2015-10-08 21:10:38
	part1_incorrect_attempt
					('0:00:00', u'26!25!24!23!22!')
					('0:03:19', u'26!/5!')
	part1_correct_attempt
					['0:06:18', u'26^5']

37 Student ID:muy002

	first_attempt
					2015-10-07 21:44:49
	part1_incorrect_attempt
					('0:00:00', u'26!/(4!*22!)')
					('0:03:59', u'26*25*24*23')
	part1_correct_attempt
					['0:10:39', u'26^4']

38 Student ID:wcwhite

	first_attempt
					2015-10-08 19:08:50
	part1_incorrect_attempt
					('0:00:00', u'4^26')
					('0:00:41', u'26*25*24*23')
	part1_correct_attempt
					['0:00:59', u'26^4']

39 Student ID:cstringh

	first_attempt
					2015-10-04 00:13:03
	part1_incorrect_attempt
					('0:00:00', u'4^26')
	part1_correct_attempt
					['0:00:18', u'26^4']

40 Student ID:ralhadda

	first_attempt
					2015-10-08 17:49:51
	part1_incorrect_attempt
					('0:00:00', u'(26*25*24)')
					('0:00:22', u'(26*25*24)/(3*2*1)')
	part1_correct_attempt
					['0:01:42', u'26*26*26']

41 Student ID:kquong

	first_attempt
					2015-10-03 21:30:17
	part1_incorrect_attempt
					('0:00:00', u'6^6')
	part1_correct_attempt
					['0:00:13', u'26^6']

42 Student ID:dcastlem

	first_attempt
					2015-10-03 21:48:46
	part1_incorrect_attempt
					('0:00:00', u'5!')
	part1_correct_attempt
					['0:27:37', u'26^5']

43 Student ID:kosung

	first_attempt
					2015-10-07 06:23:39
	part1_incorrect_attempt
					('0:00:00', u'24!/19!')
					('0:01:44', u'26!/21!')
	part1_correct_attempt
					['0:02:12', u'26^5']

44 Student ID:ajvanega

	first_attempt
					2015-10-02 22:53:31
	part1_incorrect_attempt
					('0:00:00', u'(26*25*24*23*22*21)')
					('0:00:00', u'((26*25*24*23*22*21)/(6*5*4*3*2))')
					('0:01:47', u'26!/(6!(20!))')
					('0:02:08', u'26!/(6!(26-6)!)')
					('0:04:27', u'26!/6!')
					('0:35:32', u'26!/(6!*(26-6)!)')
	part1_correct_attempt
					['5 days, 0:49:38', u'26^6']

45 Student ID:hmnaing

	first_attempt
					2015-10-07 02:57:56
	part1_incorrect_attempt
					('0:00:00', u'C(26,5)*1')
	part1_correct_attempt
					['15:10:57', u'26^5']

46 Student ID:mtrafeca

	first_attempt
					2015-10-02 06:10:03
	part1_incorrect_attempt
					('0:00:00', u'26*25*24*23*22')
	part1_correct_attempt
					['0:06:46', u'26^5']

47 Student ID:syc078

	first_attempt
					2015-10-08 19:35:35
	part1_incorrect_attempt
					('0:00:00', u'26*25*24*23*22*21')
	part1_correct_attempt
					['3:45:28', u'26^6']

48 Student ID:whcombs

	first_attempt
					2015-10-07 19:49:54
	part1_incorrect_attempt
					('0:00:00', u'(26!)/(6!(26-6)!)')
					('0:00:31', u'(26!)/((26-6)!)')
					('0:04:03', u'(26!)/(6!(26-6)!)')
	part1_correct_attempt
					['0:05:15', u'26^6']












## Part 2

### (10) Mistake Group Digits of size 10




### (6) Mistake Group ['R.0', 'R.1'] of size 6
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|25^6	|(25)(6)	|[('R.0', 25.0, u'25', u'25'), ('R.1', 6.0, u'6', u'6')]	|
|1	|25^4	|P(25,4)	|[('R.0', 25.0, u'25', u'25'), ('R.1', 4.0, u'4', u'4')]	|
|2	|25^5	|C(25,5)	|[('R.0', 25.0, u'25', u'25'), ('R.1', 5.0, u'5', u'5')]	|
|3	|25^4	|C(25,4)	|[('R.0', 25.0, u'25', u'25'), ('R.1', 4.0, u'4', u'4')]	|




### (3) Mistake Group Fraction of size 3




### (2) Mistake Group ['R.1'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|25^4	|P((25*4),4)	|[('R.1', 4.0, u'4', u'4')]	|
|1	|25^5	|24^5	|[('R.1', 5.0, u'5', u'5')]	|




### (29) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:a8ho

	first_attempt
					2015-10-07 05:50:38
	part2_incorrect_attempt
					('-1 day, 23:59:43', u'3^25')
	part2_correct_attempt
					['0:00:00', u'25^3']

1 Student ID:r2fisher

	first_attempt
					2015-10-05 20:47:10
	part2_incorrect_attempt
					('-1 day, 19:50:41', u'3^25')
	part2_correct_attempt
					['0:00:00', u'25^3']

2 Student ID:ccn001

	first_attempt
					2015-10-06 06:32:10
	part2_incorrect_attempt
					('-1 day, 23:56:17', u'25!/(5!(20!))')
	part2_correct_attempt
					['0:00:00', u'25^5']

3 Student ID:vsamant

	first_attempt
					2015-10-02 17:19:34
	part2_incorrect_attempt
					('-1 day, 23:59:15', u'25!/((5!)(20!))')
	part2_correct_attempt
					['0:00:00', u'25^5']

4 Student ID:abjara

	first_attempt
					2015-10-05 23:05:30
	part2_incorrect_attempt
					('-1 day, 23:59:19', u'5^25')
	part2_correct_attempt
					['0:00:00', u'25^5']

5 Student ID:sachadal

	first_attempt
					2015-10-05 19:08:14
	part2_incorrect_attempt
					('-1 day, 23:57:36', u'25!/(25-4)!')
	part2_correct_attempt
					['0:00:21', u'25^4']

6 Student ID:awollner

	first_attempt
					2015-10-06 15:48:11
	part2_incorrect_attempt
					('-1 day, 23:57:18', u'25!/19!')
	part2_correct_attempt
					['0:00:00', u'25^6']

7 Student ID:vsosnovs

	first_attempt
					2015-10-04 18:16:20
	part2_incorrect_attempt
					('0:00:12', u'26^5')
	part2_correct_attempt
					['0:00:20', u'25^6']

8 Student ID:alhung

	first_attempt
					2015-10-08 07:58:54
	part2_incorrect_attempt
					('-1 day, 23:59:09', u'25!/21!')
					('-1 day, 23:59:40', u'4^25')
	part2_correct_attempt
					['0:00:00', u'25^4']

9 Student ID:ksmurlo

	first_attempt
					2015-10-07 00:42:02
	part2_incorrect_attempt
					('-2 days, 21:28:44', u'25*25*25')
	part2_correct_attempt
					['0:00:33', u'25*25*25*25*25']

10 Student ID:jyc018

	first_attempt
					2015-10-05 16:10:20
	part2_incorrect_attempt
					('0:00:00', u'3*26**3')
					('0:02:26', u'25*3*26**3')
					('0:02:48', u'25*3*25**3')
					('0:03:08', u'25*4*25**3')
	part2_correct_attempt
					['0:03:35', u'25**4']

11 Student ID:jblynch

	first_attempt
					2015-10-05 04:37:48
	part2_incorrect_attempt
					('-1 day, 23:56:50', u'25!/20!')
	part2_correct_attempt
					['0:00:00', u'25^5']

12 Student ID:rlhagen

	first_attempt
					2015-10-04 22:55:34
	part2_incorrect_attempt
					('-1 day, 23:58:58', u'25!/(4!(25-4)!)')
					('-1 day, 23:59:10', u'25!/((25-4)!)')
	part2_correct_attempt
					['0:00:00', u'25^4']

13 Student ID:dis003

	first_attempt
					2015-10-08 07:26:17
	part2_incorrect_attempt
					('-1 day, 23:59:19', u'5^25')
	part2_correct_attempt
					['0:00:00', u'25^5']

14 Student ID:kalang

	first_attempt
					2015-10-05 22:50:05
	part2_incorrect_attempt
					('-1 day, 23:58:53', u'25!/19!')
	part2_correct_attempt
					['0:00:09', u'25^6']

15 Student ID:hachrist

	first_attempt
					2015-10-04 22:52:57
	part2_incorrect_attempt
					('-1 day, 23:51:31', u'25!/(19! 6!)')
	part2_correct_attempt
					['0:00:07', u'25^6']

16 Student ID:kew017

	first_attempt
					2015-10-04 20:16:52
	part2_incorrect_attempt
					('0:00:00', u'26^4')
					('0:00:17', u'2*26^4')
	part2_correct_attempt
					['0:00:41', u'25^5']

17 Student ID:tcuddy

	first_attempt
					2015-10-02 20:23:57
	part2_incorrect_attempt
					('-1 day, 23:59:31', u'25*25*25')
	part2_correct_attempt
					['0:00:00', u'25**5']

18 Student ID:ctroncos

	first_attempt
					2015-10-08 23:53:45
	part2_incorrect_attempt
					('-1 day, 23:58:46', u'26^2*25')
					('0:00:07', u'26^2*25*3!')
	part2_correct_attempt
					['0:02:16', u'25^3']

19 Student ID:dpereira

	first_attempt
					2015-10-03 21:16:31
	part2_incorrect_attempt
					('-1 day, 23:59:28', u'25! / 21!')
	part2_correct_attempt
					['0:00:00', u'25^4']

20 Student ID:mitopete

	first_attempt
					2015-10-06 04:38:09
	part2_incorrect_attempt
					('0:00:42', u'26^3-(2600)')
					('0:01:53', u'26^3-25^3')
	part2_correct_attempt
					['0:02:53', u'25^3']

21 Student ID:starinia

	first_attempt
					2015-10-07 01:45:03
	part2_incorrect_attempt
					('0:00:00', u'26^4 - 4!')
	part2_correct_attempt
					['0:02:54', u'25^4']

22 Student ID:aportuga

	first_attempt
					2015-10-06 06:35:15
	part2_incorrect_attempt
					('-1 day, 23:23:33', u'25!/(25-5)!')
	part2_correct_attempt
					['0:00:22', u'25^5']

23 Student ID:kosung

	first_attempt
					2015-10-07 06:25:51
	part2_incorrect_attempt
					('-1 day, 23:59:32', u'25!/20!')
	part2_correct_attempt
					['0:00:37', u'25^5']

24 Student ID:ajvanega

	first_attempt
					2015-10-07 23:43:09
	part2_incorrect_attempt
					('0:08:55', u'(26^1)*(25^6)')
	part2_correct_attempt
					['0:09:06', u'25^6']

25 Student ID:zig006

	first_attempt
					2015-10-06 00:43:44
	part2_incorrect_attempt
					('0:00:00', u'26^4-4*26^3')
	part2_correct_attempt
					['0:00:27', u'25^4']

26 Student ID:ralhadda

	first_attempt
					2015-10-08 17:51:33
	part2_incorrect_attempt
					('0:00:13', u'26*25*24')
	part2_correct_attempt
					['0:00:35', u'25*25*25']

27 Student ID:mtrafeca

	first_attempt
					2015-10-02 06:16:49
	part2_incorrect_attempt
					('0:25:59', u'4!')
	part2_correct_attempt
					['0:26:12', u'25^5']

28 Student ID:syc078

	first_attempt
					2015-10-08 23:21:03
	part2_incorrect_attempt
					('-1 day, 20:14:32', u'25*24*23*22*21*20')
	part2_correct_attempt
					['0:00:14', u'25^6']












## Part 3

### (137) Mistake Group ['R.0.0'] of size 137
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|26^5-25^5	|26**4 *5	|[('R.0.0', 26.0, u'26', u'26')]	|
|1	|26^4-25^4	|26!/((4!)(22!))	|[('R.0.0', 26.0, u'26', u'26')]	|
|2	|26^4-25^4	|26!/((4!))	|[('R.0.0', 26.0, u'26', u'26')]	|
|3	|26^5-25^5	|26!/(22!*4!)	|[('R.0.0', 26.0, u'26', u'26')]	|
|4	|26^5-25^5	|26!/(21!*5!)	|[('R.0.0', 26.0, u'26', u'26')]	|
|5	|26^5-25^5	|(26^4)*5	|[('R.0.0', 26.0, u'26', u'26')]	|
|6	|26^5-25^5	|26! / (4! * 22!)	|[('R.0.0', 26.0, u'26', u'26')]	|
|7	|26^5-25^5	|26^4 * 5	|[('R.0.0', 26.0, u'26', u'26')]	|
|8	|26^5-25^5	|26! / (5! * 21!)	|[('R.0.0', 26.0, u'26', u'26')]	|
|9	|26^6-25^6	|(26^5)*6	|[('R.0.0', 26.0, u'26', u'26')]	|
|10	|26^6-25^6	|26^5*6	|[('R.0.0', 26.0, u'26', u'26')]	|
|11	|26^6-25^6	|26^5*5	|[('R.0.0', 26.0, u'26', u'26')]	|
|12	|26^5-25^5	|26**4-1	|[('R.0.0', 26.0, u'26', u'26')]	|
|13	|26^5-25^5	|26**4*5	|[('R.0.0', 26.0, u'26', u'26')]	|
|14	|26^3-25^3	|26*25*25	|[('R.0.0', 26.0, u'26', u'26')]	|
|15	|26^3-25^3	|26* 25* 24	|[('R.0.0', 26.0, u'26', u'26')]	|
|16	|26^3-25^3	|26^2*3	|[('R.0.0', 26.0, u'26', u'26')]	|
|17	|26^6-25^6	|26! / 22!	|[('R.0.0', 26.0, u'26', u'26')]	|
|18	|26^6-25^6	|(26^5)(6!)	|[('R.0.0', 26.0, u'26', u'26')]	|
|19	|26^6-25^6	|(26^5)(6)	|[('R.0.0', 26.0, u'26', u'26')]	|
|20	|26^6-25^6	|(26!)/(5!)	|[('R.0.0', 26.0, u'26', u'26')]	|
|21	|26^3-25^3	|(26!/(24!*2!))	|[('R.0.0', 26.0, u'26', u'26')]	|
|22	|26^4-25^4	|(26^3)(4)	|[('R.0.0', 26.0, u'26', u'26')]	|
|23	|26^4-25^4	|26! / 23!	|[('R.0.0', 26.0, u'26', u'26')]	|
|24	|26^4-25^4	|(26^3)-24	|[('R.0.0', 26.0, u'26', u'26')]	|
|25	|26^4-25^4	|(26^3) * 4	|[('R.0.0', 26.0, u'26', u'26')]	|
|26	|26^5-25^5	|26^2*25	|[('R.0.0', 26.0, u'26', u'26')]	|
|27	|26^5-25^5	|(26*2)(26^2)	|[('R.0.0', 26.0, u'26', u'26')]	|
|28	|26^3-25^3	|26 * 26 * 3	|[('R.0.0', 26.0, u'26', u'26')]	|
|29	|26^3-25^3	|26! / (23!3!)	|[('R.0.0', 26.0, u'26', u'26')]	|
|30	|26^6-25^6	|26!/(20! 6!)	|[('R.0.0', 26.0, u'26', u'26')]	|
|31	|26^4-25^4	|26!/(26-3)!	|[('R.0.0', 26.0, u'26', u'26')]	|
|32	|26^5-25^5	|26^4+5	|[('R.0.0', 26.0, u'26', u'26')]	|
|33	|26^6-25^6	|[26^5]*6	|[('R.0.0', 26.0, u'26', u'26')]	|
|34	|26^5-25^5	|26!/22!	|[('R.0.0', 26.0, u'26', u'26')]	|
|35	|26^3-25^3	|1 * 26 * 26 * 6	|[('R.0.0', 26.0, u'26', u'1 * 26')]	|
|36	|26^3-25^3	|1 * 26 * 26 * 3	|[('R.0.0', 26.0, u'26', u'1 * 26')]	|
|37	|26^3-25^3	|(26^2) * 6	|[('R.0.0', 26.0, u'26', u'26')]	|
|38	|26^3-25^3	|(26^2) * 3	|[('R.0.0', 26.0, u'26', u'26')]	|
|39	|26^3-25^3	|(26^2) ^ 3	|[('R.0.0', 26.0, u'26', u'26')]	|
|40	|26^3-25^3	|26*26*(3!)	|[('R.0.0', 26.0, u'26', u'26')]	|
|41	|26^4-25^4	|[(26^3)(4)]	|[('R.0.0', 26.0, u'26', u'26')]	|
|42	|26^5-25^5	|1*26*26*3	|[('R.0.0', 26.0, u'26', u'1*26')]	|
|43	|26^4-25^4	|(26!)/(4!*(22!))	|[('R.0.0', 26.0, u'26', u'26')]	|
|44	|26^4-25^4	|(26!)/(1!*(23!))	|[('R.0.0', 26.0, u'26', u'26')]	|
|45	|26^5-25^5	|26^4 + 1	|[('R.0.0', 26.0, u'26', u'26')]	|
|46	|26^5-25^5	|26!/(4!(26-4)!)	|[('R.0.0', 26.0, u'26', u'26')]	|
|47	|26^5-25^5	|26^4*5	|[('R.0.0', 26.0, u'26', u'26')]	|
|48	|26^5-25^5	|26!/(26-4)!	|[('R.0.0', 26.0, u'26', u'26')]	|
|49	|26^6-25^6	|26^5-6!	|[('R.0.0', 26.0, u'26', u'26')]	|
|50	|26^6-25^6	|26^5-6	|[('R.0.0', 26.0, u'26', u'26')]	|
|51	|26^6-25^6	|26^5-324000	|[('R.0.0', 26.0, u'26', u'26')]	|
|52	|26^3-25^3	|26*26*25	|[('R.0.0', 26.0, u'26', u'26')]	|
|53	|26^6-25^6	|26!/21!	|[('R.0.0', 26.0, u'26', u'26')]	|
|54	|26^5-25^5	|26^4*((5!)/(4!(5-4)!))	|[('R.0.0', 26.0, u'26', u'26')]	|
|55	|26^5-25^5	|26^4*((5!)/((5-4)!))	|[('R.0.0', 26.0, u'26', u'26')]	|
|56	|26^6-25^6	|(26^5)^6	|[('R.0.0', 26.0, u'26', u'26')]	|
|57	|26^6-25^6	|(26^5)+6	|[('R.0.0', 26.0, u'26', u'26')]	|
|58	|26^4-25^4	|26^3*25	|[('R.0.0', 26.0, u'26', u'26')]	|
|59	|26^6-25^6	|26^5+25	|[('R.0.0', 26.0, u'26', u'26')]	|
|60	|26^4-25^4	|[26^3]*3	|[('R.0.0', 26.0, u'26', u'26')]	|
|61	|26^4-25^4	|[26^3]*4	|[('R.0.0', 26.0, u'26', u'26')]	|
|62	|26^5-25^5	|(26^4)*4	|[('R.0.0', 26.0, u'26', u'26')]	|
|63	|26^5-25^5	|(26^4)*6	|[('R.0.0', 26.0, u'26', u'26')]	|
|64	|26^5-25^5	|(26^4)5	|[('R.0.0', 26.0, u'26', u'26')]	|
|65	|26^5-25^5	|(26^4)(5!)	|[('R.0.0', 26.0, u'26', u'26')]	|
|66	|26^6-25^6	|26!/(5!21!)	|[('R.0.0', 26.0, u'26', u'26')]	|
|67	|26^6-25^6	|(26^5)*25	|[('R.0.0', 26.0, u'26', u'26')]	|
|68	|26^6-25^6	|(26^5)25	|[('R.0.0', 26.0, u'26', u'26')]	|
|69	|26^4-25^4	|26*25^3*4	|[('R.0.0', 26.0, u'26', u'26')]	|
|70	|26^4-25^4	|(26^3)*4	|[('R.0.0', 26.0, u'26', u'26')]	|
|71	|26^3-25^3	|26*26*6	|[('R.0.0', 26.0, u'26', u'26')]	|
|72	|26^3-25^3	|26*26*1	|[('R.0.0', 26.0, u'26', u'26')]	|
|73	|26^3-25^3	|(26^2)3	|[('R.0.0', 26.0, u'26', u'26')]	|
|74	|26^3-25^3	|(1*26*26)*3	|[('R.0.0', 26.0, u'26', u'1*26')]	|
|75	|26^3-25^3	|(26*26)*3	|[('R.0.0', 26.0, u'26', u'26')]	|
|76	|26^3-25^3	|(26*26)^3	|[('R.0.0', 26.0, u'26', u'26')]	|
|77	|26^3-25^3	|(26^2)*3	|[('R.0.0', 26.0, u'26', u'26')]	|
|78	|26^5-25^5	|(26!)/((5!)*(21!))	|[('R.0.0', 26.0, u'26', u'26')]	|
|79	|26^3-25^3	|26*26*3	|[('R.0.0', 26.0, u'26', u'26')]	|
|80	|26^3-25^3	|1 * 26 * 26 * (3!/2!*1!)	|[('R.0.0', 26.0, u'26', u'1 * 26')]	|
|81	|26^3-25^3	|1 * 26 * 1 * (3!/2!*1!)  + 1 * 26 * 25 * (3!/2!*1!)	|[('R.0.0', 26.0, u'26', u'1 * 26 * 1')]	|
|82	|26^3-25^3	|1 * 26 * 1 * (3!/(2!*1!)) + 1 * 26 * 25 * (3!/(2!*1!))	|[('R.0.0', 26.0, u'26', u'1 * 26 * 1')]	|
|83	|26^6-25^6	|26^5 * 25	|[('R.0.0', 26.0, u'26', u'26')]	|
|84	|26^4-25^4	|26!/23!	|[('R.0.0', 26.0, u'26', u'26')]	|
|85	|26^6-25^6	|(26^5) * 6	|[('R.0.0', 26.0, u'26', u'26')]	|
|86	|26^3-25^3	|26*25*24	|[('R.0.0', 26.0, u'26', u'26')]	|
|87	|26^3-25^3	|26*26*3!	|[('R.0.0', 26.0, u'26', u'26')]	|
|88	|26^4-25^4	|26^3 * 4	|[('R.0.0', 26.0, u'26', u'26')]	|
|89	|26^6-25^6	|26^5 - 25	|[('R.0.0', 26.0, u'26', u'26')]	|
|90	|26^6-25^6	|26^5*25	|[('R.0.0', 26.0, u'26', u'26')]	|
|91	|26^5-25^5	|26^4 * 4	|[('R.0.0', 26.0, u'26', u'26')]	|
|92	|26^4-25^4	|26**3*4	|[('R.0.0', 26.0, u'26', u'26')]	|
|93	|26^4-25^4	|26**3*3	|[('R.0.0', 26.0, u'26', u'26')]	|
|94	|26^3-25^3	|26^2 * 3	|[('R.0.0', 26.0, u'26', u'26')]	|
|95	|26^3-25^3	|26^2*3!	|[('R.0.0', 26.0, u'26', u'26')]	|
|96	|26^3-25^3	|26^2*2!	|[('R.0.0', 26.0, u'26', u'26')]	|
|97	|26^3-25^3	|26^2 +1	|[('R.0.0', 26.0, u'26', u'26')]	|




### (86) Mistake Group Digits of size 86




### (46) Mistake Group Fraction of size 46




### (43) Mistake Group Wrong_Sign of size 43




### (32) Mistake Group ['R.0'] of size 32
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|26^5-25^5	|26^5-2	|[('R.0', 11881376.0, u'26^5', u'26^5')]	|
|1	|26^5-25^5	|(26^5)*5	|[('R.0', 11881376.0, u'26^5', u'26^5')]	|
|2	|26^4-25^4	|(26^4)*4	|[('R.0', 456976.0, u'26^4', u'26^4')]	|
|3	|26^5-25^5	|26^5-24^5	|[('R.0', 11881376.0, u'26^5', u'26^5')]	|
|4	|26^5-25^5	|26^5-5	|[('R.0', 11881376.0, u'26^5', u'26^5')]	|
|5	|26^6-25^6	|(26^6)-(26^5)	|[('R.0', 308915776.0, u'26^6', u'26^6')]	|
|6	|26^5-25^5	|26^5 - 1	|[('R.0', 11881376.0, u'26^5', u'26^5')]	|
|7	|26^6-25^6	|(26^6)-(6^2)	|[('R.0', 308915776.0, u'26^6', u'26^6')]	|
|8	|26^5-25^5	|(26^5)-2115751	|[('R.0', 11881376.0, u'26^5', u'26^5')]	|
|9	|26^5-25^5	|(26^5)-(26^5-25^5)	|[('R.0', 11881376.0, u'26^5', u'26^5')]	|
|10	|26^5-25^5	|26^5 - 2	|[('R.0', 11881376.0, u'26^5', u'26^5')]	|
|11	|26^6-25^6	|26^6-6	|[('R.0', 308915776.0, u'26^6', u'26^6')]	|
|12	|26^6-25^6	|26^6-324000	|[('R.0', 308915776.0, u'26^6', u'26^6')]	|
|13	|26^5-25^5	|26^5-26^4	|[('R.0', 11881376.0, u'26^5', u'26^5')]	|
|14	|26^6-25^6	|(26^6)^6	|[('R.0', 308915776.0, u'26^6', u'26^6')]	|
|15	|26^4-25^4	|26^4 - 4!	|[('R.0', 456976.0, u'26^4', u'26^4')]	|
|16	|26^6-25^6	|26^6-21^6	|[('R.0', 308915776.0, u'26^6', u'26^6')]	|
|17	|26^3-25^3	|(26*26*26) - 3	|[('R.0', 17576.0, u'26^3', u'26*26*26')]	|
|18	|26^3-25^3	|(26*26*26) - 2	|[('R.0', 17576.0, u'26^3', u'26*26*26')]	|
|19	|26^3-25^3	|(26*26*26) - 1	|[('R.0', 17576.0, u'26^3', u'26*26*26')]	|
|20	|26^5-25^5	|26^5-25	|[('R.0', 11881376.0, u'26^5', u'26^5')]	|
|21	|26^3-25^3	|(26^3)-1	|[('R.0', 17576.0, u'26^3', u'26^3')]	|
|22	|26^5-25^5	|26^5 - 26^5	|[('R.0', 11881376.0, u'26^5', u'26^5')]	|
|23	|26^4-25^4	|26^4 / 4	|[('R.0', 456976.0, u'26^4', u'26^4')]	|
|24	|26^6-25^6	|26^6 - 26^1	|[('R.0', 308915776.0, u'26^6', u'26^6')]	|
|25	|26^6-25^6	|26^6 - 25^1	|[('R.0', 308915776.0, u'26^6', u'26^6')]	|
|26	|26^6-25^6	|26^6 - 25	|[('R.0', 308915776.0, u'26^6', u'26^6')]	|
|27	|26^5-25^5	|26^5 -1	|[('R.0', 11881376.0, u'26^5', u'26^5')]	|
|28	|26^5-25^5	|26^5 - 26^4	|[('R.0', 11881376.0, u'26^5', u'26^5')]	|




### (31) Mistake Group redirect of size 31




### (25) Mistake Group ['R.1.0'] of size 25
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|26^4-25^4	|26!/((25!))	|[('R.1.0', 25.0, u'25', u'25')]	|
|1	|26^6-25^6	|5*25^5	|[('R.1.0', 25.0, u'25', u'25')]	|
|2	|26^6-25^6	|6*26*25^5	|[('R.1.0', 25.0, u'25', u'25')]	|
|3	|26^4-25^4	|26!/(26-1)!	|[('R.1.0', 25.0, u'25', u'26-1')]	|
|4	|26^4-25^4	|26*25^3	|[('R.1.0', 25.0, u'25', u'25')]	|
|5	|26^4-25^4	|((25^3) * 5) + ((25^2)*3) + (25*5)	|[('R.1.0', 25.0, u'25', u'25')]	|
|6	|26^3-25^3	|26*25^2	|[('R.1.0', 25.0, u'25', u'25')]	|
|7	|26^5-25^5	|5*(25^4)	|[('R.1.0', 25.0, u'25', u'25')]	|
|8	|26^6-25^6	|5(25^5)	|[('R.1.0', 25.0, u'25', u'25')]	|
|9	|26^6-25^6	|6(25^5)	|[('R.1.0', 25.0, u'25', u'25')]	|
|10	|26^4-25^4	|4*(25^3)	|[('R.1.0', 25.0, u'25', u'25')]	|
|11	|26^4-25^4	|26^4+25^3*26+25^2*26^2+25*26^3	|[('R.1.0', 25.0, u'25', u'25')]	|
|12	|26^3-25^3	|3 * 25^2	|[('R.1.0', 25.0, u'25', u'25')]	|
|13	|26^3-25^3	|3*26*25^2	|[('R.1.0', 25.0, u'25', u'25')]	|
|14	|26^3-25^3	|3*25^2	|[('R.1.0', 25.0, u'25', u'25')]	|
|15	|26^4-25^4	|3*25^3	|[('R.1.0', 25.0, u'25', u'25')]	|
|16	|26^4-25^4	|26!/[25!]	|[('R.1.0', 25.0, u'25', u'25')]	|
|17	|26^6-25^6	|5*(25^5)	|[('R.1.0', 25.0, u'25', u'25')]	|
|18	|26^3-25^3	|26*26 + 26*25 + 25*24	|[('R.1.0', 25.0, u'25', u'25')]	|
|19	|26^5-25^5	|5*25^4	|[('R.1.0', 25.0, u'25', u'25')]	|
|20	|26^6-25^6	|6*25^5	|[('R.1.0', 25.0, u'25', u'25')]	|




### (5) Mistake Group ['R.1.1'] of size 5
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|26^4-25^4	|(26*25*25*25)*26^4	|[('R.1.1', 4.0, u'4', u'4')]	|
|1	|26^3-25^3	|(26*25*25)^3 * (26*25*26)^3 * 26^3	|[('R.1.1', 3.0, u'3', u'3')]	|
|2	|26^3-25^3	|(1*25*25)^3 * (26*25*1)^3 * 1^3	|[('R.1.1', 3.0, u'3', u'3')]	|
|3	|26^3-25^3	|(1*25*25)^3 * (1*25*1)^3 * 1^3	|[('R.1.1', 3.0, u'3', u'3')]	|
|4	|26^3-25^3	|(1*25*25)^3 + (1*25*1)^3 + 1^3	|[('R.1.1', 3.0, u'3', u'3')]	|




### (5) Mistake Group ['R.0', 'R.1.0'] of size 5
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|26^5-25^5	|26^5-25^4	|[('R.0', 11881376.0, u'26^5', u'26^5'), ('R.1.0', 25.0, u'25', u'25')]	|
|1	|26^6-25^6	|26^6-25^5	|[('R.0', 308915776.0, u'26^6', u'26^6'), ('R.1.0', 25.0, u'25', u'25')]	|
|2	|26^6-25^6	|(26^6)-(25^5)	|[('R.0', 308915776.0, u'26^6', u'26^6'), ('R.1.0', 25.0, u'25', u'25')]	|
|3	|26^5-25^5	|26^5 - 25^4	|[('R.0', 11881376.0, u'26^5', u'26^5'), ('R.1.0', 25.0, u'25', u'25')]	|




### (4) Mistake Group ['R.1'] of size 4
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|26^4-25^4	|(26*25*25*25)*25^4	|[('R.1', 390625.0, u'25^4', u'25^4')]	|
|1	|26^6-25^6	|6*25^6	|[('R.1', 244140625.0, u'25^6', u'25^6')]	|
|2	|26^6-25^6	|6(25^6)	|[('R.1', 244140625.0, u'25^6', u'25^6')]	|
|3	|26^5-25^5	|5*25^5	|[('R.1', 9765625.0, u'25^5', u'25^5')]	|




### (3) Mistake Group ['R.0.0', 'R.1'] of size 3
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|26^5-25^5	|26^6-25^5	|[('R.0.0', 26.0, u'26', u'26'), ('R.1', 9765625.0, u'25^5', u'25^5')]	|
|1	|26^5-25^5	|(26^6)-(25^5)	|[('R.0.0', 26.0, u'26', u'26'), ('R.1', 9765625.0, u'25^5', u'25^5')]	|




### (2) Mistake Group ['R.0.0', 'R.1.0'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|26^5-25^5	|26*5-25*5	|[('R.0.0', 26.0, u'26', u'26'), ('R.1.0', 25.0, u'25', u'25')]	|
|1	|26^6-25^6	|P(26,6) - P(25,6)	|[('R.0.0', 26.0, u'26', u'26'), ('R.1.0', 25.0, u'25', u'25')]	|




### (133) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:kvass

	first_attempt
					2015-10-06 06:18:37
	part1_correct_attempt
					['0:00:00', u'26**3']
	part2_correct_attempt
					['0:00:00', u'25**3']
	part3_incorrect_attempt
					('0:00:00', u'25*26**2')
					('0:00:30', u'26**2')
					('0:01:18', u'3*26**2')
	part3_correct_attempt
					['1 day, 8:28:23', u'26**3-25**3']

1 Student ID:kbielawi

	first_attempt
					2015-10-05 19:41:05
	part1_correct_attempt
					['0:00:00', u'26^5']
	part2_correct_attempt
					['0:00:00', u'25^5']
	part3_incorrect_attempt
					('0:00:00', u'25^4')
					('0:00:21', u'26^4')
					('0:00:36', u'4*(26^4)')
					('0:00:45', u'5*(26^4)')
					('0:04:23', u'5!*(26^4)')
					('0:12:23', u'4*(26^4)')
	part3_correct_attempt
					['0:13:51', u'26^5-25^5']

2 Student ID:jguanzho

	first_attempt
					2015-10-02 08:03:39
	part1_correct_attempt
					['0:00:00', u'26**5']
	part2_correct_attempt
					['0:00:00', u'25**5']
	part3_incorrect_attempt
					('0:00:00', u'(25**4) * 26')
					('0:00:14', u'(25**4) * 26 * 5')
					('0:01:39', u'26**4')
					('0:01:52', u'5 * 26**4')
					('0:48:59', u'5 * 26! / (4! * 22!)')
	part3_correct_attempt
					['0:54:33', u'26**5 - 25**5']

3 Student ID:alakamsa

	first_attempt
					2015-10-04 19:46:42
	part1_correct_attempt
					['0:00:00', u'26^3']
	part2_correct_attempt
					['0:00:00', u'25^3']
	part3_incorrect_attempt
					('0:00:00', u'25^2*3')
	part3_correct_attempt
					['0:01:51', u'25^2*3 + 25*3 + 1']

4 Student ID:jjm019

	first_attempt
					2015-10-08 01:47:21
	part1_correct_attempt
					['0:00:00', u'26^3']
	part2_correct_attempt
					['0:00:11', u'25^3']
	part3_incorrect_attempt
					('0:00:54', u'26^2')
					('0:01:15', u'3*26*26')
					('0:01:43', u'25^2')
					('0:02:34', u'25*25*3')
					('0:04:18', u'25*25*6')
					('0:11:13', u'26^3')
					('0:48:46', u'(25*25)+(2*25)+(3)')
					('0:49:17', u'(25*25*3)+(2*25*3)+(3)')
	part3_correct_attempt
					['0:51:53', u'(25*25*3)+(25*3)+(1)']

5 Student ID:ctgraves

	first_attempt
					2015-10-06 00:28:08
	part1_correct_attempt
					['0:00:00', u'26^5']
	part2_correct_attempt
					['0:00:00', u'25^5']
	part3_incorrect_attempt
					('0:00:00', u'26^4')
					('0:00:23', u'25^4')
					('0:00:37', u'26^5')
					('0:00:43', u'26^4')
					('0:01:16', u'(5!/(4!))26^4')
					('0:01:28', u'5*26^4')
	part3_correct_attempt
					['0:05:44', u'26^5-25^5']

6 Student ID:nhn018

	first_attempt
					2015-10-07 03:02:14
	part1_correct_attempt
					['0:00:00', u'26^4']
	part2_correct_attempt
					['0:00:00', u'25^4']
	part3_incorrect_attempt
					('0:00:00', u'25^3')
					('0:00:23', u'26^3')
					('0:00:50', u'25^4')
					('0:18:42', u'25^9')
					('0:20:21', u'25^9')
	part3_correct_attempt
					['0:20:56', u'26^4-25^4']

7 Student ID:j5phung

	first_attempt
					2015-10-02 17:17:17
	part1_correct_attempt
					['0:00:00', u'26*26*26']
	part2_correct_attempt
					['0:00:46', u'25*25*25']
	part3_incorrect_attempt
					('0:00:46', u'25*25*26*3')
					('0:01:09', u'25*25*26+25*26*26+26*26*26')
	part3_correct_attempt
					['0:02:55', u'26*26*26-25*25*25']

8 Student ID:dkostins

	first_attempt
					2015-10-06 01:53:38
	part1_correct_attempt
					['0:00:00', u'26^6']
	part2_correct_attempt
					['0:01:00', u'25^6']
	part3_incorrect_attempt
					('0:01:39', u'26^5')
					('0:01:49', u'25^5')
					('0:06:19', u'5(26^5)')
					('0:06:29', u'6(26^5)')
					('0:13:11', u'6(26^6)')
					('0:13:23', u'26^6')
	part3_correct_attempt
					['0:16:28', u'(26^6)-(25^6)']

9 Student ID:c4du

	first_attempt
					2015-10-07 07:02:55
	part1_correct_attempt
					['0:00:00', u'26^5']
	part2_correct_attempt
					['0:00:00', u'25^5']
	part3_incorrect_attempt
					('0:02:36', u'26^4')
	part3_correct_attempt
					['0:04:19', u'26^5-25^5']

10 Student ID:rlhagen

	first_attempt
					2015-10-04 22:55:34
	part1_correct_attempt
					['0:00:00', u'26^4']
	part2_correct_attempt
					['0:00:00', u'25^4']
	part3_incorrect_attempt
					('0:01:08', u'26^3')
					('0:03:25', u'25^3')
	part3_correct_attempt
					['0:05:31', u'26^4 - 25^4']

11 Student ID:avasavad

	first_attempt
					2015-10-06 06:25:54
	part1_correct_attempt
					['0:00:00', u'26^5']
	part2_correct_attempt
					['0:00:00', u'25^5']
	part3_incorrect_attempt
					('0:00:00', u'25^4 + 1')
	part3_correct_attempt
					['0:00:54', u'26^5 - 25^5']

12 Student ID:tcn013

	first_attempt
					2015-10-06 03:56:57
	part1_correct_attempt
					['0:00:00', u'26^3']
	part2_correct_attempt
					['0:00:00', u'25^3']
	part3_incorrect_attempt
					('0:00:54', u'26^2')
					('0:01:15', u'3*26^2')
					('0:06:17', u'3*25^2+4')
	part3_correct_attempt
					['1 day, 1:04:27', u'3*25^2+3*25+1']

13 Student ID:tstevens

	first_attempt
					2015-10-07 12:15:55
	part1_correct_attempt
					['0:00:00', u'26^5']
	part2_correct_attempt
					['0:00:00', u'25^5']
	part3_incorrect_attempt
					('0:00:00', u'26^4')
					('0:00:38', u'5*(26^4)')
	part3_correct_attempt
					['0:03:48', u'26^5-25^5']

14 Student ID:pthsu

	first_attempt
					2015-10-02 04:29:29
	part1_correct_attempt
					['0:00:00', u'26**5']
	part2_correct_attempt
					['0:00:00', u'25**5']
	part3_incorrect_attempt
					('0:00:00', u'26**4')
	part3_correct_attempt
					['0:03:39', u'26**5-25**5']

15 Student ID:tcuddy

	first_attempt
					2015-10-02 20:23:57
	part1_correct_attempt
					['0:00:00', u'26**5']
	part2_correct_attempt
					['0:00:00', u'25**5']
	part3_incorrect_attempt
					('0:00:00', u'26*4')
					('0:00:06', u'26**4')
					('0:01:31', u'26**4')
	part3_correct_attempt
					['0:04:41', u'(26**5)-(25**5)']

16 Student ID:l8ngo

	first_attempt
					2015-10-05 03:02:26
	part1_correct_attempt
					['0:00:00', u'26^6']
	part2_correct_attempt
					['0:00:00', u'25^6']
	part3_incorrect_attempt
					('0:00:00', u'25^5')
					('0:00:28', u'[25^5]*6')
					('0:01:26', u'26^5')
	part3_correct_attempt
					['1:29:06', u'(26^6) - (25^6)']

17 Student ID:djk006

	first_attempt
					2015-10-04 23:54:43
	part1_correct_attempt
					['0:00:00', u'26^5']
	part2_correct_attempt
					['0:00:00', u'25^5']
	part3_incorrect_attempt
					('0:00:32', u'26^4')
	part3_correct_attempt
					['0:02:24', u'26^5-25^5']

18 Student ID:aysee

	first_attempt
					2015-10-08 23:10:18
	part1_correct_attempt
					['0:00:00', u'308915776']
	part2_correct_attempt
					['0:00:00', u'244140625']
	part3_incorrect_attempt
					('0:00:00', u'244140625 * 6')
					('0:01:54', u'6*(7893600)')
	part3_correct_attempt
					['0:07:30', u'64775151']

19 Student ID:dando

	first_attempt
					2015-10-04 20:01:26
	part1_correct_attempt
					['0:00:00', u'26^3']
	part2_correct_attempt
					['0:00:00', u'25^3']
	part3_incorrect_attempt
					('0:00:00', u'26^2')
					('0:00:27', u'3*26^2')
					('0:03:16', u'3 * (1 * 26 * 26) - 3')
					('0:03:24', u'3 * (1 * 26 * 26) - 2')
					('0:03:34', u'3 * (1 * 26 * 26) - 1')
					('0:03:45', u'3 * (1 * 26 * 26) - 9')
	part3_correct_attempt
					['0:07:11', u'1 + 3 * 25 + 3 * 25^2']

20 Student ID:dsriniva

	first_attempt
					2015-10-08 17:44:48
	part1_correct_attempt
					['0:00:00', u'26^6']
	part2_correct_attempt
					['0:00:00', u'25^6']
	part3_incorrect_attempt
					('0:00:15', u'6*25^5+26*6')
	part3_correct_attempt
					['0:04:03', u'26^6-25^6']

21 Student ID:a2ahmed

	first_attempt
					2015-10-08 17:13:15
	part1_correct_attempt
					['0:00:00', u'26^4']
	part2_correct_attempt
					['0:00:00', u'25^4']
	part3_incorrect_attempt
					('0:00:00', u'4*(26^3)')
					('0:01:52', u'4*(26^3) + 4*(26^2) + 4*(26) + 1')
					('0:04:42', u'4*(26^3) + 6*(26^2) + 4*(26) + 1')
	part3_correct_attempt
					['0:06:14', u'(26^4) - (25^4)']

22 Student ID:m4salaza

	first_attempt
					2015-10-07 03:46:12
	part1_correct_attempt
					['0:00:00', u'26^6']
	part2_correct_attempt
					['0:00:00', u'25^6']
	part3_incorrect_attempt
					('0:00:00', u'1+26^5')
	part3_correct_attempt
					['0:01:51', u'26^6-25^6']

23 Student ID:yos017

	first_attempt
					2015-10-02 11:51:03
	part1_correct_attempt
					['0:00:00', u'26^6']
	part2_correct_attempt
					['0:00:00', u'25^6']
	part3_incorrect_attempt
					('0:00:00', u'25^6')
					('0:00:24', u'25^5')
					('0:02:59', u'5*26^5')
					('0:04:20', u'6*26^5')
	part3_correct_attempt
					['0:20:50', u'1+(15*25^2)+(20*25^3)+(15*25^4)+(6*25^5)']

24 Student ID:small

	first_attempt
					2015-10-08 23:40:08
	part1_correct_attempt
					['0:00:00', u'26^3']
	part2_correct_attempt
					['0:00:13', u'25^3']
	part3_incorrect_attempt
					('0:00:40', u'26*26')
					('0:02:14', u'676*3')
					('0:03:01', u'676*3 - 2')
	part3_correct_attempt
					['0:04:15', u'26^3 - 25^3']

25 Student ID:m8woo

	first_attempt
					2015-10-08 20:50:24
	part1_correct_attempt
					['0:00:00', u'26^5']
	part2_correct_attempt
					['0:00:00', u'25^5']
	part3_incorrect_attempt
					('0:00:00', u'26^4')
	part3_correct_attempt
					['0:01:40', u'26^5-25^5']

26 Student ID:ggaddi

	first_attempt
					2015-10-03 01:10:14
	part1_correct_attempt
					['0:00:00', u'26^3']
	part2_correct_attempt
					['0:00:00', u'25^3']
	part3_incorrect_attempt
					('0:01:29', u'25^2*3 + 25*2 + 1')
	part3_correct_attempt
					['0:01:51', u'25^2*3 + 25*3 + 1']

27 Student ID:a8ho

	first_attempt
					2015-10-07 05:50:38
	part1_correct_attempt
					['0:00:00', u'26^3']
	part2_correct_attempt
					['0:00:00', u'25^3']
	part3_incorrect_attempt
					('0:02:56', u'3*25*26^2')
					('0:03:46', u'3*26^2')
					('0:05:26', u'3(26^2)')
					('0:57:46', u'3*25^2+1+3*24^2')
					('0:58:42', u'3*25^2+1+3*24')
	part3_correct_attempt
					['1:01:25', u'26^3-25^3']

28 Student ID:h4tu

	first_attempt
					2015-10-08 19:03:17
	part1_correct_attempt
					['0:00:00', u'26^3']
	part2_correct_attempt
					['0:00:30', u'25^3']
	part3_incorrect_attempt
					('0:00:30', u'26^2')
	part3_correct_attempt
					['0:01:11', u'26^3-25^3']

29 Student ID:ccn001

	first_attempt
					2015-10-06 06:32:10
	part1_correct_attempt
					['0:00:00', u'26^5']
	part2_correct_attempt
					['0:00:00', u'25^5']
	part3_incorrect_attempt
					('0:00:00', u'1*26^4')
					('0:28:08', u'26^4+26^4+26^4+26^4+26^4')
	part3_correct_attempt
					['11:08:31', u'(5!/((1!)(5-1)!))25^4+(5!/((2!)(5-2)!))25^3+(5!/((3!)(5-3)!))25^2+(5!/((4!)(5-4)!))25^1+1']

30 Student ID:lrlai

	first_attempt
					2015-10-04 23:28:25
	part1_correct_attempt
					['0:00:00', u'26^4']
	part2_correct_attempt
					['0:00:00', u'25^4']
	part3_incorrect_attempt
					('0:00:00', u'(25^3) * 3')
					('0:02:17', u'((25^3) * 5) + ((25^2)*3) + (25*5) + 1')
	part3_correct_attempt
					['0:47:12', u'26^4 - (25^4)']

31 Student ID:asetters

	first_attempt
					2015-10-02 19:57:28
	part1_correct_attempt
					['0:00:00', u'26^6']
	part2_correct_attempt
					['0:00:00', u'25^6']
	part3_incorrect_attempt
					('0:00:00', u'25^5')
					('0:00:11', u'25^5*6')
	part3_correct_attempt
					['0:02:21', u'26^6-25^6']

32 Student ID:jjchung

	first_attempt
					2015-10-08 06:33:53
	part1_correct_attempt
					['0:00:00', u'26^3']
	part2_correct_attempt
					['0:00:11', u'25^3']
	part3_incorrect_attempt
					('0:00:37', u'26^2')
					('0:02:23', u'(26^2)*3-2')
					('0:02:28', u'(26^2)*3-3')
					('0:02:36', u'(26^2)*3-1')
	part3_correct_attempt
					['0:06:57', u'(26^3 - 25^3)']

33 Student ID:atorr

	first_attempt
					2015-10-05 05:57:50
	part1_correct_attempt
					['0:00:00', u'26^3']
	part2_correct_attempt
					['0:00:00', u'25^3']
	part3_incorrect_attempt
					('0:00:12', u'26^3')
					('0:00:30', u'26^2')
					('0:00:49', u'25^2')
					('0:01:00', u'1 * 26 * 26')
					('0:02:42', u'26^3')
					('0:02:57', u'3 * 26^3')
					('0:03:30', u'26^6')
	part3_correct_attempt
					['0:08:25', u'26^3 - 25^3']

34 Student ID:cprafull

	first_attempt
					2015-10-06 19:29:17
	part1_correct_attempt
					['0:00:00', u'26*26*26*26']
	part2_correct_attempt
					['0:00:14', u'25*25*25*25']
	part3_incorrect_attempt
					('0:00:59', u'26*26*26*4')
					('0:01:04', u'26*26*26')
					('0:02:03', u'26*26*26*4')
					('6:01:46', u'25*25*25*4')
	part3_correct_attempt
					['6:06:04', u'(26^4) - (25^4)']

35 Student ID:anislam

	first_attempt
					2015-10-08 23:56:54
	part1_correct_attempt
					['0:00:00', u'26^3']
	part2_correct_attempt
					['0:00:00', u'25^3']
	part3_incorrect_attempt
					('0:00:29', u'26^2 * 3 - 2')
					('0:01:32', u'26^2 * 3 - 2 - 1 -1 - 1')
					('0:05:05', u'26^2 + 26^2 + 26^2 - 1 - 1 - 26 - 26 - 26')

36 Student ID:mroknich

	first_attempt
					2015-10-06 06:11:24
	part1_correct_attempt
					['0:00:00', u'26^4']
	part2_correct_attempt
					['0:00:00', u'25^4']
	part3_incorrect_attempt
					('0:00:40', u'26^4')
					('0:07:52', u'(26^3*4)+(26^3*C(4,2))+(26*C(4,3))+1')
	part3_correct_attempt
					['0:16:01', u'26^4-25^4']

37 Student ID:alhung

	first_attempt
					2015-10-08 07:58:54
	part1_correct_attempt
					['0:00:00', u'26^4']
	part2_correct_attempt
					['0:00:00', u'25^4']
	part3_incorrect_attempt
					('0:00:00', u'26^3')
					('0:00:29', u'4*26^3')
					('0:01:53', u'4*26!/23!')
					('0:06:17', u'4!*26^3')
					('0:07:27', u'4*26^3')
	part3_correct_attempt
					['0:22:15', u'26^4-25^4']

38 Student ID:b3hwang

	first_attempt
					2015-10-08 23:26:34
	part1_correct_attempt
					['0:00:00', u'26^4']
	part2_correct_attempt
					['0:00:11', u'25^4']
	part3_incorrect_attempt
					('0:00:22', u'26^3')
					('0:00:46', u'4*26^3')
	part3_correct_attempt
					['0:01:37', u'(26^4)-(25^4)']

39 Student ID:c2qiu

	first_attempt
					2015-10-03 18:25:48
	part1_correct_attempt
					['0:00:00', u'26^6']
	part2_correct_attempt
					['0:00:00', u'25^6']
	part3_incorrect_attempt
					('0:00:00', u'6*26^5')
	part3_correct_attempt
					['0:02:50', u'26^6-25^6']

40 Student ID:jcj006

	first_attempt
					2015-10-08 00:29:09
	part1_correct_attempt
					['0:00:00', u'26^4']
	part2_correct_attempt
					['0:00:00', u'25^4']
	part3_incorrect_attempt
					('0:00:00', u'4*26^3')
	part3_correct_attempt
					['0:01:16', u'26^4-25^4']

41 Student ID:dis003

	first_attempt
					2015-10-08 07:26:17
	part1_correct_attempt
					['0:00:00', u'26^5']
	part2_correct_attempt
					['0:00:00', u'25^5']
	part3_incorrect_attempt
					('0:00:00', u'26^4')
	part3_correct_attempt
					['0:01:09', u'26^5 - 25^5']

42 Student ID:rraiyyan

	first_attempt
					2015-10-06 06:55:02
	part1_correct_attempt
					['0:00:00', u'26^3']
	part2_correct_attempt
					['0:00:00', u'25^3']
	part3_incorrect_attempt
					('0:00:00', u'3 * 26*25*25')
					('0:00:20', u'(26*25*25)^3')
					('0:01:56', u'(26*25*25 * 26*25*26 * 26)^3')
	part3_correct_attempt
					['0:06:06', u'(1*25*25)*3 + (1*25*1)*3 + 1']

43 Student ID:jhw015

	first_attempt
					2015-10-06 15:12:52
	part1_correct_attempt
					['0:00:00', u'26^3']
	part2_correct_attempt
					['0:00:19', u'25^3']
	part3_incorrect_attempt
					('0:01:24', u'26^2')
	part3_correct_attempt
					['0:08:22', u'26^3 - 25^3']

44 Student ID:krkelkar

	first_attempt
					2015-10-03 07:12:29
	part1_correct_attempt
					['0:00:00', u'26**3']
	part2_correct_attempt
					['0:00:00', u'25**3']
	part3_incorrect_attempt
					('0:00:00', u'3* 26**2')
	part3_correct_attempt
					['0:02:50', u'26**3-25**3']

45 Student ID:lcardoso

	first_attempt
					2015-10-08 07:07:35
	part1_correct_attempt
					['0:00:00', u'26*26*26']
	part2_correct_attempt
					['0:00:00', u'25*25*25']
	part3_incorrect_attempt
					('0:00:00', u'1*25*25')
					('0:00:51', u'1*25*25 * (3!/(2!*1!))')
	part3_correct_attempt
					['0:02:52', u'26*26*26 - 25*25*25']

46 Student ID:jel075

	first_attempt
					2015-10-08 00:53:10
	part1_correct_attempt
					['0:00:00', u'26*26*26*26']
	part2_correct_attempt
					['0:00:25', u'25*25*25*25']
	part3_incorrect_attempt
					('0:00:25', u'1*26*26*26')
					('0:03:28', u'26*26*26*4')
					('3:30:54', u'26*26*26+26*26*26+26*26*26+26*26*26')
	part3_correct_attempt
					['3:32:15', u'26*26*26*26-25*25*25*25']

47 Student ID:ytc012

	first_attempt
					2015-10-06 09:52:16
	part1_correct_attempt
					['0:00:00', u'26^6']
	part2_correct_attempt
					['0:00:10', u'25^6']
	part3_incorrect_attempt
					('0:00:28', u'26^5')
					('0:03:00', u'26^5')
					('0:03:11', u'6*(26^5)')
					('0:03:16', u'5*(26^5)')
					('0:14:55', u'26^5')
					('0:16:22', u'6*26^5-6!')
					('0:16:42', u'6*26^5-6')
	part3_correct_attempt
					['0:25:28', u'26^6 -25^6']

48 Student ID:kosung

	first_attempt
					2015-10-07 06:25:51
	part1_correct_attempt
					['0:00:00', u'26^5']
	part2_correct_attempt
					['0:00:37', u'25^5']
	part3_incorrect_attempt
					('0:00:37', u'26^4')
	part3_correct_attempt
					['0:05:44', u'26^5 - 25^5']

49 Student ID:etemlock

	first_attempt
					2015-10-02 17:50:03
	part1_correct_attempt
					['0:00:00', u'26^6']
	part2_correct_attempt
					['0:00:00', u'25^6']
	part3_incorrect_attempt
					('0:00:00', u'26^5')
	part3_correct_attempt
					['0:08:08', u'(26^6)-(25^6)']

50 Student ID:muy002

	first_attempt
					2015-10-07 21:55:28
	part1_correct_attempt
					['0:00:00', u'26^4']
	part2_correct_attempt
					['0:00:00', u'25^4']
	part3_incorrect_attempt
					('0:00:00', u'1*26*26*26')
	part3_correct_attempt
					['0:01:23', u'26^4-25^4']

51 Student ID:jtfrankl

	first_attempt
					2015-10-07 23:43:24
	part1_correct_attempt
					['0:00:00', u'26**6']
	part2_correct_attempt
					['0:00:00', u'25**6']
	part3_incorrect_attempt
					('0:00:00', u'26**5')
					('0:01:15', u'(26!/(5!21!))6')
					('0:01:31', u'(26!/(5!21!))5')
					('3:06:58', u'(26!/(5!21!))6')
	part3_correct_attempt
					['3:12:30', u'26**6-25**6']

52 Student ID:eshung

	first_attempt
					2015-10-08 18:41:54
	part1_correct_attempt
					['0:00:00', u'26^4']
	part2_correct_attempt
					['0:00:00', u'25^4']
	part3_incorrect_attempt
					('0:04:00', u'(25^3)*(3)+(25^2)*(6)+(25*3)+1')
					('0:05:23', u'25^4')
	part3_correct_attempt
					['0:05:40', u'26^4-25^4']

53 Student ID:rbdoming

	first_attempt
					2015-10-02 21:26:44
	part1_correct_attempt
					['0:00:00', u'26*26*26']
	part2_correct_attempt
					['0:00:00', u'25*25*25']
	part3_incorrect_attempt
					('0:00:00', u'26*26*26')
					('0:07:48', u'3(26*26*25)')
	part3_correct_attempt
					['0:11:04', u'26* 26* 26 - 25*25*25']

54 Student ID:aurodrig

	first_attempt
					2015-10-07 04:55:05
	part1_correct_attempt
					['0:00:00', u'26^6']
	part2_correct_attempt
					['0:00:23', u'25^6']
	part3_incorrect_attempt
					('0:06:43', u'6^26-6^25')
					('0:07:04', u'6^26-1^25')
					('0:07:19', u'6^26-5^25')
	part3_correct_attempt
					['0:09:37', u'26^6-25^6']

55 Student ID:dcastlem

	first_attempt
					2015-10-03 22:16:23
	part1_correct_attempt
					['0:00:00', u'26^5']
	part2_correct_attempt
					['0:00:00', u'25^5']
	part3_incorrect_attempt
					('0:01:49', u'26*2')
					('0:01:57', u'26^2')
					('0:11:38', u'26^4')
	part3_correct_attempt
					['0:16:46', u'26^5-25^5']

56 Student ID:bkoli

	first_attempt
					2015-10-08 16:45:51
	part1_correct_attempt
					['0:00:00', u'26^5']
	part2_correct_attempt
					['0:00:23', u'25^5']
	part3_incorrect_attempt
					('0:03:23', u'25*26^4')
					('0:03:47', u'1*26^4')
					('0:05:30', u'1+26^4')
					('0:11:39', u'26^4+1+26^4')
	part3_correct_attempt
					['0:15:37', u'26^5-25^5']

57 Student ID:v3doan

	first_attempt
					2015-10-04 00:06:48
	part1_correct_attempt
					['0:00:00', u'26 * 26 *26']
	part2_correct_attempt
					['0:00:00', u'25 * 25 * 25']
	part3_incorrect_attempt
					('0:01:22', u'26 * 26')
					('0:02:16', u'C(26, 3)')
					('0:06:33', u'26 * 26 * 3 - 1 -3')
					('0:06:43', u'26 * 26 * 3 - 1')
					('0:06:53', u'26 * 26 * 3 + 2')
					('0:07:00', u'26 * 26 * 3 + 1')
					('0:07:05', u'26 * 26 * 3 - 2')
					('0:08:49', u'26 * 26 * 3 + 1 - 6')
					('0:12:35', u'26 * 26 - (26 * 3) + 1')
	part3_correct_attempt
					['0:12:49', u'3 * 26 * 26 - (26 * 3) + 1']

58 Student ID:yil035

	first_attempt
					2015-10-07 06:05:33
	part1_correct_attempt
					['0:00:00', u'26^5']
	part2_correct_attempt
					['0:00:00', u'25^5']
	part3_incorrect_attempt
					('0:00:00', u'26^4')
	part3_correct_attempt
					['0:01:11', u'26^5-25^5']

59 Student ID:wmiao

	first_attempt
					2015-10-07 04:41:54
	part1_correct_attempt
					['0:00:00', u'26^5']
	part2_correct_attempt
					['0:00:00', u'25^5']
	part3_incorrect_attempt
					('0:00:00', u'26^4')
					('0:00:49', u'5*26^4')
					('0:01:10', u'5!*26^4')
	part3_correct_attempt
					['0:12:57', u'2115751']

60 Student ID:druble

	first_attempt
					2015-10-08 21:21:34
	part1_correct_attempt
					['0:00:00', u'26^4']
	part2_correct_attempt
					['0:00:00', u'25^4']
	part3_incorrect_attempt
					('0:00:00', u'4*1*26^3')
	part3_correct_attempt
					['0:00:53', u'26^4 - 25^4']

61 Student ID:lpettit

	first_attempt
					2015-10-06 03:35:15
	part1_correct_attempt
					['0:00:00', u'26^4']
	part2_correct_attempt
					['0:00:27', u'25^4']
	part3_incorrect_attempt
					('0:00:55', u'26^3')
					('0:03:34', u'4*(26^3)')
					('0:08:18', u'(26!)/(1!*(25!))')
					('0:08:32', u'(26!)/(1!*(25!)) * 26^3')
					('0:09:37', u'4*(26^3) - 4')
					('0:10:18', u'4*(26^3) - 4!')
					('0:10:35', u'4*(26^3) - 4*4!')
					('0:16:22', u'(26^3)')
	part3_correct_attempt
					['11:33:41', u'26^4 - 25^4']

62 Student ID:ctroncos

	first_attempt
					2015-10-08 23:53:45
	part1_correct_attempt
					['0:00:00', u'26^3']
	part2_correct_attempt
					['0:02:16', u'25^3']
	part3_incorrect_attempt
					('0:02:44', u'26^2')
					('0:06:31', u'25*24*3')

63 Student ID:kebao

	first_attempt
					2015-10-03 18:10:46
	part1_correct_attempt
					['0:00:00', u'26^6']
	part2_correct_attempt
					['0:00:28', u'25^6']
	part3_incorrect_attempt
					('0:01:09', u'26^5')
					('0:06:26', u'6!/5!')
					('0:11:55', u'25^5')
	part3_correct_attempt
					['0:15:33', u'26^6-25^6']

64 Student ID:glcohen

	first_attempt
					2015-10-04 23:11:58
	part1_correct_attempt
					['0:00:00', u'26*26*26']
	part2_correct_attempt
					['0:00:00', u'25*25*25']
	part3_incorrect_attempt
					('0:00:00', u'1*26*26')
					('0:00:09', u'3*26*26')
					('0:00:36', u'(26*26)(26*26)(26*26)')
					('0:08:19', u'(26*26)+(26*26)+(26*26)+(26*26)+(3*26)+1')
					('0:08:40', u'(25*25)+(25*25)+(25*25)+(25*25)+(3*25)+1')
					('0:08:54', u'(25*25)+(25*25)+(25*25)+(25*25)+(3*25)')
					('0:11:00', u'25*26*26')
					('0:11:09', u'3(25*26*26)')
					('0:11:17', u'2(25*26*26)')
					('0:11:37', u'3*(1*26*26)')
					('0:11:54', u'2*(26*26)')
					('0:11:59', u'3*(26*26)')
					('0:13:58', u'(26*26)')
					('0:14:09', u'2(26*26)')
					('0:14:15', u'4(26*26)')
					('0:14:48', u'3(26*26)')
	part3_correct_attempt
					['0:17:08', u'(26^3)-(25^3)']

65 Student ID:achava

	first_attempt
					2015-10-02 05:30:54
	part1_correct_attempt
					['0:00:00', u'26^4']
	part2_correct_attempt
					['0:16:14', u'25^4']
	part3_incorrect_attempt
					('0:16:39', u'26*25*25*25')
					('0:16:55', u'26*25*26*25')
					('0:18:08', u'26^4')
					('0:19:57', u'26!/((1!)*(25!))')
					('0:22:22', u'26*25*25*25')
					('0:22:34', u'26*26*25*26')
					('0:22:38', u'26*26*25*25')
					('0:38:09', u'25*25*25+1')
					('0:38:37', u'(25*25*25*25)+4')
	part3_correct_attempt
					['2:21:19', u'26^4-25^4']

66 Student ID:d6he

	first_attempt
					2015-10-07 21:22:22
	part1_correct_attempt
					['0:00:00', u'26^6']
	part2_correct_attempt
					['0:00:00', u'25^6']
	part3_incorrect_attempt
					('0:00:12', u'5*(26^5)')
					('0:00:21', u'6*(26^5)')
					('0:02:54', u'6*(26^5)-1')
					('0:03:00', u'6*(26^5)-6')
	part3_correct_attempt
					['0:04:04', u'(26^6)-(25^6)']

67 Student ID:sachadal

	first_attempt
					2015-10-05 19:08:14
	part1_correct_attempt
					['0:00:00', u'26^4']
	part2_correct_attempt
					['0:00:21', u'25^4']
	part3_incorrect_attempt
					('0:00:21', u'26^3')
					('0:02:07', u'4*26^3')
	part3_correct_attempt
					['0:05:41', u'(26^4) - (25^4)']

68 Student ID:awollner

	first_attempt
					2015-10-06 15:48:11
	part1_correct_attempt
					['0:00:00', u'26^6']
	part2_correct_attempt
					['0:00:00', u'25^6']
	part3_incorrect_attempt
					('0:00:00', u'26^5')
					('0:00:08', u'26^6')
	part3_correct_attempt
					['0:26:09', u'26^6-25^6']

69 Student ID:dcrume

	first_attempt
					2015-10-08 17:20:35
	part1_correct_attempt
					['0:00:00', u'26^(5)']
	part2_correct_attempt
					['0:00:00', u'25^(5)']
	part3_incorrect_attempt
					('0:00:00', u'26^(4)')
					('0:01:54', u'26^(4) + 26^(3) + 26^(2) + 26 + 1')

70 Student ID:t2li

	first_attempt
					2015-10-06 03:41:50
	part1_correct_attempt
					['0:00:00', u'26^4']
	part2_correct_attempt
					['0:00:00', u'25^4']
	part3_incorrect_attempt
					('0:02:55', u'25^3')
					('0:04:34', u'4*26*26*26')
					('0:07:28', u'26*26*26')
	part3_correct_attempt
					['0:07:50', u'26^4-25^4']

71 Student ID:dlt009

	first_attempt
					2015-10-05 00:31:46
	part1_correct_attempt
					['0:00:00', u'26^5']
	part2_correct_attempt
					['0:00:00', u'25^5']
	part3_incorrect_attempt
					('0:00:00', u'26^4')
	part3_correct_attempt
					['0:04:23', u'(26^5)-(25^5)']

72 Student ID:n2patil

	first_attempt
					2015-10-08 05:32:55
	part1_correct_attempt
					['0:00:00', u'26^4']
	part2_correct_attempt
					['0:00:13', u'25^4']
	part3_incorrect_attempt
					('0:00:52', u'26*26*26*25')
					('0:01:24', u'26*26*26')
					('0:05:36', u'26*26*26*4')
	part3_correct_attempt
					['0:21:15', u'(26^4)-(25^4)']

73 Student ID:ttimmons

	first_attempt
					2015-10-04 00:10:57
	part1_correct_attempt
					['0:00:00', u'26^5']
	part2_correct_attempt
					['0:00:00', u'25^5']
	part3_incorrect_attempt
					('0:00:12', u'25^4')
					('0:00:35', u'26*26*26*26')
					('0:00:51', u'4*26*26*26*26')
	part3_correct_attempt
					['0:02:25', u'26^5-25^5']

74 Student ID:jnatale

	first_attempt
					2015-10-08 02:38:05
	part1_correct_attempt
					['0:00:00', u'26*26*26']
	part2_correct_attempt
					['0:00:13', u'25*25*25']
	part3_incorrect_attempt
					('0:00:32', u'1*26*26')
					('0:02:36', u'26^3')
					('0:05:15', u'26*26')
					('0:05:36', u'(26*26)^3 - 3')
					('0:05:52', u'(26*26)^3 - 6')
					('0:05:57', u'(26*26)^3 - 5')
					('0:06:01', u'(26*26)^3 - 4')
					('0:06:04', u'(26*26)^3 - 7')
					('0:06:08', u'(26*26)^3 - 8')
	part3_correct_attempt
					['0:12:04', u'26^3 - 25^3']

75 Student ID:jblynch

	first_attempt
					2015-10-05 04:37:48
	part1_correct_attempt
					['0:00:00', u'26^5']
	part2_correct_attempt
					['0:00:00', u'25^5']
	part3_incorrect_attempt
					('0:00:00', u'26^4')
	part3_correct_attempt
					['0:00:23', u'26^5 - 25^5']

76 Student ID:ganajera

	first_attempt
					2015-10-03 18:27:27
	part1_correct_attempt
					['0:00:00', u'26^4']
	part2_correct_attempt
					['0:00:00', u'25^4']
	part3_incorrect_attempt
					('0:00:00', u'4*26*26*26')
	part3_correct_attempt
					['0:02:01', u'(26^4)-(25^4)']

77 Student ID:nnh002

	first_attempt
					2015-10-07 00:43:18
	part1_correct_attempt
					['0:00:00', u'26^4']
	part2_correct_attempt
					['0:00:00', u'25^4']
	part3_incorrect_attempt
					('0:00:00', u'26^3')
	part3_correct_attempt
					['0:00:46', u'26^4-(25^4)']

78 Student ID:skodigal

	first_attempt
					2015-10-08 00:51:25
	part1_correct_attempt
					['0:00:00', u'26^4']
	part2_correct_attempt
					['0:00:00', u'25^4']
	part3_incorrect_attempt
					('0:00:41', u'26^3')
					('0:10:27', u'(26^4)*4*6*4')
					('0:10:43', u'(26^4)/4*6*4')
	part3_correct_attempt
					['1:47:54', u'66351']

79 Student ID:wcwhite

	first_attempt
					2015-10-08 19:09:49
	part1_correct_attempt
					['0:00:00', u'26^4']
	part2_correct_attempt
					['0:00:44', u'25^4']
	part3_incorrect_attempt
					('0:00:59', u'26^4')
					('0:01:09', u'26^3')
					('0:01:21', u'25^3')
					('0:07:07', u'4*26^4')

80 Student ID:eaherman

	first_attempt
					2015-10-03 21:07:39
	part1_correct_attempt
					['0:00:00', u'26^4']
	part2_correct_attempt
					['0:00:24', u'25^4']
	part3_incorrect_attempt
					('0:01:31', u'(25)(26)(26)')
					('0:01:45', u'(25)(26)(26)(26)')
					('0:02:03', u'(26)(26)(26)')
					('0:08:12', u'(25^3)(4)')
					('0:19:55', u'[(26^3)(4)]-24')
					('0:37:46', u'[(26^3)(4)]-27')
					('1 day, 19:52:10', u'[(26^3)(4)]-6')
					('1 day, 19:52:24', u'(26^3)')
					('1 day, 20:15:54', u'(25^3)(4)+11')
	part3_correct_attempt
					['1 day, 20:19:56', u'(26^4)-(25^4)']

81 Student ID:lguintu

	first_attempt
					2015-10-06 16:56:19
	part1_correct_attempt
					['0:00:00', u'26^5']
	part2_correct_attempt
					['0:00:00', u'25^5']
	part3_incorrect_attempt
					('0:00:00', u'26^4')
	part3_correct_attempt
					['0:01:04', u'26^5-25^5']

82 Student ID:c1sorian

	first_attempt
					2015-10-08 05:54:51
	part1_correct_attempt
					['0:00:00', u'26^3']
	part2_correct_attempt
					['0:00:58', u'25^3']
	part3_incorrect_attempt
					('0:01:19', u'26*26')
					('0:01:42', u'3*26*26')
	part3_correct_attempt
					['0:07:28', u'(26^3)-(25^3)']

83 Student ID:volim

	first_attempt
					2015-10-03 18:52:37
	part1_correct_attempt
					['0:00:00', u'(26)^6']
	part2_correct_attempt
					['0:00:00', u'(25)^6']
	part3_incorrect_attempt
					('0:00:00', u'(26)^5')
	part3_correct_attempt
					['0:15:25', u'(26^6)-(25^6)']

84 Student ID:ralhadda

	first_attempt
					2015-10-08 17:51:33
	part1_correct_attempt
					['0:00:00', u'26*26*26']
	part2_correct_attempt
					['0:00:35', u'25*25*25']
	part3_incorrect_attempt
					('0:00:54', u'25*26*26')
					('0:01:00', u'25*26*24')
					('0:02:07', u'26*26*26')

85 Student ID:hmnaing

	first_attempt
					2015-10-07 18:08:53
	part1_correct_attempt
					['0:00:00', u'26^5']
	part2_correct_attempt
					['0:00:00', u'25^5']
	part3_incorrect_attempt
					('0:00:00', u'(25^5)*5')
	part3_correct_attempt
					['5:01:36', u'(26^5) - (25^5)']

86 Student ID:tjke

	first_attempt
					2015-10-03 23:34:41
	part1_correct_attempt
					['0:00:00', u'26^6']
	part2_correct_attempt
					['0:00:00', u'25^6']
	part3_incorrect_attempt
					('0:00:00', u'C(5,1)*26^5')
					('0:02:40', u'[5!/(4!)]*26^5')
	part3_correct_attempt
					['0:07:46', u'26^6-25^6']

87 Student ID:klala

	first_attempt
					2015-10-05 20:22:54
	part1_correct_attempt
					['0:00:00', u'26^4']
	part2_correct_attempt
					['0:00:00', u'25^4']
	part3_incorrect_attempt
					('0:00:00', u'26^3')
	part3_correct_attempt
					['0:02:15', u'26^4 - 25^4']

88 Student ID:asp025

	first_attempt
					2015-10-08 16:07:28
	part1_correct_attempt
					['0:00:00', u'26^4']
	part2_correct_attempt
					['0:00:43', u'25^4']
	part3_incorrect_attempt
					('0:02:42', u'(25^4)+1')
					('0:03:14', u'26*25*25*25')
					('0:07:02', u'(26!26!26!26!)/26^3')
					('0:12:52', u'(4*26)-1')
					('0:13:17', u'(4*25)+1')
					('0:56:09', u'4*25*25*25')
	part3_correct_attempt
					['0:56:57', u'66351']

89 Student ID:dlgoldbe

	first_attempt
					2015-10-08 05:02:14
	part1_correct_attempt
					['0:00:00', u'26^5']
	part2_correct_attempt
					['0:00:13', u'25^5']
	part3_incorrect_attempt
					('0:01:44', u'5*26^4')
					('0:02:10', u'26^4')
					('0:07:28', u'5*((104!)/(4!*100!))')
					('0:09:26', u'5*(26^4)')
					('0:10:23', u'5+(26^4)')
					('0:11:05', u'26^4')
					('0:18:08', u'(25^4)*5*4*3*2')
	part3_correct_attempt
					['0:19:50', u'(26^5)-(25^5)']

90 Student ID:jfalcone

	first_attempt
					2015-10-07 03:49:48
	part1_correct_attempt
					['0:00:00', u'26 * 26 * 26 * 26']
	part2_correct_attempt
					['0:00:00', u'25^4']
	part3_incorrect_attempt
					('0:00:30', u'25^2')
					('0:00:43', u'26^2')
					('0:01:10', u'(26^3)')
					('0:01:38', u'25^4')
	part3_correct_attempt
					['0:02:19', u'(26^4)-(25^4)']

91 Student ID:eyhu

	first_attempt
					2015-10-02 01:26:46
	part1_correct_attempt
					['0:00:00', u'26^3']
	part2_correct_attempt
					['0:00:00', u'25^3']
	part3_incorrect_attempt
					('0:00:00', u'3*26^2')
					('0:02:39', u'25^2 + 25 + 25 + 1')
	part3_correct_attempt
					['0:06:59', u'(26^3) - (25^3)']

92 Student ID:ppanourg

	first_attempt
					2015-10-02 08:28:07
	part1_correct_attempt
					['0:00:00', u'26^5']
	part2_correct_attempt
					['0:00:00', u'25^5']
	part3_incorrect_attempt
					('0:00:00', u'26^4')
					('0:02:11', u'5*26^4')
					('5 days, 21:58:09', u'5!*26^4')
					('5 days, 22:00:35', u'26^4')
	part3_correct_attempt
					['5 days, 22:04:34', u'26^5 - 25^5']

93 Student ID:ewbrenna

	first_attempt
					2015-10-04 04:17:49
	part1_correct_attempt
					['0:00:00', u'26^5']
	part2_correct_attempt
					['0:00:00', u'25^5']
	part3_incorrect_attempt
					('0:00:00', u'5*(26^4)')
	part3_correct_attempt
					['0:50:54', u'26^5-25^5']

94 Student ID:masaro

	first_attempt
					2015-10-05 15:33:06
	part1_correct_attempt
					['0:00:00', u'26^5']
	part2_correct_attempt
					['0:00:00', u'25^5']
	part3_incorrect_attempt
					('0:00:00', u'5*26^4')
	part3_correct_attempt
					['0:03:33', u'26^5-25^5']

95 Student ID:rwthomps

	first_attempt
					2015-10-06 20:06:38
	part1_correct_attempt
					['0:00:00', u'26^5']
	part2_correct_attempt
					['0:00:00', u'25^5']
	part3_incorrect_attempt
					('0:00:00', u'26^4')
	part3_correct_attempt
					['0:06:11', u'26^5 - 25^5']

96 Student ID:pcdo

	first_attempt
					2015-10-06 20:30:14
	part1_correct_attempt
					['0:00:00', u'26^6']
	part2_correct_attempt
					['0:02:43', u'25^6']
	part3_incorrect_attempt
					('0:08:35', u'26^6 - 25^6 - 5*25^5')
					('0:09:37', u'26^6 - 25^6 - 6*25^5')
	part3_correct_attempt
					['0:10:20', u'26^6 - 25^6']

97 Student ID:e9brown

	first_attempt
					2015-10-08 02:11:55
	part1_correct_attempt
					['0:00:00', u'26^3']
	part2_correct_attempt
					['0:00:00', u'25^3']
	part3_incorrect_attempt
					('0:02:57', u'(26^2-4)3')
	part3_correct_attempt
					['0:07:27', u'(25^2)3 + 76']

98 Student ID:vsosnovs

	first_attempt
					2015-10-04 18:16:20
	part1_correct_attempt
					['0:00:00', u'26^6']
	part2_correct_attempt
					['0:00:20', u'25^6']
	part3_incorrect_attempt
					('0:01:59', u'(25^6)+ 1')
					('0:02:27', u'6!')
					('0:04:58', u'6!/5!')
	part3_correct_attempt
					['0:05:49', u'(26^6)- 25^6']

99 Student ID:jdeon

	first_attempt
					2015-10-03 19:43:42
	part1_correct_attempt
					['0:00:00', u'26^3']
	part2_correct_attempt
					['0:00:13', u'25^3']
	part3_incorrect_attempt
					('0:01:08', u'26^2')
					('0:01:44', u'26^2*3 - 2')
					('0:01:50', u'26^2*3 - 3')
					('0:02:47', u'(26!/(24!*2!)) * 3')
	part3_correct_attempt
					['0:03:23', u'(26^3)-(25^3)']

100 Student ID:b1green

	first_attempt
					2015-10-08 18:55:10
	part1_correct_attempt
					['0:00:00', u'26*26*26']
	part2_correct_attempt
					['0:00:00', u'25*25*25']
	part3_incorrect_attempt
					('0:02:26', u'25*26*26')
					('0:03:52', u'26*26')
	part3_correct_attempt
					['0:41:54', u'26*26*26-25*25*25']

101 Student ID:p4kumar

	first_attempt
					2015-10-08 19:16:37
	part1_correct_attempt
					['0:00:00', u'26^5']
	part2_correct_attempt
					['0:00:00', u'25^5']
	part3_incorrect_attempt
					('0:00:43', u'(25^4) * 5')
					('0:01:23', u'(26^4)')
	part3_correct_attempt
					['0:08:48', u'(26^5) - (25^5)']

102 Student ID:j6quach

	first_attempt
					2015-10-06 18:21:10
	part1_correct_attempt
					['0:00:00', u'26^3']
	part2_correct_attempt
					['0:00:00', u'25^3']
	part3_incorrect_attempt
					('0:00:00', u'26^2')
					('0:04:40', u'3*(26^2)')
	part3_correct_attempt
					['0:28:50', u'26^3 - 25^3']

103 Student ID:gsrandha

	first_attempt
					2015-10-02 02:09:07
	part1_correct_attempt
					['0:00:00', u'26*26*26*26*26*26']
	part2_correct_attempt
					['0:00:12', u'25*25*25*25*25*25']
	part3_incorrect_attempt
					('0:01:04', u'26*26*26*26*26*1')
					('0:01:27', u'1*26*26*26*26*26')
	part3_correct_attempt
					['0:07:16', u'(26*26*26*26*26*26)-(25*25*25*25*25*25)']

104 Student ID:bmilton

	first_attempt
					2015-10-04 01:49:46
	part1_correct_attempt
					['0:00:00', u'26^3']
	part2_correct_attempt
					['0:00:14', u'25^3']
	part3_incorrect_attempt
					('0:00:14', u'3*26^2')
	part3_correct_attempt
					['0:01:39', u'26^3 - 25^3']

105 Student ID:yypan

	first_attempt
					2015-10-02 05:04:37
	part1_correct_attempt
					['0:00:00', u'26^5']
	part2_correct_attempt
					['0:00:30', u'25^5']
	part3_incorrect_attempt
					('0:04:02', u'25*26')
					('0:04:25', u'25*26^4')
					('0:06:06', u'5*25*26^4')
	part3_correct_attempt
					['0:12:28', u'26^5-25^5']

106 Student ID:dcgriffi

	first_attempt
					2015-10-08 06:38:28
	part1_correct_attempt
					['0:00:00', u'26^5']
	part2_correct_attempt
					['0:00:00', u'25^5']
	part3_incorrect_attempt
					('0:00:00', u'26^4')
					('0:02:21', u'26^4')
					('0:02:59', u'5*(26^4)')
					('0:03:05', u'4*(26^4)')
	part3_correct_attempt
					['0:03:51', u'(26^5)-(25^5)']

107 Student ID:rsmurlo

	first_attempt
					2015-10-08 02:30:19
	part1_correct_attempt
					['0:00:00', u'26^4']
	part2_correct_attempt
					['0:00:00', u'25^4']
	part3_incorrect_attempt
					('0:00:00', u'4*26^3')
					('0:03:24', u'(2*(4*25^3))*(6*25^2)+1')
					('0:04:08', u'(4*25^3)*(6*25^2)*(4*25)+1')
	part3_correct_attempt
					['0:05:37', u'(26^4)-(25^4)']

108 Student ID:anl114

	first_attempt
					2015-10-08 06:59:12
	part1_correct_attempt
					['0:00:00', u'26^3']
	part2_correct_attempt
					['0:00:00', u'25^3']
	part3_incorrect_attempt
					('0:00:34', u'26*26')
	part3_correct_attempt
					['0:01:06', u'(26^3)-(25^3)']

109 Student ID:pnquach

	first_attempt
					2015-10-08 06:37:02
	part1_correct_attempt
					['0:00:00', u'26^4']
	part2_correct_attempt
					['0:00:00', u'25^4']
	part3_incorrect_attempt
					('0:00:00', u'(26^3)*4 - 4')
					('0:00:30', u'(26^3)*4 - 1')
	part3_correct_attempt
					['0:02:15', u'26^4 - 25^4']

110 Student ID:achinn

	first_attempt
					2015-10-06 19:35:35
	part1_correct_attempt
					['0:00:00', u'26^6']
	part2_correct_attempt
					['0:00:00', u'25^6']
	part3_incorrect_attempt
					('0:00:00', u'26^5')
					('0:01:31', u'25^5')
	part3_correct_attempt
					['0:19:23', u'26^6-25^6']

111 Student ID:kalang

	first_attempt
					2015-10-05 22:50:05
	part1_correct_attempt
					['0:00:00', u'26^6']
	part2_correct_attempt
					['0:00:09', u'25^6']
	part3_incorrect_attempt
					('0:00:25', u'25^5')
					('0:00:32', u'25^6')
					('0:01:07', u'26^5')
					('0:13:29', u'6*26^5')
					('0:15:16', u'6*26^6')
					('0:16:42', u'26^5')
	part3_correct_attempt
					['0:17:50', u'26^6-25^6']

112 Student ID:msaguiar

	first_attempt
					2015-10-06 04:32:43
	part1_correct_attempt
					['0:00:00', u'26^3']
	part2_correct_attempt
					['0:00:00', u'25^3']
	part3_incorrect_attempt
					('0:00:00', u'26*26')
					('0:00:27', u'3(26*26)')
					('0:05:20', u'3(1*26*26)')
					('0:06:37', u'1*26*26')
	part3_correct_attempt
					['0:09:30', u'26^3-25^3']

113 Student ID:aalhaida

	first_attempt
					2015-10-08 12:38:07
	part1_correct_attempt
					['0:00:00', u'26^6']
	part2_correct_attempt
					['0:00:00', u'25^6']
	part3_incorrect_attempt
					('0:00:00', u'6*(26^5)')
	part3_correct_attempt
					['0:19:05', u'(26^6)-(25^6)']

114 Student ID:hah008

	first_attempt
					2015-10-08 07:10:44
	part1_correct_attempt
					['0:00:00', u'26^6']
	part2_correct_attempt
					['-1 day, 16:30:46', u'25^6']
	part3_incorrect_attempt
					('0:01:09', u'26^6')
					('0:14:21', u'26^5')
					('12:27:46', u'(26^4)')
					('12:28:32', u'25^4')
					('12:28:55', u'26^5')
	part3_correct_attempt
					['12:33:31', u'26^6- 25^6']

115 Student ID:haliew

	first_attempt
					2015-10-06 05:07:20
	part1_correct_attempt
					['0:00:00', u'26^5']
	part2_correct_attempt
					['0:00:00', u'25^5']
	part3_incorrect_attempt
					('0:00:00', u'26^5')
					('0:11:40', u'25^5 +((26^5/2))')
					('0:11:57', u'25^5 +((26^5/26))')
	part3_correct_attempt
					['0:12:51', u'26^5-25^5']

116 Student ID:ajabasa

	first_attempt
					2015-10-05 21:34:18
	part1_correct_attempt
					['0:00:00', u'26^4']
	part2_correct_attempt
					['0:01:01', u'25^4']
	part3_incorrect_attempt
					('0:01:13', u'26^3')
	part3_correct_attempt
					['0:02:55', u'26^4-25^4']

117 Student ID:jnn015

	first_attempt
					2015-10-03 21:43:03
	part1_correct_attempt
					['0:00:00', u'26^6']
	part2_correct_attempt
					['0:00:34', u'25^6']
	part3_incorrect_attempt
					('0:18:59', u'1 + 6*25^5 + 6!/2! * 25^4 + 6!/3!*25^3 + 6!/4!*25^2 +6!/5! *25')
					('0:20:34', u'1 + 6!*25^5 + 6!/2! * 25^4 + 6!/3!*25^3 + 6!/4!*25^2 +6!/5! *25')
					('0:41:43', u'6*25^5 + 6*5*25^4 + 6 * 5 * 4 * 25^3 + 6*5*4*3 *25^2 + 6* 5 * 4 * 3 *2*25 + 1')
	part3_correct_attempt
					['0:43:22', u'6*25^5 + 6*5*25^4/2! + 6 * 5 * 4 * 25^3/3! + 6*5*4*3 *25^2/4! + 6* 5 * 4 * 3 *2*25/5! + 1']

118 Student ID:dpereira

	first_attempt
					2015-10-03 21:16:31
	part1_correct_attempt
					['0:00:00', u'26^4']
	part2_correct_attempt
					['0:00:00', u'25^4']
	part3_incorrect_attempt
					('0:00:00', u'26^3')
					('0:02:08', u'25*26*26*26*4')
	part3_correct_attempt
					['0:12:55', u'26^4 - 25^4']

119 Student ID:hmshah

	first_attempt
					2015-10-06 02:10:55
	part1_correct_attempt
					['0:00:00', u'26*26*26*26']
	part2_correct_attempt
					['0:00:32', u'25*25*25*25']
	part3_incorrect_attempt
					('0:00:32', u'26*26*26')
					('0:00:47', u'26*26*26*4')
					('0:13:02', u'26*26*26')
	part3_correct_attempt
					['2 days, 19:57:22', u'(26*26*26*26)-(25*25*25*25)']

120 Student ID:dtea

	first_attempt
					2015-10-08 19:00:09
	part1_correct_attempt
					['0:00:00', u'26**4']
	part2_correct_attempt
					['0:00:06', u'25**4']
	part3_incorrect_attempt
					('0:00:21', u'26*26*26')
					('0:01:04', u'26*26*26*25')
					('0:01:45', u'26*26*26*4')
					('0:03:40', u'4*26*C(4,1)')
					('0:04:04', u'4*26*4')
					('0:04:09', u'4*26*4!')
					('2:33:23', u'26**3')
					('2:52:18', u'26**3')
	part3_correct_attempt
					['2:52:58', u'26**4-25**4']

121 Student ID:sthapa

	first_attempt
					2015-10-06 06:54:40
	part1_correct_attempt
					['0:00:00', u'26^5']
	part2_correct_attempt
					['0:00:20', u'25^5']
	part3_incorrect_attempt
					('0:01:12', u'25^5 + 1')
	part3_correct_attempt
					['0:03:58', u'26^5 - 25^5']

122 Student ID:kquong

	first_attempt
					2015-10-03 21:30:30
	part1_correct_attempt
					['0:00:00', u'26^6']
	part2_correct_attempt
					['0:00:17', u'25^6']
	part3_incorrect_attempt
					('0:00:36', u'26^5*26')
					('0:00:46', u'25^5*26')
	part3_correct_attempt
					['0:10:34', u'26^6-25^6']

123 Student ID:vasharma

	first_attempt
					2015-10-05 06:45:09
	part1_correct_attempt
					['0:00:00', u'26*26*26*26']
	part2_correct_attempt
					['0:00:15', u'25*25*25*25']
	part3_incorrect_attempt
					('0:00:55', u'4*24*24*24*24')
					('0:01:08', u'4*1*24*24*24')
					('0:01:28', u'(24*24*24)(24*24*24)(24*24*24)(24*24*24)')
					('0:03:55', u'4*(26*26*26)')
	part3_correct_attempt
					['0:05:44', u'26*26*26*26-25*25*25*25']

124 Student ID:hpc001

	first_attempt
					2015-10-03 00:18:57
	part1_correct_attempt
					['0:00:00', u'26^6']
	part2_correct_attempt
					['0:00:00', u'25^6']
	part3_incorrect_attempt
					('0:00:00', u'26^5')
					('0:03:00', u'26^6')
	part3_correct_attempt
					['0:04:19', u'26^6 - 25^6']

125 Student ID:syip

	first_attempt
					2015-10-03 20:18:50
	part1_correct_attempt
					['0:00:00', u'26^3']
	part2_correct_attempt
					['0:00:00', u'25^3']
	part3_incorrect_attempt
					('0:00:00', u'3*26^2')
					('0:01:24', u'3*26^2 - 3')
	part3_correct_attempt
					['0:03:56', u'26^3 - 25^3']

126 Student ID:xweng

	first_attempt
					2015-10-07 07:05:23
	part1_correct_attempt
					['0:00:00', u'26^4']
	part2_correct_attempt
					['0:00:20', u'25^4']
	part3_incorrect_attempt
					('0:01:03', u'3*26^3')
	part3_correct_attempt
					['0:02:02', u'26^4-25^4']

127 Student ID:c3chung

	first_attempt
					2015-10-07 23:29:37
	part1_correct_attempt
					['0:00:00', u'26^5']
	part2_correct_attempt
					['0:00:00', u'25^5']
	part3_incorrect_attempt
					('0:00:00', u'26^4')
					('0:03:35', u'(25^4)5')
					('0:10:09', u'32(26^4)')
	part3_correct_attempt
					['18:07:17', u'(26^5)-(25^5)']

128 Student ID:ajvanega

	first_attempt
					2015-10-07 23:43:09
	part1_correct_attempt
					['0:00:00', u'26^6']
	part2_correct_attempt
					['0:09:06', u'25^6']
	part3_incorrect_attempt
					('0:10:06', u'25^6')
					('0:10:18', u'27^6')
					('0:10:59', u'25^5')
					('0:11:09', u'26^5')
					('0:17:23', u'(25^5)26')
					('0:18:44', u'26^5')
					('0:20:02', u'25^5')
	part3_correct_attempt
					['3:03:23', u'(26^6)-(25^6)']

129 Student ID:jmiclat

	first_attempt
					2015-10-08 09:01:23
	part1_correct_attempt
					['0:00:00', u'26^5']
	part2_correct_attempt
					['0:00:00', u'25^5']
	part3_incorrect_attempt
					('0:01:07', u'26*25*25*25*25*25')
					('0:01:15', u'26*25*25*25*25')
					('11:08:40', u'5*26^4')
					('11:20:52', u'5*26*25*24*23')
					('11:25:05', u'5(26^4)')
	part3_correct_attempt
					['12:04:30', u'26^5-25^5']

130 Student ID:mtrafeca

	first_attempt
					2015-10-02 06:16:49
	part1_correct_attempt
					['0:00:00', u'26^5']
	part2_correct_attempt
					['0:26:12', u'25^5']
	part3_incorrect_attempt
					('0:27:13', u'4!')
	part3_correct_attempt
					['12:11:57', u'(26^5)-25^5']

131 Student ID:kgrozav

	first_attempt
					2015-10-02 21:18:30
	part1_correct_attempt
					['0:00:00', u'26^4']
	part2_correct_attempt
					['0:00:13', u'25^4']
	part3_incorrect_attempt
					('0:01:00', u'26^3')
					('0:11:34', u'4*((26^3) + (26^2) + 26)')
	part3_correct_attempt
					['0:13:33', u'(26^4) - (25^4)']

132 Student ID:j2phung

	first_attempt
					2015-10-06 19:16:32
	part1_correct_attempt
					['0:00:00', u'26^6']
	part2_correct_attempt
					['0:02:37', u'25^6']
	part3_incorrect_attempt
					('0:02:37', u'26^5')
					('0:15:59', u'(26^5)+(26^4)+(26^3)+(26^2)+(26^1)+(26^0)')
					('0:23:39', u'25^5 + 25^4 +25^3 + 25^2 + 25^1 + 21^0')
	part3_correct_attempt
					['0:28:25', u'26^6-25^6']












