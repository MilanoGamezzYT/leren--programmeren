import time
def printDelay(t: str, d=2):
    time.sleep(d)
    print(t)


game_name = "Twilight Princess 2"

printDelay(f'Welcome to {game_name}!')
start_game = input('do you want to start the game?  ').lower()
if start_game == 'yes':
    printDelay('starting game...')
    printDelay('You wake up and you heard some noices')
    printDelay('You go see whats outside')
    printDelay('You see some chilren playing')
    printDelay('You go to the children')
    printDelay('You ask them what they are doing')
    printDelay('They say they are playing')
    slingshot = input('They ask you if you can find the slingshot so you say?  ')
    if slingshot == 'yes':
        printDelay('You said yes  ')
        printDelay('You are walking to the main village')
        printDelay('You see a shop')
        printDelay('You go to the shop')
        printDelay('You ask the shopkeeper if he has a slingshot')
        man = input('He says yes but you need to do some quests')
        if man == 'yes':
            printDelay('You say yes')
            printDelay('The first quest is to catch a fish for the cat')
            help1 = input('Then an man asks if you can help him ')   
            if help1 == 'yes':
                printDelay('You go to the man')
                printDelay('You ask him what he needs help with')
                printDelay('He says you need to remove the beehive overthere')
                printDelay('You say ok')
                printDelay('The man grabs a flute and call his eagle')
                printDelay('The eagle comes and have to aim at the beehive')
                printDelay('You aim at the beehive')
                printDelay('You shoot the beehive')
                printDelay('The beehive falls down')
                printDelay('you see a cradle')
                printDelay('You aim at the cradle')
                printDelay('You shoot the cradle')
                printDelay('The eagle has the cradle and returns it')
                printDelay('You see a woman at a lake, she crys and says she lost her baby')
                printDelay('You say i think i find your baby')
                printDelay('I have the cradle')
                printDelay('She gives you a reward')
                printDelay('it is a fishing rod')
                printDelay('You go to the pond')
                printDelay('You throw the fishing rod')
                printDelay('You catch a fish')
                printDelay('You go to the cat')
                printDelay('You give the cat the fish')
                printDelay('The cat is happy')
                printDelay('you go to the shopkeeper')
                printDelay('the shopkeeper says you earned the slingshot')
                printDelay('You Got the slingshot!')
                printDelay('You go back to the children')
                printDelay('You give the children the slingshot')
                printDelay('They say you need to shoot the targets') 
                printDelay('You aim at the targets')
                printDelay('You shoot at the targets')
                printDelay('You shot all targets and the kids are very happy')
                printDelay('Now you go home again and see a chest')
                chest = input('Do you want to open the chest?')
                if chest == 'yes':
                    print('You got the standard sword!')
                    printDelay('You can now go to the Dungeon')
                    dungeon = input('Do you want to go to the Dungeon?')
                    if dungeon == 'yes':
                        printDelay('You walk to the dungeon and enters it')
                        printDelay('You hear a weird voice that says that you need to complete a few puzzles to go to the Boss')
                        printDelay('The first puzzle is a parkour, you can do this')
                    parkour = input('Do you want to jump or walk away?  ')
                    if parkour == 'jump':
                        printDelay('you chose to jump and that was a good jump, now the next one')
                    elif parkour == 'walk' or parkour == 'walk away':
                        printDelay('You chose to run away')
                        exit()
                    parkour2 = input('Do you want to jump?  ')
                    if parkour2 == 'yes' or parkour2 == 'jump':
                        printDelay('You chose jump again and you completed the first puzzle')
                        printDelay('Link, the second puzzle is a battle against some goblins. Good luck!')
                        printDelay('You walk to the goblins and they are angry')
                        attack = input('Which attack do you want to do? You can choose between Charge Attack, Fatal Blow or a Spin Attack  ').lower()
                        if attack == 'Charge attack' or 'fatal blow' or 'spin attack':
                            printDelay('You chose an attack and it was very effective')
                            printDelay('Good job Link, the final puzzle is to find the Boss Key')
                            bosskey = input('Do you want to go left or right?  ')
                            if bosskey == 'left':
                                printDelay('you go left but its a trap so you die')
                                exit()
                            elif bosskey == 'right':
                                printDelay('You walk to the right and see an chest')
                                chestkey = input('Do you want to open the chest?  ')
                                if chestkey == 'yes':
                                    printDelay('You opened the chest and got the boss key!')
                                    printDelay('you walk to the big door and opened it with the key')
                                    fight = input('Are you sure you want to start this battle? if not, it ends here  ')
                                    if fight == 'yes':
                                        printDelay('You walk to the boss and start the battle')
                                        printDelay('The boss is a big monkey')
                                        printDelay('You start the battle')
                                        printDelay('The boss is very strong')
                                        attack2 = input('Which attack do you want to use? You can choose between Charge Attack, Fatal Blow or a Spin Attack  ').lower()
                                        if attack2 == 'Charge attack' or 'spin attack':
                                            printDelay('You chose an attack and it was very effective')
                                            printDelay('You killed the boss and you completed the dungeon!')
                                            hyrule = input('Do you want to go to Hyrule Castle?  ')
                                            if hyrule == 'yes':
                                                mastersword = input('Do you want to go to Hyrule Forest to get the Master Sword?')
                                                if mastersword == 'yes':
                                                    printDelay('You walk to Hyrule Forest')
                                                    printDelay('You see the Master Sword!')
                                                    printDelay('You walk to the Master Sword')
                                                    printDelay('You grab the Master Sword')
                                                    printDelay('You walk back to Hyrule Castle')
                                                    printDelay('You walk to the castle')
                                                    printDelay('You walk to the castle and see a big door')
                                                    printDelay('You see Ganon!')
                                                    printDelay('You walk to Ganon')
                                                    printDelay('You start the battle')
                                                    printDelay('Ganon is very strong')
                                                    attack3 = input('Which attack do you want to use? You can choose between Charge Attack or a Spin Attack  ').lower()
                                                    if attack3 == 'Charge attack' or 'spin attack':
                                                        printDelay('You chose an attack and it was very effective')
                                                        printDelay('You killed Ganon and you completed the game!')
                                                        printDelay('You saved Hyrule!')
                                                        printDelay('You are the Hero of Time!')
                                                        printDelay('The End')
                                                elif mastersword == 'no':
                                                    printDelay('You walk to Hyrule Castle')
                                                    printDelay('You walk to the castle')
                                                    printDelay('You walk to the castle and see a big door')
                                                    printDelay('You see Ganon!')
                                                    printDelay('You walk to Ganon')
                                                    printDelay('You start the battle')
                                                    printDelay('Ganon is very strong')
                                                    attack3 = input('Which attack do you want to use? You can choose between Charge Attack or a Spin Attack  ').lower()
                                                    if attack3 == 'Charge attack' or 'spin attack':
                                                        printDelay('You chose an attack and it was very effective')
                                                        printDelay('You almost killed Ganon!')
                                                        attack4 = input('Which attack do you want to use? You can choose between Charge Attack, Fatal Blow or a Spin Attack  ').lower()
                                                        if attack4 == 'Charge attack' or 'spin attack':
                                                            printDelay('You chose an attack and it was very effective')
                                                            printDelay('You killed Ganon and you completed the game!')
                                                            printDelay('You saved Hyrule!')
                                                            printDelay('You are the Hero of Time!')
                                                            printDelay('The End')
                                                        


                                elif chestkey == 'no':
                                    printDelay('you need to open the chest to end this dungeon')
                                    exit()
                elif chest == 'no':
                    printDelay('you need to open the chest to go further')
                    exit()
        elif man == 'no':
            printDelay('You walk away from him')
            exit()

    elif slingshot == 'no':
        printDelay('You say no')
        printDelay('They say okay')
elif start_game == 'no':
    printDelay('ok bye')

