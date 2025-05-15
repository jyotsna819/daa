def quick_sort(arr, low, high):
    if low < high:
        # Partition the array
        pi = partition(arr, low, high)

        # Recursively sort elements before and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  # choosing the last element as pivot
    i = low - 1  # index of smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # swap

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # swap pivot into correct position
    return i + 1

# Taking input from user
arr = list(map(int, input("Enter the numbers separated by space: ").split()))

quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
