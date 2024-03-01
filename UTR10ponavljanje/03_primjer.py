# Napišite program koji će učitati N, gdje je N broj učenika. Nakon
# toga potrebno je učitati N imena. Program treba ispisati ime i
# broj učenika koji se isto zovu u formatu „ime se x puta ponavlja“.

def broj_ponavljanja_imena(ucenici):
    ponavljanja = {}
    for ime in ucenici:
        ponavljanja[ime] = ponavljanja.get(ime, 0) + 1
    return ponavljanja

n = int(input("Unesite broj učenika: \n"))

imena_ucenika = []

for i in range(n):
    ime = input(f"Unesite ime {i+1}. učenika: \n")
    imena_ucenika.append(ime)

ponavljanja = broj_ponavljanja_imena(imena_ucenika)

for ime, broj_ponavljanja in ponavljanja.items():
    print(f"{ime} se pojavljuje {broj_ponavljanja} puta. \n")
