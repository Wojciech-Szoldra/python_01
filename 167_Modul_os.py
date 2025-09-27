import os
import time

# Zwraca informację o katalogu bieżącym
print(f'Current directory is: {os.getcwd()}')

# Tworzymy nową ścieżkę łącząc katalog bieżący z nazwą pliku
current_dir = os.getcwd()
filename = 'results.txt'
fullpath = os.path.join(current_dir,filename)
print(fullpath)

# Przekazujemy ścieżkę względną otrzymujemy bezwzględną
relative_path = 'python_lab.py'
print(f'The absolute path is: {os.path.abspath(relative_path)}')

# Wyodrębniamy nazwę pliku i samą ścieżkę
file_path = r'D:\IT\Programowanie\python_01\python_lab.py' # r niweluje działanie znaków specjalnych
print(f'The file name part is: {os.path.basename(file_path)}')
print(f'The file name part is: {os.path.dirname(file_path)}')

# Uzyskujemy różne informacje o pliku
if os.path.exists(file_path):
    print(f'Modify date: {os.path.getmtime(file_path)}')
    print(f'Modify date: {time.localtime(os.path.getmtime(file_path))}')
    print(f'Creation date: {time.localtime(os.path.getctime(file_path))}')
    print(f'Last access: {time.localtime(os.path.getatime(file_path))}')
    print(f'Two parts - head and tail: {os.path.split(file_path)}')
    print(f'Only tail: {os.path.split(file_path) [1]}')
    print(f'Tuple: {os.path.splitdrive(file_path)}')
    print(f'First element - dirve letter: {os.path.splitdrive(file_path) [0]}')