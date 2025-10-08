import math

Seite1 = float(input("Geben Sie die Seite a ein: "))
Seite2 = float(input("Geben Sie die Seite b ein: "))
Seite3 = float(input("Geben Sie die Seite c ein: "))


s = (Seite1 + Seite2 + Seite3) / 2

A = (math.sqrt(s*(s-Seite1)*(s-Seite2)*(s-Seite3)))
print(A)