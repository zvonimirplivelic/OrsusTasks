# Napišite program koji će unositi string i ispisuje 
# broj pojavljivanja samoglasnika i suglasnika

unos_stringa = str(input("Molim vas da unesete tekst: ")).lower()
samoglasnici = "aeiou"
br_samoglasnika = 0
br_suglasnika = 0

for slovo in unos_stringa:
    if slovo.isalpha():
        if slovo in samoglasnici:
            br_samoglasnika += 1
        else:
            br_suglasnika += 1

print(f"Broj samoglasnika: {br_samoglasnika}\n" +
      f"Broj suglasnika: {br_suglasnika}")