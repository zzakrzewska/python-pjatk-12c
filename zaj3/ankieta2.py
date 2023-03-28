## Zofia Zakrzewska / 12c / s24365
from datetime import date
import re

print('podaj imie: ')
imie = input()
warunek = True

while(warunek):
    if isinstance(imie, str):
        warunek = False
    else:
        print('wpisano nieprawidlowa wartosc')
        print('podaj imie: ')
        imie = input()

print('podaj rok urodzenia: ')
rok = input()
warunek = True

while(warunek):
    if rok.isdigit():
        warunek = False
    else:
        print('wpisano nieprawidlowa wartosc')
        print('podaj rok urodzenia: ')
        rok = input()

print('podaj miesiac urodzenia: ')
miesiac = input()
warunek = True

while (warunek):
    if miesiac.isdigit():
        if int(miesiac) >= 1 & int(miesiac) <= 12:
            warunek = False
    else:
        print('wpisano nieprawidlowa wartosc')
        print('podaj miesiac urodzenia: ')
        miesiac = input()

print('podaj dzien urodzenia: ')
dzien = input()
warunek = True

while (warunek):
    if dzien.isdigit():
        if int(dzien) >= 1 & int(dzien) <= 31:
            warunek = False
    else:
        print('wpisano nieprawidlowa wartosc')
        print('podaj dzien urodzenia: ')
        dzien = input()

dataUrodzenia = date(int(rok), int(miesiac), int(dzien)).isoformat()

print('podaj adres email: ')
mail = input()
warunek = True

while (warunek):
    if re.match("([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+", mail):
        warunek = False
    else:
        print('wpisano nieprawidlowa wartosc')
        print('podaj adres email: ')
        mail = input()

print('podaj numer telefonu: ')
numerTelefonu = input()
warunek = True

while (warunek):
    if numerTelefonu.isdigit() & (len(numerTelefonu) == 9):
        warunek = False
    else:
        print('wpisano nieprawidlowa wartosc')
        print('podaj numer telefonu: ')
        numerTelefonu = input()

lista = [imie, dataUrodzenia, mail, numerTelefonu]
print("lista:")
print(lista)

krotka = (imie, dataUrodzenia, mail, numerTelefonu)
print("krotka:")
print(krotka)

slownik = dict(name=imie, birthdate=dataUrodzenia, email=mail, phone=numerTelefonu)

print("slownik:")
print(slownik)
