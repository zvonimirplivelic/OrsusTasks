# Napišite program koji definira klasu Trokut s metodom opseg(self), koja računa opseg trokuta.
# Nakon toga, napišite program koji će omogućiti unos koordinata vrhova trokuta te ispisati opseg
# tog trokuta.

import math

class Tocka:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def udaljenost(self, t):
        return math.sqrt((self.x - t.x)**2 + (self.y - t.y)**2)

class Trokut:
    def __init__(self, tocka1, tocka2, tocka3):
        self.vrh1 = tocka1
        self.vrh2 = tocka2
        self.vrh3 = tocka3

    def opseg(self, ab, bc, ca):
        return ab + bc + ca
             

x1 = int(input("Unesite x koordinatu prve točke: "))
y1 = int(input("Unesite y koordinatu prve točke: "))
tocka1 = Tocka(x1, y1)

x2 = int(input("Unesite x koordinatu druge točke: "))
y2 = int(input("Unesite y koordinatu druge točke: "))
tocka2 = Tocka(x2, y2)

x3 = int(input("Unesite x koordinatu treće točke: "))
y3 = float(input("Unesite y koordinatu treće točke: "))
tocka3 = Tocka(x3, y3)

trokut = Trokut(tocka1, tocka2, tocka3)

duzina12 = tocka1.udaljenost(tocka2)
print(f"Udaljenost između točke 1 i točke 2: {duzina12:.2f}")
duzina23 = tocka2.udaljenost(tocka3)
print(f"Udaljenost između točke 2 i točke 3: {duzina23:.2f}")
duzina31 = tocka3.udaljenost(tocka1)
print(f"Udaljenost između točke 1 i točke 3: {duzina31:.2f}")

print(f"Opseg trokuta iznosi: {trokut.opseg(duzina12, duzina23, duzina31):.2f}")