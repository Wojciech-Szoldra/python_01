atext='This is a text.' # zmienna tyu tekstowego

print(atext.endswith('ext.')) # sprawdzamy czy string kończy się danym ciągiem

print(atext.islower()) # sprawdzamy czy w stringu wszystkie znaki są małe

print(atext.upper()) # zmiana liter na duże

print(atext.upper().isupper()) # dwie funkcje jedna po drugiej

print(atext.find('is')) # funkcja szukająca wystąpienia danego stringa. Wskazuje numeru znaku na którym dany string się pojawia - liczymy od 0

print(atext.find('is', 3)) # możemy wskazać od której litery ma zacząć szukać

print(atext.replace('a','4')) # wymiana znaków

print(atext.split(' ')) # podział stringa według wskazanego znaku i utworzenie tabeli z powstałych stringów

number_test='100'

print(number_test)

print(number_test.isdigit()) # sprawdza czy wszystkie znaki w stringu są cyframi

number_test2='9,2'

print(number_test2.isdecimal()) # cyfry muszą być z przedziału 0-9 w innym wypadku zwraca false

print(atext.isalpha()) # sprawdza czy w stringu są tylko litery

text_test='T3stujemy'

print(text_test.isalnum()) # sprawdza czy wszystkie znaki są lierami/cyframi

# ***35. Typ string cz.1 - LAB***

print('\n'+'Zadania''\n')

quote='A good programmer is someone who always looks both ways before crossing a one-way street'

print(f'upper(): {quote.upper()}')

print(f'lower(): {quote.lower()}')

print(quote.endswith('street'))

print(quote.isupper())

print(quote.upper().isupper())

print(f'find(): {quote.find('one')}')

print(quote.replace('one','1'))

print(quote.replace('one','1').replace('both','2'))

#words=quote.split(' ')

#print(words)

print(f'split(): {quote.split(' ')}')

print(quote)

print(quote.isdigit())

print(quote.isdecimal())

print(quote.isalpha())

print(quote.isalnum())