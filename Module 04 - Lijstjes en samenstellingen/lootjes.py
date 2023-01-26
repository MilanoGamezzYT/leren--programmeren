# lootjes verdeler met 3 of meer personen

from random import shuffle
lijst1 = []
lijst2 = []
stop = False
stop2 = False

while not stop:
    userinput = input('geef een naam voor op het lootje  ')
    if userinput not in lijst1:
        lijst1.append(userinput)
        lijst2.append(userinput)
    else:
        print('deze naam is al opgegeven')

    if len(lijst1) >= 3:
        nog_een_naam = input('wil je nog een naam toevoegen?  ').lower()
        if nog_een_naam == 'nee':
           stop = True

shuffle(lijst1)


while not stop2:
    shuffle(lijst1)
    stop2 = True
    for x in range(0,len(lijst2)):
        if lijst1[x] == lijst2[x]:
            stop2 = False
for x in range(0,len(lijst2)):
    print(f'{lijst1[x]} heeft {lijst2[x]} getrokken')
