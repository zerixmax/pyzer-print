import  random
print()
print("Dobrodošli u igru pogađanja pojmova!")

#Liste tema igre
tema = ["Programski jezici", "filmovi", "Sportovi"]
programski_jezici = ["Python", "Java", "C#", "JavaScript", "TypeScript", "Golang", "Rust", "Lua"]
filmovi = ["Blade Runner", "Inception", "The Matrix", "Interstellar", "The Godfather", "Gladiator"]
sportovi = ["Nogomet", "Košarka", "Rukomet", "Odbojka", "Tenis", "Ribolov", "Plivanje"]

#Prikazivanje tema
while True:
    print()
    print("Izaberi temu igre:")
    print()
    for i in range(len(tema)):
        print(f"{i + 1}. {tema[i]}")
        print()
    izbor = input("Unesite broj teme: ")

    #odabir teme i provjera unosa korisnika
    if izbor == "1":
        odabrana_tema = programski_jezici
        naziv_teme = tema[0]
    elif izbor == "2":
        odabrana_tema = filmovi
        naziv_teme = tema[1]
    elif izbor == "3":
        odabrana_tema = sportovi
        naziv_teme = tema[2]
    else:
        print("Nevažeći unos, pokušajte ponovo.")
        continue

    # Random izbor riječi iz odabrane teme        
    tajna_rijec = random.choice(odabrana_tema).lower()
    pokusaji = 0
    max_pokusaji = 6
    print (tajna_rijec)  # Za testiranje, može se ukloniti u produkcijskoj verziji


    # Glavna igra
    while True:
        unos = input("Pogodi riječ: ").lower()
        if unos == tajna_rijec:
            print("Čestitamo, pogodili ste riječ!")
            break
        else:
            pokusaji += 1
            if pokusaji >= max_pokusaji:
                print(f"Izgubili ste! Tajna riječ je bila: {tajna_rijec}")
                break
            else:
                print(f"Pogrešan odgovor. Preostalo pokušaja: {max_pokusaji - pokusaji}")
                if pokusaji == 3:
                    print(f"Hint: Riječ počinje sa '{tajna_rijec[0]}' i završava sa '{tajna_rijec[-1]}'")

    # Kraj igre ili ponovni početak
    ponovo = input("Želite li igrati ponovo? (da/ne): ").lower()
    if ponovo != "da":
        print("Hvala na igranju! Doviđenja!")
        break

