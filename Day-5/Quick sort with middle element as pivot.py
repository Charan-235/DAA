def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    result = quick_sort(left) + middle + quick_sort(right)
    print("Array after sorting step:", result)
    return result

arr1 = [19, 72, 35, 46, 58, 91, 22, 31]
print("\nFinal sorted array:", quick_sort(arr1))
