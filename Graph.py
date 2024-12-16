class Graph:
    """
    Represents a graph using an adjacency list.
    
    Attributes:
        adjacency_list (dict): A dictionary where keys are nodes and values are lists of connected nodes.
    """
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, node):
        """
        Adds a new node to the graph.
        """
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []

    def add_edge(self, node1, node2, bidirectional=True):
        """
        Adds an edge between two nodes.

        Args:
            node1: The first node.
            node2: The second node.
            bidirectional (bool): If True, the edge is bidirectional.
        """
        if node1 not in self.adjacency_list:
            self.add_node(node1)
        if node2 not in self.adjacency_list:
            self.add_node(node2)

        self.adjacency_list[node1].append(node2)
        if bidirectional:
            self.adjacency_list[node2].append(node1)

    def remove_edge(self, node1, node2):
        """
        Removes an edge between two nodes.
        """
        if node1 in self.adjacency_list and node2 in self.adjacency_list[node1]:
            self.adjacency_list[node1].remove(node2)
        if node2 in self.adjacency_list and node1 in self.adjacency_list[node2]:
            self.adjacency_list[node2].remove(node1)

    def remove_node(self, node):
        """
        Removes a node and all edges connected to it.
        """
        if node in self.adjacency_list:
            for neighbor in self.adjacency_list[node]:
                self.adjacency_list[neighbor].remove(node)
            del self.adjacency_list[node]

    def get_neighbors(self, node):
        """
        Returns the list of neighbors for a given node.
        """
        return self.adjacency_list.get(node, [])

    def display(self):
        """
        Displays the graph's adjacency list.
        """
        for node in self.adjacency_list:
            print(f"{node}: {self.adjacency_list[node]}")
