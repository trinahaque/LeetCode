# Time Complexity: O(n)
# Space Complexity: Constant
def rotateArr(nums, k):
    if len(nums) < 2:
        return nums
    r = k % len(nums)
    reverse(nums, 0, len(nums) - r)
    reverse(nums, len(nums) - r, len(nums))
    reverse(nums, 0, len(nums))
    return nums

# Time Complexity: O(n)/2
# Space Complexity: Constant
def reverse(nums, start, end):
    mid = start + int((end-start)/2)
    i = 0
    while (start + i) < mid:
        nums[start + i], nums[end-1-i] = nums[end-1-i], nums[start + i]
        i += 1
    return nums

nums = [1, 2, 3, 4, 5, 6]
nums2 = [5, 6]
rotateArr(nums, 6)