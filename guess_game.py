
import random

# Lista mogućih jezika
languages = ['Python', 'Java', 'C#', 'Javascript', 'Typescript', 'Golang', 'Rust', 'Lua']

# Nasumično odabire indeks jezika iz liste
selected_language_index = random.randint(0, len(languages)-1)
# selected_language = languages[selected_language_index]  # možete koristiti i ovako, radi preglednosti

brojac = 0  # Brojac pokušaja

while True:
    users_guess = input('Pogodite naziv programskog jezika: ')
    brojac += 1  # Svaki pokušaj povećava brojač za 1

    # Provjerava je li unos jednak traženom jeziku (neovisno o velikim/malim slovima)
    if users_guess.lower() == languages[selected_language_index].lower():
        print(f'Čestitamo!!! Pogodili ste naziv programskog jezika iz {brojac} pokušaja!')
        break  # prekida petlju - igra je gotova
    else:
        print('Nažalost niste pogodili! Pokušajte ponovno.')

    # Daje korisniku mogućnost da odustane
    next_round = input('Želite li nastaviti? (Da/Ne): ')
    if next_round.strip().lower() == 'ne':  # pametno usporediti s malim slovima, i maknuti višak razmaka
        break

# Završna poruka
print()
print('Pozdrav, do sljedećeg puta!')
print()
