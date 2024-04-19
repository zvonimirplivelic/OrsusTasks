# Napišite program koji definira klasu Trokut s metodom povrsina(self), koja računa površinu
# trokuta. Nakon toga, napišite program koji će omogućiti unos koordinata vrhova trokuta te
# ispisati površinu tog trokuta.

import math

class Tocka:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Trokut:
    def __init__(self, tocka1, tocka2, tocka3):
        self.vrh1 = tocka1
        self.vrh2 = tocka2
        self.vrh3 = tocka3

    def povrsina(self):
        a = self.vrh1.udaljenost(self.vrh2)
        b = self.vrh2.udaljenost(self.vrh3)
        c = self.vrh3.udaljenost(self.vrh1)
        
        s = (a + b + c) / 2  # poluopseg
        povrsina = math.sqrt(s * (s - a) * (s - b) * (s - c))
        
        return povrsina


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

print(f"Površina trokuta iznosi: {trokut.povrsina():.2f}")