import time

# Iterative Insertion Sort
def insertion_sort_iterative(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            swaps += 1
            j -= 1
        arr[j + 1] = key
        if j >= 0:  # Only count comparison when a swap happens
            comparisons += 1
    return comparisons, swaps

# Recursive Insertion Sort
def insertion_sort_recursive(arr, n, index, comparisons, swaps):
    if index == n:
        return comparisons, swaps
    key = arr[index]
    j = index - 1
    while j >= 0 and arr[j] > key:
        comparisons += 1
        arr[j + 1] = arr[j]
        swaps += 1
        j -= 1
    arr[j + 1] = key
    if j >= 0:  # Only count comparison when a swap happens
        comparisons += 1
    return insertion_sort_recursive(arr, n, index + 1, comparisons, swaps)

# Main Function
def main():
    n = int(input("Enter the number of elements: "))
    arr1 = list(map(int, input("Enter the elements (space-separated): ").split()))
    
    if len(arr1) != n:
        print("Error: Number of elements entered doesn't match 'n'")
        return

    arr2 = arr1.copy()  # Copy for recursive sort

    # Iterative sort timing
    start_iter = time.perf_counter_ns()
    comp_iter, swaps_iter = insertion_sort_iterative(arr1)
    end_iter = time.perf_counter_ns()
    duration_iter = (end_iter - start_iter) / 1000  # Convert to microseconds

    # Recursive sort timing
    start_rec = time.perf_counter_ns()
    comp_rec, swaps_rec = insertion_sort_recursive(arr2, n, 1, 0, 0)
    end_rec = time.perf_counter_ns()
    duration_rec = (end_rec - start_rec) / 1000  # Convert to microseconds

    # Output
    print("\nSorting Analysis:")
    print("------------------------------------------------------------")
    print("| Method     | Execution Time (μs) | Comparisons | Swaps   |")
    print("------------------------------------------------------------")
    print(f"| Iterative  | {duration_iter:<22.2f}| {comp_iter:<11} | {swaps_iter:<7} |")
    print(f"| Recursive  | {duration_rec:<22.2f}| {comp_rec:<11} | {swaps_rec:<7} |")
    print("------------------------------------------------------------")

if __name__ == "__main__":
    main()
