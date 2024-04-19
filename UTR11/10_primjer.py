# Napišite program koji će u izlaznu datoteku izlaz.txt prepisati sve riječi uzlazno sortirane po masi.
# Masu znaka definiramo kao odgovarajući ASCII kod koji je pridružen tom znaku, a masu riječi
# definirat ćemo kao zbroj masa svih slova u toj riječi. U nekoliko prvih redaka datoteke ulaz.txt
# nalazi se po jedna riječ u svakom retku.

with open('ulaz.txt', 'r') as ulaz:
    rijeci = [rijec.strip() for rijec in ulaz.readlines()]

rijeci.sort(key=lambda rijec: sum(ord(slovo) for slovo in rijec))

with open('izlaz.txt', 'w') as izlaz:
    for rijec in rijeci:
        izlaz.write(rijec + '\n')