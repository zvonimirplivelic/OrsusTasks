# Napišite program koji će unositi brojeve sve dok se ne unese negativan broj, 
# zatim treba ispisati prosjek unesenih brojeva bez negativnog broja

suma_brojeva = 0
brojac = 0

while True:
    unos_broja = int(input("Molimo vas da unesete broj:"))
    if unos_broja < 0:
        break
    else:
        brojac += 1
        suma_brojeva += unos_broja

print(f"Unijeli ste {brojac} brojeva, čiji je prosjek {suma_brojeva / brojac}")