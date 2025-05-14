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

# Main Function
def main():
    n = int(input("Enter the number of elements: "))
    arr = list(map(int, input("Enter the elements (space-separated): ").split()))
    
    if len(arr) != n:
        print("Error: Number of elements entered doesn't match 'n'")
        return

    # Iterative sort timing
    start_iter = time.perf_counter_ns()
    comp_iter, swaps_iter = insertion_sort_iterative(arr)
    end_iter = time.perf_counter_ns()
    duration_iter = (end_iter - start_iter) / 1000  # Convert to microseconds

    # Output
    print("\nSorted Array (Iterative):")
    print(arr)
    print("\nExecution Time: {:.6f} microseconds".format(duration_iter))
    print("Comparisons:", comp_iter)
    print("Swaps:", swaps_iter)

if __name__ == "__main__":
    main()
