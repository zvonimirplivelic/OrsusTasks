# Napišite program koji učitava predefiniranu listu tri ntorki. Ispišite ime najstarije osobe, a u novi
# red godine najmlađe osobe.

o1 = ("Marko", 1988)
o2 = ("Marija", 1991)
o3 = ("Ivan", 1986)
ljudi = [o1, o2, o3]

print("Orginal: ",ljudi)

# Sort list of tuples by descending
ljudi.sort(key=lambda x: x[1], reverse=True)
print("Sorted: ",ljudi)

print(f"Najstarija osoba je: {o1[0]}\n" +
      f"Najmlađa osoba ima {2024 - o2[1]} godine")