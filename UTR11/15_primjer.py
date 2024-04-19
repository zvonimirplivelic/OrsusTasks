# Napišite program koji će u datoteku izlaz.txt ispisivati frekvenciju pojavljivanja slova u datoteci. U
# prvih nekoliko redaka tekstualne datoteke ulaz.txt nalaze se riječi odvojene razmacima. Tekst u
# datoteci će se sastojati samo od velikih slova engleske abecede.

def zapis_u_datoteku(ime_datoteke, rezultati):
    with open(ime_datoteke, 'w') as datoteka:
        for slovo, postotak in rezultati.items():
            datoteka.write(f"{slovo}: {postotak:.2f}\n")

def izracunaj_frekvenciju_slova(ulazna_datoteka):
    frekvencija = {}
    ukupno_slova = 0
    with open(ulazna_datoteka, 'r') as ulaz:
        for linija in ulaz:
            for slovo in linija.strip().replace(' ', ''):
                frekvencija[slovo] = frekvencija.get(slovo, 0) + 1
                ukupno_slova += 1
    
    for slovo, broj_pojavljivanja in frekvencija.items():
        frekvencija[slovo] = (broj_pojavljivanja / ukupno_slova)
    
    return frekvencija

rezultati = izracunaj_frekvenciju_slova('ulaz.txt')

zapis_u_datoteku('izlaz.txt', rezultati)