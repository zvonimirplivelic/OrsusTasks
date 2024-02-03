# Napišite program koji učitava pet brojeva, zatim ispisuje prosjek

prviBroj = int(input("Molim vas da unesete prvi broj: "))
drugiBroj = int(input("Molim vas da unesete drugi broj: "))
treciBroj = int(input("Molim vas da unesete treći broj: "))
cetvrtiBroj = int(input("Molim vas da unesete četvrti broj: "))
petiBroj = int(input("Molim vas da unesete peti broj: "))

prosjekBrojeva = (prviBroj + drugiBroj + treciBroj + cetvrtiBroj + petiBroj) / 5

print(f"Prosjek pet brojeva je: {prosjekBrojeva}")