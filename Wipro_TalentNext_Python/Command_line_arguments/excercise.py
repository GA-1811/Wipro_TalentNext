#Q1) Write a program to accept two numbers as command line arguments and display their sum.

import sys

if len(sys.argv) != 3:
    print("Please provide exactly two numbers as command line arguments.")
    sys.exit(1)

try:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
except ValueError:
    print("Both arguments must be numbers.")
    sys.exit(1)

print("Sum:", num1 + num2)

#Q2) Write a program to accept a welcome message through command line and display the file name along with 
# the message.

import sys

if len(sys.argv) != 2:
    print("Please provide a welcome message as a command line argument.")
    sys.exit(1)

file_name = sys.argv[0]
welcome_message = sys.argv[1]

print("File Name:", file_name)
print("Welcome Message:", welcome_message)

#Q3) Write a program to accept 10 numbers as command line arguments and calculate the sum of prime numbers 
# among them.

import sys

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

if len(sys.argv) != 11:
    print("Please provide exactly 10 numbers.")
    sys.exit(1)

try:
    numbers = [int(arg) for arg in sys.argv[1:]]
except ValueError:
    print("All arguments must be integers.")
    sys.exit(1)

prime_sum = sum(num for num in numbers if is_prime(num))
print("Sum of prime numbers:", prime_sum)