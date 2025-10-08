import math

loesungen = []


a = int(input("Gib stelle a ein: "))
b = int(input("Gib stelle b ein: "))
c = int(input("Gib stelle c ein: "))

pruefen = math.pow(b, 2) - 4 * a * c

if pruefen < 0:
    print("Hat keine Nullstelle!")
    
else:
    l1 = (-b + math.sqrt(math.pow(b, 2) - 4 * a * c)) / (2 * a)
    l2 = (-b - math.sqrt(math.pow(b, 2) - 4 * a * c)) / (2 * a)
    loesungen.append(l1)
    loesungen.append(l2)
    if l1 == l2: #if pruefen == 0 ist dasselbe
        print("Hat nur eine Nullstelle") 
        l1 = round(l1, 4)  
        print(l1)
    if l1 != l2:
        print("Hat Zwei Nullstellen") 
        l1 = round(l1, 4)
        l2 = round(l2, 4)
        print(l1)
        print(l2)
  
    


