## Zofia Zakrzewska / 12c / s24365

def pierwsza(num):
    prime = True

    for n in range(2, int(num/2+1)):
        if num%n != 0:
            prime = False

    return prime

print("podaj 20 liczb z zakresu -20 do 20 oddzielone przecinkami:")
liczbyString = input()
liczbySplit = liczbyString.split(",")
liczby = list(map(int, liczbySplit))

liczbyPierwsze = []

for liczba in liczby:
    if pierwsza(liczba):
        liczbyPierwsze.append(liczba)

pierwsze = tuple(liczbyPierwsze)
print(pierwsze)