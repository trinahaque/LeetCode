# Given an array of integers, return indices of the two numbers such that they add up 
# to a specific target. 
# Will have eactly one solution
# Don't use the same element twice
# nums = [2, 7, 11, 15], target = 9
# return [0, 1]

# O(n^2) solution
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




# O(2n) time solution (one loop to create dict, one loop to loop through the array)
# O(n) space to store the dict
def twoSumDict(arr, target):
    map = {}
    for i in range(0, len(arr)):
        map[arr[i]] = i
    # print (type(map.keys()))
    result = []
    for i in range(0, len(arr)):
        tmp = arr[i]
        remainder = target - arr[i]
        # check if the remainder is in the keys and the index is not the current index
        if remainder in map.keys() and map[remainder] != i:
            result = [i, map[remainder]]
            break
    return result

nums = [8, 11, 3, 17, 1, 15, 5]
nums2 = [2, 3]
print(twoSumDict(nums2, 5))


print (twoSum(nums2, 4))