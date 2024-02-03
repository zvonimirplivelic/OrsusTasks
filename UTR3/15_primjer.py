# Napišite program koji će učitati broj x i ispisati djelitelje broja x

broj_x = int(input("Unesite željeni broj: "))

for i in range (1, broj_x + 1):

    if(broj_x % i == 0):
        print(i)