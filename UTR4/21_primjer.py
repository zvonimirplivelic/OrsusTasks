# Napišite program koji će unositi broj N, a zatim N riječi. Potrebno je zatim 
# nakon svake unese riječi ispisati samo one riječi 
# koja ima točno 2 samoglasnika te zbroj velikih i malih slova.

unos_broja_n = int(input("Unos broja riječi: "))
broj_slova = 0

for riječ in range(unos_broja_n):
    riječ = input("Molim vas da unesete riječ: ")

    check = riječ.upper()
    broj_samoglasnika = check.count("A") + check.count("E") + check.count("I") + check.count("O") + check.count("U")

    if(broj_samoglasnika == 2):
        for slovo in riječ:
            if slovo.isalpha():
                broj_slova += 1

        print(f"Riječ je: {riječ}\nZbroj velikih i malih slova: {broj_slova}")