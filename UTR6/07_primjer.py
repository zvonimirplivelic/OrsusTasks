# Napišite program koji će unositi riječ i ispisivati ukupni broj slova koja se u toj riječi pojavljuju dva
# ili više puta. Potrebno je riješiti zadatak koristeći rječnik.

rijec = input("Unesite riječ: ")
brojac_slova = {}

for slovo in rijec:
    brojac_slova[slovo] = brojac_slova.get(slovo, 0) + 1

ukupno_slova = 0

for slovo, broj in brojac_slova.items():
    if broj >= 2:
        ukupno_slova += 1

print(f"Ukupni broj slova koja se pojavljuju dva ili više puta: {ukupno_slova}")