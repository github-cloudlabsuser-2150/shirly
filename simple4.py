#Write a function that sorts a list of numbers using bubble sort.
#The function should take a list of numbers as an argument and return the list sorted in ascending order.
def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers
# Test the function with some example inputs
print(bubble_sort([5, 3, 8, 6, 7, 2])) # [2, 3, 5, 6, 7, 8]
print(bubble_sort([1, 2, 3, 4, 5])) # [1, 2, 3, 4, 5]
print(bubble_sort([5, 4, 3, 2, 1])) # [1, 2, 3, 4, 5]
print(bubble_sort([1, 3, 2, 5, 4])) # [1, 2, 3, 4, 5]

#Write a function that converts a decimal number to binary. The function should take a decimal number as an argument and return a string containing the binary representation of the number.
def decimal_to_binary(n):
    if n == 0:
        return "0" 
    else:
        return decimal_to_binary(n // 2) + str(n % 2)
# Test the function with some example inputs
print(decimal_to_binary(0)) # "0"
print(decimal_to_binary(1)) # "1"
print(decimal_to_binary(10)) # "1010"
print(decimal_to_binary(42)) # "101010"

#Write a function that calculates the area of a circle given its radius.
#The function should take a number as an argument and return the area of the circle with that radius.
def circle_area(radius):
    return 3.14159 * radius ** 2
# Test the function with some example inputs
print(circle_area(1)) # 3.14159
print(circle_area(2)) # 12.56636
print(circle_area(3)) # 28.27431