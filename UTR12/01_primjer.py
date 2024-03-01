# Napišite program koji definira klasu Krug. Svaka instanca ove klase predstavlja krug s određenim
# polumjerom. Klasa Krug treba imati metode za računanje opsega kruga (opseg()) i površine kruga
# (povrsina()). Nakon toga, program treba omogućiti korisniku unos duljine polumjera, stvaranje
# objekta tipa Krug s tim polumjerom i ispisivanje izračunatog opsega i površine kruga, pri čemu se
# rezultati zaokružuju na dvije decimale.

import math

class Krug:
    def __init__(self, polumjer):
        self.polumjer = polumjer

    def opseg(self):
        return 2 * math.pi * self.polumjer

    def povrsina(self):
        return math.pi * self.polumjer**2

polumjer = float(input("Unesite duljinu polumjera kruga: "))

krug = Krug(polumjer)

print(f"Opseg kruga: {krug.opseg():.2f}\n" +
    f"Površina kruga: {krug.povrsina():.2f}")
