# Notes

# Variables will contain references to list rather than list values
# themselves. But for strings and integer values, variables simply contain the
# string or integer value. Python uses references whenever variables must
# store values of mutable data types, such as lists or dictionaries. For values
# of immutable data types such as strings, integers, or tuples, Python vari-
# ables will store the value itself.


#allMyFriends.py
#Enter names of all your friends in a sorted order! 

nameList = []

i=1

while True:
    print(f"Enter name of your {i} friend")
    name = input()
    #nameList = nameList + [name]
    nameList.append(name)
    i = i + 1

    if name == '':
        break

#Sort the names
newList = sorted(nameList)

for names in newList:
     print(names)


# Comma Code
spam = ['apples', 'bananas', 'tofu', 'cats', 4 ]
def callTheListFunction(givenList):

    for i in range(len(givenList)):
        if i == len(givenList) - 1 :
            spam[i] = "and "+ str(givenList[i])

callTheListFunction(spam)
print(spam)

# Have a list of names of your friends through input. 
# ash, ranjan, tiam, royal
# write a program that randoms the greeting messages for each name on each run.
# Hey, Ash! What's up Royal. On each run, the corresponding messages for users change randomly. 

import random

namesList = ["Ashish", "Josh", "Yaros", "Kevin"]

greetingMessages = ["Hey man, what's up?", 
                    "How are you doing bro",
                    "My brother, what's up with you?",
                    "Yo my bro, how are you doing?"]

for names in namesList:
    randomGreetings = random.randint(0, len(greetingMessages)-1)
    print(f"{names}, {greetingMessages[randomGreetings]}")