
def moveZeroes(nums):
    # p is a pointer to 0
    p = 1
    # q is a pointer to non zero
    q = 0
    for i in range(len(nums)):
        if nums[i] == 0 and p < q:
            nums[i], nums[q] = nums[q], nums[i]
        for j in range((i+1), len(nums)):
            if nums[j] == 0:
                p = j
                break
        for k in range((i+1), len(nums)):
            if nums[k] != 0:
                q = j
                break
    return nums
nums = [1, 0, 0, 3, 12]
print(moveZeroes(nums))
