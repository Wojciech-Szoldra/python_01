import os

# W poniższym kodzie użytkownik wprowadza ścieżkę do pliku.
# Jeżeli plik istniej pętla zostaje przerwana i wyświetlana jest informacja.

while True:
    
    file_name = input('Enter path to results file: ')

    if os.path.isfile(file_name):
        break
    else:
        print('Path is incorrect')

print(f'The results file is {file_name}')