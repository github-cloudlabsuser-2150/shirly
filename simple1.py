# Write a function that returns the factorial of a given number.
# The function should take an integer as an argument and return the factorial of that number.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Test the function with some example inputs
print(factorial(10)) # 120