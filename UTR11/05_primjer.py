# U prvom redu tekstualne datoteke ulaz.txt nalaze se dva cijela broja odvojena jednim razmakom.
# Napiši program koji će u prvi red izlazne datoteke izlaz.txt ispisati zbroj, u drugi razliku, u treći
# umnožak i u četvrti količnik unesenih brojeva

with open('ulaz.txt', 'r') as ulaz_datoteka:
    prvi_red = ulaz_datoteka.readline().strip()

brojevi = list(map(int, prvi_red.split()))

zbroj = brojevi[0] + brojevi[1]
razlika = brojevi[0] - brojevi[1]
umnozak = brojevi[0] * brojevi[1]
kolicnik = brojevi[0] / brojevi[1]

rezultati = [zbroj, razlika, umnozak, kolicnik]

with open('izlaz.txt', 'w') as datoteka:
    for rezultat in rezultati:
        datoteka.write(str(rezultat) + '\n')