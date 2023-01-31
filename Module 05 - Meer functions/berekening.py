def addition(number1, number2):
    return number1 + number2

def subtraction(number1, number2):
    return number1 - number2

def multiplication(number1, number2):
    return number1 * number2

def division(number1, number2):
    return number1 / number2

def calculator():
    result = 0
    while True:
        print("Wat wilt u doen? A) getallen optellen, B) getallen aftrekken, C) getallen vermenigvuldigen, D) getallen delen, E) getal ophogen, F) getal verlagen, G) getal verdubbelen, H) getal halveren of I) niets?")
        choice = input()
        if choice == 'a':
            n1 = float(input("Eerste getal: "))
            n2 = float(input("Tweede getal: "))
            result = addition(n1, n2)
        elif choice == 'b':
            n1 = float(input("Eerste getal: "))
            n2 = float(input("Tweede getal: "))
            result = subtraction(n1, n2)
        elif choice == 'c':
            n1 = float(input("Eerste getal: "))
            n2 = float(input("Tweede getal: "))
            result = multiplication(n1, n2)
        elif choice == 'd':
            n1 = float(input("Eerste getal: "))
            n2 = float(input("Tweede getal: "))
            result = division(n1, n2)
        elif choice == 'e':
            n1 = float(input("Getal: "))
            result = addition(n1, 1)
        elif choice == 'f':
            n1 = float(input("Getal: "))
            result = subtraction(n1, 1)
        elif choice == 'g':
            n1 = float(input("Getal: "))
            result = multiplication(n1, 2)
        elif choice == 'h':
            n1 = float(input("Getal: "))
            result = division(n1, 2)
        elif choice == 'i':
            break
        else:
            print("Ongeldige keuze.")
            continue

        print("Resultaat: ", result)

        print("Wil je wat met de uitkomst ({}) doen? A) iets optellen, B) iets aftrekken, C) met iets vermenigvuldigen, D) ergens door delen, E) ophogen, F) verlagen, G) verdubbelen, H) halveren of I) niets?".format(result))
        choice = input()
        if choice == 'i':
            break

calculator()
