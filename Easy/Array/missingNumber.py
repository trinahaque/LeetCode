def missingNumber(n):
    nums = sorted(nums)
    if nums[0] != 0:
        return 0
    else:
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] > 1:
                return nums[i] + 1

n = [9,6,4,2,3,5,7,0,1]
print (missingNumber(n))