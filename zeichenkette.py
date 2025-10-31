def anzahl_zeichen(zeichenkette):
    return len(zeichenkette)

def anzahl_buchstaben(zeichenkette):
    return sum(c.isalpha() for c in zeichenkette)

def anzahl_zeichen_B(zeichenkette):
    count = 0
    for c in zeichenkette:
        if c.lower() == 'b':
            count += 1
    return count
        
if __name__ == "__main__":
    zeichenkette = input("Gebe bitte eine Zeichenkette ein: ")
    print(f"Die eingegebene Zeichenkette lautet: {zeichenkette}")
    print(f"Die Anzahl der Zeichen beträgt: {anzahl_zeichen(zeichenkette)}")
    print(f"Die Anzahl der Buchstaben beträgt: {anzahl_buchstaben(zeichenkette)}")
    print(f"Die Anzahl des Buchstaben b beträgt: {anzahl_zeichen_B(zeichenkette)}")