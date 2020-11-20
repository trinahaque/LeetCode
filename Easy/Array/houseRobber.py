def rob(nums):
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums)
 
    for i in range(2, len(nums)):
        nums[i] = Math.max(nums[i-1], nums[i]+nums[i-2])
    return max(nums)

nums = [2, 7]
print(rob(nums))