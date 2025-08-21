#Funkcja z domyślnymi parametrami
def give_working_day(year, month=1, day=1):
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

#Parametr day przyjmie wartość domyślną
give_working_day(2017,9)

#Parametr month oraz day przyjmą wartość domyślną wartość domyślną
give_working_day(2017)

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
    elif animal == 'bear':
        print(txt_bear)
    elif animal == 'bat':
        print(txt_bat)
    else:
        print(f'Cannot print \'{animal}\'\nChoose correct value: cat, bear, bar')

print_animal()

print('====ZAD 2====\n')

#Import następuje przed funkcją ponieważ operacje na dacie wykonujemy przed samą definicją czyli 'w sygnaturze funkcji'
from datetime import date

#To co znajduje się wewnątrz funkcji określamy jako 'ciało funkcji'
def how_many_days_left(year=date.today().year,
                       month=date.today().month,
                       day=date.today().day):
    
    today = date(year,month,day)
    current_year = today.year
    last_day = date(current_year,12,31)
    days_number = last_day - today
    print(f'{days_number.days} days left to the end of the year')
    return

how_many_days_left()
how_many_days_left(2025,8)
how_many_days_left(2025,10)
how_many_days_left(day=25)