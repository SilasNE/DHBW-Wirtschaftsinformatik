jahr = int(input("Welches Jahr wählst du? "))
monat = str(input("Welchen Monat wählst du? "))

dreißig = ["April", "Juni", "September", "November"]
einunddreißig = ["Januar", "Mai", "Juli", "August", "Oktober", "Dezember"] 
                 
if monat == 'Februar':
    if jahr % 4 == 0:
        if jahr % 100 == 0:
            if jahr % 400 == 0:
                print("Der Monat", monat, "Hat 29 Tage und ist im Jahr" ,jahr) 
            else:
                print("Der Monat", monat, "Hat 28 Tage und ist im Jahr" ,jahr)   
                
        else:
            print("Der Monat", monat, "Hat 29 Tage und ist im Jahr" ,jahr)   
    else:
        print("Der Monat", monat, "Hat 28 Tage und ist im Jahr" ,jahr)

        
if monat in dreißig:
    print("Der Monat", monat, "Hat 30 Tage und ist im Jahr" ,jahr)
            
            
if monat in einunddreißig:
    print("Der Monat", monat, "Hat 31 Tage und ist im Jahr" ,jahr)

            

