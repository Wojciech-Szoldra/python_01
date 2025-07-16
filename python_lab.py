print('---1. Typy danych---')

num1 = 2
print(type(num1))
str_num = str(num1)
print(type(str_num))

print('---2. Input---')

'''
def multiplication():
    number_1 = input('Enter first number: ')
    number_2 = input('Enter second number: ')
    result = int(number_1) * int(number_2)
    return print(f'Result: {result}')

multiplication()
'''

print('---3. Struktury danych---')

hp = ['KF','KT','WA','CZO','ZF','KP','IŚ']
print(hp)
print(hp[2]) #indeksujemy od zera
hp.append('NEW1') #dodajemy na końcu
print(hp)
hp.insert(1,'NEW2') #dodajemy na we wskazanym indeksie
print(hp)
hp.remove('NEW1')
print(hp)
hp.sort() #sortujemy listę - nie zwraca nowej
print(hp)
list1 = [2,6,8,3,4]
list2 = sorted(list1) #sortujemy listę - zwraca nową
print(list2)
