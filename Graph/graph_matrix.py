class GraphMatrix:
    def __init__(self, size):
        self.size = size
        self.graph = [[0] * size for _ in range(size)]
        self.vertices = []

    def add_vertex(self, vertex):
        self.vertices.append(vertex)

    def add_edge(self, v1, v2):
        i = self.vertices.index(v1)
        j = self.vertices.index(v2)
        self.graph[i][j] = 1
        self.graph[j][i] = 1  # For undirected graph

    def display(self):
        print("   ", "  ".join(self.vertices))
        for i in range(self.size):
            print(self.vertices[i], self.graph[i])


if __name__ == "__main__":
    gm = GraphMatrix(3)
    gm.add_vertex("A")
    gm.add_vertex("B")
    gm.add_vertex("C")
    gm.add_edge("A", "B")
    gm.add_edge("B", "C")

    gm.display()
