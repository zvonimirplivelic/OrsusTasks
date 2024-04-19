# Napiši program koji će kreirati tekstualnu datoteku ulaz.txt te upisati brojeve u tu datoteku.
# Prekid unosa brojeva u ulaz2.txt napraviti tipkom ENTER. Zatim je potrebno kreirati izlaznu
# datoteku izlaz.txt u koju je potrebno upisati samo parne brojeve.

with open('ulaz.txt', 'w') as datoteka:
    print("Unesite brojeve. Pritisnite ENTER za završetak unosa.")
    while True:
        unos = input("Unesite broj: ")
        if unos == '':
            break
        datoteka.write(unos + '\n')
        
with open('ulaz.txt', 'r') as ulaz, open('izlaz.txt', 'w') as izlaz:
    for linija in ulaz:
        broj = int(linija.strip())
        if broj % 2 == 0:
            izlaz.write(str(broj) + '\n')