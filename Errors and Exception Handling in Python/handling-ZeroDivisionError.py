# Write a program that takes two numbers as input from the user.
# It should divide the first number by the second number.
# It should handle the ZeroDivisionError exception to inform the user if they attempt to divide by zero.

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

try:
    print(int(num1) / int(num2))
except ZeroDivisionError:
    print("Division by zero not allowed")
finally:
    print("Execution completed")                     

