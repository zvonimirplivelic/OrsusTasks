# Napišite program koji će unositi prirodan broj n, a zatim listu od n elemenata. 
# Program treba ispisati elemente te liste u obrnutom redoslijedu.

n = int(input("Unesite broj elemenata liste: "))

lista = [0] * n

for i in range(n):
    lista[i] = int(input("Molim vas unesite prirodan broj: "))

print(lista)

lista.reverse()
print(lista)
