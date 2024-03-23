# Napišite program koji učitava brzinu u km/h, zatim ispisuje brzinu u m/s

brzinaKMH = float(input("Molim vas da unesete brzinu u kilometrima na sat: "))

brzinaMS = brzinaKMH * 1000 / 3600

print(f"{brzinaKMH} kilometara na sat je {brzinaMS} metara po sekundi")