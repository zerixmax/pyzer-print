# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# |P|y|Z|3|R| - Number Guessing Game |
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

import random
import os

def ocisti_ekran():
    """Čisti ekran terminala."""
    os.system('cls' if os.name == 'nt' else 'clear')

def prikazi_statistike(pokusaji):
    """Prikazuje statistike na osnovu broja pokušaja."""
    if pokusaji <= 5:
        return "🏆 ODLIČNO! Ekspertni igrač!"
    elif pokusaji <= 10:
        return "👍 VRLO DOBRO! Dobra strategija!"
    elif pokusaji <= 15:
        return "😊 DOBRO! Solidna igra!"
    else:
        return "😅 Imaš prostora za poboljšanje!"

def igra_pogadanja_broja():
    """Glavna funkcija igre pogađanja broja."""
    ocisti_ekran()
    print("=" * 50)
    print("🎯  IGRA POGAĐANJA BROJA  🎯")
    print("=" * 50)
    print("Računalo je odabralo broj između 1 i 100.")
    print("Pokušaj ga pogoditi u što manje pokušaja!")
    print("-" * 50)
    
    # Generiraj tajni broj
    tajni_broj = random.randint(1, 100)
    broj_pokusaja = 0
    pokusaji_lista = []
    
    while True:
        try:
            print(f"\n📝 Pokušaj #{broj_pokusaja + 1}")
            if pokusaji_lista:
                print(f"📊 Dosadašnji pokušaji: {', '.join(map(str, pokusaji_lista))}")
            
            korisnicki_unos = input("🎲 Unesi svoj broj (1-100): ")
            
            # Provjeri da li je unos broj
            if not korisnicki_unos.isdigit():
                print("❌ Molim upiši cijeli broj!")
                continue
                
            korisnicki_unos = int(korisnicki_unos)
            broj_pokusaja += 1
            pokusaji_lista.append(korisnicki_unos)
            
        except ValueError:
            print("❌ Molim upiši važeći broj!")
            continue
        
        # Provjeri da li je broj u validnom rasponu
        if korisnicki_unos < 1 or korisnicki_unos > 100:
            print("⚠️  Broj mora biti između 1 i 100!")
            broj_pokusaja -= 1  # Ne računa kao pokušaj
            pokusaji_lista.pop()  # Ukloni neispravni unos
            continue

        # Provjeri pogodak
        if korisnicki_unos < tajni_broj:
            razlika = tajni_broj - korisnicki_unos
            if razlika <= 5:
                print("🔥 VRLO BLIZU! Moj broj je veći!")
            else:
                print("⬆️  Moj broj je veći!")
        elif korisnicki_unos > tajni_broj:
            razlika = korisnicki_unos - tajni_broj
            if razlika <= 5:
                print("🔥 VRLO BLIZU! Moj broj je manji!")
            else:
                print("⬇️  Moj broj je manji!")
        else:
            # Pobjeda!
            print("\n" + "=" * 50)
            print("🎉 ČESTITAMO! POGODIO SI! 🎉")
            print("=" * 50)
            print(f"🎯 Tajni broj: {tajni_broj}")
            print(f"📊 Broj pokušaja: {broj_pokusaja}")
            print(f"📈 Tvoji pokušaji: {', '.join(map(str, pokusaji_lista))}")
            print(f"⭐ Ocjena: {prikazi_statistike(broj_pokusaja)}")
            
            # Dodatne statistike
            if len(pokusaji_lista) > 1:
                prosjek = sum(pokusaji_lista) / len(pokusaji_lista)
                print(f"📊 Prosjek pokušaja: {prosjek:.1f}")
            
            print("=" * 50)
            break

def main():
    """Glavna funkcija programa."""
    ukupne_igre = 0
    ukupni_pokusaji = 0
    
    while True:
        igra_pogadanja_broja()
        ukupne_igre += 1
        
        print(f"\n📈 Ukupno igara: {ukupne_igre}")
        
        while True:
            odluka = input("\n🔄 Želiš li igrati opet? (da/ne): ").strip().lower()
            if odluka in ['da', 'd', 'yes', 'y']:
                break
            elif odluka in ['ne', 'n', 'no']:
                print("\n" + "=" * 50)
                print("🎮 HVALA NA IGRANJU! 🎮")
                print("=" * 50)
                print(f"📊 Ukupno odigranih igara: {ukupne_igre}")
                print("👋 Do viđenja!")
                print("=" * 50)
                return
            else:
                print("❓ Molim odgovori 'da' ili 'ne'")

if __name__ == "__main__":
    main()