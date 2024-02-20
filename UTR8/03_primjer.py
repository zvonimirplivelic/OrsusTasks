# Napišite program koji učitava jedan broj N i funkciju faktorijel koja vraća umnožak prvih N
# brojeva.

def faktorijel(unos_broja):

    faktorijel = 1
    for i in range(1, unos_broja + 1):       
        faktorijel *= i

    return faktorijel

unos_broja = int(input("Molim vas da unesete broj: "))

print(f"Faktorijel unešenog broja {unos_broja}! iznosi: {faktorijel(unos_broja)}")