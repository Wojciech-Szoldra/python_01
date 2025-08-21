#Funkcja z parametrami
def give_working_day(year, month, day):
    from datetime import date
    from datetime import timedelta

    day = date(year,month,day)

    if day.weekday() == 5:
        workingday = day + timedelta(days=2)
    elif day.weekday() == 6:
        workingday = day + timedelta(days=1)
    else:
        workingday = day

    print(f'working day for {day} is {workingday}')
    return

#Przekazanie parametrów przez pozycję
give_working_day(2017,9,30)

#Przekazanie parametrów przez nazwę - nie muszą być po kolei
give_working_day(day=6,month=9,year=2020)

print('====LAB====\n')

print('====ZAD 1====\n')

def print_animal(animal):

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
    elif animal == 'bear':
        print(txt_bear)
    elif animal == 'bat':
        print(txt_bat)
    else:
        print(f'Cannot print \'{animal}\'')

print_animal('cat')

print('====ZAD 2====\n')

def how_many_days_left(year,month,day):
    from datetime import date
    today = date(year,month,day)
    current_year = today.year
    last_day = date(current_year,12,31)
    days_number = last_day - today
    print(f'{days_number.days} days left to the end of the year')
    return

how_many_days_left(2028,9,1)
how_many_days_left(day=8,year=2025,month=9)