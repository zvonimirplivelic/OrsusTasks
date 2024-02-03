# Napišite program koji učitava tri koeficijenta kvadratne jednadžbe a, b, c te
#izračunava diskriminantu kvadratne jednadžbe po formuli D = (b*b) - 4ac

a = float(input("Unesite prvi koeficijent kvadratne jednadžbe: "))
b = float(input("Unesite drugi koeficijent kvadratne jednadžbe: "))
c = float(input("Unesite treći koeficijent kvadratne jednadžbe: "))

formula_jednadžbe = float((b**2) - (4* a * c))

print(f"D =  b*b - (4ac) za koordinate a = {a}, b = {b}, c = {c} je: {formula_jednadžbe}")