# Napišite program koji će unositi N, a zatim N brojeva u listu. Zatim je potrebno napisati lambda
# izraz sortiraj koji će sortirati listu od najvećeg prema najmanjem broju.

n = int(input("Unesite broj N: "))

brojevi = [int(input(f"Unesite {i + 1}. broj: ")) for i in range(n)]

sortiraj = lambda lista: sorted(lista, reverse=True)

sortirana_lista = sortiraj(brojevi)

print("Sortirana lista od najvećeg prema najmanjem broju:", sortirana_lista)