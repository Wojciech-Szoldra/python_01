# Importujemy moduł random
import random

# Tworzymy zmienną random w której przechowywane będą numery
my_numbers = []

# Pętla wykonuje się dopóki lista my_numbers jest mniejsza niż 7 elementów
# Przy każdym wykonaniu losujemy liczbę za pomocą randint(). Funkcja ta losuje z obustronnie domkniętego przedziału liczb całkowitych.
# Po wylosowaniu liczby sprawdzamy za pomocą instrukcji if czy liczba znajduje się już w naszej liście. jeżeli tak to wyświetlamy tę liczbę, a następnie korzystamy z instrukcji continue żeby pominąć kod znajdujący się pod nią i przejść do kolejnej iteracji
# Korzystając z append() umieszczamy wylosowaną liczbę na końcu listy 

while len(my_numbers) < 7:
    new_number = random.randint(1,49)
	
    if new_number in my_numbers:
        print(f'Eliminated: {new_number}')
        continue
    
    my_numbers.append(new_number)

print(f'Those numbers will win: {my_numbers}')

print('====LAB====\n')

print('====ZAD 1====\n')

import random

colors = ['Hearts','Diamonds','Clubs','Spades']
figures = ['Ace','King','Queen','Jack','10','9']

all_cards = []

for i in colors:
    for j in figures:
        all_cards.append(i+' '+j)

print(f'Deck in order: {all_cards}')
random.shuffle(all_cards)
print(f'Shuffled deck: {all_cards}')

print('='*40+'\n')

player1 = []
player2 = []

max = len(all_cards)
i=0

allCards = []
for c in colors:
    for f in figures:
        allCards.append("%s - %s" % (c, f))
 
print(allCards)

while i < (max-1):
    if i % 2 == 0:
        player1.append(all_cards[i])
    else:
        player2.append(all_cards[i])

    i+=1

print(f'Player 1: {player1}')
print(f'Player 2: {player2}')