# Napišite program koji učitava tri stranice trokuta i funkciju pravokutan koja vraća poruku da li su
# učitane stranice pravokutnog trokuta. Trokut je pravokutan kada vrijedi a 2 + b 2 = c 2 .

def provjera_pravokutnika(str_a, str_b, str_c):

    poruka = ""
    if(str_a ** 2 + str_b ** 2 == str_c **2):
        poruka = "je pravokutan"
    else:
        poruka = "nije pravokutan"
    return poruka


str_a = int(input("Molim vas da unesete prvu stranicu trokuta: "))
str_b = int(input("Molim vas da unesete drugu stranicu trokuta: "))
str_c = int(input("Molim vas da unesete treću stranicu trokuta: "))

print(f"Trokut sa pripadajućim stranicama {str_a}, {str_b} i {str_c} {provjera_pravokutnika(str_a, str_b, str_c)}")