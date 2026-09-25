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
def changeTurn(turn):
    if turn == "X":
        turn = "O"
    else:
        turn = "X"
    return turn

while True: 
    print(f"Player {turn} turn")
    print(f"{turn}, where would you like to place your piece? 1,2,3,4,5,6,7,8,9")
    position = input()  

    if position == "1":
        theBoard['top-L'] = turn
        turn = changeTurn(turn)
    elif position == "2":
        theBoard['top-M'] = turn
        turn = changeTurn(turn)
    elif position == "3":
        theBoard['top-R'] = turn     
        turn = changeTurn(turn)
    elif position == "4":
        theBoard['mid-L'] = turn
        turn = changeTurn(turn)
    elif position == "5":
        theBoard['mid-M'] = turn
        turn = changeTurn(turn)
    elif position == "6":
        theBoard['mid-R'] = turn
        turn = changeTurn(turn)
    elif position == "7":
        theBoard['low-L'] = turn   
        turn = changeTurn(turn)
    elif position == "8":
        theBoard['low-M'] = turn
        turn = changeTurn(turn)
    elif position == "9":
        theBoard['low-R'] = turn
        turn = changeTurn(turn)
    else: 
        print ("Wrong option selected")

    printBoard(theBoard)
