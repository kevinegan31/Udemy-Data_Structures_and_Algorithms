"""Graph Constructor"""


class Graph:
    """Graph constructor"""

    def __init__(self):
        # Create dictionary
        self.adj_list = {}

    def print_graph(self):
        """Print graph method"""
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])

    # Add vertex method
    def add_vertex(self, vertex):
        """Adds vertex to graph"""
        # Check if the vertex value is already in the dictionary
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    # Add edge method
    def add_edge(self, v1, v2):
        """Adds edge for vertices"""
        # Check if vertices both exist
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            # Appends dictionary for particular vertices
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    # Remove edge method
    def remove_edge(self, v1, v2):
        """Removes edge from graph"""
        # Need to check if vertex 1 and 2 exist
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            # Try to remove edges
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            # Ignore if true
            except ValueError:
                pass
            return True
        return False

    # Remove vertex method
    def remove_vertex(self, vertex):
        """Removes vertex from graph"""
        # Check if vertex exists in dictionary
        if vertex in self.adj_list.keys():
            # For any other vertex found in the list,
            # remove vertex from that list.
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False


# Add vertex test
my_graph = Graph()

my_graph.add_vertex("A")

my_graph.print_graph()

# Add edge test
my_graph = Graph()

my_graph.add_vertex(1)
my_graph.add_vertex(2)

my_graph.add_edge(1, 2)

my_graph.print_graph()

# Remove edge test
my_graph = Graph()
my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")

my_graph.add_edge("A", "B")
my_graph.add_edge("B", "C")
my_graph.add_edge("C", "A")

print("Graph before remove_edge():")
my_graph.print_graph()


my_graph.remove_edge("A", "C")
my_graph.remove_edge("A", "D")

print("\nGraph after remove_edge():")
my_graph.print_graph()


"""
    EXPECTED OUTPUT:
    ----------------
    Graph before remove_edge():
    A : ['B', 'C']
    B : ['A', 'C']
    C : ['B', 'A']

    Graph after remove_edge():
    A : ['B']
    B : ['A', 'C']
    C : ['B']
    
"""
# Remove Vertex

my_graph = Graph()
my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")

my_graph.add_edge("A", "B")
my_graph.add_edge("A", "C")
my_graph.add_edge("A", "D")
my_graph.add_edge("B", "D")
my_graph.add_edge("C", "D")


print("Graph before remove_vertex():")
my_graph.print_graph()


my_graph.remove_vertex("D")


print("\nGraph after remove_vertex():")
my_graph.print_graph()


"""
EXPECTED OUTPUT:
----------------
    Graph before remove_vertex():
    A : ['B', 'C', 'D']
    B : ['A', 'D']
    C : ['A', 'D']
    D : ['A', 'B', 'C']

    Graph after remove_vertex():
    A : ['B', 'C']
    B : ['A']
    C : ['A']

"""
