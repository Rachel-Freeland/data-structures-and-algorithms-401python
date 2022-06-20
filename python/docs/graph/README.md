# Graphs
A non-linear data structure that can be looked at as a collection of `vertices` (or `nodes`) potentially connected
by line segments named `edges`.

## Challenge
This is a new data structure implementation
* [Solution](/data_structures/graph.py)
* [Tests](/tests/data_structures/test_graph.py)

## Approach & Efficiency
This is an implementation of a graph represented by an adjacency list (a dictionary-like list, a hash table)
All operations are an O(1) for space and time due to the hash table like structure of the adjacency list.
## API
* `add_node(value)`:
  * adds a node to the graph
* `add_edge(start_vertex, end_vertex, weight)`:
  * adds a new edge between 2 nodes in the graph and, if specified, a
    weight can be added to that edge.
  * `NOTE:`The 2 nodes should already be in the graph
* `get_nodes()`:
  * returns all the nodes in the graph as a collection
* `get_neighbors(vertex)`:
  * returns all the edges in the graph as a collection
* `size()`:
  * gets the total number of nodes in the graph
