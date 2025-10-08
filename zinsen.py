Anlagesumme = int(input("Geben Sie die Anlagesumme ein: "))
Zinssatz = float(input("Geben Sie den Zinssatz ein: "))
Laufzeit = int(input("Geben Sie die Laufzeit in Jahren ein: "))

print(Anlagesumme * (1 + Zinssatz / 100) ** Laufzeit)