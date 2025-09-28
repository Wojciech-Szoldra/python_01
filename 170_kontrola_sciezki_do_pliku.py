import os

# W poniższym kodzie użytkownik wprowadza ścieżkę do pliku.
# Jeżeli plik istniej pętla zostaje przerwana i wyświetlana jest informacja.
'''while True:
    
    file_name = input('Enter path to results file: ')

    if os.path.isfile(file_name):
        break
    else:
        print('Path is incorrect')

print(f'The results file is {file_name}')'''


print('====LAB====\n')

print('====ZAD 1====\n')

import os
import datetime

data_input_catalog = r'D:\IT\Programowanie\testy\folder do zadan z os\pliki\temp\data_input'
data_output_catalog = r'D:\IT\Programowanie\testy\folder do zadan z os\pliki\temp\data_output'

today = datetime.date.today()
today_str = today.strftime('%Y-%m-%d')

today_output_catalog = os.path.join(data_output_catalog, today_str)

is_input_catalog_ok = os.path.isdir(data_input_catalog)
is_output_catalog_ok = os.path.isdir(data_output_catalog)
is_today_output_ok = os.path.exists(today_output_catalog)


match is_input_catalog_ok, is_output_catalog_ok, is_today_output_ok:
    case True, True, False:
        print('Conditions met! We can countinue!')
    case False, _, _:
        print('Input catalog doesn\'t exist')
    case True, False, _:
        print('Output catalog doesn\'t exist')
    case True, True, True:
        print('Today output catalog olready exist')