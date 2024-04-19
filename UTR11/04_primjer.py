# Napišite program koji će učitavati ime planine i visinu iskazanu u metrima (ime i visina su
# odvojeni zarezom) i te podatke sortirati od najveće planine prema najmanjoj i upisati sortirane
# podatke u datoteku planina tako da treba pretvoriti u kilometre. Za konačni ispis potrebno je
# sortirati. Kada korisnik unese riječ „gotovo“ prekida se unos podataka.izlaz.txt.

podaci = []
sortirani_podatci = []

while True:
    unos = input("Unesite ime planine i visinu odvojene zarezom ('gotovo' za kraj): ")
    if unos.lower() == 'gotovo':
        break
    ime, visina = unos.split(',')
    visina_km = float(visina) / 1000  # Pretvaranje visine iz metara u kilometre
    podaci.append((ime.strip(), visina_km))
    sortirani_podatci = sorted(podaci, key=lambda x: x[1], reverse=True)
        
with open('izlaz.txt', 'w') as datoteka:
    for planina, visina in podaci:
        datoteka.write(f"{planina}, {visina:.2f} km\n")

print("Sortirane planine po visini: ")
for planina, visina in sortirani_podatci:
    print(f"{planina}: {visina:.2f} km")