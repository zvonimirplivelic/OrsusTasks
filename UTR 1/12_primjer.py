# Napišite program koji učitava duljinu izraženu u km, zatim ispisuje duljinu iskazanu u cm

unosKilometara = int(input("Molim vas da unesete duljinu u kilometrima: "))

duljinaUCentimetrima = unosKilometara * 10000

print(f"{unosKilometara} kilometara je {duljinaUCentimetrima} centimetara")