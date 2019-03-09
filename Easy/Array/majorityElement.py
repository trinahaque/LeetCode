# Time Complexity: O(n+m) or linear
# Space Complexity: O(n)

def majorityElement(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n) space
        dict = {}

        # O(n) time
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        max = 0
        
        # O(m) time
        for key in dict.keys():
            if dict[key] > max:
                max = dict[key]
                result = key
        
        if max >= len(nums)/2:
            return result

arr = [3, 2, 3]
print (majorityElement(arr))