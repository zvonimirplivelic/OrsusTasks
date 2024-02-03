# Napišite program koji učitava broj te 
# zatim ispisuje poruku da li je broj pozitivan, negativan ili jednak 0

unos_broja = int(input("Unesite broj: "))


if(unos_broja > 0):
    print("Broj je pozitivan")
elif(unos_broja < 0):
    print("Broj je negativan")
else:
    print("Broj je jednak nuli")
