# Napišite program koji će unositi string i ispisuje 
# broj pojavljivanja mali i velikih slova

unos_stringa = input("Molim vas da unesete tekst: ")

mala_slova = 0
velika_slova = 0

for slovo in unos_stringa:
    if slovo.isupper():
        velika_slova += 1
    elif slovo.islower():
        mala_slova += 1

print(f"Broj velikih slova u tekstu je: {velika_slova}")
print(f"Broj malih slova u tekstu je: {mala_slova}")