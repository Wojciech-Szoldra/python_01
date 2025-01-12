country_leaders = {'PL':'Duda','US':'Trump'} # utworzenie słownika
print(country_leaders['US']) # odwołanie po kluczu -> wyświetlenie wartości

country_leaders['DE'] = 'Merkel' # dodanie nowej wartości do słownika
print(country_leaders)

print(country_leaders.keys()) # zwraca klucze znajdujące się w słowniku
print(country_leaders.values()) # zwraca wartości znajdujące się w słowniku
print(country_leaders.items()) # zwraca pary wartość/klucz

print(country_leaders.popitem()) # pobierze / zwróci / usunie - ostatni element
print(country_leaders) # słonik już bez ostatniego elementu

# metoda setdefault()
slownik = {'a': 10, 'b': 20}
print(slownik.setdefault('a')) # klucz istnieje - zwróci jego wartość

slownik.setdefault('c', 30) # klucz nie istnieje - zostanie dodany razem z wartością
print(slownik)

slownik.setdefault('d') # klucz nie istnieje / brak wartości - zostanie dodany z 'None'
print(slownik)

print(country_leaders.get('PL')) # klucz istnieje - zwróci wartość
print(country_leaders.get('RU')) # klucz nie istnieje - zwróci 'None'

new_leaders = {'IT':'Mattarella','DE':'Schulz'}
# wartość z tym samym kluczem zostanie podmienia, wartość z nowym kluczem zostanie dodana
country_leaders.update(new_leaders)
print(country_leaders)

# *** Dictionary - LAB ***

chanels = {'Google':1480, 'Email':300, 'Natural Traffic':440, 'TV Spot':700}
print(chanels)

print(chanels['Email'])

chanels_update = {'Natural Traffic':520, 'News':600}
print(chanels)

chanels.update(chanels_update)
print(chanels)

print(chanels.keys())

print(chanels.pop('Email'))
print(chanels)

# *** Testy ***

slownik_test = {'wart1':1, 'wart2':2, 'wart3':3, 'wart4':4, 'wart5':5}
print(slownik_test.pop('wart5')) # usunie wartość po przekazanym kluczu - bez argumentu wyrzuci błąd
print(slownik_test)

print(slownik_test.popitem()) # usunie ostatnią wartość, nie przyjmuje argumentów
print(slownik_test)