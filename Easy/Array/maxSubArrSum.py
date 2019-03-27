# Time Complexity: O(n) --> n + n for two loops
# Space Complexity: O(1)/constant --> only storing max variable
def maxSubArray(nums):
        if len(nums) < 2:
            return nums[0]
        
        for i in range(1, len(nums)):
            if nums[i-1] + nums[i] > nums[i]:
                nums[i] = nums[i-1] + nums[i]
        max = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[max]:
                max = i
        return nums[max]

nums = [-3, -1, -3]
print(maxSubArray(nums))

nums = [10, -11, -3, 0, 2, 5]
print(maxSubArray(nums))