#Time Complexity --> O(n) --> 2 loops, O(n) + O(n)
#Space Complexity --> O(n) --> 1 Hash map
def singleNumber(nums):
    # hashset can have default value of 1 during creation
    frequencyDict = {}
    for number in nums:
        if number in frequencyDict:
            frequencyDict[number] += 1
        else:
            frequencyDict[number] = 1
    for key in frequencyDict:
        if frequencyDict[key] == 1:
            return key

nums = [2, 2, 1]
print(singleNumber(nums))

nums = [4, 1, 2, 1, 2]
print(singleNumber(nums))