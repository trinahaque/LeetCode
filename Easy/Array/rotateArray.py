def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    k = k % len(nums)
    i = 0
    while i < k:
        nums[i], nums[i+k-len(nums)] = nums[i+k-len(nums)], nums[i]
        print ("nums at ", i , " is ", nums)
        i = i + 1
    return nums

# nums = [1, 2, 3, 4, 5, 6, 7]
# k = 3
# print(rotate(nums, k))

nums = [-1, -100, 3, 99, 0]
k = 2
print(rotate(nums, k))