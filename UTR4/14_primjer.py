# Napišite program koji će unositi string i ispisivati koliko iznosi ASCII masa riječi.

unos_stringa = input("Molim vas da unesete tekst: ")
suma_znakova = 0

for znak in unos_stringa:
    suma_znakova += ord(znak)

print(f"ASCII suma znakova za tekst {unos_stringa} iznosi: {suma_znakova}")