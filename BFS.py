# # BFS to display Order and Nodes

# from collections import deque, defaultdict

# def bfs(graph, start):
#     visited = set()
#     queue = deque([start])
#     traversal_order = []

#     while queue:
#         node = queue.popleft()
#         if node not in visited:
#             visited.add(node)
#             traversal_order.append(node)
#             for neighbor in graph[node]:
#                 if neighbor not in visited:
#                     queue.append(neighbor)

#     return traversal_order

# def main():
#     graph = defaultdict(list)
    
#     n = int(input("Enter the number of edges: "))
#     print("Enter each edge in the format 'u v' where u and v are connected nodes:")

#     for _ in range(n):
#         u, v = input().split()
#         graph[u].append(v)
#         graph[v].append(u)  # For undirected graph; remove if directed

#     start_node = input("Enter the starting node for BFS: ")

#     traversal = bfs(graph, start_node)
#     print("\nBFS Traversal Order:", traversal)
#     print("Total Nodes Visited:", len(traversal))

# if __name__ == "__main__":
#     main()


from collections import deque, defaultdict

class Graph:
    def __init__(self, nodes, directed):
        self.nodes = nodes
        self.isDirected = directed
        self.adjList = defaultdict(list)

    def add_edge(self, u, v):
        self.adjList[u].append(v)
        if not self.isDirected:
            self.adjList[v].append(u)

    def bfs(self, start, visited):
        queue = deque()
        queue.append(start)
        visited[start] = True
        print("BFS Traversal:", end=" ")
        count = 0

        while queue:
            node = queue.popleft()
            print(node, end=" ")
            count += 1
            for neighbor in self.adjList[node]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True

        print(f"\nTotal Nodes Visited: {count}")
    
    def traverse_graph(self):
        visited = [False] * self.nodes
        component_count = 0
        for i in range(self.nodes):
            if not visited[i] and self.adjList[i]:
                component_count += 1
                print(f"Component {component_count}:")
                self.bfs(i, visited)
                print("-----------------------------")
        if component_count == 0:
            print("No edges in the graph, isolated nodes present.")

def main():
    nodes = int(input("Enter number of nodes: "))
    edges = int(input("Enter number of edges: "))
    is_directed = bool(int(input("Enter 1 for directed graph, 0 for undirected graph: ")))

    g = Graph(nodes, is_directed)

    print("Enter edges (u v):")
    for _ in range(edges):
        u, v = map(int, input().split())
        g.add_edge(u, v)

    print("\nPerforming BFS Traversal on Graph:")
    g.traverse_graph()

if __name__ == "__main__":
    main()
