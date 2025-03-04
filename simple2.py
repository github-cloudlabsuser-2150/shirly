#Write a function that returns the nth Fibonacci number.
#The function should take an integer n as an argument and return the nth Fibonacci number.
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
# Test the function with some example inputs
print(fibonacci(10)) # 55
print(fibonacci(20)) # 6765
print(fibonacci(30)) # 832040