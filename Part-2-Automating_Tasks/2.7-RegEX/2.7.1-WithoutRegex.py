# Write a program that extracts just numbers from a message. 

message = " Hi there. This is my number: 415-555-4242. Alternatively, you can also reach me at: 415-666-4242."
message1 = "Radmodm message without any phone number in it!!!"
def checkIfPhoneNumber(number):
    if len(number)!= 12:
        return False

    for i in range(0,3):
        if not number[i].isdigit():
            return False
    if number[3] != '-':
        return False
    for i in range(4,7):
        if not number[i].isdigit():
            return False
    if number[7] != '-':
        return False
    for i in range(8,12):
        if not number[i].isdigit():
            return False

    return True

found = False

for i in range(len(message1)):
    chunk = message1[i:i+12]
    if checkIfPhoneNumber(chunk):
        print (f"Phone number is: {chunk}\n")
        found = True

if found == False:
    print("No phone numbers were found")