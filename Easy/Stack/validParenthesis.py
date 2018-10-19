# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid

"""
An input string is valid if:
1. Open brackets must be closed by the same type of brackets
2. Open brackets must be closed in the correct order.
"""

# {[]} --> True
# ([)]) --> False

def isValid(s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                stack.append(s[i])
            elif s[i] in dict.keys():
                if len(stack) == 0:
                    return False
                elif stack[-1] != dict[s[i]]:
                    # print ("here", stack[-1])
                    return False
                else:
                    stack.pop()
        if len(stack) > 0:
            return False
        else:
            return True

print (isValid("([]])"))