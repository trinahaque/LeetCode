# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid

"""
An input string is valid if:
1. Open brackets must be closed by the same type of brackets
2. Open brackets must be closed in the correct order.
"""

# {[]} --> True
# ([)]) --> False

# Time Complexity: O(n) to loop through every character in String + O(1) look up time
# Space Complexity: O(n) to store the stack. Worst case all char in string
# + Constact for the dict

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

# print (isValid("([]])"))

# Time Complexity: O(n) --> traverse string + O(m) --> dict.keys()
# Space Complexity: 0(m)--> dict + O(n) --> stack
def isValidParenthesis(s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 1:
            return True
        stack = []
        dict = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for i in range(len(s)):
            if s[i] not in dict.keys():
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                if stack.pop() != dict[s[i]]:
                    return False
        if len(stack) != 0:
            return False
        return True

s = ''
s1 = '('
s2 = '{([])}'
s3 = '{([])]}'
s4 = '{([{])]'

print (isValidParenthesis(s))
print (isValidParenthesis(s1))
print (isValidParenthesis(s2))
print (isValidParenthesis(s3))
print (isValidParenthesis(s4))
