# advanced methods
from graph_list import Graph

class AdvancedGraph(Graph):
    def shortest_path(self, start, end):
        queue = [(start, [start])]
        visited = set([start])

        while queue:
            vertex, path = queue.pop(0)

            for neighbor in self.get_neighbours(vertex):
                if neighbor not in visited:
                    if neighbor == end:
                        return path + [neighbor]
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))

        return None

    def is_connected(self):
        if not self.graph:
            return True

        visited = set()
        start = next(iter(self.graph))  # pick any starting vertex
        self.dfs(start, visited)
        return len(visited) == len(self.graph)

    def has_cycle(self):
        def _has_cycle_dfs(vertex, visited, parent):
            visited.add(vertex)
            for neighbor in self.get_neighbours(vertex):
                if neighbor not in visited:
                    if _has_cycle_dfs(neighbor, visited, vertex):
                        return True
                elif neighbor != parent:
                    return True
            return False
        
        visited = set()
        for vertex in self.graph:
            if vertex not in visited:
                if _has_cycle_dfs(vertex, visited, parent=None):
                    return True
        return False


if __name__ == "__main__":
    g = AdvancedGraph()
    g.add_edge("A", "B")
    g.add_edge("B", "C")
    g.add_edge("C", "A")  # creates a cycle

    print("Graph:")
    g.display()
    print("Connected?", g.is_connected())
    print("Has Cycle?", g.has_cycle())

    g2 = AdvancedGraph()
    g2.add_edge("A", "B")
    g2.add_edge("B", "C")

    print("Has Cycle?", g2.has_cycle())


# PENDING
# 1. Min Spanning Tree (Kruskal's and Prim's Algorithm)
# 2. Shortest path for weighted graph (Dijkstra’s Algorithm, Bellman-Ford, Floyd–Warshall)