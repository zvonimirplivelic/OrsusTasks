# Napišite program koji učitava visinu i težinu, a zatim ispisuje BMI indeks po formuli: BMI = (masa / visina*visina)

visina = float(input("Molim vas da unesete vašu visinu(u metrima): "))
tezina = int(input("Molim vas da unesete vašu tezinu(u kilogramima): "))

bodyMassIndex = tezina / visina**2

print(f"Vaš BMI je: {bodyMassIndex}")