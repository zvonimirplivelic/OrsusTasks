# Napišite program koji učitava duljinu i širinu,
# zatim ispisuje poruku da li je unesen četverokut kvadrat ili pravokutnik

duljina = int(input("Unesite duljinu četverokuta: "))
širina = int(input("Unesite širinu četverokuta: "))

if(duljina == širina):
    print("Geometrijski lik je Kvadrat")
else:
    print("Geometrijski lik je Pravokutnik")
