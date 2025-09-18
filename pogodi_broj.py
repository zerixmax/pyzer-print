# +-+-+-+-+-+-+
# |P|y|Z|3|R|
# +-+-+-+-+-+-+

import random
import os

def ocisti_ekran():
    """Čisti ekran terminala."""
    os.system('cls' if os.name == 'nt' else 'clear')

def igra_pogadanja_broja():
    ocisti_ekran()
    print("\n>> Igra pogađanja broja <<")
    print("Računalo je izabralo broj između 1 i 100.")
    tajni_broj = random.randint(1, 100)
    broj_pokusaja = 0
    
    while True:
        try:
            korisnicki_unos = int(input("Pokušaj pogoditi moj broj: "))
            broj_pokusaja += 1
        except ValueError:
            print("Molim upiši cijeli broj!")
            continue
        
        if korisnicki_unos < 1 or korisnicki_unos > 100:
            print("Broj treba biti između 1 i 100.")
            continue

        if korisnicki_unos < tajni_broj:
            print("Moj broj je veći!")
        elif korisnicki_unos > tajni_broj:
            print("Moj broj je manji!")
        else:
            print(f"Bravo! Pogodio si broj {tajni_broj} u {broj_pokusaja} pokušaja.")
            break

def main():
    while True:
        igra_pogadanja_broja()
        odluka = input("\nŽeliš li igrati opet? (da/ne): ").strip().lower()
        if odluka != "da":
            print("\nHvala na korištenju igre pogađanja broja!")
            break

if __name__ == "__main__":
    main()
