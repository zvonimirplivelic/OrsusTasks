# Putnik može kupiti kartu s popustom koji ovisi o njegovim godinama. Potrebno je napisati samo
# glavni program koji će za unese godine putnika napisati u koji postotni postotak spada.
# Pravo na popust određuje se:
# Godina Opis
# 0, 5 besplatna karta
# 5, 10 50% popusta
# 10, 18 25% popusta
# 18, 65 bez popusta
# 65< 75% popusta

unos_godina = int(input("Molim vas da unesete broj godina: "))

if unos_godina > 0 and unos_godina < 5:
    print(f"Imate {unos_godina}. Imate pravo na besplatnu kartu")
elif unos_godina > 5 and unos_godina < 10:
    print(f"Imate {unos_godina}. Imate pravo na 50% popusta")
elif unos_godina > 10 and unos_godina < 18:
    print(f"Imate {unos_godina}. Imate pravo na 25% popusta")
elif unos_godina > 18 and unos_godina < 65:
    print(f"Imate {unos_godina}. Nemate pravo na popust")
else:
    print(f"Imate {unos_godina} godina. Imate pravo na 75% popusta")
    