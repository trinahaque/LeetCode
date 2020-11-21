# Time Complexity: O(n) --> one for loop
# Space Complexity: O(1) or constant --> values change in place
def rob(nums):
    if len(nums) < 1:
        return 0
    if len(nums) < 2:
        return nums[0]
    nums[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        nums[i] = max(nums[i-1], nums[i]+nums[i-2])
    return nums[len(nums)-1]

nums = [1, 0, 0, 2, 5, 100]
print(rob(nums))