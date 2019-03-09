
# Time Complexity: O(n)
# Space Complexity: O(n)

def containsDuplicates(nums):
    if len(nums) < 2:
        return False
    # O(n) space
    dict = {}
    
    # O(n) time
    for i in nums:
        if i in dict:
            return True
        else:
            dict[i] = 1
    return False

arr = [1, 2, 3, 4]
print (containsDuplicates(arr))