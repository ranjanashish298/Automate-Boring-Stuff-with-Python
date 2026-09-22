import random

def throwDice(number):
    if number == 1:
        return number
    elif number == 2:
        return number
    elif number == 3:
        return number
    else:
        return "You ended up in the other teil"

print(f"The number landed on dice is: {throwDice(random.randint(1,6))}")

# Local vs Global Scope
eggs = 0
def spam():
    eggs = 99
    bacon()
    print(eggs) #99

def bacon():
    eggs = 100
    print(eggs) #100

spam()
bacon()
print(eggs) #0


#guessTheNumber.py

randomNumber = random.randint(1,3)

print("Enter a number to see if you guessed it correctly!")
userGuess = input()
print(f"User guessed - {userGuess}")

if (int(userGuess) == randomNumber):
    print("You've found the same number")
else: 
    print(randomNumber)
    print("Oops, they are not the same number!")


#Collatz Sequence
def collatz(number):
    if number % 2 == 0:
        result = number // 2
        print(result)
        return result
    else: 
        result = number * 3 + 1
        print(result)
        return result


print("Enter a number:")
userInput = int(input())

try:
    endResult = userInput
    while endResult !=1:
        endResult = collatz(endResult)
except ValueError: 
    print("An exception occured!")        
