import time

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
    arr = list(map(int, input("Enter the elements (space-separated): ").split()))
    
    if len(arr) != n:
        print("Error: Number of elements entered doesn't match 'n'")
        return

    # Recursive sort timing
    start_rec = time.perf_counter_ns()
    comp_rec, swaps_rec = insertion_sort_recursive(arr, n, 1, 0, 0)
    end_rec = time.perf_counter_ns()
    duration_rec = (end_rec - start_rec) / 1000  # Convert to microseconds

    # Output
    print("\nSorted Array (Recursive):")
    print(arr)
    print("\nExecution Time: {:.6f} microseconds".format(duration_rec))
    print("Comparisons:", comp_rec)
    print("Swaps:", swaps_rec)

if __name__ == "__main__":
    main()
