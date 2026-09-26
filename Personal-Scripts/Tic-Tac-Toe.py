#Tic-Tac-Toe Game
theBoard = { 'top-L':'1', 'top-M': '2', 'top-R':'3',
              'mid-L':'4', 'mid-M':'5', 'mid-R': '6',
              'low-L':'7', 'low-M':'8', 'low-R':'9'  
            }

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + ' |' + board['top-R'])
    print("--+--+--")
    print(board['mid-L'] + '|' + board['mid-M'] + ' |' + board['mid-R'])
    print("--+--+--")
    print(board['low-L'] + '|' + board['low-M'] + ' |' + board['low-R'])

print("Welcome to the Tic-Tac-Toe Game!")
printBoard(theBoard)
turn = "X"

listOfPositions = []
def changeTurn(turn):
    if turn == "X":
        turn = "O"
    else:
        turn = "X"
    return turn

def checkIfPositionOccupied(number):
    if number in listOfPositions:
        print(f"{number} position alreay occupied. Please choose another position.")
        return -1
    else:
        return 0

while True: 
    print(f"Player {turn} turn")
    print(f"{turn}, where would you like to place your piece? 1,2,3,4,5,6,7,8,9")
    position = input()  

    if position == "1":
        postionOccupied = checkIfPositionOccupied("1")
        if postionOccupied == -1:
            continue
        theBoard['top-L'] = turn
        listOfPositions.append("1")
        turn = changeTurn(turn)

    elif position == "2":
        postionOccupied = checkIfPositionOccupied("2")
        if postionOccupied == -1:
                continue
        theBoard['top-M'] = turn
        listOfPositions.append("2")
        turn = changeTurn(turn)

    elif position == "3":
        postionOccupied = checkIfPositionOccupied("3")
        if postionOccupied == -1:
            continue
        theBoard['top-R'] = turn
        listOfPositions.append("3")     
        turn = changeTurn(turn)

    elif position == "4":
        postionOccupied = checkIfPositionOccupied("4")
        if postionOccupied == -1:
            continue
        theBoard['mid-L'] = turn
        listOfPositions.append("4")  
        turn = changeTurn(turn)

    elif position == "5":
        postionOccupied = checkIfPositionOccupied("5")
        if postionOccupied == -1:
            continue
        theBoard['mid-M'] = turn
        listOfPositions.append("5")  
        turn = changeTurn(turn)

    elif position == "6":
        postionOccupied = checkIfPositionOccupied("6")
        if postionOccupied == -1:
                    continue
        theBoard['mid-R'] = turn
        listOfPositions.append("6")  
        turn = changeTurn(turn)

    elif position == "7":
        postionOccupied = checkIfPositionOccupied("7")
        if postionOccupied == -1:
            continue
        theBoard['low-L'] = turn  
        listOfPositions.append("7")   
        turn = changeTurn(turn)

    elif position == "8":
        postionOccupied = checkIfPositionOccupied("8")
        if postionOccupied == -1:
                continue
        theBoard['low-M'] = turn
        listOfPositions.append("8")  
        turn = changeTurn(turn)

    elif position == "9":
        postionOccupied = checkIfPositionOccupied("9")
        if postionOccupied == -1:
            continue
        theBoard['low-R'] = turn
        listOfPositions.append("9")  
        turn = changeTurn(turn)
    else: 
        print ("Wrong option selected")

    printBoard(theBoard)
