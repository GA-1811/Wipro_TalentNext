#Q1) Write a program to print the 4th element from the first and the 4th element from the last in a tuple.

my_tuple = (10, 20, 30, 40, 50, 60, 70, 80)

print("4th element from the first:", my_tuple[3])
print("4th element from the last:", my_tuple[-4])

#Q2) Write a program to check whether an element exist in the tuple or not. 

my_tuple = (10, 20, 30, 40, 50)
element = 30

if element in my_tuple:
    print(f"{element} exists in the tuple.")
else:
    print(f"{element} does NOT exist in the tuple.")

#Q3) Write a program to convert a list into tuple.

my_list = [10, 20, 30, 40, 50]
my_tuple = tuple(my_list)

print("Converted tuple:", my_tuple)

#Q4) Write a program to find the index of an item in a tuple.

my_tuple = (10, 20, 30, 40, 50)
item = 30

if item in my_tuple:
    index = my_tuple.index(item)
    print(index)
else:
    print("Index not found.")

#Q5) Write a Python program to replace the last value of each tuple in a list to 100.

sample_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
updated_list = [(a, b, 100) for (a, b, c) in sample_list]

print(updated_list)