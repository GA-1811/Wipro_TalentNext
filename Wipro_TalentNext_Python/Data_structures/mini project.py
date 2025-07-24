#------------------------------------------------MINI PROJECT-----------------------------------------------

#Create a dictionary that contains a list of people and one interesting fact about each of them. Display each 
# person and their interesting fact. Then: Change a fact about one of the people, Add an additional person and
# their fact, Display the updated list, Run the program multiple times to observe whether the order changes.

people_facts = {
    "Einstein": "He loved playing the violin.",
    "Curie": "She was the first woman to win a Nobel Prize.",
    "Tesla": "He had a photographic memory."
}

print("Original facts:")
for person, fact in people_facts.items():
    print(f"{person}: {fact}")

people_facts["Tesla"] = "He once lit 200 lamps without wires using wireless transmission."
people_facts["Newton"] = "He invented calculus in his spare time."

print("Updated facts:")
for person, fact in people_facts.items():
    print(f"{person}: {fact}")


# Given the participant’s score sheet for your University Sports Day, you are required to find the runner-up 
# score. You have scores. Store them in a list and find the score of the runner-up.

scores = [2,3,5,8,6]
first = max(scores)
runner_up = 0

for x in scores:
    if x < first and x > runner_up:
        runner_up = x

print(runner_up)


# Given a string of  words, help Alex find how many times his name appears in the string.

string = "Hi Alex WelcomeAlex Bye Alex"
target = "Alex"
string = string.replace(" ", "")

count = string.count(target)
print(count)

 
# You have a record of n students. Each record contains the strudent's name, and their percent marks inMaths, 
# Physics and Chemistry. The marks can be floating values. You are required to save the record in a dictionary 
# data type. Student's name is the key. Marks stored in a list is the value. The user enters a student's name. 
# Output the average percentage marks obtained by that student. 

marks_dict = {
    "Krishna": [67, 68, 69],
    "Arjun": [70, 98, 63],
    "Malika": [52, 56, 60]
}

name = input("Enter a name: ")

if name in marks_dict:
    marks = marks_dict[name]
    average = sum(marks) // len(marks) 
    print("Average percentage mark:", average)
else:
    print("No such record found.")