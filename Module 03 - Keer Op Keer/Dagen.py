vraag = input('Welke dag is het vandaag?')
dagen = ["maandag","dinsdag","woensdag","donderdag","vrijdag","zaterdag","zondag"]
while vraag != dagen[0]:
    print(dagen[0])
    dagen.pop(0)