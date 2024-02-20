# Napišite program koji će unositi broj i funkciju znamenke koja će vraćati zbroj znamenaka
# zadanog broja

def znamenke(unos_broja):

    zbroj_znamenaka = 0

    while unos_broja > 0:
        zbroj_znamenaka += unos_broja % 10
        unos_broja //= 10
    
    return zbroj_znamenaka

unos_broja = int(input("Molim vas da unesete broj: "))

print(f"Zbroj znamenaka broja {unos_broja} je: {znamenke(unos_broja)}")
