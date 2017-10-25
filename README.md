# Some of the University's assignments

Here you can find some of my university assignments. 


## Python assignments

They first three assignments are from course **Algorithms and Data Structures** writted by [Panos Louridas](https://github.com/louridas), *Department of Management Science and Technology*, Athens University of Economics and Business. The assignment "Handshakes Graph Construction Problem" is from course **Social Network Analysis** written by Dionysios Sotiropoulos, *Department of Management Science and Technology*, Athens University of Economics and Business.


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


**Example:** For the file [barabasi_albert_graph_1500.txt](find_networks_in_a_graph/barabasi_albert_graph_1500.txt) 
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
**Example:** For the file [fragment_file.txt](assembling_genome/fragment_file.txt)
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

### Assignment: Musical Rhythms

You can find the assignment [here](https://github.com/dmst-algorithms-course/assignment-2016-3).

In this program user can work with Euclidean rhythms. User can do different things depending on the input.
The program read a file from command prompt like:
`musical_rythms.py [-s SLOTS] [-p PULSES] [-r RECOGNIZE] [-l LIST_RYTHMS]`

* If the user gives `-s SLOTS` and `-p PULSES` the program finds the rhythm that correspond to these parameters. `PULSES` is the number of hits and `SLOTS` the length of the rhythm. **For example:** 

```
python musical_rythms.py -s 12 -p 7
E(7,12) = [101101011010] = (2122122) It is a common West African bell pattern. For example, it is used in the Mpre rhythm of the Ashanti people of Ghana. Started on the seventh (last) onset, it is a Yoruba bell pattern of Nigeria, a Babenzele pattern of Central Africa, and a Mende pattern of Sierra Leone.
```

* If the user gives `-r RECOGNIZE` the `RECOGNIZE` is the rhtyhm in binary form and the program try to recognize if it is a Euclidean rhythm or not and print an appropriate message. **For Example:**

```
python musical_rythms.py -r 101101011010
E(7,12) = [101101011010] = (2122122) It is a common West African bell pattern. For example, it is used in the Mpre rhythm of the Ashanti people of Ghana. Started on the seventh (last) onset, it is a Yoruba bell pattern of Nigeria, a Babenzele pattern of Central Africa, and a Mende pattern of Sierra Leone.
```

```
python musical_rythms.py -r 10010010010
E(4,11) = [10010010010] = (3332) It is the metric pattern used by Frank Zappa in his piece titled Outside Now.
It is a reverse Euclidean string.
```

```
python musical_rythms.py -r 10010010011
Not a Euclidean rhythm.
```
* If the user gives `-l LIST_RYTHMS` the `LIST_RYTHMS` is the rhythm in binary form and the program finds all the rhythms with the same length, sorted by Hamming distance and serial number of pulses. **For example:**

```
python musical_rythms.py -l 101010100
Distance = 0
E(4,9) = [101010100] = (2223) It is the Aksak rhythm of Turkey. It is also the metric pattern used by Dave Brubeck in his piece Rondo a la Turk.
It is a Euclidean string.
Distance = 1
E(5,9) = [101010101] = (22221) It is a popular Arabic rhythm called Agsag-Samai. Started on the second onset, it is a drum pattern used by the Venda in South Africa, as well as a Rumanian folk-dance rhythm. It is also the rhythmic pattern of the Sigaktistos rhythm of Greece, and the Samai aktsak rhythm of Turkey. Started on the third onset, it is the rhythmic pattern of the Nawahiid rhythm of Turkey.
It is a reverse Euclidean string.
Distance = 2
E(2,9) = [100010000] = (45)
It is a Euclidean string.
Distance = 3
E(1,9) = [100000000] = (9)
Distance = 3
E(3,9) = [100100100] = (333)
Distance = 3
E(7,9) = [101110111] = (2112111) It is the Bazaragana rhythmic pattern of Greece.
It is a reverse Euclidean string.
Distance = 4
E(6,9) = [101101101] = (212121)
Distance = 4
E(8,9) = [101111111] = (21111111)
It is a reverse Euclidean string.
```

We assume that the user knows how the program works and doesn't make  wrong inputs.


**More information:**

* G.T. Toussaint, "The Euclidean algorithm generates traditional musical rhythms", in proceedings of BRIDGES: Mathematical Connections in Art, Music, and Science, Banff, Alberta, Canada, July 31 to August 3, 2005, pp. 47–56 ([http://cgm.cs.mcgill.ca/~godfried/publications/banff.pdf](http://cgm.cs.mcgill.ca/~godfried/publications/banff.pdf)).

* Erik D. Demaine, Francisco Gomez-Martin, Henk Meijer, David Rappaport, Perouz Taslakian, Godfried T. Toussaint, Terry Winograd, and David R. Wood, "The Distance Geometry of Music", Computational Geometry: Theory and Applications, volume 42, number 5, July 2009, pp. 429–454. Special issue of selected papers from the 17th Canadian Conference on Computational Geometry, 2005 ([http://erikdemaine.org/papers/DeepRhythms_CGTA/paper.pdf](http://erikdemaine.org/papers/DeepRhythms_CGTA/paper.pdf)).

* E.Bjorklund, "The Theory of Rep-Rate Pattern Generation in the SNS Timing System", SNS-NOTE-CNTRL-99, 1999 ([https://ics-web.sns.ornl.gov/timing/Rep-Rate%20Tech%20Note.pdf](https://ics-web.sns.ornl.gov/timing/Rep-Rate%20Tech%20Note.pdf)).

### Assignment: Handshakes Graph Construction Problem

The new president of the United States of America, Donald Trump, held a dinner just after his inauguration at the presidential office. The dinner was held at the White House in Honor of the governors of the 50 states who attended the dinner accompanied by their spouses while the recently elected president was accompanied by the first lady of the U.S, Melania Trump. 

At the end of the dinner, the president of the U.S. asked every single person that attended the dinner about the number of handshakes he/she gave including his spouse Melania. Given that he collected a list of different numbers of handshakes and that spouses didn’t
interchanged handshakes amongst themselves, can you derive an algorithm that:

**i.** Constructs a valid network of handshakes for the participants of the dinner. (Tip: The graph G = (V,E) to be constructed is one of the possible undirected graphs of |V| = 102 nodes in total. The graph is undirected in the sense that, if (vi ,vi) ε E --> (vj,vi) ε E. In other words, handshaking is a symmetric action.

**ii.** Identifies the 50 pairs of spouses by the number of handshakes that have been conducted by each person.

**iii.** Determines the number of handshakes conducted by Melania Trump.

**iv.** Draws the network of handshakes.

Your algorithm may be implemented by utilizing the Python programming language and the NetworkX module. Your code should be able to provide results for the generalized case where the number of governor-spouse pairs is k and, thus, the total number of nodes in the
graph is |V| = 2*(k+1). 

## Java assignments

They are from course **Software Engineering in Practice** writted by [Tushar Sharma](https://github.com/tushartushar) and [Antonios Gkortzis](https://github.com/AntonisGkortzis). The course is taught by [Diomidis Spinellis](https://github.com/dspinelliss), *Department of Management Science and Technology*, Athens University of Economics and Business. 

### Assignment: Design Patterns

#### Exercise 1
In the context of the SEiP course, there is a course, students, instructors and organizers. The course has a start time and end time. If any of the timing changes, the stakeholders have to be notified. The program notifies the stakeholders whenever the time changes for the course.

#### Exercise 2
The Utility class has to methods.   
* **readFile:** Reads a file and return the result in an ArrayList.
* **writeFile:** Writes a file with the text that takes.

#### Exercise 3
The program compute the following metrics for Java code:
* LOC (Lines of Code)
* Number of classes
* Number of methods 

by using regular expressions to calculate the aforementioned metrics and use the read & write methods from the Utility class created in Exercise 2.

#### Exercise 4
The program compute the following metrics for Java code:
* LOC (Lines of Code)
* Number of classes
* Number of methods

by using string comparison to calculate the aforementioned metrics. 

#### Exercise 5
Extend the program from Exercise 4 and implements a segregated interface to compute all the supported metrics. Write all he computed metrics to a CSV file.

