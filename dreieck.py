import math

x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))
x3 = float(input("x3: "))
y3 = float(input("y3: "))

P1 = (x1, y1)
P2 = (x2, y2)
P3 = (x3, y3)

tuple = (P1, P2, P3)

def seite(p, q):  # für die Berechnung einer Seite um die heronische Formal einsetzen zu können
  return math.sqrt((q[0] - p[0])**2 + (q[1] - p[1])**2)

a = seite(P2, P3)
b = seite(P1, P3)
c = seite(P1, P2)


s = (a + b + c) / 2   #nun kann in die heronische Fomrak eingesetzt werden
A = math.sqrt(max(0.0, s * (s - a) * (s - b) * (s - c)))

print(f"Fläche A = {A}")
print(tuple)
