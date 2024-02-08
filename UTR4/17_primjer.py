# Napišite program koji će unositi rečenicu i  ispisivati svaku riječ u novi 
# redak na način to tako da prvo slovo svake riječi pretvori u veliko.

unos_recenice = input("Molim vas da unesete rečenicu: ")

for rijec in unos_recenice.split():
    print(rijec.capitalize())