print(8 * 3) # działania na liczbach

five = 5
three = 3
print(five * three) # działania na zmiennych do których przypisano liczby

print(type(five)) # sprawdzamy typ zmiennej

print(type(five * three)) # sprawdzamy typ dla wyniku wyknanego obliczenia

import sys
print(sys.maxsize)

number1 = sys.maxsize
print(type(number1))
print(type(number1 + number1)) # ze względu na dynamiczne implementowanie zwróci int

very_big_value = 99999999999999999999999999
print(type((very_big_value+1)/2)) # operator dzielenia w Pythonie zawsze zwraca float

print(five//three) # dzielenie całkowite

print(five % three) # dzielenie modulo

print(float('inf') > 9999999999999999999) # string inf rzutowany na float jest interpretowany jako nieskończoność