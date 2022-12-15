import random

kaarten = ('ruiten ', 'schoppen ', 'klaveren ', 'harten')
cijfers = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'boer', 'vrouw', 'koning', 'aas')
deck = ['joker', 'joker']

for m in (kaarten):
    for s in (cijfers):
        optellen = m + s
        deck.append(optellen)
random.shuffle(deck)

print(f"deck ({len(deck)} kaarten): {deck}")