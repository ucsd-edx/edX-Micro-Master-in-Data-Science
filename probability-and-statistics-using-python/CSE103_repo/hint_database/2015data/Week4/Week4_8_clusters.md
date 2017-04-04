#Problem 8

    In Texas Hold'Em, a standard 52-card deck is used. Each player is dealt two cards from the deck face down so that only the player that got the two cards can see them. After checking his two cards, a player places a bet. The dealer then puts 5 cards from the deck face up on the table, this is called the "board" or the "communal cards" because all players can see and used them. The board is layed down in 3 steps: first, the dealer puts 3 cards down (that is called "the flop") followed by two single cards, the first is called "the turn" and the second is called "the river". After the flop, the turn and the river each player can update their bet.  The winner  of the game is the person that can form the strongest 5-card hand from the 2 hand in their hand and the 5 cards in the board.
    ---
    In previous homework you calculated the probability of getting each 5-card hand.
    Here we are interested in something a bit more complex: what is the probability of a particular hand given the cards that are currently available to the player.

    The outcome space in this kind of problem is the set of 7 cards the user has at her disposal after all 5 board cards have been dealt. The size of this space is [`|\Omega|=C(52,7)`]

    Suppose that [`A,B`] are events, i.e. subsets of [`\Omega`]. We will want to calculate conditional probabilities of the type [`P(A|B)`]. Given that the probability of each set of seven cards  is equal to [`1/C(52,7)`] we get that the conditional probability can be expressed as:

    [``P(A|B) = \frac{P(A \cap B)}{P(B)} =
    \frac{\frac{|A \cap B|}{|\Omega|}}{\frac{|B|}{|\Omega|}}
    =\frac{|A \cap B|}{|B|}``]

    Therefore the calculation of conditional probability (for finite sample spaces with uniform distribution) boils down to calculating the ratio between the sizes of two sets.
    ---
    *Suppose you have been dealt "4[`\heartsuit`], 5[`\heartsuit`]".*

    *What is the conditional probability that you will get a straight given that you have been dealt these two cards, and that the flop is "2[`\clubsuit`], 6[`\spadesuit`], K[`\diamondsuit`]"?*
        - Define [`B`] as the set {7-card hands that contain these 5 cards already revealed}.
        - Define [`A`] as the set {7-card hands that contain a straight}.
        The question is asking for [`P(A|B)`]. According to the formula above we need to find [`|A\cap B|`] and [`|B|`].
        - In this case [`A \cap B`] is the set {7-card hands that contain the 5 revealed cards *AND* contain a straight}. To get a straight, the remaining two cards (turn and river) must either be {7,8} or contain 3. We hence define two subsets within [`A \cap B`]:
            - [`S_1`]: {7-card hands that are in [`A \cap B`] *AND* the remaining two cards are 7 and 8, regardless of order}.
                [`|S_1|=`] [____________]{Compute("4^2")}
            - [`S_2`]: {7-card hands that are in [`A \cap B`] *AND* its turn and river contain 3}.
                [`|S_2|=`] [____________]{Compute("C(52-5,2)-C(52-5-4,2)")}
            Because there is no overlap in these two cases ([`S_1 \cap S_2 = \emptyset`]) and these two cases cover all possible valid hands ([`A \cap B = S_1 \cup S_2`]), by definition [`S_1`] and [`S_2`] form a _partition_ of [`A \cap B`], and we have [`|A \cap B| = |S_1| + |S_2|`].
        - Computing [`|B|`] should be easy. 5 cards in the hand are already fixed, we have the freedom of choosing the turn and the river from the 47 cards in the deck. [`|B| = `][______]{Compute("C(47,2)")}.
        - The conditional probability [`P(A|B) = \frac{P(A \cap B)}{P(B)} = \frac{|A\cap B|}{|B|} = \frac{|S_1|+|S_2|}{|B|}`] is [____________]{Compute("(C(52-5,2)-C(52-5-4,2)+4^2)/C(52-5,2)")}


## Part 1

### (126) Mistake Group Digits of size 126




### (80) Mistake Group ['R.1'] of size 80
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4^2	|C(8,2)	|[('R.1', 2.0, u'2', u'2')]	|
|1	|4^2	|C(8,2)*C(47,2)*2	|[('R.1', 2.0, u'2', u'2')]	|
|2	|4^2	|C(45,2)	|[('R.1', 2.0, u'2', u'2')]	|
|3	|4^2	|C(52-5,2)	|[('R.1', 2.0, u'2', u'2')]	|
|4	|4^2	|C(2*4,2)	|[('R.1', 2.0, u'2', u'2')]	|
|5	|4^2	|8*7*50*49*48*47*46/2!	|[('R.1', 2.0, u'2', u'2!')]	|
|6	|4^2	|C(8, 2)	|[('R.1', 2.0, u'2', u'2')]	|
|7	|4^2	|C(47, 2)	|[('R.1', 2.0, u'2', u'2')]	|
|8	|4^2	|C(7,2)	|[('R.1', 2.0, u'2', u'2')]	|
|9	|4^2	|C(47,2)	|[('R.1', 2.0, u'2', u'2')]	|
|10	|4^2	|C(15,2)	|[('R.1', 2.0, u'2', u'2')]	|
|11	|4^2	|C(47,4)*2	|[('R.1', 2.0, u'2', u'2')]	|
|12	|4^2	|C(4^2, 2)	|[('R.1', 2.0, u'2', u'2')]	|
|13	|4^2	|4*47*2	|[('R.1', 2.0, u'2', u'2')]	|
|14	|4^2	|4*4*2	|[('R.1', 2.0, u'2', u'2')]	|
|15	|4^2	|C(16,2)	|[('R.1', 2.0, u'2', u'2')]	|
|16	|4^2	|C(43,2)	|[('R.1', 2.0, u'2', u'2')]	|
|17	|4^2	|C(47,8)*2	|[('R.1', 2.0, u'2', u'2')]	|
|18	|4^2	|(C(1, 1) + C(4, 1)) * 2	|[('R.1', 2.0, u'2', u'2')]	|
|19	|4^2	|8*4*2	|[('R.1', 2.0, u'2', u'2')]	|
|20	|4^2	|C(4,2)*2	|[('R.1', 2.0, u'2', u'2')]	|
|21	|4^2	|184-2	|[('R.1', 2.0, u'2', u'2')]	|
|22	|4^2	|C(5,2)	|[('R.1', 2.0, u'2', u'2')]	|
|23	|4^2	|C(8, 2) *2	|[('R.1', 2.0, u'2', u'2')]	|




### (26) Mistake Group Fraction of size 26




### (8) Mistake Group ['R.0'] of size 8
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4^2	|4+4	|[('R.0', 4.0, u'4', u'4')]	|
|1	|4^2	|4*47	|[('R.0', 4.0, u'4', u'4')]	|
|2	|4^2	|4*46	|[('R.0', 4.0, u'4', u'4')]	|
|3	|4^2	|C(4,1)+C(4,1)	|[('R.0', 4.0, u'4', u'C(4,1)')]	|
|4	|4^2	|4C(52-5,2)	|[('R.0', 4.0, u'4', u'4')]	|
|5	|4^2	|4+C(8,2)	|[('R.0', 4.0, u'4', u'4')]	|
|6	|4^2	|C(4, 1) + C(4, 1)	|[('R.0', 4.0, u'4', u'C(4, 1)')]	|




### (5) Mistake Group ['R.0', 'R.1'] of size 5
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|4^2	|C(4,1)*2	|[('R.0', 4.0, u'4', u'C(4,1)'), ('R.1', 2.0, u'2', u'2')]	|
|1	|4^2	|C(4,2)	|[('R.0', 4.0, u'4', u'4'), ('R.1', 2.0, u'2', u'2')]	|
|2	|4^2	|C(4,1) * 2	|[('R.0', 4.0, u'4', u'C(4,1)'), ('R.1', 2.0, u'2', u'2')]	|




### (4) Mistake Group Wrong_Sign of size 4




### (70) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:b3hwang

	first_attempt
					2015-10-21 02:16:42
	part1_incorrect_attempt
					('0:00:00', u'C(47,2) + C(47,1)')
					('0:00:48', u'C(8,2) + C(4,1)')
	part1_correct_attempt
					['0:03:52', u'2*8']

1 Student ID:ccn001

	first_attempt
					2015-10-20 22:24:35
	part1_incorrect_attempt
					('0:00:00', u'(4^5)(12!/(2!10!))(4^5)(8!/(2!6!))')
					('0:00:00', u'C(5,5)*C(8,2)')
					('0:09:03', u'C(5,5)*(C(47,2)-C(39,2))')
					('0:10:39', u'C(5,5)*C(16,2)')
	part1_correct_attempt
					['5:02:06', u'C(5,5)*16']

2 Student ID:lywong

	first_attempt
					2015-10-21 07:51:32
	part1_incorrect_attempt
					('0:00:00', u'C(47,2)-C(43,2)')
					('0:00:56', u'C(47,2)-C(39,2)')
					('0:01:45', u'C(47,2)-16')
					('0:04:43', u'C(47,2)+16')
					('1:58:26', u'C(47,2)-16')
					('2:00:47', u'C(47,2)+16')
					('2:01:42', u'C(47,2)-C(39,2)')
	part1_correct_attempt
					['2:03:53', u'C(47,2)-(C(47,2)-16)']

3 Student ID:vsamant

	first_attempt
					2015-10-21 18:56:55
	part1_incorrect_attempt
					('0:00:00', u'2*4')
					('0:00:35', u'7*4+2*4')
					('0:03:08', u'C(47,1)+C(46,1)')
	part1_correct_attempt
					['0:03:38', u'C(4,1)*C(4,1)']

4 Student ID:mcatozzi

	first_attempt
					2015-10-21 00:11:49
	part1_incorrect_attempt
					('0:00:00', u'16+204')
	part1_correct_attempt
					['0:04:40', u'16']

5 Student ID:kbielawi

	first_attempt
					2015-10-22 17:13:14
	part1_incorrect_attempt
					('0:00:00', u'(13-3)*4^5*C(52-5,2)')
					('0:01:23', u'4*4^3*C(52-5,2)')
					('0:01:44', u'4*4^3*C((52-5),2)')
	part1_correct_attempt
					['0:05:11', u'4^2']

6 Student ID:glcohen

	first_attempt
					2015-10-18 01:08:35
	part1_incorrect_attempt
					('0:00:00', u'C(52,7)')
					('0:00:22', u'C(52,5)')
					('0:00:00', u'C(46,1)*C(47,1)')
					('0:04:15', u'(C(46,1)*C(47,1))* 6180020')
					('0:04:37', u'(C(47,2))* 6180020')
					('0:08:18', u'(C(47,2)*6180020)*(4/46)*(4/47)')
	part1_correct_attempt
					['2 days, 14:12:03', u'C(4,1)C(4,1)']

7 Student ID:fichoi

	first_attempt
					2015-10-22 04:51:26
	part1_incorrect_attempt
					('0:00:00', u'C(47,2) - C(43, 2)')
					('0:13:38', u'C(47,2) - C(39, 2)')
					('0:00:00', u'C(47,2) - C(43, 1) - C(39, 1)')
					('0:00:12', u'C(47,2) - (C(43, 1) + C(39, 1))')
	part1_correct_attempt
					['0:18:38', u'16']

8 Student ID:atorr

	first_attempt
					2015-10-22 23:14:53
	part1_incorrect_attempt
					('0:00:00', u'(47 * 46) *  (4^5) * 47 * 46')
	part1_correct_attempt
					['0:14:32', u'16']

9 Student ID:any027

	first_attempt
					2015-10-19 20:30:06
	part1_incorrect_attempt
					('0:00:00', u'C(47,8)')
	part1_correct_attempt
					['0:00:56', u'16']

10 Student ID:rwthomps

	first_attempt
					2015-10-20 23:03:39
	part1_incorrect_attempt
					('0:00:00', u'C(4, 2) + C(4, 2)')
	part1_correct_attempt
					['0:00:22', u'16']

11 Student ID:sachadal

	first_attempt
					2015-10-22 19:23:28
	part1_incorrect_attempt
					('0:00:00', u'C(47,2)*C(4,1)*C(4,1)')
	part1_correct_attempt
					['0:08:10', u'4*4']

12 Student ID:dcrume

	first_attempt
					2015-10-21 20:04:57
	part1_incorrect_attempt
					('0:00:00', u'C(52,4)*(52-6)')
					('0:00:00', u'C(52,7) - C(47,2)')
					('0:00:00', u'C(47,1)*C(46,1)')
	part1_correct_attempt
					['1 day, 2:00:00', u'16']

13 Student ID:ctgraves

	first_attempt
					2015-10-21 23:18:19
	part1_incorrect_attempt
					('0:00:00', u'C(52,2)-C(52-8,2)')
					('0:00:40', u'C(52-5,2)-C(52-5-8,2)')
					('0:01:34', u'(52-5)!/(2!*(52-7)! ) - (52-5-8)!/(2!*(52-5-8-2)!)')
					('0:01:58', u'(52-5)!-  (52-5-8)!')
					('0:23:59', u'4*4 + 4*4')
					('0:25:51', u'C(52-5, 2) - C(52-5-4,2)')
					('0:26:27', u'C(4,1)')
	part1_correct_attempt
					['0:28:03', u'16']

14 Student ID:dkurli

	first_attempt
					2015-10-21 04:03:07
	part1_incorrect_attempt
					('0:00:00', u'47*46')
					('0:00:36', u'47*46-15')
					('0:02:03', u'15*46')
	part1_correct_attempt
					['0:03:41', u'C(4,1)*4']

15 Student ID:beyounge

	first_attempt
					2015-10-17 06:04:57
	part1_incorrect_attempt
					('0:00:00', u'2*C(4,1)')
	part1_correct_attempt
					['0:00:25', u'C(4,1) * C(4,1)']

16 Student ID:mbl003

	first_attempt
					2015-10-21 19:30:15
	part1_incorrect_attempt
					('0:00:00', u'C(52-5,8)')
	part1_correct_attempt
					['0:04:18', u'C(4,1)*C(4,1)']

17 Student ID:nhn018

	first_attempt
					2015-10-22 20:11:28
	part1_incorrect_attempt
					('0:00:00', u'(13-3)*4^5*C(52-5,2)')
					('0:05:04', u'4*4^3*C(52-5,2)')
	part1_correct_attempt
					['0:09:50', u'4^2']

18 Student ID:j5phung

	first_attempt
					2015-10-16 18:09:55
	part1_incorrect_attempt
					('0:00:00', u'8*7')
					('0:11:28', u'C(8,2)*C(47,2)*C(7,5)')
					('0:12:40', u'C(8,2)*C(47,2)*9')
					('0:13:16', u'C(8,2)*C(47,2)*10')
					('0:14:16', u'C(8,2)*C(47,2)*6180020')
					('0:15:18', u'C(8,2)*C(47,2)*C(13,5)*C(13,2)')
					('0:16:01', u'C(8,2)*C(47,2)*C(13,5)*C(47,2)')
					('0:16:29', u'C(8,2)*C(47,2)*C(13,5)')
					('0:16:52', u'C(8,2)*C(47,2)*40')
					('0:17:51', u'C(8,2)*C(47,2)*4^10')
					('0:19:58', u'C(8,2)*C(47,2)*13*(5^5-C(5,1))')
					('0:20:28', u'C(8,2)*C(47,2)*13')
					('0:21:16', u'C(8,2)*C(47,2)*C(13,5)')
					('0:22:21', u'C(8,2)*C(47,2)*3')
					('0:26:34', u'C(8,2)*C(47,2)*9')
					('0:26:41', u'C(8,2)*C(47,2)*9*4')
					('0:27:05', u'C(8,2)*C(47,2)*9*4*C(46,2)')
					('0:46:09', u'C(8,2)*C(47,2)*C(13,5)*C(42,2)')
					('0:47:15', u'C(8,2)*C(47,2)*4*C(13,5)*C(47,2)')
					('0:47:22', u'C(8,2)*C(47,2)*C(13,5)*C(47,2)')
					('0:53:49', u'C(8,2)*C(47,2)*C(13,5)*C(8,2)')
					('0:55:27', u'C(47,8)*C(47,2)*C(13,5)*C(8,2)')
	part1_correct_attempt
					['1:01:01', u'C(4,1)^2']

19 Student ID:p4kumar

	first_attempt
					2015-10-22 21:36:49
	part1_incorrect_attempt
					('0:00:00', u'C(52, 7) - C(52 - 5 - 2*4, 7)')
					('0:08:17', u'C(52, 1)*5*C(4, 1)*C(4, 1)')
					('0:09:17', u'5*C(52, 1)*C(2*4, 2)')
					('0:10:09', u'C(52, 1)*C(52, 1)*C(52, 1)*C(52, 1)*C(52, 1)*C(2*4, 2)')
					('0:11:20', u'C(52, 1)*C(51,1)*C(50, 1)*C(49, 1)*C(48, 1)*C(2*4, 2)')
					('0:11:54', u'C(52, 1)*C(51,1)*C(50, 1)*C(49, 1)*C(48, 1)*P(2*4, 2)')
					('0:12:11', u'C(52, 5)*P(2*4, 2)')
	part1_correct_attempt
					['0:17:26', u'16']

20 Student ID:s2chaudh

	first_attempt
					2015-10-20 20:29:42
	part1_incorrect_attempt
					('0:00:00', u'C(48,2)-C(8,2)')
	part1_correct_attempt
					['1 day, 6:23:43', u'16']

21 Student ID:tpmach

	first_attempt
					2015-10-22 01:43:33
	part1_incorrect_attempt
					('0:00:00', u'C(52-5,8)')
	part1_correct_attempt
					['1:16:32', u'16']

22 Student ID:gsrandha

	first_attempt
					2015-10-18 23:56:45
	part1_incorrect_attempt
					('0:00:00', u'1.0*C(47,2)')
					('0:00:10', u'1.0*C(52-5,2)-C(52-5-4,2)')
	part1_correct_attempt
					['0:00:32', u'1.0*4**2']

23 Student ID:haw081

	first_attempt
					2015-10-22 04:08:55
	part1_incorrect_attempt
					('0:00:00', u'C(52,5)*C(52-5,2)')
					('0:00:52', u'C(13,5)*C(52-5,2)')
					('0:01:03', u'C(13,5)*C(8,2)')
					('0:03:47', u'C(8,2)*(52-5)')
					('0:09:35', u'C(52-5,4)')
					('0:10:12', u'C(52-5,1)C(52-6,1)')
					('0:00:00', u'C(52-5,1)C(52-6,1)')
					('0:04:22', u'C(52-5,1)+C(52-6,1)')
					('0:26:19', u'C(47,2)-16')
					('0:28:15', u'C(47,2)-C(47-16,2)')
	part1_correct_attempt
					['1:49:08', u'16']

24 Student ID:vqt004

	first_attempt
					2015-10-22 13:17:17
	part1_incorrect_attempt
					('0:00:00', u'2*4')
	part1_correct_attempt
					['0:07:38', u'4*4']

25 Student ID:muy002

	first_attempt
					2015-10-22 20:57:52
	part1_incorrect_attempt
					('0:00:00', u'C(4,1)')
					('0:07:40', u'C(47,2)-C(4,1)')
					('0:11:16', u'C(47,2)-C(43,2)')
	part1_correct_attempt
					['0:13:27', u'16']

26 Student ID:rsmurlo

	first_attempt
					2015-10-21 17:39:16
	part1_incorrect_attempt
					('0:00:00', u'C(47,4)C(46,4)')
	part1_correct_attempt
					['0:01:06', u'4*4']

27 Student ID:anl114

	first_attempt
					2015-10-22 16:54:21
	part1_incorrect_attempt
					('0:00:00', u'311875200*1081')
					('0:04:45', u'2598960*1081')
					('0:00:00', u'1086008*1081')
					('0:01:07', u'1086008*28')
					('0:06:50', u'C(47,2)-C(39,2)')
					('0:08:56', u'C(47,2)-C(39,2)-96')
	part1_correct_attempt
					['0:18:28', u'16']

28 Student ID:jnatale

	first_attempt
					2015-10-21 00:57:50
	part1_incorrect_attempt
					('0:00:00', u'C(7,2)*8')
	part1_correct_attempt
					['0:06:17', u'16']

29 Student ID:rlhagen

	first_attempt
					2015-10-18 18:55:13
	part1_incorrect_attempt
					('0:00:00', u'47!/(2!(47-2)!)')
					('0:04:17', u'39!/(2!(39-2)!)')
					('0:05:51', u'(47!/(2!(47-2)!))-(39!/(2!(39-2)!))')
					('0:12:18', u'(47!/(2!(47-2)!))-(39!/(2!(39-2)!))')
					('0:18:44', u'(43!/(1!(43-1)!))*(39!/(1!(39-1)!))')
					('0:19:16', u'(43!/(1!(43-1)!))+(39!/(1!(39-1)!))')
					('0:20:47', u'(8!/(2!(8-2)!))')
					('0:21:44', u'(8!/(1!(8-1)!))*(7!/(1!(7-1)!))')
	part1_correct_attempt
					['0:24:29', u'16']

30 Student ID:nnh002

	first_attempt
					2015-10-22 03:24:47
	part1_incorrect_attempt
					('0:00:00', u'C(47,8)')
					('0:04:38', u'C(47,2)-C(39,2)')
	part1_correct_attempt
					['1:09:05', u'16']

31 Student ID:c1sorian

	first_attempt
					2015-10-21 21:37:07
	part1_incorrect_attempt
					('0:00:00', u'C(47,2)-C(39,2)')
	part1_correct_attempt
					['0:00:57', u'16']

32 Student ID:vsosnovs

	first_attempt
					2015-10-22 06:39:41
	part1_incorrect_attempt
					('0:00:00', u'C(47,5)')
	part1_correct_attempt
					['0:05:07', u'16']

33 Student ID:ajvanega

	first_attempt
					2015-10-22 01:19:23
	part1_incorrect_attempt
					('0:00:00', u'C(47,5)')
	part1_correct_attempt
					['0:02:39', u'16']

34 Student ID:jap009

	first_attempt
					2015-10-21 07:35:10
	part1_incorrect_attempt
					('0:00:00', u'C(47,8)')
					('0:00:00', u'8*7')
					('0:00:12', u'8*4')
	part1_correct_attempt
					['14:16:23', u'C(4,1)C(4,1)']

35 Student ID:dgunawan

	first_attempt
					2015-10-22 23:45:14
	part1_incorrect_attempt
					('0:00:00', u'C((52-5), 2) - C(12, 3)')
	part1_correct_attempt
					['0:45:23', u'8 * 2']

36 Student ID:hachrist

	first_attempt
					2015-10-21 22:34:05
	part1_incorrect_attempt
					('0:00:00', u'C(47,2) - C(43,2)')
					('0:01:30', u'C(47,2) - C(45,2)')
					('0:02:05', u'C(47,2) - C(39,2)')
	part1_correct_attempt
					['0:04:01', u'16']

37 Student ID:jdeon

	first_attempt
					2015-10-22 04:49:14
	part1_incorrect_attempt
					('0:00:00', u'8*4')
					('0:00:12', u'2*4*4')
	part1_correct_attempt
					['0:09:51', u'4*4']

38 Student ID:t1tran

	first_attempt
					2015-10-18 03:50:22
	part1_incorrect_attempt
					('0:00:00', u'C(8,2)+5')
					('0:11:06', u'C(47,2)-C(47-8,2)')
					('0:12:37', u'C(47,2)-C(47-4,2)')
	part1_correct_attempt
					['0:15:37', u'4*4']

39 Student ID:tcn013

	first_attempt
					2015-10-22 21:57:50
	part1_incorrect_attempt
					('0:00:00', u'C(47,2) - C(39,2)')
					('0:01:47', u'C(47,2) - C(8,2)')
	part1_correct_attempt
					['0:02:10', u'16']

40 Student ID:tcuddy

	first_attempt
					2015-10-17 21:22:07
	part1_incorrect_attempt
					('0:00:00', u'47!/(2!45!) - 8')
	part1_correct_attempt
					['0:15:57', u'16']

41 Student ID:dlgoldbe

	first_attempt
					2015-10-22 17:22:08
	part1_incorrect_attempt
					('0:00:00', u'(C(47,2)) - (C(43,2))')
	part1_correct_attempt
					['0:01:09', u'4*4']

42 Student ID:l8ngo

	first_attempt
					2015-10-22 02:58:27
	part1_incorrect_attempt
					('0:00:00', u'47!/[2!45!]')
					('0:00:00', u'47!/[2!45!]')
	part1_correct_attempt
					['1:11:53', u'4*4']

43 Student ID:sippolit

	first_attempt
					2015-10-20 16:31:13
	part1_incorrect_attempt
					('0:00:00', u'C(47,43)*C(46,42)')
					('0:00:21', u'C(47,43)-C(46,42)')
	part1_correct_attempt
					['0:02:01', u'4^2']

44 Student ID:djk006

	first_attempt
					2015-10-21 18:05:02
	part1_incorrect_attempt
					('0:00:00', u'(47!/(45!2!))-(43!/(41!2!))')
					('0:00:41', u'(47!/(45!2!))-(39!/(37!2!))')
					('0:01:34', u'(47!/(45!2!))-(39!/(37!2!))')
	part1_correct_attempt
					['0:02:12', u'16']

45 Student ID:klala

	first_attempt
					2015-10-21 03:47:39
	part1_incorrect_attempt
					('0:00:00', u'C(47,2) - C(39,2)')
					('0:00:35', u'C(47,2) - (4*4)')
	part1_correct_attempt
					['0:05:19', u'4*4']

46 Student ID:thwan

	first_attempt
					2015-10-19 16:07:25
	part1_incorrect_attempt
					('0:00:00', u'C(52-5,2)-C(52-5-8,2)')
					('0:00:00', u'C(52-5,2)-C(52-5-2,2)')
	part1_correct_attempt
					['4:08:58', u'16']

47 Student ID:dando

	first_attempt
					2015-10-23 00:10:07
	part1_incorrect_attempt
					('0:00:00', u'C(8,2) * C(4,1)')
					('0:01:18', u'C(8,1) * C(4,1)')
					('0:07:29', u'C(47,2) (C(47,2) - C(8,1) - C(4,1))')
					('0:07:39', u'C(47,2) - (C(47,2) - C(8,1) - C(4,1))')
					('0:10:35', u'C(47,2) - 16')
	part1_correct_attempt
					['0:10:43', u'16']

48 Student ID:eaherman

	first_attempt
					2015-10-22 14:59:46
	part1_incorrect_attempt
					('0:00:00', u'(4)(8)(7)')
					('0:00:14', u'(8)(7)')
					('0:00:23', u'(8)(3)')
					('0:00:30', u'(8)(4)')
					('0:05:10', u'C(52-5,8)C(52-6,4)')
					('0:11:07', u'(8)(4)(52-5)')
					('0:15:00', u'C(52-5,2)-32')
	part1_correct_attempt
					['0:31:34', u'[C(47,2) ]-[C(52-5,2)-16]']

49 Student ID:edescobe

	first_attempt
					2015-10-18 11:27:10
	part1_incorrect_attempt
					('0:00:00', u'C(47,2)-C(43,2)')
					('0:00:25', u'C(47,2)-C(39,2)')
	part1_correct_attempt
					['0:14:30', u'16']

50 Student ID:w4shin

	first_attempt
					2015-10-19 19:30:48
	part1_incorrect_attempt
					('0:00:00', u'C(52,5)*C(13,2)*C(4,2)')
					('0:01:52', u'C(13,2)*C(4,2)')
	part1_correct_attempt
					['0:21:28', u'4*4']

51 Student ID:anvan

	first_attempt
					2015-10-22 11:19:00
	part1_incorrect_attempt
					('0:00:00', u'48*16')

52 Student ID:achava

	first_attempt
					2015-10-21 22:13:36
	part1_incorrect_attempt
					('0:00:00', u'(C(47,2) * 20) * 8')
					('0:00:19', u'20 8')
					('0:00:00', u'6*8')
					('0:00:15', u'(6*4)*8')
	part1_correct_attempt
					['0:18:48', u'16']

53 Student ID:jguanzho

	first_attempt
					2015-10-19 22:42:13
	part1_incorrect_attempt
					('0:00:00', u'8*7*50*49*48*47*46')
					('0:02:31', u'(8!/(2!*6!))*(50!/(5!*45!))')
	part1_correct_attempt
					['1 day, 6:48:32', u'4**2']

54 Student ID:jtfrankl

	first_attempt
					2015-10-21 00:31:31
	part1_incorrect_attempt
					('0:00:00', u'C(52,5)*(C(47,8) +C(46,4))')
	part1_correct_attempt
					['2:06:25', u'4*4']

55 Student ID:c1wei

	first_attempt
					2015-10-21 22:14:08
	part1_incorrect_attempt
					('0:00:00', u'47*46')
					('0:00:00', u'47*46')
					('0:00:45', u'47*46')
					('0:00:00', u'4*47*2178365')
					('0:04:02', u'178365*46')
					('0:04:03', u'178365*46')
					('0:05:14', u'2162-1081')
	part1_correct_attempt
					['0:34:59', u'16']

56 Student ID:arc013

	first_attempt
					2015-10-21 10:16:12
	part1_incorrect_attempt
					('0:00:00', u'C(47,2) - C(39, 2)')
					('0:02:04', u'C(47,2) - C(39, 2)-12')
	part1_correct_attempt
					['0:06:06', u'16']

57 Student ID:ssamudra

	first_attempt
					2015-10-23 00:50:00
	part1_incorrect_attempt
					('0:00:00', u'C(47,3) - C(46,2)')

58 Student ID:mitopete

	first_attempt
					2015-10-21 01:46:15
	part1_incorrect_attempt
					('0:00:00', u'(C(52,7)-C(39,5))+(C(52,7)-C(43,5))')
					('0:00:19', u'(C(52,7)-C(39,5))+((C(52,7)-C(43,5)))')
					('0:01:38', u'C(52,7)-C(39,5)')
					('0:15:33', u'C(47,2)-C(43,2)')
					('0:17:15', u'C(47,2)-C(39,2)')
					('0:22:46', u'C(47,2)-C(39,2)')
					('0:00:00', u'C(52,2)-C(46,2)')
					('0:04:29', u'C(47,2)-C(39,2)')
	part1_correct_attempt
					['1:19:06', u'16']

59 Student ID:ajabasa

	first_attempt
					2015-10-22 06:21:18
	part1_incorrect_attempt
					('0:00:00', u'C(47, 2)-C(43,2)')
					('0:04:35', u'C(47, 2)-8*4')
					('0:07:20', u'C(47, 2)-C(39, 1)-C(42, 1)')
	part1_correct_attempt
					['0:10:38', u'C(47, 2)-(C(47,2)-16)']

60 Student ID:syip

	first_attempt
					2015-10-18 21:34:28
	part1_incorrect_attempt
					('0:00:00', u'8*4')
	part1_correct_attempt
					['0:32:01', u'4*4']

61 Student ID:v3doan

	first_attempt
					2015-10-22 20:50:58
	part1_incorrect_attempt
					('0:00:00', u'C(47, 8)')
					('0:01:59', u'2 * 4 * 4')
	part1_correct_attempt
					['0:03:26', u'16']

62 Student ID:cagatep

	first_attempt
					2015-10-22 21:17:10
	part1_incorrect_attempt
					('0:00:00', u'C(8, 1) + C(4, 1)')
	part1_correct_attempt
					['0:00:21', u'(C(4, 1) + C(4,1)) * 2']

63 Student ID:m8woo

	first_attempt
					2015-10-22 21:20:37
	part1_incorrect_attempt
					('0:00:00', u'C(4,1)^2*C(45,2)')
	part1_correct_attempt
					['0:00:49', u'C(4,1)^2']

64 Student ID:ggaddi

	first_attempt
					2015-10-20 01:07:11
	part1_incorrect_attempt
					('0:00:00', u'C(8, 1) + C(4, 1)')
	part1_correct_attempt
					['0:00:26', u'C(4,1)*C(4,1)']

65 Student ID:sghouse

	first_attempt
					2015-10-21 00:14:01
	part1_incorrect_attempt
					('0:00:00', u'47*46*45*44*43*42*41*40/(8*7*6*5*4*3*2)')
					('0:00:00', u'C(47,2)*4')
					('0:00:00', u'C(47,8)')
	part1_correct_attempt
					['23:59:41', u'16']

66 Student ID:mjethani

	first_attempt
					2015-10-22 14:39:52
	part1_incorrect_attempt
					('0:00:00', u'C(47,5)')
					('0:00:39', u'C(45,5)')
	part1_correct_attempt
					['0:27:01', u'16']

67 Student ID:ksmurlo

	first_attempt
					2015-10-20 23:53:31
	part1_incorrect_attempt
					('0:00:00', u'8*4')
	part1_correct_attempt
					['0:06:36', u'4*4']

68 Student ID:msaguiar

	first_attempt
					2015-10-21 03:59:46
	part1_incorrect_attempt
					('0:00:00', u'16+(4(46))')
	part1_correct_attempt
					['0:31:35', u'4**2']

69 Student ID:j2phung

	first_attempt
					2015-10-22 04:39:36
	part1_incorrect_attempt
					('0:00:00', u'(47!/(2!45!))-(39!/(2!37!))')
					('0:00:00', u'(4*(52-6)) - 16')
					('0:00:00', u'(47!/(2!45!)) - (84*2)')
					('0:01:24', u'(47!/(2!45!)) - (88*2)')
					('0:04:42', u'(47!/(2!45!)) - (172*2)')
	part1_correct_attempt
					['0:58:03', u'16']












## Part 2

### (303) Mistake Group Digits of size 303




### (69) Mistake Group ['R.0'] of size 69
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(52-5,2)-C(52-5-4,2)	|C(47,2)*C(4,1)	|[('R.0', 1081, u'C(52-5,2)', u'C(47,2)')]	|
|1	|C(52-5,2)-C(52-5-4,2)	|C(47,2) - C(45,2)	|[('R.0', 1081, u'C(52-5,2)', u'C(47,2)')]	|
|2	|C(52-5,2)-C(52-5-4,2)	|C(47,2)-C(12,2)	|[('R.0', 1081, u'C(52-5,2)', u'C(47,2)')]	|
|3	|C(52-5,2)-C(52-5-4,2)	|C(47,2)-C(4,2)	|[('R.0', 1081, u'C(52-5,2)', u'C(47,2)')]	|
|4	|C(52-5,2)-C(52-5-4,2)	|47!/(2!(47-2)!) - 12	|[('R.0', 1081, u'C(52-5,2)', u'47!/(2!(47-2)!)')]	|
|5	|C(52-5,2)-C(52-5-4,2)	|C(47,2) - C(45, 2)	|[('R.0', 1081, u'C(52-5,2)', u'C(47,2)')]	|
|6	|C(52-5,2)-C(52-5-4,2)	|C(47,2) - C(46, 2)	|[('R.0', 1081, u'C(52-5,2)', u'C(47,2)')]	|
|7	|C(52-5,2)-C(52-5-4,2)	|C(47,2)-C(42,2)	|[('R.0', 1081, u'C(52-5,2)', u'C(47,2)')]	|
|8	|C(52-5,2)-C(52-5-4,2)	|C(47,2)*46	|[('R.0', 1081, u'C(52-5,2)', u'C(47,2)')]	|
|9	|C(52-5,2)-C(52-5-4,2)	|C(47,2)-C(42,1)	|[('R.0', 1081, u'C(52-5,2)', u'C(47,2)')]	|
|10	|C(52-5,2)-C(52-5-4,2)	|C(47,2)-C(4,1)	|[('R.0', 1081, u'C(52-5,2)', u'C(47,2)')]	|
|11	|C(52-5,2)-C(52-5-4,2)	|C(47,2)-43	|[('R.0', 1081, u'C(52-5,2)', u'C(47,2)')]	|
|12	|C(52-5,2)-C(52-5-4,2)	|C(47,2)-4	|[('R.0', 1081, u'C(52-5,2)', u'C(47,2)')]	|
|13	|C(52-5,2)-C(52-5-4,2)	|C(47,2)-C(46,2)	|[('R.0', 1081, u'C(52-5,2)', u'C(47,2)')]	|
|14	|C(52-5,2)-C(52-5-4,2)	|C(47,2)-8	|[('R.0', 1081, u'C(52-5,2)', u'C(47,2)')]	|
|15	|C(52-5,2)-C(52-5-4,2)	|C(47,2)-16	|[('R.0', 1081, u'C(52-5,2)', u'C(47,2)')]	|
|16	|C(52-5,2)-C(52-5-4,2)	|C(47,2)-(47-8)	|[('R.0', 1081, u'C(52-5,2)', u'C(47,2)')]	|
|17	|C(52-5,2)-C(52-5-4,2)	|C(47,2)-(46-8)	|[('R.0', 1081, u'C(52-5,2)', u'C(47,2)')]	|
|18	|C(52-5,2)-C(52-5-4,2)	|C(47,2)-(8)	|[('R.0', 1081, u'C(52-5,2)', u'C(47,2)')]	|
|19	|C(52-5,2)-C(52-5-4,2)	|C(47,2)-(64)	|[('R.0', 1081, u'C(52-5,2)', u'C(47,2)')]	|
|20	|C(52-5,2)-C(52-5-4,2)	|C(47,2)-C(39,2)	|[('R.0', 1081, u'C(52-5,2)', u'C(47,2)')]	|
|21	|C(52-5,2)-C(52-5-4,2)	|C(47,2)-C(45,2)	|[('R.0', 1081, u'C(52-5,2)', u'C(47,2)')]	|
|22	|C(52-5,2)-C(52-5-4,2)	|C(47,2)-(44)	|[('R.0', 1081, u'C(52-5,2)', u'C(47,2)')]	|
|23	|C(52-5,2)-C(52-5-4,2)	|C(47,2)-(43)	|[('R.0', 1081, u'C(52-5,2)', u'C(47,2)')]	|
|24	|C(52-5,2)-C(52-5-4,2)	|C(47,2)- (4*46)	|[('R.0', 1081, u'C(52-5,2)', u'C(47,2)')]	|
|25	|C(52-5,2)-C(52-5-4,2)	|C(52-5,2) - (52-5-4)	|[('R.0', 1081, u'C(52-5,2)', u'C(52-5,2)')]	|
|26	|C(52-5,2)-C(52-5-4,2)	|C(47,2)-C(47,46)	|[('R.0', 1081, u'C(52-5,2)', u'C(47,2)')]	|
|27	|C(52-5,2)-C(52-5-4,2)	|(C(47,2)*(52-6))	|[('R.0', 1081, u'C(52-5,2)', u'C(47,2)')]	|
|28	|C(52-5,2)-C(52-5-4,2)	|(C(47,2)-(52-6))	|[('R.0', 1081, u'C(52-5,2)', u'C(47,2)')]	|
|29	|C(52-5,2)-C(52-5-4,2)	|C(47,2)*(52-6)	|[('R.0', 1081, u'C(52-5,2)', u'C(47,2)')]	|
|30	|C(52-5,2)-C(52-5-4,2)	|C(47,2)-(52-6)	|[('R.0', 1081, u'C(52-5,2)', u'C(47,2)')]	|
|31	|C(52-5,2)-C(52-5-4,2)	|C(47,2) - C(46,2)	|[('R.0', 1081, u'C(52-5,2)', u'C(47,2)')]	|
|32	|C(52-5,2)-C(52-5-4,2)	|(47!/[2!45!]) - (46!/[2!44!])	|[('R.0', 1081, u'C(52-5,2)', u'47!/[2!45!]')]	|
|33	|C(52-5,2)-C(52-5-4,2)	|47!/[2!45!] - 12	|[('R.0', 1081, u'C(52-5,2)', u'47!/[2!45!]')]	|
|34	|C(52-5,2)-C(52-5-4,2)	|47!/[2!45!] - 4	|[('R.0', 1081, u'C(52-5,2)', u'47!/[2!45!]')]	|
|35	|C(52-5,2)-C(52-5-4,2)	|47!/[2!45!] - 7	|[('R.0', 1081, u'C(52-5,2)', u'47!/[2!45!]')]	|
|36	|C(52-5,2)-C(52-5-4,2)	|47!/[2!45!] - 8	|[('R.0', 1081, u'C(52-5,2)', u'47!/[2!45!]')]	|
|37	|C(52-5,2)-C(52-5-4,2)	|47!/[2!45!] - [13*4]	|[('R.0', 1081, u'C(52-5,2)', u'47!/[2!45!]')]	|
|38	|C(52-5,2)-C(52-5-4,2)	|47!/[2!45!] - 47!/[1!46!]	|[('R.0', 1081, u'C(52-5,2)', u'47!/[2!45!]')]	|
|39	|C(52-5,2)-C(52-5-4,2)	|47!/[2!45!]-[45!/[2!43!]]	|[('R.0', 1081, u'C(52-5,2)', u'47!/[2!45!]')]	|
|40	|C(52-5,2)-C(52-5-4,2)	|47!/[2!45!]-43	|[('R.0', 1081, u'C(52-5,2)', u'47!/[2!45!]')]	|
|41	|C(52-5,2)-C(52-5-4,2)	|C(47,2)-11*11	|[('R.0', 1081, u'C(52-5,2)', u'C(47,2)')]	|
|42	|C(52-5,2)-C(52-5-4,2)	|C(47,2) - 48	|[('R.0', 1081, u'C(52-5,2)', u'C(47,2)')]	|
|43	|C(52-5,2)-C(52-5-4,2)	|C(47,2) - 43	|[('R.0', 1081, u'C(52-5,2)', u'C(47,2)')]	|
|44	|C(52-5,2)-C(52-5-4,2)	|C(47, 2)*C(4, 2)	|[('R.0', 1081, u'C(52-5,2)', u'C(47, 2)')]	|
|45	|C(52-5,2)-C(52-5-4,2)	|47*46/2-12/2	|[('R.0', 1081, u'C(52-5,2)', u'47*46/2')]	|
|46	|C(52-5,2)-C(52-5-4,2)	|1081-741	|[('R.0', 1081, u'C(52-5,2)', u'1081')]	|
|47	|C(52-5,2)-C(52-5-4,2)	|C(47,2)C(4,2)	|[('R.0', 1081, u'C(52-5,2)', u'C(47,2)')]	|
|48	|C(52-5,2)-C(52-5-4,2)	|C(52-5,2)-1024	|[('R.0', 1081, u'C(52-5,2)', u'C(52-5,2)')]	|
|49	|C(52-5,2)-C(52-5-4,2)	|C(47,2)-C(44,2)	|[('R.0', 1081, u'C(52-5,2)', u'C(47,2)')]	|
|50	|C(52-5,2)-C(52-5-4,2)	|C(52-5, 2) - C(52-5-12, 2)	|[('R.0', 1081, u'C(52-5,2)', u'C(52-5, 2)')]	|




### (40) Mistake Group Wrong_Sign of size 40




### (28) Mistake Group ['R.1.1'] of size 28
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(52-5,2)-C(52-5-4,2)	|C(4,1)+C(4,2)	|[('R.1.1', 2.0, u'2', u'2')]	|
|1	|C(52-5,2)-C(52-5-4,2)	|C(4,1)C(47,2)	|[('R.1.1', 2.0, u'2', u'2')]	|
|2	|C(52-5,2)-C(52-5-4,2)	|C(4,1)*C(4,2)	|[('R.1.1', 2.0, u'2', u'2')]	|
|3	|C(52-5,2)-C(52-5-4,2)	|4*3*C(46,2)	|[('R.1.1', 2.0, u'2', u'2')]	|
|4	|C(52-5,2)-C(52-5-4,2)	|12*C(47,2)	|[('R.1.1', 2.0, u'2', u'2')]	|
|5	|C(52-5,2)-C(52-5-4,2)	|47-C(4,2)	|[('R.1.1', 2.0, u'2', u'2')]	|
|6	|C(52-5,2)-C(52-5-4,2)	|4*3+4*47*2	|[('R.1.1', 2.0, u'2', u'2')]	|
|7	|C(52-5,2)-C(52-5-4,2)	|4*3+4*46*2	|[('R.1.1', 2.0, u'2', u'2')]	|
|8	|C(52-5,2)-C(52-5-4,2)	|C(4,1)*C(52-6,1) + C(4,2)	|[('R.1.1', 2.0, u'2', u'2')]	|
|9	|C(52-5,2)-C(52-5-4,2)	|C(4,1)*C(52-5,1) + C(4,2)	|[('R.1.1', 2.0, u'2', u'2')]	|
|10	|C(52-5,2)-C(52-5-4,2)	|C(4,1)*C(52-6,1) + C(52-5,1)*C(4,1) +C(4,2)	|[('R.1.1', 2.0, u'2', u'2')]	|
|11	|C(52-5,2)-C(52-5-4,2)	|P(4,1)*P(52-6,1) + P(52-5,1)*P(4,1) +P(4,2)	|[('R.1.1', 2.0, u'2', u'2')]	|
|12	|C(52-5,2)-C(52-5-4,2)	|46*C(4,2)	|[('R.1.1', 2.0, u'2', u'2')]	|
|13	|C(52-5,2)-C(52-5-4,2)	|4 * 45 * C(7,2)	|[('R.1.1', 2.0, u'2', u'2')]	|
|14	|C(52-5,2)-C(52-5-4,2)	|12 + 4*43*2	|[('R.1.1', 2.0, u'2', u'2')]	|
|15	|C(52-5,2)-C(52-5-4,2)	|47*C(4,2)	|[('R.1.1', 2.0, u'2', u'2')]	|
|16	|C(52-5,2)-C(52-5-4,2)	|C(4,2)*47*C(47,2)	|[('R.1.1', 2.0, u'2', u'2')]	|
|17	|C(52-5,2)-C(52-5-4,2)	|C(4,1)*C(47,2)	|[('R.1.1', 2.0, u'2', u'2')]	|
|18	|C(52-5,2)-C(52-5-4,2)	|4*46+4*46 - C(4,2)	|[('R.1.1', 2.0, u'2', u'2')]	|
|19	|C(52-5,2)-C(52-5-4,2)	|4 * C(47,2)	|[('R.1.1', 2.0, u'2', u'2')]	|
|20	|C(52-5,2)-C(52-5-4,2)	|C(47,3)-C(47,2)	|[('R.1.1', 2.0, u'2', u'2')]	|
|21	|C(52-5,2)-C(52-5-4,2)	|C(47,4)-C(47,2)	|[('R.1.1', 2.0, u'2', u'2')]	|
|22	|C(52-5,2)-C(52-5-4,2)	|C(4,1)*C(52,2)	|[('R.1.1', 2.0, u'2', u'2')]	|
|23	|C(52-5,2)-C(52-5-4,2)	|47*46-12/2	|[('R.1.1', 2.0, u'2', u'2')]	|
|24	|C(52-5,2)-C(52-5-4,2)	|4*(52-1-5)- C(3,2)	|[('R.1.1', 2.0, u'2', u'2')]	|
|25	|C(52-5,2)-C(52-5-4,2)	|C(52,5) - C(48,2)	|[('R.1.1', 2.0, u'2', u'2')]	|
|26	|C(52-5,2)-C(52-5-4,2)	|C(52,5) - C(49,2) + C(48,2)	|[('R.1.1', 2.0, u'2', u'2')]	|




### (21) Mistake Group Fraction of size 21




### (7) Mistake Group ['R.1.0'] of size 7
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(52-5,2)-C(52-5-4,2)	|47*46-43*42	|[('R.1.0', 43.0, u'52-5-4', u'43')]	|
|1	|C(52-5,2)-C(52-5-4,2)	|4*46+43*4	|[('R.1.0', 43.0, u'52-5-4', u'43')]	|
|2	|C(52-5,2)-C(52-5-4,2)	|C(52,7)-C(43,5)	|[('R.1.0', 43.0, u'52-5-4', u'43')]	|
|3	|C(52-5,2)-C(52-5-4,2)	|47*46 - 43*42	|[('R.1.0', 43.0, u'52-5-4', u'43')]	|
|4	|C(52-5,2)-C(52-5-4,2)	|4*C(46,1)+C(43,1)*4	|[('R.1.0', 43.0, u'52-5-4', u'C(43,1)')]	|




### (5) Mistake Group ['R.1.0.0'] of size 5
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(52-5,2)-C(52-5-4,2)	|C(4,1)C(52-5-1,1)	|[('R.1.0.0', 47.0, u'52-5', u'52-5')]	|
|1	|C(52-5,2)-C(52-5-4,2)	|4*C(52-5-1,1)	|[('R.1.0.0', 47.0, u'52-5', u'52-5')]	|
|2	|C(52-5,2)-C(52-5-4,2)	|4*C(52-5-4,1)	|[('R.1.0.0', 47.0, u'52-5', u'52-5')]	|
|3	|C(52-5,2)-C(52-5-4,2)	|4[C(47,2) - C(46,2)]	|[('R.1.0.0', 47.0, u'52-5', u'47')]	|
|4	|C(52-5,2)-C(52-5-4,2)	|(C(4,1) * (52 - 6)) - C(47 - 4,1)	|[('R.1.0.0', 47.0, u'52-5', u'47')]	|




### (2) Mistake Group ['R.1'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(52-5,2)-C(52-5-4,2)	|C(4,2)*C(43,2)	|[('R.1', 903, u'C(52-5-4,2)', u'C(43,2)')]	|
|1	|C(52-5,2)-C(52-5-4,2)	|C(45,2)-C(43,2)	|[('R.1', 903, u'C(52-5-4,2)', u'C(43,2)')]	|




### (2) Mistake Group ['R.1.0.0.0'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.0.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(52-5,2)-C(52-5-4,2)	|4C(52-4-5,1)	|[('R.1.0.0.0', 52.0, u'52', u'52')]	|
|1	|C(52-5,2)-C(52-5-4,2)	|C(4,1)(C(52-6-3,1))	|[('R.1.0.0.0', 52.0, u'52', u'52')]	|




### (2) Mistake Group ['R.1.0.1'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(52-5,2)-C(52-5-4,2)	|C(52 - 5,1) * C(47 - 4,1)	|[('R.1.0.1', 4.0, u'4', u'4')]	|
|1	|C(52-5,2)-C(52-5-4,2)	|C(52 - 5,1) + C(47 - 4,1)	|[('R.1.0.1', 4.0, u'4', u'4')]	|




### (1) Mistake Group ['R.1.0.0.0', 'R.1.0.0.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.0.0.0', 'R.1.0.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(52-5,2)-C(52-5-4,2)	|C(4,1) * (C(52 - 5,1) - C(47 - 4,1))	|[('R.1.0.0.0', 52.0, u'52', u'52'), ('R.1.0.0.1', 5.0, u'5', u'5')]	|




### (1) Mistake Group ['R.0', 'R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(52-5,2)-C(52-5-4,2)	|C(52-5,2)C(52-5-4,2)	|[('R.0', 1081, u'C(52-5,2)', u'C(52-5,2)'), ('R.1', 903, u'C(52-5-4,2)', u'C(52-5-4,2)')]	|




### (1) Mistake Group ['R.0', 'R.1.0.1', 'R.1.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1.0.1', 'R.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(52-5,2)-C(52-5-4,2)	|47!/[2!45!] - [13*4*2]	|[('R.0', 1081, u'C(52-5,2)', u'47!/[2!45!]'), ('R.1.0.1', 4.0, u'4', u'4'), ('R.1.1', 2.0, u'2', u'2')]	|




### (128) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:gthorn

	first_attempt
					2015-10-21 00:49:24
	part2_incorrect_attempt
					('0:04:30', u'16 * 13 - 5')
					('0:04:35', u'16 * 13 - 6')
	part2_correct_attempt
					['0:36:58', u'C(47,2) - C(43, 2)']

1 Student ID:phodgson

	first_attempt
					2015-10-21 05:39:09
	part2_incorrect_attempt
					('0:00:00', u'4*(52-6)')
					('0:00:06', u'4*(52-5)')
	part2_correct_attempt
					['0:01:43', u'C(47,2) - C(47-4,2)']

2 Student ID:v4zhang

	first_attempt
					2015-10-22 09:58:19
	part2_incorrect_attempt
					('0:00:00', u'C(4, 2)')
					('0:00:08', u'C(4, 1)*C(3, 1)')
					('0:01:13', u'C(4, 1)*C(46, 1)')
					('0:01:19', u'C(4, 1)*C(45, 1)')
					('0:01:54', u'C(4, 2)')
					('0:07:06', u'C(4, 2)*C(46, 1)')
					('0:07:11', u'C(4, 1)*C(46, 1)')
					('0:07:27', u'C(4, 1)*C(3, 1)')
	part2_correct_attempt
					['0:10:07', u'C(47,2)-C(43, 2)']

3 Student ID:kbielawi

	first_attempt
					2015-10-22 17:18:25
	part2_incorrect_attempt
					('-1 day, 23:56:50', u'4*4^5')
	part2_correct_attempt
					['0:00:00', u'C(52-5,2)-C(52-5-4,2)']

4 Student ID:jguanzho

	first_attempt
					2015-10-21 05:30:45
	part2_incorrect_attempt
					('-2 days, 17:11:28', u'4*51*50*49*48*47*46')
					('-2 days, 17:12:17', u'4*51*50*49*48*47*46/2!')
					('-2 days, 17:13:59', u'(4!/5!)*(51!/(6!*44!))')
					('-1 day, 23:06:39', u'47!/(4!*43!)')
					('0:00:21', u'4**2')
					('0:00:45', u'4*3')
	part2_correct_attempt
					['0:01:57', u'C(47,2)-C(43,2)']

5 Student ID:alakamsa

	first_attempt
					2015-10-17 23:51:15
	part2_incorrect_attempt
					('0:00:00', u'4*46')
	part2_correct_attempt
					['0:02:08', u'4*C(43,1) + C(4,2)']

6 Student ID:dcgriffi

	first_attempt
					2015-10-21 03:41:56
	part2_incorrect_attempt
					('0:08:01', u'47*46-16')
					('0:09:36', u'C(47,2)')
					('0:10:34', u'4*47')
					('0:11:12', u'4*47+4*46')
					('0:11:44', u'47+46')
					('0:12:45', u'47*46*4')
					('0:14:49', u'47*4 + 46*4')
					('0:18:52', u'4*46')
					('0:19:45', u'47*4+16')
					('0:19:59', u'43*4+16')
					('0:25:11', u'4 + (4*8) + (3*5)')
					('0:29:04', u'4*46 + 4*46 - 3')
					('0:29:29', u'12 + 4*43')
					('0:38:30', u'47*4')
					('0:39:14', u'46*4')
					('0:41:47', u'46*C(4,1)')
					('0:42:21', u'47*C(4,1)')
					('0:48:36', u'(47-1)*4')
					('0:48:59', u'46*4')
					('0:50:36', u'46*4*2')
					('0:50:45', u'46*4/2')
	part2_correct_attempt
					['0:52:16', u'C(47,2) - C(43,2)']

7 Student ID:jjm019

	first_attempt
					2015-10-22 10:30:15
	part2_incorrect_attempt
					('-1 day, 12:49:22', u'C(43,2)')
					('-1 day, 22:09:42', u'4^8')
					('-1 day, 22:11:12', u'4(46)')
					('-1 day, 22:19:50', u'4*46')
	part2_correct_attempt
					['-1 day, 23:59:43', u'C(52-5,2)-C(52-5-4,2)']

8 Student ID:mhale

	first_attempt
					2015-10-21 07:07:23
	part2_incorrect_attempt
					('0:00:29', u'4 * 46')
					('0:01:30', u'4 * 3')
					('0:02:05', u'4 * 47')
	part2_correct_attempt
					['0:08:34', u'C(47, 2) - C(43, 2)']

9 Student ID:ctgraves

	first_attempt
					2015-10-21 23:46:22
	part2_incorrect_attempt
					('-1 day, 23:55:56', u'4*(52-6)')

10 Student ID:dkurli

	first_attempt
					2015-10-21 04:06:48
	part2_incorrect_attempt
					('0:00:41', u'C(4,1)*46')
					('0:00:56', u'C(4,1)*46*2')
					('0:01:07', u'C(4,1)*46+C(4,1)*47')
					('0:03:19', u'4*46')
					('0:03:23', u'4*46*2')
					('0:04:20', u'C(4,1)*47')
					('0:04:28', u'C(4,1)*46')
					('0:04:33', u'C(4,1)*46*2')
	part2_correct_attempt
					['0:08:05', u'C(47,2)-C(43,2)']

11 Student ID:nhn018

	first_attempt
					2015-10-22 20:21:18
	part2_incorrect_attempt
					('-1 day, 23:55:14', u'4*4^5')
	part2_correct_attempt
					['0:00:00', u'C(47,2)-C(52-5-4,2)']

12 Student ID:dan029

	first_attempt
					2015-10-22 00:40:33
	part2_incorrect_attempt
					('0:01:06', u'4*46')
					('0:01:20', u'4*3')
					('0:02:03', u'C(4,1)*C(47,1)')
					('0:02:13', u'C(4,1)*C(46,1)')
	part2_correct_attempt
					['0:05:01', u'C(47,2) - C(43,2)']

13 Student ID:jyc018

	first_attempt
					2015-10-22 23:16:45
	part2_incorrect_attempt
					('0:01:05', u'4*(52-7)')
					('0:01:43', u'4*(52-5)')
					('0:02:06', u'4*(52-1-5)')
	part2_correct_attempt
					['0:07:07', u'184-6']

14 Student ID:vqt004

	first_attempt
					2015-10-22 13:24:55
	part2_incorrect_attempt
					('0:02:11', u'4*(52-9)')
	part2_correct_attempt
					['0:05:20', u'178']

15 Student ID:r9jiang

	first_attempt
					2015-10-18 22:25:16
	part2_incorrect_attempt
					('0:01:17', u'4*46')
	part2_correct_attempt
					['0:33:56', u'178']

16 Student ID:rlhagen

	first_attempt
					2015-10-18 19:19:42
	part2_incorrect_attempt
					('-1 day, 23:39:48', u'43!/(2!(43-2)!)')
	part2_correct_attempt
					['-1 day, 23:51:09', u'(47!/(2!(47-2)!))-(43!/(2!(43-2)!))']

17 Student ID:avasavad

	first_attempt
					2015-10-22 19:55:10
	part2_incorrect_attempt
					('0:00:33', u'C(4,2)')
					('0:01:25', u'4 * 46')
	part2_correct_attempt
					['0:02:51', u'C(47,2) - C(43,2)']

18 Student ID:btn023

	first_attempt
					2015-10-21 17:38:47
	part2_incorrect_attempt
					('0:01:09', u'4*2')
					('0:02:22', u'4*3')
	part2_correct_attempt
					['0:10:19', u'1081 - 903']

19 Student ID:dgunawan

	first_attempt
					2015-10-23 00:30:37
	part2_incorrect_attempt
					('0:00:18', u'C(4, 1)')
	part2_correct_attempt
					['0:09:56', u'C(52-5, 2) - C(52-5-4, 2)']

20 Student ID:tcuddy

	first_attempt
					2015-10-17 21:38:04
	part2_incorrect_attempt
					('0:02:53', u'4*46')
	part2_correct_attempt
					['0:29:00', u'47!/(2!45!)-(43!/(2!41!))']

21 Student ID:l8ngo

	first_attempt
					2015-10-22 04:10:20
	part2_incorrect_attempt
					('0:00:20', u'4*4')
					('0:00:45', u'4+4')
					('0:06:51', u'4*3')
					('0:07:01', u'4+3')
					('0:20:43', u'1+ 46')
					('0:21:32', u'[1+ 46] * 2')
					('0:22:25', u'12+ 4*46')
					('0:22:41', u'[12+ 4*46]*2')
	part2_correct_attempt
					['0:28:20', u'47!/[2!45!]-43!/[2!41!]']

22 Student ID:dando

	first_attempt
					2015-10-23 00:20:50
	part2_incorrect_attempt
					('-1 day, 23:49:17', u'C(4,1) * C(4,1)')
	part2_correct_attempt
					['0:03:33', u'C(47,2) - C(43,2)']

23 Student ID:dsriniva

	first_attempt
					2015-10-22 17:56:16
	part2_incorrect_attempt
					('0:00:27', u'4*46*2')
					('0:00:33', u'4*46')
					('0:02:43', u'4*46')
					('0:04:15', u'C(16,2)')
	part2_correct_attempt
					['0:06:27', u'C(47,2)-C(43,2)']

24 Student ID:chc286

	first_attempt
					2015-10-21 09:48:00
	part2_incorrect_attempt
					('0:01:01', u'4*48')
					('0:01:43', u'4*46')
					('0:08:03', u'4*43')
					('0:10:33', u'C(46,2)-C(38,2)')
	part2_correct_attempt
					['0:16:20', u'C(47,2)-C(43,2)']

25 Student ID:glcohen

	first_attempt
					2015-10-20 15:20:38
	part2_incorrect_attempt
					('0:01:21', u'C(4,2)')
					('0:02:52', u'C(4,2)*(C(4,1)C(4,1))')
					('0:04:40', u'C(4,1)C(46,1)')
					('0:06:29', u'C(4,1)C(46,1)+1')
					('0:06:37', u'C(4,1)C(46,1)+3')
	part2_correct_attempt
					['0:08:04', u'C(47,2)-C(43,2)']

26 Student ID:sayao

	first_attempt
					2015-10-21 19:17:59
	part2_incorrect_attempt
					('0:00:42', u'4*13')
					('0:01:20', u'4*13*4')
					('0:02:56', u'4*7*4*5*3')
					('0:03:27', u'C(4,1)+C(28+15,1)')
					('0:03:52', u'C(4,1)*C(28+15,1)')
					('0:04:25', u'43*4')
					('0:08:01', u'4*(28+15)')
					('0:10:55', u'C(4,1)*(28+15)')
	part2_correct_attempt
					['2:28:27', u'C(52-5,2)-C(52-5-4,2)']

27 Student ID:csl030

	first_attempt
					2015-10-22 04:04:09
	part2_incorrect_attempt
					('0:00:10', u'4 * 3')
					('0:01:02', u'4 * C(46, 1)')
					('0:01:48', u'4 * 46 * 2')
					('0:03:17', u'4 * 46 - 1')
					('0:03:24', u'4 * 46 - 2')
					('0:04:38', u'4 * (46) - 4')
	part2_correct_attempt
					['0:06:52', u'C(47,2) - C(43,2)']

28 Student ID:ssamudra

	first_attempt
					2015-10-23 00:55:29
	part2_incorrect_attempt
					('0:00:00', u'C(52,5) - C(49,3)')

29 Student ID:c1wei

	first_attempt
					2015-10-21 22:49:07
	part2_incorrect_attempt
					('-1 day, 23:56:19', u'2162-47-46')
	part2_correct_attempt
					['0:00:57', u'1081-903']

30 Student ID:arc013

	first_attempt
					2015-10-21 10:22:18
	part2_incorrect_attempt
					('0:00:36', u'4*C(46,1)')
	part2_correct_attempt
					['0:01:22', u'C(47,2)-C(43,2)']

31 Student ID:mitopete

	first_attempt
					2015-10-21 03:05:21
	part2_incorrect_attempt
					('-1 day, 22:46:37', u'C(4,1)*(52-6)')
					('-1 day, 22:50:22', u'C(4,1)*(52)')
	part2_correct_attempt
					['-1 day, 22:56:27', u'C(47,2)']

32 Student ID:yos017

	first_attempt
					2015-10-21 08:21:16
	part2_incorrect_attempt
					('0:09:14', u'C(4,1)*47')
					('0:10:17', u'C(4,1)*52')
					('0:10:32', u'52 ')
					('0:10:50', u'C(52,5) ')
	part2_correct_attempt
					['0:21:03', u'C(47,2)-C(43,2)']

33 Student ID:habuamar

	first_attempt
					2015-10-16 19:59:39
	part2_incorrect_attempt
					('0:01:25', u'C(4,2)+C(4,1)*C(12,1)')
	part2_correct_attempt
					['0:03:01', u'C(4,2)+C(4,1)*C(43,1)']

34 Student ID:m8woo

	first_attempt
					2015-10-22 21:21:26
	part2_incorrect_attempt
					('0:00:38', u'C(4,1)*C(46,1)')
					('0:04:25', u'4*46/2')
					('0:04:33', u'4*46')
	part2_correct_attempt
					['0:06:11', u'C(47,2)-C(43,2)']

35 Student ID:akg009

	first_attempt
					2015-10-22 23:54:21
	part2_incorrect_attempt
					('0:01:02', u'4*46')
					('0:01:12', u'4*47')
					('0:04:18', u'(52-5)')
					('0:18:31', u'C(43,1)*4*2')
	part2_correct_attempt
					['0:20:46', u'C(47,2)-C(43,2)']

36 Student ID:h4tu

	first_attempt
					2015-10-22 16:45:09
	part2_incorrect_attempt
					('0:01:46', u'4*46')
					('0:02:15', u'4*46+47*3')
					('0:02:41', u'4*46+47*4')
	part2_correct_attempt
					['0:05:58', u'C(47,2)-C(43,2)']

37 Student ID:lrlai

	first_attempt
					2015-10-22 03:23:24
	part2_incorrect_attempt
					('0:06:01', u'4*4 + 4*4')
	part2_correct_attempt
					['0:36:58', u'C(52-5,2) - C(52-5-4, 2)']

38 Student ID:lguintu

	first_attempt
					2015-10-16 06:55:38
	part2_incorrect_attempt
					('0:05:25', u'C(4,2)')
					('0:05:31', u'C(4,1)')
	part2_correct_attempt
					['0:07:18', u'C(47,2) - C(43,2)']

39 Student ID:c1sorian

	first_attempt
					2015-10-21 21:38:04
	part2_incorrect_attempt
					('0:00:50', u'C(4,1)*46')
					('0:01:22', u'C(4,2)')
					('0:03:17', u'C(4,1)*2*46')
	part2_correct_attempt
					['0:04:09', u'C(47,2)-C(43,2)']

40 Student ID:abjara

	first_attempt
					2015-10-21 18:45:35
	part2_incorrect_attempt
					('0:03:28', u'C(4,1)*C(46,1)')
	part2_correct_attempt
					['3:21:48', u'C(47,2) - C(43,2)']

41 Student ID:asp025

	first_attempt
					2015-10-21 19:03:49
	part2_incorrect_attempt
					('0:03:35', u'C(47,1)')
					('0:05:20', u'C(47,4)')
	part2_correct_attempt
					['0:08:46', u'C(47,2)-C(43,2)']

42 Student ID:krau

	first_attempt
					2015-10-21 04:07:04
	part2_incorrect_attempt
					('0:02:58', u'C(4,1) * 2')
					('0:03:31', u'4*4')
					('0:04:47', u'43*4')
					('0:04:54', u'43*4 *2')
					('0:05:33', u'4*2*46')
	part2_correct_attempt
					['0:08:00', u'C(47,2)-C(43,2)']

43 Student ID:kthui

	first_attempt
					2015-10-18 08:33:27
	part2_incorrect_attempt
					('0:00:00', u'4*4')
					('0:08:50', u'4+4')
					('0:09:12', u'4*3')
					('0:09:22', u'4*3*2')
					('0:11:22', u'4*3+4*46+47*4')
					('0:11:28', u'4*3+4*46')
					('0:11:33', u'4*3+4*47')
					('0:14:32', u'4*3+4*46+47*4')
					('0:19:42', u'4+4*46/3+4*47/3')
					('0:27:06', u'4*46')
					('0:27:12', u'4*47')
					('0:27:20', u'4*46*2')
					('0:27:25', u'4*47*2')
					('0:30:36', u'47!/((47-4)!4!)')
	part2_correct_attempt
					['0:40:18', u'47!/((47-2)!2!)-43!/((43-2)!2!)']

44 Student ID:beyounge

	first_attempt
					2015-10-17 06:05:22
	part2_incorrect_attempt
					('0:01:11', u'C(4,1) * C(46,1)')
					('0:02:15', u'C(4,1) * C(42,1)')
					('0:04:14', u'C(4,1) * C(46,1)')
					('0:08:34', u'C(4,2)')
					('0:09:19', u'C(4,1) * C(3,1)')
					('0:09:44', u'C(4,1) * C(4,1)')
					('0:09:56', u'C(4,1)')
					('0:11:48', u'C(4,2)')
	part2_correct_attempt
					['0:13:51', u'C(47,2) - C(43,2)']

45 Student ID:jic212

	first_attempt
					2015-10-22 22:52:29
	part2_incorrect_attempt
					('0:00:32', u'4*46')
					('0:01:01', u'4*3')
					('0:04:06', u'2*4*46')
					('0:04:21', u'4*46')
	part2_correct_attempt
					['0:08:44', u'C(47,2)-C(43,2)']

46 Student ID:tpmach

	first_attempt
					2015-10-22 03:00:05
	part2_incorrect_attempt
					('-1 day, 19:47:52', u'C(52-5,4)')
					('-1 day, 19:49:25', u'C(52-5,2)')
	part2_correct_attempt
					['0:01:15', u'C(47,2)-C(43,2)']

47 Student ID:c2qiu

	first_attempt
					2015-10-22 16:13:03
	part2_incorrect_attempt
					('0:00:00', u'C(2,1)*C(47,4)')
	part2_correct_attempt
					['1:54:50', u'C(52-5,2)-C(52-5-4,2)']

48 Student ID:rraiyyan

	first_attempt
					2015-10-22 20:15:25
	part2_incorrect_attempt
					('0:01:57', u'46*4')
					('3:09:43', u'C(4,2)')
					('3:23:03', u'C(45,2)-C(41,2)')
	part2_correct_attempt
					['3:23:14', u'C(47,2)-C(43,2)']

49 Student ID:t1tran

	first_attempt
					2015-10-18 04:05:59
	part2_incorrect_attempt
					('-1 day, 23:44:23', u'C(4,1)+5+C(46,1)')
	part2_correct_attempt
					['-1 day, 23:54:33', u'C(47,2)-C(47-4,2)']

50 Student ID:jel075

	first_attempt
					2015-10-21 22:21:39
	part2_incorrect_attempt
					('0:00:00', u'C(45,2)-C(41,2)')
	part2_correct_attempt
					['0:02:28', u'C(47,2)-C(43,2)']

51 Student ID:w4shin

	first_attempt
					2015-10-19 19:52:16
	part2_incorrect_attempt
					('-1 day, 23:38:32', u'C(52,5)*C(13,1)*C(4,1)*C(46,1)')
					('-1 day, 23:40:24', u'C(13,1)*C(4,1)*C(46,1)')
	part2_correct_attempt
					['0:00:00', u'4*C(43,1)+C(4,2)']

52 Student ID:bakang

	first_attempt
					2015-10-22 07:18:57
	part2_incorrect_attempt
					('0:00:40', u'4*46')
					('0:03:47', u'4*45')
					('0:05:22', u'4*46')
					('0:05:30', u'4*42')
					('0:08:03', u'4*46')
					('0:08:22', u'C(43,2)')
					('0:09:02', u'C(47,2)')
					('0:09:53', u'C(52-5-4,2)')
					('0:11:51', u'C(52-5-4,2)-12')
					('0:12:49', u'C(52-5-4,2)-12')
					('0:33:07', u'C(52-5-4,2)')
					('0:35:06', u'4*46')
					('0:35:49', u'4*43')
					('0:37:07', u'4*47')
					('0:38:56', u'46*4')
					('0:40:43', u'43*42')
					('0:41:04', u'C(52-5-4,2)')
	part2_correct_attempt
					['0:42:20', u'C(52-5,2)-C(52-5-4,2)']

53 Student ID:ggaddi

	first_attempt
					2015-10-20 01:07:37
	part2_incorrect_attempt
					('-1 day, 23:57:38', u'C(4,1) + C(52-6, 1)')
					('0:00:09', u'C(4,1)* C(52-6, 1)')
					('0:00:18', u'C(4,1)')
					('0:03:41', u'P(4,1)')
	part2_correct_attempt
					['0:04:55', u'C(52-5,2) - C(52-9,2)']

54 Student ID:jtfrankl

	first_attempt
					2015-10-21 02:37:56
	part2_incorrect_attempt
					('0:00:25', u'4*46')
					('0:01:03', u'6*46')
					('0:02:25', u'C(4,2)')
					('0:04:50', u'C(4,1)*45')
					('0:05:50', u'C(4,1)*46')
	part2_correct_attempt
					['0:07:05', u'C(47,2)-C(43,2)']

55 Student ID:cstringh

	first_attempt
					2015-10-22 01:38:15
	part2_incorrect_attempt
					('0:01:26', u'4 * 46')
					('0:01:40', u'4 * 45')
					('0:02:02', u'4 * 47')
					('0:03:08', u'C(47,2)')
					('0:04:40', u'47*4')
					('0:04:51', u'47*4 + 1')
					('0:05:26', u'4*3')
					('0:06:31', u'4*46')
					('0:08:14', u'4 * C(47,1)')
					('0:08:36', u'4 * C(46,1)')
					('0:09:20', u'4 + 47')
					('0:09:47', u'4 + 43')
					('0:09:54', u'4 * 43')
					('0:10:51', u'4 * 12')
					('0:11:43', u'4*13')
					('0:12:32', u'C(52, 47)')
					('0:12:43', u'C(52, 47) + 4')
					('0:12:58', u'52 + 47')
					('0:13:15', u'52 - 47')
	part2_correct_attempt
					['0:18:27', u'C(47,2) - C(43,2)']

56 Student ID:j5phung

	first_attempt
					2015-10-16 19:10:56
	part2_incorrect_attempt
					('-1 day, 22:58:59', u'4*47')
					('-1 day, 23:10:27', u'C(4,1)*C(47,2)*C(7,5)')
					('-1 day, 23:19:38', u'C(4,1)*C(47,2)*13')
					('-1 day, 23:21:12', u'C(4,1)*C(47,2)*2')
					('-1 day, 23:21:20', u'C(4,1)*C(47,2)*3')
					('0:00:09', u'C(4,1)')
					('0:00:38', u'C(4,1)*C(45,1)')
					('0:00:49', u'C(4,1)*C(46,1)')
					('0:02:04', u'C(4,2)')
					('0:04:23', u'C(4,1)*C(13,1)')
					('0:04:57', u'C(4,1)*C(47,1)')
					('0:05:06', u'C(4,1)*C(43,1)')
					('0:05:43', u'C(4,1)*C(3,1)')
					('0:06:01', u'C(4,2)')
					('0:06:11', u'C(4,1)^2')
					('0:07:00', u'C(4,1)*C(47,1)*C(3,1)*C(46,1)')
					('0:08:42', u'4*3*43*42')
					('0:10:09', u'C(4,2)')
					('0:10:23', u'4*3')
					('0:20:50', u'C(4,2)*C(45,2)')
					('0:20:57', u'C(4,2)*C(47,2)')
					('0:22:09', u'C(4,2)*C(45,2)')
					('0:24:10', u'C(4,1)*C(46,1)')
					('0:28:45', u'2*C(4,2)')
					('0:29:00', u'2*C(4,1)*64')
					('0:29:15', u'2*C(4,1)*46')
					('0:29:39', u'2(C(4,1)*46)+C(4,2)')
					('0:30:19', u'2(C(4,1)*43)+C(4,2)')
					('0:31:31', u'2*4*43+4*3')
					('0:31:45', u'2*4*43')
					('0:32:10', u'4*43')
					('0:32:20', u'4*46')
					('0:32:28', u'4*46*2')
					('0:32:35', u'4*46*2-1')
					('0:32:42', u'4*46*2-12')
					('0:43:35', u'2*C(4,2)')
					('4:37:20', u'2^13-C(4,2)')
					('4:38:18', u'47-12')
	part2_correct_attempt
					['4:43:40', u'C(47,2)-C(43,2)']

57 Student ID:rbdoming

	first_attempt
					2015-10-21 18:21:57
	part2_incorrect_attempt
					('0:00:41', u'46*4')
					('0:03:05', u'C(47,4)')
					('0:06:38', u'4*43')
					('0:07:46', u'47*46')
					('0:10:12', u'46*4')
	part2_correct_attempt
					['0:12:37', u'C(47,2)-C(43,2)']

58 Student ID:qfu

	first_attempt
					2015-10-16 03:06:10
	part2_incorrect_attempt
					('0:01:10', u'4*4*C(48,1)')
					('0:02:15', u'4*C(48,1)')
					('0:02:42', u'4*C(46,1)')
	part2_correct_attempt
					['0:04:48', u'C(47,2)-C(43,2)']

59 Student ID:dcastlem

	first_attempt
					2015-10-21 20:55:07
	part2_incorrect_attempt
					('0:02:31', u'(C(4,2)*(52-6))-16')
					('0:03:06', u'(C(4,2)*(52-6))')
					('0:09:59', u'C(47,3)-(52-6)')
					('0:10:33', u'C(47,1)-(52-6)')
					('0:10:40', u'C(47,5)-(52-6)')
					('0:16:26', u'C(4,1)*(52-6)-3')
					('0:23:52', u'52-16')
					('0:24:05', u'C(52,2)')
					('0:24:10', u'C(52,7)')
					('0:27:40', u'(C(4,1)*(52-6))-16')
	part2_correct_attempt
					['0:28:59', u'C(47,2)-C(43,2)']

60 Student ID:hsc052

	first_attempt
					2015-10-22 03:23:27
	part2_incorrect_attempt
					('1:17:48', u'4+4+4*3')
					('1:19:34', u'C(4,2)')
					('1:20:02', u'C(4,2)+4+4')
					('1:31:42', u'C(4,2)+C(4,1)')
					('1:37:48', u'C(47,4)')
	part2_correct_attempt
					['1:49:04', u'C(47,2)-C(43,2)']

61 Student ID:dac064

	first_attempt
					2015-10-22 20:51:27
	part2_incorrect_attempt
					('0:00:36', u'4 * (C(46,1))')
					('0:01:47', u'C(4,1)C(46,1)')
	part2_correct_attempt
					['0:05:19', u'C(47,2) - C(43,2) ']

62 Student ID:v3doan

	first_attempt
					2015-10-22 20:54:24
	part2_incorrect_attempt
					('0:00:24', u'4 * 46')
					('0:02:36', u'C(4,2) * 46')
	part2_correct_attempt
					['0:03:31', u'C(47,2) - C(43,2)']

63 Student ID:sghouse

	first_attempt
					2015-10-22 00:13:42
	part2_incorrect_attempt
					('0:00:30', u'4*46')
	part2_correct_attempt
					['0:05:52', u'C(47,2)-C(43,2)']

64 Student ID:haw081

	first_attempt
					2015-10-22 05:58:03
	part2_incorrect_attempt
					('-1 day, 22:15:29', u'C(4,1)C(52-6,1)(52-5)')
					('-1 day, 22:15:39', u'C(4,1)C(52-6,1)')
					('-1 day, 22:16:02', u'C(4,1)C(52-24,1)')
					('-1 day, 22:17:06', u'C(4,1)(52-5-4)')
					('-1 day, 22:17:16', u'C(4,1)(52-4)')
	part2_correct_attempt
					['-1 day, 23:58:25', u'C(47,2)-C(47-4,2)']

65 Student ID:b3hwang

	first_attempt
					2015-10-21 02:20:34
	part2_incorrect_attempt
					('0:00:14', u'4*4')
					('0:04:03', u'4*(52-6)')
					('0:05:26', u'8*(52-6)')
					('0:06:42', u'(4*46)')
					('0:08:02', u'3*8')
					('0:10:44', u'C(46,2)-C(42,2)')
	part2_correct_attempt
					['0:12:11', u'C(47,2)-C(43,2)']

66 Student ID:jix029

	first_attempt
					2015-10-20 21:13:06
	part2_incorrect_attempt
					('0:00:00', u'4*48')
	part2_correct_attempt
					['0:01:41', u'1081-903']

67 Student ID:kebao

	first_attempt
					2015-10-22 15:43:58
	part2_incorrect_attempt
					('-1 day, 23:55:06', u'(C(4,1)*(52-6))')
					('-1 day, 23:55:28', u'(C(4,1)*(52-7))')
					('0:02:37', u'(C(4,1)*(52-7))-1')
	part2_correct_attempt
					['0:02:45', u'(C(4,1)*(52-7))-2']

68 Student ID:abasu

	first_attempt
					2015-10-20 23:39:42
	part2_incorrect_attempt
					('0:00:33', u'4*46')
					('0:06:12', u'C(46,2)')
	part2_correct_attempt
					['0:07:32', u'C(47,2) - C(43,2)']

69 Student ID:acvuong

	first_attempt
					2015-10-18 01:07:49
	part2_incorrect_attempt
					('0:00:00', u'4*46')
					('0:12:21', u'4*12')
					('0:13:45', u'8*46')
					('0:23:12', u'C(46,2) - C(44,2)')
					('0:23:34', u'C(46,1) - C(44,1)')
					('0:25:13', u'C(46,2) - C(42,2)')
	part2_correct_attempt
					['0:26:14', u'C(47,2) - C(43,2)']

70 Student ID:sachadal

	first_attempt
					2015-10-22 19:31:38
	part2_incorrect_attempt
					('-1 day, 23:54:57', u'4*C(46,1)*4')
					('0:02:38', u'4*43')
					('0:02:45', u'4*42')
	part2_correct_attempt
					['0:17:53', u'C(47,2) - C(43,2)']

71 Student ID:awollner

	first_attempt
					2015-10-21 17:53:11
	part2_incorrect_attempt
					('0:00:00', u'4*46')
	part2_correct_attempt
					['0:04:06', u'C(47,2)- C(43,2)']

72 Student ID:pvl001

	first_attempt
					2015-10-19 22:35:54
	part2_incorrect_attempt
					('0:00:12', u'4 * 3')
					('0:02:30', u'4 * 46')
					('0:05:10', u'4 * 45')
					('0:05:43', u'4 * 46 / 2')
					('0:06:05', u'4 * 46 * 2')
					('0:06:28', u'C(4,2)')
					('0:07:47', u'4 * 46 * 2 - 1')
					('0:08:53', u'(4 * 46)/2 - 1')
	part2_correct_attempt
					['0:10:33', u'C(47,2) - C(43,2)']

73 Student ID:jcj006

	first_attempt
					2015-10-21 22:58:29
	part2_incorrect_attempt
					('-1 day, 23:59:17', u'2*46')
					('0:00:34', u'4*46')
	part2_correct_attempt
					['0:01:30', u'4*46-6']

74 Student ID:dlt009

	first_attempt
					2015-10-22 06:53:48
	part2_incorrect_attempt
					('0:00:00', u'4*46')
	part2_correct_attempt
					['0:11:27', u'C(47,2)-C(43,2)']

75 Student ID:mbl003

	first_attempt
					2015-10-21 19:34:33
	part2_incorrect_attempt
					('0:00:58', u'C(4,1)*C(4,1)')
					('0:01:35', u'C(4,2)')
	part2_correct_attempt
					['0:02:30', u'C(52-5,2)-C(52-5-4,2)']

76 Student ID:ksmurlo

	first_attempt
					2015-10-21 00:00:07
	part2_incorrect_attempt
					('0:00:00', u'4*46')
					('0:00:59', u'4*46*2')
					('0:01:07', u'4*46/2')
					('0:04:41', u'C(46,2)-C(42,2)')
	part2_correct_attempt
					['0:04:57', u'C(47,2)-C(43,2)']

77 Student ID:ttimmons

	first_attempt
					2015-10-21 18:25:30
	part2_incorrect_attempt
					('0:01:47', u'C(52-6+4, 2)')
					('0:02:08', u'52-6+4')
					('0:02:26', u'(52-6)*4')
					('0:06:06', u'(C(4,1)*C(52-6,1))')
					('0:07:53', u'(C(4,1)*(52-6))')
					('0:10:29', u'C((C(4,1)*(52-6)),2)')
					('0:13:26', u'(C(4,1)*(52-6))-4')
					('0:13:33', u'(C(4,1)*(52-6))-3')
					('0:14:36', u'(52-6)*3')
					('0:15:00', u'C(52-6,2)*C(4,1)')
					('0:16:10', u'C(4,1)*(52-6)-((52-5)*C(3,1))')
					('0:18:36', u'(52-5)-3')
					('0:21:11', u'(52-5)-4')
					('0:21:25', u'C(52-5-4,2)')
	part2_correct_attempt
					['0:23:42', u'C(52-5,2) - C(52-5-4,2)']

78 Student ID:jnatale

	first_attempt
					2015-10-21 01:04:07
	part2_incorrect_attempt
					('0:00:54', u'4*45')
					('0:02:25', u'4 * 45')
					('0:02:30', u'4 * 45 * 2')
					('0:03:04', u'4 * 46')
					('0:03:33', u'4*46*2')
					('0:13:59', u'4*19')
					('0:14:05', u'4*18')
					('0:15:23', u'4 * 46')
					('0:28:06', u'4 * 45')
					('0:28:37', u'4 * 45 * 2')
					('0:30:07', u'4 * 46 * 2')
					('0:34:46', u'4 * 3 / 2')
					('0:35:08', u'4 * 3')
					('0:37:03', u'4 * 49')
					('0:37:09', u'4 * 41')
					('0:37:15', u'4 * 42')
					('0:40:43', u'C(4,1) * 42')
					('0:40:47', u'C(4,1) * 46')
					('0:41:22', u'4 * 46')
					('1:10:09', u'4 *46')
	part2_correct_attempt
					['1:35:22', u'C(47,2) - C(43,2)']

79 Student ID:ganajera

	first_attempt
					2015-10-17 21:18:27
	part2_incorrect_attempt
					('0:00:00', u'4*46')
					('0:05:07', u'4*3')
	part2_correct_attempt
					['2:55:28', u'C(47,2)-C(43,2)']

80 Student ID:nnh002

	first_attempt
					2015-10-22 04:33:52
	part2_incorrect_attempt
					('-1 day, 22:50:55', u'C(47,4)')
	part2_correct_attempt
					['-1 day, 22:55:08', u'C(47,2)-C(43,2)']

81 Student ID:akhmelni

	first_attempt
					2015-10-22 22:24:10
	part2_incorrect_attempt
					('0:00:23', u'C(52,7)')
	part2_correct_attempt
					['0:04:45', u'12/2 + (2*4*43)/2']

82 Student ID:tol003

	first_attempt
					2015-10-21 00:19:10
	part2_incorrect_attempt
					('0:00:00', u'C(4,2)')
					('0:07:06', u'C(47,2)')
	part2_correct_attempt
					['0:11:45', u'C(47,2)-C(43,2)']

83 Student ID:aakumar

	first_attempt
					2015-10-19 07:10:07
	part2_incorrect_attempt
					('15:35:04', u'6*46')
					('15:35:34', u'6*43')
	part2_correct_attempt
					['15:37:19', u'C(47,2)-C(43,2)']

84 Student ID:kew017

	first_attempt
					2015-10-22 20:11:58
	part2_incorrect_attempt
					('0:03:53', u'C(4,2)')
					('0:05:48', u'2*4')
					('0:08:31', u'4*(52-5-1)')
					('0:08:37', u'4*(52-5)')
					('0:08:45', u'(52-5)')
					('0:09:39', u'4*(52-5-1)')
					('0:10:04', u'(52-5-1)')
	part2_correct_attempt
					['0:12:06', u'C(52-5,2)-C(52-5-4,2)']

85 Student ID:yeh013

	first_attempt
					2015-10-22 08:53:45
	part2_incorrect_attempt
					('0:01:25', u'4*46')
	part2_correct_attempt
					['0:08:55', u'178']

86 Student ID:eaherman

	first_attempt
					2015-10-22 15:31:20
	part2_incorrect_attempt
					('0:01:25', u'C(8,2)')
	part2_correct_attempt
					['0:11:53', u'C(47,2)-C(43,2)']

87 Student ID:asetters

	first_attempt
					2015-10-20 07:07:53
	part2_incorrect_attempt
					('0:00:39', u'4*46')
					('0:00:59', u'4*46/2')
					('0:02:55', u'4*47')
					('0:03:05', u'4*47/2')
					('0:03:41', u'4*46')
					('0:04:16', u'47*4 + 4*46')
					('0:05:12', u'2*4*46')
					('0:05:41', u'4*46+4*47')
					('0:06:20', u'47*46')
					('0:07:08', u'4*3 + 47 *4 + 4*43')
					('0:08:07', u'4*46')
					('0:08:32', u'4*46/2')
	part2_correct_attempt
					['0:22:13', u'12/2 + ((2*4*43)/2)']

88 Student ID:tdurrer

	first_attempt
					2015-10-22 23:32:12
	part2_incorrect_attempt
					('0:04:45', u'C(4,1)*C(46,1)')
					('0:06:15', u'C(4,1)*C(46,43)')
					('0:07:56', u'C(4,1)*(52-5-4)')
					('0:10:00', u'C(52-5-4,1)*C(4,1)')
					('0:10:11', u'C(52-5-4,1)+C(4,1)')

89 Student ID:ksrijong

	first_attempt
					2015-10-22 06:19:40
	part2_incorrect_attempt
					('0:00:54', u'4*C(43,1)')
					('0:01:28', u'C(43,1)')
	part2_correct_attempt
					['0:03:29', u'C(47,2)-C(43,2)']

90 Student ID:yhhan

	first_attempt
					2015-10-22 21:39:52
	part2_incorrect_attempt
					('0:01:15', u'8+12')
					('1:39:08', u'43*4 + 12')
	part2_correct_attempt
					['1:39:30', u'43*4 + C(4,2)']

91 Student ID:volim

	first_attempt
					2015-10-21 03:06:06
	part2_incorrect_attempt
					('0:06:42', u'C(52-5,2)*C(13,1)*C(4,1)')
					('0:08:04', u'2(C(13,1)*C(4,1))+(C(13,1)*C(4,2))')
					('0:08:22', u'(C(13,1)*C(4,1))+(C(13,1)*C(4,2))')
					('0:10:30', u'((12^4)^2)')
					('0:10:58', u'((46^4)^2)')
					('0:11:42', u'46^4')
					('0:11:56', u'(52-6)^4')
					('0:19:04', u'(46^4)+(46^4)')
					('0:20:41', u'(46^4)+(46^4)-12')
					('0:21:42', u'(46^4)+(45^4)')
					('0:25:49', u'C(13,1)*C(4,1)*C(45,1)')
					('0:25:58', u'C(13,1)*C(45,1)')
					('0:33:55', u'(4*45)')
					('0:34:18', u'(4*45)+(4*44)')
					('0:35:02', u'2(4*42)+12')
	part2_correct_attempt
					['0:42:52', u'C(47,2)-C(43,2)']

92 Student ID:v4sharma

	first_attempt
					2015-10-22 02:50:33
	part2_incorrect_attempt
					('0:02:37', u'C(4,2)')
	part2_correct_attempt
					['0:07:00', u'C(47,2) - C(43,2)']

93 Student ID:atorr

	first_attempt
					2015-10-22 23:29:25
	part2_incorrect_attempt
					('0:01:41', u'C(52,2) - C(48,2)')
					('0:01:57', u'C(52,1) - C(48,1)')
					('0:03:12', u'52 - 4')
					('0:05:40', u'C(52 - 5,1)')
					('0:06:32', u'C(52 - 5,1) - 12')
					('0:07:30', u'C(52 - 5,1) - C(52 - 9,1)')
					('0:08:11', u'C(52 - 5,1) - C(47 - 4,1)')
					('0:11:10', u'((C(52 - 5,1) * C(4,1)) - C(47 - 4,1))')
					('0:11:54', u'C(52 - 5,1) - C(47 - 4,1)')
					('0:13:15', u'(C(52 - 5,1) - C(47 - 4,1)) * C(4,1)')
					('0:18:26', u'C(4,1) * C(47,1) - C(43,1)')
					('0:18:34', u'C(4,1) (C(47,1) - C(43,1))')
					('0:18:46', u'C(4,1) * (C(47,1) - C(43,1))')

94 Student ID:cagatep

	first_attempt
					2015-10-22 21:17:31
	part2_incorrect_attempt
					('-1 day, 23:56:56', u'C(4,1) + C(46,1)')
					('0:00:16', u'(C(4,1) + C(46,1)) * 2')
					('0:00:49', u'C(4, 1)')
					('0:00:56', u'C(4, 1) * 2')
					('0:01:22', u'C(4, 1) + C(46, 1)')
					('0:03:14', u'C(4, 2)')
					('0:03:36', u'2(C(4, 1) + C(46, 1))')
	part2_correct_attempt
					['0:07:37', u'C(47, 2) - C(43, 2)']

95 Student ID:tjke

	first_attempt
					2015-10-18 04:56:52
	part2_incorrect_attempt
					('0:01:25', u'4*47')
					('0:01:59', u'4*46')
					('0:02:08', u'4*(47-4)')
	part2_correct_attempt
					['0:04:00', u'C(47,2)-C(43,2)']

96 Student ID:skarimik

	first_attempt
					2015-10-17 22:10:47
	part2_incorrect_attempt
					('0:00:00', u'(4!/(2!2!))*45')
					('0:02:19', u'(4)*46')
					('0:13:42', u'(4)*43')
					('0:19:03', u'2*(4)*46')
					('0:20:33', u'4*42')
	part2_correct_attempt
					['0:33:24', u'C(47,2)-C(43,2)']

97 Student ID:kquong

	first_attempt
					2015-10-18 04:37:47
	part2_incorrect_attempt
					('0:00:00', u'4 * 51')
					('0:00:21', u'4 * 52')
					('0:00:47', u'4 * 46')
					('0:00:53', u'4 * 47')
					('0:02:59', u'4 * 12')
					('0:04:37', u'4*3')
					('0:07:36', u'46 * 4')
					('0:07:42', u'45 * 4')
					('0:18:23', u'4 * 47 -1')
					('0:18:31', u'4 * 46 -1')
					('0:19:21', u'47!/(2!(47-2))')
					('0:24:50', u'47!/(2!(47-2))- 12')
					('0:25:41', u'4*46/2')
					('0:29:27', u'4 *43')
					('0:29:35', u'4 *44')
	part2_correct_attempt
					['0:38:36', u'(47!/(2!(47-2)!)) - 43!/(2!(43-2)!)']

98 Student ID:t2shin

	first_attempt
					2015-10-22 23:20:42
	part2_incorrect_attempt
					('0:02:22', u'4*46')
	part2_correct_attempt
					['0:06:22', u'(47!/(2!45!))-(43!/(2!41!))']

99 Student ID:vsamant

	first_attempt
					2015-10-21 19:00:33
	part2_incorrect_attempt
					('0:03:29', u'C(4,1)*C(47,1)')
	part2_correct_attempt
					['0:09:27', u'C(47,2)-C(43,2)']

100 Student ID:aportuga

	first_attempt
					2015-10-21 07:52:40
	part2_incorrect_attempt
					('0:01:39', u'1533939-962598')
	part2_correct_attempt
					['0:02:36', u'1081-903']

101 Student ID:ppanourg

	first_attempt
					2015-10-22 21:47:48
	part2_incorrect_attempt
					('-1 day, 13:14:33', u'7*4^7')
	part2_correct_attempt
					['-1 day, 23:30:39', u'1081']

102 Student ID:ewbrenna

	first_attempt
					2015-10-22 04:41:25
	part2_incorrect_attempt
					('0:01:00', u'4*52*2')
					('0:01:24', u'C(52,1)*4')
					('0:05:30', u'C(52,1)*4*2')
					('0:05:37', u'C(52,1)')
					('0:05:44', u'C(52,1)^2')
					('0:05:56', u'C(52,1)*3')
					('0:06:10', u'C(52,1)*4')
					('0:06:17', u'C(52,1)*8')
					('0:06:23', u'C(52,1)*16')
					('0:06:44', u'C(52,1)*2')
					('0:10:16', u'C(52,2)-C(48,2)')
					('0:51:36', u'C(52,2)-C(47,2)')
					('0:52:51', u'C(4,1)*C(52,2)*2')
					('0:55:09', u'C(52,2)')
					('0:55:48', u'C(52,2)-C(48,2)')
					('0:56:29', u'C(52,2)-C(42,2)')
					('0:56:50', u'52*4*2')
					('0:59:15', u'C(52,2)-C(48,2)')
					('1:00:29', u'C(52,2)-C(47,2)')
					('1:00:36', u'C(52,2)-C(48,2)')
					('1:00:41', u'C(52,2)-C(48,2)-1')
					('1:00:49', u'C(52,2)-C(48,2)-2')
					('1:00:56', u'C(52,2)-C(48,2)+2')
					('1:01:03', u'C(52,2)-C(48,2)+1')
					('1:48:45', u'46*4')
					('1:50:43', u'C(52,2)-C(48,2)')
	part2_correct_attempt
					['1:51:53', u'C(47,2)-C(43,2)']

103 Student ID:any027

	first_attempt
					2015-10-19 20:31:02
	part2_incorrect_attempt
					('0:02:27', u'P(47,2)')
					('0:04:01', u'4 * C(46,1)')
					('0:04:13', u'4 + C(46,1)')
					('0:04:45', u'4 * C(46,1)')
					('0:04:54', u'4 * C(45,1)')
					('0:05:04', u'4 * C(47,1)')
					('0:05:12', u'4 * C(44,1)')
					('0:06:29', u'4 * C(43,1)')
	part2_correct_attempt
					['0:08:59', u'C(47,2) - C(43,2)']

104 Student ID:rwthomps

	first_attempt
					2015-10-20 23:04:01
	part2_incorrect_attempt
					('0:01:00', u'4 * 43')
					('0:02:24', u'4 * (52 - 5 - 4)')
	part2_correct_attempt
					['0:03:23', u'C(47, 2) - C(43, 2)']

105 Student ID:s1powers

	first_attempt
					2015-10-21 20:00:29
	part2_incorrect_attempt
					('0:00:37', u'3*4 * 46!')
					('0:00:45', u'3*4 * 46')
					('0:00:56', u'4*46')
					('0:03:08', u'4*46 8')
					('0:03:33', u'4*45 + 4!/(2!2!)')
					('0:03:53', u'4*42 + 4!/(2!2!)')
	part2_correct_attempt
					['0:04:29', u'4*43 + 4!/(2!2!)']

106 Student ID:vsosnovs

	first_attempt
					2015-10-22 06:44:48
	part2_incorrect_attempt
					('0:01:45', u'C(47,2)')
	part2_correct_attempt
					['0:01:54', u'C(47,2)-C(43,2)']

107 Student ID:k5law

	first_attempt
					2015-10-19 06:58:32
	part2_incorrect_attempt
					('0:00:25', u'[(52-5)!/(2!47!)]-[(52-5-4)!/(2!43!)]')
	part2_correct_attempt
					['0:00:58', u'[(52-5)!/(2!45!)]-[(52-5-4)!/(2!41!)]']

108 Student ID:s2chaudh

	first_attempt
					2015-10-22 02:53:25
	part2_incorrect_attempt
					('0:04:40', u'47 2 43 2')
	part2_correct_attempt
					['0:37:15', u'C(47,2)- C(43, 2)']

109 Student ID:j6quach

	first_attempt
					2015-10-22 18:50:13
	part2_incorrect_attempt
					('0:06:03', u'4*28')
					('0:08:56', u'4*46')
					('0:28:32', u'4*42')
					('0:29:05', u'4*38')
	part2_correct_attempt
					['0:34:15', u'C(47,2) - C(43,2)']

110 Student ID:bmilton

	first_attempt
					2015-10-21 03:30:11
	part2_incorrect_attempt
					('0:02:38', u'C(52-5,4) * C(52-6,1)')
					('0:03:58', u' C(52-6,1)')
					('0:07:25', u'(C(4,1) * C(52-6,1)) - 3')
					('0:09:53', u'(C(4,1) * C(52-6,1)) - 1')
					('0:10:35', u'C(43,2)')
					('0:11:15', u'C(4,1) * C(52-6, 1)')
	part2_correct_attempt
					['0:11:28', u'(C(4,1) * C(52-6, 1)) - 6']

111 Student ID:jhc010

	first_attempt
					2015-10-22 08:26:18
	part2_incorrect_attempt
					('0:01:46', u'4*46')
	part2_correct_attempt
					['0:03:29', u'C(47,2) - C(43,2)']

112 Student ID:rsmurlo

	first_attempt
					2015-10-21 17:40:22
	part2_incorrect_attempt
					('0:02:30', u'4*46')
					('0:03:05', u'4*3')
					('0:05:57', u'4*43+4*3')
	part2_correct_attempt
					['0:17:19', u'C(47,2)-C(43,2)']

113 Student ID:agarango

	first_attempt
					2015-10-22 21:03:26
	part2_incorrect_attempt
					('0:18:44', u'4*46')
					('0:19:03', u'(4*46)/2')
					('0:23:36', u'4*47')
					('0:23:42', u'4*46')
					('0:44:27', u'4*43')
	part2_correct_attempt
					['0:48:53', u'178']

114 Student ID:achinn

	first_attempt
					2015-10-19 22:14:18
	part2_incorrect_attempt
					('0:02:19', u'4*46')
					('0:02:59', u'C(4,2)')
					('0:03:07', u'4*3*2')
					('0:14:40', u'4*46+42*4')
					('0:14:58', u'4*46+44*4')
					('1:21:01', u'4*3')
	part2_correct_attempt
					['1:24:06', u'C(47,2)-(43*42)/2']

115 Student ID:kalang

	first_attempt
					2015-10-22 20:53:19
	part2_incorrect_attempt
					('0:00:20', u'C(52,2)')
					('0:00:26', u'C(52-4,2)')
					('0:00:32', u'C(52-5,2)')
	part2_correct_attempt
					['0:01:20', u'C(52-5,2)-C(52-9,2)']

116 Student ID:mcatozzi

	first_attempt
					2015-10-21 00:16:29
	part2_incorrect_attempt
					('0:08:10', u'46*4')
	part2_correct_attempt
					['0:10:21', u'C(47,2) - C(43,2)']

117 Student ID:jnn015

	first_attempt
					2015-10-22 23:14:06
	part2_incorrect_attempt
					('-1 day, 23:59:51', u'46*4')
	part2_correct_attempt
					['0:03:25', u'C(47,2) - C(43,2)']

118 Student ID:dpereira

	first_attempt
					2015-10-19 20:18:29
	part2_incorrect_attempt
					('0:00:51', u'4*(52-6)')
					('0:00:57', u'4*(52-6)*2')
					('0:01:17', u'4*3')
					('0:05:15', u'4*46')
					('0:09:43', u'C(4,1)*C(46,1)')
					('0:09:51', u'C(4,1)*C(46,1)*2')
					('0:10:58', u'C(4,1) * 46')
					('0:12:03', u'C(4,2)')
					('0:13:01', u'C(4,1) * 46 * 2')
					('21:55:28', u'C(4,1) * 48')
					('21:57:15', u'C(4,1) * (52-9)')
					('21:57:44', u'4*3')
					('21:58:03', u'C(4,1) * 46')
					('23:52:12', u'C(47,4)*46')
					('23:54:38', u'C(47,4)*46*2')
	part2_correct_attempt
					['1 day, 6:19:50', u'C(47,2) - C(43,2)']

119 Student ID:haliew

	first_attempt
					2015-10-22 00:20:33
	part2_incorrect_attempt
					('0:14:05', u'184*2')
					('0:21:01', u'C(4,1)*C(3,1)')
	part2_correct_attempt
					['0:42:36', u'C(47,2)-C(43,2)']

120 Student ID:r2fisher

	first_attempt
					2015-10-22 23:48:30
	part2_incorrect_attempt
					('0:01:30', u'4*46')
	part2_correct_attempt
					['0:07:11', u'C(47,2)-C(43,2)']

121 Student ID:vasharma

	first_attempt
					2015-10-21 23:54:47
	part2_incorrect_attempt
					('0:02:31', u'C(52-7,1)')
					('0:03:07', u'C(52-7,1)-41')
					('0:03:28', u'C(52-7,1)-C(41,1)')
					('0:03:53', u'C(52-5,1)-43')
					('0:04:07', u'C(52-5,1)-4')
	part2_correct_attempt
					['0:06:32', u'C(52-5,2)-C(52-5-4,2)']

122 Student ID:syip

	first_attempt
					2015-10-18 22:06:29
	part2_incorrect_attempt
					('-1 day, 23:27:59', u'2*4*46')
					('0:00:00', u'4*46')
	part2_correct_attempt
					['0:03:35', u'C(47,2) - C(43,2)']

123 Student ID:yypan

	first_attempt
					2015-10-21 23:01:51
	part2_incorrect_attempt
					('0:01:54', u'C(52,1)-C(51,1)')
					('0:02:52', u'4*43')
					('0:03:21', u'4*C(43,1)')
	part2_correct_attempt
					['0:09:23', u'C(47,2)-C(43,2)']

124 Student ID:ajvanega

	first_attempt
					2015-10-22 01:22:02
	part2_incorrect_attempt
					('0:04:04', u'C(52,2) ')
					('0:04:29', u'C(50,2)')
					('0:06:08', u'4*52')
					('0:06:26', u'4*C(52,1)')
					('0:06:40', u'4*(C(52,1))')
					('1:19:52', u'C(47,12)')
					('1:20:20', u'C(47,2)')
					('1:20:32', u'C(47,4)')
					('1:20:44', u'C(47,1)')
					('1:23:28', u'C(47,4)')
					('1:25:18', u'C(47,4)+C(47,3)')
					('1:25:49', u'C(47,4)+C(46,3)')
					('1:29:14', u'4*C(46,1)')
					('1:30:34', u'4*C(47,1)')
					('1:31:32', u'16*4')
	part2_correct_attempt
					['1:35:31', u'C(47,2)-C(43,2)']

125 Student ID:zhw110

	first_attempt
					2015-10-22 07:09:18
	part2_incorrect_attempt
					('0:02:22', u'4*46')
	part2_correct_attempt
					['0:10:16', u'C(47,2)-C(43,2)']

126 Student ID:mtrafeca

	first_attempt
					2015-10-21 09:01:50
	part2_incorrect_attempt
					('-1 day, 23:29:18', u'46*(C(47,1))')
					('-1 day, 23:34:05', u'C(46,1)')
					('-1 day, 23:35:09', u'4*46')
					('-1 day, 23:35:25', u'4*47')
					('-1 day, 23:35:51', u'C(4,1)*47')
					('-1 day, 23:38:39', u'C(4,2)*47')
					('-1 day, 23:40:56', u'4*47')
					('-1 day, 23:41:07', u'8*47')
					('0:03:03', u'46*8')
					('0:03:10', u'46*4')
					('0:03:22', u'47*4')
					('0:03:30', u'47*8')
					('0:04:43', u'46*4')
					('0:05:10', u'(46*4)+(46*4)')
					('0:07:57', u'C(47,4)46')
					('0:08:16', u'C(4,1)46')
					('0:10:13', u'C(4,1)47')
					('0:10:20', u'C(4,1)45')
					('0:10:36', u'C(8,1)46')
					('0:13:25', u'4*47')
					('0:13:33', u'8*47')
					('0:13:40', u'2*47')
					('0:18:09', u'46*16')
					('0:18:17', u'47*16')
					('0:19:53', u'47-16')
					('0:23:23', u'16*45')
					('0:23:29', u'16*46')
					('0:23:37', u'16*47')
	part2_correct_attempt
					['0:33:57', u'C(47,2)-C(43,2)']

127 Student ID:kosung

	first_attempt
					2015-10-22 22:39:12
	part2_incorrect_attempt
					('0:00:51', u'C(4,1)*C(46,1)')
					('0:27:55', u'C(4,1)*C(46,1)*2-12')
					('0:28:28', u'4*42+12')
	part2_correct_attempt
					['0:37:35', u'178']












## Part 3

### (16) Mistake Group ['R.0'] of size 16
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(47,2)	|47*46	|[('R.0', 47.0, u'47', u'47')]	|
|1	|C(47,2)	|C(47,5)	|[('R.0', 47.0, u'47', u'47')]	|




### (11) Mistake Group Digits of size 11




### (6) Mistake Group redirect of size 6




### (5) Mistake Group ['R.1'] of size 5
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|C(47,2)	|47*46*2	|[('R.1', 2.0, u'2', u'2')]	|
|1	|C(47,2)	|C(48,2)	|[('R.1', 2.0, u'2', u'2')]	|
|2	|C(47,2)	|C(52,2)	|[('R.1', 2.0, u'2', u'2')]	|
|3	|C(47,2)	|C(57,2)	|[('R.1', 2.0, u'2', u'2')]	|
|4	|C(47,2)	|C(52-7,2)	|[('R.1', 2.0, u'2', u'2')]	|




### (5) Mistake Group Fraction of size 5




### (12) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:b3hwang

	first_attempt
					2015-10-21 02:20:34
	part1_correct_attempt
					['0:00:00', u'2*8']
	part2_correct_attempt
					['0:12:11', u'C(47,2)-C(43,2)']
	part3_incorrect_attempt
					('0:12:53', u'20*C(47,2)')
					('0:13:23', u'C(20,5)*C(47,2)')
					('0:13:43', u'5*C(47,2)')
					('0:14:20', u'5+C(47,2)')
					('0:14:33', u'5*C(47,2)')
	part3_correct_attempt
					['0:14:44', u'C(47,2)']

1 Student ID:v3doan

	first_attempt
					2015-10-22 20:54:24
	part1_correct_attempt
					['0:00:00', u'16']
	part2_correct_attempt
					['0:03:31', u'C(47,2) - C(43,2)']
	part3_incorrect_attempt
					('0:08:11', u'16 + C(47,2) - C(43,2)')
	part3_correct_attempt
					['0:12:06', u'C(47, 2)']

2 Student ID:kquong

	first_attempt
					2015-10-18 04:37:47
	part1_correct_attempt
					['0:00:00', u'16']
	part2_correct_attempt
					['0:38:36', u'(47!/(2!(47-2)!)) - 43!/(2!(43-2)!)']
	part3_incorrect_attempt
					('0:42:43', u'16 + (47!/(2!(47-2)!)) - 43!/(2!(43-2)!)')
					('0:43:48', u' 16 + 178')
	part3_correct_attempt
					['0:44:45', u'47!/(2!(47-2)!)']

3 Student ID:r2fisher

	first_attempt
					2015-10-22 23:48:30
	part1_correct_attempt
					['0:00:00', u'16']
	part2_correct_attempt
					['0:07:11', u'C(47,2)-C(43,2)']
	part3_incorrect_attempt
					('0:08:04', u'C(47,2)-C(43,2) + 16')
	part3_correct_attempt
					['0:08:32', u'C(47,2)']

4 Student ID:vasharma

	first_attempt
					2015-10-21 23:54:47
	part1_correct_attempt
					['0:00:00', u'16']
	part2_correct_attempt
					['0:06:32', u'C(52-5,2)-C(52-5-4,2)']
	part3_incorrect_attempt
					('0:06:51', u'C(47,1)')
	part3_correct_attempt
					['0:07:16', u'C(47,2)']

5 Student ID:abasu

	first_attempt
					2015-10-20 23:39:42
	part1_correct_attempt
					['0:00:00', u'16']
	part2_correct_attempt
					['0:07:32', u'C(47,2) - C(43,2)']
	part3_incorrect_attempt
					('0:09:32', u'178+16')
					('0:10:09', u'C(52,7)-C(47,7)')
	part3_correct_attempt
					['0:11:37', u'C(47,2)']

6 Student ID:acvuong

	first_attempt
					2015-10-18 01:07:49
	part1_correct_attempt
					['0:00:00', u'16']
	part2_correct_attempt
					['0:26:14', u'C(47,2) - C(43,2)']
	part3_incorrect_attempt
					('0:27:17', u'4*4*4*4*4')
					('0:27:51', u'4*4*4*4*4*47*46')
	part3_correct_attempt
					['0:29:56', u'C(47,2)']

7 Student ID:volim

	first_attempt
					2015-10-21 03:06:06
	part1_correct_attempt
					['0:00:00', u'16']
	part2_correct_attempt
					['0:42:52', u'C(47,2)-C(43,2)']
	part3_incorrect_attempt
					('0:43:37', u'16+(C(47,2)-C(43,2))')
	part3_correct_attempt
					['0:43:56', u'C(47,2)']

8 Student ID:any027

	first_attempt
					2015-10-19 20:31:02
	part1_correct_attempt
					['0:00:00', u'16']
	part2_correct_attempt
					['0:08:59', u'C(47,2) - C(43,2)']
	part3_incorrect_attempt
					('0:09:39', u'C(47,2) - C(43,2) +16')
	part3_correct_attempt
					['0:10:09', u'C(47,2)']

9 Student ID:mcatozzi

	first_attempt
					2015-10-21 00:16:29
	part1_correct_attempt
					['0:00:00', u'16']
	part2_correct_attempt
					['0:10:21', u'C(47,2) - C(43,2)']
	part3_incorrect_attempt
					('0:20:47', u'C(47,2) - C(43,2) + 16')
	part3_correct_attempt
					['0:21:29', u'C(47,2)']

10 Student ID:c1sorian

	first_attempt
					2015-10-21 21:38:04
	part1_correct_attempt
					['0:00:00', u'16']
	part2_correct_attempt
					['0:04:09', u'C(47,2)-C(43,2)']
	part3_incorrect_attempt
					('0:05:08', u'C(52,5)')
					('0:05:24', u'C(52,7)')
	part3_correct_attempt
					['0:05:38', u'C(47,2)']

11 Student ID:t2li

	first_attempt
					2015-10-22 23:29:22
	part1_correct_attempt
					['0:00:00', u'16']
	part2_correct_attempt
					['0:00:33', u'C(47,2)-C(43,2)']
	part3_incorrect_attempt
					('0:00:41', u'C(52-5,2)-C(52-5-4,2)')
					('0:01:38', u'16+C(47,2)-C(43,2)')
	part3_correct_attempt
					['0:01:47', u'C(47,2)']












## Part 4

### (78) Mistake Group redirect of size 78




### (4) Mistake Group ['R.0.1'] of size 4
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|[C(52-5,2)-C(52-5-4,2)+4^2]/[C(52-5,2)]	|12*C(4,1)^2/C(47,2)	|[('R.0.1', 16.0, u'4^2', u'C(4,1)^2')]	|
|1	|[C(52-5,2)-C(52-5-4,2)+4^2]/[C(52-5,2)]	|(C(4,2)+16)/C(47,2)	|[('R.0.1', 16.0, u'4^2', u'16')]	|
|2	|[C(52-5,2)-C(52-5-4,2)+4^2]/[C(52-5,2)]	|(C(4,2)+4+4+16)/C(47,2)	|[('R.0.1', 16.0, u'4^2', u'16')]	|
|3	|[C(52-5,2)-C(52-5-4,2)+4^2]/[C(52-5,2)]	|(C(4,2)+C(4,1)+16)/C(47,2)	|[('R.0.1', 16.0, u'4^2', u'16')]	|




### (3) Mistake Group Digits of size 3




### (2) Mistake Group ['R.0.0'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|[C(52-5,2)-C(52-5-4,2)+4^2]/[C(52-5,2)]	|((C(5,5)*(C(47,2)-C(43,2)))+(C(5,5)*C(8,2)))/((47!/(2!45!)))	|[('R.0.0', 178.0, u'C(52-5,2)-C(52-5-4,2)', u'C(5,5)*(C(47,2)-C(43,2))')]	|
|1	|[C(52-5,2)-C(52-5-4,2)+4^2]/[C(52-5,2)]	|((C(5,5)*(C(47,2)-C(43,2)))+(C(5,5)*C(16,2)))/((47!/(2!45!)))	|[('R.0.0', 178.0, u'C(52-5,2)-C(52-5-4,2)', u'C(5,5)*(C(47,2)-C(43,2))')]	|




### (2) Mistake Group ['R.0'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|[C(52-5,2)-C(52-5-4,2)+4^2]/[C(52-5,2)]	|16+178+1081/ C(47,2)	|[('R.0', 194.0, u'C(52-5,2)-C(52-5-4,2)+4^2', u'16+178')]	|
|1	|[C(52-5,2)-C(52-5-4,2)+4^2]/[C(52-5,2)]	|16+12/2 + (2*4*43)/2+C(47,2)	|[('R.0', 194.0, u'C(52-5,2)-C(52-5-4,2)+4^2', u'16+12/2 + (2*4*43)/2')]	|




### (1) Mistake Group ['R.0.0', 'R.0.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|[C(52-5,2)-C(52-5-4,2)+4^2]/[C(52-5,2)]	|(C(47,2)-C(43,2))*C(4,1)^2/C(47,2)	|[('R.0.0', 178.0, u'C(52-5,2)-C(52-5-4,2)', u'C(47,2)-C(43,2)'), ('R.0.1', 16.0, u'4^2', u'C(4,1)^2')]	|




### (1) Mistake Group Wrong_Sign of size 1




### (1) Mistake Group ['R.0.0.1', 'R.0.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.1', 'R.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|[C(52-5,2)-C(52-5-4,2)+4^2]/[C(52-5,2)]	|(C(52,2)-C(52-5-4,2)+4^2)/C(52-5,2)	|[('R.0.0.1', 903, u'C(52-5-4,2)', u'C(52-5-4,2)'), ('R.0.1', 16.0, u'4^2', u'4^2')]	|




### (1) Mistake Group ['R.0.0.1.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|[C(52-5,2)-C(52-5-4,2)+4^2]/[C(52-5,2)]	|(C(52,5)*C(13,2)*C(4,2)+C(52,5)*C(13,1)*C(4,1)*C(46,1))/(C(52,5))	|[('R.0.0.1.1', 2.0, u'2', u'2')]	|




### (1) Mistake Group ['R.0.0.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|[C(52-5,2)-C(52-5-4,2)+4^2]/[C(52-5,2)]	|(16+C(52-5-4,2)-12)/(C(47,2))	|[('R.0.0.1', 903, u'C(52-5-4,2)', u'C(52-5-4,2)')]	|




### (23) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:jag028

	first_attempt
					2015-10-22 17:08:52
	part1_correct_attempt
					['0:00:00', u'16']
	part2_correct_attempt
					['0:00:24', u'C(47,2)-C(43,2)']
	part3_correct_attempt
					['0:00:38', u'C(47,2)']
	part4_incorrect_attempt
					('0:01:18', u'[C(47,2)-C(43,2)]/C(47,2)')
	part4_correct_attempt
					['0:01:57', u'[(C(47,2)-C(43,2))+16]/C(47,2)']

1 Student ID:aggouw

	first_attempt
					2015-10-21 08:50:34
	part1_correct_attempt
					['0:00:00', u'C(4,1)*C(4,1)']
	part2_correct_attempt
					['0:00:32', u'C(47,2)-C(43,2)']
	part3_correct_attempt
					['0:00:32', u'C(47,2)']
	part4_incorrect_attempt
					('0:01:58', u'[C(4,1)*C(4,1)]+[C(47,2)-C(43,2)]/C(47,2)')
	part4_correct_attempt
					['0:02:13', u'[[C(4,1)*C(4,1)]+[C(47,2)-C(43,2)]]/C(47,2)']

2 Student ID:rohan

	first_attempt
					2015-10-22 22:49:42
	part1_correct_attempt
					['0:00:00', u'16']
	part3_correct_attempt
					['0:04:07', u'1081']
	part4_incorrect_attempt
					('0:07:34', u'32/1081')
	part4_correct_attempt
					['0:07:51', u'194/1081']

3 Student ID:rsmurlo

	first_attempt
					2015-10-21 17:40:22
	part1_correct_attempt
					['0:00:00', u'4*4']
	part2_correct_attempt
					['0:17:19', u'C(47,2)-C(43,2)']
	part3_correct_attempt
					['0:20:47', u'47*46/2']
	part4_incorrect_attempt
					('0:21:44', u'16+178/1081')
	part4_correct_attempt
					['0:21:58', u'(16+178)/1081']

4 Student ID:mrchin

	first_attempt
					2015-10-22 18:46:20
	part1_correct_attempt
					['0:00:00', u'16']
	part2_correct_attempt
					['0:00:00', u'178']
	part3_correct_attempt
					['0:00:25', u'1081']
	part4_incorrect_attempt
					('0:00:25', u'.179')
	part4_correct_attempt
					['0:00:44', u'.179463']

5 Student ID:nhn018

	first_attempt
					2015-10-22 20:21:18
	part1_correct_attempt
					['0:00:00', u'4^2']
	part2_correct_attempt
					['0:00:00', u'C(47,2)-C(52-5-4,2)']
	part3_correct_attempt
					['0:00:00', u'C(47,2)']
	part4_incorrect_attempt
					('0:00:00', u'42^2+C(47,2)-C(52-5-4,2)/C(47,2)')
					('0:00:22', u'(42^2+C(47,2)-C(52-5-4,2))/C(47,2)')
	part4_correct_attempt
					['0:00:37', u'(4^2+C(47,2)-C(52-5-4,2))/C(47,2)']

6 Student ID:j5phung

	first_attempt
					2015-10-16 19:10:56
	part1_correct_attempt
					['0:00:00', u'C(4,1)^2']
	part2_correct_attempt
					['4:43:40', u'C(47,2)-C(43,2)']
	part3_correct_attempt
					['-1 day, 23:06:14', u'C(47,2)']
	part4_incorrect_attempt
					('4:43:57', u'C(47,2)-C(43,2)*C(4,1)^2/C(47,2)')
					('4:44:46', u'C(47,2)-C(43,2)+C(4,1)^2/C(47,2)')
					('4:45:01', u'(C(47,2)-C(43,2)+C(4,1)^2/C(47,2))')
	part4_correct_attempt
					['4:45:11', u'(C(47,2)-C(43,2)+C(4,1)^2)/C(47,2)']

7 Student ID:dcgriffi

	first_attempt
					2015-10-21 03:41:56
	part1_correct_attempt
					['0:00:00', u'16']
	part2_correct_attempt
					['0:52:16', u'C(47,2) - C(43,2)']
	part3_correct_attempt
					['0:34:48', u'C(47,2)']
	part4_incorrect_attempt
					('0:52:34', u'(16 + 46*4)/(C(47,2) - C(43,2))')
	part4_correct_attempt
					['0:53:05', u'(16 + (C(47,2) - C(43,2)))/C(47,2)']

8 Student ID:cfgutier

	first_attempt
					2015-10-22 08:30:07
	part1_correct_attempt
					['0:00:00', u'16']
	part2_correct_attempt
					['0:00:37', u'[(47!)/(2!*45!)]-[(43!)/(2!*41!)]']
	part3_correct_attempt
					['0:00:54', u'[(47!)/(2!*45!)]']
	part4_incorrect_attempt
					('0:31:37', u'16 + [(47!)/(2!*45!)]-[(43!)/(2!*41!)]')
	part4_correct_attempt
					['0:32:21', u'[16 + [(47!)/(2!*45!)]-[(43!)/(2!*41!)]] / (47!/(2!*45!))']

9 Student ID:pnquach

	first_attempt
					2015-10-22 09:09:30
	part1_correct_attempt
					['0:00:00', u'16']
	part2_correct_attempt
					['0:04:13', u'C(47,2) - C(43,2)']
	part3_correct_attempt
					['0:00:00', u'C(47,2)']
	part4_incorrect_attempt
					('0:04:25', u'(C(47,2) - C(43,2))/(C(47,2))')
	part4_correct_attempt
					['0:05:06', u'(16+(C(47,2) - C(43,2)))/(C(47,2))']

10 Student ID:asrana

	first_attempt
					2015-10-22 21:08:31
	part1_correct_attempt
					['0:00:00', u'16']
	part2_correct_attempt
					['0:08:11', u'178']
	part3_correct_attempt
					['0:09:19', u'1081']
	part4_incorrect_attempt
					('0:09:52', u'.18')
	part4_correct_attempt
					['0:10:26', u'194/1081']

11 Student ID:vsosnovs

	first_attempt
					2015-10-22 06:44:48
	part1_correct_attempt
					['0:00:00', u'16']
	part2_correct_attempt
					['0:01:54', u'C(47,2)-C(43,2)']
	part4_incorrect_attempt
					('0:03:01', u'(16+178+1081)/ C(47,2)')
	part4_correct_attempt
					['0:03:23', u'(16+178)/ C(47,2)']

12 Student ID:akhmelni

	first_attempt
					2015-10-22 22:24:10
	part1_correct_attempt
					['0:00:00', u'16']
	part2_correct_attempt
					['0:04:45', u'12/2 + (2*4*43)/2']
	part3_correct_attempt
					['0:05:32', u'C(47,2)']
	part4_incorrect_attempt
					('0:06:56', u'(16+12/2 + (2*4*43)/2+C(47,2))/C(47,2)')
	part4_correct_attempt
					['0:07:31', u'(16+C(47,2)-C(43,2))/C(47,2)']

13 Student ID:aakumar

	first_attempt
					2015-10-19 07:10:07
	part1_correct_attempt
					['0:00:00', u'16']
	part2_correct_attempt
					['15:37:19', u'C(47,2)-C(43,2)']
	part3_correct_attempt
					['15:37:44', u'C(47,2)']
	part4_incorrect_attempt
					('15:38:07', u'[16+C(52,5)-C(40,5)]/C(47,2)')
	part4_correct_attempt
					['15:38:27', u'[16+C(47,2)-C(43,2)]/C(47,2)']

14 Student ID:pthsu

	first_attempt
					2015-10-17 00:04:32
	part1_correct_attempt
					['0:00:00', u'4^2']
	part2_correct_attempt
					['0:00:00', u'C(52-5,2)-C(52-5-4,2)']
	part3_correct_attempt
					['0:00:00', u'C(47,2)']
	part4_incorrect_attempt
					('0:00:10', u'C(52-5,2)-C(52-5-4,2)+4^2/C(52-5,2)')
	part4_correct_attempt
					['0:00:26', u'(C(52-5,2)-C(52-5-4,2)+4^2)/C(52-5,2)']

15 Student ID:hah008

	first_attempt
					2015-10-21 19:50:40
	part1_correct_attempt
					['0:00:00', u'4^2']
	part2_correct_attempt
					['0:00:39', u'C(47,2) - C(43,2)']
	part3_correct_attempt
					['0:01:17', u'C(47,2)']
	part4_incorrect_attempt
					('0:02:01', u'C(47,2) - C(43,2) / C(47,2)')
					('0:02:10', u'C(47,2) - C(43,2) + 16 / C(47,2)')
					('0:02:18', u'C(47,2) - (C(43,2) + 16) / C(47,2)')
	part4_correct_attempt
					['0:09:33', u'((C(47,2) - C(43,2)) + 16) / C(47,2)']

16 Student ID:arc013

	first_attempt
					2015-10-21 10:22:18
	part1_correct_attempt
					['0:00:00', u'16']
	part2_correct_attempt
					['0:01:22', u'C(47,2)-C(43,2)']
	part3_correct_attempt
					['0:02:33', u'C(47, 2)']
	part4_incorrect_attempt
					('0:03:12', u'16+C(47,2)-C(43,2)')
	part4_correct_attempt
					['0:03:37', u'(16+C(47,2)-C(43,2))/C(47,2)']

17 Student ID:edcole

	first_attempt
					2015-10-21 17:55:44
	part1_correct_attempt
					['0:00:00', u'4*4']
	part2_correct_attempt
					['0:06:29', u'C(47, 2) - C(43, 2)']
	part3_correct_attempt
					['0:07:11', u'C(47, 2)']
	part4_incorrect_attempt
					('0:07:46', u'(C(47, 2) - C(43, 2))/C(47, 2)')
	part4_correct_attempt
					['0:08:13', u'(16 + C(47, 2) - C(43, 2))/C(47, 2)']

18 Student ID:aordookh

	first_attempt
					2015-10-22 05:42:46
	part1_correct_attempt
					['0:00:00', u'C(47,2)-(C(47,2)-16)']
	part2_correct_attempt
					['0:00:00', u'C(47,2)-C(43,2)']
	part3_correct_attempt
					['0:00:48', u'C(47,2)']
	part4_incorrect_attempt
					('0:01:53', u'C(47,2)-(C(47,2)-16)+C(47,2)-C(43,2)/C(47,2)')
	part4_correct_attempt
					['0:02:11', u'(C(47,2)-(C(47,2)-16)+C(47,2)-C(43,2))/C(47,2)']

19 Student ID:zhz159

	first_attempt
					2015-10-22 01:41:35
	part1_correct_attempt
					['0:00:00', u'16']
	part2_correct_attempt
					['1:52:28', u'178']
	part3_correct_attempt
					['0:10:41', u'1081']
	part4_incorrect_attempt
					('1:52:28', u'0.1646623')
					('1:53:00', u'0.1776133')
	part4_correct_attempt
					['1:53:42', u'0.179463']

20 Student ID:mitopete

	first_attempt
					2015-10-21 03:05:21
	part1_correct_attempt
					['0:00:00', u'16']
	part2_correct_attempt
					['-1 day, 22:56:27', u'C(47,2)']
	part4_incorrect_attempt
					('0:01:14', u'16+C(47,2)-C(43,2)/C(47,2)')
	part4_correct_attempt
					['0:01:37', u'(16+(C(47,2)-C(43,2)))/C(47,2)']

21 Student ID:kosung

	first_attempt
					2015-10-22 22:39:12
	part1_correct_attempt
					['0:00:00', u'C(4,1)*C(4,1) ']
	part2_correct_attempt
					['0:37:35', u'178']
	part3_correct_attempt
					['0:33:00', u'C(47,2)']
	part4_incorrect_attempt
					('0:37:35', u'182/1081')
	part4_correct_attempt
					['0:37:44', u'194/1081']

22 Student ID:j2phung

	first_attempt
					2015-10-22 05:37:39
	part1_correct_attempt
					['0:00:00', u'16']
	part2_correct_attempt
					['-1 day, 23:17:24', u'(47!/(2!45!)) - (43!/(2!41!))']
	part3_correct_attempt
					['-1 day, 22:59:09', u'47!/(2!45!)']
	part4_incorrect_attempt
					('0:02:16', u'(16)+((47!/(2!45!)) - (43!/(2!41!)))/(47!/(2!45!))')
	part4_correct_attempt
					['0:02:35', u'((16)+((47!/(2!45!)) - (43!/(2!41!))))/(47!/(2!45!))']












