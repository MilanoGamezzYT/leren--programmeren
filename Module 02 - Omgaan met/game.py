import time
def printDelay(t: str, d=0.5):
    time.sleep(d)
    print(t)
#t = parameter
#d is defaultvalue (komt door =)

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
        man = input('He says yes but you need to do some quests so you say?  ')
        if man == 'yes':
            printDelay('You say yes')
            printDelay('The first quest is to catch a fish for the cat')
            help1 = input('Then a man asks if you can help him so you say? ')   
            if help1 == 'yes':
                printDelay('You go to the man')
                printDelay('You ask him what he needs help with')
                printDelay('He says you need to remove the beehive overthere')
                printDelay('You say ok')
                printDelay('The man grabs a flute and call his eagle')
                number1 = int(input('Choose a number between 1 and 20  '))
                if number1 >= 1 and number1 <= 10:
                    printDelay('You chose a wrong number')
                    printDelay('You missed the beehive  ')
                    printDelay('The bees are attacking you')
                    printDelay('You are dead')
                    exit()
                elif number1 >= 11 and number1 <= 20:
                    printDelay('You chose the right number')
                    printDelay('You hit the beehive')
                    printDelay('The beehive falls down')
                    printDelay('you see a cradle')
                    number3 = int(input('Choose a number between 5 and 25  '))
                    if number3 >= 5 and number3 <= 10:
                        printDelay('You are wrong')
                        printDelay('You missed the cradle')
                        printDelay('The cradle falls down')
                        printDelay('You are dead')
                        exit()
                    elif number3 >= 11 and number3 <= 25:
                        printDelay('You are right')
                        printDelay('You hit the cradle')
                        printDelay('The eagle is flying')
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
                    number = int(input('Choose a number between 1 and 10  '))
                    if number  >= 1 and number <=5:
                        printDelay('You shoot the targets')
                        printDelay('You win the game')
                    elif number  >5 and number <=10:
                        printDelay('You missed the targets')
                        printDelay('You died')
                        exit()
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
                                    attack = input('Which attack do you want to do? You can choose between Charge Attack,Spin Attack or Fatal Blow ').lower()
                                    if attack == 'Charge attack' or attack == 'spin attack' or attack == 'fatal blow':
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
                                        if attack2 == 'Charge attack' or attack2 == 'fatal blow' or attack2 == 'spin attack':
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
                                                    attack3 = input('Which attack do you want to use? You can choose between charge Attack or a Spin Attack  ').lower()
                                                    if attack3 == 'charge attack' or attack3 == 'spin attack':
                                                        printDelay('You chose an attack and it was very effective')
                                                        printDelay('You killed Ganon and you completed the game!')
                                                        printDelay('You saved Hyrule!')
                                                        printDelay('You are the Hero of Time!')
                                                        printDelay('The End')
                                                        exit()
                                                elif mastersword == 'no':
                                                    printDelay('You walk to Hyrule Castle')
                                                    printDelay('You walk to the castle')
                                                    printDelay('You walk to the castle and see a big door')
                                                    printDelay('You see Ganon!')
                                                    printDelay('You walk to Ganon')
                                                    printDelay('You start the battle')
                                                    printDelay('Ganon is very strong')
                                                    attack3 = input('Which attack do you want to use? You can choose between Charge Attack, Spin Attack or a Skyward strike ').lower()
                                                    if attack3 == 'charge attack' or attack3 == 'spin attack' or attack3 == 'skyward strike':
                                                        printDelay('You chose an attack and it was very effective')
                                                        printDelay('You almost killed Ganon!')
                                                        attack4 = input('Which attack do you want to use? You can choose between Jump Attack, Fatal Blow or a Skyward Strike  ').lower()
                                                        if attack4 == 'jump attack' or attack4 == 'fatal Blow' or attack4 == 'skyward Strike':
                                                            printDelay('You chose an attack and it was very effective')
                                                            printDelay('You killed Ganon and you completed the game!')
                                                            printDelay('You saved Hyrule!')
                                                            printDelay('You are the Hero of Time!')
                                                            printDelay('The End')
                                        elif chestkey == 'no':
                                            printDelay('you need to open the chest to end this dungeon')
                                            exit()
                                    elif fight == 'no':
                                        printDelay('You decided not to fight')    
                                        exit()   
                            elif dungeon == 'no':
                                printDelay('you need to enter this dungeon Link!')    
                                exit()         
                    elif chest == 'no':
                        printDelay('you need to open the chest to go further')
                        exit()
            elif help1 == 'no':
                printDelay('Ok bye')
                exit()

        elif man == 'no':
            printDelay('You walk away from him')
            exit()

    elif slingshot == 'no':
        printDelay('You say no')
        printDelay('They say okay')
elif start_game == 'no':
    printDelay('ok bye')

