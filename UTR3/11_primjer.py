# Napišite program koji će učitati broj X te ispisati zbroj svih brojeva od 1 do broja X

broj_x = int(input("Unesite željeni broj: "))
rezultat = 0

for broj_x in range (1, broj_x +1):
    rezultat = rezultat + broj_x

print(rezultat)