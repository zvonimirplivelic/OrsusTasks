# Napišite program koji će unositi broj N, a zatim N imena. Program treba ispisati koliko je uneseno muških, 
# a koliko ženskih imena. Pretpostavka je da sva ženska imena završavaju slovom a, 
# tada niti jedno muško ime ne završava tim slovom. 

unos_broja_imena = int(input("Molim vas da unesete broj imena koja će te unijeti: "))

brojač_muških = 0
brojač_ženskih = 0

for unos_imena in range(unos_broja_imena):
    unos_imena = str(input("Molim vas da unesete ime: ")).lower()
    if unos_imena.endswith('a'):
        brojač_ženskih += 1
    else:
        brojač_muških += 1

print(f"Uneseno je {brojač_muških} muških i {brojač_ženskih} ženskih imena.")