dagen_stoppen = input("Voer een dag in: ")

for dag in ("maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"):
    print(dag)
    if dag == dagen_stoppen:
        break