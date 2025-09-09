# for petlje 
#n = 5 #visina trokuta
#for i in range(1, n + 1):
#    print('*' * i)


#    print('Ispis trokuta varijabilne visine pomoću for petlje')
#print('Uz izbor znaka za iscrtavanje linija stranica trokuta')


symbol = input('Unesite znak za ispisivanje trokuta: ')
height = int(input('Unesite visinu trokuta: '))
print()
print(symbol)
for number in range(height - 2):
    print(f"{symbol}{' ' * (number)}{symbol}")

print(f"{symbol * (height)}")
print()
print('Kraj programa')