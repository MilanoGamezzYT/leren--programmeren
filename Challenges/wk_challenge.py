wedstrijd = 0
while wedstrijd < 3:
    wedstrijd += 1
    thuis = input('Wie speelt thuis? ')
    uit = input('Wie speelt uit? ')
    doelpunten_thuis = int(input('Hoeveel doelpunten maakt het thuisland? '))
    doelpunten_uit = int(input('Hoeveel doelpunten maakt het uitland? '))
    if doelpunten_thuis > doelpunten_uit:
        winnaar = thuis
    elif doelpunten_thuis < doelpunten_uit:
        winnaar = uit
    print(f'Wedstrijd: {wedstrijd}, Thuisland: {thuis}, Uitland: {uit}, Doelpunten Thuisland: {doelpunten_thuis}, Doelpunten Uitland {doelpunten_uit}')
    doelsaldo_thuis = doelpunten_thuis - doelpunten_uit
    doelsaldo_uit = doelpunten_uit - doelpunten_thuis
    if wedstrijd == 1:
        print(f'de winnaar is {winnaar} en doelsaldo is {doelsaldo_thuis or doelsaldo_uit}')
    if wedstrijd == 2:
        print(f'de winnaar is {winnaar} en doelsaldo is {doelsaldo_thuis or doelsaldo_uit}')
    if wedstrijd == 3:
        print(f'de winnaar is {winnaar} en doelsaldo is {doelsaldo_thuis or doelsaldo_uit}')


    




