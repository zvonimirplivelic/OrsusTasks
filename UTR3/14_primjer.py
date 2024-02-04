# Napišite program koji će učitati broj N koji predstavlja proizvoljan unos brojeva.
# Nakon toga je potrebno ispisati sumu parnih brojeva i umnožak neparnih

parni_brojevi = 0
neparni_brojevi = 1

broj_n = int(input("Unesite koliko brojeva želite unijeti: "))

for i in range (broj_n):
    unos_broja = int(input("Unesite broj: "))

    if(unos_broja % 2 == 0):
        parni_brojevi +=  unos_broja
    else: neparni_brojevi *=  unos_broja

print(f"Broj parnih brojeva: {parni_brojevi}")
print(f"Broj neparnih brojeva: {neparni_brojevi}")
