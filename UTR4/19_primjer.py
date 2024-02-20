# Napišite program koji će unositi niz rezultata jednog košarkaškog tima
# te ispisuje najduži niz pobjeda (W - Win) ili poraza (L – Lose)
# te ispisuje ukupan omjer pobjeda i poraza. 

unos_niza = input("Molim vas da unesete niz rezultata zadnjih 10 utakmica(W-L): ")

broj_pobjeda = unos_niza.count('W')
broj_poraza = unos_niza.count('L')


