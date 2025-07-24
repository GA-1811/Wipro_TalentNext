#Q1)  Write a program to crate a list of 5 integers and display the list items.Access the indivisual items 
# of the list.

llist = [1,2,3,4,5]

for x in llist:
    print(x)

#Q2) Write a program to append a new item to the end of the list. 

llist = [1,2,3,4,5]
item = 6

llist.append(item)

#Q3) Write a program to reverse the order of the items in the list.

llist = [1,2,3,4,5]
ll = llist[::-1]

#Q4) Write a program to print the number of occurance of a specified number in a list. 

llist = [1,2,5,3,4,5,5]
specified_number = 5
count = 0

for x in llist:
    if x == specified_number:
        count += 1

#Q5) Write a program to append the item of list to list2 at the front.

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

for x in range(len(list1)):
    list2.insert(0,list1[x])

#Q6) Write a program to insert a new item before the second element in the existing list.

llist = [1,2,3,4,5]
number = 6

llist.insert(1, number)
print(llist)

# Q7) Write a program to remove the item from a specified index in a list.

llist = [1,2,3,4,5]
index = 3

llist.remove(llist[index])

# Q8) Write a progam to remove the first occurance of the specified element from a list.

llist = [1,2,5,3,4,5]
specified_element = 5 
a = 1

for x in llist:
    if a > 0 and x == specified_element:
        llist.remove(x)
        a = 0
