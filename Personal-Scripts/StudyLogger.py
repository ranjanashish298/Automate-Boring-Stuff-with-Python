# Study Logger v1
    
# Requirements:
    # Ask what you studied.
    # Ask how many minutes.
    # Ask what you learned.
    # Save the result to study_log.txt.
    # Run it multiple times without deleting previous entries.

import datetime

name="Ashish"

print(f"Welcome {name}! What did you study today?")
whatIStudied = input()
print(f"Great that you studied {whatIStudied}!")

print("And how many hours?")
time = int(input())
print(f"So we studied {whatIStudied} for {time} hours.")

date = datetime.datetime.now()
dateToday= date.strftime("%x")
print("Today's date is: " + dateToday)


#################################
def stringChecker():
    flag=True 
    if whatIStudied.isdigit():
        flag = False
    elif whatIStudied == "":
        flag = False
    elif whatIStudied[0].isdigit():
         flag = False
    elif whatIStudied[0] == '-':
         flag = False
    return flag
#################################

## File opening, writing and closing 
file = open("studyLogger.txt")

#write the file
with open ("studyLogger.txt", "a") as file:
        isEnteredStringValid = stringChecker() 
        if isEnteredStringValid==True:      
            file.write(f"{whatIStudied}--{time}--{dateToday}\n")
            openFile = True
        else:   
            print("Please enter a valid string for what you studied.")
            openFile = False

#close before reading again
file.close()

#read the whole file again
if openFile == True:
    file = open("studyLogger.txt")
    print(file.read())