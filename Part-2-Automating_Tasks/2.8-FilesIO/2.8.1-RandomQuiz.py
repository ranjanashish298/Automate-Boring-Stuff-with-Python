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

quizQuesAndAnswers = {
    'Delhi':'New Delhi', 'Goa': 'Panaji',
    'Rajasthan' : 'Jaipur', 'Maharashtra':'Mumbai', 'Colombia': 'Bogota', 
    'Vietnam':'Ho Chin Min', 'Germany':'Berlin', 'UK':'London', 'France':'Paris',
    'Bosnia':'Sarajevo', 'Italy':'Rome', 'Spain': 'Madrid', 'Switzerland': 'Bern'
}

import random


#for number of quizzes one would like to have! 
for totalQuiz in range(25):
    listOfCities = []
    quiz = open(f"Quiz{totalQuiz+1}.txt", "w")
    quizAns = open(f"Quiz{totalQuiz+1}_ans.txt", "w")

    quiz.write(quizHeaderContent())
    #for number of questions per Quiz 
    for i in range (10):
        capitalList = ["","","",""]
        mcqPosition = random.randrange(0,4)
        place, realCapital = random.choice(list(quizQuesAndAnswers.items()))

        while place in listOfCities:
            place, realCapital = random.choice(list(quizQuesAndAnswers.items()))
        listOfCities.append(place)
        quiz.write(f"{chr(i + 65)}. What is the capital of {place}?\n")
        capitalList[mcqPosition] = realCapital
        quizAns.write(f"{chr(i+65)} -- {mcqPosition+1}\n")

        # for the four options 
        for i in range(4): 
            if capitalList[i]=="":
                newCapitalCity = random.choice(list(quizQuesAndAnswers.values()))
                while newCapitalCity in capitalList:
                    newCapitalCity = random.choice(list(quizQuesAndAnswers.values()))
                capitalList[i] = newCapitalCity

        for i in range(0,4):
            quiz.write((f"\t{i+1}. " + capitalList[i]+"\n"))
