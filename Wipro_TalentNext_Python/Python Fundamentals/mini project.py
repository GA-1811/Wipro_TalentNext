#1. 1.	create a python program that asks the user how far they want to travel. if they want to travel less 
# than three miles tell them to ride Bicycle. if they want to travel more than three miles, but less than 
# three hundred miles, tell them to ride Motor-cycle. if they want to travel three hundred miles or more tell 
# them to driver Super-Car.

def recommendation(text):
    if 0 < text <= 3:
        return "Bicycle"
    elif 3 < text < 300:
        return "Motor-cycle"
    elif text >= 300:
        return "Super-Car"
    else:
        return "you don't need to leave"
    

text = int(input("How would you like to travel in miles? "))
result = recommendation(text)
print(f"I suggest {result} to your destination.")

#2 2.	Let's assume you are planning to use your python skills to build an App for Mobile.
# You decide to host your application on servers running in the cloud. you pick a hosting provider that 
# charges $0.51 per hour. you will launch your services using one server and want to know how much it will 
# cost to operate per day, per week, per month.
# Write a python program that displays the answers to the following questions:

# How much does it cost to operate one server per day?
# How much does it cost to operate one server per week?
# How much does it cost to operate one server per month?
# How much days can I operate one server with $918?

charges = 0.51

user = input() # How much does it cost to operate one server per day?
charges *= 24
print(charges)

user = input() # How much does it cost to operate one server per week?
charges *= (24 * 30) 
print(charges)

user = input() # How much does it cost to operate one server per month?
charges *= (24 * 30) * 12 
print(charges)

user = input() # How much days can I operate one server with $918?
charges *= 24
charges /= 918
print(charges)