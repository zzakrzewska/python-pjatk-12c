# Zofia Zakrzewska s24365 / gr 12

# zad 1
print("----------zadanie 1----------")
for i in range(1, 21):
    print(i)

# zad 2
print("----------zadanie 2----------")
for i in range(5, 45):
    if (i % 5 == 0):
        print(i)

# zad 3
print("----------zadanie 3----------")
i = 100

while i >= 50:
    print(i)
    i -= 1

# zad 4
print("----------zadanie 4----------")
print("podaj x:")
x = int(input())

print("podaj y:")
y = int(input())

for i in range(x, y+1):
    print(i)

#zad 5
print("----------zadanie 5----------")
print("podaj liczbe calkowita dodatnia")
liczba = int(input())
poprawne = False

while poprawne == False:
    if liczba > 0:
        poprawne = True
    else:
        print("podano niepoprawna liczbe")
        print("podaj liczbe calkowita dodatnia")
        liczba = int(input())

#zad 6
print("----------zadanie 6----------")
x = 10
y = 128
suma = 0

for i in range (x, y+1):
    if i%2 != 0:
        suma += 1

print("suma liczb nieparzystych: " + str(suma))