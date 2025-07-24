#Q1) Write a program to accept two numbers from the user and perform division. If any exception occurs, print 
# an error message, otherwise print the result.

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    result = a / b
    print("Division result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid numbers.")
except Exception as e:
    print("Unexpected error:", e)

#Q2) Write a program to accept a number from the user and check whether it's prime or not. If the user enters 
# anything other than a number, handle the exception and print an error message.

try:
    num = int(input("Enter a number: "))
    if num <= 1:
        print("Not a prime number.")
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                print("Not a prime number.")
                break
        else:
            print("Prime number!")
except ValueError:
    print("Error: Please enter a valid integer.")

#Q3) Write a program to accept the file name from the user. If the file exists, print the contents in title 
# case, or else handle the exception and print an error message.

file_name = input("Enter the file name: ")

try:
    with open(file_name, "r") as f:
        for line in f:
            print(line.title().strip())
except FileNotFoundError:
    print("Error: File not found.")

#Q4) Declare a list with 10 integers and ask the user to enter an index. Check whether the number at that index 
# is positive or negative. If an invalid index is entered, handle the exception and print an error message.

numbers = [3, -2, 5, -7, 0, 8, -1, 6, -4, 9]

try:
    idx = int(input("Enter an index (0 to 9): "))
    value = numbers[idx]
    if value > 0:
        print("Positive number.")
    elif value < 0:
        print("Negative number.")
    else:
        print("Number is zero.")
except IndexError:
    print("Error: Invalid index. Must be between 0 and 9.")
except ValueError:
    print("Error: Please enter a valid integer index.")
