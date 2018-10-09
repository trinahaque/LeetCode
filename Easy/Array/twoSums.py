# Given an array of integers, return indices of the two numbers such that they add up 
# to a specific target. 
# Will have eactly one solution
# Don't use the same element twice
# nums = [2, 7, 11, 15], target = 9
# return [0, 1]

def twoSum(nums, target):
    # only one element, return False
    if len(nums) < 2:
        return False

    # O n^2 solution
    for i in range(0, len(nums)-1):
        for j in range(i+1, len(nums)):
            if (nums[i] + nums[j]) == target:
                return [i, j]
    return False

nums = [8, 11, 3, 17, 1, 15, 5]
print (twoSum(nums, 9))