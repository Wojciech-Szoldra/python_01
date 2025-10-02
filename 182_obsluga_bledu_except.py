# try...except -> obsługa błędów w zależności od typu
# as e -> dodatkowe informacje o błędzie, które można wykorzystać 
import sys

task_per_person = 0

try:
    tasks = 32
    people_str = input('How many people are in the team? ')
    people = int(people_str)

    task_per_person = tasks / people

except ValueError as e:
    print(f'Sorry - you need to enter an integer number / {e}')

except ZeroDivisionError as e:
    print(f'Sorry - you need to enter value > 0 / {e}')

except:
    print(f'Something went wrong: {sys.exc_info() [0]}')

print(f'Every person should have around {task_per_person} tasks')

print('====LAB====\n')

print('====ZAD 1====\n')

import sys

file_path = r'D:\IT\Programowanie\testy\txt\orders.csv'

try: 
    with open(file_path,"r") as file:
    
        for line in file:
    
            line = line.replace('\n','')
            order = line.split(',')
    
            pharmacy_name = order[0]
            item = order[1]
            amount = int(order[2])

            print(f'Order form drugstore {pharmacy_name}, item: {item}, amount: {amount}')

except ValueError as e:
    print(f'Problem with converting data to integer in line: {line}')

except IndexError as e:
    print(f'To many data in line: {line}')

except:
    print(f'Problem with line: {line} \n {sys.exc_info() [0]}')

 
print("Processing finished")