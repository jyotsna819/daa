class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))

    def bellman_ford(self, source):
        distance = [float('inf')] * self.V
        distance[source] = 0

        # Relax all edges |V| - 1 times
        for _ in range(self.V - 1):
            for u, v, weight in self.edges:
                if distance[u] != float('inf') and distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight

        # Check for negative weight cycles
        for u, v, weight in self.edges:
            if distance[u] != float('inf') and distance[u] + weight < distance[v]:
                print("\nGraph contains a negative weight cycle!")
                return

        # Print shortest distances
        print(f"\nShortest distances from source node {source}:")
        for i in range(self.V):
            print(f"Node {i}: Distance = {distance[i]}")


def main():
    V = int(input("Enter number of nodes: "))
    E = int(input("Enter number of edges: "))
    g = Graph(V)

    print("Enter edges in the format (u v weight):")
    for _ in range(E):
        u, v, w = map(int, input().split())
        g.add_edge(u, v, w)

    source = int(input("Enter the source node: "))
    g.bellman_ford(source)

if __name__ == "__main__":
    main()
