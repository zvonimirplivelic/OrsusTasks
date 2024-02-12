# Napišite program koji učitava četiri različite ocjene od 1 do 5. Unos svake ocjene mora prvo biti
# provjeren. Nakon što korisnik unese četiri ocjene od 1 do 5 potrebno je ispisati ocjenu koja
# nedostaje. Potrebno je riješiti zadatak koristeći skupove.

skup_ocjena = set()
ocjene = {1,2,3,4,5}

for o in range(0,4):
    o = int(input("Molim vas unesite ocjenu: "))
    if o < 1 or o > 5:
        print("Molim vas da unesete ocjenu između 1 i 5")
    else:
        skup_ocjena.add(o)

print(f"Ocjena koja nedostaje je: {(ocjene - skup_ocjena)}")