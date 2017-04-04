#Problem 9

    $a=random(2,2,1);
    $b=random(2,3,1);
    $c = 7-$a-$b;

    1. How many ways are there of picking one digit (from 0-9), then one letter (A-Z)?
    Your answer is: [____________________]{Compute("10*26")}.

    2. Standard automobile license plates in a country display [$a] numbers,
    followed by [$b] letters, followed by [$c] numbers.
    How many different standard plates are possible in this system?
    (Assume repetition of letters and numbers is allowed.)
    Your answer is: [____________________]{Compute("10**$a*26**$b*10**$c")}.


## Part 1

### (36) Mistake Group Digits of size 36




### (27) Mistake Group ['R.1'] of size 27
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|10*26	|9*26	|[('R.1', 26.0, u'26', u'26')]	|
|1	|10*26	|9+26	|[('R.1', 26.0, u'26', u'26')]	|




### (6) Mistake Group ['R.0'] of size 6
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|10*26	|10*24	|[('R.0', 10.0, u'10', u'10')]	|
|1	|10*26	|10^2	|[('R.0', 10.0, u'10', u'10')]	|
|2	|10*26	|10*36	|[('R.0', 10.0, u'10', u'10')]	|
|3	|10*26	|10*260	|[('R.0', 10.0, u'10', u'10')]	|




### (4) Mistake Group Fraction of size 4




### (3) Mistake Group ['R.0', 'R.1'] of size 3
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|10*26	|10^26	|[('R.0', 10.0, u'10', u'10'), ('R.1', 26.0, u'26', u'26')]	|




### (24) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:dmn009

	first_attempt
					2015-10-08 09:23:27
	part1_incorrect_attempt
					('0:00:00', u'9*27')
					('0:00:13', u'9*25')
	part1_correct_attempt
					['0:00:26', u'260']

1 Student ID:dlgoldbe

	first_attempt
					2015-10-08 04:32:40
	part1_incorrect_attempt
					('0:00:00', u'(9*26)/2')
					('0:04:32', u'(9!*26!)/2')
	part1_correct_attempt
					['0:07:03', u'10*26']

2 Student ID:jag028

	first_attempt
					2015-10-05 05:41:04
	part1_incorrect_attempt
					('0:00:00', u'9!*26!')
	part1_correct_attempt
					['0:00:25', u'10*26']

3 Student ID:ctroncos

	first_attempt
					2015-10-07 21:26:11
	part1_incorrect_attempt
					('0:00:00', u'9*27')
	part1_correct_attempt
					['0:00:35', u'10*26']

4 Student ID:kvass

	first_attempt
					2015-10-04 20:44:25
	part1_incorrect_attempt
					('0:00:00', u'9*24')
	part1_correct_attempt
					['0:01:53', u'10*26']

5 Student ID:nisharma

	first_attempt
					2015-10-04 22:42:36
	part1_incorrect_attempt
					('0:00:00', u'26*9')
	part1_correct_attempt
					['0:00:38', u'26*10']

6 Student ID:jguanzho

	first_attempt
					2015-10-02 07:47:07
	part1_incorrect_attempt
					('0:00:00', u'9!*26!')
	part1_correct_attempt
					['0:01:14', u'10*26']

7 Student ID:vsosnovs

	first_attempt
					2015-10-04 17:12:46
	part1_incorrect_attempt
					('0:00:00', u'(10!)(26!)')
					('0:00:20', u'(10!)(26!)/(36)')
	part1_correct_attempt
					['0:01:04', u'(10)(26)']

8 Student ID:lalacson

	first_attempt
					2015-10-03 02:40:41
	part1_incorrect_attempt
					('0:00:00', u'9!*26!')
	part1_correct_attempt
					['12:31:44', u'10*26']

9 Student ID:kalang

	first_attempt
					2015-10-05 22:25:41
	part1_incorrect_attempt
					('0:00:00', u'10*26/2')
	part1_correct_attempt
					['0:00:59', u'10*26']

10 Student ID:jhw015

	first_attempt
					2015-10-04 02:22:45
	part1_incorrect_attempt
					('0:00:00', u'9! * 26!')
					('0:00:16', u'10! * 26!')
	part1_correct_attempt
					['0:00:36', u'10*26']

11 Student ID:ajabasa

	first_attempt
					2015-10-05 19:42:26
	part1_incorrect_attempt
					('0:00:00', u'10*10*26*26*10*10*10')
	part1_correct_attempt
					['0:00:09', u'10*26']

12 Student ID:sayao

	first_attempt
					2015-10-02 23:58:14
	part1_incorrect_attempt
					('0:00:00', u'26*9')
					('0:46:08', u'(10!)*(26!)')
	part1_correct_attempt
					['0:46:17', u'(10)*(26)']

13 Student ID:achava

	first_attempt
					2015-10-02 04:28:37
	part1_incorrect_attempt
					('0:00:00', u'10!26!')
	part1_correct_attempt
					['0:00:08', u'260']

14 Student ID:ssamudra

	first_attempt
					2015-10-08 07:33:03
	part1_incorrect_attempt
					('0:00:00', u'26 * 9')
	part1_correct_attempt
					['0:00:21', u'10 * 26']

15 Student ID:wcwhite

	first_attempt
					2015-10-06 18:32:55
	part1_incorrect_attempt
					('0:00:00', u'10! * 26!')
					('0:00:11', u'10! +26!')
					('0:02:58', u'36!')
					('0:04:00', u'36!*10')
	part1_correct_attempt
					['0:04:24', u'10*26']

16 Student ID:sthapa

	first_attempt
					2015-10-06 06:11:02
	part1_incorrect_attempt
					('0:00:00', u'9*15')
					('0:01:45', u'(26!/(9!*15!))')
	part1_correct_attempt
					['0:03:32', u'260']

17 Student ID:arc013

	first_attempt
					2015-10-04 21:50:37
	part1_incorrect_attempt
					('0:00:00', u'10!26!')
	part1_correct_attempt
					['0:00:55', u'10*26']

18 Student ID:ralhadda

	first_attempt
					2015-10-08 16:43:55
	part1_incorrect_attempt
					('0:00:00', u'1*10^26')
					('0:01:08', u'26^10')
	part1_correct_attempt
					['0:09:16', u'260']

19 Student ID:bkoli

	first_attempt
					2015-10-08 06:36:09
	part1_incorrect_attempt
					('0:00:00', u'10!*26!')
	part1_correct_attempt
					['0:01:51', u'10*26']

20 Student ID:yypan

	first_attempt
					2015-10-02 04:41:41
	part1_incorrect_attempt
					('0:00:00', u'9*24')
	part1_correct_attempt
					['0:00:27', u'10*26']

21 Student ID:ajvanega

	first_attempt
					2015-10-02 17:59:00
	part1_incorrect_attempt
					('0:00:00', u'26^10')
	part1_correct_attempt
					['0:01:31', u'26*10']

22 Student ID:mtrafeca

	first_attempt
					2015-10-02 03:32:10
	part1_incorrect_attempt
					('0:00:00', u'10!*26!')
	part1_correct_attempt
					['0:36:29', u'10*26']

23 Student ID:kgrozav

	first_attempt
					2015-10-02 20:56:22
	part1_incorrect_attempt
					('0:00:00', u'9^2')
	part1_correct_attempt
					['0:00:52', u'10*26']












## Part 2

### (77) Mistake Group Digits of size 77




### (18) Mistake Group redirect of size 18




### (16) Mistake Group ['R.0.0'] of size 16
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|10^2*26^2*10^3	|10*10*26*10	|[('R.0.0', 100.0, u'10^2', u'10*10')]	|
|1	|10^2*26^3*10^2	|100*26*10	|[('R.0.0', 100.0, u'10^2', u'100')]	|
|2	|10^2*26^2*10^3	|10 * 10 * 26 * 10	|[('R.0.0', 100.0, u'10^2', u'10 * 10')]	|
|3	|10^2*26^2*10^3	|100 * 26 * 10	|[('R.0.0', 100.0, u'10^2', u'100')]	|
|4	|10^2*26^3*10^2	|10*10*3*2	|[('R.0.0', 100.0, u'10^2', u'10*10')]	|




### (6) Mistake Group ['R.0.1.0'] of size 6
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|10^2*26^3*10^2	|9*8+26*25+24*9*8	|[('R.0.1.0', 26.0, u'26', u'26')]	|
|1	|10^2*26^3*10^2	|9*9+26*26+24*9*9	|[('R.0.1.0', 26.0, u'26', u'26')]	|
|2	|10^2*26^3*10^2	|10!*10!*26!*10!	|[('R.0.1.0', 26.0, u'26', u'26')]	|
|3	|10^2*26^3*10^2	|20!*26!*10!	|[('R.0.1.0', 26.0, u'26', u'26')]	|
|4	|10^2*26^3*10^2	|100!*26!*10!	|[('R.0.1.0', 26.0, u'26', u'26')]	|
|5	|10^2*26^3*10^2	|2(10)*3(26)*2(10)	|[('R.0.1.0', 26.0, u'26', u'26')]	|




### (4) Mistake Group ['R.0'] of size 4
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|10^2*26^3*10^2	|10*10*26^3*1000	|[('R.0', 1757600.0, u'10^2*26^3', u'10*10*26^3')]	|
|1	|10^2*26^3*10^2	|10^2*26^3*10	|[('R.0', 1757600.0, u'10^2*26^3', u'10^2*26^3')]	|
|2	|10^2*26^2*10^3	|10*10*26*26*10	|[('R.0', 67600.0, u'10^2*26^2', u'10*10*26*26')]	|
|3	|10^2*26^3*10^2	|100*(26^3)*10	|[('R.0', 1757600.0, u'10^2*26^3', u'100*(26^3)')]	|




### (4) Mistake Group ['R.0.0.0'] of size 4
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|10^2*26^2*10^3	|10 * 9 * 26 * 8	|[('R.0.0.0', 10.0, u'10', u'10')]	|
|1	|10^2*26^2*10^3	|(10!/5!)*(26!*24!)	|[('R.0.0.0', 10.0, u'10', u'10')]	|
|2	|10^2*26^2*10^3	|(10!/5!)*(26!/24!)	|[('R.0.0.0', 10.0, u'10', u'10')]	|
|3	|10^2*26^2*10^3	|(10!/5!)+(26!/24!)	|[('R.0.0.0', 10.0, u'10', u'10')]	|




### (3) Mistake Group ['R.0.1.1'] of size 3
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|10^2*26^3*10^2	|6*10^3*26	|[('R.0.1.1', 3.0, u'3', u'3')]	|
|1	|10^2*26^3*10^2	|12*10^3*26	|[('R.0.1.1', 3.0, u'3', u'3')]	|
|2	|10^2*26^3*10^2	|11*10^3*26	|[('R.0.1.1', 3.0, u'3', u'3')]	|




### (3) Mistake Group ['R.0.1.0', 'R.0.1.1'] of size 3
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1.0', 'R.0.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|10^2*26^3*10^2	|100*(26*3)*100	|[('R.0.1.0', 26.0, u'26', u'26'), ('R.0.1.1', 3.0, u'3', u'3')]	|
|1	|10^2*26^3*10^2	|20+(26*3)+(20)	|[('R.0.1.0', 26.0, u'26', u'26'), ('R.0.1.1', 3.0, u'3', u'3')]	|
|2	|10^2*26^3*10^2	|20*(26*3)*(20)	|[('R.0.1.0', 26.0, u'26', u'26'), ('R.0.1.1', 3.0, u'3', u'3')]	|




### (2) Mistake Group Fraction of size 2




### (1) Mistake Group ['R.0.0.0', 'R.0.0.1', 'R.0.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0', 'R.0.0.1', 'R.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|10^2*26^3*10^2	|(10*2)+(26*26*26)+(20)	|[('R.0.0.0', 10.0, u'10', u'10'), ('R.0.0.1', 2.0, u'2', u'2'), ('R.0.1', 17576.0, u'26^3', u'26*26*26')]	|




### (1) Mistake Group ['R.0.0.0', 'R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|10^2*26^2*10^3	|10*26*26*1000	|[('R.0.0.0', 10.0, u'10', u'10'), ('R.1', 1000.0, u'10^3', u'1000')]	|




### (1) Mistake Group ['R.0.0', 'R.0.1', 'R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0', 'R.0.1', 'R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|10^2*26^2*10^3	|10^2 + 26^2 + 10^3	|[('R.0.0', 100.0, u'10^2', u'10^2'), ('R.0.1', 676.0, u'26^2', u'26^2'), ('R.1', 1000.0, u'10^3', u'10^3')]	|




### (1) Mistake Group ['R.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|10^2*26^2*10^3	|10*10*27*27*1000	|[('R.1', 1000.0, u'10^3', u'1000')]	|




### (1) Mistake Group ['R.0.1.0', 'R.1.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1.0', 'R.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|10^2*26^2*10^3	|C(10,2)*C(26,2)*C(10,3)	|[('R.0.1.0', 26.0, u'26', u'26'), ('R.1.1', 3.0, u'3', u'3')]	|




### (1) Mistake Group ['R.0.1', 'R.1.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1', 'R.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|10^2*26^2*10^3	|(9^2)*(26^2)*(9^3)	|[('R.0.1', 676.0, u'26^2', u'26^2'), ('R.1.1', 3.0, u'3', u'3')]	|




### (1) Mistake Group ['R.0.0.0', 'R.0.0.1', 'R.0.1.0', 'R.0.1.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.0.0', 'R.0.0.1', 'R.0.1.0', 'R.0.1.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|10^2*26^3*10^2	|(10*2)+(26*3)+(20)	|[('R.0.0.0', 10.0, u'10', u'10'), ('R.0.0.1', 2.0, u'2', u'2'), ('R.0.1.0', 26.0, u'26', u'26'), ('R.0.1.1', 3.0, u'3', u'3')]	|




### (1) Mistake Group ['R.0.1'] of size 1
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|['R.0.1']	|"hint"	|

|	|Answer	|Attempt	|Matching sub-exp|
|---|---|---|---|
|0	|10^2*26^3*10^2	|10*(26^3)*(10^2)	|[('R.0.1', 17576.0, u'26^3', u'26^3')]	|




### (34) No Match Group 
""" Please write hint here """

|ID	|Author	|Condition	|Hint Text|
|---|---|---|---|
|0|	|	|"hint"	|

0 Student ID:c2qiu

	first_attempt
					2015-10-06 15:23:09
	part1_correct_attempt
					['0:00:00', u'260']
	part2_incorrect_attempt
					('0:00:00', u'(10!/8!)*(26!/24!)*(10!/7!)')
	part2_correct_attempt
					['0:00:38', u'100*1000*26*26']

1 Student ID:jfalcone

	first_attempt
					2015-10-07 03:08:28
	part1_correct_attempt
					['0:00:00', u'10 * 26']
	part2_incorrect_attempt
					('0:00:00', u'10 * 26 * 10 * 10 *10')
					('0:00:15', u'10 * 10 * 26 * 10 * 10 *10')
	part2_correct_attempt
					['0:00:32', u'10 * 10 * 26 * 26 * 10 * 10 *10']

2 Student ID:ctroncos

	first_attempt
					2015-10-07 21:26:46
	part1_correct_attempt
					['0:00:00', u'10*26']
	part2_incorrect_attempt
					('0:00:37', u'10*9*26*10')
	part2_correct_attempt
					['0:01:39', u'10*10*26*26*26*10*10']

3 Student ID:vsamant

	first_attempt
					2015-10-02 04:12:16
	part1_correct_attempt
					['0:00:00', u'26*10']
	part2_incorrect_attempt
					('0:00:00', u'9*2+3*26+2*9')
					('0:02:00', u'9*2*3*26*2*9')
					('0:03:37', u'9*8*26*25*24*9*8')
					('0:04:18', u'9*9*26*26*26*9*9')
					('0:07:31', u'(9^4)*(26^3)')
	part2_correct_attempt
					['1 day, 22:32:57', u'(10^4)*(26^3)']

4 Student ID:jguanzho

	first_attempt
					2015-10-02 07:48:21
	part1_correct_attempt
					['0:00:00', u'10*26']
	part2_incorrect_attempt
					('0:00:00', u'(9**4)*(26**3)')
	part2_correct_attempt
					['0:00:11', u'(10**4)*(26**3)']

5 Student ID:spw006

	first_attempt
					2015-10-04 01:15:42
	part1_correct_attempt
					['0:00:00', u'260']
	part2_incorrect_attempt
					('0:00:00', u'10^5*2^26')
	part2_correct_attempt
					['0:00:10', u'10^5*26^2']

6 Student ID:any027

	first_attempt
					2015-10-03 10:26:37
	part1_correct_attempt
					['0:00:00', u'260']
	part2_incorrect_attempt
					('0:00:37', u'10 + 10 + 26 + 26 + 10 + 10 + 10')
	part2_correct_attempt
					['0:02:24', u'10 * 10 * 26 * 26 * 10 * 10 * 10']

7 Student ID:dkurli

	first_attempt
					2015-10-07 17:32:49
	part1_correct_attempt
					['0:00:00', u'10*26']
	part2_incorrect_attempt
					('0:00:00', u'26^3*10^5')
	part2_correct_attempt
					['0:00:20', u'26^3*10^4']

8 Student ID:agoldsht

	first_attempt
					2015-10-06 22:36:56
	part1_correct_attempt
					['0:00:00', u'260']
	part2_incorrect_attempt
					('0:00:00', u'20*26*26*30')
	part2_correct_attempt
					['0:03:07', u'100*26*26*100*10']

9 Student ID:jmiclat

	first_attempt
					2015-10-07 23:29:55
	part1_correct_attempt
					['0:00:00', u'260']
	part2_incorrect_attempt
					('0:00:00', u'26*26*26*10*10*10')
	part2_correct_attempt
					['0:00:23', u'10*10*26*26*10*10*10']

10 Student ID:v4zhang

	first_attempt
					2015-10-08 07:34:53
	part1_correct_attempt
					['0:00:00', u'260']
	part2_incorrect_attempt
					('0:03:15', u'9*9*26*26*26*9*9')
					('0:58:47', u'2600+126')
	part2_correct_attempt
					['1:11:23', u'(26^3) * (10^4)']

11 Student ID:jnatale

	first_attempt
					2015-10-08 00:06:33
	part1_correct_attempt
					['0:00:00', u'10*26']
	part2_incorrect_attempt
					('0:00:36', u'2*3*2')
	part2_correct_attempt
					['0:01:51', u'10*10*26*26*26*10*10']

12 Student ID:ganajera

	first_attempt
					2015-10-03 17:54:44
	part1_correct_attempt
					['0:00:00', u'10*26']
	part2_incorrect_attempt
					('0:00:00', u'10*10*10*10*26*26*26*26')
	part2_correct_attempt
					['0:00:13', u'10*10*10*10*26*26*26']

13 Student ID:acs008

	first_attempt
					2015-10-02 23:23:43
	part1_correct_attempt
					['0:00:00', u'260']
	part2_incorrect_attempt
					('0:37:03', u'10*10*26*10*26')
	part2_correct_attempt
					['0:37:20', u'10*10*26*10*26*10*10']

14 Student ID:v3doan

	first_attempt
					2015-10-03 23:56:31
	part1_correct_attempt
					['0:00:00', u'26 * 10']
	part2_incorrect_attempt
					('0:00:00', u'10 * 10 * 26 * 26 * 10 * 10')
	part2_correct_attempt
					['0:00:10', u'10 * 10 * 26 * 26 * 26 * 10 * 10']

15 Student ID:skodigal

	first_attempt
					2015-10-07 05:15:25
	part1_correct_attempt
					['0:00:00', u'260']
	part2_incorrect_attempt
					('0:00:00', u'26^3 * 10^3')
	part2_correct_attempt
					['0:00:19', u'26^3 * 10^4']

16 Student ID:hachrist

	first_attempt
					2015-10-02 19:41:28
	part1_correct_attempt
					['0:00:00', u'260']
	part2_incorrect_attempt
					('0:00:43', u'26*26*10*10*10*10')
	part2_correct_attempt
					['2 days, 1:57:17', u'175760000']

17 Student ID:kew017

	first_attempt
					2015-10-04 19:18:54
	part1_correct_attempt
					['0:00:00', u'10*26']
	part2_incorrect_attempt
					('0:00:00', u'2*3*2*6')
					('0:00:48', u'10^2*26^3*10^2*3!')
	part2_correct_attempt
					['0:02:21', u'10^2*26^3*10^2']

18 Student ID:yeh013

	first_attempt
					2015-10-08 08:15:01
	part1_correct_attempt
					['0:00:00', u'260']
	part2_incorrect_attempt
					('0:00:00', u'(26!*8100)/3!')
	part2_correct_attempt
					['0:03:39', u'175760000']

19 Student ID:wcwhite

	first_attempt
					2015-10-06 18:37:19
	part1_correct_attempt
					['0:00:00', u'10*26']
	part2_incorrect_attempt
					('0:04:39', u'2!*3!*2!')
					('0:05:35', u'2*10+3*26+2*10')
					('0:05:44', u'2*10*3*26*2*10')
	part2_correct_attempt
					['0:06:47', u'10*10*26*26*26*10*10']

20 Student ID:kmc012

	first_attempt
					2015-10-05 05:58:18
	part1_correct_attempt
					['0:00:00', u'260']
	part2_incorrect_attempt
					('0:00:00', u'2!3!2!')
	part2_correct_attempt
					['0:00:49', u'100*26*26*26*100']

21 Student ID:cprafull

	first_attempt
					2015-10-06 19:05:34
	part1_correct_attempt
					['0:00:00', u'10*26']
	part2_incorrect_attempt
					('0:00:56', u'10*10*25*25*25*10*10')
	part2_correct_attempt
					['0:01:09', u'10*10*26*26*26*10*10']

22 Student ID:dando

	first_attempt
					2015-10-04 19:48:18
	part1_correct_attempt
					['0:00:00', u'10 * 26']
	part2_incorrect_attempt
					('0:00:00', u'10 * 9 * 26 * 25 * 8 * 7 * 6')
	part2_correct_attempt
					['0:01:22', u'10 * 10 * 26 * 26 * 10 * 10 * 10']

23 Student ID:bakang

	first_attempt
					2015-10-08 02:47:31
	part1_correct_attempt
					['0:00:00', u'10*26']
	part2_incorrect_attempt
					('0:00:00', u'3*10*2*26')
					('0:00:26', u'5*10*2*26')
	part2_correct_attempt
					['0:01:22', u'(10^5)*(26^2)']

24 Student ID:jdeon

	first_attempt
					2015-10-03 19:34:19
	part1_correct_attempt
					['0:00:00', u'260']
	part2_incorrect_attempt
					('0:01:15', u'10*26*10')
	part2_correct_attempt
					['0:01:45', u'10*10*26*26*1000']

25 Student ID:ssamudra

	first_attempt
					2015-10-08 07:33:24
	part1_correct_attempt
					['0:00:00', u'10 * 26']
	part2_incorrect_attempt
					('0:00:13', u'10 * 26 * 10 * 10 * 10* 10')
					('0:03:13', u'10 * 26 * 10 * 10 * 10* 10 * 3')
					('0:08:37', u'10*26*9*10*9*8')
	part2_correct_attempt
					['0:09:02', u'10*26*10*10*10*10*26']

26 Student ID:jtfrankl

	first_attempt
					2015-10-07 23:30:31
	part1_correct_attempt
					['0:00:00', u'10*26']
	part2_incorrect_attempt
					('0:03:00', u'2*10*2*26*3*10')
	part2_correct_attempt
					['0:04:24', u'10*10*26*26*10*10*10']

27 Student ID:csl030

	first_attempt
					2015-10-04 21:28:35
	part1_correct_attempt
					['0:00:00', u'10 * 26']
	part2_incorrect_attempt
					('0:00:00', u'10^4 * 26 ^ 2')
	part2_correct_attempt
					['0:00:30', u'10^2 * 26 ^ 3 * 10^2']

28 Student ID:ralhadda

	first_attempt
					2015-10-08 16:53:11
	part1_correct_attempt
					['0:00:00', u'260']
	part2_incorrect_attempt
					('0:05:25', u' 126360000')
					('0:06:36', u' 32760000')
					('0:07:03', u' 78624000')
					('0:07:35', u' 1010880000')
					('0:10:46', u' 49400000')
					('0:11:35', u' 46124000')

29 Student ID:dcastlem

	first_attempt
					2015-10-03 21:08:39
	part1_correct_attempt
					['0:00:00', u'260']
	part2_incorrect_attempt
					('0:08:14', u'20*26*10')
					('4 days, 5:45:08', u'10^2*26*3*10')
	part2_correct_attempt
					['4 days, 5:45:31', u'10^2*26^3*10^2']

30 Student ID:ajvanega

	first_attempt
					2015-10-02 18:00:31
	part1_correct_attempt
					['0:00:00', u'26*10']
	part2_incorrect_attempt
					('0:05:40', u'10*26*10')
	part2_correct_attempt
					['0:06:21', u'10*10*26*26*1000']

31 Student ID:m8woo

	first_attempt
					2015-10-08 20:34:18
	part1_correct_attempt
					['0:00:00', u'260']
	part2_incorrect_attempt
					('0:00:00', u'1000*26^3')
	part2_correct_attempt
					['0:00:08', u'10000*26^3']

32 Student ID:sthapa

	first_attempt
					2015-10-06 06:14:34
	part1_correct_attempt
					['0:00:00', u'260']
	part2_incorrect_attempt
					('0:04:06', u'2*3*2*2')
					('0:04:27', u'2*(10)*3*2*26*2*10')
	part2_correct_attempt
					['0:12:25', u'26^3*10^4']

33 Student ID:asp025

	first_attempt
					2015-10-08 15:47:31
	part1_correct_attempt
					['0:00:00', u'10*26']
	part2_incorrect_attempt
					('0:02:48', u'(10^5)*(10^2)')
	part2_correct_attempt
					['0:03:02', u'(10^5)*(26^2)']












