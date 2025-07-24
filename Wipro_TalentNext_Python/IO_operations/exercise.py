#Q1) Write a program to read the entire content from a text file and display it to the user.

with open("sample.txt", "r") as file:
    content = file.read()
    print("File content:\n", content)

#Q2) Write a program to read the first n lines from a text file. Get n as user input

n = int(input())

with open("sample.txt", "r") as file:
    for i in range(n):
        line = file.readline()
        print(line.strip())

#Q3) Write a program to accept input from the user and append it to a text file

data = input("Enter text to append: ")

with open("sample.txt", "a") as file:
    file.write(data + "\n")

#Q4) Write a program to read contents from a text file line by line and store each line into a list.

with open("sample.txt", "r") as file:
    lines = []
    for line in file:
        a = line.strip()
        lines.append(a) 

#Q5) Write a program to find the longest word from the text file. Assume there is only one longest word.

with open("sample.txt", "r") as file:
    words = file.read().split()

longest = max(words, key=len)
print("Longest word:", longest)

#Q6) Write a program to count the frequency of a user-entered word in a text file.

target = input("Enter the word to count: ").strip()

with open("sample.txt", "r") as file:
    words = file.read().split()

frequency = words.count(target)
print(frequency)