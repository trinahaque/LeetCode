# Time Complexity: O(n) + O(n) --> O(n)
# Space Complexity: O(1)

def moveZeroes(nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        s = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[s] = nums[i]
                s += 1
        for i in range(s, len(nums)):
            nums[i] = 0
        return nums

n = [0,1,0,3,12]
print(moveZeroes(n))