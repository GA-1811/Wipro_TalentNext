#Q1) Write a fuction to return the sum of all numbers in a list.

# def sum(llist):
#     total = 0

#     for x in llist:
#         total += x
    
#     return total

# llist = [8,2,3,0,7]
# result = sum(llist)
# print(result)

#Q2) Write a function to return the reverse of a string. 

# def reverse(s):
#     return s[::-1]

# s = "1234abcd"
# result = reverse(s)
# print(result)

#Q3) Write a function to calculate and return factorial of a number.

# def factorial(n):
#     if n < 0:
#         return "Factorial is not defined for negative numbers."
    
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
    
#     return result

# num = 5
# result = factorial(num)
# print(f"Factorial of {num} is : {result}")

#Q4) Write a function that accepts a string and print the number of upper case letters and lower case letters
# in it.

# def countUpper_andlower(string):
#     count_upper = 0
#     count_lower = 0

#     for x in string:
#         if x == x.upper() and x != " ":
#             count_upper += 1
#         elif x == x.lower() and x != " ":
#             count_lower += 1
    
#     return count_upper,count_lower

# string = "Hello My Name is Garvit"
# a, b = countUpper_andlower(string)
# print(a)
# print(b)

#Q5) Write a function to print the even number form a list. List is passed to the function as an argument.

# def even_number(llist):
    
#     for x in llist:
#         if x % 2 == 0:
#             print(x, end=" ")
        


# llist = [1,2,3,4,5,6,7,8,9]
# even_number(llist)

#Q6) Write a function that takes a number as a parameter and checks wheather the number is prime or not.

# def check_prime(number):
#     if number <= 1:
#         return "The number is not a prime number."
#     if number == 2:
#         return "The number is a prime number."
#     if number % 2 == 0:
#         return "The number is not a prime number."
#     for i in range(3, int(number ** 0.5) + 1, 2):
#         if number % i == 0:
#             return "The number is not a prime number."
#     return "The number is a prime number."

# number = 69
# result = check_prime(number)
# print(result)