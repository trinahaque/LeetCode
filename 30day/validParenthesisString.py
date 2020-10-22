def checkValidString(s):
    openStack = []
    starStack = []

    # Check if all ) is accounted for
    for i in range(len(s)):
        if s[i] == "(":
            openStack.append(i)
        elif s[i] == "*":
            starStack.append(i)
        else:
            if len(openStack) > 0:
                openStack.pop()
            elif len(starStack) > 0:
                starStack.pop()
            # means both open and star stacks are empty
            else:
                return False
    
    # Check if all ( is accounted for
    # traversed through the whole string
    # check if openStack still has some (
    while len(openStack) > 0:
        # this means more ( without any match
        if len(starStack) == 0:
            return False
        # * index comes before ( index
        elif openStack[len(openStack)-1] < starStack[len(starStack)-1]:
            openStack.pop()
            starStack.pop()
        else:
            return False
    return True

s = "()"
print(checkValidString(s))
                
