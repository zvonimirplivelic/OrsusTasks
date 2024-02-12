# Napišite program koji će unositi prirodan broj n. Program treba kreirati listu s n slučajnih brojeva iz
# intervala [10,20]. Program treba obrnuti početnu listu.

from random import randint

broj_n = int(input("Unesite prirodan broj n: "))

lista_brojeva = []

for i in range(broj_n):
    lista_brojeva.append(randint(10, 20))

print(f"Lista brojeva: {lista_brojeva}")

lista_brojeva.reverse()

print(f"Ažr. lista brojeva: {lista_brojeva}")
