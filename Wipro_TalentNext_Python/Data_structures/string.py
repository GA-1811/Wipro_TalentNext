#Q1) Write a program to count the number of upper and lower case letter in a string.

string = "My Name is Garvit"
count_upper = 0
count_lower = 0

for x in string:
    if x == x.upper() and x != " ":
        count_upper += 1
    elif x == x.lower() and x != " ":
        count_lower += 1

print(count_upper)
print(count_lower)

#Q2) Write a program to check the given string is palindrome or not.

string = "aaaabaa"
reversed = string[::-1]

if string == reversed:
    print("Yes")
else:
    print("No")

#Q3) Given a string, return a new string made of n copies of the first 2 characters of the original string, 
# where n is the length of the string. The string length will be ≥ 2.

string  = "Wipro"
n = len(string)

if n >= 2:
    a = string[:2]
    new_string = n*a
    print(new_string)
else:
    print("The input is too low to be printed.")

#Q4) Given a string, if the first or last character is 'x', return the string without those 'x' characters. 
# Otherwise, return the string unchanged.

string  = "xHellox"

if string.startswith("x") and string.endswith("x"):
    print(string[1:-1])

#Q5) Given a string and an integer n, return a string made of n repetitions of the last n characters of the 
# string. You may assume that n is between 0 and the length of the string, inclusive.

string  = "Wipro"
n = 3

a = string[2:]
new_string = a * n
print(new_string)

