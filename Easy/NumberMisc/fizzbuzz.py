# Write a program that outputs the string representation of numbers from 1 to n.
# Multiples of 3 will print "Fizz", multiples of 5 will output "Buzz"
# Multiples of both 3 and 5 will output "FizzBuzz"

def fizzbuzz(n):
    result = []
    if n == 0:
        return result
    m = 1
    while(m <= n):
        if m % 3 == 0 and m % 5 == 0:
            result.append("FizzBuzz")
        elif m % 3 == 0:
            result.append("Fizz")
        elif m % 5 == 0:
            result.append("Buzz") 
        else:
            result.append(str(m))   
        m += 1
    return result

print(fizzbuzz(1))