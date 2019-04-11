# Time Complexity: O(n)
# Space Complexity: O(n)

import operator

def evalRPN(tokens):
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": lambda x, y: int(x/y)
    }
    # O(n)
    stack = []
    # O(n)
    for element in tokens:
        if element not in operators:
            stack.append(int(element))
        else:
            popFirst = stack.pop()
            popLast = stack.pop()
            stack.append(operators[element](popLast, popFirst))
    return stack.pop()

tokens = ["2", "1", "+", "3", "*"]
print (evalRPN(tokens))

tokens = ["4", "13", "5", "/", "+"]
print (evalRPN(tokens))

tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print (evalRPN(tokens))

tokens = ["4", "13", "5", "-", "-"]
print (evalRPN(tokens))

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print (evalRPN(tokens))