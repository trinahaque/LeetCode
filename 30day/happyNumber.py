# Time Complexity: O(N^2)--> while loop and for loop
# Space Complexity: O(N)?
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

print(isHappy(2))
