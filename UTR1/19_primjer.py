# Unesite katete pravokutnog trokuta, zatim ispišite hipotenuzu i površinu

import math

prvaKateta = float(input("Molim vas da unesete prvu katetu trokuta: "))
drugaKateta = float(input("Molim vas da unesete drugu katetu trokuta: "))

hipotenuzaTrokuta = math.sqrt((prvaKateta**2) + (drugaKateta**2))

povrsinaTrokuta = prvaKateta * drugaKateta / 2

print(f"Prva kateta iznosi {prvaKateta}. Druga kateta iznosi {drugaKateta}. Hipotenuza je {hipotenuzaTrokuta}. Površina trokuta je {povrsinaTrokuta}")
