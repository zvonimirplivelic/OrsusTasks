# Napišite program koji će za definiranu listu lista= ["lav", "tigar", "tigar", "zebra", "lav", "lav"]
# prebrojati svaku vrstu životinje u listi. Potrebno je riješiti zadatak koristeći rječnik.

lista_zivotinja = ["lav", "tigar", "tigar", "zebra", "lav", "lav"]

brojac_zivotinja = {}

for zivotinja in lista_zivotinja:
    if zivotinja in brojac_zivotinja:
        brojac_zivotinja[zivotinja] += 1
    else:
        brojac_zivotinja[zivotinja] = 1

for zivotinja, broj in brojac_zivotinja.items():
    print(f"{zivotinja}: {broj}")