def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements that are greater than key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Taking input from user
arr = list(map(int, input("Enter the numbers separated by space: ").split()))

insertion_sort(arr)
print("Sorted array:", arr)
