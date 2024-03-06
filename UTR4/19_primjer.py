# Napišite program koji će unositi niz rezultata jednog košarkaškog tima
# te ispisuje najduži niz pobjeda (W - Win) ili poraza (L – Lose)
# te ispisuje ukupan omjer pobjeda i poraza. 

# Unos niza rezultata
unos_rezultata = input("Unesite niz rezultata (npr. WWLLLWWL): ").upper()

trenutni_niz = 1
najduzi_niz = 1
znak_najduzeg_niza = ""

for i in range(1, len(unos_rezultata)):
    if unos_rezultata[i] == unos_rezultata[i - 1]:
        znak_najduzeg_niza = unos_rezultata[i - 1]
        print(f"{i}, {znak_najduzeg_niza}")
        trenutni_niz += 1
    else:
        trenutni_niz = 1

    if trenutni_niz > najduzi_niz:
        najduzi_niz = trenutni_niz


print(f"Najduži niz pobjeda ili poraza: {najduzi_niz}{znak_najduzeg_niza}", )

broj_pobjeda = unos_rezultata.count('W')
broj_poraza = unos_rezultata.count('L')

print(f"Omjer pobjeda i poraza: {broj_pobjeda}W - {broj_poraza}L")
