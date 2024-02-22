# Napišite program koji će unositi string te ispisati frekvenciju pojavljivanja svakog slova. Potrebno
# je riješiti zadatak koristeći rječnik

frekvencija = {}

unos_stringa= input("Unesite string: ")

for slovo in unos_stringa:
    if slovo.isspace():
        continue

    frekvencija[slovo] = frekvencija.get(slovo, 0) + 1



for slovo, brojac in frekvencija.items():
    print(f"Slovo '{slovo}' se pojavljuje {round((float(brojac / len(unos_stringa)) * 100), 2)} posto u unešenom stringu: {unos_stringa}.")