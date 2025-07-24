#Through command line arguments, three strings separated by spaces are given to you. Each string is a series 
# of numbers separated by hyphens (-). You like all the numbers in string 1 and dislike all the numbers in 
# string 2. The third string contains the numbers given to you. Your initial happiness is 0. For each number 
# in the third string: If it’s present in string 1, add 1 to happiness, If it’s present in string 2, subtract
# 1 from happiness otherwise happiness stays the same. Output your final happiness at the end.

import sys

def calculate_happiness(likes, dislikes, numbers):
    likes_set = set(likes.split('-'))
    dislikes_set = set(dislikes.split('-'))
    numbers_list = numbers.split('-')
    
    happiness = 0
    for number in numbers_list:
        if number in likes_set:
            happiness += 1
        elif number in dislikes_set:
            happiness -= 1
    return happiness

if len(sys.argv) != 4:
    print("Please provide exactly three strings separated by spaces.")
    sys.exit(1)

likes = sys.argv[1]
dislikes = sys.argv[2]
numbers = sys.argv[3]

result = calculate_happiness(likes, dislikes, numbers)
print("Final happiness:", result)
