# --Odczyt i kontroli danych wprowadzonych przez użytkownika-- #

# W tym przykładzie string (5) pomnożony zostanie przez liczbę
#file_size = input('Enter the max file size (MB): ')
#print(f'The max size in KB is {file_size * 1024}')

# Zmienna została przekonwertowana dzięki czemu możemy wykonywać obliczenia
#file_size_str = input('Enter the max file size (MB): ')
#file_size_int = int(file_size_str)
#print(f'The max size in KB is {file_size_int * 1024}')

# Pętla uniemożliwa wprowadzenie wartości innej niż liczbowa
'''while True:
    file_size_str = input('Enter the max file size (MB): ')

    if file_size_str.isdecimal():
        file_size_int = int(file_size_str)
        break'''


#print(f'The max size is {file_size_int}')
#print(f'The max size in KB is {file_size_int * 1024}')

print('====LAB====\n')

print('====ZAD 1====\n')

import math

def equation():
        
    def check_int(s):
        if s[0] in ('-', '+'):
            return s[1:].isdigit()
        return s.isdigit()

    a_str = input('Enter value \'a\':')
    b_str = input('Enter value \'b\':')
    c_str = input('Enter value \'c\':')

    if not check_int(a_str) or not check_int(b_str) or not check_int(c_str):
        print('The value must be an integer')
    else:
        a = int(a_str)
        b = int(b_str)
        c = int(c_str)
    
    if a == 0:
        print('This is no quadratic equation')
    else:
        delta = math.pow(b,2) - (4*a*c)

    if delta < 0:
        print('No solution')
    elif delta == 0:
        x1 = (-b-math.sqrt(delta)) / (2*a)
        print(f'X1 = {x1}')
    elif delta > 0:
        x1 = (-b-math.sqrt(delta)) / (2*a)
        x2 = (-b+math.sqrt(delta)) / (2*a)
        print(f'X1 = {x1}\nX2 = {x2}')

equation()