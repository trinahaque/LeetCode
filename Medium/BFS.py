# Vertices are the dots/nodes
# Edges are the lines
# Graph Representations
# Adjacency Matrix
# Adjacency List

import queue

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
# print ("graph is ", graph)
# print ("Edge of B is ", graph.neighbors("B"))



# Time Complexity: O(V + E) --> all the nodes and its connections need to be visited
# Space Complexity: O(V) --> all nodes need to be added to the queue since they have not visited
def BFS(graph, start):
    newQueue = queue.Queue()
    visited = {}
    # Enqueue --> put
    newQueue.put(start)
    visited[start] = True

    while not newQueue.empty():
        # Dequeue --> get/first one out
        current = newQueue.get()
        print ("Visiting node ", current)
        # graph.neighbors(node) returns an array
        for eachEdge in graph.neighbors(current):
            if eachEdge not in visited:
                # print (eachEdge)
                newQueue.put(eachEdge)
                visited[eachEdge] = True
BFS(graph, "A")

# A, B, C, E, G, D, F, 

# BFS --> queue, visit all node's (vertex's) neighbors before moving in to next node
def BFS2(graph, start):
    queue2 = queue.Queue()
    visited = {}
    visited[start] = True
    # put is enqueue
    queue2.put(start)
    while not queue2.empty():
        current = queue2.get()
        print ("Visiting node ", current)
        for eachVal in graph.neighbors(current):
            if eachVal not in visited:
                queue2.put(eachVal)
                visited[eachVal] = True

edges2 = {
    "0": ["1", "2"],
    "1": ["2"],
    "2": ["3"],
    "3": ["4"],
    "4": ["1", "5"],
    "5": [],
}
graph2 = Graph(edges2)
BFS2(graph2, "0")


