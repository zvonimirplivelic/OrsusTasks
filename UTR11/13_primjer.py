# Napiši program koji će kreirati tekstualne datoteke ulaz.txt potrebno je u prvi redak upisati cijeli
# broj N (poruka N = ) i zatim će upisivati N imena svako u novi redak. Nakon toga potrebno je
# kreirati izlaznu datoteku izlaz.txt u koju je potrebno ispisati u prvi redak „Ime - Broj slova“ te u
# svaki redak ime te pored imena broj slova.

def zapis_u_datoteku(ime_datoteke, sadrzaj):
    with open(ime_datoteke, 'w') as datoteka:
        datoteka.write(sadrzaj)

def obradi_datoteku_ulaz(ulazna_datoteka):
    with open(ulazna_datoteka, 'r') as ulaz:
        broj_n = ulaz.readline().strip()
        _, n = broj_n.split('=')
        n = int(n.strip())

        imena = [ulaz.readline().strip() for _ in range(n)]

    return imena

def izracunaj_broj_slova(imena):
    rezultat = "Ime - Broj slova\n"
    for ime in imena:
        broj_slova = len(ime)
        rezultat += f"{ime} - {broj_slova}\n"
    return rezultat

imena = obradi_datoteku_ulaz('ulaz.txt')

rezultat = izracunaj_broj_slova(imena)
zapis_u_datoteku('izlaz.txt', rezultat)