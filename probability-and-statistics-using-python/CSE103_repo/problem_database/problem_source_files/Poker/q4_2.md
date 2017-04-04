```python
ns = random.randrange(4,6,1)
nr = random.randrange(10,16,1)
n = ns*nr

solution1 = "C({0},2)".format(nr)
solution2 = "{0}-2".format(nr)
solution3 = "C({0},2)^2".format(ns)
solution4 = "{0}".format(ns)
solution5 = "C({1},2)*({1}-2)*(C({0},2)^2)*{0}".format(ns,nr)
solution6 = "C({1},2)*({1}-2)*(C({0},2)^2)*{1}/C({2},5)".format(ns,nr,n)

solutions = [solution1,solution2,solution3,solution4,solution5,solution6]  
```

### Two Pairs ###

*Remember, the deck you are using has $ns suits and $nr ranks.*

* The number of possibilities for the ranks of the two pairs is 

[_]

* The number of possibilities for the rank of the single is 

[_]

* The number of possibilities for the suits of the two pairs is 

[_]

* The number of possibilities for the suit of the single is 

[_]

* Thus the number of hands with exactly two pairs is 

[_]

* The ratio of this number to the number of all hands 

[_]
