def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    sorted_left = quick_sort(left)
    sorted_right = quick_sort(right)
    result = sorted_left + [pivot] + sorted_right
    print("Array after sorting step:", result)
    return result

arr1 = [10, 16, 8, 12, 15, 6, 3, 9, 5]
print("\nFinal sorted array:", quick_sort(arr1))
