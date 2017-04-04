#Problem 10

    $b = random(150,400,1);
    $p = random(0.8,0.9,0.01);
    $mean =$b*$p;
    $dev = sqrt ($b * $p * (1 - $p));

    $z = random(1.7, 3.1, 0.01);
    $s = 10*int(($z * $dev + $mean)/10+1);

    $ans = Compute("Q(($s-$mean)/$dev)");

    An airline company is considering a new policy of booking as many as [$b] persons on an
    airplane that can seat only [$s].
    (Past studies have revealed that only [$p*100]% of the booked passengers actually arrive for the flight.)

    What is the mean of the number of passengers that arrive for the flight ? [________]{$mean}

    What is the standard deviation ? [________]{$dev}

    Estimate the probability that if the company books [$b] persons, not enough seats will be
    available. [__________]{$ans}




## Part 1

### (25) Mistake Group ['R.1'] of size 25
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|175*0.89	|170*.89	|[('R.1', 0.89, u'0.89', u'.89')]	|
|1	|349*0.85	|320*.85	|[('R.1', 0.85, u'0.85', u'.85')]	|
|2	|244*0.85	|230*.85	|[('R.1', 0.85, u'0.85', u'.85')]	|
|3	|296*0.86	|280*.86	|[('R.1', 0.86, u'0.86', u'.86')]	|
|4	|163*0.82	|163/150*0.82	|[('R.1', 0.82, u'0.82', u'0.82')]	|
|5	|392*0.89	|360/.89	|[('R.1', 0.89, u'0.89', u'.89')]	|
|6	|392*0.89	|360 * .89	|[('R.1', 0.89, u'0.89', u'.89')]	|
|7	|361*0.88	|330*.88	|[('R.1', 0.88, u'0.88', u'.88')]	|
|8	|152*0.87	|150*.87	|[('R.1', 0.87, u'0.87', u'.87')]	|
|9	|213*0.89	|210*.89	|[('R.1', 0.89, u'0.89', u'.89')]	|
|10	|178*0.85	|175 * .85	|[('R.1', 0.85, u'0.85', u'.85')]	|
|11	|259*0.81	|230(.81)	|[('R.1', 0.81, u'0.81', u'.81)')]	|
|12	|308*0.86	|306*.86	|[('R.1', 0.86, u'0.86', u'.86')]	|
|13	|368*0.89	|340*0.89	|[('R.1', 0.89, u'0.89', u'0.89')]	|
|14	|382*0.89	|282*0.89	|[('R.1', 0.89, u'0.89', u'0.89')]	|
|15	|382*0.89	|360*0.89	|[('R.1', 0.89, u'0.89', u'0.89')]	|
|16	|342*0.87	|320*.87	|[('R.1', 0.87, u'0.87', u'.87')]	|
|17	|323*0.82	|290*.82	|[('R.1', 0.82, u'0.82', u'.82')]	|
|18	|284*0.82	|260*0.82	|[('R.1', 0.82, u'0.82', u'0.82')]	|
|19	|199*0.87	|190 * .87	|[('R.1', 0.87, u'0.87', u'.87')]	|
|20	|189*0.87	|180*(189*0.87/189)	|[('R.1', 0.87, u'0.87', u'189*0.87/189')]	|
|21	|378*0.88	|350*.88	|[('R.1', 0.88, u'0.88', u'.88')]	|
|22	|229*0.82	|200*0.82	|[('R.1', 0.82, u'0.82', u'0.82')]	|
|23	|287*0.86	|270*0.86	|[('R.1', 0.86, u'0.86', u'0.86')]	|




### (25) Mistake Group ['R.0'] of size 25
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|268*0.89	|268 * .8	|[('R.0', 268.0, u'268', u'268')]	|
|1	|163*0.82	|163/150	|[('R.0', 163.0, u'163', u'163')]	|
|2	|172*0.85	|172/2	|[('R.0', 172.0, u'172', u'172')]	|
|3	|172*0.85	|172/170	|[('R.0', 172.0, u'172', u'172')]	|
|4	|392*0.89	|392/360	|[('R.0', 392.0, u'392', u'392')]	|
|5	|392*0.89	|392/89	|[('R.0', 392.0, u'392', u'392')]	|
|6	|152*0.87	|152/150	|[('R.0', 152.0, u'152', u'152')]	|
|7	|384*0.84	|384/294	|[('R.0', 384.0, u'384', u'384')]	|
|8	|384*0.84	|384/322.56	|[('R.0', 384.0, u'384', u'384')]	|
|9	|319*0.81	|319/280	|[('R.0', 319.0, u'319', u'319')]	|
|10	|293*0.81	|293/260	|[('R.0', 293.0, u'293', u'293')]	|
|11	|226*0.8	|226/2	|[('R.0', 226.0, u'226', u'226')]	|
|12	|174*0.85	|174 * .84	|[('R.0', 174.0, u'174', u'174')]	|
|13	|366*0.87	|366*.8	|[('R.0', 366.0, u'366', u'366')]	|
|14	|333*0.85	|333/310	|[('R.0', 333.0, u'333', u'333')]	|
|15	|154*0.85	|154*0.8	|[('R.0', 154.0, u'154', u'154')]	|
|16	|330*0.86	|330/300	|[('R.0', 330.0, u'330', u'330')]	|
|17	|321*0.89	|321*89	|[('R.0', 321.0, u'321', u'321')]	|
|18	|159*0.8	|159*80	|[('R.0', 159.0, u'159', u'159')]	|
|19	|166*0.86	|166/160	|[('R.0', 166.0, u'166', u'166')]	|
|20	|214*0.88	|214*1/210	|[('R.0', 214.0, u'214', u'214*1')]	|
|21	|282*0.85	|282/260	|[('R.0', 282.0, u'282', u'282')]	|
|22	|378*0.88	|378/350	|[('R.0', 378.0, u'378', u'378')]	|
|23	|175*0.87	|175 * 87	|[('R.0', 175.0, u'175', u'175')]	|
|24	|283*0.89	|283*89	|[('R.0', 283.0, u'283', u'283')]	|




### (21) Mistake Group Digits of size 21




### (3) Mistake Group Fraction of size 3




### (1) Mistake Group ['R.0', 'R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|392*0.89	|392/.89	|[('R.0', 392.0, u'392', u'392'), ('R.1', 0.89, u'0.89', u'.89')]	|




### (47) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:starinia

	first_attempt
					2015-11-05 03:48:29
	part1_incorrect_attempt
					('0:00:00', u'260 + 218.4 / 2')
					('0:00:08', u'218.4')
	part1_correct_attempt
					['0:04:38', u'.84 * 285']

1 Student ID:agoldsht

	first_attempt
					2015-11-04 20:43:52
	part1_incorrect_attempt
					('0:00:00', u'150/152')
					('0:00:55', u'150/152')
	part1_correct_attempt
					['0:03:15', u'152*.87']

2 Student ID:hkhodada

	first_attempt
					2015-11-03 01:24:27
	part1_incorrect_attempt
					('0:00:00', u'81/100')
	part1_correct_attempt
					['0:00:38', u'0.81*332']

3 Student ID:glcohen

	first_attempt
					2015-11-03 22:18:15
	part1_incorrect_attempt
					('0:00:00', u'170/2')
	part1_correct_attempt
					['0:15:07', u'(172*.85)']

4 Student ID:fichoi

	first_attempt
					2015-11-04 23:35:23
	part1_incorrect_attempt
					('0:00:00', u'322.56/384')
					('0:00:00', u'294/350')
					('0:07:20', u'350/294')
					('0:08:47', u'.84 * 350')
	part1_correct_attempt
					['0:23:23', u'.84 * 384']

5 Student ID:d6he

	first_attempt
					2015-11-05 07:20:50
	part1_incorrect_attempt
					('0:00:00', u'358.36')
	part1_correct_attempt
					['0:00:49', u'346.72']

6 Student ID:asp025

	first_attempt
					2015-11-06 23:49:39
	part1_incorrect_attempt
					('0:00:00', u'1/260')
	part1_correct_attempt
					['0:04:12', u'.84*284']

7 Student ID:jjm019

	first_attempt
					2015-11-05 03:44:24
	part1_incorrect_attempt
					('0:00:00', u'(208+230)/2')
	part1_correct_attempt
					['2:31:53', u'.80(260)']

8 Student ID:mhale

	first_attempt
					2015-11-05 20:42:55
	part1_incorrect_attempt
					('0:00:00', u'.82 * 312')
	part1_correct_attempt
					['0:00:07', u'.82 * 321']

9 Student ID:thk002

	first_attempt
					2015-11-05 06:20:22
	part1_incorrect_attempt
					('0:00:00', u'131.2')
	part1_correct_attempt
					['0:38:43', u'174*.82']

10 Student ID:sachadal

	first_attempt
					2015-11-05 21:29:37
	part1_incorrect_attempt
					('0:00:00', u'0.85*190')
	part1_correct_attempt
					['0:00:07', u'0.85*201']

11 Student ID:mroknich

	first_attempt
					2015-11-01 21:37:25
	part1_incorrect_attempt
					('0:00:00', u'.88*280')
	part1_correct_attempt
					['0:00:25', u'.88*293']

12 Student ID:aordookh

	first_attempt
					2015-11-06 06:40:25
	part1_incorrect_attempt
					('0:00:00', u'.89(290)/290')
					('0:00:34', u'.89(290)')
					('0:00:47', u'290/.89(290)')
					('0:01:03', u'290/(.89(290))')
					('0:06:09', u'290/(.11*290)')
					('0:06:25', u'(.11*290)/290')
	part1_correct_attempt
					['0:11:40', u'290-(.89*18)']

13 Student ID:beyounge

	first_attempt
					2015-10-30 06:38:00
	part1_incorrect_attempt
					('0:00:00', u'0.43 * 356')
					('0:00:08', u'0.43 * 330')
	part1_correct_attempt
					['0:00:28', u'0.86 * 356']

14 Student ID:dlt009

	first_attempt
					2015-11-05 08:55:41
	part1_incorrect_attempt
					('0:00:00', u'.82*220')
	part1_correct_attempt
					['0:00:27', u'.82*244']

15 Student ID:mbl003

	first_attempt
					2015-11-06 21:12:44
	part1_incorrect_attempt
					('0:00:00', u'286/260')
					('0:00:09', u'260/282')
	part1_correct_attempt
					['0:00:31', u'282*.85']

16 Student ID:dan029

	first_attempt
					2015-11-05 10:03:16
	part1_incorrect_attempt
					('0:00:00', u'.81*200')
	part1_correct_attempt
					['0:00:10', u'.81*220']

17 Student ID:tpmach

	first_attempt
					2015-11-05 17:19:15
	part1_incorrect_attempt
					('0:00:00', u'300/334')
					('0:00:29', u'0.84(300/334)')
	part1_correct_attempt
					['0:00:53', u'0.84*334']

18 Student ID:cfgutier

	first_attempt
					2015-11-06 20:31:36
	part1_incorrect_attempt
					('0:00:00', u'.83 * 210')
	part1_correct_attempt
					['0:00:25', u'.83 * 234']

19 Student ID:dkostins

	first_attempt
					2015-11-06 05:22:54
	part1_incorrect_attempt
					('0:00:00', u'.86')
					('0:00:10', u'160/166')
	part1_correct_attempt
					['0:01:43', u'.86 * 166']

20 Student ID:jnatale

	first_attempt
					2015-11-04 08:48:43
	part1_incorrect_attempt
					('0:00:00', u'200/226')
	part1_correct_attempt
					['0:01:07', u'226*.81']

21 Student ID:rlhagen

	first_attempt
					2015-10-31 20:23:40
	part1_incorrect_attempt
					('0:00:00', u'(260+285)/2')
					('0:02:29', u'0.83')
					('0:02:47', u'0.83*260')
	part1_correct_attempt
					['0:02:54', u'0.83*285']

22 Student ID:nnh002

	first_attempt
					2015-11-06 21:28:02
	part1_incorrect_attempt
					('0:00:00', u'(0.85*397+397)/2')
	part1_correct_attempt
					['0:03:33', u'(0.85*397)']

23 Student ID:ralhadda

	first_attempt
					2015-10-31 22:30:19
	part1_incorrect_attempt
					('0:00:00', u'1-.9990356')
					('0:03:05', u'9.643*10^-4')
					('0:04:05', u'0.999')
					('0:04:24', u'0.000964')
	part1_correct_attempt
					['0:06:48', u'241.08']

24 Student ID:atorr

	first_attempt
					2015-11-06 00:45:09
	part1_incorrect_attempt
					('0:00:00', u'320.38/386')
	part1_correct_attempt
					['0:00:12', u'386 * .83']

25 Student ID:dcrume

	first_attempt
					2015-11-06 21:02:05
	part1_incorrect_attempt
					('0:00:00', u'.86')
	part1_correct_attempt
					['0:00:13', u'.86*331']

26 Student ID:r1gu

	first_attempt
					2015-11-05 12:27:04
	part1_incorrect_attempt
					('0:00:00', u'3330.85')
	part1_correct_attempt
					['0:00:07', u'333*0.85']

27 Student ID:flhernan

	first_attempt
					2015-11-05 17:25:05
	part1_incorrect_attempt
					('0:00:00', u'141.42')
	part1_correct_attempt
					['20:30:20', u'162*.82']

28 Student ID:l8ngo

	first_attempt
					2015-10-30 16:44:01
	part1_incorrect_attempt
					('0:00:00', u'340/381')
	part1_correct_attempt
					['0:00:39', u'381*0.84']

29 Student ID:ajabasa

	first_attempt
					2015-11-05 22:37:24
	part1_incorrect_attempt
					('0:00:00', u'.81*200')
	part1_correct_attempt
					['0:00:06', u'.81*222']

30 Student ID:lahawkin

	first_attempt
					2015-11-04 04:59:22
	part1_incorrect_attempt
					('0:00:00', u'(89/100)290')
	part1_correct_attempt
					['0:00:11', u'(89/100)303']

31 Student ID:dsriniva

	first_attempt
					2015-11-05 17:04:31
	part1_incorrect_attempt
					('0:00:00', u'86*320')
	part1_correct_attempt
					['0:00:06', u'.86*320']

32 Student ID:etemlock

	first_attempt
					2015-11-05 03:28:17
	part1_incorrect_attempt
					('0:00:00', u'(319*.81)/280')
	part1_correct_attempt
					['0:01:07', u'319*.81']

33 Student ID:jguanzho

	first_attempt
					2015-11-05 17:48:20
	part1_incorrect_attempt
					('0:00:00', u'0.8*240')
	part1_correct_attempt
					['0:00:12', u'0.8*273']

34 Student ID:haliew

	first_attempt
					2015-11-07 00:33:52
	part1_incorrect_attempt
					('0:00:00', u'210/223')
	part1_correct_attempt
					['0:00:20', u'223*.87']

35 Student ID:a2ahmed

	first_attempt
					2015-11-07 00:53:49
	part1_incorrect_attempt
					('0:00:00', u'182.7')
	part1_correct_attempt
					['0:00:14', u'189.66']

36 Student ID:cstringh

	first_attempt
					2015-11-04 07:33:36
	part1_incorrect_attempt
					('0:00:00', u'360/89')
	part1_correct_attempt
					['0:00:39', u'392 * .89']

37 Student ID:mitopete

	first_attempt
					2015-11-07 00:18:55
	part1_incorrect_attempt
					('0:00:00', u'(220+241)/2')
					('0:02:14', u'0.84(220)')
	part1_correct_attempt
					['0:02:26', u'0.84(241)']

38 Student ID:yjshin

	first_attempt
					2015-11-06 23:35:02
	part1_incorrect_attempt
					('0:00:00', u'(314.5+280.5)/2')
					('0:00:20', u'(314.5)/2')
	part1_correct_attempt
					['0:00:26', u'(314.5)']

39 Student ID:m4salaza

	first_attempt
					2015-11-05 05:50:45
	part1_incorrect_attempt
					('0:00:00', u'.81*260')
	part1_correct_attempt
					['0:01:06', u'.81*293']

40 Student ID:volim

	first_attempt
					2015-11-04 23:36:41
	part1_incorrect_attempt
					('0:00:00', u'290/317')
					('0:00:08', u'.84')
	part1_correct_attempt
					['0:00:17', u'(317)*.84']

41 Student ID:yypan

	first_attempt
					2015-11-03 01:30:52
	part1_incorrect_attempt
					('0:00:00', u'0.85')
	part1_correct_attempt
					['0:00:20', u'390*0.85']

42 Student ID:k4ma

	first_attempt
					2015-11-06 22:04:58
	part1_incorrect_attempt
					('0:00:00', u'(365+330)/2')
	part1_correct_attempt
					['0:01:36', u'314']

43 Student ID:aurodrig

	first_attempt
					2015-11-07 00:11:29
	part1_incorrect_attempt
					('0:00:00', u'270*89')
	part1_correct_attempt
					['0:00:38', u'283*.89']

44 Student ID:ytc012

	first_attempt
					2015-11-05 22:08:44
	part1_incorrect_attempt
					('0:00:00', u'0.85*340')
	part1_correct_attempt
					['0:00:11', u'0.85*369']

45 Student ID:mtrafeca

	first_attempt
					2015-11-05 21:43:21
	part1_incorrect_attempt
					('0:00:00', u'.89')
					('0:00:13', u'210/223')
	part1_correct_attempt
					['0:00:58', u'223*.89']

46 Student ID:j2phung

	first_attempt
					2015-11-05 18:33:17
	part1_incorrect_attempt
					('0:00:00', u'300/330')
	part1_correct_attempt
					['0:19:11', u'.86 * 330']












## Part 2

### (23) Mistake Group ['R.0.0'] of size 23
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|sqrt(286*0.83*(1-0.83))	|sqrt(237.38*.83)	|[('R.0.0', 237.38, u'286*0.83', u'237.38')]	|
|1	|sqrt(286*0.83*(1-0.83))	|sqrt(237.38*(286/250))	|[('R.0.0', 237.38, u'286*0.83', u'237.38')]	|
|2	|sqrt(276*0.87*(1-0.87))	|sqrt(.87*276*13)	|[('R.0.0', 240.12, u'276*0.87', u'.87*276')]	|
|3	|sqrt(339*0.81*(1-0.81))	|sqrt(.81 * 339 * 300)	|[('R.0.0', 274.59000000000003, u'339*0.81', u'.81 * 339')]	|
|4	|sqrt(317*0.83*(1-0.83))	|317*0.83*0.83*0.17	|[('R.0.0', 263.11, u'317*0.83', u'317*0.83')]	|
|5	|sqrt(222*0.81*(1-0.81))	|((179.82-222))^2	|[('R.0.0', 179.82000000000002, u'222*0.81', u'179.82')]	|
|6	|sqrt(262*0.8*(1-0.8))	|(209.6)(0.8)(0.2)	|[('R.0.0', 209.60000000000002, u'262*0.8', u'209.6')]	|
|7	|sqrt(161*0.81*(1-0.81))	|sqrt((161*.81)*(.81))	|[('R.0.0', 130.41, u'161*0.81', u'161*.81)')]	|
|8	|sqrt(284*0.89*(1-0.89))	|sqrt(284*.89*11)	|[('R.0.0', 252.76, u'284*0.89', u'284*.89*')]	|
|9	|sqrt(284*0.82*(1-0.82))	|sqrt((284*.82)/284)	|[('R.0.0', 232.88, u'284*0.82', u'284*.82)')]	|
|10	|sqrt(162*0.82*(1-0.82))	|sqrt(132.84*.82)	|[('R.0.0', 132.84, u'162*0.82', u'132.84')]	|
|11	|sqrt(162*0.82*(1-0.82))	|sqrt(132.84*.12)	|[('R.0.0', 132.84, u'162*0.82', u'132.84')]	|
|12	|sqrt(162*0.82*(1-0.82))	|sqrt(132.84/150)	|[('R.0.0', 132.84, u'162*0.82', u'132.84')]	|
|13	|sqrt(281*0.81*(1-0.81))	|sqrt(227.61/281)	|[('R.0.0', 227.61, u'281*0.81', u'227.61')]	|
|14	|sqrt(281*0.81*(1-0.81))	|sqrt(227.61/280)	|[('R.0.0', 227.61, u'281*0.81', u'227.61')]	|
|15	|sqrt(281*0.81*(1-0.81))	|sqrt(227.61/250)	|[('R.0.0', 227.61, u'281*0.81', u'227.61')]	|
|16	|sqrt(281*0.81*(1-0.81))	|sqrt(227.61/.81)	|[('R.0.0', 227.61, u'281*0.81', u'227.61')]	|
|17	|sqrt(284*0.82*(1-0.82))	|sqrt(232.88)/284	|[('R.0.0', 232.88, u'284*0.82', u'232.88')]	|
|18	|sqrt(339*0.82*(1-0.82))	|sqrt(3.39*82*0.16)	|[('R.0.0', 277.97999999999996, u'339*0.82', u'3.39*82')]	|
|19	|sqrt(241*0.84*(1-0.84))	|(0.84(241)(0.5))^(1/2)	|[('R.0.0', 202.44, u'241*0.84', u'0.84(241)')]	|
|20	|sqrt(241*0.84*(1-0.84))	|(0.84(241)(0.25))^(1/2)	|[('R.0.0', 202.44, u'241*0.84', u'0.84(241)')]	|
|21	|sqrt(241*0.84*(1-0.84))	|(0.84(241)(0.84*(1-0.84)))^(1/2)	|[('R.0.0', 202.44, u'241*0.84', u'0.84(241)')]	|
|22	|sqrt(241*0.84*(1-0.84))	|(0.84(241)(0.5*(1-0.5)))^(1/2)	|[('R.0.0', 202.44, u'241*0.84', u'0.84(241)')]	|




### (21) Mistake Group ['R.0.0.0'] of size 21
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|sqrt(327*0.81*(1-0.81))	|((327-.81*327) + (327-290)) / 2	|[('R.0.0.0', 327.0, u'327', u'327')]	|
|1	|sqrt(276*0.87*(1-0.87))	|sqrt(276 - (.87*276))^2	|[('R.0.0.0', 276.0, u'276', u'276')]	|
|2	|sqrt(276*0.87*(1-0.87))	|sqrt((276 - (.87*276))^2)	|[('R.0.0.0', 276.0, u'276', u'276')]	|
|3	|sqrt(264*0.89*(1-0.89))	|((264- 234.96)^2/250)	|[('R.0.0.0', 264.0, u'264', u'264')]	|
|4	|sqrt(256*0.89*(1-0.89))	|((256-[(.89)*(256)])^2)^(1/2)	|[('R.0.0.0', 256.0, u'256', u'256')]	|
|5	|sqrt(174*0.85*(1-0.85))	|(174 * .85)^1/2	|[('R.0.0.0', 174.0, u'174', u'174')]	|
|6	|sqrt(162*0.82*(1-0.82))	|sqrt((162^2-132.84^2))	|[('R.0.0.0', 162.0, u'162', u'162')]	|
|7	|sqrt(345*0.89*(1-0.89))	|sqrt ((345 - 307.05)^2 )	|[('R.0.0.0', 345.0, u'345', u'345')]	|
|8	|sqrt(330*0.86*(1-0.86))	|(330*(1/2)*(1/2))^(1/2)	|[('R.0.0.0', 330.0, u'330', u'330')]	|
|9	|sqrt(161*0.81*(1-0.81))	|((161-(161*.81))^2)/150	|[('R.0.0.0', 161.0, u'161', u'161')]	|
|10	|sqrt(161*0.81*(1-0.81))	|((161-(130.14))^2)/150	|[('R.0.0.0', 161.0, u'161', u'161')]	|
|11	|sqrt(386*0.83*(1-0.83))	|[386 - (386 * .83)]^2/5	|[('R.0.0.0', 386.0, u'386', u'386')]	|
|12	|sqrt(367*0.82*(1-0.82))	|sqrt((367-300.94)^2)	|[('R.0.0.0', 367.0, u'367', u'367')]	|
|13	|sqrt(369*0.85*(1-0.85))	|sqrt(((369-0.85*369)+ (340-0.85*369)))	|[('R.0.0.0', 369.0, u'369', u'369')]	|
|14	|sqrt(347*0.8*(1-0.8))	|sqrt((347 - 277.6)^2)	|[('R.0.0.0', 347.0, u'347', u'347')]	|
|15	|sqrt(284*0.82*(1-0.82))	|sqrt((284-232.88)^2)	|[('R.0.0.0', 284.0, u'284', u'284')]	|
|16	|sqrt(162*0.82*(1-0.82))	|sqrt(162^2-132.84^2)	|[('R.0.0.0', 162.0, u'162', u'162')]	|
|17	|sqrt(378*0.88*(1-0.88))	|((378)^2(.88)) - ((378)(.88))^2	|[('R.0.0.0', 378.0, u'378', u'378')]	|
|18	|sqrt(376*0.85*(1-0.85))	|sqrt(376 * (1/376) * (1 - (1/376)))	|[('R.0.0.0', 376.0, u'376', u'376')]	|




### (20) Mistake Group ['R.0.1'] of size 20
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|sqrt(185*0.85*(1-0.85))	|sqrt (180 * .85 * (1 - .85))	|[('R.0.1', 0.15000000000000002, u'1-0.85', u'1 - .85)')]	|
|1	|sqrt(390*0.85*(1-0.85))	|(0.85*0.15)/390	|[('R.0.1', 0.15000000000000002, u'1-0.85', u'0.15')]	|
|2	|sqrt(390*0.85*(1-0.85))	|(0.85*0.15)/360	|[('R.0.1', 0.15000000000000002, u'1-0.85', u'0.15')]	|
|3	|sqrt(208*0.86*(1-0.86))	|(.86*208*.86*.14)^.5	|[('R.0.1', 0.14, u'1-0.86', u'.14)')]	|
|4	|sqrt(392*0.89*(1-0.89))	|sqrt (360 * .89 * (1 - .89))	|[('R.0.1', 0.10999999999999999, u'1-0.89', u'1 - .89)')]	|
|5	|sqrt(282*0.88*(1-0.88))	|sqrt(260*.12)	|[('R.0.1', 0.12, u'1-0.88', u'.12)')]	|
|6	|sqrt(255*0.8*(1-0.8))	|.8*.2*255	|[('R.0.1', 0.19999999999999996, u'1-0.8', u'.2*')]	|
|7	|sqrt(152*0.87*(1-0.87))	|sqrt(370*.87*.13)	|[('R.0.1', 0.13, u'1-0.87', u'.13)')]	|
|8	|sqrt(152*0.87*(1-0.87))	|sqrt(370*.87*(1-.87))	|[('R.0.1', 0.13, u'1-0.87', u'1-.87)')]	|
|9	|sqrt(285*0.84*(1-0.84))	|sqrt (280 * .84 * .16)	|[('R.0.1', 0.16000000000000003, u'1-0.84', u'.16)')]	|
|10	|sqrt(317*0.83*(1-0.83))	|sqrt(318*0.83*0.17)	|[('R.0.1', 0.17000000000000004, u'1-0.83', u'0.17')]	|
|11	|sqrt(317*0.83*(1-0.83))	|sqrt(263.11*0.83*0.17)	|[('R.0.1', 0.17000000000000004, u'1-0.83', u'0.17')]	|
|12	|sqrt(317*0.83*(1-0.83))	|(263.11*0.83*0.17)^0.5	|[('R.0.1', 0.17000000000000004, u'1-0.83', u'0.17')]	|
|13	|sqrt(286*0.8*(1-0.8))	|sqrt(286*.8*.8*.2)	|[('R.0.1', 0.19999999999999996, u'1-0.8', u'.2)')]	|
|14	|sqrt(378*0.88*(1-0.88))	|((.88*378*.88)(1-.88))^(.5)	|[('R.0.1', 0.12, u'1-0.88', u'1-.88)')]	|
|15	|sqrt(231*0.8*(1-0.8))	|0.8*0.2*231	|[('R.0.1', 0.19999999999999996, u'1-0.8', u'0.2')]	|
|16	|sqrt(162*0.82*(1-0.82))	|sqrt(132.84*.82*.18)	|[('R.0.1', 0.18000000000000005, u'1-0.82', u'.18)')]	|
|17	|sqrt(189*0.87*(1-0.87))	|[(189*0.87/189)*[1-(189*0.87/189)]*180]	|[('R.0.1', 0.13, u'1-0.87', u'1-(189*0.87/189)')]	|
|18	|sqrt(281*0.81*(1-0.81))	|sqrt(227.61*.81*.19)	|[('R.0.1', 0.18999999999999995, u'1-0.81', u'.19)')]	|
|19	|sqrt(281*0.81*(1-0.81))	|sqrt(250*.81*.19)	|[('R.0.1', 0.18999999999999995, u'1-0.81', u'.19)')]	|




### (19) Mistake Group Digits of size 19




### (14) Mistake Group redirect of size 14




### (10) Mistake Group ['R.0.1.1'] of size 10
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|sqrt(296*0.86*(1-0.86))	|sqrt(296-296*.86)	|[('R.0.1.1', 0.86, u'0.86', u'.86)')]	|
|1	|sqrt(361*0.88*(1-0.88))	|(361-(361*.88))^(1/2)	|[('R.0.1.1', 0.88, u'0.88', u'.88)')]	|
|2	|sqrt(327*0.81*(1-0.81))	|sqrt(290-327*.81)	|[('R.0.1.1', 0.81, u'0.81', u'.81)')]	|
|3	|sqrt(161*0.81*(1-0.81))	|(161-(161*.81))^2	|[('R.0.1.1', 0.81, u'0.81', u'.81)')]	|
|4	|sqrt(161*0.81*(1-0.81))	|(150-(161*.81))^2	|[('R.0.1.1', 0.81, u'0.81', u'.81)')]	|
|5	|sqrt(386*0.83*(1-0.83))	|[386 - (386 * .83)]/5	|[('R.0.1.1', 0.83, u'0.83', u'.83)')]	|
|6	|sqrt(308*0.86*(1-0.86))	|(308-308*.86)/3	|[('R.0.1.1', 0.86, u'0.86', u'.86)')]	|
|7	|sqrt(308*0.86*(1-0.86))	|(308-308*.86)/2	|[('R.0.1.1', 0.86, u'0.86', u'.86)')]	|
|8	|sqrt(376*0.85*(1-0.85))	|sqrt((376 - (376 * .85)))	|[('R.0.1.1', 0.85, u'0.85', u'.85)')]	|
|9	|sqrt(297*0.87*(1-0.87))	|sqrt(270 - 297 * .87)	|[('R.0.1.1', 0.87, u'0.87', u'.87)')]	|




### (6) Mistake Group Wrong_Sign of size 6




### (4) Mistake Group ['R.0'] of size 4
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|sqrt(179*0.82*(1-0.82))	|((82/100)(18/100)(179))*(1/2)	|[('R.0', 26.420400000000008, u'179*0.82*(1-0.82)', u'(82/100)(18/100)(179)')]	|
|1	|sqrt(368*0.89*(1-0.89))	|(368*0.89*0.11)^1/2	|[('R.0', 36.02719999999999, u'368*0.89*(1-0.89)', u'(368*0.89*0.11)^1')]	|
|2	|sqrt(303*0.89*(1-0.89))	|((89/100)(303)(.11))^1/2	|[('R.0', 29.6637, u'303*0.89*(1-0.89)', u'((89/100)(303)(.11))^1')]	|
|3	|sqrt(202*0.8*(1-0.8))	|((202*.8)*(1-.8))*(1/2)	|[('R.0', 32.32, u'202*0.8*(1-0.8)', u'(202*.8)*(1-.8)')]	|




### (3) Mistake Group ['R.0.0', 'R.0.1.0'] of size 3
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.0.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|sqrt(346*0.87*(1-0.87))	|sqrt( (346 * 0.87)(1-0.13))	|[('R.0.0', 301.02, u'346*0.87', u'346 * 0.87'), ('R.0.1.0', 1.0, u'1', u'1')]	|
|1	|sqrt(212*0.87*(1-0.87))	|sqrt(212*.87*(1-.7))	|[('R.0.0', 184.44, u'212*0.87', u'212*.87*'), ('R.0.1.0', 1.0, u'1', u'1')]	|
|2	|sqrt(193*0.84*(1-0.84))	|sqrt (193 *.84 * (1 -.83))	|[('R.0.0', 162.12, u'193*0.84', u'193 *.84 '), ('R.0.1.0', 1.0, u'1', u'1')]	|




### (2) Mistake Group ['R.0.0', 'R.0.1'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|sqrt(327*0.81*(1-0.81))	|sqrt(327*.81-.19)	|[('R.0.0', 264.87, u'327*0.81', u'327*.81-'), ('R.0.1', 0.18999999999999995, u'1-0.81', u'.19)')]	|
|1	|sqrt(202*0.8*(1-0.8))	|((202*.8)^(1-.8))*(1/2)	|[('R.0.0', 161.60000000000002, u'202*0.8', u'202*.8)'), ('R.0.1', 0.19999999999999996, u'1-0.8', u'1-.8)')]	|




### (2) Mistake Group ['R.0.0.0', 'R.0.1.0'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0', 'R.0.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|sqrt(376*0.85*(1-0.85))	|sqrt(376 * (1/340) * (1 - (1/340)))	|[('R.0.0.0', 376.0, u'376', u'376'), ('R.0.1.0', 1.0, u'1', u'1')]	|
|1	|sqrt(193*0.84*(1-0.84))	|sqrt (193 *.83 * (1 -.83))	|[('R.0.0.0', 193.0, u'193', u'193'), ('R.0.1.0', 1.0, u'1', u'1')]	|




### (1) Mistake Group ['R.0.1.0', 'R.0.1.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1.0', 'R.0.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|sqrt(162*0.82*(1-0.82))	|sqrt((162-132.84)^2/(1/.82))	|[('R.0.1.0', 1.0, u'1', u'1'), ('R.0.1.1', 0.82, u'0.82', u'.82)')]	|




### (90) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:gthorn

	first_attempt
					2015-11-05 07:20:09
	part1_correct_attempt
					['0:00:00', u'178 * .85']
	part2_incorrect_attempt
					('0:01:37', u'sqrt((178-151.3)^2 * .85)')
	part2_correct_attempt
					['10:52:45', u'sqrt(.85 * .15 * 178)']

1 Student ID:apokhare

	first_attempt
					2015-11-05 22:19:38
	part1_correct_attempt
					['0:00:00', u'1.66*81']
	part2_incorrect_attempt
					('0:00:00', u'1.66*81*.19')
	part2_correct_attempt
					['0:02:17', u'sqrt(1.66*81*.19)']

2 Student ID:alakamsa

	first_attempt
					2015-11-02 19:38:11
	part1_correct_attempt
					['0:00:00', u'.8*255']
	part2_incorrect_attempt
					('0:01:33', u'51^2')
	part2_correct_attempt
					['1 day, 23:14:30', u'sqrt(.8*.2*255)']

3 Student ID:nhn018

	first_attempt
					2015-11-05 05:43:40
	part1_correct_attempt
					['0:00:00', u'213*.89']
	part2_incorrect_attempt
					('0:00:44', u'(213-189.57)/2')
					('0:00:55', u'(213-190)/2')
	part2_correct_attempt
					['0:22:21', u'sqrt(.89*213*(1-.89))']

4 Student ID:jyc018

	first_attempt
					2015-11-06 23:23:19
	part1_correct_attempt
					['0:00:00', u'397*.84']
	part2_incorrect_attempt
					('0:00:16', u'6.49')
	part2_correct_attempt
					['0:01:05', u'sqrt(397*.84*.16)']

5 Student ID:r9jiang

	first_attempt
					2015-11-02 04:16:09
	part1_correct_attempt
					['0:00:00', u'263*0.82']
	part2_incorrect_attempt
					('0:01:52', u'(0.82*(263-215.66)^2)^(1/2)')
					('3 days, 1:34:02', u'0.1476*263')
					('3 days, 1:34:50', u'(0.82-(0.82^2))*263')
	part2_correct_attempt
					['3 days, 1:35:09', u'((0.82-(0.82^2))*263)^(1/2)']

6 Student ID:rlhagen

	first_attempt
					2015-10-31 20:26:34
	part1_correct_attempt
					['0:00:00', u'0.83*285']
	part2_incorrect_attempt
					('0:00:18', u'sqrt((1/12)(285)^2)')
					('0:00:49', u'sqrt((1/12)(285-260)^2)')
					('0:01:08', u'sqrt((1/12)(0.83*285)^2)')
	part2_correct_attempt
					['0:05:03', u'sqrt (285 * 0.83 * (1 - 0.83))']

7 Student ID:dgunawan

	first_attempt
					2015-11-05 09:22:36
	part1_correct_attempt
					['0:00:00', u'(.89)*(256)']
	part2_incorrect_attempt
					('0:01:20', u'(((.89)*(256))^2)^(1/2)')
					('0:01:50', u'((250-[(.89)*(256)])^2)^(1/2)')
					('0:02:18', u'(([(.89)*(256)]-250)^2)^(1/2)')
					('0:02:25', u'(([(.89)*(256)]-256)^2)^(1/2)')
					('0:03:07', u'(([(.89)*(256)]-256)^2/2)^(1/2)')
					('0:38:47', u'((256-[(.89)*(256)])^2/2)^(1/2)')
	part2_correct_attempt
					['14:51:47', u'((.89)*(256)(1-.89))^(1/2)']

8 Student ID:tcn013

	first_attempt
					2015-11-05 21:07:21
	part1_correct_attempt
					['0:00:00', u'242*.81']
	part2_incorrect_attempt
					('0:02:56', u'sqrt(.81*.09*242)')
	part2_correct_attempt
					['0:07:55', u'sqrt(.81*.19*242)']

9 Student ID:tstevens

	first_attempt
					2015-11-06 12:21:35
	part1_correct_attempt
					['0:00:00', u'377*.81']
	part2_incorrect_attempt
					('0:01:48', u'0.240874033')
	part2_correct_attempt
					['0:02:46', u'7.61710575']

10 Student ID:l8ngo

	first_attempt
					2015-10-30 16:44:40
	part1_correct_attempt
					['0:00:00', u'381*0.84']
	part2_incorrect_attempt
					('0:07:30', u'sqrt([381^2]*0.84-381*0.84)')
	part2_correct_attempt
					['6 days, 7:11:52', u'sqrt[381*0.84*0.16]']

11 Student ID:djk006

	first_attempt
					2015-11-04 06:15:40
	part1_correct_attempt
					['0:00:00', u'298*.88']
	part2_incorrect_attempt
					('0:00:00', u'298(.88)(.12)^(1/2)')
	part2_correct_attempt
					['0:00:12', u'(298(.88)(.12))^(1/2)']

12 Student ID:dsriniva

	first_attempt
					2015-11-05 17:04:37
	part1_correct_attempt
					['0:00:00', u'.86*320']
	part2_incorrect_attempt
					('2:37:20', u'1/sqrt(320)*(.86*32)')
					('2:37:48', u'1/sqrt(320)*(.86*320)')
					('2:38:06', u'275.2/sqrt(320)')
	part2_correct_attempt
					['2:39:01', u'sqrt(320*0.86*0.14)']

13 Student ID:chc286

	first_attempt
					2015-11-01 02:05:21
	part1_correct_attempt
					['0:00:00', u'194*0.83']
	part2_incorrect_attempt
					('0:04:53', u'sqrt(194*0.83)')

14 Student ID:sayao

	first_attempt
					2015-11-04 02:01:34
	part1_correct_attempt
					['0:00:00', u'182*.83']
	part2_incorrect_attempt
					('0:00:18', u'182-151.06')
	part2_correct_attempt
					['1 day, 2:02:44', u'sqrt(182*.83*(1-.83))']

15 Student ID:anvan

	first_attempt
					2015-11-05 15:39:51
	part1_correct_attempt
					['0:00:00', u'.89(345)']
	part2_incorrect_attempt
					('3:17:50', u'(345 - 307.05)')
	part2_correct_attempt
					['23:26:00', u'sqrt ( .89 * .11 * 345)']

16 Student ID:flhernan

	first_attempt
					2015-11-06 13:55:25
	part1_correct_attempt
					['0:00:00', u'162*.82']
	part2_incorrect_attempt
					('0:00:00', u'sqrt(132.84)')
					('0:00:37', u'sqrt(150/132.84)')
					('0:00:46', u'sqrt(162/132.84)')
					('0:00:54', u'sqrt(162-132.84)')
					('0:15:43', u'24.26790473')
					('0:20:20', u'54.4')
					('0:22:27', u'18.4688')
					('0:25:04', u'18.6624')
					('0:27:00', u'19.44')
					('0:31:02', u'19.116')
	part2_correct_attempt
					['9:10:30', u'sqrt(162*.82*(1-.82))']

17 Student ID:c1wei

	first_attempt
					2015-11-05 05:17:04
	part1_correct_attempt
					['0:00:00', u'.83*286']
	part2_incorrect_attempt
					('0:00:10', u'286-237.38')
					('0:00:34', u'sqrt(.83*286)')
					('0:00:40', u'sqrt(.83*250)')
					('0:00:49', u'sqrt(.83*.83*286)')
					('0:00:53', u'sqrt(.83*286)')
					('0:01:47', u'sqrt(.83*237.38)')
					('0:01:52', u'sqrt(.83*237)')
					('0:04:22', u'sqrt(237.38)')
					('0:04:57', u'sqrt(250-237.38)')
					('0:05:03', u'sqrt(286-237.38)')
					('0:05:11', u'sqrt(286-250)')
					('0:05:33', u'286-237.38')
					('0:05:39', u'250-237.38')
					('0:05:58', u'sqrt(250-237.38)')
					('0:06:05', u'sqrt(286-237.38)')
					('0:07:13', u'sqrt((1/12)*286)')
					('0:07:22', u'sqrt((1/12)*250)')
	part2_correct_attempt
					['0:10:15', u'sqrt(237.38*.17)']

18 Student ID:mitopete

	first_attempt
					2015-11-07 00:21:21
	part1_correct_attempt
					['0:00:00', u'0.84(241)']
	part2_incorrect_attempt
					('0:03:16', u'(1/4*241)^(1/2)')
					('0:04:33', u'((1/4)*(0.84(241)))^(1/2)')
					('0:06:44', u'(0.25*241)^(1/2)')
					('0:07:07', u'(0.25*220)^(1/2)')
					('0:08:51', u'(0.25*241)^(1/2)')
					('0:14:07', u'(0.25*220)^(1/2)')
					('0:14:13', u'(0.25*241)^(1/2)')
					('0:14:50', u'(0.25*0.84(241))^(1/2)')
					('0:16:59', u'(0.25*0.84(220))^(1/2)')
	part2_correct_attempt
					['0:25:08', u'(241*0.84*(1-0.84))^(1/2)']

19 Student ID:ggaddi

	first_attempt
					2015-11-05 05:47:26
	part1_correct_attempt
					['0:00:00', u'0.8*266']
	part2_incorrect_attempt
					('12:15:01', u'(266-(0.8*266))/(sqrt((4/25)*266))')
	part2_correct_attempt
					['12:15:32', u'(sqrt((4/25)*266))']

20 Student ID:jit002

	first_attempt
					2015-11-06 06:51:51
	part1_correct_attempt
					['0:00:00', u'337*0.87']
	part2_incorrect_attempt
					('0:04:52', u'337*0.85*(1-0.85)')
					('0:05:07', u'337*0.87*(1-0.87)')
	part2_correct_attempt
					['0:05:36', u'(337*0.87*(1-0.87))^0.5']

21 Student ID:b3hwang

	first_attempt
					2015-11-05 09:54:14
	part1_correct_attempt
					['0:00:00', u'174 * .85']
	part2_incorrect_attempt
					('0:04:32', u'(174-147.9)^2')
	part2_correct_attempt
					['10:28:28', u'((.85*174)(1-.85))^(1/2)']

22 Student ID:jag028

	first_attempt
					2015-11-03 21:55:17
	part1_correct_attempt
					['0:00:00', u'322*.8']
	part2_incorrect_attempt
					('0:00:41', u'sqrt(322*.8)')
	part2_correct_attempt
					['0:01:06', u'sqrt((1-.8)322*.8)']

23 Student ID:lguintu

	first_attempt
					2015-11-03 05:41:25
	part1_correct_attempt
					['0:00:00', u'244*.85']
	part2_incorrect_attempt
					('0:00:26', u'244*.85*.15')
	part2_correct_attempt
					['0:01:43', u'(244*.85*.15)^(1/2)']

24 Student ID:c1sorian

	first_attempt
					2015-11-05 01:11:52
	part1_correct_attempt
					['0:00:00', u'.88*376']
	part2_incorrect_attempt
					('0:06:10', u'((1324314/25)/387)^.5')
					('0:35:03', u'0.5')
					('0:35:08', u'0.05')
					('0:35:14', u'0.005')
	part2_correct_attempt
					['1 day, 2:59:08', u'(.88*.12*376)^.5']

25 Student ID:atorr

	first_attempt
					2015-11-06 00:45:21
	part1_correct_attempt
					['0:00:00', u'386 * .83']
	part2_incorrect_attempt
					('0:00:39', u'320.38')
					('0:01:16', u'320.38 ^ 0.5')
					('0:01:27', u'320.38^2')
					('0:01:56', u'(368 - 320.38)')
					('0:02:03', u'(368 - 320.38)^0.5')
					('0:02:09', u'(368 - 320.38)^2')
					('0:02:15', u'(368 - 320.38)^0.5')
					('0:04:51', u'((368 - 320.38)^2)^0.5')

26 Student ID:cprafull

	first_attempt
					2015-11-05 09:20:11
	part1_correct_attempt
					['0:00:00', u'207*.8']
	part2_incorrect_attempt
					('0:00:46', u'sqrt(165.6)')
					('0:08:38', u'180-165.6')
					('0:09:05', u'(180-165.6)^2')
					('0:10:13', u'(207-165.6)')
					('0:25:36', u'180-165.6')
					('0:25:47', u'(180-165.6)/180')
					('0:26:05', u'(180-165.6)/165.6')
					('0:26:14', u'207 - 165.6')
	part2_correct_attempt
					['17:59:41', u'sqrt((207*.8) * (1-.8))']

27 Student ID:krau

	first_attempt
					2015-11-04 19:56:43
	part1_correct_attempt
					['0:00:00', u'.81*327']
	part2_incorrect_attempt
					('0:01:33', u'(327-.81*327)^2')
					('0:03:36', u'((327-.81*327)^2 + (327-290)^2) / 2')
					('0:05:41', u'sqrt(((327-.81*327)^2 + (327-290)^2) / 2)')
					('0:06:05', u'sqrt(((327-.81*327)^2 + (290-.81*327)^2) / 2)')
	part2_correct_attempt
					['7:40:32', u'sqrt(327*.81*.19)']

28 Student ID:crmirand

	first_attempt
					2015-11-03 06:45:04
	part1_correct_attempt
					['0:00:00', u'.86*208']
	part2_incorrect_attempt
					('0:00:51', u'(.86*208*.86*.14)^1/2')
	part2_correct_attempt
					['0:01:41', u'(.86*208*.14)^.5']

29 Student ID:beyounge

	first_attempt
					2015-10-30 06:38:28
	part1_correct_attempt
					['0:00:00', u'0.86 * 356']
	part2_incorrect_attempt
					('0:03:55', u'sqrt(0.86 * 356)')
					('0:07:53', u'sqrt((330 ^ 2) - (0.86 * 356) ^ 2)')
					('0:08:18', u'sqrt(330 - (0.86 * 356))')
	part2_correct_attempt
					['0:20:40', u'sqrt((0.86 * 356) - (0.86^2 * 356))']

30 Student ID:jhw015

	first_attempt
					2015-11-04 21:36:37
	part1_correct_attempt
					['0:00:00', u'0.85*201']
	part2_incorrect_attempt
					('0:01:23', u'50.61')
					('0:01:56', u'50.6236110921')
	part2_correct_attempt
					['0:02:47', u'sqrt(201 * 0.85(0.15))']

31 Student ID:t1tran

	first_attempt
					2015-11-04 01:18:46
	part1_correct_attempt
					['0:00:00', u'177(83/100)']
	part2_incorrect_attempt
					('0:00:00', u'177(83/100)(1-83/100)')
					('0:00:32', u'160(83/100)(1-83/100)')
	part2_correct_attempt
					['0:01:30', u'sqrt(177(83/100)(1-83/100))']

32 Student ID:dsmonaha

	first_attempt
					2015-11-04 18:20:29
	part1_correct_attempt
					['0:00:00', u'361*.88']
	part2_incorrect_attempt
					('0:06:53', u'41.5')
					('0:08:17', u'43.32')
					('2 days, 2:59:56', u'43.32')
					('2 days, 3:05:20', u'1876.62')
					('2 days, 3:06:49', u'45.0378')

33 Student ID:krkelkar

	first_attempt
					2015-11-02 23:25:52
	part1_correct_attempt
					['0:00:00', u'209 * .86']
	part2_incorrect_attempt
					('0:00:00', u'209 * .86 * (1-.86)')
	part2_correct_attempt
					['0:00:31', u'sqrt( 209 * .86 * (1-.86) )']

34 Student ID:akg009

	first_attempt
					2015-11-06 18:46:09
	part1_correct_attempt
					['0:00:00', u'320.88']
	part2_incorrect_attempt
					('0:03:42', u'0.018757')
					('0:04:22', u'0.02046578')
					('0:06:16', u'.019882')
	part2_correct_attempt
					['3:19:16', u'sqrt(.16*.84*382)']

35 Student ID:jtfrankl

	first_attempt
					2015-11-06 19:14:23
	part1_correct_attempt
					['0:00:00', u'.8*370']
	part2_incorrect_attempt
					('0:02:45', u'50**.5')
					('0:03:52', u'sqrt(.8*370**2-50**2)')

36 Student ID:cstringh

	first_attempt
					2015-11-04 07:34:15
	part1_correct_attempt
					['0:00:00', u'392 * .89']
	part2_incorrect_attempt
					('0:00:25', u'sqrt(392 * .89)')
	part2_correct_attempt
					['0:02:15', u'sqrt (392 * .89 * (1 - .89))']

37 Student ID:v4sharma

	first_attempt
					2015-11-05 23:44:05
	part1_correct_attempt
					['0:00:00', u'209.6']
	part2_incorrect_attempt
					('0:01:52', u'(262)(0.8)(0.2)')
					('0:02:00', u'(230)(0.8)(0.2)')
	part2_correct_attempt
					['22:48:52', u'sqrt((262)(.80)(.20))']

38 Student ID:yjshin

	first_attempt
					2015-11-06 23:35:28
	part1_correct_attempt
					['0:00:00', u'(314.5)']
	part2_incorrect_attempt
					('0:01:31', u'sqrt(314.5)')
					('0:02:41', u'sqrt(314.5^2)')
					('0:11:59', u'sqrt(314.5^2)')
					('0:14:24', u'sqrt((1-314.5)^2)')
					('0:20:39', u'2^2(314.5)+2^2*314.5')
					('0:20:59', u'sqrt(2^2(314.5)+2^2*314.5)')

39 Student ID:dcastlem

	first_attempt
					2015-11-03 01:28:34
	part1_correct_attempt
					['0:00:00', u'182*.8']
	part2_incorrect_attempt
					('0:01:22', u'sqrt(.8*.2*160)')
	part2_correct_attempt
					['0:01:34', u'sqrt(.8*.2*182)']

40 Student ID:v3doan

	first_attempt
					2015-11-07 00:45:23
	part1_correct_attempt
					['0:00:00', u'297 * .87']
	part2_incorrect_attempt
					('0:01:57', u'270 - 297 * .87')
	part2_correct_attempt
					['0:02:46', u'sqrt ( .87 * .13 * 297)']

41 Student ID:wmiao

	first_attempt
					2015-11-06 17:12:50
	part1_correct_attempt
					['0:00:00', u'166*0.86']
	part2_incorrect_attempt
					('0:00:00', u'(166*0.86)^0.5')
	part2_correct_attempt
					['0:00:29', u'(166*0.86*0.14)^0.5']

42 Student ID:lywong

	first_attempt
					2015-11-02 04:55:04
	part1_correct_attempt
					['0:00:00', u'348.88']
	part2_incorrect_attempt
					('0:01:02', u'30.49044')
					('3 days, 18:26:30', u'43.12')
					('3 days, 18:27:45', u'(1713.7472)^(1/2)')
					('3 days, 18:27:53', u'sqrt(1)')
	part2_correct_attempt
					['3 days, 18:56:59', u'sqrt(392*0.89(1-0.89))']

43 Student ID:jix029

	first_attempt
					2015-11-01 21:03:16
	part1_correct_attempt
					['0:00:00', u'162*.81']
	part2_incorrect_attempt
					('0:02:46', u'162*.81(1-.81)')
	part2_correct_attempt
					['0:03:29', u'(162*.81(1-.81))^.5']

44 Student ID:abasu

	first_attempt
					2015-11-05 06:01:45
	part1_correct_attempt
					['0:00:00', u'317*0.83']
	part2_incorrect_attempt
					('0:01:12', u'317*0.83*0.17')
					('0:01:30', u'263.11*0.83*0.83*0.17')
	part2_correct_attempt
					['0:04:38', u'(317*0.83*0.17)^0.5']

45 Student ID:acvuong

	first_attempt
					2015-11-05 01:20:45
	part1_correct_attempt
					['0:00:00', u'0.86*195']
	part2_incorrect_attempt
					('0:00:00', u'.86*195*.14')
	part2_correct_attempt
					['0:00:12', u'(.86*195*.14)^0.5']

46 Student ID:thk002

	first_attempt
					2015-11-05 06:59:05
	part1_correct_attempt
					['0:00:00', u'174*.82']
	part2_incorrect_attempt
					('0:00:13', u'sqrt(174*.82)')
	part2_correct_attempt
					['0:00:29', u'sqrt(174*.82*.18)']

47 Student ID:t2li

	first_attempt
					2015-11-06 03:22:11
	part1_correct_attempt
					['0:00:00', u'217 * 0.83']
	part2_incorrect_attempt
					('0:01:48', u'sqrt(0.83*0.17/217)')
	part2_correct_attempt
					['0:05:10', u'sqrt(0.83*0.17*217)']

48 Student ID:ksmurlo

	first_attempt
					2015-11-05 07:02:28
	part1_correct_attempt
					['0:00:00', u'370*.83']
	part2_incorrect_attempt
					('8:15:09', u'370*.83*.17')
	part2_correct_attempt
					['8:15:58', u'sqrt(370*.83*.17)']

49 Student ID:ttimmons

	first_attempt
					2015-11-03 18:51:59
	part1_correct_attempt
					['0:00:00', u'165*0.87']
	part2_incorrect_attempt
					('0:00:26', u'sqrt(165^2*0.87-[165*0.87]^2)')
					('0:04:38', u'165*(0.87)*(1-0.87)')
	part2_correct_attempt
					['0:04:45', u'sqrt(165*(0.87)*(1-0.87))']

50 Student ID:jeqin

	first_attempt
					2015-11-05 10:41:04
	part1_correct_attempt
					['0:00:00', u'.88*320']
	part2_incorrect_attempt
					('0:14:06', u'sqrt((320^2)*0.88 - (0.88*320)^2)')
	part2_correct_attempt
					['0:15:58', u'sqrt(0.88*320*(1-0.88))']

51 Student ID:jblynch

	first_attempt
					2015-11-04 20:33:29
	part1_correct_attempt
					['0:00:00', u'.87*276']
	part2_incorrect_attempt
					('0:01:26', u'260 - (.87*276)')
					('0:01:43', u'276 - (.87*276)')
					('0:02:16', u'.87(260 - (.87*276))')
					('0:04:35', u'(260 - (.87*276))^2')
					('9:18:54', u'sqrt(.87*260*13)')
					('9:23:12', u'276/4')
					('9:36:03', u'sqrt(.87*(267-240.12)^2)')
					('9:36:24', u'.87*(267-240.12)')
					('9:36:32', u'.87*(267-240.12)^2')
	part2_correct_attempt
					['9:47:31', u'sqrt((.87)(276)(1-.87))']

52 Student ID:ganajera

	first_attempt
					2015-11-01 00:09:59
	part1_correct_attempt
					['0:00:00', u'175*.89']
	part2_incorrect_attempt
					('0:03:54', u'sqrt(2998.1875)')
	part2_correct_attempt
					['5 days, 5:20:32', u'sqrt(.89*.11*175)']

53 Student ID:tol003

	first_attempt
					2015-11-03 23:35:13
	part1_correct_attempt
					['0:00:00', u'167*.82']
	part2_incorrect_attempt
					('0:02:48', u'4.946479')
	part2_correct_attempt
					['0:03:55', u'sqrt(167*.82(1-.82))']

54 Student ID:hachrist

	first_attempt
					2015-11-05 07:56:14
	part1_correct_attempt
					['0:00:00', u'0.82 * 367']
	part2_incorrect_attempt
					('0:08:54', u'sqrt((367-300.94)^2 + (320-300.94)^2)/2')
					('0:09:13', u'sqrt(((367-300.94)^2 + (320-300.94)^2)/2)')
					('13:16:36', u'sqrt((320-300.94)^2 + (367-300.94)^2)')
					('13:18:07', u'sqrt((320-300.94)^2)')
					('14:41:21', u'sqrt(0.82(1-0.82)*320)')
	part2_correct_attempt
					['14:41:46', u'sqrt(0.82(1-0.82)*367)']

55 Student ID:yeh013

	first_attempt
					2015-11-05 06:21:17
	part1_correct_attempt
					['0:00:00', u'347*81/100']
	part2_incorrect_attempt
					('0:43:41', u'300-281.7')
					('0:44:05', u'300*81/100')
					('0:44:19', u'(300*81/100)^(1/2)')
	part2_correct_attempt
					['0:58:54', u'(347*81/100*19/100)^(1/2)']

56 Student ID:arvenega

	first_attempt
					2015-11-06 23:42:59
	part1_correct_attempt
					['0:00:00', u'202*.8']
	part2_incorrect_attempt
					('0:00:00', u'((202*.8)*(1-.8))6(1/2)')
	part2_correct_attempt
					['0:00:56', u'((202*.8)*(1-.8))^(1/2)']

57 Student ID:csl030

	first_attempt
					2015-11-06 00:26:22
	part1_correct_attempt
					['0:00:00', u'347 * .8']
	part2_incorrect_attempt
					('0:00:23', u'(347 - 277.6)^2')
					('0:00:44', u'347 - 277.6')
					('0:02:47', u'sqrt((300 - 277.6)^2)')
	part2_correct_attempt
					['0:07:25', u'sqrt(277.6 * .2)']

58 Student ID:volim

	first_attempt
					2015-11-04 23:36:58
	part1_correct_attempt
					['0:00:00', u'(317)*.84']
	part2_incorrect_attempt
					('0:00:35', u'(.25*317)^(1/2)')
					('0:01:47', u'(.84)^(1/2)')
					('0:02:03', u'(.25)^(1/2)')
					('0:02:15', u'(.25*317)^(1/2)')
					('0:03:41', u'317-((317)*.84)')
					('0:05:48', u'(317)*.84')
					('0:06:00', u'290-((317)*.84)')
					('0:10:41', u'(.25)^(1/2)')
					('0:10:50', u'(.5)')
	part2_correct_attempt
					['0:23:08', u'[(((317)*.84)*(1-.84))^(1/2)]']

59 Student ID:cagatep

	first_attempt
					2015-11-05 07:56:02
	part1_correct_attempt
					['0:00:00', u'249 * .86']
	part2_incorrect_attempt
					('0:06:43', u'230-214.14')
					('1 day, 11:58:04', u'249 * .86 * .14')
	part2_correct_attempt
					['1 day, 11:58:15', u'sqrt(249 * .86 * .14)']

60 Student ID:ytc012

	first_attempt
					2015-11-05 22:08:55
	part1_correct_attempt
					['0:00:00', u'0.85*369']
	part2_incorrect_attempt
					('0:00:56', u'sqrt(((369-313.65)^2 + (340-313.65)^2)/2)')
					('0:02:02', u'sqrt(((369-0.85*369)^2 + (340-0.85*369)^2)/2)')
	part2_correct_attempt
					['0:52:08', u'sqrt(0.85(1-0.85)369)']

61 Student ID:yig015

	first_attempt
					2015-11-05 11:03:16
	part1_correct_attempt
					['0:00:00', u'217*0.87']
	part2_incorrect_attempt
					('0:03:09', u'217*0.87*0.13')
	part2_correct_attempt
					['0:04:55', u'4.954058942']

62 Student ID:jfalcone

	first_attempt
					2015-11-05 05:59:21
	part1_correct_attempt
					['0:00:00', u'.81 * 339']
	part2_incorrect_attempt
					('0:01:38', u'sqrt(.81 * 339)')
	part2_correct_attempt
					['0:04:12', u'sqrt(.81 * 339 * (1 -.81))']

63 Student ID:eyhu

	first_attempt
					2015-10-30 08:44:05
	part1_correct_attempt
					['0:00:00', u'275*(0.84)']
	part2_incorrect_attempt
					('0:00:00', u'275*(0.84)*(1-0.84)')
	part2_correct_attempt
					['0:01:01', u'(275*(0.84)*(1-0.84))^(1/2)']

64 Student ID:ppanourg

	first_attempt
					2015-11-06 21:30:59
	part1_correct_attempt
					['0:00:00', u'378*.88']
	part2_incorrect_attempt
					('0:09:32', u'sqrt(((378)^2(.88)) - ((378)(.88))^2)')
					('0:11:55', u'378 - 378*.88')
					('0:12:13', u'350 - 378*.88')
	part2_correct_attempt
					['0:13:50', u'sqrt((378*.88)(1 - .88))']

65 Student ID:rohan

	first_attempt
					2015-11-07 00:25:00
	part1_correct_attempt
					['0:00:00', u'199*.86']
	part2_incorrect_attempt
					('0:00:14', u'sqrt(199*.86)')

66 Student ID:rwthomps

	first_attempt
					2015-11-06 21:59:09
	part1_correct_attempt
					['0:00:00', u'376 * .85']
	part2_incorrect_attempt
					('0:48:13', u'sqrt(0.5 * 0.5 *376)')
					('0:49:30', u'sqrt(0.5 *376 * .85)')
					('0:50:56', u'sqrt(0.5 *0.5 * 340)')
					('0:51:22', u'sqrt(376 * .85)')
					('0:54:05', u'sqrt(376 * 0.25)')
					('0:55:35', u'sqrt(340 * (1/340) * (1 - (1/340)))')
					('1:04:05', u'sqrt(340 * .25)')
	part2_correct_attempt
					['1:07:51', u'sqrt(376 * .85 * .15)']

67 Student ID:vsosnovs

	first_attempt
					2015-11-05 22:13:07
	part1_correct_attempt
					['0:00:00', u'.80(155)']
	part2_incorrect_attempt
					('0:00:49', u'140-124')
					('0:00:56', u'155-124')
					('0:01:01', u'155-124/2')
					('0:01:10', u'(155-124)/2')

68 Student ID:jdeon

	first_attempt
					2015-11-04 23:41:21
	part1_correct_attempt
					['0:00:00', u'301']
	part2_incorrect_attempt
					('0:01:24', u'121.445')
	part2_correct_attempt
					['0:02:42', u'6.4915']

69 Student ID:j6quach

	first_attempt
					2015-11-05 12:06:09
	part1_correct_attempt
					['0:00:00', u'250.75']
	part2_incorrect_attempt
					('0:03:50', u'14.75')
	part2_correct_attempt
					['0:08:45', u'sqrt(295*.85*.15)']

70 Student ID:gsrandha

	first_attempt
					2015-11-05 09:01:50
	part1_correct_attempt
					['0:00:00', u'219 * .86']
	part2_incorrect_attempt
					('0:02:20', u'sqrt(219 * .86 * .14)21^2/2')
	part2_correct_attempt
					['0:02:28', u'sqrt(219 * .86 * .14)']

71 Student ID:yypan

	first_attempt
					2015-11-03 01:31:12
	part1_correct_attempt
					['0:00:00', u'390*0.85']
	part2_incorrect_attempt
					('0:05:13', u'sqrt(0.85-0.85^2)')
					('0:16:47', u'sqrt((0.85*0.15)/360)')
					('0:16:57', u'sqrt((0.85*0.15)/390)')
	part2_correct_attempt
					['0:18:36', u'sqrt((390*0.85)*(390*0.15)/390)']

72 Student ID:jhc010

	first_attempt
					2015-11-06 11:07:36
	part1_correct_attempt
					['0:00:00', u'277*.82']
	part2_incorrect_attempt
					('0:00:42', u'sqrt(.18/(.82^2))')
	part2_correct_attempt
					['0:01:25', u'sqrt(.82*.18*277)']

73 Student ID:agarango

	first_attempt
					2015-11-06 00:02:31
	part1_correct_attempt
					['0:00:00', u'284*0.82']
	part2_incorrect_attempt
					('0:00:17', u'sqrt(284*0.82)')
					('0:00:26', u'sqrt(284)')
					('9:05:59', u'sqrt((1/284)(284*.82))')
					('9:06:48', u'sqrt((1/284)(284*.82)^2)')
					('9:07:51', u'sqrt((1/284)(284-(284*.82))^2)')
					('9:10:45', u'sqrt((1/284)(284-232.88)^2)')
					('9:14:46', u'sqrt((1/283)(284-232.88)^2)')
					('9:16:25', u'sqrt((1/260)(284-232.88)^2)')
					('9:16:39', u'sqrt((1/260)(260-232.88)^2)')
					('9:21:19', u'sqrt(260-232.88)')
					('9:21:27', u'sqrt(284-232.88)')
					('9:25:01', u'sqrt(232.88)')
					('9:25:07', u'sqrt(232.88^2)')
					('9:28:11', u'sqrt((260-232.88)^2)')
					('19:27:14', u'sqrt((1/284)(2642938506/625))')
					('19:52:34', u'sqrt(260/232.88)')
					('19:52:40', u'sqrt(260-232.88)')
					('19:52:53', u'sqrt((260-232.88)^2)')
					('19:53:23', u'sqrt(((260-232.88)^2)/284)')
					('23:55:31', u'sqrt(((260-232.88)^2))/284')
					('23:55:40', u'sqrt(((260-232.88)))/284')
					('1 day, 0:00:30', u'sqrt(232.88*260)/284')
					('1 day, 0:00:38', u'sqrt(232.88*284)/284')
					('1 day, 0:02:56', u'sqrt(284-232.88)/284')
					('1 day, 0:03:15', u'sqrt((284-232.88)*284)/284')
					('1 day, 0:04:08', u'sqrt((260-232.88)*284)/284')
					('1 day, 0:04:16', u'sqrt((260-232.88)*284)/260')
					('1 day, 0:21:56', u'sqrt((284-232.88)*284)/284')
					('1 day, 0:27:26', u'sqrt(((284-232.88)*284)/284)')
					('1 day, 0:55:19', u'3.039')

74 Student ID:zhz159

	first_attempt
					2015-11-06 00:01:34
	part1_correct_attempt
					['0:00:00', u'322.26']
	part2_incorrect_attempt
					('0:00:00', u'58.0068')
	part2_correct_attempt
					['0:27:24', u'7.6162195']

75 Student ID:ajabasa

	first_attempt
					2015-11-05 22:37:30
	part1_correct_attempt
					['0:00:00', u'.81*222']
	part2_incorrect_attempt
					('0:01:52', u'((179.82-222))^2/222')
					('0:03:08', u'(.81*.29*222)^(1/2)')
					('0:03:21', u'(.81*.29*200)^(1/2)')
	part2_correct_attempt
					['0:03:30', u'(.81*.19*222)^(1/2)']

76 Student ID:aadhakal

	first_attempt
					2015-11-05 22:47:50
	part1_correct_attempt
					['0:00:00', u'3.26*84']
	part2_incorrect_attempt
					('0:00:11', u'sqrt(3.26*84)')
	part2_correct_attempt
					['0:01:07', u'sqrt(3.26*84*0.16)']

77 Student ID:dpereira

	first_attempt
					2015-11-05 22:56:10
	part1_correct_attempt
					['0:00:00', u'323*.82']
	part2_incorrect_attempt
					('0:00:51', u'sqrt((323^2 * .82) - (323 * .82)^2)')
	part2_correct_attempt
					['0:02:29', u'sqrt((.82 * (1-.82) * 323))']

78 Student ID:hmshah

	first_attempt
					2015-11-05 09:54:46
	part1_correct_attempt
					['0:00:00', u'366*.87']
	part2_incorrect_attempt
					('0:00:30', u'(366*.87) * .13')
	part2_correct_attempt
					['0:00:47', u'sqrt(366*.87* .13)']

79 Student ID:lahawkin

	first_attempt
					2015-11-04 04:59:33
	part1_correct_attempt
					['0:00:00', u'(89/100)303']
	part2_incorrect_attempt
					('0:00:23', u'((89/100)303)^1/2')
					('0:00:35', u'((89/100)303)^(1/2)')
					('0:08:41', u'(((89/100)303-290)^2)^1/2')
					('1 day, 14:51:21', u'(((.89)303-290)^2)(1/2)')
					('1 day, 14:51:33', u'(((.89)303-290)^2)^(1/2)')
					('1 day, 14:52:18', u'((((.89)303*290)^2))^(1/2)')
	part2_correct_attempt
					['2 days, 0:07:02', u'((89/100)(303)(.11))^(1/2)']

80 Student ID:aordookh

	first_attempt
					2015-11-06 06:52:05
	part1_correct_attempt
					['0:00:00', u'290-(.89*18)']
	part2_incorrect_attempt
					('0:01:47', u'308-290')
					('0:02:51', u'.11(290)')
					('0:03:18', u'.11(290)/2')
					('0:05:08', u'(.11(.89)290)^(1/2)')
					('0:12:32', u'(290-(290-(.89*18)))/.89')
	part2_correct_attempt
					['0:17:08', u'(308*.89*.11)^(1/2)']

81 Student ID:kquong

	first_attempt
					2015-11-04 23:56:32
	part1_correct_attempt
					['0:00:00', u'264 * .89']
	part2_incorrect_attempt
					('0:01:39', u'264- 234.96')
					('0:03:16', u'sqrt(((264- 234.96)^2/250))')
	part2_correct_attempt
					['0:05:35', u'sqrt(264 * .89 * .11)']

82 Student ID:kgrozav

	first_attempt
					2015-11-06 08:10:44
	part1_correct_attempt
					['0:00:00', u'284*.89']
	part2_incorrect_attempt
					('0:00:26', u'284*.89*11')
	part2_correct_attempt
					['0:00:44', u'sqrt(284*.89*.11)']

83 Student ID:xweng

	first_attempt
					2015-11-06 01:16:42
	part1_correct_attempt
					['0:00:00', u'185*0.86']
	part2_incorrect_attempt
					('0:00:13', u'185*0.86*0.14')
					('0:00:22', u'170*0.86*0.14')
	part2_correct_attempt
					['0:00:59', u'4.7195']

84 Student ID:c3chung

	first_attempt
					2015-11-06 22:52:08
	part1_correct_attempt
					['0:00:00', u'.81(281)']
	part2_incorrect_attempt
					('0:00:00', u'sqrt(.81(281)/25)')
					('0:02:09', u'sqrt((227.61-250)^2/281)')
					('0:02:15', u'sqrt((227.61-250)^2/280)')
					('1:39:33', u'(250-227.61)')
					('1:41:05', u'(250-227.61)^2')
					('1:42:45', u'(281-227.61)^2')
					('1:42:50', u'(281-227.61)')
					('1:44:36', u'(250-202.5)')
					('1:45:06', u'(227.61-202.5)')
	part2_correct_attempt
					['1:48:57', u'sqrt(281*.81*.19)']

85 Student ID:ajvanega

	first_attempt
					2015-11-05 19:27:27
	part1_correct_attempt
					['0:00:00', u'161*.81']
	part2_incorrect_attempt
					('0:13:07', u'((150-(161*.81))^2)/161')
					('0:13:24', u'((150-(161*.81))^2)/150')
					('0:15:07', u'((161-(161*.81))^2)/161')
					('0:19:23', u'(161-(161*.81))')
	part2_correct_attempt
					['7:03:16', u'sqrt((161*.81)*(1-.81))']

86 Student ID:jmiclat

	first_attempt
					2015-11-06 09:32:38
	part1_correct_attempt
					['0:00:00', u'.82*266']
	part2_incorrect_attempt
					('0:00:10', u'218.12^2')
					('0:01:57', u'(266-(.82*266))^2')
					('14:23:17', u'sqrt(1-0.82)0.82*266')
	part2_correct_attempt
					['14:23:37', u'sqrt[(1-0.82)0.82*266]']

87 Student ID:mtrafeca

	first_attempt
					2015-11-05 21:44:19
	part1_correct_attempt
					['0:00:00', u'223*.89']
	part2_incorrect_attempt
					('0:01:56', u'.89*.19*223')
					('0:02:15', u'sqrt(.89*.19*223)')
	part2_correct_attempt
					['0:02:24', u'sqrt(.89*.11*223)']

88 Student ID:syc078

	first_attempt
					2015-11-05 03:02:30
	part1_correct_attempt
					['0:00:00', u'0.8*393']
	part2_incorrect_attempt
					('0:00:25', u'393-(0.8*393)')
					('0:00:35', u'(393-(0.8*393))^2')
	part2_correct_attempt
					['23:27:49', u'sqrt((0.8*393)*(1-0.8))']

89 Student ID:j2phung

	first_attempt
					2015-11-05 18:52:28
	part1_correct_attempt
					['0:00:00', u'.86 * 330']
	part2_incorrect_attempt
					('0:29:38', u'(300*(1/2)*(1/2))^(1/2)')
	part2_correct_attempt
					['0:44:21', u'(330*(1-.86)*(.86))^(1/2)']












## Part 3

### (142) Mistake Group ['R.0.1'] of size 142
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|Q((180-185*0.85)/[sqrt(185*0.85*(1-0.85))])	|Q(((185)-(.85 * 185))/(sqrt (185 * .85 * (1 - .85))))	|[('R.0.1', 4.856696408053524, u'sqrt(185*0.85*(1-0.85))', u'sqrt (185 * .85 * (1 - .85))')]	|
|1	|Q((180-185*0.85)/[sqrt(185*0.85*(1-0.85))])	|Q((185-157.25)/(sqrt (185 * .85 * (1 - .85))))	|[('R.0.1', 4.856696408053524, u'sqrt(185*0.85*(1-0.85))', u'sqrt (185 * .85 * (1 - .85))')]	|
|2	|Q((180-185*0.85)/[sqrt(185*0.85*(1-0.85))])	|Q((185-(.85 * 185))/(sqrt (185 * .85 * (1 - .85))))	|[('R.0.1', 4.856696408053524, u'sqrt(185*0.85*(1-0.85))', u'sqrt (185 * .85 * (1 - .85))')]	|
|3	|Q((320-346*0.87)/[sqrt(346*0.87*(1-0.87))])	|Q( 320/ sqrt( (346 * 0.87)(1-0.87)))	|[('R.0.1', 6.255605486281883, u'sqrt(346*0.87*(1-0.87))', u'sqrt( (346 * 0.87)(1-0.87))')]	|
|4	|Q((200-209*0.86)/[sqrt(209*0.86*(1-0.86))])	|Q( (200.5 - 209*.86)/ (sqrt( 209 * .86 * (1-.86) )))	|[('R.0.1', 5.016333322258401, u'sqrt(209*0.86*(1-0.86))', u'sqrt( 209 * .86 * (1-.86) )')]	|
|5	|Q((280-298*0.88)/[sqrt(298*0.88*(1-0.88))])	|Q((298-298*.88)/((298(.88)(.12))^(1/2)))	|[('R.0.1', 5.609705874642627, u'sqrt(298*0.88*(1-0.88))', u'(298(.88)(.12))^(1/2)')]	|
|6	|Q((350-381*0.86)/[sqrt(381*0.86*(1-0.86))])	|Q((351-(0.86*381))/(sqrt(0.86*381*0.14)))	|[('R.0.1', 6.772916653850097, u'sqrt(381*0.86*(1-0.86))', u'sqrt(0.86*381*0.14)')]	|
|7	|Q((160-165*0.87)/[sqrt(165*0.87*(1-0.87))])	|Q([165-165*0.87]/[sqrt(165*(0.87)*(1-0.87))])	|[('R.0.1', 4.319895832077436, u'sqrt(165*0.87*(1-0.87))', u'sqrt(165*(0.87)*(1-0.87))')]	|
|8	|Q((160-165*0.87)/[sqrt(165*0.87*(1-0.87))])	|Phi([165-165*0.87]/[sqrt(165*(0.87)*(1-0.87))])	|[('R.0.1', 4.319895832077436, u'sqrt(165*0.87*(1-0.87))', u'sqrt(165*(0.87)*(1-0.87))')]	|
|9	|Q((160-165*0.87)/[sqrt(165*0.87*(1-0.87))])	|Q([166-165*0.87]/[sqrt(165*(0.87)*(1-0.87))])	|[('R.0.1', 4.319895832077436, u'sqrt(165*0.87*(1-0.87))', u'sqrt(165*(0.87)*(1-0.87))')]	|
|10	|Q((170-172*0.85)/[sqrt(172*0.85*(1-0.85))])	|Q((172-146.2)/sqrt(172*.85*.15))	|[('R.0.1', 4.682947789587239, u'sqrt(172*0.85*(1-0.85))', u'sqrt(172*.85*.15)')]	|
|11	|Q((220-247*0.84)/[sqrt(247*0.84*(1-0.84))])	|Q((247-247*.84)/sqrt(247*.84*.16))	|[('R.0.1', 5.761666425609869, u'sqrt(247*0.84*(1-0.84))', u'sqrt(247*.84*.16)')]	|
|12	|Q((220-247*0.84)/[sqrt(247*0.84*(1-0.84))])	|Q((227-247*.84)/sqrt(247*.84*.16))	|[('R.0.1', 5.761666425609869, u'sqrt(247*0.84*(1-0.84))', u'sqrt(247*.84*.16)')]	|
|13	|Q((240-264*0.83)/[sqrt(264*0.83*(1-0.83))])	|Q(((264 - 240) - (264 * 0.83)) / (264 * 0.83 * (1 - 0.83))^(1/2))	|[('R.0.1', 6.103310577055702, u'sqrt(264*0.83*(1-0.83))', u'(264 * 0.83 * (1 - 0.83))^(1/2)')]	|
|14	|Q((240-264*0.83)/[sqrt(264*0.83*(1-0.83))])	|Phi(((264 - 240) - (264 * 0.83)) / (264 * 0.83 * (1 - 0.83))^(1/2))	|[('R.0.1', 6.103310577055702, u'sqrt(264*0.83*(1-0.83))', u'(264 * 0.83 * (1 - 0.83))^(1/2)')]	|
|15	|Q((240-264*0.83)/[sqrt(264*0.83*(1-0.83))])	|Q(((240 - 264) - (264 * 0.83)) / (264 * 0.83 * (1 - 0.83))^(1/2))	|[('R.0.1', 6.103310577055702, u'sqrt(264*0.83*(1-0.83))', u'(264 * 0.83 * (1 - 0.83))^(1/2)')]	|
|16	|Q((240-264*0.83)/[sqrt(264*0.83*(1-0.83))])	|Q((264 - (264 * 0.83)) / (264 * 0.83 * (1 - 0.83))^(1/2))	|[('R.0.1', 6.103310577055702, u'sqrt(264*0.83*(1-0.83))', u'(264 * 0.83 * (1 - 0.83))^(1/2)')]	|
|17	|Q((240-264*0.83)/[sqrt(264*0.83*(1-0.83))])	|Phi((264 - (264 * 0.83)) / (264 * 0.83 * (1 - 0.83))^(1/2))	|[('R.0.1', 6.103310577055702, u'sqrt(264*0.83*(1-0.83))', u'(264 * 0.83 * (1 - 0.83))^(1/2)')]	|
|18	|Q((350-384*0.84)/[sqrt(384*0.84*(1-0.84))])	|Q((384 - .84 * 384)/sqrt(384 * .84(1 - .84)))	|[('R.0.1', 7.183982182605968, u'sqrt(384*0.84*(1-0.84))', u'sqrt(384 * .84(1 - .84))')]	|
|19	|Q((290-317*0.84)/[sqrt(317*0.84*(1-0.84))])	|Q((317-(317)*.84)/[(((317)*.84)*(1-.84))^(1/2)])	|[('R.0.1', 6.527235249322642, u'sqrt(317*0.84*(1-0.84))', u'(((317)*.84)*(1-.84))^(1/2)')]	|
|20	|Q((350-384*0.84)/[sqrt(384*0.84*(1-0.84))])	|Phi((384 - .84 * 384)/sqrt(384 * .84(1 - .84)))	|[('R.0.1', 7.183982182605968, u'sqrt(384*0.84*(1-0.84))', u'sqrt(384 * .84(1 - .84))')]	|
|21	|Q((290-317*0.84)/[sqrt(317*0.84*(1-0.84))])	|Q((260-((317)*.84))/[(((317)*.84)*(1-.84))^(1/2)])	|[('R.0.1', 6.527235249322642, u'sqrt(317*0.84*(1-0.84))', u'(((317)*.84)*(1-.84))^(1/2)')]	|
|22	|Q((200-226*0.81)/[sqrt(226*0.81*(1-0.81))])	|Q((226*.81)/(sqrt(226*.81*(1-.81))))	|[('R.0.1', 5.897575773146115, u'sqrt(226*0.81*(1-0.81))', u'sqrt(226*.81*(1-.81))')]	|
|23	|Q((250-264*0.89)/[sqrt(264*0.89*(1-0.89))])	|Q((250.5-234.96)/sqrt(264 * .89 * .11))	|[('R.0.1', 5.083856803648191, u'sqrt(264*0.89*(1-0.89))', u'sqrt(264 * .89 * .11)')]	|
|24	|Q((250-264*0.89)/[sqrt(264*0.89*(1-0.89))])	|Q((250.5 - 234.96) / (sqrt(264 * .89 * .11)))	|[('R.0.1', 5.083856803648191, u'sqrt(264*0.89*(1-0.89))', u'sqrt(264 * .89 * .11)')]	|
|25	|Q((210-213*0.89)/[sqrt(213*0.89*(1-0.89))])	|Q((210-.89-213)/(sqrt(.89*213*(1-.89))))	|[('R.0.1', 4.566475665105421, u'sqrt(213*0.89*(1-0.89))', u'sqrt(.89*213*(1-.89))')]	|
|26	|Q((250-264*0.89)/[sqrt(264*0.89*(1-0.89))])	| Q((250.5 - 234.96) / (sqrt(264 * .89 * .11)))	|[('R.0.1', 5.083856803648191, u'sqrt(264*0.89*(1-0.89))', u'sqrt(264 * .89 * .11)')]	|
|27	|Q((250-264*0.89)/[sqrt(264*0.89*(1-0.89))])	| Q((251 - 234.96) / (sqrt(264 * .89 * .11)))	|[('R.0.1', 5.083856803648191, u'sqrt(264*0.89*(1-0.89))', u'sqrt(264 * .89 * .11)')]	|
|28	|Q((200-226*0.8)/[sqrt(226*0.8*(1-0.8))])	|Q((4-(226*(0.8)))/(sqrt((226*(0.8))*(1-(0.8)))))	|[('R.0.1', 6.013318551349163, u'sqrt(226*0.8*(1-0.8))', u'sqrt((226*(0.8))*(1-(0.8)))')]	|
|29	|Q((200-226*0.8)/[sqrt(226*0.8*(1-0.8))])	|Q((10-(226*(0.8)))/(sqrt((226*(0.8))*(1-(0.8)))))	|[('R.0.1', 6.013318551349163, u'sqrt(226*0.8*(1-0.8))', u'sqrt((226*(0.8))*(1-(0.8)))')]	|
|30	|Q((200-226*0.8)/[sqrt(226*0.8*(1-0.8))])	|Q((11-(226*(0.8)))/(sqrt((226*(0.8))*(1-(0.8)))))	|[('R.0.1', 6.013318551349163, u'sqrt(226*0.8*(1-0.8))', u'sqrt((226*(0.8))*(1-(0.8)))')]	|
|31	|Q((200-226*0.8)/[sqrt(226*0.8*(1-0.8))])	|Q((12-(226*(0.8)))/(sqrt((226*(0.8))*(1-(0.8)))))	|[('R.0.1', 6.013318551349163, u'sqrt(226*0.8*(1-0.8))', u'sqrt((226*(0.8))*(1-(0.8)))')]	|
|32	|Q((200-226*0.8)/[sqrt(226*0.8*(1-0.8))])	|Q((13-(226*(0.8)))/(sqrt((226*(0.8))*(1-(0.8)))))	|[('R.0.1', 6.013318551349163, u'sqrt(226*0.8*(1-0.8))', u'sqrt((226*(0.8))*(1-(0.8)))')]	|
|33	|Q((200-226*0.8)/[sqrt(226*0.8*(1-0.8))])	|Q((14-(226*(0.8)))/(sqrt((226*(0.8))*(1-(0.8)))))	|[('R.0.1', 6.013318551349163, u'sqrt(226*0.8*(1-0.8))', u'sqrt((226*(0.8))*(1-(0.8)))')]	|
|34	|Q((200-220*0.81)/[sqrt(220*0.81*(1-0.81))])	|Q(2.8/sqrt(220*.81*.19))	|[('R.0.1', 5.818762755088061, u'sqrt(220*0.81*(1-0.81))', u'sqrt(220*.81*.19)')]	|
|35	|Q((200-220*0.81)/[sqrt(220*0.81*(1-0.81))])	|Q(1.8/sqrt(220*.81*.19))	|[('R.0.1', 5.818762755088061, u'sqrt(220*0.81*(1-0.81))', u'sqrt(220*.81*.19)')]	|
|36	|Q((200-220*0.81)/[sqrt(220*0.81*(1-0.81))])	|Q(2/sqrt(220*.81*.19))	|[('R.0.1', 5.818762755088061, u'sqrt(220*0.81*(1-0.81))', u'sqrt(220*.81*.19)')]	|
|37	|Q((350-378*0.88)/[sqrt(378*0.88*(1-0.88))])	|Q((((28) - ((378)-(378*.88)))/((.88*378)(1-.88))^(.5)))	|[('R.0.1', 6.317974358922328, u'sqrt(378*0.88*(1-0.88))', u'((.88*378)(1-.88))^(.5)')]	|
|38	|Q((200-220*0.81)/[sqrt(220*0.81*(1-0.81))])	|Q((.81*220-200)/sqrt(220*.81*.19))	|[('R.0.1', 5.818762755088061, u'sqrt(220*0.81*(1-0.81))', u'sqrt(220*.81*.19)')]	|
|39	|Q((170-182*0.83)/[sqrt(182*0.83*(1-0.83))])	|Q((182-170)/5.06756)	|[('R.0.1', 5.067563517115499, u'sqrt(182*0.83*(1-0.83))', u'5.06756')]	|
|40	|Q((170-182*0.83)/[sqrt(182*0.83*(1-0.83))])	|Q((182-151.06)/5.06756)	|[('R.0.1', 5.067563517115499, u'sqrt(182*0.83*(1-0.83))', u'5.06756')]	|
|41	|Q((260-276*0.87)/[sqrt(276*0.87*(1-0.87))])	|Q((261 - 240.12)/5.58709)	|[('R.0.1', 5.5870922670025776, u'sqrt(276*0.87*(1-0.87))', u'5.58709')]	|
|42	|Q((200-226*0.8)/[sqrt(226*0.8*(1-0.8))])	|Q((226-(226*(0.8)))/sqrt((226*(0.8))*(1-(0.8))))	|[('R.0.1', 6.013318551349163, u'sqrt(226*0.8*(1-0.8))', u'sqrt((226*(0.8))*(1-(0.8)))')]	|
|43	|Q((200-226*0.8)/[sqrt(226*0.8*(1-0.8))])	|Q(((201)-(226*(0.8)))/(sqrt((226*(0.8))*(1-(0.8)))))	|[('R.0.1', 6.013318551349163, u'sqrt(226*0.8*(1-0.8))', u'sqrt((226*(0.8))*(1-(0.8)))')]	|
|44	|Q((310-340*0.87)/[sqrt(340*0.87*(1-0.87))])	|Q((340-340*0.87)/(340*0.87*0.13)^0.5)	|[('R.0.1', 6.201128929477277, u'sqrt(340*0.87*(1-0.87))', u'(340*0.87*0.13)^0.5')]	|
|45	|Q((310-340*0.88)/[sqrt(340*0.88*(1-0.88))])	|Q((311-299.2)/5.99199)	|[('R.0.1', 5.991994659543681, u'sqrt(340*0.88*(1-0.88))', u'5.99199')]	|
|46	|Q((300-334*0.84)/[sqrt(334*0.84*(1-0.84))])	|Phi((334-0.84*334)/sqrt(0.84(1-0.84)334))	|[('R.0.1', 6.6999701491872345, u'sqrt(334*0.84*(1-0.84))', u'sqrt(0.84(1-0.84)334)')]	|
|47	|Q((300-334*0.84)/[sqrt(334*0.84*(1-0.84))])	|Phi((334-0.84*330)/sqrt(0.84(1-0.84)334))	|[('R.0.1', 6.6999701491872345, u'sqrt(334*0.84*(1-0.84))', u'sqrt(0.84(1-0.84)334)')]	|
|48	|Q((230-266*0.8)/[sqrt(266*0.8*(1-0.8))])	|Q((266-0.8*266)/(sqrt((4/25)*266)))	|[('R.0.1', 6.523802572120036, u'sqrt(266*0.8*(1-0.8))', u'sqrt((4/25)*266)')]	|
|49	|Q((290-320*0.86)/[sqrt(320*0.86*(1-0.86))])	|Q(30/6.20709)	|[('R.0.1', 6.207092717206663, u'sqrt(320*0.86*(1-0.86))', u'6.20709')]	|
|50	|Q((290-320*0.86)/[sqrt(320*0.86*(1-0.86))])	|Q(31/6.20709)	|[('R.0.1', 6.207092717206663, u'sqrt(320*0.86*(1-0.86))', u'6.20709')]	|
|51	|Q((300-330*0.86)/[sqrt(330*0.86*(1-0.86))])	|Phi((330.5-(.86 * 330))/((330*(1-.86)*(.86))^(1/2)))	|[('R.0.1', 6.303332451965389, u'sqrt(330*0.86*(1-0.86))', u'(330*(1-.86)*(.86))^(1/2)')]	|
|52	|Q((300-330*0.86)/[sqrt(330*0.86*(1-0.86))])	|Phi((330-(.86 * 330))/((330*(1-.86)*(.86))^(1/2)))	|[('R.0.1', 6.303332451965389, u'sqrt(330*0.86*(1-0.86))', u'(330*(1-.86)*(.86))^(1/2)')]	|
|53	|Q((300-330*0.86)/[sqrt(330*0.86*(1-0.86))])	|Phi((331-(.86 * 330))/((330*(1-.86)*(.86))^(1/2)))	|[('R.0.1', 6.303332451965389, u'sqrt(330*0.86*(1-0.86))', u'(330*(1-.86)*(.86))^(1/2)')]	|
|54	|Q((160-174*0.85)/[sqrt(174*0.85*(1-0.85))])	|Phi((174-147.9)/4.7101)	|[('R.0.1', 4.710095540432275, u'sqrt(174*0.85*(1-0.85))', u'4.7101')]	|
|55	|Q((290-321*0.82)/[sqrt(321*0.82*(1-0.82))])	|Q((321 - 263.22)/6.88328)	|[('R.0.1', 6.883284099904639, u'sqrt(321*0.82*(1-0.82))', u'6.88328')]	|
|56	|Q((210-211*0.89)/[sqrt(211*0.89*(1-0.89))])	|Q([211-187.79]/[sqrt(.89*(1-.89)*211)])	|[('R.0.1', 4.544986248604059, u'sqrt(211*0.89*(1-0.89))', u'sqrt(.89*(1-.89)*211)')]	|
|57	|Q((210-211*0.89)/[sqrt(211*0.89*(1-0.89))])	|Q([211-187.79]/[4.54499])	|[('R.0.1', 4.544986248604059, u'sqrt(211*0.89*(1-0.89))', u'4.54499')]	|
|58	|Q((290-306*0.89)/[sqrt(306*0.89*(1-0.89))])	|Q(16/sqrt(306*.89*.11))	|[('R.0.1', 5.473335363377617, u'sqrt(306*0.89*(1-0.89))', u'sqrt(306*.89*.11)')]	|
|59	|Q((290-306*0.89)/[sqrt(306*0.89*(1-0.89))])	|Q(290/sqrt(306*.89*.11))	|[('R.0.1', 5.473335363377617, u'sqrt(306*0.89*(1-0.89))', u'sqrt(306*.89*.11)')]	|
|60	|Q((320-367*0.82)/[sqrt(367*0.82*(1-0.82))])	|Q((367-300.94)/sqrt(0.82(1-0.82)*367))	|[('R.0.1', 7.359972826036793, u'sqrt(367*0.82*(1-0.82))', u'sqrt(0.82(1-0.82)*367)')]	|
|61	|Q((320-367*0.82)/[sqrt(367*0.82*(1-0.82))])	|Q((368-300.94)/sqrt(0.82(1-0.82)*367))	|[('R.0.1', 7.359972826036793, u'sqrt(367*0.82*(1-0.82))', u'sqrt(0.82(1-0.82)*367)')]	|
|62	|Q((200-222*0.81)/[sqrt(222*0.81*(1-0.81))])	|Q((100-.81*222)/(.81*.19*222)^(1/2))	|[('R.0.1', 5.845151837206626, u'sqrt(222*0.81*(1-0.81))', u'(.81*.19*222)^(1/2)')]	|
|63	|Q((300-326*0.84)/[sqrt(326*0.84*(1-0.84))])	|Q((326-220.08)/sqrt(3.26*84*0.16))	|[('R.0.1', 6.619244669900033, u'sqrt(326*0.84*(1-0.84))', u'sqrt(3.26*84*0.16)')]	|
|64	|Q((300-326*0.84)/[sqrt(326*0.84*(1-0.84))])	|Q((326-220.08)/6.61924)	|[('R.0.1', 6.619244669900033, u'sqrt(326*0.84*(1-0.84))', u'6.61924')]	|
|65	|Q((300-326*0.84)/[sqrt(326*0.84*(1-0.84))])	|Q((326-273.84)/6.61924)	|[('R.0.1', 6.619244669900033, u'sqrt(326*0.84*(1-0.84))', u'6.61924')]	|
|66	|Q((150-159*0.8)/[sqrt(159*0.8*(1-0.8))])	|Q((159-159*.80)/sqrt(159*.8(1-.8)) )	|[('R.0.1', 5.043808085167396, u'sqrt(159*0.8*(1-0.8))', u'sqrt(159*.8(1-.8))')]	|
|67	|Q((170-182*0.83)/[sqrt(182*0.83*(1-0.83))])	|Q((182-151.06)/sqrt(182*.83*(1-.83)))	|[('R.0.1', 5.067563517115499, u'sqrt(182*0.83*(1-0.83))', u'sqrt(182*.83*(1-.83))')]	|
|68	|Q((360-392*0.89)/[sqrt(392*0.89*(1-0.89))])	|sqrt((392-348.88)/sqrt(392*0.89(1-0.89)))	|[('R.0.1', 6.194901129154524, u'sqrt(392*0.89*(1-0.89))', u'sqrt(392*0.89(1-0.89))')]	|
|69	|Q((170-182*0.83)/[sqrt(182*0.83*(1-0.83))])	|Q((182-182*0.83)/sqrt(182*.83*(1-.83)))	|[('R.0.1', 5.067563517115499, u'sqrt(182*0.83*(1-0.83))', u'sqrt(182*.83*(1-.83))')]	|
|70	|Q((170-182*0.83)/[sqrt(182*0.83*(1-0.83))])	|Phi((182-182*0.83)/sqrt(182*.83*(1-.83)))	|[('R.0.1', 5.067563517115499, u'sqrt(182*0.83*(1-0.83))', u'sqrt(182*.83*(1-.83))')]	|
|71	|Q((360-392*0.89)/[sqrt(392*0.89*(1-0.89))])	|Q((392-348.88)/(sqrt(392*0.89(1-0.89))))	|[('R.0.1', 6.194901129154524, u'sqrt(392*0.89*(1-0.89))', u'sqrt(392*0.89(1-0.89))')]	|
|72	|Q((200-217*0.83)/[sqrt(217*0.83*(1-0.83))])	|Q(17/sqrt(0.83*0.17*217))	|[('R.0.1', 5.533416666039167, u'sqrt(217*0.83*(1-0.83))', u'sqrt(0.83*0.17*217)')]	|
|73	|Q((200-217*0.83)/[sqrt(217*0.83*(1-0.83))])	|Q((217-217 * 0.83)/sqrt(0.83*0.17*217))	|[('R.0.1', 5.533416666039167, u'sqrt(217*0.83*(1-0.83))', u'sqrt(0.83*0.17*217)')]	|
|74	|Q((200-228*0.8)/[sqrt(228*0.8*(1-0.8))])	|Q(1-sqrt(80/100*(20/100)*228))	|[('R.0.1', 6.039867548216599, u'sqrt(228*0.8*(1-0.8))', u'sqrt(80/100*(20/100)*228)')]	|
|75	|Q((170-175*0.89)/[sqrt(175*0.89*(1-0.89))])	|Q((171- 175*.89)/sqrt(.89*.11*175))	|[('R.0.1', 4.1391424232562954, u'sqrt(175*0.89*(1-0.89))', u'sqrt(.89*.11*175)')]	|
|76	|Q((160-166*0.86)/[sqrt(166*0.86*(1-0.86))])	|(Phi((166-.86 * 166)/sqrt(166*.86*.14)))	|[('R.0.1', 4.470615170197497, u'sqrt(166*0.86*(1-0.86))', u'sqrt(166*.86*.14)')]	|
|77	|Q((200-212*0.86)/[sqrt(212*0.86*(1-0.86))])	|Q((212-182.32)/sqrt(212*.86*(1-.86)))	|[('R.0.1', 5.0522074383382165, u'sqrt(212*0.86*(1-0.86))', u'sqrt(212*.86*(1-.86))')]	|
|78	|Q((200-212*0.86)/[sqrt(212*0.86*(1-0.86))])	|Q((212- (.86*212))/(sqrt(212*.86*(1-.86))))	|[('R.0.1', 5.0522074383382165, u'sqrt(212*0.86*(1-0.86))', u'sqrt(212*.86*(1-.86))')]	|
|79	|Q((160-166*0.86)/[sqrt(166*0.86*(1-0.86))])	|(Phi((166-.24 * 166)/sqrt(166*.86*.14)))	|[('R.0.1', 4.470615170197497, u'sqrt(166*0.86*(1-0.86))', u'sqrt(166*.86*.14)')]	|
|80	|Q((200-212*0.86)/[sqrt(212*0.86*(1-0.86))])	|Phi((212- (.86*212))/(sqrt(212*.86*(1-.86))))	|[('R.0.1', 5.0522074383382165, u'sqrt(212*0.86*(1-0.86))', u'sqrt(212*.86*(1-.86))')]	|
|81	|Q((340-382*0.84)/[sqrt(382*0.84*(1-0.84))])	|Q((42 - 382*.84)/(sqrt(382*.84*(1 - .84))))	|[('R.0.1', 7.165249472279386, u'sqrt(382*0.84*(1-0.84))', u'sqrt(382*.84*(1 - .84))')]	|
|82	|Q((340-382*0.84)/[sqrt(382*0.84*(1-0.84))])	|Phi((42 - 382*.84)/(sqrt(382*.84*(1 - .84))))	|[('R.0.1', 7.165249472279386, u'sqrt(382*0.84*(1-0.84))', u'sqrt(382*.84*(1 - .84))')]	|
|83	|Q((160-166*0.86)/[sqrt(166*0.86*(1-0.86))])	|Phi((166-160)/sqrt(166*.86*.14))	|[('R.0.1', 4.470615170197497, u'sqrt(166*0.86*(1-0.86))', u'sqrt(166*.86*.14)')]	|
|84	|Q((160-166*0.86)/[sqrt(166*0.86*(1-0.86))])	|Phi(((166-.86*166)/sqrt(166*.86*.14)))	|[('R.0.1', 4.470615170197497, u'sqrt(166*0.86*(1-0.86))', u'sqrt(166*.86*.14)')]	|
|85	|Q((160-166*0.86)/[sqrt(166*0.86*(1-0.86))])	|Q(((166-.86*166)/sqrt(166*.86*.14)))	|[('R.0.1', 4.470615170197497, u'sqrt(166*0.86*(1-0.86))', u'sqrt(166*.86*.14)')]	|
|86	|Q((340-382*0.84)/[sqrt(382*0.84*(1-0.84))])	|Q((2 - 382*.84)/(sqrt(382*.84*(1 - .84))))	|[('R.0.1', 7.165249472279386, u'sqrt(382*0.84*(1-0.84))', u'sqrt(382*.84*(1 - .84))')]	|
|87	|Q((200-228*0.8)/[sqrt(228*0.8*(1-0.8))])	|Q(2*sqrt(80/100*(20/100)*228))	|[('R.0.1', 6.039867548216599, u'sqrt(228*0.8*(1-0.8))', u'sqrt(80/100*(20/100)*228)')]	|
|88	|Q((200-212*0.86)/[sqrt(212*0.86*(1-0.86))])	|Q((212-182.32)/5.05221)	|[('R.0.1', 5.0522074383382165, u'sqrt(212*0.86*(1-0.86))', u'5.05221')]	|
|89	|Q((200-228*0.8)/[sqrt(228*0.8*(1-0.8))])	|Q(1-sqrt(20/100*(80/100)*228))	|[('R.0.1', 6.039867548216599, u'sqrt(228*0.8*(1-0.8))', u'sqrt(20/100*(80/100)*228)')]	|
|90	|Q((160-166*0.86)/[sqrt(166*0.86*(1-0.86))])	|(((166-.86*166)/sqrt(166*.86*.14)))/1000	|[('R.0.1', 4.470615170197497, u'sqrt(166*0.86*(1-0.86))', u'sqrt(166*.86*.14)')]	|
|91	|Q((160-166*0.86)/[sqrt(166*0.86*(1-0.86))])	|(((166-.86*166)/sqrt(166*.86*.14)))/100	|[('R.0.1', 4.470615170197497, u'sqrt(166*0.86*(1-0.86))', u'sqrt(166*.86*.14)')]	|
|92	|Q((160-166*0.86)/[sqrt(166*0.86*(1-0.86))])	|(((166-.86*166)/sqrt(166*.86*.14)))/10	|[('R.0.1', 4.470615170197497, u'sqrt(166*0.86*(1-0.86))', u'sqrt(166*.86*.14)')]	|
|93	|Q((200-228*0.8)/[sqrt(228*0.8*(1-0.8))])	|Q((228-228*80/100)/(sqrt(80/100*(20/100)*228)))	|[('R.0.1', 6.039867548216599, u'sqrt(228*0.8*(1-0.8))', u'sqrt(80/100*(20/100)*228)')]	|
|94	|Q((210-214*0.88)/[sqrt(214*0.88*(1-0.88))])	|Q((214-214*0.88)/sqrt(0.88*0.12*214))	|[('R.0.1', 4.753777445358585, u'sqrt(214*0.88*(1-0.88))', u'sqrt(0.88*0.12*214)')]	|
|95	|Q((200-228*0.8)/[sqrt(228*0.8*(1-0.8))])	|Q((201-228*80/100)/(sqrt(80/100*(20/100)*228)))	|[('R.0.1', 6.039867548216599, u'sqrt(228*0.8*(1-0.8))', u'sqrt(80/100*(20/100)*228)')]	|
|96	|Q((290-308*0.89)/[sqrt(308*0.89*(1-0.89))])	|Q((308-(308*.89))/(308*.89*.11)^(1/2))	|[('R.0.1', 5.4911929487134215, u'sqrt(308*0.89*(1-0.89))', u'(308*.89*.11)^(1/2)')]	|
|97	|Q((290-308*0.89)/[sqrt(308*0.89*(1-0.89))])	|Q(3((308*.89*.11)^(1/2)))	|[('R.0.1', 5.4911929487134215, u'sqrt(308*0.89*(1-0.89))', u'(308*.89*.11)^(1/2)')]	|
|98	|Q((290-308*0.89)/[sqrt(308*0.89*(1-0.89))])	|Q((308-(308*.89))/(308*.89*.11)^(1/2)((308*.89*.11)^(1/2)))	|[('R.0.1', 5.4911929487134215, u'sqrt(308*0.89*(1-0.89))', u'(308*.89*.11)^(1/2)')]	|
|99	|Q((200-226*0.8)/[sqrt(226*0.8*(1-0.8))])	|Q((4-(226*0.8))/(sqrt((226*(0.8))*(1-(0.8)))))	|[('R.0.1', 6.013318551349163, u'sqrt(226*0.8*(1-0.8))', u'sqrt((226*(0.8))*(1-(0.8)))')]	|
|100	|Q((240-277*0.82)/[sqrt(277*0.82*(1-0.82))])	|Q((277-277*.82)/sqrt(.82*.18*277))	|[('R.0.1', 6.394153579638201, u'sqrt(277*0.82*(1-0.82))', u'sqrt(.82*.18*277)')]	|
|101	|Q((280-304*0.87)/[sqrt(304*0.87*(1-0.87))])	|Q((304-280)/5.86365)	|[('R.0.1', 5.863650739940093, u'sqrt(304*0.87*(1-0.87))', u'5.86365')]	|
|102	|Q((280-304*0.87)/[sqrt(304*0.87*(1-0.87))])	|Q((304-264.48)/5.86365)	|[('R.0.1', 5.863650739940093, u'sqrt(304*0.87*(1-0.87))', u'5.86365')]	|
|103	|Q((280-304*0.87)/[sqrt(304*0.87*(1-0.87))])	|Q((304-(304*.87))/5.86365)	|[('R.0.1', 5.863650739940093, u'sqrt(304*0.87*(1-0.87))', u'5.86365')]	|
|104	|Q((200-212*0.86)/[sqrt(212*0.86*(1-0.86))])	|Q([212 - (212*.86)]/(sqrt(212*(.86)(1-.86))))	|[('R.0.1', 5.0522074383382165, u'sqrt(212*0.86*(1-0.86))', u'sqrt(212*(.86)(1-.86))')]	|
|105	|Q((200-212*0.86)/[sqrt(212*0.86*(1-0.86))])	|Q((212-182)/(5.05221))	|[('R.0.1', 5.0522074383382165, u'sqrt(212*0.86*(1-0.86))', u'5.05221')]	|
|106	|Q((270-287*0.85)/[sqrt(287*0.85*(1-0.85))])	|Q(((270-287)(0.85))/(sqrt((287 * 0.85)(1-0.85))))	|[('R.0.1', 6.0491734972639035, u'sqrt(287*0.85*(1-0.85))', u'sqrt((287 * 0.85)(1-0.85))')]	|
|107	|Q((260-282*0.85)/[sqrt(282*0.85*(1-0.85))])	|Q(282*.85/(sqrt(.85(1-.85)282)))	|[('R.0.1', 5.996248827392006, u'sqrt(282*0.85*(1-0.85))', u'sqrt(.85(1-.85)282)')]	|
|108	|Q((260-282*0.85)/[sqrt(282*0.85*(1-0.85))])	|Q((260-282)*.85/(sqrt(.85(1-.85)282)))	|[('R.0.1', 5.996248827392006, u'sqrt(282*0.85*(1-0.85))', u'sqrt(.85(1-.85)282)')]	|
|109	|Q((330-365*0.86)/[sqrt(365*0.86*(1-0.86))])	|Phi((365-314)/sqrt(.86*(1-.86)*365))	|[('R.0.1', 6.629177927918363, u'sqrt(365*0.86*(1-0.86))', u'sqrt(.86*(1-.86)*365)')]	|
|110	|Q((350-378*0.88)/[sqrt(378*0.88*(1-0.88))])	|Q((378 - 378*(.88))/sqrt((378*.88)(1 - .88)))	|[('R.0.1', 6.317974358922328, u'sqrt(378*0.88*(1-0.88))', u'sqrt((378*.88)(1 - .88))')]	|
|111	|Q((350-378*0.88)/[sqrt(378*0.88*(1-0.88))])	|Phi((378 - 378*(.88))/sqrt((378*.88)(1 - .88)))	|[('R.0.1', 6.317974358922328, u'sqrt(378*0.88*(1-0.88))', u'sqrt((378*.88)(1 - .88))')]	|
|112	|Q((190-201*0.85)/[sqrt(201*0.85*(1-0.85))])	|Q((201 - (0.85*201))/(sqrt((0.85)*(0.15)*201)))	|[('R.0.1', 5.062361109205861, u'sqrt(201*0.85*(1-0.85))', u'sqrt((0.85)*(0.15)*201)')]	|
|113	|Q((350-378*0.88)/[sqrt(378*0.88*(1-0.88))])	|Phi(((378 - 378*(.88))/sqrt((378*.88)(1 - .88))))	|[('R.0.1', 6.317974358922328, u'sqrt(378*0.88*(1-0.88))', u'sqrt((378*.88)(1 - .88))')]	|
|114	|Q((340-376*0.85)/[sqrt(376*0.85*(1-0.85))])	|Q((376 - (376 * .85))/sqrt(376 * .85 * .15))	|[('R.0.1', 6.923871749245505, u'sqrt(376*0.85*(1-0.85))', u'sqrt(376 * .85 * .15)')]	|
|115	|Q((350-378*0.88)/[sqrt(378*0.88*(1-0.88))])	|Phi(((379 - 378*(.88))/sqrt((378*.88)(1 - .88))))	|[('R.0.1', 6.317974358922328, u'sqrt(378*0.88*(1-0.88))', u'sqrt((378*.88)(1 - .88))')]	|
|116	|Q((350-378*0.88)/[sqrt(378*0.88*(1-0.88))])	|Q(((379 - 378*(.88))/sqrt((378*.88)(1 - .88))))	|[('R.0.1', 6.317974358922328, u'sqrt(378*0.88*(1-0.88))', u'sqrt((378*.88)(1 - .88))')]	|
|117	|Q((320-349*0.85)/[sqrt(349*0.85*(1-0.85))])	|Q((349-296.65)/6.67064)	|[('R.0.1', 6.670644646509062, u'sqrt(349*0.85*(1-0.85))', u'6.67064')]	|
|118	|Q((310-335*0.88)/[sqrt(335*0.88*(1-0.88))])	|Phi(310/sqrt(335*.88*.12))	|[('R.0.1', 5.947772692361402, u'sqrt(335*0.88*(1-0.88))', u'sqrt(335*.88*.12)')]	|
|119	|Q((310-335*0.88)/[sqrt(335*0.88*(1-0.88))])	|Phi((335*.88)/sqrt(335*.88*.12))	|[('R.0.1', 5.947772692361402, u'sqrt(335*0.88*(1-0.88))', u'sqrt(335*.88*.12)')]	|
|120	|Q((260-275*0.87)/[sqrt(275*0.87*(1-0.87))])	|Q((275-239.25)/5.57696)	|[('R.0.1', 5.576961538328914, u'sqrt(275*0.87*(1-0.87))', u'5.57696')]	|
|121	|Q((220-248*0.8)/[sqrt(248*0.8*(1-0.8))])	|Q((248 * .8 - 220)/sqrt((4/5)(1/5)(248)))	|[('R.0.1', 6.299206299209448, u'sqrt(248*0.8*(1-0.8))', u'sqrt((4/5)(1/5)(248))')]	|
|122	|Q((260-275*0.87)/[sqrt(275*0.87*(1-0.87))])	|Q(1/5.57696)	|[('R.0.1', 5.576961538328914, u'sqrt(275*0.87*(1-0.87))', u'5.57696')]	|
|123	|Q((260-275*0.87)/[sqrt(275*0.87*(1-0.87))])	|Q(.75/5.57696)	|[('R.0.1', 5.576961538328914, u'sqrt(275*0.87*(1-0.87))', u'5.57696')]	|
|124	|Q((260-275*0.87)/[sqrt(275*0.87*(1-0.87))])	|Q((261-.87*275)/5.57696)	|[('R.0.1', 5.576961538328914, u'sqrt(275*0.87*(1-0.87))', u'5.57696')]	|
|125	|Q((260-275*0.87)/[sqrt(275*0.87*(1-0.87))])	|Q((261-241)/5.57696)	|[('R.0.1', 5.576961538328914, u'sqrt(275*0.87*(1-0.87))', u'5.57696')]	|
|126	|Q((260-275*0.87)/[sqrt(275*0.87*(1-0.87))])	|Q((261-240)/5.57696)	|[('R.0.1', 5.576961538328914, u'sqrt(275*0.87*(1-0.87))', u'5.57696')]	|
|127	|Q((260-275*0.87)/[sqrt(275*0.87*(1-0.87))])	|Q((261-239.25)/5.57696)	|[('R.0.1', 5.576961538328914, u'sqrt(275*0.87*(1-0.87))', u'5.57696')]	|
|128	|Q((300-333*0.84)/[sqrt(333*0.84*(1-0.84))])	|Q((333-333*0.84)/(sqrt(0.84 * (1-0.84) * 333)))	|[('R.0.1', 6.68993273508785, u'sqrt(333*0.84*(1-0.84))', u'sqrt(0.84 * (1-0.84) * 333)')]	|
|129	|Q((300-333*0.84)/[sqrt(333*0.84*(1-0.84))])	|Phi((333-333*0.84)/(sqrt(0.84 * (1-0.84) * 333)))	|[('R.0.1', 6.68993273508785, u'sqrt(333*0.84*(1-0.84))', u'sqrt(0.84 * (1-0.84) * 333)')]	|
|130	|Q((330-390*0.8)/[sqrt(390*0.8*(1-0.8))])	|Q((390-312)/(sqrt(312*(1-0.8))))	|[('R.0.1', 7.8993670632525985, u'sqrt(390*0.8*(1-0.8))', u'sqrt(312*(1-0.8))')]	|
|131	|Q((330-390*0.8)/[sqrt(390*0.8*(1-0.8))])	|Q((390-312)/(7.89937))	|[('R.0.1', 7.8993670632525985, u'sqrt(390*0.8*(1-0.8))', u'7.89937')]	|




### (50) Mistake Group redirect of size 50




### (27) Mistake Group Digits of size 27




### (20) Mistake Group Wrong_Sign of size 20




### (13) Mistake Group ['R.0.0'] of size 13
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|Q((250-275*0.84)/[sqrt(275*0.84*(1-0.84))])	|Q((250-275*(0.84))/(275*(0.84)*(1-0.84)))	|[('R.0.0', 19.0, u'250-275*0.84', u'250-275*(0.84)')]	|
|1	|Q((200-209*0.86)/[sqrt(209*0.86*(1-0.86))])	|Q ( (200-.86*209)/(.86*209*.14))	|[('R.0.0', 20.25999999999999, u'200-209*0.86', u'200-.86*209')]	|
|2	|Q((290-332*0.81)/[sqrt(332*0.81*(1-0.81))])	|Q(21.08/7.14)	|[('R.0.0', 21.079999999999984, u'290-332*0.81', u'21.08')]	|
|3	|Q((290-327*0.81)/[sqrt(327*0.81*(1-0.81))])	|Q(290-.81*327)/sqrt(327*.81*.19)	|[('R.0.0', 25.129999999999995, u'290-327*0.81', u'290-.81*327')]	|
|4	|Q((260-285*0.84)/[sqrt(285*0.84*(1-0.84))])	|Q(260-239.4)/6.18902	|[('R.0.0', 20.600000000000023, u'260-285*0.84', u'260-239.4')]	|
|5	|Q((160-174*0.82)/[sqrt(174*0.82*(1-0.82))])	|Q((160- 142.68)/6.06778)	|[('R.0.0', 17.32000000000002, u'160-174*0.82', u'160- 142.68')]	|
|6	|Q((160-174*0.82)/[sqrt(174*0.82*(1-0.82))])	|Phi((160- 142.68)/6.06778)	|[('R.0.0', 17.32000000000002, u'160-174*0.82', u'160- 142.68')]	|
|7	|Q((240-273*0.8)/[sqrt(273*0.8*(1-0.8))])	|Q((240-0.8*273)/(0.8*0.2*240)**0.5)	|[('R.0.0', 21.599999999999994, u'240-273*0.8', u'240-0.8*273')]	|
|8	|Q((150-166*0.81)/[sqrt(166*0.81*(1-0.81))])	|Q((150-134.46)/25.54)	|[('R.0.0', 15.539999999999992, u'150-166*0.81', u'150-134.46')]	|
|9	|Q((160-166*0.86)/[sqrt(166*0.86*(1-0.86))])	|Q((160-166*0.86)/(166*0.86)^0.5)	|[('R.0.0', 17.24000000000001, u'160-166*0.86', u'160-166*0.86')]	|
|10	|Q((220-247*0.84)/[sqrt(247*0.84*(1-0.84))])	|Q((220-207.48)/5.76)	|[('R.0.0', 12.52000000000001, u'220-247*0.84', u'220-207.48')]	|




### (6) Mistake Group ['R.0'] of size 6
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|Q((350-384*0.84)/[sqrt(384*0.84*(1-0.84))])	|Phi((350 - .84 * 384)/sqrt(384 * .84(1 - .84)))	|[('R.0', 3.8196085823317314, u'(350-384*0.84)/[sqrt(384*0.84*(1-0.84))]', u'(350 - .84 * 384)/sqrt(384 * .84(1 - .84))')]	|
|1	|Q((300-347*0.81)/[sqrt(347*0.81*(1-0.81))])	|Phi((300-281.07)/7.30776)	|[('R.0', 2.5903984208284525, u'(300-347*0.81)/[sqrt(347*0.81*(1-0.81))]', u'(300-281.07)/7.30776')]	|
|2	|Q((160-174*0.85)/[sqrt(174*0.85*(1-0.85))])	|Phi((160-147.9)/4.7101)	|[('R.0', 2.5689500130372096, u'(160-174*0.85)/[sqrt(174*0.85*(1-0.85))]', u'(160-147.9)/4.7101')]	|
|3	|Q((290-306*0.89)/[sqrt(306*0.89*(1-0.89))])	|((290-272.34)/5.47334)/5.47334	|[('R.0', 3.2265517874464593, u'(290-306*0.89)/[sqrt(306*0.89*(1-0.89))]', u'(290-272.34)/5.47334')]	|
|4	|Q((170-188*0.84)/[sqrt(188*0.84*(1-0.84))])	|((170-(188*.84))/sqrt(188*.84*(1-.84))) * 100	|[('R.0', 2.403191478149097, u'(170-188*0.84)/[sqrt(188*0.84*(1-0.84))]', u'(170-(188*.84))/sqrt(188*.84*(1-.84))')]	|
|5	|Q((310-335*0.88)/[sqrt(335*0.88*(1-0.88))])	|Phi((310-335*.88)/sqrt(335*.88*.12))	|[('R.0', 2.555578497396349, u'(310-335*0.88)/[sqrt(335*0.88*(1-0.88))]', u'(310-335*.88)/sqrt(335*.88*.12)')]	|




### (5) Mistake Group ['R.0.0.0', 'R.0.1'] of size 5
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0', 'R.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|Q((150-152*0.87)/[sqrt(152*0.87*(1-0.87))])	|Q((150-132)/sqrt(152*.87*(1-.87)))	|[('R.0.0.0', 150.0, u'150', u'150'), ('R.0.1', 4.146227200721157, u'sqrt(152*0.87*(1-0.87))', u'sqrt(152*.87*(1-.87))')]	|
|1	|Q((150-152*0.87)/[sqrt(152*0.87*(1-0.87))])	|Q((150-133)/sqrt(152*.87*(1-.87)))	|[('R.0.0.0', 150.0, u'150', u'150'), ('R.0.1', 4.146227200721157, u'sqrt(152*0.87*(1-0.87))', u'sqrt(152*.87*(1-.87))')]	|
|2	|Q((290-302*0.89)/[sqrt(302*0.89*(1-0.89))])	|Q((290-((2)/(sqrt((1/12)*(1)^2*100))))/(sqrt(0.89*0.11*302)))	|[('R.0.0.0', 290.0, u'290', u'290'), ('R.0.1', 5.437444252587791, u'sqrt(302*0.89*(1-0.89))', u'sqrt(0.89*0.11*302)')]	|
|3	|Q((260-275*0.87)/[sqrt(275*0.87*(1-0.87))])	|Q((260-240)/5.57696)	|[('R.0.0.0', 260.0, u'260', u'260'), ('R.0.1', 5.576961538328914, u'sqrt(275*0.87*(1-0.87))', u'5.57696')]	|
|4	|Q((260-275*0.87)/[sqrt(275*0.87*(1-0.87))])	|Q((260-241)/5.57696)	|[('R.0.0.0', 260.0, u'260', u'260'), ('R.0.1', 5.576961538328914, u'sqrt(275*0.87*(1-0.87))', u'5.57696')]	|




### (3) Mistake Group ['R.0.0', 'R.0.1.0.1'] of size 3
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.0.1.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|Q((150-163*0.82)/[sqrt(163*0.82*(1-0.82))])	|Q((150-163*0.82)/[sqrt(340*0.82*(1-0.82))])	|[('R.0.0', 16.340000000000003, u'150-163*0.82', u'150-163*0.82'), ('R.0.1.0.1', 0.18000000000000005, u'1-0.82', u'1-0.82')]	|
|1	|Q((250-266*0.87)/[sqrt(266*0.87*(1-0.87))])	|Q((250-(.87*266))/(sqrt(.81*266*(1-.87))))	|[('R.0.0', 18.580000000000013, u'250-266*0.87', u'250-(.87*266)'), ('R.0.1.0.1', 0.13, u'1-0.87', u'1-.87)')]	|
|2	|Q((180-193*0.84)/[sqrt(193*0.84*(1-0.84))])	|Q((180-(193*.84))/(sqrt (193 *.83 * (1 -.84))))	|[('R.0.0', 17.879999999999995, u'180-193*0.84', u'180-(193*.84)'), ('R.0.1.0.1', 0.16000000000000003, u'1-0.84', u'1 -.84)')]	|




### (2) Mistake Group ['R.0.0.0'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|Q((210-213*0.89)/[sqrt(213*0.89*(1-0.89))])	|Q(210-.89-213/(sqrt(.89*213*(1-.89))))	|[('R.0.0.0', 210.0, u'210', u'210')]	|
|1	|Q((150-166*0.81)/[sqrt(166*0.81*(1-0.81))])	|Q((150-5.05444)/25.54)	|[('R.0.0.0', 150.0, u'150', u'150')]	|




### (1) Mistake Group ['R.0.0', 'R.0.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|Q((360-397*0.85)/[sqrt(397*0.85*(1-0.85))])	|Q((360-(.85*397))sqrt(.85*.15*397))	|[('R.0.0', 22.55000000000001, u'360-397*0.85', u'360-(.85*397)'), ('R.0.1', 7.114597669580481, u'sqrt(397*0.85*(1-0.85))', u'sqrt(.85*.15*397)')]	|




### (1) Mistake Group ['R.0.1.0.0.0'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1.0.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|Q((300-347*0.8)/[sqrt(347*0.8*(1-0.8))])	|Q(300-(347*80/100)/sqrt((347*80/100)*(1-80/100)))	|[('R.0.1.0.0.0', 347.0, u'347', u'347')]	|




### (1) Mistake Group ['R.0.0', 'R.0.1.0.1.0'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.0.1.0.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|Q((180-193*0.84)/[sqrt(193*0.84*(1-0.84))])	|Q((180-(193*.84))/(sqrt (193 *.83 * (1 -.83))))	|[('R.0.0', 17.879999999999995, u'180-193*0.84', u'180-(193*.84)'), ('R.0.1.0.1.0', 1.0, u'1', u'1')]	|




### (1) Mistake Group ['R.0.0.0', 'R.0.1.0.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0', 'R.0.1.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|Q((180-189*0.87)/[sqrt(189*0.87*(1-0.87))])	|Q([180-[180*(189*0.87/189)]]/[(189*0.87/189)*[1-(189*0.87/189)]*180])	|[('R.0.0.0', 180.0, u'180', u'180'), ('R.0.1.0.1', 0.13, u'1-0.87', u'1-(189*0.87/189)')]	|




### (1) Mistake Group ['R.0.1.0.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|Q((250-266*0.87)/[sqrt(266*0.87*(1-0.87))])	|Q((266-(.87*266))/(sqrt(.81*266*(1-.87))))	|[('R.0.1.0.1', 0.13, u'1-0.87', u'1-.87)')]	|




### (1) Mistake Group ['R.0.1.0.1.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1.0.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|Q((170-188*0.84)/[sqrt(188*0.84*(1-0.84))])	|1/((170-(188*.84))/sqrt(188*.84*(1-.84))) * 100	|[('R.0.1.0.1.1', 0.84, u'0.84', u'.84)')]	|




### (123) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:v4zhang

	first_attempt
					2015-11-06 07:56:40
	part1_correct_attempt
					['0:00:00', u'.89*265']
	part2_correct_attempt
					['0:00:00', u'sqrt[.89(1-.89)265]']
	part3_incorrect_attempt
					('0:03:07', u'Q(.89*265)')
					('0:12:21', u'Q(5)')
	part3_correct_attempt
					['0:41:02', u'Q([260-(.89*265)]/sqrt[.89(1-.89)265])']

1 Student ID:kew060

	first_attempt
					2015-11-05 01:40:27
	part1_correct_attempt
					['0:00:00', u'132.6']
	part2_correct_attempt
					['0:00:12', u'4.46']
	part3_incorrect_attempt
					('0:00:25', u'.000048')
					('0:01:20', u'0.00048')
					('22:08:35', u'Q((156-132.6)/4.46)')
	part3_correct_attempt
					['22:09:08', u'Q((150-132.6)/4.46)']

2 Student ID:kbielawi

	first_attempt
					2015-11-06 00:39:46
	part1_correct_attempt
					['0:00:00', u'304*.87']
	part2_correct_attempt
					['17:55:43', u'sqrt(.87*(1-.87)*304)']
	part3_incorrect_attempt
					('17:56:06', u'.13')
					('17:59:02', u'1-Q((304-(304*.87))/5.86365)')
					('18:00:16', u'1-Q((304-280)/5.86365)')
					('18:45:31', u'2*Q((304-280)/5.86365)')
	part3_correct_attempt
					['18:46:47', u'Q((280-264.48)/5.86365)']

3 Student ID:jguanzho

	first_attempt
					2015-11-05 17:48:32
	part1_correct_attempt
					['0:00:00', u'0.8*273']
	part2_correct_attempt
					['0:00:00', u'(0.8*0.2*273)**0.5']
	part3_incorrect_attempt
					('0:00:18', u'Q((273-0.8*273)/(0.8*0.2*240)**0.5)')
					('0:02:46', u'Q((241-0.8*273)/(0.8*0.2*240)**0.5)')
					('0:04:24', u'1-Q((240-0.8*273)/(0.8*0.2*240)**0.5)')
					('0:04:40', u'1-Phi((240-0.8*273)/(0.8*0.2*240)**0.5)')
					('0:13:41', u'1-Phi((241-0.8*273)/(0.8*0.2*240)**0.5)')
	part3_correct_attempt
					['0:14:20', u'1-Phi((240-0.8*273)/(0.8*0.2*273)**0.5)']

4 Student ID:jhc010

	first_attempt
					2015-11-06 11:07:36
	part1_correct_attempt
					['0:00:00', u'277*.82']
	part2_correct_attempt
					['0:01:25', u'sqrt(.82*.18*277)']
	part3_incorrect_attempt
					('0:04:59', u'(277-277*.82)/sqrt(.82*.18*277)')
	part3_correct_attempt
					['0:05:48', u'Q((240-277*.82)/sqrt(.82*.18*277))']

5 Student ID:mhale

	first_attempt
					2015-11-05 20:43:02
	part1_correct_attempt
					['0:00:00', u'.82 * 321']
	part2_correct_attempt
					['0:00:31', u'(263.22 * (1 - .82))^(1/2)']
	part3_incorrect_attempt
					('0:01:54', u'(321 - 263.22) / 6.88328')
					('0:02:15', u'Q(8.39425)')
	part3_correct_attempt
					['0:03:37', u'Q((290 - 263.22) / 6.88328)']

6 Student ID:rsmurlo

	first_attempt
					2015-11-05 18:25:02
	part1_correct_attempt
					['0:00:00', u'.88*340']
	part2_correct_attempt
					['0:00:40', u'sqrt(.88(.12)(340))']
	part3_incorrect_attempt
					('0:02:31', u'(311-299.2)/5.99199')
	part3_correct_attempt
					['0:06:16', u'Q((310-299.2)/5.99199)']

7 Student ID:j5phung

	first_attempt
					2015-11-04 22:10:17
	part1_correct_attempt
					['0:00:00', u'311(0.8)']
	part2_correct_attempt
					['0:04:00', u'sqrt(311*.8*.2)']
	part3_incorrect_attempt
					('0:12:04', u'C(311,270)(.8)^270*(.2)^41')
	part3_correct_attempt
					['3:27:27', u'1-((1/2)+(1/2)erf(((270-311(0.8))/sqrt(311*.8*.2))/sqrt(2)))']

8 Student ID:jyc018

	first_attempt
					2015-11-06 23:23:19
	part1_correct_attempt
					['0:00:00', u'397*.84']
	part2_correct_attempt
					['0:01:05', u'sqrt(397*.84*.16)']
	part3_incorrect_attempt
					('0:01:56', u'1-Phi((397-333.48)/7.3)')
	part3_correct_attempt
					['0:02:22', u'1-Phi((350-333.48)/7.304)']

9 Student ID:vqt004

	first_attempt
					2015-11-06 06:35:42
	part1_correct_attempt
					['0:00:00', u'214*0.88']
	part2_correct_attempt
					['0:00:00', u'sqrt(0.88*0.12*214)']
	part3_incorrect_attempt
					('0:01:45', u'2*Q((214-214*0.88)/sqrt(0.88*0.12*214))')
					('0:03:13', u'1-Q((214-214*0.88)/sqrt(0.88*0.12*214))')
	part3_correct_attempt
					['0:03:35', u'Q((210-214*0.88)/sqrt(0.88*0.12*214))']

10 Student ID:rlhagen

	first_attempt
					2015-10-31 20:26:34
	part1_correct_attempt
					['0:00:00', u'0.83*285']
	part2_correct_attempt
					['0:05:03', u'sqrt (285 * 0.83 * (1 - 0.83))']
	part3_incorrect_attempt
					('0:16:54', u'(0.83*285)/(sqrt (285 * 0.83 * (1 - 0.83)))')
					('0:37:12', u'2.70E-05')
					('0:37:19', u'1-2.70E-05')
					('0:39:17', u'1-0.99997775')
					('0:39:47', u'0.99997775')
					('0:39:56', u'0.99')
					('0:40:01', u'0.98')
					('0:40:05', u'0.97')
					('0:40:08', u'0.96')
					('0:40:14', u'0.90')
					('0:40:19', u'0.80')
					('0:40:24', u'0.75')
					('0:40:29', u'0.50')
					('0:41:55', u'C(285,260)(0.83)(1-0.83)^(285-260)')
					('0:42:10', u'C(285,260)*(0.83)(1-0.83)^(285-260)')
					('0:42:32', u'C(285,260)')
					('0:42:44', u'C(10,2)')
					('0:49:40', u'0.0000222456')
					('0:52:05', u'0.0000226')
					('0:52:08', u'0.000022')
					('0:52:11', u'0.00002')
					('0:54:15', u'0.01')
					('0:54:22', u'0.02')
					('0:54:26', u'0.03')
					('0:54:30', u'0.04')
					('0:54:34', u'0.05')
					('0:54:38', u'0.06')
					('0:54:41', u'0.07')
					('0:54:45', u'0.08')
					('0:54:55', u'0.1')
					('0:54:59', u'0.2')
					('0:55:03', u'0.3')
					('0:55:06', u'0.4')
					('0:55:11', u'0.5')
					('0:55:14', u'0.6')
					('0:55:18', u'0.7')
					('0:55:22', u'0.8')
					('0:56:53', u'0.0708')
					('0:57:01', u'0.08')
					('0:57:06', u'0.09')
					('0:57:10', u'0.01')
					('0:57:15', u'0.02')
					('0:57:19', u'0.03')
					('0:57:23', u'0.04')
					('0:57:26', u'0.05')
					('0:57:30', u'0.06')
					('0:57:33', u'0.07')
					('0:57:38', u'0.08')
					('0:57:41', u'0.09')
					('0:57:48', u'0.001')
					('0:57:52', u'0.002')
					('0:57:56', u'0.003')
					('1:02:24', u'0.00002225')
					('1:02:34', u'0.000023')
					('1:02:39', u'0.000024')
					('1:02:43', u'0.000021')
					('1:02:48', u'0.00001')
					('1:02:53', u'0.00002')
					('1:02:56', u'0.00003')
					('1:03:00', u'0.00004')
					('1:03:05', u'0.00005')
					('1:03:08', u'0.00008')
					('1:03:12', u'0.00009')
					('1:03:16', u'0.0001')
					('1:03:20', u'0.0002')
					('1:03:24', u'0.0003')
					('1:03:27', u'0.0004')
					('1:03:31', u'0.0005')
					('1:03:36', u'0.0006')
					('1:03:40', u'0.0007')
					('1:03:44', u'0.0008')
					('1:03:48', u'0.0009')
					('1:03:52', u'0.0010')
					('1:03:56', u'0.0011')
					('1:04:00', u'0.0012')
					('1:04:03', u'0.0013')
					('1:04:41', u'0.0000222456')
					('1:06:40', u'1-0.83')
	part3_correct_attempt
					['1:12:51', u'0.000108688']

11 Student ID:btn023

	first_attempt
					2015-11-06 11:36:16
	part1_correct_attempt
					['0:00:00', u'334*.87']
	part2_correct_attempt
					['0:00:00', u'sqrt(334*.87*.13)']
	part3_incorrect_attempt
					('0:01:26', u'(310-334*.87)/sqrt(334*.87*.13)')
	part3_correct_attempt
					['0:01:51', u'0.00079']

12 Student ID:dgunawan

	first_attempt
					2015-11-05 09:22:36
	part1_correct_attempt
					['0:00:00', u'(.89)*(256)']
	part2_correct_attempt
					['14:51:47', u'((.89)*(256)(1-.89))^(1/2)']
	part3_incorrect_attempt
					('14:52:07', u'(1 - (0.89))')
					('14:59:34', u'256(1 - (0.89))')
					('14:59:41', u'256( (0.89))')
					('14:59:48', u'0.89')
					('15:23:47', u'[256-250]/[((.89)*(256)(1-.89))^(1/2)]')
					('15:24:24', u'[256-227.84]/[((.89)*(256)(1-.89))^(1/2)]')
					('15:27:55', u'[250-227.84]/[((.89)*(256)(1-.89))^(1/2)]')
	part3_correct_attempt
					['15:31:22', u'1-Phi([250-227.84]/[((.89)*(256)(1-.89))^(1/2)])']

13 Student ID:mpanelo

	first_attempt
					2015-11-05 23:56:14
	part1_correct_attempt
					['0:00:00', u'304.22']
	part2_correct_attempt
					['0:00:00', u'sqrt( .82 * .18 * 371)']
	part3_incorrect_attempt
					('0:00:00', u'(330 - 304.22)/sqrt( .82 * .18 * 371)')
	part3_correct_attempt
					['0:01:45', u'Q((330 - 304.22)/sqrt( .82 * .18 * 371))']

14 Student ID:tstevens

	first_attempt
					2015-11-06 12:21:35
	part1_correct_attempt
					['0:00:00', u'377*.81']
	part2_correct_attempt
					['0:02:46', u'7.61710575']
	part3_incorrect_attempt
					('0:03:50', u'0.000267937342225966')
					('0:04:08', u'0.00045715260934398')
	part3_correct_attempt
					['0:12:49', u'Q(3.233511626)']

15 Student ID:tcuddy

	first_attempt
					2015-11-03 17:40:00
	part1_correct_attempt
					['0:00:00', u'258(.89)']
	part2_correct_attempt
					['2 days, 1:26:20', u'[ 258(.89(1-.89))]**.5']
	part3_incorrect_attempt
					('2 days, 1:36:38', u'[ (258) -(258(.89)) ] /([ 258(.89(1-.89))]**.5 )')
	part3_correct_attempt
					['2 days, 1:39:51', u'Q [ [(250) -(258(.89)) ] /([ 258(.89(1-.89))]**.5 )]']

16 Student ID:djk006

	first_attempt
					2015-11-04 06:15:40
	part1_correct_attempt
					['0:00:00', u'298*.88']
	part2_correct_attempt
					['0:00:12', u'(298(.88)(.12))^(1/2)']
	part3_incorrect_attempt
					('0:00:51', u'298*.88/((298(.88)(.12))^(1/2))')
					('0:01:38', u'(298-298*.88)/((298(.88)(.12))^(1/2))')
	part3_correct_attempt
					['0:03:20', u'Q((280-298*.88)/((298(.88)(.12))^(1/2)))']

17 Student ID:dando

	first_attempt
					2015-11-07 00:00:54
	part1_correct_attempt
					['0:00:00', u'248 * .8']
	part2_correct_attempt
					['0:03:35', u'sqrt((4/5)(1/5)(248))']
	part3_incorrect_attempt
					('0:04:15', u'1 - Phi(sqrt((4/5)(1/5)(248)))')
					('0:04:26', u'Phi(sqrt((4/5)(1/5)(248)))')
	part3_correct_attempt
					['0:11:21', u'1 - Q((248 * .8 - 220)/sqrt((4/5)(1/5)(248)))']

18 Student ID:dsriniva

	first_attempt
					2015-11-05 17:04:37
	part1_correct_attempt
					['0:00:00', u'.86*320']
	part2_correct_attempt
					['2:39:01', u'sqrt(320*0.86*0.14)']
	part3_incorrect_attempt
					('2:43:32', u'Q(5)')
					('2:43:41', u'Q(4.99428660282)')
	part3_correct_attempt
					['3:00:38', u'Q(14.8/sqrt(320*0.86*0.14))']

19 Student ID:abasu

	first_attempt
					2015-11-05 06:01:45
	part1_correct_attempt
					['0:00:00', u'317*0.83']
	part2_correct_attempt
					['0:04:38', u'(317*0.83*0.17)^0.5']
	part3_incorrect_attempt
					('0:06:24', u'1-Phi(8.0578)')
					('0:06:31', u'Phi(8.0578)')
					('0:08:19', u'Q(8.0578)')
					('0:08:44', u'Q(2.675)')
					('0:13:20', u'Q(2.8411)')
					('0:15:41', u'Q(8.0578)')
					('0:16:12', u'1-Phi(8.0578)')
					('0:16:19', u'Phi(8.0578)')
					('0:17:46', u'Q(-1.9602)')
					('0:17:54', u'1-Q(-1.9602)')
					('0:17:59', u'1-Phi(-1.9602)')
	part3_correct_attempt
					['0:18:32', u'Q(2.5254)']

20 Student ID:sayao

	first_attempt
					2015-11-04 02:01:34
	part1_correct_attempt
					['0:00:00', u'182*.83']
	part2_correct_attempt
					['1 day, 2:02:44', u'sqrt(182*.83*(1-.83))']
	part3_incorrect_attempt
					('1 day, 2:03:58', u'(182-151.06)/(sqrt(182*.83*(1-.83)))')
					('1 day, 2:05:20', u'30.94/5.06756')
					('1 day, 2:11:36', u'C(182,170)*(.83)^170*(1-.83)^(182-170)')
					('1 day, 2:12:40', u'1903717178010268530*(.83)^170*(1-.83)^(182-170)')
					('1 day, 2:13:59', u'C(182, 170)')
					('1 day, 3:13:47', u'0.00000950672')
					('1 day, 3:13:57', u'0.0000950672')
					('1 day, 3:14:01', u'0.000950672')
					('1 day, 3:19:09', u'(182-170)/5.06756')
					('1 day, 3:19:56', u'0.49111')
					('1 day, 3:20:01', u'0.49')
					('1 day, 3:21:39', u'.9909')
					('1 day, 3:21:53', u'.0091')
					('1 day, 3:22:31', u'.0089')
					('1 day, 3:23:45', u'1-.9909')
					('1 day, 3:23:51', u'1-.9911')
					('1 day, 3:24:04', u'1-.9913')
					('1 day, 3:24:14', u'1-.9916')
					('1 day, 3:25:37', u'1-.9911')
					('1 day, 3:27:11', u'.00089')
					('1 day, 3:28:34', u'1-.9911')
					('1 day, 3:28:48', u'(182-170)/5.06756')
					('1 day, 14:36:33', u'Q(2.368)')
					('1 day, 14:36:53', u'Q(2.37)')
					('1 day, 14:37:37', u'Phi(2.37)')
					('1 day, 14:37:46', u'Q(2.68)')
					('1 day, 14:38:39', u'Q(2.6)')
					('1 day, 14:40:32', u'Q(2)')
					('1 day, 14:41:34', u'182-151.06/5.06756')
					('1 day, 14:41:43', u'(182-151.06)/5.06756')
					('1 day, 14:41:55', u'Q(6.1055)')
					('1 day, 14:55:37', u'Phi(6.1055)')
					('1 day, 14:55:46', u'Q(6.1)')
					('1 day, 14:56:28', u'1-Q(6.1)')
					('1 day, 14:56:39', u'Q(6)')
					('1 day, 14:56:47', u'Q(6.1)')
					('1 day, 14:57:00', u'Q(6.105)')
	part3_correct_attempt
					['1 day, 21:57:32', u'Q((170-182*0.83)/sqrt(182*.83*(1-.83)))']

21 Student ID:anvan

	first_attempt
					2015-11-05 15:39:51
	part1_correct_attempt
					['0:00:00', u'.89(345)']
	part2_correct_attempt
					['23:26:00', u'sqrt ( .89 * .11 * 345)']
	part3_incorrect_attempt
					('23:43:49', u'Q(6.453)')
					('23:45:27', u'Q(4.121)')
					('23:54:16', u'1 - Q(4.121)')
					('23:55:06', u'Phi(4.121)')
					('23:55:13', u'1 - Phi(4.121)')
	part3_correct_attempt
					['23:58:46', u'1 - Phi(3.949)']

22 Student ID:m4bui

	first_attempt
					2015-11-06 04:21:23
	part1_correct_attempt
					['0:00:00', u'212*.87']
	part2_correct_attempt
					['0:00:34', u'sqrt(212*.87*(1-.87))']
	part3_incorrect_attempt
					('0:03:51', u'(212-184.44)/4.89665')

23 Student ID:flhernan

	first_attempt
					2015-11-06 13:55:25
	part1_correct_attempt
					['0:00:00', u'162*.82']
	part2_correct_attempt
					['9:10:30', u'sqrt(162*.82*(1-.82))']
	part3_incorrect_attempt
					('9:12:39', u'(150 - 162*.82)/sqrt(162*.82*(1-.82))')
					('9:13:56', u'1-0.99978')
					('9:19:43', u'(162-162*.85)/(sqrt(162*.82*(1-.82)))')
					('9:20:14', u'1-0.99997')
					('9:21:45', u'(162-162*.82)/(sqrt(162*.82*(1-.82)))')

24 Student ID:m4salaza

	first_attempt
					2015-11-05 05:51:51
	part1_correct_attempt
					['0:00:00', u'.81*293']
	part2_correct_attempt
					['0:00:00', u'sqrt(.81*293*(1-.81))']
	part3_incorrect_attempt
					('0:01:04', u'Q(293-.81*293)')
					('0:01:21', u'Q(260-.81*293)')
	part3_correct_attempt
					['0:02:38', u'Q((260-.81*293)/sqrt(.81*293*(1-.81)))']

25 Student ID:yos017

	first_attempt
					2015-11-06 10:06:25
	part1_correct_attempt
					['0:00:00', u'339* 0.89']
	part2_correct_attempt
					['0:00:40', u'(339*0.89*0.11)^0.5']
	part3_incorrect_attempt
					('0:10:12', u'[(339-301.71)/5.76091]')
					('0:12:37', u'Phi(6.47294)')
					('0:13:18', u'Q(6.47294)')
	part3_correct_attempt
					['0:26:55', u'Q([320 - 301.71]/5.76091)']

26 Student ID:b3hwang

	first_attempt
					2015-11-05 09:54:14
	part1_correct_attempt
					['0:00:00', u'174 * .85']
	part2_correct_attempt
					['10:28:28', u'((.85*174)(1-.85))^(1/2)']
	part3_incorrect_attempt
					('10:30:03', u'1-Phi((174-147.9)/4.7101)')
					('10:30:46', u'((160-147.9)/4.7101)')
	part3_correct_attempt
					['10:30:57', u'1-Phi((160-147.9)/4.7101)']

27 Student ID:ccn001

	first_attempt
					2015-11-05 17:45:58
	part1_correct_attempt
					['0:00:00', u'259(.81)']
	part2_correct_attempt
					['4:20:35', u'((.81)(1-.81)(259))^(0.5)']
	part3_incorrect_attempt
					('4:20:35', u'Q(((.81)(1-.81)(259))^(0.5))')
					('4:20:40', u'1- Q(((.81)(1-.81)(259))^(0.5))')
					('4:22:15', u'Q(((.81)(1-.81)(259))^(0.5))')
					('4:25:12', u'Q(((.81)(1-.81)(230))^(0.5))')
					('4:25:21', u'Q(((.81)(1-.81)(231))^(0.5))')
					('4:27:32', u'Q(((.88)(1-.88)(259))^(0.5))')
					('4:27:42', u'Q(((.89)(1-.89)(259))^(0.5))')
					('4:30:02', u'Q(0)')
					('4:33:22', u'Q(((.90)(1-.90)(259))^(0.5))')
					('4:47:12', u'Q(((230/259)(1-(230/259))(259))^(0.5))')
					('4:49:37', u'Q(((231/259)(1-(231/259))(259))^(0.5))')
					('4:50:30', u'Q(((231/259)(1-(231/259))/(259))^(0.5))')
					('4:50:50', u'Q(((.81)(1-.81)/(259))^(0.5))')
	part3_correct_attempt
					['7:16:57', u'Q((230-259(.81))/((.81)(1-.81)(259))^(0.5))']

28 Student ID:quwong

	first_attempt
					2015-11-02 05:22:40
	part1_correct_attempt
					['0:00:00', u'186*0.85']
	part2_correct_attempt
					['0:00:00', u'(186*0.85*(1-0.85))^0.5']
	part3_incorrect_attempt
					('0:02:08', u'5.586289 * 10^(-7)')
					('0:03:55', u'1-(5.586289 * 10^(-7))')
					('0:07:58', u'5.050816*10^(-9)')
					('0:08:26', u'1/197987815')
					('0:09:02', u'1-1/197987815')
	part3_correct_attempt
					['0:10:30', u'0.00727']

29 Student ID:asetters

	first_attempt
					2015-11-05 20:41:16
	part1_correct_attempt
					['0:00:00', u'308*.86']
	part2_correct_attempt
					['0:45:14', u'sqrt(.86(1-.86)*308)']
	part3_incorrect_attempt
					('0:47:03', u'Q(290)')
	part3_correct_attempt
					['5:45:41', u'Q((290-308*.86)/sqrt(.86(1-.86)*308))']

30 Student ID:c1sorian

	first_attempt
					2015-11-05 01:11:52
	part1_correct_attempt
					['0:00:00', u'.88*376']
	part2_correct_attempt
					['1 day, 2:59:08', u'(.88*.12*376)^.5']
	part3_incorrect_attempt
					('1 day, 3:00:36', u'((350-330.88)/((.88*.12*376)^.5))')
	part3_correct_attempt
					['1 day, 3:00:50', u'Q(((350-330.88)/((.88*.12*376)^.5)))']

31 Student ID:atorr

	first_attempt
					2015-11-06 00:45:21
	part1_correct_attempt
					['0:00:00', u'386 * .83']
	part3_incorrect_attempt
					('0:05:38', u'(386 - 350)/350')

32 Student ID:skarimik

	first_attempt
					2015-11-06 03:11:16
	part1_correct_attempt
					['0:00:00', u'327*(83/100)']
	part2_correct_attempt
					['0:06:03', u'sqrt(327*(83/100)(1-(83/100)))']
	part3_incorrect_attempt
					('0:12:37', u'(1/(327*(83/100)))/327')
					('0:15:00', u'1/(327*(83/100))')
					('0:15:09', u'1-1/(327*(83/100))')
					('0:20:48', u'1-83/100')
					('0:21:08', u'327(1-83/100)')
					('0:27:01', u'C(327,290)(83/100)^(290)(17/100)^(37)')
					('0:27:26', u'C(327,290)*(83/100)^(290)(17/100)^(37)')
					('0:32:16', u'.0010949')
					('0:32:36', u'.001094915')
					('0:40:31', u'.1/((327-271.41)/6.79262)^2')
					('0:40:49', u'1/((327-271.41)/6.79262)^2')
					('0:44:53', u'17/100')
					('0:45:13', u'327(17/100)')
					('0:45:32', u'37(17/100)')
					('0:49:22', u'0.00161238')
					('0:54:35', u'0.001612')
	part3_correct_attempt
					['1:12:54', u'1-Phi(((290-327*(83/100))/sqrt(327*(83/100)(1-(83/100)))))']

33 Student ID:thk002

	first_attempt
					2015-11-05 06:59:05
	part1_correct_attempt
					['0:00:00', u'174*.82']
	part2_correct_attempt
					['0:00:29', u'sqrt(174*.82*.18)']
	part3_incorrect_attempt
					('0:02:10', u'(160-142.68)/(sqrt(174*.82*.18))')
					('0:04:13', u'(160-(174*.82))/(sqrt(174*.82*.18))')
					('0:04:34', u'(160-(174*.82))/5.06778')
					('0:05:09', u'(174-(174*.82))/5.06778')
					('0:05:58', u'Q(6.18022)')
					('0:06:09', u'Phi(6.18022)')
					('0:08:05', u'(160- 142.68)/6.06778')
					('0:10:51', u'((160- 142.68)/6.06778)')
	part3_correct_attempt
					['1:05:29', u'Q((160- 142.68)/5.06778)']

34 Student ID:krau

	first_attempt
					2015-11-04 19:56:43
	part1_correct_attempt
					['0:00:00', u'.81*327']
	part2_correct_attempt
					['7:40:32', u'sqrt(327*.81*.19)']
	part3_incorrect_attempt
					('7:41:20', u'Q(290-.81*327/sqrt(327*.81*.19))')
	part3_correct_attempt
					['7:41:28', u'Q((290-.81*327)/sqrt(327*.81*.19))']

35 Student ID:crmirand

	first_attempt
					2015-11-03 06:45:04
	part1_correct_attempt
					['0:00:00', u'.86*208']
	part2_correct_attempt
					['0:01:41', u'(.86*208*.14)^.5']
	part3_incorrect_attempt
					('0:02:34', u'(200 - (.86*208))/(.86*208*.14)^.5')
					('0:02:57', u'0.000012')
					('0:04:22', u'0.000005')
					('0:04:28', u'0.000005*2')
					('0:04:42', u'0.000012*2')
					('0:05:28', u'200 - 178.88')
					('0:05:45', u'21.12/5.00432')
					('0:06:06', u'0.000012')
					('0:08:24', u'0.000005')
					('0:11:30', u'1.1614E-6')
					('0:20:43', u'(.86*208/2)^.5')
					('0:22:41', u'0.000012 - C(208,200) *.86^200*.14^8')
					('0:24:37', u'2.945842E-9')
					('0:53:36', u'Q(200)')
					('0:53:42', u'Q(201)')
					('0:53:48', u'-Q(201)')
					('0:56:25', u'Phi(201)')
					('0:56:32', u'Phi(200)')
					('0:56:37', u'1 - Phi(200)')
					('0:56:43', u'1 - Phi(201)')
					('0:58:17', u'Phi(201)')
					('0:58:29', u'1 - Phi (208)')
					('0:58:39', u'1 - Phi (200)')
					('0:59:48', u'Phi(200)')
					('0:59:56', u'1 - Phi(200)')
	part3_correct_attempt
					['1:01:44', u'1 - Phi((200 - .86*208)/(.86*208*.14)^.5)']

36 Student ID:beyounge

	first_attempt
					2015-10-30 06:38:28
	part1_correct_attempt
					['0:00:00', u'0.86 * 356']
	part2_correct_attempt
					['0:20:40', u'sqrt((0.86 * 356) - (0.86^2 * 356))']
	part3_incorrect_attempt
					('0:28:41', u'((0.86 * 356 - 0.86^2 * 356) / (330 - 0.86 * 356) ^ 2)')
					('17:45:00', u'1- (0.86^2 * 330) / (0.86 * 330)')
					('18:25:11', u'[((0.86 * 356) - (0.86^2 * 356))/ (330 ^ 2)]')
					('18:25:41', u'[((0.86 * 356) - (0.86^2 * 356))/ (26 ^ 2)]')
					('18:26:28', u'[((0.86 * 356) - (0.86^2 * 356))/ ((0.86*356) ^ 2)]')
					('18:27:05', u'[((0.86 * 356) - (0.86^2 * 356))/ (26 ^ 2)]')
					('18:27:15', u'[((0.86 * 356) - (0.86^2 * 356))/ (26 ^ 2)]/2')
					('18:36:26', u'1 - (330/356)')
					('18:36:44', u'1 - (331/356)')
	part3_correct_attempt
					['6 days, 0:30:36', u'1- [0.5 + 0.5*erf((330 - (0.86 * 356))/sqrt((0.86 * 356) - (0.86^2 * 356))/sqrt(2))]']

37 Student ID:psable

	first_attempt
					2015-11-06 01:02:30
	part1_correct_attempt
					['0:00:00', u'180.11']
	part2_correct_attempt
					['0:02:45', u'5.53342']
	part3_incorrect_attempt
					('0:04:32', u'Q(6.66676)')
	part3_correct_attempt
					['0:05:43', u'Q(1.787321)']

38 Student ID:tpmach

	first_attempt
					2015-11-05 17:20:08
	part1_correct_attempt
					['0:00:00', u'0.84*334']
	part2_correct_attempt
					['0:38:36', u'sqrt(0.84(1-0.84)334)']
	part3_incorrect_attempt
					('1:08:07', u'1-Phi(sqrt(0.84(1-0.84)334))')
					('1:09:36', u'(334-0.84*334)/(sqrt(0.84(1-0.84)334))')
					('1:11:01', u'1-Phi(2*sqrt(0.84(1-0.84)334))')
					('1:11:07', u'1-Phi(sqrt(0.84(1-0.84)334))')
					('1:14:39', u'1-Phi((334-0.84*334)/sqrt(0.84(1-0.84)334))')
					('8:43:41', u'1-(Phi((300)84*334)/sqrt(0.84(1-0.84)334))')
					('8:44:10', u'1-Phi((300-84*334)/sqrt(0.84(1-0.84)334))')
	part3_correct_attempt
					['8:44:28', u'1-Phi((300-0.84*334)/sqrt(0.84(1-0.84)334))']

39 Student ID:k4ma

	first_attempt
					2015-11-06 22:06:34
	part1_correct_attempt
					['0:00:00', u'314']
	part2_correct_attempt
					['0:04:32', u'sqrt(.86*(1-.86)*365)']
	part3_incorrect_attempt
					('0:04:45', u'1-Phi(sqrt(.86*(1-.86)*365))')
					('0:08:12', u'1-Phi((365-314)/sqrt(.86*(1-.86)*365))')
					('0:09:52', u'1-Phi((330-314)/sqrt(.86*(1-.86)*365))')
					('0:10:13', u'1-Phi((365-314)/sqrt(.86*(1-.86)*365))')
					('0:10:44', u'1-Phi((330-284)/sqrt(.86*(1-.86)*330))')
					('0:12:19', u'1-Phi((365-314)/sqrt(.86*(1-.86)*365))')
					('0:15:23', u'1-Phi((330-284)/sqrt(.86*(1-.86)*330))')
					('0:15:32', u'1-Phi((330-283)/sqrt(.86*(1-.86)*330))')
					('0:17:38', u'1-Phi((365-314)/sqrt(.86*(1-.86)*365))')
					('0:18:14', u'1-[[1-Phi((365-314)/sqrt(.86*(1-.86)*365))]*2]')
					('0:18:57', u'1-Phi((365-314)/sqrt(.86*(1-.86)*365))')
					('0:19:14', u'2*(1-Phi((365-314)/sqrt(.86*(1-.86)*365)))')
					('0:19:25', u'1-(2*(1-Phi((365-314)/sqrt(.86*(1-.86)*365))))')
					('0:20:55', u'1-Phi((365-314)/sqrt(.86*(1-.86)*365))')

40 Student ID:dwzhang

	first_attempt
					2015-11-06 21:43:17
	part1_correct_attempt
					['0:00:00', u'301*.83']
	part2_correct_attempt
					['0:00:00', u'sqrt(301* 0.83 * (1-0.83))']
	part3_incorrect_attempt
					('0:06:29', u'(290 - 301*.83) / sqrt(301* 0.83 * (1-0.83))')
					('0:06:40', u'301*.83 / (sqrt(301* 0.83 * (1-0.83)))')
					('0:06:55', u'(290 - 301*.83) / (sqrt(301* 0.83 * (1-0.83)))')
	part3_correct_attempt
					['0:13:23', u'1 - Phi ( (270-0.83*301) / (sqrt(301* 0.83 * (1-0.83))))']

41 Student ID:rraiyyan

	first_attempt
					2015-11-07 00:19:59
	part1_correct_attempt
					['0:00:00', u'333*0.84']
	part2_correct_attempt
					['0:02:42', u'sqrt(0.84 * (1-0.84) * 333)']
	part3_incorrect_attempt
					('0:02:52', u'1- Q(sqrt(0.84 * (1-0.84) * 333))')
					('0:03:03', u'Q(sqrt(0.84 * (1-0.84) * 333))')
					('0:03:52', u'333-333*0.84/(sqrt(0.84 * (1-0.84) * 333))')
					('0:04:14', u'(333-333*0.84)/(sqrt(0.84 * (1-0.84) * 333))')
					('0:06:20', u'1 - Q((333-333*0.84)/(sqrt(0.84 * (1-0.84) * 333)))')
					('0:06:48', u'333 - 333*0.84')
	part3_correct_attempt
					['0:07:29', u'Q((300-333*0.84)/(sqrt(0.84 * (1-0.84) * 333)))']

42 Student ID:jhw015

	first_attempt
					2015-11-04 21:36:37
	part1_correct_attempt
					['0:00:00', u'0.85*201']
	part2_correct_attempt
					['0:02:47', u'sqrt(201 * 0.85(0.15))']
	part3_incorrect_attempt
					('1 day, 21:32:21', u'Q(190-201*0.85/sqrt(201*0.85*0.15))')
	part3_correct_attempt
					['1 day, 21:32:42', u'Q((190-201*0.85)/sqrt(201*0.85*0.15))']

43 Student ID:dsmonaha

	first_attempt
					2015-11-04 18:20:29
	part1_correct_attempt
					['0:00:00', u'361*.88']
	part3_incorrect_attempt
					('0:16:09', u'(.88)^361')
					('0:20:56', u'1-.984476')
					('0:24:19', u'1-.984476')
					('0:25:00', u'.015524')
					('0:59:06', u'.008428')
					('0:59:30', u'1-.008428')

44 Student ID:krkelkar

	first_attempt
					2015-11-02 23:25:52
	part1_correct_attempt
					['0:00:00', u'209 * .86']
	part2_correct_attempt
					['0:00:31', u'sqrt( 209 * .86 * (1-.86) )']
	part3_incorrect_attempt
					('0:13:01', u'Q ( (209-.86*209)/(.86*209*.14))')
					('1:01:14', u'Q ( (200-.86*209)/(.86*209*.14)) - Q ( (209-.86*209)/(.86*209*.14))')
					('1:01:44', u'0.5(Q ( (200-.86*209)/(.86*209*.14)) - Q ( (209-.86*209)/(.86*209*.14)))')
					('1:02:24', u'Q ( (201-.86*209)/(.86*209*.14)) - Q ( (209-.86*209)/(.86*209*.14))')
					('1:03:01', u'Q ( (201-.86*209)/(.86*209*.14)) - Q ( (210-.86*209)/(.86*209*.14))')
					('1:18:22', u'.087914')
					('1:20:53', u'.2103719')
	part3_correct_attempt
					['1:22:46', u'Q( (200 - (.86*209))/(sqrt(209*.86*.14)))']

45 Student ID:jel075

	first_attempt
					2015-11-05 23:00:20
	part1_correct_attempt
					['0:00:00', u'351.12']
	part2_correct_attempt
					['0:00:43', u'sqrt(399*(0.88) * (1-0.88))']
	part3_incorrect_attempt
					('0:00:55', u'1-Phi(sqrt(399*(0.88) * (1-0.88)))')
					('0:02:19', u'1-Phi((399-351.12)/6.4911)')
					('0:02:40', u'1-Phi((371-351.12)/6.4911)')
	part3_correct_attempt
					['0:02:45', u'1-Phi((370-351.12)/6.4911)']

46 Student ID:edescobe

	first_attempt
					2015-11-01 10:10:23
	part1_correct_attempt
					['0:00:00', u'379*.88']
	part2_correct_attempt
					['0:00:00', u'(379*.88*.12)^(1/2)']
	part3_incorrect_attempt
					('0:03:05', u'1-.99534')
					('0:04:06', u'1-.99547')
					('1:13:50', u'1-.99547')
					('1:54:01', u'1-.99598')
					('1:54:33', u'1-.99534')
					('1:55:15', u'1-.99632')
					('2:00:19', u'1-.996')
					('4 days, 22:47:40', u'(350-379*.88)/((379*.88*.12)^(1/2))')
					('4 days, 22:47:45', u'1-.99547')
					('4 days, 22:47:59', u'1-.99534')
					('4 days, 22:51:16', u'1-.995')
	part3_correct_attempt
					['4 days, 22:55:04', u'Q((350-333.52)/6.32633)']

47 Student ID:w4shin

	first_attempt
					2015-11-06 23:52:56
	part1_correct_attempt
					['0:00:00', u'335*.88']
	part2_correct_attempt
					['0:00:00', u'sqrt(335*.88*.12)']
	part3_incorrect_attempt
					('0:00:00', u'1-Phi(310/sqrt(335*.88*.12))')
	part3_correct_attempt
					['0:01:27', u'1-Phi((310-335*.88)/sqrt(335*.88*.12))']

48 Student ID:muy002

	first_attempt
					2015-11-06 05:04:53
	part1_correct_attempt
					['0:00:00', u'228*80/100']
	part2_correct_attempt
					['0:00:37', u'sqrt(80/100*(20/100)*228)']
	part3_incorrect_attempt
					('0:01:24', u'Q(sqrt(80/100*(20/100)*228))')
					('0:22:02', u'(228-228*80/100)/sqrt(80/100*(20/100)*228)')
					('0:23:04', u'(200-228*80/100)/sqrt(80/100*(20/100)*228)')
					('1:08:57', u'(228*80/100)*(sqrt(80/100*(20/100)*228))')
					('1:12:30', u'2*Q(sqrt(80/100*(20/100)*228))')
					('1:22:27', u'Q(sqrt(20/100*(80/100)*228))')
					('1:28:16', u'(228*80/100)/(sqrt(80/100*(20/100)*228))')
					('1:29:34', u'(228-228*80/100)/(sqrt(80/100*(20/100)*228))')
					('1:32:04', u'((200-228*80/100)/(sqrt(80/100*(20/100)*228)))')
					('1:52:20', u'((201-228*80/100)/(sqrt(80/100*(20/100)*228)))')
	part3_correct_attempt
					['1:54:25', u'Q((200-228*80/100)/(sqrt(80/100*(20/100)*228)))']

49 Student ID:dan029

	first_attempt
					2015-11-05 10:03:26
	part1_correct_attempt
					['0:00:00', u'.81*220']
	part2_correct_attempt
					['0:01:47', u'sqrt(220*.81*.19)']
	part3_incorrect_attempt
					('0:09:06', u'1.8/sqrt(220*.81*.19)')
					('0:09:15', u'1-1.8/sqrt(220*.81*.19)')
					('0:09:55', u'2.8/sqrt(220*.81*.19)')
					('0:11:26', u'Q(-2.8/sqrt(220*.81*.19))')
					('0:13:44', u'Q(.81*220-200/sqrt(220*.81*.19))')
	part3_correct_attempt
					['0:14:23', u'Q(21.8/sqrt(220*.81*.19))']

50 Student ID:qfu

	first_attempt
					2015-11-06 03:21:34
	part1_correct_attempt
					['0:00:00', u'324*0.82']
	part2_correct_attempt
					['0:00:00', u'sqrt(324*0.82*0.18)']
	part3_incorrect_attempt
					('0:00:00', u'(290-324*0.82)/sqrt(324*0.82*0.18)')
					('0:01:13', u'(324-324*0.82)/sqrt(324*0.82*0.18)')
	part3_correct_attempt
					['0:02:25', u'Q((290-324*0.82)/sqrt(324*0.82*0.18))']

51 Student ID:dcastlem

	first_attempt
					2015-11-03 01:28:34
	part1_correct_attempt
					['0:00:00', u'182*.8']
	part2_correct_attempt
					['0:01:34', u'sqrt(.8*.2*182)']
	part3_incorrect_attempt
					('0:03:56', u'145.6/5.3963')
					('0:04:03', u'145.6*5.3963')
					('0:04:15', u'5.3963/145.6')
					('0:12:03', u'.80^182')
					('0:12:12', u'.80^160')
					('0:12:20', u'.80^161')
					('0:15:25', u'(.8)^182*.4')
					('0:15:36', u'(.8)^160*.4')
					('0:15:59', u'.8^182*.4')
					('0:21:56', u'C(182,182)*.8^182*.2^0')
					('0:24:58', u'.8^182')
					('0:58:09', u'.8^160')
					('0:58:18', u'.8^145.6')
					('0:58:35', u'.8^5.3963')
	part3_correct_attempt
					['1 day, 23:09:24', u'Q((160-.8*182)/sqrt(.8*.2*182))']

52 Student ID:bpandayk

	first_attempt
					2015-11-06 21:37:06
	part1_correct_attempt
					['0:00:00', u'323*83/100']
	part2_correct_attempt
					['0:00:00', u'sqrt((323*83/100)*(1-83/100))']
	part3_incorrect_attempt
					('0:00:00', u'Q(sqrt((323*83/100)*(1-83/100)))')
	part3_correct_attempt
					['0:01:29', u'Q((290-(323*83/100))/sqrt((323*83/100)*(1-83/100)))']

53 Student ID:hsc052

	first_attempt
					2015-11-06 23:37:11
	part1_correct_attempt
					['0:00:00', u'229*0.82']
	part2_correct_attempt
					['0:00:00', u'sqrt(229*0.82(1-0.82))']
	part3_incorrect_attempt
					('0:00:00', u'[229-229*0.82]/sqrt(229*0.82(1-0.82))')
	part3_correct_attempt
					['0:00:44', u'Q([200-229*0.82]/sqrt(229*0.82(1-0.82)))']

54 Student ID:xil109

	first_attempt
					2015-11-06 01:41:45
	part1_correct_attempt
					['0:00:00', u'312*0.83']
	part2_correct_attempt
					['0:00:29', u'sqrt(312*0.83*(1-0.83))']
	part3_incorrect_attempt
					('0:01:58', u'(280-312*0.83)/sqrt(312*0.83*(1-0.83))')
	part3_correct_attempt
					['0:02:38', u'0.000759419']

55 Student ID:zhz159

	first_attempt
					2015-11-06 00:01:34
	part1_correct_attempt
					['0:00:00', u'322.26']
	part2_correct_attempt
					['0:27:24', u'7.6162195']
	part3_incorrect_attempt
					('0:27:24', u'8.261E-9')
	part3_correct_attempt
					['0:28:43', u'0.000135153']

56 Student ID:sghouse

	first_attempt
					2015-11-05 21:06:52
	part1_correct_attempt
					['0:00:00', u'187.79']
	part2_correct_attempt
					['0:00:00', u'sqrt(.89*(1-.89)*211)']
	part3_incorrect_attempt
					('0:05:11', u'.11^211')
					('0:05:30', u'.89^211')
					('0:16:51', u'.89^211')
					('3:11:13', u'Q(5)')
					('3:12:29', u'Q(5.10673)')
	part3_correct_attempt
					['5:18:25', u'Q(22.21/sqrt(.89*(1-.89)*211))']

57 Student ID:k3tan

	first_attempt
					2015-11-04 18:16:12
	part1_correct_attempt
					['0:00:00', u'176.8']
	part2_correct_attempt
					['0:22:42', u'5.149']
	part3_incorrect_attempt
					('2 days, 5:23:44', u'0.002275')
					('2 days, 5:24:13', u'0.00227504608')

58 Student ID:haw081

	first_attempt
					2015-11-02 02:29:14
	part1_correct_attempt
					['0:00:00', u'0.86*251']
	part2_correct_attempt
					['0:01:07', u'sqrt(251*0.86*(1-0.86))']
	part3_incorrect_attempt
					('0:07:34', u'Q(4.39)')
					('0:08:39', u'1-Q(4.39)')
					('0:08:52', u'1-Q(-4.39)')
	part3_correct_attempt
					['0:10:38', u'Q((240-215.86)/5.49731)']

59 Student ID:h4tu

	first_attempt
					2015-11-07 00:26:32
	part1_correct_attempt
					['0:00:00', u'287*0.86']
	part2_correct_attempt
					['0:00:35', u'sqrt(0.86*0.14*287)']
	part3_incorrect_attempt
					('0:01:54', u'(280-287*0.86)/sqrt(0.86*0.14*287)')
					('0:02:21', u'1-Phi((280-287*0.86)/sqrt(0.86*0.14*287))')
					('0:21:51', u'1-Phi((287*0.86)/sqrt(0.86*0.14*287))')
	part3_correct_attempt
					['0:22:02', u'1-Phi((270-287*0.86)/sqrt(0.86*0.14*287))']

60 Student ID:lywong

	first_attempt
					2015-11-02 04:55:04
	part1_correct_attempt
					['0:00:00', u'348.88']
	part2_correct_attempt
					['3 days, 18:56:59', u'sqrt(392*0.89(1-0.89))']
	part3_incorrect_attempt
					('3 days, 18:59:28', u'sqrt(392-348.88/sqrt(392*0.89(1-0.89)))')
					('3 days, 18:59:54', u'Q(sqrt((392-348.88)/sqrt(392*0.89(1-0.89))))')
					('3 days, 19:01:05', u'1-Q(sqrt((392-348.88)/sqrt(392*0.89(1-0.89))))')
					('3 days, 19:01:51', u'Q(sqrt((392-348.88)/sqrt(392*0.89(1-0.89))))')
					('3 days, 19:02:40', u'(392-348.88)/(sqrt(392*0.89(1-0.89)))')
	part3_correct_attempt
					['3 days, 19:04:00', u'Q((360-348.88)/(sqrt(392*0.89(1-0.89))))']

61 Student ID:jix029

	first_attempt
					2015-11-01 21:03:16
	part1_correct_attempt
					['0:00:00', u'162*.81']
	part2_correct_attempt
					['0:03:29', u'(162*.81(1-.81))^.5']
	part3_incorrect_attempt
					('0:06:03', u'3.747^10-5')
					('0:06:15', u'3.747^10^-5')
					('0:08:40', u'3.747*10^-5')
					('1:54:48', u'1-.99991504')
					('1:56:15', u'.0000368')
					('1:56:43', u'.0000837665')
					('2:03:05', u'8.97638528096767E-06')
					('2:04:11', u'2.76128185879854E-05')
					('2:05:52', u'8.97638528096767E-06')
					('2:37:34', u'8.97E-06')
					('2 days, 8:51:15', u'.00008')
					('2 days, 8:51:55', u'.00004')
					('2 days, 8:51:59', u'.00005')
					('2 days, 8:52:03', u'.00003')
					('4 days, 0:56:49', u'(162!/(150!*12!))*.81^150*.19^12')
					('4 days, 1:00:03', u'8.97638528096767E-06')
					('4 days, 1:52:39', u'.02')
	part3_correct_attempt
					['4 days, 1:54:09', u'.0000845']

62 Student ID:hkhodada

	first_attempt
					2015-11-03 01:25:05
	part1_correct_attempt
					['0:00:00', u'0.81*332']
	part2_correct_attempt
					['0:07:07', u'sqrt(51.0948)']
	part3_incorrect_attempt
					('0:08:21', u'(0.81*332)/290')
					('0:12:08', u'(0.81*290)/332')
					('0:50:27', u'(332*0.81)/290')
					('0:54:39', u'7.14806/268.92')
					('1 day, 18:20:30', u'Q(2.952)')
					('1 day, 18:21:27', u'Q(290-0.81*332/sqrt(51.094))')
	part3_correct_attempt
					['1 day, 18:21:53', u'Q((290-0.81*332)/sqrt(51.094))']

63 Student ID:glcohen

	first_attempt
					2015-11-03 22:33:22
	part1_correct_attempt
					['0:00:00', u'(172*.85)']
	part2_correct_attempt
					['9:29:00', u'sqrt(172*.85*.15)']
	part3_incorrect_attempt
					('9:30:44', u'((172-146.2)/sqrt(172*.85*.15))')
					('21:47:32', u'(170-142.6)/sqrt(172*.85*.15)')
					('21:47:47', u'(171-142.6)/sqrt(172*.85*.15)')
					('21:47:52', u'(172-142.6)/sqrt(172*.85*.15)')
					('22:13:12', u'((170-142.6)/sqrt(172*.85*.15))')
	part3_correct_attempt
					['22:24:28', u'Q((170-146.2)/sqrt(172*.85*.15))']

64 Student ID:achava

	first_attempt
					2015-11-06 08:36:09
	part1_correct_attempt
					['0:00:00', u'336*.8']
	part2_correct_attempt
					['0:00:32', u'sqrt((.8)(.2)336)']
	part3_incorrect_attempt
					('0:01:59', u'(336-268.8)/7.33212')
					('0:11:49', u'(300-268.8)/7.33212')
					('0:13:07', u'8.539898*10^(-6)')
					('0:13:28', u'2.334576*10^(-6)')
					('0:25:00', u'0.9999982695')
					('0:25:25', u'1-0.9999982695')
					('0:26:10', u'1.73047602*10^(-6)')
					('0:55:52', u'Q(4.25)')
					('0:57:05', u'Q(9.17)')
					('0:57:35', u'Q(4.255)')
	part3_correct_attempt
					['0:59:13', u'Q((300-268.8)/(sqrt((.8)(.2)336)))']

65 Student ID:sachadal

	first_attempt
					2015-11-05 21:29:44
	part1_correct_attempt
					['0:00:00', u'0.85*201']
	part2_correct_attempt
					['1 day, 1:27:04', u'sqrt((0.85)*(0.15)*201)']
	part3_incorrect_attempt
					('1 day, 1:27:36', u'(201 - (0.85*201))/(sqrt((0.85)*(0.15)*201))')
					('1 day, 1:28:14', u'(190 - (0.85*201))/(sqrt((0.85)*(0.15)*201))')
					('1 day, 1:29:38', u'(201 - (0.85*201))/(sqrt((0.85)*(0.15)*201))')
	part3_correct_attempt
					['1 day, 1:41:56', u'Q((190 - (0.85*201))/(sqrt((0.85)*(0.15)*201)))']

66 Student ID:pvl001

	first_attempt
					2015-11-03 21:02:38
	part1_correct_attempt
					['0:00:00', u'.89 * 397']
	part2_correct_attempt
					['6:58:22', u'sqrt(397 * .89 * .11)']
	part3_incorrect_attempt
					('6:59:34', u'1 - Phi((397 - (.89 * 397))/sqrt(397 * .89 * .11))')
					('6:59:52', u'(397 - (.89 * 397))/sqrt(397 * .89 * .11)')
					('7:10:08', u'.11')
	part3_correct_attempt
					['7:12:14', u'1 - Phi((380 - (.89 * 397))/(sqrt(397 * .89 * .11)))']

67 Student ID:dlt009

	first_attempt
					2015-11-05 08:56:08
	part1_correct_attempt
					['0:00:00', u'.82*244']
	part2_correct_attempt
					['-1 day, 23:59:33', u'sqrt[244*.82*.18]']
	part3_incorrect_attempt
					('0:01:16', u'1-[(.82)(244)/220]')
					('0:02:34', u'1/82')
	part3_correct_attempt
					['0:17:42', u'1-Phi[ (220-(244*.82)) /(sqrt[244*.82*.18]) ]']

68 Student ID:mbl003

	first_attempt
					2015-11-06 21:13:15
	part1_correct_attempt
					['0:00:00', u'282*.85']
	part2_correct_attempt
					['0:03:06', u'sqrt(.85(1-.85)282)']
	part3_incorrect_attempt
					('0:04:36', u'(282-(282*.85))/(sqrt(.85(1-.85)282))')
					('0:14:32', u'Q(260-282*.85/(sqrt(.85(1-.85)282)))')
	part3_correct_attempt
					['0:15:03', u'Q((260-(282*.85))/(sqrt(.85(1-.85)282)))']

69 Student ID:n2patil

	first_attempt
					2015-11-05 02:39:48
	part1_correct_attempt
					['0:00:00', u'165.6']
	part2_correct_attempt
					['0:00:44', u'33.12^(1/2)']
	part3_incorrect_attempt
					('0:04:14', u'0.9938')
					('1:20:50', u'1-Phi((207-165.6)/33.12^(1/2))')
	part3_correct_attempt
					['1:21:37', u'1-Phi((180-165.6)/33.12^(1/2))']

70 Student ID:ttimmons

	first_attempt
					2015-11-03 18:51:59
	part1_correct_attempt
					['0:00:00', u'165*0.87']
	part2_correct_attempt
					['0:04:45', u'sqrt(165*(0.87)*(1-0.87))']
	part3_incorrect_attempt
					('1 day, 1:11:25', u'[165-165*0.87]/[sqrt(165*(0.87)*(1-0.87))]')
					('1 day, 1:12:12', u'1-Q([165-165*0.87]/[sqrt(165*(0.87)*(1-0.87))])')
	part3_correct_attempt
					['1 day, 1:15:59', u'Q([160-165*0.87]/[sqrt(165*(0.87)*(1-0.87))])']

71 Student ID:jnatale

	first_attempt
					2015-11-04 08:49:50
	part1_correct_attempt
					['0:00:00', u'226*.81']
	part2_correct_attempt
					['0:00:50', u'sqrt(226*.81*(1-.81))']
	part3_incorrect_attempt
					('0:02:45', u'200-(226*.81)')
					('0:02:53', u'1/(200-(226*.81))')
					('0:03:08', u'(200-(226*.81))/(sqrt(226*.81*(1-.81)))')
					('0:07:49', u'1/(200-(226*.81))/(sqrt(226*.81*(1-.81)))')
					('0:07:59', u'1/((200-(226*.81))/(sqrt(226*.81*(1-.81))))')
					('0:08:19', u'1-(1/((200-(226*.81))/(sqrt(226*.81*(1-.81)))))')
					('0:08:38', u'(200-(226*.81))/(sqrt(226*.81*(1-.81)))')
					('0:25:25', u'(226-(226*.81))/(sqrt(226*.81*(1-.81)))')
					('0:27:40', u'.00008')
					('0:30:58', u'.00219')
					('0:31:11', u'.00159')
					('0:31:27', u'.00226')
					('0:31:38', u'.00233')
					('0:31:45', u'.00240')
					('0:31:54', u'.00248')
					('0:32:08', u'.00256')
					('0:32:20', u'.00212')
					('0:32:29', u'.00205')
					('0:32:39', u'.00199')
					('0:32:43', u'.00193')
					('0:33:52', u'.00175')
					('0:34:00', u'.00169')
					('0:34:09', u'.00181')
					('0:34:16', u'.00187')
					('0:34:30', u'.00154')
					('0:34:39', u'.00149')
					('0:34:46', u'.00144')
					('0:34:51', u'.00139')
					('0:36:59', u'.00154')
	part3_correct_attempt
					['17:55:17', u'Q((200-(226*.81))/(sqrt(226*.81*(1-.81))))']

72 Student ID:jblynch

	first_attempt
					2015-11-04 20:33:29
	part1_correct_attempt
					['0:00:00', u'.87*276']
	part2_correct_attempt
					['9:47:31', u'sqrt((.87)(276)(1-.87))']
	part3_incorrect_attempt
					('9:54:37', u'1 - 0.99981')
					('9:57:28', u'0.99981')
					('10:00:56', u'Q(260) + 1')
					('10:01:03', u'Q(261) + 1')
					('10:01:10', u'Q(260)')
					('10:01:15', u'Q(261)')
					('10:02:44', u'(1 - Q(261))')
					('19:40:19', u'0.99981')
					('19:40:57', u'0.99990')
					('19:42:55', u'1 - 0.99990')
					('19:43:23', u'1 - 0.99981')
					('19:47:04', u'1- 0.000187')
					('19:47:49', u'0.000187')
					('19:48:28', u'0.000093')
					('19:59:36', u'1 - 0.99981')
					('20:00:41', u'1 - 0.99991')
					('20:06:00', u'0.000187')
					('20:06:26', u'0.00019')
					('20:07:11', u'0.000093')
					('20:10:14', u'0.025749')
					('20:11:37', u'0.000093')
					('20:11:50', u'1/10748')
					('20:14:57', u'Q(3.7372)')
	part3_correct_attempt
					['20:15:56', u'Q((260 - 240.12)/5.58709)']

73 Student ID:tol003

	first_attempt
					2015-11-03 23:35:13
	part1_correct_attempt
					['0:00:00', u'167*.82']
	part2_correct_attempt
					['0:03:55', u'sqrt(167*.82(1-.82))']
	part3_incorrect_attempt
					('0:03:55', u'1-Phi(17/4.9468)')
					('0:04:14', u'Phi(17/4.9468)')
					('0:05:59', u'(167-167*.82)/sqrt(167*.82(1-.82))')
					('0:07:54', u'1-Phi(150)')
	part3_correct_attempt
					['0:11:24', u'1-Phi((150-(167*.82))/sqrt(167*.82(1-.82)))']

74 Student ID:skodigal

	first_attempt
					2015-11-06 20:28:19
	part1_correct_attempt
					['0:00:00', u'212*(.86)']
	part2_correct_attempt
					['0:00:00', u'sqrt(212*(.86)(1-.86))']
	part3_incorrect_attempt
					('0:10:04', u'[212 - (212*.86)]/(sqrt(212*(.86)(1-.86)))')
					('0:11:40', u'Q([212 - (212*.86)]/(sqrt(212*(.86)(1-.86)))) + .50')
					('0:16:40', u'.495306844')
					('0:17:56', u'(212-182)/(5.05221)')
					('0:18:21', u'(212-182)/(5.05221)')
					('0:27:06', u'(200-182)/(5.05221)')
					('0:27:17', u'(200-182.32)/(5.05221)')
	part3_correct_attempt
					['0:27:26', u'Q((200-182.32)/(5.05221))']

75 Student ID:aakumar

	first_attempt
					2015-11-05 06:01:56
	part1_correct_attempt
					['0:00:00', u'286*.8']
	part2_correct_attempt
					['0:05:17', u'sqrt(286*.8*.2)']
	part3_incorrect_attempt
					('0:07:28', u'286*.2')
					('0:14:46', u'Q(3.2818)')
	part3_correct_attempt
					['0:17:48', u'Q(3.134)']

76 Student ID:q3wen

	first_attempt
					2015-11-06 19:48:14
	part1_correct_attempt
					['0:00:00', u'155.2']
	part2_correct_attempt
					['0:00:00', u'5.57']
	part3_incorrect_attempt
					('0:00:00', u'Q(5.57)')
					('0:00:08', u'1-Q(5.57)')
					('0:03:39', u'Q(5.21)')
					('0:06:01', u'Q(2.66)')
					('0:06:52', u'Q(2.656)')
					('0:09:38', u'Q(2.657091)')
					('0:10:34', u'Q(6.9658)')
					('0:55:01', u'1-Q(6.964)')
	part3_correct_attempt
					['0:57:19', u'Q(2.656445335)']

77 Student ID:lguintu

	first_attempt
					2015-11-03 05:41:25
	part1_correct_attempt
					['0:00:00', u'244*.85']
	part2_correct_attempt
					['0:01:43', u'(244*.85*.15)^(1/2)']
	part3_incorrect_attempt
					('0:03:46', u'1-Phi((244*.85-230)/(244*.85*.15)^(1/2))')
	part3_correct_attempt
					['0:04:09', u'1-Phi((230-244*.85)/(244*.85*.15)^(1/2))']

78 Student ID:csl030

	first_attempt
					2015-11-06 00:26:22
	part1_correct_attempt
					['0:00:00', u'347 * .8']
	part2_correct_attempt
					['0:07:25', u'sqrt(277.6 * .2)']
	part3_incorrect_attempt
					('0:11:19', u'(347 - 277.6) / 7.45')
					('0:38:32', u'(300 - 277.6) / 7.45')
					('0:39:34', u'.9985')
					('0:41:56', u'(300 - 277.6) / 7.45')
					('0:47:43', u'1 - .9986')
					('0:48:48', u'1 - .9988')
					('0:51:04', u'1 - .9986')
	part3_correct_attempt
					['0:52:02', u'Q(3.006)']

79 Student ID:azkong

	first_attempt
					2015-11-06 20:23:24
	part1_correct_attempt
					['0:00:00', u'236(0.81)']
	part2_correct_attempt
					['0:01:08', u'sqrt(236(0.81)(1-0.81))']
	part3_incorrect_attempt
					('0:08:34', u'Q(236(0.81)/sqrt(236(0.81)(1-0.81)))')
	part3_correct_attempt
					['0:26:05', u'Q([210-236(0.81)]/sqrt(236(0.81)(1-0.81)))']

80 Student ID:volim

	first_attempt
					2015-11-04 23:36:58
	part1_correct_attempt
					['0:00:00', u'(317)*.84']
	part2_correct_attempt
					['0:23:08', u'[(((317)*.84)*(1-.84))^(1/2)]']
	part3_incorrect_attempt
					('0:23:31', u'e^[-[(((317)*.84)*(1-.84))^(1/2)]/((317)*.84)]')
					('1:17:29', u'Q(260-((317)*.84)/[(((317)*.84)*(1-.84))^(1/2)])')
	part3_correct_attempt
					['1:17:57', u'Q((290-((317)*.84))/[(((317)*.84)*(1-.84))^(1/2)])']

81 Student ID:abjara

	first_attempt
					2015-11-04 06:00:23
	part1_correct_attempt
					['0:00:00', u'204.18']
	part2_correct_attempt
					['0:03:43', u'sqrt(246*.83*(1-.83))']
	part3_incorrect_attempt
					('0:05:37', u'(230-204.18)/[sqrt(246*.83*(1-.83))]')
	part3_correct_attempt
					['0:05:54', u'Q((230-204.18)/[sqrt(246*.83*(1-.83))])']

82 Student ID:aurodrig

	first_attempt
					2015-11-07 00:12:07
	part1_correct_attempt
					['0:00:00', u'283*.89']
	part2_correct_attempt
					['0:00:46', u'sqrt(283*.89*(1-.89))']
	part3_incorrect_attempt
					('0:02:33', u'Q(270-283*.89/5.26362042704)')
					('0:02:55', u'Q(270-(283*.89)/5.26362042704)')
	part3_correct_attempt
					['0:03:05', u'Q((270-(283*.89))/5.26362042704)']

83 Student ID:hmnaing

	first_attempt
					2015-11-06 18:54:43
	part1_correct_attempt
					['0:00:00', u'390*.80']
	part2_correct_attempt
					['0:00:58', u'sqrt(390*.8 (1-.8))']
	part3_incorrect_attempt
					('0:11:54', u'Q(330 - (390*.80) / (sqrt(390*.8 (1-.8))) )')
	part3_correct_attempt
					['0:12:10', u'Q((330 - (390*.80)) / (sqrt(390*.8 (1-.8))) )']

84 Student ID:asp025

	first_attempt
					2015-11-06 23:53:51
	part1_correct_attempt
					['0:00:00', u'.84*284']
	part2_correct_attempt
					['0:01:22', u'[.16*.84*284]^(1/2)']
	part3_incorrect_attempt
					('0:03:19', u'(284-.84*284)/[.16*.84*284]^(1/2)')
					('0:03:46', u'(284-(.84*284))/[.16*.84*284]^(1/2)')
					('0:26:30', u'(1-Phi((3-0)/[85(.5+.5)^2/12]^(1/2)))')
					('0:51:50', u' 1-Phi((260-.81*337)/(284*.84(1-.84))^(1/2))')
					('0:52:10', u' 1-Phi((260-.84*337)/(284*.84(1-.84))^(1/2))')
	part3_correct_attempt
					['0:52:32', u' 1-Phi((260-.84*284)/(284*.84(1-.84))^(1/2))']

85 Student ID:dmn009

	first_attempt
					2015-11-05 10:04:38
	part1_correct_attempt
					['0:00:00', u'321.3']
	part2_correct_attempt
					['0:00:55', u'6.94226']
	part3_incorrect_attempt
					('0:01:42', u'2.03325')
					('0:02:17', u'.0210136')
	part3_correct_attempt
					['0:24:36', u'.0000178174']

86 Student ID:dlgoldbe

	first_attempt
					2015-11-05 07:02:17
	part1_correct_attempt
					['0:00:00', u'226*(0.8)']
	part2_correct_attempt
					['0:00:56', u'sqrt((226*(0.8))*(1-(0.8)))']
	part3_incorrect_attempt
					('10:01:57', u'(226-226*(0.8))/sqrt((226*(0.8))*(1-(0.8)))')
					('10:02:10', u'(226-(226*(0.8)))/sqrt((226*(0.8))*(1-(0.8)))')
					('10:06:00', u'((201)-(226*(0.8)))/(sqrt((226*(0.8))*(1-(0.8))))')
					('10:06:08', u'Q((201)-(226*(0.8)))/(sqrt((226*(0.8))*(1-(0.8))))')
					('1 day, 0:32:57', u'Q(4)')
					('1 day, 0:33:20', u'Q(3)')
	part3_correct_attempt
					['1 day, 0:34:49', u'Q((200-(226*0.8))/(sqrt((226*(0.8))*(1-(0.8)))))']

87 Student ID:kquong

	first_attempt
					2015-11-04 23:56:32
	part1_correct_attempt
					['0:00:00', u'264 * .89']
	part2_correct_attempt
					['0:05:35', u'sqrt(264 * .89 * .11)']
	part3_incorrect_attempt
					('0:08:58', u'(264 - 234.96)/(sqrt(264 * .89 * .11))')
					('0:09:23', u'(250 - 234.96)/(sqrt(264 * .89 * .11))')
					('3:55:41', u'Q(sqrt(264 * .89 * .11))')
					('5:12:33', u'Q(sqrt(264 * .89 * .11))')
					('5:39:12', u'(250.5 - 234.96) / (sqrt(264 * .89 * .11))')
					('5:41:32', u'0.0011')
					('5:51:03', u'(250.5 - 234.96) / (sqrt(264 * .89 * .11))')
					('5:56:25', u'.0015')
					('6:18:44', u' (250.5 - 234.96) / (sqrt(265 * .89 * .11))')
					('8:25:12', u' 1-Q((250.5 - 234.96) / (sqrt(264 * .89 * .11)))')
					('8:25:25', u' 1-Q((251 - 234.96) / (sqrt(264 * .89 * .11)))')
					('8:27:45', u' 1-Q((250.5 - 234.96) / (sqrt(264 * .89 * .11)))')
					('8:48:19', u' 1 - Q((250 - 234.96) / (sqrt(264 * .89 * .11)))')
	part3_correct_attempt
					['1 day, 17:43:04', u' Q((250 - 234.96) / (sqrt(264 * .89 * .11)))']

88 Student ID:t2shin

	first_attempt
					2015-11-05 21:59:16
	part1_correct_attempt
					['0:00:00', u'306*.89']
	part2_correct_attempt
					['0:01:13', u'sqrt(306*.89*.11)']
	part3_incorrect_attempt
					('0:05:56', u'1-0.99986464')
					('0:11:03', u'1-(189522596370757120325902215*(.89^290)*(.11^16))')
					('0:11:29', u'1-(189522596370757120325902215*(.89^306)*(.11^16))')
					('0:13:07', u'1-((.89^290)*(.11^16))')
					('0:14:38', u'(290.5-272.34)/5.47334')
					('0:15:09', u'(290-272.34)/5.47334')
					('0:22:37', u'.99999999')
					('0:24:41', u'.0002')
					('0:24:46', u'1-.0002')
					('0:25:55', u'.0003')
					('0:26:00', u'1-.0003')
					('0:26:41', u'1-.0003186')
					('0:26:48', u'.0003186')
					('0:27:33', u'Q(.0003186)')
					('0:28:44', u'1-Q(16/sqrt(306*.89*.11))')
	part3_correct_attempt
					['0:32:13', u'Q((290-272.34)/5.47334)']

89 Student ID:aportuga

	first_attempt
					2015-11-03 22:31:17
	part1_correct_attempt
					['0:00:00', u'344.43']
	part2_correct_attempt
					['0:01:24', u'6.15526603812']
	part3_incorrect_attempt
					('0:06:15', u'25.57/6.15526603812')
					('0:09:15', u'42.57/6.15526603812')
					('0:09:22', u'25.57/6.15526603812')

90 Student ID:ppanourg

	first_attempt
					2015-11-06 21:30:59
	part1_correct_attempt
					['0:00:00', u'378*.88']
	part2_correct_attempt
					['0:13:50', u'sqrt((378*.88)(1 - .88))']
	part3_incorrect_attempt
					('0:17:57', u'(378 - 378*(.88))/sqrt((378*.88)(1 - .88))')
					('0:19:22', u'(378 - 378*(.88))/sqrt((378*.88)(1 - .88))')
					('1:14:52', u'(378 - 378*(.88))/sqrt((378*.88)(1 - .88))')
					('1:18:35', u'.0001')
					('1:19:48', u'1 - Q((378 - 378*(.88))/sqrt((378*.88)(1 - .88)))')
					('1:21:39', u'1-Q((378 - 378*(.88))/sqrt((378*.88)(1 - .88)))')
					('1:32:59', u'((378 - 378*(.88))/sqrt((378*.88)(1 - .88)))')
					('1:34:35', u'((378 - 378*(.88))/sqrt((378*.88)(1 - .88)))')
					('1:34:57', u'1 - Phi(((378 - 378*(.88))/sqrt((378*.88)(1 - .88))))')
					('1:35:06', u'1 - Q(((378 - 378*(.88))/sqrt((378*.88)(1 - .88))))')
					('1:40:23', u'1 - Q(((379 - 378*(.88))/sqrt((378*.88)(1 - .88))))')
					('1:40:30', u'1 - Phi(((379 - 378*(.88))/sqrt((378*.88)(1 - .88))))')
	part3_correct_attempt
					['1:41:26', u'Q(((350 - 378*(.88))/sqrt((378*.88)(1 - .88))))']

91 Student ID:rohan

	first_attempt
					2015-11-07 00:25:00
	part1_correct_attempt
					['0:00:00', u'199*.86']
	part3_incorrect_attempt
					('0:04:28', u'.14')
					('0:30:16', u'199*.14')

92 Student ID:spw006

	first_attempt
					2015-11-04 03:30:12
	part1_correct_attempt
					['0:00:00', u'291*.83']
	part2_correct_attempt
					['0:00:27', u'sqrt((291*0.83*0.17))']
	part3_incorrect_attempt
					('0:00:53', u'1-Phi((sqrt((291*0.83*0.17))))')
					('0:06:11', u'1-Phi((291-91*.83)/(sqrt((291*0.83*0.17))))')
					('0:06:53', u'1-Phi((291-291*.83)/(sqrt((291*0.83*0.17))))')
	part3_correct_attempt
					['0:07:26', u'1-Phi((270-291*.83)/(sqrt((291*0.83*0.17))))']

93 Student ID:masaro

	first_attempt
					2015-11-03 17:38:11
	part1_correct_attempt
					['0:00:00', u'296*.86']
	part2_correct_attempt
					['0:02:56', u'sqrt(296*.86*(1-.86))']
	part3_incorrect_attempt
					('0:04:23', u'1-0.877543')
					('0:04:29', u'0.877543')
					('0:14:47', u'0.99999')
					('0:15:13', u'0.999999999')
					('0:17:09', u'1-0.99999')
					('0:17:21', u'0.99')
	part3_correct_attempt
					['1 day, 3:17:08', u'Q([280-296*.86]/sqrt(296*.86*(1-.86)))']

94 Student ID:rwthomps

	first_attempt
					2015-11-06 21:59:09
	part1_correct_attempt
					['0:00:00', u'376 * .85']
	part2_correct_attempt
					['1:07:51', u'sqrt(376 * .85 * .15)']
	part3_incorrect_attempt
					('1:08:03', u'Q(sqrt(376 * .85 * .15))')
	part3_correct_attempt
					['1:12:39', u'Q((340 - (376 * .85))/sqrt(376 * .85 * .15))']

95 Student ID:vsosnovs

	first_attempt
					2015-11-05 22:13:07
	part1_correct_attempt
					['0:00:00', u'.80(155)']
	part3_incorrect_attempt
					('0:02:32', u'.20')
					('1 day, 1:23:12', u'.1')

96 Student ID:k5law

	first_attempt
					2015-11-04 08:41:27
	part1_correct_attempt
					['0:00:00', u'.88*282']
	part2_correct_attempt
					['0:01:15', u'sqrt(.88*282*.12)']
	part3_incorrect_attempt
					('0:04:20', u'(282-260)/sqrt(.88*282*.12)')
					('0:07:26', u'(260-(.88*282))/sqrt(.88*282*.12)')
					('0:07:32', u'(282-(.88*282))/sqrt(.88*282*.12)')
					('0:10:07', u'(260-(.88*282))/sqrt(.88*282*.12)')
					('0:11:53', u'(260-(.88*282))/[sqrt(.88*282*.12)/282]')
					('0:12:07', u'(282-(.88*282))/[sqrt(.88*282*.12)/260]')
					('0:12:14', u'(282-(.88*282))/[sqrt(.88*282*.12)/282]')
					('0:12:36', u'.015')
					('0:54:17', u'1-.96164')
					('0:55:09', u'(260-(.88*282))/sqrt(.88*282*.12)')
					('0:56:39', u'.88*282')
					('0:57:43', u'1-.98500')
					('0:59:31', u'.88^282')
					('0:59:44', u'.88^22')
					('1:01:47', u'.88^282')
	part3_correct_attempt
					['1:06:06', u'Q((260-(.88*282))/sqrt(.88*282*.12))']

97 Student ID:s2chaudh

	first_attempt
					2015-11-06 06:53:40
	part1_correct_attempt
					['0:00:00', u'188*.84']
	part2_correct_attempt
					['0:00:45', u'sqrt(188*.84*(1-.84))']
	part3_incorrect_attempt
					('0:02:18', u'((170-(188*.84))/sqrt(188*.84*(1-.84)))')
					('0:02:25', u'1/((170-(188*.84))/sqrt(188*.84*(1-.84)))')
					('0:03:37', u'((170-(188*.84))/sqrt(188*.84*(1-.84)))')
					('16:33:13', u'((170-(188*.84))/sqrt(188*.84*(1-.84)))')
	part3_correct_attempt
					['16:35:01', u'1-(1/2+1/2erf((((170-(188*.84))/sqrt(188*.84*(1-.84))) )/sqrt(2)))']

98 Student ID:jmiclat

	first_attempt
					2015-11-06 09:32:38
	part1_correct_attempt
					['0:00:00', u'.82*266']
	part2_correct_attempt
					['14:23:37', u'sqrt[(1-0.82)0.82*266]']
	part3_incorrect_attempt
					('14:24:55', u'1-Phi((266-218.12)/6.26591)')
					('14:25:39', u'1-Phi((266-240)/6.26591)')
	part3_correct_attempt
					['14:25:56', u'1-Phi((240-218.12)/6.26591)']

99 Student ID:yypan

	first_attempt
					2015-11-03 01:31:12
	part1_correct_attempt
					['0:00:00', u'390*0.85']
	part2_correct_attempt
					['0:18:36', u'sqrt((390*0.85)*(390*0.15)/390)']
	part3_incorrect_attempt
					('0:27:02', u'1-[C(21,21)*0.85^390*0.15*0]')
					('0:29:12', u'1-[1*0.85^390*0.15*0]')
					('0:30:43', u'1-[1*0.85^390*0.15^0]')
					('0:31:01', u'[1*0.85^390*0.15^0]')
					('0:32:07', u'1-[1*0.85^360*0.15^0]')
					('0:36:02', u'1-[C(390,360)*0.85^360*0.15^30]')
	part3_correct_attempt
					['2 days, 5:02:56', u'1-[0.5+0.5*erf(((360-390*0.85)/sqrt((390*0.85)*(390*0.15)/390))/sqrt(2))]']

100 Student ID:dcgriffi

	first_attempt
					2015-11-07 00:15:04
	part1_correct_attempt
					['0:00:00', u'268']
	part2_correct_attempt
					['0:00:00', u'sqrt(335*.8*.2)']
	part3_incorrect_attempt
					('0:01:25', u'.003')
					('0:09:02', u'.0015')
					('0:12:17', u'1/(sqrt(2*3.1415926535)*sqrt(335*.8*.2))*e^(-(32^2)/2(sqrt(335*.8*.2))^2)')
					('0:13:08', u'1/(sqrt(2*3.1415926535)*sqrt(335*.8*.2))*e^(-(32^2)/(2(sqrt(335*.8*.2))^2))')
					('0:14:47', u'1/(sqrt(2*3.1415926535)*sqrt(335*.8*.2))*e^(-(32^2))/(2(sqrt(335*.8*.2))^2)')
					('0:15:42', u'1/(sqrt(2*3.1415926535)*sqrt(335*.8*.2))*e^(-(32^2)/(2*335*.8*.2))')
					('0:16:23', u'.0027')
					('0:16:28', u'1/(sqrt(2*3.1415926535)*sqrt(335*.8*.2))*e^(-(32^2)/2(sqrt(335*.8*.2))^2)')
					('0:17:38', u'1/(sqrt(2*3.1415926535)*sqrt(335*.8*.2))*e^(-(32^2)/(2(335*.8*.2)))')
					('0:35:32', u'0.000657670233796037')
					('0:36:46', u'0.001101565')
					('0:42:15', u'.00131')
					('0:43:36', u'.00087')
					('0:43:48', u'.00094')
					('0:43:59', u'.00181')
					('0:44:05', u'.00131')
					('0:44:26', u'.00135')
					('0:44:33', u'.00126')
					('0:44:40', u'.00131')

101 Student ID:cfgutier

	first_attempt
					2015-11-06 20:32:01
	part1_correct_attempt
					['0:00:00', u'.83 * 234']
	part2_correct_attempt
					['0:00:33', u'((234 * (1 - .83) * .83)) ^ (1/2)']
	part3_incorrect_attempt
					('0:01:38', u'1 - Phi((234-.83*234)/((234 * (1 - .83) * .83)) ^ (1/2))')
	part3_correct_attempt
					['0:02:08', u'1 - Phi((210-.83*234)/((234 * (1 - .83) * .83)) ^ (1/2))']

102 Student ID:dkostins

	first_attempt
					2015-11-06 05:24:37
	part1_correct_attempt
					['0:00:00', u'.86 * 166']
	part2_correct_attempt
					['0:20:51', u'sqrt(166*.86*.14)']
	part3_incorrect_attempt
					('0:28:57', u'(166-.86 * 166)/sqrt(166*.86*.14)')
					('0:29:58', u'1-Phi((166-.86 * 166)/sqrt(166*.86*.14))')
					('0:30:22', u'2(1-Phi((166-.86 * 166)/sqrt(166*.86*.14)))')
					('0:36:04', u'1-(Phi((166-.24 * 166)/sqrt(166*.86*.14)))')
					('0:36:20', u'1-(Phi((165)/sqrt(166*.86*.14)))')
					('0:36:29', u'1-(Phi((164)/sqrt(166*.86*.14)))')
					('0:36:34', u'1-(Phi((163)/sqrt(166*.86*.14)))')
					('0:36:38', u'1-(Phi((162)/sqrt(166*.86*.14)))')
					('0:36:42', u'1-(Phi((161)/sqrt(166*.86*.14)))')
					('0:36:47', u'1-(Phi((160)/sqrt(166*.86*.14)))')
					('0:36:53', u'1-(Phi((159)/sqrt(166*.86*.14)))')
					('0:36:57', u'1-(Phi((158)/sqrt(166*.86*.14)))')
					('0:37:01', u'1-(Phi((157)/sqrt(166*.86*.14)))')
					('0:37:05', u'1-(Phi((156)/sqrt(166*.86*.14)))')
					('0:37:08', u'1-(Phi((155)/sqrt(166*.86*.14)))')
					('0:37:34', u'1-(Phi((154)/sqrt(166*.86*.14)))')
					('0:37:38', u'1-(Phi((153)/sqrt(166*.86*.14)))')
					('0:37:43', u'1-(Phi((152)/sqrt(166*.86*.14)))')
					('0:37:47', u'1-(Phi((151)/sqrt(166*.86*.14)))')
					('0:37:51', u'1-(Phi((150)/sqrt(166*.86*.14)))')
					('0:37:56', u'1-(Phi((149)/sqrt(166*.86*.14)))')
					('0:37:59', u'1-(Phi((148)/sqrt(166*.86*.14)))')
					('0:38:03', u'1-(Phi((147)/sqrt(166*.86*.14)))')
					('0:38:07', u'1-(Phi((146)/sqrt(166*.86*.14)))')
					('0:38:11', u'1-(Phi((145)/sqrt(166*.86*.14)))')
					('0:38:14', u'1-(Phi((144)/sqrt(166*.86*.14)))')
					('0:38:18', u'1-(Phi((143)/sqrt(166*.86*.14)))')
					('0:38:22', u'1-(Phi((142)/sqrt(166*.86*.14)))')
					('0:38:25', u'1-(Phi((141)/sqrt(166*.86*.14)))')
					('0:38:29', u'1-(Phi((140)/sqrt(166*.86*.14)))')
					('0:38:35', u'1-(Phi((139)/sqrt(166*.86*.14)))')
					('0:38:40', u'1-(Phi((138)/sqrt(166*.86*.14)))')
					('0:38:43', u'1-(Phi((137)/sqrt(166*.86*.14)))')
					('0:38:49', u'1-(Phi((136)/sqrt(166*.86*.14)))')
					('0:38:53', u'1-(Phi((135)/sqrt(166*.86*.14)))')
					('0:38:56', u'1-(Phi((134)/sqrt(166*.86*.14)))')
					('0:39:00', u'1-(Phi((133)/sqrt(166*.86*.14)))')
					('0:39:04', u'1-(Phi((132)/sqrt(166*.86*.14)))')
					('0:39:07', u'1-(Phi((131)/sqrt(166*.86*.14)))')
					('0:39:11', u'1-(Phi((130)/sqrt(166*.86*.14)))')
					('0:39:15', u'1-(Phi((129)/sqrt(166*.86*.14)))')
					('0:39:20', u'1-(Phi((128)/sqrt(166*.86*.14)))')
					('0:39:48', u'1-(Phi((127)/sqrt(166*.86*.14)))')
					('0:43:57', u'C(166,160)*.86^160*.14^(166-160)')
					('0:46:34', u'1-Phi((166-160)/sqrt(166*.86*.14))')
					('0:46:48', u'2(1-Phi((166-160)/sqrt(166*.86*.14)))')
					('0:48:27', u'2(1-Phi((166-.86*166)/sqrt(166*.86*.14)))')
					('0:48:35', u'(1-Phi((166-.86*166)/sqrt(166*.86*.14)))')
					('0:49:39', u'1-Q(((166-.86*166)/sqrt(166*.86*.14)))')
					('0:52:48', u'1-Phi(((166-.86*166)/sqrt(166*.86*.14)))')
					('1:09:03', u'(((166-.86*166)/sqrt(166*.86*.14)))')
					('1:09:54', u'(((166-.86*166)/sqrt(166*.86*.14)))')
					('1:15:50', u'(166-142.76)/4.47062')
					('1:16:11', u'Phi((166-142.76)/4.47062)')
					('1:16:20', u'1-Phi((166-142.76)/4.47062)')
					('1:16:34', u'Q((166-142.76)/4.47062)')
					('1:16:41', u'1-Q((166-142.76)/4.47062)')
					('1:16:47', u'Q((166-142.76)/4.47062)')
					('1:17:49', u'Q((166-.14*166)/4.47062)')
					('1:18:02', u'1-Q((166-.14*166)/4.47062)')
					('1:18:36', u'Q((166-.86*160)/4.47062)')
					('1:19:50', u'Q((166-.86*166)/4.47062)')
					('1:20:53', u'1-Phi((166-.86*166)/4.47062)')
					('1:21:07', u'1-(Phi((166-.86*166)/4.47062))^2')
					('1:21:59', u'1-(Phi(((166-.86*166)/4.47062))^2)')
					('1:24:05', u'((166-.86*166)/4.47062)^2')
					('1:26:20', u'((166-.86*166)/4.47062)')
					('1:26:36', u'sqrt(((166-.86*166)/4.47062))')
					('1:26:57', u'Phi(sqrt(((166-.86*166)/4.47062)))')
					('1:27:02', u'1-Phi(sqrt(((166-.86*166)/4.47062)))')
					('1:28:48', u'1-Phi(sqrt(((166-.86*166))/4.47062))')
					('1:29:20', u'sqrt(166-.86*166)')
					('1:29:38', u'sqrt(166-.86*166)/4.47062')
					('1:30:02', u'1-Phi(sqrt(166-.86*166)/4.47062)')
					('12:30:31', u'0.99')
					('12:30:40', u'0.97')
					('12:33:55', u'0.12')
					('12:39:03', u'Q(3)')
					('12:42:17', u'Q(3.32177)')
					('12:44:48', u'Phi(166-(.86 * 166) / sqrt(166*.86*.14))')
					('12:44:56', u'1 - Phi(166-(.86 * 166) / sqrt(166*.86*.14))')
					('12:45:14', u'3.321 * (1 - Phi(166-(.86 * 166) / sqrt(166*.86*.14)))')
					('12:45:27', u'3 * (1 - Phi(166-(.86 * 166) / sqrt(166*.86*.14)))')
					('12:48:21', u'1 - Phi(17 / sqrt(166*.86*.14))')
					('12:48:32', u'1 - Phi(18 / sqrt(166*.86*.14))')
					('12:49:05', u'Phi(166-(.86 * 166) / sqrt(166*.86*.14))')
					('12:49:14', u'1 - Phi(166-(.86 * 166) / sqrt(166*.86*.14))')
					('12:49:25', u'2 * (1 - Phi(166-(.86 * 166) / sqrt(166*.86*.14)))')
					('12:49:47', u'1 - Phi(166-(.86 * 166) / sqrt(166*.86*.14))')
					('12:53:17', u'C(5,2)')
					('14:10:42', u'1 - Phi(161 - (0.86 * 166) / sqrt(166 * 0.86 * 0.14))')
					('14:12:24', u'1 - (Phi(161 - (0.86 * 166)) / sqrt(166 * 0.86 * 0.14))')
					('14:12:39', u'1 - Phi((161 - (0.86 * 166)) / sqrt(166 * 0.86 * 0.14))')
					('14:13:12', u'1 - Phi((161 - (0.86 * 166)) / sqrt(161 * 0.86 * 0.14))')
					('14:13:33', u'1 - Phi((161 - (0.86 * 160)) / sqrt(166 * 0.86 * 0.14))')
					('14:57:00', u'1 - Phi((160 - (0.86 * 160)) / sqrt(166 * 0.86 * 0.14))')
	part3_correct_attempt
					['15:38:40', u'1 - Phi((160 - (0.86 * 166)) / sqrt(166 * 0.86 * 0.14))']

103 Student ID:twsalim

	first_attempt
					2015-11-06 03:44:10
	part1_correct_attempt
					['0:00:00', u'239.76']
	part2_correct_attempt
					['0:10:26', u'6.7494']
	part3_incorrect_attempt
					('0:10:26', u'Q(8.3563)')
					('0:11:49', u'Q(6.32566)')
					('0:11:55', u'Q(6.3256)')
	part3_correct_attempt
					['0:13:21', u'Q(2.99879)']

104 Student ID:s6deng

	first_attempt
					2015-11-05 07:56:44
	part1_correct_attempt
					['0:00:00', u'.86*172']
	part2_correct_attempt
					['0:01:01', u'sqrt(172*.86*.14)']
	part3_incorrect_attempt
					('0:07:08', u'0.3302')
					('0:08:32', u'0.43949357326')

105 Student ID:achinn

	first_attempt
					2015-11-03 22:08:56
	part1_correct_attempt
					['0:00:00', u'0.86*381']
	part2_correct_attempt
					['0:00:00', u'sqrt(0.86*381*0.14)']
	part3_incorrect_attempt
					('0:00:00', u'(350-(0.86*381))/(sqrt(0.86*381*0.14))')
					('0:00:24', u'0.0005')
					('0:01:49', u'0.0003')
					('0:38:21', u'0.03')
					('9:54:20', u'Q(351-(0.86*381))/(sqrt(0.86*381*0.14))')
	part3_correct_attempt
					['9:55:39', u'Q((350-(0.86*381))/(sqrt(0.86*381*0.14)))']

106 Student ID:aalhaida

	first_attempt
					2015-11-05 23:56:50
	part1_correct_attempt
					['0:00:00', u'.85*201']
	part3_incorrect_attempt
					('0:02:02', u'.25')

107 Student ID:jdeon

	first_attempt
					2015-11-04 23:41:21
	part1_correct_attempt
					['0:00:00', u'301']
	part2_correct_attempt
					['0:02:42', u'6.4915']
	part3_incorrect_attempt
					('0:07:54', u'Q((350-301)/(6.4915))')
					('0:08:10', u'Q((350-320)/(6.4915))')
					('0:08:28', u'Phi((350-301)/(6.4915))')
					('0:12:16', u'Phi((49-19)/(6.4915))')
					('0:12:22', u'Q((49-19)/(6.4915))')
					('0:12:34', u'Q((50-19)/(6.4915))')
					('0:12:47', u'Phi((50-19)/(6.4915))')
					('0:16:01', u'Phi((351-301)/(6.4915))')
					('0:16:18', u'Q((351-301)/(6.4915))')
					('0:20:45', u'Q((321-301)/(6.4915))')
					('0:21:09', u'Phi((321-301)/(6.4915))')
	part3_correct_attempt
					['0:21:50', u'Q((320-301)/(6.4915))']

108 Student ID:hah008

	first_attempt
					2015-11-06 23:17:33
	part1_correct_attempt
					['0:00:00', u'390 * 0.8']
	part2_correct_attempt
					['0:00:36', u'sqrt(312*(1-0.8))']
	part3_incorrect_attempt
					('0:47:18', u'0.00804601')
					('0:47:26', u'1-0.00804601')
					('0:47:40', u'0.00351161')
					('0:48:25', u'0.988442')
					('1:02:39', u'1-0.988442')
					('1:02:52', u'1-0.00351161')
					('1:03:04', u'1-0.00804601')
					('1:03:30', u'0.00351161')
					('1:03:38', u'0.00804601')
					('1:03:46', u'0.988442')
					('1:07:07', u'0.8^390')
					('1:18:38', u'Q(390-312)/(sqrt(312*(1-0.8)))')

109 Student ID:mcatozzi

	first_attempt
					2015-11-03 23:35:17
	part1_correct_attempt
					['0:00:00', u'.89*375']
	part2_correct_attempt
					['0:01:07', u'sqrt(375*(.89)*(.11))']
	part3_incorrect_attempt
					('0:02:42', u'15/375')
					('0:02:50', u'15/360')
					('0:04:21', u'15/(.89*375)')
					('0:05:54', u'(.89*375)/375')
					('0:05:58', u'(.89*375)/360')
					('0:07:12', u'1 -(.89*375)/360')
					('0:07:18', u'1 -(.89*375)/375')
	part3_correct_attempt
					['0:14:40', u'1 -Phi((360-333.75)/sqrt(375*(.89)*(.11)))']

110 Student ID:acs008

	first_attempt
					2015-11-05 21:59:52
	part1_correct_attempt
					['0:00:00', u'382*0.89']
	part2_correct_attempt
					['0:00:24', u'sqrt(382*0.89*0.11)']
	part3_incorrect_attempt
					('0:03:52', u'(382-339.98)/6.11547')
					('0:04:08', u'2*Q((382-339.98)/6.11547)')
					('0:04:18', u'2*Q((360-339.98)/6.11547)')
					('0:04:34', u'Q((382-339.98)/6.11547)')
					('0:11:19', u'1-0.52543690')
					('0:11:39', u'1-0.99986463')
					('0:13:20', u'(1-Q(6.11537))*(Q(6.11537))')
					('0:14:40', u'1-Q(6.87121)*2')
					('0:15:29', u'(360-339.98)/6.11537')
					('0:15:48', u'1-Q(3.27372)*2')
	part3_correct_attempt
					['0:32:38', u'Q((360-339.98)/6.11537)']

111 Student ID:hmshah

	first_attempt
					2015-11-05 09:54:46
	part1_correct_attempt
					['0:00:00', u'366*.87']
	part2_correct_attempt
					['0:00:47', u'sqrt(366*.87* .13)']
	part3_incorrect_attempt
					('0:22:32', u'0.000108134009137006')
					('0:24:14', u'(1-0.999891865990863)')

112 Student ID:lahawkin

	first_attempt
					2015-11-04 04:59:33
	part1_correct_attempt
					['0:00:00', u'(89/100)303']
	part2_correct_attempt
					['2 days, 0:07:02', u'((89/100)(303)(.11))^(1/2)']
	part3_incorrect_attempt
					('2 days, 0:07:56', u'.000023')
					('2 days, 0:22:24', u'1/(((89/100)(303)(.11))^(1/2))')

113 Student ID:aordookh

	first_attempt
					2015-11-06 06:52:05
	part1_correct_attempt
					['0:00:00', u'290-(.89*18)']
	part2_correct_attempt
					['0:17:08', u'(308*.89*.11)^(1/2)']
	part3_incorrect_attempt
					('0:17:50', u'(290-(290-(.89*18)))/(308*.89*.11)^(1/2)')
					('0:24:20', u'1-Phi(290)')
					('0:24:40', u'Q(290)')
					('0:26:26', u'Q((308*.89*.11)^(1/2))')
					('0:26:42', u'1-Phi((308*.89*.11)^(1/2))')
					('0:29:51', u'1-Phi((308-(308*.89))(308*.89*.11)^(1/2))')
					('0:30:14', u'1-Phi((308-(308*.89))/(308*.89*.11)^(1/2))')
					('0:37:01', u'Q(308-(308*.89)/(308*.89*.11)^(1/2))')
	part3_correct_attempt
					['0:41:19', u'Q((290-(308*.89))/(308*.89*.11)^(1/2))']

114 Student ID:yig015

	first_attempt
					2015-11-05 11:03:16
	part1_correct_attempt
					['0:00:00', u'217*0.87']
	part2_correct_attempt
					['0:04:55', u'4.954058942']
	part3_incorrect_attempt
					('1 day, 0:16:49', u'7.038063327')
					('1 day, 0:19:15', u'(217-0.87*210)/sqrt(0.87*0.13*210)')
					('1 day, 0:19:39', u'(217-0.87/210)/sqrt(0.87*0.13*210)')
					('1 day, 0:19:57', u'(217-0.87*210)/sqrt(0.87*0.13/210)')
					('1 day, 0:23:58', u'Q((217*0.87-210)/sqrt(0.87*0.13*210))')
					('1 day, 0:24:39', u'Q((217-0.87*210)/sqrt(0.87*0.13*210))')
	part3_correct_attempt
					['1 day, 0:35:41', u'Q((210-0.87*217)/sqrt(0.87*0.13*217))']

115 Student ID:vasharma

	first_attempt
					2015-11-05 22:56:17
	part1_correct_attempt
					['0:00:00', u'159*.80']
	part2_correct_attempt
					['0:00:23', u'sqrt(159*.8(1-.8))']
	part3_incorrect_attempt
					('0:04:15', u'6.3048')
	part3_correct_attempt
					['0:37:48', u'Q((150-159*.80)/sqrt(159*.8(1-.8)) )']

116 Student ID:hpc001

	first_attempt
					2015-11-01 01:21:31
	part1_correct_attempt
					['0:00:00', u'349*.85']
	part2_correct_attempt
					['0:04:53', u'sqrt(349*.85*.15)']
	part3_incorrect_attempt
					('0:06:18', u'(320-296.65)/6.67064')
					('0:07:54', u'0.00023')
					('0:08:39', u'1/85')
	part3_correct_attempt
					['5 days, 22:16:37', u'Q((320-296.65)/6.67064)']

117 Student ID:xweng

	first_attempt
					2015-11-06 01:16:42
	part1_correct_attempt
					['0:00:00', u'185*0.86']
	part2_correct_attempt
					['0:00:59', u'4.7195']
	part3_incorrect_attempt
					('0:02:21', u'0.0004664')
					('3:35:16', u'C(120,1)*(1/1200)^1*(1199/1200)^119')
					('3:37:06', u'1-0.00494923037219612')
					('3:37:11', u'0.00494923037219612')
					('3:37:21', u'0.00997656868661001')
					('3:37:25', u'0.009976568686610010.00502733831441404')
					('3:37:29', u'0.00502733831441404')
					('3:37:34', u'0.00997656868661001')
					('3:37:44', u'1-0.00502733831441404')
					('3:37:56', u'1-0.00494923037219612')
					('3:40:33', u'0.00502733831441404')
					('3:41:11', u'0.005')
					('4:27:27', u'(185-159.1)/4.7195')
					('4:29:15', u'(185-159.1)4.7195')
					('4:33:56', u'0.00503')
					('4:34:27', u'0.004949')
					('4:34:56', u'0.002666878')
					('4:37:18', u'1-0.86^185')
					('4:37:33', u'0.86^185')
					('4:38:55', u'0.000001')
					('4:39:08', u'0.00502733831441404')
					('4:39:13', u'1-0.00502733831441404')
					('4:40:52', u'1-0.99497266')
					('5:04:56', u'0.00502734')
					('5:05:13', u'4.7195/185*0.86')
					('5:05:24', u'4.7195/159.1')

118 Student ID:amquinte

	first_attempt
					2015-11-05 06:46:40
	part1_correct_attempt
					['0:00:00', u'218.4']
	part2_correct_attempt
					['0:04:05', u'6.61']
	part3_incorrect_attempt
					('0:05:46', u'2.013E-4')
					('1 day, 16:19:00', u'3.142E-4')
					('1 day, 16:19:47', u'2.013E-4')
					('1 day, 17:21:59', u'3.14237E-4')
					('1 day, 17:31:50', u'.99966')
					('1 day, 17:36:01', u'5.420E-4')
					('1 day, 17:38:04', u'4.834E-4')
					('1 day, 17:42:15', u'3.369E-4')

119 Student ID:c3chung

	first_attempt
					2015-11-06 22:52:08
	part1_correct_attempt
					['0:00:00', u'.81(281)']
	part2_correct_attempt
					['1:48:57', u'sqrt(281*.81*.19)']
	part3_incorrect_attempt
					('1:49:36', u'(250-227.61)/6.57616')
					('1:50:10', u'1-.9997')
					('1:50:32', u'0.0004')
					('1:50:35', u'0.0005')
					('1:50:37', u'0.0006')
					('1:50:41', u'0.0003')
					('1:50:43', u'0.0002')
					('1:50:46', u'0.0001')
					('1:50:50', u'0.0007')
					('1:50:52', u'0.0008')
					('1:50:54', u'0.0009')
					('1:50:58', u'0.001')
					('1:51:00', u'0.002')
					('1:53:04', u'(250-227.61)/6.57616')
					('1:53:23', u'1-0.9997')
					('1:53:40', u'1-0.99966')
					('1:53:50', u'1-0.99968')
					('1:54:57', u'(281-227.61)/6.57616')
					('1:56:32', u'(250-227.61)/6.57616')

120 Student ID:mtrafeca

	first_attempt
					2015-11-05 21:44:19
	part1_correct_attempt
					['0:00:00', u'223*.89']
	part2_correct_attempt
					['0:02:24', u'sqrt(.89*.11*223)']
	part3_incorrect_attempt
					('0:02:57', u'210/223')
					('0:03:12', u'1-(210/223)')

121 Student ID:kosung

	first_attempt
					2015-11-05 20:53:32
	part1_correct_attempt
					['0:00:00', u'368*0.89']
	part2_correct_attempt
					['0:01:06', u'(368*0.89*0.11)^(1/2)']
	part3_incorrect_attempt
					('0:25:28', u'7.9*e^-7')
					('0:26:48', u'5.2*e^-12')
					('0:28:59', u'Q((368-327.52)/6.0023)')
	part3_correct_attempt
					['4:47:12', u'Q((340-327.52)/6.0023)']

122 Student ID:j2phung

	first_attempt
					2015-11-05 18:52:28
	part1_correct_attempt
					['0:00:00', u'.86 * 330']
	part2_correct_attempt
					['0:44:21', u'(330*(1-.86)*(.86))^(1/2)']
	part3_incorrect_attempt
					('0:47:43', u'(330-(.86 * 330))/((330*(1-.86)*(.86))^(1/2))')
					('1:03:47', u'(330.5-(.86 * 330))/((330*(1-.86)*(.86))^(1/2))')
					('1:09:33', u'1-Phi((330.5-(.86 * 330))/((330*(1-.86)*(.86))^(1/2)))')
					('1:10:40', u'1-Phi((330-(.86 * 330))/((330*(1-.86)*(.86))^(1/2)))')
					('1:11:04', u'1-Phi((331-(.86 * 330))/((330*(1-.86)*(.86))^(1/2)))')
	part3_correct_attempt
					['1:14:08', u'1-Phi((300-(.86 * 330))/((330*(1-.86)*(.86))^(1/2)))']












