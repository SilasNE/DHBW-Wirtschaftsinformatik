while True:
    durchmaesser = int(input("Durchmesser in mm: "))
    laenge = int(input("Länge in mm: "))

    if 4 <= durchmaesser <= 6 and 21 <= laenge <= 30:
        print("Typ2")
        print("Unbekannter Schraubentyp!")
        break
        
    elif 7 <= durchmaesser <= 20 and 31 <= laenge <= 50:
        print("Typ3")

    elif 0 < durchmaesser <= 3 and  laenge <= 20:
        print("Typ1")

    else:
        print("Unbekannter Schraubentyp!")
        break


