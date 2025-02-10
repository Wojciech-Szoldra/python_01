print('Lesson')

print('\nver_1\n')

# Na jedno wykonanie zewnętrznej pętli, pętla wewnętrzna wykonuje się 5 razy

for x in range(1,6):
    line = str(x)
    for y in range(1,6):
        line += ('\t%3d' % (x*y)) #dodanie tabulacji i trzech znaków-wyrównanie do prawej
    print(line)

print('\nver_2\n')

for x in range(1,6):
    line = str(x)
    for y in range(1,6):
        line += (f'\t{x*y:>3}') # wykorzystanie f-stringa 
    print(line)

print('\n*** LAB ***')
print('\nTask 1\n')

i = 10
result = 1

for x in range (1,i+1):
    result *= x

print(f'{i}! = {result}')

print('\nTask 2\n')

x = 10

for i in range (1,x+1):
    result=1

    for j in range (1,i+1):
        result *= j

    print(f'{i}! = {result}')

print('\nTask 3\n')

list_noun = ['dog','potato','meal','icecream','car']
list_adj = ['dirty','big','hot','colorful','fast']

for noun in list_noun:

    for adj in list_adj:
        print(f'{adj} {noun}')

    print('---')