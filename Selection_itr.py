import time

def iterative_selection_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1
    return comparisons, swaps

def print_array(arr, message):
    print(message)
    for num in arr:
        print(num, end=" ")
    print()

def main():
    n = int(input("Enter number of elements: "))
    arr = list(map(int, input(f"Enter {n} elements (space-separated): ").split()))

    if len(arr) != n:
        print("Error: Number of elements entered doesn't match 'n'")
        return

    start = time.time()
    comparisons, swaps = iterative_selection_sort(arr)
    end = time.time()

    print_array(arr, "\nSorted Array (Iterative):")
    print("\nExecution Time: {:.6f} seconds".format(end - start))
    print("Comparisons:", comparisons)
    print("Swaps:", swaps)

if __name__ == "__main__":
    main()
