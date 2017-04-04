#Problem 6

    $n=random(10,20,1);
    $ans = Formula("$n*($n-1)*($n-2)");

    #### Sampling with and without replacement when the order matters ####
    Suppose there are four children---Alice, Bill, Christie, and Doug---at an animal
    shelter, checking out the current pool of [`n`] dogs. Each child writes down the
    name of the dog he or she likes most. How many possible outcomes are there?

    We can represent each outcome as a 4-tuple (Alice's choice, Bill's choice,
    Christie's choice, Doug's choice) in which each entry is the name of a dog.
    So the number of outcomes is [`n^4`]

    Now suppose that these same children are actually picking out dogs. First Alice
    chooses a dog to adopt, then Bill chooses a dog to adopt, and so on. How many
    outcomes are there now?

    In this situation, Alice has [`n`] choices, but Bill has only [`n-1`] choices,
    Christie has [`n-2`] choices, and Doug has [`n-3`] choices. So there are [`n(n-1)(n-2)(n-3)`] possible outcomes.

    The first situation is called _sampling with replacement_: the
    outcomes are tuples in which the same element (dog) can occur more
    than once. The number of such [`k`] tuples, chosen from [`n`] elements, is [`n^k`]  In the example, [`k=4`]  The second situation is _sampling
      without replacement_: the outcomes are tuples in which no element
    can be repeated. The number of such [`k`] tuples, chosen from [`n`] elements, is [`n(n-1)(n-2) \cdots (n-k+1)`]

    Here's a related question: how many ways are there to order (shuffle)
    a deck of 52 cards?  (Each such ordering is called a _permutation_
    of the cards.) Well, the result is a 52-tuple, drawn from a set of
    size 52, in which no card is repeated. Therefore, the number of
    permutations is [`52 \cdot 51 \cdot 50 \cdots 1`]  which is called [`52 `]     _factorial_ and denoted as [`52!`]  More generally, the number of permutations of [`n`] elements is [`n`] factorial or [`n!`]

    To Rcap, how many ways are there to order 10 elements? [_____]{"10!"} (you can use expressions such as 3*2 and 7! in your answer).

    Coming back to sampling [`k`] out of [`n`] elements without replacement,
    we can write it succinctly as
    [``
    n(n-1)(n-2) \cdots (n-k+1) = \frac{n!}{(n-k)!}
    ``]

    *Question:*
    Suppose you have a deck with [$n] different cards. (*Copy* the number
    of cards here [__]{$n}) How many ways are there to choose 3 cards out
    of this deck? (the order of the 3 picked out cards _does_ matter)
    o [_____________]{"$n!/($n-3)!"} (Note: You don't have to perform the
    calculation, you can instead use the notation for factorial [`n!`] in
    your answer).



## Part 1

### (4) Mistake Group Digits of size 4




### (2) Mistake Group ['R.0'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|10!	|10^10	|[('R.0', 10.0, u'10', u'10')]	|
|1	|10!	|P(10,10)	|[('R.0', 10.0, u'10', u'10')]	|




### (0) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|












## Part 2

### (10) Mistake Group Digits of size 10




### (3) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:aadhakal

	first_attempt
					2015-10-12 06:35:51
	part2_incorrect_attempt
					('0:00:20', u'10!/7!')
	part2_correct_attempt
					['0:00:49', u'10']

1 Student ID:jag028

	first_attempt
					2015-10-14 23:12:17
	part2_incorrect_attempt
					('0:05:32', u'19!')
	part2_correct_attempt
					['0:14:06', u'19']

2 Student ID:acs008

	first_attempt
					2015-10-14 21:47:07
	part2_incorrect_attempt
					('0:00:14', u'16!')
					('0:01:28', u'16*15*14')
	part2_correct_attempt
					['0:01:54', u'16']












## Part 3

### (75) Mistake Group ['R.0'] of size 75
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|20!/(20-3)!	|20!/(3!*17!)	|[('R.0', 2432902008176640000, u'20!', u'20!')]	|
|1	|19!/(19-3)!	|19! / (16! * 3!)	|[('R.0', 121645100408832000, u'19!', u'19!')]	|
|2	|15!/(15-3)!	|15!/[3!*12!]	|[('R.0', 1307674368000, u'15!', u'15!')]	|
|3	|11!/(11-3)!	|11!/ [(8!)(3!)]	|[('R.0', 39916800, u'11!', u'11!')]	|
|4	|10!/(10-3)!	|10! / (3! * 7!)	|[('R.0', 3628800, u'10!', u'10!')]	|
|5	|16!/(16-3)!	|16!/(3!*13!)	|[('R.0', 20922789888000, u'16!', u'16!')]	|
|6	|19!/(19-3)!	|19!/3!	|[('R.0', 121645100408832000, u'19!', u'19!')]	|
|7	|19!/(19-3)!	|19!/(16!*3!)	|[('R.0', 121645100408832000, u'19!', u'19!')]	|
|8	|18!/(18-3)!	|18!/[(18-3)!3!]	|[('R.0', 6402373705728000, u'18!', u'18!')]	|
|9	|20!/(20-3)!	|20!/(17!*3!)	|[('R.0', 2432902008176640000, u'20!', u'20!')]	|
|10	|14!/(14-3)!	|14!/7!	|[('R.0', 87178291200, u'14!', u'14!')]	|
|11	|14!/(14-3)!	|14!/10!	|[('R.0', 87178291200, u'14!', u'14!')]	|
|12	|12!/(12-3)!	|12!/(3!*(12-3)!)	|[('R.0', 479001600, u'12!', u'12!')]	|
|13	|14!/(14-3)!	|14!/[3![14-3]!]	|[('R.0', 87178291200, u'14!', u'14!')]	|
|14	|14!/(14-3)!	|14!/[3!*([14-3]!)]	|[('R.0', 87178291200, u'14!', u'14!')]	|
|15	|14!/(14-3)!	|14!/3!	|[('R.0', 87178291200, u'14!', u'14!')]	|
|16	|15!/(15-3)!	|15!/(3!12!)	|[('R.0', 1307674368000, u'15!', u'15!')]	|
|17	|17!/(17-3)!	|17!/(14!*6)	|[('R.0', 355687428096000, u'17!', u'17!')]	|
|18	|17!/(17-3)!	|(17!)/(14!*3!)	|[('R.0', 355687428096000, u'17!', u'17!')]	|
|19	|17!/(17-3)!	|(17!)/3!	|[('R.0', 355687428096000, u'17!', u'17!')]	|
|20	|16!/(16-3)!	|16!/3!	|[('R.0', 20922789888000, u'16!', u'16!')]	|
|21	|14!/(14-3)!	|14!/(11!(3!))	|[('R.0', 87178291200, u'14!', u'14!')]	|
|22	|14!/(14-3)!	|(14!)/(3!(11!))	|[('R.0', 87178291200, u'14!', u'14!')]	|
|23	|20!/(20-3)!	|(20!)/(3!)	|[('R.0', 2432902008176640000, u'20!', u'20!')]	|
|24	|20!/(20-3)!	|(20!)/((3!)(17!))	|[('R.0', 2432902008176640000, u'20!', u'20!')]	|
|25	|15!/(15-3)!	|15!/(3!*12!)	|[('R.0', 1307674368000, u'15!', u'15!')]	|
|26	|11!/(11-3)!	|(11!)/(3!*8!)	|[('R.0', 39916800, u'11!', u'11!')]	|
|27	|11!/(11-3)!	|(11!)/(3!)	|[('R.0', 39916800, u'11!', u'11!')]	|
|28	|11!/(11-3)!	|(11!)/(11-3!)	|[('R.0', 39916800, u'11!', u'11!')]	|
|29	|12!/(12-3)!	|12!/3!	|[('R.0', 479001600, u'12!', u'12!')]	|
|30	|12!/(12-3)!	|12!/(3!*9!)	|[('R.0', 479001600, u'12!', u'12!')]	|
|31	|11!/(11-3)!	|11!/(3!8!)	|[('R.0', 39916800, u'11!', u'11!')]	|
|32	|20!/(20-3)!	|20!/3!	|[('R.0', 2432902008176640000, u'20!', u'20!')]	|
|33	|13!/(13-3)!	|13!/(10!3!)	|[('R.0', 6227020800, u'13!', u'13!')]	|
|34	|12!/(12-3)!	|12!/(3!9!)	|[('R.0', 479001600, u'12!', u'12!')]	|
|35	|12!/(12-3)!	|12!/(3!)	|[('R.0', 479001600, u'12!', u'12!')]	|
|36	|17!/(17-3)!	|17!/((17)(16)(15))	|[('R.0', 355687428096000, u'17!', u'17!')]	|
|37	|14!/(14-3)!	|14!/(3!11!)	|[('R.0', 87178291200, u'14!', u'14!')]	|
|38	|16!/(16-3)!	|16! / ((13!)(3!))	|[('R.0', 20922789888000, u'16!', u'16!')]	|
|39	|10!/(10-3)!	|10!/(3! * 7!)	|[('R.0', 3628800, u'10!', u'10!')]	|
|40	|15!/(15-3)!	|15!/(12!3!)	|[('R.0', 1307674368000, u'15!', u'15!')]	|
|41	|15!/(15-3)!	|15!/3!	|[('R.0', 1307674368000, u'15!', u'15!')]	|
|42	|11!/(11-3)!	|11!/(7!)	|[('R.0', 39916800, u'11!', u'11!')]	|
|43	|19!/(19-3)!	|19!/(3!16!)	|[('R.0', 121645100408832000, u'19!', u'19!')]	|
|44	|19!/(19-3)!	|19!/(3!*16!)	|[('R.0', 121645100408832000, u'19!', u'19!')]	|
|45	|11!/(11-3)!	|11! / ((8!)(3!))	|[('R.0', 39916800, u'11!', u'11!')]	|
|46	|17!/(17-3)!	|17!/(15!)	|[('R.0', 355687428096000, u'17!', u'17!')]	|
|47	|17!/(17-3)!	|17!/(14!3!)	|[('R.0', 355687428096000, u'17!', u'17!')]	|
|48	|20!/(20-3)!	|(20!)/((3!)*(17!))	|[('R.0', 2432902008176640000, u'20!', u'20!')]	|
|49	|13!/(13-3)!	|13!/3!	|[('R.0', 6227020800, u'13!', u'13!')]	|
|50	|13!/(13-3)!	|13!/ (3!10!)	|[('R.0', 6227020800, u'13!', u'13!')]	|
|51	|13!/(13-3)!	|13!/ 3!	|[('R.0', 6227020800, u'13!', u'13!')]	|
|52	|10!/(10-3)!	|10!/(7!3!)	|[('R.0', 3628800, u'10!', u'10!')]	|
|53	|17!/(17-3)!	|17!/(3!)	|[('R.0', 355687428096000, u'17!', u'17!')]	|
|54	|20!/(20-3)!	|(20!)/((20-17)!)	|[('R.0', 2432902008176640000, u'20!', u'20!')]	|
|55	|17!/(17-3)!	|17!/(3!14!)	|[('R.0', 355687428096000, u'17!', u'17!')]	|
|56	|19!/(19-3)!	|19!/17!	|[('R.0', 121645100408832000, u'19!', u'19!')]	|
|57	|14!/(14-3)!	|14!/(14-3)	|[('R.0', 87178291200, u'14!', u'14!')]	|
|58	|18!/(18-3)!	|18!/(3!15!)	|[('R.0', 6402373705728000, u'18!', u'18!')]	|
|59	|18!/(18-3)!	|18!/3!	|[('R.0', 6402373705728000, u'18!', u'18!')]	|
|60	|18!/(18-3)!	|18!/(8!)	|[('R.0', 6402373705728000, u'18!', u'18!')]	|
|61	|15!/(15-3)!	|15!/ (3! * 12!)	|[('R.0', 1307674368000, u'15!', u'15!')]	|
|62	|11!/(11-3)!	|11! / ( 3! * 8!)	|[('R.0', 39916800, u'11!', u'11!')]	|
|63	|20!/(20-3)!	|20!/(17!3!)	|[('R.0', 2432902008176640000, u'20!', u'20!')]	|
|64	|16!/(16-3)!	|(16!)/[(3!)(12!)]	|[('R.0', 20922789888000, u'16!', u'16!')]	|
|65	|16!/(16-3)!	|(16!)/[(3!)(13!)]	|[('R.0', 20922789888000, u'16!', u'16!')]	|
|66	|13!/(13-3)!	|13!/(13-3)	|[('R.0', 6227020800, u'13!', u'13!')]	|




### (11) Mistake Group Fraction of size 11




### (10) Mistake Group Digits of size 10




### (4) Mistake Group redirect of size 4




### (4) Mistake Group ['R.1'] of size 4
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|20!/(20-3)!	|20!/3!*17!	|[('R.1', 355687428096000, u'(20-3)!', u'17!')]	|
|1	|12!/(12-3)!	|12!/3!*9!	|[('R.1', 362880, u'(12-3)!', u'9!')]	|
|2	|18!/(18-3)!	|13!(15!)	|[('R.1', 1307674368000, u'(18-3)!', u'15!')]	|
|3	|18!/(18-3)!	|18!/3!15!	|[('R.1', 1307674368000, u'(18-3)!', u'15!')]	|




### (1) Mistake Group ['R.0', 'R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|19!/(19-3)!	|19!((19-3)!)	|[('R.0', 121645100408832000, u'19!', u'19!'), ('R.1', 20922789888000, u'(19-3)!', u'(19-3)!')]	|




### (1) Mistake Group ['R.1.0.0'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|13!/(13-3)!	|C(10,3)13!/(10!3!)	|[('R.1.0.0', 13.0, u'13', u'13')]	|




### (51) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:agoldsht

	first_attempt
					2015-10-14 01:35:45
	part1_correct_attempt
					['0:00:00', u'10!']
	part2_correct_attempt
					['0:01:21', u'15']
	part3_incorrect_attempt
					('0:01:21', u'10!/(7!3!)')
	part3_correct_attempt
					['0:29:26', u'15!/(12!)']

1 Student ID:dis003

	first_attempt
					2015-10-15 10:44:21
	part1_correct_attempt
					['0:00:00', u'10!']
	part2_correct_attempt
					['0:00:00', u'18']
	part3_incorrect_attempt
					('0:00:00', u'C(18,3)')
	part3_correct_attempt
					['0:00:22', u'18!/(18-3)!']

2 Student ID:vsamant

	first_attempt
					2015-10-10 00:33:46
	part1_correct_attempt
					['0:00:00', u'10!']
	part2_correct_attempt
					['0:00:00', u'20']
	part3_incorrect_attempt
					('0:00:00', u'C(20,3)')
	part3_correct_attempt
					['0:01:34', u'20!/(20-3)!']

3 Student ID:kalang

	first_attempt
					2015-10-11 23:33:42
	part1_correct_attempt
					['0:00:00', u'10!']
	part2_correct_attempt
					['0:00:00', u'19']
	part3_incorrect_attempt
					('0:00:00', u'C(19,3)')
	part3_correct_attempt
					['0:00:25', u'19!/(16!)']

4 Student ID:lguintu

	first_attempt
					2015-10-09 20:58:55
	part1_correct_attempt
					['0:00:00', u'10!']
	part2_correct_attempt
					['0:00:00', u'12']
	part3_incorrect_attempt
					('0:00:00', u'3!')
	part3_correct_attempt
					['0:00:21', u'12!/9!']

5 Student ID:c1sorian

	first_attempt
					2015-10-14 21:51:52
	part1_correct_attempt
					['0:00:00', u'10!']
	part2_correct_attempt
					['0:00:27', u'10']
	part3_incorrect_attempt
					('0:00:27', u'10!/7!3!')
	part3_correct_attempt
					['0:01:35', u'10!/(7!)']

6 Student ID:ewbrenna

	first_attempt
					2015-10-12 19:27:38
	part1_correct_attempt
					['0:00:00', u'10!']
	part2_correct_attempt
					['0:00:00', u'19']
	part3_incorrect_attempt
					('0:00:35', u'(19!((19-3)!))*3!')
	part3_correct_attempt
					['0:00:57', u'19!/((19-3)!)']

7 Student ID:masaro

	first_attempt
					2015-10-10 00:06:52
	part1_correct_attempt
					['0:00:00', u'10!']
	part2_correct_attempt
					['0:00:00', u'15']
	part3_incorrect_attempt
					('0:00:00', u'C(15,3)')
	part3_correct_attempt
					['0:02:35', u'6*(15!/[3!*12!])']

8 Student ID:anislam

	first_attempt
					2015-10-15 08:46:37
	part1_correct_attempt
					['0:00:00', u'10!']
	part2_correct_attempt
					['0:00:00', u'18']
	part3_incorrect_attempt
					('0:00:00', u'C(18,3)')
	part3_correct_attempt
					['0:00:44', u'18!/15!']

9 Student ID:mitopete

	first_attempt
					2015-10-13 17:14:22
	part1_correct_attempt
					['0:00:00', u'10!']
	part2_correct_attempt
					['0:00:00', u'19']
	part3_incorrect_attempt
					('0:03:40', u'19^3')
	part3_correct_attempt
					['0:04:21', u'19!/((19-3)!)']

10 Student ID:pcdo

	first_attempt
					2015-10-13 18:10:44
	part1_correct_attempt
					['0:00:00', u'10!']
	part2_correct_attempt
					['0:00:00', u'17']
	part3_incorrect_attempt
					('0:00:00', u'C(17,3)')
	part3_correct_attempt
					['0:00:25', u'17!/(17-3)!']

11 Student ID:t2li

	first_attempt
					2015-10-14 03:15:43
	part1_correct_attempt
					['0:00:00', u'10!']
	part2_correct_attempt
					['0:00:50', u'18']
	part3_incorrect_attempt
					('0:01:09', u'C(18,3)')
	part3_correct_attempt
					['0:02:30', u'18!/(15!)']

12 Student ID:alhung

	first_attempt
					2015-10-15 18:39:56
	part1_correct_attempt
					['0:00:00', u'10!']
	part2_correct_attempt
					['0:00:00', u'13']
	part3_incorrect_attempt
					('0:00:00', u'C(13,3)')
	part3_correct_attempt
					['0:01:17', u'(13!)/[(13-3)!]']

13 Student ID:jag028

	first_attempt
					2015-10-14 23:12:17
	part1_correct_attempt
					['0:00:00', u'10!']
	part2_correct_attempt
					['0:14:06', u'19']
	part3_incorrect_attempt
					('0:15:39', u'19!18!17!')
					('0:15:53', u'19*18*17!')
	part3_correct_attempt
					['0:15:59', u'19*18*17']

14 Student ID:amquinte

	first_attempt
					2015-10-12 19:35:57
	part1_correct_attempt
					['0:00:00', u'10!']
	part2_correct_attempt
					['0:00:00', u'16']
	part3_incorrect_attempt
					('0:00:00', u'16!15!14!')
					('0:04:29', u'16!15!14!')
	part3_correct_attempt
					['0:04:43', u'16(15)(14)']

15 Student ID:j6quach

	first_attempt
					2015-10-09 05:05:15
	part1_correct_attempt
					['0:00:00', u'10!']
	part2_correct_attempt
					['0:00:00', u'15']
	part3_incorrect_attempt
					('0:00:00', u'P(10,3)')
					('0:00:10', u'10!/7!')
	part3_correct_attempt
					['0:00:25', u'15!/12!']

16 Student ID:gsrandha

	first_attempt
					2015-10-12 06:46:12
	part1_correct_attempt
					['0:00:00', u'10!']
	part2_correct_attempt
					['0:00:06', u'15']
	part3_incorrect_attempt
					('0:00:57', u'15^3')
	part3_correct_attempt
					['0:01:27', u'15*14*13']

17 Student ID:jyc018

	first_attempt
					2015-10-12 01:38:59
	part1_correct_attempt
					['0:00:00', u'10!']
	part2_correct_attempt
					['0:01:02', u'15']
	part3_incorrect_attempt
					('0:01:02', u'52!/(49!)')
	part3_correct_attempt
					['0:01:46', u'15!/(12!)']

18 Student ID:bmilton

	first_attempt
					2015-10-09 22:49:54
	part1_correct_attempt
					['0:00:00', u'10!']
	part2_correct_attempt
					['0:00:00', u'19']
	part3_incorrect_attempt
					('0:00:00', u'C(19,3)')
	part3_correct_attempt
					['0:00:31', u'19! / 16!']

19 Student ID:jnatale

	first_attempt
					2015-10-15 03:10:19
	part1_correct_attempt
					['0:00:00', u'10!']
	part2_correct_attempt
					['0:00:00', u'16']
	part3_incorrect_attempt
					('0:00:00', u'52*51*50')
	part3_correct_attempt
					['0:00:15', u'16*15*14']

20 Student ID:jew037

	first_attempt
					2015-10-14 04:41:33
	part1_correct_attempt
					['0:00:00', u'10!']
	part3_incorrect_attempt
					('0:00:10', u'3!')
	part3_correct_attempt
					['0:00:23', u'990']

21 Student ID:rsmurlo

	first_attempt
					2015-10-13 06:08:56
	part1_correct_attempt
					['0:00:00', u'10!']
	part2_correct_attempt
					['0:00:00', u'15']
	part3_incorrect_attempt
					('0:00:00', u'15*14*14')
	part3_correct_attempt
					['0:00:13', u'15*14*13']

22 Student ID:mnrahman

	first_attempt
					2015-10-15 06:53:57
	part1_correct_attempt
					['0:00:00', u'10!']
	part2_correct_attempt
					['0:00:00', u'15']
	part3_incorrect_attempt
					('0:00:00', u'C(15,3)')
	part3_correct_attempt
					['0:00:35', u'15!/(15-3)!']

23 Student ID:jblynch

	first_attempt
					2015-10-12 06:41:39
	part1_correct_attempt
					['0:00:00', u'10!']
	part2_correct_attempt
					['0:00:00', u'14']
	part3_incorrect_attempt
					('0:00:00', u'C(14,4)')
	part3_correct_attempt
					['0:00:25', u'14!/(14-3)!']

24 Student ID:akhmelni

	first_attempt
					2015-10-15 22:05:42
	part1_correct_attempt
					['0:00:00', u'10!']
	part2_correct_attempt
					['0:00:24', u'17']
	part3_incorrect_attempt
					('0:00:24', u'3!')
	part3_correct_attempt
					['0:00:54', u'(17!)/(17-3)!']

25 Student ID:tol003

	first_attempt
					2015-10-13 23:08:51
	part1_correct_attempt
					['0:00:00', u'10!']
	part2_correct_attempt
					['0:00:00', u'16']
	part3_incorrect_attempt
					('0:00:00', u'16!')
	part3_correct_attempt
					['0:01:03', u'16!/(16-3)!']

26 Student ID:jcl084

	first_attempt
					2015-10-13 20:06:08
	part1_correct_attempt
					['0:00:00', u'10!']
	part2_correct_attempt
					['0:00:19', u'13']
	part3_incorrect_attempt
					('0:00:19', u'13!/10!3!')
	part3_correct_attempt
					['0:01:57', u'13!/(13-3)!']

27 Student ID:jhw015

	first_attempt
					2015-10-13 07:47:13
	part1_correct_attempt
					['0:00:00', u'10!']
	part2_correct_attempt
					['0:00:11', u'11']
	part3_incorrect_attempt
					('0:00:26', u'C(11,3)')
	part3_correct_attempt
					['0:00:50', u'11!/8!']

28 Student ID:dsmonaha

	first_attempt
					2015-10-13 16:53:08
	part1_correct_attempt
					['0:00:00', u'10!']
	part2_correct_attempt
					['0:00:00', u'17']
	part3_incorrect_attempt
					('0:00:00', u'C(17,3)')
					('0:00:14', u'17!16!15!')
					('0:00:23', u'17!')
	part3_correct_attempt
					['0:01:31', u'17!/14!']

29 Student ID:z3meng

	first_attempt
					2015-10-15 02:20:04
	part1_correct_attempt
					['0:00:00', u'10!']
	part2_correct_attempt
					['0:00:00', u'12']
	part3_incorrect_attempt
					('0:00:16', u'3!')
	part3_correct_attempt
					['0:00:35', u'12*11*10']

30 Student ID:hah008

	first_attempt
					2015-10-13 02:23:04
	part1_correct_attempt
					['0:00:00', u'10!']
	part2_correct_attempt
					['0:00:00', u'12']
	part3_incorrect_attempt
					('0:00:28', u'12!/9!3!')
					('0:01:13', u'C(12,3)')
	part3_correct_attempt
					['0:08:15', u'12*11*10']

31 Student ID:abasu

	first_attempt
					2015-10-11 01:23:04
	part1_correct_attempt
					['0:00:00', u'10!']
	part2_correct_attempt
					['0:00:00', u'15']
	part3_incorrect_attempt
					('0:00:00', u'(15!*14!*13!)')
	part3_correct_attempt
					['0:01:06', u'15*14*13']

32 Student ID:mcatozzi

	first_attempt
					2015-10-13 22:56:39
	part1_correct_attempt
					['0:00:00', u'10*9*8*7*6*5*4*3*2']
	part2_correct_attempt
					['0:01:55', u'16']
	part3_incorrect_attempt
					('0:01:55', u'C(16,3)')
	part3_correct_attempt
					['0:06:59', u'16!/13!']

33 Student ID:eaherman

	first_attempt
					2015-10-13 18:31:00
	part1_correct_attempt
					['0:00:00', u'10!']
	part2_correct_attempt
					['0:00:00', u'16']
	part3_incorrect_attempt
					('0:00:00', u'C(16,3)')
	part3_correct_attempt
					['0:01:15', u'16!/(16-3)!']

34 Student ID:tcuddy

	first_attempt
					2015-10-10 18:38:01
	part1_correct_attempt
					['0:00:00', u'10!']
	part2_correct_attempt
					['0:00:00', u'15']
	part3_incorrect_attempt
					('0:00:00', u'10!/7!')
	part3_correct_attempt
					['0:00:11', u'15!/12!']

35 Student ID:etemlock

	first_attempt
					2015-10-09 20:55:23
	part1_correct_attempt
					['0:00:00', u'10!']
	part2_correct_attempt
					['0:00:00', u'10']
	part3_incorrect_attempt
					('0:00:00', u'C(10,3)')
	part3_correct_attempt
					['0:00:36', u'10!/(10-3)!']

36 Student ID:dpereira

	first_attempt
					2015-10-10 05:32:42
	part1_correct_attempt
					['0:00:00', u'10!']
	part2_correct_attempt
					['0:00:00', u'10']
	part3_incorrect_attempt
					('0:00:00', u'C(10,3)')
	part3_correct_attempt
					['0:00:46', u'10! / 7!']

37 Student ID:haliew

	first_attempt
					2015-10-13 17:24:11
	part1_correct_attempt
					['0:00:00', u'10!']
	part2_correct_attempt
					['0:00:00', u'16']
	part3_incorrect_attempt
					('0:00:00', u'C(16,3)')
	part3_correct_attempt
					['0:00:16', u'16!/(16-3)!']

38 Student ID:nisharma

	first_attempt
					2015-10-14 17:45:27
	part1_correct_attempt
					['0:00:00', u'10!']
	part2_correct_attempt
					['0:00:14', u'17']
	part3_incorrect_attempt
					('0:00:30', u'C (17,3)')
	part3_correct_attempt
					['0:01:53', u'17!/(14!)']

39 Student ID:csl030

	first_attempt
					2015-10-13 22:48:44
	part1_correct_attempt
					['0:00:00', u'10!']
	part2_correct_attempt
					['0:00:00', u'14']
	part3_incorrect_attempt
					('0:00:00', u'C(14,3)')
	part3_correct_attempt
					['0:01:10', u'14!/(14 - 3)!']

40 Student ID:arc013

	first_attempt
					2015-10-13 01:56:12
	part1_correct_attempt
					['0:00:00', u'10!']
	part2_correct_attempt
					['0:00:24', u'15']
	part3_incorrect_attempt
					('0:00:43', u'C(15,3)')
	part3_correct_attempt
					['0:01:24', u'15*14*13']

41 Student ID:qfu

	first_attempt
					2015-10-09 04:02:55
	part1_correct_attempt
					['0:00:00', u'10!']
	part2_correct_attempt
					['0:00:00', u'15']
	part3_incorrect_attempt
					('0:00:00', u'C(15,3)')
					('0:00:39', u'(15*14*13)/3!')
	part3_correct_attempt
					['0:01:48', u'15*14*13']

42 Student ID:aportuga

	first_attempt
					2015-10-13 22:29:11
	part1_correct_attempt
					['0:00:00', u'10!']
	part2_correct_attempt
					['0:00:00', u'17']
	part3_incorrect_attempt
					('0:04:23', u'17!/(17)(16)(15)')
					('0:04:48', u'14!')
	part3_correct_attempt
					['0:05:46', u'17!/14!']

43 Student ID:syip

	first_attempt
					2015-10-10 19:53:08
	part1_correct_attempt
					['0:00:00', u'10!']
	part2_correct_attempt
					['0:00:00', u'19']
	part3_incorrect_attempt
					('0:00:00', u'C(19,3)')
	part3_correct_attempt
					['0:00:22', u'19*18*17']

44 Student ID:dac064

	first_attempt
					2015-10-15 19:20:03
	part1_correct_attempt
					['0:00:00', u'10!']
	part2_correct_attempt
					['0:00:00', u'11']
	part3_incorrect_attempt
					('0:00:00', u'C(11,3)')
	part3_correct_attempt
					['0:00:51', u'11! / ( 8!)']

45 Student ID:jmiclat

	first_attempt
					2015-10-15 02:47:13
	part1_correct_attempt
					['0:00:00', u'10!']
	part2_correct_attempt
					['0:00:00', u'17']
	part3_incorrect_attempt
					('0:00:00', u'17!/3!15!')
	part3_correct_attempt
					['0:00:39', u'17!/(14!)']

46 Student ID:srl006

	first_attempt
					2015-10-10 03:59:28
	part1_correct_attempt
					['0:00:00', u'10!']
	part2_correct_attempt
					['0:00:19', u'11']
	part3_incorrect_attempt
					('0:00:19', u'C(11,3)')
					('0:00:50', u'11!/ (8!)(3!)')
	part3_correct_attempt
					['0:01:56', u'990']

47 Student ID:akg009

	first_attempt
					2015-10-15 21:29:51
	part1_correct_attempt
					['0:00:00', u'10!']
	part2_correct_attempt
					['0:00:00', u'16']
	part3_incorrect_attempt
					('0:00:00', u'(16!)/(3!)(12!)')
	part3_correct_attempt
					['0:05:12', u'(16!)/[(13!)]']

48 Student ID:sthapa

	first_attempt
					2015-10-15 04:07:20
	part1_correct_attempt
					['0:00:00', u'10!']
	part2_correct_attempt
					['0:00:31', u'12']
	part3_incorrect_attempt
					('0:01:02', u'10!/7!')
	part3_correct_attempt
					['0:01:15', u'12!/9!']

49 Student ID:whcombs

	first_attempt
					2015-10-12 23:43:22
	part1_correct_attempt
					['0:00:00', u'10!']
	part2_correct_attempt
					['0:00:00', u'14']
	part3_incorrect_attempt
					('0:00:00', u'C(14,3)')
	part3_correct_attempt
					['0:00:41', u'14!/(14-3)!']

50 Student ID:asp025

	first_attempt
					2015-10-13 06:44:50
	part1_correct_attempt
					['0:00:00', u'10!']
	part2_correct_attempt
					['0:01:41', u'13']
	part3_incorrect_attempt
					('0:01:41', u'13!')
	part3_correct_attempt
					['0:02:15', u'13*12*11']












