# Program za ispis božićnog drvca

print("=== BOŽIĆNO DRVCE ===")

# Unos od korisnika
visina = int(input("Unesite visinu drvca: "))
znak = input("Unesite znak za drvce: ")

print()
print("Vaše božićno drvce:")
print()

# Ispis krošnje drvca
for i in range(visina):
    # Broj razmaka na početku reda
    razmaci = ' ' * (visina - i - 1)
    
    # Broj znakova u redu (neparan broj: 1, 3, 5, 7...)
    broj_znakova = 2 * i + 1
    
    # Ispis reda
    print(razmaci + znak * broj_znakova)

# Ispis debla drvca
deblo_sirina = 3  # deblo ima 3 znaka
deblo_visina = 2  # deblo ima 2 reda

for j in range(deblo_visina):
    # Razmaci za centriranje debla
    razmaci_deblo = ' ' * (visina - 2)
    print(razmaci_deblo + '|' * deblo_sirina)
