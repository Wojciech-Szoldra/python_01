print(8 * 3) # działania na liczbach

five = 5
three = 3
print(five * three) # działania na zmiennych do których przypisano liczby

print(type(five)) # sprawdzamy typ zmiennej

print(type(five * three)) # sprawdzamy typ dla wyniku wykonanego obliczenia

import sys
print(sys.maxsize)

number1 = sys.maxsize
print(type(number1))
print(type(number1 + number1)) # ze względu na dynamiczne implementowanie zwróci int

very_big_value = 99999999999999999999999999
print(type((very_big_value+1)/2)) # operator dzielenia w Pythonie zawsze zwraca float

print(f'Dzielenie całkowite: {five//three}') # dzielenie całkowite

print(five % three) # dzielenie modulo

print(float('inf') > 9999999999999999999) # string inf rzutowany na float jest interpretowany jako nieskończoność

# *** Formatowanie napisów i typy numeryczne - LAB ***

name = 'John'
age = 35
days_in_year = 365
days_old = age * days_in_year
message = '{0:s} is {1:d} years old, so he is about {2:d} days old'
print(message.format(name,age,days_old))

print(f'1234567890 devided by 12345 is {1234567890//12345} and the rest is {1234567890 % 12345}')