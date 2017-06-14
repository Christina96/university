# Some of the University's assignments

Here you can find some of my university assignments. 


## Python assignments

They are from course **Algorithms and Data Structures** writted by [Panos Louridas](https://github.com/louridas), *Department of Management Science and Technology*, Athens University of Economics and Business. 

### Assignment: Find networks in a graph

You can find the assignment [here](https://github.com/dmst-algorithms-course/assignment-2016-1).

The program read a file from command prompt like
`python trusses.py graph_file size_of_trusses`
create a dictionary with the parts of file and finds the trusses between neighbors.

* The `graph_file` in the form:

```
0 2
1 3 
2 4
...
```
 If numbers are `x` `y` the graph will have a link between the nodes.
* The `size_of_trusses` is the size of networks.


Example: for the file [barabasi_albert_graph_1500.txt](barabasi_albert_graph_1500.txt) returns:

```
(0, 3, 4, 5)
(0, 3, 4, 5, 7, 9, 11, 15, 26)
(0, 3, 4, 5, 7, 11)
(0, 4, 7, 11)
(0, 9, 15, 26)
```

**More information:**

* Jonathan Cohen, Trusses: Cohesive Subgraphs for Social Network Analysis, 2008 (http://www.csee.ogi.edu/~zak/cs506-pslc/trusses.pdf).
* Jonathan Cohen, Graph Twiddling in a MapReduce World, Computers in Science and Engineering, Vol. 11, issue 4, pp. 29-41, July/August 2009 (http://lintool.github.io/UMD-courses/bigdata-2015-Spring/content/Cohen_2009.pdf).
