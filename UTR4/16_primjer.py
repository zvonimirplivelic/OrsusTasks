# Napišite program koji će unositi jedan znak i string te ispisivati sve stringove 
# koji se mogu dobiti postavljanjem unesenog znaka na svako mjesto u unesenom stringu.   

unos_stringa = str(input("Molim vas da unesete riječ: "))
unos_znaka = str(input("Molim vas da unesete znak: "))

for i in range((len(unos_stringa) + 1)):
    print(f"{unos_stringa[:i]}{unos_znaka}{unos_stringa[i:]}")