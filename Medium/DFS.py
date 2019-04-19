class Graph:
    def __init__(self, edges):
        self.edges = edges
    def neighbors(self, id):
        return self.edges[id]
edges = {
    "A": ["B", "C"],
    "B": ["C", "E", "G"],
    "C": ["D", "F"],
    "D": ["G"],
    "E": ["F"],
    "F": ["G"],
    "G": [],
}
graph = Graph(edges)

# Time Complexity: V + E
# Space Complexity: V (all the nodes in the stack)
def DFS(graph, start):
    visited = {}
    dfs(graph, start, visited)

def dfs(graph, node, visited):
    visited[node] = True
    print (node)
    for neighbor in graph.neighbors(node):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

print (DFS(graph, "A"))
# A, B, C, D, G, F, E
