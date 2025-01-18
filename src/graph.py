class Graph:
    def __init__(self, directed=False):
        self.graph = {}
        self.directed = directed

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, u, v, weight=1):
        self.add_node(u)
        self.add_node(v)
        self.graph[u].append((v, weight))
        if not self.directed:
            self.graph[v].append((u, weight))

    def get_neighbors(self, node):
        return self.graph.get(node, [])

    def __str__(self):
        return str(self.graph)
