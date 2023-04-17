def welkom():
    print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.")

def hoeveelheid():
    bolletjes = input("Hoeveel bolletjes wilt u? ")
    if bolletjes.isdigit():
        bolletjes = int(bolletjes)
        if bolletjes >= 1 and bolletjes <= 3:
            return bolletjes
        elif bolletjes >= 4 and bolletjes <= 8:
            print(f"Dan krijgt u van mij een bakje met {bolletjes} bolletjes")
            return bolletjes
        elif bolletjes > 8:
            print("Sorry, zulke grote bakken hebben we niet")
            return hoeveelheid()
    else:
        print("Sorry dat snap ik niet...")
        return hoeveelheid()

def hoorntje_bakje(bolletjes):
    keuze = input(f"Wilt u deze {bolletjes} bolletje(s) in een hoorntje of een bakje? ")
    if keuze.lower() == "hoorntje" or keuze.lower() == "bakje":
        return keuze
    else:
        print("Sorry, dat snap ik niet...")
        return hoorntje_bakje(bolletjes)

def serve_ijs(bolletjes, keuze):
    print(f"Hier is uw {keuze} met {bolletjes} bolletje(s).")
    antwoord = input("Wilt u nog meer bestellen? ")
    if antwoord.lower() == "ja":
        return True
    elif antwoord.lower() == "nee":
        print("Bedankt en tot ziens!")
        return False
    else:
        print("Sorry, dat snap ik niet...")
        return serve_ijs(bolletjes, keuze)

def bestel_ijs():
    welkom()
    while True:
        bolletjes = hoeveelheid()
        keuze = hoorntje_bakje(bolletjes)
        if not serve_ijs(bolletjes, keuze):
            break

bestel_ijs()