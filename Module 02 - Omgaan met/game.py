def start_game(game_name: str) -> None:

    print(f'Welcome to {game_name}!')
    start_game = input('do you want to start the game?  ').lower()
    if start_game != 'yes':
        print('Goodbye!')
        return

    print('starting game...')
    print('You wake up and you heard some noices')
    print('You go see whats outside')
    print('You see some chilren playing')
    print('You go to the children')
    print('You ask them what they are doing')
    print('They say they are playing')
    slingshot = input('They ask you if you can find the slingshot so you say?  ')
    if slingshot != 'yes':
        print('Goodbye!')
        return
    
    print('You said yes  ')
    print('You are walking to the main village')
    print('You see a shop')
    print('You go to the shop')
    print('You ask the shopkeeper if he has a slingshot')
    man = input('He says yes but you need to do some quests so you say?  ')
    if man != 'yes':
        print('Goodbye!')
        return

    print('You say yes')
    print('The first quest is to catch a fish for the cat')
    help1 = input('Then a man asks if you can help him so you say? ')   
    if help1 != 'yes':
        print('Goodbye!')
        return

    print('You go to the man')
    print('You ask him what he needs help with')
    print('He says you need to remove the beehive overthere')
    print('You say ok')
    print('The man grabs a flute and call his eagle')
    number1 = int(input('Choose a number between 1 and 20  '))
    if number1 < 11:
        print('You chose a wrong number')
        print('You missed the beehive  ')
        print('The bees are attacking you')
        print('You are dead')
        return
    else:
        print('You chose the right number')
        print('You hit the beehive')
        print('The beehive falls down')
        print('you see a cradle')
        number3 = int(input('Choose a number between 5 and 25  '))
        if number3 < 11:
            print('You are wrong')
            print('You missed the cradle')
            print('The cradle falls down')
            print('You are dead')
            return
        else:
            print('You are right')
            print('You hit the cradle')
            print('The eagle is flying with the cradle')
            print('The eagle has the cradle and returns it')
            print('You see a woman at a lake, she crys and says she lost her baby')
            print('You say i think i find your baby')
            print('I have the cradle')
            print('She gives you a reward')
            print('it is a fishing rod')
            print('You go to the pond')
            print('You throw the fishing rod')
            print('You catch a fish')
            print('You go to the cat')
            print('You give the cat the fish')
            print('The cat is happy')
            print('you go to the shopkeeper')
            print('the shopkeeper says you earned the slingshot')
            print('You Got the slingshot!')
            print('You go back to the children')
            print('You give the children the slingshot')
            print('They say you need to shoot the targets') 
            number = int(input('Choose a number between 1 and 10  '))
            if number  >= 1 and number <=5:
                        print('You shoot the targets')
                        print('You win the game')
            elif number  >5 and number <=10:
                print('You missed the targets')
                print('You died')
                exit()
            print('You shot all targets and the kids are very happy')
            print('Now you go home again and see a chest')
            chest = input('Do you want to open the chest?')
            if chest == 'yes':
                    print('You got the standard sword!')
                    print('You can now go to the Dungeon')
                    dungeon = input('Do you want to go to the Dungeon?')
                    if dungeon == 'yes':
                        print('You walk to the dungeon and enters it')
                        print('You hear a weird voice that says that you need to complete a few puzzles to go to the Boss')
                        print('The first puzzle is a parkour, you can do this')
                        parkour = input('Do you want to jump or walk away?  ')
                        if parkour == 'jump':
                            print('you chose to jump and that was a good jump, now the next one')
                        elif parkour == 'walk' or parkour == 'walk away':
                            print('You chose to run away')
                            exit()
                        parkour2 = input('Do you want to jump?  ')
                        if parkour2 == 'yes' or parkour2 == 'jump':
                            print('You chose jump again and you completed the first puzzle')
                            print('Link, the second puzzle is a battle against some goblins. Good luck!')
                            print('You walk to the goblins and they are angry')
                            attack = input('Which attack do you want to do? You can choose between Charge Attack,Spin Attack or Fatal Blow ').lower()
                            if attack == 'Charge attack' or attack == 'spin attack' or attack == 'fatal blow':
                                print('You chose an attack and it was very effective')
                                print('Good job Link, the final puzzle is to find the Boss Key')
                                bosskey = input('Do you want to go left or right?  ')
                                if bosskey == 'left':
                                    print('you go left but its a trap so you die')
                                    exit()
                                elif bosskey == 'right':
                                    print('You walk to the right and see an chest')
                                    chestkey = input('Do you want to open the chest?  ')
                                    if chestkey == 'yes':
                                        print('You opened the chest and got the boss key!')
                                        print('you walk to the big door and opened it with the key')
                            fight = int(input('Are you sure you want to start this battle? if not, it ends here  '))
                            if fight == 'yes':
                                print('You walk to the boss and start the battle')
                                print('The boss is a big monkey')
                                print('You start the battle')
                                print('The boss is very strong')
                                attack2 = input('Which attack do you want to use? You can choose between Charge Attack, Fatal Blow or a Spin Attack  ').lower()
                                if attack2 == 'Charge attack' or attack2 == 'fatal blow' or attack2 == 'spin attack':
                                    print('You chose an attack and it was very effective')
                                    print('You killed the boss and you completed the dungeon!')
                                    hyrule = input('Do you want to go to Hyrule Castle?  ')
                                    if hyrule == 'yes':
                                        mastersword = input('Do you want to go to Hyrule Forest to get the Master Sword?')
                                        if mastersword == 'yes':
                                            print('You walk to Hyrule Forest')
                                            print('You see the Master Sword!')
                                            print('You walk to the Master Sword')
                                            print('You grab the Master Sword')
                                            print('You walk back to Hyrule Castle')
                                            print('You walk to the castle')
                                            print('You walk to the castle and see a big door')
                                            print('You see Ganon!')
                                            print('You walk to Ganon')
                                            print('You start the battle')
                                            print('Ganon is very strong')
                                            attack3 = input('Which attack do you want to use? You can choose between charge Attack or a Spin Attack  ').lower()
                                            if attack3 == 'charge attack' or attack3 == 'spin attack':
                                                print('You chose an attack and it was very effective')
                                                print('You killed Ganon and you completed the game!')
                                                print('You saved Hyrule!')
                                                print('You are the Hero of Time!')
                                                print('The End')
                                                exit()
                                        elif mastersword == 'no':
                                            print('You walk to Hyrule Castle')
                                            print('You walk to the castle')
                                            print('You walk to the castle and see a big door')
                                            print('You see Ganon!')
                                            print('You walk to Ganon')
                                            print('You start the battle')
                                            print('Ganon is very strong')
                                            attack3 = input('Which attack do you want to use? You can choose between Charge Attack, Spin Attack or a Skyward strike ').lower()
                                            if attack3 == 'charge attack' or attack3 == 'spin attack' or attack3 == 'skyward strike':
                                                print('You chose an attack and it was very effective')
                                                print('You almost killed Ganon!')
                                                attack4 = input('Which attack do you want to use? You can choose between Jump Attack, Fatal Blow or a Skyward Strike  ').lower()
                                                if attack4 == 'jump attack' or attack4 == 'fatal Blow' or attack4 == 'skyward Strike':
                                                    print('You chose an attack and it was very effective')
                                                    print('You killed Ganon and you completed the game!')
                                                    print('You saved Hyrule!')
                                                    print('You are the Hero of Time!')
                                                    print('The End')
                                elif chestkey == 'no':
                                    print('you need to open the chest to end this dungeon')
                                    exit()
                            elif fight == 'no':
                                print('You decided not to fight')    
                                exit()   
                    elif dungeon == 'no':
                        print('you need to enter this dungeon Link!')    
                        exit()         
            elif chest == 'no':
                print('you need to open the chest to go further')
                exit()

