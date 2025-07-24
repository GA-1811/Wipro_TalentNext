# Q1) Write a program to add key and value pair in a dictionary.

my_dict = {0: 10, 1: 20}
my_dict[2] = 30

#Q2) Write a program to concatenate the following dictionaries to a new one.
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}

result = {}
result.update(dic1)
result.update(dic2)
result.update(dic3)
print(result)

#Q3) Write a program to check if a given key already exist in a dictionary.

my_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_check = 'b'

if key_to_check in my_dict:
    print("Yes")
else:
    print("No")

#Q4) Write a program to iterate over a dictionary using a for loop and print the keys alone, values alone and 
# both keys and values.

my_dict = {'name': 'Garvit', 'age': 21, 'city': 'Bhopal'}

print("Keys:")
for key in my_dict:
    print(key)

print("Values:")
for value in my_dict.values():
    print(value)

print("Key-Value Pairs:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

#Q5) Write a program to prepare a dictionary where the keys are numbers between 1 and 15 (both included), 
# and the values are the squares of the keys.

user_dict = {}

for x in range(1, 16):
    user_dict[x] = x * x

print(user_dict)

#Q6) Write a Python program to sum all the values in a dictionary, assuming the values are of int type.

my_dict = {'a': 100, 'b': 200, 'c': 300}
total = 0

for value in my_dict.values():
    total += value

print("Sum of values:", total)