### Input
1. out-degree list
format:
```
source-node-id   target-node-id    out-degree-of-source-node
```
example:
```
0 1 2
0 2 2
1 0 3 
1 2 3
1 3 3
2 0 2
2 1 2
3 1 1
```

```sh
// directed full-graph
$ python convert_outdegree.py ../../data/wiki/ 1 1
// directed train-graph
$ python convert_outdegree.py ../../data/wiki/ 1 0
// undirected full-graph
$ python convert_outdegree.py ../../data/wiki/ 0 1
// undirected train-graph
$ python convert_outdegree.py ../../data/wiki/ 0 0
```

2. in-degree list
format:
```
node-id   in-degree
```
example:
```
0 2
1 3
2 2
3 1
```

```sh
// directed full-graph
$ python convert_indegree.py ../../data/wiki/ 1 1
// directed train-graph
$ python convert_indegree.py ../../data/wiki/ 1 0
// undirected full-graph
$ python convert_indegree.py ../../data/wiki/ 0 1
// undirected train-graph
$ python convert_indegree.py ../../data/wiki/ 0 0
```

### Output
A binary double array with size:  number-of-nodes * embedding-dimensionality

### Functions
1. nrp.m :the node-reweighted PPR embedding algorithm, input arguments are: graph-data-name, if-it-is-full, if-it-is-directed, dimensionality, epoch-number
2. bksvd.m : the randomized SVD algorithm, input arguments are: the square matrix you wanna decompose, the low-rank, others as default
3. update_dw.m : the algorithm for updating forward/backward weights of directed graphs
4. update_uw.m : the algorithm for updating forward/backward weights of undirected graphs


### How to run
```sh
$ matlab -nodisplay -r "cd('.'); nrp('wiki', 0,  1, 128, 20, 10);exit"
```
Parameters: graph-name, full (1) or partial (0), directed (1) or undirected (0), embedding dimensionality, number of iterations for PPR approximation, number of iterations for learning weights. 
