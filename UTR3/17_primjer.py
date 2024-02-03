# Napišite program koji će ispisati tablicu množenja od 1 do 10.
# Potrebno je pripaziti na format ispisa

for faktor1 in range (1, 11):
    print("\n")
    for faktor2 in range (1, 11):
        print(f"{faktor1} * {faktor2} = {faktor1 * faktor2}", end = "\t")