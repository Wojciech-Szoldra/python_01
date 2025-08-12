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

print(f'Deck in order: {all_cards}')
random.shuffle(all_cards)
print('\n')
print(f'Shuffled deck: {all_cards}')

print('\n')

player1 = []
player2 = []

max = len(all_cards)

for i in range(max):
    if i % 2 == 0:
        player1.append(all_cards[i])
    else:
        player2.append(all_cards[i])

print(f'Player 1: {player1}\n')
print(f'Player 2: {player2}')

game=1

while len(player1) > 0:
    card1 = player1.pop(0)
    card2 = player2.pop(0)

    if card1['Power'] == card2['Power']:
        player1.append(card1)
        player2.append(card2)
        print(f'Game:{game}    EQUAL  {card1['Power']} vs {card2['Power']}') 
    elif card1['Power'] > card2['Power']:
        player1.append(card1)
        player1.append(card2)
        print(f'Game:{game}    PLAY-1  {card1['Power']} vs {card2['Power']}  {'*'*len(player1)}') 
    elif card1['Power'] < card2['Power']:
        player2.append(card1)
        player2.append(card2)
        print(f'Game:{game}    PLAY-2  {card1['Power']} vs {card2['Power']}  {'*'*len(player2)}') 

    game+=1

print('Player 1 WON !!!') if len(player1) > 0 else print('Player 2 WON !!!')


