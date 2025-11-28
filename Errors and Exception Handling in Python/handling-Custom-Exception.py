# Create a custom exception class called ValueTooHighError that inherits from the Exception class.
# Write a program that takes a number as input from the user.
# If the number is greater than 100, raise the ValueTooHighError exception.

class ValueTooHighError(Exception):
    """Custom exception raised when the input value is too high."""
    pass
try:
    number = int(input("Enter a number: "))
    if number > 100:
        raise ValueTooHighError("The value is too high!")
except ValueError:
    print("Error: Please enter a valid number.")
except ValueTooHighError as e:
    print(f"Custom Exception: {e}")
finally:
    print("Program has ended.")