# Napišite program koji će unositi string i ispisivati samo 
# VELIKA slova iz unesenog stringa.

unos_stringa = input("Molim vas da unesete tekst: ")
velika_slova = ""

for slovo in unos_stringa:
    if slovo.isupper():
        velika_slova += slovo

print(velika_slova)