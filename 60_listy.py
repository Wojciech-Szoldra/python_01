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

countries = ['FR', 'USA', 'DE', 'RU']
countries_copy = countries.copy() # skopiowanie i utworzenie nowej listy, każda zmienna to osobna lista

# *** Listy - LAB ***

hits_titles = ['BROTHERS IN ARMS','BOHEMIAN RHAPSODY','STAIRWAY TO HEAVEN','RIDERS ON THE STORM','WISH YOU WERE HERE']
print(hits_titles)

hits_titles.append('CHILD IN TIME')
hits_titles.append('AGAIN')
print(hits_titles)

hits_titles.insert(2,'HOTEL CALIFORNIA')
print(hits_titles)

hits_titles.insert(0,'THE SOUND OF SILENCE')
print(hits_titles)

print(hits_titles.index('THE SOUND OF SILENCE'))

hits_titles.remove('HOTEL CALIFORNIA')
print(hits_titles)

hits_titles[0] = 'ENJOY THE SILENCE'
print(hits_titles)

hits_to_read = hits_titles.copy()
hits_to_read.reverse()
print(hits_to_read)

hits_to_read.sort()
print(hits_to_read)

print(hits_to_read.pop(0))
print(hits_to_read.pop(1))
print(hits_to_read)

aditional_songs = ['NOTHING COMPARES 2 U','WISH YOU WERE HERE']
hits_to_read.extend(aditional_songs)
print(hits_to_read)

print(hits_to_read.count('RIDERS ON THE STORM'))
print(hits_to_read.count('WISH YOU WERE HERE'))

hits_to_read.clear()
print(hits_to_read)