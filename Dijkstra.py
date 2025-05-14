import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.adj[u].append((v, weight))
        self.adj[v].append((u, weight))  # Comment this line if directed

    def dijkstra(self, source):
        distances = [float('inf')] * self.V
        distances[source] = 0
        visited = [False] * self.V
        priority_queue = [(0, source)]  # (distance, node)

        while priority_queue:
            curr_dist, u = heapq.heappop(priority_queue)
            if visited[u]:
                continue
            visited[u] = True

            for neighbor, weight in self.adj[u]:
                if not visited[neighbor] and curr_dist + weight < distances[neighbor]:
                    distances[neighbor] = curr_dist + weight
                    heapq.heappush(priority_queue, (distances[neighbor], neighbor))

        print("\nShortest distances from source node", source)
        for i in range(self.V):
            print(f"Node {i}: Distance = {distances[i]}")

def main():
    V = int(input("Enter number of nodes: "))
    E = int(input("Enter number of edges: "))
    g = Graph(V)

    print("Enter edges in the format (u v weight):")
    for _ in range(E):
        u, v, w = map(int, input().split())
        g.add_edge(u, v, w)

    source = int(input("Enter the source node: "))
    g.dijkstra(source)

if __name__ == "__main__":
    main()
