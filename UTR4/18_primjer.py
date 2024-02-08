# Napišite program koji će unositi broj setova u teniskom meču. Nakon toga za svaki set 
# potrebno je unijeti A za pobjedu gema igrača A ili B za pobjedu gema igrača B. 
# Na kraju program treba ispisati konačni rezultat.

broj_setova = int(input("Molim vas da unesete broj setova: "))

set_a = 0
set_b = 0
gem_a = 0
gem_b = 0

for set in range(broj_setova):
    unos_pobjednika_gema = input("Unesite pobjednika gema: ")
    if unos_pobjednika_gema == 'A':
        gem_a += 1
    elif unos_pobjednika_gema == 'B':
        gem_b += 1

    if(gem_a == 6):
        set_a += 1
        gem_a = 0
    elif(gem_b == 6):
        set_b += 1
        gem_b = 0