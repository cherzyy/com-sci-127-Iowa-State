# <Gregory Chernyavskiy>             <23/11/2022>
# Assignment #6 Naval Battle

import random
import gameBoard

def getHumanInput():
    
    row = int(input("Enter the row of the ship: "))
    while row < 0 and row > gameBoard.GAME_BOARD_HEIGHT-1:
        print('Invalid input, please select a valid row')
        row = int(input("Enter the row of the ship: "))
    pass
    
    col = int(input("Enter the row of the ship: "))
    while col < 0 and row > gameBoard.GAME_BOARD_HEIGHT-1:
        print('Invalid input, please select a valid row')
        col = int(input("Enter the row of the ship: "))
    pass
    
    return row, col

def getComputerInput():
    
    row = random.randint(0, gameBoard.GAME_BOARD_WIDTH - 1)

    col = random.randint(0, gameBoard.GAME_BOARD_WIDTH - 1)

    return row, col