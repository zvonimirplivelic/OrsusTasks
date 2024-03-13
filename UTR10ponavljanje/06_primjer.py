# Napisati funkciju zrcali koja zadani znakovni niz zrcali s obzirom na njegovu sredinu (prvi element dolazi na posljednju poziciju, a
# posljednji na prvu, drugi element na pretposljednju, pretposljednji na drugu itd.) Napisati glavni program u kojem će se s tipkovnice 
# učitati niz znakova (može se pretpostaviti da korisnik sigurno neće zadati niz dulji od 50 znakova). Na zaslon ispisati niz koji treba 
# izmijeniti na način da se nad njime pozove funkcija zrcali. Na kraju, nakon što je niz izmijenjen, na zaslon ispisati izmijenjeni niz.

def zrcali(niz):
    duljina = len(niz)
    zrcaljen_niz = []
    for i in range(duljina - 1, -1, -1):
        zrcaljen_niz.append(niz[i])
    return ''.join(zrcaljen_niz)

unons_niza_znakova = input("Unesite niz znakova: ")

if len(unons_niza_znakova) > 50:
    print("Niz ne smije biti dulji od 50 znakova.")

zrcaljeni_niz = zrcali(unons_niza_znakova)
print(f"Unešeni niz znakova je: {unons_niza_znakova}\nIzmijenjeni niz: {zrcaljeni_niz}")
