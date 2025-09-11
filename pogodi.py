# Definira riječ koju korisnik mora pogoditi (mala slova)
hidden_word = 'python'

while True:
    user_guess = input('Koju riječ sam zamislio: ').lower()  # unos odmah u mala slova

    if user_guess == '?':
        print(f"HINT: Prvo slovo riječi je '{hidden_word[0]}'")
        continue

    if user_guess == hidden_word:
        print(f'Pogodili ste!!! Bravo!!! Zamišljena riječ je {hidden_word}!')
        break

    # Ako ne pogodi, ispiši dodatnu sugestiju za hint
    print("Nažalost niste pogodili zamišljenu riječ. Pokušajte ponovno.")
    print("Ako želite POMOĆ, upišite znak ? za hint!")  # ← dodatna uputa za korisnika
