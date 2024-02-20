# Napišite glavni program i lambda izraz provjeri koja provjerava da li je broj djeljiv s 5.

unos_broja = int(input("Unesite broj: "))

provjeri_djeljivost = lambda x: x % 5 == 0

if provjeri_djeljivost(unos_broja):
    print(f"Broj {unos_broja} je djeljiv s 5.")
else:
    print(f"Broj {unos_broja} nije djeljiv s 5.")