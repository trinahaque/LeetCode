# Time Complexity: O(N^2)--> while loop and for loop
# Space Complexity: O(N)?
# look up fast/slow method
def isHappy(n):
    i = 0
    while i < 500:
        i += 1
        sum = 0
        # digits is an arry of each digit from n
        digits = [int(x) for x in str(n)]
        for number in digits:
            sum += (number)**2
        # n is back to the new sum
        n = sum
        if n == 1:
            return True
    return False

# print(isHappy(2))
# print(isHappy(4))
# print(isHappy(7))

# Using Set/HashSet
# If same number is seen in the Set, it means there is a cycle and it's False
def isHappy2(n):
    sumSet = set()

    # duplicate not seen yet
    while n not in sumSet:
        if n == 1:
            return True
        sumSet.add(n)
        # squaring and adding each digit to sum
        n = sum(int(i) ** 2 for i in str(n))  
    return False

print(isHappy2(2))
print(isHappy2(4))
print(isHappy2(19))