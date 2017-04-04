#Problem 4

    $R=random(4,9,1);
    $A1=Formula("[$R]^4");

    Suppose a seqeunce of 4 digits in the range 1-[$R] is chosen uniformly
    at random. What is the probability that the first and third digit are
    equal, the second and the fourth digits are equal, but the first and
    second digits are unequal?

    1.  We are going to use the standard formula for probability of sets
        in a discrete uniform distribution space: the probability of a set
        [`A`] in an event space [`\Omega`] is

        [``P(A) = \frac{|A|}{|\Omega|}``]

    2.  In the enumerator we place the _size_ of the sample space. This is
        easy, as we have [$R1] choices in each of the four locations the
        number of sequences, which is equal to the size of the sample
        space, thus [`|\Omega| =`] [__________]{"[$R]^4"} (remember that "2^3"
        means [`2^3`] )

    3.  Now we want to compute the size of the set [`A`]. To do that it is
        useful to realize that we need only concern ourselves with the
        choices of two digits, say digits 1 and 2.  This is because digit
        1 determines the value of digit 3 and digit 2 determines the value
        of digit [_]{4}. Now, how many choices do we have for digit 1?
        Obviously, any integer in the range [`1,\ldots,[$R]`], or [$R]
        choices. Once the first digit has been chosen, we have one less
        choice for the second digit, in other words [$R-1]. The size of
        the set [`A`] is the product of these two numbers,
        i.e. [_______________]{"([$R]-1)*[$R]"}

    4.  Putting this all together we get that the probability of [`A`] is

    [`P(A)=`] [_______]{"$R*($R-1)"} / [_________]{"$R^4"} = [___________________________]{"$R*($R-1)/($R^4)"}



## Part 1

### (70) Mistake Group Digits of size 70




### (39) Mistake Group ['R.1'] of size 39
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4^4	|10^4	|[('R.1', 4.0, u'4', u'4')]	|
|1	|7^4	|2^4	|[('R.1', 4.0, u'4', u'4')]	|
|2	|4^4	|9^4	|[('R.1', 4.0, u'4', u'4')]	|
|3	|4^4	|13^4	|[('R.1', 4.0, u'4', u'4')]	|
|4	|9^4	|8^4	|[('R.1', 4.0, u'4', u'4')]	|
|5	|6^4	|3^4	|[('R.1', 4.0, u'4', u'4')]	|
|6	|5^4	|C(5,4)	|[('R.1', 4.0, u'4', u'4')]	|
|7	|5^4	|20*4	|[('R.1', 4.0, u'4', u'4')]	|
|8	|9^4	|10 ^ 4	|[('R.1', 4.0, u'4', u'4')]	|




### (10) Mistake Group ['R.0'] of size 10
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|5^4	|5^2	|[('R.0', 5.0, u'5', u'5')]	|
|1	|7^4	|7^2	|[('R.0', 7.0, u'7', u'7')]	|
|2	|5^4	|5!	|[('R.0', 5.0, u'5', u'5')]	|
|3	|9^4	|9^3	|[('R.0', 9.0, u'9', u'9')]	|
|4	|8^4	|(8)(7)	|[('R.0', 8.0, u'8', u'8')]	|
|5	|8^4	|8!	|[('R.0', 8.0, u'8', u'8')]	|
|6	|9^4	|9*8	|[('R.0', 9.0, u'9', u'9')]	|
|7	|8^4	|8*7	|[('R.0', 8.0, u'8', u'8')]	|
|8	|8^4	|C(8,2)	|[('R.0', 8.0, u'8', u'8')]	|




### (5) Mistake Group ['R.0', 'R.1'] of size 5
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|6^4	|C(6,4)	|[('R.0', 6.0, u'6', u'6'), ('R.1', 4.0, u'4', u'4')]	|
|1	|5^4	|5*4	|[('R.0', 5.0, u'5', u'5'), ('R.1', 4.0, u'4', u'4')]	|
|2	|9^4	|C(9,4)	|[('R.0', 9.0, u'9', u'9'), ('R.1', 4.0, u'4', u'4')]	|




### (5) Mistake Group Fraction of size 5




### (70) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:galu

	first_attempt
					2015-10-15 22:41:30
	part1_incorrect_attempt
					('0:00:00', u'4^5')
	part1_correct_attempt
					['0:00:50', u'5^4']

1 Student ID:kew017

	first_attempt
					2015-10-15 05:22:06
	part1_incorrect_attempt
					('0:00:00', u'6!/2!')
	part1_correct_attempt
					['0:01:34', u'6^4']

2 Student ID:ttimmons

	first_attempt
					2015-10-11 00:39:00
	part1_incorrect_attempt
					('0:00:00', u'4^9')
	part1_correct_attempt
					['0:00:45', u'9^4']

3 Student ID:abjara

	first_attempt
					2015-10-12 03:14:49
	part1_incorrect_attempt
					('0:00:00', u'4^7')
	part1_correct_attempt
					['0:01:33', u'7^4']

4 Student ID:jag028

	first_attempt
					2015-10-14 21:50:27
	part1_incorrect_attempt
					('0:00:00', u'4^5')
					('0:31:05', u'[5!/(4!(5-4)!)]')
					('0:38:49', u'([5!/(4!(5-4)!)])')
					('0:00:00', u'(4)^5')
					('0:00:00', u'(2)^5 + (2)^4')
					('0:17:04', u'2^3')
					('0:17:17', u'2^5')
					('0:17:22', u'2^6')
	part1_correct_attempt
					['1:04:40', u'5^4']

5 Student ID:dis003

	first_attempt
					2015-10-15 10:41:49
	part1_incorrect_attempt
					('0:00:00', u'4^6')
	part1_correct_attempt
					['0:00:26', u'6^4']

6 Student ID:kew060

	first_attempt
					2015-10-14 00:54:24
	part1_incorrect_attempt
					('0:00:00', u'2^8')
	part1_correct_attempt
					['0:01:36', u'8^4']

7 Student ID:glcohen

	first_attempt
					2015-10-13 04:09:06
	part1_incorrect_attempt
					('0:00:00', u'4^7')
	part1_correct_attempt
					['0:00:06', u'7^4']

8 Student ID:jjchung

	first_attempt
					2015-10-14 18:23:16
	part1_incorrect_attempt
					('0:00:00', u'4^6')
	part1_correct_attempt
					['0:00:35', u'6^4']

9 Student ID:ewbrenna

	first_attempt
					2015-10-12 19:23:22
	part1_incorrect_attempt
					('0:00:00', u'4^5')
	part1_correct_attempt
					['0:00:10', u'5^4']

10 Student ID:atorr

	first_attempt
					2015-10-11 00:47:00
	part1_incorrect_attempt
					('0:00:00', u'4^7')
					('0:00:23', u'2^7 * 2^6')
	part1_correct_attempt
					['0:00:48', u'7^4']

11 Student ID:ffhaddad

	first_attempt
					2015-10-10 05:36:41
	part1_incorrect_attempt
					('0:00:00', u'4^6')
	part1_correct_attempt
					['0:01:51', u'6^4']

12 Student ID:mitopete

	first_attempt
					2015-10-13 06:30:50
	part1_incorrect_attempt
					('0:00:00', u'4^7')
	part1_correct_attempt
					['0:00:23', u'7^4']

13 Student ID:krau

	first_attempt
					2015-10-13 18:18:25
	part1_incorrect_attempt
					('0:00:00', u'8!/4!')
	part1_correct_attempt
					['0:04:27', u'8^4']

14 Student ID:edescobe

	first_attempt
					2015-10-12 00:50:55
	part1_incorrect_attempt
					('0:00:00', u'4^7')
	part1_correct_attempt
					['0:00:12', u'7^4']

15 Student ID:vsosnovs

	first_attempt
					2015-10-12 01:42:09
	part1_incorrect_attempt
					('0:00:00', u'4^9')
					('0:00:42', u'4^8')
	part1_correct_attempt
					['0:05:27', u'8^4']

16 Student ID:k5law

	first_attempt
					2015-10-12 00:55:11
	part1_incorrect_attempt
					('0:00:00', u'4^9')
	part1_correct_attempt
					['0:00:34', u'9^4']

17 Student ID:nhn018

	first_attempt
					2015-10-15 19:03:00
	part1_incorrect_attempt
					('0:00:00', u'4^6')

18 Student ID:jic212

	first_attempt
					2015-10-11 22:16:19
	part1_incorrect_attempt
					('0:00:00', u'2^3')
	part1_correct_attempt
					['0:02:17', u'4^4']

19 Student ID:amquinte

	first_attempt
					2015-10-12 19:07:44
	part1_incorrect_attempt
					('0:00:00', u'2^10')
	part1_correct_attempt
					['0:15:09', u'9^4']

20 Student ID:jmiclat

	first_attempt
					2015-10-15 01:05:00
	part1_incorrect_attempt
					('0:00:00', u'4^7')
	part1_correct_attempt
					['0:00:16', u'7^4']

21 Student ID:syc078

	first_attempt
					2015-10-14 14:13:02
	part1_incorrect_attempt
					('0:00:00', u'8! / ( (6!) (2!) )')
					('0:00:52', u'2^2')
	part1_correct_attempt
					['9:44:46', u'8^4']

22 Student ID:haw081

	first_attempt
					2015-10-10 21:33:25
	part1_incorrect_attempt
					('0:00:00', u'4!')
	part1_correct_attempt
					['0:34:18', u'4^4']

23 Student ID:aportuga

	first_attempt
					2015-10-13 22:15:20
	part1_incorrect_attempt
					('0:00:00', u'2^7')
	part1_correct_attempt
					['0:02:12', u'7^4']

24 Student ID:jew037

	first_attempt
					2015-10-13 22:45:15
	part1_incorrect_attempt
					('0:00:00', u'4^9')
					('0:00:00', u'2^3')
					('0:00:34', u'9*8*7*6')
					('0:00:40', u'9*8*7*6*5')
					('0:00:00', u'4^9')
					('0:00:30', u'4*9')
	part1_correct_attempt
					['4:10:37', u'9^4']

25 Student ID:cfgutier

	first_attempt
					2015-10-15 02:04:45
	part1_incorrect_attempt
					('0:00:00', u'9*8*7*6')
	part1_correct_attempt
					['0:07:26', u'9^4']

26 Student ID:t1tran

	first_attempt
					2015-10-10 05:18:05
	part1_incorrect_attempt
					('0:00:00', u'4^6')
	part1_correct_attempt
					['0:00:43', u'6^4']

27 Student ID:jnatale

	first_attempt
					2015-10-15 03:05:10
	part1_incorrect_attempt
					('0:00:00', u'8*7*1*1')
	part1_correct_attempt
					['0:00:25', u'8^4']

28 Student ID:jblynch

	first_attempt
					2015-10-12 06:36:29
	part1_incorrect_attempt
					('0:00:00', u'4^8')
	part1_correct_attempt
					['0:00:58', u'8^4']

29 Student ID:smohiman

	first_attempt
					2015-10-11 16:42:53
	part1_incorrect_attempt
					('0:00:00', u'2^7')
	part1_correct_attempt
					['0:03:15', u'7^4']

30 Student ID:seleon

	first_attempt
					2015-10-14 04:01:28
	part1_incorrect_attempt
					('0:00:00', u'2^3')
					('0:00:07', u'4^6')
	part1_correct_attempt
					['0:00:44', u'6^4']

31 Student ID:c1sorian

	first_attempt
					2015-10-14 21:45:44
	part1_incorrect_attempt
					('0:00:00', u'4^8')
					('0:01:25', u'4^8')
					('0:03:31', u'8!/(4!4!)')
					('0:04:00', u'8!/(6!2!)')
					('0:00:00', u'8!/(4!4!)')
					('0:00:00', u'8!/(2!)')
	part1_correct_attempt
					['0:53:52', u'8^4']

32 Student ID:ralhadda

	first_attempt
					2015-10-15 17:08:35
	part1_incorrect_attempt
					('0:00:00', u'4^7')
	part1_correct_attempt
					['0:01:16', u'7^4']

33 Student ID:s6deng

	first_attempt
					2015-10-13 22:42:31
	part1_incorrect_attempt
					('0:00:00', u'2^5')
					('0:00:00', u'5*4*3*2')
	part1_correct_attempt
					['0:03:42', u'5^4']

34 Student ID:r2fisher

	first_attempt
					2015-10-14 22:29:50
	part1_incorrect_attempt
					('0:00:00', u'4^7')
	part1_correct_attempt
					['0:00:25', u'7^4']

35 Student ID:akhmelni

	first_attempt
					2015-10-15 21:56:41
	part1_incorrect_attempt
					('0:00:00', u'4^5')
	part1_correct_attempt
					['0:00:11', u'5^4']

36 Student ID:kalang

	first_attempt
					2015-10-11 23:24:40
	part1_incorrect_attempt
					('0:00:00', u'4^6')
	part1_correct_attempt
					['0:01:18', u'6^4']

37 Student ID:jcl084

	first_attempt
					2015-10-13 18:43:34
	part1_incorrect_attempt
					('0:00:00', u'2^7')
					('0:00:31', u'4^7')
	part1_correct_attempt
					['0:01:22', u'7^4']

38 Student ID:agarango

	first_attempt
					2015-10-15 07:24:05
	part1_incorrect_attempt
					('0:00:00', u'9*8*9*8')
					('0:03:40', u'2^9')
	part1_correct_attempt
					['0:06:12', u'9^4']

39 Student ID:ssamudra

	first_attempt
					2015-10-15 03:01:20
	part1_incorrect_attempt
					('0:00:00', u'6*5*4*3*2*1')
					('0:00:42', u'6*5*4*3')
	part1_correct_attempt
					['0:02:25', u'6^4']

40 Student ID:jhw015

	first_attempt
					2015-10-13 07:06:21
	part1_incorrect_attempt
					('0:00:00', u'4!')
	part1_correct_attempt
					['0:06:08', u'7^4']

41 Student ID:bbturner

	first_attempt
					2015-10-15 23:33:54
	part1_incorrect_attempt
					('0:00:00', u'4^8')
	part1_correct_attempt
					['0:00:10', u'8^4']

42 Student ID:alhung

	first_attempt
					2015-10-15 17:47:09
	part1_incorrect_attempt
					('0:00:00', u'(2^8)*(2^7)')
	part1_correct_attempt
					['0:03:21', u'8^4']

43 Student ID:achava

	first_attempt
					2015-10-12 03:32:53
	part1_incorrect_attempt
					('0:00:00', u'2! * 2!')
					('0:00:08', u'2^3')
					('0:00:00', u'4^4')
					('0:00:31', u'4*3*4*3')
					('0:00:00', u'4^4')
					('0:00:18', u'4*3*4*3')
	part1_correct_attempt
					['1 day, 3:32:44', u'8^4']

44 Student ID:tcn013

	first_attempt
					2015-10-14 02:51:12
	part1_incorrect_attempt
					('0:00:00', u'2^3')
	part1_correct_attempt
					['0:00:33', u'4^4']

45 Student ID:tstevens

	first_attempt
					2015-10-10 10:23:24
	part1_incorrect_attempt
					('0:00:00', u'4^5')
	part1_correct_attempt
					['0:00:07', u'5^4']

46 Student ID:tcuddy

	first_attempt
					2015-10-10 18:19:49
	part1_incorrect_attempt
					('0:00:00', u'4^5')
	part1_correct_attempt
					['0:01:07', u'5^4']

47 Student ID:sippolit

	first_attempt
					2015-10-12 02:31:13
	part1_incorrect_attempt
					('0:00:00', u'2^7')
					('0:06:04', u'2^3')
	part1_correct_attempt
					['0:07:42', u'7^4']

48 Student ID:starinia

	first_attempt
					2015-10-13 05:12:51
	part1_incorrect_attempt
					('0:00:00', u'4^5')
	part1_correct_attempt
					['0:07:48', u'5 * 5 * 5 * 5']

49 Student ID:c1wei

	first_attempt
					2015-10-09 19:37:49
	part1_incorrect_attempt
					('0:00:00', u'2^3')
	part1_correct_attempt
					['0:01:59', u'7^4']

50 Student ID:chc286

	first_attempt
					2015-10-11 21:50:49
	part1_incorrect_attempt
					('0:00:00', u'2^5')
	part1_correct_attempt
					['0:01:23', u'5^4']

51 Student ID:zhw110

	first_attempt
					2015-10-09 03:59:58
	part1_incorrect_attempt
					('0:00:00', u'9*9*8*8')
	part1_correct_attempt
					['0:00:52', u'9*9*9*9']

52 Student ID:jnn015

	first_attempt
					2015-10-11 02:25:41
	part1_incorrect_attempt
					('0:00:00', u'5!/1!')
	part1_correct_attempt
					['0:00:30', u'5^4']

53 Student ID:acs008

	first_attempt
					2015-10-09 16:22:21
	part1_incorrect_attempt
					('0:00:00', u'4^7')
	part1_correct_attempt
					['0:00:15', u'7^4']

54 Student ID:m4bui

	first_attempt
					2015-10-15 18:49:18
	part1_incorrect_attempt
					('0:00:00', u'4^8')
	part1_correct_attempt
					['2:48:00', u'8^4']

55 Student ID:fichoi

	first_attempt
					2015-10-12 04:57:46
	part1_incorrect_attempt
					('0:00:00', u'4^6')
	part1_correct_attempt
					['0:03:15', u'6^4']

56 Student ID:wcwhite

	first_attempt
					2015-10-14 01:21:43
	part1_incorrect_attempt
					('0:00:00', u'2^3')
	part1_correct_attempt
					['0:01:02', u'9^4']

57 Student ID:cstringh

	first_attempt
					2015-10-12 18:59:45
	part1_incorrect_attempt
					('0:00:00', u'4^5')
	part1_correct_attempt
					['0:00:28', u'5^4']

58 Student ID:aordookh

	first_attempt
					2015-10-15 14:06:10
	part1_incorrect_attempt
					('0:00:00', u'4^4')
	part1_correct_attempt
					['0:00:12', u'7^4']

59 Student ID:yjshin

	first_attempt
					2015-10-14 07:58:42
	part1_incorrect_attempt
					('0:00:00', u'2^7')
	part1_correct_attempt
					['0:02:03', u'7^4']

60 Student ID:rohan

	first_attempt
					2015-10-15 22:57:06
	part1_incorrect_attempt
					('0:00:00', u'4^9')
	part1_correct_attempt
					['0:04:06', u'9^4']

61 Student ID:m4salaza

	first_attempt
					2015-10-15 23:01:44
	part1_incorrect_attempt
					('0:00:00', u'4^6')

62 Student ID:tak068

	first_attempt
					2015-10-14 04:43:49
	part1_incorrect_attempt
					('0:00:00', u'4^4')
	part1_correct_attempt
					['0:00:07', u'9^4']

63 Student ID:k4ma

	first_attempt
					2015-10-15 02:20:09
	part1_incorrect_attempt
					('0:00:00', u'4^2')
	part1_correct_attempt
					['0:01:40', u'4^4']

64 Student ID:dac064

	first_attempt
					2015-10-15 17:50:21
	part1_incorrect_attempt
					('0:00:00', u'9 * 8 * 7 * 6')
					('0:00:13', u'10 * 9 * 8 * 7')
	part1_correct_attempt
					['0:01:42', u'9 ^ 4']

65 Student ID:ajvanega

	first_attempt
					2015-10-14 17:34:27
	part1_incorrect_attempt
					('0:00:00', u'4^5')
	part1_correct_attempt
					['0:00:11', u'5^4']

66 Student ID:jguanzho

	first_attempt
					2015-10-09 19:45:28
	part1_incorrect_attempt
					('0:00:00', u'4**8')
	part1_correct_attempt
					['0:00:26', u'8**4']

67 Student ID:aurodrig

	first_attempt
					2015-10-15 00:29:51
	part1_incorrect_attempt
					('0:00:00', u'4^6')
					('0:00:24', u'2^6')
	part1_correct_attempt
					['0:07:28', u'6^4']

68 Student ID:ggaddi

	first_attempt
					2015-10-10 05:28:06
	part1_incorrect_attempt
					('0:00:00', u'2^3')
	part1_correct_attempt
					['0:01:38', u'9^4']

69 Student ID:mtrafeca

	first_attempt
					2015-10-10 19:26:12
	part1_incorrect_attempt
					('0:00:00', u'4^7')
	part1_correct_attempt
					['0:00:17', u'7^4']












## Part 2

### (21) Mistake Group Digits of size 21




### (0) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|












## Part 3

### (20) Mistake Group Digits of size 20




### (8) Mistake Group ['R.0.0'] of size 8
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(5-1)*5	|(5!/(2!3!))	|[('R.0.0', 5.0, u'5', u'5')]	|
|1	|(7-1)*7	|7!/(3!*4!)	|[('R.0.0', 7.0, u'7', u'7')]	|
|2	|(7-1)*7	|7^4 + 6^4	|[('R.0.0', 7.0, u'7', u'7')]	|
|3	|(7-1)*7	|7^4 * 6^4	|[('R.0.0', 7.0, u'7', u'7')]	|
|4	|(9-1)*9	|9!*8!	|[('R.0.0', 9.0, u'9', u'9')]	|
|5	|(8-1)*8	|8! / ( (6!) (2!) )	|[('R.0.0', 8.0, u'8', u'8')]	|
|6	|(7-1)*7	|7^2 * 6^2	|[('R.0.0', 7.0, u'7', u'7')]	|
|7	|(8-1)*8	|8!7!	|[('R.0.0', 8.0, u'8', u'8')]	|




### (2) Mistake Group ['R.0'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(5-1)*5	|4*3	|[('R.0', 4.0, u'5-1', u'4')]	|
|1	|(9-1)*9	|8*7	|[('R.0', 8.0, u'9-1', u'8')]	|




### (1) Mistake Group ['R.0.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(8-1)*8	|C(8,1)+C(7,1)	|[('R.0.1', 1.0, u'1', u'1')]	|




### (11) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:alhung

	first_attempt
					2015-10-15 17:50:30
	part3_incorrect_attempt
					('0:00:00', u'C(8,2)')
	part3_correct_attempt
					['0:05:45', u'8*7']

1 Student ID:haliew

	first_attempt
					2015-10-13 17:07:54
	part3_incorrect_attempt
					('0:00:00', u'P(8,4)')
					('0:00:20', u'C(8,4)')
	part3_correct_attempt
					['0:01:05', u'8*7']

2 Student ID:dlt009

	first_attempt
					2015-10-14 00:08:41
	part3_incorrect_attempt
					('0:00:00', u'9*7')
	part3_correct_attempt
					['0:00:13', u'9*8']

3 Student ID:r1gu

	first_attempt
					2015-10-15 10:53:18
	part3_incorrect_attempt
					('0:00:33', u'4^3')
	part3_correct_attempt
					['0:00:39', u'4*3']

4 Student ID:aurodrig

	first_attempt
					2015-10-15 00:37:19
	part3_incorrect_attempt
					('0:02:29', u'4 - 1 * 4')
					('0:02:36', u'6 - 1 * 6')
					('0:02:57', u'6 - 1 * 5')
					('0:03:59', u'6 - 1 * 6')
	part3_correct_attempt
					['0:04:20', u'30']

5 Student ID:dis003

	first_attempt
					2015-10-15 10:42:15
	part3_incorrect_attempt
					('-1 day, 23:59:34', u'6!')
	part3_correct_attempt
					['0:00:00', u'6*5']

6 Student ID:hkhodada

	first_attempt
					2015-10-10 15:48:48
	part3_incorrect_attempt
					('0:02:00', u'2^4')
					('0:03:11', u'4^2')
					('0:04:01', u'12^2')
	part3_correct_attempt
					['0:05:05', u'12']

7 Student ID:yil035

	first_attempt
					2015-10-13 22:42:03
	part3_incorrect_attempt
					('0:00:00', u'6*5*4*3')
	part3_correct_attempt
					['0:01:02', u'6*5']

8 Student ID:mtrafeca

	first_attempt
					2015-10-10 19:26:29
	part3_incorrect_attempt
					('0:03:56', u'7!')
					('0:06:06', u'7!/3!*4!')
	part3_correct_attempt
					['0:09:02', u'42']

9 Student ID:whcombs

	first_attempt
					2015-10-12 23:14:06
	part3_incorrect_attempt
					('0:00:00', u'4!')
	part3_correct_attempt
					['0:01:16', u'12']

10 Student ID:vsosnovs

	first_attempt
					2015-10-12 01:47:36
	part3_incorrect_attempt
					('0:01:24', u'3^7')
					('0:01:30', u'3^8')
	part3_correct_attempt
					['0:02:50', u'8*7']












## Part 4

### (12) Mistake Group redirect of size 12




### (9) Mistake Group Digits of size 9




### (2) Mistake Group ['R.1'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|8*(8-1)	|C(8,1)+C(7,1)	|[('R.1', 7.0, u'8-1', u'C(7,1)')]	|
|1	|4*(4-1)	|4*3*4*3	|[('R.1', 3.0, u'4-1', u'3')]	|




### (4) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:ytc012

	first_attempt
					2015-10-14 21:43:37
	part1_correct_attempt
					['0:00:00', u'7^4']
	part2_correct_attempt
					['0:03:03', u'4']
	part3_correct_attempt
					['0:05:27', u'42']
	part4_incorrect_attempt
					('0:06:48', u'7^4')
	part4_correct_attempt
					['0:07:13', u'42']

1 Student ID:msaguiar

	first_attempt
					2015-10-12 03:08:00
	part1_correct_attempt
					['0:00:00', u'7^4']
	part2_correct_attempt
					['0:14:23', u'4']
	part3_correct_attempt
					['0:14:23', u'7*6']
	part4_incorrect_attempt
					('0:14:23', u'7^4')
	part4_correct_attempt
					['0:15:13', u'7*6']

2 Student ID:lalacson

	first_attempt
					2015-10-11 15:08:30
	part1_correct_attempt
					['0:00:00', u'5^4']
	part2_correct_attempt
					['0:01:41', u'4']
	part3_correct_attempt
					['0:01:41', u'5!/3!']
	part4_incorrect_attempt
					('0:02:12', u'(5!3!)')
	part4_correct_attempt
					['0:03:42', u'(5!/3!)']

3 Student ID:yhhan

	first_attempt
					2015-10-15 04:43:40
	part1_correct_attempt
					['0:00:00', u'9^4']
	part2_correct_attempt
					['0:01:38', u'4']
	part3_correct_attempt
					['0:01:38', u'9*8']
	part4_incorrect_attempt
					('0:02:06', u'9*7')
	part4_correct_attempt
					['0:02:14', u'9*8']












## Part 5

### (22) Mistake Group Digits of size 22




### (16) Mistake Group redirect of size 16




### (3) Mistake Group ['R.0'] of size 3
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|8^4	|8^7	|[('R.0', 8.0, u'8', u'8')]	|
|1	|7^4	|7*6	|[('R.0', 7.0, u'7', u'7')]	|
|2	|5^4	|5!	|[('R.0', 5.0, u'5', u'5')]	|




### (3) Mistake Group ['R.1'] of size 3
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|9^4	|8^4	|[('R.1', 4.0, u'4', u'4')]	|
|1	|7^4	|2^4	|[('R.1', 4.0, u'4', u'4')]	|




### (0) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|












## Part 6

### (24) Mistake Group redirect of size 24




### (15) Mistake Group ['R.0'] of size 15
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4*(4-1)/(4^4)	|12/10000	|[('R.0', 12.0, u'4*(4-1)', u'12')]	|
|1	|8*(8-1)/(8^4)	|56/4**8	|[('R.0', 56.0, u'8*(8-1)', u'56')]	|
|2	|8*(8-1)/(8^4)	|8*7/(8^7)	|[('R.0', 56.0, u'8*(8-1)', u'8*7')]	|
|3	|6*(6-1)/(6^4)	|30/4096	|[('R.0', 30.0, u'6*(6-1)', u'30')]	|
|4	|9*(9-1)/(9^4)	|[9*8]/[4^9]	|[('R.0', 72.0, u'9*(9-1)', u'9*8')]	|
|5	|6*(6-1)/(6^4)	|30/2^6	|[('R.0', 30.0, u'6*(6-1)', u'30')]	|
|6	|4*(4-1)/(4^4)	|12/16	|[('R.0', 12.0, u'4*(4-1)', u'12')]	|
|7	|8*(8-1)/(8^4)	|(8*7)/(4^8)	|[('R.0', 56.0, u'8*(8-1)', u'8*7')]	|
|8	|5*(5-1)/(5^4)	|5*4/4^5	|[('R.0', 20.0, u'5*(5-1)', u'5*4')]	|
|9	|5*(5-1)/(5^4)	|5*4/5!	|[('R.0', 20.0, u'5*(5-1)', u'5*4')]	|
|10	|4*(4-1)/(4^4)	|12/32	|[('R.0', 12.0, u'4*(4-1)', u'12')]	|
|11	|4*(4-1)/(4^4)	|12/64	|[('R.0', 12.0, u'4*(4-1)', u'12')]	|
|12	|7*(7-1)/(7^4)	|(7 * 6)/4	|[('R.0', 42.0, u'7*(7-1)', u'7 * 6')]	|
|13	|7*(7-1)/(7^4)	|(7*6)/(4^7)	|[('R.0', 42.0, u'7*(7-1)', u'7*6')]	|




### (8) Mistake Group ['R.1'] of size 8
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|5*(5-1)/(5^4)	|(5!3!)/5^4	|[('R.1', 625.0, u'5^4', u'5^4')]	|
|1	|4*(4-1)/(4^4)	|24/256	|[('R.1', 256.0, u'4^4', u'256')]	|
|2	|8*(8-1)/(8^4)	|P(8,4)/8^4	|[('R.1', 4096.0, u'8^4', u'8^4')]	|
|3	|8*(8-1)/(8^4)	|C(8,4)/8^4	|[('R.1', 4096.0, u'8^4', u'8^4')]	|
|4	|5*(5-1)/(5^4)	|4/ (5^4)	|[('R.1', 625.0, u'5^4', u'5^4')]	|
|5	|9*(9-1)/(9^4)	|(9*7)/ (9^4)	|[('R.1', 6561.0, u'9^4', u'9^4')]	|
|6	|6*(6-1)/(6^4)	|120/6^4	|[('R.1', 1296.0, u'6^4', u'6^4')]	|
|7	|8*(8-1)/(8^4)	|(8*7!)/(8^4)	|[('R.1', 4096.0, u'8^4', u'8^4')]	|




### (4) Mistake Group Digits of size 4




### (1) Mistake Group ['R.1.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|8*(8-1)/(8^4)	|(8!7!)/(2^4)	|[('R.1.1', 4.0, u'4', u'4')]	|




### (13) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:daw023

	first_attempt
					2015-10-14 22:32:08
	part1_correct_attempt
					['0:00:00', u'8^4']
	part2_correct_attempt
					['0:00:00', u'4']
	part3_correct_attempt
					['0:00:00', u'8*7']
	part6_incorrect_attempt
					('0:00:00', u'8^4/(8*7)')
	part6_correct_attempt
					['0:00:16', u'(8*7)/8^4']

1 Student ID:hachrist

	first_attempt
					2015-10-14 04:07:55
	part1_correct_attempt
					['0:00:00', u'4^4']
	part2_correct_attempt
					['0:00:00', u'4']
	part3_correct_attempt
					['0:00:00', u'4 * 3']
	part6_incorrect_attempt
					('0:00:00', u'0.46875')
	part6_correct_attempt
					['0:00:54', u'0.046875']

2 Student ID:yjshin

	first_attempt
					2015-10-14 08:00:45
	part1_correct_attempt
					['0:00:00', u'7^4']
	part2_correct_attempt
					['-1 day, 23:57:57', u'4']
	part3_correct_attempt
					['-1 day, 23:57:57', u'42']
	part6_incorrect_attempt
					('0:00:00', u'0.017')
	part6_correct_attempt
					['0:00:50', u'42/2401']

3 Student ID:vasharma

	first_attempt
					2015-10-10 02:09:31
	part1_correct_attempt
					['0:00:00', u'4^4']
	part2_correct_attempt
					['0:03:27', u'4']
	part3_correct_attempt
					['0:04:37', u'12']
	part6_incorrect_attempt
					('0:04:48', u'1/3')
	part6_correct_attempt
					['0:06:05', u'12/(4^4)']

4 Student ID:jew037

	first_attempt
					2015-10-14 02:55:52
	part1_correct_attempt
					['0:00:00', u'9^4']
	part2_correct_attempt
					['0:00:42', u'4']
	part3_correct_attempt
					['0:01:08', u'9*8']
	part6_incorrect_attempt
					('0:01:33', u'0.011')
	part6_correct_attempt
					['0:01:40', u'0.010974']

5 Student ID:anl114

	first_attempt
					2015-10-15 07:08:49
	part1_correct_attempt
					['0:00:00', u'6^4']
	part2_correct_attempt
					['0:00:00', u'4']
	part3_correct_attempt
					['0:00:00', u'30']
	part6_incorrect_attempt
					('0:00:00', u'0.0231')
	part6_correct_attempt
					['0:00:23', u'0.023148']

6 Student ID:msaguiar

	first_attempt
					2015-10-12 03:08:00
	part1_correct_attempt
					['0:00:00', u'7^4']
	part2_correct_attempt
					['0:14:23', u'4']
	part3_correct_attempt
					['0:14:23', u'7*6']
	part6_incorrect_attempt
					('0:14:23', u'(7^4)/(7*6)')
	part6_correct_attempt
					['0:15:13', u'(7*6)/(7^4)']

7 Student ID:bpandayk

	first_attempt
					2015-10-15 21:47:04
	part1_correct_attempt
					['0:00:00', u'9^4']
	part2_correct_attempt
					['0:00:05', u'4']
	part3_correct_attempt
					['0:00:20', u'8*9']
	part6_incorrect_attempt
					('0:01:26', u'9*(9-1)')
	part6_correct_attempt
					['0:02:06', u'8*9/(9^4)']

8 Student ID:lcardoso

	first_attempt
					2015-10-12 22:56:03
	part1_correct_attempt
					['0:00:00', u'4*4*4*4']
	part2_correct_attempt
					['0:00:00', u'4']
	part3_correct_attempt
					['0:00:00', u'4*3*1*1']
	part6_incorrect_attempt
					('0:00:00', u'4*3*1*1 / 4*4*4*4')
	part6_correct_attempt
					['0:00:14', u'(4*3*1*1) / (4*4*4*4)']

9 Student ID:mcatozzi

	first_attempt
					2015-10-13 22:46:47
	part1_correct_attempt
					['0:00:00', u'7^4']
	part2_correct_attempt
					['0:00:41', u'4']
	part3_correct_attempt
					['0:04:52', u'42']
	part6_incorrect_attempt
					('0:05:27', u'.017')
	part6_correct_attempt
					['0:05:38', u'.0174927114']

10 Student ID:yil035

	first_attempt
					2015-10-13 22:42:03
	part1_correct_attempt
					['0:00:00', u'6^4']
	part2_correct_attempt
					['0:00:00', u'4']
	part3_correct_attempt
					['0:01:02', u'6*5']
	part6_incorrect_attempt
					('0:01:02', u'0.023')
	part6_correct_attempt
					['0:01:29', u'30/(6^4)']

11 Student ID:ytc012

	first_attempt
					2015-10-14 21:43:37
	part1_correct_attempt
					['0:00:00', u'7^4']
	part2_correct_attempt
					['0:03:03', u'4']
	part3_correct_attempt
					['0:05:27', u'42']
	part6_incorrect_attempt
					('0:06:48', u'(7^4)/42')
	part6_correct_attempt
					['0:07:13', u'42/7^4']

12 Student ID:jnn015

	first_attempt
					2015-10-11 02:26:11
	part1_correct_attempt
					['0:00:00', u'5^4']
	part2_correct_attempt
					['1:04:58', u'4']
	part3_correct_attempt
					['1:04:58', u'20']
	part6_incorrect_attempt
					('1:05:08', u'.30')
	part6_correct_attempt
					['1:05:51', u'4/125']












