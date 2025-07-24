#                                               EXERCISES

#Q1. Write a program to check if a given number is Positive, Negative or Zero.

def check_number(number):
    
    number = int(number)
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

number = input()
result = check_number(number)
print(result)

#Q2. Write a program to check if a given number is odd or even.

def evenOdd(number):

    number = int(number)
    if number == 0:
        return "Zero"
    
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

number = input()
result = evenOdd(number)
print(result)

#Q3. Given two non-negative values, print true if they have the same last digit, such as with 27 and 57

def checkLast(number):

    if number.endswith("27") or number.endswith("57"):
        return "True"
    else:
        return "False"



number = input()
result = checkLast(number)
print(result)

#Q4. Write a program to print numbers from 1 to 10 in a single row with one tab space.

for x in range(1,11):
    print(x, end=" ")

#Q5. Write a program to print even numbers between 23 and 57. Each number should be printed in a seperate row.

start = 23
end = 57

for x in range(start, end+1):
    if x % 2 == 0:
        print(x)

#Q6. Write a program to check if a given number is prime or not.

def check_prime(number):
    if number <= 1:
        return "The number is not a prime number."
    if number == 2:
        return "The number is a prime number."
    if number % 2 == 0:
        return "The number is not a prime number."
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return "The number is not a prime number."
    return "The number is a prime number."

number = int(input())
result = check_prime(number)
print(result)

#Q7. Write a program to print prime numbers between 10 and 99.

def print_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for num in range(1, 100):
    if print_prime(num):
        print(num, end=' ')

#Q8. Write a program to print the sum of all the digits of a given number.

def print_sum(number):

    sum = 0
    for x in number:
        a = int(x)
        sum += a
    
    return sum

number = input()
result = print_sum(number)
print(result)

#Q9. Write a program to reverse a given number and print.

number = input()
n = len(number)-1

for x in range(len(number)):
    i = n - x
    print(number[i], end="")

#Q10. Write a program to find if the given number is palindrom or not.

def palindrome(number):
    n = len(number) - 1

    for x in range(len(number)):
        i = n - x
        if number[i] == number[x]:
            pass
        else:
            return "No"
    
    return "Yes"

number = input()
result = palindrome(number)
print(result)

