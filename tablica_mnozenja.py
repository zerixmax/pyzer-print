# +-+-+-+-+-+-+
# |P|y|Z|3|R|
# +-+-+-+-+-+-+

def prikazi_tablicu_mnozenja():
    print("Dobrodošli u program za tablicu množenja!\n")
    while True:
        try:
            n = int(input("Unesi broj do kojeg želiš tablicu množenja: "))
            if n < 1:
                print("Molim unesi broj veći od nule.\n")
                continue
            break
        except ValueError:
            print("Unesi cijeli broj!\n")

    print("\nTablica množenja do broja", n, ":\n")

    # Ispis zaglavlja (brojevi iznad stupaca)
    print("\t", end="")
    for i in range(1, n+1):
        print(f"{i}\t", end="")
    print("\n" + "-" * (n+1)*4)

    # Ispis redova tablice
    for i in range(1, n+1):
        print(f"{i}|\t", end="")
        for j in range(1, n+1):
            print(f"{i*j}\t", end="")
        print()  # novi red

def main():
    while True:
        prikazi_tablicu_mnozenja()
        izbor = input("\nŽeliš li generirati novu tablicu množenja? (da/ne): ").strip().lower()
        if izbor != "da":
            print("\nHvala na korištenju programa za tablicu množenja!")
            break

if __name__ == "__main__":
    main()
