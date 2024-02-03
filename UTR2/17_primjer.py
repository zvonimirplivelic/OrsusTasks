# Napišite program koji učitava broj, zatim ispisuje poruku 
# je li uneseni broj unutar intervala od 1 do 10 ili od 20 do 30.
# Npr. broj 27 je unutar zadanog intervala, isto kao i broj 5, ali
# broj 17 nije unutar zadanog intervala

unos_broja = int(input("Unesite broj: "))

if unos_broja >= 1 and unos_broja <=10:
    print("Broj je unutar intervala")
elif unos_broja >= 20 and unos_broja <= 30:
    print("Broj je unutar intervala")
else:
    print("Broj nije unutar intervala")