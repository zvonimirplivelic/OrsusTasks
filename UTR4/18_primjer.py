# Napišite program koji će unositi broj setova u teniskom meču. Nakon toga za svaki set 
# potrebno je unijeti A za pobjedu gema igrača A ili B za pobjedu gema igrača B. 
# Na kraju program treba ispisati konačni rezultat.

unos_broja_setova = int(input("Molim vas da unesete broj setova:\n"))


gemovi_a = 0
gemovi_b = 0
setovi_a = 0
setovi_b = 0

for set in range(unos_broja_setova):
    unos_rezultata = input("Molim vas da unesete rezultate pojednika gemova (A ili B):\n").upper()

    gemovi_a = unos_rezultata.count("A")
    gemovi_b = unos_rezultata.count("B")

    if(gemovi_a > gemovi_b):
        setovi_a += 1
    else:
        setovi_b += 1

print(f"Rezultat teniskog meča je: {setovi_a} : {setovi_b}")


