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

    arr1 = arr.copy()
    arr2 = arr.copy()

    start_iter = time.time()
    comp_iter, swap_iter = iterative_selection_sort(arr1)
    end_iter = time.time()
    print_array(arr1, "\nSorted Array (Iterative):")

    start_rec = time.time()
    comp_rec, swap_rec = recursive_selection_sort(arr2, n, 0, 0, 0)
    end_rec = time.time()
    print_array(arr2, "\nSorted Array (Recursive):")

    print("\nMethod       Time(s)   Comparisons   Swaps")
    print("Iterative    {:.6f}   {}           {}".format(end_iter - start_iter, comp_iter, swap_iter))
    print("Recursive    {:.6f}   {}           {}".format(end_rec - start_rec, comp_rec, swap_rec))

if __name__ == "__main__":
    main()
