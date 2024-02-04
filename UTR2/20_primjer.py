# Napišite program koji učitava tri stranice te provjerava postoji li takav trokut.
# Ako trokut postoji tada ispisuje poruku kakav je trokut: jednakokračan, 
# jednakostraničan ili raznostraničan

stranica_a = float(input("Molimo vas da unesete dužinu stranice a: "))
stranica_b = float(input("Molimo vas da unesete dužinu stranice b: "))
stranica_c = float(input("Molimo vas da unesete dužinu stranice c: "))

if (stranica_a + stranica_b > stranica_c and 
    stranica_b + stranica_c > stranica_a and 
    stranica_a + stranica_c > stranica_b):
    print("\nStranice ovih dimenzija mogu činiti trokut.")
    if (stranica_a == stranica_b == stranica_c):
        print("\nTrokut je jednakostraničan.")
    elif(stranica_a == stranica_b or stranica_b == stranica_c or stranica_c == stranica_a):
        print("Trokut je jednakokračan.")
    else:
        print("Trokut je raznostraničan.")
else:
    print("\nStranice ovih dimenzija ne mogu činiti trokut.")