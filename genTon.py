import os

tonovi = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "H"]

def ocisti_terminal():
    # Očisti terminal (Windows: 'cls', ostalo: 'clear')
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    ocisti_terminal()
    print('\nMogući tonovi su:')
    print()  # Dodan prazan red za bolji pregled
    for ton in tonovi:
        print(ton, end="  ")
    print("\n")
    
    pocetni_ton = input("Unesi početni ton za akord (primjer: C, D#, G, ...): ").strip()
    print()

    if pocetni_ton not in tonovi:
        print("Unio si nepoznat ton! Pokušaj ponovno i unesi ton točno kako piše gore.\n")
    else:
        print(f'Unio si ton: {pocetni_ton}\n')
        indeks = tonovi.index(pocetni_ton)

        dur_akord = [
            tonovi[indeks],
            tonovi[(indeks + 4) % 12],
            tonovi[(indeks + 7) % 12]
        ]
        mol_akord = [
            tonovi[indeks],
            tonovi[(indeks + 3) % 12],
            tonovi[(indeks + 7) % 12]
        ]

        print("Rezultat:\n")
        print(f'   DUR akord ({pocetni_ton} dur): {", ".join(dur_akord)}')
        print(f'   MOL akord ({pocetni_ton} mol): {", ".join(mol_akord)}')
        print()
        print("\033[92m")  # Uključi zelenu boju
    print(""" +-+-+-+-+-+
 |P|y|Z|3|R|
 +-+-+-+-+-+
""")
    print("\033[0m")  # RESET boje (vrati na normalno)

    izbor = input("Želiš li još jedan generator akorda? (upiši da / ne): ").strip().lower()

   #
    if izbor != "da":
        print("\nHvala na korištenju generatora akorda! Do viđenja :)\n")
        break
