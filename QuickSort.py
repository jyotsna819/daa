# import random
# import time

# # Global counters
# comparisons = 0
# swaps = 0

# # Function to swap two elements
# def swap(arr, i, j):
#     global swaps
#     swaps += 1
#     arr[i], arr[j] = arr[j], arr[i]

# # Partition function with randomized pivot
# def partition(arr, low, high):
#     global comparisons
#     random_index = random.randint(low, high)
#     swap(arr, random_index, high)
#     pivot = arr[high]
#     i = low - 1

#     for j in range(low, high):
#         comparisons += 1
#         if arr[j] <= pivot:
#             i += 1
#             swap(arr, i, j)
#     swap(arr, i + 1, high)
#     return i + 1

# # Quick Sort function
# def quick_sort(arr, low, high, pass_num):
#     if low < high:
#         pivot_index = partition(arr, low, high)
#         print(f"Pass {pass_num}: Comparisons = {comparisons}, Swaps = {swaps}")
#         quick_sort(arr, low, pivot_index - 1, pass_num + 1)
#         quick_sort(arr, pivot_index + 1, high, pass_num + 1)

# # Main function with user input
# def main():
#     global comparisons, swaps
#     n = int(input("Enter the number of elements: "))
#     arr = list(map(int, input(f"Enter {n} integers (space-separated): ").split()))

#     if len(arr) != n:
#         print("Error: Number of elements entered doesn't match 'n'")
#         return

#     print("\nOriginal Array:", arr)
#     random.seed(time.time())  # Seed the random number generator
#     quick_sort(arr, 0, n - 1, 1)

#     print("\nSorted Array:", arr)
#     print("Total Comparisons:", comparisons)
#     print("Total Swaps:", swaps)

# if __name__ == "__main__":
#     main()


# BFS to display Order and Nodes

from collections import deque, defaultdict

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    traversal_order = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            traversal_order.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return traversal_order

def main():
    graph = defaultdict(list)
    
    n = int(input("Enter the number of edges: "))
    print("Enter each edge in the format 'u v' where u and v are connected nodes:")

    for _ in range(n):
        u, v = input().split()
        graph[u].append(v)
        graph[v].append(u)  # For undirected graph; remove if directed

    start_node = input("Enter the starting node for BFS: ")

    traversal = bfs(graph, start_node)
    print("\nBFS Traversal Order:", traversal)
    print("Total Nodes Visited:", len(traversal))

if __name__ == "__main__":
    main()

