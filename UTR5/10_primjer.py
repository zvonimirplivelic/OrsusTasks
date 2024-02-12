# Napišite program koji će unositi prirodan broj n, a zatim listu od n elemenata. Program treba
# kreirati novu listu koja će sadržavati samo parne elemente iz početne liste.

broj_n = int(input("Unesite prirodan broj n: "))

lista_brojeva = []
parni_brojevi = []

for i in range(broj_n):
    unos_broja = int(input("Unesite broj u listu: "))
    lista_brojeva.append(unos_broja)

for i in lista_brojeva:
    if i % 2 == 0:
        parni_brojevi.append(i)

print(f"Lista brojeva: {lista_brojeva}")
print(f"Lista parnih brojeva: {parni_brojevi}")