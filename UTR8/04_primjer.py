# Napišite program koji učitava stranice pravokutnika i funkciju opseg koja vraća opseg
# pravokutnika.

def opseg_pravokutnika(str_a, str_b):
    
    return 2 * (str_a + str_b)


str_a = int(input("Molim vas da unesete prvu stranicu pravokutnika: "))
str_b = int(input("Molim vas da unesete drugu stranicu pravokutnika: "))

print(f"Opseg pravoktutnika sa pripadajućim stranicama {str_a} i {str_b} iznosi: {opseg_pravokutnika(str_a, str_b)}")