countries = ['FR', 'USA', 'DE', 'RU'] # utworzenie listy
print(countries)

print(countries[1]) # wyświetlenie elementu o indeksie 1

countries[1] = 'GB' # zmiana wartości indeksu
print(countries)

countries.append('PL') # dodanie elementu na końcu listy 
print(countries)

countries.insert(2,'ES') # wstawianie elementu na wskazaną pozycję
print(countries)

countries.remove('RU') # usunięcie elementu
print(countries)

countries.reverse() # odwrócenie listy
print(countries)

print(countries.pop(2)) # wyświetlenie i usunięcie elementu z listy
print(countries)

print(countries.index('PL')) # na którym indeksie występuje dana wartość

print(countries.count('GB')) # sprawdzamyile razy dana wartość występuje w liście

new_list = ['FI','SE']
countries.extend(new_list) # połączenie dwóch list
print(countries)

countries_copy = countries # dwie zmienne wskazują na tą samą listę
countries_copy.clear() # usunięcie wszystkich elementów z listy
print(countries_copy, countries)