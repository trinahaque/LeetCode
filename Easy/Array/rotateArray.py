def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    k = k % len(nums)
    i = 0
    while i < k:
        nums[i], nums[i+k-len(nums)] = nums[i+k-len(nums)], nums[i]
        # print ("nums at ", i , " is ", nums)
        i = i + 1
    return nums

def rotateArr(arr, r):
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(arr) < 2:
            return arr
        reverseArr(arr, 0, len(arr)-r-1)
        reverseArr(arr, r, len(arr)-1)
        reverseArr(arr, 0, len(arr)-1)
        return arr
        
    
def reverseArr(arr, start, end):
    middle = int((end - start) / 2)
    
    for i in range(middle + 1):
        arr[start + i], arr[end - i] = arr[end - i], arr[start + i]
    return arr

def reverse(nums):
    if len(nums) < 2:
        return nums
    mid = int(len(nums)/2)
    for i in range(mid):
        nums[i], nums[len(nums)-1-i] = nums[len(nums)-1-i], nums[i]
    return nums

nums = [1, 2, 3, 4, 5, 6]
nums2 = [5, 6]
print (reverse(nums))
# k = 3
# print(rotate(nums, k))

nums = [-1, -100, 3, 99]
k = 1
# print(rotateArr(nums, k))