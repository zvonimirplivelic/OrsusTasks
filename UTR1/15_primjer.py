# Napišite program koji pretvara sate u minute i sekunde

unosSati = int(input("Molim vas da unesete broj sati: "))

iznosMinuta = unosSati * 60
iznosSekundi = iznosMinuta * 60

print(f"{unosSati} sati je {iznosMinuta} minuta ili {iznosSekundi} sekundi")