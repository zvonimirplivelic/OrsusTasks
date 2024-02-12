# Napišite program koji će unositi prirodan broj n, a zatim n prirodnih brojeva u listu te još dva
# prirodna broja x i y. Program treba u početnu listu ubaciti prirodan broj x na mjesto pod rednim
# brojem y.

broj_n = int(input("Unesite prirodan broj n: "))
broj_x = int(input("Unesite broj x: "))
broj_y = int(input("Unesite broj y: "))

lista_brojeva = []

for i in range(broj_n):
    unos_broja = int(input("Unesite broj: "))
    lista_brojeva.append(unos_broja)

print(f"Lista brojeva: {lista_brojeva}")

lista_brojeva[broj_y] = broj_x

print(f"Až. lista brojeva: {lista_brojeva}")