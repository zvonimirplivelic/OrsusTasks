# Napišite program koji će učitati broj N koji predstvlja proizvoljan unos brojeva.
# Nakon toga potrebno je ispisati koliko ima parnih, a koliko neparnih brojeva

parni_brojevi = 0
neparni_brojevi = 0

broj_n = int(input("Unesite koliko brojeva želite unijeti: "))

for i in range (broj_n):
    unos_broja = int(input("Unesite broj: "))

    if(unos_broja % 2 == 0):
        parni_brojevi += 1
    else: neparni_brojevi += 1

print(f"Broj parnih brojeva: {parni_brojevi}")
print(f"Broj neparnih brojeva: {neparni_brojevi}")
