while True:
    durchmaesser = int(input("Durchmesser in mm: "))
    laenge = int(input("Länge in mm: "))

    # Obergrenzen prüfen (bis 20mm Durchmesser und bis 50mm Länge)
    if durchmaesser <= 20 and laenge <= 50:
        # Bis 6mm/30mm kann Typ1 oder Typ2 sein
        if durchmaesser <= 6 and laenge <= 30:
            # Typ1: d <= 3 und l <= 20
            if durchmaesser <= 3 and laenge <= 20:
                print("Typ1")
            # Typ2: 4 <= d <= 6 und 21 <= l <= 30
            elif 4 <= durchmaesser <= 6 and 21 <= laenge <= 30:
                print("Typ2")
            else:
                print("Unbekannter Schraubentyp!")
                break
        # Typ3: 7 <= d <= 20 und 31 <= l <= 50
        elif 7 <= durchmaesser <= 20 and 31 <= laenge <= 50:
            print("Typ3")
        else:
            print("Unbekannter Schraubentyp!")
            break
    else:
        print("Unbekannter Schraubentyp!")
        break


