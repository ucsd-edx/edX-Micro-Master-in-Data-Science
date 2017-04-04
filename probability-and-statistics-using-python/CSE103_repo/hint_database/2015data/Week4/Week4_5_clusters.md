#Problem 5

    $p_men = random(6,8,1);
    $p_women = random(3,5,1);
    $p_male_given_colorblind = $p_men/($p_men+$p_women);


    Suppose that there are equal numbers of men and women in the world, and that [$p_men]\% of men
    are colorblind whereas only [$p_women]\% of women are colorblind. A person is chosen at random and found
    to be colorblind. What is the probability that the person is male? [_______________]{$p_men/($p_men+$p_women)}

    Reverse the condition:

    [``
    \begin{align*}
    \textbf{Pr}(\text{male} \ | \ \text{colorblind}) & = \frac{\textbf{Pr}(\text{male},\text{colorblind})}{\textbf{Pr}(\text{colorblind})} \\
    & = \frac{\textbf{Pr}(\text{colorblind} \ | \ \text{male}) \textbf{Pr}(\text{male})}{\textbf{Pr}(\text{colorblind})} \\
    \end{align*}
    ``]

    Law of total probability + Bayes rule:

    [``
    \begin{align*}
    \textbf{Pr}(\text{colorblind}) & = \textbf{Pr}(\text{male},\text{colorblind}) +  \textbf{Pr}(\text{female},\text{colorblind}) \\
    & = \textbf{Pr}(\text{colorblind} \ | \ \text{male}) \textbf{Pr}(\text{male}) + \textbf{Pr}(\text{colorblind} \ | \ \text{female}) \textbf{Pr}(\text{female})
    \end{align*}
    ``]



## Part 1

### (5) Mistake Group Digits of size 5




### (112) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:phodgson

	first_attempt
					2015-10-21 05:14:08
	part1_incorrect_attempt
					('0:00:00', u'.5 * .07 / .1')
	part1_correct_attempt
					['0:00:27', u'.5 * .07 / (.5 * .1)']

1 Student ID:v4zhang

	first_attempt
					2015-10-22 08:17:28
	part1_incorrect_attempt
					('0:00:00', u'.2727')
	part1_correct_attempt
					['0:03:00', u'(.06*.5)/.055']

2 Student ID:kew060

	first_attempt
					2015-10-22 22:35:20
	part1_incorrect_attempt
					('0:00:00', u'0.06*0.5/(0.6*0.5+0.3*0.5)')
	part1_correct_attempt
					['0:01:17', u'0.06*0.5/(0.06*0.5+0.03*0.5)']

3 Student ID:srl006

	first_attempt
					2015-10-22 04:45:56
	part1_incorrect_attempt
					('0:00:00', u'.06')
	part1_correct_attempt
					['0:01:05', u'.5833333']

4 Student ID:ssamudra

	first_attempt
					2015-10-22 22:14:24
	part1_incorrect_attempt
					('0:00:00', u'0.12')
	part1_correct_attempt
					['0:01:19', u'2/3']

5 Student ID:dcgriffi

	first_attempt
					2015-10-21 01:41:10
	part1_incorrect_attempt
					('0:00:00', u'.04/(.12)')
	part1_correct_attempt
					['0:00:26', u'.04/.06']

6 Student ID:jjm019

	first_attempt
					2015-10-20 16:12:49
	part1_incorrect_attempt
					('0:00:00', u'0.025')
					('0:11:44', u'.055')
					('0:13:43', u'.5')
	part1_correct_attempt
					['1 day, 10:32:07', u'.06*0.5/0.055']

7 Student ID:l5han

	first_attempt
					2015-10-22 06:50:26
	part1_incorrect_attempt
					('0:00:00', u'[0.08*0.5]/[0.08*0.2+0.04*0.5]')
	part1_correct_attempt
					['0:00:56', u'[0.08*0.5]/[0.08*0.5+0.04*0.5]']

8 Student ID:ctgraves

	first_attempt
					2015-10-21 01:21:52
	part1_incorrect_attempt
					('0:00:00', u'(0.06*0.5)/(0.06*0.5+0.03+0.5)')
	part1_correct_attempt
					['0:00:41', u'(0.06*0.5)/(0.06*0.5+0.03*0.5)']

9 Student ID:nhn018

	first_attempt
					2015-10-22 19:30:46
	part1_incorrect_attempt
					('0:00:00', u'.75')
	part1_correct_attempt
					['0:00:46', u'8/12']

10 Student ID:j5phung

	first_attempt
					2015-10-16 16:58:26
	part1_incorrect_attempt
					('0:00:00', u'0.06*.5/(0.06+0.5)')
	part1_correct_attempt
					['0:00:18', u'0.06*.5/(0.06*.5+0.05*.5)']

11 Student ID:haw081

	first_attempt
					2015-10-18 06:34:01
	part1_incorrect_attempt
					('0:00:00', u'0.07*0.04/0.11')
					('0:00:17', u'0.07*0.5/0.11')
	part1_correct_attempt
					['0:00:53', u'0.07*0.5/(0.07*0.5+0.04*0.5)']

12 Student ID:mnrahman

	first_attempt
					2015-10-22 17:26:01
	part1_incorrect_attempt
					('0:00:00', u'0.7')
					('0:00:34', u'0.6')
					('0:00:50', u'0.5')
					('0:00:00', u'0.4')
					('0:00:07', u'0.3')
					('0:00:12', u'0.2')
					('0:00:17', u'0.1')
					('0:00:22', u'0.8')
					('0:00:27', u'0.9')
					('0:00:34', u'1.0')
					('0:00:40', u'1.1')
					('0:00:46', u'.11')
					('0:00:00', u'((0.07*0.7))/((0.07*0.7)+(0.4*0.7))')
	part1_correct_attempt
					['2:53:51', u'(0.07)/(0.07+0.04)']

13 Student ID:rlhagen

	first_attempt
					2015-10-18 16:59:43
	part1_incorrect_attempt
					('0:00:00', u'(0.08*0.5)/(0.08/0.5+0.05/0.5)')
	part1_correct_attempt
					['0:01:57', u'(0.08*0.5)/(0.08*0.5+0.05*0.5)']

14 Student ID:asrana

	first_attempt
					2015-10-22 19:16:02
	part1_incorrect_attempt
					('0:00:00', u'.04')
	part1_correct_attempt
					['0:07:18', u'.6153846154']

15 Student ID:avasavad

	first_attempt
					2015-10-20 23:42:14
	part1_incorrect_attempt
					('0:00:00', u'(1/20)/(9/100)')
					('0:00:49', u'[(1/20)*(1/2)]/(9/100)')
	part1_correct_attempt
					['20:25:36', u'6/11']

16 Student ID:lalacson

	first_attempt
					2015-10-22 05:52:21
	part1_incorrect_attempt
					('0:00:00', u'(8/13)/.13')
	part1_correct_attempt
					['0:00:09', u'8/13']

17 Student ID:pthsu

	first_attempt
					2015-10-16 23:38:57
	part1_incorrect_attempt
					('0:00:00', u'.5')
	part1_correct_attempt
					['0:02:04', u'0.66666666666666666666666666666667']

18 Student ID:tcuddy

	first_attempt
					2015-10-17 06:09:13
	part1_incorrect_attempt
					('0:00:00', u'(.5)(.07)')
					('0:00:47', u'(.11)(.5)/(.07)')
					('0:01:40', u'(.07)(.5)/(.11)')
					('0:02:11', u'(.07)(.5)(.5)/(.11)')
					('10:51:54', u'[(.5)(.04)]')
	part1_correct_attempt
					['11:03:26', u'(.5)(.07)/[(.5)(.07)+(.5)(.04)]']

19 Student ID:dando

	first_attempt
					2015-10-20 15:34:15
	part1_incorrect_attempt
					('0:00:00', u'.5')
	part1_correct_attempt
					['2 days, 8:28:07', u'.7']

20 Student ID:sayao

	first_attempt
					2015-10-21 16:25:39
	part1_incorrect_attempt
					('0:00:00', u'.07')
	part1_correct_attempt
					['0:01:21', u'.07/(.07+.04)']

21 Student ID:seleon

	first_attempt
					2015-10-22 03:27:29
	part1_incorrect_attempt
					('0:00:00', u'.06/(.06*.03)')
	part1_correct_attempt
					['0:00:08', u'.06/(.06 + .03)']

22 Student ID:c1wei

	first_attempt
					2015-10-21 21:25:06
	part1_incorrect_attempt
					('0:00:00', u'0.12307')
	part1_correct_attempt
					['0:01:13', u'0.6153']

23 Student ID:mitopete

	first_attempt
					2015-10-19 02:54:48
	part1_incorrect_attempt
					('0:00:00', u'0.50')
					('0:01:46', u'(0.08*0.50)/0.13')
	part1_correct_attempt
					['0:02:52', u'(0.08*0.50)/((0.08*0.50)+(0.05*0.50))']

24 Student ID:tak068

	first_attempt
					2015-10-20 09:26:21
	part1_incorrect_attempt
					('0:00:00', u'0.8')
	part1_correct_attempt
					['0:00:53', u'0.8/(1.2)']

25 Student ID:yos017

	first_attempt
					2015-10-21 02:17:37
	part1_incorrect_attempt
					('0:00:00', u'0.5*0.07')
	part1_correct_attempt
					['0:04:55', u'(0.5*0.07)/[(0.5*0.07)+(0.5*0.05)]']

26 Student ID:jguanzho

	first_attempt
					2015-10-16 20:12:57
	part1_incorrect_attempt
					('0:00:00', u'.06*.5/(0.06-.05)')
	part1_correct_attempt
					['0:00:25', u'.06*.5/(0.06*.5+.05*.5)']

27 Student ID:small

	first_attempt
					2015-10-22 13:16:40
	part1_incorrect_attempt
					('0:00:00', u'54/5000')
	part1_correct_attempt
					['11:08:14', u'(0.06*0.5)/(0.06*0.5 + 0.03*0.5)']

28 Student ID:b3hwang

	first_attempt
					2015-10-21 04:58:32
	part1_incorrect_attempt
					('0:00:00', u'0.06/.1')
	part1_correct_attempt
					['0:00:11', u'0.06/.09']

29 Student ID:ccn001

	first_attempt
					2015-10-18 04:33:55
	part1_incorrect_attempt
					('0:00:00', u'0.06')
					('0:00:59', u'0.06(0.5)/0.9')
					('0:01:24', u'0.06(0.5)/0.09')
	part1_correct_attempt
					['0:02:24', u'(0.06(0.5))/((0.06)(0.5)+0.03(0.5))']

30 Student ID:lrlai

	first_attempt
					2015-10-21 19:00:24
	part1_incorrect_attempt
					('0:00:00', u'.08*.5 + .5*.05')
	part1_correct_attempt
					['0:09:06', u'.08*.5/(.08*.5 + .5*.05)']

31 Student ID:c1sorian

	first_attempt
					2015-10-21 20:58:08
	part1_incorrect_attempt
					('0:00:00', u'.5')
	part1_correct_attempt
					['0:03:16', u'.07*.5/.055']

32 Student ID:asp025

	first_attempt
					2015-10-21 17:43:46
	part1_incorrect_attempt
					('0:00:00', u'0.54')
	part1_correct_attempt
					['0:00:09', u'0.5454']

33 Student ID:thk002

	first_attempt
					2015-10-20 21:06:53
	part1_incorrect_attempt
					('0:00:00', u'3/100')
					('0:01:02', u'2/600')
					('0:05:49', u'10/100')
	part1_correct_attempt
					['0:18:52', u'0.6']

34 Student ID:krau

	first_attempt
					2015-10-20 20:11:47
	part1_incorrect_attempt
					('0:00:00', u'.07')
					('0:05:26', u'.07*.5/.11')
					('0:07:03', u'.00385')
					('0:07:53', u'.07*.5/.11')
	part1_correct_attempt
					['0:09:53', u'.07/.11']

35 Student ID:kthui

	first_attempt
					2015-10-18 06:41:01
	part1_incorrect_attempt
					('0:00:00', u'0.08*0.5+0.05*0.5')
					('0:01:55', u'0.08')
	part1_correct_attempt
					['0:03:14', u'(0.08*0.5)/(0.08*0.5+0.05*0.5)']

36 Student ID:mroknich

	first_attempt
					2015-10-22 05:44:39
	part1_incorrect_attempt
					('0:00:00', u'1.25')
					('0:00:14', u'.25')
					('0:00:00', u'.125')
					('0:00:20', u'1-.125')
					('0:00:00', u'(.66667)*(.004678)')

37 Student ID:alhung

	first_attempt
					2015-10-22 09:08:05
	part1_incorrect_attempt
					('0:00:00', u'.035')
	part1_correct_attempt
					['8:15:55', u'[(0.07)*(0.5)]/[(0.07)*(0.5)+(0.03)*(0.5)]']

38 Student ID:tpmach

	first_attempt
					2015-10-19 00:13:12
	part1_incorrect_attempt
					('0:00:00', u'0.04')
					('0:00:42', u'0.06')
					('0:00:00', u'0.03')
	part1_correct_attempt
					['3 days, 2:29:49', u'0.6']

39 Student ID:dis003

	first_attempt
					2015-10-22 06:37:05
	part1_incorrect_attempt
					('0:00:00', u'(.8)(.5)/(.12)')
					('0:02:15', u'(.08)(.05)/(.12)')
					('0:02:29', u'(.08)(.05)')
					('0:03:15', u'(.08)(.5)')
					('0:03:28', u'(.08)(.5)/(.12)')
	part1_correct_attempt
					['0:03:45', u'(.08)/(.12)']

40 Student ID:rraiyyan

	first_attempt
					2015-10-22 05:52:43
	part1_incorrect_attempt
					('0:00:00', u'0.07*0.5/0.08')
	part1_correct_attempt
					['0:00:58', u'0.07*0.5/0.05']

41 Student ID:t1tran

	first_attempt
					2015-10-18 01:36:10
	part1_incorrect_attempt
					('0:00:00', u'7/100/1/2')
					('0:09:38', u'1/2*7/100')
					('0:09:48', u'1/2*(7/100)')
	part1_correct_attempt
					['0:49:21', u'(7/100*.5)/(7/100*.5+4/100*.5)']

42 Student ID:dsmonaha

	first_attempt
					2015-10-19 15:38:58
	part1_incorrect_attempt
					('0:00:00', u'.35')
	part1_correct_attempt
					['0:02:35', u'.7']

43 Student ID:thwan

	first_attempt
					2015-10-18 04:20:55
	part1_incorrect_attempt
					('0:00:00', u'(0.08-0.5*0.03)/0.05')
					('0:01:29', u'(0.08-0.5*0.03)/0.5')
					('0:02:03', u'(0.08-0.5*0.03)')
	part1_correct_attempt
					['19:22:02', u'0.5*0.08/(0.5*0.08+0.5*0.03)']

44 Student ID:krkelkar

	first_attempt
					2015-10-21 21:22:57
	part1_incorrect_attempt
					('0:00:00', u'(.08)*(1/2)+(.03)*(1/2)')
	part1_correct_attempt
					['0:05:40', u'[(.08)*(.5)] / [ (.08)*(.5)+(.03)*(.5) ]']

45 Student ID:hmnaing

	first_attempt
					2015-10-20 22:01:08
	part1_incorrect_attempt
					('0:00:00', u'0.07*0.5/0.13')
					('0:00:10', u'0.07/0.5*0.13')
					('0:05:40', u'0.07/0.13')
					('0:00:00', u'(0.07*0.5)+ (0.04*0.5)')
					('0:00:00', u'(0.7*0.5)/((0.07*0.5)+ (0.04*0.5))')
	part1_correct_attempt
					['1 day, 4:43:43', u'(0.07*0.5)/((0.07*0.5)+ (0.04*0.5))']

46 Student ID:edescobe

	first_attempt
					2015-10-18 10:48:42
	part1_incorrect_attempt
					('0:00:00', u'.5*.08')
	part1_correct_attempt
					['0:02:20', u'.04/(.04+.5*.05)']

47 Student ID:etemlock

	first_attempt
					2015-10-21 09:21:39
	part1_incorrect_attempt
					('0:00:00', u'0.04/0.05')
					('0:00:06', u'0.04/0.5')
					('0:00:19', u'0.06/0.5')
					('0:00:32', u'0.006/0.5')
					('0:09:40', u'0.4')
	part1_correct_attempt
					['0:09:44', u'0.6']

48 Student ID:muy002

	first_attempt
					2015-10-22 21:37:08
	part1_incorrect_attempt
					('0:00:00', u'(0.06*(0.11))/(0.5)')
					('0:00:58', u'(0.06*((0.06*0.5)+(0.05*0.5)))/(0.5)')
	part1_correct_attempt
					['0:01:59', u'(0.06)(0.5)/(0.06*0.5+0.05*0.5)']

49 Student ID:jtfrankl

	first_attempt
					2015-10-20 23:16:26
	part1_incorrect_attempt
					('0:00:00', u'.5*.07')
	part1_correct_attempt
					['0:02:00', u'(.5*.07)/(.5*.07+.5*.04)']

50 Student ID:rbdoming

	first_attempt
					2015-10-18 00:27:45
	part1_incorrect_attempt
					('0:00:00', u'0.5')
	part1_correct_attempt
					['0:02:45', u'(0.08*0.5)/(0.5*0.08+0.5*0.05)']

51 Student ID:ralhadda

	first_attempt
					2015-10-22 16:44:47
	part1_incorrect_attempt
					('0:00:00', u'0.3')
					('0:03:21', u'0.48')
					('0:04:27', u'0.96')
					('0:09:15', u'0.943')
					('0:11:05', u'0.943396')
					('0:00:00', u'0.625')
					('0:00:40', u'0.943396')
					('0:00:51', u'0.94')
					('0:01:50', u'0.943')
	part1_correct_attempt
					['0:56:50', u'0.6']

52 Student ID:bpandayk

	first_attempt
					2015-10-22 04:02:59
	part1_incorrect_attempt
					('0:00:00', u'0.01523')
					('0:00:00', u'0.666')
	part1_correct_attempt
					['0:26:36', u'0.667']

53 Student ID:bkoli

	first_attempt
					2015-10-22 20:05:11
	part1_incorrect_attempt
					('0:00:00', u'0.9')
					('0:00:10', u'0.10')
					('0:11:13', u'((0.06)(0.6))/(((0.06)(0.6))+((0.4)(0.6)))')
					('0:00:00', u'((0.06)(0.5))/(((0.06)(0.5))+((0.4)(0.5)))')
	part1_correct_attempt
					['0:14:04', u'(0.06)/(0.06+0.04)']

54 Student ID:k3tan

	first_attempt
					2015-10-22 21:48:43
	part1_incorrect_attempt
					('0:00:00', u'0.03/0.045')
					('0:00:00', u'0.05/0.045')
					('0:00:00', u'0.05/0.055')
					('0:00:04', u'0.06/0.055')
	part1_correct_attempt
					['0:15:36', u'0.03/0.055']

55 Student ID:ctroncos

	first_attempt
					2015-10-22 03:20:45
	part1_incorrect_attempt
					('0:00:00', u'0.5')
					('0:00:00', u'0.2916')
					('0:00:00', u'0.035')
					('0:01:36', u'0.0105')
					('0:02:33', u'0.3')
					('0:02:43', u'0.29167')
	part1_correct_attempt
					['0:54:16', u'0.5833']

56 Student ID:lywong

	first_attempt
					2015-10-20 23:17:49
	part1_incorrect_attempt
					('0:00:00', u'.35')
					('0:00:00', u'.035')
	part1_correct_attempt
					['8:30:18', u'.70']

57 Student ID:jix029

	first_attempt
					2015-10-20 19:50:37
	part1_incorrect_attempt
					('0:00:00', u'.06*.5')
					('0:01:41', u'.06*.5/.5')
	part1_correct_attempt
					['0:02:09', u'.06*.5/(.5*.06+.5*.03)']

58 Student ID:hkhodada

	first_attempt
					2015-10-17 19:29:02
	part1_incorrect_attempt
					('0:00:00', u'40/10000')
					('0:00:54', u'4000/80000')
					('0:00:00', u'8/100')
					('0:00:08', u'1/2')
					('0:00:40', u'4/100')
					('0:11:16', u'2/25')
					('0:00:00', u'4/12')
	part1_correct_attempt
					['3 days, 4:32:12', u'2/3']

59 Student ID:glcohen

	first_attempt
					2015-10-17 23:35:49
	part1_incorrect_attempt
					('0:00:00', u'7/12')
	part1_correct_attempt
					['0:00:10', u'7/11']

60 Student ID:acvuong

	first_attempt
					2015-10-18 00:28:12
	part1_incorrect_attempt
					('0:00:00', u'0.07*0.5+0.04*0.5')
	part1_correct_attempt
					['0:00:46', u'(0.07*0.5)/(0.07*0.5+0.04*0.5)']

61 Student ID:sachadal

	first_attempt
					2015-10-22 17:51:44
	part1_incorrect_attempt
					('0:00:00', u'((0.06)*(0.09))/(0.5)')
	part1_correct_attempt
					['0:04:38', u'(0.06*0.5)/((0.06*0.5)+(0.03*0.5))']

62 Student ID:pvl001

	first_attempt
					2015-10-19 02:51:11
	part1_incorrect_attempt
					('0:00:00', u'0.50')
	part1_correct_attempt
					['0:09:31', u'.50 * .07 / ((.07 * .50) + (.05 * .50))']

63 Student ID:t2li

	first_attempt
					2015-10-22 23:09:54
	part1_incorrect_attempt
					('0:00:00', u'(0.05*0.5)/(0.05*0.5 + 0.01*0.5)')
					('0:00:17', u'(0.05*0.5)/(0.05*0.5 + 0.01*0.5)')
					('0:00:27', u'(0.05*0.5)/(0.05*0.5 + 0.07*0.5)')
	part1_correct_attempt
					['0:01:27', u'(0.07*0.5)/(0.05*0.5 + 0.07*0.5)']

64 Student ID:dlt009

	first_attempt
					2015-10-22 05:55:35
	part1_incorrect_attempt
					('0:00:00', u'0.08')
					('0:01:03', u'.307')
					('0:01:09', u'.3077')
					('0:01:18', u'.3')
					('0:03:21', u'0.065')
	part1_correct_attempt
					['0:03:51', u'0.615']

65 Student ID:mbl003

	first_attempt
					2015-10-18 20:25:32
	part1_incorrect_attempt
					('0:00:00', u'.5*.08+.03*.5')
					('0:00:47', u'(.5*.08)+(.5*.03)')
	part1_correct_attempt
					['0:02:21', u'(.5*.08)/((.5*.08)+(.5*.03))']

66 Student ID:n2patil

	first_attempt
					2015-10-21 02:51:12
	part1_incorrect_attempt
					('0:00:00', u'.5')
	part1_correct_attempt
					['2:29:42', u'.04/.065']

67 Student ID:ganajera

	first_attempt
					2015-10-16 01:59:27
	part1_incorrect_attempt
					('0:00:00', u'0.065')
					('0:03:15', u'.06')
					('0:06:08', u'.04/.06')
	part1_correct_attempt
					['0:10:28', u'(.08*.5)/.065']

68 Student ID:nnh002

	first_attempt
					2015-10-21 23:29:19
	part1_incorrect_attempt
					('0:00:00', u'.12')
					('0:05:14', u'1/3')
					('0:06:42', u'0.04')
	part1_correct_attempt
					['0:07:09', u'2/3']

69 Student ID:akhmelni

	first_attempt
					2015-10-22 20:02:52
	part1_incorrect_attempt
					('0:00:00', u'5/7')
	part1_correct_attempt
					['2:03:17', u'((7/100)(.5))/(6/100)']

70 Student ID:tol003

	first_attempt
					2015-10-20 22:48:06
	part1_incorrect_attempt
					('0:00:00', u'.35')
	part1_correct_attempt
					['0:00:17', u'.7']

71 Student ID:aakumar

	first_attempt
					2015-10-19 04:50:04
	part1_incorrect_attempt
					('0:00:00', u'.055')
	part1_correct_attempt
					['0:15:00', u'.04/.055']

72 Student ID:kew017

	first_attempt
					2015-10-22 18:14:22
	part1_incorrect_attempt
					('0:00:00', u'1/0.05')
	part1_correct_attempt
					['0:01:54', u'6/11']

73 Student ID:q3wen

	first_attempt
					2015-10-21 22:46:45
	part1_incorrect_attempt
					('0:00:00', u'1/3')
	part1_correct_attempt
					['0:00:26', u'2/3']

74 Student ID:yeh013

	first_attempt
					2015-10-22 08:04:52
	part1_incorrect_attempt
					('0:00:00', u'7/200')
	part1_correct_attempt
					['0:02:01', u'7/10']

75 Student ID:eaherman

	first_attempt
					2015-10-22 05:37:00
	part1_incorrect_attempt
					('0:00:00', u'.0064')
					('0:01:19', u'.064')
					('0:01:32', u'6.4')
					('0:01:43', u'.64')
					('0:00:00', u'.0052/.5')
					('0:00:00', u'.052/.5')
	part1_correct_attempt
					['11:50:24', u'8/13']

76 Student ID:fichoi

	first_attempt
					2015-10-22 02:58:36
	part1_incorrect_attempt
					('0:00:00', u'0.065')
					('0:00:05', u'0.065*100')
					('0:02:31', u'0.5')
					('0:02:53', u'0.61')
	part1_correct_attempt
					['0:02:58', u'0.6154']

77 Student ID:csl030

	first_attempt
					2015-10-22 00:10:05
	part1_incorrect_attempt
					('0:00:00', u'.5 * .06')
	part1_correct_attempt
					['0:02:41', u'(.5 * .06)/ ((.5 * .06) + (.5*.04))']

78 Student ID:ytc012

	first_attempt
					2015-10-21 10:29:23
	part1_incorrect_attempt
					('0:00:00', u'(6/100)0.5/0.11')
	part1_correct_attempt
					['0:04:59', u'0.06(0.5)/((0.06)(0.5)+(0.05)(0.5))']

79 Student ID:dlgoldbe

	first_attempt
					2015-10-22 06:18:05
	part1_incorrect_attempt
					('0:00:00', u'((0.08)*(0.5))/(0.12)')
	part1_correct_attempt
					['0:00:26', u'((0.08)*(0.5))/0.06']

80 Student ID:kquong

	first_attempt
					2015-10-17 22:32:02
	part1_incorrect_attempt
					('0:00:00', u'.08 * .05/(.08 * .05 + .3 * .5)')
					('0:01:36', u'.08/(.08 * .05 + .3 * .5)')
					('0:02:16', u'.08* .05(.08 * .5 + .3 * .5)')
					('0:02:26', u'.08* .05/(.08 * .5 + .3 * .5)')
					('0:12:15', u'.08* .05/(.08 * .5 + .03 * .5)')
	part1_correct_attempt
					['0:12:50', u'.08* .5/(.08 * .5 + .03 * .5)']

81 Student ID:agoldsht

	first_attempt
					2015-10-20 05:10:29
	part1_incorrect_attempt
					('0:00:00', u'((.08*.5)*.5)/((.08*.5)*.5)+(.03*.5*.5)')
	part1_correct_attempt
					['0:21:26', u'.08/(.13)']

82 Student ID:agian

	first_attempt
					2015-10-22 20:35:58
	part1_incorrect_attempt
					('0:00:00', u'0.07/0.07+0.04')
	part1_correct_attempt
					['0:00:07', u'0.07/(0.07+0.04)']

83 Student ID:vsamant

	first_attempt
					2015-10-16 18:10:39
	part1_incorrect_attempt
					('0:00:00', u'.06*.5/(.06*.5+.05*.5)')
	part1_correct_attempt
					['0:00:09', u'.06*.5/(.06*.5+.04*.5)']

84 Student ID:ppanourg

	first_attempt
					2015-10-22 09:36:43
	part1_incorrect_attempt
					('0:00:00', u'.1')
					('0:00:00', u'(.06*.1)/.5')
					('0:07:08', u'(.06)(.06*.5+.4*.5)/.5')
					('0:07:25', u'(.06)(.06*.5+.04*.5)/.5')
					('0:09:29', u'(.06)((.06*.5+.04*.5)/2)/.5')
					('0:10:31', u'.5')
					('0:10:53', u'.5*.06')
					('0:13:05', u'(.06)((.06+.04)/2)/.5')
					('0:13:16', u'(.06)((.06+.04))/.5')
	part1_correct_attempt
					['0:30:52', u'(.06*.5)/(.5*.06 + .5*.04)']

85 Student ID:any027

	first_attempt
					2015-10-19 19:17:51
	part1_incorrect_attempt
					('0:00:00', u'0.07')
	part1_correct_attempt
					['0:07:56', u'(0.07 * 0.50) / ( (0.07 * 0.50) + (0.05 * 0.50) )']

86 Student ID:rwthomps

	first_attempt
					2015-10-20 22:21:23
	part1_incorrect_attempt
					('0:00:00', u'(.07 * .5 * .5) / (.07 * .5 * .03 * .5)')
					('0:00:38', u'(.07 * .5) / (.07 * .5 * .03 * .5)')
	part1_correct_attempt
					['0:04:14', u'(.07 * .5) / (.07 * .5 + .03 * .5)']

87 Student ID:vsosnovs

	first_attempt
					2015-10-21 06:52:46
	part1_incorrect_attempt
					('0:00:00', u'.7*.5')
					('0:00:11', u'.07*.5')
					('0:00:23', u'.5')
					('0:01:02', u'.5*.12')
					('0:01:48', u'(.5*.07)/.07')
					('0:01:55', u'(.5*.07)/.12')
	part1_correct_attempt
					['0:03:06', u'.07/.12']

88 Student ID:jdeon

	first_attempt
					2015-10-21 22:47:41
	part1_incorrect_attempt
					('0:00:00', u'(.06 * .5)/(.1)')
	part1_correct_attempt
					['0:00:49', u'(.06 * .5)/(.06 * .5 + .04 *.5)']

89 Student ID:p4kumar

	first_attempt
					2015-10-22 16:19:05
	part1_incorrect_attempt
					('0:00:00', u'7/13')
					('0:00:00', u'0.07/(0.07*0.5 + 0.05*0.5)')
	part1_correct_attempt
					['1:11:18', u'0.07/0.12']

90 Student ID:s2chaudh

	first_attempt
					2015-10-19 17:05:59
	part1_incorrect_attempt
					('0:00:00', u'(.007*.05)/.1')
					('0:00:13', u'(.07*.5)/.1')
					('0:00:49', u'(.07*.43)/.1')
	part1_correct_attempt
					['0:06:05', u'7/10']

91 Student ID:jmiclat

	first_attempt
					2015-10-19 23:11:51
	part1_incorrect_attempt
					('0:00:00', u'(0.50)(0.06)/(0.11)')
	part1_correct_attempt
					['0:01:00', u'(0.50)(0.06)/[(0.05)(0.50) + (0.06)(0.50)]']

92 Student ID:bmilton

	first_attempt
					2015-10-21 03:00:28
	part1_incorrect_attempt
					('0:00:00', u'.08/(.08*.5 + .04*.5)')
	part1_correct_attempt
					['0:00:40', u'.08*.5/(.08*.5 + .04*.5)']

93 Student ID:jhc010

	first_attempt
					2015-10-22 07:18:44
	part1_incorrect_attempt
					('0:00:00', u'0.06*(0.07/0.05)')
					('0:00:10', u'(0.07/0.05)')
					('0:03:29', u'.06*.07/.06')
	part1_correct_attempt
					['0:04:24', u'7/12']

94 Student ID:cfgutier

	first_attempt
					2015-10-22 09:42:26
	part1_incorrect_attempt
					('0:00:00', u'.0088/.11')
					('0:00:21', u'.8')
	part1_correct_attempt
					['12:30:16', u'(.08*.5)/((.08*.5)+(.03*.5))']

95 Student ID:dkostins

	first_attempt
					2015-10-20 22:28:18
	part1_incorrect_attempt
					('0:00:00', u'.06')
	part1_correct_attempt
					['0:01:01', u'.06/.1']

96 Student ID:twsalim

	first_attempt
					2015-10-20 05:06:19
	part1_incorrect_attempt
					('0:00:00', u'0.54')
	part1_correct_attempt
					['0:05:47', u'0.54545454']

97 Student ID:s6deng

	first_attempt
					2015-10-21 22:50:57
	part1_incorrect_attempt
					('0:00:00', u'5/13')
					('0:05:12', u'0.08*.5')
					('0:05:22', u'(0.08*.5) / 1')
					('0:06:06', u'(8/100)(1/2)')

98 Student ID:kalang

	first_attempt
					2015-10-22 02:35:16
	part1_incorrect_attempt
					('0:00:00', u'.05/(.05+.06)')
					('0:00:24', u'.05/((.05+.06)*2)')
					('0:00:31', u'.05/((.05+.06))')
					('0:05:02', u'5/6')
					('0:05:21', u'5/11')
	part1_correct_attempt
					['0:06:26', u'6/11']

99 Student ID:aalhaida

	first_attempt
					2015-10-22 19:12:38
	part1_incorrect_attempt
					('0:00:00', u'.5')
					('0:01:44', u'.6')
					('0:01:50', u'.06')
					('0:01:55', u'.05')
					('0:00:00', u'3.33')
					('0:00:59', u'6.66')
	part1_correct_attempt
					['0:08:05', u'.6666']

100 Student ID:hah008

	first_attempt
					2015-10-21 07:08:33
	part1_incorrect_attempt
					('0:00:00', u'(7 * 50) / 11')
					('0:00:08', u'0.318182')
					('0:20:03', u'0.5')
					('0:00:00', u'(1/2 * 7/100) / ((1/2 * 7/100) * (1/2 * 4/100))')
					('0:00:54', u'(1/2 * 7/100) / ((1/2 * (7/100)) * (1/2 * (4/100)))')
					('0:01:08', u'(1/2 * (7/100)) / ((1/2 * (7/100)) * (1/2 * (4/100)))')
					('0:03:42', u'(50 * (7/100)) / ((50 * (7/100)) * (50 * (4/100)))')
	part1_correct_attempt
					['13:12:19', u'(1/2 * (7/100)) / ((1/2 * (7/100)) + (1/2 * (4/100)))']

101 Student ID:jjchung

	first_attempt
					2015-10-21 02:46:01
	part1_incorrect_attempt
					('0:00:00', u'.024/.05')
	part1_correct_attempt
					['0:04:07', u'6/10']

102 Student ID:acs008

	first_attempt
					2015-10-22 03:59:35
	part1_incorrect_attempt
					('0:00:00', u'(0.07*0.5)/(0.05*0.07+0.05*0.04)')
	part1_correct_attempt
					['0:03:11', u'(0.07*0.5)/(0.5*0.07+0.5*0.04)']

103 Student ID:dtea

	first_attempt
					2015-10-22 21:39:17
	part1_incorrect_attempt
					('0:00:00', u'0.06')
					('0:00:00', u'(.5*.06+.5*.04)*0.5/(.5*.06+.5*.04)')
					('0:00:00', u'.5*.06+.5*.04')
					('0:00:00', u'(0.06)*.05(.5*.06+.5*.04)')
					('0:00:07', u'(0.06)*.5(.5*.06+.5*.04)')
					('0:00:54', u'(0.06)*.5')
	part1_correct_attempt
					['0:25:47', u'(0.06)*.5/(.5*.06+.5*.04)']

104 Student ID:lahawkin

	first_attempt
					2015-10-19 04:17:11
	part1_incorrect_attempt
					('0:00:00', u'(.06*.5)+(.05+.5)')
					('0:00:36', u'(.06*.5)/((.06*.5)+(.05+.5))')
	part1_correct_attempt
					['0:00:49', u'(.06*.5)/((.06*.5)+(.05*.5))']

105 Student ID:edcole

	first_attempt
					2015-10-20 01:02:33
	part1_incorrect_attempt
					('0:00:00', u'(.5)(.06)')
					('0:01:14', u'(.06)/(.03)')
					('0:01:55', u'((.06)/(.03))/.5')
					('0:02:11', u'((.06)/(.03))*(.5)')
					('0:04:16', u'((.06)*(.5))/((.06)*(.03))')
					('0:00:00', u'((.06)*(.09))/(.5)')
					('0:03:07', u'((.06)*(.045))/(.5)')
	part1_correct_attempt
					['16:57:47', u'2/3']

106 Student ID:aordookh

	first_attempt
					2015-10-21 22:25:25
	part1_incorrect_attempt
					('0:00:00', u'.63')
					('0:01:38', u'.64')
					('0:00:00', u'.07/.055')
	part1_correct_attempt
					['5:35:10', u'0.07*0.5/0.055']

107 Student ID:yig015

	first_attempt
					2015-10-22 09:00:06
	part1_incorrect_attempt
					('0:00:00', u'7/5')
	part1_correct_attempt
					['0:00:36', u'7/10']

108 Student ID:vasharma

	first_attempt
					2015-10-20 18:47:54
	part1_incorrect_attempt
					('0:00:00', u'.06*.5 + .5*.05')
					('0:00:25', u'.06/(.06*.5 + .5*.05)')
	part1_correct_attempt
					['0:00:57', u'.06/(.06 +.05)']

109 Student ID:ajvanega

	first_attempt
					2015-10-20 23:25:14
	part1_incorrect_attempt
					('0:00:00', u'.72')
	part1_correct_attempt
					['0:00:33', u'.7272']

110 Student ID:j6quach

	first_attempt
					2015-10-22 17:28:11
	part1_incorrect_attempt
					('0:00:00', u'.16')
					('0:01:16', u'.307')
	part1_correct_attempt
					['0:03:31', u'.6153846']

111 Student ID:mjethani

	first_attempt
					2015-10-21 23:04:41
	part1_incorrect_attempt
					('0:00:00', u'0.5')
					('0:06:48', u'((0.07)(0.05))/(0.055)')
	part1_correct_attempt
					['0:07:10', u'((0.07)(0.5))/(0.055)']












