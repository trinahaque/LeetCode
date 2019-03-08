# Time Complexity: O(n) --> loops through every element in the array
# Space Complexity: O(1) --> solved in space. only created one variable start
def removeDuplicates(nums):
    if len(nums) < 2:
        return len(nums)
    start = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[start]:
            start = start + 1
            nums[start] = nums[i]
    return start + 1