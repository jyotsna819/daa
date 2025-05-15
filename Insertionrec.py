def recursive_insertion_sort(arr, n=None):
    if n is None:
        n = len(arr)
    
    # Base case
    if n <= 1:
        return

    # Sort first n-1 elements
    recursive_insertion_sort(arr, n - 1)

    # Insert last element at its correct position in sorted array
    last = arr[n - 1]
    j = n - 2

    # Move elements that are greater than last to one position ahead
    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = last

# Taking input from user
arr = list(map(int, input("Enter the numbers separated by space: ").split()))

recursive_insertion_sort(arr)
print("Sorted array:", arr)
