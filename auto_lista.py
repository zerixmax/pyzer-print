# +-+-+-+-+-+-+
# |P|y|Z|3|R|
# +-+-+-+-+-+-+
# Program za upravljanje bazom podataka vozila
# Autor: Ivo Cetinic
print("PyZ3R - Program za upravljanje bazom podataka vozila")
print()

def napravi_bazu_vozila():
    vozila = {
        1: {
            'tip': 'MPV',
            'model': 'Partner Tepee',
            'marka': 'Peugeot',
            'registracija': 'DU 283 KN',
            'godina': 2010,
            'cijena': 6500
        },
        2: {
            'tip': 'hatchback',
            'marka': 'Renault',
            'model': 'Clio',
            'registracija': 'DU 951 DK',
            'godina': 2006,
            'cijena': 1500
        },
        3: {
            'tip': 'limuzina',
            'marka': 'Audi',
            'model': 'A4',
            'registracija': 'DU 696 KB',
            'godina': 2012,
            'cijena': 5500
        },
        4: {
            'tip': 'hatchback',
            'marka': 'Renault',
            'model': '4 GTL',
            'registracija': 'DU 751 BC',
            'godina': 1988,
            'cijena': 3500
        },
        5: {
            'tip': 'MPV',
            'marka': 'Peugeot',
            'model': 'Rifter',
            'registracija': 'DU Z3R 1X',
            'godina': 2020,
            'cijena': 10500
        }
    }
    return vozila   

def ispis_vozila(baza):
    """Ispis baze vozila u tabličnom formatu."""
    print(f"{'ID':<5} {'Tip':<15} {'Marka':<15} {'Model':<15} {'Registracija':<15} {'Godina':<10} {'Cijena (EUR)':>12}")
    print("=" * 100)
    for id, vozilo in baza.items():
        print(f"{id:<5} {vozilo['tip']:<15} {vozilo['marka']:<15} {vozilo['model']:<15} {vozilo['registracija']:<15} {vozilo['godina']:<10} {vozilo['cijena']:>12,}")

def unos_novog_vozila():
    """Prikuplja podatke o novom vozilu od korisnika."""
    print("\n--- Unos novog vozila ---")
    tip = input("Unesite tip vozila: ")
    marka = input("Unesite marku vozila: ")
    model = input("Unesite model vozila: ")
    registracija = input("Unesite registraciju vozila: ")
    
    while True:
        try:
            godina = int(input("Unesite godinu proizvodnje: "))
            break
        except ValueError:
            print("Greška: Godina mora biti broj.")
            
    while True:
        try:
            cijena = int(input("Unesite cijenu vozila (EUR): "))
            break
        except ValueError:
            print("Greška: Cijena mora biti broj.")
            
    return tip, marka, model, registracija, godina, cijena

def dodaj_vozilo(baza, tip, marka, model, registracija, godina, cijena):
    """Dodaje novo vozilo u bazu podataka."""
    novo_id = max(baza.keys()) + 1 if baza else 1
    baza[novo_id] = {
        'tip': tip,
        'marka': marka,
        'model': model,
        'registracija': registracija,
        'godina': godina,
        'cijena': cijena
    }
    print(f"\nVozilo s ID {novo_id} dodano u bazu podataka.")
    print()

if __name__ == "__main__":
    baza_vozila = napravi_bazu_vozila()
    print("--- Trenutni inventar vozila ---")
    ispis_vozila(baza_vozila)
    print()

    unos = input("Želite li unijeti novo vozilo? (da/ne): ").strip().lower()
    if unos == "da":
        tip, marka, model, registracija, godina, cijena = unos_novog_vozila()
        dodaj_vozilo(baza_vozila, tip, marka, model, registracija, godina, cijena)
        print("\n--- Ažurirani inventar vozila ---")
        print()
        ispis_vozila(baza_vozila)
        print()