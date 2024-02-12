# Napišite program koji će učitati broj te ispisati sumu njegovih znamenaka

unos_broja = input("Molim vas da unesete broj: ")
suma = 0

for i in unos_broja:
    #print(f"{suma} +* {int(i)}")
    suma += int(i)

print(suma)

