# Napišite program koji učitava broj bodova na ispitu koji je od 1 do 100,
# zatim ispisuje odgovarajuću ocjenu: (1) < 50 bodova; (2) od 50 do 59;
# (3) od 60 do 74; (4) od 75 do 89; (5) više od 90 bodova

unos_bodova = int(input("Unesite broj bodova: "))

if unos_bodova >= 1 and unos_bodova < 50:
    print("Nedovoljan")
elif unos_bodova >= 50 and unos_bodova <= 59:
    print("Dovoljan")
elif unos_bodova >= 60 and unos_bodova <= 74:
    print("Dobar")
elif unos_bodova >= 75 and unos_bodova <= 89:
    print("Vrlo dobar")
elif unos_bodova >= 90 and unos_bodova <= 100:
    print("Odličan")
else:
    print("Unesite ispravan broj bodova")