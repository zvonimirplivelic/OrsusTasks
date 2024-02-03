# Napišite program koji učitava broj te 
# zatim ispisuje poruku da li je broj paran ili neparan

unos_broja = int(input("Unesite broj za provjeru: "))

if(unos_broja % 2 == 0):
    print("Broj je paran")
else:
    print("Broj je neparan")