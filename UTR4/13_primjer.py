# Napišite program koji ispisuje svaku ASCII vrijednost 
# od znamenaka: 0, 1, 2, 3, 4, 5, 6 , 7, 8, 9.

for i in range(0, 10):
    print(f"ASCII vrijednost broja {i} iznosi {ord(str(i))}")