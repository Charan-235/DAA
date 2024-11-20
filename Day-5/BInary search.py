def binary_search(arr, key):
    left, right = 0, len(arr) - 1
    comparisons = 0

    while left <= right:
        comparisons += 1
        mid = (left + right) // 2
        if arr[mid] == key:
            print("Number of comparisons:", comparisons)
            return mid + 1  # Return 1-based index
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    print("Number of comparisons:", comparisons)
    return -1  # Element not found
# Test cases
arr1 = [5, 10, 15, 20, 25, 30, 35, 40, 45]
print("Index of 20:", binary_search(arr1, 20))
