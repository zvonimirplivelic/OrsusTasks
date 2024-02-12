# Napišite program koji će unositi prirodan broj n, te brojeve a i b, a zatim n prirodnih brojeva većih
# od 1. Program treba ispisati one od unesenih brojeva koji su iz intervala [a,b] te broj brojeva u
# intervalu i sumu brojeva intervala. Granice su uključene

broj_n = int(input("Unesite prirodan broj n: "))
broj_a = int(input("Unesite donju granicu: "))
broj_b = int(input("Unesite gornju granicu: "))

lista_odabranih_brojeva = [0] * broj_n

brojac = 0
suma = 0

for i in range(broj_n):
    lista_odabranih_brojeva[i] = int(input("Unesite broj: "))

for i in lista_odabranih_brojeva:
    if i >= broj_a and i <= broj_b:
        print(f"Broj u intervalu: {i}")
        brojac += 1
        suma += i
    
print(f"U intervalu od {broj_a} do {broj_b} se nalazi {brojac} brojeva.")
print(f"Suma brojeva u intervalu je: {suma}")