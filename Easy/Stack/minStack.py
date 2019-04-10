# Time Complexity: Constant (just return the last value)
# Space Complexity: O(n) --> for the minStack

class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minVals = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if len(self.minVals) == 0:
            self.minVals.append(x)
        else:
            if x <= self.minVals[- 1]:
                self.minVals.append(x)
        

    def pop(self):
        """
        :rtype: None
        """
        popVal = self.stack.pop()
        if popVal == self.minVals[- 1]:
            self.minVals.pop()

        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[- 1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minVals[- 1]
        


minStack = MinStack()
minStack.push(0)
minStack.push(1)
minStack.push(0)
print (minStack.getMin())
minStack.pop()
print (minStack.getMin())

