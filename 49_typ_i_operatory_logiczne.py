is_weekend = True # zmienna logiczna
temperature = 22
to_do_list = ''
is_happy = is_weekend and temperature >= 20 and to_do_list == '' # wyznaczenie wartości zmiennej logicznej
print('1. Are you happy? True/False:',is_happy)

is_weekend = True
temperature = 5 # zmiana wartości 
to_do_list = ''
is_happy = is_weekend and temperature >= 20 and to_do_list == '' # zmieniła się wartośc przez co mamy inny rezultat
print('2. Are you happy? True/False:',is_happy)

# zmieniamy 'powody' dla których zwrócone ma zostać True
is_weekend = False
temperature = 5 
to_do_list = 'Shopping'
is_happy = not is_weekend and temperature < 20 and to_do_list != '' # zastosowanie operatora not
print('3. Are you happy? True/False:',is_happy)

# Tworzenie alternatywy z wykorzystaniem operatora OR
is_happy = is_weekend and temperature >= 20 and to_do_list == '' or \
not is_weekend and temperature < 20 and to_do_list != '' # pierwsze trzy warunki LUB ostatnie trzy warunki muszą być spełnione aby wynik był True. Znak backshlash umożliwia podzielnie kodu

print('4. Are you happy? True/False:',is_happy)

# Przykłądy z operatorem NOT
x = 30
test1 = x < 30
print('test1:',test1)
test2 = not x < 30 # not odwraca wartość logiczną
print('test2:',test2)

y = 10
z = 15
test3 = y < 10 and z < 15
print('test3:',test3)
test4 = not y < 10 and not z < 15
print('test4:',test4)
test5 = not (y < 10 or z < 15) # zamiast zaprzeczać dwa warunki można zaprzeczyć ich alternatywę
print('test5:',test5)