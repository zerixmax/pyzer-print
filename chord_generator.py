# +-+-+-+-+-+-+
# |P|y|Z|3|R|
# +-+-+-+-+-+-+

import os

# Chord Generator
# This program generates major and minor chords based on a user-provided starting note.

notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "H"]

while True:
    # Clear the terminal screen for a clean interface on each run.
    os.system('cls' if os.name == 'nt' else 'clear')

    # 1. Display the list of available notes to the user.
    print("--- Chord Generator ---")
    print("Available notes:", ", ".join(notes))
    print()

    # 2. Prompt the user to enter the name of a starting note.
    start_note = input("Enter a starting note (e.g., C, D#, F#): ").strip()

    # 3. Validate the input.
    if start_note not in notes:
        print(f"\nError: '{start_note}' is not a valid note. Please choose from the list above.")
    else:
        # 4. If the input is valid, find the position (index) of the note.
        print(f"\nCalculating chords for the note: {start_note}")
        root_index = notes.index(start_note)

        # 5. Calculate the notes for the MAJOR (DUR) and MINOR (MOL) chords.
        major_chord_notes = [
            notes[root_index],
            notes[(root_index + 4) % 12],
            notes[(root_index + 7) % 12]
        ]

        minor_chord_notes = [
            notes[root_index],
            notes[(root_index + 3) % 12],
            notes[(root_index + 7) % 12]
        ]

        # 6. Print the results.
        print(f"MAJOR (DUR) Chord: {', '.join(major_chord_notes)}")
        print(f"MINOR (MOL) Chord: {', '.join(minor_chord_notes)}")

    # Prompt the user to continue or exit.
    print()
    play_again = input("Generate another chord? (yes/no): ").strip().lower()
    if play_again != 'yes':
        print("\nThank you for using the Chord Generator!")
        break

