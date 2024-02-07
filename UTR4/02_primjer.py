# Napišite program koji će unositi dva stringa 
# i ispisuje poruku koji string je kraći.

prvi_string = input("Molim vas da unesete prvi string: ")
drugi_string = input("Molim vas da unesete drugi string: ")


if len(prvi_string) < len(drugi_string):
    print("Prvi string je kraći")
else:
    print("Drugi string je kraći")
