# CSE255 Homework 2 - Scalable assignment

This repository contains the homework assignment 2 for the CSE 255 class and corresponding grader that works with edX XQueue.

## Structure

* `assignment/`: The homework assignment that will be distributed to students
* `deploy/`: Bootstrap scripts for launching Spark cluster for this assignment using the Spark Notebook software
* `grader/`
    - `grader/input/`: the file paths to the input files of different sizes
    - `grader/grade.py`: the grader entrance
    - `grader/spark_grader.py`: the actual grader class that works with XQueue-watcher
    - `grader/spark-grader.yml`: configurations for the grader

## Usage

To use the grader, please install all dependencies:

```bash
pip install -r grader/requirements.txt
```

After that, start as many Spark clusters as needed using [Spark Notebook](github.com/mas-dse/spark-notebook).
Spark Notebook support using custom bootstrap code, for which please provide `deploy/s3hook.sh`,
and set $PUBLIC_KEY to the public key value of the server that the grader will be running on.

Finally, set the server head node URLs in `grader/spark-grader.yml`.

### Switch between different input sizes

There are four problems in this assignment, each for a different input file size:

* twitter-10mb
* twitter-1gb
* twitter-10gb
* twitter-100gb

Their only differences are the input file size.

### Other settings

The grader supports setting timeout for running the student's submission
in `spark-grader.yml`.
The time unit of the timeout parameter is second.
If the student's program does not terminate within the specified time frame,
it will be forced exited and a TIME_OUT error would be returned.




## Grading

A score of 10 is assigned to a submission if

* it is a valid Jupyter notebook;
* it can be converted to a Python file using `jupyter convert`;
* the python file does not contain any syntax error;
* the python program exits before timeout happens;
* the output of the program matches our solution.

The matching between the output and our solution is
a line by line comparison procedure.
Any empty line would be ignored.
The comparison is determined to be matched if and only if all non-empty lines are identical.


## Scaling

In any given time, there can be at most one program running on the Spark cluster.
To scale up the grader, a new cluster should be launched using
the [Spark Notebook](https://github.com/mas-dse/spark-notebook).
Once the cluster is up, simply append its master URL to `spark-grader.yml`.
The grader will always choose the first free Spark cluster to send a submission
for grading.

### Credentials

The grader uses `ssh` to submit jobs to the Spark clusters.
Therefore, the Spark clusters must know the public key of the server
that the grader is running on.
To achieve that, please set the `$PUBLIC_KEY` variable in the `deploy/s3hook.sh`
accordingly.
