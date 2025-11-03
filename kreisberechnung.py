import math

def umfang_von_kreis():
    radius = float(input("Geben Sie den Radius des Kreises ein: "))
    umfang = 2 * math.pi * radius
    print(f"Der Umfang des Kreises beträgt: {umfang}")

def flaeche_von_kreis():
    radius = float(input("Geben Sie den Radius des Kreises ein: "))
    flaeche = math.pi * radius**2
    print(f"Die Fläche des Kreises beträgt: {flaeche}")

def umfang_von_kreis2():
    radius = float(input("Geben Sie den Radius des Kreises ein: "))
    umfang = 2 * math.pi * radius
    return umfang

def flaeche_von_kreis2():
    radius = float(input("Geben Sie den Radius des Kreises ein: "))
    flaeche = math.pi * radius**2
    return flaeche

if __name__ == "__main__":
    menge = int(input("Wie viele Kreise möchten Sie berechnen? "))
    x = 0
    y = 0
    was = input("Möchten Sie den Umfang oder die Fläche berechnen? (u/f): ").lower()
    if was == 'f':
        if menge == 1:
            flaeche_von_kreis()
        else:
            for _ in range(menge):
                y += flaeche_von_kreis2()
            print("Die Summe der Flächen der Kreise ergibt ", y)
    else:
        if menge == 1:
            umfang_von_kreis()  
        else:
            for _ in range(menge):
                x += umfang_von_kreis2()
            print("Die Summe der Umfänge der Kreise ergibt ", x)