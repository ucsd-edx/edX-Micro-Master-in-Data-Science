## How to create and add hint

* Start by forking this repo.

* Go to ```2015data``` and in the corresponding week, look through the history data to fill in some hint in the hint table.

* Create your hint class in ```hint_class``` folder in the corresponding week.

* Make sure your hint class name is the **same** as your file name.

* Go to the ```hint_database``` directory

* Run test.py, you can run ```python test.py --help``` to see how to use test.py

```
python test.py <week_no> <problem_no> <part_no> <no of attempts tested> <name of hint filter(optional)>
```

If you only want to test one hint class, input the name of the hint class. Otherwise, it will run all hint classes inside the folder of the week.
for example:

```
python test.py 2 13 1 10 firstHint
```

* Read the output to make sure it is correct.

* Do a pull request
