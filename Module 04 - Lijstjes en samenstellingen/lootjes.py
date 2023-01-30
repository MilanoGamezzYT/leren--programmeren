# lootjes verdeler met 3 of meer personen

from random import shuffle
lijst1 = []
lijst2 = []
stop_namen = False
stop_lootjes = False

while not stop_namen:
    naam = input('Vul een naam in ')
    if naam not in lijst1:
        lijst1.append(naam)
        lijst2.append(naam)
    else:
        print('deze naam is al opgegeven')

    if len(lijst1) >= 3:
        nog_een_naam = input('Wil je meer namen toevoegen?  ').lower()
        if nog_een_naam == 'nee':
           stop_namen = True

shuffle(lijst1)


while not stop_lootjes:
    shuffle(lijst1)
    stop_lootjes = True
    for x in range(0,len(lijst2)):
        if lijst1[x] == lijst2[x]:
            stop_lootjes = False
for x in range(0,len(lijst2)):
    print(f'{lijst1[x]} heeft {lijst2[x]} getrokken')
