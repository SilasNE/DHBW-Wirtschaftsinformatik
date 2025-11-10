import math

def f1(a, x, b):
    return a * math.sin(x + b)

def f2(a, b, x):
    return a * math.exp(b * x)


def main():
    try:
        choice = int(input("Welche Funktion möchten Sie auswählen? (1 oder 2): "))
    except ValueError:
        print("Ungültige Eingabe. Bitte 1 oder 2 eingeben.")
        return

    if choice == 1:
        print("Ihre Formel ist: f1(x) = a * sin(x + b)")
        try:
            a = float(input("Geben Sie den Wert für a ein: "))
            x = float(input("Geben Sie den Wert für x ein: "))
            b = float(input("Geben Sie den Wert für b ein: "))
        except ValueError:
            print("Ungültige Zahlenangabe.")
            return
        ergebnis = f1(a, x, b)
        print("Das Ergebnis von f1 ist:", ergebnis)

    elif choice == 2:
        print("Ihre Formel ist: f2(x) = a * e^(-b * x)")
        try:
            a = float(input("Geben Sie den Wert für a ein: "))
            b = float(input("Geben Sie den Wert für b ein: "))
            x = float(input("Geben Sie den Wert für x ein: "))
        except ValueError:
            print("Ungültige Zahlenangabe.")
            return
        ergebnis = f2(a, b, x)
        print("Das Ergebnis von f2 ist:", ergebnis)
    else:
        print("Bitte 1 oder 2 auswählen.")


if __name__ == "__main__":
    main()