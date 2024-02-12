# Napiši program koji će unositi prirodan broj n, te prirodan broj x. Program treba kreirati listu s n
# slučajnih brojeva iz intervala [10,20]. Program treba iz početne liste izbaciti svako pojavljivanje
# prirodnog broja x (ostale brojeve treba pomaknuti za jedno mjesto).

from random import randint

broj_n = int(input("Unesite prirodan broj n: "))
broj_x = int(input("Unesite prirodan broj x: "))


lista_brojeva = []

for i in range(broj_n):
    lista_brojeva.append(randint(10, 20))

print(f"Lista brojeva: {lista_brojeva}")

while broj_x in lista_brojeva: lista_brojeva.remove(broj_x)

print(f"Ažr. lista brojeva: {lista_brojeva}")
