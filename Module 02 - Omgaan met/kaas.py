kaas_geel = input('Is de kaas geel?').lower()
if kaas_geel == 'ja':
    gaten_kaas = input('Zitten er gaten in?').lower()
    if gaten_kaas == 'ja': 
        prijs_kaas = input('Is de kaas belachelijk duur?').lower()
        if prijs_kaas == 'ja':
            input('Het is de Emmenthaler!')
        elif prijs_kaas == 'nee':
            input('Het is de Leerdammer!')
    elif gaten_kaas == 'nee':
        kaas_hard = input('Is de kaas hard als steen?').lower()
        if kaas_hard == 'ja':
            input('Het is de Parmigiano Reggiano!')
        elif kaas_hard == 'nee':
            input('Het is de Goudse Kaas!')
elif kaas_geel == 'nee':
    schimmel_kaas = input('Heeft de kaas blauwe schimmel?').lower()
    if schimmel_kaas == 'ja':
        korst_kaas = input("Heeft de kaas een korst?").lower()
        if korst_kaas == 'ja':
            input('Het is de Blue de Rochbaron!')
        elif korst_kaas == 'nee':
            input('Het is de Foumme dAmbert!')
    elif schimmel_kaas == 'nee':
        korst_kaas2 =  input("Heeft de kaas een korst?").lower()
        if korst_kaas2 == 'ja':
            input('Het is de Camembert!')
        elif korst_kaas2 == 'nee':
            input('Het is de Mozzarella!')
    


