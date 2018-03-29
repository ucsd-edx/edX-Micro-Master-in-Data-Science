This directory shall contain all the Homework Programming Assignments for CSE 255 | DSE 230 for Spring 2018

Since grading is managed by nbgrader, an example directory structure is as follows:

```
course101/
├── gradebook.db
├── nbgrader_config.py
├── source
│   ├── header.ipynb
│   └── ps1
│       ├── jupyter.png
│       ├── problem1.ipynb
│       └── problem2.ipynb
├── release
│   └── ps1
│       ├── jupyter.png
│       ├── problem1.ipynb
│       └── problem2.ipynb
├── submitted
│   ├── bitdiddle \\studentID
│   │   └── ps1
│   │       ├── jupyter.png
│   │       ├── problem1.ipynb
│   │       ├── problem2.ipynb
│   │       └── timestamp.txt
│   └── hacker \\studentID
│       └── ps1
│           ├── jupyter.png
│           ├── problem1.ipynb
│           ├── problem2.ipynb
│           └── timestamp.txt
├── autograded/
└── feedback/
```
More on this here: http://nbgrader.readthedocs.io/en/stable/user_guide/philosophy.html

Specifically:
1. The "source" will have the base notebook with all test cases (hidden and visible). It is here that we define which cells are to be modified by students, which aren't. Also, here we give marks to each question.
2. Next, nbgrader generates a student copy of the assignment, in the "release" folder.
3. Students' submissions are received in the "submitted" directory.
4. The autograded notebooks will be present in the "autograded" directory.
