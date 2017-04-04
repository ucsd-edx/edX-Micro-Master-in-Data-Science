```python
# random variables (no need to import random library)
variable_values = {'n':[20,30,40]}
index_of_test_value = 2

k = random.randrange(3, 5)
p = (k - 1) / k

# Solutions with variables converted to string
# Make sure you name the solution with part id at the end. e.g. 'solution1' will be solution for part 1. 
solution1 = "20"
solution2 = "n"
solution3 = "1"
solution4 = "n/2"



# Group all solutions into a list
solutions = [solution1, solution2, solution3, solution4]


```



#### Average query time ####
Assume \\\(n\\\) items are hashed to \\\(n\\\) locations.
Suppose query \\\(q\\\) is picked at random, so that it is equally likely to hash to any of the locations \\\(1,2,\\ldots, n\\\). What is the expected query time?


\\\[ 
\\mbox{Expected query time}
\\ = \\
\\sum_{i=1}^n \\Pr(\\mbox{$q$ hashes to location $i$}) \\cdot \\mbox{(length of list at $T[i]$)}
\\\] 
\\\[ = \\frac{1}{n} \\sum_i  \\mbox{(length of list at $T[i]$)} 
\\ = \\frac{1}{n} \\cdot n \\ = \\ 1
\\\]

So the average query time is constant!

#### Worst case query time, and a balls-in-bins problem ####

What is the worst case query time; that is, what is the length of the longest linked list in \\\(T\\\)? Equivalently, when you throw \\\(n\\\) balls in \\\(n\\\) bins, what is the size of the largest bin? We'll see that with very high probability, no bin gets \\\(\\geq \\log n\\\) balls.

For any bin \\\(i\\\), let \\\(E_i\\\) be the event that it gets \\\(\\geq \\log n\\\) balls.


\\\[ \\Pr(E_i) \\  \\leq \\ {n \\choose \\log n} \\left( \\frac{1}{n} \\right)^{\log n} \\\]


(Do you see why? Because we want to select \\\(\\log n\\\) balls to go into bin \\\(i\\\), but do not care where the other balls go.)

To upper bound this probability we use the inequality (see cheat sheet) that

\\\[
{n \\choose k} \\leq \\left( \\frac{ne}{k} \\right)^k
\\\]


Applying this inequality we get:


\\\[
{n \\choose \\log n} \\left( \\frac{1}{n} \\right)^{\\log n} \\leq
\\left( \\frac{ne}{n \\log n}  \\right)^{\\log n} = 
\\left( \\frac{e}{\\log n}  \\right)^{\\log n} = 
\\frac{n^{\\log e}}{(\\log n)^{\\log n}} \\leq \\frac{1}{n^2}
\\\]


Where the last inequality can be shown by taking the log of both sides:


\\\[
\\log{\\frac{n^{\\log e}}{(\\log n) ^{\\log n}}}\\\] 
\\\[=\\log \\left(n^{\\log e} \\right) - \\log \\left[(\\log n)^{\\log n}\\right]
\\\]
\\\[
= \\log e~\\log n - \\log n ~\\log\\log n\\\] 
\\\[= \\log n~ (\\log e - \\log\\log n) \\le -2\\log n
\\\]

or equivalently
\\\[\\log \\log n \\ge 2+\\log e\\\]
which holds when \\\(n>2000\\\).

Having shown that \\\(\\Pr(E_i) \\leq 1/n^2\\\), it follows that


\\\[ \\Pr(\\mbox{some bin gets $\\geq \\log n$ balls}) = 
\\Pr(E_1 \\cup E_2 \\cup \\cdots \\cup E_n)\\\]
\\\[ \\Pr(E_1 \\cup E_2 \\cup \\cdots \\cup E_n) \\leq 
\\Pr(E_1) + \\cdots + \\Pr(E_n)
\\ \\leq \\frac{1}{n}.
\\\]


For instance, if you throw a million balls into a million bins, then the chance that
there is a bin with at least how many (round to integer) balls is at most 1 in a million?

[_]

Getting back to hashing, this means that for \\\(n\\\) elements, the worst case query time (with probability as high as \\\(1-1/n\\\) is \\\(O(?)\\\)

[_]

(answer in terms of \\\(n\\\), you can use \\\("log"\\\) in the answer, but not \\\("log2"\\\) although they are equivalent in big-O notation)


Suppose we already hashed \\\(n\\\) elements, and bucket 1 gets half of them.

What is the expected search time for a new element, \\\(O(?)\\\)

[_]

What is the worst search time? Notice that this scenario is a rare one. \\\(O(?)\\\)

[_]

 (answer in terms of \\\(n\\\))