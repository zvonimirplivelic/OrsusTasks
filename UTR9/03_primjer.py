# Napišite program koji će zamisliti broj između 0 i 100 te svaki puta ispisati poruku da li je broj
# bliže donjoj granici ili gornjoj ovisno o unosu korisnika. Korisnik ima pravo na 10 unosa. Koristite
# random modul.

import random

def rand_broj():
    return random.randint(0,100)

def provjera_granice(i):
    if zamišljen_broj < i:
        print("Broj je bliži donjoj granici")
    elif zamišljen_broj > i:
        print("Broj je bliži gornjoj granici")

broj_pokusaja = 10
zamišljen_broj = rand_broj()

while broj_pokusaja > 0:
    unos_broja = int(input(f"Pokušajte pogoditi zamišljen broj: "))
    if(zamišljen_broj == unos_broja):
        print(f"Čestitamo!!! Pogodili ste zamišljen broj: {zamišljen_broj}")
        break
    else:
        broj_pokusaja -= 1
        provjera_granice(unos_broja)
        
    

