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
time = input()
print(f"So we studied {whatIStudied} for {time} hours.")

date = datetime.datetime.now()
dateToday= date.strftime("%x")
print("Today's date is: " + dateToday)

file = open("studyLogger.txt")
with open ("studyLogger.txt", "a") as file:
    file.write(f"{whatIStudied}--{time}--{dateToday}")
