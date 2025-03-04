# Write a function that checks if a given string is a palindrome.
# A palindrome is a string that reads the same forwards and backwards.
# Example: "racecar" is a palindrome.
# The function should take a string as an argument and return True if the string is a palindrome and False otherwise.
def is_palindrome(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and is_palindrome(s[1:-1])
    
# Test the function with some example inputs
print(is_palindrome("racecar")) # True
print(is_palindrome("hello")) # False
print(is_palindrome("a")) # True
print(is_palindrome("")) # True
print(is_palindrome("abba")) # True