# Dokładny opis w notatkach
# W pętli while wykonujemy dodawanie wewnątrz append() - ciekawe 

width = 50
height = 5

numbers = [1]

line = ''

for n in numbers:
    line+= '%4d' % (n)

print(line.center(width))

for i in range(height):
	
    new_numbers = [1]
    position = 0
    
    while position < len(numbers) -1:
        new_numbers.append(numbers[position] + numbers[position+1])
        position+=1
        
    new_numbers.append(1)
    numbers = new_numbers.copy()

    line = ''
    for n in numbers:
        line+= '%4d' % (n)

    print(line.center(width))

print('====LAB====\n')

print('====ZAD 1====\n')

import random

colors = ['Hearts','Diamonds','Clubs','Spades']

figures = [
    {'Figure':'Ace',  'Power':14},
    {'Figure':'King', 'Power':13},
    {'Figure':'Queen','Power':12},
    {'Figure':'Jack', 'Power':11},
    {'Figure':'10',   'Power':10},
    {'Figure':'9',    'Power':9}]

all_cards = []

for c in colors:
    for f in figures:
        a_card = f.copy()
        a_card['Color'] = c
        all_cards.append(a_card)

print(all_cards)
print(len(all_cards))