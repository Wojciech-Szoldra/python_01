print('---1---')

num1 = 2
print(type(num1))
str_num = str(num1)
print(type(str_num))

print('---2---')

def multiplication():
    number_1 = input('Enter first number: ')
    number_2 = input('Enter second number: ')
    result = int(number_1) * int(number_2)
    return print(f'Result: {result}')

multiplication()
