# Napišite program koji učitava dvije točke A(x1,y1) i B(x2,y2) te zatim izračunava udaljenost između točaka

import math

tocka_ax = float(input("Molim vas da unesete x komponentu točke A:"))
tocka_ay = float(input("Molim vas da unesete y komponentu točke A:"))
tocka_bx = float(input("Molim vas da unesete x komponentu točke B:"))
tocka_by = float(input("Molim vas da unesete y komponentu točke B:"))

udaljenost_tocaka = float(math.sqrt((tocka_bx - tocka_ax)**2 + (tocka_by - tocka_ay)**2))

print(f"Udaljenost između točaka A i B iznosi: {udaljenost_tocaka}")