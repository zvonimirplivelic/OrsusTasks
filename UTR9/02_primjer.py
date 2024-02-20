# Napišite program koji učitava koordinate dvije točaka i funkciju udaljenost koja vraća udaljenost
# između dvije točke. Koristite math modul.

from math import dist

def udaljenost_tocaka(p, q):
    return dist(p, q)

def unos_koordinata():
    tocka1.append(int(input("Molim vas da unesete x koordinatu prve točke: ")))
    tocka1.append(int(input("Molim vas da unesete y koordinatu prve točke: ")))
    tocka2.append(int(input("Molim vas da unesete x koordinatu druge točke: ")))
    tocka2.append(int(input("Molim vas da unesete y koordinatu druge točke: ")))
 
tocka1 = []
tocka2 = []

unos_koordinata()
print(f"Udaljenost točaka {tocka1} i {tocka2} iznosi: {udaljenost_tocaka(tocka1, tocka2)}")


