# Napišite program koji definira klasu Tocka, čija će svojstva biti koordinate jedne točke u
# koordinatnom sustavu. Nakon toga, definirajte klasu Trokut, čija će svojstva biti koordinate
# vrhova trokuta, pri čemu će ti vrhovi biti objekti tipa Tocka. Nad klasom Tocka, definirajte
# metodu udaljenost(self, t) koja će vraćati udaljenost između dviju točaka. Napišite program koji
# će omogućiti unos koordinata dviju točaka te ispisati njihovu međusobnu udaljenost

import math

class Tocka:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def udaljenost(self, t):
        return math.sqrt((self.x - t.x)**2 + (self.y - t.y)**2)

x1 = float(input("Unesite x koordinatu prve točke: "))
y1 = float(input("Unesite y koordinatu prve točke: "))
tocka1 = Tocka(x1, y1)
x2 = float(input("Unesite x koordinatu druge točke: "))
y2 = float(input("Unesite y koordinatu druge točke: "))
tocka2 = Tocka(x2, y2)

udaljenost_tocaka = tocka1.udaljenost(tocka2)
print(f"Udaljenost između točke 1 i točke 2: {udaljenost_tocaka:.2f}")