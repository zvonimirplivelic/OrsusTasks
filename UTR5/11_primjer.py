# Napišite program koji će unositi prirodan broj n, a zatim listu od n elemenata te još jedan broj x.
# Program treba izbaciti svako pojavljivanje broja x iz te liste.

broj_n = int(input("Unesite prirodan broj n: "))
broj_x = int(input("Unesite prirodan broj x: "))

lista_brojeva = []

for i in range(broj_n):
    unos_broja = int(input("Unesite broj u listu: "))
    lista_brojeva.append(unos_broja)

lista_brojeva.remove(broj_x)

print(f"Lista brojeva bez broja {broj_x}: {lista_brojeva}")
