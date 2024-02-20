# Napišite program koji prvo unosi donju granicu(dg) i gornju granicu(gg). Pretpostaviti da su
# granice ispravno unesene. Zatim u programu učitavajte brojeve sve dok ne unesete broj 0.
# Potrebno je prebrojati sve unesene brojeve koji su bili u intervalu [dg,gg] (granice su uključene).

donja_granica = int(input("Molim vas da unesete donju granicu: "))
gornja_granica = int(input("Molim vas da unesete gornju granicu: "))

brojevi_unutar_intervala = []

while True:
    unos_broja = int(input("Unesite željeni broj: "))

    if unos_broja == 0:
        break

    if unos_broja > donja_granica and unos_broja < gornja_granica:
        brojevi_unutar_intervala.append(unos_broja)

print(f"Brojevi unutar intervala su: {brojevi_unutar_intervala}")