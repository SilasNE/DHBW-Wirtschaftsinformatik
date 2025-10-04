produktkategorien = []
hersteller = []
preise = []

x = 0
while x < 3:
    kategorie = input("Nenne mir die Produktkategorie: ")
    produktkategorien.append(kategorie)
    steller = input("Nenne mir den Hersteller: ")
    hersteller.append(steller)
    eise = int(input("Nenne mir den Preis: "))
    preise.append(eise)
    x = x + 1  # oder x += 1s

print(produktkategorien)
print(hersteller)
print(preise)




