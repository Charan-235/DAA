def sum_of_squares(nums):
    total_sum = 0
    for i in range(len(nums)):
        distinct_elements = []
        for j in range(i, len(nums)):
            if nums[j] not in distinct_elements:
                distinct_elements.append(nums[j])
            total_sum += len(distinct_elements) ** 2
    return total_sum
nums = [1, 2, 1]
print(sum_of_squares(nums)) 

# Output: 15
