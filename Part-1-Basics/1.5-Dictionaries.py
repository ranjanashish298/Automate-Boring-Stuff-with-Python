#Saving birthday of my friends in a dictionary
birthdays = {'Ashish': 'July 18', 'Apoorb': 'July 07', 'Nata': 'June 21'}

print("Enter the name of your friend to check their birthday")
name = input().lower()

while True: 

    if name  in birthdays:
        print(f"{name}'s birthday is on - {birthdays[name]}")
        break
    else:
        print("Name not found in the Database! Please enter the name.")
        newName = input()
        print("Please enter their birthday")
        newBirthday = input()
        birthdays[newName] = newBirthday
        print("Database updated successfully....Try checking for their birthday again!")


#check number of occurences:
message = "check number of occurences..."
occurences = {}
for char in message:
    occurences.setdefault(char, 0)
    occurences[char] = (occurences[char] + 1) 

print(occurences)


#Tic-Tac-Toe Game - in other file Personal-Scripts/Tic-Tac-Toe.py