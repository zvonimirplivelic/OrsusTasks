# Napišite program koji učitava polumjer i funkciju kruznica koja računa te ispisuje opseg i površinu
# kruga na 3 decimale. Funkcija mora vratiti dvije vrijednosti. Koristite math modul.

import math

m = math

def kruznica(r):
    opseg = round(float(2 * r * m.pi), 3)
    povrsina = round(float(r ** 2 * m.pi), 3)
    return opseg, povrsina

unos_polumjera = float(input(f"Molim vas da unesete polumjer kružnice: "))

opseg = kruznica(unos_polumjera)[0]
povrsina = kruznica(unos_polumjera)[1]


print(f"Polumjer kružnice je {unos_polumjera}, njen opseg iznosi {opseg} i površina je {povrsina}")