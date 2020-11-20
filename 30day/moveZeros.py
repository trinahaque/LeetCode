# Time Complexity: O(n) --> two loops
# Space Compexity: O(1) or constant --> in place swap

# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# def moveZeroes(nums):
#     nonZeroIndex = 0
#     # find all the non zero numbers and move them to the front
#     for i in range(len(nums)):
#         if nums[i] != 0:
#             nums[nonZeroIndex] = nums[i]
#             nonZeroIndex += 1
#     # nonZeroIndex should point to the index where the first zero should be
#     # add all the zeros to the end of the array
#     for i in range(nonZeroIndex, len(nums)):
#         nums[i] = 0
#     return nums
# nums = [0, 0, 5, 4, 6]
# print(moveZeroes(nums))


# optimized zolution
#Time Complexity: O(n)
#Space Complexity: O(1) or constant
def moveZeros2(nums):
    zeroIndex = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[zeroIndex], nums[i] = nums[i], nums[zeroIndex]
            zeroIndex = zeroIndex + 1
    return nums

nums = [0, 0, 5, 4, 6]
print(moveZeros2(nums))


