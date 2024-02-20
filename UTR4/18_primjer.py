# Napišite program koji će unositi broj setova u teniskom meču. Nakon toga za svaki set 
# potrebno je unijeti A za pobjedu gema igrača A ili B za pobjedu gema igrača B. 
# Na kraju program treba ispisati konačni rezultat.

unos_broj_setova = int(input("Molim vas da unesete broj setova teniskog meča: "))

set_a = 0
set_b = 0

for set in range(0, unos_broj_setova):
    rezultat_seta = input(f"Unesite (A ili B) pobjednike gemova {set + 1}. seta: ").upper()

    broj_poena_a = rezultat_seta.count("A")
    broj_poena_b = rezultat_seta.count("B")

    print(broj_poena_a)
    print(broj_poena_b)
    if broj_poena_a > broj_poena_b: 
        set_a += 1
    else:
        set_b += 1

print(f"Rezultat meča A protiv B je {set_a} : {set_b}")

    