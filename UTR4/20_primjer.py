# Napišite program koji će unositi niz rezultata jednog nogometnog tima 
# te ispisuje broj ostvarenih bodova te najdulji niz bez poraza 
# te ispisuje ukupan broj bodova. Pobjedom (W – Win) je nogometni tim ostvario 3 boda, 
# neriješen rezultat (D – Draw) 1 bod, poraz (L – Lost) 0 bodova. 

unos_rezultata = input("Unesite niz rezultata (npr. WWLDLWDL): ").upper()
niz_bez_poraza = 0
najdulji_niz_bez_poraza = 0

broj_pobjeda = unos_rezultata.count('W')
broj_poraza = unos_rezultata.count('L')
broj_izjednacenih = unos_rezultata.count('D')

broj_bodova = broj_pobjeda * 3 + broj_izjednacenih

print(f"Broj bodova: {broj_bodova}")

for utakmica in unos_rezultata:

    if(utakmica == "L"):
        najdulji_niz_bez_poraza = niz_bez_poraza
        niz_bez_poraza = 0
    else:
        niz_bez_poraza += 1

    
print(f"Najdulji niz bez poraza: {najdulji_niz_bez_poraza}")

