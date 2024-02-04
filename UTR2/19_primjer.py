# Napišite program koji učitava dva broja i operator (+, -, * ili /)
# te zatim ispisuje odgovarajući rezultat s obzirom na odabrani operator

prvi_broj = int(input("Unesite prvi broj: "))
drugi_broj = int(input("Unesite drugi broj: "))
operator = input("Unesite operator(+, -, *, /, %): ")

if operator == "+": rezultat = prvi_broj + drugi_broj
elif operator == "-": rezultat = prvi_broj - drugi_broj
elif operator == "*": rezultat = prvi_broj * drugi_broj
elif operator == "/": rezultat = prvi_broj / drugi_broj
elif operator == "%": rezultat = prvi_broj % drugi_broj
else: print("Unesite ispravan operator!!!")

print (f"\n{prvi_broj} {operator} {drugi_broj} = {rezultat}")