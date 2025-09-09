potrosnja_l_100km = 5.3     # litara na 100 km
cijena_goriva_eur_l = 1.27  # cijena goriva u EUR po litri
udaljenost_posao_km = 20 # udaljenost do posla u km (jedan smjer)
dani_mjesecno = 30

potrosnja_po_km = potrosnja_l_100km / 100
trosak_po_km = potrosnja_po_km * cijena_goriva_eur_l

km_dnevno = udaljenost_posao_km * 2
km_mjesecno = km_dnevno * dani_mjesecno
trosak_mjesecno = km_mjesecno * trosak_po_km

print("=== Automobil: trošak EUR ===")
print(f"Trošak po kilometru: {trosak_po_km:.2f} EUR/km")
print(f"Mjesečni trošak goriva: {trosak_mjesecno:.2f} EUR")

# Zadatak 2: Jednostavna kamata (direktno u eurima)
glavnica_eur = 1327        # početni iznos u eurima
kamata_postotak = 2.5
vrijeme_godine = 15

kamata = glavnica_eur * kamata_postotak * vrijeme_godine / 100
ukupan_iznos = glavnica_eur + kamata

print("\n=== Jednostavna kamata EUR ===")
print(f"Kamata nakon {vrijeme_godine} godina: {kamata:.2f} EUR")
print(f"Ukupan iznos (glavnica + kamata): {ukupan_iznos:.2f} EUR")
