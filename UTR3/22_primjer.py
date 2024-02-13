# Napišite program koji će učitati brojeve sve dok se ne unese negativan broj
# te ispisati za svaki učitani broj izračunati korijen
import math

unos_broja = 0
while unos_broja >= 0:
    unos_broja = float(input("Molim vas da unesete broj: "))
    
    if unos_broja < 0: 
        print("Unijeli ste negativan broj")
        break
    korijen_broja = math.sqrt(unos_broja)
    print(f"Korijen broja {unos_broja} je: {korijen_broja}")
