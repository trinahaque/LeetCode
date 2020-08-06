# Time Complexity: O(n) --> one loop
# Space Complexity: O(1) or Constant --> only storing two variables

# Kadane's Algorithm: start a new sum at current index or continue from
# previous sum

# There is a divide/conquer way

def maxSubArray(nums):
    current_max = nums[0]
    max_sum = current_max

    for i in range(1, len(nums)):
        if nums[i] > current_max + nums[i]:
            current_max = nums[i]
        elif nums[i] < current_max + nums[i]:
            current_max = current_max + nums[i]
        if current_max > max_sum:
            max_sum = current_max
    return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
# print(maxSubArray(nums))
nums = [4,-1,2,1]
nums = [1,2,-1,-2,2,1,-2,1,4,-5,4]
# print(maxSubArray(nums))

# surprisingly, the previous solution runs faster and uses less memory
def maxSubArray2(nums):
    current_max = nums[0]
    max_sum = current_max

    for i in range(1, len(nums)):
        current_max = max(nums[i], current_max + nums[i])
        max_sum = max(current_max, max_sum)
    return max_sum


nums = [1,2,-1,-2,2,1,-2,1,4,-5,4]
print(maxSubArray2(nums))