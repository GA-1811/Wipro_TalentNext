#Write a Python function that accepts a hyphen-separated sequence of color names as input and returns the 
# colors in a hyphen-separated sequence after sorting them alphabetically.

def sort_colors(color_sequence):

    color_list = color_sequence.split('-')
    color_list.sort()
    sorted_sequence = '-'.join(color_list)

    return sorted_sequence

input = "green-red-yellow-black-white"
result = sort_colors(input)
print(result)


# Create a python module with the fucntions: ispalindrome(name), count_the_vowels(name),
# frequency_of_letters(name)

class NameAnalyzer:
    def __init__(self, name):
        self.name = name

    def ispalindrome(string):
        return string == string[::-1]

    def count_the_vowels(string):
        vowels = "aeiouAEIOU"
        count = 0

        for x in string:
            if x in vowels:
                count += 1
        
        return count

    def frequency_of_letters(string):
        freq_dict = {}
        for x in string:
            freq_dict[x] = freq_dict.get(x, 0) + 1
        return freq_dict