# Gregory Chernyavskiy            10/16/2022
# Assignment4

import random
import sys

# GLOBAL CONSTANT VARIABLES
START_ROOM = 1
FINAL_ROOM = 9999
START_HEALTH = 10




def room1(currentRoom, goldAmount, visited_room, health):
    if visited_room == False:
        gold = 20
    
        print()
        print("The room has", gold, "gold pieces in it...")
        goldAmount += gold
        print("After taking the gold, you currently have", goldAmount, "gold pieces in your posession...")
        print()


        if health > 0:
            print("\nYour helath is: ",health,)
            print("You are very strong right now! Let's find the way out!")
        else:
            print()
            print("You have perished in the dungeon, and your bones are still there. The dungeon is now hidden and nobody will ever know where you are. \nGAMEOVER!")
            print()
            sys.exit()
       
        visited_room = True
    else:
        print()
        print("You have already visited this room before...")
        print()

    direction = input("Which way are you gonna go now? [n] [s] [e] [w]?: ")
    while direction != "n" and direction != "s" and direction != "e" and direction != "w":
        print("Invalid input...")
        direction = input("What path? [n] [s] [e] [w]?: ")
    
    currentRoom = 1
    if direction == "n":
        currentRoom = 2
    elif direction == "s":
        currentRoom = 2
    elif direction == "e":
        currentRoom = 2
    elif direction == "w":
        currentRoom = 2
    
    return currentRoom, goldAmount, visited_room, health




def room2(currentRoom, goldAmount, visited_room, health):

    if visited_room == False:
        gold = 20 # This is the amount of gold the room contains.

        print()
        print("The room has", gold, "gold pieces in it...")
        goldAmount += gold
        print("After taking the gold, you currently have", goldAmount, "gold pieces in your posession...")
        print()


        health = combat(100,health,START_HEALTH,60,1)

        if health > 0:
            print("Your helath is: ",health,)
            print("That was awesome! Let's try to find the tresure or the way out!")
        else:
            print()
            print("You have perished in the dungeon, and your bones are still there. The dungeon is now hidden and nobody will ever know where you are. \nGAMEOVER!")
            print()
            sys.exit()
       
        visited_room = True

    else:
        print()
        print("You have already visited this room before...")
        print()


    direction = input("[n] [s]?: ")
    while direction != "n" and direction != "s":
        print("Invalid input...")
        direction = input("[n] [s]?: ")
    

    currentRoom = 2
    if direction == "n":
        currentRoom = FINAL_ROOM
    elif direction == "s":
        currentRoom = 3

    return currentRoom, goldAmount, visited_room, health



def room3(currentRoom, goldAmount, visited_room, health):
    if visited_room == False:
        gold = 20
    
        print()
        print("The room has", gold, "gold pieces in it...")
        goldAmount += gold
        print("After taking the gold, you currently have", goldAmount, "gold pieces in your posession...")
        print()

        health = health - 3
        if health > 0:
            print("Your helath is: ",health,)
            print("You were poisoned by the slime monster! But you have recovered! Let's continue...")
        else:
            print()
            print("You were poisoned by the slime monster!")
            print("You have perished in the dungeon, and your bones are still there. The dungeon is now hidden and nobody will ever know where you are. \nGAMEOVER!")
            print()
            sys.exit()
       
        visited_room = True

    else:
        print()
        print("You have already visited this room before...")
        print()

    
    direction = input("[e] [w]?: ")
    while direction != "e" and direction != "w":
        print("Invalid input...")
        direction = input("[e] [w]?: ")
    

    currentRoom = 3
    if direction == "e":
        currentRoom = 4
    elif direction == "s":
        currentRoom = 2

    return currentRoom, goldAmount, visited_room, health



def room4(currentRoom, goldAmount, visited_room, health):
    if visited_room == False:
        gold = 100
    
        print()
        print("This room has a lot of gold for you! The amount you got is: ", gold, "")
        goldAmount += gold
        print("After taking the gold, you currently have", goldAmount, "gold pieces in your posession...")
        print()


        if health > 0:
            print("Your helath is: ",health,)
        else:
            print()
            print("You have perished in the dungeon, and your bones are still there. The dungeon is now hidden and nobody will ever know where you are. \nGAMEOVER!")
            print()
            sys.exit()
       
        visited_room = True

    else:
        print()
        print("You have already visited this room before...")
        print()

    direction = input("[n] [s]?: ")
    while direction != "n" and direction != "s":
        print("Invalid input...")
        direction = input("[n] [s]?: ")
    

    currentRoom = 2
    if direction == "n":
        currentRoom = FINAL_ROOM
    elif direction == "s":
        currentRoom = 2

    return currentRoom, goldAmount, visited_room, health



def combat(combatChance, health, maxHealth, playerAccuracy, playerDamage):
    enemyName = ""
    enemyHealth = 0
    enemyAccuracy = 0
    enemyDamage = 0
    
    if combatChance > random.randint(0, 9):
        print("You have engaged in combat!")
        print()

        
        monsterSelection = random.randint(0, 0)
        if monsterSelection == 0:
            enemyName = "SLIME"
            maxEnemyHealth = 4
            enemyHealth = maxEnemyHealth
            enemyAccuracy = 6
            enemyDamage = 2
            print("You have encountered an enemy {0} monster...".format(enemyName))
            print()
            print("It has {0} HP and {1} ATTACK strength...".format(enemyHealth, enemyDamage))
            print()
        else:
            print("Error - 'combat' function: 'monsterSelection' value is invalid:", monsterSelection)

       
        currentTurn = random.randint(0, 1)
        if currentTurn == 0:
            print("You have taken the initiative!")
        else:
            print("The enemy {0} monster has struck first!".format(enemyName))
        print()


        while health > 0 and enemyHealth > 0:
            if currentTurn == 0: 
                
                action = input("COMBAT: [a]ttack, [f]lee: ")
                while action != "a" and action != "f":
                    print("Invalid combat choice...")
                    action = input("COMBAT: [a]ttack, [f]lee: ")
                print()

                
                if action == "a":
                    if random.randint(0, 9) < playerAccuracy:
                        enemyHealth -= playerDamage
                        print("You have HIT the enemy monster! Its HP is: {0} / {1}".format(enemyHealth, maxEnemyHealth))
                        print()
                    else:
                        print("You have MISSED the enemy monster...")
                        print()
                elif action == "f":
                    if random.randint(0, 9) < playerDamage:
                        print("You have escaped from combat!")
                        print()
                        break
                else:
                    print("Error - 'combat' function: 'action' value is invalid:", action)

            else: 
                if random.randint(0, 9) < enemyAccuracy:
                    health -= enemyDamage
                    print("You have been HIT by the the enemy {0} monster! Your HP is: {1} / {2}".format(enemyName, health, maxHealth))
                    print()
                else:
                    print("The enemy {0} monster has MISSED you...".format(enemyName))
                    print()
            
            currentTurn += 1
            currentTurn %= 2
        
        if health > 0 and enemyHealth <= 0:
            print("Congratulations! You have defeated the enemy {0} monster...".format(enemyName))
            print()
        elif health > 0 and enemyHealth > 0:
            print("That was a close one! The enemy {0} monster almost got you!".format(enemyName))
            print()
        else:
            print("Sadly, the enemy {0} monster was victorious...".format(enemyName))
            print()
    else:
        print("Fortunately, there were no monsters in this room...")
        print()
    
    return health



def main():
    gameOver = False

    START_GOLD = 0
    health = START_HEALTH
    goldAmount = START_GOLD
    currentRoom = START_ROOM
    visited_room1 = False
    visited_room2 = False
    visited_room3 = False
    visited_room4 = False

    print("Welcome to Dungeon Crawl...")
    print()

    print("By: Gregory Chernyavskiy")
    print("[COM S 127 B]")
    print()

    while gameOver == False:
        choice = input("MAIN MENU: \n Please enter a first letter. \n [p]lay, [i]nstructions, or [q]uit?: ")
        print()
        if choice.lower() == "p":
            print("\n\nYou have entered the dangeon!")

            if health > 0:
                while currentRoom != FINAL_ROOM:
                    if currentRoom == 1:
                        currentRoom, goldAmount, visited_room1, health = room1(currentRoom, goldAmount, visited_room1, health)
                    elif currentRoom == 2:
                        currentRoom, goldAmount, visited_room2, health = room2(currentRoom, goldAmount, visited_room2, health)
                    elif currentRoom == 3:
                        currentRoom, goldAmount, visited_room3, health = room3(currentRoom, goldAmount, visited_room3, health)
                    elif currentRoom == 4:
                        currentRoom, goldAmount, visited_room4, health = room4(currentRoom, goldAmount, visited_room4, health)
                    else:
                        print("Error - currentRoom number", currentRoom, "does not correspond with available rooms")
                        sys.exit()

            else:
                print()
                print("You have perished in the dungeon, and your bones are still there. The dungeon is now hidden and nobody will ever know where you are. You LOST!")
                print()
                gameOver = True
        
            print()
            print("You have escaped with", goldAmount, "gold from the dungeon! Congratualtions! Your helath will recover within a day. Enjoy and go buy something for yourself!")
            print()



            goldAmount = START_GOLD
            currentRoom = START_ROOM
            visited_room1 = False
            visited_room2 = False

        elif choice.lower() == "i": 
            print("The instructions to the game: ")
            print("\nTraverse the dangeon, collect all the gold you can possibly carry with you and try to find a way out. \n GOODLUCK!")
            print()

        elif choice.lower() == "q": 
            gameOver = True
            print("\nSee ya later!")
            print()

        else:
            print()
            print("Please enter [p], [i], or [q]...")
            print()



if __name__ == "__main__":
    main()