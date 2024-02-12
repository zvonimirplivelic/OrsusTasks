# Napišite program koji će unositi prirodan broj n, a zatim listu od n elemenata. Program treba
# ispisati one od unesenih brojeva koji su djeljivi s 3.

n = int(input("Unesite broj elemenata liste: "))

lista = [0] * n

for i in range(n):
    lista[i] = int(input("Molim vas unesite prirodan broj: "))
print(lista)

for j in range(n):
    if lista[j] % 3 == 0:
        print(lista[j])
