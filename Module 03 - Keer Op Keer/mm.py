import random

rondes = 0
punten = 0
antwoord = ""
nieuwe_ronde = ""

raden = 10
UserGuess = ""

while raden != 0:
    number = random.randint(1,1000)
    while not ((UserGuess:= input("Zeg \"stop\" om te stoppen, of raad tussen 1 en 1000")).isdigit() and 1 < int(UserGuess) < 1000):
        if UserGuess.lower() == "stop":
            exit(f"Jammer dat je gaat stoppen met een score van {punten} in ronde {rondes}")
        print('Ik zei tussen 1 en 1000 of stop')

    UserGuess = int(UserGuess)

    if UserGuess == number:
        guesses = 0
        rondes += 1
        punten += 1
    else:
        raden -= 1

        if number > UserGuess and number - UserGuess > 50:
            print('hoger')
        elif UserGuess > number and UserGuess - number > 50:
            print('lager')
        elif number > UserGuess and 50 > number - UserGuess > 20:
           print('je wordt warm, gok hoger')
        elif UserGuess > number and 50 > UserGuess - number > 20:
            print('Je wordt warm, gok lager')
        elif number > UserGuess and number - UserGuess < 20:
            print('je wordt heel warm, gok hoger')
        elif UserGuess > number and UserGuess - number < 20:
            print('je wordt heel heet, gok lager')
