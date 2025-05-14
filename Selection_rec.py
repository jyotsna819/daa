import time

def recursive_selection_sort(arr, n, index, comparisons, swaps):
    if index >= n - 1:
        return comparisons, swaps
    min_index = index
    for j in range(index + 1, n):
        comparisons += 1
        if arr[j] < arr[min_index]:
            min_index = j
    if min_index != index:
        arr[index], arr[min_index] = arr[min_index], arr[index]
        swaps += 1
    return recursive_selection_sort(arr, n, index + 1, comparisons, swaps)

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
    comparisons, swaps = recursive_selection_sort(arr, n, 0, 0, 0)
    end = time.time()

    print_array(arr, "\nSorted Array (Recursive):")
    print("\nExecution Time: {:.6f} seconds".format(end - start))
    print("Comparisons:", comparisons)
    print("Swaps:", swaps)

if __name__ == "__main__":
    main()
