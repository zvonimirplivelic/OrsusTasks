# Napišite program koji će unutar liste ocjene=[1,2,30,40,5] napraviti zamjenu 3. i 4. elementa i
# nakon toga ispisati svaki drugi element.

ocjene=[1,2,30,40,5]
ocjene[2:4] = [3, 4]
print(ocjene)
print(ocjene[::2])

