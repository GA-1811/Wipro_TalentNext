#Your friend has sent you a text file containing n lines. He sent a secret message with it, which tells you the 
#place and time where you have to go and meet him. He challenges you ti find it out without seeing content of 
#the file. He has given hints to find it. Let's surprise him by breaking the challenge with out python code.

from collections import Counter

def extract_meeting_details(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            line_count = len(lines)
            
            if line_count > 12:
                meeting_hour = line_count % 12
                meeting_time = f"{meeting_hour or 12} PM"
            else:
                meeting_time = f"{line_count} AM"
    
            words = []
            for line in lines:
                words.extend(line.strip().split())
            
            word_freq = Counter(words)
            meeting_place = word_freq.most_common(1)[0][0]
            
            print(f"Meeting Time: {meeting_time}")
            print(f"Meeting Place: {meeting_place}")
    
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("error:", e)

extract_meeting_details("secret.txt")