##Week2

	Assigned problem file name:
   	+--------+------------+---------------------------------------------+
   	| set_id | problem_id | source_file                                 |
   	+--------+------------+---------------------------------------------+
   	| Week2  |          1 | Reorganized/Sets/BasicSets_1.pg             |
   	| Week2  |          2 | Reorganized/Sets/q2.pg                      |
   	| Week2  |          3 | Reorganized/Sets/BasicSets1.pg              |
   	| Week2  |          4 | Reorganized/Sets/ClassSize.pg               |
   	| Week2  |          5 | Reorganized/Combinatorics/p10.pg            |
   	| Week2  |          6 | Reorganized/Combinatorics/sw10_2_14_PGML.pg |
   	| Week2  |          8 | Reorganized/Combinatorics/p12.pg            |
   	| Week2  |          9 | Reorganized/Combinatorics/sw10_1_21_pgml.pg |
   	| Week2  |         10 | Reorganized/Combinatorics/sw10_2_52.pg      |
   	| Week2  |         11 | Reorganized/UniformDiscrete/UniformDist.pg  |
   	| Week2  |         12 | Reorganized/UniformDiscrete/UniformDist3.pg |
   	| Week2  |         13 | Reorganized/Combinatorics/coinProblems.pg   |
   	| Week2  |         14 | local/Reorganized/Combinatorics/p13.pg      |
   	+--------+------------+---------------------------------------------+


### Sorted with number of attempts
[problem 13](https://github.com/cse103/Attempt_Analysis/blob/master/clustering_code/clusters/Week2/md_files/Week2_13_clusters.md): 2248

		 part  1 :  367
		 part  2 :  426
		 part  3 :  204
		 part  4 :  678
		 part  5 :  573


[problem 14](https://github.com/cse103/Attempt_Analysis/blob/master/clustering_code/clusters/Week2/md_files/Week2_14_clusters.md): 1065

		 part  1 :  159
		 part  2 :  63
		 part  3 :  843


[problem 10](https://github.com/cse103/Attempt_Analysis/blob/master/clustering_code/clusters/Week2/md_files/Week2_10_clusters.md): 861

		 part  1 :  500
		 part  2 :  361


problem 8（Incomplete）: 860

		 part  1 :  119
		 part  2 :  180
		 part  3 :  561


problem 2（Set Problem): 742

		 part  1 :  220
		 part  2 :  233
		 part  3 :  289


problem 3（Set Problem): 661

		 part  1 :  98
		 part  2 :  60
		 part  3 :  50
		 part  4 :  130
		 part  5 :  103
		 part  6 :  110
		 part  7 :  52
		 part  8 :  58


[problem 9](https://github.com/cse103/Attempt_Analysis/blob/master/clustering_code/clusters/Week2/md_files/Week2_9_clusters.md): 310

		 part  1 :  111
		 part  2 :  199


[problem 11](https://github.com/cse103/Attempt_Analysis/blob/master/clustering_code/clusters/Week2/md_files/Week2_11_clusters.md): 263

		 part  1 :  142
		 part  2 :  74
		 part  3 :  47


problem 4（Set Problem): 138

		 part  1 :  4
		 part  2 :  2
		 part  3 :  78
		 part  4 :  54


problem 1（Set Problem): 97

		 part  1 :  39
		 part  2 :  58


[problem 6](https://github.com/cse103/Attempt_Analysis/blob/master/clustering_code/clusters/Week2/md_files/Week2_6_clusters.md): 88

		 part  1 :  47
		 part  2 :  41


[problem 5](https://github.com/cse103/Attempt_Analysis/blob/master/clustering_code/clusters/Week2/md_files/Week2_5_clusters.md): 78

		 part  1 :  37
		 part  2 :  41


[problem 12](https://github.com/cse103/Attempt_Analysis/blob/master/clustering_code/clusters/Week2/md_files/Week2_12_clusters.md): 31

		 part  1 :  12
		 part  2 :  19


### Problem Content



Problem 1

		$min = random(3,6,1);
		$max = random(10,16,1);
		@rng = ($min..$max);
		$rs = Set(join(",",@rng));
		$S = Set(3,5,7,9,11,13,15);
		$A = $rs->intersect($S);
		$Ac = Set(1,2,3,4,5,6);

		######################################################################
		BEGIN_PGML

		##Mathematical Preliminaries##

		Probability theory is about sets. In the first lesson you encountered
		the set of possible outcomes of flipping two coins which contains four
		elements. If we use [`H`] to denote "Heads" and [`T`] to denote
		"Tails" then the set of possible outcomes, also known as the
		_outcome space_ contains four elements: [`\{(H,H),(H,T),(T,H),(T,T)\}`]. We say
		that the outcome space is the set of four _tuples_ . As the
		concepts of "set" and "tuple" will be used many times throughout
		the course, we take some pains to define these concepts and the
		associated notation, in a somewhat formal mathematical way.

		#### Sets ####
		*Sets* are collections of _elements_ .
		We will mostly consider sets of numbers, but elements can be most anything.

		A set can be specified by listing its elements between braces, as in

		o The possible outcomes of the roll of a six sided die: [`A= \{1,2,3,4,5,6\}`]
		o The positive integers: [`\mathbb{Z}^+= \{1,2,\ldots\}`]
		o The possible outcomes of the flip of a coin: [`C= \{ H,T \}`]

		We say that [`5`] is an element of [`A`] and denote it by [`5 \in A`]. Sets
		are _unordered_ collections, in other words [`\{1,2,3,4,5,6\} =
		\{5,2,1,3,4,6\}`]. The number of times an element can appear in a set
		is either 0 or 1, *an element  cannot appear multiple times
		in the set*. For that there is a different construct called *bags* which we shall not use in this course.

		Write the set [`A`] given above as the possible outcomes of the roll of a six-sided die. (Separate the elements using commas and surround the list with curly braces as in the examples above.)
		[______]{$Ac}

		What is the set of odd numbers that are larger than [$min-1] and smaller than [$max+1]?
		Answer = [______]{$A}

Problem 2

		BEGIN_PGML

		### Union, Intersection, and Complements for Sets of Countries ###
		Suppose A = {'China','France','Egypt','US'}, B = {x | x is a country in Asia}, C = {x | x is a country not in Europe}.

		In the answer, use the numbers {0,1,2,3} to represent the four countries {'China','France','Egypt','US'}. In other words {'China'}={0}, {'France','US'}={1,3}.

		a. What is the set [`A \cap B`]? The intersection of two sets is the set of elements in both A and B. The set of countries in A that are also in Asia is [_______]{Set(0)}

		b. What is the set [`A \cap C^c`]? The complement of C is the entire outcome space excluding the elements in C. The outcome space here is the set of all countries, and excluding all countries in C, namely non-European countries, we know [`C^c`] means all European countries. When we take its intersection with A, we get [________]{Set(1)}

		c. What is the set [`A \cap (B \cup C)`]? The union of two sets is the set formed by all the elements in both sets. [`B \cup C`] means all countries that are in Asia OR not in Europe. Note that all countries in Asia are not in Europe, which means each element in B is in C, so [`B \subset C`]. In this case, [`B \cup C = C`]. The intersection of this set with A is therefore [_________________]{Set(0,2,3)}

Problem 3

		$isProfessor = ($studentLogin eq 'yoav.freund' || $studentLogin eq 'professor');
		Context("Interval");
		$showPartialCorrectAnswers = 1; # show student the correct part of their answer.

		@A_elements=NchooseK(10,8);
		$A=Set("{".join(",",@A_elements)."}");

		@B_elements=NchooseK(10,6);
		$B=Set("{".join(",",@B_elements)."}");

		@C_elements=NchooseK(10,7);
		$C=Set("{".join(",",@C_elements)."}");

		@Universe_elements=NchooseK(10,10);
		$Universe=Set("{".join(",",@Universe_elements)."}");

		$Ac=Set($Universe-$A);
		$Bc=Set($Universe-$B);
		$Cc=Set($Universe-$C);

		BEGIN_PGML

		### More Practice with Set Union, Intersection, Complement ###
		Let the outcome space be [`\{0,1,...9\}`], and define subsets of this outcome space [`A = [$A]`], [`B = [$B]`], and [`C = [$C]`].  Evaluate the following sets:

		o [`A^c`]?  [_________]{$Ac}
		o [`B^c`]?  [_________]{$Bc}
		o [`C^c`]?  [_________]{$Cc}
		o [`A^c \cup B^c`]? [__________]{Union($Ac,$Bc)}
		o [`A^c \cup B^c \cup C^c`]? [__________]{Union($Ac,$Bc,$Cc)}
		o [`(A^c \cup B^c \cup C^c)^c`]? [__________]{$Universe-Union($Ac,$Bc,$Cc)}

		Then evaluate the following sets:
		o [`A \cap B`]? [__________]{$A->intersect($B)}
		o [`A \cap B \cap C`]? [__________]{$A->intersect($B)->intersect($C)}

		### De Morgan's Law for Sets ###
		Notice something?  [`(A^c \cup B^c \cup C^c)^c = A \cap B \cap C`]!  

		This is not a coincidence.  There is a more general underlying fact that holds for sets, and an analogous version for boolean logic.  
		For any sets [`S_1,S_2,...S_n`], [`(S_1^c \cup S_2^c \cup ...S_n^c)^c = S_1 \cap S_2 ...S_n`]

		Likewise, [`(S_1^c \cap S_2^c \cap ...S_n^c)^c = S_1 \cup S_2 ...S_n`]

Problem 4

		#$Prod=List([List(["R",0]),List(["R",1])]);
		#$L = Compute("(R,0),(R,1),(G,0),(G,1),(B,0),(B,1)");
		$L=List("(R,0),(R,1),(G,0),(G,1),(B,0),(B,1)");
		$L ->{open} = "{";
		$L ->{close} = "}";
		$L ->{requireParenMatch}=0;

		$R=random(10,30,1);
		$K=random(2,6,1);
		$N=int($R/$K);

		TEXT(PGML::Format2(<<'END_PGML'));

		## The size of a set ##

		The _size_ of a set [`A`] is the number of elements in it and is denoted
		by [`|A|`]  

		Thus [`|\{H,T\}|=2`],  [`|\emptyset|=0`] and [`|\mathbb{Z}^+|=\infty`]

		#### Problem ####

		1.   What is the size of the set [`\{R,G,B\}`]? [___]{3}
		2.   What is the size of the set [`\{0,1\}`]? [___]{2}
		3.   What is the size of the set [` \{0,1,2,3\} \cap \{0,2,4,6,8,10\} `]? [___]{2}
		4.   Let [`A`] be the set of integers between 1 and [$R]. Let [`B`] be the set of integers divisible by [$K].  What is the size of [`A \cap B`] is [___]{$N}?


Problem 5

    $a = random(10,14,1);
    $n = random(2,5,1);
    $b = $a * 2 * $n;

    1. For lunch, I can eat one sandwich and a piece of fruit. I can choose between veggie, chicken, and beef sandwiches; and between an orange and an apple. How many different lunch combinations can I have?
    Your answer is: [______]{Compute("3*2")}

    2. A particular brand of shirt comes in [$a] colors, has a male
    version and a female version, and comes in [$n] sizes for each sex.
    How many different types of this shirt are made?
    Your answer is: [______]{Compute("$a * 2 * $n")}


Problem 6

    $a=random(4,9,1);

    1. How many strings of letters can be formed by rearranging the letters "CAB"? (Order matters.)
    Your answer is : [________________]{fact(3)}

    2. A pianist plans to play [$a] different pieces at a recital. In how many ways can she
    arrange these pieces in the program?
    Your answer is : [________________]{fact($a)}


Problem 8

    $n2 = random(3,6,1);

    1. Roll two fair dice: a red die and a green die. How many different ways are there of getting at least one six?
    Your answer is: [_______]{Compute("36 - (5*5)")}

    2. How many strings of [$n2] lower case English letters are there that
    have
    the letter x in them somewhere? Here strings may use the same letter more
    than once.
    (Hint: It might be easier to first count the strings that don't have an
    x in them.)
    Your answer is: [_______]{Compute("26**$n2-25**$n2")}


Problem 9

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


Problem 10

    $a=random(48,55,1);

    1. Suppose we choose two *different* numbers, each from 1 to 5. If the order of the numbers is *not* important, how many different choices can we pick?
    [_______]{Compute("(5*4)/2")}

    2. In the "6/[$a]" lottery game, a player picks six numbers from 1 to [$a].
    How many different choices does the player have if repetition is not allowed?
    Note again that the order of the numbers is not important.
    Your answer is : [_______]{Compute("$a*($a-1)*($a-2)*($a-3)*($a-4)*($a-5)/(6*5*4*3*2)")}


Problem 11

    $R1=random(10,20,1); # size of instance space
    $R2=random(5,$R1,1); # size of event set.

    Suppose we have [$R1] cards, numbered 1,...,[$R1]. Suppose that when we pick a card at random the distribution of the card number is uniform. Let [`A`] be the event that number of the card that we picked is smaller or equal to [$R2]. What is the probability of the event [`A`]?

    o *Copy* the number of cards here: [_________]{$R1}
    o *Copy* the maximal card value in [`A`] here: [________]{$R2}
    o The probability of the event is equal to [__________________________]{Compute("$R2/$R1")}


Problem 12

    $Outcomes=Set("{1,2,3,4,5,6,7,8,9,10,11,12}");
    $Div2=Set("{2,4,6,8,10,12}");
    $Div3=Set("{3,6,9,12}");
    $Div6=Set("{6,12}");

    ## Cards ##
    o How many kings are in a standard deck of 52 cards? [_________]{4}
    o What is the probability a uniformly randomly chosen card from a standard deck of 52 cards is a king?
    [_________]{1/13}


Problem 13

    $coins=random(9,11,1); # number of tosses of the dice

    ## Tossing a coin ##
    A fair coin is tossed [$coins] times.
    o  There is a natural outcome space for the experiment of tossing coins in sequence, where the probability of each outcome is equally likely.  What is the size of this outcome space? [______]{Compute("2^$coins")}
    o  What is the size of the event set for getting exactly [$coins-1] heads?  [______]{Compute("$coins!/($coins-1)!")}
    o  What is the probability of getting exactly [$coins-1] heads? [_________]{Compute("($coins!/($coins-1)!)/2^$coins")}
    o  What is the probability of getting at most [$coins-1] heads? [________]{Compute("1-1/2^$coins")}
    o  What is the probability of getting exactly 6 heads?  [______________]{Compute("($coins!/(6!($coins-6)!))/2^$coins")}


Problem 14

    $n2 = random(3,6,1);

    Lower case English letters are from "a-z". The order matters here. For example, "ab" is a different string from "ba". Repetition is allowed, i.e. the same letter can occur multiple times in a string.
    1. How many strings of length [$n2] consisting of lower case English letters are there?  [__________]{Compute("26**$n2")}
    2. How many strings of length [$n2] consisting of lower case English letters, **excluding the letter "x"**, are there? [__________]{Compute("25**$n2")}
    3. How many strings of length [$n2] consisting of lower case English letters, **and including at least one "x"**, are there? [__________]{Compute("26**$n2-25**$n2")}
