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
        n1 = float(input("Eerste getal: "))
        n2 = float(input("Tweede getal: "))
        if choice == 'A':
            result = addition(n1, n2)
        elif choice == 'B':
            result = subtraction(n1, n2)
        elif choice == 'C':
            result = multiplication(n1, n2)
        elif choice == 'D':
            result = division(n1, n2)
        elif choice == 'E':
            n1 = float(input("Getal: "))
            result = addition(n1, 1)
        elif choice == 'F':
            n1 = float(input("Getal: "))
            result = subtraction(n1, 1)
        elif choice == 'G':
            n1 = float(input("Getal: "))
            result = multiplication(n1, 2)
        elif choice == 'H':
            n1 = float(input("Getal: "))
            result = division(n1, 2)
        elif choice == 'I':
            break
        else:
            print("Ongeldige keuze.")
            continue

        print("Resultaat: ", result)

        print("Wilt u nog een berekening doen? (J/N)")
        choice = input().lower()
        if choice == 'j':
            continue
        elif choice == 'n':
            break
        else:
            break
        
calculator()