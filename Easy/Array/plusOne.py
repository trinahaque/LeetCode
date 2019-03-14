# Time Complexity: On + On --> On
# Space Complexity: O(n) for creating a new array
def plusOne(digits):
    
    sum = ""
    # On
    for num in digits:
        sum += str(num)
    sum = int(sum) + 1
    # On time and space
    return [int(n) for n in str(sum)]

digits = [9, 9, 9]
print (plusOne(digits))

digits = [1, 2, 3]
print (plusOne(digits))
