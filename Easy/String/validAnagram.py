# Given two strings s and t, write a function to determine if t is an anagram of s.
# s = ant, t = nat --> True
# s = cat, t = car --> False
# s = aab, t = baa --> True

# O(n) time complexity
# O(n) space complexity
def isAnagram(s, t):
    # false if two strings are of different length
    if len(s) != len(t):
        return False
    
    dict = {}
    # O(n) for the loop here
    # O(n) for space
    for i in range(len(s)):
        if s[i] in dict:
            dict[s[i]] += 1
        else:
            dict[s[i]] = 1
    
    # O(n) for the loop here
    for i in range(len(t)):
        # O(1) or constant look up
        if t[i] not in dict:
            return False
        elif dict[t[i]] == 0:
            return False
        else:
            dict[t[i]] -= 1
    return True

s = "aad"
t = "aaa"
print (isAnagram(s, t))