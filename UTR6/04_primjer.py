# Napišite program koji učitava imena životinja u ZOO-u, sva imena su napisana u jednom redu i
# odvojena zarezom. Stigla je oluja te je oštećeni dio ZOO-a. Od korisnika se očekuje da u novi red
# napiše imena životinja koja nisu pobjegla u ZOO-u poredana po abecedi ili poruku "Sve životinje
# su u ZOO-u". Potrebno je riješiti zadatak koristeći skupove.

zivotinje_u_zoo = set(input("Unesi životinju:").split(","))

print("     ###############\n#####     OLUJA     #####\n     ###############")
zivotinje_ostale = set(input("Unesi životinju koja je ostala:").split(","))


if(zivotinje_ostale == zivotinje_u_zoo):
    print("Sve su životinje u ZOO")
else:
    pobjegle_zivotinje = zivotinje_u_zoo ^ zivotinje_ostale
    print(f"Pobjegle životinje su: {pobjegle_zivotinje}")
