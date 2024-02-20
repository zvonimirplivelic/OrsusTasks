# Napišite program koji će unositi tri broja i funkciju max_broj za pronalaženje najvećeg broja i
# ispisuje najveći broj

def max_broj(a, b, c):
    return max(a, b, c)

unos_broja1 = int(input("Unesite prvi broj: "))
unos_broja2 = int(input("Unesite drugi broj: "))
unos_broja3 = int(input("Unesite treći broj: "))

print(f"Najveci broj je: {max_broj(unos_broja1, unos_broja2, unos_broja3)}")