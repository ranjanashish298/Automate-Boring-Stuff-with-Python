# I want to have a random quiz for me. I have 10 students and I want 10 different Q/A's for them. 
# Quiz 1 - 10 question -->  quiz1.txt, 10 answer keys --> quiz1answer.txt
# Quiz 2 - 10 question --> quiz2.txt, 10 answers --> quiz2answer.txt
# . . .. Quiz10 --> 10 questions --> quiz10.txt, 10 answers --> quiz10answer.txt

# Each quiz --> header + 10 questions listed with 4 MCQ options. 


## Let's try to create two files first and write to these two files. 

def quizHeaderContent():
    return '''Darmstadt University of Applied Sciences
Name:
Matriculation Number: 
\n
'''

#Create 2 quizzes and quiz answers 
# for i in range(1,3):
#     quiz = open(f"Quiz{i}.txt", "x")
#     #quizAns = open(f"Quiz{i}_ans.txt", "x")

# for i in range(1,3):
#     with open(f"Quiz{i}.txt", "a") as f:
#         f.write(quizHeaderContent())


quizQuesAndAnswers = {
    'Delhi':'New Delhi', 'Goa': 'Panaji',
    'Rajasthan' : 'Jaipur', 'Maharashtra':'Mumbai', 'Colombia': 'Bogota', 
    'Vietnam':'Ho Chin Min', 'Germany':'Berlin', 'UK':'London', 'France':'Paris',
    'Bosnia':'Sarajevo', 'Italy':'Rome', 'Spain': 'Madrid', 'Switzerland': 'Bern'
}

import random
listOfCities = []

for i in range (5):
    capitalList = ["","","",""]
    mcqPosition = random.randrange(0,4)
    place, realCapital = random.choice(list(quizQuesAndAnswers.items()))

    while place in listOfCities:
        place, realCapital = random.choice(list(quizQuesAndAnswers.items()))
    listOfCities.append(place)

    print(f"What is the capital of {place}?")
    capitalList[mcqPosition] = realCapital

    for i in range(4): 
        if capitalList[i]=="":
            newCapitalCity = random.choice(list(quizQuesAndAnswers.values()))
            while newCapitalCity in capitalList:
                newCapitalCity = random.choice(list(quizQuesAndAnswers.values()))
            capitalList[i] = newCapitalCity

    for i in range(0,4):
        print(f"{i+1}. " + capitalList[i])
