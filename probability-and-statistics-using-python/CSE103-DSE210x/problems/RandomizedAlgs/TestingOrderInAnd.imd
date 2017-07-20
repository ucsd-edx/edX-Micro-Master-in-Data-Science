```python
# random variables (no need to import random library)
N=random.randrange(3,10,1);
T=random.randrange(1,N-1,1);
F=N-T;

# Solutions with variables converted to string
# Make sure you name the solution with part id at the end. e.g. 'solution1' will be solution for part 1. 
solution1 = "1"
solution2 = "1"
solution3 = "2"
solution4 = "2"
solution5 = "2"
solution6 = "1.5"
solution7 = "1"
solution8 = "1.5"
solution9 = "2"
solution10 = "1.5"


# Group all solutions into a list
solutions = [solution1, solution2, solution3, solution4, solution5, solution6, solution7, solution8, solution9, solution10]


```

#### Order Of Evaluation ####

Suppose C1,C2 are boolean variables and that A equal to their conjunction:

A= C1 and C2

Our goal is to evaluate A by checking the smallest number of C's.

Because this is a conjunction, it is enough to find one variable that is false to make A false. Therefor a good technique is to check the two variables one after the other and stop early if the variable is false.

However, we don't know what the values of the C's are until we check them. This is a situation in which randomization can help.

We will contrast two methods:

* **Deterministic Method:** Check C1, if True, check C2


* **Randomized Method:** Chose C1 or C2 at random, by flipping a fair coin. If the chosen variable is True, check the other.

Lets compare how many checks need to be done in difference situations:

* **C1=False, C2=False **
    - The Deterministic method will require checks:
    
    [_]

    - The expected number of checks of the randomized method is: 
 
    [_]

* **C1=True, C2=True **
    - The Deterministic method will require checks:
    
    [_]

    - The expected number of checks of the randomized method is: 
     
    [_]

* **C1=True, C2=False **
    - The Deterministic method will require checks:
    
    [_]

    - The expected number of checks of the randomized method is: 
    
    [_]

* **C1=False, C2=True **
    - The Deterministic method will require checks
    
    [_]

    - The expected number of checks of the randomized method is 
     
    [_]


* **If we are interested in the worst case (the worst performance over the 4 choices above) we find that **
    - The Deterministic method will require how many checks in the worst case?
    
    [_]

    - The expected number of checks of the randomized method in the worst case is: 
     
    [_]



---
