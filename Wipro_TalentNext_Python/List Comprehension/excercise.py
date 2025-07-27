#Q1) Create an output dictionary using list comprehension containing only the odd numbers from the list 
# [1, 2, 3, 4, 5, 6, 7] as keys, and their cubes as values.

input_list = [1, 2, 3, 4, 5, 6, 7]
output_dict = {x: x**3 for x in input_list if x % 2 != 0}

#Q2) Make a dictionary of the 26 lowercase English alphabets, mapping each letter to its corresponding integer 
# from 1 to 26.

import string
alphabet_dict = {letter: index + 1 for index, letter in enumerate(string.ascii_lowercase)}

