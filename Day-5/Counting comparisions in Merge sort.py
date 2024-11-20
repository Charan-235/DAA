def merge_sort(arr):
    global comparison_count
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        comparison_count += 1
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:] + right[j:])
    return merged

comparison_count = 0
arr1 = [12, 4, 78, 23, 45, 67, 89, 1]
arr1 = merge_sort(arr1)
print("Sorted array:", arr1)
print("Number of comparisons:", comparison_count)

