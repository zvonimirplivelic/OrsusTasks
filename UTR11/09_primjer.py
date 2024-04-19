# Napiši program koji će iz tekstualne datoteke ulaz.txt čitati riječi u svakom retku. U ulaznoj
# datoteci se nalaze jedna ili više riječi međusobno odvojenih jednim ili više razmakom. Potrebno je
# kreirati izlaz.txt i upisati samo one riječi koje imaju manje od 5 slova.

with open('ulaz.txt', 'r') as ulaz, open('izlaz.txt', 'w') as izlaz:
    for linija in ulaz:
        rijeci = linija.split()
        for rijec in rijeci:
            if len(rijec) < 5:
                izlaz.write(rijec + ' ')