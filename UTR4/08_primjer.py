# Napišite program koji će unositi string i ispisivati koliko je znamenaka tom stringu

unos_stringa = input("Molim vas da unesete tekst: ")

brojac = 0

for slovo in unos_stringa:
    if slovo.isdigit():
        brojac += 1

print(f"Broj znamenaka: {brojac}")