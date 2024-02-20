# Napiši program koji će unositi prirodan broj n, a zatim n prirodnih brojeva većih od 1. Program
# treba ispisati one od unesenih brojeva koji su prosti. Provjeru za proste brojeve treba se odraditi
# u funkciji prosti.

def prosti(broj):
    if broj < 2:
        return False
    for i in range(2, int(broj**0.5) + 1):
        if broj % i == 0:
            return False
    return True

n = int(input("Unesite prirodan broj n: "))

brojevi = []
prosti_brojevi = []

for i in range(n):
    unos = int(input(f"Unesite prirodan broj veći od 1: "))
    brojevi.append(unos)
    if prosti(unos):
        prosti_brojevi.append(unos)

print(f"Svi uneseni brojevi su: {brojevi}\nProsti brojevi su: {prosti_brojevi}")
      
