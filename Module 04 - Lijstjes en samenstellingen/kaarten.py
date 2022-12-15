import random

KaartTypes = ("harten ", "klaveren ", "schoppen ", "ruiten ")
Nummers = ("aas", "2", "3", "4", "5", "6", "7", "8", "9", "10", "boer", "vrouw", "koning")
Deck = ["joker", "joker"]

for x in (KaartTypes):
    for y in (Nummers):
        optellen = x + y 
        Deck.append(optellen)

random.shuffle(Deck)
for z in range(1,8):
    print(f'Kaart {z}: {Deck[z]}')
    Deck.pop(z)

print(f"deck {len(Deck)} kaarten: {Deck}")