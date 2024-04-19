# Napiši program koji će kreirati tekstualnu datoteku ulaz.txt potrebno je u prvi redak upisati cijeli
# broj N ( u obliku „N = “) i u drugi redak upisati N brojeva u tu datoteku. Nakon toga potrebno je
# kreirati izlaznu datoteku izlaz.txt u koju je potrebno u prvi redak upisati sumu neparnih brojeva, a
# u drugi redak umnožak parnih brojeva.

with open('ulaz.txt', 'r') as ulaz:
    broj_n = ulaz.readline().strip()
    _, n = broj_n.split('=')
    n = int(n.strip())

    red_brojeva = ulaz.readline().strip()
    brojevi = list(map(int, red_brojeva.split()))

suma_neparnih = sum(broj for broj in brojevi if broj % 2 != 0)
umnozak_parnih = 1
for broj in brojevi:
    if broj % 2 == 0:
        umnozak_parnih *= broj

with open('izlaz.txt', 'w') as datoteka:
    datoteka.write(str(f"Suma neparnih brojeva: {suma_neparnih}\n"))
    datoteka.write(str(f"Umnožak parnih brojeva: {umnozak_parnih}\n"))