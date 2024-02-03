# Unesite katete pravokutnog trokuta, zatim ispišite hipotenuzu, opseg i površinu opisane kružnice

import math


prvaKateta = float(input("Molim vas da unesete prvu katetu trokuta: "))
drugaKateta = float(input("Molim vas da unesete drugu katetu trokuta: "))

hipotenuzaTrokuta = math.sqrt((prvaKateta**2) + (drugaKateta**2))
opsegKružnice = 2 * (hipotenuzaTrokuta / 2) * math.pi
povrsinaKruga = (hipotenuzaTrokuta/2)**2 * math.pi

print(f"Prva kateta iznosi {prvaKateta}. Druga kateta iznosi {drugaKateta}. Hipotenuza je {hipotenuzaTrokuta}. Opseg kružnice je {opsegKružnice}. Površina kruga je {povrsinaKruga}")