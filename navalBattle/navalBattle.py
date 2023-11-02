# <Gregory Chernyavskiy>             <23/11/2022>
# Assignment #6 Naval Battle


import gameBoard
import gamePlay

def main():
    
    gameOver = False

    gameboardChoice = 0
    humanGameBoard = None
    targetBoard = None
    computerGameBoard = None
    
    numHumanTargets = 0
    numComputerTargets = 0
    
    print("Welcome to Naval Battle!")
    print()
    
    
    print("By: <Gregory Chernyavskiy>")
    print("[COM S 127 <B>]")
    print()

    while gameOver == False:
        choice = input("[p]lay, [i]nstructions, or [q]uit?: ")
        print()
        if choice == "p": 

            gameboardChoice = gameBoard.chooseHumanGameBoard()

            humanGameBoard, numHumanTargets = gameBoard.loadGameBoard(gameboardChoice)
            gameboardChoice = gameBoard.chooseComputerGameBoard()

            computerGameBoard, numComputerTargets = gameBoard.loadGameBoard(gameboardChoice)
            targetBoard = gameBoard.loadTargetBoard

            gamePlay.runGame(humanGameBoard, targetBoard, computerGameBoard, numHumanTargets, numComputerTargets)
            

        elif choice == "i":
            print("Enter a row and a column to fire on the COMPUTER's ships!"
                "Sink all the COMPUTER's vessels before they sink yours!")
            print()
            pass

        elif choice == "q":
            gameOver = True
            print("Goodbye.")
            print()
            pass
        else:
            print()
            print("Please enter [p], [i], or [q]...")
            print()

if __name__ == "__main__":
    main()