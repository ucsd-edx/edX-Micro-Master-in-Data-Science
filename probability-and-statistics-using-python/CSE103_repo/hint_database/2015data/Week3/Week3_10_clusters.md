#Problem 10

    $R1=random(7,15,1);	   # number of cards
    $R2=random(2,$R1-1,1);    # number of envelopes

    ### Putting cards in envelopes (Guided Problem) ###
    This is a challenge problem, you have until wed to solve it.
    It is recommended that you try, this will help you understand what we
    do in class.
    ---
    Suppose we have [$R1] cards and [$R2] envelopes to put them in. The envelopes are marked (1,...,[$R2]).
    We will calculate the number of ways to put the cards into the envelopes under different conditions.

    1.  Suppose all the cards are *distinct* (i.e. are numbered
        (1,2,....,[$R1])). How many ways are there to place cards into
        envelopes?
        As should be expected from the first part of a question, this is
        an easy one. Think of placing the cards into envelopes in the
        following way: take the first card and choose an envelope for it,
        then take the second card and choose an envelope for it etc. Until
        all of the cards have been placed. Clearly we can get any possible
        combination this way. It takes a little thought, but you can also
        convince yourself that there is only *one* way to get each
        combination. In other words, there is no overcounting.

        Counting the number of combinations we get this way is simple. At
        each of the [$R1] step we place one card in one of the [$R2]
        envelopes. Taking the product over all of these steps we get that
        the number of combinations is [____________]{Compute("$R2^$R1")}

    2.  Suppose that cards are *identical*. (The envelopes remain distinct)
        How many combinations are possible in this case?

        Consider the difference between part 1 and part 2. In part 1, each configuration
        specified exactly *which* cards were placed in each envelope. Here
        the cards are identical, therefor we can only say how *many* cards
        are in each envelope, but we cannot identify them.

        Thinking of the problem this way, we realize that it is
        mathematically equivalent to the problem of choosing [$R1] candies
        when there are [$R2] *types* of candy to choose from. As the Candies
        are indistinguishable, we are only interested in the number of
        candies chosen from each type. The correspondence is card <-> candy and candy type <-> envelope.

        If you go back to this problem, you will recall the formula for it and use it to get the
        answer: [__________]{Compute("C($R1+$R2-1,$R1)")}

    3.  Suppose the cards are identical as in 2. and, in addition, we
        require that each envelope contain at least one card.  In this
        case we first have to check that the number of cards is at least
        as large as the number of envelopes, otherwise there will be no
        way to satisfy the requirements. Luckily (thanks to the magic of
        WebWork) [`[$R1]>[$R2]`].

        OK, good. Now we can proceed in two steps, first, take [$R2] cards
        and put one card in each envelope, satisfying the reuirement that
        each envelop contains a card. The remaining cards can be placed in
        any envelope, with no constraints. We now have the same situation
        we had in part 2. but where, instead of [$R1] cards, we have
        [$R1]-[$R2]=[$R1-$R2] cards. We use the same formula that we used
        in 2. to find that the answer is
        [________________]{Compute("C($R1-1,$R1-$R2)")}





## Part 1

### (165) Mistake Group Digits of size 165




### (55) Mistake Group ['R.0'] of size 55
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|6^9	|6!	|[('R.0', 6.0, u'6', u'6')]	|
|1	|9^13	|9!	|[('R.0', 9.0, u'9', u'9')]	|
|2	|12^14	|12!	|[('R.0', 12.0, u'12', u'12')]	|
|3	|10^15	|10!	|[('R.0', 10.0, u'10', u'10')]	|
|4	|6^8	|C(6,2)	|[('R.0', 6.0, u'6', u'6')]	|
|5	|13^14	|13!	|[('R.0', 13.0, u'13', u'13')]	|
|6	|7^10	|7!	|[('R.0', 7.0, u'7', u'7')]	|
|7	|10^15	|C(10,5)	|[('R.0', 10.0, u'10', u'10')]	|
|8	|8^15	|8^8	|[('R.0', 8.0, u'8', u'8')]	|
|9	|6^7	|6*6	|[('R.0', 6.0, u'6', u'6')]	|
|10	|8^13	|C(8,4)	|[('R.0', 8.0, u'8', u'8')]	|
|11	|2^11	|2*11!	|[('R.0', 2.0, u'2', u'2')]	|
|12	|8^10	|8!	|[('R.0', 8.0, u'8', u'8')]	|
|13	|3^9	|3*9!	|[('R.0', 3.0, u'3', u'3')]	|
|14	|4^14	|4(14!)	|[('R.0', 4.0, u'4', u'4')]	|
|15	|6^7	|6^3	|[('R.0', 6.0, u'6', u'6')]	|
|16	|6^7	|6^6	|[('R.0', 6.0, u'6', u'6')]	|
|17	|10^15	|10^10	|[('R.0', 10.0, u'10', u'10')]	|
|18	|5^12	|5!	|[('R.0', 5.0, u'5', u'5')]	|
|19	|7^10	|7*C(10,7)	|[('R.0', 7.0, u'7', u'7')]	|
|20	|6^8	|P(6,2)	|[('R.0', 6.0, u'6', u'6')]	|
|21	|2^7	|2*7!	|[('R.0', 2.0, u'2', u'2')]	|
|22	|7^10	|C(7,1)^7	|[('R.0', 7.0, u'7', u'C(7,1)')]	|
|23	|2^11	|2^10	|[('R.0', 2.0, u'2', u'2')]	|
|24	|3^13	|3^9	|[('R.0', 3.0, u'3', u'3')]	|
|25	|11^12	|11!	|[('R.0', 11.0, u'11', u'11')]	|
|26	|10^11	|10*10	|[('R.0', 10.0, u'10', u'10')]	|
|27	|11^12	|11*11	|[('R.0', 11.0, u'11', u'11')]	|




### (35) Mistake Group ['R.1'] of size 35
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|6^9	|6!*9	|[('R.1', 9.0, u'9', u'9')]	|
|1	|6^9	|C(16,9)	|[('R.1', 9.0, u'9', u'9')]	|
|2	|6^9	|P(16,9)	|[('R.1', 9.0, u'9', u'9')]	|
|3	|6^8	|C(12, 8)	|[('R.1', 8.0, u'8', u'8')]	|
|4	|9^11	|C(19,11)	|[('R.1', 11.0, u'11', u'11')]	|
|5	|9^11	|P(20,11)	|[('R.1', 11.0, u'11', u'11')]	|
|6	|9^11	|C(20,11)	|[('R.1', 11.0, u'11', u'11')]	|
|7	|13^14	|C(27,14)	|[('R.1', 14.0, u'14', u'14')]	|
|8	|13^14	|C(26,14)	|[('R.1', 14.0, u'14', u'14')]	|
|9	|3^12	|C(14,12)	|[('R.1', 12.0, u'12', u'12')]	|
|10	|2^12	|13*12	|[('R.1', 12.0, u'12', u'12')]	|
|11	|5^12	|C(16,12)	|[('R.1', 12.0, u'12', u'12')]	|
|12	|6^12	|C(12+6-1, 12)	|[('R.1', 12.0, u'12', u'12')]	|
|13	|6^7	|2**7	|[('R.1', 7.0, u'7', u'7')]	|
|14	|7^15	|15*7*15	|[('R.1', 15.0, u'15', u'15')]	|
|15	|7^15	|(15*7)*15	|[('R.1', 15.0, u'15', u'15')]	|
|16	|3^9	|C(11,9)	|[('R.1', 9.0, u'9', u'9')]	|
|17	|7^9	|C(15, 9)	|[('R.1', 9.0, u'9', u'9')]	|
|18	|9^10	|2^10	|[('R.1', 10.0, u'10', u'10')]	|
|19	|9^10	|10!-10	|[('R.1', 10.0, u'10', u'10')]	|
|20	|10^13	|12^13	|[('R.1', 13.0, u'13', u'13')]	|
|21	|4^7	|35 * 7	|[('R.1', 7.0, u'7', u'7')]	|
|22	|4^12	|5^12	|[('R.1', 12.0, u'12', u'12')]	|
|23	|12^14	|14*12*14	|[('R.1', 14.0, u'14', u'14')]	|
|24	|12^14	|C(25,14)	|[('R.1', 14.0, u'14', u'14')]	|
|25	|5^13	|(5!)^13	|[('R.1', 13.0, u'13', u'13')]	|
|26	|12^13	|13!13	|[('R.1', 13.0, u'13', u'13')]	|
|27	|12^13	|13!/13	|[('R.1', 13.0, u'13', u'13')]	|
|28	|3^10	|C(12,10)	|[('R.1', 10.0, u'10', u'10')]	|
|29	|4^9	|C(12,9)	|[('R.1', 9.0, u'9', u'9')]	|
|30	|3^7	|C(9,7)	|[('R.1', 7.0, u'7', u'7')]	|




### (25) Mistake Group Fraction of size 25




### (8) Mistake Group ['R.0', 'R.1'] of size 8
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|2^8	|2*8	|[('R.0', 2.0, u'2', u'2'), ('R.1', 8.0, u'8', u'8')]	|
|1	|4^14	|4(14)	|[('R.0', 4.0, u'4', u'4'), ('R.1', 14.0, u'14', u'14')]	|
|2	|2^7	|2*7	|[('R.0', 2.0, u'2', u'2'), ('R.1', 7.0, u'7', u'7')]	|
|3	|8^14	|8 * 14	|[('R.0', 8.0, u'8', u'8'), ('R.1', 14.0, u'14', u'14')]	|
|4	|7^10	|7*10	|[('R.0', 7.0, u'7', u'7'), ('R.1', 10.0, u'10', u'10')]	|
|5	|9^14	|9*14	|[('R.0', 9.0, u'9', u'9'), ('R.1', 14.0, u'14', u'14')]	|
|6	|5^11	|5*11	|[('R.0', 5.0, u'5', u'5'), ('R.1', 11.0, u'11', u'11')]	|
|7	|10^11	|10*11	|[('R.0', 10.0, u'10', u'10'), ('R.1', 11.0, u'11', u'11')]	|




### (4) Mistake Group Wrong_Sign of size 4




### (181) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:gthorn

	first_attempt
					2015-10-11 04:39:11
	part1_incorrect_attempt
					('0:00:00', u'18!/(13!(18-13)!)')
	part1_correct_attempt
					['2 days, 13:23:28', u'6^13']

1 Student ID:v4zhang

	first_attempt
					2015-10-15 06:50:13
	part1_incorrect_attempt
					('0:00:00', u'15!/[13!*(2!)]')
					('0:00:48', u'(15*14)/(2)')
					('0:01:32', u'15*14*13*12*11*10*9*8*7*6*5*4*3')
					('0:02:05', u'(15!)/[13!*(15-13)!]')
					('0:02:29', u'C(15, 13)')
					('0:00:00', u'15*14*13*12*11*10*9*8*7*6*5*4*3')
	part1_correct_attempt
					['0:07:38', u'13^15']

2 Student ID:kbielawi

	first_attempt
					2015-10-11 23:40:26
	part1_incorrect_attempt
					('0:00:00', u'13*12*11*10')
					('0:00:33', u'C(13,4)')
					('0:00:44', u'P(13,4)')
					('0:01:22', u'C(17,4)')
	part1_correct_attempt
					['3:12:07', u'4^13']

3 Student ID:srl006

	first_attempt
					2015-10-10 05:33:25
	part1_incorrect_attempt
					('0:00:00', u'13!')
	part1_correct_attempt
					['0:02:02', u'9^13']

4 Student ID:seleon

	first_attempt
					2015-10-15 06:37:16
	part1_incorrect_attempt
					('0:00:00', u'12**4')
	part1_correct_attempt
					['0:00:05', u'4**12']

5 Student ID:jjm019

	first_attempt
					2015-10-15 23:14:49
	part1_incorrect_attempt
					('0:00:00', u'12!')
					('0:03:00', u'12!/11!')
					('0:06:30', u'(12-1)11+1')
					('0:06:40', u'(11-1)12+1')
					('0:07:14', u'12!11!')
					('0:08:32', u'12!')
	part1_correct_attempt
					['0:44:06', u'11^12']

6 Student ID:mhale

	first_attempt
					2015-10-14 21:49:06
	part1_incorrect_attempt
					('0:00:00', u'7 * 6 * 5 * 4')
					('0:00:36', u'7 * 6 * 5 * 4 * 4')
					('0:00:49', u'7 * 6 * 5 * 4 * 3 * 2 * 1')
					('0:00:56', u'7 * 6 * 5 * 4 * 3 * 2 * 1 * 4')
					('0:02:25', u'28 * 18 * 10')
					('0:03:59', u'4 * 3 * 2')
					('0:04:33', u'35 * 4')
	part1_correct_attempt
					['0:06:12', u'4^7']

7 Student ID:ctgraves

	first_attempt
					2015-10-13 21:33:55
	part1_incorrect_attempt
					('0:00:00', u'10*4*9*3*8*2*7*1')
					('0:00:48', u'10!/(10-4)!')
					('0:05:20', u'13!/(9!)')
	part1_correct_attempt
					['0:07:17', u'4^10']

8 Student ID:dkurli

	first_attempt
					2015-10-14 03:40:26
	part1_incorrect_attempt
					('0:00:00', u'40*10!')
					('0:00:09', u'10!/40')
					('0:00:45', u'10!*4')
					('0:00:51', u'10!^4')
					('0:00:00', u'10!*40')
	part1_correct_attempt
					['0:02:52', u'4^10']

9 Student ID:j5phung

	first_attempt
					2015-10-09 18:13:41
	part1_incorrect_attempt
					('0:00:00', u'13*12*11/3')
					('0:00:21', u'13*12*11/3!')
					('0:00:43', u'13*12*11')
					('0:03:58', u'13!*3')
	part1_correct_attempt
					['0:06:38', u'3^13']

10 Student ID:anl114

	first_attempt
					2015-10-15 07:38:26
	part1_incorrect_attempt
					('0:00:00', u'13!/5')
	part1_correct_attempt
					['0:06:13', u'5^13']

11 Student ID:haw081

	first_attempt
					2015-10-11 00:59:30
	part1_incorrect_attempt
					('0:00:00', u'C(10,7)')
					('0:00:27', u'10*9*7*8*6*5*4')
					('0:01:14', u'10*9*7*8*6*5*4 * 7!')
					('0:00:00', u'10*9*8*7*6*5*4')
					('0:00:19', u'10^7')
					('0:03:18', u'10*9*7*8*6*5*4 * 7!')
					('0:00:00', u'10*9*7*8*6*5*4 * 7')
					('0:03:20', u'C(10,7)')
					('0:04:38', u'C(15,7)')
					('0:00:00', u'P(10,7)')
					('0:00:10', u'P(10,7)*7!')
					('0:00:00', u'10*9*7*8*6*5*4 * 7!')
					('0:00:45', u'10*9*7*8*6*5*4')
					('0:01:07', u'10*9*7*8*6*5*4 *7^7')
					('0:00:00', u'7!P(10,7)')
					('0:00:09', u'P(10,7)')
					('0:00:00', u'10!')
					('0:00:00', u'10*9*7')
					('0:00:00', u'C(10,7)')
					('0:00:09', u'P(10,7)')
					('0:01:55', u'C(16,7)')
					('0:00:00', u'2^7')
	part1_correct_attempt
					['4 days, 1:54:31', u'7^10']

12 Student ID:airanmeh

	first_attempt
					2015-10-15 23:42:35
	part1_incorrect_attempt
					('0:00:00', u'20!/(5!15!)')
					('0:00:14', u'20!/(6!14!)')
					('0:00:52', u'20!/(6!14!) *15!')
					('0:01:49', u'15^6')
	part1_correct_attempt
					['0:02:01', u'6^15']

13 Student ID:jew037

	first_attempt
					2015-10-14 04:02:45
	part1_incorrect_attempt
					('0:00:00', u'9!/8!')
					('0:00:38', u'9!')
					('0:00:50', u'9!-8!')
					('0:02:24', u'9^8')
	part1_correct_attempt
					['0:02:31', u'8^9']

14 Student ID:rlhagen

	first_attempt
					2015-10-11 18:01:41
	part1_incorrect_attempt
					('0:00:00', u'10!/(10-7)!')
					('0:01:50', u'10!')
					('0:04:57', u'16!/(10!(16-10)!)')
					('0:05:22', u'10!/(7!(10-7)!)')
					('0:05:35', u'10!/(10-7)!')
					('0:06:56', u'10^7')
	part1_correct_attempt
					['0:07:09', u'7^10']

15 Student ID:asrana

	first_attempt
					2015-10-15 19:45:12
	part1_incorrect_attempt
					('0:00:00', u'14^8')
	part1_correct_attempt
					['0:00:47', u'8^14']

16 Student ID:jmmcalex

	first_attempt
					2015-10-15 07:39:50
	part1_incorrect_attempt
					('0:00:00', u'12!/2!')
					('0:02:06', u'22!/12!')
					('0:02:11', u'21!/12!')
					('0:02:28', u'21!/11!')
					('0:02:45', u'21!/10!')
					('0:02:52', u'22!/10!')
	part1_correct_attempt
					['0:03:56', u'10^12']

17 Student ID:lalacson

	first_attempt
					2015-10-11 16:43:23
	part1_incorrect_attempt
					('0:00:00', u'14!')
					('0:01:57', u'14!-1')
					('5:08:18', u'C(14,13)')
	part1_correct_attempt
					['5:09:04', u'13^14']

18 Student ID:mpanelo

	first_attempt
					2015-10-10 20:01:22
	part1_incorrect_attempt
					('0:00:00', u'11!7!')
					('0:11:22', u'11! / 4!')
	part1_correct_attempt
					['0:30:19', u'7^11']

19 Student ID:tcn013

	first_attempt
					2015-10-14 19:27:00
	part1_incorrect_attempt
					('0:00:00', u'11!/5!')
	part1_correct_attempt
					['0:03:40', u'6^11']

20 Student ID:tstevens

	first_attempt
					2015-10-12 10:15:51
	part1_incorrect_attempt
					('0:00:00', u'15*14*13*12*11*10*9*8')
					('0:01:17', u'15^8')
					('0:01:36', u'15*14*13*12*11*10*9*8')
					('0:04:46', u'15*14*13*12*11*10*9')
					('0:04:53', u'15*14*13*12*11*10*9*8')
					('0:07:40', u'15^8')
	part1_correct_attempt
					['0:08:27', u'8^15']

21 Student ID:pthsu

	first_attempt
					2015-10-10 19:56:52
	part1_incorrect_attempt
					('0:00:00', u'P(11,8)')
					('0:01:23', u'11!10!9!8!7!6!5!4!')
					('0:01:39', u'11*10*9*8*7*6*5*4')
	part1_correct_attempt
					['0:02:41', u'8**11']

22 Student ID:tcuddy

	first_attempt
					2015-10-10 19:26:21
	part1_incorrect_attempt
					('0:00:00', u'11!/2')
	part1_correct_attempt
					['0:00:54', u'2**10']

23 Student ID:l8ngo

	first_attempt
					2015-10-12 15:23:11
	part1_incorrect_attempt
					('0:00:00', u'12^2')
	part1_correct_attempt
					['1:21:32', u'2^12']

24 Student ID:aysee

	first_attempt
					2015-10-13 23:03:04
	part1_incorrect_attempt
					('0:00:00', u'C(7,6)*C(6,5)*C(5,4)*C(4,3)*C(3,2)*C(2,1)')
	part1_correct_attempt
					['0:02:54', u'6^7']

25 Student ID:sayao

	first_attempt
					2015-10-12 19:00:52
	part1_incorrect_attempt
					('0:00:00', u'C(7,6)')
					('0:00:00', u'7!')
					('0:00:00', u'36*5')
	part1_correct_attempt
					['21:29:39', u'6^7']

26 Student ID:anvan

	first_attempt
					2015-10-14 22:22:42
	part1_incorrect_attempt
					('0:00:00', u'13!/(10!3!)')
					('0:00:00', u'13!/3!')
	part1_correct_attempt
					['3:25:21', u'10^13']

27 Student ID:csl030

	first_attempt
					2015-10-14 01:47:00
	part1_incorrect_attempt
					('0:00:00', u'C(8, 5)')
					('0:00:26', u'8*7* 6* 5*4')
					('0:01:07', u'C(8,5)')
					('0:01:19', u'P(8,5)')
					('0:04:58', u'C(12, 5)')
	part1_correct_attempt
					['0:07:21', u'5^8']

28 Student ID:jguanzho

	first_attempt
					2015-10-09 20:02:48
	part1_incorrect_attempt
					('0:00:00', u'13!/(10!)')
					('0:01:58', u'13!')
					('0:50:48', u'3**4*2**3')
					('0:00:00', u'13!/10!')
					('0:00:00', u'13!')
					('0:00:16', u'13!/(10!*3!)')
					('0:00:00', u'13!/(3!)')
					('0:00:11', u'13!/(10!)')
					('0:01:08', u'13**3')
	part1_correct_attempt
					['1:24:57', u'3**13']

29 Student ID:flhernan

	first_attempt
					2015-10-14 22:53:02
	part1_incorrect_attempt
					('0:00:00', u'C(16,5)')
					('0:01:18', u'C(12,5)')
					('0:00:00', u'C(7,5)')
					('0:01:39', u'P(7,5)')
	part1_correct_attempt
					['19:40:22', u'5^12']

30 Student ID:a2ahmed

	first_attempt
					2015-10-15 03:43:18
	part1_incorrect_attempt
					('0:00:00', u'10*9*8*7*6*5*4*3')
					('0:00:25', u'C(10,7)')
	part1_correct_attempt
					['0:05:11', u'7^10']

31 Student ID:mitopete

	first_attempt
					2015-10-13 19:36:04
	part1_incorrect_attempt
					('0:00:00', u'10!/(4!(6!))')
					('0:00:00', u'13!/(4!9!)')
					('0:00:00', u'14!/(4!10!)')
					('0:02:31', u'(14!/(10!))')
	part1_correct_attempt
					['0:43:04', u'4^10']

32 Student ID:starinia

	first_attempt
					2015-10-15 02:22:02
	part1_incorrect_attempt
					('0:00:00', u'8!/5!')
	part1_correct_attempt
					['3:11:52', u'5^8']

33 Student ID:tak068

	first_attempt
					2015-10-14 06:12:55
	part1_incorrect_attempt
					('0:00:00', u'7^3')
					('0:00:00', u'7*6*5*6')
					('0:00:39', u'35*6')
					('0:00:55', u'35*34*33')
					('0:00:00', u'21*12*5')
	part1_correct_attempt
					['0:26:44', u'3^7']

34 Student ID:yos017

	first_attempt
					2015-10-14 06:12:04
	part1_incorrect_attempt
					('0:00:00', u'13!/3!')
					('0:00:00', u'22!/(13!*9!)')
					('0:00:00', u'24!/(13!*11!)')
	part1_correct_attempt
					['0:10:22', u'10^13']

35 Student ID:habuamar

	first_attempt
					2015-10-09 05:44:35
	part1_incorrect_attempt
					('0:00:00', u'(11!)/(6!)')
	part1_correct_attempt
					['0:00:42', u'5^11']

36 Student ID:akg009

	first_attempt
					2015-10-15 22:28:57
	part1_incorrect_attempt
					('0:00:00', u'12!')
					('0:01:07', u'12!/(11)!')
					('0:01:45', u'12!')
					('0:02:55', u'12!')
					('0:00:00', u'12*11')
	part1_correct_attempt
					['0:35:52', u'11^12']

37 Student ID:b3hwang

	first_attempt
					2015-10-14 18:14:30
	part1_incorrect_attempt
					('0:00:00', u'13!')
					('0:01:44', u'13*12*10*11*10*9*8*7*6')
					('0:02:40', u'13*12*11*10*9*8*7*6*5')
					('0:04:52', u'13!/((13-9)!*9!)')
					('0:05:56', u'13^9')
	part1_correct_attempt
					['0:06:09', u'9^13']

38 Student ID:jag028

	first_attempt
					2015-10-15 00:35:49
	part1_incorrect_attempt
					('0:00:00', u'10!')
					('0:00:00', u'10*7')
					('0:00:00', u'(10*7)/7')
					('0:00:46', u'(10!)/(7!(10-7)!)')
					('0:00:00', u'C(10,7)')
					('0:00:00', u'C(10,7)')
					('0:02:23', u'C(10,7)')
					('0:00:00', u'10*9*8*7*6*5*4')
					('0:03:58', u'10!')
					('0:00:00', u'[(10!)/3!]')
					('0:43:27', u'C(17,7)')
	part1_correct_attempt
					['16:09:27', u'7^10']

39 Student ID:ccn001

	first_attempt
					2015-10-12 21:32:07
	part1_incorrect_attempt
					('0:00:00', u'15! * 14!')
					('0:03:05', u'15!/(13!)')
					('0:04:04', u'15!/(13!)*2')
	part1_correct_attempt
					['0:04:46', u'2^15']

40 Student ID:quwong

	first_attempt
					2015-10-14 04:21:55
	part1_incorrect_attempt
					('0:00:00', u'12!/(7!*5!)')
					('0:03:24', u'12!/5!')
					('0:03:39', u'12!/7!')
					('0:07:41', u'12!')
					('0:11:33', u'12^7')
					('0:13:13', u'12!*7')
					('0:00:00', u'12!*7!')
					('0:06:15', u'12!/(7!*5!)*12*7')
					('0:08:29', u'12!/(5!)*12*7')
					('0:11:01', u'12!/(7!*5!)*12^7')
					('0:18:02', u'12!/(7!*5!)*7^12')
					('0:18:57', u'12!/(7!*5!)*5')
					('0:30:55', u'12!/(7!*5!)*12!/7')
					('0:31:17', u'12!/(7!*5!)*12!/7!')
					('0:33:46', u'12!/(5!)/7')
					('0:37:37', u'12!/7')
					('0:00:00', u'12!/(7!*5!)*12!/5!')
					('0:00:00', u'19!/(12! * 7!)')
					('0:10:31', u'12!/(7!*5!)')
					('0:10:45', u'12!/(5!)')
					('0:10:52', u'12!/(7!)')
	part1_correct_attempt
					['11:48:51', u'7^12']

41 Student ID:lguintu

	first_attempt
					2015-10-09 21:14:12
	part1_incorrect_attempt
					('0:00:00', u'9*6')
					('0:00:37', u'C(9,6)')
					('0:01:13', u'9!/3!')
					('0:01:19', u'9!/3!/6!')
					('0:06:28', u'C(9,6)*6!')
					('0:07:18', u'P(9,6)*6!')
					('0:07:26', u'P(9,3)*6!')
					('0:09:01', u'P(7,6)')
					('0:09:36', u'P(13,6)')
					('0:09:41', u'P(13,7)')
					('0:09:47', u'C(13,6)')
					('0:00:00', u'P(16,7)')
					('0:00:07', u'P(16,6)')
					('0:00:12', u'P(15,6)')
					('0:00:00', u'P(14,6)')
					('0:00:00', u'9!*6')
					('0:00:10', u'9!*6!')
					('0:14:00', u'C(8,5)')
	part1_correct_attempt
					['0:30:14', u'6^9']

42 Student ID:jjchung

	first_attempt
					2015-10-14 19:22:53
	part1_incorrect_attempt
					('0:00:00', u'11!10!9!8!7!6!5!')
					('0:00:25', u'C(11,7)')
					('0:00:00', u'11!10!9!8!7!6!')
					('0:00:25', u'11!/4!')
					('0:00:32', u'11!/7!')
					('0:00:41', u'12!/4!')
					('0:00:56', u'C(11,7)')
					('0:02:00', u'11^7')
	part1_correct_attempt
					['0:09:52', u'7^11']

43 Student ID:abjara

	first_attempt
					2015-10-12 21:04:25
	part1_incorrect_attempt
					('0:00:00', u'9!/(5!*4!)')
					('0:00:36', u'9*8*7*6*5')
	part1_correct_attempt
					['0:02:55', u'5^9']

44 Student ID:skarimik

	first_attempt
					2015-10-09 16:48:46
	part1_incorrect_attempt
					('0:00:00', u'13^10')
	part1_correct_attempt
					['0:01:18', u'10^13']

45 Student ID:anislam

	first_attempt
					2015-10-15 23:02:49
	part1_incorrect_attempt
					('0:00:00', u'C(7,3)')
	part1_correct_attempt
					['0:01:51', u'3^7']

46 Student ID:thk002

	first_attempt
					2015-10-12 02:16:26
	part1_incorrect_attempt
					('0:00:00', u'13!')
					('0:01:24', u'C(13,10)')
					('0:02:21', u'P(13,10)')
					('0:00:00', u'13!/3!')
					('0:00:09', u'13!/10!')
					('0:19:04', u'C(13,3)')
	part1_correct_attempt
					['2 days, 4:37:43', u'10^13']

47 Student ID:krau

	first_attempt
					2015-10-14 03:39:55
	part1_incorrect_attempt
					('0:00:00', u'11!')
					('0:00:00', u'11!/((4!)*(7!))')
	part1_correct_attempt
					['0:03:10', u'7^11']

48 Student ID:mroknich

	first_attempt
					2015-10-13 21:07:58
	part1_incorrect_attempt
					('0:00:00', u'14!/(6!8!)')
					('0:00:59', u'21!/8!')
					('0:00:00', u'14*13*12*11*10*9*8*7*6')
					('0:00:20', u'14*13*12*11*10*9*8*7')
					('0:02:00', u'14^8')
					('0:02:14', u'14*13*12*11*10*9*8*7')
					('0:03:27', u'14*13*12*11*10*9*8*7*8!')
					('0:03:36', u'14*13*12*11*10*9*8*7*8')
					('0:00:00', u'14!/(8!6!)')
					('0:01:03', u'14!')
					('0:02:59', u'21!/8!')

49 Student ID:alhung

	first_attempt
					2015-10-15 19:42:24
	part1_incorrect_attempt
					('0:00:00', u'C(13,3)')
					('0:00:00', u'13^3')
	part1_correct_attempt
					['0:03:51', u'3^13']

50 Student ID:jic212

	first_attempt
					2015-10-12 06:31:19
	part1_incorrect_attempt
					('0:00:00', u'P(9,4)')
					('0:00:36', u'9*8*7*6')
					('0:03:53', u'9!')
					('0:09:05', u'C(9,4)*C(8,4)')
					('0:09:30', u'C(9,4)')
	part1_correct_attempt
					['0:11:26', u'4^9']

51 Student ID:r1gu

	first_attempt
					2015-10-15 11:39:05
	part1_incorrect_attempt
					('0:00:00', u'C(12,3)')
					('0:00:39', u'C(12,2)')
					('0:01:31', u'10*9*8')
					('0:04:36', u'C(12,3)')
					('0:04:45', u'C(12,2)')
					('0:15:02', u'10*3*9*2*8*1')
					('0:15:55', u'720*6')
					('0:18:51', u'C(12,3)')
					('0:18:56', u'C(12,2)')
					('0:20:02', u'C(12,9)')
					('0:21:07', u'10*9')
					('0:22:09', u'10*9+1')
					('0:23:52', u'C(12,3)')
					('0:23:57', u'C(12,2)')
	part1_correct_attempt
					['0:26:28', u'3^10']

52 Student ID:sippolit

	first_attempt
					2015-10-12 04:05:04
	part1_incorrect_attempt
					('0:00:00', u'11!')
					('0:00:34', u'11!/(11-9)!')
					('0:02:04', u'11!/(9)!')
					('0:03:24', u'11!/9!')
					('0:06:21', u'11!/(11-9)!')
					('0:06:38', u'11!/(9!(11-9)!)')
	part1_correct_attempt
					['0:14:57', u'9^11']

53 Student ID:hak014

	first_attempt
					2015-10-13 04:50:43
	part1_incorrect_attempt
					('0:00:00', u'11!/7!')
					('0:00:14', u'11!/4!')
					('0:01:12', u'17!/(7!10!)')
					('0:02:35', u'11!/(4!7!)')
					('0:06:15', u'17!(6!11!)')
					('0:06:24', u'17!/(6!11!)')
					('0:06:36', u'17!/6!')
					('0:00:00', u'330*7!')
	part1_correct_attempt
					['0:13:04', u'7^11']

54 Student ID:dwzhang

	first_attempt
					2015-10-13 21:55:38
	part1_incorrect_attempt
					('0:00:00', u'13!')
					('0:00:25', u'C(13,12)')
	part1_correct_attempt
					['0:02:04', u'12^13']

55 Student ID:dis003

	first_attempt
					2015-10-15 11:02:01
	part1_incorrect_attempt
					('0:00:00', u'11*5')
					('0:00:17', u'11**5')
	part1_correct_attempt
					['0:00:48', u'5**11']

56 Student ID:atorr

	first_attempt
					2015-10-11 01:18:19
	part1_incorrect_attempt
					('0:00:00', u'C(8,6)')
					('0:01:29', u'C(8,2)')
					('0:02:26', u'C(6,5)')
					('0:04:49', u'C(10,6)')
					('0:00:00', u'C(12,4)')
					('0:00:28', u'P(8,6)')
					('0:01:36', u'8!/(2!2!)')
					('0:01:47', u'6!/(2!2!)')
					('0:02:24', u'C(8,6)')
					('0:00:00', u'C(5 + 8 - 1, 8 - 1)')
					('0:00:12', u'C(5 + 2 - 1, 2 - 1)')
					('0:00:00', u'C(14,6)')
	part1_correct_attempt
					['3 days, 0:13:29', u'6^8']

57 Student ID:rraiyyan

	first_attempt
					2015-10-14 23:19:11
	part1_incorrect_attempt
					('0:00:00', u'7!')
					('0:09:05', u'C(7,6)')
					('0:11:08', u'7!*6 ')
	part1_correct_attempt
					['0:11:39', u'6^7']

58 Student ID:jhw015

	first_attempt
					2015-10-15 04:27:33
	part1_incorrect_attempt
					('0:00:00', u'C(8,3)')
					('0:10:32', u'C(8,1)+C(8,2)+C(8,3)')
					('0:10:40', u'C(8,1)*C(8,2)*C(8,3)')
					('0:00:00', u'8^3')
	part1_correct_attempt
					['0:45:30', u'3^8']

59 Student ID:dsmonaha

	first_attempt
					2015-10-13 17:35:25
	part1_incorrect_attempt
					('0:00:00', u'11!10!9!')
					('0:00:12', u'11*10*9')
					('0:00:35', u'C(11,3)')
					('0:01:59', u'11!10!')
					('0:02:32', u'11!10!9!')
					('0:03:40', u'C(11,1)*C(10,1)*C(9,1)')
	part1_correct_attempt
					['0:04:42', u'3^11']

60 Student ID:thwan

	first_attempt
					2015-10-11 18:50:54
	part1_incorrect_attempt
					('0:00:00', u'(10+3)!/3!')
	part1_correct_attempt
					['0:01:46', u'[C(4,1)]^10']

61 Student ID:lcardoso

	first_attempt
					2015-10-13 16:40:30
	part1_incorrect_attempt
					('0:00:00', u'C(14-1+7,7)')
					('0:01:31', u'C(14,7)')
					('0:02:14', u'14^7')
	part1_correct_attempt
					['0:03:29', u'7^14']

62 Student ID:hmnaing

	first_attempt
					2015-10-13 15:22:48
	part1_incorrect_attempt
					('0:00:00', u'C(13 + 8, 8)')
					('0:03:21', u'14!/8!')
	part1_correct_attempt
					['1 day, 9:10:50', u'8^14']

63 Student ID:etemlock

	first_attempt
					2015-10-11 00:37:25
	part1_incorrect_attempt
					('0:00:00', u'P(8,5)')
					('0:02:44', u'C(8,3)')
					('0:02:57', u'C(8,5)')
	part1_correct_attempt
					['0:03:48', u'5^8']

64 Student ID:ggaddi

	first_attempt
					2015-10-13 17:43:19
	part1_incorrect_attempt
					('0:00:00', u'13!')
					('0:11:48', u'13!/12!')
					('0:14:53', u'24!/(12!*12!)')
					('0:18:00', u'13!*12!')
					('0:18:17', u'13!*12^13')
					('0:22:41', u'13*12')
					('0:22:52', u'13!*12!')
					('0:30:43', u'13!*12')
					('0:30:57', u'13*12!')
					('0:32:24', u'13!*12^12')
					('0:00:00', u'24!/(11!*13!)')
					('0:03:27', u'13!*(12^13)')
	part1_correct_attempt
					['10:33:30', u'12^13']

65 Student ID:smohiman

	first_attempt
					2015-10-11 19:40:13
	part1_incorrect_attempt
					('0:00:00', u'16!')
					('0:00:56', u'C(9,8)')
					('0:02:32', u'C(16,7)')
					('0:07:34', u'9*8*7*6*5*4*3*2')
					('0:09:52', u'9+8')
	part1_correct_attempt
					['0:12:59', u'8^9']

66 Student ID:muy002

	first_attempt
					2015-10-14 22:24:49
	part1_incorrect_attempt
					('0:00:00', u'8*7')
					('0:00:00', u'8!/6!')
					('0:02:38', u'8!')
					('0:02:42', u'8!/2')
					('0:02:46', u'8!/2!')
					('0:03:04', u'8!/(2!6!)')
	part1_correct_attempt
					['0:11:32', u'2^8']

67 Student ID:wcwhite

	first_attempt
					2015-10-14 01:56:24
	part1_incorrect_attempt
					('0:00:00', u'7!')
					('0:00:31', u'7!/(7(7-2)!)')
					('0:00:50', u'7!/(2!(7-2)!)')
					('0:04:52', u'7!*.5')
					('0:05:05', u'7!')
					('0:05:16', u'(7-2)!')
					('0:06:30', u'7^2')
	part1_correct_attempt
					['0:06:37', u'2^7']

68 Student ID:cstringh

	first_attempt
					2015-10-12 22:08:24
	part1_incorrect_attempt
					('0:00:00', u'12*2')
					('0:00:27', u'12!/(2!(10!))')
					('0:01:40', u'12!')
					('0:02:06', u'12! * 2')
					('0:05:21', u'12^2')
	part1_correct_attempt
					['0:05:31', u'2^12']

69 Student ID:v4sharma

	first_attempt
					2015-10-14 01:02:15
	part1_incorrect_attempt
					('0:00:00', u'C(15, 7)')
	part1_correct_attempt
					['0:03:38', u'7^9']

70 Student ID:qfu

	first_attempt
					2015-10-10 16:05:09
	part1_incorrect_attempt
					('0:00:00', u'15*7*12')
					('0:03:03', u'C(25,11)*14!')
					('0:04:18', u'105*12')
					('0:19:53', u'C(14,12)*C(12,2)')
					('0:41:29', u'C(14,12)*C(12,1)+12')
					('0:41:59', u'P(14,12)*C(12,1)+12*2')
					('0:44:45', u'14*12+13*11+12*10+11*9+10*8+9*7+8*6+7*5+6*4+5*3+3*2+2*1')
					('0:46:20', u'14*12+13*11+12*10+11*9+10*8+9*7+8*6+7*5+6*4+5*3+3*1+2*14+13')
	part1_correct_attempt
					['0:47:46', u'12^14']

71 Student ID:yjshin

	first_attempt
					2015-10-14 09:42:18
	part1_incorrect_attempt
					('0:00:00', u'13*12*11*10*9*8*7*6*5*4*3')
					('0:00:51', u'13!/2!')
					('0:06:35', u'(13*11)*(12*10)*(11*9)*(10*8)*(9*7)*(8*6)*(7*5)*(6*4)*(5*3)*(4*2)*(3*1)')
					('0:08:48', u'13!/2!')
					('0:00:00', u'13!-2!')
					('0:09:50', u'13^11')
	part1_correct_attempt
					['1 day, 1:08:20', u'11^13']

72 Student ID:aportuga

	first_attempt
					2015-10-13 23:01:24
	part1_incorrect_attempt
					('0:00:00', u'10!')
					('0:00:00', u'10!')
					('0:00:13', u'10!-9')
					('0:00:00', u'10!/9!')
					('0:00:00', u'10*9*8*7*6*5*4*3')
					('0:00:00', u'10^9')
	part1_correct_attempt
					['4:05:57', u'9^10']

73 Student ID:bpandayk

	first_attempt
					2015-10-15 22:16:31
	part1_incorrect_attempt
					('0:00:00', u'12^14')
	part1_correct_attempt
					['0:00:18', u'4^7']

74 Student ID:hsc052

	first_attempt
					2015-10-15 05:19:39
	part1_incorrect_attempt
					('0:00:00', u'P(14,9)')
					('0:00:00', u'P(22,8)')
	part1_correct_attempt
					['0:12:53', u'9^14']

75 Student ID:v3doan

	first_attempt
					2015-10-11 01:50:42
	part1_incorrect_attempt
					('0:00:00', u'P(7,4)')
					('0:00:00', u'7 * 6 * 5 * 4')
	part1_correct_attempt
					['0:25:00', u'4^7']

76 Student ID:sghouse

	first_attempt
					2015-10-12 18:59:24
	part1_incorrect_attempt
					('0:00:00', u'15!')
					('0:00:00', u'25!/15!')
					('0:00:12', u'25!')
	part1_correct_attempt
					['1:04:35', u'9^15']

77 Student ID:k3tan

	first_attempt
					2015-10-13 05:22:40
	part1_incorrect_attempt
					('0:00:00', u'10!')
					('0:01:31', u'10!/1!')
					('0:04:19', u'10!9')
	part1_correct_attempt
					['0:08:15', u'9^10']

78 Student ID:jyc018

	first_attempt
					2015-10-12 02:19:22
	part1_incorrect_attempt
					('0:00:00', u'7^2')
	part1_correct_attempt
					['0:00:08', u'2^7']

79 Student ID:h4tu

	first_attempt
					2015-10-15 06:19:46
	part1_incorrect_attempt
					('0:00:00', u'9*8*7')
					('0:00:47', u'9*8*7/3!')
	part1_correct_attempt
					['0:04:33', u'3^9']

80 Student ID:lywong

	first_attempt
					2015-10-13 00:13:58
	part1_incorrect_attempt
					('0:00:00', u'(2^11)11!')
	part1_correct_attempt
					['0:00:54', u'2^11']

81 Student ID:jix029

	first_attempt
					2015-10-11 06:19:38
	part1_incorrect_attempt
					('0:00:00', u'11*10!')
	part1_correct_attempt
					['2 days, 13:21:29', u'10^11']

82 Student ID:hkhodada

	first_attempt
					2015-10-10 17:18:07
	part1_incorrect_attempt
					('0:00:00', u'15!')
					('0:58:34', u'15!')
					('1:28:18', u'10!*P(15,5)')
					('1:28:28', u'10!*C(15,5)')
					('0:00:00', u'C(12,3)')
					('0:00:49', u'C(9,2)')
					('0:07:09', u'C(9,3)')
					('0:00:00', u'P(9,3)')
					('0:00:00', u'P(15,5)*P(10,5)')
					('0:01:09', u'P(15,5)*C(10,5)')
					('0:00:00', u'C(25,2)')
					('0:00:09', u'C(25,3)')
					('0:02:09', u'C(25,10)')
					('0:02:31', u'P(25,10)')
					('0:06:22', u'C(15,5)')
					('0:07:21', u'P(15,10)')
					('0:07:30', u'P(15,5)')
					('0:11:01', u'P(25,15)*P(10,5)')
					('0:00:00', u'P(15,10)*P(9,5)')
					('0:00:12', u'C(15,10)*C(9,5)')
					('0:00:30', u'P(15,10)*P(9,4)')
					('0:00:00', u'15^15')
					('0:00:58', u'15^10')
	part1_correct_attempt
					['3 days, 2:22:40', u'10^15']

83 Student ID:jcl084

	first_attempt
					2015-10-13 21:16:12
	part1_incorrect_attempt
					('0:00:00', u'C(12,6)')
					('0:00:00', u'C(12+6-1, 6-1)')
					('0:00:28', u'C(12+6-1, 6-1)')
					('0:00:00', u'12*6')
					('0:00:00', u'C(12,6)')
	part1_correct_attempt
					['0:25:22', u'6^12']

84 Student ID:glcohen

	first_attempt
					2015-10-13 05:01:31
	part1_incorrect_attempt
					('0:00:00', u'14!')
					('0:00:09', u'14*4')
					('0:00:21', u'14*13*12*11')
					('0:00:00', u'14^4')
					('0:01:14', u'14!/(10!4!)')
					('0:02:36', u'14(14!/(10!4!))')
					('0:03:08', u'14(14!)')
					('0:03:31', u'14*4')
					('0:06:31', u'14^4')
	part1_correct_attempt
					['0:07:29', u'4^14']

85 Student ID:acvuong

	first_attempt
					2015-10-13 04:10:10
	part1_incorrect_attempt
					('0:00:00', u'12!/(8!)')
					('0:04:56', u'12!')
	part1_correct_attempt
					['0:07:29', u'4^12']

86 Student ID:d6he

	first_attempt
					2015-10-15 05:45:54
	part1_incorrect_attempt
					('0:00:00', u'7!')
					('0:02:10', u'7*6!')
					('0:03:37', u'7^6')
					('0:11:11', u'12!/(6!6!)')
					('0:11:42', u'12!/6!')
					('0:18:17', u'7*12!/6!')
					('0:18:31', u'7!*12!/6!')
					('0:18:50', u'7*12!/(6!6!)')
					('0:00:00', u'7*6!')
					('0:00:00', u'7^6')
	part1_correct_attempt
					['1:42:26', u'6^7']

87 Student ID:sachadal

	first_attempt
					2015-10-14 17:52:33
	part1_incorrect_attempt
					('0:00:00', u'C(12,6)')
					('0:00:12', u'P(12,6)')
					('0:03:47', u'12!/6!')
					('0:06:04', u'12*11*10*9*8*7')
					('0:09:01', u'C(12,6)*C(6,1)')
					('0:00:00', u'C(12,6)*6!')
	part1_correct_attempt
					['0:35:12', u'6^12']

88 Student ID:awollner

	first_attempt
					2015-10-11 19:58:21
	part1_incorrect_attempt
					('0:00:00', u'12!')
					('0:00:12', u'12^8')
	part1_correct_attempt
					['0:00:20', u'8^12']

89 Student ID:dcrume

	first_attempt
					2015-10-14 20:14:15
	part1_incorrect_attempt
					('0:00:00', u'14*13*12*11*10')
	part1_correct_attempt
					['1 day, 3:00:08', u'5^14']

90 Student ID:pvl001

	first_attempt
					2015-10-13 19:09:03
	part1_incorrect_attempt
					('0:00:00', u'7!')
					('0:00:00', u'7 * 6 * 5 / 3')
					('0:00:07', u'7 * 6 * 5 * 3')
	part1_correct_attempt
					['0:33:37', u'3^7']

91 Student ID:t2li

	first_attempt
					2015-10-14 06:07:51
	part1_incorrect_attempt
					('0:00:00', u'12!')
					('0:00:05', u'12!*6')
					('0:00:29', u'12!*6^12')
	part1_correct_attempt
					['0:00:36', u'6^12']

92 Student ID:dlt009

	first_attempt
					2015-10-14 01:21:35
	part1_incorrect_attempt
					('0:00:00', u'7!')
					('0:02:49', u'7!/[(7-5)!]')
					('0:03:00', u'7!/[(7-5)!5!]')
	part1_correct_attempt
					['0:09:59', u'5^7']

93 Student ID:mbl003

	first_attempt
					2015-10-15 07:01:13
	part1_incorrect_attempt
					('0:00:00', u'10!/3!')
					('0:00:33', u'10^7')
					('0:01:06', u'10!/3!')
	part1_correct_attempt
					['0:04:19', u'7^10']

94 Student ID:agoldsht

	first_attempt
					2015-10-14 02:41:48
	part1_incorrect_attempt
					('0:00:00', u'11!/8!')
					('0:00:10', u'11!/(8!3!)')
					('0:00:00', u'8!/3!')
					('0:02:05', u'11!/8!')
					('0:02:19', u'11!/8')
	part1_correct_attempt
					['0:24:16', u'8^11']

95 Student ID:n2patil

	first_attempt
					2015-10-13 16:11:15
	part1_incorrect_attempt
					('0:00:00', u'10!/(2*(8!))')
	part1_correct_attempt
					['0:00:51', u'2^10']

96 Student ID:bakang

	first_attempt
					2015-10-15 02:01:08
	part1_incorrect_attempt
					('0:00:00', u'7^6')
	part1_correct_attempt
					['0:00:13', u'6^7']

97 Student ID:ksmurlo

	first_attempt
					2015-10-13 23:11:26
	part1_incorrect_attempt
					('0:00:00', u'15*14*13*12*11*10*9')
					('0:00:25', u'15!')
					('0:00:52', u'15*7')
					('0:01:24', u'C(15,7)')
					('0:02:31', u'15!*15^7')
					('0:02:38', u'15!*7^15')
					('0:04:23', u'(15*7)')
	part1_correct_attempt
					['0:04:50', u'7^15']

98 Student ID:jeqin

	first_attempt
					2015-10-15 12:18:20
	part1_incorrect_attempt
					('0:00:00', u'7!/2!')
					('0:00:37', u'(7!/2!)*5!')
					('0:02:10', u'7*6*5*4*3*5*4*3*2*1')
					('0:04:20', u'7!/(5!2!)')
	part1_correct_attempt
					['0:06:46', u'5^7']

99 Student ID:jnatale

	first_attempt
					2015-10-15 03:51:06
	part1_incorrect_attempt
					('0:00:00', u'(11!)/8')
					('0:00:04', u'(11!)/8!')
					('0:00:24', u'11*10*9*8*7*6*5*4')
					('0:01:01', u'8*7*6*5*4*3*2*1')
	part1_correct_attempt
					['0:01:44', u'8^11']

100 Student ID:jblynch

	first_attempt
					2015-10-12 07:01:33
	part1_incorrect_attempt
					('0:00:00', u'P(12,3)')
					('0:00:14', u'C(12,3)')
					('0:01:30', u'C(14,3)')
	part1_correct_attempt
					['0:03:36', u'3^12']

101 Student ID:nnh002

	first_attempt
					2015-10-13 17:11:10
	part1_incorrect_attempt
					('0:00:00', u'14!')
					('0:00:06', u'14!/2!')
	part1_correct_attempt
					['0:00:33', u'2^14']

102 Student ID:syc078

	first_attempt
					2015-10-15 00:47:17
	part1_incorrect_attempt
					('0:00:00', u'13! 12! 11! 10! 9! 8! 7! 6! 5! 4! 3! 2! 1!')
					('0:00:23', u'13! 12! 11! 10! 9! 8! 7! 6!')
					('0:00:00', u'(13! 12! 11! 10! 9! 8! 7! 6! )')
					('0:05:40', u'(7*13)-1')
	part1_correct_attempt
					['2:02:49', u'8^13']

103 Student ID:agian

	first_attempt
					2015-10-15 07:19:33
	part1_incorrect_attempt
					('0:00:00', u'9^8')
	part1_correct_attempt
					['0:00:21', u'8^9']

104 Student ID:tol003

	first_attempt
					2015-10-14 00:01:17
	part1_incorrect_attempt
					('0:00:00', u'C(13,7)')
					('0:00:39', u'P(13,7)')
					('0:02:01', u'C(13,1)^7')
					('0:02:47', u'13^7')
					('0:04:08', u'13!/[(13-7)!]')
	part1_correct_attempt
					['0:12:53', u'7^13']

105 Student ID:skodigal

	first_attempt
					2015-10-15 00:31:54
	part1_incorrect_attempt
					('0:00:00', u'C(13,8)')
					('0:00:07', u'P(13,8)')
					('0:00:00', u'C(13,8)')
					('0:00:00', u'C(25,8)')
	part1_correct_attempt
					['0:06:51', u'8^13']

106 Student ID:aakumar

	first_attempt
					2015-10-11 01:52:35
	part1_incorrect_attempt
					('0:00:00', u'7!')
					('0:00:00', u'7^6')
	part1_correct_attempt
					['2:58:59', u'6^7']

107 Student ID:hachrist

	first_attempt
					2015-10-14 20:15:16
	part1_incorrect_attempt
					('0:00:00', u'15*13')
					('0:00:00', u'15*13')
					('0:00:21', u'15*13 +26')
	part1_correct_attempt
					['2:11:34', u'13^15']

108 Student ID:q3wen

	first_attempt
					2015-10-14 04:17:22
	part1_incorrect_attempt
					('0:00:00', u'12^10')
					('0:04:22', u'12!*10^12')
	part1_correct_attempt
					['0:08:29', u'10^12']

109 Student ID:jtfrankl

	first_attempt
					2015-10-15 20:49:07
	part1_incorrect_attempt
					('0:00:00', u'9**4')
					('0:02:52', u'9*4')
					('0:03:26', u'(9)*4')
	part1_correct_attempt
					['0:08:44', u'4**9']

110 Student ID:kmc012

	first_attempt
					2015-10-15 02:19:49
	part1_incorrect_attempt
					('0:00:00', u'(14!)/((4!)*(10!))')
					('0:00:00', u'(14!)/((3!)*(11!))')
					('0:00:00', u'11^4')
	part1_correct_attempt
					['2:30:40', u'4^11']

111 Student ID:lahawkin

	first_attempt
					2015-10-15 05:05:20
	part1_incorrect_attempt
					('0:00:00', u'12!')
					('0:00:00', u'14!/(12!*2!)')
	part1_correct_attempt
					['13:15:01', u'3^12']

112 Student ID:eyhu

	first_attempt
					2015-10-09 02:53:14
	part1_incorrect_attempt
					('0:00:00', u'9!/(9-3)!')
					('0:02:45', u'(9+(3-1))!/(9+(3-1) - 3)!')
	part1_correct_attempt
					['2:00:02', u'3^9']

113 Student ID:eaherman

	first_attempt
					2015-10-13 19:14:13
	part1_incorrect_attempt
					('0:00:00', u'15(5)')
					('0:01:02', u'C(15,5)')
					('0:02:48', u'15(5)(5)')
					('0:15:31', u'15!/(15-5)!')
					('0:16:30', u'C(19,5)')
					('0:00:00', u'15!/[5!(15-5)!]')
	part1_correct_attempt
					['7:28:32', u'5^15']

114 Student ID:asetters

	first_attempt
					2015-10-12 06:04:28
	part1_incorrect_attempt
					('0:00:00', u'8*2*7*2*6*2*5*2*4*2*3*2*2*2')
	part1_correct_attempt
					['0:01:00', u'2^8']

115 Student ID:c1sorian

	first_attempt
					2015-10-14 22:11:32
	part1_incorrect_attempt
					('0:00:00', u'13!/(11!2!)')
					('0:00:00', u'12!/(10!2!)')
					('0:01:07', u'12!')
					('0:01:29', u'12!/(11!)')
					('0:03:35', u'12!/(10!)')
					('0:03:49', u'11!/2!')
					('0:10:34', u'11!/9!')
					('0:10:51', u'12!/10!')
					('0:00:00', u'12!/11!')
					('0:01:00', u'12!/1!')
					('0:01:14', u'11!/1!')
					('0:04:40', u'12!/11!')
					('0:05:01', u'11!')
					('0:07:34', u'11!*12')
					('0:08:49', u'11!')
					('0:08:57', u'12!')
	part1_correct_attempt
					['0:57:27', u'2^11']

116 Student ID:ksrijong

	first_attempt
					2015-10-15 05:27:12
	part1_incorrect_attempt
					('0:00:00', u'C(14,6)')
					('0:00:21', u'8!')
	part1_correct_attempt
					['0:01:26', u'6^8']

117 Student ID:azkong

	first_attempt
					2015-10-15 18:37:17
	part1_incorrect_attempt
					('0:00:00', u'8*7*7*6*6*5*5*4*4*3*3*2*2*1')
					('0:00:00', u'8^7')
					('0:01:42', u'8*7*7*6*6*5*5*4*4*3*3*2*2')
					('0:01:50', u'8*7*7*6*6*5*5*4*4*3*3*2')
					('0:00:00', u'C(14, 7)')
	part1_correct_attempt
					['0:09:48', u'7^8']

118 Student ID:volim

	first_attempt
					2015-10-12 22:31:20
	part1_incorrect_attempt
					('0:00:00', u'(11!)/(3!)')
	part1_correct_attempt
					['0:01:03', u'8^11']

119 Student ID:rbdoming

	first_attempt
					2015-10-14 18:37:16
	part1_incorrect_attempt
					('0:00:00', u'C(8,6)')
					('0:03:22', u'8!/2!')
					('0:04:27', u'C(8,6)')
					('0:00:00', u'C(8,2)')
	part1_correct_attempt
					['6:36:58', u'6^8']

120 Student ID:k4ma

	first_attempt
					2015-10-15 03:09:16
	part1_incorrect_attempt
					('0:00:00', u'12!')
					('0:03:29', u'12^11')
	part1_correct_attempt
					['0:03:37', u'11^12']

121 Student ID:ralhadda

	first_attempt
					2015-10-15 18:04:15
	part1_incorrect_attempt
					('0:00:00', u'11*10')
					('0:02:45', u'11*11')

122 Student ID:cagatep

	first_attempt
					2015-10-14 02:43:59
	part1_incorrect_attempt
					('0:00:00', u'10!/(8!2!)')
					('0:00:00', u'10!/(2!)')
					('0:00:37', u'10!/(8!)')
	part1_correct_attempt
					['0:02:14', u'8^10']

123 Student ID:ytc012

	first_attempt
					2015-10-14 22:27:28
	part1_incorrect_attempt
					('0:00:00', u'13^15')
	part1_correct_attempt
					['0:00:12', u'9^12']

124 Student ID:tjke

	first_attempt
					2015-10-11 21:42:56
	part1_incorrect_attempt
					('0:00:00', u'14!(14-10)!')
					('0:00:12', u'C(14,10)')
	part1_correct_attempt
					['0:01:12', u'10^14']

125 Student ID:klala

	first_attempt
					2015-10-12 04:16:11
	part1_incorrect_attempt
					('0:00:00', u'12!')
					('0:00:53', u'12^7')
	part1_correct_attempt
					['0:01:10', u'7^12']

126 Student ID:asp025

	first_attempt
					2015-10-15 07:07:34
	part1_incorrect_attempt
					('0:00:00', u'14*13*12*11*10*9*8*7*6')
					('0:01:11', u'14!/(14-9)!')
					('0:01:29', u'14!/(9!(14-9)!)')
					('0:00:00', u'14^9')
					('0:00:00', u'22!/(9!13!)')
					('0:00:57', u'14!/(9!5!)')
	part1_correct_attempt
					['11:36:13', u'9^14']

127 Student ID:dlgoldbe

	first_attempt
					2015-10-13 01:14:46
	part1_incorrect_attempt
					('0:00:00', u'10!-2')
					('0:00:29', u'10!')
					('0:01:24', u'10!/(8!*(2!))')
					('0:02:34', u'(10*8)!')
					('0:02:59', u'(10*9*8*7*6*5*4*3)')
					('0:03:40', u'10!*8!')
					('0:04:25', u'(10!-2!)*8!')
	part1_correct_attempt
					['1 day, 23:11:13', u'8^10']

128 Student ID:fichoi

	first_attempt
					2015-10-14 02:42:18
	part1_incorrect_attempt
					('0:00:00', u'11!')
					('0:00:00', u'11!/(11-6)!')
					('0:00:15', u'11!/(11-6)!6!')
					('0:00:00', u'11!/((11-6)!6!)')
					('0:00:00', u'11^6')
	part1_correct_attempt
					['0:05:46', u'6^11']

129 Student ID:kquong

	first_attempt
					2015-10-10 23:56:10
	part1_incorrect_attempt
					('0:00:00', u'13 * 9')
					('0:00:20', u'13!/(13-9)!')
					('0:00:56', u'13!/4!(13-9)!')
					('0:00:00', u'13!/(13-4)!')
					('0:02:19', u'21!/(21-9)!')
					('0:03:37', u'21!/(9!*(21-9)!)')
					('0:07:24', u'21!/(13*(21-13)!)')
					('0:07:35', u'21!/(12*(21-12)!)')
	part1_correct_attempt
					['4:18:58', u'9^13']

130 Student ID:jfalcone

	first_attempt
					2015-10-14 22:27:29
	part1_incorrect_attempt
					('0:00:00', u'8*7*6*5')
					('0:00:00', u'8!')
	part1_correct_attempt
					['0:04:26', u'4^8']

131 Student ID:ielouaae

	first_attempt
					2015-10-15 07:45:36
	part1_incorrect_attempt
					('0:00:00', u'13!/12!')
					('0:01:12', u'13!')
					('0:01:19', u'13!-1')
					('0:02:55', u'13!')
					('0:35:29', u'13!/12')
					('0:40:30', u'25!/(12!13!)')
					('0:50:12', u'24!/(12!12!)')
					('0:53:46', u'13!12!')
					('0:00:00', u'24!/(13!11!)')
					('0:00:00', u'24!/13!')
					('0:04:27', u'24!/13!')
					('0:06:54', u'13*12')
	part1_correct_attempt
					['1:08:10', u'12^13']

132 Student ID:t2shin

	first_attempt
					2015-10-15 05:32:17
	part1_incorrect_attempt
					('0:00:00', u'11!/7!')
					('0:00:18', u'11^4')
					('0:00:50', u'11*10*9*8')
					('0:02:11', u'11!/(4!7!)')
	part1_correct_attempt
					['0:02:31', u'4^11']

133 Student ID:vsamant

	first_attempt
					2015-10-10 01:37:46
	part1_incorrect_attempt
					('0:00:00', u'P(9,6)')
					('0:00:13', u'C(9,6)')
					('0:00:00', u'9*8*7*6*5*4')
	part1_correct_attempt
					['14:38:49', u'6^9']

134 Student ID:dcastlem

	first_attempt
					2015-10-15 03:58:29
	part1_incorrect_attempt
					('0:00:00', u'10!/3!')
					('0:00:15', u'10!/((3!)(7!))')
					('0:00:56', u'10!/3!')
					('0:00:00', u'12!/((3!)(9!))')
					('0:01:17', u'12!/((3!))')
	part1_correct_attempt
					['12:48:09', u'3^10']

135 Student ID:ppanourg

	first_attempt
					2015-10-15 07:09:35
	part1_incorrect_attempt
					('0:00:00', u'C(8,1)*C(7,1)*C(6,1)*C(5,1)*C(4,1)*C(3,1)*C(2,1)*C(1,1)')
					('0:00:21', u'8!')
					('0:00:00', u'C(11,3)')
	part1_correct_attempt
					['0:12:12', u'(C(4,1))^8']

136 Student ID:qtluong

	first_attempt
					2015-10-12 20:06:08
	part1_incorrect_attempt
					('0:00:00', u'11!')
	part1_correct_attempt
					['0:01:50', u'9^11']

137 Student ID:spw006

	first_attempt
					2015-10-13 21:18:19
	part1_incorrect_attempt
					('0:00:00', u'10!')
					('0:00:31', u'10!(8!2!)')
					('0:00:36', u'10!/(8!2!)')
					('0:00:00', u'10!/(8!)')
					('0:00:26', u'10!/(2!)')
					('0:02:14', u'C(10,8) * 8')
					('0:03:51', u'10!/2!* 8')
					('0:15:15', u'10!/(8!2!)')
	part1_correct_attempt
					['2:14:56', u'8^10']

138 Student ID:any027

	first_attempt
					2015-10-12 19:49:45
	part1_incorrect_attempt
					('0:00:00', u'C(14, 10)')
					('0:00:16', u'14!')
					('0:01:53', u'14! / 4!')
					('0:08:12', u'14^10')
	part1_correct_attempt
					['0:08:20', u'10^14']

139 Student ID:rwthomps

	first_attempt
					2015-10-11 22:22:45
	part1_incorrect_attempt
					('0:00:00', u'11!/(11 - 9)!')
					('0:02:00', u'11 * 10 * 8 * 7 * 6 * 5 * 4 * 3 * 2')
					('0:03:48', u'(11 * 9) + (10 * 8) + (9 * 7) + (8 * 6) + (7 * 5) + (6 * 4) + (5 * 3) + (4 * 2) + (3 * 1)')
					('0:04:58', u'11 * 10 * 8 * 7 * 6 * 5 * 4 * 3')
					('0:07:15', u'(11 * 9) * (10 * 8) * (9 * 7) * (8 * 6) * (7 * 5) * (6 * 4) * (5 * 3) * (4 * 2) * (3 * 1)')
					('0:14:22', u'11 * 9')
					('0:16:14', u'C(19, 9)')
	part1_correct_attempt
					['0:22:32', u'9^11']

140 Student ID:syip

	first_attempt
					2015-10-11 00:52:34
	part1_incorrect_attempt
					('0:00:00', u'P(9,6)')
	part1_correct_attempt
					['0:00:37', u'6^9']

141 Student ID:pcdo

	first_attempt
					2015-10-13 20:47:44
	part1_incorrect_attempt
					('0:00:00', u'C(12,5)')
					('0:00:10', u'12*5')
					('0:01:20', u'P(12,5)')
					('0:02:41', u'C(10, 4)')
					('0:04:19', u'C(16, 5)')
					('0:00:00', u'12!')
					('0:00:00', u'C(16,4)')
					('0:01:06', u'P(12,5)/5')
					('0:01:11', u'P(12,5)')
					('0:00:00', u'6^10')
	part1_correct_attempt
					['0:55:24', u'5^12']

142 Student ID:vsosnovs

	first_attempt
					2015-10-15 04:02:33
	part1_incorrect_attempt
					('0:00:00', u'13!')
					('0:00:30', u'13^2')
					('0:00:40', u'13*12')
					('0:02:53', u'C(13,2)')
					('0:05:18', u'13!/2')
	part1_correct_attempt
					['0:06:03', u'2^13']

143 Student ID:k5law

	first_attempt
					2015-10-12 01:38:40
	part1_incorrect_attempt
					('0:00:00', u'(9+4-1)!/(4-1)!')
					('0:00:10', u'(9+4-1)!/(4)!')
					('0:00:20', u'(9+4-1)!')
					('0:00:00', u'[(9+4-1)!]/(9!)')
					('0:00:17', u'[(9+4-1)!]/(4!)')
					('0:00:22', u'[(9+4-1)!]/(3!)')
					('0:00:37', u'[(9+4-1)!]/(12!)')
					('0:01:24', u'[(9+4-1)!]/(3!)')
					('0:02:51', u'8!/(3!5!)')
					('0:03:13', u'8!/(4!4!)')
					('0:06:11', u'12!/(9!3!)')
					('0:06:29', u'12!/(3!)')
					('0:06:35', u'12!/(4!)')
					('0:07:03', u'12!')
					('0:07:09', u'9!')
					('0:07:37', u'(9!^4)')
					('0:07:53', u'9*8*7*6')
	part1_correct_attempt
					['1:52:57', u'4^9']

144 Student ID:p4kumar

	first_attempt
					2015-10-15 08:40:08
	part1_incorrect_attempt
					('0:00:00', u'(15!)/(15-7)!')
					('0:00:00', u'15^7')
	part1_correct_attempt
					['0:03:32', u'7^15']

145 Student ID:s2chaudh

	first_attempt
					2015-10-13 00:09:09
	part1_incorrect_attempt
					('0:00:00', u'C(13,8)')
					('0:00:35', u'13*12*11*10*9*8*7*6')
					('0:02:24', u'P(13,8)')
					('0:00:00', u'C(20,7)')
					('0:01:48', u'C(20,12)')
					('0:02:07', u'C(20,7)')
					('0:04:07', u'P(13,8)')
					('0:04:15', u'C(13,8)')
					('0:05:53', u'13!/8!(13-8)!')
	part1_correct_attempt
					['19:17:25', u'8^13']

146 Student ID:jmiclat

	first_attempt
					2015-10-15 17:10:18
	part1_incorrect_attempt
					('0:00:00', u'12!')
					('0:00:58', u'12*11*10*9*8*7*6*5*4*3*2')
					('0:07:16', u'22!/(11!11!)')
					('0:00:00', u'12!')
	part1_correct_attempt
					['2:45:57', u'11^12']

147 Student ID:gsrandha

	first_attempt
					2015-10-12 06:55:40
	part1_incorrect_attempt
					('0:00:00', u'13!')
					('0:00:11', u'13*12*11')
					('0:00:23', u'13!/10!')
					('0:00:00', u'13*12*11')
	part1_correct_attempt
					['2 days, 23:09:20', u'3^13']

148 Student ID:jhc010

	first_attempt
					2015-10-15 15:55:22
	part1_incorrect_attempt
					('0:00:00', u'13^12')
					('0:00:08', u'13!')
					('0:00:25', u'13!/2')
	part1_correct_attempt
					['0:00:58', u'12^13']

149 Student ID:cfgutier

	first_attempt
					2015-10-15 23:08:39
	part1_incorrect_attempt
					('0:00:00', u'11*10*9')
					('0:01:01', u'11!')
					('0:01:28', u'11! *3')
					('0:01:35', u'11! *3!')
					('0:02:18', u'11! 3^11')
	part1_correct_attempt
					['0:04:29', u'3^11']

150 Student ID:dkostins

	first_attempt
					2015-10-15 18:26:11
	part1_incorrect_attempt
					('0:00:00', u'14^11')
	part1_correct_attempt
					['0:00:09', u'11^14']

151 Student ID:pnquach

	first_attempt
					2015-10-15 02:15:26
	part1_incorrect_attempt
					('0:00:00', u'10!/4!')
	part1_correct_attempt
					['0:12:32', u'6^10']

152 Student ID:agarango

	first_attempt
					2015-10-15 19:01:43
	part1_incorrect_attempt
					('0:00:00', u'12!')
	part1_correct_attempt
					['0:02:37', u'6^12']

153 Student ID:achinn

	first_attempt
					2015-10-12 23:39:30
	part1_incorrect_attempt
					('0:00:00', u'10!')
					('0:00:00', u'10^5')
	part1_correct_attempt
					['0:54:09', u'5^10']

154 Student ID:jap009

	first_attempt
					2015-10-15 21:17:58
	part1_incorrect_attempt
					('0:00:00', u'7*6*5*4*3')
					('0:13:49', u'4!')
					('0:14:31', u'7!')
					('0:16:18', u'11!/(7!4!)')
					('0:19:13', u'11!/4!')
	part1_correct_attempt
					['0:19:47', u'5^7']

155 Student ID:kalang

	first_attempt
					2015-10-13 15:16:47
	part1_incorrect_attempt
					('0:00:00', u'10!/3!')
					('0:01:44', u'C(17,7)')
					('0:00:00', u'17!')
					('0:00:17', u'10!*7!')
					('0:00:00', u'10^7')
	part1_correct_attempt
					['14:41:46', u'7^10']

156 Student ID:msaguiar

	first_attempt
					2015-10-14 03:08:15
	part1_incorrect_attempt
					('0:00:00', u'C(8,1)')
	part1_correct_attempt
					['1:05:13', u'2^7']

157 Student ID:aalhaida

	first_attempt
					2015-10-15 17:26:51
	part1_incorrect_attempt
					('0:00:00', u'10*9*8*7*6*5*4')
	part1_correct_attempt
					['0:00:18', u'7^10']

158 Student ID:hah008

	first_attempt
					2015-10-13 06:12:47
	part1_incorrect_attempt
					('0:00:00', u'7*6*5*4')
	part1_correct_attempt
					['0:01:47', u'4^7']

159 Student ID:haliew

	first_attempt
					2015-10-13 23:52:07
	part1_incorrect_attempt
					('0:00:00', u'C(9,2)')
					('0:00:00', u'9*9')
					('0:00:21', u'9*8')
					('0:04:08', u'C(9,2)^2')
					('0:00:00', u'9^4*8^3*7^2*6')
					('0:00:45', u'9^4*8^3*7^2*6+1')
	part1_correct_attempt
					['1:17:07', u'2^9']

160 Student ID:ajabasa

	first_attempt
					2015-10-14 06:34:30
	part1_incorrect_attempt
					('0:00:00', u'10!/2!')
					('0:06:57', u'10!/(8!)')
					('0:07:25', u'10!/(8!*2!)')
	part1_correct_attempt
					['0:08:07', u'8^10']

161 Student ID:aadhakal

	first_attempt
					2015-10-13 02:17:13
	part1_incorrect_attempt
					('0:00:00', u'14*7')
	part1_correct_attempt
					['1 day, 2:44:20', u'7^14']

162 Student ID:mtrafeca

	first_attempt
					2015-10-11 05:46:02
	part1_incorrect_attempt
					('0:00:00', u'7!*2')
					('0:00:34', u'7!/(5!*2!)')
	part1_correct_attempt
					['0:07:38', u'2^7']

163 Student ID:acs008

	first_attempt
					2015-10-15 06:05:17
	part1_incorrect_attempt
					('0:00:00', u'10!')

164 Student ID:hmshah

	first_attempt
					2015-10-14 02:11:59
	part1_incorrect_attempt
					('0:00:00', u'8*7*6*5*4')
					('0:00:50', u'C(8,5)')
					('0:01:53', u'8^5')
	part1_correct_attempt
					['0:02:03', u'5^8']

165 Student ID:dtea

	first_attempt
					2015-10-15 22:55:36
	part1_incorrect_attempt
					('0:00:00', u'15!')
					('0:02:06', u'22!/(15!(22-15)!)')
					('0:03:08', u'27!/(15!(27-15)!)')
					('0:04:45', u'27!/(13!(27-13)!)')
					('0:05:30', u'15!')
					('0:05:52', u'15!/(13!(15-13)!)')
					('0:00:00', u'15!/(13!(15-13)!)')
					('0:00:00', u'15^13')
	part1_correct_attempt
					['0:18:26', u'13^15']

166 Student ID:daw023

	first_attempt
					2015-10-15 05:21:22
	part1_incorrect_attempt
					('0:00:00', u'15!')
					('0:00:00', u'15^2')
	part1_correct_attempt
					['1:34:53', u'2^15']

167 Student ID:edcole

	first_attempt
					2015-10-10 18:49:59
	part1_incorrect_attempt
					('0:00:00', u'13!/(5!*6!)')
					('0:00:00', u'13!/(5!*8!)')
					('0:03:36', u'13*12*11*10*9')
					('0:00:00', u'13!/(5!*8!)')
					('0:00:00', u'13!/5!')
					('0:00:27', u'13!/(5!8!)')
					('0:00:00', u'(13!/5!8!) + (8!/5!3!) + (3*2*1)')
					('0:00:29', u'(13!/(5!8!)) + (8!/(5!3!)) + (3*2*1)')
	part1_correct_attempt
					['4 days, 7:56:11', u'5^13']

168 Student ID:aordookh

	first_attempt
					2015-10-15 20:31:52
	part1_incorrect_attempt
					('0:00:00', u'C(14,2)')
					('0:05:33', u'13!')
	part1_correct_attempt
					['0:05:43', u'2^13']

169 Student ID:r2fisher

	first_attempt
					2015-10-14 22:55:23
	part1_incorrect_attempt
					('0:00:00', u'10!/(4!*6!)')
					('0:00:10', u'10!/4!')
					('0:00:28', u'10^4')
	part1_correct_attempt
					['0:00:36', u'4^10']

170 Student ID:vasharma

	first_attempt
					2015-10-10 05:00:51
	part1_incorrect_attempt
					('0:00:00', u'29!/[9!(29-9)!]')
					('0:00:00', u'C(11,9)')
					('0:00:21', u'11!/(11-9)!')
					('0:00:39', u'11!/(9!(11-9)!)')
					('0:04:48', u'C(11,9)')
					('0:07:26', u'(11!/2!)9!')
					('0:07:35', u'(11!/2!)')
					('0:07:56', u'(11!/2!)C(9,1)')
					('0:09:10', u'(11!)')
					('0:14:49', u'11!/9!')
					('0:17:06', u'11!/3!')
					('0:19:56', u'9!11!')
					('0:20:43', u'(11*10*9*8*7*6*5*3*2)(9*8*7*6*5*4*3*2*1)')
					('0:00:00', u'11!/9!')
					('0:00:05', u'11!/2!')
					('0:00:20', u'C(20,9)')
					('0:01:31', u'9!11!')
					('0:01:36', u'11!')
					('0:01:42', u'11!/2!')
					('0:02:35', u'C(19,9)')
					('0:00:00', u'P(11,9)')
					('0:00:05', u'P(11,2)')
					('0:00:15', u'P(20,9)')
					('0:00:00', u'P(20,9)')
					('0:00:05', u'C(20,9)')
					('0:06:21', u'11*9')
					('0:07:02', u'11!/3!')
					('0:10:27', u'11^9')
	part1_correct_attempt
					['1 day, 1:29:26', u'9^11']

171 Student ID:hpc001

	first_attempt
					2015-10-14 21:21:44
	part1_incorrect_attempt
					('0:00:00', u'C(27,13)')
					('0:01:07', u'14!')
					('0:04:31', u'14!/2')
					('0:07:15', u'14^13')
	part1_correct_attempt
					['0:07:34', u'13^14']

172 Student ID:kgrozav

	first_attempt
					2015-10-15 18:54:50
	part1_incorrect_attempt
					('0:00:00', u'9^8')
	part1_correct_attempt
					['0:00:34', u'8^9']

173 Student ID:xweng

	first_attempt
					2015-10-12 22:33:48
	part1_incorrect_attempt
					('0:00:00', u'10!*2^10')
	part1_correct_attempt
					['0:00:20', u'2^10']

174 Student ID:yypan

	first_attempt
					2015-10-12 20:31:22
	part1_incorrect_attempt
					('0:00:00', u'C(13,3)')
					('0:00:27', u'P(13,3)')
	part1_correct_attempt
					['0:01:05', u'3^11']

175 Student ID:ajvanega

	first_attempt
					2015-10-15 00:46:31
	part1_incorrect_attempt
					('0:00:00', u'8!/(2!6!)')
					('0:00:00', u'9!/(2!7!)')
					('0:00:00', u'8^2')
	part1_correct_attempt
					['0:14:19', u'2^8']

176 Student ID:sthapa

	first_attempt
					2015-10-15 04:38:37
	part1_incorrect_attempt
					('0:00:00', u'14*12')
					('0:00:40', u'14*C(14,12)')
					('0:11:16', u'14*C(12,1)')
					('0:00:00', u'14*C(25,12)')
					('0:00:07', u'14*C(25,1)')
					('0:00:40', u'C(25,12)')
					('0:01:01', u'14*C(25,14)')
					('0:02:12', u'14*12')
	part1_correct_attempt
					['0:20:13', u'12^14']

177 Student ID:mjethani

	first_attempt
					2015-10-13 05:59:38
	part1_incorrect_attempt
					('0:00:00', u'13!')
					('0:00:00', u'13^5')
	part1_correct_attempt
					['1 day, 20:52:40', u'5^13']

178 Student ID:kosung

	first_attempt
					2015-10-15 06:21:04
	part1_incorrect_attempt
					('0:00:00', u'9!/2!')
					('0:08:18', u'7! + 42')
					('0:08:53', u'7! *42')
					('0:11:07', u'36 * 21 * 7!')
	part1_correct_attempt
					['1:05:51', u'7^9']

179 Student ID:whcombs

	first_attempt
					2015-10-13 02:53:30
	part1_incorrect_attempt
					('0:00:00', u'(1/3)*9!')
					('0:00:22', u'9!')
					('0:10:28', u'9*3')
					('0:22:30', u'9*3*3')
	part1_correct_attempt
					['0:40:33', u'3^9']

180 Student ID:j2phung

	first_attempt
					2015-10-14 02:57:35
	part1_incorrect_attempt
					('0:00:00', u'7*6*5*4')
					('0:00:00', u'7!/(3!4!)')
	part1_correct_attempt
					['1:39:19', u'4^7']












## Part 2

### (103) Mistake Group Digits of size 103




### (72) Mistake Group ['R.0'] of size 72
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(10+6-1,10)	|C(15, 9)	|[('R.0', 15.0, u'10+6-1', u'15')]	|
|1	|C(8+3-1,8)	|C(10,3)	|[('R.0', 10.0, u'8+3-1', u'10')]	|
|2	|C(9+6-1,9)	|C(14,6)	|[('R.0', 14.0, u'9+6-1', u'14')]	|
|3	|C(15+4-1,15)	|C(18,4)	|[('R.0', 18.0, u'15+4-1', u'18')]	|
|4	|C(11+6-1,11)	|C(16,6)	|[('R.0', 16.0, u'11+6-1', u'16')]	|
|5	|C(10+4-1,10)	|C(13,4)	|[('R.0', 13.0, u'10+4-1', u'13')]	|
|6	|C(9+6-1,9)	|C(14,3)	|[('R.0', 14.0, u'9+6-1', u'14')]	|
|7	|C(11+3-1,11)	|C(13,3)	|[('R.0', 13.0, u'11+3-1', u'13')]	|
|8	|C(8+5-1,8)	|C(12,5)	|[('R.0', 12.0, u'8+5-1', u'12')]	|
|9	|C(7+4-1,7)	|C(10,4)	|[('R.0', 10.0, u'7+4-1', u'10')]	|
|10	|C(7+6-1,7)	|C(12,6)	|[('R.0', 12.0, u'7+6-1', u'12')]	|
|11	|C(12+8-1,12)	|C(19,8)	|[('R.0', 19.0, u'12+8-1', u'19')]	|
|12	|C(15+10-1,15)	|C(24,12)	|[('R.0', 24.0, u'15+10-1', u'24')]	|
|13	|C(15+10-1,15)	|C(24,21)	|[('R.0', 24.0, u'15+10-1', u'24')]	|
|14	|C(15+10-1,15)	|C(24,10)	|[('R.0', 24.0, u'15+10-1', u'24')]	|
|15	|C(15+10-1,15)	|P(24,10)	|[('R.0', 24.0, u'15+10-1', u'24')]	|
|16	|C(12+11-1,12)	|C(22,11)	|[('R.0', 22.0, u'12+11-1', u'22')]	|
|17	|C(14+10-1,14)	|C( 23, 10)	|[('R.0', 23.0, u'14+10-1', u'23')]	|
|18	|C(11+2-1,11)	|C(12,2)	|[('R.0', 12.0, u'11+2-1', u'12')]	|
|19	|C(11+2-1,11)	|C(12,10)	|[('R.0', 12.0, u'11+2-1', u'12')]	|
|20	|C(12+4-1,12)	|C(15,4)	|[('R.0', 15.0, u'12+4-1', u'15')]	|
|21	|C(15+7-1,15)	|C(21,7)	|[('R.0', 21.0, u'15+7-1', u'21')]	|
|22	|C(13+7-1,13)	|C(19,7)	|[('R.0', 19.0, u'13+7-1', u'19')]	|
|23	|C(9+7-1,9)	|C(15, 7)	|[('R.0', 15.0, u'9+7-1', u'15')]	|
|24	|C(9+2-1,9)	|C(10,2)	|[('R.0', 10.0, u'9+2-1', u'10')]	|
|25	|C(8+6-1,8)	|C(13,6)	|[('R.0', 13.0, u'8+6-1', u'13')]	|
|26	|C(15+5-1,15)	|C(19,5)	|[('R.0', 19.0, u'15+5-1', u'19')]	|
|27	|C(8+4-1,8)	|C(11,7)	|[('R.0', 11.0, u'8+4-1', u'11')]	|
|28	|C(10+5-1,10)	|C(14,5)	|[('R.0', 14.0, u'10+5-1', u'14')]	|
|29	|C(10+5-1,10)	|C(14,9)	|[('R.0', 14.0, u'10+5-1', u'14')]	|
|30	|C(11+3-1,11)	|P(13,3)	|[('R.0', 13.0, u'11+3-1', u'13')]	|
|31	|C(11+7-1,11)	|C(17,7)	|[('R.0', 17.0, u'11+7-1', u'17')]	|
|32	|C(11+2-1,11)	|12!	|[('R.0', 12.0, u'11+2-1', u'12')]	|
|33	|C(10+7-1,10)	|C(16,7)	|[('R.0', 16.0, u'10+7-1', u'16')]	|
|34	|C(13+8-1,13)	|C(20,8)	|[('R.0', 20.0, u'13+8-1', u'20')]	|
|35	|C(13+3-1,13)	|C(15,9)	|[('R.0', 15.0, u'13+3-1', u'15')]	|
|36	|C(11+8-1,11)	|C(18,8)	|[('R.0', 18.0, u'11+8-1', u'18')]	|
|37	|C(13+2-1,13)	|C(14,2)	|[('R.0', 14.0, u'13+2-1', u'14')]	|
|38	|C(14+9-1,14)	|C(22,9)	|[('R.0', 22.0, u'14+9-1', u'22')]	|
|39	|C(8+5-1,8)	|P(12,5)	|[('R.0', 12.0, u'8+5-1', u'12')]	|
|40	|C(15+2-1,15)	|C(16,2)	|[('R.0', 16.0, u'15+2-1', u'16')]	|
|41	|C(15+13-1,15)	|C(15+13-1, 13)	|[('R.0', 27.0, u'15+13-1', u'15+13-1')]	|
|42	|C(15+13-1,15)	|C(27, 13)	|[('R.0', 27.0, u'15+13-1', u'27')]	|
|43	|C(8+4-1,8)	|C(11,4)	|[('R.0', 11.0, u'8+4-1', u'11')]	|
|44	|C(10+3-1,10)	|C(12,3)	|[('R.0', 12.0, u'10+3-1', u'12')]	|
|45	|C(12+6-1,12)	|C(17,6)	|[('R.0', 17.0, u'12+6-1', u'17')]	|
|46	|C(10+7-1,10)	|C(16,9)	|[('R.0', 16.0, u'10+7-1', u'16')]	|
|47	|C(12+5-1,12)	|C(12+5-1,5)	|[('R.0', 16.0, u'12+5-1', u'12+5-1')]	|
|48	|C(12+5-1,12)	|C(16,5)	|[('R.0', 16.0, u'12+5-1', u'16')]	|
|49	|C(8+7-1,8)	|C(14, 7)	|[('R.0', 14.0, u'8+7-1', u'14')]	|
|50	|C(13+3-1,13)	|C(15,3)	|[('R.0', 15.0, u'13+3-1', u'15')]	|
|51	|C(7+4-1,7)	|C(4+7-1,4)	|[('R.0', 10.0, u'7+4-1', u'4+7-1')]	|




### (31) Mistake Group Fraction of size 31




### (21) Mistake Group ['R.0.0'] of size 21
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(13+5-1,13)	|(13+5)!/(13!*5!)	|[('R.0.0', 18.0, u'13+5', u'13+5')]	|
|1	|C(9+4-1,9)	|C(13,4)*C(9,4)	|[('R.0.0', 13.0, u'9+4', u'13')]	|
|2	|C(9+5-1,9)	|14!/(5!*9!)	|[('R.0.0', 14.0, u'9+5', u'14')]	|
|3	|C(11+10-1,11)	|21!/(11!*10!)	|[('R.0.0', 21.0, u'11+10', u'21')]	|
|4	|C(15+14-1,15)	|(14+15)! / (15!*14!)	|[('R.0.0', 29.0, u'15+14', u'14+15')]	|
|5	|C(11+2-1,11)	|13!/((2!)(11!))	|[('R.0.0', 13.0, u'11+2', u'13')]	|
|6	|C(12+4-1,12)	|16!/(12!*4!)	|[('R.0.0', 16.0, u'12+4', u'16')]	|
|7	|C(12+9-1,12)	|21!/9!	|[('R.0.0', 21.0, u'12+9', u'21')]	|
|8	|C(8+5-1,8)	|13!/(5!8!)	|[('R.0.0', 13.0, u'8+5', u'13')]	|
|9	|C(8+5-1,8)	|13!/(7!5!)	|[('R.0.0', 13.0, u'8+5', u'13')]	|
|10	|C(11+4-1,11)	|15!/(4!*11!)	|[('R.0.0', 15.0, u'11+4', u'15')]	|
|11	|C(12+9-1,12)	|21!/(9!12!)	|[('R.0.0', 21.0, u'12+9', u'21')]	|
|12	|C(12+9-1,12)	|21!/(9!)	|[('R.0.0', 21.0, u'12+9', u'21')]	|
|13	|C(12+9-1,12)	|21!/12!	|[('R.0.0', 21.0, u'12+9', u'21')]	|
|14	|C(13+12-1,13)	|25!/(12!13!)	|[('R.0.0', 25.0, u'13+12', u'25')]	|
|15	|C(12+9-1,12)	|21!/(12!9!)	|[('R.0.0', 21.0, u'12+9', u'21')]	|
|16	|C(10+3-1,10)	|13!/((3!))	|[('R.0.0', 13.0, u'10+3', u'13')]	|
|17	|C(10+3-1,10)	|13!/((10!))	|[('R.0.0', 13.0, u'10+3', u'13')]	|




### (8) Mistake Group ['R.0.0.0'] of size 8
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(9+3-1,9)	|(9 + (3-1))! / ((9 + (3-1))-9)!	|[('R.0.0.0', 9.0, u'9', u'9')]	|
|1	|C(9+4-1,9)	|C(9,4)*C(8,4)*4	|[('R.0.0.0', 9.0, u'9', u'9')]	|
|2	|C(14+4-1,14)	|14*13*12*11	|[('R.0.0.0', 14.0, u'14', u'14')]	|
|3	|C(7+2-1,7)	|7!/2!(7-2)!	|[('R.0.0.0', 7.0, u'7', u'7')]	|
|4	|C(13+5-1,13)	|(13+4)!/(12!*5!)	|[('R.0.0.0', 13.0, u'13', u'13')]	|
|5	|C(8+4-1,8)	|8*7*6*5	|[('R.0.0.0', 8.0, u'8', u'8')]	|
|6	|C(10+3-1,10)	|(10*9*8)/(3!)	|[('R.0.0.0', 10.0, u'10', u'10')]	|




### (1) Mistake Group ['R.0.0.0', 'R.0.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0', 'R.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(12+4-1,12)	|C(12+3-1, 3-1)	|[('R.0.0.0', 12.0, u'12', u'12'), ('R.0.1', 1.0, u'1', u'1')]	|




### (1) Mistake Group ['R.0.0', 'R.0.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(12+5-1,12)	|C(12+5+1,5)	|[('R.0.0', 17.0, u'12+5', u'12+5'), ('R.0.1', 1.0, u'1', u'1')]	|




### (1) Mistake Group ['R.0.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(11+3-1,11)	|C(11,1)C(3,1)	|[('R.0.1', 1.0, u'1', u'1')]	|




### (137) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:v4zhang

	first_attempt
					2015-10-15 06:57:51
	part2_incorrect_attempt
					('-1 day, 23:56:00', u'C(15, 13)')
					('-1 day, 23:59:12', u'C(14, 13)')
					('0:10:57', u'C(29, 13)')
					('0:11:07', u'C(28, 13)')
	part2_correct_attempt
					['0:11:27', u'C(27, 15)']

1 Student ID:kvass

	first_attempt
					2015-10-14 05:03:18
	part2_incorrect_attempt
					('0:00:36', u'C(14,8)')
	part2_correct_attempt
					['0:04:51', u'C(14+8-1,8-1)']

2 Student ID:jguanzho

	first_attempt
					2015-10-09 21:27:45
	part2_incorrect_attempt
					('-1 day, 22:35:03', u'13!/(10!*3!)')
					('-1 day, 22:37:01', u'15!/(10!*3!)')
					('-1 day, 23:56:48', u'12!/(2!)')
					('-1 day, 23:57:12', u'15!/(2!)')
	part2_correct_attempt
					['-1 day, 23:57:20', u'15!/(2!*13!)']

3 Student ID:ctgraves

	first_attempt
					2015-10-13 21:41:12
	part2_incorrect_attempt
					('0:01:37', u'13!/(4!*9!)')
					('0:02:03', u'13!/(9!)')
					('0:02:31', u'13!/(4!*(13-4)!)')
					('0:03:27', u'12!/(3!(12-3)!)')
					('0:04:15', u'13!/(4!(13-4)!)')
	part2_correct_attempt
					['0:04:27', u'13!/(10!(13-10)!)']

4 Student ID:nhn018

	first_attempt
					2015-10-15 19:52:52
	part2_incorrect_attempt
					('0:02:37', u'14!/11!')
	part2_correct_attempt
					['0:04:05', u'364']

5 Student ID:j5phung

	first_attempt
					2015-10-09 18:20:19
	part2_incorrect_attempt
					('0:02:08', u'13!/3!')
					('6 days, 1:30:00', u'C(12,10)')
	part2_correct_attempt
					['6 days, 1:30:35', u'C(15,13)']

6 Student ID:haw081

	first_attempt
					2015-10-15 02:54:01
	part2_incorrect_attempt
					('-1 day, 1:46:29', u'7!*C(10,7)')
	part2_correct_attempt
					['0:03:39', u'C(16,6)']

7 Student ID:airanmeh

	first_attempt
					2015-10-15 23:44:36
	part2_incorrect_attempt
					('0:00:17', u'20!(5!15!)')
					('0:00:27', u'20!(6!14!)')

8 Student ID:ffhaddad

	first_attempt
					2015-10-10 20:59:30
	part2_incorrect_attempt
					('0:04:05', u'13!/(8!5!)')
	part2_correct_attempt
					['0:04:44', u'13!/(4!9!)']

9 Student ID:jmmcalex

	first_attempt
					2015-10-15 07:43:46
	part2_incorrect_attempt
					('-1 day, 23:56:04', u'12!/[2!10!]')
					('0:01:23', u'12!/[2!]')
					('0:03:06', u'21!/[11!10!]')
	part2_correct_attempt
					['0:04:02', u'21!/[12!9!]']

10 Student ID:pthsu

	first_attempt
					2015-10-10 19:59:33
	part2_incorrect_attempt
					('0:10:37', u'C(15,8)')
					('0:10:49', u'C(15,11)')
	part2_correct_attempt
					['1:06:14', u'C(18,11)']

11 Student ID:djk006

	first_attempt
					2015-10-10 21:32:55
	part2_incorrect_attempt
					('0:02:26', u'18!/10!(8!)')
	part2_correct_attempt
					['0:02:36', u'18!/(10!8!)']

12 Student ID:dando

	first_attempt
					2015-10-09 23:11:28
	part2_incorrect_attempt
					('0:09:55', u'C(11,6)')
	part2_correct_attempt
					['0:31:23', u'C(16,11)']

13 Student ID:chc286

	first_attempt
					2015-10-11 23:17:46
	part2_incorrect_attempt
					('0:01:11', u'C(11,4)')
	part2_correct_attempt
					['0:05:35', u'C(13,3)']

14 Student ID:abasu

	first_attempt
					2015-10-11 02:07:17
	part2_incorrect_attempt
					('0:01:19', u'C(34,13)')
					('0:01:27', u'C(34,7)')
	part2_correct_attempt
					['0:02:56', u'C(19,13)']

15 Student ID:sayao

	first_attempt
					2015-10-13 16:30:31
	part2_incorrect_attempt
					('0:02:35', u'7*7')
					('0:02:54', u'6^6')
					('11:07:58', u'7!')
					('11:08:11', u'7!*6!*5!*4!*3!*2!')
					('11:08:21', u'6*6')
					('11:08:26', u'6^6')
	part2_correct_attempt
					['11:11:50', u'C((7+6-1), 7)']

16 Student ID:anvan

	first_attempt
					2015-10-15 01:48:03
	part2_incorrect_attempt
					('0:07:25', u'13!10!')
					('0:07:33', u'13!/3!')
					('0:07:39', u'13!/10!')
					('0:09:57', u'22! / 10!')
	part2_correct_attempt
					['1:40:57', u'22! / (9!13!)']

17 Student ID:csl030

	first_attempt
					2015-10-14 01:54:21
	part2_incorrect_attempt
					('0:03:54', u'C(13,5)')
	part2_correct_attempt
					['0:04:48', u'C(12,8)']

18 Student ID:m4bui

	first_attempt
					2015-10-15 21:55:25
	part2_incorrect_attempt
					('0:00:13', u'C(12,2)')
	part2_correct_attempt
					['0:01:00', u'C(13,12)']

19 Student ID:a2ahmed

	first_attempt
					2015-10-15 03:48:29
	part2_incorrect_attempt
					('0:06:08', u'C(9,7)')
					('0:12:43', u'C(9,7)')
					('0:13:40', u'C(17,10)')
	part2_correct_attempt
					['0:13:52', u'C(16,10)']

20 Student ID:c1wei

	first_attempt
					2015-10-14 07:39:04
	part2_incorrect_attempt
					('0:19:43', u'8!')
					('0:21:37', u'8!/8')
					('0:23:02', u'8!/4!')
					('0:24:39', u'4^8')
					('0:24:51', u'8^4')
					('0:35:39', u'4^8')
	part2_correct_attempt
					['12:57:25', u'165']

21 Student ID:mitopete

	first_attempt
					2015-10-13 20:19:08
	part2_incorrect_attempt
					('-1 day, 23:39:48', u'10!/(4!6!)')
					('-1 day, 23:40:09', u'13!/(4!9!)')
					('-1 day, 23:43:41', u'9!/(3!6!)')
					('-1 day, 23:45:28', u'13!/(4!9!)')
					('-1 day, 23:59:20', u'4!')
					('20:21:34', u'10!/(4!6!)')
					('20:23:15', u'13!/(4!6!)')
	part2_correct_attempt
					['20:26:49', u'13!/(10!3!)']

22 Student ID:starinia

	first_attempt
					2015-10-15 05:33:54
	part2_incorrect_attempt
					('0:10:15', u'12!/(7!5!)')
	part2_correct_attempt
					['0:11:09', u'C(12,8)']

23 Student ID:m4salaza

	first_attempt
					2015-10-15 23:27:19
	part2_incorrect_attempt
					('0:03:01', u'14^7')

24 Student ID:tak068

	first_attempt
					2015-10-14 06:39:39
	part2_incorrect_attempt
					('-1 day, 23:59:28', u'7^3')
					('-1 day, 23:59:38', u'3^7')
					('-1 day, 23:59:43', u'3^6')
	part2_correct_attempt
					['0:00:58', u'36']

25 Student ID:yos017

	first_attempt
					2015-10-14 06:22:26
	part2_incorrect_attempt
					('0:00:43', u'24!/(13!*11!)')
	part2_correct_attempt
					['0:02:04', u'22!/(13!*9!)']

26 Student ID:habuamar

	first_attempt
					2015-10-09 05:45:17
	part2_incorrect_attempt
					('-1 day, 23:59:18', u'(13!)/(4!*9!)')
					('0:04:48', u'C(13,8)')
	part2_correct_attempt
					['0:06:54', u'C(15,4)']

27 Student ID:ggaddi

	first_attempt
					2015-10-14 04:16:49
	part2_incorrect_attempt
					('-1 day, 13:41:46', u'24!/(12!*12!)')
					('-1 day, 13:57:13', u'12!')
					('-1 day, 13:57:27', u'13*12!')
					('-1 day, 22:03:25', u'24!/(12!*12!)')
	part2_correct_attempt
					['-1 day, 22:06:19', u'24!/(11!*13!)']

28 Student ID:druble

	first_attempt
					2015-10-13 04:08:53
	part2_incorrect_attempt
					('0:00:00', u'C(11,4)')
					('0:02:15', u'11^4')
	part2_correct_attempt
					['0:15:26', u'C(14, 11)']

29 Student ID:b3hwang

	first_attempt
					2015-10-14 18:20:39
	part2_incorrect_attempt
					('0:01:01', u'13!/((13-9)!*9!)')
					('0:01:58', u'13!/(13-9)!')
					('0:06:01', u'(13+9-1)!/(9!*(13-1)!)')
	part2_correct_attempt
					['0:07:27', u'(13+9-1)!/(13!*(9-1)!)']

30 Student ID:jag028

	first_attempt
					2015-10-15 16:45:16
	part2_incorrect_attempt
					('-1 day, 10:32:45', u'C(17,7)')
					('-1 day, 10:35:17', u'C(10,7)')
					('0:02:17', u'7^10')
					('0:02:31', u'7!')
					('0:04:26', u'C(9,7)')
					('0:04:33', u'C(10,7)')
					('0:04:43', u'C(17,7)')
					('0:14:31', u'C(17,9)')
	part2_correct_attempt
					['0:14:45', u'C(16,6)']

31 Student ID:ccn001

	first_attempt
					2015-10-12 21:36:53
	part2_incorrect_attempt
					('-1 day, 23:55:14', u'16!/(2!(14!))')
					('-1 day, 23:58:19', u'15!/(2!(13!))')
					('0:23:03', u'15*14')
					('0:23:15', u'15*15')
	part2_correct_attempt
					['4:50:24', u'16']

32 Student ID:quwong

	first_attempt
					2015-10-14 16:10:46
	part2_incorrect_attempt
					('-1 day, 11:03:31', u'18!/(11!*7!)')
	part2_correct_attempt
					['-1 day, 12:11:09', u'18!/(12!*6!)']

33 Student ID:lguintu

	first_attempt
					2015-10-09 21:44:26
	part2_incorrect_attempt
					('-1 day, 23:37:37', u'C(9,6)')
					('-1 day, 23:37:47', u'C(9,6)*6!')
					('-1 day, 23:39:56', u'C(13,6)')
					('-1 day, 23:42:29', u'C(14,6)*9')
					('-1 day, 23:46:42', u'6^9/9')
					('-1 day, 23:56:10', u'6^9/6')
					('-1 day, 23:56:36', u'6*9')
					('-1 day, 23:57:41', u'6^9/9')
					('0:00:00', u'C(8,5)')
					('0:00:37', u'C(13,5)')
	part2_correct_attempt
					['0:01:11', u'C(14,5)']

34 Student ID:c1sorian

	first_attempt
					2015-10-14 23:08:59
	part2_incorrect_attempt
					('-1 day, 23:41:24', u'11!/(9!2!)')
					('-1 day, 23:47:25', u'1+1+11+55+165+330+462+462+330+165+55+11')
	part2_correct_attempt
					['-1 day, 23:49:37', u'12!/11!']

35 Student ID:atorr

	first_attempt
					2015-10-14 01:31:48
	part2_incorrect_attempt
					('0:00:42', u'6^8')
					('0:01:50', u'C(14,6)')
					('0:02:49', u'6!')

36 Student ID:cprafull

	first_attempt
					2015-10-14 07:03:03
	part2_incorrect_attempt
					('0:04:00', u'10!/((2!)(8!))')
	part2_correct_attempt
					['0:07:58', u'12']

37 Student ID:sachadal

	first_attempt
					2015-10-14 18:27:45
	part2_incorrect_attempt
					('-1 day, 23:33:49', u'C(12,6)')
					('-1 day, 23:34:03', u'P(12,6)')
					('0:00:55', u'C(12,6)')
	part2_correct_attempt
					['20:42:44', u'C(17,12)']

38 Student ID:kthui

	first_attempt
					2015-10-11 08:26:07
	part2_incorrect_attempt
					('0:01:24', u'12!/((12-5)!5!)')
	part2_correct_attempt
					['0:02:18', u'12!/((12-4)!4!)']

39 Student ID:alhung

	first_attempt
					2015-10-15 19:46:15
	part2_incorrect_attempt
					('-1 day, 23:56:09', u'P(13,3)')
					('0:00:21', u'C(13,3)')
	part2_correct_attempt
					['0:03:45', u'C(15,13)']

40 Student ID:beyounge

	first_attempt
					2015-10-09 05:32:59
	part2_incorrect_attempt
					('0:00:00', u'C(8,3)')
	part2_correct_attempt
					['0:02:47', u'C(10,2)']

41 Student ID:jic212

	first_attempt
					2015-10-12 06:42:45
	part2_incorrect_attempt
					('0:04:19', u'C(13,9)')
					('0:04:27', u'C(13,4)')
					('0:09:34', u'C(13,9)')
					('0:09:47', u'C(9,4)')
					('0:24:13', u'9!')
					('0:29:12', u'C(13,4)*C(9,4)*4')
					('0:34:13', u'C(13,9)')
	part2_correct_attempt
					['0:40:38', u'C(12,9)']

42 Student ID:tpmach

	first_attempt
					2015-10-11 01:23:31
	part2_incorrect_attempt
					('0:01:42', u'13!/(2!*(13-2)!)')
	part2_correct_attempt
					['0:02:25', u'13!/(1!*(13-1)!)']

43 Student ID:r1gu

	first_attempt
					2015-10-15 12:05:33
	part2_incorrect_attempt
					('0:01:10', u'C(10,3)')
					('0:04:56', u'C(13,3)')
	part2_correct_attempt
					['10:48:13', u'C(12,10)']

44 Student ID:dis003

	first_attempt
					2015-10-15 11:02:49
	part2_incorrect_attempt
					('-1 day, 23:59:12', u'C(11,5)')
					('0:02:26', u'5**11')
					('0:03:29', u'11!/(5!(11-5)!)')
	part2_correct_attempt
					['0:05:15', u'C(11+5-1,5-1)']

45 Student ID:rraiyyan

	first_attempt
					2015-10-14 23:30:50
	part2_incorrect_attempt
					('-1 day, 23:48:21', u'C(7,6)')
	part2_correct_attempt
					['-1 day, 23:50:03', u'C(12,7)']

46 Student ID:jhw015

	first_attempt
					2015-10-15 05:13:03
	part2_incorrect_attempt
					('0:11:38', u'8^3')
					('12:08:52', u'C(12,8)')
					('12:09:16', u'C(12,3)')
	part2_correct_attempt
					['12:16:25', u'C(10,8)']

47 Student ID:dsmonaha

	first_attempt
					2015-10-13 17:40:07
	part2_incorrect_attempt
					('0:00:48', u'C(11,3)')
					('0:01:40', u'P(11,3)')
					('1 day, 1:00:56', u'P(11,3)')
					('1 day, 1:01:17', u'C(11,3)')
					('1 day, 1:01:55', u'11^3')
					('1 day, 1:07:17', u'C(11,3)')
					('1 day, 1:08:52', u'11*6*90')
					('1 day, 1:11:36', u'C(10,4)')
	part2_correct_attempt
					['1 day, 1:13:11', u'C(13,11)']

48 Student ID:krkelkar

	first_attempt
					2015-10-14 02:33:28
	part2_incorrect_attempt
					('0:00:00', u'15!/(14!*1!)')
	part2_correct_attempt
					['1:16:06', u'(13+15)! / (15!*13!)']

49 Student ID:jel075

	first_attempt
					2015-10-15 00:57:09
	part2_incorrect_attempt
					('0:00:00', u'10!/(8!*2!)')
					('0:09:33', u'2^10')
					('3:59:29', u'2^10')
	part2_correct_attempt
					['4:12:11', u'11']

50 Student ID:ytc012

	first_attempt
					2015-10-14 22:27:40
	part2_incorrect_attempt
					('0:14:08', u'12!/(9!(3!))')
					('0:14:15', u'12!/(9!)')
					('0:15:58', u'20!/9!')
					('0:16:20', u'19!/9!')
					('0:16:25', u'19!/11!')
					('0:16:32', u'19!/10!')
					('9:07:09', u'20!/(9!)')
					('9:11:24', u'20!/(9!11!)')
					('9:12:22', u'12!/(7!5!)')
					('9:12:56', u'11!/(7!5!)')
					('9:13:06', u'11!/(7!4!)')
					('9:13:25', u'21!/(20!)')
					('9:43:22', u'22!/(9!12!)')
					('9:49:21', u'21!')
					('9:50:09', u'12^9')
					('9:50:19', u'12!')
					('10:00:13', u'11!/(9!2!)')
					('10:00:32', u'12!/(9!3!)')
					('10:01:06', u'11!/(8!3!)')
					('10:04:31', u'23!/(9!12!)')
					('10:04:57', u'23!/(9!14!)')
	part2_correct_attempt
					['12:43:29', u'20!/(12!8!)']

51 Student ID:bakang

	first_attempt
					2015-10-15 02:01:21
	part2_incorrect_attempt
					('-1 day, 23:59:47', u'C(13,7)')
					('0:00:00', u'C(13,6)')
	part2_correct_attempt
					['0:00:41', u'C(12,7)']

52 Student ID:wcwhite

	first_attempt
					2015-10-14 02:03:01
	part2_incorrect_attempt
					('0:01:53', u'C(7,2)')
					('0:02:17', u'7!/(2!(7-2)!)')
					('0:08:12', u'7!/5!')
	part2_correct_attempt
					['0:10:22', u'C(7+2-1,7)']

53 Student ID:rbdoming

	first_attempt
					2015-10-15 01:14:14
	part2_incorrect_attempt
					('-1 day, 17:23:33', u'C(8,6)')
					('-1 day, 17:24:56', u'C(14,6)')
	part2_correct_attempt
					['-1 day, 23:54:27', u'C(13,8)']

54 Student ID:aurodrig

	first_attempt
					2015-10-15 23:34:01
	part2_incorrect_attempt
					('0:00:00', u'18!/(8!10!)')
					('0:00:55', u'17!/(8!9!)')
					('0:02:08', u'18!/(8!10!)')
	part2_correct_attempt
					['0:03:44', u'18!/(7!11!)']

55 Student ID:yjshin

	first_attempt
					2015-10-15 10:50:38
	part2_incorrect_attempt
					('0:06:06', u'11!')
					('0:06:09', u'13!')
					('0:15:48', u'23!/(12!11!)')
	part2_correct_attempt
					['0:16:08', u'23!/(13!10!)']

56 Student ID:aportuga

	first_attempt
					2015-10-14 03:07:21
	part2_incorrect_attempt
					('-1 day, 23:37:30', u'10!')
					('-1 day, 23:39:43', u'10!-1')
	part2_correct_attempt
					['-1 day, 23:42:33', u'43758']

57 Student ID:bkoli

	first_attempt
					2015-10-15 06:09:31
	part2_incorrect_attempt
					('0:06:07', u'19!/(6!13!)')
	part2_correct_attempt
					['0:14:41', u'19!/(5!14!)']

58 Student ID:dac064

	first_attempt
					2015-10-15 19:39:10
	part2_incorrect_attempt
					('0:01:09', u'C(12,6)')
					('0:31:27', u'C(19,12)')
					('0:32:31', u'C(19,6)')
					('0:34:19', u'C(19,12)')
	part2_correct_attempt
					['0:35:59', u'C(17,12)']

59 Student ID:v3doan

	first_attempt
					2015-10-11 02:15:42
	part2_incorrect_attempt
					('-1 day, 23:35:00', u'C(7,4)')
					('0:00:53', u'7^4')
	part2_correct_attempt
					['0:04:30', u'C(10,7)']

60 Student ID:sghouse

	first_attempt
					2015-10-12 20:03:59
	part2_incorrect_attempt
					('-1 day, 22:55:25', u'15!/(6!*9!)')
					('0:01:10', u'25!/(10!*15!)')
	part2_correct_attempt
					['0:01:58', u'23!/(8!*15!)']

61 Student ID:k3tan

	first_attempt
					2015-10-13 05:30:55
	part2_incorrect_attempt
					('0:01:03', u'9^10')
	part2_correct_attempt
					['0:10:53', u'(18*17*16*15*14*13*12*11)/8!']

62 Student ID:lpettit

	first_attempt
					2015-10-14 16:58:46
	part2_incorrect_attempt
					('0:08:47', u'(14 + 8-1)!/(14!*(14-8-1)!)')
					('0:13:12', u'(14 + 8-1)!/(8!*(14-8-1)!)')
	part2_correct_attempt
					['0:14:57', u'21!/(14!*(21-14)!)']

63 Student ID:h4tu

	first_attempt
					2015-10-15 06:24:19
	part2_incorrect_attempt
					('0:02:24', u'9*8*7')
	part2_correct_attempt
					['0:06:43', u'11!/(9!*2!)']

64 Student ID:lywong

	first_attempt
					2015-10-13 00:14:52
	part2_incorrect_attempt
					('0:00:33', u'2^11')
					('0:02:03', u'C(10,2)')
	part2_correct_attempt
					['0:06:55', u'C(12,11)']

65 Student ID:jix029

	first_attempt
					2015-10-13 19:41:07
	part2_incorrect_attempt
					('0:02:39', u'20!/9!')
	part2_correct_attempt
					['0:03:00', u'20!/(9!11!)']

66 Student ID:hkhodada

	first_attempt
					2015-10-13 19:40:47
	part2_incorrect_attempt
					('-2 days, 8:00:33', u'C(14,10)')
					('-2 days, 8:00:49', u'C(14,5)')
					('-2 days, 8:03:00', u'C(16,10)')
					('-2 days, 8:51:24', u'C(18,10)')
					('-2 days, 8:51:37', u'C(15,13)')
					('-2 days, 9:03:53', u'C(19,15)')
					('-2 days, 9:27:24', u'P(17,10)')
					('-2 days, 9:27:46', u'C(17,10)')
	part2_correct_attempt
					['0:02:42', u'C(24,15)']

67 Student ID:glcohen

	first_attempt
					2015-10-13 05:09:00
	part2_incorrect_attempt
					('-1 day, 23:52:40', u'14*4')
					('-1 day, 23:54:36', u'14!/(10!4!)')
					('0:17:00', u'14^4')
					('0:17:23', u'14!')
					('0:17:42', u'14!/(10!4!)')
					('0:17:52', u'14!/(4!)')
					('0:19:24', u'11!/(3!)')
					('0:20:11', u'17!/11!')
					('0:21:07', u'(14!)/(10!4!)')
					('0:21:18', u'(14!)/(4!)')
					('0:31:56', u'17!/(13!4!)')
					('0:32:39', u'17!/(11!)')
					('0:32:53', u'17!/(11!6!)')
	part2_correct_attempt
					['0:33:10', u'17!/(14!3!)']

68 Student ID:acvuong

	first_attempt
					2015-10-13 04:17:39
	part2_incorrect_attempt
					('-1 day, 23:52:31', u'C(12,4)')
					('-1 day, 23:57:27', u'12!/8!')
					('0:09:08', u'C(7,4)')
					('0:10:08', u'C(14,4)')
	part2_correct_attempt
					['0:16:51', u'C(15,12)']

69 Student ID:d6he

	first_attempt
					2015-10-15 07:28:20
	part2_incorrect_attempt
					('-1 day, 22:35:51', u'12!/6!')
					('-1 day, 22:36:05', u'12!/(6!6!)')
	part2_correct_attempt
					['0:04:55', u'12!/(7!5!)']

70 Student ID:jew037

	first_attempt
					2015-10-14 04:05:16
	part2_incorrect_attempt
					('0:00:57', u'C(9,8)')
					('0:02:43', u'8!')
					('0:03:01', u'9^8')
	part2_correct_attempt
					['0:07:12', u'C(9+8-1, 9)']

71 Student ID:thk002

	first_attempt
					2015-10-14 06:54:09
	part2_incorrect_attempt
					('-3 days, 20:09:46', u'C(13,10)')
	part2_correct_attempt
					['1 day, 12:50:43', u'C(22,13)']

72 Student ID:awollner

	first_attempt
					2015-10-11 19:58:41
	part2_incorrect_attempt
					('0:02:45', u'C(17,8)')
	part2_correct_attempt
					['0:05:16', u'C(19,12)']

73 Student ID:dcrume

	first_attempt
					2015-10-15 23:14:23
	part2_incorrect_attempt
					('0:01:44', u'C(15, 14)')

74 Student ID:t2li

	first_attempt
					2015-10-14 06:08:27
	part2_incorrect_attempt
					('0:04:38', u'12!')
					('0:04:46', u'12! * 6')
					('0:05:01', u'12! * 6^12')
					('0:05:17', u'P(12,6)')
					('0:05:35', u'C(12,6)')
					('0:06:45', u'12!6!')
					('0:09:37', u'12!*6^12')
					('0:10:58', u'12^12')
					('0:13:37', u'P(12,6)')
					('0:13:44', u'P(12,6) * 6!')
					('0:13:48', u'P(12,6) * 6^12')
					('0:14:08', u'P(12,6)12')
					('0:14:14', u'P(12,12)')
	part2_correct_attempt
					['0:17:53', u'C(17,5)']

75 Student ID:dlt009

	first_attempt
					2015-10-14 01:31:34
	part2_incorrect_attempt
					('-1 day, 23:50:01', u'11!/[(11-5)!5!]')
					('-1 day, 23:52:50', u'7!/[(7-5)!5!]')
					('0:02:24', u'5^7')
	part2_correct_attempt
					['0:06:44', u'11!/[(11-7)!7!]']

76 Student ID:mbl003

	first_attempt
					2015-10-15 07:05:32
	part2_incorrect_attempt
					('-1 day, 23:56:47', u'10!/3!')
	part2_correct_attempt
					['0:01:57', u'8008']

77 Student ID:agoldsht

	first_attempt
					2015-10-14 03:06:04
	part2_incorrect_attempt
					('0:01:57', u'11^8')
					('0:11:48', u'(11+8-1)!/11!')
	part2_correct_attempt
					['0:13:26', u'(11+8-1)!/(11!*(18-11)!)']

78 Student ID:n2patil

	first_attempt
					2015-10-13 16:12:06
	part2_incorrect_attempt
					('0:02:43', u'10!/(2(8!))')
					('0:15:47', u'10^2')
					('0:15:57', u'10*9')
	part2_correct_attempt
					['2:46:16', u'11']

79 Student ID:etemlock

	first_attempt
					2015-10-11 00:41:13
	part2_incorrect_attempt
					('0:11:05', u'C(11,8)')
	part2_correct_attempt
					['0:12:32', u'C(12,8)']

80 Student ID:ttimmons

	first_attempt
					2015-10-12 18:45:28
	part2_incorrect_attempt
					('0:00:00', u'12*(11-1)+1')
					('0:00:06', u'12!')
					('0:00:31', u'C(12,11)')
					('0:01:22', u'(12!)/2!')
					('0:01:56', u'12*11')
					('0:02:12', u'11!')
					('0:02:24', u'11*(12-1)+1')
	part2_correct_attempt
					['0:04:12', u'C(22,10)']

81 Student ID:jeqin

	first_attempt
					2015-10-15 12:25:06
	part2_incorrect_attempt
					('0:01:41', u'6!/(5!)')
					('0:04:15', u'11!/(5!6!)')
					('0:05:12', u'11!/(7!/4!)')
	part2_correct_attempt
					['0:05:18', u'11!/(7!4!)']

82 Student ID:jblynch

	first_attempt
					2015-10-12 07:05:09
	part2_incorrect_attempt
					('-1 day, 23:56:24', u'C(12,3)')
					('-1 day, 23:56:38', u'P(12,3)')
					('-1 day, 23:57:54', u'P(11,3)')
	part2_correct_attempt
					['-1 day, 23:58:59', u'P(11,9)']

83 Student ID:nnh002

	first_attempt
					2015-10-13 17:11:43
	part2_incorrect_attempt
					('0:13:30', u'C(16,1)')
	part2_correct_attempt
					['0:13:46', u'C(15,1)']

84 Student ID:ielouaae

	first_attempt
					2015-10-15 08:53:46
	part2_incorrect_attempt
					('-1 day, 23:42:02', u'24!/(12!12!)')
	part2_correct_attempt
					['-1 day, 23:49:04', u'24!/(13!11!)']

85 Student ID:tol003

	first_attempt
					2015-10-14 00:14:10
	part2_incorrect_attempt
					('0:00:00', u'12*(7^13-1)')
					('0:00:30', u'6*(7^13-1)')
					('0:01:32', u'12*(7^13 + 1)')
					('0:02:20', u'6*(7^13 + 1)')
	part2_correct_attempt
					['0:04:30', u'C(19,13)']

86 Student ID:hachrist

	first_attempt
					2015-10-14 22:26:50
	part2_incorrect_attempt
					('4:58:19', u'27!/(13!*14!)')
					('5:07:23', u'15!/(2!*13!)')
					('5:07:46', u'15!/13!')
	part2_correct_attempt
					['5:12:17', u'27!/(15!*12!)']

87 Student ID:kew017

	first_attempt
					2015-10-15 17:43:50
	part2_incorrect_attempt
					('0:00:00', u'10!/(6!4!)')
	part2_correct_attempt
					['0:01:47', u'15!/(5!10!)']

88 Student ID:haliew

	first_attempt
					2015-10-14 01:09:14
	part2_incorrect_attempt
					('-1 day, 22:42:53', u'C(11,2)')
					('0:05:29', u'9^4*8^3*7^2*6')
					('0:12:04', u'9!/(7!(9-7)!)')
					('0:12:24', u'C(9,2)')
					('1:20:06', u'2^9')
					('1:24:13', u'C(8,1)')
	part2_correct_attempt
					['1:24:24', u'C(10,1)']

89 Student ID:kmc012

	first_attempt
					2015-10-15 04:50:29
	part2_incorrect_attempt
					('0:19:47', u'(12!)/((8!)*(4!))')
					('2:12:01', u'14!/(4!*10!)')
	part2_correct_attempt
					['2:12:12', u'14!/(3!*11!)']

90 Student ID:asetters

	first_attempt
					2015-10-12 06:05:28
	part2_incorrect_attempt
					('-1 day, 23:59:00', u'2^8')
	part2_correct_attempt
					['0:10:56', u'9']

91 Student ID:arvenega

	first_attempt
					2015-10-14 19:02:51
	part2_incorrect_attempt
					('0:02:58', u'7*6')
	part2_correct_attempt
					['0:53:04', u'8']

92 Student ID:ksrijong

	first_attempt
					2015-10-15 05:28:38
	part2_incorrect_attempt
					('0:01:05', u'C(14,8)')
	part2_correct_attempt
					['0:01:46', u'C(13,8)']

93 Student ID:azkong

	first_attempt
					2015-10-15 18:47:05
	part2_incorrect_attempt
					('-1 day, 23:59:13', u'14!/7!')
					('-1 day, 23:59:22', u'14!/(7!7!)')
	part2_correct_attempt
					['0:00:45', u'C(14, 8)']

94 Student ID:abjara

	first_attempt
					2015-10-12 21:07:20
	part2_incorrect_attempt
					('0:01:03', u'9*8*7*6*5')
					('0:01:19', u'9!/(5!*4!)')
					('0:01:40', u'9!/4!')
					('0:07:16', u'5!')
					('0:08:12', u'5^9 + 4^8 + 3^7 + 2 ^6 + 1^5')
					('0:12:24', u'15!/(5!*10!)')
	part2_correct_attempt
					['0:17:54', u'13!/(9!*4!)']

95 Student ID:cagatep

	first_attempt
					2015-10-14 02:46:13
	part2_incorrect_attempt
					('0:00:27', u'10!/(8!2!)')
					('0:00:35', u'10!/(8!)')
					('2:02:06', u'10!/(8!/2!)')
					('2:02:15', u'10!/(8!2!)')
	part2_correct_attempt
					['2:05:57', u'C(17, 10)']

96 Student ID:hmnaing

	first_attempt
					2015-10-15 00:33:38
	part2_incorrect_attempt
					('-2 days, 14:49:10', u'C(14, 8)')
	part2_correct_attempt
					['-1 day, 23:59:04', u'C(14+ 8-1, 8-1)']

97 Student ID:asp025

	first_attempt
					2015-10-15 18:43:47
	part2_incorrect_attempt
					('0:05:00', u'22!/(9!13!)')
	part2_correct_attempt
					['0:12:53', u'22!/(8!14!)']

98 Student ID:dlgoldbe

	first_attempt
					2015-10-15 00:25:59
	part2_incorrect_attempt
					('0:02:29', u'10!/(8!*2!)')
					('0:06:44', u'17!/(8!*11!)')
	part2_correct_attempt
					['0:07:18', u'17!/(7!*10!)']

99 Student ID:kquong

	first_attempt
					2015-10-11 04:15:08
	part2_incorrect_attempt
					('0:03:58', u'21!/(13*(21-13)!)')
					('0:04:16', u'21!/(9!*(21-9)!)')
	part2_correct_attempt
					['0:09:57', u'21!/(13!*(21-13)!) ']

100 Student ID:jfalcone

	first_attempt
					2015-10-14 22:31:55
	part2_incorrect_attempt
					('0:04:15', u'14!/(3!11!)')
					('0:05:12', u'10!/(3!7!)')
					('0:07:35', u'11!/(4!7!)')
					('0:09:49', u'15!/(8!7!)')
					('0:09:55', u'15!/(8!)')
					('0:12:18', u'11!/(4!7!)')
					('21:40:36', u'8 * 8 * 8 * 8')
	part2_correct_attempt
					['23:05:23', u'C(11,8)']

101 Student ID:t2shin

	first_attempt
					2015-10-15 05:34:48
	part2_incorrect_attempt
					('0:00:51', u'11!/(4!7!)')
					('0:03:32', u'11^4')
					('0:09:26', u'14!/(10!4!)')
	part2_correct_attempt
					['0:10:42', u'14!/(11!3!)']

102 Student ID:vsamant

	first_attempt
					2015-10-10 16:16:35
	part2_incorrect_attempt
					('-1 day, 9:21:11', u'C(9,6)')
					('-1 day, 9:21:24', u'P(9,6)')
					('-1 day, 13:10:50', u'C(9,6)')
	part2_correct_attempt
					['1:10:04', u'C(14,9)']

103 Student ID:dcastlem

	first_attempt
					2015-10-15 16:46:38
	part2_incorrect_attempt
					('-1 day, 11:12:33', u'10!/((3!)(7!))')
					('-1 day, 11:12:47', u'10!/3!')
					('-1 day, 22:18:09', u'12!/((3!)(9!))')
					('-1 day, 22:18:53', u'12!/((3!))')
					('0:03:32', u'10!/((3!)(7!))')
					('0:03:40', u'10!/((3!))')
					('0:03:58', u'12!/((3!))')
					('0:09:54', u'12!/((10!))')
					('0:10:06', u'12!/((9!))')
					('0:10:56', u'3^10')
					('0:13:33', u'11!/3!')
					('0:13:52', u'11!/((3!)(8!))')
					('0:14:01', u'11!/((8!))')
					('0:16:08', u'12!/2!')
					('0:16:21', u'12!/9!')
	part2_correct_attempt
					['0:17:08', u'12!/((2!)(10!))']

104 Student ID:ewbrenna

	first_attempt
					2015-10-12 19:54:05
	part2_incorrect_attempt
					('0:00:00', u'10!')
	part2_correct_attempt
					['0:05:45', u'293930']

105 Student ID:qtluong

	first_attempt
					2015-10-12 20:07:58
	part2_incorrect_attempt
					('-1 day, 23:58:10', u'19!/(10!9!)')
					('0:00:00', u'19!(11!8!)')
	part2_correct_attempt
					['0:00:06', u'19!/(11!8!)']

106 Student ID:spw006

	first_attempt
					2015-10-13 23:33:15
	part2_incorrect_attempt
					('-1 day, 21:46:23', u'10!/(8!2!)')
					('-1 day, 23:45:35', u'C(10,8)')
					('-1 day, 23:54:23', u'C(18,10)')
					('-1 day, 23:59:47', u'10!/(8!2!)')
	part2_correct_attempt
					['0:00:00', u'C(17,7)']

107 Student ID:any027

	first_attempt
					2015-10-12 19:58:05
	part2_incorrect_attempt
					('0:03:24', u'C( 19 ,10)')
					('0:04:20', u'C( 18, 10)')
					('0:09:02', u'C( 24, 9)')
	part2_correct_attempt
					['0:09:25', u'C(23, 9 )']

108 Student ID:e9brown

	first_attempt
					2015-10-14 08:38:34
	part2_incorrect_attempt
					('0:00:34', u'C(10,5)')
	part2_correct_attempt
					['0:02:56', u'C(14,10)']

109 Student ID:vsosnovs

	first_attempt
					2015-10-15 04:08:36
	part2_incorrect_attempt
					('0:00:52', u'13!')
	part2_correct_attempt
					['0:06:25', u'C(14,13)']

110 Student ID:amquinte

	first_attempt
					2015-10-12 20:36:08
	part2_incorrect_attempt
					('0:00:00', u'8^9')
	part2_correct_attempt
					['3 days, 3:08:59', u'11440']

111 Student ID:jmiclat

	first_attempt
					2015-10-15 19:56:15
	part2_incorrect_attempt
					('-1 day, 21:14:03', u'12^11')
					('-1 day, 21:21:40', u'22!/(11!11!)')

112 Student ID:syc078

	first_attempt
					2015-10-15 02:50:06
	part2_incorrect_attempt
					('-1 day, 21:59:43', u'(20!) / ( (12!) (8!) )')
	part2_correct_attempt
					['0:00:37', u'(20!) / ( (13!) (7!) )']

113 Student ID:cfgutier

	first_attempt
					2015-10-15 23:13:08
	part2_incorrect_attempt
					('0:01:51', u'13!/3!/10!')
	part2_correct_attempt
					['0:05:14', u'13!/11!/2!']

114 Student ID:dkostins

	first_attempt
					2015-10-15 18:26:20
	part2_incorrect_attempt
					('0:26:19', u'C(25,14)')
	part2_correct_attempt
					['0:26:31', u'C(24,14)']

115 Student ID:pnquach

	first_attempt
					2015-10-15 02:27:58
	part2_incorrect_attempt
					('-1 day, 23:47:28', u'10!/(6!*4!)')
	part2_correct_attempt
					['0:00:00', u'15!/(5!*10!)']

116 Student ID:achinn

	first_attempt
					2015-10-13 00:33:39
	part2_incorrect_attempt
					('0:01:07', u'5!')
					('0:01:38', u'10!/5!')
					('0:03:23', u'5^5')
					('0:05:23', u'10^5')
					('0:10:22', u'C(10,5)*5!')
					('0:10:28', u'C(10,5)*10!')
					('0:13:12', u'10*9*8*7*6')
					('0:35:55', u'C(10,5)')
	part2_correct_attempt
					['0:43:13', u'C(14,10)']

117 Student ID:jap009

	first_attempt
					2015-10-15 21:37:45
	part2_incorrect_attempt
					('0:00:39', u'11!(7!4!)')
	part2_correct_attempt
					['0:00:47', u'11!/(7!4!)']

118 Student ID:kalang

	first_attempt
					2015-10-14 05:58:33
	part2_incorrect_attempt
					('0:01:04', u'C(10,7)')
					('0:01:16', u'C(10,3)')
					('0:06:18', u'10!/3!')
					('0:10:44', u'7^10')
					('0:11:50', u'7!')
					('0:11:56', u'10!')
					('0:12:02', u'10!/7!')
					('0:12:08', u'10!/3!')
					('0:12:25', u'10!/(7!*3!)')
					('16:59:25', u'C(17,7)')
					('17:00:02', u'C(17,6)')
	part2_correct_attempt
					['17:00:56', u'C(16,10)']

119 Student ID:aalhaida

	first_attempt
					2015-10-15 17:27:09
	part2_incorrect_attempt
					('0:03:12', u'13!/(10!3!)')
	part2_correct_attempt
					['0:13:32', u'16!/(10!6!)']

120 Student ID:jjchung

	first_attempt
					2015-10-14 19:32:45
	part2_incorrect_attempt
					('-1 day, 23:59:40', u'11^7')
					('0:00:00', u'7^11')
					('0:03:00', u'11!/4!')
					('0:06:17', u'11!/(7!4!)')
					('0:06:31', u'11!/(7!)')
					('0:06:40', u'12!/(4!)')
					('0:08:22', u'C(12,7)')
					('0:08:30', u'C(12,4)')
					('0:09:30', u'C(10,7)')
					('0:09:36', u'C(10,4)')
					('0:11:09', u'C(13,7)')
					('0:11:49', u'C(18,7)')
	part2_correct_attempt
					['0:14:20', u'C(11+7-1,11)']

121 Student ID:aadhakal

	first_attempt
					2015-10-14 05:01:33
	part2_incorrect_attempt
					('0:00:00', u'C(17,14)')
	part2_correct_attempt
					['0:03:18', u'C(20,14)']

122 Student ID:mtrafeca

	first_attempt
					2015-10-11 05:53:40
	part2_incorrect_attempt
					('0:00:31', u'2^7')
					('0:01:58', u'7!/(2!*5!)')
	part2_correct_attempt
					['0:03:13', u'8']

123 Student ID:gsrandha

	first_attempt
					2015-10-15 06:05:00
	part2_incorrect_attempt
					('0:05:15', u'(15*14*13)/6')

124 Student ID:hmshah

	first_attempt
					2015-10-14 02:14:02
	part2_incorrect_attempt
					('1 day, 6:30:37', u'12!  / (5! * 8!)')
					('1 day, 6:31:42', u'12! / (5! * 7!)')
					('1 day, 6:33:37', u'C(12!, 8!)')
	part2_correct_attempt
					['1 day, 6:34:43', u'C(12, 8)']

125 Student ID:dtea

	first_attempt
					2015-10-15 23:14:02
	part2_incorrect_attempt
					('0:02:38', u'27!/(13!(27-13)!)')
	part2_correct_attempt
					['0:03:43', u'27!/(15!(27-15)!)']

126 Student ID:daw023

	first_attempt
					2015-10-15 06:56:15
	part2_incorrect_attempt
					('-1 day, 22:25:07', u'16!/(2*14!)')
					('-1 day, 23:58:08', u'C(15,2)')
	part2_correct_attempt
					['0:17:59', u'C(16,1)']

127 Student ID:aordookh

	first_attempt
					2015-10-15 20:37:35
	part2_incorrect_attempt
					('0:01:00', u'C(13,2)')
					('0:05:07', u'13!')
					('0:05:34', u'13^2')
					('0:41:50', u'13^13')
					('0:43:15', u'C(12,1)')
	part2_correct_attempt
					['0:45:35', u'C(14,13)']

128 Student ID:r2fisher

	first_attempt
					2015-10-14 22:55:59
	part2_incorrect_attempt
					('0:01:04', u'10!/4!')
					('0:01:13', u'10!/(4!*6!)')
					('0:01:31', u'10!/6!')
					('0:03:50', u'C(12,10)')
					('0:04:11', u'C(12,3)')
	part2_correct_attempt
					['0:04:35', u'C(13,10)']

129 Student ID:hpc001

	first_attempt
					2015-10-14 21:29:18
	part2_incorrect_attempt
					('0:00:40', u'C(14, 13)')
					('0:01:12', u'C(27, 14)')
	part2_correct_attempt
					['0:01:28', u'C(26, 14)']

130 Student ID:kosung

	first_attempt
					2015-10-15 07:26:55
	part2_incorrect_attempt
					('-1 day, 22:54:09', u'9!/(2!7!)')
	part2_correct_attempt
					['0:18:31', u'5005']

131 Student ID:xweng

	first_attempt
					2015-10-12 22:34:08
	part2_incorrect_attempt
					('0:00:29', u'10!2^10')
					('0:01:58', u'2^10')
					('0:02:11', u'10!')
					('0:02:18', u'10^2')
	part2_correct_attempt
					['0:05:39', u'11']

132 Student ID:yypan

	first_attempt
					2015-10-12 20:32:27
	part2_incorrect_attempt
					('0:09:03', u'13!/(3!*10!)')
					('0:10:28', u'11!/(3!*8!)')
					('0:10:38', u'11!/3!')
					('0:11:25', u'11!')
	part2_correct_attempt
					['0:12:53', u'C(13,11)']

133 Student ID:zig006

	first_attempt
					2015-10-12 23:17:43
	part2_incorrect_attempt
					('-1 day, 23:59:01', u'20!/(10!*10!)')
	part2_correct_attempt
					['0:00:24', u'20!/(11!*9!)']

134 Student ID:sthapa

	first_attempt
					2015-10-15 04:58:50
	part2_incorrect_attempt
					('0:02:30', u'14!/(12!*2!)')
					('0:07:02', u'(25*24*23)/(6)')
	part2_correct_attempt
					['2:10:31', u'C(14+12-1,14)']

135 Student ID:kgrozav

	first_attempt
					2015-10-15 18:55:24
	part2_incorrect_attempt
					('0:03:08', u'(8+8)!/(8!*8!)')
					('0:03:21', u'(16)!/(8!*8!)')
	part2_correct_attempt
					['0:04:36', u'(16)!/(9!*7!)']

136 Student ID:j2phung

	first_attempt
					2015-10-14 04:36:54
	part2_incorrect_attempt
					('0:06:03', u'10!/(2!4!)')
					('0:08:59', u'10!/(6!4!)')
					('0:19:58', u'10!/(7!4!)')
	part2_correct_attempt
					['0:20:07', u'10!/(7!3!)']












## Part 3

### (61) Mistake Group redirect of size 61




### (51) Mistake Group Digits of size 51




### (36) Mistake Group ['R.1'] of size 36
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(9-1,9-6)	|C(14,3)	|[('R.1', 3.0, u'9-6', u'3')]	|
|1	|C(11-1,11-9)	|C(12,2)	|[('R.1', 2.0, u'11-9', u'2')]	|
|2	|C(11-1,11-9)	|C(11,2)	|[('R.1', 2.0, u'11-9', u'2')]	|
|3	|C(9-1,9-6)	|C(6,3)	|[('R.1', 3.0, u'9-6', u'3')]	|
|4	|C(9-1,9-6)	|C(11,3)	|[('R.1', 3.0, u'9-6', u'3')]	|
|5	|C(11-1,11-8)	|C(18,3)	|[('R.1', 3.0, u'11-8', u'3')]	|
|6	|C(11-1,11-9)	|C(9,2)	|[('R.1', 2.0, u'11-9', u'2')]	|
|7	|C(12-1,12-7)	|C(18,5)	|[('R.1', 5.0, u'12-7', u'5')]	|
|8	|C(12-1,12-7)	|C(13,5)	|[('R.1', 5.0, u'12-7', u'5')]	|
|9	|C(15-1,15-10)	|C(7,5)	|[('R.1', 5.0, u'15-10', u'5')]	|
|10	|C(11-1,11-2)	|C(11,9)	|[('R.1', 9.0, u'11-2', u'9')]	|
|11	|C(7-1,7-4)	|C(7,3)	|[('R.1', 3.0, u'7-4', u'3')]	|
|12	|C(13-1,13-8)	|C(8,5)	|[('R.1', 5.0, u'13-8', u'5')]	|
|13	|C(13-1,13-7)	|C(19,6)	|[('R.1', 6.0, u'13-7', u'6')]	|
|14	|C(9-1,9-7)	|C(7, 2)	|[('R.1', 2.0, u'9-7', u'2')]	|
|15	|C(9-1,9-7)	|C(15, 2)	|[('R.1', 2.0, u'9-7', u'2')]	|
|16	|C(9-1,9-7)	|7^2	|[('R.1', 2.0, u'9-7', u'2')]	|
|17	|C(9-1,9-7)	|C(9, 2)	|[('R.1', 2.0, u'9-7', u'2')]	|
|18	|C(7-1,7-5)	|5^2	|[('R.1', 2.0, u'7-5', u'2')]	|
|19	|C(10-1,10-8)	|C(17, 2)	|[('R.1', 2.0, u'10-8', u'2')]	|
|20	|C(10-1,10-3)	|C(10,7)	|[('R.1', 7.0, u'10-3', u'7')]	|
|21	|C(10-1,10-7)	|C(16,3)	|[('R.1', 3.0, u'10-7', u'3')]	|
|22	|C(10-1,10-7)	|C(5,3)	|[('R.1', 3.0, u'10-7', u'3')]	|
|23	|C(13-1,13-3)	|C(13,10)	|[('R.1', 10.0, u'13-3', u'10')]	|
|24	|C(10-1,10-7)	|C(7, 3)	|[('R.1', 3.0, u'10-7', u'3')]	|
|25	|C(10-1,10-7)	|C(6, 3)	|[('R.1', 3.0, u'10-7', u'3')]	|
|26	|C(10-1,10-7)	|7^3	|[('R.1', 3.0, u'10-7', u'3')]	|
|27	|C(13-1,13-2)	|C(14,11)	|[('R.1', 11.0, u'13-2', u'11')]	|
|28	|C(10-1,10-7)	|C(10,3)	|[('R.1', 3.0, u'10-7', u'3')]	|
|29	|C(7-1,7-3)	|C(5,4)	|[('R.1', 4.0, u'7-3', u'4')]	|
|30	|C(15-1,15-13)	|C(13,2)	|[('R.1', 2.0, u'15-13', u'2')]	|




### (14) Mistake Group ['R.0'] of size 14
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(10-1,10-6)	|C(9,3)	|[('R.0', 9.0, u'10-1', u'9')]	|
|1	|C(8-1,8-3)	|C(7,3)	|[('R.0', 7.0, u'8-1', u'7')]	|
|2	|C(8-1,8-5)	|C(7,5)	|[('R.0', 7.0, u'8-1', u'7')]	|
|3	|C(13-1,13-8)	|C(12,4)	|[('R.0', 12.0, u'13-1', u'12')]	|
|4	|C(7-1,7-3)	|3 * 2 * 1 * 20	|[('R.0', 6.0, u'7-1', u'3 * 2 * 1')]	|
|5	|C(7-1,7-3)	|3 * 2 * 1 * 15	|[('R.0', 6.0, u'7-1', u'3 * 2 * 1')]	|
|6	|C(12-1,12-5)	|C(6+6-1, 6-1)	|[('R.0', 11.0, u'12-1', u'6+6-1')]	|
|7	|C(9-1,9-2)	|C(8,1)+2	|[('R.0', 8.0, u'9-1', u'C(8,1)')]	|
|8	|C(8-1,8-4)	|C(7,2)	|[('R.0', 7.0, u'8-1', u'7')]	|
|9	|C(14-1,14-7)	|C(13,5)	|[('R.0', 13.0, u'14-1', u'13')]	|
|10	|C(14-1,14-7)	|C(13,8)	|[('R.0', 13.0, u'14-1', u'13')]	|
|11	|C(9-1,9-2)	|C(8,2)	|[('R.0', 8.0, u'9-1', u'8')]	|
|12	|C(10-1,10-7)	|C(9,4)	|[('R.0', 9.0, u'10-1', u'9')]	|




### (12) Mistake Group Fraction of size 12




### (4) Mistake Group ['R.0.1'] of size 4
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(12-1,12-5)	|C(7+7-1, 7-1)	|[('R.0.1', 1.0, u'1', u'1')]	|
|1	|C(12-1,12-5)	|C(5+5-1, 5-1)	|[('R.0.1', 1.0, u'1', u'1')]	|
|2	|C(14-1,14-8)	|C(14+6-1,8-1)	|[('R.0.1', 1.0, u'1', u'1')]	|
|3	|C(12-1,12-4)	|C(8+3-1,3-1)	|[('R.0.1', 1.0, u'1', u'1')]	|




### (2) Mistake Group ['R.1.1'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(8-1,8-5)	|C(12,8) - C(8, 5)	|[('R.1.1', 5.0, u'5', u'5')]	|
|1	|C(10-1,10-2)	|8!/(6!*2!)	|[('R.1.1', 2.0, u'2', u'2!')]	|




### (1) Mistake Group ['R.0', 'R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(13-1,13-3)	|P(12,10)	|[('R.0', 12.0, u'13-1', u'12'), ('R.1', 10.0, u'13-3', u'10')]	|




### (46) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:dwzhang

	first_attempt
					2015-10-13 21:57:42
	part1_correct_attempt
					['0:00:00', u'12^13']
	part2_correct_attempt
					['0:04:56', u'C(13+(12-1), 12-1)']
	part3_incorrect_attempt
					('0:06:32', u'C(13+(12-1), 12-1) + 12')
					('0:06:38', u'C(13+(12-1), 12-1) * 12')
	part3_correct_attempt
					['0:10:42', u'C(1+12-1, 12-1)']

1 Student ID:jfalcone

	first_attempt
					2015-10-14 22:31:55
	part1_correct_attempt
					['0:00:00', u'4^8']
	part2_correct_attempt
					['23:05:23', u'C(11,8)']
	part3_incorrect_attempt
					('23:56:09', u'C(11,4)')
	part3_correct_attempt
					['23:56:26', u'C(7,4)']

2 Student ID:ccn001

	first_attempt
					2015-10-12 21:36:53
	part1_correct_attempt
					['0:00:00', u'2^15']
	part2_correct_attempt
					['4:50:24', u'16']
	part3_incorrect_attempt
					('5:05:55', u'13!/(1!(12!))')
	part3_correct_attempt
					['5:10:40', u'14!/(1!(13!))']

3 Student ID:d6he

	first_attempt
					2015-10-15 07:28:20
	part1_correct_attempt
					['0:00:00', u'6^7']
	part2_correct_attempt
					['0:04:55', u'12!/(7!5!)']
	part3_incorrect_attempt
					('0:06:07', u'12!/(7!5!)')
					('0:06:15', u'6*12!/(7!5!)')
					('0:07:25', u'7*12!/(7!5!)')
	part3_correct_attempt
					['0:09:29', u'6']

4 Student ID:vsamant

	first_attempt
					2015-10-10 16:16:35
	part1_correct_attempt
					['0:00:00', u'6^9']
	part2_correct_attempt
					['1:10:04', u'C(14,9)']
	part3_incorrect_attempt
					('1:10:46', u'C(11,9)')
	part3_correct_attempt
					['1:11:23', u'C(8,3)']

5 Student ID:ppanourg

	first_attempt
					2015-10-15 07:21:47
	part1_correct_attempt
					['0:00:00', u'(C(4,1))^8']
	part2_correct_attempt
					['0:02:32', u'C(11,3)']
	part3_incorrect_attempt
					('0:04:20', u'C(10,3)')
	part3_correct_attempt
					['0:05:04', u'C(7,3)']

6 Student ID:alakamsa

	first_attempt
					2015-10-10 19:56:54
	part1_correct_attempt
					['0:00:00', u'3^14']
	part2_correct_attempt
					['0:04:17', u'C(16,2)']
	part3_incorrect_attempt
					('0:39:44', u'C(14,3)')
	part3_correct_attempt
					['0:39:58', u'C(13,2)']

7 Student ID:qtluong

	first_attempt
					2015-10-12 20:07:58
	part1_correct_attempt
					['0:00:00', u'9^11']
	part2_correct_attempt
					['0:00:06', u'19!/(11!8!)']
	part3_incorrect_attempt
					('0:00:42', u'11!/(2!8!)')
	part3_correct_attempt
					['0:00:50', u'10!/(2!8!)']

8 Student ID:asp025

	first_attempt
					2015-10-15 18:43:47
	part1_correct_attempt
					['0:00:00', u'9^14']
	part2_correct_attempt
					['0:12:53', u'22!/(8!14!)']
	part3_incorrect_attempt
					('0:15:39', u'22!/(5!17!)')
	part3_correct_attempt
					['0:18:36', u'13!/(8!5!)']

9 Student ID:mhale

	first_attempt
					2015-10-14 21:55:18
	part1_correct_attempt
					['0:00:00', u'4^7']
	part2_correct_attempt
					['0:00:50', u'120']
	part3_incorrect_attempt
					('0:01:58', u'35 * 20')
	part3_correct_attempt
					['0:02:32', u'20']

10 Student ID:krau

	first_attempt
					2015-10-14 03:43:05
	part1_correct_attempt
					['0:00:00', u'7^11']
	part2_correct_attempt
					['0:03:42', u'17!/11!/6!']
	part3_incorrect_attempt
					('0:04:47', u'13!/7!/6!')
					('0:05:38', u'13!/11!/2!')
	part3_correct_attempt
					['0:07:16', u'10!/4!/6!']

11 Student ID:s1powers

	first_attempt
					2015-10-11 00:25:47
	part1_correct_attempt
					['0:00:00', u'5^7']
	part2_correct_attempt
					['19:10:45', u'11!/(4!7!)']
	part3_incorrect_attempt
					('19:11:33', u'5!/(3!2!)')
	part3_correct_attempt
					['19:12:23', u'6!/(4!2!)']

12 Student ID:pvl001

	first_attempt
					2015-10-13 19:42:40
	part1_correct_attempt
					['0:00:00', u'3^7']
	part2_correct_attempt
					['-1 day, 23:59:31', u'36']
	part3_incorrect_attempt
					('0:03:12', u'3 * 2 * 1 * 4 * 8')
					('0:03:30', u'3 * 2 * 1 * 3 * 3 * 3 * 3')
	part3_correct_attempt
					['0:05:14', u'15']

13 Student ID:mrchin

	first_attempt
					2015-10-14 22:26:56
	part1_correct_attempt
					['0:00:00', u'4^12']
	part2_correct_attempt
					['0:01:21', u'15!/(12!*3!)']
	part3_incorrect_attempt
					('0:01:45', u'11!/(3!*3!)')
					('0:02:02', u'7!/(3!*3!)')
					('0:02:30', u'16!/(8!*8!)')
					('0:03:27', u'10!/(4!*6!)')
					('0:03:33', u'10!/(2!*8!)')
					('0:04:05', u'10!/(7!*3!)')
	part3_correct_attempt
					['0:05:54', u'11!/(8!*3!)']

14 Student ID:jag028

	first_attempt
					2015-10-15 16:45:16
	part1_correct_attempt
					['0:00:00', u'7^10']
	part2_correct_attempt
					['0:14:45', u'C(16,6)']
	part3_incorrect_attempt
					('0:16:11', u'C(10,2)')
	part3_correct_attempt
					['0:16:29', u'C(9,3)']

15 Student ID:jic212

	first_attempt
					2015-10-12 06:42:45
	part1_correct_attempt
					['0:00:00', u'4^9']
	part2_correct_attempt
					['0:40:38', u'C(12,9)']
	part3_incorrect_attempt
					('1:20:45', u'C(8,4)*C(8,5)')
					('1:21:14', u'C(7,4)*C(8,5)')
					('1:22:18', u'9*8*7*6*C(8,5)')
					('1:22:57', u'C(9,4)*C(8,5)')
	part3_correct_attempt
					['1:29:47', u'C(8,5)']

16 Student ID:edescobe

	first_attempt
					2015-10-12 19:57:18
	part1_correct_attempt
					['0:00:00', u'34522712143931']
	part2_correct_attempt
					['0:03:48', u'1144066']
	part3_incorrect_attempt
					('0:04:40', u'11*11')
	part3_correct_attempt
					['0:11:24', u'66']

17 Student ID:v4zhang

	first_attempt
					2015-10-15 06:57:51
	part1_correct_attempt
					['0:00:00', u'13^15']
	part2_correct_attempt
					['0:11:27', u'C(27, 15)']
	part3_incorrect_attempt
					('0:11:34', u'13! * C(27, 15)')
					('0:12:08', u'13! * C(14, 2)')
					('0:12:23', u'13^15 * C(14, 2)')
					('0:14:14', u'C(27, 13) * C(14, 2)')
					('0:14:20', u'C(27, 15) * C(14, 2)')
					('16:34:48', u'13! * C(13, 12)')
					('16:35:26', u'13^15 * C(27, 15)')
					('16:41:05', u'13^15 * C(12,2)')
					('16:41:17', u'13^15 * C(13,2)')
					('16:41:30', u'C(27, 13) * C(13,2)')
	part3_correct_attempt
					['16:45:44', u'C(2+13-1, 13-1)']

18 Student ID:hak014

	first_attempt
					2015-10-13 05:03:47
	part1_correct_attempt
					['0:00:00', u'7^11']
	part2_correct_attempt
					['-1 day, 23:54:13', u'17!/(11!6!)']
	part3_incorrect_attempt
					('0:02:11', u'11!/(6!5!)')
	part3_correct_attempt
					['0:02:43', u'10!/(6!4!)']

19 Student ID:xil109

	first_attempt
					2015-10-10 19:30:28
	part1_correct_attempt
					['0:00:00', u'2^13']
	part2_correct_attempt
					['0:01:01', u'C(14,13)']
	part3_incorrect_attempt
					('0:02:15', u'C(13,2)*C(12,11)')
					('0:02:57', u'2* C(13,2)*C(12,11)')
					('0:04:11', u'2*C(13,2)*C(12,11)')
					('0:30:02', u'C(13,2)*C(12,11)')
					('0:54:28', u'P(13,2)*C(12,11)')
	part3_correct_attempt
					['0:55:20', u'C(12,11)']

20 Student ID:asrana

	first_attempt
					2015-10-15 19:45:59
	part1_correct_attempt
					['0:00:00', u'8^14']
	part2_correct_attempt
					['0:09:00', u'116280']
	part3_incorrect_attempt
					('0:15:36', u'3003*1716')
	part3_correct_attempt
					['0:22:38', u'1716']

21 Student ID:jmmcalex

	first_attempt
					2015-10-15 07:43:46
	part1_correct_attempt
					['0:00:00', u'10^12']
	part2_correct_attempt
					['0:04:02', u'21!/[12!9!]']
	part3_incorrect_attempt
					('0:33:13', u'9!/[7!2!]')
					('0:34:30', u'21!/[12!9!]')
	part3_correct_attempt
					['0:35:21', u'11!/[9!2!]']

22 Student ID:lalacson

	first_attempt
					2015-10-11 21:52:27
	part1_correct_attempt
					['0:00:00', u'13^14']
	part2_correct_attempt
					['0:08:22', u'C(13-1+14,14)']
	part3_incorrect_attempt
					('0:12:00', u'C(12-1+13,13)')
					('0:12:06', u'C(13-1+13,13)')
	part3_correct_attempt
					['0:12:29', u'C(13-1+1,1)']

23 Student ID:jap009

	first_attempt
					2015-10-15 21:37:45
	part1_correct_attempt
					['0:00:00', u'5^7']
	part2_correct_attempt
					['0:00:47', u'11!/(7!4!)']
	part3_incorrect_attempt
					('0:02:53', u'8!/(2!6!)')
	part3_correct_attempt
					['0:03:13', u'6!/(2!4!)']

24 Student ID:agian

	first_attempt
					2015-10-15 07:19:54
	part1_correct_attempt
					['0:00:00', u'8^9']
	part2_correct_attempt
					['0:00:30', u'C(9+8-1,9)']
	part3_incorrect_attempt
					('0:00:56', u'C(9-1,8)')
	part3_correct_attempt
					['0:01:16', u'C(9-1,1)']

25 Student ID:kalang

	first_attempt
					2015-10-14 05:58:33
	part1_correct_attempt
					['0:00:00', u'7^10']
	part2_correct_attempt
					['17:00:56', u'C(16,10)']
	part3_incorrect_attempt
					('17:02:10', u'C(16,2)')
					('17:02:19', u'C(16,8)')
					('17:02:23', u'C(16,7)')
					('17:03:19', u'C(13,10)')
	part3_correct_attempt
					['17:05:01', u'C(9,3)']

26 Student ID:dgunawan

	first_attempt
					2015-10-15 19:00:00
	part1_correct_attempt
					['0:00:00', u'3^13']
	part2_correct_attempt
					['0:00:00', u'(13+3-1)!/(13!*(3-1)!)']
	part3_incorrect_attempt
					('0:00:00', u'(10+2-1)!/(10!*(2-1)!)')
	part3_correct_attempt
					['0:00:08', u'(10+3-1)!/(10!*(3-1)!)']

27 Student ID:aakumar

	first_attempt
					2015-10-11 04:51:34
	part1_correct_attempt
					['0:00:00', u'6^7']
	part2_correct_attempt
					['0:11:22', u'C(12,7)']
	part3_incorrect_attempt
					('0:13:08', u'C(8,7)')
					('0:14:43', u'C(12,1)')
					('0:18:00', u'C(5,5)')
					('0:18:59', u'C(8,7)')
					('0:19:46', u'C(7,7)')
	part3_correct_attempt
					['0:20:12', u'C(6,1)']

28 Student ID:kew017

	first_attempt
					2015-10-15 17:43:50
	part1_correct_attempt
					['0:00:00', u'6^10']
	part2_correct_attempt
					['0:01:47', u'15!/(5!10!)']
	part3_incorrect_attempt
					('0:01:47', u'10!/(4!6!)')
	part3_correct_attempt
					['0:02:31', u'9!/(4!5!)']

29 Student ID:z3meng

	first_attempt
					2015-10-15 02:43:54
	part1_correct_attempt
					['0:00:00', u'6^7']
	part2_correct_attempt
					['0:00:00', u'12!/(7!*5!)']
	part3_incorrect_attempt
					('0:00:00', u'6!*6')
					('0:00:36', u'7*6!*6')
	part3_correct_attempt
					['0:05:04', u'6']

30 Student ID:lcardoso

	first_attempt
					2015-10-13 16:43:59
	part1_correct_attempt
					['0:00:00', u'7^14']
	part2_correct_attempt
					['-1 day, 23:56:31', u'C(14-1+7,7-1)']
	part3_incorrect_attempt
					('0:21:18', u'C(14,7) + C(14-7-1+7,7-1)')
					('0:22:25', u'14^7')
	part3_correct_attempt
					['0:27:26', u'C(14-(7*1)-1+7,7-1)']

31 Student ID:dando

	first_attempt
					2015-10-09 23:11:28
	part1_correct_attempt
					['0:00:00', u'6^11']
	part2_correct_attempt
					['0:31:23', u'C(16,11)']
	part3_incorrect_attempt
					('0:31:23', u'6^6 * C(16,5)')
	part3_correct_attempt
					['0:33:45', u'C(10,5)']

32 Student ID:chc286

	first_attempt
					2015-10-11 23:17:46
	part1_correct_attempt
					['0:00:00', u'4^10']
	part2_correct_attempt
					['0:05:35', u'C(13,3)']
	part3_incorrect_attempt
					('0:06:44', u'C(7,3)')
	part3_correct_attempt
					['0:07:41', u'C(9,3)']

33 Student ID:bakang

	first_attempt
					2015-10-15 02:01:21
	part1_correct_attempt
					['0:00:00', u'6^7']
	part2_correct_attempt
					['0:00:41', u'C(12,7)']
	part3_incorrect_attempt
					('0:02:47', u'C(7,1)')
	part3_correct_attempt
					['0:03:08', u'C(6,1)']

34 Student ID:csl030

	first_attempt
					2015-10-14 01:54:21
	part1_correct_attempt
					['0:00:00', u'5^8']
	part2_correct_attempt
					['0:04:48', u'C(12,8)']
	part3_incorrect_attempt
					('0:08:06', u'C(8, 5)  + C(7,3)')
	part3_correct_attempt
					['0:08:30', u' C(7,3)']

35 Student ID:rraiyyan

	first_attempt
					2015-10-14 23:30:50
	part1_correct_attempt
					['0:00:00', u'6^7']
	part2_correct_attempt
					['-1 day, 23:50:03', u'C(12,7)']
	part3_incorrect_attempt
					('0:04:24', u'6*6!')
	part3_correct_attempt
					['0:05:04', u'6']

36 Student ID:dtea

	first_attempt
					2015-10-15 23:14:02
	part1_correct_attempt
					['0:00:00', u'13^15']
	part2_correct_attempt
					['0:03:43', u'27!/(15!(27-15)!)']
	part3_incorrect_attempt
					('0:04:35', u'27!/(15!(27-15)!)')
					('0:04:48', u'27!/(2!(27-2)!)')
					('0:04:59', u'16!/(2!(16-2)!)')
					('0:05:20', u'13!/(2!(13-2)!)')
	part3_correct_attempt
					['0:05:42', u'14!/(2!(14-2)!)']

37 Student ID:ksrijong

	first_attempt
					2015-10-15 05:28:38
	part1_correct_attempt
					['0:00:00', u'6^8']
	part2_correct_attempt
					['0:01:46', u'C(13,8)']
	part3_incorrect_attempt
					('0:04:37', u'C(7,6)')
	part3_correct_attempt
					['0:05:17', u'C(7,2)']

38 Student ID:arc013

	first_attempt
					2015-10-14 03:05:19
	part1_correct_attempt
					['0:00:00', u'2^10']
	part2_correct_attempt
					['0:00:44', u'C(11, 10)']
	part3_incorrect_attempt
					('0:01:35', u'C(10, 9)')
	part3_correct_attempt
					['0:15:16', u'C(9, 8)']

39 Student ID:azkong

	first_attempt
					2015-10-15 18:47:05
	part1_correct_attempt
					['0:00:00', u'7^8']
	part2_correct_attempt
					['0:00:45', u'C(14, 8)']
	part3_incorrect_attempt
					('0:01:36', u'C(14, 7)')
					('0:04:01', u'C(13, 8)')
					('0:04:23', u'C(14, 8)')
					('0:04:56', u'C(8, 1)')
	part3_correct_attempt
					['0:05:02', u'C(7, 1)']

40 Student ID:mitopete

	first_attempt
					2015-10-13 20:19:08
	part1_correct_attempt
					['0:00:00', u'4^10']
	part2_correct_attempt
					['20:26:49', u'13!/(10!3!)']
	part3_incorrect_attempt
					('20:40:27', u'9!/(4!5!)')
	part3_correct_attempt
					['20:43:15', u'9!/(6!3!)']

41 Student ID:yjshin

	first_attempt
					2015-10-15 10:50:38
	part1_correct_attempt
					['0:00:00', u'11^13']
	part2_correct_attempt
					['0:16:08', u'23!/(13!10!)']
	part3_incorrect_attempt
					('0:22:37', u'12!(2!10!)')
	part3_correct_attempt
					['0:22:42', u'12!/(2!10!)']

42 Student ID:vasharma

	first_attempt
					2015-10-11 06:30:17
	part1_correct_attempt
					['0:00:00', u'9^11']
	part3_incorrect_attempt
					('0:06:06', u'C(19,11)+C(19,2)')
					('0:06:16', u'C(19,11)+C(11,2)')
					('0:06:21', u'C(19,11)+C(10,2)')
					('0:06:29', u'C(19,11)+C(9,2)')
	part3_correct_attempt
					['0:06:49', u'C(10,2)']

43 Student ID:yos017

	first_attempt
					2015-10-14 06:22:26
	part1_correct_attempt
					['0:00:00', u'10^13']
	part2_correct_attempt
					['0:02:04', u'22!/(13!*9!)']
	part3_incorrect_attempt
					('0:04:02', u'10!*10^3')
					('0:10:36', u'(10!*12!)/(3!*9!)')
					('0:14:56', u'(13!*12!)/(10!*3!*3!*9!)')
					('0:16:38', u'(13!*10!)/(10!*3!*3!*7!)')
	part3_correct_attempt
					['0:19:57', u'12!/(3!*9!)']

44 Student ID:aurodrig

	first_attempt
					2015-10-15 23:34:01
	part1_correct_attempt
					['0:00:00', u'8^11']
	part2_correct_attempt
					['0:03:44', u'18!/(7!11!)']
	part3_incorrect_attempt
					('0:05:03', u'11!/(8!3!)')
					('0:06:42', u'(13!)/(10!3!)')
					('0:07:44', u'(11!)/(8!3!)')
	part3_correct_attempt
					['0:09:48', u'(10!)/(7!3!)']

45 Student ID:kgrozav

	first_attempt
					2015-10-15 18:55:24
	part1_correct_attempt
					['0:00:00', u'8^9']
	part2_correct_attempt
					['0:04:36', u'(16)!/(9!*7!)']
	part3_incorrect_attempt
					('0:11:02', u'9!/9!')
	part3_correct_attempt
					['0:11:21', u'8']












