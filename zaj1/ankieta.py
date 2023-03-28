# Zofia Zakrzewska / 12c / s24365

print('podaj wzrost: ')
wzrost = input()
warunek = True

while(warunek):
    if wzrost.isdigit():
        warunek = False
    else:
        print('wpisano nieprawidlowa wartosc')
        print('podaj wzrost: ')
        wzrost = input()

print('podaj wiek: ')
wiek = input()
warunek = True

while(warunek):
    if wiek.isdigit() and wiek < 150:
        warunek = False
    else:
        print('wpisano nieprawidlowa wartosc')
        print('podaj wiek: ')
        wiek = input()

print('podaj kolor oczu: ')
kolorOczu = input()
warunek = True

while(warunek):
    if isinstance(kolorOczu, str):
        warunek = False
    else:
        print('wpisano nieprawidlowa wartosc')
        print('podaj kolor oczu: ')
        kolorOczu = input()

print('podaj kolor wlosow: ')
kolorWlosow = input()
warunek = True

while(warunek):
    if isinstance(kolorWlosow, str):
        warunek = False
    else:
        print('wpisano nieprawidlowa wartosc')
        print('podaj kolor wlosow: ')
        kolorWlosow = input()

print()
print('podane odpowiedzi: ')
print(f'wzrost: {wzrost}')
print(f'wiek: {wiek}')
print(f'kolor oczu: {kolorOczu}')
print(f'kolor wlosow: {kolorWlosow}')

exit()
