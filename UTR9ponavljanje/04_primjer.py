# Napisati program koji učitava granice dva zatvorena intervala [dg1, gg1] i [dg2, gg2] cijelih
# brojeva. Pretpostaviti da su granice ispravno unesene. Nakon toga učitavati cijele brojeve za koje
# je potrebno utvrditi nalaze li se u zadanim intervalima. Učitavanje brojeva prekida se nakon
# učitavanja nule. Program treba ispisati koliko učitanih brojeva (ne uključujući nulu) je bilo iz
# intervala [dg1, gg1], koliko iz intervala [dg2, gg2] i koliko je brojeva iz presjeka zadanih intervala,
# ako presjek zadanih intervala postoji.

unesi_interval = lambda: (int(input("Unesite donju granicu intervala: ")), int(input("Unesite gornju granicu intervala: ")))
provjeri_prisutnost_broja = lambda broj, interval: interval[0] <= broj <= interval[1]

dg1, gg1 = unesi_interval()
dg2, gg2 = unesi_interval()

brojevi_u_intervalu1 = 0
brojevi_u_intervalu2 = 0
presjek_brojeva = 0

brojevi_interval1 = []
brojevi_interval2 = []
presjek_intervala = []

while True:
    broj = int(input("Unesite cijeli broj (unesite 0 za izlaz): "))
    if broj == 0:
        break
    if provjeri_prisutnost_broja(broj, (dg1, gg1)):
        brojevi_u_intervalu1 += 1
        brojevi_interval1.append(broj)
    if provjeri_prisutnost_broja(broj, (dg2, gg2)):
        brojevi_u_intervalu2 += 1
        brojevi_interval2.append(broj)
    if (lambda x: provjeri_prisutnost_broja(x, (dg1, gg1)) and provjeri_prisutnost_broja(x, (dg2, gg2)))(broj):
        presjek_brojeva += 1
        presjek_intervala.append(broj)
print(f"Brojevi u intervalu [{dg1}, {gg1}]:\t {brojevi_u_intervalu1} - {brojevi_interval1}")
print(f"Brojevi u intervalu [{dg2}, {gg2}]:\t {brojevi_u_intervalu2} - {brojevi_interval2}")
print(f"Brojevi u presjeku intervala:\t {presjek_brojeva} - {presjek_intervala}")