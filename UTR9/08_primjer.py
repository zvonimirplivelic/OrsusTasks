# Napišite program koji će unositi N, a zatim N riječi u listu. Zatim je potrebno napisati lambda izraz
# sortiraj koji će sortirati listu od riječi koja ima najmanje slova do riječi koja ima najviše slova.

broj_n = int(input("Unesite broj N: "))

rijeci = [input(f"Unesite {i + 1}. riječ: ") for i in range(broj_n)]

sortiraj = lambda lista: sorted(lista, key= lambda slova: len(slova))

sortirana_lista = sortiraj(rijeci)

print("Sortirana lista od najmanje do najveće riječi prema broju slova:", sortirana_lista)