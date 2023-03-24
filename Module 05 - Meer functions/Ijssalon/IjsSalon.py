# maak een dry ijssalon met behulp van de flowchart

aantal = input("Welkom bij papi Gelato, hoeveel bolletjes wilt u bestellen?  ")
if aantal == "1" or "2" or "3":
    keuze = input("Prima, wilt uw een bakje of een hoorntje?")
    if keuze == "bakje":
        print(f'hier is uw {keuze} met {aantal} bolletje(s)')
    elif keuze == "hoorntje":
        print(f'hier is uw {keuze} met {aantal} bolletje(s)')
        
    else:
        print("sorry, dat snap ik niet..")

elif aantal == "4" or "5" or "6" or "7" or "8":
    print("Prima, u krijgt een bakje")
elif aantal > 8:
    print("Sorry, zulke grote bakken hebben we niet")
else: 
    print("Sorry, dat snap ik niet...")