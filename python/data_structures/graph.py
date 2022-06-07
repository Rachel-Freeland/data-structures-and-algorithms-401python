class Graph:
    """
    A non-linear data structure that can be looked at as a collection of vertices or nodes potentially connected by
    line segments called edges.
    """

    def __init__(self):
        self._adjacency_list = {}
        pass

    def add_node(self, value):
        """
        Arguments: a value -->
        Returns: the added node
        This method takes in a value and creates a node that is then, added to the graph.
        """
        vertex = Vertex(value)
        self._adjacency_list[vertex] = []
        return vertex

    def add_edge(self, start_vertex, end_vertex, weight=0):
        """
        Arguments: 2 nodes to be connected and,  the weight (optional) of that segment -->
        Returns: nothing -->
        Adds a new edge between 2 nodes in the graph. If specified, assigns a weight to the edge. Both nodes should
        already be in the graph.
        """
        if start_vertex not in self._adjacency_list or end_vertex not in self._adjacency_list:
            raise KeyError()

        edge = Edge(end_vertex, weight)
        self._adjacency_list[start_vertex].append(edge)

    def get_nodes(self):
        """
        Arguments: none -->
        Returns: all of the nodes in the graph as a collection -->
        This method takes no arguments. It returns a collection (set, list, or similar) of the nodes.
        """
        return self._adjacency_list.keys()

    def get_neighbors(self, vertex):
        """
        Arguments: a node -->
        Returns: A collection of edges to the given node
        This method takes in a node and returns a collection of its given edges and their weight.
        """
        return self._adjacency_list[vertex]

    def size(self):
        """
        Arguments: none -->
        Returns: number of nodes -->
        This method returns the total number of nodes in the given graph.
        """
        return len(self._adjacency_list)


class Vertex:
    def __init__(self, value):
        self.value = value


class Edge():
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight
