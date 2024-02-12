# Napišite program koji će unositi prirodan broj n, te brojeve a i b, a zatim u listu spremiti n nasumično
# odabranih brojeva iz intervala [a,b] . Program treba ispisati one od unesenih brojeva koji su parni.
from random import randint

broj_n = int(input("Unesite prirodan broj n: "))
broj_a = int(input("Unesite donju granicu: "))
broj_b = int(input("Unesite gornju granicu: "))

lista_brojeva = []
parni_brojevi = []

for i in range(broj_n):
    lista_brojeva.append(randint(broj_a, broj_b))

for i in lista_brojeva:
    if i % 2 == 0:
        parni_brojevi.append(i)

print(f"Lista brojeva: {lista_brojeva}")
print(f"Lista parnih brojeva: {parni_brojevi}")