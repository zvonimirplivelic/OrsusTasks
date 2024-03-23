# Napišite program koji učitava temperaturu u Celzijus stupnjevima 
# i pretvara ju u Kelvine. Prema definiciji na Celzijevoj ljesvici 0°C jednako je 273,15K

unosTemperatureUCelzijevimStupnjevima = input("Molim vas da unesete temperaturu u Celzijevim stupnjevima: ")
temperaturaUKelvinima = float(unosTemperatureUCelzijevimStupnjevima) + 273.15

print(f"Temperatura {unosTemperatureUCelzijevimStupnjevima}°C iznosi {temperaturaUKelvinima}K")