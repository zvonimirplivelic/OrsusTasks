# Napišite program koji učitava stranicu kocke, zatim ispisuje volumen i oplošje kocke

stranicaKocke = int(input("Molim vas da unesete duljinu stranice kocke: "))

volumenKocke = stranicaKocke ** 3
oplošjeKocke = 6 * (stranicaKocke ** 2)

print(f"Duljina stranice kocke je {stranicaKocke}. Oplošje kocke je {oplošjeKocke}. Volumen kocke je {volumenKocke} ")