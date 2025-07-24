#Q1) Write a program to remove an item from the set. 

my_set = {10, 20, 30, 40, 50}
element = 30

my_set.discard(element)
print("Updated set:", my_set)

#Q2) Write a program to create an intersection of sets. 

set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

intersection = set1 & set2
print("Intersection of sets:", intersection)

#Q3) Write a program to create a union of sets. 

set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

union_set = set1 | set2
print("Union of sets:", union_set)

#Q4) Write a program to find the maximum and the minimum value from the set.

my_set = {15, 25, 35, 45, 5, 60}

max_val = max(my_set)
min_val = min(my_set)

print("Maximum value:", max_val)
print("Minimum value:", min_val)
