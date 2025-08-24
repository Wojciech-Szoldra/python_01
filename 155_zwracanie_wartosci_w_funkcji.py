#Zwracanie wartości z funkcji (return)
from datetime import date
from datetime import timedelta

def give_working_day(year=date.today().year, 
                     month=date.today().month, 
                     day=date.today().day):

    day = date(year,month,day)

    if day.weekday() == 5:
        workingday = day + timedelta(days=2)
    elif day.weekday() == 6:
        workingday = day + timedelta(days=1)
    else:
        workingday = day

    return workingday

#Przypisanie zwróconej wartości do zmiennej
next_work = give_working_day()
print(next_work)

#Wyświetlenie zwróconej wartości bezpośrednio w print()
print(give_working_day())

print('====LAB====\n')

print('====ZAD 1====\n')

def print_animal(animal=''):

    txt_cat ='''
    |\---/|
    | o_o |
     \_^_/
    '''
    txt_bear ='''
    /  \.-"""-./  \\
    \    -   -    /
    |   o   o   |
    \  .-'"'-.  /
     '-\__Y__/-'
        `---`
    '''
    txt_bat ='''
      /\                 /\\
     /  '._   (\_/)   _.'  \\
    /_.''._'--('.')--'_.''._\\
    | \_ / `;=/ " \=;` \ _/ |
     \/ `\__|`\___/`|__/` \/
             \(/|\)/  
    '''
    
    if animal == 'cat':
        print(txt_cat)
        return True
    elif animal == 'bear':
        print(txt_bear)
        return True
    elif animal == 'bat':
        print(txt_bat)
        return True
    else:
        print(f'Cannot print \'{animal}\'\nChoose correct value: cat, bear, bar')
        return False
    
variable_t_f = print_animal('')
print(variable_t_f)

print('====ZAD 2====\n')

from datetime import date

def how_many_days_left(year=date.today().year,
                       month=date.today().month,
                       day=date.today().day):
    
    today = date(year,month,day)
    current_year = today.year
    last_day = date(current_year,12,31)
    days_number = last_day - today
    return days_number.days

print(how_many_days_left())