## Directions for running HWs

Refer this: https://docs.google.com/document/d/1J3PoGcJhcEORUoU7I4UMLocQzIHz7b2dZyJMmpxDCEQ/edit#heading=h.14a8l423o7a9

The directions in this file are intended for Vocareum. Vocareum will use them to create the infrastructure needed to run and grade HW assignments for DSE230x on edX.

Please give all of the information that they would need. They probably will not use our code, but I (@Yoav) will ask them to closely imitate how the TAs interact with the HW systems.

There are two types of HW: Scaled and unscaled, or "small"

### Unscaled HW

Small, uses nbgrader, has two modes of submissions.

@Jayanth, please explain:

1. What are the files that need to be prepared by the TA and how they are organized in the nbgrader. (point to HW1 example on github)
2. How the nbgrader instance is started and how it interacts with xQueue. Point to code on github.

### Scaled HW

Large, uses multiple spark clusters

@Jayanth, @ Julaiti, please explain:

1. What are the files that need to be prepared by the TA (point to HW2 example on github)
2. How the Queue watcher is started, how the cluster is created and how edX, xQueue, the watcher and the cluster interact. (point to the spark-notebook github and to an example of the bootstrap files and data files used).



### Desired improvements
1. For scaled HW, run the queue watcher on the head node of the cluster.
2. For scaled HW, use spark-submit on both the user computer and on the Yarn cluster.  Append at the beginning a line to start the sparkCluster (unless it already exists) to ensure that yarn, rather than local server, is used.


