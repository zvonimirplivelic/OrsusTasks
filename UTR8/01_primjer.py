# Napišite program koji učitava jedan broj i funkciju provjera koja vraća poruku da li je broj djeljiv s
# brojem 5.

def provjera(unos_broja):
    poruka = ""

    if unos_broja % 5 == 0:
        poruka = print("Broj je djeljiv s 5")
    else:
        poruka = print("Broj nije djeljiv s 5")
        
    return poruka

unos_broja = int(input("Molim vas da unesete broj: "))
provjera(unos_broja)
