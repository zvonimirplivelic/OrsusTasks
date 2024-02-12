# Napišite program koji će unositi dvije liste jednakih duljina. Dvije liste jednakih duljina mogu se
# skalarno množiti na način da zbrajamo umnoške elemenata s istim indeksima.

broj_n = int(input("Unesite prirodan broj n: "))

suma = 0
prva_lista = [0] * broj_n
druga_lista = [0] * broj_n

for i in range(broj_n):
    prva_lista[i] = int(input("Unesite broj prve liste: "))
    druga_lista[i] = int(input("Unesite broj druga liste: "))

print(prva_lista)
print(druga_lista)

for i in range(broj_n):
    suma += int(prva_lista[i]) * int(druga_lista[i])

print(suma)

