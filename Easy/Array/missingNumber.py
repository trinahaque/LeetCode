def missingNumber(nums):
    # sort the array
    # time complexity: O(n)
    nums = sorted(nums)

    # if 1st val is not 0, return 0
    # regardless of the length of the nums, the first value will be 0
    if nums[0] != 0:
        return 0
    # if last value is not len(nums), return len(nums)
    # regardless of length
    elif nums[-1] != len(nums):
        return len(nums)
    else:
        for i in range(len(nums) - 1):
            if nums[i+1] - nums[i] > 1:
                return nums[i] + 1
    

n = [9,6,4,2,3,5,7,0,1]
print (missingNumber(n))

m = [0,1,2]
print (missingNumber(m))

k = [1,1]
print (missingNumber(k))

# do I need to handle this?
l = [12]
print (missingNumber(l))