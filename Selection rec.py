def recursive_selection_sort(arr, start=0):
    n = len(arr)
    if start >= n - 1:
        return

    # Find index of minimum element
    min_index = start
    for i in range(start + 1, n):
        if arr[i] < arr[min_index]:
            min_index = i

    # Swap the found minimum with the first unsorted element
    arr[start], arr[min_index] = arr[min_index], arr[start]

    # Recur for the remaining unsorted part
    recursive_selection_sort(arr, start + 1)

# Taking input from user
arr = list(map(int, input("Enter the numbers separated by space: ").split()))

recursive_selection_sort(arr)
print("Sorted array:", arr)
