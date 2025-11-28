# Write a program that attempts to open and read data from a file specified by the user.
# It should handle the FileNotFoundError exception to inform the user if the file does not exist.

file_name = input("Enter the file name to read: ")
try:
    with open(file_name, 'r') as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("File not found. Please check the file name and try again.")
finally:
    print("Execution completed")