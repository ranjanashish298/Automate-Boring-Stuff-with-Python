# Takes a user name, print the total number of characters in their name and tell them how old they are based on their DOB. 
from datetime import datetime

print("Hello, what is your name?")
myName = input()
print("Welcome", myName)

totalChars= len(myName)
print(f"You have a total of {totalChars} characters")

print("Enter your Year of Birth")
dob=input()
currentYear = datetime.now().year
type(currentYear)
print(f"You are {currentYear-int(dob)} years old")