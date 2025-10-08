zahl = int(input("Geben Sie eine Zahl ein: "))

groß = zahl // 144
rest = zahl % 144
   

schock = rest // 60
rest = rest % 60


dutzend = rest // 12
rest = rest % 12


rest1 = rest // 12
rest = rest % 12


print(groß, "Groß passen rein.")
print(schock, "Schock passen rein.")
print(dutzend, "Dutzend passen rein.")
print(rest, "ist der Rest.")