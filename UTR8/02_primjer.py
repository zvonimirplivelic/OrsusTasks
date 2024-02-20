# Napišite program koji učitava jedan broj N i funkciju sumator koja vraća zbroj prvih N brojeva.

def sumator(unos_broja):

    suma_brojeva = 0
    for i in range(1, unos_broja + 1):

        print(f"sum:{suma_brojeva} + i:{i}")

        suma_brojeva += i

    return suma_brojeva



unos_broja = int(input("Molim vas da unesete broj: "))

print(f"Zbroj svih brojeva do broja {unos_broja} iznosi: {sumator(unos_broja)}")
