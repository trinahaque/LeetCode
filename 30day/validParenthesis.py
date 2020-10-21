def checkValidString(s):
    openStack = []
    starStack = []
    for i in range(len(s)):
        if s[i] == "(":
            openStack.append(i)
        elif s[i] == "*":
            starStack.append(i)
        else:
            if len(openStack) == 0 and len(starStack) == 0:
                return False
            else:
                if len(openStack) > 0:
                    openStack.pop()
                elif len(starStack) > 0:
                    starStack.pop()
    if len(openStack) > 0 and len(starStack) == 0:
        return False
    elif len(openStack) > 0 and len(starStack) > 0:
        # will be a case when we have * * (
        if openStack.pop() > starStack.pop():
            return False
    return True

s = "()"
print(checkValidString(s))
                
