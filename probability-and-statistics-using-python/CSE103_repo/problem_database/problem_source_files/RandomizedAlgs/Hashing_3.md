```python
# random variables (no need to import random library)

# Solutions with variables converted to string
# Make sure you name the solution with part id at the end. e.g. 'solution1' will be solution for part 1. 
solution1 = "6"




# Group all solutions into a list
solutions = [solution1]


```




#### The power of two choices ####

Here's a variant on the balls and bins setup. As usual, you have before you a
row of \\\(n\\\) bins, along with a collection of \\\(n\\\) identical balls. But now,
when throwing each ball, _you pick two bins at random and you put the
ball in whichever of them is less full_.

It turns out, using an analysis that is too complicated to get into here, that
under this small change, the maximum bin size will be just \\\(O(\\log \\log n)\\\)
instead of \\\(O(\\log n)\\\).

This inspires an alternative hashing scheme:

1 Pick _two_ completely random functions \\\(h_1, h_2: U \\rightarrow {1,2,\\ldots, n}\\\).


2 Create a table \\\(T\\\) of size \\\(n\\\), each of whose entries is a pointer to a
linked list, initialized to null.


3 For each \\\(x_i\\\), store it in either the linked list at \\\(T[h_1(x_i)]\\\) or \\\(T[h_2(x_i)]\\\),
whichever is shorter.


4 Given a query \\\(q\\\), look through _both_ the linked list at \\\(T[h_1(q)]\\\) and
at \\\(T[h_2(q)]\\\) to see if it's there.


The storage requirement is still \\\(O(n)\\\), the average query time is still \\\(O(1)\\\), but now
the worst case query time drops to \\\(O(\\log \\log n)\\\).

What is the worst case query time for \\\(n = 2^{64}\\\), \\\(O(?)\\\)

[_]
