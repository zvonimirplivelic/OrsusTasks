# Napišite program koji učitava broj, zatim ispisuje poruku da li je broj dvoznamenkasti

unos_broja = int(input("Unesite broj: "))

if unos_broja < 100 and unos_broja >= 10:
    print("Broj je dvoznamenkasti")
else:
    print("Broj nije dvoznamenkasti")