# Napišite program koji učitava stranicu pravokutnika, zatim ispisuje opseg i površinu pravokutnika

prvaStranicaPravokutnika = int(input("Molim vas da unesete prvu stranicu pravokutnika: "))
drugaStranicaPravokutnika = int(input("Molim vas da unesete drugu stranicu pravokutnika: "))

opsegPravokutnika = 2 * (prvaStranicaPravokutnika + drugaStranicaPravokutnika)
povrsinaPravokutnika = prvaStranicaPravokutnika * drugaStranicaPravokutnika

print(f"Duljine stranica pravokutnika su: {prvaStranicaPravokutnika} i {drugaStranicaPravokutnika}. Opseg kvadrata je {opsegPravokutnika}. Površina kvadrata je {povrsinaPravokutnika}")