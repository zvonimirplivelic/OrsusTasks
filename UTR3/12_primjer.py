# Napišite program koji će učitati broj X te prebrojati koliko u 
# intervalu od 1 do 100 ima brojeva djeljivih sa X

broj_x = int(input("Unesite željeni broj: "))
counter = 0

for i in range (1, 101):
    if(i % broj_x == 0):
        counter += 1
        print(i)

print(f"Između 1 i 100 ima {counter} brojeva djeljivih sa {broj_x}")
