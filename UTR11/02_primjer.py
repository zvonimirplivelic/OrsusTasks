# Napišite program koji će učitavati ime planine i visinu iskazanu u metrima (ime i visina su
# odvojeni zarezom) i te podatke upisivati u datoteku izlaz.txt tako da treba pretvoriti u kilometre.
# Kada korisnik unese riječ „gotovo“ prekida se unos podataka.

with open('izlaz.txt', 'a') as datoteka:
    while True:
        unos = input("Unesite ime planine i visinu odvojene zarezom ('gotovo' za kraj): ")
        if unos.lower() == 'gotovo':
            break
        ime, visina = unos.split(',')
        datoteka.write(f"{ime}, {float(visina) / 1000}km\n")