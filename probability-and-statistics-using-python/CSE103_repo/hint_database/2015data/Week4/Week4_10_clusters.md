#Problem 10

    $n = random(13,16,1);
    $x = random(2,9,1);
    $y = random($x+2,13,1);

    *Three cards are drawn sequentially from a deck that contains [$n] cards numbered 1 to [$n] in an arbitrary order. Suppose the first card drawn is a [$x], what is the probability that the three cards form an increasing sequence?*
        Note that unlike the previous question, we are considering a sequence instead of a set of cards, so the order matters. Define the event of interest, A, as the set of all increasing 3-card sequences, i.e. [`` A = \{(x_1,x_2,x_3) | x_1 < x_2 < x_3\} ``], where [`x_1, x_2, x_3 \in \{1, \cdots, [$n]\}`]. Define event [`B`] as the set of 3-card sequence that starts with [$x], i.e. [`` B = \{(x_1,x_2,x_3) | x_1=[$x]\} ``] or simply [`` B = \{([$x],x_2,x_3) \} ``].
        - [`|B| = `] [____________]{Compute("($n-1)*($n-2)")}.
        It follows that [`` A \cap B = \{([$x],x_2,x_3) | [$x] < x_2 < x_3\} ``]. This set can be partitioned into subsets according to [`x_3`], where in each subset [`x_3`] is a constant: [`` A \cap B = \cup_{x_3 = [$x+2]}^{[$n]} \{([$x],x_2,x_3)|[$x] < x_2 < x_3\} ``].
        Let [`S_{x_3=t}`] represent the subset [`\{([$x],x_2,t)|[$x] < x_2 < t\}`], then [`` |A \cap B| = \sum_{t = [$x+2]}^{[$n]} \left|S_{x_3=t}\right| ``].
        - To compute each [`\left|S_{x_3=t}\right|`], let's start with a specific case, say,  [`t=[$y]`],
            [`\left|S_{x_3=[$y]}\right| = \left| \{([$x],x_2,[$y])|[$x] < x_2 < [$y]\} \right| = `] [_____________]{($y-$x-1)}.
        - Generalize this computation, it should be straightforward to compute [`|A \cap B|`] as the sum of [`S_{x_3=t}`] over all valid [`t`].
            [`|A \cap B|=`][_______________]{($n-$x)*($n-$x-1)/2}
        - Now we are ready to compute the conditional probability [`P(A|B) = `] [______________________]{Compute("($n-$x)*($n-$x-1)/2/(($n-1)*($n-2))")}


## Part 1

### (181) Mistake Group Digits of size 181




### (56) Mistake Group ['R.0'] of size 56
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(15-1)*(15-2)	|C(14,2)	|[('R.0', 14.0, u'15-1', u'14')]	|
|1	|(15-1)*(15-2)	|(5+4+3+2+1)	|[('R.0', 14.0, u'15-1', u'5+4+3+2')]	|
|2	|(13-1)*(13-2)	|C(12,2)	|[('R.0', 12.0, u'13-1', u'12')]	|
|3	|(16-1)*(16-2)	|C(15,2)	|[('R.0', 15.0, u'16-1', u'15')]	|
|4	|(14-1)*(14-2)	|C(13,2)	|[('R.0', 13.0, u'14-1', u'13')]	|
|5	|(14-1)*(14-2)	|C(13, 2)	|[('R.0', 13.0, u'14-1', u'13')]	|
|6	|(15-1)*(15-2)	|C(14,3)	|[('R.0', 14.0, u'15-1', u'14')]	|
|7	|(15-1)*(15-2)	|5+4+3+2+1	|[('R.0', 14.0, u'15-1', u'5+4+3+2')]	|
|8	|(13-1)*(13-2)	|C(12, 2)	|[('R.0', 12.0, u'13-1', u'12')]	|
|9	|(13-1)*(13-2)	|12!	|[('R.0', 12.0, u'13-1', u'12')]	|
|10	|(13-1)*(13-2)	|C(13-1,2)	|[('R.0', 12.0, u'13-1', u'13-1')]	|
|11	|(14-1)*(14-2)	|13!	|[('R.0', 13.0, u'14-1', u'13')]	|
|12	|(13-1)*(13-2)	|12*13	|[('R.0', 12.0, u'13-1', u'12')]	|
|13	|(15-1)*(15-2)	|C(14, 2)	|[('R.0', 14.0, u'15-1', u'14')]	|
|14	|(15-1)*(15-2)	|14*12	|[('R.0', 14.0, u'15-1', u'14')]	|
|15	|(14-1)*(14-2)	|C(13, 1) * 2	|[('R.0', 13.0, u'14-1', u'C(13, 1)')]	|




### (50) Mistake Group Fraction of size 50




### (9) Mistake Group ['R.1'] of size 9
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(14-1)*(14-2)	|14*13*12	|[('R.1', 12.0, u'14-2', u'12')]	|
|1	|(15-1)*(15-2)	|15*14*13	|[('R.1', 13.0, u'15-2', u'13')]	|
|2	|(15-1)*(15-2)	|C(14,2)+13	|[('R.1', 13.0, u'15-2', u'13')]	|
|3	|(13-1)*(13-2)	|13*12*11	|[('R.1', 11.0, u'13-2', u'11')]	|
|4	|(13-1)*(13-2)	|1+C(12,1)+C(11,1)	|[('R.1', 11.0, u'13-2', u'C(11,1)')]	|
|5	|(14-1)*(14-2)	|14 * 12	|[('R.1', 12.0, u'14-2', u'12')]	|




### (8) Mistake Group ['R.0.1', 'R.1.1'] of size 8
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1', 'R.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(14-1)*(14-2)	|(16-1)*(16-2)	|[('R.0.1', 1.0, u'1', u'1'), ('R.1.1', 2.0, u'2', u'2')]	|
|1	|(15-1)*(15-2)	|C(15, 1)*C(14, 2)	|[('R.0.1', 1.0, u'1', u'1'), ('R.1.1', 2.0, u'2', u'2')]	|
|2	|(13-1)*(13-2)	|(15-1)*(15-2)	|[('R.0.1', 1.0, u'1', u'1'), ('R.1.1', 2.0, u'2', u'2')]	|
|3	|(15-1)*(15-2)	|(13-1)(13-2)	|[('R.0.1', 1.0, u'1', u'1'), ('R.1.1', 2.0, u'2', u'2')]	|
|4	|(13-1)*(13-2)	|(13-5-1)*(13-5-2)	|[('R.0.1', 1.0, u'1', u'1'), ('R.1.1', 2.0, u'2', u'2')]	|
|5	|(14-1)*(14-2)	|C(4, 1) + C(51, 2)	|[('R.0.1', 1.0, u'1', u'1'), ('R.1.1', 2.0, u'2', u'2')]	|
|6	|(14-1)*(14-2)	|C(4, 1) * C(51, 2)	|[('R.0.1', 1.0, u'1', u'1'), ('R.1.1', 2.0, u'2', u'2')]	|
|7	|(14-1)*(14-2)	|C(4, 1) * C(55, 2)	|[('R.0.1', 1.0, u'1', u'1'), ('R.1.1', 2.0, u'2', u'2')]	|




### (8) Mistake Group ['R.0.1'] of size 8
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(15-1)*(15-2)	|(7+6+5+4+3+2+1)*2	|[('R.0.1', 1.0, u'1', u'1')]	|
|1	|(13-1)*(13-2)	|3! + 2! + 1 + 20	|[('R.0.1', 1.0, u'1', u'1')]	|
|2	|(13-1)*(13-2)	|C(8,1)C(7,1)	|[('R.0.1', 1.0, u'1', u'1')]	|
|3	|(13-1)*(13-2)	|C(4,1)C(6,1)C(4,1)C(5,1)C(4,1)	|[('R.0.1', 1.0, u'1', u'1')]	|
|4	|(13-1)*(13-2)	|C(6,1)C(5,1)	|[('R.0.1', 1.0, u'1', u'1')]	|
|5	|(14-1)*(14-2)	|C(7,1)*C(6,1)	|[('R.0.1', 1.0, u'1', u'1')]	|
|6	|(14-1)*(14-2)	|C(11, 1) + C(10, 1)	|[('R.0.1', 1.0, u'1', u'1')]	|
|7	|(16-1)*(16-2)	|P(13-1,2)	|[('R.0.1', 1.0, u'1', u'1')]	|




### (7) Mistake Group ['R.1.1'] of size 7
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(15-1)*(15-2)	|12(13)/2	|[('R.1.1', 2.0, u'2', u'2')]	|
|1	|(15-1)*(15-2)	|11(12)/2	|[('R.1.1', 2.0, u'2', u'2')]	|
|2	|(13-1)*(13-2)	|3* C(52,2)	|[('R.1.1', 2.0, u'2', u'2')]	|
|3	|(13-1)*(13-2)	|4* C(52,2)	|[('R.1.1', 2.0, u'2', u'2')]	|
|4	|(13-1)*(13-2)	|10!/(8!2!)	|[('R.1.1', 2.0, u'2', u'2!')]	|
|5	|(15-1)*(15-2)	|3*C(14,2)	|[('R.1.1', 2.0, u'2', u'2')]	|
|6	|(15-1)*(15-2)	|C(15,3) - C(14,2)	|[('R.1.1', 2.0, u'2', u'2')]	|




### (3) Mistake Group Wrong_Sign of size 3




### (2) Mistake Group ['R.0', 'R.1'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(14-1)*(14-2)	|C(13, 1) + C(12, 1)	|[('R.0', 13.0, u'14-1', u'C(13, 1)'), ('R.1', 12.0, u'14-2', u'C(12, 1)')]	|




### (1) Mistake Group ['R.1.0', 'R.1.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.0', 'R.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(13-1)*(13-2)	|1* C(13,2)	|[('R.1.0', 13.0, u'13', u'13'), ('R.1.1', 2.0, u'2', u'2')]	|




### (104) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:aggouw

	first_attempt
					2015-10-21 08:53:56
	part1_incorrect_attempt
					('0:00:00', u'P(15,2)')
	part1_correct_attempt
					['0:01:41', u'P(13,2)']

1 Student ID:srl006

	first_attempt
					2015-10-23 00:39:40
	part1_incorrect_attempt
					('0:00:00', u'14 * 11')
					('0:00:05', u'14 * 10')
					('0:00:10', u'14 * 9')
					('0:00:15', u'14 * 8')
					('0:00:19', u'14 * 7')
					('0:00:23', u'14 * 6')
					('0:00:29', u'14 * 5')
					('0:00:33', u'14 * 4')
					('0:00:46', u'14 * 14')
					('0:00:50', u'14 * 15')
					('0:00:54', u'14 * 16')
					('0:00:59', u'14 * 17')
					('0:01:04', u'14 * 18')
					('0:01:12', u'14 * 3')
					('0:01:17', u'14 * 4')
					('0:01:22', u'14 ')
					('0:02:30', u'14 * 13')
	part1_correct_attempt
					['0:03:54', u'12 * 13']

2 Student ID:jguanzho

	first_attempt
					2015-10-18 21:38:56
	part1_incorrect_attempt
					('0:00:00', u'8*7')
					('0:02:28', u'8!*7!')
					('0:03:11', u'7+6+5+4+3+2+1')
					('0:04:35', u'8+7+6+5+4+3+2+1')
					('0:05:00', u'8!/2!')
					('0:05:04', u'8!')
					('0:06:38', u'(12!/(2!*10!))')
					('0:07:24', u'(13!/(2!*10!)) - 13')
	part1_correct_attempt
					['0:44:26', u'12*11']

3 Student ID:alakamsa

	first_attempt
					2015-10-18 00:04:36
	part1_incorrect_attempt
					('0:00:00', u'P(11,2)')
	part1_correct_attempt
					['0:00:21', u'P(14,2)']

4 Student ID:dcgriffi

	first_attempt
					2015-10-21 02:17:37
	part1_incorrect_attempt
					('0:00:00', u'7!')
					('0:00:46', u'7+6+5+4+3+2+1')
					('0:00:00', u'16*16')
	part1_correct_attempt
					['2:11:23', u'15*14']

5 Student ID:jjm019

	first_attempt
					2015-10-22 10:04:22
	part1_incorrect_attempt
					('0:00:00', u'10*9')
	part1_correct_attempt
					['0:11:04', u'12*11']

6 Student ID:mhale

	first_attempt
					2015-10-21 07:25:02
	part1_incorrect_attempt
					('0:00:00', u'4 + 3 + 2 + 1')
					('0:00:37', u'4!')
					('0:00:48', u'5!')
					('0:01:08', u'5 * 4')
					('0:01:29', u'4 * 3')
					('0:01:54', u'3! + 2! + 1')
	part1_correct_attempt
					['0:06:39', u'12 * 11']

7 Student ID:dkurli

	first_attempt
					2015-10-21 04:19:57
	part1_incorrect_attempt
					('0:00:00', u'C(8,2)')
					('0:00:39', u'C(7,2)')
	part1_correct_attempt
					['0:02:14', u'P(15,2)']

8 Student ID:j5phung

	first_attempt
					2015-10-17 00:42:22
	part1_incorrect_attempt
					('0:00:00', u'C(8,2)')
					('0:00:36', u'C(6,2)')
					('0:00:49', u'6*5')
					('0:02:08', u'6*5+6*4+6*3+6*2+6*1')
					('0:02:52', u'6(5+4+3+2+1)')
					('0:03:11', u'6(5!)')
					('0:03:17', u'6!')
					('0:03:28', u'P(6,2)')
					('0:11:07', u'5(5+4+3+2+1)')
					('0:16:19', u'5(6+5+4+3+2+1)')
					('0:16:26', u'6(6+5+4+3+2+1)')
					('0:19:38', u'15*5')
	part1_correct_attempt
					['2 days, 4:13:42', u'14*13']

9 Student ID:jyc018

	first_attempt
					2015-10-22 22:57:44
	part1_incorrect_attempt
					('0:00:00', u'13*12')
					('0:00:22', u'12*11')
					('0:00:00', u'12+11+10+9+8+7+6+5+4+3+2+1')
	part1_correct_attempt
					['0:39:09', u'C(15,2) * 2']

10 Student ID:rlhagen

	first_attempt
					2015-10-18 20:07:12
	part1_incorrect_attempt
					('0:00:00', u'9!')
					('0:00:18', u'9+8+7+6+5+4+3+2+1')
					('0:27:26', u'10*10')
					('0:28:20', u'10*9')
					('0:29:34', u'C(10,2)')
					('0:31:38', u'P(10,2)')
					('0:32:16', u'P(14,2)')
					('0:32:33', u'14^2')
	part1_correct_attempt
					['0:32:43', u'13*12']

11 Student ID:avasavad

	first_attempt
					2015-10-22 19:25:52
	part1_incorrect_attempt
					('0:00:00', u'C(9,2)')
					('0:01:04', u'C(13,2)')
	part1_correct_attempt
					['0:01:26', u'14 * 13']

12 Student ID:btn023

	first_attempt
					2015-10-21 18:06:21
	part1_incorrect_attempt
					('0:00:00', u'8*7')
	part1_correct_attempt
					['0:04:47', u'12*11']

13 Student ID:dgunawan

	first_attempt
					2015-10-23 00:44:42
	part1_incorrect_attempt
					('0:00:00', u'C(55, 2)')
	part1_correct_attempt
					['0:08:14', u'13* 12']

14 Student ID:tcuddy

	first_attempt
					2015-10-17 22:31:32
	part1_incorrect_attempt
					('0:00:00', u'13*12*11')
	part1_correct_attempt
					['0:00:12', u'12*13']

15 Student ID:l8ngo

	first_attempt
					2015-10-22 02:02:07
	part1_incorrect_attempt
					('0:00:00', u'4*9*8')
					('0:00:11', u'9*8')
	part1_correct_attempt
					['0:03:58', u'12*11']

16 Student ID:djk006

	first_attempt
					2015-10-21 18:30:42
	part1_incorrect_attempt
					('0:00:00', u'12!/(2!10!)')
	part1_correct_attempt
					['0:02:20', u'12!/(10!)']

17 Student ID:dsriniva

	first_attempt
					2015-10-22 17:37:17
	part1_incorrect_attempt
					('0:00:00', u'P(7, 2)')
	part1_correct_attempt
					['0:00:29', u'P(15, 2)']

18 Student ID:glcohen

	first_attempt
					2015-10-18 01:15:48
	part1_incorrect_attempt
					('0:00:00', u'C(13,2)')
	part1_correct_attempt
					['0:01:07', u'14*13']

19 Student ID:achava

	first_attempt
					2015-10-21 17:23:27
	part1_incorrect_attempt
					('0:00:00', u'6!+1')
					('0:00:06', u'6!')
					('0:03:09', u'6!')
					('0:03:46', u'C(6,2)')
	part1_correct_attempt
					['4:20:29', u'14*13']

20 Student ID:arc013

	first_attempt
					2015-10-21 10:31:08
	part1_incorrect_attempt
					('0:00:00', u'C(10, 2)')
					('0:00:21', u'10*9')
	part1_correct_attempt
					['0:01:54', u'13*12']

21 Student ID:mitopete

	first_attempt
					2015-10-21 23:41:59
	part1_incorrect_attempt
					('0:00:00', u'P(9,2)')
					('0:00:00', u'P(15,2)')
	part1_correct_attempt
					['1:59:03', u'P(14,2)']

22 Student ID:yos017

	first_attempt
					2015-10-21 09:33:38
	part1_incorrect_attempt
					('0:00:00', u'13^2')
	part1_correct_attempt
					['0:01:52', u'12*11']

23 Student ID:h4tu

	first_attempt
					2015-10-22 17:37:10
	part1_incorrect_attempt
					('0:00:00', u'5*11')
					('0:00:00', u'5*11-10')
	part1_correct_attempt
					['0:02:58', u'13*12']

24 Student ID:jag028

	first_attempt
					2015-10-22 17:12:21
	part1_incorrect_attempt
					('0:00:00', u'13*12')
	part1_correct_attempt
					['0:01:40', u'14*13']

25 Student ID:lguintu

	first_attempt
					2015-10-16 07:07:48
	part1_incorrect_attempt
					('0:00:00', u'C(6,3)')
					('0:00:29', u'C(8,6)')
					('0:01:03', u'C(8,7)')
					('0:01:23', u'C(7,2)')
					('0:01:54', u'7+6+5+4+3+2+1')
					('0:03:38', u'P(8,2)')
					('0:04:03', u'P(7,2)')
					('0:04:57', u'P(8,2)')
					('0:05:13', u'7+6+5+4+3+2')
	part1_correct_attempt
					['0:08:21', u'P(14,2)']

26 Student ID:jjchung

	first_attempt
					2015-10-21 02:54:26
	part1_incorrect_attempt
					('0:00:00', u'P(35,2)')
	part1_correct_attempt
					['0:00:06', u'P(13,2)']

27 Student ID:abjara

	first_attempt
					2015-10-21 22:27:00
	part1_incorrect_attempt
					('0:00:00', u'C(16,7)')
					('0:00:00', u'C(16,7)/C(16,1)')
					('0:00:31', u'C(7,2)')
	part1_correct_attempt
					['0:05:06', u'C(15,1)*C(14,1)']

28 Student ID:krau

	first_attempt
					2015-10-21 04:22:16
	part1_incorrect_attempt
					('0:00:00', u'11*10')
	part1_correct_attempt
					['0:00:19', u'P(12,2)']

29 Student ID:kthui

	first_attempt
					2015-10-18 09:31:28
	part1_incorrect_attempt
					('0:00:00', u'12!')
					('0:00:29', u'12+11+10+9+8+7+6+5+4+3+2+1')
					('0:00:57', u'11+10+9+8+7+6+5+4+3+2+1')
					('0:02:05', u'12+11+10+9+8+7+6+5+4+3+2+1')
					('0:03:03', u'12*11/2')
					('0:03:08', u'12*11')
					('0:03:13', u'12*11*2')
	part1_correct_attempt
					['0:03:40', u'14*13']

30 Student ID:alhung

	first_attempt
					2015-10-22 19:24:00
	part1_incorrect_attempt
					('0:00:00', u'12*11')
	part1_correct_attempt
					['0:00:15', u'13*12']

31 Student ID:beyounge

	first_attempt
					2015-10-17 06:36:04
	part1_incorrect_attempt
					('0:00:00', u'C(11,2)')
	part1_correct_attempt
					['0:00:43', u'P(15,2)']

32 Student ID:b3hwang

	first_attempt
					2015-10-21 03:35:16
	part1_incorrect_attempt
					('0:00:00', u'1 * 13 * 13')
					('0:00:18', u'4 * 13 * 13')
					('0:02:41', u'4 * 4* 13 * 4*  13')
	part1_correct_attempt
					['0:08:28', u'1 * 12 * 11']

33 Student ID:tpmach

	first_attempt
					2015-10-21 22:20:27
	part1_incorrect_attempt
					('0:00:00', u'13*12')
					('0:01:38', u'P(13,2)')
					('0:01:56', u'C(13,2)')
					('0:00:00', u'P(13,2)')
					('0:00:00', u'C(13,2)')
					('0:00:00', u'13*12')
	part1_correct_attempt
					['4:48:47', u'15*14']

34 Student ID:dsmonaha

	first_attempt
					2015-10-21 20:05:33
	part1_incorrect_attempt
					('0:00:00', u'C(6,2)')
					('0:00:06', u'C(7,2)')
					('0:00:35', u'P(7,2)')
	part1_correct_attempt
					['4:06:38', u'C(12,1)C(11,1)']

35 Student ID:jel075

	first_attempt
					2015-10-21 23:31:03
	part1_incorrect_attempt
					('0:00:00', u'8+C(8,1)+C(7,1)+C(6,1)+C(5,1)+C(4,1)+C(3,1)+C(2,1)')
					('0:00:00', u'8+C(8,1)+C(7,1)+C(6,1)+C(5,1)+C(4,1)+C(3,1)+C(2,1)+C(1,1)')
					('0:00:16', u'C(8,1)+C(7,1)+C(6,1)+C(5,1)+C(4,1)+C(3,1)+C(2,1)+C(1,1)')
					('0:00:00', u'8!')
					('0:00:08', u'8+7+6+5+4+3+2+1')
	part1_correct_attempt
					['0:12:19', u'P(15,2)']

36 Student ID:edescobe

	first_attempt
					2015-10-18 11:46:59
	part1_incorrect_attempt
					('0:00:00', u'9+8+7+6+5+4+3+2+1')
					('0:06:06', u'9+8+7+6+5+4+3+2+1')
					('0:08:22', u'C(10,2)')
	part1_correct_attempt
					['0:09:20', u'210']

37 Student ID:bakang

	first_attempt
					2015-10-22 07:44:29
	part1_incorrect_attempt
					('0:00:00', u'C(8,2)+C(6,2)+8*6')
	part1_correct_attempt
					['0:02:24', u'14*13']

38 Student ID:muy002

	first_attempt
					2015-10-22 21:25:56
	part1_incorrect_attempt
					('0:00:00', u'C(9,2)')
					('0:02:12', u'14*13')
	part1_correct_attempt
					['0:02:24', u'13*12']

39 Student ID:jtfrankl

	first_attempt
					2015-10-21 00:27:04
	part1_incorrect_attempt
					('0:00:00', u'4+3+2+1')
	part1_correct_attempt
					['0:00:29', u'12*11']

40 Student ID:cstringh

	first_attempt
					2015-10-22 00:37:17
	part1_incorrect_attempt
					('0:00:00', u'12*11*10')
	part1_correct_attempt
					['0:24:29', u'12 * 11']

41 Student ID:rbdoming

	first_attempt
					2015-10-18 01:45:23
	part1_incorrect_attempt
					('0:00:00', u'C(13,10)')
					('0:01:24', u'10+9+8+7+6+5+4+3+2+1')
					('0:01:52', u'C(10,2)')
					('0:05:51', u'9+8+7+6+5+4+3+2+1')
					('0:06:18', u'C(10,2)')
					('0:00:00', u'C(9,2)')
					('0:00:14', u'C(10,2)')
	part1_correct_attempt
					['3 days, 3:14:48', u'12*11']

42 Student ID:qfu

	first_attempt
					2015-10-16 03:26:10
	part1_incorrect_attempt
					('0:00:00', u'11*5')
	part1_correct_attempt
					['0:03:56', u'12*11']

43 Student ID:hsc052

	first_attempt
					2015-10-22 06:23:05
	part1_incorrect_attempt
					('0:00:00', u'C(11,2)')
	part1_correct_attempt
					['0:02:07', u'P(13,2)']

44 Student ID:dac064

	first_attempt
					2015-10-22 21:08:08
	part1_incorrect_attempt
					('0:00:00', u'7+6+5+4+3+2+1')
	part1_correct_attempt
					['0:02:41', u'15*14']

45 Student ID:yil035

	first_attempt
					2015-10-21 00:10:35
	part1_incorrect_attempt
					('0:00:00', u'8+7+6+5+4+3+2+1')
	part1_correct_attempt
					['0:01:31', u'12*11']

46 Student ID:sghouse

	first_attempt
					2015-10-21 03:08:51
	part1_incorrect_attempt
					('0:00:00', u'10!')
					('0:00:00', u'C(10, 3)')
					('0:00:23', u'C(11, 3)')
					('0:00:47', u'C(10,2)')
					('0:01:02', u'C(11,2)')
	part1_correct_attempt
					['20:23:59', u'(14*13)']

47 Student ID:k3tan

	first_attempt
					2015-10-22 21:52:07
	part1_incorrect_attempt
					('0:00:00', u'12*11')
	part1_correct_attempt
					['0:20:01', u'15*14']

48 Student ID:haw081

	first_attempt
					2015-10-22 06:04:54
	part1_incorrect_attempt
					('0:00:00', u'C(13-1,2)-C(4,2)')
					('0:00:33', u'C(13,2)-C(13-1,2)')
	part1_correct_attempt
					['0:04:02', u'P(13-1,2)']

49 Student ID:ctroncos

	first_attempt
					2015-10-22 17:13:05
	part1_incorrect_attempt
					('0:00:00', u'(15) * (15-1)')
	part1_correct_attempt
					['0:00:09', u'(15 -2) * (15-1)']

50 Student ID:lywong

	first_attempt
					2015-10-21 07:57:11
	part1_incorrect_attempt
					('0:00:00', u'C(15,3)')
	part1_correct_attempt
					['15:35:00', u'(14)(13)']

51 Student ID:kebao

	first_attempt
					2015-10-22 03:08:42
	part1_incorrect_attempt
					('0:00:00', u'13*12')
	part1_correct_attempt
					['0:01:12', u'11*12']

52 Student ID:hkhodada

	first_attempt
					2015-10-21 02:18:40
	part1_incorrect_attempt
					('0:00:00', u'14*13')
	part1_correct_attempt
					['0:02:08', u'13*12']

53 Student ID:nisharma

	first_attempt
					2015-10-22 15:00:34
	part1_incorrect_attempt
					('0:00:00', u'14*13')
	part1_correct_attempt
					['0:00:34', u'12*11']

54 Student ID:abasu

	first_attempt
					2015-10-21 00:05:03
	part1_incorrect_attempt
					('0:00:00', u'6 * 5')
					('0:00:22', u'10 * 9')
					('0:01:03', u'9! 8!')
					('0:01:10', u'9!')
					('0:01:23', u'C(10,2)')
	part1_correct_attempt
					['0:01:51', u'13*12']

55 Student ID:acvuong

	first_attempt
					2015-10-20 16:39:32
	part1_incorrect_attempt
					('0:00:00', u'C(8,2)')
					('0:14:34', u'C(14,3)')
	part1_correct_attempt
					['23:21:51', u'13*12']

56 Student ID:d6he

	first_attempt
					2015-10-22 22:17:06
	part1_incorrect_attempt
					('0:00:00', u'13*12')
	part1_correct_attempt
					['0:00:58', u'15*14']

57 Student ID:sachadal

	first_attempt
					2015-10-22 17:15:53
	part1_incorrect_attempt
					('0:00:00', u'8*7')
	part1_correct_attempt
					['0:10:53', u'13*12']

58 Student ID:awollner

	first_attempt
					2015-10-21 18:15:12
	part1_incorrect_attempt
					('0:00:00', u'3+2+1')
	part1_correct_attempt
					['0:02:06', u'12!/10!']

59 Student ID:dcrume

	first_attempt
					2015-10-21 20:10:03
	part1_incorrect_attempt
					('0:00:00', u'16*15')
	part1_correct_attempt
					['20:57:41', u'15*14']

60 Student ID:mrchin

	first_attempt
					2015-10-22 18:49:55
	part1_incorrect_attempt
					('0:00:00', u'15*14')
	part1_correct_attempt
					['0:00:32', u'12*11']

61 Student ID:mbl003

	first_attempt
					2015-10-21 20:07:05
	part1_incorrect_attempt
					('0:00:00', u'6+7+8+9+10+11+12+13+14+15+16')
					('0:02:55', u'9+8+7+6+5+4+3+2+1')
					('0:00:00', u'16*15')
	part1_correct_attempt
					['0:08:30', u'15*14']

62 Student ID:n2patil

	first_attempt
					2015-10-21 22:40:17
	part1_incorrect_attempt
					('0:00:00', u'C(10,2)')
					('0:00:06', u'P(10,2)')
					('0:35:46', u'14*13')
					('0:36:13', u'13*12')
	part1_correct_attempt
					['0:36:57', u'12*11']

63 Student ID:jblynch

	first_attempt
					2015-10-21 05:54:49
	part1_incorrect_attempt
					('0:00:00', u'4(10+9+8+7+6+5+4+3+2+1)')
					('0:00:18', u'10+9+8+7+6+5+4+3+2+1')
	part1_correct_attempt
					['0:27:25', u'13*12']

64 Student ID:nnh002

	first_attempt
					2015-10-22 04:43:58
	part1_incorrect_attempt
					('0:00:00', u'10+9+8+7+6+5+4+3+2+1')
	part1_correct_attempt
					['0:01:42', u'14*13']

65 Student ID:akhmelni

	first_attempt
					2015-10-22 22:34:40
	part1_incorrect_attempt
					('0:00:00', u'14*13')
					('0:00:16', u'15*14')
	part1_correct_attempt
					['0:00:37', u'13*12']

66 Student ID:tol003

	first_attempt
					2015-10-21 00:48:47
	part1_incorrect_attempt
					('0:00:00', u'C(13,2)-C(11,2)')
	part1_correct_attempt
					['0:03:15', u'13*12']

67 Student ID:skodigal

	first_attempt
					2015-10-22 01:36:13
	part1_incorrect_attempt
					('0:00:00', u'14*13')
	part1_correct_attempt
					['0:00:51', u'12*11']

68 Student ID:hachrist

	first_attempt
					2015-10-21 22:27:01
	part1_incorrect_attempt
					('0:00:00', u'C(14,3) - C(12,3)')
					('0:00:00', u'C(12,3)')
					('0:00:00', u'C(14,3)')
					('0:00:00', u'C(14,3)')
	part1_correct_attempt
					['8:02:28', u'13*12']

69 Student ID:kew017

	first_attempt
					2015-10-22 20:51:13
	part1_incorrect_attempt
					('0:00:00', u'C(11,2)')
					('0:00:23', u'P(11,2)')
	part1_correct_attempt
					['0:01:40', u'P(14,2)']

70 Student ID:arvenega

	first_attempt
					2015-10-22 21:50:56
	part1_incorrect_attempt
					('0:00:00', u'P(14,2)')
					('0:00:00', u'P(16,3)')
	part1_correct_attempt
					['0:13:38', u'15*14']

71 Student ID:csl030

	first_attempt
					2015-10-22 04:31:31
	part1_incorrect_attempt
					('0:00:00', u'14 * 14')
					('0:09:01', u'14*13')
	part1_correct_attempt
					['0:09:10', u'12*13']

72 Student ID:yhhan

	first_attempt
					2015-10-22 23:27:46
	part1_incorrect_attempt
					('0:00:00', u'8*7')
					('0:00:42', u'8+7+6+5+4+3+2+1')
					('0:00:48', u'8+7+6+5+4+3+2')
					('0:02:32', u'C(9,2)')
					('0:03:17', u'9*8')
					('0:03:23', u'8*7')
	part1_correct_attempt
					['0:03:37', u'15*14']

73 Student ID:atorr

	first_attempt
					2015-10-22 23:00:51
	part1_incorrect_attempt
					('0:00:00', u'1* 10 * 9')
					('0:00:24', u'1* 9 * 8')
					('0:00:40', u'1 * 9 * 9')
	part1_correct_attempt
					['0:01:22', u'1 * 13 * 12']

74 Student ID:cagatep

	first_attempt
					2015-10-22 21:36:28
	part1_incorrect_attempt
					('0:00:00', u'C(11, 2)')
	part1_correct_attempt
					['0:03:10', u'13*12']

75 Student ID:tjke

	first_attempt
					2015-10-18 04:47:11
	part1_incorrect_attempt
					('0:00:00', u'P(11,2)')
					('0:00:34', u'C(11,2)')
					('0:01:41', u'P(11,2)')
	part1_correct_attempt
					['0:02:47', u'P(12,2)']

76 Student ID:any027

	first_attempt
					2015-10-19 20:49:33
	part1_incorrect_attempt
					('0:00:00', u'P(12,2)')
	part1_correct_attempt
					['0:01:24', u'P(15,2)']

77 Student ID:t2shin

	first_attempt
					2015-10-22 23:39:58
	part1_incorrect_attempt
					('0:00:00', u'7*6')
					('0:01:43', u'6+5+4+3+2+1')
					('0:01:49', u'6+5+4+3+2')
	part1_correct_attempt
					['0:02:05', u'14*13']

78 Student ID:vsamant

	first_attempt
					2015-10-21 19:33:28
	part1_incorrect_attempt
					('0:00:00', u'11*10*9')
					('0:01:03', u'12*11*9')
					('0:01:10', u'12*11*10')
	part1_correct_attempt
					['0:01:36', u'12*11']

79 Student ID:spw006

	first_attempt
					2015-10-20 21:48:57
	part1_incorrect_attempt
					('0:00:00', u'6+5+4+3+2+1')
					('0:01:44', u'13*13')
	part1_correct_attempt
					['0:01:56', u'12*11']

80 Student ID:masaro

	first_attempt
					2015-10-20 17:41:57
	part1_incorrect_attempt
					('0:00:00', u'12*11')
	part1_correct_attempt
					['3:20:17', u'156']

81 Student ID:jdeon

	first_attempt
					2015-10-22 05:08:10
	part1_incorrect_attempt
					('0:00:00', u'8+7+6+5+4+3+2+1')
					('0:00:50', u'9+8+7+6+5+4+3+2+1')
	part1_correct_attempt
					['0:07:03', u'15*14']

82 Student ID:s2chaudh

	first_attempt
					2015-10-22 03:08:10
	part1_incorrect_attempt
					('0:00:00', u'C(13,2)')
					('0:00:00', u'16*15')
	part1_correct_attempt
					['0:01:23', u'15*14']

83 Student ID:j6quach

	first_attempt
					2015-10-22 18:34:02
	part1_incorrect_attempt
					('0:00:00', u'11*10')
	part1_correct_attempt
					['0:00:29', u'14*13']

84 Student ID:gsrandha

	first_attempt
					2015-10-16 01:55:18
	part1_incorrect_attempt
					('0:00:00', u'1*13*12')
	part1_correct_attempt
					['2 days, 22:07:23', u'12*11']

85 Student ID:jhc010

	first_attempt
					2015-10-22 08:34:43
	part1_incorrect_attempt
					('0:00:00', u'6*5')
					('0:01:06', u'C(6,2)')
					('0:01:34', u'P(6,2)')
					('0:03:41', u'6*5')
	part1_correct_attempt
					['0:04:23', u'12*11']

86 Student ID:rsmurlo

	first_attempt
					2015-10-21 23:31:31
	part1_incorrect_attempt
					('0:00:00', u'C(10,2)')
					('0:00:00', u'9+8+7+6+5+4+3+2+1')
	part1_correct_attempt
					['0:04:45', u'C(12,2)*2']

87 Student ID:dkostins

	first_attempt
					2015-10-22 00:37:38
	part1_incorrect_attempt
					('0:00:00', u'14*13')
	part1_correct_attempt
					['0:00:55', u'13*12']

88 Student ID:agarango

	first_attempt
					2015-10-22 19:32:55
	part1_incorrect_attempt
					('0:00:00', u'13!')
					('0:04:44', u'8*7')
					('0:04:53', u'5*8*7')
	part1_correct_attempt
					['0:06:40', u'12*11']

89 Student ID:c1sorian

	first_attempt
					2015-10-21 21:56:05
	part1_incorrect_attempt
					('0:00:00', u'C(12,2)-C(6,2)')
					('0:00:59', u'C(13,3)')
					('0:13:07', u'C(13,3)-C(12,3)')
	part1_correct_attempt
					['0:17:21', u'12*11']

90 Student ID:twsalim

	first_attempt
					2015-10-20 18:32:12
	part1_incorrect_attempt
					('0:00:00', u'C(14 - 5, 2)')
					('0:00:20', u'C(9, 2)')
	part1_correct_attempt
					['0:01:57', u'P(13, 2)']

91 Student ID:msaguiar

	first_attempt
					2015-10-22 03:38:20
	part1_incorrect_attempt
					('0:00:00', u'6*5')
	part1_correct_attempt
					['0:04:39', u'14*13']

92 Student ID:k5law

	first_attempt
					2015-10-19 08:00:39
	part1_incorrect_attempt
					('0:00:00', u'11+10+9+8+7+8+7+6+5+4+3')
					('0:06:14', u'(12*14)+(11*14)+(10*14)+(9*14)+(8*14)+(7*14)+(6*14)+(5*14)+(4*14)+(3*14)+(2*14)+(1*14)')
					('0:06:28', u'(12*14)+(11*14)+(10*14)+(9*14)+(8*14)+(7*14)+(6*14)+(5*14)+(4*14)+(3*14)+(2*14)')
					('0:06:34', u'(12*14)+(11*14)+(10*14)+(9*14)+(8*14)+(7*14)+(6*14)+(5*14)+(4*14)+(3*14)')
					('12:07:37', u'12*11')
					('12:12:39', u'11+10+9+8+7+8+7+6+5+4+3')
					('12:13:07', u'11+10+9+8+7+8+7+6+5+4+3+2+1')
					('12:13:34', u'13+12+11+10+9+8+7+8+7+6+5+4+3+2+1')
					('12:13:45', u'12+11+10+9+8+7+8+7+6+5+4+3+2+1')
	part1_correct_attempt
					['12:22:09', u'13!/(11!)']

93 Student ID:ajabasa

	first_attempt
					2015-10-22 06:45:22
	part1_incorrect_attempt
					('0:00:00', u'15!/12!')
	part1_correct_attempt
					['0:01:06', u'13*14']

94 Student ID:jnn015

	first_attempt
					2015-10-22 23:31:17
	part1_incorrect_attempt
					('0:00:00', u'6*5 + 5*4 + 4*3 + 3*2 + 2')
					('0:01:00', u'5 + 4 + 3 + 2 + 1')
	part1_correct_attempt
					['0:12:54', u'P(13, 2)']

95 Student ID:edcole

	first_attempt
					2015-10-21 18:13:58
	part1_incorrect_attempt
					('0:00:00', u'C(12, 2) + 1')
					('0:00:00', u'C(11, 2)')
	part1_correct_attempt
					['0:02:54', u'12*11']

96 Student ID:aordookh

	first_attempt
					2015-10-22 06:20:25
	part1_incorrect_attempt
					('0:00:00', u'C(6,2)')
	part1_correct_attempt
					['0:02:17', u'13*12']

97 Student ID:kquong

	first_attempt
					2015-10-18 05:32:37
	part1_incorrect_attempt
					('0:00:00', u'8 * 7 * 6')
					('0:05:56', u'7 + 6 + 5 + 4 + 3+ 2+ 1')
	part1_correct_attempt
					['0:09:58', u'15*14']

98 Student ID:vasharma

	first_attempt
					2015-10-21 23:28:59
	part1_incorrect_attempt
					('0:00:00', u'9*8')
	part1_correct_attempt
					['0:00:31', u'13*12']

99 Student ID:syip

	first_attempt
					2015-10-18 22:27:02
	part1_incorrect_attempt
					('0:00:00', u'9*8')
	part1_correct_attempt
					['0:00:33', u'14*13']

100 Student ID:yypan

	first_attempt
					2015-10-22 00:20:56
	part1_incorrect_attempt
					('0:00:00', u'7*6')
					('0:02:49', u'7*7')
	part1_correct_attempt
					['0:03:18', u'14*13']

101 Student ID:ajvanega

	first_attempt
					2015-10-22 17:21:17
	part1_incorrect_attempt
					('0:00:00', u'3!')
					('0:01:44', u'P(14,2)')
	part1_correct_attempt
					['0:01:53', u'P(15,2)']

102 Student ID:zhw110

	first_attempt
					2015-10-22 17:14:45
	part1_incorrect_attempt
					('0:00:00', u'6*13')
	part1_correct_attempt
					['0:10:22', u'13*12']

103 Student ID:mtrafeca

	first_attempt
					2015-10-21 07:57:40
	part1_incorrect_attempt
					('0:00:00', u'1+2+3+4+5+6+7+8+9+10+11+12+13+14+15')
					('0:14:38', u'7+8+9+10+11+12+13+14+15')
					('0:14:45', u'8+9+10+11+12+13+14+15')
					('0:15:28', u'C(8,3)')
					('0:15:34', u'C(9,3)')
					('0:15:42', u'C(7,3)')
					('0:15:52', u'C(7,2)')
					('0:19:28', u'7+8+9')
					('0:20:26', u'15!/7!')
					('0:20:33', u'15!/8!')
					('0:20:45', u'15!/6!')
					('0:26:57', u'C(8,2)')
					('0:27:10', u'C(8,2)+7')
	part1_correct_attempt
					['1 day, 13:04:46', u'14*13']












## Part 2

### (123) Mistake Group Digits of size 123




### (8) Mistake Group Fraction of size 8




### (4) Mistake Group Wrong_Sign of size 4




### (23) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:dlgoldbe

	first_attempt
					2015-10-22 17:46:42
	part2_incorrect_attempt
					('1:55:48', u'C(11,1)')
					('2:00:05', u'3+4+5+6+7+8+9+10+11+12')
	part2_correct_attempt
					['2:03:28', u'10']

1 Student ID:haw081

	first_attempt
					2015-10-22 06:08:56
	part2_incorrect_attempt
					('0:02:51', u'P(13-2,1)')
	part2_correct_attempt
					['0:03:02', u'3']

2 Student ID:ctroncos

	first_attempt
					2015-10-22 17:13:14
	part2_incorrect_attempt
					('0:01:48', u'12 - 9')
	part2_correct_attempt
					['0:01:53', u'12 - 9 -1']

3 Student ID:kebao

	first_attempt
					2015-10-22 03:09:54
	part2_incorrect_attempt
					('16:05:05', u'10*9')
					('16:05:18', u'9*8')
	part2_correct_attempt
					['17:55:38', u'9']

4 Student ID:kbielawi

	first_attempt
					2015-10-21 20:38:54
	part2_incorrect_attempt
					('0:00:37', u'15-2')
	part2_correct_attempt
					['0:00:48', u'6']

5 Student ID:tol003

	first_attempt
					2015-10-21 00:52:02
	part2_incorrect_attempt
					('0:02:38', u'11*10')
	part2_correct_attempt
					['0:08:08', u'2']

6 Student ID:jjchung

	first_attempt
					2015-10-21 02:54:32
	part2_incorrect_attempt
					('3:10:49', u'(14-8)*(14-8-1)/2')
	part2_correct_attempt
					['3:11:07', u'2']

7 Student ID:abjara

	first_attempt
					2015-10-21 22:32:06
	part2_incorrect_attempt
					('0:08:39', u'C(14,1)')
	part2_correct_attempt
					['0:11:55', u'1']

8 Student ID:spw006

	first_attempt
					2015-10-20 21:50:53
	part2_incorrect_attempt
					('-1 day, 23:59:32', u'6+5+4+3+2+1')
	part2_correct_attempt
					['0:00:13', u'5']

9 Student ID:skarimik

	first_attempt
					2015-10-18 03:41:26
	part2_incorrect_attempt
					('0:00:00', u'12+13+14')
					('0:04:54', u'9+10+11')
	part2_correct_attempt
					['0:12:37', u'3']

10 Student ID:thk002

	first_attempt
					2015-10-21 01:54:05
	part2_incorrect_attempt
					('2:39:17', u'C(12,5)')
					('2:39:24', u'C(12,1)')
					('2:39:38', u'C(12,1)-1')
	part2_correct_attempt
					['2:42:12', u'5']

11 Student ID:dcrume

	first_attempt
					2015-10-22 17:07:44
	part2_incorrect_attempt
					('0:04:49', u'9+10+11+12+13+14+15+16')

12 Student ID:k5law

	first_attempt
					2015-10-19 20:22:48
	part2_incorrect_attempt
					('-1 day, 11:27:35', u'5+6+7+8+9+10+11')
	part2_correct_attempt
					['-1 day, 11:27:45', u'5']

13 Student ID:mbl003

	first_attempt
					2015-10-21 20:15:35
	part2_incorrect_attempt
					('-1 day, 23:59:13', u'9+8+7+6+5+4+3+2+1')
	part2_correct_attempt
					['0:00:42', u'3']

14 Student ID:jyc018

	first_attempt
					2015-10-22 23:36:53
	part2_incorrect_attempt
					('0:00:49', u'12+11+10+9+8+7+6+5+4+3+2+1')
	part2_correct_attempt
					['0:04:52', u'9']

15 Student ID:ffhaddad

	first_attempt
					2015-10-22 20:45:37
	part2_incorrect_attempt
					('0:01:57', u'7-4')
	part2_correct_attempt
					['0:09:27', u'1']

16 Student ID:dis003

	first_attempt
					2015-10-22 17:42:09
	part2_incorrect_attempt
					('-1 day, 23:58:27', u'9-6-1')
	part2_correct_attempt
					['0:00:00', u'13-5-1']

17 Student ID:kalang

	first_attempt
					2015-10-22 21:06:06
	part2_incorrect_attempt
					('0:01:25', u'2*4')
	part2_correct_attempt
					['0:03:06', u'3']

18 Student ID:dtea

	first_attempt
					2015-10-22 22:42:02
	part2_incorrect_attempt
					('0:06:57', u'P(13-1,2)')
	part2_correct_attempt
					['0:07:02', u'5']

19 Student ID:eaherman

	first_attempt
					2015-10-22 17:32:53
	part2_incorrect_attempt
					('0:02:39', u'10+11+12+13')
					('0:03:47', u'11+12+13')
					('0:03:56', u'9+10+11+12')
					('0:05:05', u'6+7+8+9')
	part2_correct_attempt
					['0:05:12', u'4']

20 Student ID:haliew

	first_attempt
					2015-10-22 01:19:38
	part2_incorrect_attempt
					('0:00:40', u'1*11*1')
	part2_correct_attempt
					['0:00:57', u'1*2*1']

21 Student ID:ggaddi

	first_attempt
					2015-10-20 00:49:54
	part2_incorrect_attempt
					('0:01:24', u'P(12,1)')
					('0:03:01', u'C(12,1)')
	part2_correct_attempt
					['0:04:42', u'7']

22 Student ID:cprafull

	first_attempt
					2015-10-22 19:55:10
	part2_incorrect_attempt
					('0:00:00', u'12-2-1')
	part2_correct_attempt
					['0:02:13', u'12-5-1']












## Part 3

### (228) Mistake Group Digits of size 228




### (36) Mistake Group redirect of size 36




### (16) Mistake Group Fraction of size 16




### (63) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:b3hwang

	first_attempt
					2015-10-21 03:43:44
	part1_correct_attempt
					['0:00:00', u'1 * 12 * 11']
	part2_correct_attempt
					['0:01:19', u'1']
	part3_incorrect_attempt
					('0:02:19', u'(8(9))/2')
	part3_correct_attempt
					['0:02:28', u'(9(10))/2']

1 Student ID:apokhare

	first_attempt
					2015-10-21 18:19:19
	part1_correct_attempt
					['0:00:00', u'12*11']
	part2_correct_attempt
					['0:03:18', u'5']
	part3_incorrect_attempt
					('0:03:18', u'4*(5/2)')
	part3_correct_attempt
					['0:37:42', u'(6*5)/2']

2 Student ID:jag028

	first_attempt
					2015-10-22 17:14:01
	part1_correct_attempt
					['0:00:00', u'14*13']
	part2_correct_attempt
					['0:00:45', u'2']
	part3_incorrect_attempt
					('0:01:34', u'1+2+3+4+5+6+7+8')
					('0:01:51', u'1+2+3+4+5+6+7+8+9')
					('0:03:00', u'1+2+3+4+5+6')
	part3_correct_attempt
					['0:03:05', u'1+2+3+4+5']

3 Student ID:ctroncos

	first_attempt
					2015-10-22 17:13:14
	part1_correct_attempt
					['0:00:00', u'(15 -2) * (15-1)']
	part2_correct_attempt
					['0:01:53', u'12 - 9 -1']
	part3_incorrect_attempt
					('0:02:14', u'15 - 12')
	part3_correct_attempt
					['0:03:16', u'(15-9)*(15-9-1)/2']

4 Student ID:t2shin

	first_attempt
					2015-10-22 23:42:03
	part1_correct_attempt
					['0:00:00', u'14*13']
	part2_correct_attempt
					['0:02:26', u'4']
	part3_incorrect_attempt
					('0:03:40', u'7*6')
	part3_correct_attempt
					['0:04:04', u'1+2+3+4+5+6']

5 Student ID:kew060

	first_attempt
					2015-10-22 22:41:56
	part1_correct_attempt
					['0:00:00', u'P(16-1,2)']
	part2_correct_attempt
					['0:01:08', u'2']
	part3_incorrect_attempt
					('0:02:29', u'1+2+3+4+5')
					('0:04:11', u'1+2')
					('0:05:20', u'1+2+3+4')
					('0:05:30', u'1+2+3')
	part3_correct_attempt
					['0:05:38', u'1+2+3+4+5+6']

6 Student ID:ajvanega

	first_attempt
					2015-10-22 17:23:10
	part1_correct_attempt
					['0:00:00', u'P(15,2)']
	part2_correct_attempt
					['0:07:35', u'1']
	part3_incorrect_attempt
					('0:15:21', u'8*7')
					('0:17:59', u'8^2')
					('0:18:25', u'8+7+6+5+4+3+2+1')
	part3_correct_attempt
					['0:19:25', u'8+7+6+5+4+3+2+1+9']

7 Student ID:hkhodada

	first_attempt
					2015-10-21 02:20:48
	part1_correct_attempt
					['0:00:00', u'13*12']
	part2_correct_attempt
					['0:02:17', u'3']
	part3_incorrect_attempt
					('20:50:28', u'1+2+3+4')
	part3_correct_attempt
					['20:51:13', u'1+2+3+4+5+6+7+8']

8 Student ID:lguintu

	first_attempt
					2015-10-16 07:16:09
	part1_correct_attempt
					['0:00:00', u'P(14,2)']
	part2_correct_attempt
					['-1 day, 23:56:36', u'5']
	part3_incorrect_attempt
					('0:00:18', u'P(8,2)')
	part3_correct_attempt
					['0:00:25', u'C(8,2)']

9 Student ID:fichoi

	first_attempt
					2015-10-22 05:35:44
	part1_correct_attempt
					['0:00:00', u'P(14,2)']
	part2_correct_attempt
					['0:05:36', u'2']
	part3_incorrect_attempt
					('0:14:56', u'P(15,3)')
					('0:23:54', u'P(15,8)')
					('0:25:59', u'C(15,6)')
					('0:26:11', u'P(15,6)')
	part3_correct_attempt
					['0:29:13', u'21']

10 Student ID:any027

	first_attempt
					2015-10-19 20:50:57
	part1_correct_attempt
					['0:00:00', u'P(15,2)']
	part2_correct_attempt
					['0:01:42', u'3']
	part3_incorrect_attempt
					('0:03:07', u'1+2+3+4+5+6')
					('0:03:26', u'1+2+3+4+5+6+7+8+9+10+11+12')
	part3_correct_attempt
					['0:05:33', u'1+2+3+4+5+6+7+8+9+10+11']

11 Student ID:aadhakal

	first_attempt
					2015-10-21 18:58:04
	part1_correct_attempt
					['0:00:00', u'12*11']
	part2_correct_attempt
					['0:01:15', u'4']
	part3_incorrect_attempt
					('0:01:15', u'(5*4)/2')
					('0:01:52', u'(11*4)/2')
	part3_correct_attempt
					['0:02:06', u'(11*10)/2']

12 Student ID:kthui

	first_attempt
					2015-10-18 09:35:08
	part1_correct_attempt
					['0:00:00', u'14*13']
	part2_correct_attempt
					['0:00:41', u'7']
	part3_incorrect_attempt
					('0:01:27', u'12*11')
					('0:01:50', u'12+11+10+9+8+7+6+5+4+3+2+1')
	part3_correct_attempt
					['0:02:21', u'11+10+9+8+7+6+5+4+3+2+1']

13 Student ID:pvl001

	first_attempt
					2015-10-19 22:56:02
	part1_correct_attempt
					['0:00:00', u'13 * 12']
	part2_correct_attempt
					['0:03:20', u'6']
	part3_incorrect_attempt
					('0:03:38', u'6 + 5 + 4 + 3 + 2 +1')
	part3_correct_attempt
					['0:06:33', u'1 + 2 + 3 + 4 + 5 + 6 + 7 + 8']

14 Student ID:vsosnovs

	first_attempt
					2015-10-21 06:09:42
	part1_correct_attempt
					['0:00:00', u'210']
	part2_correct_attempt
					['23:25:20', u'4']
	part3_incorrect_attempt
					('23:30:08', u'(9*8)/(3)')
	part3_correct_attempt
					['23:30:13', u'(9*8)/(2)']

15 Student ID:alhung

	first_attempt
					2015-10-22 19:24:15
	part1_correct_attempt
					['0:00:00', u'13*12']
	part2_correct_attempt
					['0:07:39', u'8']
	part3_incorrect_attempt
					('0:11:33', u'9*8')
					('0:12:45', u'8*9/2')
	part3_correct_attempt
					['0:13:42', u'(9*10)/2']

16 Student ID:n2patil

	first_attempt
					2015-10-21 23:17:14
	part1_correct_attempt
					['0:00:00', u'12*11']
	part2_correct_attempt
					['-1 day, 23:59:46', u'1']
	part3_incorrect_attempt
					('0:00:32', u'1+2+3+4+5')
					('0:01:35', u'4+5')
					('0:04:00', u'1+2+3')
					('0:10:25', u'3+4+5')
					('0:10:53', u'1+2+3+4+5+6+7+8')
					('0:10:58', u'1+2+3+4+5+6+7')
					('0:11:20', u'1+2+3+4+5+6+7+8+9+10')
	part3_correct_attempt
					['0:12:05', u'1+2+3+4+5+6+7+8+9']

17 Student ID:s2chaudh

	first_attempt
					2015-10-22 03:09:33
	part1_correct_attempt
					['0:00:00', u'15*14']
	part2_correct_attempt
					['1:06:34', u'2']
	part3_incorrect_attempt
					('1:11:49', u'15*14')
					('1:14:26', u'16*15*14')
	part3_correct_attempt
					['14:24:39', u'1+2+3+4+5+6+7+8+9+10']

18 Student ID:tpmach

	first_attempt
					2015-10-22 03:09:14
	part1_correct_attempt
					['0:00:00', u'15*14']
	part2_correct_attempt
					['0:07:11', u'5']
	part3_incorrect_attempt
					('0:20:40', u'12*11*10*9*8*7*6*5*4*3*2')
	part3_correct_attempt
					['0:27:27', u'78']

19 Student ID:haw081

	first_attempt
					2015-10-22 06:08:56
	part1_correct_attempt
					['0:00:00', u'P(13-1,2)']
	part2_correct_attempt
					['0:03:02', u'3']
	part3_incorrect_attempt
					('0:15:46', u'11+10+9+8+7+6+5+4+3+2+1')
	part3_correct_attempt
					['0:23:40', u'3+2+1']

20 Student ID:bmilton

	first_attempt
					2015-10-21 03:49:57
	part1_correct_attempt
					['0:00:00', u'13 * 12']
	part2_correct_attempt
					['0:00:46', u'9']
	part3_incorrect_attempt
					('0:04:38', u'1+2+3+4+5+6+7+8+9')
	part3_correct_attempt
					['0:05:05', u'1+2+3+4+5+6+7+8+9+10']

21 Student ID:vqt004

	first_attempt
					2015-10-22 14:54:37
	part1_correct_attempt
					['0:00:00', u'12*11']
	part2_correct_attempt
					['0:00:00', u'1']
	part3_incorrect_attempt
					('0:00:00', u'4*9')
	part3_correct_attempt
					['0:02:46', u'4*7']

22 Student ID:mnrahman

	first_attempt
					2015-10-22 17:34:20
	part1_correct_attempt
					['0:00:00', u'(14-1)(14-2)']
	part2_correct_attempt
					['2:18:26', u'1']
	part3_incorrect_attempt
					('3:30:45', u'(14-8)(14-7)/2')
	part3_correct_attempt
					['3:31:11', u'((14-8)*(14-8-1))/2']

23 Student ID:pnquach

	first_attempt
					2015-10-22 21:08:26
	part1_correct_attempt
					['0:00:00', u'14*13']
	part2_correct_attempt
					['0:00:00', u'4']
	part3_incorrect_attempt
					('0:00:00', u'66*14*13')
	part3_correct_attempt
					['0:00:34', u'66']

24 Student ID:agarango

	first_attempt
					2015-10-22 19:39:35
	part1_correct_attempt
					['0:00:00', u'12*11']
	part2_correct_attempt
					['0:02:41', u'7']
	part3_incorrect_attempt
					('0:05:07', u'8+7+6+5+4+3+2+1')
	part3_correct_attempt
					['0:05:24', u'7+6+5+4+3+2+1']

25 Student ID:btn023

	first_attempt
					2015-10-21 18:11:08
	part1_correct_attempt
					['0:00:00', u'12*11']
	part2_correct_attempt
					['14:03:17', u'4']
	part3_incorrect_attempt
					('14:05:54', u'1+2+3+4+5+6')
					('14:07:53', u'(1+2+3+4+5)')
	part3_correct_attempt
					['14:09:21', u'(1+2+3+4+5+6+7)']

26 Student ID:achinn

	first_attempt
					2015-10-19 22:42:22
	part1_correct_attempt
					['0:00:00', u'14*13']
	part2_correct_attempt
					['0:05:48', u'1']
	part3_incorrect_attempt
					('0:10:49', u'11*10')
	part3_correct_attempt
					['0:11:52', u'1+2+3+4+5+6+7+8+9+10']

27 Student ID:dwzhang

	first_attempt
					2015-10-22 08:12:12
	part1_correct_attempt
					['0:00:00', u'15*14']
	part2_correct_attempt
					['0:04:40', u'7']
	part3_incorrect_attempt
					('0:07:16', u'1+2+3+4+5+6+7+8+19+20+21')
					('0:07:24', u'1+2+3+4+5+6+7+8+19+20')
	part3_correct_attempt
					['0:08:23', u'1+2+3+4+5+6+7+8+9+10']

28 Student ID:kalang

	first_attempt
					2015-10-22 21:06:06
	part1_correct_attempt
					['0:00:00', u'12*11']
	part2_correct_attempt
					['0:03:06', u'3']
	part3_incorrect_attempt
					('0:05:27', u'8*7')
	part3_correct_attempt
					['0:05:33', u'8*7/2']

29 Student ID:dgunawan

	first_attempt
					2015-10-23 00:52:56
	part1_correct_attempt
					['0:00:00', u'13* 12']
	part2_correct_attempt
					['0:00:53', u'3']
	part3_incorrect_attempt
					('0:05:58', u'9*10/2')
					('0:06:12', u'12*10/2')
					('0:06:48', u'11*10/2')
					('0:06:56', u'11(10)/2')
					('0:07:09', u'12(10)/2')

30 Student ID:rraiyyan

	first_attempt
					2015-10-22 20:33:37
	part1_correct_attempt
					['0:00:00', u'14*13']
	part2_correct_attempt
					['0:03:24', u'7']
	part3_incorrect_attempt
					('0:04:46', u'11!')
					('0:05:49', u'10!')
					('0:05:55', u'9!')
	part3_correct_attempt
					['0:06:22', u'C(11,2)']

31 Student ID:hmshah

	first_attempt
					2015-10-22 09:12:11
	part1_correct_attempt
					['0:00:00', u'1.0*(14-1)*(14-2)']
	part2_correct_attempt
					['0:00:54', u'1.0*(10-8-1)']
	part3_incorrect_attempt
					('0:01:35', u'1.0*(14-8)*(10-8-1)/2')
	part3_correct_attempt
					['0:01:52', u'1.0*(14-8)*(14-8-1)/2']

32 Student ID:v4zhang

	first_attempt
					2015-10-22 10:20:41
	part1_correct_attempt
					['0:00:00', u'C(14, 1)*C(13, 1)']
	part2_correct_attempt
					['10:04:41', u'5']
	part3_incorrect_attempt
					('10:05:54', u'C(10, 2)')
					('10:13:47', u'1+2+3+4+5')
	part3_correct_attempt
					['10:20:44', u'1+2+3+4+5+6+7+8']

33 Student ID:dsmonaha

	first_attempt
					2015-10-22 00:12:11
	part1_correct_attempt
					['0:00:00', u'C(12,1)C(11,1)']
	part2_correct_attempt
					['0:00:22', u'5']
	part3_incorrect_attempt
					('0:11:43', u'6!')
	part3_correct_attempt
					['0:12:05', u'6+5+4+3+2+1']

34 Student ID:tcuddy

	first_attempt
					2015-10-17 22:31:44
	part1_correct_attempt
					['0:00:00', u'12*13']
	part2_correct_attempt
					['0:00:50', u'5']
	part3_incorrect_attempt
					('0:04:06', u'10(11)/2')
					('0:05:29', u'14*15/2 - 10')
					('0:07:12', u'14*15/2 - (12)/2')
					('0:07:58', u'13*14/2 - (12)/2')
					('0:11:43', u'14*15/2 - (4*3)/2')
					('0:11:53', u'14*15/2 - (5*4)/2')
	part3_correct_attempt
					['0:12:07', u'11*12/2']

35 Student ID:dlgoldbe

	first_attempt
					2015-10-22 17:46:42
	part1_correct_attempt
					['0:00:00', u'C(14,2)*2']
	part2_correct_attempt
					['2:03:28', u'10']
	part3_incorrect_attempt
					('2:04:21', u'4+5+6+7+8+9+10+11+12+13+14+15')
					('2:09:07', u'C(14,2)*20')
					('2:10:35', u'1+2+3+4+5+6+7+8+9+10+11+12+13')
	part3_correct_attempt
					['2:11:19', u'1+2+3+4+5+6+7+8+9+10+11+12']

36 Student ID:sghouse

	first_attempt
					2015-10-21 23:32:50
	part1_correct_attempt
					['0:00:00', u'(14*13)']
	part2_correct_attempt
					['0:02:05', u'1']
	part3_incorrect_attempt
					('0:03:07', u'10!')
					('0:04:09', u'1+2+3+4+5+6+7+8+9+10+11')
					('0:04:17', u'1+2+3+4+5+6+7+8+9+10')
					('0:04:24', u'2+3+4+5+6+7+8+9+10')
	part3_correct_attempt
					['0:05:48', u'1+2+3+4+5+6+7+8+9']

37 Student ID:eaherman

	first_attempt
					2015-10-22 17:32:53
	part1_correct_attempt
					['0:00:00', u'12(11)']
	part2_correct_attempt
					['0:05:12', u'4']
	part3_incorrect_attempt
					('0:10:22', u'10+11+12+13')
					('0:11:04', u'4+5+6+7')
					('0:11:39', u'4+3+2+1')
					('0:19:37', u'6+7+8+9+10+11+12+13')
	part3_correct_attempt
					['0:20:43', u'28']

38 Student ID:glcohen

	first_attempt
					2015-10-18 01:16:55
	part1_correct_attempt
					['0:00:00', u'14*13']
	part2_correct_attempt
					['0:04:44', u'10']
	part3_incorrect_attempt
					('0:06:26', u'3+4+5+6+7+8+9+10+11+12')
	part3_correct_attempt
					['0:06:35', u'1+ 2+3+4+5+6+7+8+9+10+11+12']

39 Student ID:sayao

	first_attempt
					2015-10-21 16:46:03
	part1_correct_attempt
					['0:00:00', u'P(14,2)']
	part2_correct_attempt
					['0:00:39', u'2']
	part3_incorrect_attempt
					('0:01:05', u'P(15,3)-P(14,2)')
					('0:09:35', u'P(15,3)*P(14,2)')
					('0:10:33', u'P(15,3)-P(14,2)')
					('0:10:41', u'P(15,3)-2548')
					('0:22:42', u'P(14,2)')
	part3_correct_attempt
					['0:24:10', u'1+2+3+4+5+6+7+8']

40 Student ID:achava

	first_attempt
					2015-10-21 21:43:56
	part1_correct_attempt
					['0:00:00', u'14*13']
	part2_correct_attempt
					['-1 day, 19:41:13', u'1']
	part3_incorrect_attempt
					('0:04:10', u'1+2+3+4')
	part3_correct_attempt
					['0:04:15', u'1+2+3+4+5']

41 Student ID:dpereira

	first_attempt
					2015-10-19 21:10:01
	part1_correct_attempt
					['0:00:00', u'15*14']
	part2_correct_attempt
					['0:01:09', u'1']
	part3_incorrect_attempt
					('0:01:09', u'1+2+3+4+5+6+7+8')
					('0:01:14', u'1+2+3+4+5+6+7')
	part3_correct_attempt
					['0:01:40', u'1+2+3+4+5+6+7+8+9']

42 Student ID:arvenega

	first_attempt
					2015-10-22 22:04:34
	part1_correct_attempt
					['0:00:00', u'15*14']
	part2_correct_attempt
					['0:00:00', u'2']
	part3_incorrect_attempt
					('0:00:00', u'1+2+3+4+5+6+7+8+9')
	part3_correct_attempt
					['0:00:07', u'1+2+3+4+5+6']

43 Student ID:haliew

	first_attempt
					2015-10-22 01:19:38
	part1_correct_attempt
					['0:00:00', u'1*12*11']
	part2_correct_attempt
					['0:00:57', u'1*2*1']
	part3_incorrect_attempt
					('0:02:00', u'8!')
	part3_correct_attempt
					['0:02:37', u'8+7+6+5+4+3+2+1']

44 Student ID:dcastlem

	first_attempt
					2015-10-21 18:13:18
	part1_correct_attempt
					['0:00:00', u'13*12']
	part2_correct_attempt
					['0:00:30', u'4']
	part3_incorrect_attempt
					('0:06:43', u'13*12*4')
					('0:08:47', u'8+9+10+11+12+13')
					('0:08:55', u'8+9+10+11+12+13+14')
					('0:09:00', u'8+9+10+11')
					('0:09:11', u'7+8+9+10')
					('0:09:23', u'7+8+9+10+11+12+13')
					('0:09:32', u'7+8+9+10+11+12+13+14')
					('0:09:41', u'8+9+10+11+12+13')
					('0:09:56', u'10+11+12+13')
					('0:10:05', u'11+12+13+14')
					('0:11:08', u'8+9+10')
					('0:11:16', u'7+8+9')
					('0:12:33', u'8+9+10+11')
					('0:13:01', u'8*9*10*11')
					('0:14:50', u'7+8+9+10')
					('0:15:02', u'8+9+10')
					('0:18:13', u'8+9+10+11+12+13')
					('0:18:19', u'8+9+10+11+12+13+14')
					('0:18:25', u'7+8+9+10+11+12+13+14')
					('0:20:32', u'8+9+10+11+12')
					('0:20:37', u'8+9+10+11')
					('0:20:52', u'8+9+10+11+12+13')
					('0:20:58', u'8+9+10+11+12+13+14')
					('0:21:05', u'7+8+9+10+11+12+13+14')
					('0:21:51', u'8+9+10+11+12+13+14')
					('0:22:03', u'8+9+10+11+12+13')
					('0:24:37', u'8+9+10+11')
					('0:26:11', u'7+8+9+10')
					('0:55:49', u'8+9+10+11')
					('0:56:01', u'8*9*10*11')
					('0:56:39', u'8+9+10+11+12+13+14')
					('0:57:55', u'9+10+11+12+13+14')
					('0:58:01', u'9+10+11+12+13')
					('0:58:09', u'9+10+11')
	part3_correct_attempt
					['0:58:47', u'1+2+3+4+5+6']

45 Student ID:csl030

	first_attempt
					2015-10-22 04:40:41
	part1_correct_attempt
					['0:00:00', u'12*13']
	part2_correct_attempt
					['0:00:48', u'1']
	part3_incorrect_attempt
					('0:03:59', u'4*3')
					('0:04:07', u'4*2')
					('0:04:52', u'4*(4!)')
					('0:04:59', u'4*(3!)')
					('0:05:06', u'4*(2!)')
					('0:06:37', u'4+ 4!')
					('0:14:00', u'14 - 9')
					('0:14:18', u'14 - 10')
	part3_correct_attempt
					['0:23:52', u'1 + 2 + 3 + 4']

46 Student ID:edcole

	first_attempt
					2015-10-21 18:16:52
	part1_correct_attempt
					['0:00:00', u'12*11']
	part2_correct_attempt
					['0:02:52', u'9']
	part3_incorrect_attempt
					('0:03:06', u'12*11*9')
	part3_correct_attempt
					['0:05:14', u'10+9+8+7+6+5+4+3+2+1']

47 Student ID:v4sharma

	first_attempt
					2015-10-21 16:26:39
	part1_correct_attempt
					['0:00:00', u'14*13']
	part2_correct_attempt
					['0:05:32', u'9']
	part3_incorrect_attempt
					('0:21:15', u'9!')
	part3_correct_attempt
					['0:24:23', u'66']

48 Student ID:zig006

	first_attempt
					2015-10-21 20:42:32
	part1_correct_attempt
					['0:00:00', u'156']
	part2_correct_attempt
					['0:01:00', u'1']
	part3_incorrect_attempt
					('0:01:00', u'1+2+3+4+5+6')
	part3_correct_attempt
					['0:01:11', u'1+2+3+4+5']

49 Student ID:p4kumar

	first_attempt
					2015-10-22 22:52:54
	part1_correct_attempt
					['0:00:00', u'210']
	part2_correct_attempt
					['0:00:47', u'3']
	part3_incorrect_attempt
					('0:01:26', u'1+2+3+4+5+6+7+8+9+10+11+12+13+14')
	part3_correct_attempt
					['0:01:33', u'1+2+3+4+5+6+7+8+9+10+11+12+13']

50 Student ID:vasharma

	first_attempt
					2015-10-21 23:29:30
	part1_correct_attempt
					['0:00:00', u'13*12']
	part2_correct_attempt
					['0:00:09', u'1']
	part3_incorrect_attempt
					('0:00:49', u'1+2+3+4+5+6+7+8+9')
					('0:01:12', u'1+2+3+4+5+6+7+8+11+12+13+14')
					('0:01:29', u'1+2+3+4+5+6+7+8+11+12')
					('0:03:05', u'1+2+3+4+5+6+7+8')
					('0:03:29', u'1+2+3+4+5+6+7+8+9+10+11+12+13+14')
					('0:06:18', u'1+2+3+4+5+6+7+8')
					('0:06:26', u'1+2+3+4+5+6+7+8+9')
					('0:07:43', u'1+2+3+4+5+(14-9+1)')
					('0:08:13', u'1+2+3+4+5+(14-9-1)')
					('0:08:39', u'1+2+3+4+(14-9-1)')
	part3_correct_attempt
					['0:08:49', u'1+2+3+(14-9-1)']

51 Student ID:volim

	first_attempt
					2015-10-21 02:54:44
	part1_correct_attempt
					['0:00:00', u'12*11']
	part2_correct_attempt
					['0:00:34', u'9']
	part3_incorrect_attempt
					('0:00:57', u'9+8+7+6+5')
	part3_correct_attempt
					['0:01:05', u'9+8+7+6+5+4+3+2+1']

52 Student ID:k4ma

	first_attempt
					2015-10-22 04:04:04
	part1_correct_attempt
					['0:00:00', u'15*14']
	part2_correct_attempt
					['0:01:31', u'4']
	part3_incorrect_attempt
					('0:02:52', u'8*7')
	part3_correct_attempt
					['0:05:34', u'28']

53 Student ID:v3doan

	first_attempt
					2015-10-22 21:09:42
	part1_correct_attempt
					['0:00:00', u'P(12,2)']
	part2_correct_attempt
					['0:00:35', u'5']
	part3_incorrect_attempt
					('0:03:25', u'7!')
					('0:03:42', u'10!')
	part3_correct_attempt
					['0:04:16', u'10 * 11 / 2']

54 Student ID:jguanzho

	first_attempt
					2015-10-18 22:23:22
	part1_correct_attempt
					['0:00:00', u'12*11']
	part2_correct_attempt
					['0:04:12', u'2']
	part3_incorrect_attempt
					('0:04:12', u'13-4-1')
					('0:05:20', u'8*7')
	part3_correct_attempt
					['0:06:39', u'(6+7+8+9+10+11+12+13)-(8*5)']

55 Student ID:j2phung

	first_attempt
					2015-10-22 05:57:34
	part1_correct_attempt
					['0:00:00', u'15*14']
	part2_correct_attempt
					['0:01:16', u'2']
	part3_incorrect_attempt
					('0:02:38', u'2*7')
					('0:03:04', u'2*15')
					('0:03:14', u'2*13')
	part3_correct_attempt
					['0:17:19', u'36']

56 Student ID:srl006

	first_attempt
					2015-10-23 00:43:34
	part1_correct_attempt
					['0:00:00', u'12 * 13']
	part3_incorrect_attempt
					('0:02:02', u'((14-8)(14-8-1))/2')
					('0:02:19', u'((14-7)(14-7-1))/2')
					('0:02:26', u'((14-6)(14-6-1))/2')
					('0:02:34', u'((14-9)(14-9-1))/2')
					('0:02:45', u'((14-10)(14-10-1))/2')
					('0:02:52', u'((14-11)(14-11-1))/2')
					('0:03:06', u'((14-8)(14-8-1))/2')
					('0:03:13', u'((14-7)(14-7-1))/2')
					('0:05:21', u'((14+9)(14-9+1))/2')

57 Student ID:hmnaing

	first_attempt
					2015-10-22 00:34:59
	part1_correct_attempt
					['0:00:00', u'15*14']
	part2_correct_attempt
					['15:08:47', u'13-6-1']
	part3_incorrect_attempt
					('15:09:03', u'1+2+3+4+5+6')
					('15:09:46', u'7+8+9+10+11+12')
					('15:13:20', u'1+2+3+4+5+6+7+8+9+10')
	part3_correct_attempt
					['15:13:27', u'1+2+3+4+5+6+7+8+9']

58 Student ID:ggaddi

	first_attempt
					2015-10-20 00:49:54
	part1_correct_attempt
					['0:00:00', u'P(13,2)']
	part2_correct_attempt
					['0:04:42', u'7']
	part3_incorrect_attempt
					('0:05:54', u'4+5+6+7+8+9+10+11+12+13+14')
	part3_correct_attempt
					['0:07:49', u'1+2+3+4+5+6+7+8+9+10+11']

59 Student ID:mtrafeca

	first_attempt
					2015-10-22 21:02:26
	part1_correct_attempt
					['0:00:00', u'14*13']
	part2_correct_attempt
					['0:01:50', u'4']
	part3_incorrect_attempt
					('0:12:03', u'8+9+10+11+12+13+14+15')
					('0:12:14', u'7+8+9+10+11+12+13+14+15')
					('0:17:27', u'8+9+10+11+12+13+14+15')
					('0:17:54', u'14*13')
					('0:26:26', u'1+2+3+4+5+6+7+8+9+10+11+12+13+14+15')
					('0:26:57', u'7+8+9+10+11+12+13+14+15')
					('0:27:38', u'8+9+10+11+12+13+14+15')
	part3_correct_attempt
					['0:32:04', u'28']

60 Student ID:bkoli

	first_attempt
					2015-10-22 20:31:32
	part1_correct_attempt
					['0:00:00', u'(14-1)(14-2)']
	part2_correct_attempt
					['0:06:47', u'8']
	part3_incorrect_attempt
					('0:33:26', u'(14-4)(14-3)/2')
					('0:33:41', u'(14-4)(14-3-1)/2')
	part3_correct_attempt
					['0:34:00', u'(14-4)(14-4-1)/2']

61 Student ID:k3tan

	first_attempt
					2015-10-22 22:12:08
	part1_correct_attempt
					['0:00:00', u'15*14']
	part2_correct_attempt
					['0:00:13', u'1']
	part3_incorrect_attempt
					('0:32:33', u'6!')
					('0:33:13', u'5!')
					('0:33:18', u'4!')
	part3_correct_attempt
					['0:52:51', u'1+2+3+4+5+6']

62 Student ID:cprafull

	first_attempt
					2015-10-22 19:55:10
	part1_correct_attempt
					['0:00:00', u'(12)(11)']
	part2_correct_attempt
					['0:02:13', u'12-5-1']
	part3_incorrect_attempt
					('0:02:28', u'(12)(11)/2')
					('0:09:50', u'(12)(11)/6')
					('0:09:56', u'(12)(11)/1')
					('0:10:02', u'(12)(11)/2')
					('0:10:07', u'(12)(11)/3')
					('0:10:11', u'(12)(11)/4')
					('0:10:16', u'(12)(11)/6')
					('0:11:36', u'(23)*(2)/2')
	part3_correct_attempt
					['0:12:57', u'(13-5)(13-6)/2']












## Part 4

### (24) Mistake Group ['R.0'] of size 24
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(15-4)*(15-4-1)/2/[(15-1)*(15-2)]	|55/P(11,2)	|[('R.0', 55.0, u'(15-4)*(15-4-1)/2', u'55')]	|
|1	|(15-6)*(15-6-1)/2/[(15-1)*(15-2)]	|(1+2+3+4+5+6+7+8) / (9*8)	|[('R.0', 36.0, u'(15-6)*(15-6-1)/2', u'1+2+3+4+5+6+7+8')]	|
|2	|(13-4)*(13-4-1)/2/[(13-1)*(13-2)]	|36/121	|[('R.0', 36.0, u'(13-4)*(13-4-1)/2', u'36')]	|
|3	|(14-5)*(14-5-1)/2/[(14-1)*(14-2)]	|(1+2+3+4+5+6+7+8) / C(9,2)	|[('R.0', 36.0, u'(14-5)*(14-5-1)/2', u'1+2+3+4+5+6+7+8')]	|
|4	|(14-2)*(14-2-1)/2/[(14-1)*(14-2)]	|66/132	|[('R.0', 66.0, u'(14-2)*(14-2-1)/2', u'66')]	|
|5	|(14-2)*(14-2-1)/2/[(14-1)*(14-2)]	|66/78	|[('R.0', 66.0, u'(14-2)*(14-2-1)/2', u'66')]	|
|6	|(14-2)*(14-2-1)/2/[(14-1)*(14-2)]	|66/91	|[('R.0', 66.0, u'(14-2)*(14-2-1)/2', u'66')]	|
|7	|(14-2)*(14-2-1)/2/[(14-1)*(14-2)]	|66/182	|[('R.0', 66.0, u'(14-2)*(14-2-1)/2', u'66')]	|
|8	|(16-8)*(16-8-1)/2/[(16-1)*(16-2)]	|28/28	|[('R.0', 28.0, u'(16-8)*(16-8-1)/2', u'28')]	|
|9	|(16-8)*(16-8-1)/2/[(16-1)*(16-2)]	|28/(16*16)	|[('R.0', 28.0, u'(16-8)*(16-8-1)/2', u'28')]	|
|10	|(13-3)*(13-3-1)/2/[(13-1)*(13-2)]	|45/121	|[('R.0', 45.0, u'(13-3)*(13-3-1)/2', u'45')]	|
|11	|(15-6)*(15-6-1)/2/[(15-1)*(15-2)]	|36/5	|[('R.0', 36.0, u'(15-6)*(15-6-1)/2', u'36')]	|
|12	|(16-3)*(16-3-1)/2/[(16-1)*(16-2)]	|78/260	|[('R.0', 78.0, u'(16-3)*(16-3-1)/2', u'78')]	|
|13	|(13-3)*(13-3-1)/2/[(13-1)*(13-2)]	|45/131	|[('R.0', 45.0, u'(13-3)*(13-3-1)/2', u'45')]	|
|14	|(16-7)*(16-7-1)/2/[(16-1)*(16-2)]	|36/2	|[('R.0', 36.0, u'(16-7)*(16-7-1)/2', u'36')]	|
|15	|(14-3)*(14-3-1)/2/[(14-1)*(14-2)]	|55/C(11,2)	|[('R.0', 55.0, u'(14-3)*(14-3-1)/2', u'55')]	|
|16	|(14-6)*(14-6-1)/2/[(14-1)*(14-2)]	|28/210	|[('R.0', 28.0, u'(14-6)*(14-6-1)/2', u'28')]	|
|17	|(15-4)*(15-4-1)/2/[(15-1)*(15-2)]	|55/110	|[('R.0', 55.0, u'(15-4)*(15-4-1)/2', u'55')]	|
|18	|(15-3)*(15-3-1)/2/[(15-1)*(15-2)]	|C(12,2)/6	|[('R.0', 66.0, u'(15-3)*(15-3-1)/2', u'C(12,2)')]	|
|19	|(13-8)*(13-8-1)/2/[(13-1)*(13-2)]	|20/2/(14*13)	|[('R.0', 10.0, u'(13-8)*(13-8-1)/2', u'20/2')]	|
|20	|(13-2)*(13-2-1)/2/[(13-1)*(13-2)]	|(11*10/2)/(11*10)	|[('R.0', 55.0, u'(13-2)*(13-2-1)/2', u'11*10/2')]	|
|21	|(13-2)*(13-2-1)/2/[(13-1)*(13-2)]	|11*10/2/(11*10)	|[('R.0', 55.0, u'(13-2)*(13-2-1)/2', u'11*10/2')]	|
|22	|(16-9)*(16-9-1)/2/[(16-1)*(16-2)]	|21/132	|[('R.0', 21.0, u'(16-9)*(16-9-1)/2', u'21')]	|
|23	|(13-7)*(13-7-1)/2/[(13-1)*(13-2)]	|15/91	|[('R.0', 15.0, u'(13-7)*(13-7-1)/2', u'15')]	|




### (20) Mistake Group ['R.1'] of size 20
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(15-4)*(15-4-1)/2/[(15-1)*(15-2)]	|P(11,2)/(14*13)	|[('R.1', 182.0, u'(15-1)*(15-2)', u'14*13')]	|
|1	|(15-7)*(15-7-1)/2/[(15-1)*(15-2)]	|10/182	|[('R.1', 182.0, u'(15-1)*(15-2)', u'182')]	|
|2	|(16-6)*(16-6-1)/2/[(16-1)*(16-2)]	|(((16-6)*(16-6-1)/2)+(8-6-1))/((16-1)*(16-2))	|[('R.1', 210.0, u'(16-1)*(16-2)', u'(16-1)*(16-2)')]	|
|3	|(14-8)*(14-8-1)/2/[(14-1)*(14-2)]	|(1+2+3+4+5+6+7+8)/P(13,2)	|[('R.1', 156.0, u'(14-1)*(14-2)', u'P(13,2)')]	|
|4	|(14-8)*(14-8-1)/2/[(14-1)*(14-2)]	|(1+2+3+4+5+6+7+8+9)/P(13,2)	|[('R.1', 156.0, u'(14-1)*(14-2)', u'P(13,2)')]	|
|5	|(14-8)*(14-8-1)/2/[(14-1)*(14-2)]	|(1+2+3+4+5+6+7+8+9+10)/P(13,2)	|[('R.1', 156.0, u'(14-1)*(14-2)', u'P(13,2)')]	|
|6	|(14-8)*(14-8-1)/2/[(14-1)*(14-2)]	|(1+2+3+4+5+6+7+8+9+10+11)/P(13,2)	|[('R.1', 156.0, u'(14-1)*(14-2)', u'P(13,2)')]	|
|7	|(14-8)*(14-8-1)/2/[(14-1)*(14-2)]	|(1+2+3+4+5+6+7+8+9+10+11+12)/P(13,2)	|[('R.1', 156.0, u'(14-1)*(14-2)', u'P(13,2)')]	|
|8	|(14-9)*(14-9-1)/2/[(14-1)*(14-2)]	|5/P(13,2)	|[('R.1', 156.0, u'(14-1)*(14-2)', u'P(13,2)')]	|
|9	|(14-5)*(14-5-1)/2/[(14-1)*(14-2)]	|10/(13*12)	|[('R.1', 156.0, u'(14-1)*(14-2)', u'13*12')]	|
|10	|(14-3)*(14-3-1)/2/[(14-1)*(14-2)]	|(10(11)/12)/(13*12)	|[('R.1', 156.0, u'(14-1)*(14-2)', u'13*12')]	|
|11	|(13-9)*(13-9-1)/2/[(13-1)*(13-2)]	|(13-5)*(13-5-1)/2/[(13-1)*(13-2)]	|[('R.1', 132.0, u'(13-1)*(13-2)', u'(13-1)*(13-2)')]	|
|12	|(16-5)*(16-5-1)/2/[(16-1)*(16-2)]	|36/210	|[('R.1', 210.0, u'(16-1)*(16-2)', u'210')]	|
|13	|(14-8)*(14-8-1)/2/[(14-1)*(14-2)]	|(((14-9)*(14-9-1))/2)/((14-1)*(14-2))	|[('R.1', 156.0, u'(14-1)*(14-2)', u'(14-1)*(14-2)')]	|
|14	|(15-7)*(15-7-1)/2/[(15-1)*(15-2)]	|(15-4)*(15-4-1)/2/[(15-1)*(15-2)]	|[('R.1', 182.0, u'(15-1)*(15-2)', u'(15-1)*(15-2)')]	|
|15	|(15-7)*(15-7-1)/2/[(15-1)*(15-2)]	|(15-5)*(15-5-1)/2/[(15-1)*(15-2)]	|[('R.1', 182.0, u'(15-1)*(15-2)', u'(15-1)*(15-2)')]	|
|16	|(15-7)*(15-7-1)/2/[(15-1)*(15-2)]	|(15-5)*(15-5-1)/5/[(15-1)*(15-2)]	|[('R.1', 182.0, u'(15-1)*(15-2)', u'(15-1)*(15-2)')]	|
|17	|(15-7)*(15-7-1)/2/[(15-1)*(15-2)]	|(15-2)*(15-2-1)/2/[(15-1)*(15-2)]	|[('R.1', 182.0, u'(15-1)*(15-2)', u'(15-1)*(15-2)')]	|
|18	|(15-7)*(15-7-1)/2/[(15-1)*(15-2)]	|(15-3)*(15-3-1)/2/[(15-1)*(15-2)]	|[('R.1', 182.0, u'(15-1)*(15-2)', u'(15-1)*(15-2)')]	|
|19	|(16-9)*(16-9-1)/2/[(16-1)*(16-2)]	|(1+2+3+4+5+6+7+8+9)/(15*14)	|[('R.1', 210.0, u'(16-1)*(16-2)', u'15*14')]	|




### (18) Mistake Group redirect of size 18




### (5) Mistake Group ['R.0', 'R.1.0'] of size 5
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(14-5)*(14-5-1)/2/[(14-1)*(14-2)]	|(1+2+3+4+5+6+7+8) / C(13,2)	|[('R.0', 36.0, u'(14-5)*(14-5-1)/2', u'1+2+3+4+5+6+7+8'), ('R.1.0', 13.0, u'14-1', u'13')]	|
|1	|(14-4)*(14-4-1)/2/[(14-1)*(14-2)]	|45/C(13,2)	|[('R.0', 45.0, u'(14-4)*(14-4-1)/2', u'45'), ('R.1.0', 13.0, u'14-1', u'13')]	|
|2	|(15-4)*(15-4-1)/2/[(15-1)*(15-2)]	|55/(14*14)	|[('R.0', 55.0, u'(15-4)*(15-4-1)/2', u'55'), ('R.1.0', 14.0, u'15-1', u'14')]	|
|3	|(14-3)*(14-3-1)/2/[(14-1)*(14-2)]	|55/C(13,2)	|[('R.0', 55.0, u'(14-3)*(14-3-1)/2', u'55'), ('R.1.0', 13.0, u'14-1', u'13')]	|
|4	|(13-4)*(13-4-1)/2/[(13-1)*(13-2)]	|36/C(12,2)	|[('R.0', 36.0, u'(13-4)*(13-4-1)/2', u'36'), ('R.1.0', 12.0, u'13-1', u'12')]	|




### (3) Mistake Group Digits of size 3




### (3) Mistake Group ['R.0.0.1'] of size 3
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(14-9)*(14-9-1)/2/[(14-1)*(14-2)]	|(1+2+3+4)/13*12	|[('R.0.0.1', 4.0, u'14-9-1', u'4')]	|
|1	|(13-9)*(13-9-1)/2/[(13-1)*(13-2)]	|[(13-9)*(13-9-1)/2]/[11-9-1]	|[('R.0.0.1', 3.0, u'13-9-1', u'13-9-1')]	|
|2	|(16-9)*(16-9-1)/2/[(16-1)*(16-2)]	|(1+2+3+4+5+6+7)/(P(14,2))	|[('R.0.0.1', 6.0, u'16-9-1', u'6')]	|




### (1) Mistake Group ['R.0.0'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(15-4)*(15-4-1)/2/[(15-1)*(15-2)]	|P(11,2)/14*13	|[('R.0.0', 110.0, u'(15-4)*(15-4-1)', u'P(11,2)')]	|




### (1) Mistake Group ['R.0', 'R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(15-8)*(15-8-1)/2/[(15-1)*(15-2)]	|21(14*13)	|[('R.0', 21.0, u'(15-8)*(15-8-1)/2', u'21'), ('R.1', 182.0, u'(15-1)*(15-2)', u'14*13')]	|




### (1) Mistake Group ['R.0', 'R.1.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(13-5)*(13-5-1)/2/[(13-1)*(13-2)]	|28/[22(11)]	|[('R.0', 28.0, u'(13-5)*(13-5-1)/2', u'28'), ('R.1.1', 11.0, u'13-2', u'11')]	|




### (1) Mistake Group Wrong_Sign of size 1




### (1) Mistake Group ['R.0.0.1.0.1', 'R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.1.0.1', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(13-5)*(13-5-1)/2/[(13-1)*(13-2)]	|((15-6)*(15-5-1)/2)/((13-1)*(13-2))	|[('R.0.0.1.0.1', 5.0, u'5', u'5'), ('R.1', 132.0, u'(13-1)*(13-2)', u'(13-1)*(13-2)')]	|




### (1) Mistake Group ['R.0.0.1', 'R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.1', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(14-8)*(14-8-1)/2/[(14-1)*(14-2)]	|(1+2+3+4+5+6)/P(13,2)	|[('R.0.0.1', 5.0, u'14-8-1', u'5'), ('R.1', 156.0, u'(14-1)*(14-2)', u'P(13,2)')]	|




### (1) Mistake Group ['R.0.0.1.0.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.1.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|(16-6)*(16-6-1)/2/[(16-1)*(16-2)]	|(((16-6)*(16-6-1)/2)+(8-6-1))/(16-1)*(16-2)	|[('R.0.0.1.0.1', 6.0, u'6', u'6')]	|




### (22) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:agoldsht

	first_attempt
					2015-10-20 05:56:57
	part1_correct_attempt
					['0:00:00', u'(15-1)*(15-2)']
	part2_correct_attempt
					['0:01:24', u'13-2-1']
	part3_correct_attempt
					['0:01:24', u'(15-2)*(15-2-1)/2']
	part4_incorrect_attempt
					('0:02:22', u'(15-2)*(15-2-1)/2 * (15-1)*(15-2)')
	part4_correct_attempt
					['0:02:42', u'(15-2)*(15-2-1)/(2 * (15-1)*(15-2))']

1 Student ID:lrlai

	first_attempt
					2015-10-21 20:10:58
	part1_correct_attempt
					['0:00:00', u'12*11']
	part2_correct_attempt
					['0:01:09', u'2']
	part3_correct_attempt
					['0:03:19', u'45']
	part4_incorrect_attempt
					('0:03:19', u'(45/(13*12*11) * (12*11/(13*12*11)))/(12*11/(13*12*11))')
	part4_correct_attempt
					['7:50:48', u'45/(12*11)']

2 Student ID:asetters

	first_attempt
					2015-10-20 07:27:34
	part1_correct_attempt
					['0:00:00', u'14*13']
	part2_correct_attempt
					['0:00:00', u'2']
	part3_correct_attempt
					['-1 day, 23:59:10', u'12(13)/2']
	part4_incorrect_attempt
					('0:00:00', u'(12*13/2)/14*13')
	part4_correct_attempt
					['0:00:10', u'(12*13/2)/(14*13)']

3 Student ID:spw006

	first_attempt
					2015-10-20 21:50:53
	part1_correct_attempt
					['0:00:00', u'12*11']
	part2_correct_attempt
					['0:00:13', u'5']
	part3_correct_attempt
					['-1 day, 23:59:32', u'6+5+4+3+2+1']
	part4_incorrect_attempt
					('0:00:28', u'6+5+4+3+2+1/(12*11)')
	part4_correct_attempt
					['0:00:39', u'(6+5+4+3+2+1)/(12*11)']

4 Student ID:asp025

	first_attempt
					2015-10-21 19:37:12
	part1_correct_attempt
					['0:00:00', u'12*11']
	part2_correct_attempt
					['0:00:56', u'6']
	part3_correct_attempt
					['0:18:33', u'8*7/2']
	part4_incorrect_attempt
					('0:24:04', u'(8*7/2)/12*11')
	part4_correct_attempt
					['0:24:14', u'(8*7/2)/(12*11)']

5 Student ID:aadhakal

	first_attempt
					2015-10-21 18:58:04
	part1_correct_attempt
					['0:00:00', u'12*11']
	part2_correct_attempt
					['0:01:15', u'4']
	part3_correct_attempt
					['0:02:06', u'(11*10)/2']
	part4_incorrect_attempt
					('0:02:06', u'((11*10)/2)/12*11')
	part4_correct_attempt
					['0:02:21', u'((11*10)/2)/(12*11)']

6 Student ID:aakumar

	first_attempt
					2015-10-19 23:21:21
	part1_correct_attempt
					['0:00:00', u'12*11']
	part2_correct_attempt
					['0:00:55', u'3']
	part3_correct_attempt
					['0:39:44', u'36']
	part4_incorrect_attempt
					('0:40:02', u'36/12*11')
	part4_correct_attempt
					['0:40:14', u'36/132']

7 Student ID:jfalcone

	first_attempt
					2015-10-22 20:11:11
	part1_correct_attempt
					['0:00:00', u'(14)(13)']
	part2_correct_attempt
					['0:01:21', u'8']
	part3_correct_attempt
					['0:02:20', u'(12)*(11)/2']
	part4_incorrect_attempt
					('0:02:49', u'182/66')
	part4_correct_attempt
					['0:03:23', u'(12)*(11)/2/182']

8 Student ID:hak014

	first_attempt
					2015-10-20 07:53:56
	part1_correct_attempt
					['0:00:00', u'14*13']
	part2_correct_attempt
					['0:00:36', u'1']
	part3_correct_attempt
					['0:02:23', u'21']
	part4_incorrect_attempt
					('0:02:42', u'21/14*13')
	part4_correct_attempt
					['0:04:26', u'21/(14*13)']

9 Student ID:jcj006

	first_attempt
					2015-10-21 23:04:57
	part1_correct_attempt
					['0:00:00', u'15*14']
	part2_correct_attempt
					['0:00:00', u'1']
	part3_correct_attempt
					['0:00:00', u'1+2+3+4+5+6+7']
	part4_incorrect_attempt
					('0:00:00', u'1+2+3+4+5+6+7/(15*14)')
	part4_correct_attempt
					['0:00:10', u'(1+2+3+4+5+6+7)/(15*14)']

10 Student ID:achinn

	first_attempt
					2015-10-19 22:42:22
	part1_correct_attempt
					['0:00:00', u'14*13']
	part2_correct_attempt
					['0:05:48', u'1']
	part3_correct_attempt
					['0:11:52', u'1+2+3+4+5+6+7+8+9+10']
	part4_incorrect_attempt
					('0:16:02', u'(65/15!)/((14*13)/15!)')
					('0:16:35', u'(65/(15*14*13))/((14*13)/(15*14*13))')
	part4_correct_attempt
					['0:16:56', u'(55/(15*14*13))/((14*13)/(15*14*13))']

11 Student ID:jcl084

	first_attempt
					2015-10-20 03:02:56
	part1_correct_attempt
					['0:00:00', u'11*12']
	part2_correct_attempt
					['0:00:43', u'10-4-1']
	part3_correct_attempt
					['0:01:28', u'9*8/2']
	part4_incorrect_attempt
					('0:02:01', u'9*8/2/11*12')
	part4_correct_attempt
					['0:02:17', u'(9*8/2)/(11*12)']

12 Student ID:rraiyyan

	first_attempt
					2015-10-22 20:33:37
	part1_correct_attempt
					['0:00:00', u'14*13']
	part2_correct_attempt
					['0:03:24', u'7']
	part3_correct_attempt
					['0:06:22', u'C(11,2)']
	part4_incorrect_attempt
					('0:08:31', u'C(11,2)*14*13/(C(15,3))')
	part4_correct_attempt
					['0:12:11', u'C(11,2)/(14*13)']

13 Student ID:thwan

	first_attempt
					2015-10-19 17:00:29
	part1_correct_attempt
					['0:00:00', u'15*14']
	part2_correct_attempt
					['0:00:40', u'2']
	part3_correct_attempt
					['0:03:39', u'45']
	part4_incorrect_attempt
					('0:03:39', u'45/15*14')
	part4_correct_attempt
					['0:03:59', u'45/(15*14)']

14 Student ID:eaherman

	first_attempt
					2015-10-22 17:32:53
	part1_correct_attempt
					['0:00:00', u'12(11)']
	part2_correct_attempt
					['0:05:12', u'4']
	part3_correct_attempt
					['0:20:43', u'28']
	part4_incorrect_attempt
					('0:21:03', u'28/22(11)')
	part4_correct_attempt
					['0:22:04', u'28/[12(11)]']

15 Student ID:edcole

	first_attempt
					2015-10-21 18:16:52
	part1_correct_attempt
					['0:00:00', u'12*11']
	part2_correct_attempt
					['0:02:52', u'9']
	part3_correct_attempt
					['0:05:14', u'10+9+8+7+6+5+4+3+2+1']
	part4_incorrect_attempt
					('0:06:29', u'(10+9+8+7+6+5+4+3+2+1)/12*11')
	part4_correct_attempt
					['0:06:39', u'(10+9+8+7+6+5+4+3+2+1)/(12*11)']

16 Student ID:rbdoming

	first_attempt
					2015-10-21 05:00:11
	part1_correct_attempt
					['0:00:00', u'12*11']
	part2_correct_attempt
					['-1 day, 23:42:43', u'8']
	part3_correct_attempt
					['-1 day, 23:43:22', u'C(10,2)']
	part4_incorrect_attempt
					('0:00:13', u'121/45')
	part4_correct_attempt
					['0:00:46', u'45/132']

17 Student ID:mitopete

	first_attempt
					2015-10-22 01:41:02
	part1_correct_attempt
					['0:00:00', u'P(14,2)']
	part2_correct_attempt
					['-1 day, 21:58:52', u'5']
	part3_correct_attempt
					['0:06:30', u'36']
	part4_incorrect_attempt
					('0:13:41', u'(36/(C(9,2)))/((P(14,2))/(C(14,2)))')
					('0:35:13', u'(36/120)/(P(14,2)/P(15,2))')
					('0:37:36', u'(36/44)/(P(14,2)/P(15,2))')

18 Student ID:zhz159

	first_attempt
					2015-10-22 04:20:01
	part1_correct_attempt
					['0:00:00', u'210']
	part2_correct_attempt
					['0:00:00', u'1']
	part3_correct_attempt
					['0:00:58', u'66']
	part4_incorrect_attempt
					('0:00:58', u'0.314857')
	part4_correct_attempt
					['0:01:17', u'0.3142857']

19 Student ID:qfu

	first_attempt
					2015-10-16 03:30:06
	part1_correct_attempt
					['0:00:00', u'12*11']
	part2_correct_attempt
					['-1 day, 23:56:04', u'7']
	part3_correct_attempt
					['-1 day, 23:58:51', u'55']
	part4_incorrect_attempt
					('0:00:00', u'55/12*11')
	part4_correct_attempt
					['0:00:13', u'55/(12*11)']

20 Student ID:k3tan

	first_attempt
					2015-10-22 22:12:08
	part1_correct_attempt
					['0:00:00', u'15*14']
	part2_correct_attempt
					['0:00:13', u'1']
	part3_correct_attempt
					['0:52:51', u'1+2+3+4+5+6']
	part4_incorrect_attempt
					('0:53:03', u'21/15*14')
	part4_correct_attempt
					['0:53:23', u'21/210']

21 Student ID:j2phung

	first_attempt
					2015-10-22 05:57:34
	part1_correct_attempt
					['0:00:00', u'15*14']
	part2_correct_attempt
					['0:01:16', u'2']
	part3_correct_attempt
					['0:17:19', u'36']
	part4_incorrect_attempt
					('0:19:10', u'(36/210)/(2/210)')
	part4_correct_attempt
					['0:22:29', u'36/210']












