#Problem 3

    $r = random(0.4,0.6,0.1);
    $k = random(100,200,1);
    $p = random($r+0.1,0.9,0.1);
    $n2 = random(300,500,1);
    $k2 = random(251,299,1);
    $ans1 = ceil($p*$k/$r);

    ### Markov's Inequality
    Markov's inequality relate probabilities to expectations, and provide bounds for the cumulative distribution function of a random variable.
    The Markov's inequality is stated as follow:

    If X is any nonnegative random variable and a > 0, then  [`\mathbb{P}(X \geq a) \leq \frac{\mathbb{E}(X)}{a}`]
    ---
    John has a biased coin with [`P(\mathrm{heads}) = [$r]`].
    He tosses this coin [`N`] times and, out of the [`N`] times,
    the coin lands on heads [$k] times.
    Using Markov's inequality that he learned from CSE103,
    he says that the probabality of seeing at least this many
    heads is at most [$p].

    o Give the best lower bound, using Markov inequality, on the number of times John tossed the coin?
    [`N`] = [____________]{Compute("$p*$k/$r")}
    (Provide the exact answer, don't round it to the next larger integer number.)

    Suppose John lends you this coin. If you flip the coin [$n2] times,
    what is the upper bound of the probability of seeing at least [$k2] heads
    using Markov's inequality?

    o [`P(\mbox{Number of heads} > [$k2])`] [`\le`] [____________]{Compute("$n2*$r/$k2")->with(tolType=>'absolute', tolerance=>'0.01')}




## Part 1

### (61) Mistake Group Digits of size 61




### (35) Mistake Group Fraction of size 35




### (4) Mistake Group ['R.1'] of size 4
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|0.9*183/0.4	|183/.4	|[('R.1', 0.4, u'0.4', u'.4')]	|
|1	|0.6*197/0.4	|197*0.4	|[('R.1', 0.4, u'0.4', u'0.4')]	|
|2	|0.6*197/0.4	|197/0.4	|[('R.1', 0.4, u'0.4', u'0.4')]	|
|3	|0.7*115/0.4	|0.6*179/0.4	|[('R.1', 0.4, u'0.4', u'0.4')]	|




### (1) Mistake Group ['R.0', 'R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|0.9*183/0.4	|(.9*183).4	|[('R.0', 164.70000000000002, u'0.9*183', u'.9*183'), ('R.1', 0.4, u'0.4', u'.4')]	|




### (1) Mistake Group Wrong_Sign of size 1




### (1) Mistake Group ['R.0.0', 'R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|0.6*196/0.5	|(0.6)*194/0.5	|[('R.0.0', 0.6, u'0.6', u'0.6'), ('R.1', 0.5, u'0.5', u'0.5')]	|




### (31) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:h4tu

	first_attempt
					2015-10-28 01:07:54
	part1_incorrect_attempt
					('0:00:00', u'18/1')
	part1_correct_attempt
					['0:00:07', u'1/18']

1 Student ID:lywong

	first_attempt
					2015-10-28 08:09:34
	part1_incorrect_attempt
					('0:00:00', u'18/1000000000')
					('0:00:14', u'18/1000000')
	part1_correct_attempt
					['1 day, 19:43:14', u'1/18']

2 Student ID:aggouw

	first_attempt
					2015-10-27 03:24:11
	part1_incorrect_attempt
					('0:00:00', u'459*0.4/276')
					('0:00:00', u'(0.1*1000000)/0.9')
	part1_correct_attempt
					['3 days, 19:07:44', u'1/10']

3 Student ID:asetters

	first_attempt
					2015-10-26 08:04:31
	part1_incorrect_attempt
					('0:00:00', u'1- 1/1000000')
	part1_correct_attempt
					['21:00:18', u'1/18']

4 Student ID:seleon

	first_attempt
					2015-10-30 21:12:28
	part1_incorrect_attempt
					('0:00:00', u'(1/10^6)/(10/10^6)')
					('0:01:05', u'(1/1*10^6)/(10/1*10^6)')
					('0:01:23', u'(1/(1*10^6))/(10/1*(10^6))')
					('0:01:34', u'(1/(1*10^6))/(10/(1*10^6))')
					('0:03:08', u'(1/(1*10^6))/(10/(1*10^6))')
					('0:05:18', u'(1/(1*10^6)/10/(1*10^6))')
					('0:06:13', u'(1/(1*10^6))/(10/(1*10^6))')
					('0:07:03', u'(1/0.000001)/(10/0.000001)')
					('0:08:15', u'0.000001/0.00001')
					('0:08:37', u'0.1')
					('0:09:51', u'(1/(1*10^6))')
					('0:10:07', u'(1/(1*10^6))/(10/(1*10^6))')
					('0:10:39', u'1/(1*10^6)')
					('0:11:17', u'(1/(1*10^6)/(10/(1*10^6)))')
					('0:11:46', u'(1/(1*10^6))/(10/(1*10^6))')
					('0:13:44', u'(10/(1*10^6))/(1/(1*10^6))')
					('0:15:12', u'(12/(1*10^6))/(1/(1*10^6))')
	part1_correct_attempt
					['0:15:29', u'(1/(1*10^6))/(12/(1*10^6))']

5 Student ID:atorr

	first_attempt
					2015-10-29 06:33:09
	part1_incorrect_attempt
					('0:00:00', u'14/1000000')
					('0:00:12', u'1/1000000')
					('0:00:00', u'14/(10^6)')
	part1_correct_attempt
					['11:49:17', u'1/14']

6 Student ID:any027

	first_attempt
					2015-10-26 03:31:21
	part1_incorrect_attempt
					('0:00:00', u'14 / 1000000')
	part1_correct_attempt
					['0:02:58', u'( 1000000/ 14000000)']

7 Student ID:s1powers

	first_attempt
					2015-10-25 21:04:16
	part1_incorrect_attempt
					('0:00:00', u'14/1')
	part1_correct_attempt
					['0:00:55', u'1/14']

8 Student ID:jcj006

	first_attempt
					2015-10-28 21:30:36
	part1_incorrect_attempt
					('0:00:00', u'(1/1000000)/(1/13000000)')
	part1_correct_attempt
					['0:01:22', u'1/((1/1000000)/(1/13000000))']

9 Student ID:beyounge

	first_attempt
					2015-10-23 05:01:27
	part1_incorrect_attempt
					('0:00:00', u'1940/4')
	part1_correct_attempt
					['4 days, 12:09:08', u'1/13']

10 Student ID:j5phung

	first_attempt
					2015-10-23 08:52:18
	part1_incorrect_attempt
					('0:00:00', u'197*0.6')
					('0:01:35', u'197/0.6')
					('0:03:46', u'196/0.6')
					('0:03:56', u'197/0.6')
	part1_correct_attempt
					['2 days, 9:10:11', u'1/13']

11 Student ID:tpmach

	first_attempt
					2015-10-28 06:32:47
	part1_incorrect_attempt
					('0:00:00', u'17*10^-6')
	part1_correct_attempt
					['0:00:32', u'1/17']

12 Student ID:bmilton

	first_attempt
					2015-10-25 00:40:50
	part1_incorrect_attempt
					('0:00:00', u'1/1000000')
	part1_correct_attempt
					['0:01:13', u'(1/1000000)/(19/1000000)']

13 Student ID:jew037

	first_attempt
					2015-10-28 18:19:15
	part1_incorrect_attempt
					('0:00:00', u'.05')
	part1_correct_attempt
					['1 day, 8:54:00', u'1/17']

14 Student ID:lalacson

	first_attempt
					2015-10-29 04:31:01
	part1_incorrect_attempt
					('0:00:00', u'1*17')
					('0:00:14', u'1*17*21')
	part1_correct_attempt
					['0:01:59', u'1/17']

15 Student ID:yfreund

	first_attempt
					2015-10-23 17:36:24
	part1_incorrect_attempt
					('0:00:00', u'1/16')

16 Student ID:agian

	first_attempt
					2015-10-30 22:18:41
	part1_incorrect_attempt
					('0:00:00', u'0.6*175/0.5')
					('0:38:29', u'(15+10^6)')
	part1_correct_attempt
					['0:39:48', u'.01/.15']

17 Student ID:dgunawan

	first_attempt
					2015-10-29 23:00:25
	part1_incorrect_attempt
					('0:00:00', u'10/1000000')
					('0:00:06', u'1/1000000')
					('0:23:57', u'10/1000000')
	part1_correct_attempt
					['0:28:41', u'[1/1000000]/[10/1000000]']

18 Student ID:hachrist

	first_attempt
					2015-10-26 00:36:41
	part1_incorrect_attempt
					('0:00:00', u'53/13')
					('0:00:09', u'13/53')
	part1_correct_attempt
					['0:07:39', u'1/13']

19 Student ID:t1tran

	first_attempt
					2015-10-23 06:31:50
	part1_incorrect_attempt
					('0:00:00', u'195*2')
	part1_correct_attempt
					['0:23:24', u'.7*195/.5']

20 Student ID:krkelkar

	first_attempt
					2015-10-23 05:58:24
	part1_incorrect_attempt
					('0:00:00', u'1830/4')
	part1_correct_attempt
					['0:02:48', u'(.9*183)/.4']

21 Student ID:tcuddy

	first_attempt
					2015-10-23 16:35:09
	part1_incorrect_attempt
					('0:00:00', u'.5(174)')
					('0:00:00', u'.5(174)/.9')
	part1_correct_attempt
					['1:37:00', u'1/17']

22 Student ID:aadhakal

	first_attempt
					2015-10-30 06:20:36
	part1_incorrect_attempt
					('0:00:00', u'12/1000000')
	part1_correct_attempt
					['0:00:34', u'[1/1000000]/[12/1000000]']

23 Student ID:anvan

	first_attempt
					2015-10-30 10:15:32
	part1_incorrect_attempt
					('0:00:00', u'34/52')
	part1_correct_attempt
					['0:03:06', u'1/18']

24 Student ID:muy002

	first_attempt
					2015-10-29 11:04:52
	part1_incorrect_attempt
					('0:00:00', u'15/1000000')
	part1_correct_attempt
					['0:05:45', u'1/15']

25 Student ID:dtea

	first_attempt
					2015-10-30 23:41:42
	part1_incorrect_attempt
					('0:00:00', u'(11/1000000)/(1/1000000)')
					('0:00:34', u'100-(11/1000000)/(1/1000000)')
	part1_correct_attempt
					['0:02:12', u'(1/1000000)/(11/1000000)']

26 Student ID:ralhadda

	first_attempt
					2015-10-24 01:45:09
	part1_incorrect_attempt
					('0:00:00', u'17/1')
	part1_correct_attempt
					['0:00:10', u'1/17']

27 Student ID:kquong

	first_attempt
					2015-10-28 17:52:19
	part1_incorrect_attempt
					('0:00:00', u'14000000/1000000')
	part1_correct_attempt
					['0:00:10', u'1/14']

28 Student ID:ajvanega

	first_attempt
					2015-10-23 16:30:05
	part1_incorrect_attempt
					('0:00:00', u'(401/2)/299')
	part1_correct_attempt
					['6 days, 23:52:11', u'1/16']

29 Student ID:akg009

	first_attempt
					2015-10-30 20:06:16
	part1_incorrect_attempt
					('0:00:00', u'11/1')
	part1_correct_attempt
					['0:01:03', u'1/11']

30 Student ID:j2phung

	first_attempt
					2015-10-29 00:26:41
	part1_incorrect_attempt
					('0:00:00', u'18/1000000000')
	part1_correct_attempt
					['1 day, 5:50:43', u'1/18']












## Part 2

### (21) Mistake Group Digits of size 21




### (15) Mistake Group redirect of size 15




### (1) Mistake Group ['R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|424*0.5/265	|424/265	|[('R.1', 265.0, u'265', u'265')]	|




### (1) Mistake Group ['R.0.1', 'R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|403*0.5/279	|403*2*.5/279	|[('R.0.1', 0.5, u'0.5', u'.5/'), ('R.1', 279.0, u'279', u'279')]	|




### (1) Mistake Group Wrong_Sign of size 1




### (1) Mistake Group ['R.0.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|353*0.4/284	|459*0.4/276	|[('R.0.1', 0.4, u'0.4', u'0.4')]	|




### (30) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:apokhare

	first_attempt
					2015-10-29 20:57:29
	part1_correct_attempt
					['0:00:00', u'[1/1000000]/[14/1000000]']
	part2_incorrect_attempt
					('0:00:47', u'1/1000000')
					('0:02:28', u'[1/1000000]/[14/1000000]')
					('0:02:36', u'[1/1000000]*[14/1000000]')
					('0:02:46', u'[14/1000000]')
					('0:03:44', u'1 - [1/1000000]/[14/1000000]')
	part2_correct_attempt
					['0:04:06', u'[1/1000000]/[23/1000000]']

1 Student ID:jix029

	first_attempt
					2015-10-25 19:54:09
	part1_correct_attempt
					['0:00:00', u'1/16']
	part2_incorrect_attempt
					('0:00:44', u'1/32')
	part2_correct_attempt
					['0:06:13', u'1/34']

2 Student ID:lrlai

	first_attempt
					2015-10-29 02:38:00
	part1_correct_attempt
					['0:00:00', u'1/15']
	part2_incorrect_attempt
					('0:00:00', u'1/36')
	part2_correct_attempt
					['0:00:40', u'1/24']

3 Student ID:srl006

	first_attempt
					2015-10-29 23:24:07
	part1_correct_attempt
					['0:00:00', u'.0909']
	part2_incorrect_attempt
					('0:17:11', u'.0303')
					('0:17:34', u'.36666')
	part2_correct_attempt
					['0:18:47', u'.033333333']

4 Student ID:ppanourg

	first_attempt
					2015-10-30 20:33:16
	part1_correct_attempt
					['0:00:00', u'1/20']
	part2_incorrect_attempt
					('0:00:29', u'1/30')
	part2_correct_attempt
					['0:15:39', u'1/28']

5 Student ID:atorr

	first_attempt
					2015-10-29 18:22:26
	part1_correct_attempt
					['0:00:00', u'1/14']
	part2_incorrect_attempt
					('0:00:31', u'1/(14+25)')
					('0:00:38', u'1/(14*25)')
	part2_correct_attempt
					['0:00:51', u'1/(25)']

6 Student ID:cprafull

	first_attempt
					2015-10-30 03:12:11
	part1_correct_attempt
					['0:00:00', u'1/11']
	part2_incorrect_attempt
					('0:00:15', u'25/11')
					('0:00:24', u'11/25')
	part2_correct_attempt
					['0:00:31', u'1/25']

7 Student ID:dcrume

	first_attempt
					2015-10-28 19:47:38
	part1_correct_attempt
					['0:00:00', u'1/14']
	part2_incorrect_attempt
					('0:00:17', u'1/14')
	part2_correct_attempt
					['0:02:09', u'1/34']

8 Student ID:t2li

	first_attempt
					2015-10-30 22:34:47
	part1_correct_attempt
					['0:00:00', u'1/17']
	part2_incorrect_attempt
					('0:00:00', u'1/17')
	part2_correct_attempt
					['0:00:20', u'1/23']

9 Student ID:p4kumar

	first_attempt
					2015-10-30 23:14:14
	part1_correct_attempt
					['0:00:00', u'1/16']
	part2_incorrect_attempt
					('0:00:24', u'1/32')
	part2_correct_attempt
					['0:00:33', u'1/31']

10 Student ID:pcdo

	first_attempt
					2015-10-28 23:11:45
	part1_correct_attempt
					['0:00:00', u'1/17']
	part2_incorrect_attempt
					('0:00:17', u'1/(17^2)')
	part2_correct_attempt
					['0:00:54', u'1/38']

11 Student ID:lalacson

	first_attempt
					2015-10-29 04:33:00
	part1_correct_attempt
					['0:00:00', u'1/17']
	part2_incorrect_attempt
					('0:00:32', u'1/(17*21)')
					('0:00:43', u'21/17')
	part2_correct_attempt
					['0:00:53', u'1/21']

12 Student ID:jcl084

	first_attempt
					2015-10-28 23:11:46
	part1_correct_attempt
					['0:00:00', u'1/16']
	part2_incorrect_attempt
					('0:00:09', u'1/(16^2)')
	part2_correct_attempt
					['0:00:16', u'1/30']

13 Student ID:rraiyyan

	first_attempt
					2015-10-27 23:12:17
	part1_correct_attempt
					['0:00:00', u'1/12']
	part2_incorrect_attempt
					('0:00:40', u'12/23')
	part2_correct_attempt
					['0:00:46', u'1/23']

14 Student ID:kew017

	first_attempt
					2015-10-24 22:31:12
	part1_correct_attempt
					['0:00:00', u'1/14']
	part2_incorrect_attempt
					('0:00:17', u'34/14')
	part2_correct_attempt
					['0:00:45', u'1/34']

15 Student ID:dsmonaha

	first_attempt
					2015-10-29 22:22:31
	part1_correct_attempt
					['0:00:00', u'1/10']
	part2_incorrect_attempt
					('0:00:21', u'33/10')
					('0:00:59', u'33/1')
	part2_correct_attempt
					['0:01:16', u'1/33']

16 Student ID:jtfrankl

	first_attempt
					2015-10-28 18:49:30
	part1_correct_attempt
					['0:00:00', u'1/19']
	part2_incorrect_attempt
					('0:00:46', u'19/23')
	part2_correct_attempt
					['0:00:53', u'1/23']

17 Student ID:aysee

	first_attempt
					2015-10-29 23:57:12
	part1_correct_attempt
					['0:00:00', u'1/15']
	part2_incorrect_attempt
					('0:00:08', u'36/15')
					('0:00:40', u'15/36')
	part2_correct_attempt
					['0:00:46', u'1/36']

18 Student ID:mcatozzi

	first_attempt
					2015-10-27 20:46:16
	part1_correct_attempt
					['0:00:00', u'1/11']
	part2_incorrect_attempt
					('1:35:49', u'(24*11)/1000000')
					('1:36:25', u'1/11')
	part2_correct_attempt
					['1:36:42', u'1/24']

19 Student ID:aadhakal

	first_attempt
					2015-10-30 06:21:10
	part1_correct_attempt
					['0:00:00', u'[1/1000000]/[12/1000000]']
	part2_incorrect_attempt
					('0:00:00', u'12/1000000')
					('0:00:07', u'12/10000000')
					('0:00:49', u'22/1000000')
	part2_correct_attempt
					['0:02:37', u'[1/1000000]/[22/1000000]']

20 Student ID:w4shin

	first_attempt
					2015-10-30 19:08:47
	part1_correct_attempt
					['0:00:00', u'1/19']
	part2_incorrect_attempt
					('0:00:00', u'23/19')
	part2_correct_attempt
					['0:00:17', u'1/23']

21 Student ID:flhernan

	first_attempt
					2015-10-26 03:37:10
	part1_correct_attempt
					['0:00:00', u'1/19']
	part2_incorrect_attempt
					('0:00:23', u'1/(19*20)')
	part2_correct_attempt
					['0:00:49', u'1/(20)']

22 Student ID:daw023

	first_attempt
					2015-10-30 00:42:48
	part1_correct_attempt
					['0:00:00', u'1/11']
	part2_incorrect_attempt
					('0:00:00', u'11/26')
	part2_correct_attempt
					['0:00:18', u'1/26']

23 Student ID:aurodrig

	first_attempt
					2015-10-30 18:09:15
	part1_correct_attempt
					['0:00:00', u'1/16']
	part2_incorrect_attempt
					('0:00:13', u'39/16')
	part2_correct_attempt
					['0:00:29', u'1/39']

24 Student ID:dcastlem

	first_attempt
					2015-10-29 18:39:32
	part1_correct_attempt
					['0:00:00', u'1/13']
	part2_incorrect_attempt
					('0:01:19', u'1-1/13')
					('0:01:48', u'1/13')
	part2_correct_attempt
					['0:06:46', u'1/32']

25 Student ID:tak068

	first_attempt
					2015-10-29 20:55:08
	part1_correct_attempt
					['0:00:00', u'1/12']
	part2_incorrect_attempt
					('0:00:05', u'1/12')
					('0:00:22', u'11/12')
	part2_correct_attempt
					['0:00:38', u'1/30']

26 Student ID:k4ma

	first_attempt
					2015-10-29 01:26:49
	part1_correct_attempt
					['0:00:00', u'1/16']
	part2_incorrect_attempt
					('0:00:17', u'1/32')
	part2_correct_attempt
					['0:00:25', u'1/37']

27 Student ID:v3doan

	first_attempt
					2015-10-27 00:58:29
	part1_correct_attempt
					['0:00:00', u'1/17']
	part2_incorrect_attempt
					('0:00:20', u'20/17')
	part2_correct_attempt
					['0:00:32', u'1/20']

28 Student ID:akg009

	first_attempt
					2015-10-30 20:07:19
	part1_correct_attempt
					['0:00:00', u'1/11']
	part2_incorrect_attempt
					('0:00:12', u'11/37')
	part2_correct_attempt
					['0:00:19', u'1/37']

29 Student ID:mjethani

	first_attempt
					2015-10-30 16:22:15
	part1_correct_attempt
					['0:00:00', u'1/20']
	part2_incorrect_attempt
					('0:00:25', u'39/20')
	part2_correct_attempt
					['0:01:17', u'1/39']












