# Napišite program koji će učitati dva broja, X i Y, 
# te ispisati sve brojeve u intervalu od X do Y

prvi_broj = int(input("Unesite prvi broj: "))
drugi_broj = int(input("Unesite drugi broj: "))

for i in range(prvi_broj, drugi_broj + 1):
    print(f"{i}", end = " ")