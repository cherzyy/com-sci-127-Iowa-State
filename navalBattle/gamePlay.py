# <Gregory Chernyavskiy>             <23/11/2022>
# Assignment #6 Naval Battle

import gameBoard
import gameInput
import random

playerList = []
computerList = []

def _humanTurn(humanGameBoard, targetBoard, computerGameBoard, numComputerTargets, numHumanTargets):
    
    print("It's HUMAN turn now!")
    gameBoard.printBoard(targetBoard, gameBoard.GAME_BOARD_HEIGHT, gameBoard. GAME_BOARD_WIDTH)
    gameBoard.printBoard(humanGameBoard, gameBoard.GAME_BOARD_HEIGHT, gameBoard. GAME_BOARD_WIDTH)

    while True:

        counter = 0
        row, col = gameInput.getHumanInput()
        humanAttack = (row,col)
        for coordinate in playerList:
            if humanAttack == coordinate:
                print("Please enter a coordinate that you haven't chosen before!")
                counter +- 1
        if counter == 0:
            playerList.append(humanAttack)
            break
    
    print("The HUMAN is attacking (" ,row, "," ,col, ")")
    if computerGameBoard[row][col] == "@":
        computerGameBoard[row][col] = "X"
        targetBoard[row][col] = "X"
        print()
        print("HIT")
        print("You have hit the COMPUTERS ship!!!")
        numComputerTargets -= 1
        print()
        print("____________________________________")
    
    else:
        print()
        print("MISS")
        print("HUMAN missed and did NOT hit the COMPUTERS ship!")
        computerGameBoard[row][col] = "0"
        targetBoard[row][col] = "0"
        print()
        print("____________________________________")

    return humanGameBoard, targetBoard, computerGameBoard, numComputerTargets


 
def _computerTurn(humanGameBoard, numHumanTargets):
    
    print("It's COMPUTER turn now!")
    gameBoard.printBoard(humanGameBoard, gameBoard.GAME_BOARD_HEIGHT, gameBoard. GAME_BOARD_WIDTH)

    while True:
        counter = 0
        row = random.randint(0, gameBoard.GAME_BOARD_WIDTH - 1)
        col = random.randint(0, gameBoard.GAME_BOARD_WIDTH - 1)
        computerAttack = (row,col)
        for coordinate in computerList:
            if computerAttack == coordinate:
                print("Please enter a coordinate that you haven't chosen before!")
                counter +- 1
        if counter == 0:
            computerList.append(computerAttack)
            break
    
    print("The Computer is attacking (" ,row, "," ,col, ")")
    if humanGameBoard[row][col] == "@":
        humanGameBoard[row][col] = "X"
        print()
        print("HIT")
        print("COMPUTER has hit the HUMANS ship!!!")
        numHumanTargets -= 1
        print()
        print("____________________________________")
    
    else:
        print()
        print("MISS")
        print("COMPUTER missed and did NOT hit the HUMANS ship!")
        humanGameBoard[row][col] = "0"
        print()
        print("____________________________________")

    return humanGameBoard, numHumanTargets




def _printWinner(numComputerTargets, computerGameBoard):
    
    if numComputerTargets == 0:
        print("THE HUMAN HAS WON!!!")
        print("CONGRADULATIONS!")
        print()

    else:
        print("COMPUTER HAS WON!")
        print("GAME OVER!!!")
        print()
    
    gameBoard.printBoard(computerGameBoard, gameBoard.GAME_BOARD_HEIGHT, gameBoard. GAME_BOARD_WIDTH)
    return



def runGame(humanGameBoard, targetBoard, computerGameBoard, numHumanTargets, numComputerTargets):
    
    currentTurn = 0 
    
    while numHumanTargets > 0 and numComputerTargets > 0:
        if currentTurn == 0:
            print()
            print("Enemy ship has" ,numComputerTargets, "remaining.")
            print("Enemy ship has" ,numHumanTargets, "remaining.")
            print()
            humanGameBoard, targetBoard, computerGameBoard, numComputerTargets = _humanTurn(humanGameBoard, targetBoard, computerGameBoard, numComputerTargets)
        else:
            print()
            print("Enemy ship has" ,numComputerTargets, "remaining.")
            print("Enemy ship has" ,numHumanTargets, "remaining.")
            print()
            humanGameBoard, numHumanTargets = _computerTurn(humanGameBoard, numHumanTargets)

        currentTurn += 1
        currentTurn %= 2

    _printWinner(numComputerTargets, computerGameBoard)

    return