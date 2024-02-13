# Napišite program koji će učitati broj X koji je veći od 100 i predstavlja kraj intervala te
# zatim ispisuje sve troznamenkaste brojeve čiji je zbroj znamenki djeljiv s 5, 
# a koji se nalaze unutar intervala od 100 do N

unos_limita = int(input("Molim vas da unesete broj: "))

if unos_limita >= 100:
    for broj in range(100, unos_limita):
        broj_string = str(broj)
        suma_znamenaka = 0

        for znamenka in broj_string:
            suma_znamenaka += int(znamenka)

        if suma_znamenaka % 5 == 0:
            print(f"Zbroj znamenaka broja {broj} je dijeljiv s 5\n")




