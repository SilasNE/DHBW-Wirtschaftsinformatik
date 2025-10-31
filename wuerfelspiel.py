import random

def a():

    spieler1 = 0
    spieler2 = 0

    zaehler1 = 0
    zaehler2 = 0

    while spieler1 < 10:
        wurf = random.randint(1, 6)
        zaehler1 += wurf
        spieler1 += 1

    print(f"Spieler 1 hat den Wert {zaehler1}")
    
    while spieler2 < 10:
        wurf = random.randint(1, 6)
        zaehler2 += wurf
        spieler2 += 1

    print(f"Spieler 2 hat den Wert {zaehler2}")


    if zaehler1 > zaehler2:
        print("Spieler 1 hat gewonnen!")

    elif zaehler1 < zaehler2:
        print("Spieler 2 hat gewonnen!")

    else:
        print("Kein Spieler hat gewonnen!")

def b():
    zahle1 = 0
    zahle2 = 0
    while zahle1 < 100 and zahle2 < 100:
        wurf1 = random.randint(1, 6)
        zahle1 += wurf1
        if zahle1 >= 100:
            print("Spieler 1 hat gewonnen!")
            break
        wurf2 = random.randint(1, 6)
        zahle2 += wurf2
        if zahle2 >= 100:
            print("Spieler 2 hat gewonnen!")
            break

def c():
    # Erster Spieler, der dreimal hintereinander die gleiche Zahl würfelt, gewinnt
    prev1 = None
    prev2 = None
    streak1 = 0
    streak2 = 0

    while True:
        # Spieler 1
        wurf1 = random.randint(1, 6)
        streak1 = streak1 + 1 if wurf1 == prev1 else 1
        prev1 = wurf1
        print(f"Spieler 1 würfelt: {wurf1} (Serie: {streak1})")
        if streak1 >= 3:
            print("Spieler 1 hat gewonnen!")
            break

        # Spieler 2
        wurf2 = random.randint(1, 6)
        streak2 = streak2 + 1 if wurf2 == prev2 else 1
        prev2 = wurf2
        print(f"Spieler 2 würfelt: {wurf2} (Serie: {streak2})")
        if streak2 >= 3:
            print("Spieler 2 hat gewonnen!")
            break

def d():
    while True:
        wurf1 = random.randint(1, 6)
        if wurf1 == 6:
            print("Spieler 1 hat Gewonnen!")
            break
        wurf2 = random.randint(1, 6)
        if wurf2 == 6:
            print("Spieler 2 hat Gewonnen!")
            break


if __name__ == "__main__":
    was = int(input("Was willst du Spielen (1-4)? "))
    if was == 1:
        a()
    elif was == 2:
        b()
    elif was == 3:
        c()
    elif was == 4:
        d()
    else:
        print("Bitte 1-4 wählen!")

