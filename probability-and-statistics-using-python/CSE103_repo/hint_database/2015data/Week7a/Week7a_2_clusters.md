#Problem 2:

      $a = Compute("0.05/sqrt(0.16/200)");
      $q = Compute("Q($a)");

      A noted psychic was tested for extrasensory perception. The psychic was presented
      with 200 cards face down and asked to determine if the card were one of five symbols.
      The psychic was correct in 50 cases. Let p represent the probability that the psychic
      correctly identifies the symbol on the card in a random trial. Assume the 200 trials
      can be treated as a simple random sample.

      Suppose you wished to see if there were evidence that the psychic is
      doing better than just guessing. To do this, you test the hypotheses [`H_0 : p = .20`]
      versus [`H_{alternative} : p > .20`].

      What is the z-score? [__________________________________________]{$a}

      What is the p-value for the test statistic? (You can use Q function in the answer) [_________]{$q}

      Can you reject at the .05 significance level? (answer "yes" or "no") [_______]{"yes"}

      Can you reject at the .01 significance level? (answer "yes" or "no") [_______]{"no"}



## Part 1

### (64) Mistake Group Wrong_Sign of size 64




### (34) Mistake Group ['R.0'] of size 34
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|0.05/[sqrt(0.16/200)]	|(50/200 - (.2))/sqrt(40 * 4/5)	|[('R.0', 0.05, u'0.05', u'50/200 - (.2)')]	|
|1	|0.05/[sqrt(0.16/200)]	|(.25-0.20) / sqrt((200*0.25)*(0.75))	|[('R.0', 0.05, u'0.05', u'.25-0.2')]	|
|2	|0.05/[sqrt(0.16/200)]	|(.25-0.20) / sqrt((200*0.20)*(0.80))	|[('R.0', 0.05, u'0.05', u'.25-0.2')]	|
|3	|0.05/[sqrt(0.16/200)]	|(.25-0.20) / sqrt( (200*0.20)*(1 - 0.20 ) )	|[('R.0', 0.05, u'0.05', u'.25-0.2')]	|
|4	|0.05/[sqrt(0.16/200)]	|(.25-0.20) / sqrt( (200*0.25)*(1 - 0.25 ) )	|[('R.0', 0.05, u'0.05', u'.25-0.2')]	|
|5	|0.05/[sqrt(0.16/200)]	|(0.25-0.2)/(200*0.2*0.8)^0.5	|[('R.0', 0.05, u'0.05', u'0.25-0.2')]	|
|6	|0.05/[sqrt(0.16/200)]	|(0.25-0.2)/(0.2*0.8)^0.5	|[('R.0', 0.05, u'0.05', u'0.25-0.2')]	|
|7	|0.05/[sqrt(0.16/200)]	|(0.25-0.2)/(0.25*0.75)^0.5	|[('R.0', 0.05, u'0.05', u'0.25-0.2')]	|
|8	|0.05/[sqrt(0.16/200)]	|(0.25-0.2)/(40/sqrt(200))	|[('R.0', 0.05, u'0.05', u'0.25-0.2')]	|
|9	|0.05/[sqrt(0.16/200)]	|(0.25-0.2)/(40)	|[('R.0', 0.05, u'0.05', u'0.25-0.2')]	|
|10	|0.05/[sqrt(0.16/200)]	|(0.25-0.2) / ( ( 0.2(1-0.2) ) /(sqrt(200) ) )	|[('R.0', 0.05, u'0.05', u'0.25-0.2')]	|
|11	|0.05/[sqrt(0.16/200)]	|(.05/sqrt(40))	|[('R.0', 0.05, u'0.05', u'.05/')]	|
|12	|0.05/[sqrt(0.16/200)]	|(0.25-0.2)/50	|[('R.0', 0.05, u'0.05', u'0.25-0.2')]	|
|13	|0.05/[sqrt(0.16/200)]	|((50/200)-.2)/((.2*(1-.2)/200))	|[('R.0', 0.05, u'0.05', u'(50/200)-.2)')]	|
|14	|0.05/[sqrt(0.16/200)]	|((50/200)-.2)/(200 * .2 * (1-.2))	|[('R.0', 0.05, u'0.05', u'(50/200)-.2)')]	|
|15	|0.05/[sqrt(0.16/200)]	|((50/200)-.2)/(200 * .2 * (1-.2)^2)	|[('R.0', 0.05, u'0.05', u'(50/200)-.2)')]	|
|16	|0.05/[sqrt(0.16/200)]	|((50/200)-.2)/(200 * .2 * (1-.2))^2	|[('R.0', 0.05, u'0.05', u'(50/200)-.2)')]	|
|17	|0.05/[sqrt(0.16/200)]	|((50/200)-.2)/sqrt(200 * .2 * (1-.2))	|[('R.0', 0.05, u'0.05', u'(50/200)-.2)')]	|
|18	|0.05/[sqrt(0.16/200)]	|((50/200)-.2)/sqrt(50 * .2 * (1-.2))	|[('R.0', 0.05, u'0.05', u'(50/200)-.2)')]	|
|19	|0.05/[sqrt(0.16/200)]	|((50/200)-.2)/sqrt((50/200) * .2 * (1-.2))	|[('R.0', 0.05, u'0.05', u'(50/200)-.2)')]	|
|20	|0.05/[sqrt(0.16/200)]	|((50/200)-.2)/sqrt((200) * .2 * (1-.2))	|[('R.0', 0.05, u'0.05', u'(50/200)-.2)')]	|
|21	|0.05/[sqrt(0.16/200)]	|(0.25 - 0.2)/(0.2(1 - 0.2))^0.5	|[('R.0', 0.05, u'0.05', u'0.25 - 0.2')]	|
|22	|0.05/[sqrt(0.16/200)]	|[(50/200) - 0.2]/[(0.2) * (1 - 0.2)]^0.5	|[('R.0', 0.05, u'0.05', u'(50/200) - 0.2')]	|
|23	|0.05/[sqrt(0.16/200)]	|((50/200)-(40/200))/sqrt(( ((50^2)+ (40^2) )/2))	|[('R.0', 0.05, u'0.05', u'(50/200)-(40/200)')]	|
|24	|0.05/[sqrt(0.16/200)]	|((50/200) - .20) / (.20(1 - .20)200)	|[('R.0', 0.05, u'0.05', u'(50/200) - .20')]	|
|25	|0.05/[sqrt(0.16/200)]	|.05/(200*.2*.8)	|[('R.0', 0.05, u'0.05', u'.05/')]	|
|26	|0.05/[sqrt(0.16/200)]	|.05/sqrt(200*.2*.8)	|[('R.0', 0.05, u'0.05', u'.05/')]	|
|27	|0.05/[sqrt(0.16/200)]	|((50/200)-(40/200))/((.2*.8)/200)	|[('R.0', 0.05, u'0.05', u'(50/200)-(40/200)')]	|
|28	|0.05/[sqrt(0.16/200)]	|((50/200)-(40/200))/((.25*.75)/200)	|[('R.0', 0.05, u'0.05', u'(50/200)-(40/200)')]	|
|29	|0.05/[sqrt(0.16/200)]	|((50/200)-(40/200))/((.25*.75)/200)^.5	|[('R.0', 0.05, u'0.05', u'(50/200)-(40/200)')]	|
|30	|0.05/[sqrt(0.16/200)]	|(.25 - .2)/((.2)(.8)/(200)^(1/2))	|[('R.0', 0.05, u'0.05', u'.25 - .2)')]	|
|31	|0.05/[sqrt(0.16/200)]	|(.25-.2)/sqrt(200)	|[('R.0', 0.05, u'0.05', u'.25-.2)')]	|
|32	|0.05/[sqrt(0.16/200)]	|(.25 -  .2) / sqrt( (.2 * .8 ) )	|[('R.0', 0.05, u'0.05', u'.25 -  .2)')]	|




### (29) Mistake Group Digits of size 29




### (12) Mistake Group ['R.1'] of size 12
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|0.05/[sqrt(0.16/200)]	|0.5/sqrt(0.16/200)	|[('R.1', 0.0282842712474619, u'sqrt(0.16/200)', u'sqrt(0.16/200)')]	|
|1	|0.05/[sqrt(0.16/200)]	|(50-40)/(sqrt(0.2 * ( 1 - 0.2 ) / 200 ))	|[('R.1', 0.0282842712474619, u'sqrt(0.16/200)', u'sqrt(0.2 * ( 1 - 0.2 ) / 200 )')]	|
|2	|0.05/[sqrt(0.16/200)]	|(50 - .2*200)/sqrt(.2*.8/200)	|[('R.1', 0.0282842712474619, u'sqrt(0.16/200)', u'sqrt(.2*.8/200)')]	|
|3	|0.05/[sqrt(0.16/200)]	|(50 - (40))/sqrt(.2*.8/200)	|[('R.1', 0.0282842712474619, u'sqrt(0.16/200)', u'sqrt(.2*.8/200)')]	|
|4	|0.05/[sqrt(0.16/200)]	|(50 - (200 * .2)) / (sqrt((.2*.8)/200))	|[('R.1', 0.0282842712474619, u'sqrt(0.16/200)', u'sqrt((.2*.8)/200)')]	|
|5	|0.05/[sqrt(0.16/200)]	|(50-40)/sqrt((.2*.8)/200)	|[('R.1', 0.0282842712474619, u'sqrt(0.16/200)', u'sqrt((.2*.8)/200)')]	|
|6	|0.05/[sqrt(0.16/200)]	|[50-200*0.2]/[sqrt([0.2*(1-0.2)]/200)]	|[('R.1', 0.0282842712474619, u'sqrt(0.16/200)', u'sqrt([0.2*(1-0.2)]/200)')]	|
|7	|0.05/[sqrt(0.16/200)]	|10/(((0.2*0.8)/200)^0.5)	|[('R.1', 0.0282842712474619, u'sqrt(0.16/200)', u'((0.2*0.8)/200)^0.5')]	|
|8	|0.05/[sqrt(0.16/200)]	|(0.25-.02)/sqrt(0.2(1-0.2)/200)	|[('R.1', 0.0282842712474619, u'sqrt(0.16/200)', u'sqrt(0.2(1-0.2)/200)')]	|
|9	|0.05/[sqrt(0.16/200)]	|10/sqrt((0.2)*(0.8)/200)	|[('R.1', 0.0282842712474619, u'sqrt(0.16/200)', u'sqrt((0.2)*(0.8)/200)')]	|
|10	|0.05/[sqrt(0.16/200)]	|0.5/(0.16/200)^(1/2)	|[('R.1', 0.0282842712474619, u'sqrt(0.16/200)', u'(0.16/200)^(1/2)')]	|




### (8) Mistake Group ['R.1.0.0'] of size 8
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|0.05/[sqrt(0.16/200)]	|(50-40)/sqrt((.2*.8)/40)	|[('R.1.0.0', 0.16, u'0.16', u'.2*.8)')]	|
|1	|0.05/[sqrt(0.16/200)]	|(50-40)/sqrt((.2*.8)/50)	|[('R.1.0.0', 0.16, u'0.16', u'.2*.8)')]	|
|2	|0.05/[sqrt(0.16/200)]	|(200-40)/sqrt((.2*.8)/50)	|[('R.1.0.0', 0.16, u'0.16', u'.2*.8)')]	|
|3	|0.05/[sqrt(0.16/200)]	|(200-50)/sqrt((.2*.8)/40)	|[('R.1.0.0', 0.16, u'0.16', u'.2*.8)')]	|
|4	|0.05/[sqrt(0.16/200)]	|(200-50)/sqrt(.2*.8*40)	|[('R.1.0.0', 0.16, u'0.16', u'.2*.8*')]	|
|5	|0.05/[sqrt(0.16/200)]	|(200-50)/sqrt(.2*.8*200)	|[('R.1.0.0', 0.16, u'0.16', u'.2*.8*')]	|
|6	|0.05/[sqrt(0.16/200)]	|(200-40)/sqrt(.2*.8*200)	|[('R.1.0.0', 0.16, u'0.16', u'.2*.8*')]	|
|7	|0.05/[sqrt(0.16/200)]	|(200-0.2*200)/(sqrt(0.2*(1-0.2)200))	|[('R.1.0.0', 0.16, u'0.16', u'0.2*(1-0.2)')]	|




### (3) Mistake Group ['R.1.0.1'] of size 3
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|0.05/[sqrt(0.16/200)]	|(.20/sqrt(.40/200))	|[('R.1.0.1', 200.0, u'200', u'200')]	|
|1	|0.05/[sqrt(0.16/200)]	|(.40/sqrt(.20/200))	|[('R.1.0.1', 200.0, u'200', u'200')]	|
|2	|0.05/[sqrt(0.16/200)]	|0.5/sqrt(0.20/200)	|[('R.1.0.1', 200.0, u'200', u'200')]	|




### (2) Mistake Group ['R.0', 'R.1.0.0'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|0.05/[sqrt(0.16/200)]	|(0.25-0.2) / ( sqrt( 0.2(1-0.2) ) / (200)  )	|[('R.0', 0.05, u'0.05', u'0.25-0.2'), ('R.1.0.0', 0.16, u'0.16', u'0.2(1-0.2)')]	|
|1	|0.05/[sqrt(0.16/200)]	|(.25-.2)/(sqrt(.2(1-.2))/200)	|[('R.0', 0.05, u'0.05', u'.25-.2)'), ('R.1.0.0', 0.16, u'0.16', u'.2(1-.2)')]	|




### (2) Mistake Group ['R.1.0'] of size 2
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|0.05/[sqrt(0.16/200)]	|(50 - (40))/(.2*.8/200)^2	|[('R.1.0', 0.0008, u'0.16/200', u'.2*.8/200')]	|
|1	|0.05/[sqrt(0.16/200)]	|0.5/(0.16/200)^2	|[('R.1.0', 0.0008, u'0.16/200', u'0.16/200')]	|




### (1) Mistake Group ['R.0', 'R.1.0.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|0.05/[sqrt(0.16/200)]	|0.05/sqrt(0.20/200)	|[('R.0', 0.05, u'0.05', u'0.05'), ('R.1.0.1', 200.0, u'200', u'200')]	|




### (101) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:v4zhang

	first_attempt
					2015-11-13 11:11:21
	part1_incorrect_attempt
					('0:00:00', u'(50-(200*.2))/.2')
	part1_correct_attempt
					['0:02:35', u'[(50/200)-.20]/[sqrt([.2*(1-.2)]/[200])]']

1 Student ID:kbielawi

	first_attempt
					2015-11-11 23:08:55
	part1_incorrect_attempt
					('0:00:00', u'.2/.5')
	part1_correct_attempt
					['0:04:05', u'(0.25-0.2)/(sqrt((.2*(1-.2))/200))']

2 Student ID:ssamudra

	first_attempt
					2015-11-13 22:10:59
	part1_incorrect_attempt
					('0:00:00', u'6.123')
	part1_correct_attempt
					['0:03:13', u'1.7677']

3 Student ID:jhc010

	first_attempt
					2015-11-12 07:39:35
	part1_incorrect_attempt
					('0:00:00', u'(50-40)/(200*0.2)(0.8)')
					('0:00:09', u'(50-40)/((200*0.2)(0.8))')
					('0:00:39', u'(50-40)/((200*0.2)(0.8))')
	part1_correct_attempt
					['1:25:28', u'(50-40)/(sqrt((200*0.2*0.8)))']

4 Student ID:mhale

	first_attempt
					2015-11-11 05:45:13
	part1_incorrect_attempt
					('0:00:00', u'200(0.2)')
					('0:03:57', u'10/3')
					('0:04:08', u'10/15')
	part1_correct_attempt
					['0:06:26', u'10 / [(200/5 * 0.8)^(1/2)]']

5 Student ID:rsmurlo

	first_attempt
					2015-11-10 17:13:26
	part1_incorrect_attempt
					('0:00:00', u'150/sqrt(48)')
					('0:00:46', u'150/sqrt(80)')
					('0:05:15', u'50/sqrt(48)')
					('0:05:25', u'50/sqrt(80)')
					('0:07:34', u'150/sqrt(24)')
					('0:07:50', u'50/sqrt(24)')
					('0:08:49', u'10/sqrt(24)')
					('0:09:19', u'30/sqrt(24)')
					('0:16:47', u'30/sqrt(40)')
					('0:17:10', u'10/sqrt(40)')
	part1_correct_attempt
					['0:37:33', u'10/sqrt(40*.8)']

6 Student ID:j5phung

	first_attempt
					2015-11-10 17:04:57
	part1_incorrect_attempt
					('0:00:00', u'10/sqrt(40)')
	part1_correct_attempt
					['0:04:26', u'10/sqrt(40*4/5)']

7 Student ID:c4du

	first_attempt
					2015-11-13 23:52:15
	part1_incorrect_attempt
					('0:00:00', u'50/200')

8 Student ID:haw081

	first_attempt
					2015-11-10 04:22:44
	part1_incorrect_attempt
					('0:00:00', u'8.4')
	part1_correct_attempt
					['0:10:21', u'(0.25-0.2)/(sqrt(0.2 * ( 1 - 0.2 ) / 200 ))']

9 Student ID:vqt004

	first_attempt
					2015-11-13 06:28:49
	part1_incorrect_attempt
					('0:00:00', u'((0.2*200)-5)/sqrt(200*0.2(1-0.2))')
	part1_correct_attempt
					['0:00:48', u'-((0.2*200)-50)/sqrt(200*0.2(1-0.2))']

10 Student ID:r9jiang

	first_attempt
					2015-11-11 05:03:45
	part1_incorrect_attempt
					('0:00:00', u'0.3125')
	part1_correct_attempt
					['0:01:32', u'1.7678']

11 Student ID:avasavad

	first_attempt
					2015-11-13 01:50:48
	part1_incorrect_attempt
					('0:00:00', u'16/[3*sqrt(2)]')
	part1_correct_attempt
					['15:48:01', u'(.25-.2)/sqrt[[.2*(1-.2)]/200]']

12 Student ID:btn023

	first_attempt
					2015-11-13 08:20:24
	part1_incorrect_attempt
					('0:00:00', u'(50 - 40)/(200)^(1/2)')
					('0:01:20', u'(50 - 40)/(200)')
					('0:00:00', u'(50 - 40)/((.2)(.8)/(200)^1/2)')
					('0:00:12', u'(50 - 40)/((.2)(.8)/(200)^(1/2))')
	part1_correct_attempt
					['0:05:55', u'(.25 - .2)/((.2)(.8)/(200))^(1/2)']

13 Student ID:dgunawan

	first_attempt
					2015-11-12 21:01:28
	part1_incorrect_attempt
					('0:00:00', u'[200-50]/0.2')
					('0:02:58', u'[200-50]/0.25')
					('0:00:00', u'.0793')
					('0:00:18', u'.0987')
	part1_correct_attempt
					['5:23:12', u'[0.25-0.2]/[(0.16/200)^(1/2)]']

14 Student ID:tcn013

	first_attempt
					2015-11-10 01:11:40
	part1_incorrect_attempt
					('0:00:00', u'Q(.2)')
	part1_correct_attempt
					['0:13:08', u'10/5.65685424949']

15 Student ID:tcuddy

	first_attempt
					2015-11-10 18:17:24
	part1_incorrect_attempt
					('0:00:00', u'(50-32)/(32**.5)')
	part1_correct_attempt
					['0:00:37', u'(50-40)/(32**.5)']

16 Student ID:abasu

	first_attempt
					2015-11-09 00:14:55
	part1_incorrect_attempt
					('0:00:00', u'63.2456')
	part1_correct_attempt
					['0:10:06', u'1.7678']

17 Student ID:anvan

	first_attempt
					2015-11-12 02:50:23
	part1_incorrect_attempt
					('0:00:00', u'.842')
					('0:00:00', u'sqrt(200(.2)(.8))')
	part1_correct_attempt
					['2:33:21', u'10 / sqrt(200(.2)(.8))']

18 Student ID:jguanzho

	first_attempt
					2015-11-12 02:09:14
	part1_incorrect_attempt
					('0:00:00', u'(50-200/5)/sqrt(0.2*0.8)')
					('0:02:59', u'(50-200*0.2)/sqrt(0.2*200)')
	part1_correct_attempt
					['0:03:45', u'(50-200*0.2)/sqrt(0.8*0.2*200)']

19 Student ID:flhernan

	first_attempt
					2015-11-11 22:28:49
	part1_incorrect_attempt
					('0:00:00', u'Q(2)')
					('0:01:06', u'200 - 50/(sqrt(50 * 200))')
					('0:11:00', u'200*.2 - 50/(sqrt(200*.2*(1-.2)))')
	part1_correct_attempt
					['0:12:01', u'abs((200*.2 - 50))/(sqrt(200*.2*(1-.2)))']

20 Student ID:c1wei

	first_attempt
					2015-11-11 22:55:29
	part1_incorrect_attempt
					('0:00:00', u'1/4')
	part1_correct_attempt
					['0:01:36', u'10/sqrt(32)']

21 Student ID:arc013

	first_attempt
					2015-11-14 00:35:55
	part1_incorrect_attempt
					('0:00:00', u'Q((200*0.2-50)/sqrt(32))')
					('0:01:43', u'(50-32)/sqrt(32)')
	part1_correct_attempt
					['0:06:45', u'1.7678']

22 Student ID:mitopete

	first_attempt
					2015-11-08 19:06:03
	part1_incorrect_attempt
					('0:00:00', u'3.4')
					('0:18:35', u'0.8')
					('0:18:42', u'0.8/2')
	part1_correct_attempt
					['4 days, 7:20:28', u'(0.25-0.20)/(((0.20(1-0.20))/(200))^(1/2))']

23 Student ID:yos017

	first_attempt
					2015-11-13 09:31:13
	part1_incorrect_attempt
					('0:00:00', u'[(200 * 0.25) - (200 * 0.20)]/[200 * 0.25 * (1-0.25)]^(1/2)')
	part1_correct_attempt
					['0:10:42', u'[(0.25) - (0.20)]/[[0.20 * (1-0.20)]/200]^(1/2)']

24 Student ID:small

	first_attempt
					2015-11-13 20:15:12
	part1_incorrect_attempt
					('0:00:00', u'sqrt(2)/10')
	part1_correct_attempt
					['0:27:34', u'1.7678']

25 Student ID:m8woo

	first_attempt
					2015-11-11 22:56:11
	part1_incorrect_attempt
					('0:00:00', u'[50-0.2*200]/[.2 * .8 * 200]')
	part1_correct_attempt
					['0:00:49', u'[50-0.2*200]/sqrt([.2 * .8 * 200])']

26 Student ID:akg009

	first_attempt
					2015-11-13 20:47:52
	part1_incorrect_attempt
					('0:00:00', u'Q(.2)')
					('0:03:23', u'28.288')
	part1_correct_attempt
					['0:05:34', u'1.768']

27 Student ID:jag028

	first_attempt
					2015-11-11 05:09:10
	part1_incorrect_attempt
					('0:00:00', u'.20')
	part1_correct_attempt
					['0:03:15', u'[0.25-0.2]/[sqrt[0.2(1-0.2)/200]]']

28 Student ID:quwong

	first_attempt
					2015-11-07 22:40:58
	part1_incorrect_attempt
					('0:00:00', u'(200 - 50) / (200 * 0.2 * 0.8)^0.5')
	part1_correct_attempt
					['0:06:37', u'(50/200 - 0.2)/(0.2*(1-0.2)/200)^0.5']

29 Student ID:lrlai

	first_attempt
					2015-11-12 07:01:32
	part1_incorrect_attempt
					('0:00:00', u'0.25')
	part1_correct_attempt
					['1 day, 15:10:50', u'(50-40)/sqrt(32)']

30 Student ID:asetters

	first_attempt
					2015-11-08 02:29:59
	part1_incorrect_attempt
					('0:00:00', u'(50 - .2*100)/(.2*.8*200)')
					('0:00:27', u'(50 - .2*100)/(1/(.2*.8*200))')
					('0:00:00', u'(50 - .2*100)/(sqrt(20*.8))')
					('0:00:13', u'(50 - .2*100)/(20*.8)^2')
					('0:01:33', u'(50 - .2*100)/sqrt(20*.8)')
					('0:04:34', u'(50 - (.2*200))/sqrt(200*2*.8)')
					('0:07:16', u'(50 - (40))/.2*.8/200')
					('0:07:27', u'(50 - (40))/(.2*.8/200)')
					('0:00:00', u'(50 - (40))/sqrt(.2*.8)')
	part1_correct_attempt
					['2 days, 20:38:48', u'(50 - (40))/sqrt(200*.2*.8)']

31 Student ID:atorr

	first_attempt
					2015-11-11 22:43:17
	part1_incorrect_attempt
					('0:00:00', u'(200 - 50)/0.20')
	part1_correct_attempt
					['0:10:56', u'[(50/200) - 0.2]/[(0.2) * (1 - 0.2)/200]^0.5']

32 Student ID:skarimik

	first_attempt
					2015-11-13 04:02:26
	part1_incorrect_attempt
					('0:00:00', u'(40-40)/(32)^(1/2)')
					('0:00:32', u'(40-8)/(32)^(1/2)')
	part1_correct_attempt
					['0:13:32', u'(50/200-.2)/(.2*.8/200)^(1/2)']

33 Student ID:anislam

	first_attempt
					2015-11-13 08:22:28
	part1_incorrect_attempt
					('0:00:00', u'.05/(.16/200)^1/2')
	part1_correct_attempt
					['0:00:09', u'.05/(.16/200)^(1/2)']

34 Student ID:krau

	first_attempt
					2015-11-12 01:49:38
	part1_incorrect_attempt
					('0:00:00', u'50*10/40')
					('0:02:05', u'50*sqrt(20)/40')
	part1_correct_attempt
					['0:14:51', u'(50-40)/sqrt(32)']

35 Student ID:psable

	first_attempt
					2015-11-12 21:24:20
	part1_incorrect_attempt
					('0:00:00', u'.5')
					('0:00:00', u'1.41421')
	part1_correct_attempt
					['0:15:06', u'1.767767']

36 Student ID:hak014

	first_attempt
					2015-11-11 22:19:23
	part1_incorrect_attempt
					('0:00:00', u'50/200')
	part1_correct_attempt
					['4:10:09', u'(.25-.2)/sqrt( (.2)*(1-.2)/200 )']

37 Student ID:jhw015

	first_attempt
					2015-11-10 20:13:56
	part1_incorrect_attempt
					('0:00:00', u'(50-40)/sqrt(40)')
					('0:03:37', u'0.9429')
					('0:04:04', u'0.0571')
	part1_correct_attempt
					['0:05:44', u'1.7678']

38 Student ID:t1tran

	first_attempt
					2015-11-11 04:48:03
	part1_incorrect_attempt
					('0:00:00', u'(50-40)/(sqrt(200*.2))')
	part1_correct_attempt
					['0:00:15', u'(50-40)/(sqrt(200*.2(1-.2)))']

39 Student ID:z3meng

	first_attempt
					2015-11-13 20:35:51
	part1_incorrect_attempt
					('0:00:00', u'10/(32)^1/2')
	part1_correct_attempt
					['0:00:12', u'10/(32)^0.5']

40 Student ID:akalathi

	first_attempt
					2015-11-12 06:06:52
	part1_incorrect_attempt
					('0:00:00', u'(50-40)*sqrt(200*.2*.2)')
					('0:00:12', u'(50-40)*sqrt(200*.2*.8)')
	part1_correct_attempt
					['0:02:17', u'(50-40)/sqrt(200*.2*.8)']

41 Student ID:edescobe

	first_attempt
					2015-11-08 02:41:52
	part1_incorrect_attempt
					('0:00:00', u'(50/200-.2)/(.2*.8/200)^1/2')
	part1_correct_attempt
					['0:00:23', u'(50/200-.2)/(.2*.8/200)^(1/2)']

42 Student ID:bakang

	first_attempt
					2015-11-12 18:19:31
	part1_incorrect_attempt
					('0:00:00', u'(50-40)/(sqrt(0.2*0.8))')
	part1_correct_attempt
					['0:04:06', u'(50-40)/(sqrt(200*0.2*0.8))']

43 Student ID:ggaddi

	first_attempt
					2015-11-10 18:01:10
	part1_incorrect_attempt
					('0:00:00', u'(50-40)/(sqrt(40))')
	part1_correct_attempt
					['0:01:58', u'(50-40)/(sqrt(200*0.2*(1-0.2)))']

44 Student ID:jtfrankl

	first_attempt
					2015-11-11 18:55:31
	part1_incorrect_attempt
					('0:00:00', u'10/(50**.5)')
					('0:00:00', u'10/(5**.5)')
	part1_correct_attempt
					['0:06:07', u'10/sqrt(40*.8)']

45 Student ID:yjshin

	first_attempt
					2015-11-13 16:18:04
	part1_incorrect_attempt
					('0:00:00', u'1.25')
					('0:05:12', u'17.6776695297')
	part1_correct_attempt
					['0:06:20', u'(.25-.2)/sqrt((.2*.8)/(200))']

46 Student ID:bkoli

	first_attempt
					2015-11-12 21:27:11
	part1_incorrect_attempt
					('0:00:00', u'0.0385')
	part1_correct_attempt
					['0:26:52', u'((50/200)-0.20)/sqrt((0.20(1-0.20))/200)']

47 Student ID:xil109

	first_attempt
					2015-11-07 21:57:39
	part1_incorrect_attempt
					('0:00:00', u'0.2')
	part1_correct_attempt
					['0:05:19', u'(50/200-0.2)/sqrt(0.2*(1-0.2)/200)']

48 Student ID:dac064

	first_attempt
					2015-11-12 21:18:08
	part1_incorrect_attempt
					('0:00:00', u'((200*(1/5))(1-1/5))^(.5)')
	part1_correct_attempt
					['0:05:03', u'(50 - 200/5)/(((200*(1/5))(1-1/5))^(.5))']

49 Student ID:zhz159

	first_attempt
					2015-11-13 21:06:03
	part1_incorrect_attempt
					('0:00:00', u'0.883883476')
	part1_correct_attempt
					['0:07:56', u'1.76776695']

50 Student ID:jyc018

	first_attempt
					2015-11-09 19:06:50
	part1_incorrect_attempt
					('0:00:00', u'.2')
	part1_correct_attempt
					['0:03:48', u'1.77']

51 Student ID:lywong

	first_attempt
					2015-11-11 23:44:46
	part1_incorrect_attempt
					('0:00:00', u'(50-40)')
					('0:01:07', u'(50-40)/(90^(1/2))')
					('0:01:17', u'(50-40)/(45^(1/2))')
					('0:02:30', u'(50-40)/sqrt((  ((50^2)+ (40^2) )/2))')
					('0:00:00', u'(50-40)/sqrt(( ((50^2)+ (40^2) )/2))')
	part1_correct_attempt
					['23:46:34', u'(50-40)/sqrt( 40(1-(1/5)) )']

52 Student ID:hkhodada

	first_attempt
					2015-11-10 00:25:57
	part1_incorrect_attempt
					('0:00:00', u'160/sqrt(32)')
	part1_correct_attempt
					['0:04:22', u'10/sqrt(32)']

53 Student ID:glcohen

	first_attempt
					2015-11-12 16:49:45
	part1_incorrect_attempt
					('0:00:00', u'.2')
					('0:00:07', u'.8')
					('0:02:40', u'.6')
					('0:03:06', u'.1')
					('0:03:33', u'.2')
					('0:04:02', u'.05')
	part1_correct_attempt
					['0:07:17', u'(.25-.20)/sqrt((.2(1-.2))/200)']

54 Student ID:achava

	first_attempt
					2015-11-09 19:03:07
	part1_incorrect_attempt
					('0:00:00', u'0.2-0.25/40')
					('0:01:58', u'(50-40) / (50/sqrt(200))')
	part1_correct_attempt
					['0:06:46', u'(0.25-0.2) / sqrt ( 0.16/200)']

55 Student ID:sachadal

	first_attempt
					2015-11-12 03:56:48
	part1_incorrect_attempt
					('0:00:00', u'8/sqrt(32)')
					('0:01:28', u'(50-40)/(sqrt((40*0.2)(1-0.2)))')
	part1_correct_attempt
					['0:01:42', u'(50-40)/(sqrt((200*0.2)(1-0.2)))']

56 Student ID:jcj006

	first_attempt
					2015-11-11 03:14:56
	part1_incorrect_attempt
					('0:00:00', u'10/(200*.2*.8)^2')
	part1_correct_attempt
					['0:01:42', u'10/sqrt(200*.2*.8)']

57 Student ID:n2patil

	first_attempt
					2015-11-09 08:16:02
	part1_incorrect_attempt
					('0:00:00', u'.0385')
					('0:03:34', u'1.96')
					('0:04:19', u'2.326')
					('0:05:29', u'2.31')
					('0:00:00', u'8.696')
					('0:07:19', u'1.463')
					('0:22:55', u'1.7')
					('0:24:22', u'.07')
	part1_correct_attempt
					['2 days, 18:26:43', u'1.7678']

58 Student ID:ksmurlo

	first_attempt
					2015-11-10 17:48:00
	part1_incorrect_attempt
					('0:00:00', u'(50-40)/sqrt(1000*.2*.8)')
	part1_correct_attempt
					['0:00:31', u'(50-40)/sqrt(200*.2*.8)']

59 Student ID:jblynch

	first_attempt
					2015-11-11 21:18:59
	part1_incorrect_attempt
					('0:00:00', u'.2')
	part1_correct_attempt
					['0:06:38', u'(50 - ((1/5)*200))/sqrt(((1/5)*200) - ((1/5)^2*200))']

60 Student ID:ganajera

	first_attempt
					2015-11-11 22:14:28
	part1_incorrect_attempt
					('0:00:00', u'0.052579672')
					('0:03:00', u'0.041399332')
	part1_correct_attempt
					['1:49:35', u'(5*sqrt(2))/(4)']

61 Student ID:nnh002

	first_attempt
					2015-11-12 18:32:14
	part1_incorrect_attempt
					('0:00:00', u'0.2')
					('0:11:48', u'10/sqrt(40)')
					('0:17:02', u'18/sqrt(32)')
	part1_correct_attempt
					['4:33:32', u'(50-40)/sqrt(200*.2*.8)']

62 Student ID:akhmelni

	first_attempt
					2015-11-13 21:01:25
	part1_incorrect_attempt
					('0:00:00', u'(10)/(40^(1/2))')
					('0:00:00', u'(50 - 40)/(40^(1/2))')
					('0:00:36', u'(50 - 40)/(40)')
					('0:10:43', u'(50 - 40)/(50)')
					('0:10:53', u'(50 - 40)/(50^(1/2))')
					('0:11:00', u'(50 - 40)/(40^(1/2))')
					('0:13:12', u'(50 - 40)/(10^(1/2))')
	part1_correct_attempt
					['0:29:47', u'(50 - 40)/(32^(1/2))']

63 Student ID:q3wen

	first_attempt
					2015-11-13 06:32:48
	part1_incorrect_attempt
					('0:00:00', u'1.632993162')
	part1_correct_attempt
					['0:01:33', u'1.767766953']

64 Student ID:yeh013

	first_attempt
					2015-11-13 07:12:57
	part1_incorrect_attempt
					('0:00:00', u'160/32')
					('0:00:09', u'10/32')
					('0:01:43', u'160/(32^(1/2))')
	part1_correct_attempt
					['0:01:53', u'10/(32^(1/2))']

65 Student ID:eaherman

	first_attempt
					2015-11-13 00:38:00
	part1_incorrect_attempt
					('0:00:00', u'(200-40)/(.5)')
					('0:00:00', u'(200-40)/(sqrt((200)(.2)(.8)))')
	part1_correct_attempt
					['4:34:10', u'(50-40)/(sqrt((200)(.2)(.8)))']

66 Student ID:volim

	first_attempt
					2015-11-12 16:59:50
	part1_incorrect_attempt
					('0:00:00', u'50/200')
					('0:00:16', u'(1/5)*200')
					('0:00:26', u'(1/5)')
					('0:00:36', u'.2')
					('0:00:00', u'(50-40)/(200)')
	part1_correct_attempt
					['6:20:21', u'(.25-.2)/(((.2*.8)/200)^(1/2))']

67 Student ID:cagatep

	first_attempt
					2015-11-12 21:41:50
	part1_incorrect_attempt
					('0:00:00', u'.5/(200*.2*.8)')
	part1_correct_attempt
					['0:01:44', u'10/sqrt(200*.2*.8)']

68 Student ID:hmnaing

	first_attempt
					2015-11-11 18:57:05
	part1_incorrect_attempt
					('0:00:00', u'(200-(1*5))/((.2*(1-.2)/200))')
					('0:00:13', u'(200-(.2))/((.2*(1-.2)/200))')
					('0:00:00', u'(50-(.2))/((.2*(1-.2)/200))')
	part1_correct_attempt
					['9:59:19', u'((50-(200*.2))/sqrt(200 * .2 * (1-.2)))']

69 Student ID:tjke

	first_attempt
					2015-11-12 04:09:43
	part1_incorrect_attempt
					('0:00:00', u'200*0.2')
					('0:07:17', u'[50-200*0.2]/[sqrt([0.2*(1-0.2)]/200)*sqrt(200)]')
	part1_correct_attempt
					['1 day, 19:16:48', u'[50/200-0.2]/[sqrt([0.2*(1-0.2)]/200)]']

70 Student ID:any027

	first_attempt
					2015-11-08 20:06:35
	part1_incorrect_attempt
					('0:00:00', u'(.25-0.20) / sqrt(200*0.25)*(0.75)')
					('0:06:52', u'(0.5-0.20) / sqrt( (200*0.5)*(1 - 0.5 ) )')
					('0:06:59', u'(0.5-0.25) / sqrt( (200*0.5)*(1 - 0.5 ) )')
					('0:12:01', u'(50-20) / sqrt( (200*0.5)*(1 - 0.5 ) )')
					('0:12:16', u'(50-50) / sqrt( (200*0.5)*(1 - 0.5 ) )')
					('0:14:04', u'(50-32) / sqrt( (200*0.2)*(1 - 0.5 ) )')
					('0:20:35', u'(50-32) / sqrt(32)')
	part1_correct_attempt
					['0:23:03', u'(.25-0.20) / sqrt( (0.20(1-0.20))/200 )']

71 Student ID:galu

	first_attempt
					2015-11-13 09:54:42
	part1_incorrect_attempt
					('0:00:00', u'.05')
					('0:00:35', u'.01')
	part1_correct_attempt
					['0:09:10', u'1.76777']

72 Student ID:t2shin

	first_attempt
					2015-11-10 22:08:11
	part1_incorrect_attempt
					('0:00:00', u'150/.2')
					('0:00:00', u'150/(200*.2*.8)')
					('0:00:28', u'150/sqrt(200*.2*.8)')
	part1_correct_attempt
					['0:11:33', u'((50/200)-0.2)/sqrt(0.2*0.8/200)']

73 Student ID:fichoi

	first_attempt
					2015-11-10 22:31:52
	part1_incorrect_attempt
					('0:00:00', u'(50-40)/80')
					('0:01:51', u'(200-40)/80')
					('0:17:06', u'(50-40)/80')
					('0:00:00', u'(50-40)/sqrt(40)')
	part1_correct_attempt
					['0:35:07', u'(50/200-0.2)/sqrt(0.2(1-0.2)/200)']

74 Student ID:ewbrenna

	first_attempt
					2015-11-13 09:18:32
	part1_incorrect_attempt
					('0:00:00', u'(50-40)/sqrt(200)')
					('0:04:14', u'(50-40)/1')
					('0:09:07', u'(50-40)/sqrt(10)')
					('0:09:51', u'(50-40)/sqrt(40)')
	part1_correct_attempt
					['0:14:43', u'-(40-50)/sqrt(40*(1-.2))']

75 Student ID:spw006

	first_attempt
					2015-11-09 09:34:57
	part1_incorrect_attempt
					('0:00:00', u'.25')
	part1_correct_attempt
					['0:01:23', u'0.05/sqrt(0.16/200)']

76 Student ID:masaro

	first_attempt
					2015-11-10 16:06:36
	part1_incorrect_attempt
					('0:00:00', u'10/sqrt(8)')
	part1_correct_attempt
					['0:07:52', u'10/sqrt(32)']

77 Student ID:rwthomps

	first_attempt
					2015-11-13 16:13:52
	part1_incorrect_attempt
					('0:00:00', u'(200 * (50/200) - 50) / (sqrt((200 * (50/200)) - (1 - (50/200))))')
					('0:03:49', u'(200 * (1/4) - 50) / (sqrt((200 * .2) * (1 - (1/4))))')
	part1_correct_attempt
					['0:13:43', u'((50/200) - .2)/(sqrt((.2(1 - .2))/200))']

78 Student ID:s1powers

	first_attempt
					2015-11-13 03:04:14
	part1_incorrect_attempt
					('0:00:00', u'0.5590169944')
	part1_correct_attempt
					['0:02:28', u'(0.25-0.2)/sqrt((0.2)(1-0.2)/200)']

79 Student ID:e9brown

	first_attempt
					2015-11-12 07:13:14
	part1_incorrect_attempt
					('0:00:00', u'.2')
					('0:05:56', u'200 * .20')
					('0:10:24', u'200 * .2')
					('0:11:32', u'200*.2/ ((40(.8))^.5)')
	part1_correct_attempt
					['0:13:49', u'10/ ((40(.8))^.5)']

80 Student ID:vsosnovs

	first_attempt
					2015-11-11 05:19:50
	part1_incorrect_attempt
					('0:00:00', u'(50/200)-.20')
	part1_correct_attempt
					['2:08:23', u'((50/200)-.20)/(sqrt(.2(1-.2)/200))']

81 Student ID:b1green

	first_attempt
					2015-11-13 18:40:55
	part1_incorrect_attempt
					('0:00:00', u'sqrt(32)')
	part1_correct_attempt
					['0:10:18', u'(1/4-1/5)/(sqrt[[1/5(1-1/5)]/200])']

82 Student ID:dcgriffi

	first_attempt
					2015-11-13 21:37:47
	part1_incorrect_attempt
					('0:00:00', u'5/(4*sqrt(2))')
					('0:00:00', u'10/(4*sqrt(0.2*0.8*200))')
	part1_correct_attempt
					['0:07:50', u'10/(sqrt(0.2*0.8*200))']

83 Student ID:cfgutier

	first_attempt
					2015-11-13 08:17:58
	part1_incorrect_attempt
					('0:00:00', u'28.2843')
					('0:00:00', u'(50-40)/(32^(2/2))')
	part1_correct_attempt
					['13:20:39', u'(50-40)/(32^(1/2))']

84 Student ID:dkostins

	first_attempt
					2015-11-10 02:46:18
	part1_incorrect_attempt
					('0:00:00', u'sqrt(200*(1-.20) *.8)')
					('0:04:03', u'40/sqrt(200*(1-.20) *.8)')
					('0:04:25', u'(200-40)/sqrt(200*(1-.20) *.8)')
					('0:04:49', u'(50-40)/sqrt(200*(1-.20) *.8)')
	part1_correct_attempt
					['0:05:18', u'(50-40)/sqrt(200*(1-.20) *.2)']

85 Student ID:pnquach

	first_attempt
					2015-11-12 22:04:48
	part1_incorrect_attempt
					('0:00:00', u'8/sqrt(2)')
					('0:01:24', u'2/sqrt(2)')
	part1_correct_attempt
					['0:02:25', u'10/sqrt(32)']

86 Student ID:jap009

	first_attempt
					2015-11-12 17:38:12
	part1_incorrect_attempt
					('0:00:00', u'.125')
	part1_correct_attempt
					['0:03:53', u'1.767766953']

87 Student ID:msaguiar

	first_attempt
					2015-11-13 04:08:56
	part1_incorrect_attempt
					('0:00:00', u'50/200')
	part1_correct_attempt
					['0:03:35', u'0.05/((.16/200)^(1/2))']

88 Student ID:b1yao

	first_attempt
					2015-11-07 23:05:30
	part1_incorrect_attempt
					('0:00:00', u'2*sqrt(6)/3')
	part1_correct_attempt
					['0:06:26', u'(0.25-0.2)/(sqrt(0.2*0.8)/sqrt(200))']

89 Student ID:acs008

	first_attempt
					2015-11-10 22:06:13
	part1_incorrect_attempt
					('0:00:00', u'0.25')
					('0:01:35', u'0.1')
					('0:01:39', u'0.01')
					('0:01:48', u'0.001')
					('0:00:00', u'750.0')
					('0:00:00', u'(200-50)/sqrt(200*1/5*4/5)')
					('0:01:41', u'(200-50)/sqrt(200*1/4*3/4)')
	part1_correct_attempt
					['0:14:34', u'((50/200)-0.2)/sqrt(0.2(1-0.2)/200)']

90 Student ID:dpereira

	first_attempt
					2015-11-08 03:16:05
	part1_incorrect_attempt
					('0:00:00', u'(50 - 40) / (.2 * .8 * 200)')
	part1_correct_attempt
					['0:00:11', u'(50 - 40) / sqrt(.2 * .8 * 200)']

91 Student ID:dtea

	first_attempt
					2015-11-13 23:40:21
	part1_incorrect_attempt
					('0:00:00', u'Q(.2)')
					('0:00:45', u'Q(.2)')
					('0:00:49', u'Q(.2)')
					('0:03:27', u'(50-40)/sqrt(50)')
					('0:05:29', u'(50-40)/sqrt(50-40)')
	part1_correct_attempt
					['0:17:43', u'(50-40)/sqrt(.2(1-.2)200)']

92 Student ID:lahawkin

	first_attempt
					2015-11-12 00:45:36
	part1_incorrect_attempt
					('0:00:00', u'150/((10*((6)^(1/2))/4))')
					('0:04:09', u'150/((10*((6)^(1/2))/4)^(1/2))')
					('0:06:02', u'150/((10*((8)^(1/2))/5)^(1/2))')
					('0:00:00', u'.25-.2/((10*((8)^(1/2))/5)^(1/2))')
	part1_correct_attempt
					['2:42:17', u'(.25-.2)/(((.2*.8)/200)^(1/2))']

93 Student ID:edcole

	first_attempt
					2015-11-12 01:42:14
	part1_incorrect_attempt
					('0:00:00', u'.5')
					('0:00:00', u'1.58')
					('0:01:00', u'(50-40)/sqrt(40)')
	part1_correct_attempt
					['18:56:23', u'(50-40)/sqrt(200*.2*.8)']

94 Student ID:z2tan

	first_attempt
					2015-11-09 00:56:20
	part1_incorrect_attempt
					('0:00:00', u'(0.25-0.2)')
	part1_correct_attempt
					['0:06:04', u'(50-40)/(200*0.2*0.8)^0.5']

95 Student ID:aordookh

	first_attempt
					2015-11-13 15:58:54
	part1_incorrect_attempt
					('0:00:00', u'0.5/(0.16/200)^1/2')
	part1_correct_attempt
					['0:00:24', u'0.05/(0.16/200)^(1/2)']

96 Student ID:kquong

	first_attempt
					2015-11-07 20:06:10
	part1_incorrect_attempt
					('0:00:00', u'20 - (200/5)/sqrt(5/6 * 200/5)')
	part1_correct_attempt
					['0:12:53', u'(50/200 - (.2))/sqrt(.2(.8)/200)']

97 Student ID:ajvanega

	first_attempt
					2015-11-13 22:58:03
	part1_incorrect_attempt
					('0:00:00', u'1/2')
					('0:02:40', u'.579')
					('0:03:00', u'.5793')
					('0:06:55', u'.0793')
					('0:00:00', u'(50-(200/5))/(200(1/5)(1-(1/5)))')
	part1_correct_attempt
					['0:52:19', u'(50-(200/5))/sqrt((200(1/5)(1-(1/5))))']

98 Student ID:zig006

	first_attempt
					2015-11-12 08:03:53
	part1_incorrect_attempt
					('0:00:00', u'10/((((0.2*0.8)/200)^0.5)/(200)^0.5)')
					('0:00:12', u'10/((((0.2*0.8)/200)^0.5)*(200)^0.5)')
	part1_correct_attempt
					['0:02:33', u'1.76776']

99 Student ID:mtrafeca

	first_attempt
					2015-11-10 01:39:47
	part1_incorrect_attempt
					('0:00:00', u'.2')
	part1_correct_attempt
					['4:55:50', u'(.05/sqrt(.16/200))']

100 Student ID:j2phung

	first_attempt
					2015-11-12 01:49:29
	part1_incorrect_attempt
					('0:00:00', u'50-40/((32)^(1/2))')
	part1_correct_attempt
					['0:02:20', u'(50-40)/((32)^(1/2))']












## Part 2

### (10) Mistake Group Digits of size 10




### (3) Mistake Group Wrong_Sign of size 3




### (1) Mistake Group ['R.0'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|Q(1.76777)	|1.76777-.2	|[('R.0', 1.76777, u'1.76777', u'1.76777')]	|




### (73) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:galu

	first_attempt
					2015-11-13 10:03:52
	part2_incorrect_attempt
					('-1 day, 23:50:50', u'.05')
					('-1 day, 23:51:25', u'.01')
	part2_correct_attempt
					['0:00:00', u'Q(1.76777)']

1 Student ID:apokhare

	first_attempt
					2015-11-09 20:01:30
	part2_incorrect_attempt
					('-1 day, 23:59:24', u'Q(0.5/sqrt(0.16/200))')
	part2_correct_attempt
					['0:00:00', u'Q(0.05/sqrt(0.16/200))']

2 Student ID:lpettit

	first_attempt
					2015-11-12 17:37:39
	part2_incorrect_attempt
					('0:00:00', u'1 - Q(10/(200*0.2*0.8)^0.5)')
	part2_correct_attempt
					['0:13:12', u'Q(10/(200*0.2*0.8)^0.5)']

3 Student ID:jag028

	first_attempt
					2015-11-11 05:12:25
	part2_incorrect_attempt
					('0:01:37', u'0.039')
					('0:03:04', u'0.039')
	part2_correct_attempt
					['1 day, 16:55:50', u'Q([0.25-0.2]/[sqrt[0.2(1-0.2)/200]])']

4 Student ID:h4tu

	first_attempt
					2015-11-12 22:53:13
	part2_incorrect_attempt
					('0:00:00', u'0.039')
					('0:01:13', u'Q(0.2)')
					('0:01:18', u'Q(0.25)')
					('0:02:23', u'1- Phi(0.2)')
					('0:02:28', u'1- Phi(0.25)')
	part2_correct_attempt
					['0:08:29', u'Q(1.7678)']

5 Student ID:quwong

	first_attempt
					2015-11-07 22:47:35
	part2_incorrect_attempt
					('0:00:00', u'0.039')
	part2_correct_attempt
					['0:01:41', u'0.038547']

6 Student ID:hkhodada

	first_attempt
					2015-11-10 00:30:19
	part2_incorrect_attempt
					('-1 day, 1:44:41', u'0.8')
	part2_correct_attempt
					['0:00:36', u'Q(10/sqrt(32))']

7 Student ID:lrlai

	first_attempt
					2015-11-13 22:12:22
	part2_incorrect_attempt
					('0:00:19', u'Q(50-40)/sqrt(32)')
					('0:00:33', u'Q(50-40/sqrt(32))')
	part2_correct_attempt
					['0:00:41', u'Q((50-40)/sqrt(32))']

8 Student ID:srl006

	first_attempt
					2015-11-12 22:22:34
	part2_incorrect_attempt
					('0:02:00', u'.039')
					('0:02:20', u'0.039')
					('0:05:18', u'.2322')
					('0:05:28', u'.7322')
					('0:06:47', u'0.0771')
					('0:07:02', u'0.1542')
					('0:09:08', u'0.0104')
	part2_correct_attempt
					['0:10:34', u'.0385']

9 Student ID:jjchung

	first_attempt
					2015-11-10 03:23:14
	part2_incorrect_attempt
					('0:01:29', u'.039')
					('0:02:28', u'.039')
					('0:02:51', u'.05')
					('0:02:57', u'.2')
	part2_correct_attempt
					['7:50:07', u'Q(0.05/sqrt(0.16/200))']

10 Student ID:alakamsa

	first_attempt
					2015-11-12 17:20:17
	part2_incorrect_attempt
					('-1 day, 23:59:30', u'Q((40 - 50)/sqrt(40*.8))')
	part2_correct_attempt
					['0:00:00', u'Q((50 - 40)/sqrt(40*.8))']

11 Student ID:ewbrenna

	first_attempt
					2015-11-13 09:33:15
	part2_incorrect_attempt
					('-1 day, 22:43:11', u'.2')
					('-1 day, 23:44:21', u'.025')
					('-1 day, 23:52:43', u'Q(.2)')
	part2_correct_attempt
					['0:00:21', u'Q(1.76777)']

12 Student ID:atorr

	first_attempt
					2015-11-11 22:54:13
	part2_incorrect_attempt
					('-1 day, 23:58:44', u'1 - [(0.25 - 0.2)/(0.2(1 - 0.2))^0.5]')
					('0:02:21', u'1.7678')
					('0:02:37', u'0.039')
	part2_correct_attempt
					['0:04:15', u'Q([(50/200) - 0.2]/[(0.2) * (1 - 0.2)/200]^0.5)']

13 Student ID:spw006

	first_attempt
					2015-11-09 09:36:20
	part2_incorrect_attempt
					('-1 day, 23:58:37', u'.039')
	part2_correct_attempt
					['0:00:13', u'1-Phi(0.05/sqrt(0.16/200))']

14 Student ID:jjm019

	first_attempt
					2015-11-11 03:16:48
	part2_incorrect_attempt
					('0:00:55', u'0.039')
	part2_correct_attempt
					['21:56:47', u'Q(1.7678)']

15 Student ID:thk002

	first_attempt
					2015-11-10 09:27:49
	part2_incorrect_attempt
					('0:00:00', u'.039')
					('0:00:40', u'1.7678')
					('0:00:45', u'.2')
					('0:12:20', u'.039*2')
	part2_correct_attempt
					['0:12:33', u'Q(1.7678)']

16 Student ID:tjke

	first_attempt
					2015-11-13 23:26:31
	part2_incorrect_attempt
					('-2 days, 4:43:12', u'Q(200*0.2)')
					('-2 days, 4:50:29', u'0.2')
	part2_correct_attempt
					['0:00:39', u'Q([50/200-0.2]/[sqrt([0.2*(1-0.2)]/200)])']

17 Student ID:dcrume

	first_attempt
					2015-11-12 01:06:48
	part2_incorrect_attempt
					('0:02:58', u'.0392')
					('0:05:14', u'1.96')
					('0:07:40', u'1.98')
					('0:12:59', u'0.9687')
					('0:14:46', u'.0784')
	part2_correct_attempt
					['0:15:11', u'Q(1.76777)']

18 Student ID:edescobe

	first_attempt
					2015-11-08 02:42:15
	part2_incorrect_attempt
					('-1 day, 23:59:37', u'Q((50/200-.2)/(.2*.8/200)^1/2)')
	part2_correct_attempt
					['0:00:00', u'Q((50/200-.2)/(.2*.8/200)^(1/2))']

19 Student ID:nhn018

	first_attempt
					2015-11-13 03:11:09
	part2_incorrect_attempt
					('0:00:00', u'.039')
	part2_correct_attempt
					['0:01:25', u'Q(1.7678)']

20 Student ID:j5phung

	first_attempt
					2015-11-10 17:09:23
	part2_incorrect_attempt
					('-1 day, 23:55:34', u'Q(10/sqrt(40))')
	part2_correct_attempt
					['0:00:00', u'Q(10/sqrt(40*4/5))']

21 Student ID:p4kumar

	first_attempt
					2015-11-14 00:32:20
	part2_incorrect_attempt
					('0:00:44', u' 0.039')

22 Student ID:haw081

	first_attempt
					2015-11-10 04:33:05
	part2_incorrect_attempt
					('0:00:14', u'Q(0.25-0.2)/(sqrt(0.2 * ( 1 - 0.2 ) / 200 ))')
	part2_correct_attempt
					['0:00:25', u'Q((0.25-0.2)/(sqrt(0.2 * ( 1 - 0.2 ) / 200 )))']

23 Student ID:vqt004

	first_attempt
					2015-11-13 06:29:37
	part2_incorrect_attempt
					('-1 day, 23:59:12', u'Q(((0.2*200)-5)/sqrt(200*0.2(1-0.2)))')
	part2_correct_attempt
					['0:00:16', u'Q(-((0.2*200)-50)/sqrt(200*0.2(1-0.2)))']

24 Student ID:dcgriffi

	first_attempt
					2015-11-13 21:45:37
	part2_incorrect_attempt
					('-1 day, 23:52:10', u'0.04935333238')
					('-1 day, 23:59:33', u'Q(10/(4*sqrt(0.2*0.8*200)))')
	part2_correct_attempt
					['0:00:00', u'Q(10/(sqrt(0.2*0.8*200)))']

25 Student ID:cfgutier

	first_attempt
					2015-11-13 21:38:37
	part2_incorrect_attempt
					('-1 day, 10:56:52', u'Q(200)')
					('-1 day, 10:56:58', u'Q(150)')
					('-1 day, 10:57:03', u'Q(.2)')
					('-1 day, 10:57:11', u'Q(40)')
					('0:00:27', u'(Q(50-40)/(32^(1/2)))')
	part2_correct_attempt
					['0:00:37', u'Q((50-40)/(32^(1/2)))']

26 Student ID:mnrahman

	first_attempt
					2015-11-12 22:02:38
	part2_incorrect_attempt
					('-1 day, 23:56:38', u'.20')
					('-1 day, 23:57:08', u'.25')
					('-1 day, 23:57:18', u'0.05')
					('-1 day, 23:57:44', u'0.039')
					('-1 day, 23:58:02', u'0.20')
					('0:00:26', u'0.039')
					('0:02:11', u'Q(0.1/sqrt(0.1*0.9/40))')
	part2_correct_attempt
					['0:02:42', u'Q(1.76777)']

27 Student ID:r9jiang

	first_attempt
					2015-11-11 05:05:17
	part2_incorrect_attempt
					('-1 day, 23:58:28', u'Q(0.3125)')
	part2_correct_attempt
					['0:00:00', u'Q(1.7678)']

28 Student ID:seleon

	first_attempt
					2015-11-12 08:38:36
	part2_incorrect_attempt
					('0:00:28', u'.039')
					('0:34:44', u'1.76')
					('0:36:22', u'.020')
					('0:36:33', u'.39')
					('0:36:38', u'.039')
					('7:57:10', u'Q(1.76)')
	part2_correct_attempt
					['7:57:22', u'Q(1.7678)']

29 Student ID:avasavad

	first_attempt
					2015-11-13 17:38:49
	part2_incorrect_attempt
					('0:01:23', u'Q(1.21)')
					('0:01:58', u'0.07841')
					('0:02:13', u'0.07673')
					('0:03:22', u'0.9599')
					('0:03:44', u'0.9608')
					('0:04:07', u'0.9616')
	part2_correct_attempt
					['0:04:46', u'1 - 0.9616']

30 Student ID:k3tan

	first_attempt
					2015-11-12 19:44:45
	part2_incorrect_attempt
					('0:11:29', u'0.392')
					('0:11:40', u'0.0392')
					('0:11:54', u'0.039')
	part2_correct_attempt
					['0:13:23', u'0.0384']

31 Student ID:s6deng

	first_attempt
					2015-11-11 22:15:39
	part2_incorrect_attempt
					('-1 day, 23:59:52', u'0.039')
					('0:01:30', u'.961')
					('0:01:36', u'.39')
					('0:01:40', u'.039')
					('0:02:25', u'0.0771')
					('0:02:41', u'0.038')
					('0:02:49', u'0.030')
					('0:02:55', u'0.031')
					('0:02:59', u'0.032')
					('0:03:02', u'0.033')
	part2_correct_attempt
					['0:04:23', u'0.038547']

32 Student ID:habuamar

	first_attempt
					2015-11-12 05:56:06
	part2_incorrect_attempt
					('0:00:00', u'1-Q((50-200*.2)/(sqrt(200*0.2*0.8)))')
	part2_correct_attempt
					['0:00:13', u'Q((50-200*.2)/(sqrt(200*0.2*0.8)))']

33 Student ID:jap009

	first_attempt
					2015-11-12 17:42:05
	part2_incorrect_attempt
					('0:00:31', u'Q(1.776953)')
					('0:00:35', u'1-Q(1.776953)')
					('0:02:07', u'.2')
					('0:02:29', u'Q(1.776953)')
					('0:03:26', u'2*Q(1.776953)')
	part2_correct_attempt
					['0:03:45', u'Q(1.767766953)']

34 Student ID:dis003

	first_attempt
					2015-11-13 21:54:38
	part2_incorrect_attempt
					('-1 day, 23:59:12', u'Q(0.5/sqrt(0.16/200))')
					('-1 day, 23:59:27', u'Q(0.5/sqrt(0.20/200))')
					('-1 day, 23:59:48', u'Q(0.05/sqrt(0.20/200))')
	part2_correct_attempt
					['0:00:00', u'Q(0.05/sqrt(0.16/200))']

35 Student ID:ppanourg

	first_attempt
					2015-11-12 02:28:36
	part2_incorrect_attempt
					('0:32:40', u'.9616')
	part2_correct_attempt
					['0:32:57', u'1 -.9616']

36 Student ID:msaguiar

	first_attempt
					2015-11-13 04:12:31
	part2_incorrect_attempt
					('-1 day, 23:56:25', u'50/200')
					('0:00:00', u'0.039')
					('0:04:30', u'0.0390')
					('0:04:36', u'0.0391')
					('0:04:45', u'0.0392')
					('0:04:51', u'0.0393')
					('0:04:57', u'0.0394')
					('0:05:08', u'0.0395')
					('0:05:14', u'0.0396')
					('0:05:19', u'0.0397')
					('0:05:25', u'0.0398')
					('0:05:31', u'0.0399')
	part2_correct_attempt
					['0:06:05', u'0.0385']

37 Student ID:asrana

	first_attempt
					2015-11-12 20:23:42
	part2_incorrect_attempt
					('0:00:23', u'0.039')
					('0:01:26', u'0.04')
	part2_correct_attempt
					['0:03:22', u'0.0385']

38 Student ID:hachrist

	first_attempt
					2015-11-08 23:34:02
	part2_incorrect_attempt
					('0:00:00', u'0.039')
					('0:00:45', u'0.20')
					('0:00:50', u'0.25')
					('0:00:58', u'1.76777')
					('0:01:59', u'1-Q(1.76777)')
	part2_correct_attempt
					['0:02:07', u'Q(1.76777)']

39 Student ID:muy002

	first_attempt
					2015-11-13 09:27:04
	part2_incorrect_attempt
					('0:00:32', u'0.039')
	part2_correct_attempt
					['0:18:14', u'Q(1.7678)']

40 Student ID:t1tran

	first_attempt
					2015-11-11 04:48:18
	part2_incorrect_attempt
					('-1 day, 23:59:06', u'Q((200*.2-50)/(sqrt(200*.2(1-.2))))')
	part2_correct_attempt
					['0:00:51', u'Q((50-40)/(sqrt(200*.2(1-.2))))']

41 Student ID:ganajera

	first_attempt
					2015-11-12 00:04:03
	part2_incorrect_attempt
					('-1 day, 22:10:25', u'Q(0.052579672)')
					('-1 day, 22:13:25', u'Q(0.052579672)0.041399332')
	part2_correct_attempt
					['0:00:00', u'Q((5*sqrt(2))/(4))']

42 Student ID:tstevens

	first_attempt
					2015-11-12 19:51:17
	part2_incorrect_attempt
					('0:00:00', u'.16/200')
	part2_correct_attempt
					['0:00:45', u'Q(.05/sqrt(.16/200))']

43 Student ID:flhernan

	first_attempt
					2015-11-11 22:40:50
	part2_incorrect_attempt
					('-1 day, 23:49:55', u'Q(.2)')
	part2_correct_attempt
					['0:00:17', u'Q(1.76777)']

44 Student ID:dlgoldbe

	first_attempt
					2015-11-13 07:02:10
	part2_incorrect_attempt
					('0:00:15', u'0.2')
	part2_correct_attempt
					['0:01:21', u'Q(((50/200)-(0.2))/(sqrt(((0.2)*(1-0.2))/(200))))']

45 Student ID:l8ngo

	first_attempt
					2015-11-09 18:00:00
	part2_incorrect_attempt
					('0:00:00', u'0.039')
	part2_correct_attempt
					['0:00:51', u'Q[0.05/sqrt[0.16/200]]']

46 Student ID:ajabasa

	first_attempt
					2015-11-13 21:17:12
	part2_incorrect_attempt
					('0:04:47', u'Q(.2)')
					('0:06:47', u'1-Q(.2)')
					('0:06:55', u'2*Q(.2)')
	part2_correct_attempt
					['0:10:44', u'Q((50-40)/((.2*.8*200)^.5))']

47 Student ID:dando

	first_attempt
					2015-11-11 09:42:51
	part2_incorrect_attempt
					('-1 day, 23:58:40', u'Q(-10/sqrt(32))')
	part2_correct_attempt
					['0:00:00', u'Q(10/sqrt(32))']

48 Student ID:eaherman

	first_attempt
					2015-11-13 05:12:10
	part2_incorrect_attempt
					('14:50:12', u'.2')
					('15:10:35', u'.2608')
					('16:19:11', u'.15')
					('16:22:17', u'.025')
					('16:22:23', u'.0015')
					('16:22:32', u'.0003')
					('16:33:12', u'Q(1)')
					('16:33:18', u'Q(2)')
					('16:33:23', u'Q(3)')
					('16:33:28', u'Q(4)')
					('16:33:35', u'Q(.2)')
					('16:33:44', u'Q(50)')
					('16:33:54', u'Q(1)')
	part2_correct_attempt
					['16:34:30', u'Q(1.7677)']

49 Student ID:q3wen

	first_attempt
					2015-11-13 06:34:21
	part2_incorrect_attempt
					('-1 day, 23:58:27', u'Q(1.632993162)')
	part2_correct_attempt
					['0:00:00', u'Q(1.767766953)']

50 Student ID:anvan

	first_attempt
					2015-11-12 05:23:44
	part2_incorrect_attempt
					('-1 day, 21:26:39', u'.674')
	part2_correct_attempt
					['0:01:21', u'Q(10 / sqrt(200(.2)(.8)))']

51 Student ID:achava

	first_attempt
					2015-11-09 19:09:53
	part2_incorrect_attempt
					('0:03:11', u'0.039')
					('0:04:11', u'0.039')
					('0:04:45', u'0.04')
					('0:07:51', u'0.039')
	part2_correct_attempt
					['0:10:32', u'Q(1.7677)']

52 Student ID:acs008

	first_attempt
					2015-11-10 22:20:47
	part2_incorrect_attempt
					('0:00:36', u'0.039')
	part2_correct_attempt
					['0:00:53', u'Q(1.76777)']

53 Student ID:ssamudra

	first_attempt
					2015-11-13 22:14:12
	part2_incorrect_attempt
					('0:00:13', u'0.077')
					('0:00:31', u'0.077099')
	part2_correct_attempt
					['0:00:55', u'0.0385']

54 Student ID:dtea

	first_attempt
					2015-11-13 23:58:04
	part2_incorrect_attempt
					('-1 day, 23:55:14', u'Q(.25)')
	part2_correct_attempt
					['0:00:19', u'Q(1.76777)']

55 Student ID:tdurrer

	first_attempt
					2015-11-13 07:38:38
	part2_incorrect_attempt
					('0:00:00', u'.04')
					('0:00:45', u'1-Q(1.767766953)')
	part2_correct_attempt
					['0:00:52', u'Q(1.767766953)']

56 Student ID:c1wei

	first_attempt
					2015-11-11 22:57:05
	part2_incorrect_attempt
					('-1 day, 23:58:24', u'Q(1/4)')
					('-1 day, 23:59:09', u'Q(.2)')
	part2_correct_attempt
					['0:00:24', u'Q(1.76777)']

57 Student ID:edcole

	first_attempt
					2015-11-12 20:38:37
	part2_incorrect_attempt
					('-1 day, 5:02:56', u'Q(8)')
					('-1 day, 5:03:37', u'Q(.5)')
					('-1 day, 5:26:24', u'Q(1.58)')
	part2_correct_attempt
					['0:00:11', u'Q((50-40)/sqrt(200*.2*.8))']

58 Student ID:ahh002

	first_attempt
					2015-11-12 04:25:14
	part2_incorrect_attempt
					('-1 day, 23:56:08', u'Q(((50/200) - .20) / (.20(1 - .20)200))')
	part2_correct_attempt
					['0:00:00', u'Q((50 - .20(200)) / sqrt(.20(1 - .20)200))']

59 Student ID:ralhadda

	first_attempt
					2015-11-07 21:55:52
	part2_incorrect_attempt
					('0:00:00', u'0.039')
					('0:00:14', u'0.25')
					('0:00:41', u'0.039')
	part2_correct_attempt
					['0:03:21', u'0.0385']

60 Student ID:yjshin

	first_attempt
					2015-11-13 16:24:24
	part2_incorrect_attempt
					('1:37:32', u'.039')
					('1:43:25', u'.077')
	part2_correct_attempt
					['1:46:25', u'0.038556']

61 Student ID:yhhan

	first_attempt
					2015-11-13 04:41:21
	part2_incorrect_attempt
					('0:00:16', u'.2')
	part2_correct_attempt
					['0:04:03', u'1-.9616']

62 Student ID:c3chung

	first_attempt
					2015-11-13 23:08:12
	part2_incorrect_attempt
					('0:00:31', u'0.039')
	part2_correct_attempt
					['0:01:14', u'Q(1.7678)']

63 Student ID:rohan

	first_attempt
					2015-11-13 20:28:57
	part2_incorrect_attempt
					('-1 day, 23:49:07', u'.2')
					('-1 day, 23:56:39', u'.25')
					('0:01:16', u'(10*.2)/sqrt(32)')
	part2_correct_attempt
					['0:02:44', u'Q(10/sqrt(32))']

64 Student ID:dac064

	first_attempt
					2015-11-12 21:23:11
	part2_incorrect_attempt
					('0:00:00', u'.2')
					('0:00:56', u'1/5')
	part2_correct_attempt
					['0:09:45', u'Q((50 - 200/5)/(((200*(1/5))(1-1/5))^(.5)))']

65 Student ID:zhz159

	first_attempt
					2015-11-13 21:13:59
	part2_incorrect_attempt
					('-1 day, 23:52:04', u'Q(0.883883476)')
	part2_correct_attempt
					['0:00:00', u'Q(1.76776695)']

66 Student ID:jguanzho

	first_attempt
					2015-11-12 02:12:59
	part2_incorrect_attempt
					('-1 day, 23:56:15', u'Q((50-200/5)/sqrt(0.2*0.8))')
					('-1 day, 23:59:14', u'Q((50-200*0.2)/sqrt(0.2*200))')
	part2_correct_attempt
					['0:00:13', u'Q((50-200*0.2)/sqrt(0.8*0.2*200))']

67 Student ID:small

	first_attempt
					2015-11-13 20:42:46
	part2_incorrect_attempt
					('0:08:56', u'0.039')
					('0:09:43', u'Q(0.3)')
					('0:10:20', u'Q(0.31)')
					('0:10:37', u'Q(0.29)')
					('0:10:43', u'Q(0.299)')
					('0:10:56', u'Q(0.2999999)')
					('0:11:06', u'Q(0.33)')
					('0:11:16', u'Q(0.28)')
					('0:11:26', u'Q(0.26)')
					('0:12:26', u'Q(0.279)')
					('0:13:02', u'Q(1.8)')
					('0:13:10', u'Q(1.89)')
					('0:13:19', u'Q(1.79)')
					('0:13:34', u'Q(1.6)')
					('0:13:44', u'Q(1.799999)')
	part2_correct_attempt
					['0:31:30', u'Q(1.7678)']

68 Student ID:m8woo

	first_attempt
					2015-11-11 22:57:00
	part2_incorrect_attempt
					('-1 day, 23:59:11', u'Q([50-0.2*200]/[.2 * .8 * 200])')
	part2_correct_attempt
					['0:00:00', u'Q([50-0.2*200]/sqrt([.2 * .8 * 200]))']

69 Student ID:akg009

	first_attempt
					2015-11-13 20:53:26
	part2_incorrect_attempt
					('-1 day, 23:58:32', u'0.03')
					('-1 day, 23:58:37', u'0.02')
					('-1 day, 23:58:43', u'0.04')
	part2_correct_attempt
					['0:00:12', u'Q(1.768)']

70 Student ID:mjethani

	first_attempt
					2015-11-13 23:51:14
	part2_incorrect_attempt
					('-1 day, 23:57:37', u'sqrt((1/5)(200)(1-(1/5)))')
	part2_correct_attempt
					['0:00:15', u'Q((50-(200/5))/sqrt(200*(1/5)(1-1/5)))']

71 Student ID:pnquach

	first_attempt
					2015-11-12 22:07:13
	part2_incorrect_attempt
					('-1 day, 23:57:35', u'Q(8/sqrt(2))')
					('-1 day, 23:58:59', u'Q(2/sqrt(2))')
	part2_correct_attempt
					['0:00:00', u'Q(10/sqrt(32))']

72 Student ID:jhp077

	first_attempt
					2015-11-13 07:46:40
	part2_incorrect_attempt
					('0:01:01', u'1-Q((0.25-0.2) /((0.2)(1-0.2)/200)^(1/2))')
	part2_correct_attempt
					['0:01:06', u'Q((0.25-0.2) /((0.2)(1-0.2)/200)^(1/2))']












