# Napišite program koji učitava promjer kugle, 
# zatim ispisuje polumjer, volumen i oplošje kugle
import math

promjer_kugle = float(input("Molim vas da unesete promjer kugle: "))

polumjer_kugle = promjer_kugle / 2
volumen_kugle = (4 / 3) * (polumjer_kugle ** 3) * math.pi
oplošje_kugle = 4 * (polumjer_kugle ** 2) * math.pi

print(f"\nUnijeli ste promjer kugle od {promjer_kugle}\n" +
        f"Polumjer kugle je: {polumjer_kugle}\n" +
        f"Volumen kugle je: {volumen_kugle}\n" + 
        f"Oplošje kugle je: {oplošje_kugle}")