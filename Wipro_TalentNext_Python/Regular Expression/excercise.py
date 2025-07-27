#Q1) Write a program to check if strings have only octal digits.

def is_octal(s):
    for c in s:
        if c not in '01234567':
            return False
    return True

strings = ['789', '123', '004']
results = []
for s in strings:
    results.append(is_octal(s))

print(results)

#Q2) Extract user ID, domain name, and suffix from email addresses.

import re
emails = """zuck@facebook.com
sunder33@google.com
jeff42@amazon.com"""

pattern = r'(\w+)@(\w+)\.(\w+)'
matches = re.findall(pattern, emails)
for match in matches:
    print(f"User ID: {match[0]}, Domain Name: {match[1]}, Suffix: {match[2]}")

#Q3) Convert an irregular sentence into proper words.

import re

sentence = "A, very   very; irregular_sentence"
cleaned_sentence = re.sub(r'[^\w\s]', '', sentence)
cleaned_sentence = re.sub(r'\s+', ' ', cleaned_sentence)
print(cleaned_sentence) 

#Q4) Clean up the tweet so that it contains only the user's message. That is, Remove all URLs, hashtags, 
# mentions, punctuations, RTs, and CCs from a tweet.

import re

tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today 
http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''

cleaned_tweet = re.sub(r'http\S+', '', tweet)
cleaned_tweet = re.sub(r'@\w+', '', cleaned_tweet)
cleaned_tweet = re.sub(r'#\w+', '', cleaned_tweet)
cleaned_tweet = re.sub(r'RT', '', cleaned_tweet)
cleaned_tweet = re.sub(r'cc:', '', cleaned_tweet)
cleaned_tweet = re.sub(r'[^\w\s]', '', cleaned_tweet)
cleaned_tweet = re.sub(r'\s+', ' ', cleaned_tweet).strip()

print(cleaned_tweet)

#Q5) 

import requests
import re

url = "https://raw.githubusercontent.com/selva86/datasets/master/sample.html"
res = requests.get(url)
html = res.text

texts = re.findall(r'>([^<>]+)<', html)

for text in texts:
    print(text.strip())

#Q6) Given below are the list of words, identify the words that begin and end witht he same word. 

words = ['civic', 'trust', 'widows', 'maximum', 'museums', 'aa', 'as']

for w in words:
    if w[0] == w[-1]:
        print(w)

