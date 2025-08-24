#Funkcja przyjmująca dwa argumenty
def do_action(action, parameter):
	print(f'action: {action}')
	print(f'parameter: {parameter}')
	return

do_action('buy','shoes')

print('\n') 

#Funkcja z krotką (tuple)
def do_action2(action, *parameter):
	print(f'action: {action}')
	print(f'parameter: {parameter}')
	for element in parameter:
		print(f'element is {parameter}')
	return

do_action2('buy','shoes','socks','t-shirt')

print('\n') 

#Funkcja ze słownikiem (dictionary)
def do_action3(action, what, **parameter):
	print(f'action: {action}')
	print(f'what: {what}')
	print(f'parameter: {parameter}')
	for element in parameter:
		print(f'{element} = {parameter[element]}')
	return

do_action3('buy','shoes',size=45,color='brown',type='sport')

print('====LAB====\n')

print('====ZAD 1====\n')

#Tuple
def print_animal(*animal):

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
    
    for i in animal:
        if i == 'cat':
             print(txt_cat)
        elif i == 'bear':
             print(txt_bear)
        elif i == 'bat':
            print(txt_bat)
        else:
            print(f'Cannot print \'{i}\' - choose correct value: cat, bear, bar')
    return

print_animal('cat','bear','dog','bat','cow')

print('====ZAD 2====\n')

from datetime import date 

def how_many_days_left(*date_p1):
      
    for date_today in date_p1:
        last_day = date(date_today.year,12,31)
        days_number = last_day - date_today
        print(days_number.days)
    return

how_many_days_left(date.today(),date(2025,9,8))
