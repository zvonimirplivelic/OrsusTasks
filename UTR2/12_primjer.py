# Napišite program koji učitava dva broja, 
# zatim ispisuje poruku da li je umnožak ta dva broja 
# paran ili neparan broj

prvi_broj = int(input("Unesite prvi broj: "))
drugi_broj = int(input("Unesite drugi broj: "))

umnožak_brojeva = prvi_broj * drugi_broj

if(umnožak_brojeva % 2 == 0):
    print("Broj je paran")
else:
    print("Broj je neparan")
