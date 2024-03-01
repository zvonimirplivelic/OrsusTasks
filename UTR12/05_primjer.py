# Napišite program koji definira klasu Trokut s metodama jednakostraničan(self),
# jednakokračan(self) i raznostraničan(self), koje će vraćati True ako je trokut jednakostraničan,
# jednakokračan ili raznostraničan, redom. Metode trebaju raditi na principu usporedbe duljina
# stranica trokuta. Nakon toga, napišite program koji će omogućiti unos koordinata vrhova trokuta
# i ispisati kakav je trokut (jednakostraničan, jednakokračan ili raznostraničan).

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

    def jednakostraničan(self):
        a = self.vrh1.udaljenost(self.vrh2)
        b = self.vrh2.udaljenost(self.vrh3)
        c = self.vrh3.udaljenost(self.vrh1)

        return a == b == c

    def jednakokračan(self):
        a = self.vrh1.udaljenost(self.vrh2)
        b = self.vrh2.udaljenost(self.vrh3)
        c = self.vrh3.udaljenost(self.vrh1)

        return a == b or b == c or c == a

    def raznostraničan(self):
        a = self.vrh1.udaljenost(self.vrh2)
        b = self.vrh2.udaljenost(self.vrh3)
        c = self.vrh3.udaljenost(self.vrh1)

        return a != b != c != a

x1 = float(input("Unesite x koordinatu vrha 1: "))
y1 = float(input("Unesite y koordinatu vrha 1: "))
vrh1 = Tocka(x1, y1)   

x2 = float(input("Unesite x koordinatu vrha 2: "))             
y2 = float(input("Unesite y koordinatu vrha 2: "))
vrh2 = Tocka(x2, y2)   

x3 = float(input("Unesite x koordinatu vrha 3: "))
y3 = float(input("Unesite y koordinatu vrha 3: "))
vrh3 = Tocka(x3, y3)

trokut = Trokut(vrh1, vrh2, vrh3)

if trokut.jednakostraničan():
    print("Trokut je jednakostraničan.")
elif trokut.jednakokračan():
    print("Trokut je jednakokračan.")
elif trokut.raznostraničan():
    print("Trokut je raznostraničan.")
else:
    print("Nepoznat tip trokuta.")

    