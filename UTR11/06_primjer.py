# Napiši program koji će iz tekstualnu datoteku ulaz.txt. Potrebno je kreirati izlaz1.txt i upisati samo
# neparne cijele brojeve u izlaznu datoteku izlaz.txt.

with open('ulaz.txt', 'r') as ulaz_datoteka:
    brojevi = ulaz_datoteka.readline().strip()

brojevi = list(map(int, brojevi.split()))
print(brojevi)

with open('izlaz.txt', 'w') as datoteka:
    for broj in brojevi:
        if broj % 2 == 1:
            datoteka.write(str(broj) + " ")