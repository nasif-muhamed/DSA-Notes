# Implementation 1: Adjacency List (Most Common & Efficient)
class Graph:
    def __init__(self):
        self.graph = dict()

    def add_edge(self, u, v):
        """Adds an edge from vertex u to vertex v."""
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)
        self.graph[v].append(u)  # for undirected graph.

    def remove_edge(self, u, v):
        """Removes the edge from vertex u to vertex v."""
        if self.has_edge(u, v):
            self.graph[u].remove(v)

        if self.has_edge(v, u):  # For undirected graph
            self.graph[v].remove(u)

    def has_edge(self, u, v):
        """Checks if there is an edge between u and v."""
        return u in self.graph and v in self.graph[u]
    
    def get_neighbours(self, u):
        """Returns a list of neighbors for vertex u."""
        return self.graph.get(u, [])
    
    def get_edge_count(self):
        """Returns number of edges in a graph."""
        count = sum([len(self.graph[vertex]) for vertex in self.graph])
        return count // 2  # For undirected
    
    def display(self):
        """Displays the graph as an adjacency list."""
        for vertex in self.graph:
            print(vertex, ':', self.graph[vertex])

    def bfs(self, start):
        """Breadth First Search"""
        queue = [start]
        visited = set([start])

        while queue:
            vertex = queue.pop(0)
            print(vertex, end=" ")

            for neighbour in self.get_neighbours(vertex):
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)

    def dfs(self, start, visited=None):
        """Depth First Search"""
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=" ")

        for neighbor in self.get_neighbours(start):
            if neighbor not in visited:
                self.dfs(neighbor, visited)


if __name__ == "__main__":
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("C", "E")

    print("Graph:")
    g.display()

    print("Total edges:")
    print(g.get_edge_count())

    print("\nBFS Traversal:")
    g.bfs("A")

    print("\nDFS Traversal:")
    g.dfs("A")
