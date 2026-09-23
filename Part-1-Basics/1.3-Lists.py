#allMyFriends.py
#Enter names of all your friends in a sorted order! 

nameList = []

i=1

while True:
    print(f"Enter name of your {i} friend")
    name = input()
    #nameList = nameList + [name]
    nameList = nameList.append(name)
    i = i + 1

    if name == '':
        break

# Sort the names
newList = sorted(nameList)

for names in newList:
     print(names)

