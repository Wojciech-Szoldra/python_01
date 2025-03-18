print('*** Lesson ***\n')

#import modułu
import random

print(random.random()) #zwraca liczbę zmiennoprzecinkowa z przedziału [0.0, 1.0]

print(random.randint(1, 10)) #zwraca liczbę całkowitą z przedziału [a,b] włącznie z a i b

fruits = ['jabłko','banan','wiśnia'] #wybiera losowy element z sekwencji
print(random.choice(fruits))

#wybiera k elementów z populacji, z możliwością ustawienia wag
colors = ['czerwony','zielony','niebieski'] 
print(random.choices(colors, weights=[10,1,1], k =2))

#łuży do losowego przetasowania elementów listy
numbers = [1,2,3,4,5]
random.shuffle(numbers)
print(numbers)

print('\n*** LAB ***')
print('\nTask 1\n')

for i in range(1,11):
    num1 = random.randint(1,100)
    print(f'{i} random number: {num1}')

print('\nTask 2\n')

number1 = random.randint(1,100)
number2 = 0
counter = 1

while number1 != number2:
    number2 = random.randint(1,100)
    print(f'Attempt {counter}: number1 - {number1} / number2 - {number2}')
    
    if number1 == number2:
        print(f'It took {counter} tries')
    
    counter += 1

    