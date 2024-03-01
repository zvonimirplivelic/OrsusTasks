# Napisati funkciju prebroji koja broji koliko se puta traženi znak
# pojavljuje u nizu. Napisati program koji će učitati niz znakova,
# provjeriti da je najviše 20 znakova učitano. Nakon toga u
# slijedećem retku učitati znak koji tražimo. Potrebno je ispisati
# koliko ima traženih znakova u rečenici.

def prebroji_znak(niz, trazeni_znak):
    return niz.count(trazeni_znak)

niz = input("Unesite niz znakova (najviše 20 znakova): ")[:20]

if len(niz) >= 20:
    niz = input("Niz znakova mora imati manje od 20 znakova. Unesite ponovno: ")[:20]

trazeni_znak = input("Unesite traženi znak: ")

if len(trazeni_znak) == 1:
    broj_pojavljivanja = prebroji_znak(niz, trazeni_znak)
    print(f"Znak '{trazeni_znak}' se pojavljuje {broj_pojavljivanja} puta u nizu.")
else:
    print("Unesite samo jedan znak za pretragu.")