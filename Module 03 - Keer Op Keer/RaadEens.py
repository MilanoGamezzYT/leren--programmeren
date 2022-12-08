import random
MAX_RONDES = 10
MAX_GAMES = 20
game = 0
punt = 0
stop = False
while game != MAX_GAMES and stop == False:
    game += 1
    computer_getal = random.randint(1,1000)
    print(computer_getal)
    rondes = 0  
    while rondes < MAX_RONDES:
        rondes += 1
        speler_getal = int(input('type een nummer tussen 1 en 1000:  '))
        if speler_getal == computer_getal:
            print('correct +1 punt')
            punt += 1
            break
        else:
            if rondes < MAX_RONDES:
                if speler_getal > computer_getal:
                    print('Lager')
                else:
                    print('hoger')
                verschil = computer_getal - speler_getal
                if verschil < 0 :
                    verschil *= -1
                if verschil <= 20:
                    print('je bent erg warm')
                elif verschil <= 50:
                    print('je bent warm')
            else:
                print(f'je hebt {MAX_RONDES} rondes gespeeld')
    if game < MAX_GAMES:
        nog_een_keer = input('wil je nog een keer?  ').lower()
        if nog_een_keer == 'nee':
                print(f'Je bent met {punt} punten geëindigt en na {rondes} ronde(s) gestopt.')
                stop = True
        else :
            print(f'{punt} aantal punten')
            print('volgende ronde')    
    else:
        print('bedankt voor het spelen!') 