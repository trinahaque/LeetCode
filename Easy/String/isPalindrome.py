def isPalindrome(s):
    # if only one character, it should be true
    if len(s) < 2:
        return True

    i = 0
    j = len(s) - 1

    while i <= j:
        # if the character is a special character or space
        if s[i].isalnum() == False and i < j:
            i += 1
            continue
        elif s[j].isalnum() == False and i < j:
            j -= 1
            continue
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True

# Time Complexity: O(n) [more like n/2]
# Space Complexity: O(1) constant. Only storing j and j
def isPalindromeOptimized(s):
    if len(s) < 2:
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
print (isPalindromeOptimized(false))
