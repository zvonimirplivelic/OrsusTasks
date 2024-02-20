# Napišite program koji učitava broj i n te funkciju nti_korijen koja prima dva argumenta 
# te ispisuje n-ti korijen broja. Koristite math modul.

from math import pow

def nti_korijen(unos_broja, unos_potencije_korijena):
    return pow(unos_broja, (1 / unos_potencije_korijena))

unos_broja = int(input("Molim vas da unesete broj koji se korijenuje: "))
unos_potencije_korijena = int(input("Molim vas da unesete potenciju korijena: "))

print(f"{unos_potencije_korijena}. korijen broja {unos_broja} iznosi {nti_korijen(unos_broja, unos_potencije_korijena)}")
