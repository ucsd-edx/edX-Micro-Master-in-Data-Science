#Problem 9

    $R1=random(8,15,1);
    $R2=random(2,$R1-2,1);
    $F=fact($R1)/(fact($R2)*fact($R1-$R2));

    #### Choosing candies ####
    This is a challenge problem, you have until wed to solve it.
    It is recommended that you try, this will help you understand what we
    do in class.
    ---
    You walk into a candy store and notice that there are five types of candy. Your mother allows you to pick exactly three pieces of candy, of whichever type(s)
    you want. How many ways are there to do this?

    You can represent the outcome by 5-tuple [`(n_1, n_2, \ldots, n_5)`] in
    which [`n_i`] is the number of pieces of the [`i`] h type of candy. How
    many such tuples are there, subject to [`n_1 + n_2 + \cdots + n_5 = 3`]
    To answer the question, we'll represent each tuple in a different
    format, as a sequence of length 7 containing three stars and four
    bars. For instance, the sequence [`|\,**\,|\,|\,|\,*`] denotes [`(0,2,0,0,1)`] (two candies of type 2 and one candy of type 5): the
    number of candies of type [`i`] is the number of stars between the [`(i-1)`] t and [`i`] h bars.

    So we have rephrased the question thus: how many sequences are there
    with four bars and three stars? Well, this is a sequence of size 7,
    and we must pick three of the seven positions at which to place
    stars. The number of such choices is [`{7 \choose 3} = 35`]

    *PROBLEM:*
    Suppose balls come in [$R1] colors and that you are to pick out [$R2] balls. How many different color combinations are possible?

    By the analogy explained above, how many bars do you need[______]{($R1-1)}
    By the analogy explained above, how many stars do you need[______]{($R2)}

    o The number of color combinations is [______]{"(($R2+$R1-1)!)/(($R2)!*($R1-1)!)"}


## Part 1

### (532) Mistake Group Digits of size 532




### (1) Mistake Group Wrong_Sign of size 1




### (1) Mistake Group Fraction of size 1




### (28) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:b3hwang

	first_attempt
					2015-10-15 21:14:41
	part1_incorrect_attempt
					('0:00:00', u'C(8,6)')
					('1:27:37', u'C(5,3)')
	part1_correct_attempt
					['1:32:57', u'7']

1 Student ID:ppanourg

	first_attempt
					2015-10-14 23:27:25
	part1_incorrect_attempt
					('0:00:00', u'(42*41*40)/6')
	part1_correct_attempt
					['0:18:10', u'13']

2 Student ID:ewbrenna

	first_attempt
					2015-10-12 19:46:01
	part1_incorrect_attempt
					('0:00:00', u'C(14,12)')
	part1_correct_attempt
					['0:00:59', u'13']

3 Student ID:spw006

	first_attempt
					2015-10-13 21:11:27
	part1_incorrect_attempt
					('0:00:00', u'11!/(7!4!)')
	part1_correct_attempt
					['0:03:23', u'10']

4 Student ID:sachadal

	first_attempt
					2015-10-09 18:22:36
	part1_incorrect_attempt
					('0:00:00', u'C(12,9)')
	part1_correct_attempt
					['5 days, 20:43:56', u'11']

5 Student ID:e9brown

	first_attempt
					2015-10-14 08:33:06
	part1_incorrect_attempt
					('0:00:00', u'8^5')
					('0:00:07', u'8!')
	part1_correct_attempt
					['0:02:53', u'7']

6 Student ID:t2li

	first_attempt
					2015-10-14 05:28:22
	part1_incorrect_attempt
					('0:00:00', u'C(8,2)')
	part1_correct_attempt
					['0:05:27', u'7']

7 Student ID:alhung

	first_attempt
					2015-10-15 19:26:32
	part1_incorrect_attempt
					('0:00:00', u'(7-1)')
	part1_correct_attempt
					['0:02:27', u'10']

8 Student ID:jic212

	first_attempt
					2015-10-11 23:06:39
	part1_incorrect_attempt
					('0:00:00', u'(15!)/((13!)(2!))')
	part1_correct_attempt
					['0:03:00', u'14']

9 Student ID:gsrandha

	first_attempt
					2015-10-12 06:53:22
	part1_incorrect_attempt
					('0:00:00', u'13!/((4!)(9!))')
					('0:00:16', u'13!/((9!))')
	part1_correct_attempt
					['0:01:05', u'12']

10 Student ID:jhc010

	first_attempt
					2015-10-15 15:52:37
	part1_incorrect_attempt
					('0:00:00', u'C(14,7)')
	part1_correct_attempt
					['0:00:31', u'13']

11 Student ID:jeqin

	first_attempt
					2015-10-15 12:14:14
	part1_incorrect_attempt
					('0:00:00', u'8!(4!4!)')
					('0:01:26', u'10!(6!4!)')
	part1_correct_attempt
					['0:01:59', u'7']

12 Student ID:jhw015

	first_attempt
					2015-10-15 02:27:30
	part1_incorrect_attempt
					('0:00:00', u'C(15,13)')
					('0:02:00', u'C(7,4)')
	part1_correct_attempt
					['1:48:58', u'14']

13 Student ID:tstevens

	first_attempt
					2015-10-12 10:12:16
	part1_incorrect_attempt
					('0:00:00', u'9*8*7')
					('0:00:14', u'9*9*9')
	part1_correct_attempt
					['0:02:26', u'8']

14 Student ID:krkelkar

	first_attempt
					2015-10-14 02:21:53
	part1_incorrect_attempt
					('0:00:00', u'10-1')
	part1_correct_attempt
					['0:01:25', u'11-1']

15 Student ID:hah008

	first_attempt
					2015-10-15 08:50:26
	part1_incorrect_attempt
					('0:00:00', u'C(16, 9)')
					('0:00:06', u'C(16, 7)')
	part1_correct_attempt
					['0:02:11', u'8']

16 Student ID:djk006

	first_attempt
					2015-10-10 21:23:17
	part1_incorrect_attempt
					('0:00:00', u'(9*8*7*6*5)/5!')
	part1_correct_attempt
					['0:02:31', u'8']

17 Student ID:hmnaing

	first_attempt
					2015-10-13 00:34:04
	part1_incorrect_attempt
					('0:00:00', u'3-1')
	part1_correct_attempt
					['14:42:31', u'13']

18 Student ID:anvan

	first_attempt
					2015-10-15 00:12:25
	part1_incorrect_attempt
					('0:00:00', u'8*7*6*5*4')
	part1_correct_attempt
					['4:41:27', u'7']

19 Student ID:hmshah

	first_attempt
					2015-10-14 02:09:34
	part1_incorrect_attempt
					('0:00:00', u'C(12,2)')
	part1_correct_attempt
					['1 day, 6:30:44', u'11']

20 Student ID:flhernan

	first_attempt
					2015-10-14 22:42:42
	part1_incorrect_attempt
					('0:00:00', u'C(4,3)')
					('0:04:22', u'C(20,7)')
					('0:04:31', u'C(20,14)')
	part1_correct_attempt
					['0:06:06', u'13']

21 Student ID:arc013

	first_attempt
					2015-10-13 03:02:50
	part1_incorrect_attempt
					('0:00:00', u'C(14,4)')
					('0:02:19', u'C(17,14)')
	part1_correct_attempt
					['0:03:58', u'13']

22 Student ID:aurodrig

	first_attempt
					2015-10-15 18:43:23
	part1_incorrect_attempt
					('0:00:00', u'14!/9!*(14-9)!')
					('0:00:12', u'14!/(9!(14-9)!)')
					('0:00:29', u'14!/9!(14-9)!')
	part1_correct_attempt
					['0:04:22', u'13']

23 Student ID:kquong

	first_attempt
					2015-10-10 23:54:06
	part1_incorrect_attempt
					('0:00:00', u'10!/(6!*(10-6)!)')
	part1_correct_attempt
					['3:59:38', u'9']

24 Student ID:dcastlem

	first_attempt
					2015-10-15 03:47:28
	part1_incorrect_attempt
					('0:00:00', u'15!/((6!)(9!))')
					('0:00:24', u'15!/((6!)(9!))')
	part1_correct_attempt
					['0:06:10', u'14']

25 Student ID:tak068

	first_attempt
					2015-10-14 05:46:27
	part1_incorrect_attempt
					('0:00:00', u'15!/8!')
					('0:00:08', u'7!')
	part1_correct_attempt
					['0:08:42', u'14']

26 Student ID:yypan

	first_attempt
					2015-10-12 20:26:57
	part1_incorrect_attempt
					('0:00:00', u'C(9,2)')
	part1_correct_attempt
					['0:01:54', u'8']

27 Student ID:wcwhite

	first_attempt
					2015-10-14 01:42:59
	part1_incorrect_attempt
					('0:00:00', u'35-7')
					('0:01:17', u'14!/7!(7!)')
					('0:01:26', u'14!/(7!(7!))')
					('0:01:43', u'14!/(7!(14-7)!)')
					('0:02:05', u'7!/(3!(7-3)!)')
					('0:02:18', u'14!')
					('0:02:23', u'7!')
					('0:02:31', u'7^7')
					('0:02:37', u'7^17')
					('0:05:52', u'14!/(14-7)!')
					('0:06:26', u'7!')
					('0:14:51', u'14!/(7!(14-7)!)')
					('0:24:54', u'13*7')
					('0:25:04', u'6*7')
					('0:25:08', u'6*14')
					('0:25:14', u'13*14')












## Part 2

### (85) Mistake Group Digits of size 85




### (3) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:tak068

	first_attempt
					2015-10-14 05:55:09
	part2_incorrect_attempt
					('-1 day, 23:51:18', u'7!')
	part2_correct_attempt
					['-1 day, 23:59:49', u'7']

1 Student ID:alhung

	first_attempt
					2015-10-15 19:28:59
	part2_incorrect_attempt
					('-1 day, 23:57:33', u'(11+6)')
	part2_correct_attempt
					['0:00:10', u'7']

2 Student ID:dcastlem

	first_attempt
					2015-10-15 03:53:38
	part2_incorrect_attempt
					('-1 day, 23:54:14', u'15!/((6!)(9!))')
	part2_correct_attempt
					['-1 day, 23:57:09', u'21!/((6!)(15!))']












## Part 3

### (103) Mistake Group Digits of size 103




### (85) Mistake Group redirect of size 85




### (22) Mistake Group Fraction of size 22




### (13) Mistake Group ['R.1'] of size 13
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(4+11-1,11-1)	|C((10 + 4 - 1), (10))	|[('R.1', 10.0, u'11-1', u'10')]	|
|1	|C(4+11-1,11-1)	|C(10 + 4 - 1, 10)	|[('R.1', 10.0, u'11-1', u'10')]	|
|2	|C(4+11-1,11-1)	|C(10 + 4 - 1,10)	|[('R.1', 10.0, u'11-1', u'10')]	|
|3	|C(4+11-1,11-1)	|C(13,10)	|[('R.1', 10.0, u'11-1', u'10')]	|
|4	|C(13+15-1,15-1)	|C(15,14)	|[('R.1', 14.0, u'15-1', u'14')]	|
|5	|C(6+8-1,8-1)	|6**7	|[('R.1', 7.0, u'8-1', u'7')]	|
|6	|C(2+8-1,8-1)	|(8*7)	|[('R.1', 7.0, u'8-1', u'7')]	|
|7	|C(4+14-1,14-1)	|C(16,13)	|[('R.1', 13.0, u'14-1', u'13')]	|
|8	|C(12+14-1,14-1)	|12*13	|[('R.1', 13.0, u'14-1', u'13')]	|
|9	|C(12+14-1,14-1)	|14*13	|[('R.1', 13.0, u'14-1', u'13')]	|
|10	|C(12+14-1,14-1)	|12^13	|[('R.1', 13.0, u'14-1', u'13')]	|
|11	|C(7+9-1,9-1)	|C(4+9-1, 9-1)	|[('R.1', 8.0, u'9-1', u'9-1')]	|




### (9) Mistake Group ['R.0.0'] of size 9
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(12+15-1,15-1)	|27!/[(27-7)!7!]	|[('R.0.0', 27.0, u'12+15', u'27')]	|
|1	|C(12+15-1,15-1)	|27!/[(27-7)!]	|[('R.0.0', 27.0, u'12+15', u'27')]	|
|2	|C(12+15-1,15-1)	|27!/[(27-12)!]	|[('R.0.0', 27.0, u'12+15', u'27')]	|
|3	|C(12+15-1,15-1)	|27!/[12!(27-12)!]	|[('R.0.0', 27.0, u'12+15', u'27')]	|
|4	|C(5+8-1,8-1)	|13!/(5!(13-5)!)	|[('R.0.0', 13.0, u'5+8', u'13')]	|
|5	|C(4+11-1,11-1)	|15!/((15-4)!4!)	|[('R.0.0', 15.0, u'4+11', u'15')]	|
|6	|C(3+10-1,10-1)	|13!/(3!*4!)	|[('R.0.0', 13.0, u'3+10', u'13')]	|
|7	|C(7+13-1,13-1)	|20!/(7!3!)	|[('R.0.0', 20.0, u'7+13', u'20')]	|
|8	|C(2+10-1,10-1)	|12!/(2!8!)	|[('R.0.0', 12.0, u'2+10', u'12')]	|




### (9) Mistake Group ['R.0'] of size 9
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(9+12-1,12-1)	|C(12+8,8)	|[('R.0', 20.0, u'9+12-1', u'12+8')]	|
|1	|C(9+12-1,12-1)	|C(12+8,12)	|[('R.0', 20.0, u'9+12-1', u'12+8')]	|
|2	|C(5+9-1,9-1)	|C(9+5-1,5-1)	|[('R.0', 13.0, u'5+9-1', u'9+5-1')]	|
|3	|C(4+10-1,10-1)	|C(13,3)	|[('R.0', 13.0, u'4+10-1', u'13')]	|
|4	|C(7+9-1,9-1)	|C(7+9-1, 7-1)	|[('R.0', 15.0, u'7+9-1', u'7+9-1')]	|
|5	|C(5+11-1,11-1)	|C(15,4)	|[('R.0', 15.0, u'5+11-1', u'15')]	|
|6	|C(5+8-1,8-1)	|C(12,9)	|[('R.0', 12.0, u'5+8-1', u'12')]	|
|7	|C(9+14-1,14-1)	|C(22,14)	|[('R.0', 22.0, u'9+14-1', u'22')]	|
|8	|C(6+15-1,15-1)	|C(20,15)	|[('R.0', 20.0, u'6+15-1', u'20')]	|




### (2) Mistake Group ['R.1.1'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(11+13-1,13-1)	|12!/(11!(12-11)!)	|[('R.1.1', 1.0, u'1', u'(12-11)!')]	|
|1	|C(7+9-1,9-1)	|(8!)/(7!*(8-7)!)	|[('R.1.1', 1.0, u'1', u'(8-7)!')]	|




### (1) Mistake Group Wrong_Sign of size 1




### (117) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:phodgson

	first_attempt
					2015-10-13 02:15:46
	part1_correct_attempt
					['0:00:00', u'9']
	part2_correct_attempt
					['0:00:00', u'6']
	part3_incorrect_attempt
					('0:00:00', u'9!/(6!*3!)')
					('0:00:13', u'C(9,6)')
					('0:01:04', u'C(16,6)')
	part3_correct_attempt
					['0:01:20', u'C(15,6)']

1 Student ID:kbielawi

	first_attempt
					2015-10-11 23:35:55
	part1_correct_attempt
					['0:00:00', u'7']
	part2_correct_attempt
					['-1 day, 23:59:53', u'5']
	part3_incorrect_attempt
					('0:00:06', u'C(7,5)')
	part3_correct_attempt
					['0:00:37', u'C(12,5)']

2 Student ID:dcgriffi

	first_attempt
					2015-10-14 07:10:56
	part1_correct_attempt
					['0:00:00', u'11']
	part2_correct_attempt
					['0:00:00', u'9']
	part3_incorrect_attempt
					('0:00:00', u'11!/(2!*9!)')
	part3_correct_attempt
					['0:00:42', u'20!/(11!*9!)']

3 Student ID:nhn018

	first_attempt
					2015-10-15 19:43:44
	part1_correct_attempt
					['0:00:00', u'7']
	part2_correct_attempt
					['-1 day, 23:56:26', u'2']
	part3_incorrect_attempt
					('1:00:31', u'C(7,2)')

4 Student ID:dan029

	first_attempt
					2015-10-09 22:46:26
	part1_correct_attempt
					['0:00:00', u'12']
	part2_correct_attempt
					['0:00:00', u'9']
	part3_incorrect_attempt
					('0:00:00', u'C(12,9)')
					('0:00:25', u'C(13,9)')
	part3_correct_attempt
					['0:00:44', u'C(21,9)']

5 Student ID:ffhaddad

	first_attempt
					2015-10-10 20:50:07
	part1_correct_attempt
					['0:00:00', u'11']
	part2_correct_attempt
					['0:00:16', u'8']
	part3_incorrect_attempt
					('0:01:56', u'(11+8-1)!/(8!9!)')
					('0:02:54', u'(11+8)!/(8!9!)')
	part3_correct_attempt
					['0:04:56', u'(12+8-1)!/(8!11!)']

6 Student ID:rlhagen

	first_attempt
					2015-10-11 17:43:35
	part1_correct_attempt
					['0:00:00', u'12']
	part2_correct_attempt
					['0:00:00', u'11']
	part3_incorrect_attempt
					('0:01:00', u'12!/((12-11)!)')
					('0:02:37', u'23!/(10!(23-10)!)')
	part3_correct_attempt
					['0:04:27', u'23!/(11!(23-11)!)']

7 Student ID:jmmcalex

	first_attempt
					2015-10-15 07:20:50
	part1_correct_attempt
					['0:00:00', u'10']
	part2_correct_attempt
					['-3 days, 18:55:12', u'7']
	part3_incorrect_attempt
					('0:00:00', u'10!/[3!7!]')
	part3_correct_attempt
					['0:00:37', u'17!/[10!7!]']

8 Student ID:btn023

	first_attempt
					2015-10-14 17:39:42
	part1_correct_attempt
					['0:00:00', u'14']
	part2_correct_attempt
					['-1 day, 13:33:32', u'6']
	part3_incorrect_attempt
					('0:00:31', u'C(14,6)')
					('0:01:40', u'14!/(6!8!)')
					('0:02:09', u'P(15,6)')
					('0:02:21', u'15!')
					('0:02:33', u'C(15,6)')
					('0:03:44', u'C(9,6)')
					('0:04:00', u'C(15,9)')
	part3_correct_attempt
					['4:26:29', u'20!/(14!6!)']

9 Student ID:dgunawan

	first_attempt
					2015-10-14 20:34:23
	part1_correct_attempt
					['0:00:00', u'11']
	part2_correct_attempt
					['-1 day, 23:42:06', u'3']
	part3_incorrect_attempt
					('0:00:00', u'C(11, 3)')
					('0:00:10', u'C(12, 3)')
					('0:01:15', u'12^3')
					('1 day, 2:41:00', u'12 * 3')
					('1 day, 2:41:08', u'C(12,3)')

10 Student ID:mpanelo

	first_attempt
					2015-10-10 19:32:26
	part1_correct_attempt
					['0:00:00', u'12']
	part2_correct_attempt
					['-1 day, 23:47:45', u'2']
	part3_incorrect_attempt
					('0:00:00', u'12! / (2!9!)')
					('0:00:07', u'12! / (2!10!)')
	part3_correct_attempt
					['0:00:59', u'14! / (2!12!)']

11 Student ID:tcn013

	first_attempt
					2015-10-14 19:08:45
	part1_correct_attempt
					['0:00:00', u'10']
	part2_correct_attempt
					['-1 day, 23:59:23', u'7']
	part3_incorrect_attempt
					('0:00:35', u'C(10,7)')
					('0:00:42', u'C(9,7)')
	part3_correct_attempt
					['0:00:48', u'C(17,7)']

12 Student ID:pthsu

	first_attempt
					2015-10-10 19:46:18
	part1_correct_attempt
					['0:00:00', u'9']
	part2_correct_attempt
					['0:00:00', u'5']
	part3_incorrect_attempt
					('0:00:18', u'C(10,5)')
					('0:00:58', u'C(9,5)')
	part3_correct_attempt
					['0:01:07', u'C(14,5)']

13 Student ID:tcuddy

	first_attempt
					2015-10-10 19:14:08
	part1_correct_attempt
					['0:00:00', u'9']
	part2_correct_attempt
					['0:00:00', u'5']
	part3_incorrect_attempt
					('0:00:00', u'10!/(5!*5!)')
	part3_correct_attempt
					['0:01:21', u'14!/(5!9!)']

14 Student ID:djk006

	first_attempt
					2015-10-10 21:25:48
	part1_correct_attempt
					['0:00:00', u'8']
	part2_correct_attempt
					['0:00:00', u'5']
	part3_incorrect_attempt
					('0:00:00', u'13!/5!(8!)')
	part3_correct_attempt
					['0:00:16', u'13!/(5!8!)']

15 Student ID:dando

	first_attempt
					2015-10-09 23:04:10
	part1_correct_attempt
					['0:00:00', u'13']
	part2_correct_attempt
					['-1 day, 23:57:50', u'5']
	part3_incorrect_attempt
					('0:00:00', u'C(13,5)')
	part3_correct_attempt
					['0:00:33', u'C(18,5)']

16 Student ID:chc286

	first_attempt
					2015-10-11 23:13:53
	part1_correct_attempt
					['0:00:00', u'7']
	part2_correct_attempt
					['-1 day, 23:57:29', u'3']
	part3_incorrect_attempt
					('0:00:00', u'C(7,3)')
					('0:00:36', u'(7*6*5)/(3*2)')
	part3_correct_attempt
					['0:00:50', u'C(10,3)']

17 Student ID:abasu

	first_attempt
					2015-10-11 02:01:31
	part1_correct_attempt
					['0:00:00', u'9']
	part2_correct_attempt
					['0:00:00', u'7']
	part3_incorrect_attempt
					('0:01:08', u'9!/(7!*3!)')
					('0:04:00', u'C(9,7)')
	part3_correct_attempt
					['0:04:35', u'C(16,7)']

18 Student ID:sayao

	first_attempt
					2015-10-12 18:56:23
	part1_correct_attempt
					['0:00:00', u'11']
	part2_correct_attempt
					['0:00:00', u'8']
	part3_incorrect_attempt
					('0:00:11', u'C(11,8)')
					('0:00:24', u'P(11,8)')
					('0:00:31', u'C(11,8)')
					('0:00:50', u'C(12,8)')
	part3_correct_attempt
					['0:01:15', u'C(19,8)']

19 Student ID:anvan

	first_attempt
					2015-10-15 04:53:52
	part1_correct_attempt
					['0:00:00', u'7']
	part2_correct_attempt
					['-1 day, 19:54:20', u'5']
	part3_incorrect_attempt
					('0:01:03', u'12!(5!7!)')
	part3_correct_attempt
					['0:01:08', u'12!/(5!7!)']

20 Student ID:acvuong

	first_attempt
					2015-10-13 03:49:54
	part1_correct_attempt
					['0:00:00', u'10']
	part2_correct_attempt
					['0:00:00', u'4']
	part3_incorrect_attempt
					('0:00:00', u'C(10,4)')
	part3_correct_attempt
					['0:00:14', u'C(14,4)']

21 Student ID:flhernan

	first_attempt
					2015-10-14 22:48:48
	part1_correct_attempt
					['0:00:00', u'13']
	part2_correct_attempt
					['0:00:23', u'7']
	part3_incorrect_attempt
					('0:00:34', u'C(13,7)')
	part3_correct_attempt
					['0:00:44', u'C(20,7)']

22 Student ID:c1wei

	first_attempt
					2015-10-14 06:59:21
	part1_correct_attempt
					['0:00:00', u'13']
	part2_correct_attempt
					['0:00:48', u'12']
	part3_incorrect_attempt
					('0:19:14', u'12*14')
					('0:35:46', u'14!')
					('0:40:04', u'14^12')
					('0:55:43', u'13^12')
					('0:56:24', u'12^3')
					('13:19:07', u'14*13*12')
					('13:19:32', u'13*12')
	part3_correct_attempt
					['13:30:49', u'5200300']

23 Student ID:arc013

	first_attempt
					2015-10-13 03:06:48
	part1_correct_attempt
					['0:00:00', u'13']
	part2_correct_attempt
					['0:00:00', u'4']
	part3_incorrect_attempt
					('0:00:52', u'C(16,4)')
					('0:01:55', u'C(12,3)')
					('0:02:01', u'C(13,4)')
	part3_correct_attempt
					['23:55:06', u'C(17,13)']

24 Student ID:mitopete

	first_attempt
					2015-10-13 18:06:54
	part1_correct_attempt
					['0:00:00', u'11']
	part2_correct_attempt
					['-1 day, 23:57:13', u'3']
	part3_incorrect_attempt
					('0:00:48', u'12!')
					('0:01:11', u'3^12')
					('0:03:49', u'12!(3!(9!))')
					('0:03:58', u'12!/(3!(9!))')
					('1:20:50', u'14!/(3!4!)')
	part3_correct_attempt
					['1:21:35', u'364']

25 Student ID:starinia

	first_attempt
					2015-10-15 02:09:45
	part1_correct_attempt
					['0:00:00', u'8']
	part2_correct_attempt
					['0:00:00', u'4']
	part3_incorrect_attempt
					('0:00:04', u'8!/(4!4!)')
	part3_correct_attempt
					['0:01:26', u'12!/(4!8!)']

26 Student ID:m4salaza

	first_attempt
					2015-10-15 23:22:26
	part1_correct_attempt
					['0:00:00', u'12']
	part2_correct_attempt
					['0:00:00', u'10']
	part3_incorrect_attempt
					('0:00:23', u'C(12, 10)')
					('0:02:07', u'12!/(10!*2)')
					('0:03:50', u'13!/(10!*3*2)')

27 Student ID:tak068

	first_attempt
					2015-10-14 05:55:09
	part1_correct_attempt
					['0:00:00', u'14']
	part2_correct_attempt
					['-1 day, 23:59:49', u'7']
	part3_incorrect_attempt
					('0:00:47', u'14!/7!/7!')
					('0:02:54', u'15!/7!/8!')
					('0:05:32', u'15!/(7!8!)')
					('0:06:18', u'7!')
					('0:06:25', u'7!14!')
					('0:06:31', u'7!8!')
					('0:06:41', u'15!/7!')
					('0:06:46', u'15!/8!')
					('0:06:53', u'14!/7!')
					('0:06:58', u'14!/8!')
					('0:07:04', u'14!/6!')
					('0:12:13', u'15!14!13!12!11!10!9!')
	part3_correct_attempt
					['0:14:22', u'21!/(7!14!)']

28 Student ID:yos017

	first_attempt
					2015-10-14 06:06:31
	part1_correct_attempt
					['0:00:00', u'13']
	part2_correct_attempt
					['-1 day, 23:59:35', u'4']
	part3_incorrect_attempt
					('0:00:51', u'13!/(4!*9!)')
					('0:01:51', u'17!/(4!*9!)')
	part3_correct_attempt
					['0:02:12', u'17!/(4!*13!)']

29 Student ID:ggaddi

	first_attempt
					2015-10-12 18:31:00
	part1_correct_attempt
					['0:00:00', u'9']
	part2_correct_attempt
					['0:00:00', u'2']
	part3_incorrect_attempt
					('0:00:00', u'11!/9!')
					('0:00:08', u'11!/2!')
	part3_correct_attempt
					['0:00:32', u'11!/(9!*2!)']

30 Student ID:jit002

	first_attempt
					2015-10-15 04:24:27
	part1_correct_attempt
					['0:00:00', u'13']
	part2_correct_attempt
					['0:00:00', u'7']
	part3_incorrect_attempt
					('0:00:00', u'C(13,7)')
	part3_correct_attempt
					['0:03:10', u'C(20,7)']

31 Student ID:b3hwang

	first_attempt
					2015-10-15 22:47:38
	part1_correct_attempt
					['0:00:00', u'7']
	part2_correct_attempt
					['-1 day, 23:55:46', u'6']
	part3_incorrect_attempt
					('0:01:06', u'C(7,6)')
	part3_correct_attempt
					['0:01:57', u'C(13,6)']

32 Student ID:jag028

	first_attempt
					2015-10-15 00:28:08
	part1_correct_attempt
					['0:00:00', u'14']
	part2_correct_attempt
					['-1 day, 23:59:44', u'3']
	part3_incorrect_attempt
					('0:00:19', u'C(15,3)')
					('0:00:28', u'C(14,3)')
					('0:03:18', u'15*14*13')
					('0:03:51', u'(15!)/(3!(15-3)!)')
					('0:05:16', u'C(14,3)')
					('0:06:56', u'C(15,3)')
					('0:21:55', u'C(14,3)')
					('0:22:15', u'C(15,3)')
					('0:22:30', u'C(12,3)')
					('0:22:36', u'C(11,3)')
					('0:22:42', u'C(10,3)')
					('0:22:48', u'C(16,3)')
					('0:22:56', u'C(9,3)')
					('0:23:02', u'C(8,3)')
					('0:23:07', u'C(7,3)')
					('0:23:17', u'C(6,3)')
					('0:23:25', u'C(15,4)')
					('0:23:31', u'C(15,2)')
					('0:23:40', u'C(14,2)')
					('0:23:48', u'C(13,2)')
					('0:23:55', u'C(12,2)')
					('0:24:08', u'C(11,2)')
					('0:24:14', u'C(11,3)')
	part3_correct_attempt
					['2:18:59', u'C(17,3)']

33 Student ID:ccn001

	first_attempt
					2015-10-12 21:28:00
	part1_correct_attempt
					['0:00:00', u'14']
	part2_correct_attempt
					['-1 day, 23:54:37', u'7']
	part3_incorrect_attempt
					('0:00:00', u'15!/(7!8!)')
	part3_correct_attempt
					['0:01:01', u'21!/(7!14!)']

34 Student ID:jjchung

	first_attempt
					2015-10-14 19:16:40
	part1_correct_attempt
					['0:00:00', u'13']
	part2_correct_attempt
					['0:00:00', u'2']
	part3_incorrect_attempt
					('0:00:00', u'14!/(12!2!)')
					('0:00:20', u'13!/(11!2!)')
					('0:01:09', u'C(14,2)')
					('0:01:17', u'C(13,2)')
					('0:02:11', u'14^2')
	part3_correct_attempt
					['0:02:52', u'C(15,2)']

35 Student ID:atorr

	first_attempt
					2015-10-11 01:09:38
	part1_correct_attempt
					['0:00:00', u'10']
	part2_correct_attempt
					['-1 day, 23:59:19', u'4']
	part3_incorrect_attempt
					('0:02:33', u'C((10 + 4 - 1), (4 - 1))')
					('0:02:57', u'C((10 + 4 - 1), (10 - 1))')
					('0:03:16', u'C((10 + 4 - 1), (4))')
					('0:03:38', u'C((10 + 4 - 1), (4 - 1))')
					('0:04:15', u'C((10 + 4 - 1), (11))')
					('0:04:53', u'C((10 + 4 - 1), (10 - 4))')
					('0:05:16', u'C((10 + 4 - 1), (4 - 1))')
					('0:06:03', u'C((10 - 1), (4 - 1))')
					('0:06:29', u'C(10,4)')
					('1:38:33', u'C(9,3)')
					('1:38:52', u'C(9,4)')
					('1:39:43', u'C(10,4)')
					('1:40:41', u'C(10 + 4 - 1, 10 - 1)')
					('1:41:19', u'C(10 + 4 - 1, 4 - 1)')
					('1:42:56', u'C(9,3)')
					('1:43:35', u'C(10 - 1,4-1)')
					('1:43:56', u'C(10 - 1,4)')
					('1:45:44', u'C(9,3)')
					('2:42:22', u'C((10 + 4 - 1), (4 - 1))')
					('3:09:18', u'C(10 + 4 - 1, 4 - 1)')
					('3:17:26', u'C(11,4)')
					('3:19:07', u'11 * 10 * 9 * 8')
					('3:21:56', u'C(10 + 4 - 1, 4 - 1)')
					('3:28:29', u'C(10,4)')
					('3:28:44', u'11^4')
					('3:29:23', u'C(10 - 1, 4 - 1)')
					('3:29:33', u'C(10 - 1, 4)')
					('3:34:20', u'C(10,4)')
					('3:35:07', u'C(10+4-1,4-1)')
					('3:36:21', u'C(11,3)')
					('3:36:27', u'C(11,4)')
					('3:36:44', u'C(10 + 4 - 1, 4 - 1)')
					('3:37:51', u'C(13,4)')
					('3:38:00', u'C(13,9)')
	part3_correct_attempt
					['3 days, 0:18:57', u'C(14,4)']

36 Student ID:cprafull

	first_attempt
					2015-10-14 06:58:53
	part1_correct_attempt
					['0:00:00', u'11']
	part2_correct_attempt
					['-1 day, 23:59:41', u'10']
	part3_incorrect_attempt
					('0:01:17', u'21!/(10!)(11!)')
	part3_correct_attempt
					['0:01:23', u'21!/((10!)(11!))']

37 Student ID:sachadal

	first_attempt
					2015-10-15 15:06:32
	part1_correct_attempt
					['0:00:00', u'11']
	part2_correct_attempt
					['-1 day, 23:41:13', u'C(14,9)']
	part3_incorrect_attempt
					('0:00:07', u'C(11,9)')
	part3_correct_attempt
					['0:00:19', u'C(20,9)']

38 Student ID:jic212

	first_attempt
					2015-10-11 23:09:39
	part1_correct_attempt
					['0:00:00', u'14']
	part2_correct_attempt
					['0:00:00', u'13']
	part3_incorrect_attempt
					('0:00:29', u'(14!)/(13!)')
					('0:05:33', u'13!')
					('0:06:21', u'C(14,13)')
					('0:06:32', u'C(15,13)')
					('0:08:02', u'13!')
					('3:30:54', u'C(14,13)')
	part3_correct_attempt
					['3:31:19', u'C(27,13)']

39 Student ID:c2qiu

	first_attempt
					2015-10-11 09:23:30
	part1_correct_attempt
					['0:00:00', u'9']
	part2_correct_attempt
					['0:00:00', u'3']
	part3_incorrect_attempt
					('0:00:00', u'10!/(3!*7!)')
	part3_correct_attempt
					['0:00:37', u'12!/(3!*9!)']

40 Student ID:dis003

	first_attempt
					2015-10-15 11:00:02
	part1_correct_attempt
					['0:00:00', u'9']
	part2_correct_attempt
					['-1 day, 23:59:12', u'8']
	part3_incorrect_attempt
					('0:00:19', u'C(9,8)')
	part3_correct_attempt
					['0:00:38', u'C(17,8)']

41 Student ID:thwan

	first_attempt
					2015-10-10 19:05:00
	part1_correct_attempt
					['0:00:00', u'9']
	part2_correct_attempt
					['0:00:00', u'5']
	part3_incorrect_attempt
					('0:00:00', u'9!/[(5!)(4!)]')
	part3_correct_attempt
					['0:00:51', u'(9+5)!/[(5!)(9!)]']

42 Student ID:krkelkar

	first_attempt
					2015-10-14 02:23:18
	part1_correct_attempt
					['0:00:00', u'11-1']
	part2_correct_attempt
					['-1 day, 23:58:35', u'3']
	part3_incorrect_attempt
					('0:00:00', u'11! / (3!*(11-3)! )')
	part3_correct_attempt
					['1:10:28', u'13! / (3!*10!)']

43 Student ID:lcardoso

	first_attempt
					2015-10-13 16:04:59
	part1_correct_attempt
					['0:00:00', u'8']
	part2_correct_attempt
					['0:00:00', u'5']
	part3_incorrect_attempt
					('0:00:36', u'C(8,5)')
	part3_correct_attempt
					['0:01:53', u'C(9-1+5,5)']

44 Student ID:jel075

	first_attempt
					2015-10-15 00:52:36
	part1_correct_attempt
					['0:00:00', u'14']
	part2_correct_attempt
					['0:00:00', u'13']
	part3_incorrect_attempt
					('0:00:00', u'C(14,13)')
					('0:00:15', u'14!/(13!)')
					('0:01:09', u'15!/(13!2!)')
	part3_correct_attempt
					['0:01:30', u'27!/(13!14!)']

45 Student ID:etemlock

	first_attempt
					2015-10-11 00:35:30
	part1_correct_attempt
					['0:00:00', u'10']
	part2_correct_attempt
					['0:00:00', u'3']
	part3_incorrect_attempt
					('0:00:00', u'C(10,3)')
	part3_correct_attempt
					['0:00:07', u'C(13,3)']

46 Student ID:wcwhite

	first_attempt
					2015-10-14 01:40:38
	part2_correct_attempt
					['0:00:00', u'7']
	part3_incorrect_attempt
					('0:08:06', u'14!/(14-7)!')
					('0:08:41', u'7!')
					('0:08:52', u'14!')
					('0:17:05', u'14!/(7!(14-7)!)')
					('0:28:09', u'C(14,7)')
					('0:28:29', u'14!/7!(7!)')
					('0:28:42', u'14!/7!(14-7)!')
					('0:28:52', u'14!/[7!(14-7)!]')

47 Student ID:cstringh

	first_attempt
					2015-10-12 22:00:23
	part1_correct_attempt
					['0:00:00', u'7']
	part2_correct_attempt
					['-1 day, 23:59:40', u'5']
	part3_incorrect_attempt
					('0:00:09', u'7*5')
	part3_correct_attempt
					['0:05:56', u'792']

48 Student ID:v4sharma

	first_attempt
					2015-10-14 00:41:38
	part1_correct_attempt
					['0:00:00', u'14']
	part2_correct_attempt
					['0:00:00', u'7']
	part3_incorrect_attempt
					('0:00:20', u'C(14, 7)')
					('0:00:49', u'14!/((7!) * (7!))')
	part3_correct_attempt
					['0:02:49', u'C(21, 7)']

49 Student ID:aurodrig

	first_attempt
					2015-10-15 18:47:45
	part1_correct_attempt
					['0:00:00', u'13']
	part2_correct_attempt
					['0:04:50', u'9']
	part3_incorrect_attempt
					('0:06:05', u'C(14,9)')
					('0:08:33', u'C(27,14)')
					('0:08:41', u'C(27,9)')
					('0:09:33', u'C(14,9)')
					('0:10:37', u'14!/(9!5!)')
					('0:11:23', u'C(9,9)')
					('0:12:34', u'C(27,14)')
	part3_correct_attempt
					['0:13:32', u'C(22,9)']

50 Student ID:dcastlem

	first_attempt
					2015-10-15 03:53:38
	part1_correct_attempt
					['0:00:00', u'14']
	part2_correct_attempt
					['-1 day, 23:57:09', u'21!/((6!)(15!))']
	part3_incorrect_attempt
					('0:00:19', u'14!((6!)(8!))')
					('0:00:27', u'14!/((6!)(8!))')
					('0:00:49', u'14!/6!')
	part3_correct_attempt
					['0:01:24', u'20!/((6!)(14!))']

51 Student ID:dac064

	first_attempt
					2015-10-15 19:34:09
	part1_correct_attempt
					['0:00:00', u'10']
	part2_correct_attempt
					['0:00:00', u'9']
	part3_incorrect_attempt
					('0:00:38', u'11^9')
					('0:01:03', u'C(11,9)')
	part3_correct_attempt
					['0:02:15', u'C(19,9)']

52 Student ID:sghouse

	first_attempt
					2015-10-12 18:53:48
	part1_correct_attempt
					['0:00:00', u'12']
	part2_correct_attempt
					['-1 day, 23:58:24', u'2']
	part3_incorrect_attempt
					('0:00:43', u'6*11')
	part3_correct_attempt
					['0:01:11', u'7*13']

53 Student ID:lywong

	first_attempt
					2015-10-13 00:07:31
	part1_correct_attempt
					['0:00:00', u'13']
	part2_correct_attempt
					['-1 day, 23:58:05', u'7']
	part3_incorrect_attempt
					('0:00:16', u'13!(7!(13-7)!)')
					('0:00:22', u'13!/(7!(13-7)!)')
					('0:01:17', u'14!/(7!(14-7)!)')
					('0:02:59', u'C(17,7)')
	part3_correct_attempt
					['0:03:11', u'C(20,7)']

54 Student ID:jcl084

	first_attempt
					2015-10-13 20:22:09
	part1_correct_attempt
					['0:00:00', u'10']
	part2_correct_attempt
					['0:00:00', u'4']
	part3_incorrect_attempt
					('0:00:06', u'C(10,4)')
					('0:00:21', u'P(10,4)')
					('0:00:36', u'P(11,4)')
					('0:00:42', u'C(11,4)')
					('0:00:59', u'C(10,3)')
	part3_correct_attempt
					['0:01:46', u'C(14,4)']

55 Student ID:glcohen

	first_attempt
					2015-10-13 04:48:18
	part1_correct_attempt
					['0:00:00', u'9']
	part2_correct_attempt
					['0:00:00', u'2']
	part3_incorrect_attempt
					('0:00:24', u'9!/(2!7!)')
					('0:01:03', u'10!/(2!7!)')
					('0:01:16', u'(9 2)')
					('0:03:17', u'11!/10!')
					('0:03:23', u'9!/2!')
					('0:04:29', u'9!')
	part3_correct_attempt
					['0:06:23', u'11!/(2!9!)']

56 Student ID:achava

	first_attempt
					2015-10-13 07:34:47
	part1_correct_attempt
					['0:00:00', u'9']
	part2_correct_attempt
					['0:00:00', u'5']
	part3_incorrect_attempt
					('0:00:28', u'C(9, 5)')
					('0:01:04', u'9!/(5!(4!))')
					('0:01:25', u'9!/(4!)')
	part3_correct_attempt
					['0:02:06', u'C(14, 5)']

57 Student ID:d6he

	first_attempt
					2015-10-15 05:41:07
	part1_correct_attempt
					['0:00:00', u'12']
	part2_correct_attempt
					['-1 day, 23:59:22', u'8']
	part3_incorrect_attempt
					('0:00:35', u'12!/(8!4!)')
					('0:00:45', u'13!/(8!5!)')
	part3_correct_attempt
					['0:01:52', u'20!/(8!12!)']

58 Student ID:thk002

	first_attempt
					2015-10-12 01:31:45
	part1_correct_attempt
					['0:00:00', u'7']
	part2_correct_attempt
					['-1 day, 23:45:06', u'4']
	part3_incorrect_attempt
					('0:00:17', u'C(7,4)')
	part3_correct_attempt
					['0:00:22', u'C(11,4)']

59 Student ID:jcj006

	first_attempt
					2015-10-13 20:34:56
	part1_correct_attempt
					['0:00:00', u'9']
	part2_correct_attempt
					['0:00:00', u'8']
	part3_incorrect_attempt
					('0:00:00', u'9!/8!')
	part3_correct_attempt
					['0:01:01', u'17!/(8!9!)']

60 Student ID:mtrafeca

	first_attempt
					2015-10-11 05:27:12
	part1_correct_attempt
					['0:00:00', u'8']
	part2_correct_attempt
					['0:00:34', u'5']
	part3_incorrect_attempt
					('0:01:04', u'9!/(5!*4!)')
					('0:01:29', u'7!/(3!*4!)')
	part3_correct_attempt
					['0:03:21', u'13!/(5!*8!)']

61 Student ID:dlt009

	first_attempt
					2015-10-14 01:07:29
	part1_correct_attempt
					['0:00:00', u'10']
	part2_correct_attempt
					['0:00:00', u'6']
	part3_incorrect_attempt
					('0:00:00', u'10!/[(10-6)!(6!)]')
					('0:00:17', u'10!/[(10-6)!]')
	part3_correct_attempt
					['0:01:27', u'16!/[ (16-10)!10!]']

62 Student ID:n2patil

	first_attempt
					2015-10-13 15:47:17
	part1_correct_attempt
					['0:00:00', u'9']
	part2_correct_attempt
					['0:00:13', u'3']
	part3_incorrect_attempt
					('0:00:32', u'C(9,3)')
	part3_correct_attempt
					['0:02:40', u'220']

63 Student ID:bakang

	first_attempt
					2015-10-15 01:31:58
	part1_correct_attempt
					['0:00:00', u'14']
	part2_correct_attempt
					['0:00:00', u'10']
	part3_incorrect_attempt
					('0:00:00', u'C(14,10)')
					('0:00:28', u'C(14,10)')
	part3_correct_attempt
					['0:00:41', u'C(24,10)']

64 Student ID:ksmurlo

	first_attempt
					2015-10-13 23:09:15
	part1_correct_attempt
					['0:00:00', u'11-1']
	part2_correct_attempt
					['0:00:00', u'3']
	part3_incorrect_attempt
					('0:00:00', u'C(10,3)')
	part3_correct_attempt
					['0:00:20', u'C(13,3)']

65 Student ID:ttimmons

	first_attempt
					2015-10-11 01:00:05
	part1_correct_attempt
					['0:00:00', u'8']
	part2_correct_attempt
					['0:00:00', u'7']
	part3_incorrect_attempt
					('0:00:00', u'C(8,7)')
	part3_correct_attempt
					['0:00:15', u'C((8+7),7)']

66 Student ID:jeqin

	first_attempt
					2015-10-15 12:16:13
	part1_correct_attempt
					['0:00:00', u'7']
	part2_correct_attempt
					['-1 day, 23:59:27', u'4']
	part3_incorrect_attempt
					('0:00:36', u'11!(7!4!)')
	part3_correct_attempt
					['0:00:40', u'11!/(7!4!)']

67 Student ID:jnatale

	first_attempt
					2015-10-15 03:45:50
	part1_correct_attempt
					['0:00:00', u'12']
	part2_correct_attempt
					['-1 day, 23:54:45', u'5']
	part3_incorrect_attempt
					('0:00:11', u'C(12,5)')
					('0:01:36', u'C(13,5)')
	part3_correct_attempt
					['0:03:56', u'C(17,5)']

68 Student ID:ielouaae

	first_attempt
					2015-10-15 07:40:39
	part1_correct_attempt
					['0:00:00', u'12']
	part2_correct_attempt
					['0:00:14', u'7']
	part3_incorrect_attempt
					('0:01:25', u'12!/(5!7!)')
	part3_correct_attempt
					['0:02:04', u'19!/(12!7!)']

69 Student ID:tol003

	first_attempt
					2015-10-13 23:54:43
	part1_correct_attempt
					['0:00:00', u'12']
	part2_correct_attempt
					['0:00:00', u'7']
	part3_incorrect_attempt
					('0:00:00', u'C(12,7)')
					('0:00:49', u'C(13,7)')
	part3_correct_attempt
					['0:01:17', u'C(19,7)']

70 Student ID:skodigal

	first_attempt
					2015-10-15 00:26:36
	part1_correct_attempt
					['0:00:00', u'11']
	part2_correct_attempt
					['0:00:13', u'7']
	part3_incorrect_attempt
					('0:00:13', u'C(23,7)')
	part3_correct_attempt
					['0:00:25', u'C(18,7)']

71 Student ID:kew017

	first_attempt
					2015-10-15 17:26:53
	part1_correct_attempt
					['0:00:00', u'12']
	part2_correct_attempt
					['-1 day, 23:59:43', u'7']
	part3_incorrect_attempt
					('0:00:07', u'19!/(7!3!)')
	part3_correct_attempt
					['0:01:18', u'19!/(7!12!)']

72 Student ID:haliew

	first_attempt
					2015-10-13 23:41:33
	part1_correct_attempt
					['0:00:00', u'10']
	part2_correct_attempt
					['0:00:00', u'3']
	part3_incorrect_attempt
					('0:00:00', u'C(10,3)')
					('0:00:13', u'C(11,3)')
	part3_correct_attempt
					['0:00:32', u'C(13,3)']

73 Student ID:kmc012

	first_attempt
					2015-10-15 02:07:44
	part1_correct_attempt
					['0:00:00', u'7']
	part2_correct_attempt
					['0:00:00', u'4']
	part3_incorrect_attempt
					('0:00:25', u'(7!)/((3!)*(4!))')
					('0:03:02', u'(9!)/((5!)*(4!))')
	part3_correct_attempt
					['0:06:24', u'(11!)/((4!)*(7!))']

74 Student ID:daw023

	first_attempt
					2015-10-14 23:06:31
	part1_correct_attempt
					['0:00:00', u'9']
	part2_correct_attempt
					['0:00:00', u'4']
	part3_incorrect_attempt
					('0:00:00', u'9!/(4!*5!)')
					('0:00:33', u'C(9,4)')
					('0:00:55', u'9!/4!')
	part3_correct_attempt
					['0:01:37', u'(9+4)!/(4!*(13-4)!)']

75 Student ID:csl030

	first_attempt
					2015-10-14 01:30:01
	part1_correct_attempt
					['0:00:00', u'14']
	part2_correct_attempt
					['-1 day, 23:56:40', u'8']
	part3_incorrect_attempt
					('0:00:12', u'C(14,7)')
					('0:01:13', u'C(14,8)')
	part3_correct_attempt
					['0:02:15', u'C(22,8)']

76 Student ID:rbdoming

	first_attempt
					2015-10-14 18:31:04
	part1_correct_attempt
					['0:00:00', u'13']
	part2_correct_attempt
					['0:00:00', u'5']
	part3_incorrect_attempt
					('0:00:00', u'14*13*12*11*10/5!')
					('0:01:01', u'C(14,5)')
					('0:02:52', u'C(13,5)')
	part3_correct_attempt
					['0:03:17', u'C(18,5)']

77 Student ID:abjara

	first_attempt
					2015-10-12 09:34:27
	part1_correct_attempt
					['0:00:00', u'7']
	part2_correct_attempt
					['-1 day, 23:23:36', u'6']
	part3_incorrect_attempt
					('0:00:00', u'8!/6!')
					('0:00:27', u'8!/(2!*6!)')
					('0:09:50', u'8^6')
					('0:10:04', u'6^8')
					('0:51:10', u'7!/6!')
					('0:51:39', u'8!/6!')
					('0:58:40', u'13!/6!')
	part3_correct_attempt
					['0:58:55', u'13!/(6!*7!)']

78 Student ID:klala

	first_attempt
					2015-10-12 04:12:21
	part1_correct_attempt
					['0:00:00', u'12']
	part2_correct_attempt
					['0:00:00', u'5']
	part3_incorrect_attempt
					('0:00:22', u'C(12,5)')
	part3_correct_attempt
					['0:00:41', u'C(17,5)']

79 Student ID:dlgoldbe

	first_attempt
					2015-10-13 00:56:19
	part1_correct_attempt
					['0:00:00', u'8']
	part2_correct_attempt
					['-1 day, 23:57:25', u'7']
	part3_incorrect_attempt
					('0:02:14', u'(7!)/(3!*(7-3)!)')
					('0:03:06', u'(9!)/(7!*(9-7)!)')
	part3_correct_attempt
					['0:03:46', u'(15!)/(7!*(15-7)!)']

80 Student ID:akhmelni

	first_attempt
					2015-10-15 22:36:54
	part1_correct_attempt
					['0:00:00', u'14']
	part3_incorrect_attempt
					('0:00:11', u'C(14,3)')
					('0:01:22', u'C(15,3)')
					('0:03:16', u'C(14,3)')
	part3_correct_attempt
					['0:03:55', u'C(17,3)']

81 Student ID:qtluong

	first_attempt
					2015-10-12 07:43:51
	part1_correct_attempt
					['0:00:00', u'14']
	part2_correct_attempt
					['0:00:00', u'9']
	part3_incorrect_attempt
					('0:00:00', u'23!/(23-9)!')
	part3_correct_attempt
					['0:00:24', u'23!/(9!(23-9)!)']

82 Student ID:masaro

	first_attempt
					2015-10-10 09:27:30
	part1_correct_attempt
					['0:00:00', u'12']
	part2_correct_attempt
					['0:00:00', u'10']
	part3_incorrect_attempt
					('0:00:00', u'12!/(10!*2!)')
	part3_correct_attempt
					['0:01:01', u'22!/(10!*12!)']

83 Student ID:rwthomps

	first_attempt
					2015-10-11 22:15:19
	part1_correct_attempt
					['0:00:00', u'12']
	part2_correct_attempt
					['0:00:00', u'9']
	part3_incorrect_attempt
					('0:00:00', u'C(12, 9)')
	part3_correct_attempt
					['0:01:21', u'C(21, 9)']

84 Student ID:s1powers

	first_attempt
					2015-10-11 19:32:09
	part1_correct_attempt
					['0:00:00', u'9']
	part2_correct_attempt
					['-1 day, 23:59:34', u'8']
	part3_incorrect_attempt
					('0:00:25', u'9!/(1!8!)')
					('0:01:03', u'17!/(11!8!)')
	part3_correct_attempt
					['0:03:24', u'17!/(9!8!)']

85 Student ID:e9brown

	first_attempt
					2015-10-14 08:35:59
	part1_correct_attempt
					['0:00:00', u'7']
	part2_correct_attempt
					['-1 day, 23:58:42', u'5']
	part3_incorrect_attempt
					('0:00:23', u'C(7,5)')
	part3_correct_attempt
					['0:00:43', u'C(12,5)']

86 Student ID:vsosnovs

	first_attempt
					2015-10-15 03:57:21
	part1_correct_attempt
					['0:00:00', u'14']
	part2_correct_attempt
					['-1 day, 23:57:22', u'6']
	part3_incorrect_attempt
					('0:00:46', u'C(14,7)')
					('0:00:52', u'C(14,6)')
	part3_correct_attempt
					['0:01:14', u'C(20,6)']

87 Student ID:k5law

	first_attempt
					2015-10-12 01:33:52
	part1_correct_attempt
					['0:00:00', u'13']
	part2_correct_attempt
					['-1 day, 23:59:54', u'7']
	part3_incorrect_attempt
					('0:01:11', u'(13+7)!/(7!)')
					('0:01:16', u'(13+7)!/(13!)')
					('0:01:27', u'(13+7)!/(14!)')
					('0:02:14', u'20!/(20-7)!')
					('0:02:19', u'20!/(20-13)!')
	part3_correct_attempt
					['0:02:34', u'20!/(13!7!)']

88 Student ID:b1green

	first_attempt
					2015-10-15 20:38:42
	part1_correct_attempt
					['0:00:00', u'14']
	part2_correct_attempt
					['0:00:00', u'6']
	part3_incorrect_attempt
					('0:00:00', u'C(14,6)')
					('0:02:08', u'14!/[6!(14-6)!]')
					('0:02:35', u'C(15,6)')
	part3_correct_attempt
					['0:03:05', u'C(20,6)']

89 Student ID:s2chaudh

	first_attempt
					2015-10-13 00:04:05
	part1_correct_attempt
					['0:00:00', u'13']
	part2_correct_attempt
					['-1 day, 23:55:05', u'10']
	part3_incorrect_attempt
					('0:00:14', u'C(13,10)')
					('0:00:44', u'C(13,9)')
	part3_correct_attempt
					['0:01:24', u'C(23,10)']

90 Student ID:jmiclat

	first_attempt
					2015-10-15 17:04:43
	part1_correct_attempt
					['0:00:00', u'9']
	part2_correct_attempt
					['-1 day, 22:13:50', u'6']
	part3_incorrect_attempt
					('0:00:00', u'9!/(6!3!)')
	part3_correct_attempt
					['0:00:39', u'15!/(6!9!)']

91 Student ID:gsrandha

	first_attempt
					2015-10-12 06:54:27
	part1_correct_attempt
					['0:00:00', u'12']
	part2_correct_attempt
					['0:00:00', u'4']
	part3_incorrect_attempt
					('0:00:09', u'12!/((4!))')
	part3_correct_attempt
					['0:00:32', u'16!/((12!)(4!))']

92 Student ID:jhc010

	first_attempt
					2015-10-15 15:53:08
	part1_correct_attempt
					['0:00:00', u'13']
	part3_incorrect_attempt
					('0:00:37', u'C(13,7)')
	part3_correct_attempt
					['0:00:55', u'C(20,7)']

93 Student ID:rsmurlo

	first_attempt
					2015-10-13 16:17:38
	part1_correct_attempt
					['0:00:00', u'14']
	part2_correct_attempt
					['-1 day, 23:59:24', u'4']
	part3_incorrect_attempt
					('0:00:36', u'14!/(10!4!)')
	part3_correct_attempt
					['0:01:13', u'18!/(14!4!)']

94 Student ID:anl114

	first_attempt
					2015-10-15 07:32:24
	part1_correct_attempt
					['0:00:00', u'11']
	part2_correct_attempt
					['0:00:00', u'2']
	part3_incorrect_attempt
					('0:00:59', u'12^2')
					('0:02:34', u'12!')
					('0:02:52', u'12!/2!')
	part3_correct_attempt
					['0:03:45', u'78']

95 Student ID:pnquach

	first_attempt
					2015-10-15 01:52:57
	part1_correct_attempt
					['0:00:00', u'7']
	part2_correct_attempt
					['0:00:00', u'3']
	part3_incorrect_attempt
					('0:00:00', u'7!/(3!*4!)')
	part3_correct_attempt
					['0:00:24', u'10!/(3!*7!)']

96 Student ID:achinn

	first_attempt
					2015-10-12 23:30:16
	part1_correct_attempt
					['0:00:00', u'7']
	part2_correct_attempt
					['-1 day, 23:54:43', u'2']
	part3_incorrect_attempt
					('0:00:41', u'8*7/2')
					('0:02:27', u'C(8,2)')
					('0:04:02', u'7!')
					('0:48:58', u'(8*7)/2')
					('0:59:59', u'56/2')
	part3_correct_attempt
					['1:50:14', u'C(9,2)']

97 Student ID:kalang

	first_attempt
					2015-10-13 15:13:08
	part1_correct_attempt
					['0:00:00', u'10']
	part2_correct_attempt
					['-1 day, 23:59:39', u'6']
	part3_incorrect_attempt
					('0:00:14', u'C(10,6)')
	part3_correct_attempt
					['0:00:43', u'C(16,6)']

98 Student ID:msaguiar

	first_attempt
					2015-10-13 05:25:55
	part1_correct_attempt
					['0:00:00', u'13']
	part2_correct_attempt
					['0:00:00', u'4']
	part3_incorrect_attempt
					('0:00:00', u'C(13,4)')
					('0:00:10', u'C(14,4)')
					('0:00:40', u'C(18,4)')
	part3_correct_attempt
					['0:01:09', u'C(17,4)']

99 Student ID:aalhaida

	first_attempt
					2015-10-15 17:03:37
	part1_correct_attempt
					['0:00:00', u'9']
	part2_correct_attempt
					['0:00:00', u'8']
	part3_incorrect_attempt
					('0:00:00', u'9!/(8!)')
	part3_correct_attempt
					['0:01:01', u'17!/(8!9!)']

100 Student ID:hah008

	first_attempt
					2015-10-15 08:52:37
	part1_correct_attempt
					['0:00:00', u'8']
	part2_correct_attempt
					['0:00:18', u'7']
	part3_incorrect_attempt
					('0:01:06', u'14!/(7!7!)')
					('0:02:25', u'14!/(7!*7!)')
	part3_correct_attempt
					['0:06:19', u'15!/(8!7!)']

101 Student ID:mcatozzi

	first_attempt
					2015-10-13 23:55:17
	part1_correct_attempt
					['0:00:00', u'13']
	part2_correct_attempt
					['0:00:00', u'9']
	part3_incorrect_attempt
					('0:00:12', u'C(13,9)')
	part3_correct_attempt
					['0:00:34', u'C(22,9)']

102 Student ID:jnn015

	first_attempt
					2015-10-11 05:14:22
	part1_correct_attempt
					['0:00:00', u'14']
	part2_correct_attempt
					['0:00:00', u'12']
	part3_incorrect_attempt
					('0:00:00', u'14!/12!/2!')
					('0:11:27', u'5^3')
					('0:31:25', u'12^15')
					('0:32:40', u'15^12')
					('0:33:05', u'15!/12!/3!')
					('0:34:04', u'14!/2!/12!')
					('0:35:16', u'26!/2!/12!')
	part3_correct_attempt
					['0:35:42', u'26!/14!/12!']

103 Student ID:acs008

	first_attempt
					2015-10-15 05:45:19
	part1_correct_attempt
					['0:00:00', u'10']
	part2_correct_attempt
					['-1 day, 23:59:00', u'7']
	part3_incorrect_attempt
					('0:11:32', u'11!/(4!*7!)')
					('0:12:38', u'10!/(3!*7!)')
					('0:16:30', u'11!/4!')
					('0:17:08', u'11!/4!*7!')

104 Student ID:dpereira

	first_attempt
					2015-10-10 05:48:21
	part1_correct_attempt
					['0:00:00', u'7']
	part2_correct_attempt
					['0:00:36', u'2']
	part3_incorrect_attempt
					('0:00:36', u'C(7,2)')
	part3_correct_attempt
					['0:00:44', u'C(9,2)']

105 Student ID:hmshah

	first_attempt
					2015-10-15 08:40:18
	part1_correct_attempt
					['0:00:00', u'11']
	part2_correct_attempt
					['0:00:00', u'2']
	part3_incorrect_attempt
					('0:00:25', u'C(11,2)')
	part3_correct_attempt
					['0:01:59', u'13!/ ( 11! * 2!)']

106 Student ID:dtea

	first_attempt
					2015-10-15 22:51:37
	part1_correct_attempt
					['0:00:00', u'12']
	part2_correct_attempt
					['-1 day, 23:55:06', u'10']
	part3_incorrect_attempt
					('0:01:24', u'7!/(3!(7-3)!)')
					('0:01:42', u'12!/(10!(12-10)!)')
	part3_correct_attempt
					['0:02:14', u'22!/(10!(22-10)!)']

107 Student ID:lahawkin

	first_attempt
					2015-10-15 04:59:03
	part1_correct_attempt
					['0:00:00', u'8']
	part2_correct_attempt
					['0:00:00', u'5']
	part3_incorrect_attempt
					('0:01:25', u'13!/(7!*6!)')
					('0:03:03', u'12!/(4!*8!)')
					('13:14:55', u'8!/5!')
	part3_correct_attempt
					['13:16:17', u'13!/(8!*5!)']

108 Student ID:edcole

	first_attempt
					2015-10-10 18:40:06
	part1_correct_attempt
					['0:00:00', u'8']
	part2_correct_attempt
					['0:00:00', u'7']
	part3_incorrect_attempt
					('0:00:33', u'15!/7!')
	part3_correct_attempt
					['0:03:21', u'15!/(7!*8!)']

109 Student ID:kquong

	first_attempt
					2015-10-11 03:53:44
	part1_correct_attempt
					['0:00:00', u'9']
	part3_incorrect_attempt
					('0:00:21', u'9!/(6!*(9-6)!)')
	part3_correct_attempt
					['0:01:16', u'15!/(6!*(15-6)!)']

110 Student ID:vasharma

	first_attempt
					2015-10-10 03:54:47
	part1_correct_attempt
					['0:00:00', u'14']
	part2_correct_attempt
					['0:01:17', u'12']
	part3_incorrect_attempt
					('0:02:14', u'C(14,7)')
					('0:07:12', u'14!/[(14-7)!7!]')
	part3_correct_attempt
					['0:19:12', u'26!/[12!(26-12)!]']

111 Student ID:hpc001

	first_attempt
					2015-10-14 21:17:15
	part1_correct_attempt
					['0:00:00', u'9']
	part2_correct_attempt
					['-1 day, 23:51:39', u'6']
	part3_incorrect_attempt
					('0:00:00', u'C(9,6)')
	part3_correct_attempt
					['0:00:09', u'C(15,6)']

112 Student ID:xweng

	first_attempt
					2015-10-12 22:30:46
	part1_correct_attempt
					['0:00:00', u'11']
	part2_correct_attempt
					['0:00:12', u'7']
	part3_incorrect_attempt
					('0:00:33', u'C(11,7)')
	part3_correct_attempt
					['0:00:43', u'C(18,7)']

113 Student ID:ajvanega

	first_attempt
					2015-10-14 18:07:24
	part1_correct_attempt
					['0:00:00', u'12']
	part3_incorrect_attempt
					('0:00:26', u'12!/(3!9!)')
	part3_correct_attempt
					['0:01:14', u'21!/(12!9!)']

114 Student ID:sthapa

	first_attempt
					2015-10-15 04:35:36
	part1_correct_attempt
					['0:00:00', u'14']
	part2_correct_attempt
					['-1 day, 23:59:12', u'12']
	part3_incorrect_attempt
					('0:01:01', u'C(28,12)')
	part3_correct_attempt
					['0:01:20', u'C(26,12)']

115 Student ID:kgrozav

	first_attempt
					2015-10-15 18:38:59
	part1_correct_attempt
					['0:00:00', u'12']
	part2_correct_attempt
					['-1 day, 23:58:09', u'11']
	part3_incorrect_attempt
					('0:00:08', u'12!/11!')
					('0:00:45', u'23!/11!')
					('0:01:11', u'23!/11!12!')
	part3_correct_attempt
					['0:01:22', u'23!/(11!*12!)']

116 Student ID:whcombs

	first_attempt
					2015-10-13 02:34:27
	part1_correct_attempt
					['0:00:00', u'12']
	part2_correct_attempt
					['0:00:00', u'3']
	part3_incorrect_attempt
					('0:00:00', u'C(12,3)')
					('0:04:46', u'12!/(3!(12-3)!)')
	part3_correct_attempt
					['0:09:09', u'455']












