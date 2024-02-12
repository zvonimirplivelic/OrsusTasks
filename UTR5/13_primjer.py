# Napiši program koji će unositi prirodan broj n, a zatim n prirodnih brojeva u listu te još jedan
# prirodan broj x. Program treba iz početne liste izbaciti prvo pojavljivanje broja x (ostale brojeve
# treba pomaknuti za jedno mjesto)

broj_n = int(input("Unesite prirodan broj n: "))
broj_x = int(input("Unesite broj x: "))

lista_brojeva = []

for i in range(broj_n):
    unos_broja = int(input("Unesite broj: "))
    lista_brojeva.append(unos_broja)

print(f"Lista brojeva: {lista_brojeva}")

lista_brojeva.remove(broj_x)

print(f"Až. lista brojeva: {lista_brojeva}")