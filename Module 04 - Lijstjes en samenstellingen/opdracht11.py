from fruitmand import fruitmand


isrond = False
rond = 0
nietrond = 0

while not isrond:
    kleur = input("Geef een kleur op ").lower()
    for i in fruitmand:
        if kleur == i['color']:
            if i['round']:
                rond += 1
            else:
                nietrond += 1
            isrond = True
    if not isrond:
        print(f"De kleur {kleur} zit er niet in de fruitmand")

if rond > nietrond:
    print(f'Er zijn {rond - nietrond} meer ronde vruchten dan niet ronde vruchten in de kleur {kleur}')
elif rond < nietrond:
        print(f'Er zijn {abs(rond - nietrond)} minder ronde vruchten dan niet ronde vruchten in de kleur {kleur}')
else:
    print(f'Er zijn {rond} ronde vruchten en {nietrond} niet ronde vruchten in de kleur {kleur}')
