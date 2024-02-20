# Napišite program koji unosi listu brojeva i funkciju jedinstveni koja vraća novu listu s
# jedinstvenim elementima prve liste.

def jedinstveni(lista):
    jedinstvena_lista = list(set(lista))
    return jedinstvena_lista

lista_brojeva = []

while True:
    unos_broja = int(input("Unesite broj (0 za prekid): "))

    if(unos_broja == 0):
        break
    
    lista_brojeva.append(unos_broja)

print(f"Unijeli ste listu brojeva: {lista_brojeva}.\n Ovo su jedinstveni elementi te liste: {jedinstveni(lista_brojeva)}")