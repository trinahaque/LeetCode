# Time Complexity: O(n) [more like n/2]
# Space Complexity: O(1) constant. Only storing j and j
# Doesn't handle case when there are multiple special characters
def isPalindromeOptimized(s):
    if len(s) < 2 and s[0].isalnum() == False:
        return False
    else: 
        return True
    i, j = 0, len(s) - 1
    while (i <= j):
        while s[i].isalnum() == False and i < j:
            i += 1
        while s[j].isalnum() == False and i < j:
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True


true = "A man, a plan, a canal : Panama"
false = "race e car! d"
tacocat = "tacocat"
lam = "!"
print (isPalindromeOptimized(lam)