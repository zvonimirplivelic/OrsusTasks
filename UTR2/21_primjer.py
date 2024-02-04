# Napišite program koji učitava četveroznamenkasti broj, zatim ispisuje poruku
# je li unesen broj magičan. Broj je magičan ako mu je zbroj prve i zadnje znamenke
# jednak umnošku druge i treće znamenke. 
# Npr. 1235 - magičan zato što je 1 + 5 i 2 * 3 = 6
# UPUTA: Isključivo riješiti na temelju aritmetičkih operacija

unos_broja = int(input("Molim vas da unesete četveroznamenkasti broj: "))

prva_znamenka = unos_broja // 1000
druga_znamenka = unos_broja // 100 % 10
treća_znamenka = unos_broja // 10 % 10
četvrta_znamenka = unos_broja % 10

print(f"\nUnijeli ste broj: {unos_broja}" +
      f"\nPrva znamenka je: {prva_znamenka}" + 
      f"\nDruga znamenka je: {druga_znamenka}" +
      f"\nTreća znamenka je: {treća_znamenka}" +
      f"\nČetvrta znamenka je: {četvrta_znamenka}")

if(prva_znamenka + četvrta_znamenka) and (druga_znamenka * treća_znamenka):
    print("Broj je magičan")
