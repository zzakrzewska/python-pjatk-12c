# Zofia Zakrzewska / 12c / s24365

print('wpisz dzialanie (format [x + y]: ')
input = input()

x = input.split()

try:
    if x[1] == '+':
        print(int(x[0]) + int(x[2]))
    elif x[1] == '-':
        print(int(x[0]) - int(x[2]))
    elif x[1] == '*':
        print(int(x[0]) * int(x[2]))
    elif x[1] == '/':
        print(int(x[0]) / int(x[2]))
    else:
        print('nieprawidlowy input')

except(IndexError, ValueError):
    print('nieprawidlowy input')

exit()

##wzrost, kolor oczu, wlosow, wiek