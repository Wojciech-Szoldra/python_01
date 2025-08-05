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