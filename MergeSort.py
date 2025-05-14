def print_steps(steps):
    for step in steps:
        print("[", end=" ")
        print("] ", end="")
    print()

def divide_array(arr, left, right, division_steps):
    if left >= right:
        return
    mid = left + (right - left) // 2
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]
    division_steps.append(left_part)
    division_steps.append(right_part)
    divide_array(arr, left, mid, division_steps)
    divide_array(arr, mid + 1, right, division_steps)

def merge(arr, left, mid, right, merge_steps):
    n1 = mid - left + 1
    n2 = right - mid
    left_arr = arr[left:left + n1]
    right_arr = arr[mid + 1:mid + 1 + n2]

    i = j = k = left
    while i < n1 and j < n2:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = right_arr[j]
        j += 1
        k += 1

    merged = arr[left:right + 1]
    merge_steps.append(merged)

def merge_sort(arr, left, right, merge_steps):
    if left < right:
        mid = left + (right - left) // 2
        merge_sort(arr, left, mid, merge_steps)
        merge_sort(arr, mid + 1, right, merge_steps)
        merge(arr, left, mid, right, merge_steps)

def main():
    n = int(input("Enter number of elements: "))
    arr = list(map(int, input(f"Enter {n} elements: ").split()))

    division_steps, merge_steps = [], []
    division_steps.append(arr.copy())  # Store the original array
    divide_array(arr, 0, n - 1, division_steps)

    print("\nDivision Steps:")
    # Print division steps on the same line with each part in brackets
    print(" ".join(f"[{' '.join(map(str, step))}]" for step in division_steps))

    merge_sort(arr, 0, n - 1, merge_steps)

    print("\nMerging Steps:")
    # Print merging steps on the same line with each part in brackets
    print(" ".join(f"[{' '.join(map(str, step))}]" for step in merge_steps))

    print("\nSorted array:", arr)

if __name__ == "__main__":
    main()
