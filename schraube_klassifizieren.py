while True:

    durchmaesser = float(input("Durchmesser in mm: "))
    laenge = int(input("Länge in mm: "))
    
    if durchmaesser < 21 and laenge < 51:
    
        if durchmaesser < 7 and laenge < 31:
        
            if durchmaesser < 4 and laenge < 21:
                print("Typ1")
            else:
                print("Typ2")
    
        else: 
            print("Typ3")

    else:
        print("Unbekannter Schraubentyp!")
        break


