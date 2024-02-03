# Napišite program koji će učitati broj X te ispisati obrnutim redoslijedom brojeve u intervalu od 1 do broja X

broj_x = int(input("Unesite broj x: "))

for i in range(broj_x, 0, -1):
    print(i)