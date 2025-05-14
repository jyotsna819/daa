from collections import defaultdict

class Graph:
    def __init__(self, nodes, directed):
        self.nodes = nodes
        self.directed = directed
        self.adjList = defaultdict(list)

    def add_edge(self, u, v):
        self.adjList[u].append(v)
        if not self.directed:
            self.adjList[v].append(u)

    def dfs_util(self, node, visited, traversal_order):
        visited[node] = True
        traversal_order.append(node)
        for neighbor in self.adjList[node]:
            if not visited[neighbor]:
                self.dfs_util(neighbor, visited, traversal_order)

    def dfs(self, source):
        visited = [False] * self.nodes
        traversal_order = []
        self.dfs_util(source, visited, traversal_order)
        
        print("DFS Traversal:", " ".join(map(str, traversal_order)))
        print("Total Nodes Visited:", len(traversal_order))


def main():
    nodes = int(input("Enter number of nodes: "))
    edges = int(input("Enter number of edges: "))
    directed = bool(int(input("Enter 1 for directed graph, 0 for undirected graph: ")))
    
    g = Graph(nodes, directed)

    print("Enter edges (u v):")
    for _ in range(edges):
        u, v = map(int, input().split())
        g.add_edge(u, v)

    source = int(input("Enter the source node for DFS traversal: "))

    print("\nPerforming DFS Traversal from node", source)
    g.dfs(source)

if __name__ == "__main__":
    main()
