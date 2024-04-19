# Napiši program koji će iz tekstualne datoteke ulaz.txt čitati riječi u svakom retku. U ulaznoj
# datoteci se nalaze jedna ili više riječi međusobno odvojenih jednim ili više razmakom. Potrebno je
# kreirati izlaz.txt i upisati samo jedan broj u izlaznu datoteku, a to je broj riječi iz ulazne datoteke.

with open('ulaz.txt', 'r') as ulaz_datoteka:
    broj_rijeci = 0
    for linija in ulaz_datoteka:
        rijeci_u_liniji = linija.split()
        broj_rijeci += len(rijeci_u_liniji)

broj_rijeci_ukupno = broj_rijeci

with open('izlaz.txt', 'w') as izlaz_datoteka:
    izlaz_datoteka.write(str(broj_rijeci_ukupno))