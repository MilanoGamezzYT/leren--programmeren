# lootjes verdeler met 3 of meer personen

from random import randint
naam = input("Geef je naam op: ")
personen = [naam]
while True:
    naam = input("Geef een naam op: ")
    if naam == "":
        break
    else:
        personen.append(naam)
print(personen)

