# Napišite program koji će unositi string i ispisuje sljedeće poruke: 
# duljinu stringa, prvi znak u stringu, posljednji znak u stringu, 
# prva 3 znaka u stringu, posljednja 3 znaka u stringu,  
# peti znak u stringu, obrnuti string. 

unos_stringa = str(input("Molimo vas da unesete tekst: "))

duljina_stringa = len(unos_stringa)
prvi_znak_stringa = unos_stringa[0]
posljednji_znak_stringa = unos_stringa[len(unos_stringa) - 1]
prva_tri_znaka_stringa = unos_stringa[:3]
posljednja_tri_znaka_stringa = unos_stringa[-3:]
peti_znak_stringa = unos_stringa[4]
obrnuti_string = unos_stringa[::-1]

print(f"Duljina stringa: {duljina_stringa}\n" +
      f"Prvi znak: {prvi_znak_stringa}\n" +
      f"Posljednji znak: {posljednji_znak_stringa}\n" +
      f"Prva tri znaka: {prva_tri_znaka_stringa}\n" +
      f"Posljednja tri znaka: {posljednja_tri_znaka_stringa}\n" +
      f"Peti znak: {peti_znak_stringa}\n" +
      f"Obrnuti string: {obrnuti_string}\n")