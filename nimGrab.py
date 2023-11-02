# Gregory Chernyavskiy            10/05/2022
# Assignment3

import random 

print("Welcome to NIMGRAB!")
print()

print("By: Gregory Chernyavskiy")
print("[COM S 127 <B>]")
print()


NUM_ITEMS_LOW = 9
NUM_ITEMS_HIGH = 21
NUM_TO_TAKE_LOW = 1
NUM_TO_TAKE_HIGH = 3


gameOver = False
currentTurn = 0

while gameOver == False:
    player = input("[p]lay, [i]nstructions, or [q]uit?: ")
    print()

    if player.lower() == "p":
        print("Let's play the NIMGRAB!")
        pool = random.randrange(NUM_ITEMS_LOW, NUM_ITEMS_HIGH)
        gameplay = True

        while pool > 0 and gameplay:

            if currentTurn == 0:
                print("\nHUMAN TURN: ")
                print("Items left in pool: {0}.".format(pool))
                print("|"* pool, end="")
                print("\nChoose the number between {0} and {1}. ".format(NUM_TO_TAKE_LOW, NUM_TO_TAKE_HIGH))
                print()
                while True:
                    amount = int(input("Enter the amount you want to subtract: "))
                    print()
                    try:
                        amount = int(amount)
                    except:
                        print("Please enter an INTEGER number...")
                        continue
                    if amount < NUM_TO_TAKE_LOW or amount > NUM_TO_TAKE_HIGH:
                        print("Please enter the number between {0} and {1}. ".format(NUM_TO_TAKE_LOW, NUM_TO_TAKE_HIGH))
                        continue
                    break
                print("The amount you've taken is: ",amount,)
                pool -= amount
                print()
                currentTurn += 1
                currentTurn = currentTurn % 2
            
            else:
                print("COMPUTER TURN: ")
                print("Items left in pool: {0}.".format(pool))
                print("|"* pool, end="")
                print()

                if pool > 3:
                    variable = random.randrange(NUM_TO_TAKE_LOW, NUM_TO_TAKE_HIGH)
                elif pool >1 or pool <= 3:
                    variable = random.randrange(1,2)
                else:
                    variable = 1
                
                print("The computer chose: {0}".format(variable))
                pool -= variable
                print()

                currentTurn += 1
                currentTurn = currentTurn % 2

        if currentTurn == 0:
            print("The COMPUTER has taken the last item... Therefore, the HUMAN Has Won!")
            print()
        else:
            print("The HUMAN has taken the last item... Therefore, the COMPUTER Has Won!")
            print()


    elif player.lower() == "i":
        print("The Instructions of the game: ")
        print("\nEach player, the human and the computer, take turns removing objects from a pool." 
        "\nEach player can remove between NUM_TO_TAKE_LOW and NUM_TO_TAKE_HIGH items total."
        "\nThe game progresses until the last item is removed from the pool."
        "\nThe player to take the last item loses the game.")
        print()


    elif player.lower() == "q":
        gameOver = True
        print("Goodbye.")
        print()
    

    else:
        print("Please restart the program!")
        print()