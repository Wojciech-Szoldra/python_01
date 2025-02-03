cargo = [40,20,4,5,30,8,2,7,3,19,32,40,20,35,15,32,9]
cargo.sort()
cargo.reverse()

print('The cargo list is:', cargo)

box_capacity = 90
box = []
i = 0

while i < len(cargo) and (box_capacity - sum(box)) >= min(cargo):
    if (box_capacity - sum(box)) >= cargo[i]:
        box.append(cargo[i])
    i+=1

# Testy

def suma(a, b):
    wynik = a + b
    return wynik

x = 10
y = 20

rezultat = suma(x, y)
print(f'x + y = {rezultat}')

# *** Debuggowanie skryptu - LAB ***

print('\n*** LAB ***')
print('\nTask 1\n')

number = 1
previus_number = 0
 
while number<50:
    print(number + previus_number)
    previus_number=number
    number+=1

print('\nTask 2\n')

text = ''
number = 10
condition = True
 
while condition:
 
    text+='x'
    print(text)
    
    if len(text)>number:
        condition=False

print(len(text))