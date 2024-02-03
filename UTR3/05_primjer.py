# Napišite program koji će ispisati u jednom redu sve parne brojeve u intervalu od 1 do 19 odvojene zarezom

for i in range(1, 19):
    if (i % 2 == 0):
        print(f"{i}", end = ", ")