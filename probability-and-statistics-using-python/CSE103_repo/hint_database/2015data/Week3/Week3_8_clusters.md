#Problem 8

	(part 1,2,3 are multiple choice questions, below is part 4)
	
    $R1=random(5,20,1);  # Number of balls (both white and black)
    $R2=random(2,$R1-1,1);  # Number of white balls

    *PROBLEM:*
    Suppose we have [$R1] bins, numbered 1,...,[$R1] and that we have [$R1] balls,
    [$R2] of them white and [$R1-$R2] of them black.

    o How many white/black patterns can one make by placing the balls in the bins? [________]{"$R1!/($R2!*($R1-$R2)!)"}
## Part 4

### (43) Mistake Group Digits of size 43




### (22) Mistake Group ['R.0'] of size 22
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|16!/[4!*(16-4)!]	|16!/(16-4)!	|[('R.0', 20922789888000, u'16!', u'16!')]	|
|1	|6!/[3!*(6-3)!]	|6!/(4!2!)	|[('R.0', 720, u'6!', u'6!')]	|
|2	|17!/[4!*(17-4)!]	|17!/3!	|[('R.0', 355687428096000, u'17!', u'17!')]	|
|3	|15!/[2!*(15-2)!]	|15!/(15!(15-15)!)	|[('R.0', 1307674368000, u'15!', u'15!')]	|
|4	|9!/[5!*(9-5)!]	|9!/(9-5)!	|[('R.0', 362880, u'9!', u'9!')]	|
|5	|9!/[5!*(9-5)!]	|9!/(9-4)!	|[('R.0', 362880, u'9!', u'9!')]	|
|6	|15!/[7!*(15-7)!]	|15!/(15!)	|[('R.0', 1307674368000, u'15!', u'15!')]	|
|7	|20!/[11!*(20-11)!]	|20!/(2!18!)	|[('R.0', 2432902008176640000, u'20!', u'20!')]	|
|8	|19!/[18!*(19-18)!]	|19! / 1!(19-1)!	|[('R.0', 121645100408832000, u'19!', u'19! / 1!')]	|
|9	|7!/[5!*(7-5)!]	|7!/(5!)	|[('R.0', 5040, u'7!', u'7!')]	|
|10	|13!/[8!*(13-8)!]	|13!/((13-2)! * 2!)	|[('R.0', 6227020800, u'13!', u'13!')]	|
|11	|14!/[2!*(14-2)!]	|14!/12!	|[('R.0', 87178291200, u'14!', u'14!')]	|
|12	|14!/[2!*(14-2)!]	|14! * (14/(2!12!))	|[('R.0', 87178291200, u'14!', u'14!')]	|
|13	|14!/[2!*(14-2)!]	|14! / P(14,2)	|[('R.0', 87178291200, u'14!', u'14!')]	|
|14	|15!/[9!*(15-9)!]	|15!/9!	|[('R.0', 1307674368000, u'15!', u'15!')]	|
|15	|15!/[10!*(15-10)!]	|15!/10!	|[('R.0', 1307674368000, u'15!', u'15!')]	|
|16	|13!/[9!*(13-9)!]	|13!/4!	|[('R.0', 6227020800, u'13!', u'13!')]	|
|17	|13!/[9!*(13-9)!]	|13!/9!	|[('R.0', 6227020800, u'13!', u'13!')]	|
|18	|6!/[3!*(6-3)!]	|6!(3!)	|[('R.0', 720, u'6!', u'6!')]	|
|19	|11!/[6!*(11-6)!]	|11!/(2!(9!))	|[('R.0', 39916800, u'11!', u'11!')]	|
|20	|13!/[4!*(13-4)!]	|13!/(11!*2!)	|[('R.0', 6227020800, u'13!', u'13!')]	|




### (18) Mistake Group Fraction of size 18




### (4) Mistake Group ['R.1.0'] of size 4
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|9!/[8!*(9-8)!]	|17!/(8!9!)	|[('R.1.0', 40320, u'8!', u'8!')]	|
|1	|7!/[6!*(7-6)!]	|13!/(6!*7!)	|[('R.1.0', 720, u'6!', u'6!')]	|
|2	|19!/[14!*(19-14)!]	|16!/(14!(16-14)!)	|[('R.1.0', 87178291200, u'14!', u'14!')]	|
|3	|18!/[13!*(18-13)!]	|20!/(13!(20-13)!)	|[('R.1.0', 6227020800, u'13!', u'13!')]	|




### (3) Mistake Group ['R.0', 'R.1'] of size 3
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|17!/[15!*(17-15)!]	|17!(15!2!)	|[('R.0', 355687428096000, u'17!', u'17!'), ('R.1', 2615348736000.0, u'15!*(17-15)!', u'15!2!')]	|
|1	|6!/[3!*(6-3)!]	|6!(3!3!)	|[('R.0', 720, u'6!', u'6!'), ('R.1', 36.0, u'3!*(6-3)!', u'3!3!')]	|
|2	|13!/[2!*(13-2)!]	|13!(2!11!)	|[('R.0', 6227020800, u'13!', u'13!'), ('R.1', 79833600.0, u'2!*(13-2)!', u'2!11!')]	|




### (3) Mistake Group ['R.0', 'R.1.1'] of size 3
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|19!/[16!*(19-16)!]	|19!/ (13!(3)!)	|[('R.0', 121645100408832000, u'19!', u'19!'), ('R.1.1', 6, u'(19-16)!', u'(3)!')]	|
|1	|14!/[2!*(14-2)!]	|14! * (14!/2!12!)	|[('R.0', 87178291200, u'14!', u'14!'), ('R.1.1', 479001600, u'(14-2)!', u'12!')]	|
|2	|14!/[2!*(14-2)!]	|14! * (14/(12!))	|[('R.0', 87178291200, u'14!', u'14!'), ('R.1.1', 479001600, u'(14-2)!', u'12!')]	|




### (3) Mistake Group Wrong_Sign of size 3




### (2) Mistake Group ['R.1.1'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|19!/[12!*(19-12)!]	|(19!*19!)/[(19-7)!(19-12)!(12!)(7!)]	|[('R.1.1', 5040, u'(19-12)!', u'7!')]	|
|1	|13!/[9!*(13-9)!]	|(13!/9!)*(13!/4!)	|[('R.1.1', 24, u'(13-9)!', u'4!')]	|




### (2) Mistake Group ['R.0', 'R.1.0'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|9!/[7!*(9-7)!]	|9! / (7! * 3!)	|[('R.0', 362880, u'9!', u'9!'), ('R.1.0', 5040, u'7!', u'7!')]	|
|1	|9!/[6!*(9-6)!]	|9!/(6!(4!))	|[('R.0', 362880, u'9!', u'9!'), ('R.1.0', 720, u'6!', u'6!')]	|




### (1) Mistake Group ['R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|19!/[16!*(19-16)!]	|3*[19!]/[(3!)(16!)]	|[('R.1', 125536739328000.0, u'16!*(19-16)!', u'(3!)(16!)')]	|




### (1) Mistake Group ['R.0', 'R.1.1.0'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|14!/[2!*(14-2)!]	|14! / (14!/12!)	|[('R.0', 87178291200, u'14!', u'14!'), ('R.1.1.0', 12.0, u'14-2', u'12')]	|




### (55) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:b3hwang

	first_attempt
					2015-10-14 18:03:24
	part4_incorrect_attempt
					('0:03:05', u'C(13,2)')
	part4_correct_attempt
					['0:07:14', u'13!/((13-8)! * 8!)']

1 Student ID:jfalcone

	first_attempt
					2015-10-14 21:51:22
	part4_incorrect_attempt
					('0:12:26', u'8!/[5!(3)!] + 8!/[3!(5)!]')
					('0:15:04', u'8!/(5!)(3!)')
	part4_correct_attempt
					['0:15:13', u'8!/(5!3!)']

2 Student ID:ccn001

	first_attempt
					2015-10-12 21:17:07
	part4_incorrect_attempt
					('0:00:00', u'18 * 16 * 2')
					('0:01:31', u'16! * 2!')
					('0:03:13', u'18!/(16!(18-16)!)+18!/(2!(18-2)!)')
					('0:03:35', u'18*18!/(16!(18-16)!)+18!/(2!(18-2)!)')
					('18:38:38', u'((18+18-1)!)/(18!*(18-1)!)')
					('19:11:09', u'(35!)/(2*17!*(35-17)!)')
					('19:55:43', u'18^18')
					('20:00:26', u'18^16 + 18^2')
					('1 day, 1:49:24', u'18! - (18!/(18-16)!) - (18!/(18-2)!)')
	part4_correct_attempt
					['1 day, 1:56:48', u'18!/(16!*2!)']

3 Student ID:aggouw

	first_attempt
					2015-10-15 07:41:55
	part4_incorrect_attempt
					('0:10:20', u'9!')
	part4_correct_attempt
					['0:10:41', u'9!/(7!*2!)']

4 Student ID:lrlai

	first_attempt
					2015-10-11 00:00:50
	part4_incorrect_attempt
					('0:02:47', u'C(7+3-1, 7)')
					('0:03:18', u'9!/(7!*2)')
					('2 days, 0:37:04', u'C(12,6)*C(7,6)')
					('2 days, 0:40:07', u'12!/(6!(6!))*6')
					('2 days, 0:40:41', u'12!/(6!(6!))*7')
					('2 days, 1:22:16', u'C(7,6)+C(7,1)')
					('2 days, 1:22:58', u'C(7,1)')
	part4_correct_attempt
					['2 days, 1:23:03', u'7']

5 Student ID:glcohen

	first_attempt
					2015-10-13 04:44:23
	part4_incorrect_attempt
					('0:00:00', u'11!')
	part4_correct_attempt
					['0:00:39', u'11!/(3!8!)']

6 Student ID:ppanourg

	first_attempt
					2015-10-14 21:43:06
	part4_incorrect_attempt
					('0:01:38', u'17!')
	part4_correct_attempt
					['0:03:55', u'17!/(12!(5!))']

7 Student ID:ewbrenna

	first_attempt
					2015-10-12 19:41:05
	part4_incorrect_attempt
					('0:01:26', u'6!/2!*4!')
	part4_correct_attempt
					['0:01:34', u'6!/(2!*4!)']

8 Student ID:masaro

	first_attempt
					2015-10-10 00:23:16
	part4_incorrect_attempt
					('0:00:00', u'14!/9!+14!/5!')
					('0:03:34', u'14!/(5!*9!)+14!/(5!*9)')
	part4_correct_attempt
					['0:27:34', u'14!/(5!*9!)+1']

9 Student ID:rwthomps

	first_attempt
					2015-10-11 22:09:39
	part4_incorrect_attempt
					('0:00:00', u'6!/2!(6 - 2)!')
	part4_correct_attempt
					['0:00:42', u'6!/[2! * (6 - 2)!]']

10 Student ID:jew037

	first_attempt
					2015-10-14 03:53:03
	part4_incorrect_attempt
					('0:05:10', u'C(12,7) + C(12,5)')
	part4_correct_attempt
					['0:07:07', u'12!/(7!*5!)']

11 Student ID:pcdo

	first_attempt
					2015-10-13 18:31:14
	part4_incorrect_attempt
					('0:08:54', u'P(5,4)')
	part4_correct_attempt
					['0:09:12', u'5!/(4!(5-4)!)']

12 Student ID:mroknich

	first_attempt
					2015-10-13 18:28:32
	part4_incorrect_attempt
					('0:02:45', u'C(11,3) * C(11,8)')
	part4_correct_attempt
					['0:03:50', u'11!/(3!*(8!))']

13 Student ID:t2li

	first_attempt
					2015-10-14 03:32:38
	part4_incorrect_attempt
					('0:27:27', u'9!*4*6!*3!')
					('0:29:22', u'6!3!9!')
					('0:29:35', u'6!3!9!/4')
					('0:44:28', u'P(9,6)P(9,3)')
					('1:31:45', u'7056*9!')
					('1:39:02', u'C(9,6) + C(9,3)')
	part4_correct_attempt
					['1:50:10', u'84']

14 Student ID:n2patil

	first_attempt
					2015-10-13 15:27:44
	part4_incorrect_attempt
					('0:02:41', u'5!/(5-3)!2!')
	part4_correct_attempt
					['0:04:46', u'5!/(3!2!)']

15 Student ID:jic212

	first_attempt
					2015-10-11 22:45:52
	part4_incorrect_attempt
					('0:05:04', u'4!*13!')
					('0:05:20', u'(4!)*(13!)')
					('0:07:02', u'C(10,4)')
					('0:09:03', u'4!')
					('0:12:30', u'4^4*13^13')
					('0:12:48', u'4!*13!')
	part4_correct_attempt
					['0:13:09', u'17!/(4!*13!)']

16 Student ID:s2chaudh

	first_attempt
					2015-10-13 05:41:55
	part4_incorrect_attempt
					('-1 day, 23:52:13', u'C(19,3)+C(27,11)')
					('0:02:13', u'12!*4!')
					('11:35:19', u'C(16,4)*C(16,12)')
					('14:31:01', u'C(19,15)*C(27,15)')
					('1 day, 20:48:58', u'P(19,15)*P(27,15)')
					('1 day, 21:00:12', u'(16!/(4!*12!))*(16!/(12!*4!))')
					('1 day, 21:00:30', u'(16!/(4!*12!))+(16!/(12!*4!))')
	part4_correct_attempt
					['1 day, 21:25:09', u'(16!/(12!*4!))']

17 Student ID:syc078

	first_attempt
					2015-10-15 00:15:03
	part4_incorrect_attempt
					('-1 day, 23:22:44', u'3! * 4!')
	part4_correct_attempt
					['0:01:46', u'7! / (3! 4!)']

18 Student ID:vasharma

	first_attempt
					2015-10-10 02:55:16
	part4_incorrect_attempt
					('0:03:54', u'10!/[(10-4)!4!]')
	part4_correct_attempt
					['0:04:02', u'14!/[(14-4)!4!]']

19 Student ID:jnatale

	first_attempt
					2015-10-15 03:20:07
	part4_incorrect_attempt
					('0:04:43', u'C(17,14)*C(17,3)')
					('0:08:13', u'(17!/(3)!)*(17!/(14)!)')
					('0:10:18', u'17!')
	part4_correct_attempt
					['0:12:55', u'17!/(14!(17-14)!)']

20 Student ID:ffhaddad

	first_attempt
					2015-10-10 14:56:46
	part4_incorrect_attempt
					('0:06:19', u'(33 16)')
					('0:15:32', u'33!/(16!17!)')
					('0:23:18', u'[22!/(6!(22-6)!)][27!/(16!(27-16)!)]')
					('0:35:09', u'33!/(16!17!)')
					('0:56:17', u'[22!/(6!16!)][27!/(11!16!)]')
					('0:56:27', u'[22!/(6!16!)]+[27!/(11!16!)]')
					('0:57:03', u'[22!/(6!16!)]*[27!/(11!16!)]')
					('0:59:07', u'13037895*74613')
					('0:59:16', u'13037895+74613')
	part4_correct_attempt
					['1:02:40', u'17!/(6!11!)']

21 Student ID:dkostins

	first_attempt
					2015-10-15 18:17:52
	part4_incorrect_attempt
					('0:01:14', u'14!/((14-2)!2!)')
	part4_correct_attempt
					['0:02:30', u'16!/((16-2)!2!)']

22 Student ID:mnrahman

	first_attempt
					2015-10-15 06:57:03
	part4_incorrect_attempt
					('0:00:00', u'5!/(4!(5-4)!)')
					('0:00:21', u'5!/4!(5-4)!')
	part4_correct_attempt
					['0:00:47', u'6!/(3!(6-3)!)']

23 Student ID:agarango

	first_attempt
					2015-10-15 14:48:17
	part4_incorrect_attempt
					('0:16:35', u'1.3076744*10^12')
	part4_correct_attempt
					['0:31:33', u'3003']

24 Student ID:dsmonaha

	first_attempt
					2015-10-13 17:19:29
	part4_incorrect_attempt
					('0:02:59', u'15!')
	part4_correct_attempt
					['0:04:43', u'15!/(7!(8!))']

25 Student ID:mrchin

	first_attempt
					2015-10-12 03:22:48
	part4_incorrect_attempt
					('0:07:13', u'19!/[(17)!*2!] + 19!/[(2)!*17!]')
					('0:08:34', u'2^17')
	part4_correct_attempt
					['2 days, 19:11:57', u'19!/(2!*17!)']

26 Student ID:lalacson

	first_attempt
					2015-10-11 16:02:46
	part4_incorrect_attempt
					('0:02:07', u'C(6,2)')
	part4_correct_attempt
					['0:02:46', u'6!/(3!3!)']

27 Student ID:agian

	first_attempt
					2015-10-15 07:17:25
	part4_incorrect_attempt
					('-1 day, 23:59:13', u'11!/[7!*(11-7)!]')
	part4_correct_attempt
					['0:00:00', u'9!/[4!*(9-4)!]']

28 Student ID:tol003

	first_attempt
					2015-10-13 23:41:15
	part4_incorrect_attempt
					('0:00:00', u'15!/[5!(15-5)!]*[15!/[10!(15-10)!]]')
	part4_correct_attempt
					['0:00:47', u'15!/[5!(15-5)!]']

29 Student ID:vsosnovs

	first_attempt
					2015-10-15 03:37:58
	part4_incorrect_attempt
					('0:13:39', u'16!/4!12!')
	part4_correct_attempt
					['0:13:53', u'16!/(4!12!)']

30 Student ID:aakumar

	first_attempt
					2015-10-11 01:14:46
	part4_incorrect_attempt
					('0:03:17', u'15!')
	part4_correct_attempt
					['0:03:33', u'15!/[9!6!]']

31 Student ID:hachrist

	first_attempt
					2015-10-14 21:58:11
	part4_incorrect_attempt
					('0:04:00', u'((19!)/((7!)12!)) * ((19!)/((12!)*7!))')
					('0:04:23', u'((19!)/((7!)12!)) + ((19!)/((12!)*7!))')
	part4_correct_attempt
					['0:12:39', u'19!/(12!*7!)']

32 Student ID:jhw015

	first_attempt
					2015-10-15 01:53:15
	part4_incorrect_attempt
					('0:04:35', u'14!/2!12!')
					('0:09:37', u'14!')
	part4_correct_attempt
					['0:10:10', u'91']

33 Student ID:hkhodada

	first_attempt
					2015-10-10 16:24:50
	part4_incorrect_attempt
					('0:38:17', u'10!')
					('2:10:23', u'2*4!*13!')
					('1 day, 10:15:14', u'10!')
					('1 day, 10:15:21', u'13!')
					('1 day, 10:36:15', u'P(17,4)')
					('1 day, 10:39:05', u'17!')
					('1 day, 11:11:06', u'2*4!*13!')
					('1 day, 11:12:19', u'4!*C(17,4)')
					('1 day, 14:42:32', u'17!')
					('4 days, 2:48:51', u'17!')
	part4_correct_attempt
					['4 days, 2:50:52', u'2380']

34 Student ID:jit002

	first_attempt
					2015-10-15 04:17:52
	part4_incorrect_attempt
					('0:00:00', u'6*6!')
	part4_correct_attempt
					['0:02:18', u'11!/5!/6!']

35 Student ID:yeh013

	first_attempt
					2015-10-15 06:58:22
	part4_incorrect_attempt
					('0:08:20', u'12!/4!')
					('0:09:14', u'12!/8!')
	part4_correct_attempt
					['0:16:46', u'13!/(4!*9!)']

36 Student ID:pthsu

	first_attempt
					2015-10-10 19:20:03
	part4_incorrect_attempt
					('0:03:15', u'C(19,12)*C(19,7)')
	part4_correct_attempt
					['0:11:46', u'19!/(12!7!)']

37 Student ID:dsriniva

	first_attempt
					2015-10-15 19:48:31
	part4_incorrect_attempt
					('0:00:00', u'6+5+4+3+2+1')
	part4_correct_attempt
					['0:00:44', u'10!/(5!*5!)']

38 Student ID:etemlock

	first_attempt
					2015-10-09 21:07:47
	part4_incorrect_attempt
					('0:00:00', u'9!')
					('0:00:12', u'C(9,1)')
					('0:13:17', u'9!/1!')
	part4_correct_attempt
					['0:13:34', u'9!/(1!8!)']

39 Student ID:mtrafeca

	first_attempt
					2015-10-11 04:39:07
	part4_incorrect_attempt
					('17:49:08', u'15!')
					('17:49:21', u'15^15')

40 Student ID:cstringh

	first_attempt
					2015-10-12 21:47:38
	part4_incorrect_attempt
					('0:03:59', u'(17!/(15!(2!))) + (17!/(2!(15!)))')
	part4_correct_attempt
					['0:08:46', u'(17!/(15!(2!)))']

41 Student ID:csl030

	first_attempt
					2015-10-14 01:12:20
	part4_incorrect_attempt
					('0:02:52', u'C(20,2)')
	part4_correct_attempt
					['0:06:26', u'20!/(11!9!)']

42 Student ID:arc013

	first_attempt
					2015-10-13 02:56:35
	part4_incorrect_attempt
					('0:01:53', u'C(7,1)')
	part4_correct_attempt
					['0:02:02', u'7']

43 Student ID:rbdoming

	first_attempt
					2015-10-14 18:21:22
	part4_incorrect_attempt
					('0:00:00', u'(6 4)')
	part4_correct_attempt
					['0:01:37', u'15']

44 Student ID:mitopete

	first_attempt
					2015-10-13 17:42:31
	part4_incorrect_attempt
					('0:06:07', u'17!/(15!(17-15)!)+17!/(2!(17-2)!)')
	part4_correct_attempt
					['0:18:12', u'17!/(15!2!)']

45 Student ID:starinia

	first_attempt
					2015-10-15 01:12:06
	part4_incorrect_attempt
					('0:05:21', u'5!/((1!)(5-1)!) + 5!/((2!)(5-2)!) + 5!/((3!)(5-3)!) + 5!/((4!)(5-4)!) + 5!/((5!)(5-5)!)')
	part4_correct_attempt
					['0:06:21', u'((5!)/(5-3)!)/3!']

46 Student ID:m4salaza

	first_attempt
					2015-10-15 23:16:26
	part4_incorrect_attempt
					('0:02:00', u'15!')

47 Student ID:volim

	first_attempt
					2015-10-12 22:19:18
	part4_incorrect_attempt
					('-1 day, 23:56:36', u'(18!)/(16!)(2!)')
					('0:00:00', u'(18!)/(2!)(16!)')
	part4_correct_attempt
					['0:00:35', u'(18!)/((2!)(16!))']

48 Student ID:ajvanega

	first_attempt
					2015-10-14 17:45:17
	part4_incorrect_attempt
					('0:09:17', u'7*13')
					('0:10:00', u'14!')
					('0:10:17', u'9!5!')
	part4_correct_attempt
					['0:12:54', u'(14!)/(5!9!)']

49 Student ID:aordookh

	first_attempt
					2015-10-15 14:38:24
	part4_incorrect_attempt
					('0:01:15', u'C(11,2)')
	part4_correct_attempt
					['0:05:40', u'(11!/(6!(5!)))']

50 Student ID:akg009

	first_attempt
					2015-10-15 22:15:08
	part4_incorrect_attempt
					('0:02:10', u'8! / (8-6)!  + 8! / (8-2)!')
	part4_correct_attempt
					['0:03:35', u'8! / (2! * 6!)']

51 Student ID:sthapa

	first_attempt
					2015-10-15 04:26:37
	part4_incorrect_attempt
					('0:03:57', u'8!/(2!(8-2)!) + (8!/(6!(8-6)!))')
					('0:04:35', u'8!/(2!(8-2)!) + (8!/(4!(8-4)!))')
	part4_correct_attempt
					['0:06:38', u'8!/(2!*6!)']

52 Student ID:mjethani

	first_attempt
					2015-10-13 04:44:03
	part4_incorrect_attempt
					('0:11:04', u'8!')
					('0:14:48', u'8!')
	part4_correct_attempt
					['0:15:54', u'28']

53 Student ID:kosung

	first_attempt
					2015-10-15 05:50:43
	part4_incorrect_attempt
					('0:00:00', u'15!/7!8!')
	part4_correct_attempt
					['0:00:15', u'15!/(7!8!)']

54 Student ID:asp025

	first_attempt
					2015-10-15 01:57:41
	part4_incorrect_attempt
					('4:38:45', u'15!')
					('4:42:46', u'(15!/(10!(15-10)!))(15!/(5!(15-5)!))')
	part4_correct_attempt
					['4:43:06', u'(15!/(5!(15-5)!))']












