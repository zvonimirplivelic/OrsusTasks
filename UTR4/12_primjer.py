# Napišite program koji će unositi ime i prezime kao jedan string 
# (ne odvojeno) i ispisivati inicijale odvojene jednim razmakom.

unos_imena_i_prezimena = input("Molim vas da unesete ime i prezime: ")

print(f"{unos_imena_i_prezimena.split()[0][0]}. {unos_imena_i_prezimena.split()[1][0]}.")
