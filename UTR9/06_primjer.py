# Napišite glavni program i lambda izraz oduzmi koji oduzima dva broja.

oduzmi = lambda x, y: x - y

broj1 = int(input("Unesite prvi broj: "))
broj2 = int(input("Unesite drugi broj: "))

rezultat = oduzmi(broj1, broj2)

print(f"Rezultat oduzimanja --> {broj1} - {broj2} = {rezultat}")