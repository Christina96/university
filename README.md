# Some of the University's assignments

Here you can find some of my university assignments. 


## Python assignments

They are from course **Algorithms and Data Structures** writted by [Panos Louridas](https://github.com/louridas), *Department of Management Science and Technology*, Athens University of Economics and Business. 

### Assignment: Find networks in a graph

You can find the assignment [here](https://github.com/dmst-algorithms-course/assignment-2016-1).

The program read a file from command prompt like
`python trusses.py graph_file size_of_trusses`
creates a dictionary with the parts of file and finds the trusses between neighbors.

* The `graph_file` in the form:

```
0 2
1 3 
2 4
...
```
 If numbers are `x` `y` the graph will have a link between the nodes.
* The `size_of_trusses` is the size of networks.


**Example:** For the file [barabasi_albert_graph_1500.txt](barabasi_albert_graph_1500.txt) 
`python trusses.py barabasi_albert_graph_1500.txt 4` the output is:

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

### Assignment: Assembling Genome

You can find the assignment [here](https://github.com/dmst-algorithms-course/assignment-2016-2).

The program read a file from command prompt like
`python dna_assembly.py fragments_file`
creates a dictionary with the fragments and finds the  synthesis of a
chain of unknown DNA.

* The `fragments_file` in the form:

```
ATG
GTG
TGG
GGC
GCG
CGT
GCA
TGC
CAA
AAT
ATG
AAT
...
```
**Example:** For the file [fragment_file.txt](fragment_file.txt)
`python dna_assembly.py fragments_file.txt` the output is: 
```
CTCGGACGAGATCACTGGTCTAC
```
If someone try to solve the assignment there is a case to have different output like:

```
GACTACCTGGTCTCGATCACGGA
```
or:

```
CGGTCACTCTGGACCTACGAGAT
```
or:

```
TACTCGGACGAGATCACCTGGTC
```
If you want to verify your result you can create a function that:

* Checks if all the fragments present in the input file exist in the final result.
* All the fragments from the final sequence exists in the input file.

**More information:**

* Phillip E. C. Compeau, Pavel A. Pevzner, and Glenn Tesler, How to apply de Bruijn graphs to genome assembly, Nature Biotechnology, Vol. 29, no. 11, November 2011 (http://www.nature.com/nbt/journal/v29/n11/full/nbt.2023.html).
* Pavel A. Pevzner, Haixu Tang, and Michael S. Waterman, An Eulerian path approach to DNA fragment assembly, Proceedings of the National Academy of Sciences (PNAS), Vol. 18, no. 17, August 14, 2001 (http://www.pnas.org/content/98/17/9748.long).








